<!--
repo: awesome-ai4cad
scope: AI methods for Computer-Aided Design (2018-2026)
catalog_entries: 553
deduplicated_registry_records: 638
registry_records_2024_2026: 496
entry_format: "Markdown list item with title, authors, venue/year, and Paper URL"
validation: "python3 scripts/validate_catalog.py"
-->

# Awesome AI for CAD [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated catalog of papers, datasets, and resources on AI for Computer-Aided Design.

![Catalog](https://img.shields.io/badge/Catalog-553_entries-blue)
![Registry](https://img.shields.io/badge/Registry-638_unique_records-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Taxonomy

```text
AI for CAD
├── 2D CAD Intelligence
│   ├── Symbol Detection & Spotting
│   ├── Text & Annotation Extraction
│   ├── Drawing Understanding & Benchmarks
│   ├── Compliance Checking
│   ├── Floor Plan Generation & Analysis
│   ├── Vectorization & Digitization
│   ├── P&ID Diagram Intelligence
│   └── Electrical & Circuit Schematics
├── 3D CAD Generation
│   ├── Autoregressive Sequence Models
│   ├── Diffusion-Based Generation
│   ├── LLM/VLM-Based Generation
│   ├── B-Rep & CSG Generation
│   ├── Point Cloud / Image / Sketch to CAD
│   ├── CAD Editing & Assembly
│   └── Shape Programs & Procedural Generation
├── CAD Understanding
│   ├── B-Rep Representation Learning
│   ├── Multi-Modal CAD Representations
│   ├── Machining Feature Recognition
│   ├── Retrieval & Classification
│   └── Assembly Understanding
├── Simulation & Optimization
│   ├── Neural Operators & FEA Surrogates
│   ├── Computational Fluid Dynamics
│   ├── Physics-Informed Neural Networks
│   ├── Topology Optimization
│   └── AI-Driven Generative Design
└── Manufacturing-Aware Design
    ├── Design for Manufacturing
    ├── Design for Additive Manufacturing
    ├── Assembly Planning & Tolerance
    └── CAD/CAM Integration
```

## Contents

- [Surveys](#surveys)
- [Foundational CAD AI Papers](#foundational-cad-ai-papers)
- [CAD Representations and Foundations](#cad-representations-and-foundations)
- [2D CAD and Drawing Intelligence](#2d-cad-and-drawing-intelligence)
- [3D CAD Generation and Reconstruction](#3d-cad-generation-and-reconstruction)
- [CAD Understanding and Retrieval](#cad-understanding-and-retrieval)
- [Simulation and Design Optimization](#simulation-and-design-optimization)
- [Manufacturing-Aware Design](#manufacturing-aware-design)
- [Challenges and Future Directions](#challenges-and-future-directions)
- [Datasets and Benchmarks](#datasets-and-benchmarks)
- [Tools and Platforms](#tools-and-platforms)
- [Contributing](#contributing)
- [Catalog Metadata](#catalog-metadata)

---

## Surveys

Overview and survey papers covering AI for CAD and related 3D generation domains.

- **3D Shape Generation: A Survey** — Surveys methods and benchmarks for 3D shape generation across representations. *Zibo Zhao et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2506.22678)]
- **A Survey on Deep Learning in 3D CAD Reconstruction** — Reviews deep learning approaches for reconstructing 3D CAD models from various inputs. *Ding et al., Applied Sciences (MDPI) 2025*. [[Paper](https://doi.org/10.3390/app15126681)]
- **Advances in 3D Generation: A Survey** — Comprehensive survey of recent advances in 3D content generation techniques. *Xiaoyu Li et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2401.17807)]
- **Diffusion Models in 3D Vision: A Survey** — Surveys applications of diffusion models to 3D vision tasks. *Zhen Wang et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2410.04738)]
- **A Survey On Text-to-3D Contents Generation In The Wild** — Reviews text-to-3D generation methods for open-domain content creation. *Chenhan Jiang et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2405.09431)]
- **Applications of Artificial Intelligence in the AEC Industry: A Review** — Reviews AI applications in architecture, engineering, and construction workflows. *Zheng et al., Journal of Asian Architecture and Building Engineering 2024*. [[Paper](https://doi.org/10.1080/13467581.2024.2346257)]
- **LLM4CAD: Multi-Modal Large Language Models for 3D Computer-Aided Design Generation** — Proposes using multi-modal LLMs for generating 3D CAD models. *Various, ASME IDETC-CIE 2024*. [[Paper](https://doi.org/10.1115/detc2024-143740)]

---

## Foundational CAD AI Papers

Curated CAD-specific anchors that introduced reusable datasets, representations, or modeling paradigms later work repeatedly builds on. This section is intentionally selective; the longer category lists below remain chronological.

| Area | Anchor paper | Why it matters |
|---|---|---|
| CAD construction sequences | [DeepCAD](https://arxiv.org/abs/2105.09492) | Established sketch-and-extrude sequence generation as a core CAD generative modeling setup. |
| Programmatic CAD data | [Fusion 360 Gallery](https://arxiv.org/abs/2010.02392) | Provided human design sequences and an environment for programmatic CAD construction. |
| Large-scale B-rep data | [ABC](https://arxiv.org/abs/1812.06216) | Became a common source dataset for geometric deep learning on CAD/B-rep geometry. |
| Relational sketch geometry | [SketchGraphs](https://arxiv.org/abs/2007.08506) | Made constraint graphs and relational geometry a reusable learning target. |
| Neural CSG parsing | [CSGNet](https://arxiv.org/abs/1712.08290) | Early neural approach for constructive solid geometry program recovery. |
| B-rep representation learning | [BRepNet](https://arxiv.org/abs/2104.00706) | Established topological message passing over faces, edges, and coedges for solid models. |
| Surface-aware B-rep learning | [UV-Net](https://arxiv.org/abs/2006.10211) | Combined UV-sampled surface grids with graph structure for B-rep understanding. |
| Hierarchical CAD generation | [SkexGen](https://arxiv.org/abs/2207.04632) | Introduced disentangled codebooks for sketch and extrusion generation. |
| B-rep generation | [BrepGen](https://arxiv.org/abs/2401.15563) | Helped move CAD generation from command sequences toward structured B-rep geometry. |

<details>
<summary>Related general AI background references</summary>

- **Multi-Scale Latent Diffusion with Mamba+ for Complex Parametric Sequence** — Generates complex parametric CAD sequences using multi-scale latent diffusion combined with Mamba+ architecture. *Liyuan Deng, Yunpeng Bai, Yongkang Dai et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.17647)]
- **CAD-Coder: Text-to-CAD Generation with Chain-of-Thought and Geometric Reward** — Converts text descriptions to CAD models using chain-of-thought reasoning and geometric reward signals. *Yandong Guan, Xilin Wang, Ximing Xing et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.19713)]
- **An Open-Source Vision-Language Model for Computer-Aided Design Code Generation** — Proposes an open-source vision-language model that generates CAD code from visual inputs. *Anna C. Doris, Md Ferdous Alam, Amin Heyrani Nobari et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.14646)]
- **OpenECAD: An Efficient Visual Language Model for Editable 3D-CAD Design** — Presents an efficient visual language model for generating editable 3D CAD designs. *Zhe Yuan, Jianqi Shi, Yanhong Huang, arXiv 2024*. [[Paper](https://arxiv.org/abs/2406.09913)]
- **Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges** — Unifies geometric deep learning approaches through symmetry and invariance principles across domains. *Bronstein et al., arXiv / IEEE Signal Processing Magazine 2021*. [[Paper](https://arxiv.org/abs/2104.13478)]
- **Dynamic Graph CNN for Learning on Point Clouds** — Introduces EdgeConv module that dynamically computes graphs for learning on point clouds. *Wang et al., ACM TOG 2019*. [[Paper](https://arxiv.org/abs/1801.07829)]
- **PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation** — Proposes a unified architecture for directly consuming unordered point sets for 3D tasks. *Qi et al., CVPR 2017*. [[Paper](https://arxiv.org/abs/1612.00593)]
- **PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space** — Extends PointNet with hierarchical feature learning to capture local geometric structures. *Qi et al., NeurIPS 2017*. [[Paper](https://arxiv.org/abs/1706.02413)]

</details>

---

## CAD Representations and Foundations

Papers establishing core CAD representation paradigms (B-rep, CSG, sequence, code) that form the basis for generative and understanding methods.

**Representative anchors:** CSGNet for neural CSG parsing; BRepNet for topological message passing; SkexGen for disentangled CAD codebooks.

- **BRepFormer: AutoRegressive Generation with B-rep Holistic Token Sequence Representation** — Autoregressively generates B-rep CAD models using a holistic token sequence representation. *Xu et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.16771)]
- **Masked BRep Autoencoder via Hierarchical Graph Transformer** — Learns B-rep representations through masked autoencoding on hierarchical graph transformers. *Xu et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.14927)]
- **Iterative Program Editing for CAD Reverse Engineering** — Recovers CAD construction programs from shapes via iterative program editing. *Chen et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.29847)]
- **CAD-Coder: A New Paradigm for CAD Generation with Scalable Large Model Capabilities** — Generates CAD models by leveraging scalable large language model code generation. *Li et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.06507)]
- **Towards Text-based CAD Prototyping via Modality-Specific Tokenization** — Enables text-driven CAD prototyping using modality-specific tokenization of geometry. *Chen et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.21150)]
- **A Language Model-Driven Multi-Agent System for Collaborative Design** — Proposes a multi-agent system powered by language models for collaborative CAD design. *Makatura et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.04417)]
- **Generating Constructive Solid Geometry Instead of Meshes by Fine-Tuning a Code-Generation LLM** — Fine-tunes a code-generation LLM to output CSG representations instead of meshes. *Skalic et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2411.15279)]
- **HNC-CAD: Hierarchical Neural Coding for Controllable CAD Model Generation** — Introduces hierarchical neural coding for controllable generation of CAD models. *Xu et al., CVPR 2023*. [[Paper](https://arxiv.org/abs/2307.00149)]
- **D2CSG: Unsupervised Learning of Compact CSG Trees with Dual Complements and Dropouts** — Learns compact CSG tree representations from point clouds using dual complement operations and dropout regularization. *Kania et al., NeurIPS 2023*. [[Paper](https://arxiv.org/abs/2301.11497)]
- **Self-Supervised CAD Reconstruction by Learning Sketch-Extrude Operations** — Reconstructs CAD models from point clouds by learning sketch-and-extrude modeling sequences without supervision. *Ren et al., arXiv 2023*. [[Paper](https://arxiv.org/abs/2303.10613)]
- **SkexGen: Autoregressive Generation of CAD Construction Sequences with Disentangled Codebooks** — Autoregressively generates CAD sketch-extrude sequences using disentangled codebooks for topology and geometry. *Xu et al., ICML 2022*. [[Paper](https://arxiv.org/abs/2207.04632)]
- **BRepNet: A Topological Message Passing System for Solid Models** — Proposes message passing on B-Rep topology graphs for learning directly from CAD solid models. *Lambourne et al., CVPR 2021 (Oral)*. [[Paper](https://arxiv.org/abs/2104.00706)]
- **UV-Net: Learning from Boundary Representations** — Learns from B-Rep UV-domain surface parameterizations for CAD model understanding tasks. *Jayaraman et al., CVPR 2021*. [[Paper](https://arxiv.org/abs/2006.10211)]
- **UCSG-Net: Unsupervised Discovering of Constructive Solid Geometry Tree** — Discovers CSG tree structures from shapes in an unsupervised manner without ground-truth programs. *Kania et al., NeurIPS 2020*. [[Paper](https://arxiv.org/abs/2006.09102)]
- **CSGNet: Neural Shape Parser for Constructive Solid Geometry** — Parses 2D/3D shapes into CSG primitive programs using a neural network shape parser. *Sharma et al., CVPR 2018*. [[Paper](https://arxiv.org/abs/1712.08290)]
- **B-Rep Distance Functions (BR-DF): How to Represent a B-Rep Model by Volumetric Distance Functions?** — Represents B-rep CAD models with volumetric distance functions as a new geometric representation. *Zhang et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.14870)]

---

## 2D CAD and Drawing Intelligence

AI methods for interpreting, analyzing, and generating 2D engineering drawings, floor plans, P&ID diagrams, and circuit schematics.

**Representative anchors:** SymPoint for panoptic symbol spotting; FloorPlanCAD for drawing datasets; GAT-CADNet for graph-based symbol detection.

### Symbol Detection and Spotting

- **ArchCAD-400K** — Introduces a 400K-image large-scale CAD drawing dataset with a new baseline for panoptic symbol spotting. *Ruifeng Luo, Zhengjie Liu, Tianxiao Cheng et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.22346)]
- **Point or Line?** — Proposes line-based representation as an alternative to point-based methods for panoptic symbol spotting. *Xingguang Wei, Haomin Wang, Shenglong Ye et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.23395)]
- **Text-Enhanced Panoptic Symbol Spotting** — Integrates textual information to improve panoptic symbol spotting performance in CAD drawings. *Xianlin Liu, Yan Gong, Bohao Li et al., BESC 2025*. [[Paper](https://arxiv.org/abs/2510.11091)]
- **Relative Drawing Identification Complexity** — Shows that drawing identification difficulty remains consistent across modalities in vision-language models. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.10583)]
- **Architectural Practice Process and Artificial Intelligence** — Examines how AI reshapes evolving architectural design practice processes. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2507.23653)]
- **Symbol as Points** — Represents symbols as points for unified panoptic symbol spotting via point-based detection. *Wenlong Liu, Tianyu Yang, Yuhan Wang et al., ICLR 2024*. [[Paper](https://arxiv.org/abs/2401.10556)]
- **SymPoint Revolutionized** — Boosts panoptic symbol spotting accuracy by enhancing layer-wise feature representations in SymPoint. *Wenlong Liu, Tianyu Yang, Qizhi Yu et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2407.01928)]
- **CADSpotting** — Presents a robust panoptic symbol spotting method designed to scale to large-scale CAD drawings. *Fuyi Yang, Jiazuo Mu, Yanshun Zhang et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2412.07377)]
- **Generative AI in the Construction Industry: A State-of-the-art Analysis** — Surveys generative AI applications across construction tasks including design, planning, and documentation. *Ridwan Taiwo, Idris Temitope Bello, Sulemana Fatoama Abdulai et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2402.09939)]
- **Exploring Gen-AI applications in building research and industry: A review** — Reviews generative AI use cases in building design, energy modeling, and facility management. *Hanlong Wan, Jian Zhang, Yan Chen et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2410.01098)]
- **GAT-CADNet: Graph Attention Network for Panoptic Symbol Spotting in CAD Drawings** — Proposes a graph attention network for panoptic symbol spotting in CAD drawings. *Zhaohua Zheng, Jianfang Li, Lingjie Zhu et al., arXiv 2022*. [[Paper](https://arxiv.org/abs/2201.00625)]
- **Automatic Detection and Classification of Symbols in Engineering Drawings** — Detects and classifies symbols in engineering drawings using deep learning methods. *Sourish Sarkar, Pranav Pandey, Sibsambhu Kar, arXiv 2022*. [[Paper](https://arxiv.org/abs/2204.13277)]
- **Discovering Design Concepts for CAD Sketches** — Learns reusable design concepts from CAD sketch datasets via unsupervised discovery. *Yuezhi Yang, Hao Pan, NeurIPS 2022*. [[Paper](https://arxiv.org/abs/2210.14451)]
- **The Scope for AI-Augmented Interpretation of Building Blueprints in Commercial and Industrial Property Insurance** — Explores AI-driven blueprint interpretation to automate property insurance risk assessment. *Long Chen, Mao Ye, Alistair Milne et al., arXiv 2022*. [[Paper](https://arxiv.org/abs/2205.01671)]
- **An Automated Engineering Assistant** — Presents an automated system for recognizing and interpreting symbols in technical drawings. *Dries Van Daele, Nicholas Decleyre, Herman Dubois et al., arXiv 2019*. [[Paper](https://arxiv.org/abs/1909.08552)]

### Text and Annotation Extraction

- **Context-Aware Mapping of 2D Drawing Annotations to 3D CAD Features Using LLM-Assisted Reasoning for Manufacturing Automation** — Maps 2D drawing annotations to 3D CAD features using LLM-assisted reasoning for manufacturing workflows. *Muhammad Tayyab Khan, Lequn Chen, Wenhe Feng et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.18296)]
- **A Multi-Stage Hybrid Framework for Automated Interpretation of Multi-View Engineering Drawings Using Vision Language Model** — Proposes a multi-stage hybrid framework combining vision-language models to interpret multi-view engineering drawings. *Muhammad Tayyab Khan, Zane Yong, Lequn Chen et al., ICIEA 2026*. [[Paper](https://arxiv.org/abs/2510.21862)]
- **Automated Parsing of Engineering Drawings for Structured Information Extraction Using a Fine-tuned Document Understanding Transformer** — Fine-tunes a document understanding transformer to parse engineering drawings into structured information. *Muhammad Tayyab Khan, Zane Yong, Lequn Chen et al., IEEE IEEM 2025*. [[Paper](https://arxiv.org/abs/2505.01530)]
- **A Hybrid Vision-Language Framework for Parsing 2D Engineering Drawings into Structured Manufacturing Knowledge** — Parses 2D engineering drawings into structured manufacturing knowledge using a hybrid vision-language framework. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2506.17374)]
- **Fine-Tuning Vision-Language Model for Automated Engineering Drawing Information Extraction** — Fine-tunes a vision-language model to automate information extraction from engineering drawings. *Muhammad Tayyab Khan, Lequn Chen, Ye Han Ng et al., ICIAI 2025*. [[Paper](https://arxiv.org/abs/2411.03707)]

### Drawing Understanding and Benchmarks

- **AECV-Bench** — Benchmarks multimodal models on understanding architectural and engineering construction drawings. *Aleksei Kondratenko, Mussie Birhane, Houssame E. Hsain et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.04819)]
- **AEC-Bench** — Evaluates agentic AI systems on multimodal tasks in architecture, engineering, and construction. *Harsh Mankodiya, Chase Gallik, Theodoros Galanos et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.29199)]
- **Blueprint** — Multimodal retrieval system for complex engineering drawings and technical documents. *Authors, arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.13345)]
- **Advancing Multimodal LLM Evaluation of Engineering Documentation** — Enhances retrieval-augmented evaluation of multimodal LLMs on engineering documents. *Authors, arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.09552)]
- **Solving Idealized Beam Models from Hand-Drawn Drawings** — Extracts structural beam models automatically from hand-drawn engineering sketches. *Authors, arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.21432)]
- **Blueprint-Bench** — Compares spatial intelligence of LLMs, agents, and image models on blueprint tasks. *Lukas Petersson, Axel Backlund, Axel Wennstöm et al., Submitted to ICLR 2026*. [[Paper](https://arxiv.org/abs/2509.25229)]
- **AECBench** — Hierarchical benchmark for evaluating LLM knowledge in architecture, engineering, and construction. *Chen Liang, Zhaoqi Huang, Haofen Wang et al., Advanced Engineering Informatics 2025*. [[Paper](https://arxiv.org/abs/2509.18776)]
- **VectorGraphNET** — Uses graph attention networks for accurate segmentation of complex technical drawings. *Andrea Carrara, Stavros Nousias, André Borrmann, arXiv 2024*. [[Paper](https://arxiv.org/abs/2410.01336)]
- **DesignQA: A Multimodal Benchmark for Evaluating Large Language Models' Understanding of Engineering Documentation** — Introduces a multimodal benchmark to evaluate LLMs on engineering drawing comprehension tasks. *Anna C. Doris, Daniele Grandi, Ryan Tomich et al., ASME JCISE 2024*. [[Paper](https://arxiv.org/abs/2404.07917)]
- **Prediction of Visual Relations in Engineering Drawings** — Proposes methods to predict spatial and semantic relations between entities in engineering drawings. *Chao Gu, Ke Lin, Yiyang Luo et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2409.00909)]

### 2D-3D Annotation Mapping

- **CAD2Program: From 2D CAD Drawings to 3D Parametric Models** — Converts 2D CAD drawings into 3D parametric modeling programs via learned mappings. *Xilin Wang, Jia Zheng, Yuanchao Hu et al., AAAI 2025*. [[Paper](https://arxiv.org/abs/2412.11892)]

### Compliance Checking

- **Automated Facility Enumeration for Building Compliance Checking using Door Detection and Large Language Models** — Combines door detection with LLMs to automate facility enumeration for building code compliance. *Licheng Zhang, Bach Le, Naveed Akhtar et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.17283)]
- **Automatic Building Code Review** — Automates building code review processes using AI-driven analysis of architectural plans. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.02634)]
- **DRC-Coder: Automated DRC Checker Code Generation Using LLM Autonomous Agent** — Uses an LLM autonomous agent to automatically generate design rule checking code. *Chen-Chia Chang, Chia-Tung Ho, Yaguang Li et al., ISPD 2025*. [[Paper](https://arxiv.org/abs/2412.05311)]
- **ARCEAK: An Automated Rule Checking Framework Enhanced with Architectural Knowledge** — Proposes a rule checking framework that integrates architectural knowledge for compliance automation. *Junyong Chen, Ling-I Wu, Minyu Chen et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2501.14735)]
- **CODE-ACCORD: A Corpus of Building Regulatory Data for Rule Generation towards Automatic Compliance Checking** — Introduces a building regulatory corpus for generating machine-readable rules for compliance checking. *Hansi Hettiarachchi, Amna Dridi, Mohamed Medhat Gaber et al., Scientific Data 2024*. [[Paper](https://arxiv.org/abs/2403.02231)]

### Floor Plan and Drawing Generation

- **Unified Vector Floorplan Generation via Markup Representation** — Generates vector floor plans using a unified markup language representation. *Authors, arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.04859)]
- **A Two-Level Codebook Based Network for End-to-End Vector Floorplan Generation** — Uses a two-level codebook to encode and generate vector floor plans end-to-end. *Authors, arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.07100)]
- **HouseMind: Tokenization Allows Multimodal Large Language Models to Understand, Generate and Edit Architectural Floor Plans** — Enables multimodal LLMs to understand, generate, and edit floor plans via tokenization. *Sizhong Qin, Ramon Elias Weber, Xinzheng Lu, CVPR 2026*. [[Paper](https://arxiv.org/abs/2603.11640)]
- **Controllable End-to-End Vector Floor Plan Generation** — Proposes controllable end-to-end generation of vector floor plans with user constraints. *Authors, arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.20377)]
- **Text-to-Layout: A Generative Workflow for Drafting Architectural Floor Plans Using LLMs** — Drafts architectural floor plan layouts from natural language descriptions using LLMs. *Jayakrishna Duggempudi, Lu Gao, Ahmed Senouci et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.00543)]
- **Small Building Model: A Transformer for Layout Synthesis in BIM** — Applies a transformer architecture for automated layout synthesis in BIM environments. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.04832)]
- **DiffPlanner: Direct Vector Floor Plan Generation with Diffusion** — Generates vector floor plans directly using a diffusion-based generative model. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.13738)]
- **Computer-Aided Layout Generation for Building Design: A Survey** — Surveys computational methods for automated building layout generation. *Authors, Computational Visual Media 2025*. [[Paper](https://arxiv.org/abs/2504.09694)]
- **HypergraphFormer: Learning Hypergraphs from LLMs for Editable Floor Plan Generation** — Generates editable floor plans by learning hypergraph representations distilled from large language models. *Klimenko et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2605.18932)]
- **Generative Floor Plan Design with LLMs via Reinforcement Learning with Verifiable Rewards** — Controls room dimensions and connectivity in floor plan design using LLMs trained with verifiable-reward RL. *Lara et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2605.14117)]
- **What a Comfortable World: Ergonomic Principles Guided Apartment Layout Generation** — Generates apartment layouts guided by ergonomic principles to avoid inefficiencies learned from real data. *Nieciecki et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.08411)]
- **Space Syntax-guided Post-training for Residential Floor Plan Generation** — Post-trains floor plan generators with space-syntax guidance for better spatial configurational logic. *Jiang et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.22507)]
- **GFLAN: Generative Functional Layouts** — Generates functional floor plan layouts combining combinatorial search with geometric constraint satisfaction. *Abouagour et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.16275)]

### Vectorization and Digitization

- **FloorplanVLM: A Vision-Language Model for Floorplan Vectorization** — Uses a vision-language model to vectorize floorplan images into structured representations. *Authors, arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.06507)]
- **Drawing2CAD: Sequence-to-Sequence Learning for CAD Generation from Vectorized Drawings** — Proposes sequence-to-sequence learning to generate CAD models from vectorized engineering drawings. *Feiwei Qin, Shichao Lu, Junhao Hou et al., ACM MM 2025*. [[Paper](https://arxiv.org/abs/2508.18733)]
- **Line Drawing Pretraining for Efficient, Transferable, and Human-Aligned Vision** — Pretrains vision models on line drawings for efficient and human-aligned visual representations. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.06696)]
- **Enhancing Structured Reasoning for Vector Graphics Generation with Reinforcement Learning** — Applies reinforcement learning to improve structured reasoning in vector graphics generation. *Authors, CVPR 2026*. [[Paper](https://arxiv.org/abs/2505.24499)]
- **Rendering-Aware Reinforcement Learning for Vector Graphics Generation** — Introduces rendering-aware rewards in reinforcement learning for higher-quality vector graphics output. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.20793)]
- **Vector Graphic Animation via Neural Implicits and Video Diffusion Priors** — Animates vector graphics using neural implicit representations and video diffusion priors. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.07484)]
- **Advanced Knowledge Extraction of Physical Design Drawings, Translation and Conversion to CAD Formats using Deep Learning** — Extracts knowledge from physical design drawings and converts them to CAD formats via deep learning. *Jesher Joshua M, Ragav V, Syed Ibrahim S P, arXiv 2024*. [[Paper](https://arxiv.org/abs/2403.11291)]
- **Evaluating Large Language Models on Vector Graphics Understanding and Generation** — Benchmarks LLM capabilities on understanding and generating vector graphics. *Authors, arXiv 2024*. [[Paper](https://arxiv.org/abs/2407.10972)]
- **Tokenizing Strokes for Vector Graphic Synthesis** — Introduces a stroke tokenization method for generating vector graphics via sequence modeling. *Zecheng Tang, Chenfei Wu, Zekai Zhang et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2401.17093)]
- **A Comprehensive End-to-End Computer Vision Framework for Restoration and Recognition of Low-Quality Engineering Drawings** — Proposes an end-to-end framework to restore and recognize degraded engineering drawings. *Lvyang Yang, Jiankang Zhang, Huaiqiang Li et al., Engineering Applications of Artificial Intelligence 2023*. [[Paper](https://arxiv.org/abs/2312.13620)]
- **Component Segmentation of Engineering Drawings Using Graph Convolutional Networks** — Applies graph convolutional networks to segment components in engineering drawings. *Wentai Zhang, Joe Joseph, Yue Yin et al., Computers in Industry 2022*. [[Paper](https://arxiv.org/abs/2212.00290)]
- **Deep Vectorization of Technical Drawings** — Presents a deep learning approach to convert raster technical drawings into vector representations. *Egiazarian et al., ECCV 2020*. [[Paper](https://arxiv.org/abs/2003.05471)]

### P&ID Diagram Intelligence

- **GraphRAG for Engineering Diagrams** — Applies graph-based retrieval-augmented generation to query and reason over engineering diagram content. *Jan Marius Stürmer, Tobias Koch, arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.22528)]
- **A Closed-Loop, Physics-Aware Agentic Framework for Auto-Generating Chemical Process and Instrumentation Diagrams** — Proposes a physics-aware agentic framework that automatically generates chemical process and instrumentation diagrams. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.24584)]
- **From Engineering Diagrams to Graphs: Digitizing P&IDs with Transformers** — Uses transformer models to convert P&ID diagrams into structured graph representations. *Jan Marius Stürmer, Marius Graumann, Tobias Koch, IEEE DSAA 2025*. [[Paper](https://arxiv.org/abs/2411.13929)]
- **Talking like Piping and Instrumentation Diagrams (P&IDs)** — Introduces a natural language interface for interpreting and communicating P&ID diagram content. *Achmad Anggawirya Alimin, Dominik P. Goldstein, Lukas Schulze Balhorn et al., Systems and Control Transactions 2025*. [[Paper](https://arxiv.org/abs/2502.18928)]
- **Visual Language Model as a Judge for Object Detection in Industrial Diagrams** — Leverages vision-language models to evaluate object detection quality in industrial diagrams. *Sanjukta Ghosh, IEEE ICASSP 2026*. [[Paper](https://arxiv.org/abs/2510.03376)]
- **Advanced Integration of Discrete Line Segments in Digitized P&ID for Continuous Instrument Connectivity** — Integrates discrete line segments in digitized P&IDs to reconstruct continuous instrument connectivity paths. *Soumya Swarup Prusty, Astha Agarwal, Srinivasan Iyenger, arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.11976)]
- **Rule-Based Autocorrection of Piping and Instrumentation Diagrams (P&IDs) on Graphs** — Applies rule-based methods on graph representations to automatically correct errors in P&IDs. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2502.18493)]
- **Accelerating Manufacturing Scale-Up from Material Discovery Using Agentic Web Navigation and Retrieval-Augmented AI for Process Engineering Schematics Design** — Combines agentic web navigation with retrieval-augmented AI to accelerate process engineering schematic design. *Authors, arXiv 2024*. [[Paper](https://arxiv.org/abs/2412.05937)]
- **An Agentic Approach to Automatic Creation of P&ID Diagrams from Natural Language Descriptions** — Uses LLM agents to automatically generate P&ID diagrams from natural language input. *Shreeyash Gowaikar, Srinivasan Iyengar, Sameer Segal et al., AAAI 2025 Workshop AI2ASE*. [[Paper](https://arxiv.org/abs/2412.12898)]
- **Towards Automatic Generation of Piping and Instrumentation Diagrams (P&IDs) with Artificial Intelligence** — Explores AI methods for automatically generating P&ID diagrams from process descriptions. *Edwin Hirtreiter, Lukas Schulze Balhorn, Artur M. Schweidtmann, arXiv 2022*. [[Paper](https://arxiv.org/abs/2211.05583)]
- **Digitize-PID: Automatic Digitization of Piping and Instrumentation Diagrams** — Proposes a pipeline for automatically digitizing scanned P&ID sheets into structured formats. *Shubham Paliwal, Arushi Jain, Monika Sharma et al., PAKDD 2021*. [[Paper](https://arxiv.org/abs/2109.03794)]
- **OSSR-PID: One-Shot Symbol Recognition in P&ID Sheets using Path Sampling and GCN** — Performs one-shot symbol recognition in P&IDs using path sampling and graph convolutional networks. *Shubham Paliwal, Monika Sharma, Lovekesh Vig, IJCNN 2021*. [[Paper](https://arxiv.org/abs/2109.03849)]
- **SynthPID: P&ID Digitization from Topology-Preserving Synthetic Data** — Digitizes piping and instrumentation diagrams into process graphs using topology-preserving synthetic training data. *Prasad et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.16513)]

### Electrical and Circuit Schematics

- **SINA: A Circuit Schematic Image-to-Netlist Generator Using Artificial Intelligence** — Converts circuit schematic images to netlists using AI-based recognition and extraction. *Saoud Aldowaish, Yashwanth Karumanchi, Kai-Chen Chiang et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.22114)]
- **OmniSch: A Multimodal PCB Schematic Benchmark For Structured Diagram Visual Reasoning** — Introduces a multimodal benchmark for visual reasoning over PCB schematic diagrams. *Taiting Lu, Kaiyuan Lin, Yuxin Tian et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.00270)]
- **CircuitLM: A Multi-Agent LLM-Aided Design Framework for Generating Circuit Schematics from Natural Language Prompts** — Generates circuit schematics from natural language using a multi-agent LLM framework. *Authors, arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.04505)]
- **PCBSchemaGen: Constraint-Guided Schematic Design via LLM for Printed Circuit Boards** — Uses LLMs with constraint guidance to automatically generate PCB schematic designs. *Authors, arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.00510)]
- **Agentic Hardware Design Reviews** — Proposes LLM-based agents to automate hardware design review processes. *AllSpice Inc., arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.15672)]
- **Component Centric Placement Using Deep Reinforcement Learning for PCB Design** — Applies deep reinforcement learning for component placement optimization in PCB layout. *Authors, arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.23540)]
- **AMSnet 2.0: A Large AMS Database with AI Segmentation for Net Detection** — Provides a large analog/mixed-signal database with AI-driven segmentation for net detection. *Yichen Shi, Zhuofu Tao, Yuhao Gao et al., LAD 2025*. [[Paper](https://arxiv.org/abs/2505.09155)]
- **SkeySpot: Automating Service Key Detection for Digital Electrical Layout Plans in the Construction Industry** — Automates service key detection in digital electrical layout plans for construction. *Dhruv Dosi, Rohit Meena, Param Rajpura et al., IEEE SMC 2025*. [[Paper](https://arxiv.org/abs/2508.10449)]
- **AMSnet: A Netlist Dataset for AMS Circuits** — Introduces a large-scale netlist dataset for analog and mixed-signal circuit design automation. *Zhuofu Tao, Yichen Shi, Yiru Huo et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2405.09045)]
- **PCBDet** — Proposes an efficient edge-deployable deep neural network for automatic PCB component detection. *Brian Li, Steven Palayew, Francis Li et al., arXiv 2023*. [[Paper](https://arxiv.org/abs/2301.09268)]
- **Hand-Drawn Electrical Circuit Recognition** — Recognizes hand-drawn electrical circuit diagrams using object detection and node recognition. *Rachala Rohith Reddy, Mahesh Raveendranatha Panicker, arXiv 2021*. [[Paper](https://arxiv.org/abs/2106.11559)]
- **SchGen: PCB Schematic Generation with Semantic-Grounded Code Representations** — Generates PCB schematics from semantic-grounded code representations using generative AI. *Luo et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2605.30345)]

### Architectural Floor Plan Analysis

- **Raster2Seq: Polygon Sequence Generation for Floorplan Reconstruction** — Generates polygon sequences from raster floor plan images for vectorized reconstruction. *Authors, arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.09016)]
- **A Fully Automated Hybrid Learning Scan-to-BIM Pipeline with Integrated Topology Refinement** — Automates scan-to-BIM conversion using hybrid learning with topology-aware refinement. *Authors, arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.24311)]
- **MitUNet: Enhancing Floor Plan Recognition using a Hybrid Mix-Transformer and U-Net Architecture** — Combines Mix-Transformer and U-Net for improved floor plan element recognition. *Dmitriy Parashchuk, Alexey Kaspshitskiy, Yuriy Karyakin, arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.02413)]
- **SAM-Guided Floorplan Reconstruction with Semantic-Geometric Fusion** — Leverages Segment Anything Model with semantic-geometric fusion for floor plan reconstruction. *Hanfu Ye, Hanfu Wang, Yunchi Zhang et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.15750)]
- **A Multi-Agent Human-AI Collaborative Pipeline to Convert Hand-Drawn Floor Plans to 3D BIM** — Uses multi-agent collaboration to convert hand-drawn sketches into 3D BIM models. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.20838)]
- **Graph Similarity Learning of Floor Plans** — Learns graph-based representations to measure structural similarity between floor plans. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.03737)]
- **Cloud2BIM: Open-source Automatic Pipeline for Efficient Conversion of Large-scale Point Clouds to IFC Format** — Provides an open-source pipeline converting large-scale point clouds to IFC-format BIM. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.11498)]
- **WAFFLE: Multimodal Floorplan Understanding in the Wild** — Proposes a multimodal benchmark for diverse real-world floor plan understanding tasks. *Keren Ganon, Morris Alper, Rachel Mikulinsky et al., WACV 2025*. [[Paper](https://arxiv.org/abs/2412.00955)]
- **Offset-Guided Attention Network for Room-Level Aware Floor Plan Segmentation** — Proposes an offset-guided attention mechanism for room-level segmentation of architectural floor plans. *Zhangyu Wang, Ningyuan Sun, arXiv 2022*. [[Paper](https://arxiv.org/abs/2210.17411)]
- **Room Classification on Floor Plan Graphs using Graph Neural Networks** — Applies graph neural networks to classify rooms from floor plan graph representations. *Abhishek Paudel, Roshan Dhakal, Sakshat Bhattarai, arXiv 2021*. [[Paper](https://arxiv.org/abs/2108.05947)]
- **Deep Floor Plan Recognition Using a Multi-Task Network with Room-Boundary-Guided Attention** — Introduces a multi-task network with room-boundary-guided attention for floor plan recognition. *Zhiliang Zeng, Xianzhi Li, Ying Kin Yu et al., ICCV 2019*. [[Paper](https://arxiv.org/abs/1908.11025)]

---

## 3D CAD Generation and Reconstruction

Methods for generating parametric 3D CAD models from various inputs including text, images, point clouds, and sketches.

**Representative anchors:** DeepCAD for autoregressive CAD sequence generation; SkexGen for disentangled codebook generation; recent code-generation methods for LLM-native CAD.

### Autoregressive Sequence Models

- **AGDC: Autoregressive Generation of Variable-Length Sequences with Joint Discrete and Continuous Spaces** — Proposes autoregressive generation handling variable-length sequences in joint discrete-continuous parameter spaces. *Yeonsang Shin, Insoo Kim, Bongkeun Kim et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.05680)]
- **Position: You Can't Manufacture a NeRF** — Argues that implicit neural representations are insufficient for downstream CAD manufacturing workflows. *Kimmel et al., ICML 2025*.
- **CAD-SIGNet: CAD Language Inference from Point Clouds using Layer-wise Sketch Instance Guided Attention** — Infers CAD modeling sequences from point clouds using sketch-instance-guided attention layers. *Mohammad Sadil Khan, Elona Dupont, Sk Aziz Ali et al., CVPR 2024*. [[Paper](https://arxiv.org/abs/2402.17678)]
- **FlexCAD: Unified and Versatile Controllable CAD Generation with Fine-tuned Large Language Models** — Enables controllable CAD generation through fine-tuned large language models in a unified framework. *Zhanwei Zhang, Shizhao Sun, Wenxiao Wang et al., ICLR 2025*. [[Paper](https://arxiv.org/abs/2411.05823)]
- **Img2CAD: Conditioned 3D CAD Model Generation from Single Image with Structured Visual Geometry** — Generates 3D CAD models from single images using structured visual geometry conditioning. *Authors, arXiv 2024*. [[Paper](https://arxiv.org/abs/2410.03417)]
- **Img2CAD: Reverse Engineering 3D CAD Models from Images through VLM-Assisted Conditional Factorization** — Reverse engineers 3D CAD models from images via vision-language-model-assisted conditional factorization. *Authors, arXiv 2024*. [[Paper](https://arxiv.org/abs/2408.01437)]
- **ContrastCAD: Contrastive Learning-based Representation Learning for Computer-Aided Design Models** — Learns CAD model representations through contrastive learning for downstream design tasks. *Kim et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2404.01645)]
- **Pushing Auto-regressive Models for 3D Shape Generation at Capacity and Scalability** — Scales autoregressive models for 3D shape generation to higher capacity and larger datasets. *Qian et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2402.12225)]

### Diffusion-Based Generation

- **SketchDNN: Joint Continuous-Discrete Diffusion for CAD Sketch Generation** — Proposes a joint continuous-discrete diffusion model for generating CAD sketches with mixed parameter types. *Sathvik Chereddy, John Femiani, ICML 2025*. [[Paper](https://arxiv.org/abs/2507.11579)]
- **RECAD: Revisiting CAD Model Generation by Learning Raster Sketch** — Generates CAD models by learning from rasterized sketch representations rather than sequential commands. *Pu Li, Wenhao Zhang, Jianwei Guo et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.00928)]
- **Feasibility Enhancement for 3D CAD Generation** — Improves physical and geometric feasibility of diffusion-generated 3D CAD models. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.23287)]
- **Physically Grounded 3D Shape Generation for Industrial Design** — Generates 3D shapes grounded in physical constraints for industrial design applications. *Mezghanni et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.00422)]
- **GenCAD: Image-Conditioned Computer-Aided Design Generation with Transformer-Based Contrastive Representation and Diffusion Priors** — Generates CAD models from images using contrastive learning and diffusion priors. *Md Ferdous Alam, Faez Ahmed, arXiv 2024*. [[Paper](https://arxiv.org/abs/2409.16294)]
- **Shaping Realities: Enhancing 3D Generative AI with Fabrication Constraints** — Integrates fabrication constraints into 3D generative models to ensure manufacturability. *Faruqi et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2404.10142)]
- **Computer-Aided Design Generation by Cascaded Discrete Diffusion Model** — Generates CAD command-and-parameter sequences with a cascaded discrete diffusion model. *Pan et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2605.05031)]
- **Target-Guided Bayesian Flow Networks for Quantitatively Constrained CAD Generation** — Generates CAD models satisfying quantitative constraints using target-guided Bayesian flow networks. *Zheng et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.25163)]

### LLM and VLM-Based Generation

- **PR-CAD** — Progressive refinement framework for unified controllable and faithful text-to-CAD generation using LLMs. *Chen et al., ICLR 2026*. [[Paper](https://arxiv.org/abs/2604.19773)]
- **Learning Hierarchical and Geometry-Aware Graph Representations for Text-to-CAD** — Learns hierarchical graph representations encoding geometry for text-driven CAD model generation. *Zhang et al., ICLR 2026*. [[Paper](https://arxiv.org/abs/2604.10075)]
- **FutureCAD** — Achieves high-fidelity CAD generation via LLM-driven program synthesis and text-based B-Rep primitive grounding. *Jiahao Li, Qingwang Zhang, Qiuyu Chen et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.11831)]
- **ProCAD** — Proactive agents that clarify ambiguous user intent before generating robust text-to-CAD outputs. *Bo Yuan, Zelin Zhao, Petr Molodyk et al., arXiv (in review) 2026*. [[Paper](https://arxiv.org/abs/2602.03045)]
- **CAD-Tokenizer** — Modality-specific tokenization enabling text-based CAD prototyping from language descriptions. *Ruiyu Wang, Shizhao Sun, Weijian Ma et al., ICLR 2026*. [[Paper](https://arxiv.org/abs/2509.21150)]
- **CADSmith** — Multi-agent CAD generation system with programmatic geometric validation for structural correctness. *Makatura et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2603.26512)]
- **Proc3D** — Procedural 3D shape generation and parametric editing driven by large language models. *Li et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2601.12234)]
- **CAD-Coder** — Generates CAD file code from text guidance using language models. *Wang et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.08686)]
- **CADgpt: Harnessing Natural Language Processing for 3D Modelling to Enhance Computer-Aided Design Workflows** — Leverages natural language processing to generate 3D CAD models from text instructions. *Timo Kapsalis, arXiv 2024*. [[Paper](https://arxiv.org/abs/2401.05476)]
- **CAD2Program: From 2D CAD Drawings to 3D Parametric Models: A Vision-Language Approach** — Converts 2D CAD drawings into 3D parametric models using vision-language methods. *Xilin Wang, Jia Zheng, Yuanchao Hu et al., AAAI 2025*. [[Paper](https://arxiv.org/abs/2412.11892)]
- **3D-GPT: Procedural 3D Modeling with Large Language Models** — Uses LLM agents to generate procedural 3D models via structured instructions. *Sun et al., arXiv 2023*. [[Paper](https://arxiv.org/abs/2310.12945)]
- **Self-Improving CAD Generation Agents with Finite Element Analysis as Feedback** — Improves learned CAD generators by using finite element analysis results as iterative feedback. *Son et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2605.17448)]
- **STEP-LLM: Generating CAD STEP Models from Natural Language with Large Language Models** — Generates STEP-format CAD models directly from natural language using large language models. *Shi et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.12641)] [[Code](https://github.com/JasonShiii/STEP-LLM)]

### Reinforcement Learning-Enhanced Generation

- **CME-CAD** — Heterogeneous collaborative multi-expert reinforcement learning framework for CAD code generation. *Zhang et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.23333)]
- **ReCAD** — Reinforcement learning enhanced parametric CAD model generation with vision-language models. *Jiahao Li, Yusheng Luo, Yunzhong Lou et al., AAAI 2026 (Oral)*. [[Paper](https://arxiv.org/abs/2512.06328)]
- **CAD-RL** — Multimodal chain-of-thought reinforcement learning for precise CAD code generation from intent. *Ke Niu, Haiyang Yu, Zhuofan Chen et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.10118)]
- **Memory-Augmented Reinforcement Learning Agent for CAD Generation** — Generates CAD models with a memory-augmented reinforcement learning agent for advanced manufacturing. *Xiaolong et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2605.19748)]

### B-Rep and CSG Generation

- **HiDiGen** — Hierarchical diffusion model for B-Rep generation with explicit topological constraints. *Shurui Liu, Weide Chen, Ancong Wu, arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.02847)]
- **BrepARG** — Autoregressive B-Rep generation using a holistic token sequence representation. *Jiahao Li, Yunpeng Bai, Yongkang Dai et al., CVPR 2026*. [[Paper](https://arxiv.org/abs/2601.16771)]
- **Flatten The Complex** — Joint B-Rep generation via compositional k-cell particles flattening complex topology. *Junran Lu, Yuanqi Li, Hengji Li et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.17733)]
- **Topology-First B-Rep Meshing** — Prioritizes topological structure before geometry in B-Rep mesh generation. *Zhou et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.02141)]
- **DTGBrepGen** — Decouples topology and geometry into separate stages for B-Rep generation. *Jing Li, Yihang Fu, Falai Chen, arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.13110)]
- **AutoBrep** — Autoregressive B-Rep generation unifying topology and geometry in a single model. *Xiang Xu, Pradeep Kumar Jayaraman, Joseph G. Lambourne et al., SIGGRAPH Asia 2025*. [[Paper](https://arxiv.org/abs/2512.03018)]
- **HoLa** — B-Rep generation using a holistic latent representation capturing full solid structure. *Yilin Liu, Duoteng Xu, Xingyao Yu et al., SIGGRAPH 2025*. [[Paper](https://arxiv.org/abs/2504.14257)]
- **BrepGPT** — Autoregressive B-Rep generation leveraging Voronoi half-patch decomposition. *Pu Li, Wenhao Zhang, Weize Quan et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.22171)]
- **A Unified Differentiable Boolean Operator with Fuzzy Logic** — Proposes a differentiable Boolean operator using fuzzy logic for end-to-end CSG optimization. *Hsueh-Ti Derek Liu, Maneesh Agrawala, Cem Yuksel et al., SIGGRAPH 2024*. [[Paper](https://arxiv.org/abs/2407.10954)]
- **SolidGen: An Autoregressive Model for Direct B-rep Synthesis** — Generates B-rep CAD solids directly via an autoregressive transformer without intermediate representations. *Pradeep Kumar Jayaraman, Joseph G. Lambourne, Nishkrit Desai et al., TMLR 2023*. [[Paper](https://arxiv.org/abs/2203.13944)]
- **Implicit Conversion of Manifold B-Rep Solids by Neural Halfspace Representation** — Converts manifold B-rep solids to implicit fields using learned neural halfspace representations. *Hao-Xiang Guo, Yang Liu, Hao Pan et al., arXiv 2022*. [[Paper](https://arxiv.org/abs/2209.10191)]
- **CSG-Stump: A Learning Friendly CSG-Like Representation for Interpretable Shape Parsing** — Introduces a flat, learning-friendly CSG representation for interpretable 3D shape parsing. *Daxuan Ren, Jianmin Zheng, Jianfei Cai et al., ICCV 2021*. [[Paper](https://arxiv.org/abs/2108.11305)]
- **Learning Compact CAD Shapes with Adaptive Primitive Assembly** — Learns compact shape representations by adaptively assembling geometric primitives into CAD models. *Fenggen Yu, Zhiqin Chen, Manyi Li et al., arXiv 2021*. [[Paper](https://arxiv.org/abs/2104.05652)]
- **CSGNet: Neural Shape Parsers for Constructive Solid Geometry** — Parses 3D shapes into CSG program sequences using a neural network. *Gopal Sharma, Rishabh Goyal, Difan Liu et al., arXiv 2019*. [[Paper](https://arxiv.org/abs/1912.11393)]

### Point Cloud to CAD

- **CADReasoner** — Iterative program editing approach for CAD reverse engineering from point clouds. *Soslan Kabisov, Vsevolod Kirichuk, Andrey Volkov et al., CVPR 2026*. [[Paper](https://arxiv.org/abs/2603.29847)]
- **Fast Curvature Regularization of Neural SDFs for CAD Models** — Accelerates curvature regularization of neural signed distance fields for CAD geometry. *Kang et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2506.16627)]
- **Point2Primitive** — Reconstructs CAD models from point clouds by directly predicting geometric primitives. *Xinzhu Ma, Cheng Wang, Chen Tang et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.02043)]
- **NeurCADRecon** — Reconstructs CAD surfaces via neural representation enforcing zero Gaussian curvature constraints. *Kang et al., SIGGRAPH 2024*. [[Paper](https://arxiv.org/abs/2404.13420)]
- **TransCAD** — Hierarchical transformer that infers CAD modeling sequences from point clouds. *Elona Dupont, Kseniya Cherenkova, Dimitrios Mallis et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2407.12702)]
- **CAD-Recode** — Reverse engineers parametric CAD code from point cloud inputs. *Danila Rukhovich, Elona Dupont, Dimitrios Mallis et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2412.14042)]
- **PS-CAD** — Leverages local geometry prompting and selection guidance for CAD reconstruction. *Authors, ACM TOG 2024*. [[Paper](https://arxiv.org/abs/2405.15188)]
- **P2CADNet** — End-to-end network that reconstructs featured CAD models from point clouds. *Zhang et al., arXiv 2023*. [[Paper](https://arxiv.org/abs/2310.02638)]
- **Point2CAD: Reverse Engineering CAD Models from 3D Point Clouds** — Reconstructs parametric CAD models from raw 3D point clouds via surface fitting and topology recovery. *Yujia Liu, Anton Obukhov, Jan Dirk Wegner et al., arXiv 2023*. [[Paper](https://arxiv.org/abs/2312.04962)]
- **ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation** — Generates B-Rep CAD models from point clouds by predicting vertices, edges, and faces as chain complexes. *Haoxiang Guo, Shilin Liu, Hao Pan et al., SIGGRAPH 2022*. [[Paper](https://arxiv.org/abs/2205.14573)]
- **CADFit: Precise Mesh-to-CAD Program Generation with Hybrid Optimization** — Recovers precise parametric CAD programs from meshes or point clouds via hybrid optimization. *Nehme et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2605.01171)] [[Code](https://github.com/ghadinehme/CADFit)]
- **Extrusion Segmentation Strategy to Improve CAD Reconstruction from Point Cloud** — Improves CAD reconstruction from point clouds with an extrusion-segmentation strategy. *Harb et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2605.08971)]
- **Scheduling the Off-Diagonal Weingarten Loss of Neural SDFs for CAD Models** — Schedules an off-diagonal Weingarten loss to improve neural SDF reconstruction of CAD models. *Yin et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.03147)]

### Image to CAD

- **BrepGaussian** — Reconstructs B-rep CAD models from multi-view images using Gaussian splatting representations. *Wang et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2602.21105)]
- **ProcGen3D** — Learns neural procedural graph representations for image-to-3D reconstruction. *Gao et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.07142)]
- **GACO-CAD** — Generates geometry-augmented and conciseness-optimized CAD models from a single image. *Wang et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.17157)]
- **View2CAD** — Reconstructs view-centric CAD models from single RGB-D scans. *Noeckel et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2504.04000)]
- **CAD Sequence and Knowledge Inference** — Infers CAD modeling sequences and design knowledge from product images. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2501.04928)]
- **DiffCAD** — Performs weakly-supervised probabilistic CAD model retrieval and alignment from an RGB image. *Gao et al., SIGGRAPH 2024*. [[Paper](https://arxiv.org/abs/2311.18610)]
- **Multi-View to CAD** — Creates CAD models from multi-view images via geometric reconstruction. *Kniaz et al., arXiv 2023*. [[Paper](https://arxiv.org/abs/2309.13281)]
- **Img2CADSeq: Image-to-CAD Generation via Sequence-Based Diffusion** — Reconstructs high-quality B-rep CAD from single-view images via sequence-based diffusion. *Tan et al., SIGGRAPH 2026*. [[Paper](https://arxiv.org/abs/2605.13293)] [[Code](https://github.com/Rilpraa0110/Img2CADSeq)]

### Sketch to CAD

- **Learning Multimodal Feature-Enhanced Diffusion Models for Zero-Shot Sketch-Based 3D Shape Retrieval** — Combines multimodal features with diffusion models for zero-shot 3D shape retrieval from sketches. *Authors, arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.19135)]
- **AutoConstrain: Aligning Constraint Generation with Design Intent in Parametric CAD** — Generates geometric constraints aligned with designer intent for parametric CAD sketches. *Casey et al., ICCV 2025*. [[Paper](https://arxiv.org/abs/2504.13178)]
- **Robust Self-Supervised CAD Reconstruction from Three Orthographic Views Using 3D Gaussian Splatting** — Reconstructs CAD models from three orthographic views via self-supervised 3D Gaussian splatting. *Zhou et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.05161)]
- **Efficient CAD Parametric Primitive Analysis with Progressive Hierarchical Tuning** — Analyzes parametric primitives in CAD sketches using progressive hierarchical tuning for efficiency. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.18147)]
- **Sketch-Driven 3D Model Generation** — Generates 3D models directly from freehand sketches as input. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.04185)]
- **DAVINCI: A Single-Stage Architecture for Constrained CAD Sketch Inference** — Proposes a single-stage architecture that jointly infers primitives and constraints in CAD sketches. *Mallis et al., BMVC 2024*. [[Paper](https://arxiv.org/abs/2410.22857)]
- **Parametric Primitive Analysis of CAD Sketches with Vision Transformer** — Applies vision transformers to detect and parameterize geometric primitives in CAD sketches. *Li et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2407.00410)]
- **PICASSO: A Feed-Forward Framework for Parametric Inference of CAD Sketches via Rendering Self-Supervision** — Feed-forward network for parametric CAD sketch inference supervised through differentiable rendering. *Karadeniz, Mallis, Mejri et al., WACV 2025*. [[Paper](https://arxiv.org/abs/2407.13394)]
- **3D CAD Model Reconstruction from 2D Sketch using Visual Transformer and Rhino Grasshopper** — Reconstructs 3D CAD models from 2D sketches using visual transformers integrated with Rhino Grasshopper. *Authors, arXiv 2023*. [[Paper](https://arxiv.org/abs/2309.16850)]
- **3D Modeling from Free-hand Sketches with View- and Structural-Aware Adversarial Training** — Generates 3D models from freehand sketches via view-aware and structure-aware adversarial training. *Authors, arXiv 2023*. [[Paper](https://arxiv.org/abs/2312.04435)]
- **Engineering Sketch Generation for Computer-Aided Design** — Generates parametric engineering sketches for CAD using a generative model over constraint graphs. *Willis et al., arXiv 2021*. [[Paper](https://arxiv.org/abs/2104.09621)]
- **Reconstruction of a 3D Wireframe from a Single Line Drawing via Generative Depth Estimation** — Reconstructs 3D wireframes from single freehand line drawings using generative depth estimation. *Cao and Lipson, arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.13549)]

### CAD Editing

- **CAD-Editor** — A locate-then-infill framework with automated training data synthesis for text-based CAD editing. *Li et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2502.03997)]
- **BRepLer** — Language-guided editing of boundary representation CAD models via natural language instructions. *Liu et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.10201)]
- **GenPara** — Infers users' regions of interest with text-conditional shape parameters for 3D design editing. *Li et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.14096)]
- **CADMorph** — Geometry-driven parametric CAD editing via a plan-generate-verify loop. *Ma et al., NeurIPS 2025*. [[Paper](https://arxiv.org/abs/2512.11480)]
- **ParSEL** — Parameterized shape editing through natural language instructions. *Huang et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2405.20319)]
- **Zero-shot CAD Program Re-Parameterization** — Enables interactive manipulation of CAD programs without task-specific training. *Cascaval et al., arXiv 2023*. [[Paper](https://arxiv.org/abs/2306.03217)]
- **Differentiable 3D CAD Programs** — Proposes differentiable CAD programs enabling bidirectional editing between geometry and code. *Cascaval et al., arXiv 2021*. [[Paper](https://arxiv.org/abs/2110.01182)]

### Assembly Generation

- **AADvark: Agent-Aided Design for Dynamic CAD Models** — Uses LLM agents to assist designers in creating and modifying dynamic parametric CAD assemblies. *Mitch Adler, Matthew Russo, Michael Cafarella, CAIS 2026*. [[Paper](https://arxiv.org/abs/2604.15184)]
- **Error Notebook-Guided, Training-Free Part Retrieval in 3D CAD Assemblies via Vision-Language Models** — Leverages vision-language models with error notebooks for training-free part retrieval in CAD assemblies. *Tan et al., ICLR 2026*. [[Paper](https://arxiv.org/abs/2509.01350)]
- **CADKnitter: Compositional CAD Generation from Text and Geometry Guidance** — Generates compositional CAD models guided by both text descriptions and geometric constraints. *Tri Le, Khang Nguyen, Baoru Huang et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.11199)]
- **Human-Crafted 3D Primitive Assembly Generation with Auto-Regressive Transformer** — Generates human-style 3D primitive assemblies using an auto-regressive transformer architecture. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.04622)]
- **Diverse Part Synthesis for 3D Shape Creation** — Synthesizes diverse interchangeable parts to enable varied 3D shape creation. *Koo et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2401.09384)]
- **Category-Level Multi-Part Multi-Joint 3D Shape Assembly** — Assembles 3D shapes from multiple parts with multiple joint connections at category level. *Li et al., CVPR 2023*. [[Paper](https://arxiv.org/abs/2303.06163)]
- **Unsupervised 3D Shape Reconstruction by Part Retrieval and Assembly** — Reconstructs 3D shapes without supervision by retrieving and assembling compatible parts. *Authors, arXiv 2023*. [[Paper](https://arxiv.org/abs/2303.01999)]
- **JoinABLe: Learning Bottom-up Assembly of Parametric CAD Joints** — Learns to predict joint connections for bottom-up assembly of parametric CAD models. *Karl D.D. Willis, Pradeep Kumar Jayaraman, Hang Chu et al., CVPR 2022*. [[Paper](https://arxiv.org/abs/2111.12772)]

### Shape Programs and Procedural Generation

- **PyTorchGeoNodes: Enabling Differentiable Shape Programs for 3D Shape Reconstruction** — Integrates Blender geometry nodes into PyTorch for differentiable procedural shape fitting. *Stekovic et al., CVPR 2025*. [[Paper](https://arxiv.org/abs/2404.10620)]
- **Example-driven Visual Program Learning for Generating 3D Object Arrangements** — Synthesizes visual programs from examples to generate plausible 3D scene arrangements. *Hu et al., 3DV 2025 (Oral)*. [[Paper](https://arxiv.org/abs/2408.02211)]
- **GEMA: Generative Medial Abstractions for 3D Shape Synthesis** — Generates 3D shapes via medial axis-based structural abstractions for diverse synthesis. *Stekovic et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2402.16994)]
- **Discovering Abstractions for Visual Programs from Unstructured Primitives** — Learns reusable program abstractions from unstructured geometric primitives for shape modeling. *Bowers et al., arXiv 2023*. [[Paper](https://arxiv.org/abs/2305.05661)]
- **Learning to Infer 3D Shape Programs with Differentiable Renderer** — Infers procedural shape programs from images using a differentiable rendering loss. *Liu et al., arXiv 2022*. [[Paper](https://arxiv.org/abs/2206.12675)]
- **Interpretable Shape Programs** — Recovers human-readable constructive shape programs that explain 3D geometry. *Jones et al., arXiv 2022*. [[Paper](https://arxiv.org/abs/2212.11715)]
- **Learning to Infer and Execute 3D Shape Programs** — Jointly learns to infer and execute programs that reconstruct 3D shapes from primitives. *Tian et al., ICLR 2019*. [[Paper](https://arxiv.org/abs/1901.02875)]
- **Draw it like Euclid: Teaching Transformer Models to Generate CAD Profiles Using Ruler and Compass Construction Steps** — Teaches transformers to generate CAD profiles via sequences of ruler-and-compass geometric constructions. *Li et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.09428)]

### Shape Completion

- **3D Shape Completion with Latent Diffusion Models** — Leverages latent diffusion models to complete partial 3D shapes from incomplete inputs. *Authors, arXiv 2024*. [[Paper](https://arxiv.org/abs/2403.12470)]
- **Partial Object Completion with SDF Latent Transformers** — Uses signed distance field latent transformers to complete partially observed 3D objects. *Authors, arXiv 2024*. [[Paper](https://arxiv.org/abs/2411.05419)]
- **A Spatial-Aware Generative Model for 3D Shape Completion, Reconstruction, and Generation** — Proposes a spatial-aware generative model unifying shape completion, reconstruction, and generation. *Authors, arXiv 2024*. [[Paper](https://arxiv.org/abs/2403.18241)]

### NURBS and Surface Modeling

- **Flexible Neural Surface Parameterization** — Proposes a neural approach for flexible and adaptive parameterization of freeform surfaces. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2504.19210)]
- **Neural Parametric Surfaces for Shape Modeling** — Learns neural parametric surface representations for reconstructing and modeling complex 3D shapes. *Mehta et al., arXiv 2023*. [[Paper](https://arxiv.org/abs/2309.09911)]
- **NURBGen: High-Fidelity Text-to-CAD Generation through LLM-Driven NURBS Modeling** — Generates editable high-fidelity CAD from text by having an LLM drive NURBS surface modeling. *Usama et al., AAAI 2026*. [[Paper](https://arxiv.org/abs/2511.06194)] [[Code](https://github.com/SadilKhan/NURBGen)]

### Multi-Modal CAD Generation

- **Captioning and Generating 3D Content via Multi-modal Large Language Models** — Leverages multi-modal LLMs to jointly caption and generate 3D content. *Authors, arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.21798)]
- **Text-Image Conditioned 3D Generation** — Generates 3D assets conditioned on both text and image inputs. *Authors, arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.21295)]
- **Omni123: Unified Native 3D Generation and Editing within a Multimodal Framework** — Unifies 3D generation and editing natively within a single multimodal framework. *Authors, arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.02289)]
- **Collaborative Multi-Modal Coding for High-Quality 3D Generation** — Uses collaborative multi-modal coding strategies to produce high-quality 3D outputs. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.15228)]
- **Idea23D: Collaborative LMM Agents Enable 3D Model Generation from Interleaved Multimodal Inputs** — Employs collaborative LMM agents to generate 3D models from interleaved multimodal inputs. *Junhao Chen et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2404.04363)]

### Procedural and Constraint-Based Generation

- **Procedural Material Generation with Large Vision-Language Models** — Generates procedural material graphs from text or image inputs using vision-language models. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2501.18623)]
- **FeaGPT: An End-to-End Agentic AI for Finite Element Analysis** — Proposes an agentic AI system that automates the full finite element analysis workflow. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.21993)]
- **Leveraging Automatic CAD Annotations for Supervised Learning in 3D Scene Understanding** — Uses automatically generated CAD annotations to train supervised models for 3D scene understanding. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2504.13580)]
- **A Software Engineering-Inspired Shape Grammar for Durand's Plates** — Applies software engineering principles to formalize shape grammars for architectural plate designs. *Authors, arXiv 2024*. [[Paper](https://arxiv.org/abs/2404.14448)]
- **A Review on Geometric Constraint Solving** — Surveys methods and algorithms for solving geometric constraint systems in CAD. *Gao et al., ASME JCISE 2022*. [[Paper](https://arxiv.org/abs/2202.13795)]

---

## CAD Understanding and Retrieval

Representation learning, feature recognition, retrieval, and semantic understanding of CAD models.

**Representative anchors:** BRepNet and UV-Net for boundary representation learning; SketchGraphs for relational geometry modeling.

### B-Rep Representation Learning

- **Pointer-CAD: Unifying B-Rep and Command Sequences via Pointer-based Edges & Faces Selection** — Unifies B-Rep topology and CAD command sequences through pointer-based edge and face selection. *Tianzhe Chu, Yuxiao Yang, Hao Pan et al., CVPR 2026*. [[Paper](https://arxiv.org/abs/2603.04337)]
- **Joint B-Rep Generation via Compositional k-Cell Particles** — Generates B-Rep solids jointly by composing topological k-cell particles. *Authors, arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.17733)]
- **BRepMAE: Self-Supervised Masked BRep Autoencoders for Machining Feature Recognition** — Pre-trains masked autoencoders on B-Rep data for self-supervised machining feature recognition. *Can Yao, Kang Wu, Zuheng Zheng et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.22701)]
- **Boundary and Shape Representation Alignment via Self-Supervised Transformers** — Aligns boundary and shape representations through self-supervised transformer learning. *Authors, arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.07429)]
- **MiCADangelo: Fine-Grained Reconstruction of Constrained CAD Models from 3D Scans** — Reconstructs constrained CAD B-Rep models from 3D scans with fine-grained detail. *Milin Kodnongbua, Benjamin Jones, Adriana Schulz et al., NeurIPS 2025*. [[Paper](https://arxiv.org/abs/2510.23429)]
- **NH-Rep: Implicit Conversion of Manifold B-Rep Solids by Neural Halfspace Representation** — Converts B-Rep solids to implicit representations using neural halfspace decomposition. *Hao-Xiang Guo, Yang Liu, Hao Pan et al., SIGGRAPH Asia 2022*. [[Paper](https://arxiv.org/abs/2209.10191)]

### Multi-Modal CAD Representations

- **CADCrafter** — Generates parametric CAD models from unconstrained single-view images via a multi-stage pipeline. *Yunlong Chen, Xiang Xu, Ganzhangqin Yuan et al., CVPR 2025*. [[Paper](https://arxiv.org/abs/2504.04753)]
- **BrepLLM** — Enables large language models to natively understand boundary representation CAD geometry. *Liyuan Deng, Hao Guo, Yunpeng Bai et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.16413)]
- **TAMM** — Learns multi-modal 3D shape representations via three lightweight adapters for different modalities. *Zhihao Zhang, Shengcao Cao, Yu-Xiong Wang, CVPR 2024*. [[Paper](https://arxiv.org/abs/2402.18490)]
- **ULIP-2** — Scales multimodal pre-training for 3D understanding using automatically generated language descriptions. *Le Xue, Ning Yu, Shu Zhang et al., CVPR 2024*. [[Paper](https://arxiv.org/abs/2305.08275)]
- **LaGeM** — A large geometry model for unified 3D representation learning and shape diffusion. *Biao Zhang, Peter Wonka, ICLR 2025*. [[Paper](https://arxiv.org/abs/2410.01295)]
- **OpenShape** — Scales 3D shape representation learning toward open-world understanding with multi-modal alignment. *Minghua Liu, Ruoxi Shi, Kaiming Kuang et al., NeurIPS 2023*. [[Paper](https://arxiv.org/abs/2305.10764)]
- **Uni3D** — Explores unified 3D representation at scale by aligning point clouds with images and text. *Junsheng Zhou, Jinsheng Wang, Baorui Ma et al., ICLR 2024*. [[Paper](https://arxiv.org/abs/2310.06773)]
- **ULIP** — Learns a unified representation aligning language, images, and point clouds for 3D understanding. *Le Xue, Mingfei Gao, Chen Xing et al., CVPR 2023*. [[Paper](https://arxiv.org/abs/2212.05171)]
- **Point-Bind & Point-LLM** — Aligns point clouds with multi-modal models for unified 3D understanding, generation, and instruction following. *Ziyu Guo, Renrui Zhang, Xiangyang Zhu et al., arXiv 2023*. [[Paper](https://arxiv.org/abs/2309.00615)]
- **Self-Supervised Generative-Contrastive Learning of Multi-Modal Euclidean Input for 3D Shape Latent Representations** — Combines generative and contrastive self-supervised learning on multi-modal Euclidean inputs for 3D shape embeddings. *Chengzhi Wu, Julius Pfrommer, Mingyuan Zhou et al., arXiv 2023*. [[Paper](https://arxiv.org/abs/2301.04612)]

### Machining Feature Recognition

- **BRepFormer: Transformer-Based B-rep Geometric Feature Recognition** — Applies transformer architecture to recognize geometric features directly from B-rep CAD models. *Yongkang Dai, Xiaoshui Huang, Yunpeng Bai et al., ACM ICMR 2025*. [[Paper](https://arxiv.org/abs/2504.07378)]
- **Leveraging Vision-Language Models for Manufacturing Feature Recognition in CAD Designs** — Uses vision-language models to recognize manufacturing features in CAD designs without task-specific training. *Lequn Chen, Muhammad Tayyab Khan, Ye Han Ng et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2411.02810)]
- **AAGNet: Automatic Machining Feature Recognition using Geometric Attributed Adjacency Graphs** — Recognizes machining features automatically using graph neural networks on attributed adjacency graphs. *Hongjin Wu, Ang Liu, Kai Wu, Computer-Aided Design 2024*. [[Paper](https://doi.org/10.1016/j.rcim.2023.102661)]
- **CNC-Net: Self-Supervised Learning for CNC Machining Operations** — Proposes self-supervised learning to recognize CNC machining operations from 3D shapes. *Mohsen Yavartanoo, Sangmin Hong, Reyhaneh Neshatavar et al., arXiv 2023*. [[Paper](https://arxiv.org/abs/2312.09925)]
- **Simplified Learning of CAD Features Leveraging a Deep Residual Autoencoder** — Employs a deep residual autoencoder to simplify learning of CAD feature representations. *Authors, arXiv 2022*. [[Paper](https://arxiv.org/abs/2202.10099)]
- **Geometry based Machining Feature Retrieval with Inductive Transfer Learning** — Retrieves machining features from geometric data using inductive transfer learning. *Sai Sree Harsha, Bharadwaj Manda, Ramanathan Muthuganapathy, arXiv 2021*. [[Paper](https://arxiv.org/abs/2108.11838)]
- **A Learning-based Approach to Feature Recognition of Engineering Shapes** — Presents a learning-based method for recognizing features in engineering shape models. *Authors, arXiv 2021*. [[Paper](https://arxiv.org/abs/2112.07962)]
- **FeatureNet: Machining Feature Recognition Based on 3D Convolution Neural Network** — Introduces 3D CNN for machining feature recognition from volumetric CAD representations. *Zhibo Zhang, Prakhar Jaiswal, Rahul Rai, CAD 2018*. [[Paper](https://doi.org/10.1016/j.cad.2018.03.006)]
- **FeatureFox: Sample-Efficient Panoptic Graph Segmentation for Machining Feature Recognition in B-Rep 3D-CAD Models** — Recognizes machining features on B-rep models via sample-efficient panoptic graph segmentation. *Fuchs et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.26770)]

### CAD Model Retrieval

- **OSCAR: Open-Set CAD Retrieval from a Language Prompt and a Single Image** — Retrieves CAD models from open-set databases using combined language and single-image queries. *Tessa Pulli, Jean-Baptiste Weibel, Peter Hoenig et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.07333)]
- **CADGCL: Unsupervised Retrieval of CAD Models via Boundary Representations** — Proposes unsupervised graph contrastive learning for CAD retrieval using B-Rep structures. *Qin et al., The Visual Computer 2025*. [[Paper](https://doi.org/10.1007/s00371-025-03949-y)]
- **SCA3D: Enhancing Cross-modal 3D Retrieval via 3D Shape and Caption Paired Data Augmentation** — Augments paired shape-caption data to improve cross-modal 3D shape retrieval. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2502.19128)]
- **GC-CAD: Self-supervised Graph Neural Network for Mechanical CAD Retrieval** — Introduces a self-supervised graph neural network with graph contrastive learning for CAD retrieval. *Yuhan Quan, Huan Zhao, Jinfeng Yi et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2406.08863)]
- **Leveraging Cross-View Correspondence and Cross-Modal Mining for 3D Retrieval** — Exploits cross-view correspondence and cross-modal mining to enhance 3D object retrieval. *Authors, arXiv 2024*. [[Paper](https://arxiv.org/abs/2405.04103)]
- **FastCAD: Real-Time CAD Retrieval and Alignment from Scans and Videos** — Enables real-time CAD model retrieval and alignment from RGB-D scans and video streams. *Gumeli et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2403.15161)]
- **HOC-Search: Efficient CAD Model and Pose Retrieval from RGB-D Scans** — Proposes hierarchical optimization for efficient joint CAD model and pose retrieval from RGB-D data. *Stefan Ainetter, Sinisa Stekovic, Friedrich Fraundorfer et al., 3DV 2024*. [[Paper](https://arxiv.org/abs/2309.06107)]
- **Fine-Tuned but Zero-Shot 3D Shape Sketch View Similarity and Retrieval** — Enables zero-shot sketch-based 3D shape retrieval using fine-tuned view similarity without task-specific training data. *Tisse et al., arXiv 2023*. [[Paper](https://arxiv.org/abs/2306.08541)]
- **Accurate Instance-Level CAD Model Retrieval in a Large-Scale Database** — Proposes instance-level CAD model retrieval with accurate alignment from large-scale shape databases. *Jiaxin Wei, Haibin Huang, Chongyang Ma et al., ICCV 2023*. [[Paper](https://arxiv.org/abs/2207.01339)]
- **UVStyle-Net: Unsupervised Few-shot Learning of 3D Style Similarity Measure for B-Reps** — Learns a 3D style similarity metric for B-Rep CAD models via unsupervised few-shot learning. *Peter Meltzer, Hooman Shayani, Aditya Sanghi et al., ICCV 2021*. [[Paper](https://arxiv.org/abs/2105.02961)]
- **Text-to-CAD Retrieval: A Strong Baseline** — Establishes a strong baseline for retrieving CAD models from natural-language queries. *Pan et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2605.05572)]

### Sketch-Based Retrieval

- **Multi-View Hierarchical Graph Neural Network for Sketch-Based 3D Shape Retrieval** — Proposes a multi-view hierarchical graph neural network for sketch-based 3D shape retrieval. *Authors, arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.18019)]
- **SketchCleanNet: A Deep Learning Approach to the Enhancement and Correction of Query Sketches for a 3D CAD Model Retrieval System** — Uses deep learning to clean and correct hand-drawn query sketches for improved 3D CAD retrieval. *Bharadwaj Manda, Ramanathan Muthuganapathy, Computers & Graphics 2024*. [[Paper](https://arxiv.org/abs/2207.00732)]
- **CADSketchNet: An Annotated Sketch Dataset for 3D CAD Model Retrieval with Deep Neural Networks** — Introduces an annotated sketch dataset and benchmarks deep neural networks for 3D CAD model retrieval. *Bharadwaj Manda, Sai Sree Harsha, Subhrajit Dey et al., Computers & Graphics 2022*. [[Paper](https://arxiv.org/abs/2107.06212)]

### Shape Classification

- **CSTNet: Constraint-Aware Feature Learning for Parametric Point Cloud** — Learns geometric constraint features from parametric point clouds for CAD shape classification. *Cheng Cheng, Changqing Zou, Ruowei Wang et al., ICCV 2025*. [[Paper](https://arxiv.org/abs/2411.07747)]
- **CAD 3D Model Classification by Graph Neural Networks: A New Approach Based on STEP Format** — Classifies CAD models using graph neural networks applied directly to STEP file representations. *Lorenzo Mandelli, Stefano Berretti, arXiv 2022*. [[Paper](https://arxiv.org/abs/2210.16815)]

### B-Rep Segmentation

- **Geometry-Conditioned Instance Segmentation for Industrial Objects** — Proposes geometry-conditioned methods for instance segmentation of industrial CAD objects. *Li et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.20551)]
- **Repurposing 3D Generative Model for Part Segmentation** — Repurposes pretrained 3D generative models to perform part segmentation tasks. *Wu et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.16869)]
- **Geometric Deep Learning with A-to-Z BRep Annotations for AI-Assisted CAD Modeling and Reverse Engineering** — Provides comprehensive B-Rep annotations enabling geometric deep learning for CAD modeling and reverse engineering. *Wenjie Niu, Qiang Zou, arXiv 2025*. [[Paper](https://arxiv.org/abs/2603.12605)]
- **Joint Neural SDF Reconstruction and Semantic Segmentation for CAD Models** — Jointly reconstructs signed distance fields and performs semantic segmentation on CAD models. *Chen et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.03837)]
- **Few-shot Structure-Informed Machinery Part Segmentation with Foundation Models and Graph Neural Networks** — Combines foundation models and graph neural networks for few-shot machinery part segmentation. *Zhang et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2501.10080)]
- **Label-Efficient Part Segmentation** — Proposes label-efficient methods to reduce annotation cost for 3D part segmentation. *Liu et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2501.07434)]
- **Scan-to-BRep: BRep Boundary and Junction Detection for CAD Reverse Engineering** — Detects B-Rep boundaries and junctions from 3D scans for CAD reverse engineering. *Yujia Liu, Anton Obukhov, Riccardo De Lutio et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2409.14087)]

### Sequence-Based Encoding

- **Unsupervised Contrastive Learning for Efficient and Robust Spectral Shape Matching** — Proposes unsupervised contrastive learning to improve efficiency and robustness of spectral shape matching. *Cao et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.18924)]
- **3D Shape Matching: From Foundations to Open Challenges and Opportunities** — Surveys 3D shape matching methods from classical foundations to modern open challenges. *Eisenberger et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.01274)]
- **Diffusion Models for Shape Correspondence** — Applies diffusion models to establish dense correspondences between 3D shapes. *Attaiki et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.01845)]

### Assembly Understanding

- **DYNAMO: Dependency-Aware Deep Learning Framework for Articulated Assembly Motion Prediction** — Predicts articulated motion in mechanical assemblies using dependency-aware deep learning. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.12430)]
- **Generative 3D Part Assembly via Part-Whole-Hierarchy Message Passing** — Generates 3D part assemblies using hierarchical message passing between parts and wholes. *Bi'an Du, Jianxin Ma, Junyi Zhu et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2402.17464)]
- **DiffAssemble: A Unified Graph-Diffusion Model for 2D and 3D Reassembly** — Unifies 2D and 3D reassembly tasks with a graph-diffusion generative model. *Scarpellini et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2402.19302)]
- **What's in a Name? Evaluating Assembly-Part Semantic Knowledge in Language Models through User-Provided Names in CAD Files** — Evaluates whether language models understand semantic relationships in CAD assembly-part naming. *Peter Hartog, Daniele Grandi, Karl D.D. Willis et al., arXiv 2023*. [[Paper](https://arxiv.org/abs/2304.14275)]
- **Synthesizing CAD Assemblies in Fusion 360** — Proposes methods for synthesizing multi-part CAD assemblies within Fusion 360. *Dominik Bauer, Nikolas Lamb, Sean Bittner, arXiv 2023*. [[Paper](https://arxiv.org/abs/2311.18492)]
- **HG-CAD: Material Prediction for Design Automation Using Graph Representation Learning** — Predicts materials for CAD components using heterogeneous graph representation learning. *Shijie Bian, Daniele Grandi, Pradeep Kumar Jayaraman et al., IDETC-CIE 2022 / JCISE 2024*. [[Paper](https://arxiv.org/abs/2209.12793)]

---

## Simulation and Design Optimization

AI-accelerated simulation surrogates, physics-informed methods, and topology optimization.

**Representative anchors:** Fourier Neural Operator for PDE surrogates; Physics-Informed Neural Networks for physics-constrained learning; TopoDiff and related models for generative topology optimization.

### Neural Operators and FEA Surrogates

- **NOEM: Efficient and Scalable Finite Element Method Enabled by Reusable Neural Operators** — Proposes reusable neural operators to accelerate and scale finite element simulations. *NOEM authors, Nature Computational Science 2026*.
- **A Graph Neural Network Surrogate for 3D Finite Element Modeling: Accelerated Full-Field Parameter Identification in Aluminum Alloy 6DR1** — Uses a GNN surrogate to accelerate full-field parameter identification in 3D FE models. *GNN-FE authors, Modelling and Simulation in Materials Science and Engineering 2026*.
- **Efficient Dilated Squeeze and Excitation Neural Operator for Differential Equations** — Introduces a dilated squeeze-and-excitation architecture for efficiently solving differential equations. *Authors, arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2601.17407)]
- **Generative AI-Enhanced Probabilistic Multi-Fidelity Surrogate Modeling via Transfer Learning** — Combines generative AI with transfer learning for probabilistic multi-fidelity surrogate models. *Authors, arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2602.00072)]
- **A Unified Hierarchical Multi-Task Multi-Fidelity Framework for Data-Efficient Surrogate Modeling in Manufacturing** — Presents a hierarchical multi-task multi-fidelity framework for data-efficient manufacturing surrogates. *Authors, arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2603.09842)]
- **A Practical Introduction to Neural Operators in Scientific Computing** — Provides a practical tutorial on neural operator methods for scientific computing applications. *de Hoop et al., arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2503.05598)]
- **Equilibrium Neural Operator: A Physics-Informed Neural Operator for Multiscale Simulations** — Proposes a physics-informed neural operator enforcing equilibrium constraints for multiscale simulations. *EquiNO authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2504.07976)]
- **A Comprehensive Evaluation of Graph Neural Networks and Physics Informed Learning for Surrogate Modelling of Finite Element Analysis** — Benchmarks GNNs and physics-informed methods as surrogates for finite element analysis. *Evaluation authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2510.15750)]
- **An FEA Surrogate Model with Boundary Oriented Graph Embedding Approach for Rapid Design** — Proposes boundary-oriented graph embeddings to accelerate FEA surrogate predictions for rapid design iteration. *Xingyu Fu, Fengfeng Zhou, Dheeraj Peddireddy et al., Journal of Computational Design and Engineering 2023*. [[Paper](https://arxiv.org/abs/2108.13509)]
- **Sequential Deep Operator Networks (S-DeepONet) for Predicting Full-Field Solutions Under Time-Dependent Loads** — Extends DeepONet sequentially to predict full-field structural responses under time-dependent loading conditions. *Junyan He, Shashank Kushwaha, Jaewan Park et al., arXiv preprint 2023*. [[Paper](https://arxiv.org/abs/2306.08218)]
- **Reduced-order Modeling for Parameterized PDEs via Implicit Neural Representations** — Uses implicit neural representations to build compact reduced-order models for parameterized PDEs. *Tianshu Wen, Kookjin Lee, Youngsoo Choi, arXiv 2023*. [[Paper](https://arxiv.org/abs/2311.16410)]
- **Learning Deep Implicit Fourier Neural Operators (IFNOs) with Applications to Heterogeneous Material Modeling** — Introduces implicit Fourier neural operators for learning solution maps in heterogeneous material simulations. *Huaiqian You, Quinn Zhang, Colton J. Ross et al., CMAME 2022*. [[Paper](https://arxiv.org/abs/2203.08205)]
- **Toward Reusable Surrogate Models: Graph-Based Transfer Learning on Trusses** — Applies graph-based transfer learning to create reusable surrogate models across different truss topologies. *Whalen et al., Journal of Mechanical Design 2022*. [[Paper](https://arxiv.org/abs/2109.02689)]
- **Fourier Neural Operator for Parametric Partial Differential Equations** — Learns mappings between function spaces using Fourier layers for efficient PDE solving. *Li et al., ICLR 2021*. [[Paper](https://arxiv.org/abs/2010.08895)]
- **Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators** — Proposes DeepONet architecture for learning nonlinear operators between infinite-dimensional function spaces. *Lu et al., Nature Machine Intelligence 2021*. [[Paper](https://doi.org/10.1038/s42256-021-00302-5)]

### Computational Fluid Dynamics

- **Faster by Design: Interactive Aerodynamics via Neural Surrogates Trained on Expert-Validated CFD** — Enables interactive aerodynamic exploration using neural surrogates trained on expert-validated CFD simulations. *Thumiger et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.18491)]
- **A Forward Look on AI Foundation Models in Computational Fluid Dynamics** — Surveys opportunities and challenges for large-scale AI foundation models in CFD workflows. *AI-CFD Foundation authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.20455)]
- **Accelerating Transient CFD through Machine Learning-Based Flow Initialization** — Uses machine learning to generate better initial flow fields, accelerating transient CFD convergence. *ML-CFD Init authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.15766)]
- **Physics-Constrained DeepONet for Surrogate CFD Models** — Incorporates physics constraints into DeepONet architectures to build accurate surrogate CFD models. *PC-DeepONet CFD authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.11196)]
- **Physics-Based Simulations with Masked Graph Neural Networks** — Applies masked graph neural networks to improve accuracy and efficiency of physics-based simulations. *Masked GNN authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2501.08738)]
- **TripOptimizer: Generative 3D Shape Optimization and Drag Prediction using Triplane VAE Networks** — Proposes triplane VAE networks for joint generative 3D shape optimization and drag prediction. *Thumiger et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.12224)]
- **Accelerating Shape Optimization by Deep Neural Networks with On-the-fly Determined Architecture** — Accelerates shape optimization using DNNs whose architecture is determined dynamically during training. *Kang et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.03555)]
- **Surrogate-Based Differentiable Pipeline for Shape Optimization** — Presents a fully differentiable surrogate pipeline enabling gradient-based aerodynamic shape optimization. *Muller et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.10761)]
- **Learning Mesh-Based Simulation with Graph Networks** — Uses graph neural networks to learn physics simulations directly on mesh representations. *Pfaff et al., ICLR 2021 (Outstanding Paper)*. [[Paper](https://arxiv.org/abs/2010.03409)]
- **The Neural Particle Method -- An Updated Lagrangian Physics Informed Neural Network for Computational Fluid Dynamics** — Combines Lagrangian particle methods with physics-informed neural networks for fluid simulation. *Henning Wessels, Christian Weienfels, Peter Wriggers, arXiv preprint 2020*. [[Paper](https://arxiv.org/abs/2003.10208)]

### Physics-Informed Neural Networks

- **Equation Discovery, Parametric Simulation, and Optimization Using PINN for Heat Conduction** — Combines equation discovery with parametric PINN simulation for heat conduction optimization. *PINN Heat Opt authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2510.25925)]
- **PINNsAgent: Automated PDE Surrogation with Large Language Models** — Uses LLM agents to automate physics-informed neural network construction for PDE surrogate modeling. *PINNsAgent authors, ICML 2025*. [[Paper](https://arxiv.org/abs/2501.12053)]
- **Physics-Informed Diffusion Models** — Integrates physical constraints into diffusion models for generating physically consistent samples. *Bastek et al., ICLR 2025*. [[Paper](https://arxiv.org/abs/2403.14404)]
- **eXtended Physics-Informed Neural Network Method for Fracture Mechanics Problems** — Extends PINNs with enrichment functions to model crack discontinuities in fracture mechanics. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2509.13952)]
- **Physics-Informed Neural Operator for Learning Partial Differential Equations** — Proposes a neural operator architecture incorporating physical equations to learn PDE solution mappings. *Li et al., ACM/JMS 2024*. [[Paper](https://arxiv.org/abs/2111.03794)]
- **Physics-Informed Neural Networks and Extensions: A Review** — Surveys PINN methodologies, training strategies, and extensions across scientific computing applications. *PINN Review authors, arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2408.16806)]
- **Physics-Informed Neural Networks: From Fundamentals to Applications in Complex Systems** — Reviews PINN fundamentals and their application to multiphysics and complex engineering systems. *PINN Complex authors, arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2410.00422)]
- **Physics-Informed Neural Networks for Solving Thermo-Mechanics Problems of Functionally Graded Material** — Applies PINNs to solve coupled thermo-mechanical problems in functionally graded materials. *Thermo-PINN authors, arXiv preprint 2022*. [[Paper](https://arxiv.org/abs/2111.10751)]
- **Scientific Machine Learning Through Physics-Informed Neural Networks: Where We Are and What's Next** — Comprehensive survey of PINN methods, architectures, training strategies, and open challenges. *Cuomo et al., Journal of Scientific Computing 2022*. [[Paper](http://arxiv.org/abs/2201.05624)]
- **Transfer Learning Based Physics-Informed Neural Networks for Solving Inverse Problems in Engineering Structures** — Applies transfer learning to PINNs for efficient inverse problem solving in structural engineering. *Chen Xu, Ba Trung Cao, Yong Yuan et al., arXiv preprint 2022*. [[Paper](https://arxiv.org/abs/2205.07731)]
- **Physics-Informed Neural Networks (PINNs) for Heat Transfer Problems** — Demonstrates PINNs for solving forward and inverse heat transfer problems without labeled data. *Cai et al., Journal of Heat Transfer 2021*. [[Paper](https://doi.org/10.1115/1.4050542)]
- **Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations** — Introduces PINNs embedding physical laws into neural network loss functions for PDE solving. *Maziar Raissi, Paris Perdikaris, George Em Karniadakis, Journal of Computational Physics 2019*. [[Paper](https://doi.org/10.1016/j.jcp.2018.10.045)]

### Deep Learning for Topology Optimization

- **Multiscale Topology Optimization of Hyperelastic Structures Using Physics-Augmented Neural Networks** — Combines physics-augmented neural networks with multiscale methods for hyperelastic topology optimization. *Authors, arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2604.06519)]
- **Physics-Informed Transformer for Real-Time High-Fidelity Topology Optimization** — Proposes a physics-informed transformer enabling real-time high-fidelity topology optimization predictions. *Authors, arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2604.03522)]
- **Variational Quantum Latent Encoding for Topology Optimization** — Leverages variational quantum circuits for latent space encoding in topology optimization. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2506.17487)]
- **Transformer-Based Topology Optimization** — Applies transformer architectures to directly predict optimized topologies from boundary conditions. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2509.05800)]
- **A Foundation Model for Shape- and Resolution-Free Structural Topology Optimization** — Introduces a foundation model that generalizes across arbitrary shapes and resolutions for topology optimization. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2510.23667)]
- **Latent Space Diffusion for Topology Optimization** — Uses diffusion models in latent space to generate diverse high-performance topology designs. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2508.05624)]
- **Accelerating Metamaterial Topology Optimization Using Deep Super-Resolution Networks** — Applies deep super-resolution networks to accelerate metamaterial topology optimization on coarse meshes. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2511.04795)]
- **Diverse Topology Optimization Using Modulated Neural Fields (TOM)** — Proposes modulated neural fields to generate diverse near-optimal topology solutions from single optimization. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2502.13174)]
- **Accelerated Topology Optimization Design of 3D Structures Based on Deep Learning** — Uses deep learning to accelerate topology optimization for 3D structural design. *Xiang Cheng, Dalei Wang, Yue Pan et al., Structural and Multidisciplinary Optimization 2022*. [[Paper](https://doi.org/10.1007/s00158-022-03194-0)]
- **TOuNN: Topology Optimization using Neural Networks** — Represents topology as a continuous neural network field for gradient-based structural optimization. *Chandrasekhar and Suresh, Structural and Multidisciplinary Optimization 2021*. [[Paper](https://doi.org/10.1007/s00158-020-02748-4)]

### Generative and LLM-Driven Topology Optimization

- **Multi-Material Multi-Physics Topology Optimization with Physics-Informed Gaussian Process Priors** — Integrates physics-informed Gaussian process priors into multi-material, multi-physics topology optimization. *Authors, arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2602.17783)]
- **Toward Large Language Model-Driven Symbolic Topology Optimisation for Rapid Structural Concept Generation in Manufacturable Design** — Uses LLMs to drive symbolic topology optimization for rapid, manufacturable structural concept generation. *Al Ali, Journal of Manufacturing and Materials Processing 2026*. [[Paper](https://doi.org/10.3390/jmmp10040117)]
- **Using Hand-Drawn Inputs for Diffusion-Based Topology Optimization** — Leverages hand-drawn sketches as inputs to guide diffusion-based topology optimization. *Authors, arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2603.18960)]
- **Guiding Topology Optimization Diffusion with Human Preferences** — Incorporates human preference feedback to steer diffusion-model-based topology optimization results. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2508.01589)]
- **Two-Stage Multiobjective Topology Optimization Method via SwinUnet with Enhanced Generalization** — Proposes a two-stage SwinUnet approach for multiobjective topology optimization with improved generalization. *Xiang et al., Scientific Reports 2025*. [[Paper](https://doi.org/10.1038/s41598-025-92793-0)]
- **Diffusion Models for Topology Optimization in 3D Printing Applications** — Applies diffusion models to generate topology-optimized structures tailored for 3D printing. *Bekbolat et al., Journal of Applied Physics 2025*. [[Paper](https://doi.org/10.1063/5.0246189)]
- **Multiphysics Design Optimization via Generative Adversarial Networks** — Employs GANs to accelerate multiphysics design optimization across coupled physical domains. *Kazemi et al., Journal of Mechanical Design 2022*. [[Paper](https://doi.org/10.1115/1.4055377)]

### AI-Driven Generative Design

- **Agentic LLM Orchestration of Engineering Analysis in Product Development Design Practice** — Orchestrates LLM agents to automate engineering analysis workflows in product development. *Authors, arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2603.10249)]
- **SimuAgent: An LLM-Based Simulink Modeling Assistant Enhanced with Reinforcement Learning** — Proposes an RL-enhanced LLM agent that assists engineers in building Simulink models. *Authors, arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2601.05187)]
- **An LLM-Driven Multi-Agent Framework for Autonomous Construction of Deep Learning Surrogate Models in Subsurface Flow** — Uses LLM-driven multi-agent collaboration to autonomously build surrogate models for subsurface flow. *Authors, arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2604.11945)]
- **Large Language Model-Empowered Next-Generation Computer-Aided Engineering** — Presents a vision for LLM-empowered CAE covering simulation, optimization, and design automation. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2509.11447)]
- **Automating Data-Driven Modeling and Analysis for Engineering Applications using Large Language Model Agents** — Automates data-driven modeling pipelines for engineering tasks via LLM agents. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2510.01398)]
- **Large Language Models for Combinatorial Optimization of Design Structure Matrix** — Applies LLMs to solve combinatorial optimization problems on design structure matrices. *Authors, ICED 2025*. [[Paper](https://arxiv.org/abs/2506.09749)]
- **Bayesian and Non-Bayesian Multi-Fidelity Surrogate Models for Multi-Objective Aerodynamic Optimization Under Extreme Cost Imbalance** — Compares multi-fidelity surrogate strategies for multi-objective aerodynamic shape optimization. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2505.17279)]
- **Benchmarking Generative AI Against Bayesian Optimization for Constrained Multi-Objective Inverse Design** — Benchmarks generative AI methods against Bayesian optimization for constrained multi-objective inverse design. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2511.00070)]
- **Towards Goal, Feasibility, and Diversity-Oriented Deep Generative Models in Design** — Proposes generative model frameworks that balance goal performance, feasibility, and diversity in engineering design. *Lyle Regenwetter, Faez Ahmed, Journal of Mechanical Design 2022*. [[Paper](https://arxiv.org/abs/2206.07170)]
- **Evolving Through the Looking Glass: Learning Improved Search Spaces with Variational Autoencoders** — Uses variational autoencoders to learn improved latent search spaces for evolutionary design optimization. *Peter J. Bentley, Soo Ling Lim, Adam Gaier et al., Autodesk Research 2020*. [[Paper](https://doi.org/10.1007/978-3-031-14714-2_26)]
- **COSMO-Agent: Tool-Augmented Agent for Closed-Loop Optimization, Simulation, and Modeling Orchestration** — Bridges the CAD-CAE gap with a tool-augmented agent orchestrating closed-loop design, simulation, and optimization. *Deng et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2605.20190)]

---

## Manufacturing-Aware Design

Design for manufacturing, additive manufacturing, assembly planning, and CAD/CAM integration.

**Representative anchors:** MeshCNN for mesh-based learning applicable to manufacturing; InverseCSG for reverse engineering; recent DfAM methods that integrate topology optimization with additive-manufacturing constraints.

### Design for Manufacturing (DFM)

- **Kolmogorov-Arnold Networks-Based Tolerance-Aware Manufacturability Assessment Integrating Design-for-Manufacturing Principles** — Uses Kolmogorov-Arnold networks for tolerance-aware manufacturability assessment integrating DFM principles. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2601.06334)]
- **Enhancing the Product Quality of the Injection Process Using eXplainable Artificial Intelligence** — Applies explainable AI to enhance product quality in injection molding processes. *arXiv preprint / Processes 2025*. [[Paper](https://arxiv.org/abs/2503.02338)]
- **Machine Learning-Based Manufacturing Cost Prediction from 2D Engineering Drawings via Geometric Features** — Predicts manufacturing costs from 2D engineering drawings using geometric feature extraction and ML. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2508.12440)]
- **Data-Driven Prediction of Casting Defects in Magnesium High-Pressure Die Casting Using Machine Learning** — Predicts casting defects in magnesium high-pressure die casting using data-driven ML models. *Pachandrin et al., International Journal of Metalcasting 2025*. [[Paper](https://doi.org/10.1007/s40962-025-01592-w)]
- **An Artificial Intelligence Application for In-Process Springback Control of Sheet Metal Bending** — Applies AI for real-time springback control during sheet metal bending processes. *Fann et al., ASME J. Manufacturing Science and Engineering 2025*. [[Paper](https://doi.org/10.1115/1.4067740)]
- **DRL-Based Injection Molding Process Parameter Optimization for Adaptive and Profitable Production** — Uses deep reinforcement learning to optimize injection molding parameters for adaptive production. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2505.10988)]
- **Advancing Welding Defect Detection in Maritime Operations via Adapt-WeldNet** — Proposes Adapt-WeldNet for improved welding defect detection in maritime operations. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2508.00381)]
- **Adapting CLIP for Few-Shot Image Inspection in Manufacturing Quality Control** — Adapts CLIP for few-shot visual inspection in manufacturing quality control settings. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2501.12596)]
- **Explainable Artificial Intelligence for Manufacturing Cost Estimation and Machining Feature Visualization** — Uses explainable AI to estimate manufacturing costs and visualize machining features. *Soyoung Yoo, Namwoo Kang, arXiv preprint 2020*. [[Paper](https://arxiv.org/abs/2010.14824)]
- **A Machine-Learning Framework for Design for Manufacturability** — Proposes a machine-learning framework to evaluate and improve design manufacturability. *Aditya Balu, Sambit Ghadai, Gavin Young et al., arXiv preprint 2017*. [[Paper](https://arxiv.org/abs/1703.01499)]
- **Learning Localized Geometric Features Using 3D-CNN: An Application to Manufacturability Analysis of Drilled Holes** — Applies 3D-CNNs to learn localized geometric features for manufacturability analysis of drilled holes. *Aditya Balu, Sambit Ghadai, Kin Gwn Lore et al., arXiv preprint 2016*. [[Paper](https://arxiv.org/abs/1612.02141)]

### Design for Additive Manufacturing (DFAM)

- **Discovery of Feasible 3D Printing Configurations for Metal Alloys via AI-Driven Adaptive Experimental Design** — Uses AI-driven adaptive experiments to identify viable printing parameters for metal alloy additive manufacturing. *Authors, arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2601.17587)]
- **Graph Neural Network-Based Topology Optimization for Self-Supporting Structures in Additive Manufacturing** — Applies graph neural networks to topology optimization that ensures self-supporting structures without post-processing. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2508.19169)]
- **Generative Artificial Intelligence in Lattice Structure Design for Additive Manufacturing: A Critical Review** — Reviews generative AI methods for designing lattice structures tailored to additive manufacturing constraints. *Su et al., eScience of Additive Manufacturing 2025*. [[Paper](https://doi.org/10.36922/esam025110006)]
- **Additive Manufacturing Processes Protocol Prediction by Artificial Intelligence using X-ray Computed Tomography Data** — Predicts AM process protocols from X-ray CT scan data using artificial intelligence models. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2501.14306)]
- **Sample-Efficient Bayesian Transfer Learning for Online Machine Parameter Optimization** — Proposes Bayesian transfer learning to efficiently optimize manufacturing machine parameters with limited samples. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2503.15928)]
- **Real-Time Decision-Making for Digital Twin in Additive Manufacturing with Model Predictive Control** — Integrates model predictive control with digital twins for real-time AM process decisions. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2501.07601)]
- **Digital Twin-Enabled Real-Time Control in Robotic Additive Manufacturing via Soft Actor-Critic RL** — Applies soft actor-critic reinforcement learning for real-time control of robotic AM via digital twins. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2501.18016)]
- **Computational, Data-Driven, and Physics-Informed ML Approaches for Microstructure Modeling in Metal AM** — Surveys computational and physics-informed machine learning methods for predicting microstructure in metal AM. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2505.01424)]

### Assembly Planning and Tolerance

- **Learning-Based Strategy for Composite Robot Assembly Skill Adaptation** — Learns transferable assembly skills for composite robot systems via strategy adaptation. *Authors, arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2604.06949)]
- **Connector-Aware General Robotic Assembly from Instruction Manuals via Vision-Language Models** — Uses vision-language models to interpret instruction manuals for connector-aware robotic assembly. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2510.16344)]
- **AssemMate: Graph-Based LLM for Robotic Assembly Assistance** — Leverages graph-based large language models to provide step-by-step robotic assembly guidance. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2509.11617)]
- **Fabrica: Dual-Arm Assembly of General Multi-Part Objects via Integrated Planning and Learning** — Integrates planning and learning for dual-arm robotic assembly of general multi-part objects. *Tian et al., CoRL 2025 (Best Paper Award)*. [[Paper](https://arxiv.org/abs/2506.05168)]
- **Hierarchical Hybrid Learning for Long-Horizon Contact-Rich Robotic Assembly** — Proposes hierarchical hybrid learning to solve long-horizon contact-rich assembly tasks. *Sun et al., CoRL 2025*. [[Paper](https://arxiv.org/abs/2409.16451)]
- **REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly** — Introduces a multimodal benchmark dataset for contact-rich robotic assembly and disassembly research. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2502.05086)]
- **Tolerance Allocation of Complex Systems Based on Supervised Machine Learning and Adaptive Sampling** — Applies supervised learning with adaptive sampling to optimize tolerance allocation in complex systems. *Dantan et al., International Journal of Advanced Manufacturing Technology 2025*. [[Paper](https://doi.org/10.1007/s00170-025-17336-3)]
- **Contact-Rich Robotic Assembly in Construction via Diffusion Policy Learning** — Applies diffusion-based policy learning to contact-rich robotic assembly tasks in construction. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2511.17774)]
- **Large-Scale Multi-Robot Assembly Planning for Autonomous Manufacturing** — Proposes scalable planning methods for coordinating multiple robots in large-scale assembly tasks. *Kyle Brown, Dylan M. Asmar, Mac Schwager et al., arXiv 2023*. [[Paper](https://arxiv.org/abs/2311.00192)]
- **Statistical Tolerance Allocation Design Considering Form Errors Based on Rigid Assembly Simulation and Deep Q-Network** — Uses deep Q-network with rigid assembly simulation to optimize statistical tolerance allocation under form errors. *Ci He, Shuyou Zhang, Lemiao Qiu et al., International Journal of Advanced Manufacturing Technology 2021*. [[Paper](https://doi.org/10.1007/s00170-020-06283-w)]

### CAD/CAM Integration

- **Self-Supervised Masked BRep Autoencoders for Machining Feature Recognition** — Pre-trains masked autoencoders on B-Rep data for self-supervised machining feature recognition. *Authors, arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2602.22701)]
- **DeepMill: Neural Accessibility Learning for Subtractive Manufacturing** — Learns tool accessibility maps via neural networks to guide subtractive milling operations. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2502.06093)]
- **Implicit Neural Field-Based Process Planning for Multi-Axis Manufacturing** — Uses implicit neural fields to automate process planning for multi-axis manufacturing. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2511.17578)]
- **Knowledge Graph Fusion with Large Language Models for Accurate, Explainable Manufacturing Process Planning** — Fuses knowledge graphs with LLMs to generate explainable manufacturing process plans. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2506.13026)]
- **Implicit Neural Fields for Collision-Free Multi-Axis 3D Printing** — Represents collision constraints as implicit neural fields for safe multi-axis 3D printing paths. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2509.05345)]
- **A Cutting Mechanics-Based Machine Learning Modeling Method to Discover Governing Equations of Machining Dynamics** — Discovers governing equations of machining dynamics using mechanics-informed machine learning. *Authors, arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2501.14817)]
- **Deep Neural Implicit Representation of Accessibility for Multi-Axis Manufacturing** — Encodes tool accessibility as a deep implicit representation for multi-axis machining planning. *Authors, Computer-Aided Design 2024*. [[Paper](https://arxiv.org/abs/2409.02115)]
- **Automatic Feature Recognition and Dimensional Attributes Extraction From CAD Models for Hybrid Additive-Subtractive Manufacturing** — Extracts manufacturing features and dimensions from CAD models for hybrid manufacturing workflows. *Authors, arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2408.06891)]
- **BrepMFR: Enhancing Machining Feature Recognition in B-rep Models through Deep Learning and Domain Adaptation** — Combines deep learning with domain adaptation to recognize machining features in B-rep CAD models. *Zhang et al., Computer Aided Geometric Design 2024*. [[Paper](https://doi.org/10.1016/j.cagd.2024.102318)]
- **BRepGAT: Graph Neural Network to Segment Machining Feature Faces in a B-rep Model** — Uses graph attention networks to segment machining feature faces directly from B-rep models. *Authors, ResearchGate / Journal 2024*. [[Paper](https://www.researchgate.net)]
- **Real-Time Tool-Path Planning Using Deep Learning for Subtractive Manufacturing** — Proposes a deep learning approach for real-time tool-path planning in subtractive manufacturing. *Authors, ResearchGate / Journal 2024*. [[Paper](https://www.researchgate.net)]
- **Large Language Models for Manufacturing** — Explores applications of large language models to manufacturing processes and decision-making. *Yixin Tian et al., arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2410.21418)]
- **Co-Optimization of Tool Orientations, Kinematic Redundancy, and Waypoint Timing for Robot-Assisted Manufacturing** — Jointly optimizes tool orientations, redundancy resolution, and timing for robotic machining paths. *Authors, arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2409.13448)]
- **Learning-Based Toolpath Planner on Diverse Graphs for 3D Printing** — Learns toolpath planning strategies over graph representations for additive manufacturing. *Yuming Huang et al., arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2408.09198)]
- **Reinforcement Learning-Based Cutting Parameter Dynamic Decision Method Considering Tool Wear for a Turning Machining Process** — Applies reinforcement learning to dynamically adjust cutting parameters accounting for tool wear. *Authors, International Journal of Precision Engineering and Manufacturing-Green Technology 2023*. [[Paper](https://doi.org/10.1007/s40684-023-00517-w)]
- **Making Informed Decisions in Cutting Tool Maintenance in Milling** — Proposes a data-driven framework for predictive cutting tool maintenance decisions in milling. *Authors, arXiv preprint 2023*. [[Paper](https://arxiv.org/abs/2310.14629)]
- **Data-driven Modelling of Machine Tool Feedrate Behavior with Neural Networks** — Models CNC machine tool feedrate behavior using neural networks for improved toolpath prediction. *Authors, arXiv preprint 2021*. [[Paper](https://arxiv.org/abs/2106.09719)]

---

## Challenges and Future Directions

Papers analyzing open problems, technical challenges, and long-term research directions for AI in CAD.

### Data and Representation Challenges

- **DreamCAD** — Scales multi-modal CAD generation using differentiable parametric surface representations. *Khan et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.05607)]
- **CADEvolve** — Creates realistic CAD models through iterative program evolution strategies. *Elistratov et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.16317)]
- **Learning From Design Procedure** — Generates CAD programs by mimicking human design procedures for data augmentation. *Chen et al., NeurIPS 2025 Workshop*. [[Paper](https://arxiv.org/abs/2603.06894)]
- **GenCAD-3D** — Aligns multimodal latent spaces and balances synthetic datasets for CAD program generation. *Yu et al., ASME J. Mechanical Design 2025*. [[Paper](https://arxiv.org/abs/2509.15246)]
- **CADmium** — Fine-tunes code language models for text-driven sequential CAD design generation. *Govindarajan et al., TMLR 2026*. [[Paper](https://arxiv.org/abs/2507.09792)]

### Technical Challenges

- **Mamba-CAD** — Applies state space models to efficient autoregressive 3D CAD sequence generation. *Li et al., AAAI 2025*. [[Paper](https://arxiv.org/abs/2603.00439)]
- **GeoFusion-CAD** — Combines geometric state space modeling with diffusion for structure-aware parametric 3D design. *Zhou et al., CVPR 2026*. [[Paper](https://arxiv.org/abs/2603.21978)]
- **ArtiCAD** — Generates articulated CAD assemblies through multi-agent collaborative code generation. *Shui et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.10992)]
- **MamTiff-CAD** — Integrates Mamba and multi-scale latent diffusion for complex parametric CAD sequences. *Deng et al., ICCV 2025*. [[Paper](https://arxiv.org/abs/2511.17647)]
- **Aligning Constraint Generation with Design Intent in Parametric CAD** — Aligns geometric constraint generation with user design intent in parametric modeling. *Casey et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2504.13178)]
- **RLCAD** — Provides a reinforcement learning gym for CAD command sequences involving revolution operations. *Yin et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.18549)]

### Engineering and Deployment Challenges

- **neuralCAD-Edit: An Expert Benchmark for Multimodal-Instructed 3D CAD Model Editing** — Introduces a benchmark for evaluating multimodal-instructed editing of 3D CAD models. *Perrett et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.16170)]
- **Toward AI-driven Multimodal Interfaces for Industrial CAD Modeling** — Explores multimodal interface design combining speech, gesture, and vision for industrial CAD workflows. *Choi et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.16824)]
- **From Intent to Execution: Multimodal Chain-of-Thought Reinforcement Learning for Precise CAD Code Generation** — Applies chain-of-thought reinforcement learning to translate multimodal intent into precise CAD code. *Niu et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.10118)]

### Ecosystem Challenges

- **Human-in-the-Loop: Quantitative Evaluation of 3D Models Generation by Large Language Models** — Proposes a human-in-the-loop framework for quantitatively evaluating LLM-generated 3D models. *Sadik et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.07010)]
- **3DGen-Bench: Comprehensive Benchmark Suite for 3D Generative Models** — Introduces a comprehensive benchmark suite for systematically evaluating 3D generative models. *Zhang et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.21745)]

### Near-Term Directions

- **Agent-Aided Design for Dynamic CAD Models** — Introduces an LLM agent framework that interactively modifies parametric CAD models through natural language. *Adler et al., CAIS 2026*. [[Paper](https://arxiv.org/abs/2604.15184)]
- **BrepCoder: A Unified Multimodal Large Language Model for Multi-task B-rep Reasoning** — Unifies multiple B-rep understanding and generation tasks within a single multimodal LLM. *Kim et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.22284)]
- **cadrille: Multi-modal CAD Reconstruction with Online Reinforcement Learning** — Applies online reinforcement learning to reconstruct CAD models from multi-modal inputs. *Kolodiazhnyi et al., ICLR 2026 (Oral)*. [[Paper](https://arxiv.org/abs/2505.22914)]
- **CADFusion: Text-to-CAD Generation Through Infusing Visual Feedback in Large Language Models** — Generates CAD models from text by infusing iterative visual feedback into LLMs. *Wang et al., ICML 2025*. [[Paper](https://arxiv.org/abs/2501.19054)]
- **CAD-GPT: Synthesising CAD Construction Sequence with Spatial Reasoning-Enhanced Multimodal LLMs** — Synthesizes CAD construction sequences using spatially-enhanced multimodal LLM reasoning. *Wang et al., AAAI 2025*. [[Paper](https://arxiv.org/abs/2412.19663)]
- **CADDreamer: CAD Object Generation from Single-view Images** — Generates editable CAD objects from a single RGB image via generative modeling. *Li et al., CVPR 2025*. [[Paper](https://arxiv.org/abs/2502.20732)]
- **CAD-Assistant: Tool-Augmented VLLMs as Generic CAD Task Solvers** — Augments vision-language models with CAD tools to solve diverse CAD tasks generically. *Mallis et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2412.13810)]

### Mid-Term Directions

- **VideoCAD: A Dataset and Model for Learning Long-Horizon 3D CAD UI Interactions from Video** — Introduces a dataset and model for learning extended CAD modeling sequences from video demonstrations. *Man et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.24838)]
- **QueryCAD: Grounded Question Answering for CAD Models** — Proposes a grounded question-answering framework that reasons over 3D CAD model geometry and structure. *Kienle et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2409.08704)]

### Long-Term Vision

- **The Dawn of Agentic EDA: A Survey of Autonomous Digital Chip Design** — Surveys autonomous agent-based approaches to electronic design automation for digital chips. *Zang et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.23189)]
- **Intelligent CAD 2.0** — Proposes a long-term vision for next-generation intelligent computer-aided design systems. *Zou et al., Visual Informatics 2024*. [[Paper](https://arxiv.org/abs/2410.03759)]

---

## Datasets and Benchmarks

Major datasets and benchmarks used across the AI for CAD research community.

### Dataset Papers

- **Zero-to-CAD: Agentic Synthesis of Interpretable CAD Programs at Million-Scale Without Real Data** — Synthesizes a million-scale dataset of interpretable CAD programs using agentic methods without real data. *Willis et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.24479)]
- **Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding** — Benchmarks multimodal models on their ability to understand architectural and engineering drawings. *Zhang et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.04819)]
- **Geometrically Constrained Parametric History-based CAD Dataset** — Introduces a CAD dataset with geometric constraints and parametric modeling history. *Authors et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2602.19171)]
- **Objaverse++: Curated 3D Object Dataset with Quality Annotations** — Provides a curated large-scale 3D object dataset enhanced with quality annotations. *Authors et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2504.07334)]
- **An Open Large-Scale Architectural CAD Dataset and New Baseline for Panoptic Symbol Spotting** — Releases a large-scale architectural CAD dataset with baselines for panoptic symbol spotting. *Luo et al., NeurIPS 2025*. [[Paper](https://arxiv.org/abs/2503.22346)]
- **Enginuity: Building an Open Multi-Domain Dataset of Complex Engineering Diagrams** — Builds an open multi-domain dataset of complex engineering diagrams for diagram understanding. *Authors et al., NeurIPS 2025*. [[Paper](https://arxiv.org/abs/2601.13299)]
- **VideoCAD: A Large-Scale Video Dataset for Learning UI Interactions and 3D Reasoning from CAD Software** — Presents a large-scale video dataset capturing UI interactions and 3D reasoning in CAD software. *Lambourne et al., NeurIPS 2025*. [[Paper](https://arxiv.org/abs/2505.24838)]
- **SldprtNet: A Large-Scale Multimodal Dataset for CAD Generation in Language-Driven 3D Design** — Introduces a large-scale multimodal dataset linking natural language to CAD model generation. *Guo et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2603.13098)]
- **A Cascade MAR with Topology Predictor for Multimodal Conditional CAD Generation** — Introduces a cascade masked autoregressive model with topology prediction for multimodal CAD generation. *Wang et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2504.20830)]
- **mrCAD: Multimodal Refinement of Computer-aided Designs** — Presents a dataset and benchmark for iterative multimodal refinement of CAD designs. *McCarthy et al., EMNLP 2025 Findings*. [[Paper](https://arxiv.org/abs/2504.20294)]
- **Reinforcement Learning Training Gym for Revolution Involved CAD Command Sequence Generation** — Provides an RL training environment for generating CAD command sequences involving revolution operations. *Yin et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.18549)]
- **Synthetic Generation Tool of Digital Measurement Device CAD Model Datasets for Fine-tuning Large Vision-Language Models** — Proposes a synthetic data generation tool for measurement device CAD models to fine-tune VLMs. *Authors et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.21732)]
- **A Large-Scale CAD Drawings Dataset and New Baseline for Panoptic Symbol Spotting** — Releases a large-scale CAD drawing dataset with baselines for panoptic symbol spotting. *Wang et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.22346)]
- **IEC3D-AD: A 3D Dataset of Industrial Equipment Components for Unsupervised Point Cloud Anomaly Detection** — Introduces a 3D industrial equipment component dataset for unsupervised point cloud anomaly detection. *Wang et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.03267)]
- **CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM** — Unifies multimodal-conditioned CAD generation within a single multimodal large language model framework. *Xu et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2411.04954)]
- **Text2CAD: Generating Sequential CAD Models from Beginner-to-Expert Level Text Prompts** — Presents a dataset and method for generating sequential CAD models from varied-difficulty text prompts. *Khan et al., NeurIPS 2024 Spotlight*. [[Paper](https://arxiv.org/abs/2409.17106)]
- **Slice-100K: A Multimodal Dataset for Extrusion-based 3D Printing** — Provides 100K sliced 3D printing files with multimodal annotations for manufacturing research. *Authors et al., NeurIPS 2024 D&B Track*. [[Paper](https://arxiv.org/abs/2407.04180)]
- **From Engineering Diagrams to Graphs** — Converts engineering diagrams into structured graph representations for automated understanding. *Chen et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2411.13929)]
- **Objaverse: A Universe of Annotated 3D Objects** — Presents a large-scale dataset of 800K+ annotated 3D objects for vision and language tasks. *Deitke et al., CVPR 2023*. [[Paper](https://arxiv.org/abs/2212.08051)]
- **Objaverse-XL: A Universe of 10M+ 3D Objects** — Scales 3D object datasets to over 10 million objects sourced from diverse repositories. *Deitke et al., NeurIPS 2023*. [[Paper](https://arxiv.org/abs/2307.05663)]
- **DeepPatent2: A Large-Scale Benchmarking Corpus for Technical Drawing Understanding** — Offers a large-scale patent drawing benchmark for technical illustration recognition and retrieval. *Kucer et al., Scientific Data 2023*. [[Paper](https://arxiv.org/abs/2311.04098)]
- **FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting** — Introduces a large-scale floorplan CAD dataset with panoptic-level symbol annotations. *Fan et al., ICCV 2021 / TPAMI 2022*. [[Paper](https://arxiv.org/abs/2105.07147)]
- **DeepCAD: A Deep Generative Network for Computer-Aided Design Models** — Introduces a dataset and generative model for CAD command sequence generation. *Wu et al., ICCV 2021*. [[Paper](https://arxiv.org/abs/2105.09492)]
- **Fusion 360 Gallery: A Dataset and Environment for Programmatic CAD Construction from Human Design Sequences** — Provides real human CAD design sequences from Autodesk Fusion 360 for reconstruction research. *Willis et al., SIGGRAPH 2021*. [[Paper](https://arxiv.org/abs/2010.02392)]
- **AutoMate: A Dataset and Learning Approach for Automatic Mating of CAD Assemblies** — Provides a dataset and methods for predicting mate constraints in CAD assemblies. *Jones et al., SIGGRAPH 2021*. [[Paper](https://arxiv.org/abs/2105.12238)]
- **Synthetic 3D Data Generation Pipeline for Geometric Deep Learning in Architecture** — Presents a pipeline for generating synthetic 3D architectural data for deep learning. *Stojanovic et al., arXiv 2021*. [[Paper](https://arxiv.org/abs/2104.12564)]
- **SketchGraphs: A Large-Scale Dataset for Modeling Relational Geometry in Computer-Aided Design** — Offers a large-scale dataset of parametric CAD sketches with geometric and constraint graphs. *Seff et al., ICML 2020 Workshop*. [[Paper](https://arxiv.org/abs/2007.08506)]
- **A Large-Scale Annotated Mechanical Components Benchmark for Classification and Retrieval Tasks with Deep Neural Networks** — Introduces an annotated benchmark of mechanical components for 3D classification and retrieval. *Kim et al., ECCV 2020*. [[Paper](https://doi.org/10.1007/978-3-030-58523-5_11)]
- **MFCAD: A Dataset of 3D CAD Models with Machining Feature Labels** — Provides labeled CAD models annotated with machining feature types for recognition tasks. *Cao et al., CAD Journal 2020*. [[Paper](https://github.com/hducg/MFCAD)]
- **ABC: A Big CAD Model Dataset For Geometric Deep Learning** — Offers one million CAD models with ground-truth geometry for geometric deep learning. *Koch et al., CVPR 2019*. [[Paper](https://arxiv.org/abs/1812.06216)]
- **ShapeNet: An Information-Rich 3D Model Repository** — Provides a richly annotated large-scale repository of 3D shapes organized by WordNet taxonomy. *Chang et al., arXiv 2015*. [[Paper](https://arxiv.org/abs/1512.03012)]
- **3D ShapeNets: A Deep Representation for Volumetric Shapes** — Introduces a large-scale 3D shape dataset and a deep volumetric representation for recognition. *Wu et al., CVPR 2015*. [[Paper](https://arxiv.org/abs/1406.5670)]
- **SESYD: A Synthetic Document Database for Performance Evaluation** — Provides synthetic engineering drawing symbols and diagrams for document recognition benchmarking. *Delalandre et al., DAS 2010*. [[Paper](https://doi.org/10.1007/s10032-010-0120-x)]
- **CADFS: A Big CAD Program Dataset and Framework for Computer-Aided Design with Large Language Models** — Provides a large CAD-program dataset and framework enabling vision-language models to generate complex design histories. *Pyatov et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2605.01925)]

### Evaluation Metrics

- **Quantitative Evaluation of 3D Models Generation by Large Language Models** — Proposes quantitative metrics to assess quality of 3D models generated by LLMs. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.07010)]
- **CAD-Judge: Toward Efficient Morphological Grading and Verification for Text-to-CAD Generation** — Introduces an automated judge for morphological grading and verification of text-to-CAD outputs. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.04002)]
- **Generating CAD Code with Vision-Language Models for 3D Designs** — Leverages vision-language models to generate CAD code and evaluates output fidelity. *Authors, ICLR 2025*. [[Paper](https://arxiv.org/abs/2410.05340)]
- **Advancing 3D Generation Evaluation with Hierarchical Validity** — Proposes a hierarchical validity framework for more fine-grained 3D generation evaluation. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.05609)]
- **CadVLM: Bridging Language and Vision in the Generation of Parametric CAD Sketches** — Bridges language and vision modalities to generate and evaluate parametric CAD sketches. *Authors, arXiv 2024*. [[Paper](https://arxiv.org/abs/2409.17457)]

### Benchmark Challenges

- **CAD Arena: Open Benchmark for AI-Generated Parametric CAD** — Provides an open platform for evaluating and comparing AI-generated parametric CAD models. *CAD Arena Team, Online Platform 2025*.
- **State Space Model For 3D Computer-Aided Design Generative Modeling** — Applies state space models to generative modeling of 3D CAD sequences. *Authors, arXiv 2025*. [[Paper](https://arxiv.org/abs/2603.00439)]
- **BlenderLLM: Training Large Language Models for Computer-Aided Design with Self-improvement** — Trains LLMs for CAD generation using a self-improvement learning framework. *Authors, arXiv 2024*. [[Paper](https://arxiv.org/abs/2412.14203)]
- **Geometric Deep Learning for Computer-Aided Design: A Survey** — Surveys geometric deep learning techniques applied to CAD representation and generation. *Lambourne et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2402.17695)]
- **MUSE: Benchmarking Manufacturable, Functional, and Assemblable Text-to-CAD Generation** — Benchmarks text-to-CAD on manufacturability, functionality, and assemblability for industrial product design. *Dong et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2605.28579)]
- **Text2CAD-Bench: A Benchmark for LLM-based Text-to-Parametric CAD Generation** — Benchmarks LLM-based generation of parametric CAD models from natural language. *Wang et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2605.18430)]
- **Text-to-CAD Evaluation with CADTests** — Introduces CADTests, a functional test-based evaluation protocol for text-to-CAD generation. *Mallis et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2605.07807)] [[Code](https://github.com/dimitrismallis/CADTestBench)]
- **BenchCAD: A Comprehensive, Industry-Standard Benchmark for Programmatic CAD** — Benchmarks programmatic CAD code generation from visual or textual inputs against industry standards. *Zhang et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2605.10865)]

---

## Tools and Platforms

### Commercial CAD with AI Features

- **Dassault Systemes Virtual Companions** — Introduces AI-powered expert assistants on the 3DEXPERIENCE platform for industrial workflows. *Dassault Systemes, Technical Platform 2026*. [[Paper](https://www.3ds.com/newsroom/press-releases/dassault-systemes-unveils-new-way-working-industry-ai-powered-virtual-companions)]
- **AI-Assisted Analysis and Synthesis of Engineering Systems from Multimodal Engineering Data** — Proposes AI methods to analyze and synthesize engineering systems from multimodal data sources. *H. Sinan Bank, Daniel R. Herber, IISE 2026*. [[Paper](https://arxiv.org/abs/2603.00251)]
- **Large Language Models for Computer-Aided Design: A Survey** — Surveys applications of large language models across CAD tasks and workflows. *Zhang et al., arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2505.08137)]
- **A Multidisciplinary Design and Optimization (MDO) Agent Driven by Large Language Models** — Proposes an LLM-driven agent for automated multidisciplinary design optimization. *Guo et al., arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2511.17511)]
- **Automated CAD Modeling Sequence Generation from Text Descriptions via Transformer-Based Large Language Models** — Generates CAD modeling operation sequences from natural language descriptions using transformers. *Liao et al., arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2505.19490)]
- **AI-Driven Digital Twins for Manufacturing** — Reviews AI-driven digital twin approaches across hierarchical manufacturing system levels. *Nguyen et al., Sensors 2025*. [[Paper](https://doi.org/10.3390/s26010124)]
- **Autodesk Neural CAD** — Presents 3D generative AI foundation models for design-to-make workflows. *Autodesk, Technical Report 2025*. [[Paper](https://www.autodesk.com/solutions/autodesk-ai/neural-technology)]
- **Siemens Design Copilot NX** — Provides an AI copilot for product engineering within the NX CAD environment. *Siemens Digital Industries Software, Technical Platform 2025*. [[Paper](https://news.siemens.com/en-us/siemens-designcenter-nx-summer-2025/)]
- **Siemens Digital Twin Composer for Industrial Metaverse Digital Twins** — Platform enabling creation of interactive digital twins for industrial metaverse applications. *Siemens Digital Industries Software, Technical Platform 2026*. [[Paper](https://news.siemens.com/en-us/digital-twin-composer-ces-2026/)]
- **A Survey of AI Methods for Geometry Preparation and Mesh Generation in Engineering Simulation** — Surveys AI techniques for automating geometry cleanup and mesh generation in CAE workflows. *Steven Owen, Nathan Brown, Nikos Chrisochoides et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.23719)]
- **MotionAnymesh: Physics-Grounded Articulation for Simulation-Ready Digital Twins** — Generates physically plausible articulated motion for mesh models to create simulation-ready digital twins. *WenBo Xu, Liu Liu, Li Zhang et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.12936)]
- **NVIDIA Omniverse Blueprint for Real-Time Computer-Aided Engineering Digital Twins** — Blueprint for building real-time physics-based digital twins integrated with CAE software. *NVIDIA, Technical Platform 2024*. [[Paper](https://nvidianews.nvidia.com/news/nvidia-announces-omniverse-real-time-physics-digital-twins-with-industry-software-leaders)]
- **A Survey on AI-Driven Digital Twins in Industry 4.0: Smart Manufacturing and Advanced Robotics** — Surveys AI-driven digital twin approaches for smart manufacturing and robotics applications. *Huang et al., Sensors 2021*. [[Paper](https://doi.org/10.3390/s21196340)]

### AI-Native CAD Platforms

- **Neural Concept: Physics- and Geometry-Aware AI Design Copilot for Engineering** — Accelerates engineering design with AI that understands physical constraints and 3D geometry. *Neural Concept, Technical Platform 2025*.
- **Adam: AI-Native CAD Platform for Text-to-Parametric Design** — Generates editable parametric CAD models from natural language descriptions. *Adam (YC W25), Technical Platform 2025*.
- **Leo AI: Large Mechanical Model for CAD-Aware Engineering Assistance** — Applies a domain-specific large model to assist mechanical engineers within CAD environments. *Leo AI, Technical Platform 2025*.
- **Zoo.dev Text-to-CAD: Parametric CAD Generation via KCL Programming Language** — Converts text prompts into parametric CAD geometry using a code-first modeling language. *Zoo (formerly KittyCAD), Technical Platform 2024*.
- **MecAgent: AI Copilot for Mechanical CAD Software Automation** — Automates repetitive mechanical CAD tasks through an AI-driven copilot interface. *MecAgent, Technical Platform 2024*.
- **Luminary Cloud: Physics AI Factory for Real-Time Engineering Simulation** — Delivers GPU-accelerated physics simulation for real-time engineering design exploration. *Luminary Cloud, Technical Platform 2024*.

### Open-Source Tools and Frameworks

- **TOOLCAD** — Leverages tool-using LLMs with reinforcement learning for text-to-CAD generation. *Gong et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.07960)]
- **Clarify Before You Draw** — Introduces proactive agents that ask clarifying questions for robust text-to-CAD generation. *Yuan et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.03045)]
- **PLLM** — Proposes pseudo-labeling large language models for CAD program synthesis. *Li et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.12561)]
- **Procedural 3D Generation with LLMs** — Enables parametric editing and procedural generation of 3D shapes via large language models. *Fadlullah Raji, Stefano Petrangeli, Matheus Gadelha et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.12234)]
- **From Idea to CAD** — Presents a language model-driven multi-agent system for collaborative CAD design. *Ocker et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.04417)]
- **Text-to-CadQuery** — Proposes a new paradigm for CAD generation using scalable large model capabilities. *Xie and Ju, arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.06507)]
- **CAD-Coder** — An open-source vision-language model for generating computer-aided design code. *Doris et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.14646)]
- **CADDesigner** — General-purpose agent for conceptual CAD model generation from high-level design intent. *Fan, Ni, Yin et al., arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2508.01031)]
- **Generative AI for CAD Automation** — Leverages large language models to automate 3D modelling workflows in CAD. *Kumar et al., arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2508.00843)]
- **CAD-Llama** — Leverages large language models for parametric 3D CAD model generation from text. *Li et al., arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2505.04481)]
- **Text-to-CAD Generation** — Infuses visual feedback into large language models for text-to-CAD generation. *Wang et al., arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2501.19054)]
- **Autodesk and Model Context Protocol** — Makes MCP enterprise-ready for connecting AI agents to CAD design data. *Autodesk, Technical Blog 2025*. [[Paper](https://www.autodesk.com/autodesk-university/class/Equip-AI-with-Access-to-Your-Design-Data-and-Projects-Model-Context-Protocol-Autodesk-Platform-Services-2025)]
- **FreecadMCP** — Model Context Protocol server enabling AI-driven parametric design in FreeCAD. *bonninr (open-source), GitHub 2025*. [[Paper](https://github.com/bonninr/freecad_mcp)]
- **CAD Skills** — Agent skills framework for parametric CAD generation via the build123d library. *earthtojake (open-source), GitHub 2025*. [[Paper](https://github.com/earthtojake/text-to-cad)]
- **CADAM** — Open-source text-to-CAD web application powered by OpenSCAD-WASM. *Adam-CAD (open-source), GitHub 2026*. [[Paper](https://github.com/Adam-CAD/CADAM)]
- **HiCAD** — Parametric 3D CAD modeling platform integrating JSCAD with multi-LLM support for AI-driven design. *MrXujiang, GitHub 2025*. [[Paper](https://github.com/MrXujiang/HiCAD)]
- **CQAsk** — LLM-powered CAD generation tool that produces 3D models using CadQuery from natural language. *OpenOrion, GitHub 2024*. [[Paper](https://github.com/OpenOrion/CQAsk)]
- **multiCAD-mcp** — MCP server enabling AI assistants to control AutoCAD, ZWCAD, and BricsCAD simultaneously. *AnCode666, GitHub 2025*. [[Paper](https://github.com/AnCode666/multiCAD-mcp)]
- **CAD Agent** — AI-driven CAD modeling agent with visual feedback loop using build123d and MCP. *Svetlana-DAO-LLC, GitHub 2025*. [[Paper](https://github.com/Svetlana-DAO-LLC/cad-agent)]
- **gNucleus Text-to-CAD MCP** — MCP server for generating CAD parts and assemblies from text descriptions. *gNucleus, GitHub 2025*. [[Paper](https://github.com/gNucleus/text-to-cad-mcp)]
- **cadquery-mcp-server** — MCP server for generating and verifying CAD models through CadQuery with automated validation. *Rishi Gundakaram, GitHub 2025*. [[Paper](https://github.com/rishigundakaram/cadquery-mcp-server)]
- **FreeCAD MCP** — Model Context Protocol server for FreeCAD with integrated finite element analysis support. *neka-nat, GitHub 2025*. [[Paper](https://github.com/neka-nat/freecad-mcp)]
- **Dingcad** — Live-reload CAD scripting environment combining ManifoldCAD geometry kernel with QuickJS runtime. *yacineMTB, GitHub 2025*. [[Paper](https://github.com/yacineMTB/dingcad)]
- **OpenSCAD Agent** — Claude Code-powered agent that generates 3D-printable designs through natural language to OpenSCAD code. *iancanderson, GitHub 2025*. [[Paper](https://github.com/iancanderson/openscad-agent)]
- **CodeToCAD** — Vendor-agnostic framework enabling code-based CAD automation across multiple modeling backends. *CodeToCAD, GitHub 2024*. [[Paper](https://github.com/CodeToCAD/CodeToCAD)]
- **Curated Code CAD** — Comprehensive curated list of code-based CAD tools, languages, and frameworks. *Irev-Dev, GitHub 2024*. [[Paper](https://github.com/Irev-Dev/curated-code-cad)]
- **The Power of Small LLMs in Geometry Generation for Physical Simulations** — Demonstrates small language models can effectively generate geometry for physical simulation workflows. *Ossama Shafiq, Bahman Ghiassi, Alessio Alexiadis, arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.18178)]
- **DreamCAD** — Scales multi-modal CAD generation using differentiable parametric surface representations. *Mohammad Sadil Khan, Muhammad Usama, Rolandos Alexandros Potamias et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.05607)]
- **Towards High-Fidelity CAD Generation** — Combines LLM-driven program generation with text-based B-Rep primitive grounding for precise CAD output. *Jiahao Li, Qingwang Zhang, Qiuyu Chen et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.11831)]
- **Generating Human-AI Collaborative Design Sequence for 3D Assets** — Proposes differentiable operation graphs to model human-AI collaborative 3D design sequences. *Xiaoyang Huang, Bingbing Ni, Wenjun Zhang, arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.17645)]
- **A Solver-Aided Hierarchical Language for LLM-Driven CAD Design** — Introduces a solver-aided hierarchical language enabling LLMs to produce constraint-satisfying CAD designs. *Benjamin T. Jones, Felix Hahnlein, Zihan Zhang et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2502.09819)]
- **Multimodal Chain-of-Thought Reinforcement Learning for Precise CAD Code Generation** — Combines multimodal reasoning with reinforcement learning to improve precision of generated CAD code. *Ke Niu, Haiyang Yu, Zhuofan Chen et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.10118)]
- **Generative Parametric Design: A Framework for Real-time Geometry Generation and On-the-fly Multiparametric Approximation** — Proposes a framework for real-time parametric geometry generation with on-the-fly multiparametric approximation. *Mohammed El Fallaki Idrissi, Jad Mounayer, Sebastian Rodriguez et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.11748)]
- **Designing a Human-AI Collaborative Ideation System for Concept Designers** — Presents a human-AI collaborative system supporting concept designers during early-stage ideation. *Wen-Fan Wang, Chien-Ting Lu, Nil Ponsa Campanya et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2502.14747)]
- **Query2CAD: Generating CAD models using natural language queries** — Generates CAD models directly from natural language queries via a language-driven pipeline. *Badagabettu et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2406.00144)]
- **CADCodeVerify: Generating CAD Code with Vision-Language Models for 3D Designs** — Uses vision-language models to generate and verify CAD code for 3D designs. *Alrashedy et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2410.05340)]
- **CADgpt: Harnessing Natural Language Processing for 3D Modelling to Enhance Computer-Aided Design Workflows** — Applies natural language processing to streamline 3D modelling within CAD workflows. *Timo Kapsalis, arXiv 2024*. [[Paper](https://arxiv.org/abs/2401.05476)]
- **Experiments on Generative AI-Powered Parametric Modeling and BIM for Architectural Design** — Explores generative AI for parametric modeling and BIM in architectural design workflows. *Jaechang Ko, John Ajibefun, Wei Yan, arXiv 2023*. [[Paper](https://arxiv.org/abs/2308.00227)]

### Research on AI Tools and Deployment

- **Supervising Ralph Wiggum: Exploring a Metacognitive Co-Regulation Agentic AI Loop for Engineering Design** — Explores a metacognitive co-regulation loop for supervising agentic AI in engineering design tasks. *Xu et al., arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.24768)]
- **Is Academia Catching Up with Industry Demands? AI for CAE User Experience -- A Multivocal Literature Review** — Multivocal literature review comparing academic and industry perspectives on AI for CAE user experience. *Authors et al., arXiv 2025*. [[Paper](https://arxiv.org/abs/2507.16586)]
- **Beyond Development: Challenges in Deploying Machine Learning Models for Structural Engineering Applications** — Identifies challenges in deploying ML models for real-world structural engineering applications. *Zaker Esteghamati et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2404.12544)]
- **Naming the Pain in Machine Learning-Enabled Systems Engineering** — Categorizes pain points encountered when integrating machine learning into systems engineering workflows. *Kalinowski et al., arXiv 2024*. [[Paper](https://arxiv.org/abs/2406.04359)]
- **Towards a Framework for Deep Learning Certification in Safety-Critical Applications Using Inherently Safe Design and Run-Time Error Detection** — Proposes a certification framework combining inherently safe design with runtime error detection for deep learning. *Valentin, arXiv 2024*. [[Paper](https://arxiv.org/abs/2403.14678)]
- **Artificial Intelligence for Safety-Critical Systems in Industrial and Transportation Domains: A Survey** — Surveys AI methods and challenges for safety-critical systems in industrial and transportation domains. *Nascimento et al., ACM Computing Surveys 2023*. [[Paper](https://doi.org/10.1145/3626314)]
- **Challenges in Deploying Machine Learning: A Survey of Case Studies** — Surveys real-world case studies to identify recurring challenges in deploying machine learning systems. *Paleyes et al., ACM Computing Surveys 2022*. [[Paper](https://doi.org/10.1145/3533378)]

---

## Contributing

Contributions are welcome. To add a paper or resource:

1. Fork this repository
2. Add the entry in the appropriate section, following the existing format
3. Ensure the paper link is valid (use arXiv links when available)
4. Run `python3 scripts/validate_catalog.py`
5. Submit a pull request with a brief description

Please ensure entries are:
- Placed in the correct thematic section
- Sorted by year (newest first) within each subsection
- Formatted consistently with existing entries

For questions or suggestions, please open an issue.

## Maintenance

Run the catalog validator before submitting maintenance changes:

```bash
python3 scripts/validate_catalog.py
```

## Catalog Metadata

This repository intentionally separates three denominators:

| Denominator | Current Count | Source |
|---|---:|---|
| Markdown catalog entries | 709 | `README.md` list entries |
| Deduplicated registry records | 638 | `research/papers/*.jsonl` |
| Registry records dated 2024-2026 | 496 | `research/papers/*.jsonl` |

Use these terms explicitly when citing counts. Do not collapse them into an undefined "papers" total.

For the current catalog-entry confidence review, see
[catalog_entry_audit_summary_2026-05-15.md](research/catalog_audit/catalog_entry_audit_summary_2026-05-15.md).

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
