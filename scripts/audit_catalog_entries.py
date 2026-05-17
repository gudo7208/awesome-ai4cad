#!/usr/bin/env python3
"""Audit every README catalog entry against external metadata where available."""

from __future__ import annotations

import argparse
import concurrent.futures
import csv
import difflib
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DEFAULT_OUTPUT_DIR = ROOT / "research" / "catalog_audit"
ENTRY_RE = re.compile(
    r"^- \*\*(?P<title>.+?)\*\* - (?P<authors>.+?)\. "
    r"\*(?P<venue>.+?)\*\.(?P<rest>.*)$"
)
DESCRIBED_ENTRY_RE = re.compile(
    r"^- \*\*(?P<title>.+?)\*\* — (?P<description>.+?)\. "
    r"\*(?P<citation>.+?)\*\.(?P<rest>.*)$"
)
PAPER_URL_RE = re.compile(r"\[\[Paper\]\((?P<url>[^)]+)\)\]")
ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(?P<id>[^)\]\s?#]+)")
DOI_RE = re.compile(r"doi\.org/(?P<doi>10\.\d{4,9}/[^)\]\s]+)", re.IGNORECASE)
YEAR_RE = re.compile(r"\b(19|20)\d{2}\b")
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}
USER_AGENT = "AwesomeAI4CAD-catalog-audit/0.1 (metadata verification)"


@dataclass
class Entry:
    index: int
    line: int
    section: str
    subsection: str
    title: str
    description: str
    authors: str
    venue: str
    url: str
    arxiv_id: str


def normalize_text(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii")
    value = value.lower()
    value = value.replace("&", " and ")
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def compact(value: str) -> str:
    return normalize_text(value).replace(" ", "")


def parse_year(value: str) -> int | None:
    years = [int(match.group(0)) for match in YEAR_RE.finditer(value)]
    return years[-1] if years else None


def first_author_last_name(authors: str) -> str:
    value = authors.strip()
    if not value or value.lower() in {"unknown", "n/a", "various", "authors"}:
        return ""
    value = re.sub(r"\bet al\.?$", "", value, flags=re.IGNORECASE).strip()
    first = re.split(r"\s+and\s+|,", value)[0].strip()
    parts = first.split()
    return normalize_text(parts[-1]) if parts else ""


def extract_arxiv_id(url: str) -> str:
    match = ARXIV_RE.search(url)
    if not match:
        return ""
    arxiv_id = match.group("id").removesuffix(".pdf")
    return re.sub(r"v\d+$", "", arxiv_id)


def extract_doi(url: str) -> str:
    match = DOI_RE.search(url)
    if not match:
        return ""
    return urllib.parse.unquote(match.group("doi")).rstrip(".")


def fetch_openalex_doi(doi: str, timeout: float) -> dict:
    api_url = f"https://api.openalex.org/works/{urllib.parse.quote('https://doi.org/' + doi, safe=':/')}"
    request = urllib.request.Request(
        api_url,
        headers={"User-Agent": USER_AGENT + " mailto:guan123m@qq.com"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        data = json.load(response)

    authors = [
        authorship.get("author", {}).get("display_name", "")
        for authorship in data.get("authorships", [])
    ]
    return {
        "source": "openalex",
        "source_status": "found",
        "source_title": data.get("display_name") or "",
        "source_year": data.get("publication_year"),
        "source_authors": [author for author in authors if author],
        "source_url": data.get("id") or "",
    }


def split_described_citation(citation: str) -> tuple[str, str]:
    year_matches = list(YEAR_RE.finditer(citation))
    if not year_matches:
        return "Unknown", citation.strip()

    last_year = year_matches[-1]
    comma = citation.rfind(",", 0, last_year.start())
    if comma == -1:
        return "Unknown", citation.strip()

    authors = citation[:comma].strip()
    venue = citation[comma + 1 :].strip()
    return authors or "Unknown", venue


def is_transient_url_error(exc: Exception) -> bool:
    text = str(exc).lower()
    return any(
        needle in text
        for needle in (
            "timed out",
            "unexpected_eof",
            "connection reset",
            "connection aborted",
            "bad gateway",
            "service unavailable",
        )
    )


def parse_entries() -> list[Entry]:
    entries: list[Entry] = []
    section = ""
    subsection = ""
    for line_no, line in enumerate(README.read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("## "):
            section = line[3:].strip()
            subsection = ""
        elif line.startswith("### "):
            subsection = line[4:].strip()

        match = ENTRY_RE.match(line)
        description = ""
        if match:
            authors = match.group("authors").strip()
            venue = match.group("venue").strip()
            rest = match.group("rest")
        else:
            match = DESCRIBED_ENTRY_RE.match(line)
            if not match:
                continue
            description = match.group("description").strip()
            authors, venue = split_described_citation(match.group("citation").strip())
            rest = match.group("rest")

        if not match:
            continue

        url_match = PAPER_URL_RE.search(rest)
        url = url_match.group("url").strip() if url_match else ""
        entries.append(
            Entry(
                index=len(entries) + 1,
                line=line_no,
                section=section,
                subsection=subsection,
                title=match.group("title").strip(),
                description=description,
                authors=authors,
                venue=venue,
                url=url,
                arxiv_id=extract_arxiv_id(url),
            )
        )
    return entries


def fetch_url(url: str, timeout: float) -> dict:
    if not url:
        return {"url_status": "missing_url"}
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return {"url_status": "error", "url_error": f"invalid_url: {url}"}
    doi = extract_doi(url)
    if doi:
        try:
            return {
                "url_status": "ok",
                "url_kind": "doi",
                "doi": doi,
                **fetch_openalex_doi(doi, timeout),
            }
        except Exception as exc:
            return {
                "url_status": "ok",
                "url_kind": "doi",
                "doi": doi,
                "source_status": "metadata_error",
                "source_error": str(exc),
            }
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return {"url_status": "ok", "http_status": response.status}
    except urllib.error.HTTPError as exc:
        if exc.code in {403, 405}:
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            try:
                with urllib.request.urlopen(request, timeout=timeout) as response:
                    return {"url_status": "ok", "http_status": response.status}
            except Exception as inner:
                if exc.code == 403 or is_transient_url_error(inner):
                    return {
                        "url_status": "blocked",
                        "http_status": getattr(inner, "code", exc.code),
                        "url_error": str(inner),
                    }
                return {
                    "url_status": "error",
                    "http_status": getattr(inner, "code", None),
                    "url_error": str(inner),
                }
        if exc.code in {403, 429, 500, 502, 503, 504}:
            return {"url_status": "blocked", "http_status": exc.code, "url_error": str(exc)}
        return {"url_status": "error", "http_status": exc.code, "url_error": str(exc)}
    except Exception as exc:
        if is_transient_url_error(exc):
            return {"url_status": "blocked", "url_error": str(exc)}
        return {"url_status": "error", "url_error": str(exc)}


def fetch_arxiv_batch(ids: list[str], timeout: float) -> dict[str, dict]:
    if not ids:
        return {}
    query = urllib.parse.urlencode({"id_list": ",".join(ids), "max_results": len(ids)})
    url = f"https://export.arxiv.org/api/query?{query}"
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = response.read()

    root = ET.fromstring(body)
    out: dict[str, dict] = {}
    for item in root.findall("atom:entry", ATOM_NS):
        id_text = item.findtext("atom:id", default="", namespaces=ATOM_NS)
        arxiv_id = extract_arxiv_id(id_text)
        title = " ".join(item.findtext("atom:title", default="", namespaces=ATOM_NS).split())
        published = item.findtext("atom:published", default="", namespaces=ATOM_NS)
        authors = [
            node.findtext("atom:name", default="", namespaces=ATOM_NS)
            for node in item.findall("atom:author", ATOM_NS)
        ]
        out[arxiv_id] = {
            "source": "arxiv",
            "source_title": title,
            "source_year": int(published[:4]) if published[:4].isdigit() else None,
            "source_authors": [author for author in authors if author],
            "source_url": id_text,
        }
    return out


def fetch_arxiv_metadata(
    ids: list[str],
    batch_size: int,
    timeout: float,
    sleep_seconds: float,
) -> tuple[dict[str, dict], dict[str, str]]:
    metadata: dict[str, dict] = {}
    errors: dict[str, str] = {}
    for start in range(0, len(ids), batch_size):
        batch = ids[start : start + batch_size]
        try:
            metadata.update(fetch_arxiv_batch(batch, timeout))
        except Exception as exc:
            for arxiv_id in batch:
                errors[arxiv_id] = str(exc)
        if start + batch_size < len(ids):
            time.sleep(sleep_seconds)
    return metadata, errors


def load_manual_verifications(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    records = json.loads(path.read_text(encoding="utf-8"))
    return {record["url"]: record for record in records}


def title_match(readme_title: str, source_title: str) -> str:
    if not source_title:
        return "not_checked"
    a = compact(readme_title)
    b = compact(source_title)
    if a == b:
        return "exact"
    if a and b and (a in b or b in a):
        return "contains"
    ratio = difflib.SequenceMatcher(None, a, b).ratio()
    if ratio >= 0.92:
        return "close"
    return "mismatch"


def author_match(readme_authors: str, source_authors: list[str]) -> str:
    readme_last = first_author_last_name(readme_authors)
    if not readme_last:
        return "readme_unknown"
    if not source_authors:
        return "not_checked"
    source_last = first_author_last_name(source_authors[0])
    return "match" if readme_last == source_last else "mismatch"


def classify(record: dict) -> tuple[str, list[str]]:
    reasons: list[str] = []

    if record["url_status"] == "missing_url":
        reasons.append("missing_paper_url")
    elif record["url_status"] == "blocked":
        reasons.append("paper_url_check_blocked_or_transient")
    elif record["url_status"] == "error":
        reasons.append("paper_url_error")

    if record.get("source_status") == "manual_verified" and record["url_status"] in {
        "ok",
        "blocked",
    }:
        return "high", []

    if record["arxiv_id"]:
        if record.get("source_status") != "found":
            reasons.append("arxiv_metadata_missing")
        if record.get("title_match") == "mismatch":
            reasons.append("title_mismatch")
        if record.get("author_match") in {"mismatch", "readme_unknown"}:
            reasons.append(f"author_{record.get('author_match')}")
        if record.get("year_match") == "mismatch":
            reasons.append("year_mismatch")

        blocking = {"arxiv_metadata_missing", "title_mismatch", "year_mismatch"}
        if any(reason in blocking for reason in reasons):
            return "low", reasons
        if reasons:
            return "medium", reasons
        return "high", reasons

    if record["url_status"] == "blocked":
        return "medium", reasons

    if record["url_status"] == "ok":
        if record.get("source_status") == "found":
            if record.get("title_match") == "mismatch":
                reasons.append("title_mismatch")
            if record.get("author_match") in {"mismatch", "readme_unknown"}:
                reasons.append(f"author_{record.get('author_match')}")
            if "title_mismatch" in reasons:
                return "low", reasons
            if reasons:
                return "medium", reasons
            return "high", reasons
        return "medium", reasons or ["non_arxiv_url_metadata_not_checked"]

    return "low", reasons


def audit_entries(args: argparse.Namespace) -> list[dict]:
    entries = parse_entries()
    manual_verifications = load_manual_verifications(args.manual_verifications)
    duplicate_arxiv_ids = {
        arxiv_id
        for arxiv_id, count in Counter(e.arxiv_id for e in entries if e.arxiv_id).items()
        if count > 1
    }

    arxiv_ids = sorted({entry.arxiv_id for entry in entries if entry.arxiv_id})
    arxiv_metadata: dict[str, dict] = {}
    arxiv_errors: dict[str, str] = {}
    if not args.skip_network:
        arxiv_metadata, arxiv_errors = fetch_arxiv_metadata(
            arxiv_ids,
            batch_size=args.arxiv_batch_size,
            timeout=args.timeout,
            sleep_seconds=args.arxiv_sleep,
        )

    url_results: dict[int, dict] = {}
    if args.skip_network:
        for entry in entries:
            url_results[entry.index] = {"url_status": "not_checked"}
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.url_workers) as pool:
            future_map = {
                pool.submit(fetch_url, entry.url, args.timeout): entry.index
                for entry in entries
                if not entry.arxiv_id
            }
            for future in concurrent.futures.as_completed(future_map):
                url_results[future_map[future]] = future.result()

    records: list[dict] = []
    for entry in entries:
        record = asdict(entry)
        venue_year = parse_year(entry.venue)
        record["venue_year"] = venue_year
        record["duplicate_arxiv_id"] = entry.arxiv_id in duplicate_arxiv_ids

        if entry.arxiv_id:
            record["url_status"] = "ok" if entry.arxiv_id in arxiv_metadata else "not_checked"
            source = arxiv_metadata.get(entry.arxiv_id, {})
            record.update(source)
            record["source_status"] = "found" if source else "missing"
            if entry.arxiv_id in arxiv_errors:
                record["source_error"] = arxiv_errors[entry.arxiv_id]
            record["title_match"] = title_match(entry.title, source.get("source_title", ""))
            record["author_match"] = author_match(entry.authors, source.get("source_authors", []))
            source_year = source.get("source_year")
            if source_year is None or venue_year is None:
                record["year_match"] = "not_checked"
            elif "arxiv" not in entry.venue.lower() and "preprint" not in entry.venue.lower():
                # arXiv publication year often predates conference/journal year.
                record["year_match"] = "not_applicable_non_arxiv_venue"
            else:
                record["year_match"] = "match" if source_year == venue_year else "mismatch"
        else:
            record.update(url_results.get(entry.index, {"url_status": "missing_url"}))
            manual = manual_verifications.get(entry.url)
            if manual:
                record["source"] = "manual"
                record["source_status"] = "manual_verified"
                record["source_title"] = manual.get("title", "")
                record["manual_evidence"] = manual.get("evidence", "")

            if record.get("source_status") == "manual_verified":
                record["title_match"] = "manual_verified"
                record["author_match"] = "manual_verified"
                record["year_match"] = "manual_verified"
            elif record.get("source_status") == "found":
                record["title_match"] = title_match(entry.title, record.get("source_title", ""))
                record["author_match"] = author_match(entry.authors, record.get("source_authors", []))
                source_year = record.get("source_year")
                if source_year is None or venue_year is None:
                    record["year_match"] = "not_checked"
                else:
                    record["year_match"] = "match" if source_year == venue_year else "mismatch"
            else:
                record["source_status"] = record.get("source_status", "not_checked")
                record["title_match"] = "not_checked"
                record["author_match"] = "not_checked"
                record["year_match"] = "not_checked"

        confidence, reasons = classify(record)
        record["catalog_flags"] = []
        if record["duplicate_arxiv_id"]:
            record["catalog_flags"].append("duplicate_arxiv_id")
        record["confidence"] = confidence
        record["review_reasons"] = reasons
        records.append(record)
    return records


def write_jsonl(path: Path, records: list[dict]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
    tmp.replace(path)


def write_summary(path: Path, records: list[dict]) -> None:
    total = len(records)
    confidence_counts = Counter(record["confidence"] for record in records)
    reason_counts = Counter(
        reason for record in records for reason in record.get("review_reasons", [])
    )
    flag_counts = Counter(
        flag for record in records for flag in record.get("catalog_flags", [])
    )
    section_counts: dict[str, Counter[str]] = defaultdict(Counter)
    for record in records:
        section_counts[record["section"]][record["confidence"]] += 1

    lines = [
        "# Catalog Entry Verification Summary",
        "",
        f"Audit date: {date.today().isoformat()}",
        "",
        "## Scope",
        "",
        f"- README entries audited: {total}",
        "- External source: arXiv Atom API for arXiv-linked entries; HTTP status checks for non-arXiv paper links.",
        "- Confidence is metadata confidence, not a claim that the paper is technically correct.",
        "",
        "## Confidence Counts",
        "",
        "| Confidence | Count |",
        "|---|---:|",
    ]
    for name in ("high", "medium", "low"):
        lines.append(f"| {name} | {confidence_counts[name]} |")

    lines.extend(["", "## Top Review Reasons", "", "| Reason | Count |", "|---|---:|"])
    if reason_counts:
        for reason, count in reason_counts.most_common(20):
            lines.append(f"| {reason} | {count} |")
    else:
        lines.append("| None | 0 |")

    lines.extend(["", "## Catalog Flags", "", "| Flag | Count |", "|---|---:|"])
    if flag_counts:
        for flag, count in flag_counts.most_common(20):
            lines.append(f"| {flag} | {count} |")
    else:
        lines.append("| None | 0 |")

    lines.extend(["", "## Section Breakdown", "", "| Section | High | Medium | Low |", "|---|---:|---:|---:|"])
    for section, counts in sorted(section_counts.items()):
        lines.append(
            f"| {section} | {counts['high']} | {counts['medium']} | {counts['low']} |"
        )

    lines.extend(
        [
            "",
            "## Next Step",
            "",
            "Metadata confidence is fully cleared when `low=0` and `medium=0`. Review `catalog_flags` separately for curation issues such as deliberate cross-section duplicates.",
            "",
        ]
    )
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text("\n".join(lines), encoding="utf-8")
    tmp.replace(path)


def write_review_queue(path: Path, records: list[dict]) -> None:
    """Write every non-high-confidence row as a compact human-review queue."""
    tmp = path.with_suffix(path.suffix + ".tmp")
    rows = [
        record
        for record in records
        if record["confidence"] != "high"
    ]
    rows.sort(key=lambda record: (record["confidence"] != "low", record["line"]))

    with tmp.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(
            [
                "line",
                "confidence",
                "section",
                "subsection",
                "title",
                "authors",
                "venue",
                "url",
                "source_title",
                "source_authors",
                "source_year",
                "review_reasons",
                "catalog_flags",
            ]
        )
        for record in rows:
            writer.writerow(
                [
                    record["line"],
                    record["confidence"],
                    record["section"],
                    record["subsection"],
                    record["title"],
                    record["authors"],
                    record["venue"],
                    record["url"],
                    record.get("source_title", ""),
                    "; ".join(record.get("source_authors", [])),
                    record.get("source_year", ""),
                    "; ".join(record.get("review_reasons", [])),
                    "; ".join(record.get("catalog_flags", [])),
                ]
            )
    tmp.replace(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--skip-network", action="store_true")
    parser.add_argument("--timeout", type=float, default=20.0)
    parser.add_argument("--url-workers", type=int, default=8)
    parser.add_argument("--arxiv-batch-size", type=int, default=100)
    parser.add_argument("--arxiv-sleep", type=float, default=3.0)
    parser.add_argument("--manual-verifications", type=Path)
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    if args.manual_verifications is None:
        args.manual_verifications = (
            args.output_dir / f"manual_source_verifications_{date.today().isoformat()}.json"
        )
    records = audit_entries(args)
    jsonl_path = args.output_dir / f"catalog_entry_audit_{date.today().isoformat()}.jsonl"
    summary_path = args.output_dir / f"catalog_entry_audit_summary_{date.today().isoformat()}.md"
    queue_path = args.output_dir / f"catalog_entry_review_queue_{date.today().isoformat()}.tsv"
    write_jsonl(jsonl_path, records)
    write_summary(summary_path, records)
    write_review_queue(queue_path, records)

    counts = Counter(record["confidence"] for record in records)
    print(f"Wrote {jsonl_path.relative_to(ROOT)}")
    print(f"Wrote {summary_path.relative_to(ROOT)}")
    print(f"Wrote {queue_path.relative_to(ROOT)}")
    print(
        "Confidence: "
        + ", ".join(f"{name}={counts[name]}" for name in ("high", "medium", "low"))
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
