<!--
repo: awesome-ai4cad
scope: AI methods for Computer-Aided Design (2018-2026)
catalog_entries: 709
deduplicated_registry_records: 638
registry_records_2024_2026: 496
entry_format: "Markdown list item with title, authors, venue/year, and Paper URL"
validation: "python3 scripts/validate_catalog.py"
-->

# Awesome AI for CAD [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated catalog of papers, datasets, and resources on AI for Computer-Aided Design.

![Catalog](https://img.shields.io/badge/Catalog-709_entries-blue)
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

- **3D Shape Generation: A Survey** - Nicolas Caytuiro, Ivan Sipiran. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2506.22678)]
- **A Survey on Deep Learning in 3D CAD Reconstruction** - Ruiquan Lin, Yonggang Ji, Wanting Ding et al. *Applied Sciences (MDPI) 2025*. [[Paper](https://doi.org/10.3390/app15126681)]
- **Advances in 3D Generation: A Survey** - Xiaoyu Li et al.. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2401.17807)]
- **Diffusion Models in 3D Vision: A Survey** - Zhen Wang et al.. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2410.04738)]
- **A Survey On Text-to-3D Contents Generation In The Wild** - Chenhan Jiang et al.. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2405.09431)]
- **Applications of Artificial Intelligence in the AEC Industry: A Review** - Huimin Li, Yafei Zhang, Yongchao Cao et al. *Journal of Asian Architecture and Building Engineering 2024*. [[Paper](https://doi.org/10.1080/13467581.2024.2343800)]
- **LLM4CAD: Multi-Modal Large Language Models for 3D Computer-Aided Design Generation** - Xingang Li, Yuewan Sun, Zhenghui Sha. *ASME IDETC-CIE 2024*. [[Paper](https://doi.org/10.1115/detc2024-143740)]

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

- **Multi-Scale Latent Diffusion with Mamba+ for Complex Parametric Sequence** - Liyuan Deng, Yunpeng Bai, Yongkang Dai et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.17647)]
- **CAD-Coder: Text-to-CAD Generation with Chain-of-Thought and Geometric Reward** - Yandong Guan, Xilin Wang, Ximing Xing et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.19713)]
- **An Open-Source Vision-Language Model for Computer-Aided Design Code Generation** - Anna C. Doris, Md Ferdous Alam, Amin Heyrani Nobari et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.14646)]
- **OpenECAD: An Efficient Visual Language Model for Editable 3D-CAD Design** - Zhe Yuan, Jianqi Shi, Yanhong Huang. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2406.09913)]
- **Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges** - Bronstein et al.. *arXiv / IEEE Signal Processing Magazine 2021*. [[Paper](https://arxiv.org/abs/2104.13478)]
- **Dynamic Graph CNN for Learning on Point Clouds** - Wang et al.. *ACM TOG 2019*. [[Paper](https://arxiv.org/abs/1801.07829)]
- **PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation** - Qi et al.. *CVPR 2017*. [[Paper](https://arxiv.org/abs/1612.00593)]
- **PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space** - Qi et al.. *NeurIPS 2017*. [[Paper](https://arxiv.org/abs/1706.02413)]

</details>

---

## CAD Representations and Foundations

Papers establishing core CAD representation paradigms (B-rep, CSG, sequence, code) that form the basis for generative and understanding methods.

**Representative anchors:** CSGNet for neural CSG parsing; BRepNet for topological message passing; SkexGen for disentangled CAD codebooks.

- **BRepFormer: AutoRegressive Generation with B-rep Holistic Token Sequence Representation** - Jiahao Li, Yunpeng Bai, Yongkang Dai et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.16771)]
- **Masked BRep Autoencoder via Hierarchical Graph Transformer** - Yifei Li, Kang Wu, Wenming Wu et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.14927)]
- **Iterative Program Editing for CAD Reverse Engineering** - Soslan Kabisov, Vsevolod Kirichuk, Andrey Volkov et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.29847)]
- **Text-to-CadQuery: A New Paradigm for CAD Generation with Scalable Large Model Capabilities** - Haoyang Xie, Feng Ju. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.06507)]
- **Towards Text-based CAD Prototyping via Modality-Specific Tokenization** - Ruiyu Wang, Shizhao Sun, Weijian Ma et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.21150)]
- **A Language Model-Driven Multi-Agent System for Collaborative Design** - Felix Ocker, Stefan Menzel, Ahmed Sadik et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.04417)]
- **Generating Constructive Solid Geometry Instead of Meshes by Fine-Tuning a Code-Generation LLM** - Maximilian Mews, Ansar Aynetdinov, Vivian Schiller et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2411.15279)]
- **HNC-CAD: Hierarchical Neural Coding for Controllable CAD Model Generation** - Xu et al.. *CVPR 2023*. [[Paper](https://arxiv.org/abs/2307.00149)]
- **D2CSG: Unsupervised Learning of Compact CSG Trees with Dual Complements and Dropouts** - Fenggen Yu, Qimin Chen, Maham Tanveer et al. *NeurIPS 2023*. [[Paper](https://arxiv.org/abs/2301.11497)]
- **Self-Supervised CAD Reconstruction by Learning Sketch-Extrude Operations** - Pu Li, Jianwei Guo, Xiaopeng Zhang et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2303.10613)]
- **SkexGen: Autoregressive Generation of CAD Construction Sequences with Disentangled Codebooks** - Xu et al.. *ICML 2022*. [[Paper](https://arxiv.org/abs/2207.04632)]
- **BRepNet: A Topological Message Passing System for Solid Models** - Lambourne et al.. *CVPR 2021 (Oral)*. [[Paper](https://arxiv.org/abs/2104.00706)]
- **UV-Net: Learning from Boundary Representations** - Jayaraman et al.. *CVPR 2021*. [[Paper](https://arxiv.org/abs/2006.10211)]
- **UCSG-Net: Unsupervised Discovering of Constructive Solid Geometry Tree** - Kania et al.. *NeurIPS 2020*. [[Paper](https://arxiv.org/abs/2006.09102)]
- **CSGNet: Neural Shape Parser for Constructive Solid Geometry** - Sharma et al.. *CVPR 2018*. [[Paper](https://arxiv.org/abs/1712.08290)]

---

## 2D CAD and Drawing Intelligence

AI methods for interpreting, analyzing, and generating 2D engineering drawings, floor plans, P&ID diagrams, and circuit schematics.

**Representative anchors:** SymPoint for panoptic symbol spotting; FloorPlanCAD for drawing datasets; GAT-CADNet for graph-based symbol detection.

### Symbol Detection and Spotting

- **ArchCAD-400K: A Large-Scale CAD Drawings Dataset and New Baseline for Panoptic Symbol Spotting** - Ruifeng Luo, Zhengjie Liu, Tianxiao Cheng et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.22346)]
- **Point or Line? Using Line-based Representation for Panoptic Symbol Spotting in CAD Drawings** - Xingguang Wei, Haomin Wang, Shenglong Ye et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.23395)]
- **Text-Enhanced Panoptic Symbol Spotting in CAD Drawings** - Xianlin Liu, Yan Gong, Bohao Li et al.. *BESC 2025*. [[Paper](https://arxiv.org/abs/2510.11091)]
- **Relative Drawing Identification Complexity is Invariant to Modality in Vision-Language Models** - Diogo Freitas, Brigt Havardstun, Cesar Ferri et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.10583)]
- **Architectural Practice Process and Artificial Intelligence -- An Evolving Practice** - Mustapha El Moussaoui. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2507.23653)]
- **Symbol as Points: Panoptic Symbol Spotting via Point-based Representation** - Wenlong Liu, Tianyu Yang, Yuhan Wang et al.. *ICLR 2024*. [[Paper](https://arxiv.org/abs/2401.10556)]
- **SymPoint Revolutionized: Boosting Panoptic Symbol Spotting with Layer Feature Enhancement** - Wenlong Liu, Tianyu Yang, Qizhi Yu et al.. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2407.01928)]
- **CADSpotting: Robust Panoptic Symbol Spotting on Large-Scale CAD Drawings** - Fuyi Yang, Jiazuo Mu, Yanshun Zhang et al.. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2412.07377)]
- **Generative AI in the Construction Industry: A State-of-the-art Analysis** - Ridwan Taiwo, Idris Temitope Bello, Sulemana Fatoama Abdulai et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2402.09939)]
- **Exploring Gen-AI applications in building research and industry: A review** - Hanlong Wan, Jian Zhang, Yan Chen et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2410.01098)]
- **GAT-CADNet: Graph Attention Network for Panoptic Symbol Spotting in CAD Drawings** - Zhaohua Zheng, Jianfang Li, Lingjie Zhu et al.. *arXiv 2022*. [[Paper](https://arxiv.org/abs/2201.00625)]
- **Automatic Detection and Classification of Symbols in Engineering Drawings** - Sourish Sarkar, Pranav Pandey, Sibsambhu Kar. *arXiv 2022*. [[Paper](https://arxiv.org/abs/2204.13277)]
- **Discovering Design Concepts for CAD Sketches** - Yuezhi Yang, Hao Pan. *NeurIPS 2022*. [[Paper](https://arxiv.org/abs/2210.14451)]
- **The Scope for AI-Augmented Interpretation of Building Blueprints in Commercial and Industrial Property Insurance** - Long Chen, Mao Ye, Alistair Milne et al. *arXiv 2022*. [[Paper](https://arxiv.org/abs/2205.01671)]
- **An Automated Engineering Assistant** - Dries Van Daele, Nicholas Decleyre, Herman Dubois et al. *arXiv 2019*. [[Paper](https://arxiv.org/abs/1909.08552)]

### Text and Annotation Extraction

- **Context-Aware Mapping of 2D Drawing Annotations to 3D CAD Features Using LLM-Assisted Reasoning for Manufacturing Automation** - Muhammad Tayyab Khan, Lequn Chen, Wenhe Feng et al.. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.18296)]
- **A Multi-Stage Hybrid Framework for Automated Interpretation of Multi-View Engineering Drawings Using Vision Language Model** - Muhammad Tayyab Khan, Zane Yong, Lequn Chen et al.. *ICIEA 2026*. [[Paper](https://arxiv.org/abs/2510.21862)]
- **Automated Parsing of Engineering Drawings for Structured Information Extraction Using a Fine-tuned Document Understanding Transformer** - Muhammad Tayyab Khan, Zane Yong, Lequn Chen et al.. *IEEE IEEM 2025*. [[Paper](https://arxiv.org/abs/2505.01530)]
- **A Hybrid Vision-Language Framework for Parsing 2D Engineering Drawings into Structured Manufacturing Knowledge** - Muhammad Tayyab Khan, Lequn Chen, Zane Yong et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2506.17374)]
- **Fine-Tuning Vision-Language Model for Automated Engineering Drawing Information Extraction** - Muhammad Tayyab Khan, Lequn Chen, Ye Han Ng et al.. *ICIAI 2025*. [[Paper](https://arxiv.org/abs/2411.03707)]

### Drawing Understanding and Benchmarks

- **AECV-Bench: Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding** - Aleksei Kondratenko, Mussie Birhane, Houssame E. Hsain et al.. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.04819)]
- **AEC-Bench: A Multimodal Benchmark for Agentic Systems in Architecture, Engineering, and Construction** - Harsh Mankodiya, Chase Gallik, Theodoros Galanos et al.. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.29199)]
- **BLUEPRINT Rebuilding a Legacy: Multimodal Retrieval for Complex Engineering Drawings and Documents** - Ethan Seefried, Ran Eldegaway, Sanjay Das et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.13345)]
- **Advancing Multimodal LLM Evaluation of Engineering Documentation with Enhanced Retrieval** - Kiarash Naghavi Khanghah, Hoang Anh Nguyen, Anna C. Doris et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.09552)]
- **Image-Based Structural Analysis Using Computer Vision and LLMs: PhotoBeamSolver** - Altamirano-Muniz Emilio Fernando. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.21432)]
- **Blueprint-Bench: Comparing Spatial Intelligence of LLMs, Agents and Image Models** - Lukas Petersson, Axel Backlund, Axel Wennstöm et al.. *Submitted to ICLR 2026*. [[Paper](https://arxiv.org/abs/2509.25229)]
- **AECBench: A Hierarchical Benchmark for Knowledge Evaluation of Large Language Models in the AEC Field** - Chen Liang, Zhaoqi Huang, Haofen Wang et al.. *Advanced Engineering Informatics 2025*. [[Paper](https://arxiv.org/abs/2509.18776)]
- **VectorGraphNET: Graph Attention Networks for Accurate Segmentation of Complex Technical Drawings** - Andrea Carrara, Stavros Nousias, André Borrmann. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2410.01336)]
- **DesignQA: A Multimodal Benchmark for Evaluating Large Language Models' Understanding of Engineering Documentation** - Anna C. Doris, Daniele Grandi, Ryan Tomich et al.. *ASME JCISE 2024*. [[Paper](https://arxiv.org/abs/2404.07917)]
- **Prediction of Visual Relations in Engineering Drawings** - Chao Gu, Ke Lin, Yiyang Luo et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2409.00909)]

### 2D-3D Annotation Mapping

- **Drawing2CAD: Sequence-to-Sequence Learning for CAD Generation from Vector Drawings** - Feiwei Qin, Shichao Lu, Junhao Hou et al.. *ACM MM 2025*. [[Paper](https://arxiv.org/abs/2508.18733)]
- **From 2D CAD Drawings to 3D Parametric Models: A Vision-Language Approach** - Xilin Wang, Jia Zheng, Yuanchao Hu et al. *AAAI 2025*. [[Paper](https://arxiv.org/abs/2412.11892)]

### Compliance Checking

- **Automated Facility Enumeration for Building Compliance Checking using Door Detection and Large Language Models** - Licheng Zhang, Bach Le, Naveed Akhtar et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.17283)]
- **Automatic Building Code Review** - Hanlong Wan, Weili Xu, Michael Rosenberg et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.02634)]
- **DRC-Coder: Automated DRC Checker Code Generation Using LLM Autonomous Agent** - Chen-Chia Chang, Chia-Tung Ho, Yaguang Li et al.. *ISPD 2025*. [[Paper](https://arxiv.org/abs/2412.05311)]
- **ARCEAK: An Automated Rule Checking Framework Enhanced with Architectural Knowledge** - Junyong Chen, Ling-I Wu, Minyu Chen et al.. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2501.14735)]
- **CODE-ACCORD: A Corpus of Building Regulatory Data for Rule Generation towards Automatic Compliance Checking** - Hansi Hettiarachchi, Amna Dridi, Mohamed Medhat Gaber et al.. *Scientific Data 2024*. [[Paper](https://arxiv.org/abs/2403.02231)]

### Floor Plan and Drawing Generation

- **Unified Vector Floorplan Generation via Markup Representation** - Kaede Shiohara, Toshihiko Yamasaki. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.04859)]
- **A Two-Level Codebook Based Network for End-to-End Vector Floorplan Generation** - Biao Xiong, Zhen Peng, Ping Wang et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.07100)]
- **HouseMind: Tokenization Allows Multimodal Large Language Models to Understand, Generate and Edit Architectural Floor Plans** - Sizhong Qin, Ramon Elias Weber, Xinzheng Lu. *CVPR 2026*. [[Paper](https://arxiv.org/abs/2603.11640)]
- **Controllable End-to-End Vector Floor Plan Generation** - Shidong Wang, Renato Pajarola. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.20377)]
- **Text-to-Layout: A Generative Workflow for Drafting Architectural Floor Plans Using LLMs** - Jayakrishna Duggempudi, Lu Gao, Ahmed Senouci et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.00543)]
- **Tokenizing Buildings: A Transformer for Layout Synthesis** - Manuel Ladron de Guevara, Jinmo Rhee, Ardavan Bidgoli et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.04832)]
- **Eliminating Rasterization: Direct Vector Floor Plan Generation with DiffPlanner** - Shidong Wang, Renato Pajarola. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.13738)]
- **Computer-Aided Layout Generation for Building Design: A Survey** - Jiachen Liu, Yuan Xue, Haomiao Ni et al. *Computational Visual Media 2025*. [[Paper](https://arxiv.org/abs/2504.09694)]
- **Text2MBL: Text-to-Code Generation for Modular Building Layouts in Building Information Modeling** - Yinyi Wei, Xiao Li. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.23713)]
- **Large Language Model Agent for Structural Drawing Generation Using ReAct Prompt Engineering and Retrieval Augmented Generation** - Xin Zhang, Lissette Iturburu, Juan Nicolas Villamizar et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2507.19771)]
- **Pro-DG: Procedural Diffusion Guidance for Architectural Facade Generation** - Aleksander Plocharski, Jan Swidzinski, Przemyslaw Musialski. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2504.01571)]
- **ChatHouseDiffusion: Prompt-Guided Generation and Editing of Floor Plans** - Sizhong Qin, Chengyu He, Qiaoyun Chen et al.. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2410.11908)]
- **HouseTune: Two-Stage Floorplan Generation with LLM Assistance** - Ziyang Zong, Guanying Chen, Zhaohuan Zhan et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2411.12279)]
- **GSDiff: Synthesizing Vector Floorplans via Geometry-enhanced Structural Graph Generation** - Sizhe Hu, Wenming Wu, Yuntao Wang et al.. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2408.16258)]
- **Generating Floorplans for Various Building Functionalities via Latent Diffusion Model** - Mohamed R. Ibrahim, Josef Musil, Irene Gallou. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2412.06859)]
- **Text2CAD: Text to 3D CAD Generation via Technical Drawings** - Mohsen Yavartanoo, Sangmin Hong, Reyhaneh Neshatavar et al.. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2411.06206)]
- **Text2BIM: Generating Building Models Using a Large Language Model-based Multi-Agent Framework** - Changyu Du, Sebastian Esser, Stavros Nousias et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2408.08054)]
- **Generative AI Models for Different Steps in Architectural Design** - Chengyuan Li, Tianyu Zhang, Xusheng Du et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2404.01335)]
- **Zero-shot Sequential Neuro-symbolic Reasoning for Automatically Generating Architecture Schematic Designs** - Milin Kodnongbua, Lawrence H. Curtis, Adriana Schulz. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2402.00052)]
- **Can LLMs Generate Architectural Design Decisions?** - Rudra Dhar, Karthik Vaidhyanathan, Vasudeva Varma. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2403.01709)]
- **A Comprehensive Survey on Design and Generation of Virtual Architecture by Deep Learning** - Anqi Wang, Jiahua Dong, Lik-Hang Lee et al. *Computational Visual Media 2023*. [[Paper](https://arxiv.org/abs/2305.00510)]
- **Automating Computational Design with Generative AI** - Joern Ploennigs, Markus Berger. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2307.02511)]
- **HouseDiffusion: Vector Floorplan Generation via a Diffusion Model with Discrete and Continuous Denoising** - Mohammad Amin Shabani, Sepidehsadat Hosseini, Yasutaka Furukawa. *arXiv 2022*. [[Paper](https://arxiv.org/abs/2211.13287)]
- **Learning Floorplan Generation from Layout Graphs** - Ruizhen Hu, Zeyu Huang, Yuhan Tang et al. *arXiv 2020*. [[Paper](https://arxiv.org/abs/2004.13204)]

### Vectorization and Digitization

- **FloorplanVLM: A Vision-Language Model for Floorplan Vectorization** - Yuanqing Liu, Ziming Yang, Yulong Li et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.06507)]
- **Drawing2CAD: Sequence-to-Sequence Learning for CAD Generation from Vectorized Drawings** - Feiwei Qin, Shichao Lu, Junhao Hou et al.. *ACM MM 2025*. [[Paper](https://arxiv.org/abs/2508.18733)]
- **Learning More by Seeing Less: Structure First Learning for Efficient, Transferable, and Human-Aligned Vision** - Tianqin Li, George Liu, Tai Sing Lee. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.06696)]
- **Enhancing Structured Reasoning for Vector Graphics Generation with Reinforcement Learning** - Ximing Xing, Ziteng Xue, Yandong Guan et al. *CVPR 2026*. [[Paper](https://arxiv.org/abs/2505.24499)]
- **Rendering-Aware Reinforcement Learning for Vector Graphics Generation** - Juan A. Rodriguez, Haotian Zhang, Abhay Puri et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.20793)]
- **Vector Graphic Animation via Neural Implicits and Video Diffusion Priors** - Wenshuo Gao, Xicheng Lan, Luyao Zhang et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.07484)]
- **Advanced Knowledge Extraction of Physical Design Drawings, Translation and Conversion to CAD Formats using Deep Learning** - Jesher Joshua M, Ragav V, Syed Ibrahim S P. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2403.11291)]
- **Evaluating Large Language Models on Vector Graphics Understanding and Generation** - Bocheng Zou, Mu Cai, Jianrui Zhang et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2407.10972)]
- **Tokenizing Strokes for Vector Graphic Synthesis** - Zecheng Tang, Chenfei Wu, Zekai Zhang et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2401.17093)]
- **A Comprehensive End-to-End Computer Vision Framework for Restoration and Recognition of Low-Quality Engineering Drawings** - Lvyang Yang, Jiankang Zhang, Huaiqiang Li et al.. *Engineering Applications of Artificial Intelligence 2023*. [[Paper](https://arxiv.org/abs/2312.13620)]
- **Component Segmentation of Engineering Drawings Using Graph Convolutional Networks** - Wentai Zhang, Joe Joseph, Yue Yin et al.. *Computers in Industry 2022*. [[Paper](https://arxiv.org/abs/2212.00290)]
- **Deep Vectorization of Technical Drawings** - Egiazarian et al.. *ECCV 2020*. [[Paper](https://arxiv.org/abs/2003.05471)]

### P&ID Diagram Intelligence

- **GraphRAG for Engineering Diagrams** - Achmad Anggawirya Alimin, Artur M. Schweidtmann. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.22528)]
- **AutoChemSchematic AI: Agentic Physics-Aware Automation for Chemical Manufacturing Scale-Up** - Sakhinana Sagar Srinivas, Shivam Gupta, Venkataramana Runkana. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.24584)]
- **From Engineering Diagrams to Graphs: Digitizing P&IDs with Transformers** - Jan Marius Stürmer, Marius Graumann, Tobias Koch. *IEEE DSAA 2025*. [[Paper](https://arxiv.org/abs/2411.13929)]
- **Talking like Piping and Instrumentation Diagrams (P&IDs)** - Achmad Anggawirya Alimin, Dominik P. Goldstein, Lukas Schulze Balhorn et al.. *Systems and Control Transactions 2025*. [[Paper](https://arxiv.org/abs/2502.18928)]
- **Visual Language Model as a Judge for Object Detection in Industrial Diagrams** - Sanjukta Ghosh. *IEEE ICASSP 2026*. [[Paper](https://arxiv.org/abs/2510.03376)]
- **Advanced Integration of Discrete Line Segments in Digitized P&ID for Continuous Instrument Connectivity** - Soumya Swarup Prusty, Astha Agarwal, Srinivasan Iyenger. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.11976)]
- **Rule-Based Autocorrection of Piping and Instrumentation Diagrams (P&IDs) on Graphs** - Lukas Schulze Balhorn, Niels Seijsener, Kevin Dao et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2502.18493)]
- **Accelerating Manufacturing Scale-Up from Material Discovery Using Agentic Web Navigation and Retrieval-Augmented AI for Process Engineering Schematics Design** - Sakhinana Sagar Srinivas, Akash Das, Shivam Gupta et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2412.05937)]
- **An Agentic Approach to Automatic Creation of P&ID Diagrams from Natural Language Descriptions** - Shreeyash Gowaikar, Srinivasan Iyengar, Sameer Segal et al.. *AAAI 2025 Workshop AI2ASE*. [[Paper](https://arxiv.org/abs/2412.12898)]
- **Towards Automatic Generation of Piping and Instrumentation Diagrams (P&IDs) with Artificial Intelligence** - Edwin Hirtreiter, Lukas Schulze Balhorn, Artur M. Schweidtmann. *arXiv 2022*. [[Paper](https://arxiv.org/abs/2211.05583)]
- **Digitize-PID: Automatic Digitization of Piping and Instrumentation Diagrams** - Shubham Paliwal, Arushi Jain, Monika Sharma et al.. *PAKDD 2021*. [[Paper](https://arxiv.org/abs/2109.03794)]
- **OSSR-PID: One-Shot Symbol Recognition in P&ID Sheets using Path Sampling and GCN** - Shubham Paliwal, Monika Sharma, Lovekesh Vig. *IJCNN 2021*. [[Paper](https://arxiv.org/abs/2109.03849)]

### Electrical and Circuit Schematics

- **SINA: A Circuit Schematic Image-to-Netlist Generator Using Artificial Intelligence** - Saoud Aldowaish, Yashwanth Karumanchi, Kai-Chen Chiang et al.. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.22114)]
- **OmniSch: A Multimodal PCB Schematic Benchmark For Structured Diagram Visual Reasoning** - Taiting Lu, Kaiyuan Lin, Yuxin Tian et al.. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.00270)]
- **CircuitLM: A Multi-Agent LLM-Aided Design Framework for Generating Circuit Schematics from Natural Language Prompts** - Khandakar Shakib Al Hasan, Syed Rifat Raiyan, Hasin Mahtab Alvee et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.04505)]
- **PCBSchemaGen: Constraint-Guided Schematic Design via LLM for Printed Circuit Boards** - Huanghaohe Zou, Peng Han, Emad Nazerian et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.00510)]
- **Agentic Hardware Design Reviews** - Kyle Dumont, Nicholas Herbert, Hayder Tirmazi et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.15672)]
- **Component Centric Placement Using Deep Reinforcement Learning for PCB Design** - Kart Leong Lim. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.23540)]
- **AMSnet 2.0: A Large AMS Database with AI Segmentation for Net Detection** - Yichen Shi, Zhuofu Tao, Yuhao Gao et al.. *LAD 2025*. [[Paper](https://arxiv.org/abs/2505.09155)]
- **SkeySpot: Automating Service Key Detection for Digital Electrical Layout Plans in the Construction Industry** - Dhruv Dosi, Rohit Meena, Param Rajpura et al.. *IEEE SMC 2025*. [[Paper](https://arxiv.org/abs/2508.10449)]
- **EEschematic: Multimodal-LLM Based AI Agent for Schematic Generation of Analog Circuit** - Chang Liu, Others. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.17002)]
- **CircuitSense: A Hierarchical MLLM Benchmark Bridging Visual Comprehension and Symbolic Reasoning in Engineering Design Process** - Arman Akbari, Jian Gao, Yifei Zou et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.22339)]
- **Enhancing Large Language Models for End-to-End Circuit Analysis Problem Solving** - Liangliang Chen, Weiyu Sun, Huiru Xie et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.10159)]
- **AutoCircuit-RL: Reinforcement Learning-Driven LLM for Automated Circuit Topology Generation** - Prashanth Vijayaraghavan, Luyao Shi, Ehsan Degan et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2506.03122)]
- **Efficient and Effective Representation Learning for Circuit Design at Scale** - Ziyang Zheng, Shan Huang, Jianyuan Zhong et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2502.01681)]
- **Masala-CHAI: A Large-Scale SPICE Netlist Dataset for Analog Circuits by Harnessing AI** - Jitendra Bhandari, Vineet Bhat, Yuheng He et al.. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2411.14299)]
- **Modular Graph Extraction for Handwritten Circuit Diagram Images** - Johannes Bayer, Leo van Waveren, Andreas Dengel. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2402.11093)]
- **Opportunities and Challenges of Large Circuit Models** - Lei Chen, Yiqi Chen, Zhufei Chu et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2403.07257)]
- **AMSnet: A Netlist Dataset for AMS Circuits** - Zhuofu Tao, Yichen Shi, Yiru Huo et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2405.09045)]
- **PCBDet: An Efficient Deep Neural Network Object Detection Architecture for Automatic PCB Component Detection on the Edge** - Brian Li, Steven Palayew, Francis Li et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2301.09268)]
- **Hand-Drawn Electrical Circuit Recognition using Object Detection and Node Recognition** - Rachala Rohith Reddy, Mahesh Raveendranatha Panicker. *arXiv 2021*. [[Paper](https://arxiv.org/abs/2106.11559)]

### Architectural Floor Plan Analysis

- **Raster2Seq: Polygon Sequence Generation for Floorplan Reconstruction** - Hao Phung, Hadar Averbuch-Elor. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.09016)]
- **A Fully Automated Hybrid Learning Scan-to-BIM Pipeline with Integrated Topology Refinement** - Mahdi Chamseddine, Fabian Kaufmann, Marius Schellen et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.24311)]
- **Enhancing Floor Plan Recognition: A Hybrid Mix-Transformer and U-Net Approach for Precise Wall Segmentation** - Dmitriy Parashchuk, Alexey Kaspshitskiy, Yuriy Karyakin. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.02413)]
- **SAM-Guided Floorplan Reconstruction with Semantic-Geometric Fusion** - Hanfu Ye, Hanfu Wang, Yunchi Zhang et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.15750)]
- **A Multi-Agent Human-AI Collaborative Pipeline to Convert Hand-Drawn Floor Plans to 3D BIM** - Abir Khan Ratul, Sanjay Acharjee, Somin Park et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.20838)]
- **Graph Similarity Learning of Floor Plans** - Casper van Engelenburg, Jan van Gemert, Seyran Khademi. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.03737)]
- **Cloud2BIM: Open-source Automatic Pipeline for Efficient Conversion of Large-scale Point Clouds to IFC Format** - Slavek Zbirovsky, Vaclav Nezerka. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.11498)]
- **WAFFLE: Multimodal Floorplan Understanding in the Wild** - Keren Ganon, Morris Alper, Rachel Mikulinsky et al.. *WACV 2025*. [[Paper](https://arxiv.org/abs/2412.00955)]
- **Multi-Unit Floor Plan Recognition and Reconstruction Using Improved Semantic Segmentation of Raster-Wise Floor Plans** - Lukas Kratochvila, Gijs de Jong, Monique Arkesteijn et al.. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2408.01526)]
- **Building Point Cloud Completion Benchmarks** - Weixiao Gao, Ravi Peters, Jantien Stoter. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2404.15644)]
- **MuraNet: Multi-task Floor Plan Recognition with Relation Attention** - Lingxiao Huang, Jung-Hsuan Wu, Chiching Wei et al.. *ICDAR 2023 Workshops*. [[Paper](https://arxiv.org/abs/2309.00348)]
- **GLSP: Parsing Line Segments of Floor Plan Images Using Graph Neural Networks** - Mingxiang Chen, Cihui Pan. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2303.03851)]
- **Automatic Reconstruction of Semantic 3D Models from 2D Floor Plans** - Aleixo Cambeiro Barreiro, Mariusz Trzeciakiewicz, Anna Hilsmann et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2306.01642)]
- **Polygon Detection for Room Layout Estimation using Heterogeneous Graphs and Wireframes** - David Gillsjo, Gabrielle Flood, Kalle Astrom. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2306.12203)]
- **Extracting Real Estate Values of Rental Apartment Floor Plans using Graph Convolutional Networks** - Atsushi Takizawa. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2303.13568)]
- **Assistive Scan to Building Information Modeling** - Weilian Song, Jieliang Luo, Dale Zhao et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2311.18166)]
- **Offset-Guided Attention Network for Room-Level Aware Floor Plan Segmentation** - Zhangyu Wang, Ningyuan Sun. *arXiv 2022*. [[Paper](https://arxiv.org/abs/2210.17411)]
- **Room Classification on Floor Plan Graphs using Graph Neural Networks** - Abhishek Paudel, Roshan Dhakal, Sakshat Bhattarai. *arXiv 2021*. [[Paper](https://arxiv.org/abs/2108.05947)]
- **Deep Floor Plan Recognition Using a Multi-Task Network with Room-Boundary-Guided Attention** - Zhiliang Zeng, Xianzhi Li, Ying Kin Yu et al. *ICCV 2019*. [[Paper](https://arxiv.org/abs/1908.11025)]

---

## 3D CAD Generation and Reconstruction

Methods for generating parametric 3D CAD models from various inputs including text, images, point clouds, and sketches.

**Representative anchors:** DeepCAD for autoregressive CAD sequence generation; SkexGen for disentangled codebook generation; recent code-generation methods for LLM-native CAD.

### Autoregressive Sequence Models

- **AGDC: Autoregressive Generation of Variable-Length Sequences with Joint Discrete and Continuous Spaces** - Yeonsang Shin, Insoo Kim, Bongkeun Kim et al.. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.05680)]
- **Position: You Can't Manufacture a NeRF** - Marta An Kimmel, Mueed Ur Rehman, Yonatan Bisk et al. *ICML 2025*. [[Paper](https://openreview.net/forum?id=kJzB6lQmcb)]
- **CAD-SIGNet: CAD Language Inference from Point Clouds using Layer-wise Sketch Instance Guided Attention** - Mohammad Sadil Khan, Elona Dupont, Sk Aziz Ali et al.. *CVPR 2024*. [[Paper](https://arxiv.org/abs/2402.17678)]
- **FlexCAD: Unified and Versatile Controllable CAD Generation with Fine-tuned Large Language Models** - Zhanwei Zhang, Shizhao Sun, Wenxiao Wang et al.. *ICLR 2025*. [[Paper](https://arxiv.org/abs/2411.05823)]
- **Img2CAD: Conditioned 3D CAD Model Generation from Single Image with Structured Visual Geometry** - Tianrun Chen, Chunan Yu, Yuanqi Hu et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2410.03417)]
- **Img2CAD: Reverse Engineering 3D CAD Models from Images through VLM-Assisted Conditional Factorization** - Yang You, Mikaela Angelina Uy, Jiaqi Han et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2408.01437)]
- **ContrastCAD: Contrastive Learning-based Representation Learning for Computer-Aided Design Models** - Minseop Jung, Minseong Kim, Jibum Kim. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2404.01645)]
- **Pushing Auto-regressive Models for 3D Shape Generation at Capacity and Scalability** - Qian et al.. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2402.12225)]
- **Semantic-Free Procedural 3D Shapes Are Surprisingly Good Teachers** - Xuweiyi Chen, Zezhou Cheng. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2411.17467)]
- **Hierarchical Neural Coding for Controllable CAD Model Generation** - Xiang Xu, Pradeep Kumar Jayaraman, Joseph G. Lambourne et al.. *ICML 2023*. [[Paper](https://arxiv.org/abs/2307.00149)]
- **Model2Scene: Learning 3D Scene Representation via Contrastive Language-CAD Models Pre-training** - Runnan Chen, Xinge Zhu, Nenglun Chen et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2309.16956)]
- **Vitruvion: A Generative Model of Parametric CAD Sketches** - Ari Seff, Wenda Zhou, Nick Richardson et al.. *ICLR 2022*. [[Paper](https://arxiv.org/abs/2109.14124)]
- **ExtrudeNet: Unsupervised Inverse Sketch-and-Extrude for Shape Parsing** - Daxuan Ren, Jianmin Zheng, Jianfei Cai et al.. *ECCV 2022*. [[Paper](https://arxiv.org/abs/2209.15632)]
- **Self-Supervised Representation Learning for CAD** - Jones et al.. *arXiv 2022*. [[Paper](https://arxiv.org/abs/2210.10807)]
- **SketchGen: Generating Constrained CAD Sketches** - Wamiq Reyaz Para, Shariq Farooq Bhat, Paul Guerrero et al.. *NeurIPS 2021*. [[Paper](https://arxiv.org/abs/2106.02711)]
- **Fusion 360 Gallery: A Dataset and Environment for Programmatic CAD Construction** - Willis et al.. *arXiv 2020*. [[Paper](https://arxiv.org/abs/2010.02392)]

### Diffusion-Based Generation

- **SketchDNN: Joint Continuous-Discrete Diffusion for CAD Sketch Generation** - Sathvik Chereddy, John Femiani. *ICML 2025*. [[Paper](https://arxiv.org/abs/2507.11579)]
- **RECAD: Revisiting CAD Model Generation by Learning Raster Sketch** - Pu Li, Wenhao Zhang, Jianwei Guo et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.00928)]
- **Feasibility Enhancement for 3D CAD Generation** - Chikaha Tsuji, Enrique Flores Medina, Harshit Gupta et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.23287)]
- **Physically Grounded 3D Shape Generation for Industrial Design** - Yingxuan You, Chen Zhao, Hantao Zhang et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.00422)]
- **GenCAD: Image-Conditioned Computer-Aided Design Generation with Transformer-Based Contrastive Representation and Diffusion Priors** - Md Ferdous Alam, Faez Ahmed. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2409.16294)]
- **Shaping Realities: Enhancing 3D Generative AI with Fabrication Constraints** - Faruqi et al.. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2404.10142)]

### LLM and VLM-Based Generation

- **PR-CAD: Progressive Refinement for Unified Controllable and Faithful Text-to-CAD Generation with Large Language Models** - Jiyuan An, Jiachen Zhao, Fan Chen et al. *ICLR 2026*. [[Paper](https://arxiv.org/abs/2604.19773)]
- **Learning Hierarchical and Geometry-Aware Graph Representations for Text-to-CAD** - Shengjie Gong, Wenjie Peng, Hongyuan Chen et al. *ICLR 2026*. [[Paper](https://arxiv.org/abs/2604.10075)]
- **FutureCAD: Towards High-Fidelity CAD Generation via LLM-Driven Program Generation and Text-Based B-Rep Primitive Grounding** - Jiahao Li, Qingwang Zhang, Qiuyu Chen et al.. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.11831)]
- **ProCAD: Clarify Before You Draw: Proactive Agents for Robust Text-to-CAD Generation** - Bo Yuan, Zelin Zhao, Petr Molodyk et al.. *arXiv (in review) 2026*. [[Paper](https://arxiv.org/abs/2602.03045)]
- **CAD-Tokenizer: Towards Text-based CAD Prototyping via Modality-Specific Tokenization** - Ruiyu Wang, Shizhao Sun, Weijian Ma et al.. *ICLR 2026*. [[Paper](https://arxiv.org/abs/2509.21150)]
- **CADSmith: Multi-Agent CAD Generation with Programmatic Geometric Validation** - Jesse Barkley, Rumi Loghmani, Amir Barati Farimani. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.26512)]
- **Proc3D: Procedural 3D Generation and Parametric Editing of 3D Shapes with Large Language Models** - Fadlullah Raji, Stefano Petrangeli, Matheus Gadelha et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.12234)]
- **CAD-Coder (MIT): Text-Guided CAD Files Code Generation** - Changqi He, Shuhan Zhang, Liguo Zhang et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.08686)]
- **Fine-Tuning Code Language Models for Text-Driven Sequential CAD Design** - Prashant Govindarajan, Davide Baldelli, Jay Pathak et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2507.09792)]
- **GeoCAD: Local Geometry-Controllable CAD Generation with Large Language Models** - Zhanwei Zhang, Kaiyuan Liu, Junjie Liu et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2506.10337)]
- **3Dify: A Framework for Procedural 3D-CG Generation Assisted by LLMs Using MCP and RAG** - Shun-ichiro Hayashi, Daichi Mukunoki, Tetsuya Hoshino et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.04536)]
- **LLM Agents for Structured, Textured and Interactive 3D Modeling** - Shuyuan Zhang, Chenhan Jiang, Zuoou Li et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.17603)]
- **Seek-CAD: A Self-refined Generative Modeling for 3D Parametric CAD Using Local Inference via DeepSeek** - Xueyang Li, Jiahao Li, Yu Song et al.. *ICLR 2026*. [[Paper](https://arxiv.org/abs/2505.17702)]
- **TCADGen: Automated CAD Modeling Sequence Generation from Text Descriptions via Transformer-Based Large Language Models** - Jianxing Liao, Junyan Xu, Yatao Sun et al.. *ACL 2025*. [[Paper](https://arxiv.org/abs/2505.19490)]
- **CAD-Coder (MIT): An Open-Source Vision-Language Model for Computer-Aided Design Code Generation** - Anna C. Doris, Md Ferdous Alam, Amin Heyrani Nobari et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.14646)]
- **Image2CADSeq: Computer-Aided Design Sequence and Knowledge Inference from Product Images** - Xingang Li, Zhenghui Sha. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2501.04928)]
- **CADgpt: Harnessing Natural Language Processing for 3D Modelling to Enhance Computer-Aided Design Workflows** - Timo Kapsalis. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2401.05476)]
- **CAD2Program: From 2D CAD Drawings to 3D Parametric Models: A Vision-Language Approach** - Xilin Wang, Jia Zheng, Yuanchao Hu et al.. *AAAI 2025*. [[Paper](https://arxiv.org/abs/2412.11892)]
- **3D-GPT: Procedural 3D Modeling with Large Language Models** - Sun et al.. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2310.12945)]

### Reinforcement Learning-Enhanced Generation

- **CME-CAD: Heterogeneous Collaborative Multi-Expert Reinforcement Learning for CAD Code Generation** - Ke Niu, Haiyang Yu, Zhuofan Chen et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.23333)]
- **ReCAD: Reinforcement Learning Enhanced Parametric CAD Model Generation with Vision-Language Models** - Jiahao Li, Yusheng Luo, Yunzhong Lou et al.. *AAAI 2026 (Oral)*. [[Paper](https://arxiv.org/abs/2512.06328)]
- **CAD-RL: From Intent to Execution: Multimodal Chain-of-Thought Reinforcement Learning for Precise CAD Code Generation** - Ke Niu, Haiyang Yu, Zhuofan Chen et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.10118)]

### B-Rep and CSG Generation

- **HiDiGen: Hierarchical Diffusion for B-Rep Generation with Explicit Topological Constraints** - Shurui Liu, Weide Chen, Ancong Wu. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.02847)]
- **BrepARG: AutoRegressive Generation with B-rep Holistic Token Sequence Representation** - Jiahao Li, Yunpeng Bai, Yongkang Dai et al.. *CVPR 2026*. [[Paper](https://arxiv.org/abs/2601.16771)]
- **Flatten The Complex: Joint B-Rep Generation via Compositional k-Cell Particles** - Junran Lu, Yuanqi Li, Hengji Li et al.. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.17733)]
- **Topology-First B-Rep Meshing** - Zhou et al.. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.02141)]
- **DTGBrepGen: A Novel B-rep Generative Model through Decoupling Topology and Geometry** - Jing Li, Yihang Fu, Falai Chen. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.13110)]
- **AutoBrep: Autoregressive B-Rep Generation with Unified Topology and Geometry** - Xiang Xu, Pradeep Kumar Jayaraman, Joseph G. Lambourne et al.. *SIGGRAPH Asia 2025*. [[Paper](https://arxiv.org/abs/2512.03018)]
- **HoLa: B-Rep Generation using a Holistic Latent Representation** - Yilin Liu, Duoteng Xu, Xingyao Yu et al.. *SIGGRAPH 2025*. [[Paper](https://arxiv.org/abs/2504.14257)]
- **BrepGPT: Autoregressive B-rep Generation with Voronoi Half-Patch** - Pu Li, Wenhao Zhang, Weize Quan et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.22171)]
- **NURBGen: High-Fidelity Text-to-CAD Generation through LLM-Driven NURBS Modeling** - Muhammad Usama, Mohammad Sadil Khan, Didier Stricker et al.. *AAAI 2026*. [[Paper](https://arxiv.org/abs/2511.06194)]
- **Pointer-CAD: Unifying B-Rep and Command Sequences via Pointer-based Edges and Faces Selection** - Dacheng Qi, Chenyu Wang, Jingwei Xu et al. *CVPR 2026*. [[Paper](https://arxiv.org/abs/2603.04337)]
- **CMT: A Cascade MAR with Topology Predictor for Multimodal Conditional CAD Generation** - Wu et al.. *ICCV 2025*. [[Paper](https://arxiv.org/abs/2504.20830)]
- **Learning B-Rep in Graph Structure for Efficient CAD Generation** - Weilin Lai, Tie Xu, Hu Wang. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2507.04765)]
- **Transformer-Based B-rep Geometric Feature Recognition** - Yongkang Dai, Xiaoshui Huang, Yunpeng Bai et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2504.07378)]
- **BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry** - Xiang Xu, Joseph G. Lambourne, Pradeep Kumar Jayaraman et al.. *SIGGRAPH 2024*. [[Paper](https://arxiv.org/abs/2401.15563)]
- **DiffCSG: Differentiable CSG via Rasterization** - Haocheng Yuan, Adrien Bousseau, Hao Pan et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2409.01421)]
- **Learning Efficient Surface Representations for 3D Solids** - Jiajie Fan, Babak Gholami, Thomas Back et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2411.10848)]
- **A Unified Differentiable Boolean Operator with Fuzzy Logic** - Hsueh-Ti Derek Liu, Maneesh Agrawala, Cem Yuksel et al. *SIGGRAPH 2024*. [[Paper](https://arxiv.org/abs/2407.10954)]
- **SolidGen: An Autoregressive Model for Direct B-rep Synthesis** - Pradeep Kumar Jayaraman, Joseph G. Lambourne, Nishkrit Desai et al.. *TMLR 2023*. [[Paper](https://arxiv.org/abs/2203.13944)]
- **Implicit Conversion of Manifold B-Rep Solids by Neural Halfspace Representation** - Hao-Xiang Guo, Yang Liu, Hao Pan et al. *arXiv 2022*. [[Paper](https://arxiv.org/abs/2209.10191)]
- **CSG-Stump: A Learning Friendly CSG-Like Representation for Interpretable Shape Parsing** - Daxuan Ren, Jianmin Zheng, Jianfei Cai et al.. *ICCV 2021*. [[Paper](https://arxiv.org/abs/2108.11305)]
- **Learning Compact CAD Shapes with Adaptive Primitive Assembly** - Fenggen Yu, Zhiqin Chen, Manyi Li et al. *arXiv 2021*. [[Paper](https://arxiv.org/abs/2104.05652)]
- **CSGNe: Neural Shape Parsers for Constructive Solid Geometry** - Gopal Sharma, Rishabh Goyal, Difan Liu et al.. *arXiv 2019*. [[Paper](https://arxiv.org/abs/1912.11393)]

### Point Cloud to CAD

- **CADReasoner: Iterative Program Editing for CAD Reverse Engineering** - Soslan Kabisov, Vsevolod Kirichuk, Andrey Volkov et al.. *CVPR 2026*. [[Paper](https://arxiv.org/abs/2603.29847)]
- **Fast Curvature Regularization of Neural SDFs for CAD Models** - Haotian Yin, Aleksander Plocharski, Michal Jan Wlodarczyk et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2506.16627)]
- **Point2Primitive: CAD Reconstruction from Point Cloud by Direct Primitive Prediction** - Xinzhu Ma, Cheng Wang, Chen Tang et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.02043)]
- **NeurCADRecon: Neural Representation for Reconstructing CAD Surfaces by Enforcing Zero Gaussian Curvature** - Qiujie Dong, Rui Xu, Pengfei Wang et al. *SIGGRAPH 2024*. [[Paper](https://arxiv.org/abs/2404.13420)]
- **TransCAD: A Hierarchical Transformer for CAD Sequence Inference from Point Clouds** - Elona Dupont, Kseniya Cherenkova, Dimitrios Mallis et al.. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2407.12702)]
- **CAD-Recode: Reverse Engineering CAD Code from Point Clouds** - Danila Rukhovich, Elona Dupont, Dimitrios Mallis et al.. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2412.14042)]
- **PS-CAD: Local Geometry Guidance via Prompting and Selection for CAD Reconstruction** - Bingchen Yang, Haiyong Jiang, Hao Pan et al. *ACM TOG 2024*. [[Paper](https://arxiv.org/abs/2405.15188)]
- **P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds** - Zhihao Zong, Fazhi He, Rubin Fan et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2310.02638)]
- **Point2CAD: Reverse Engineering CAD Models from 3D Point Clouds** - Yujia Liu, Anton Obukhov, Jan Dirk Wegner et al.. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2312.04962)]
- **ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation** - Haoxiang Guo, Shilin Liu, Hao Pan et al.. *SIGGRAPH 2022*. [[Paper](https://arxiv.org/abs/2205.14573)]

### Image to CAD

- **BrepGaussian: CAD reconstruction from Multi-View Images with Gaussian Splatting** - Jiaxing Yu, Dongyang Ren, Hangyu Xu et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.21105)]
- **ProcGen3D: Learning Neural Procedural Graph Representations for Image-to-3D Reconstruction** - Xinyi Zhang, Daoyi Gao, Naiqi Li et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.07142)]
- **GACO-CAD: Geometry-Augmented and Conciseness-Optimized CAD Model Generation from Single Image** - Yinghui Wang, Xinyu Zhang, Peng Du. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.17157)]
- **View2CAD: Reconstructing View-Centric CAD Models from Single RGB-D Scans** - James Noeckel, Benjamin Jones, Adriana Schulz et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2504.04000)]
- **Image2CADSeq: Computer-Aided Design Sequence and Knowledge Inference from Product Images** - Xingang Li, Zhenghui Sha. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2501.04928)]
- **DiffCAD: Weakly-Supervised Probabilistic CAD Model Retrieval and Alignment from an RGB Image** - Gao et al.. *SIGGRAPH 2024*. [[Paper](https://arxiv.org/abs/2311.18610)]
- **Automatic Reverse Engineering: Creating computer-aided design (CAD) models from multi-view images** - Henrik Jobczyk, Hanno Homann. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2309.13281)]

### Sketch to CAD

- **Learning Multimodal Feature-Enhanced Diffusion Models for Zero-Shot Sketch-Based 3D Shape Retrieval** - Hang Cheng, Fanhe Dong, Long Zeng. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.19135)]
- **AutoConstrain: Aligning Constraint Generation with Design Intent in Parametric CAD** - Casey et al.. *ICCV 2025*. [[Paper](https://arxiv.org/abs/2504.13178)]
- **Robust Self-Supervised CAD Reconstruction from Three Orthographic Views Using 3D Gaussian Splatting** - Zhou et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.05161)]
- **Efficient CAD Parametric Primitive Analysis with Progressive Hierarchical Tuning** - Ke Niu, Yuwen Chen, Haiyang Yu et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.18147)]
- **Sketch-Driven 3D Model Generation** - Hail Song, Wonsik Shin, Naeun Lee et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.04185)]
- **DAVINCI: A Single-Stage Architecture for Constrained CAD Sketch Inference** - Ahmet Serdar Karadeniz, Dimitrios Mallis, Nesryne Mejri et al. *BMVC 2024*. [[Paper](https://arxiv.org/abs/2410.22857)]
- **Parametric Primitive Analysis of CAD Sketches with Vision Transformer** - Xiaogang Wang, Liang Wang, Hongyu Wu et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2407.00410)]
- **PICASSO: A Feed-Forward Framework for Parametric Inference of CAD Sketches via Rendering Self-Supervision** - Ahmet Serdar Karadeniz, Dimitrios Mallis, Nesryne Mejri et al.. *WACV 2025*. [[Paper](https://arxiv.org/abs/2407.13394)]
- **Sketch2CAD: 3D CAD Model Reconstruction from 2D Sketch using Visual Transformer** - Hong-Bin Yang. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2309.16850)]
- **3D Modeling from Free-hand Sketches with View- and Structural-Aware Adversarial Training** - Tianrun Chen, Chenglong Fu, Lanyun Zhu et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2312.04435)]
- **Engineering Sketch Generation for Computer-Aided Design** - Willis et al.. *arXiv 2021*. [[Paper](https://arxiv.org/abs/2104.09621)]

### CAD Editing

- **CAD-Editor: A Locate-then-Infill Framework with Automated Training Data Synthesis for Text-Based CAD Editing** - Yu Yuan, Shizhao Sun, Qi Liu et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2502.03997)]
- **BRepLer: Language-guided Editing of CAD Models** - Liu et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.10201)]
- **GenPara: Enhancing 3D Design Editing by Inferring Users' Regions of Interest with Text-Conditional Shape Parameters** - Jiin Choi, Seung Won Lee, Kyung Hoon Hyun. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.14096)]
- **CADMorph: Geometry-Driven Parametric CAD Editing via a Plan-Generate-Verify Loop** - Weijian Ma, Shizhao Sun, Ruiyu Wang et al.. *NeurIPS 2025*. [[Paper](https://arxiv.org/abs/2512.11480)]
- **ParSEL: Parameterized Shape Editing with Language** - Aditya Ganeshan, Ryan Y. Huang, Xianghao Xu et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2405.20319)]
- **Zero-shot CAD Program Re-Parameterization for Interactive Manipulation** - Milin Kodnongbua, Benjamin T. Jones, Maaz Bin Safeer Ahmad et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2306.03217)]
- **Differentiable 3D CAD Programs for Bidirectional Editing** - Cascaval et al.. *arXiv 2021*. [[Paper](https://arxiv.org/abs/2110.01182)]

### Assembly Generation

- **AADvark: Agent-Aided Design for Dynamic CAD Models** - Mitch Adler, Matthew Russo, Michael Cafarella. *CAIS 2026*. [[Paper](https://arxiv.org/abs/2604.15184)]
- **Error Notebook-Guided, Training-Free Part Retrieval in 3D CAD Assemblies via Vision-Language Models** - Yunqing Liu, Nan Zhang, Zhiming Tan. *ICLR 2026*. [[Paper](https://arxiv.org/abs/2509.01350)]
- **CADKnitter: Compositional CAD Generation from Text and Geometry Guidance** - Tri Le, Khang Nguyen, Baoru Huang et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.11199)]
- **Human-Crafted 3D Primitive Assembly Generation with Auto-Regressive Transformer** - Jingwen Ye, Yuze He, Yanning Zhou et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.04622)]
- **Diverse Part Synthesis for 3D Shape Creation** - Yanran Guan, Oliver van Kaick. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2401.09384)]
- **Category-Level Multi-Part Multi-Joint 3D Shape Assembly** - Li et al.. *CVPR 2023*. [[Paper](https://arxiv.org/abs/2303.06163)]
- **Unsupervised 3D Shape Reconstruction by Part Retrieval and Assembly** - Xianghao Xu, Paul Guerrero, Matthew Fisher et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2303.01999)]
- **JoinABLe: Learning Bottom-up Assembly of Parametric CAD Joints** - Karl D.D. Willis, Pradeep Kumar Jayaraman, Hang Chu et al.. *CVPR 2022*. [[Paper](https://arxiv.org/abs/2111.12772)]

### Shape Programs and Procedural Generation

- **PyTorchGeoNodes: Enabling Differentiable Shape Programs for 3D Shape Reconstruction** - Stekovic et al.. *CVPR 2025*. [[Paper](https://arxiv.org/abs/2404.10620)]
- **Example-driven Visual Program Learning for Generating 3D Object Arrangements** - Hou In Ivan Tam, Hou In Derek Pun, Austin T. Wang et al. *3DV 2025 (Oral)*. [[Paper](https://arxiv.org/abs/2408.02211)]
- **GEMA: Generative Medial Abstractions for 3D Shape Synthesis** - Dmitry Petrov, Pradyumn Goyal, Vikas Thamizharasan et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2402.16994)]
- **Discovering Abstractions for Visual Programs from Unstructured Primitives** - R. Kenny Jones, Paul Guerrero, Niloy J. Mitra et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2305.05661)]
- **Learning to Infer 3D Shape Programs with Differentiable Renderer** - Yichao Liang. *arXiv 2022*. [[Paper](https://arxiv.org/abs/2206.12675)]
- **Interpretable Shape Programs** - Ofek Pearl, Itai Lang, Yuhua Hu et al. *arXiv 2022*. [[Paper](https://arxiv.org/abs/2212.11715)]
- **Learning to Infer and Execute 3D Shape Programs** - Tian et al.. *ICLR 2019*. [[Paper](https://arxiv.org/abs/1901.02875)]

### Shape Completion

- **3D Shape Completion with Latent Diffusion Models** - Simon Schaefer, Juan D. Galvis, Xingxing Zuo et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2403.12470)]
- **Partial Object Completion with SDF Latent Transformers** - Faezeh Zakeri, Raphael Braun, Lukas Ruppert et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2411.05419)]
- **A Spatial-Aware Generative Model for 3D Shape Completion, Reconstruction, and Generation** - Ruikai Cui, Weizhe Liu, Weixuan Sun et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2403.18241)]

### NURBS and Surface Modeling

- **Flexible Neural Surface Parameterization** - Yuming Zhao, Qijian Zhang, Junhui Hou et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2504.19210)]
- **Neural Parametric Surfaces for Shape Modeling** - Lei Yang, Yongqing Liang, Xin Li et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2309.09911)]

### Multi-Modal CAD Generation

- **Captioning and Generating 3D Content via Multi-modal Large Language Models** - Junming Huang, Weiwei Xu. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.21798)]
- **Text-Image Conditioned 3D Generation** - Jiazhong Cen, Jiemin Fang, Sikuang Li et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.21295)]
- **Omni123: Exploring 3D Native Foundation Models with Limited 3D Data by Unifying Text to 2D and 3D Generation** - Chongjie Ye, Cheng Cao, Chuanyu Pan et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.02289)]
- **Collaborative Multi-Modal Coding for High-Quality 3D Generation** - Ziang Cao, Zhaoxi Chen, Liang Pan et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.15228)]
- **Idea23D: Collaborative LMM Agents Enable 3D Model Generation from Interleaved Multimodal Inputs** - Junhao Chen, Xiang Li, Xiaojun Ye et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2404.04363)]

### Procedural and Constraint-Based Generation

- **Procedural Material Generation with Large Vision-Language Models** - Beichen Li, Rundi Wu, Armando Solar-Lezama et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2501.18623)]
- **FeaGPT: An End-to-End Agentic AI for Finite Element Analysis** - Yupeng Qi, Ran Xu, Xu Chu. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.21993)]
- **Leveraging Automatic CAD Annotations for Supervised Learning in 3D Scene Understanding** - Yuchen Rao, Stefan Ainetter, Sinisa Stekovic et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2504.13580)]
- **A Software Engineering-Inspired Shape Grammar for Durand's Plates** - Rohan Agarwal. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2404.14448)]
- **A Review on Geometric Constraint Solving** - Qiang Zou, Zhihong Tang, Hsi-Yung Feng et al. *ASME JCISE 2022*. [[Paper](https://arxiv.org/abs/2202.13795)]

---

## CAD Understanding and Retrieval

Representation learning, feature recognition, retrieval, and semantic understanding of CAD models.

**Representative anchors:** BRepNet and UV-Net for boundary representation learning; SketchGraphs for relational geometry modeling.

### B-Rep Representation Learning

- **Pointer-CAD: Unifying B-Rep and Command Sequences via Pointer-based Edges & Faces Selection** - Dacheng Qi, Chenyu Wang, Jingwei Xu et al. *CVPR 2026*. [[Paper](https://arxiv.org/abs/2603.04337)]
- **Joint B-Rep Generation via Compositional k-Cell Particles** - Junran Lu, Yuanqi Li, Hengji Li et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.17733)]
- **BRepMAE: Self-Supervised Masked BRep Autoencoders for Machining Feature Recognition** - Can Yao, Kang Wu, Zuheng Zheng et al.. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.22701)]
- **Boundary and Shape Representation Alignment via Self-Supervised Transformers** - Yuanxu Sun, Yuezhou Ma, Haixu Wu et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.07429)]
- **MiCADangelo: Fine-Grained Reconstruction of Constrained CAD Models from 3D Scans** - Ahmet Serdar Karadeniz, Dimitrios Mallis, Danila Rukhovich et al. *NeurIPS 2025*. [[Paper](https://arxiv.org/abs/2510.23429)]
- **BRT: Bringing Attention to CAD - Boundary Representation Learning via Transformer** - Qiang Zou, Lizhen Zhu. *Computer-Aided Design 2025*. [[Paper](https://arxiv.org/abs/2504.07134)]
- **A Novel B-rep Generative Model through Decoupling Topology and Geometry** - Jing Li, Yihang Fu, Falai Chen. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.13110)]
- **Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning** - Yilin Liu, Jiale Chen, Shanshan Pan et al.. *SIGGRAPH 2024*. [[Paper](https://arxiv.org/abs/2406.05261)]
- **NH-Rep: Implicit Conversion of Manifold B-Rep Solids by Neural Halfspace Representation** - Hao-Xiang Guo, Yang Liu, Hao Pan et al.. *SIGGRAPH Asia 2022*. [[Paper](https://arxiv.org/abs/2209.10191)]

### Multi-Modal CAD Representations

- **CADCrafter: Generating Computer-Aided Design Models from Unconstrained Images** - Yunlong Chen, Xiang Xu, Ganzhangqin Yuan et al.. *CVPR 2025*. [[Paper](https://arxiv.org/abs/2504.04753)]
- **BrepLLM: Native Boundary Representation Understanding with Large Language Models** - Liyuan Deng, Hao Guo, Yunpeng Bai et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.16413)]
- **TAMM: TriAdapter Multi-Modal Learning for 3D Shape Understanding** - Zhihao Zhang, Shengcao Cao, Yu-Xiong Wang. *CVPR 2024*. [[Paper](https://arxiv.org/abs/2402.18490)]
- **ULIP-2: Towards Scalable Multimodal Pre-training for 3D Understanding** - Le Xue, Ning Yu, Shu Zhang et al.. *CVPR 2024*. [[Paper](https://arxiv.org/abs/2305.08275)]
- **LaGeM: A Large Geometry Model for 3D Representation Learning and Diffusion** - Biao Zhang, Peter Wonka. *ICLR 2025*. [[Paper](https://arxiv.org/abs/2410.01295)]
- **OpenShape: Scaling Up 3D Shape Representation Towards Open-World Understanding** - Minghua Liu, Ruoxi Shi, Kaiming Kuang et al.. *NeurIPS 2023*. [[Paper](https://arxiv.org/abs/2305.10764)]
- **Uni3D: Exploring Unified 3D Representation at Scale** - Junsheng Zhou, Jinsheng Wang, Baorui Ma et al.. *ICLR 2024*. [[Paper](https://arxiv.org/abs/2310.06773)]
- **ULIP: Learning a Unified Representation of Language, Images, and Point Clouds for 3D Understanding** - Le Xue, Mingfei Gao, Chen Xing et al.. *CVPR 2023*. [[Paper](https://arxiv.org/abs/2212.05171)]
- **Point-Bind & Point-LLM: Aligning Point Cloud with Multi-modality for 3D Understanding, Generation, and Instruction Following** - Ziyu Guo, Renrui Zhang, Xiangyang Zhu et al.. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2309.00615)]
- **Self-Supervised Generative-Contrastive Learning of Multi-Modal Euclidean Input for 3D Shape Latent Representations** - Chengzhi Wu, Julius Pfrommer, Mingyuan Zhou et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2301.04612)]

### Machining Feature Recognition

- **BRepFormer: Transformer-Based B-rep Geometric Feature Recognition** - Yongkang Dai, Xiaoshui Huang, Yunpeng Bai et al.. *ACM ICMR 2025*. [[Paper](https://arxiv.org/abs/2504.07378)]
- **Leveraging Vision-Language Models for Manufacturing Feature Recognition in CAD Designs** - Muhammad Tayyab Khan, Lequn Chen, Ye Han Ng et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2411.02810)]
- **AAGNet: A graph neural network towards multi-task machining feature recognition** - Hongjin Wu, Ruoshan Lei, Yibing Peng et al. *Robotics and Computer-Integrated Manufacturing 2024*. [[Paper](https://doi.org/10.1016/j.rcim.2023.102661)]
- **CNC-Net: Self-Supervised Learning for CNC Machining Operations** - Mohsen Yavartanoo, Sangmin Hong, Reyhaneh Neshatavar et al.. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2312.09925)]
- **Simplified Learning of CAD Features Leveraging a Deep Residual Autoencoder** - Raoul Schonhof, Jannes Elstner, Radu Manea et al. *arXiv 2022*. [[Paper](https://arxiv.org/abs/2202.10099)]
- **Geometry based Machining Feature Retrieval with Inductive Transfer Learning** - N S Kamal, Barathi Ganesh HB, Sajith Variyar VV et al. *arXiv 2021*. [[Paper](https://arxiv.org/abs/2108.11838)]
- **A Learning-based Approach to Feature Recognition of Engineering Shapes** - Lakshmi Priya Muraleedharan, Ramanathan Muthuganapathy. *arXiv 2021*. [[Paper](https://arxiv.org/abs/2112.07962)]
- **FeatureNet: Machining Feature Recognition Based on 3D Convolution Neural Network** - Zhibo Zhang, Prakhar Jaiswal, Rahul Rai. *CAD 2018*. [[Paper](https://doi.org/10.1016/j.cad.2018.03.006)]

### CAD Model Retrieval

- **OSCAR: Open-Set CAD Retrieval from a Language Prompt and a Single Image** - Tessa Pulli, Jean-Baptiste Weibel, Peter Hoenig et al.. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.07333)]
- **CADGCL: Unsupervised Retrieval of CAD Models via Boundary Representations** - Feiwei Qin, Liangzhe Zhu, Zijian Xu et al. *The Visual Computer 2025*. [[Paper](https://doi.org/10.1007/s00371-025-03949-y)]
- **SCA3D: Enhancing Cross-modal 3D Retrieval via 3D Shape and Caption Paired Data Augmentation** - Junlong Ren, Hao Wu, Hui Xiong et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2502.19128)]
- **GC-CAD: Self-supervised Graph Neural Network for Mechanical CAD Retrieval** - Yuhan Quan, Huan Zhao, Jinfeng Yi et al.. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2406.08863)]
- **Leveraging Cross-View Correspondence and Cross-Modal Mining for 3D Retrieval** - Hao Wu, Ruochong LI, Hao Wang et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2405.04103)]
- **Self-supervised Graph Neural Network for Mechanical CAD Retrieval** - Yuhan Quan, Huan Zhao, Jinfeng Yi et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2406.08863)]
- **FastCAD: Real-Time CAD Retrieval and Alignment from Scans and Videos** - Florian Langer, Jihong Ju, Georgi Dikov et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2403.15161)]
- **HOC-Search: Efficient CAD Model and Pose Retrieval from RGB-D Scans** - Stefan Ainetter, Sinisa Stekovic, Friedrich Fraundorfer et al.. *3DV 2024*. [[Paper](https://arxiv.org/abs/2309.06107)]
- **Fine-Tuned but Zero-Shot 3D Shape Sketch View Similarity and Retrieval** - Gianluca Berardi, Yulia Gryaditskaya. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2306.08541)]
- **Accurate Instance-Level CAD Model Retrieval in a Large-Scale Database** - Jiaxin Wei, Haibin Huang, Chongyang Ma et al.. *ICCV 2023*. [[Paper](https://arxiv.org/abs/2207.01339)]
- **UVStyle-Net: Unsupervised Few-shot Learning of 3D Style Similarity Measure for B-Reps** - Peter Meltzer, Hooman Shayani, Aditya Sanghi et al.. *ICCV 2021*. [[Paper](https://arxiv.org/abs/2105.02961)]

### Sketch-Based Retrieval

- **Multi-View Hierarchical Graph Neural Network for Sketch-Based 3D Shape Retrieval** - Hang Cheng, Muyan He, Mingyu Fan et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.18019)]
- **SketchCleanNet: A Deep Learning Approach to the Enhancement and Correction of Query Sketches for a 3D CAD Model Retrieval System** - Bharadwaj Manda, Ramanathan Muthuganapathy. *Computers & Graphics 2024*. [[Paper](https://arxiv.org/abs/2207.00732)]
- **CADSketchNet: An Annotated Sketch Dataset for 3D CAD Model Retrieval with Deep Neural Networks** - Bharadwaj Manda, Sai Sree Harsha, Subhrajit Dey et al.. *Computers & Graphics 2022*. [[Paper](https://arxiv.org/abs/2107.06212)]

### Shape Classification

- **CSTNet: Constraint-Aware Feature Learning for Parametric Point Cloud** - Cheng Cheng, Changqing Zou, Ruowei Wang et al.. *ICCV 2025*. [[Paper](https://arxiv.org/abs/2411.07747)]
- **CAD 3D Model Classification by Graph Neural Networks: A New Approach Based on STEP Format** - Lorenzo Mandelli, Stefano Berretti. *arXiv 2022*. [[Paper](https://arxiv.org/abs/2210.16815)]

### B-Rep Segmentation

- **Geometry-Conditioned Instance Segmentation for Industrial Objects** - Zhenran Tang, Rohan Nagabhirava, Changliu Liu. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.20551)]
- **Repurposing 3D Generative Model for Part Segmentation** - Lin Li, Haoran Feng, Zehuan Huang et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.16869)]
- **A2Z-10M+: Geometric Deep Learning with A-to-Z BRep Annotations for AI-Assisted CAD Modeling and Reverse Engineering** - Pritham Kumar Jena, Bhavika Baburaj, Tushar Anand et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.12605)]
- **Joint Neural SDF Reconstruction and Semantic Segmentation for CAD Models** - Shen Fan, Przemyslaw Musialski. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.03837)]
- **Few-shot Structure-Informed Machinery Part Segmentation with Foundation Models and Graph Neural Networks** - Michael Schwingshackl, Fabio Francisco Oberweger, Markus Murschitz. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2501.10080)]
- **Label-Efficient Part Segmentation** - S. B. van Rooij, G. J. Burghouts. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2501.07434)]
- **Scan-to-BRep: BRep Boundary and Junction Detection for CAD Reverse Engineering** - Sk Aziz Ali, Mohammad Sadil Khan, Didier Stricker. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2409.14087)]

### Sequence-Based Encoding

- **Unsupervised Contrastive Learning for Efficient and Robust Spectral Shape Matching** - Feifan Luo, Hongyang Chen. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.18924)]
- **Non-Rigid 3D Shape Correspondences: From Foundations to Open Challenges and Opportunities** - Aleksei Zhuravlev, Lennart Bastian, Dongliang Cao et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.01274)]
- **Diffusion Models for Shape Correspondence** - Aleksei Zhuravlev, Zorah Lahner, Vladislav Golyanik. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.01845)]

### Assembly Understanding

- **DYNAMO: Dependency-Aware Deep Learning Framework for Articulated Assembly Motion Prediction** - Mayank Patel, Rahul Jain, Asim Unmesh et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.12430)]
- **Generative 3D Part Assembly via Part-Whole-Hierarchy Message Passing** - Bi'an Du, Jianxin Ma, Junyi Zhu et al.. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2402.17464)]
- **DiffAssemble: A Unified Graph-Diffusion Model for 2D and 3D Reassembly** - Scarpellini et al.. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2402.19302)]
- **What's in a Name? Evaluating Assembly-Part Semantic Knowledge in Language Models through User-Provided Names in CAD Files** - Peter Meltzer, Joseph G. Lambourne, Daniele Grandi. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2304.14275)]
- **Synthesizing CAD Assemblies in Fusion 360** - Constantin Chaumet, Jakob Rehof. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2311.18492)]
- **HG-CAD: Material Prediction for Design Automation Using Graph Representation Learning** - Shijie Bian, Daniele Grandi, Pradeep Kumar Jayaraman et al.. *IDETC-CIE 2022 / JCISE 2024*. [[Paper](https://arxiv.org/abs/2209.12793)]

---

## Simulation and Design Optimization

AI-accelerated simulation surrogates, physics-informed methods, and topology optimization.

**Representative anchors:** Fourier Neural Operator for PDE surrogates; Physics-Informed Neural Networks for physics-constrained learning; TopoDiff and related models for generative topology optimization.

### Neural Operators and FEA Surrogates

- **NOEM: Efficient and Scalable Finite Element Method Enabled by Reusable Neural Operators** - Weihang Ouyang, Yeonjong Shin, Si-Wei Liu et al. *Nature Computational Science 2026*. [[Paper](https://doi.org/10.1038/s43588-026-00974-2)]
- **A Graph Neural Network Surrogate for 3D Finite Element Modeling: Accelerated Full-Field Parameter Identification in Aluminum Alloy 6DR1** - Ossama Abou Ali Modad, Mustapha Makki, Abdallah Chehade et al. *Modelling and Simulation in Materials Science and Engineering 2026*. [[Paper](https://doi.org/10.1186/s41313-026-00075-7)]
- **Efficient Dilated Squeeze and Excitation Neural Operator for Differential Equations** - Prajwal Chauhan, Salah Eddine Choutri, Saif Eddin Jabari. *arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2601.17407)]
- **Generative AI-Enhanced Probabilistic Multi-Fidelity Surrogate Modeling via Transfer Learning** - Jice Zeng, David Barajas-Solano, Hui Chen. *arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2602.00072)]
- **A Unified Hierarchical Multi-Task Multi-Fidelity Framework for Data-Efficient Surrogate Modeling in Manufacturing** - Manan Mehta, Zhiqiao Dong, Yuhang Yang et al. *arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2603.09842)]
- **A Practical Introduction to Neural Operators in Scientific Computing** - Prashant K. Jha. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2503.05598)]
- **EquiNO: A Physics-Informed Neural Operator for Multiscale Simulations** - Hamidreza Eivazi, Jendrik-Alexander Troger, Stefan Wittek et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2504.07976)]
- **A Comprehensive Evaluation of Graph Neural Networks and Physics Informed Learning for Surrogate Modelling of Finite Element Analysis** - Nayan Kumar Singh. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2510.15750)]
- **A Comprehensive Comparison of Neural Operators for 3D Industry-Scale Engineering Designs** - Weiheng Zhong, Qibang Liu, Diab Abueidda et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2510.05995)]
- **Neural Operators for Stochastic Modeling of Nonlinear Structural System Response to Natural Hazards** - Somdatta Goswami, Dimitris G. Giovanis, Bowei Li et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2502.11279)]
- **PhysiX: A Foundation Model for Physics Simulations** - Tung Nguyen, Arsh Koneru, Shufan Li et al. *ICLR 2026*. [[Paper](https://arxiv.org/abs/2506.17774)]
- **OmniArch: Building Foundation Model for Scientific Computing** - Chen et al.. *ICLR 2025*. [[Paper](https://arxiv.org/abs/2402.16014)]
- **Towards a Physics Foundation Model** - Florian Wiesner, Matthias Wessling, Stephen Baek. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2509.13805)]
- **Geometry Aware Operator Transformer as an Efficient and Accurate Neural Surrogate for PDEs on Arbitrary Domains** - Shizheng Wen, Arsh Kumbhat, Levi Lingsch et al. *NeurIPS 2025*. [[Paper](https://arxiv.org/abs/2505.18781)]
- **Probabilistic operator learning: generative modeling and uncertainty quantification for foundation models of differential equations** - Benjamin J. Zhang, Siting Liu, Stanley J. Osher et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2509.05186)]
- **Probabilistic Neural Operators for Functional Uncertainty Quantification** - Christopher Bulte, Philipp Scholl, Gitta Kutyniok. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2502.12902)]
- **Accelerating PDE-Constrained Optimization by the Derivative of Neural Operators** - Ze Cheng, Zhuoyu Li, Xiaoqiang Wang et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2506.13120)]
- **MeshODENet: A Graph-Informed Neural Ordinary Differential Equation Neural Network for Simulating Mesh-Based Physical Systems** - Kangzheng Liu, Leixin Ma. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2509.18445)]
- **Defining Foundation Models for Computational Science** - Youngsoo Choi, Siu Wun Cheung, Youngkyu Kim et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2505.22904)]
- **Learning to Solve PDEs on Neural Shape Representations** - Lilian Welschinger, Yilin Liu, Zican Wang et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.21311)]
- **Transolver++: An Accurate Neural Solver for PDEs on Million-Scale Geometries** - Huakun Luo, Haixu Wu, Hang Zhou et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2502.02414)]
- **Multi-patch isogeometric neural solver for partial differential equations on computer-aided design domains** - Moritz von Tresckow, Ion Gabriel Ion, Dimitrios Loukrezis. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.25450)]
- **Neural PDE Solvers with Physics Constraints** - Jiakang Chen. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.09693)]
- **Fourier Neural Operators Explained** - Valentin Duruisseaux, Jean Kossaifi, Anima Anandkumar. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.01421)]
- **Fourier-Embedded DeepONet for Spectrally Accurate Operator Learning** - Arth Sojitra, Mrigank Dhingra, Omer San. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.12344)]
- **Reduced Order Modeling of Energetic Materials Using Physics-Aware Recurrent Convolutional Neural Networks in a Latent Space (LatentPARC)** - Zoe J. Gray, Joseph B. Choi, Youngsoo Choi et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.12401)]
- **Neural operators for accelerating scientific simulations and design** - Kamyar Azizzadenesheli, Nikola Kovachki, Zongyi Li et al. *Nature Reviews Physics 2024*. [[Paper](https://doi.org/10.1038/s42254-024-00712-5)]
- **Learning nonlinear operators in latent spaces for real-time predictions of complex dynamics in physical systems** - Katiana Kontolati, Somdatta Goswami, George Em Karniadakis et al. *Nature Communications 2024*. [[Paper](https://doi.org/10.1038/s41467-024-49411-w)]
- **Finite Operator Learning: Bridging Neural Operators and Numerical Methods for Efficient Parametric Solution and Optimization of PDEs** - Shahed Rezaei, Reza Najian Asl, Kianoosh Taghikhani et al. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2407.04157)]
- **A Physics-Encoded Fourier Neural Operator Approach for Surrogate Modeling of Divergence-Free Stress Fields in Solids** - Khorrami et al.. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2408.15408)]
- **Shape-Informed Surrogate Models Based on Signed Distance Function Domain Encoding** - Linying Zhang, Stefano Pagani, Jun Zhang et al. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2409.12400)]
- **Graph convolutional network as a fast statistical emulator for numerical ice sheet modeling** - Maryam Rahnemoonfar, Younghyun Koo. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2402.05291)]
- **Unified Physics Transformers: A Framework For Efficiently Scaling Neural Operators** - Alkin et al.. *NeurIPS 2024*. [[Paper](https://arxiv.org/abs/2402.12365)]
- **G-Adaptivity: optimised graph-based mesh relocation for finite element methods** - James Rowbottom, Georg Maierhofer, Teo Deveney et al. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2407.04516)]
- **Deep Operator Network Based on Kolmogorov-Arnold Networks for Mechanics Problems** - Diab W. Abueidda, Panos Pantidis, Mostafa E. Mobasher. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2405.19143)]
- **Physics-informed Reduced Order Model with Conditional Neural Fields** - Minji Kim, Tianshu Wen, Kookjin Lee et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2412.05233)]
- **Convolutional Neural Network based Reduced Order Modeling for Multiscale Problems** - Xuhan Zhang, Lijian Jiang. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2406.16328)]
- **Latent Neural PDE Solver: a Reduced-Order Modelling Framework for Partial Differential Equations** - Zijie Li, Saurabh Patil, Francis Ogoke et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2402.17853)]
- **Learning Nonlinear Reduced Order Models using State-Space Neural Networks with Ordered State Variance** - Midhun T. Augustine, Mani Bhushan, Sharad Bhartiya. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2406.10359)]
- **An FEA Surrogate Model with Boundary Oriented Graph Embedding Approach for Rapid Design** - Xingyu Fu, Fengfeng Zhou, Dheeraj Peddireddy et al. *Journal of Computational Design and Engineering 2023*. [[Paper](https://arxiv.org/abs/2108.13509)]
- **Sequential Deep Operator Networks (S-DeepONet) for Predicting Full-Field Solutions Under Time-Dependent Loads** - Junyan He, Shashank Kushwaha, Jaewan Park et al. *arXiv preprint 2023*. [[Paper](https://arxiv.org/abs/2306.08218)]
- **Reduced-order Modeling for Parameterized PDEs via Implicit Neural Representations** - Tianshu Wen, Kookjin Lee, Youngsoo Choi. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2311.16410)]
- **Learning Deep Implicit Fourier Neural Operators (IFNOs) with Applications to Heterogeneous Material Modeling** - Huaiqian You, Quinn Zhang, Colton J. Ross et al. *CMAME 2022*. [[Paper](https://arxiv.org/abs/2203.08205)]
- **Toward Reusable Surrogate Models: Graph-Based Transfer Learning on Trusses** - Whalen et al.. *Journal of Mechanical Design 2022*. [[Paper](https://arxiv.org/abs/2109.02689)]
- **Fourier Neural Operator for Parametric Partial Differential Equations** - Li et al.. *ICLR 2021*. [[Paper](https://arxiv.org/abs/2010.08895)]
- **Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators** - Lu et al.. *Nature Machine Intelligence 2021*. [[Paper](https://doi.org/10.1038/s42256-021-00302-5)]

### Computational Fluid Dynamics

- **Faster by Design: Interactive Aerodynamics via Neural Surrogates Trained on Expert-Validated CFD** - Thumiger et al.. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.18491)]
- **A Forward Look on AI Foundation Models in Computational Fluid Dynamics** - Neil Ashton, Johannes Brandstetter, Siddhartha Mishra. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2511.20455)]
- **Accelerating Transient CFD through Machine Learning-Based Flow Initialization** - Peter Sharpe, Rishikesh Ranade, Kaustubh Tangsali et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2503.15766)]
- **Physics-Constrained DeepONet for Surrogate CFD Models** - Anas Jnini, Harshinee Goordoyal, Sujal Dave et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2503.11196)]
- **Physics-Based Simulations with Masked Graph Neural Networks** - Paul Garnier, Vincent Lannelongue, Jonathan Viquerat et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2501.08738)]
- **TripOptimizer: Generative 3D Shape Optimization and Drag Prediction using Triplane VAE Networks** - Parsa Vatani, Mohamed Elrefaie, Farhad Nazarpour et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.12224)]
- **Accelerating Shape Optimization by Deep Neural Networks with On-the-fly Determined Architecture** - Lucie Kubickova, Onrej Gebousky, Jan Haidl et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.03555)]
- **Surrogate-Based Differentiable Pipeline for Shape Optimization** - Andrin Rehmann, Nolan Black, Josiah Bjorgaard et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.10761)]
- **Neural Surrogate-assisted Glider Wing Design with Stability Analysis and Multi-method Optimization** - Arash Fath Lipaei, AmirHossein Ghaemi, Melika Sabzikari. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.08582)]
- **Data-Driven Turbulence Modeling: A Survey** - Paola Cinnella. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2404.09074)]
- **Turbulence closure modeling with machine learning approaches: A perspective** - Sharath S. Girimaji. *arXiv preprint 2023*. [[Paper](https://arxiv.org/abs/2312.14902)]
- **Neural Fields for Rapid Aircraft Aerodynamics Simulations** - Giovanni Catalani, Siddhant Agarwal, Xavier Bertrand et al. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2407.19916)]
- **Scalable Multi-Scale Graph Neural Networks for Physics Simulation** - Mohammad Amin Nabian, Chang Liu, Rishikesh Ranade et al. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2411.17164)]
- **A Graph Neural Network Surrogate Model for Multi-Objective Fluid-Acoustic Shape Optimization** - Farnoosh Hadizadeh, Wrik Mallik, Rajeev K. Jaiman. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2412.16817)]
- **A Mechanism-informed Reinforcement Learning Framework for Shape Optimization of Airfoils** - Jingfeng Wang, Guanghui Hu. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2403.04329)]
- **Discovering explicit Reynolds-averaged turbulence closures for turbulent separated flows through deep learning-based symbolic regression with non-linear corrections** - Hongwei Tang, Yan Wang, Tongguang Wang et al. *arXiv preprint 2023*. [[Paper](https://arxiv.org/abs/2301.09048)]
- **Learning Mesh-Based Simulation with Graph Networks** - Pfaff et al.. *ICLR 2021 (Outstanding Paper)*. [[Paper](https://arxiv.org/abs/2010.03409)]
- **The Neural Particle Method -- An Updated Lagrangian Physics Informed Neural Network for Computational Fluid Dynamics** - Henning Wessels, Christian Weienfels, Peter Wriggers. *arXiv preprint 2020*. [[Paper](https://arxiv.org/abs/2003.10208)]

### Physics-Informed Neural Networks

- **Equation Discovery, Parametric Simulation, and Optimization Using the Physics-Informed Neural Network (PINN) Method for the Heat Conduction Problem** - Ehsan Ghaderi, Mohamad Ali Bijarchi, Siamak Kazemzadeh Hannani et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2510.25925)]
- **PINNsAgent: Automated PDE Surrogation with Large Language Models** - Qingpo Wuwu, Chonghan Gao, Tianyu Chen et al. *ICML 2025*. [[Paper](https://arxiv.org/abs/2501.12053)]
- **Physics-Informed Diffusion Models** - Jan-Hendrik Bastek, WaiChing Sun, Dennis Kochmann. *ICLR 2025*. [[Paper](https://arxiv.org/abs/2403.14404)]
- **eXtended Physics-Informed Neural Network Method for Fracture Mechanics Problems** - Amin Lotfalian, Mohammad Reza Banan, Pooyan Broumand. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2509.13952)]
- **Physics-Informed Neural Operator for Learning Partial Differential Equations** - Li et al.. *ACM/JMS 2024*. [[Paper](https://arxiv.org/abs/2111.03794)]
- **Physics-Informed Neural Networks and Extensions: A Review** - Maziar Raissi, Paris Perdikaris, Nazanin Ahmadi et al. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2408.16806)]
- **Physics-Informed Neural Networks: From Fundamentals to Applications in Complex Systems** - Sai Ganga, Ziya Uddin. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2410.00422)]
- **Physics-informed neural networks for solving thermo-mechanics problems of functionally graded material** - Mayank Raj, Pramod Kumbhar, Ratna Kumar Annabattula. *arXiv preprint 2021*. [[Paper](https://arxiv.org/abs/2111.10751)]
- **Scientific Machine Learning Through Physics-Informed Neural Networks: Where We Are and What's Next** - Cuomo et al.. *Journal of Scientific Computing 2022*. [[Paper](http://arxiv.org/abs/2201.05624)]
- **Transfer Learning Based Physics-Informed Neural Networks for Solving Inverse Problems in Engineering Structures** - Chen Xu, Ba Trung Cao, Yong Yuan et al. *arXiv preprint 2022*. [[Paper](https://arxiv.org/abs/2205.07731)]
- **Physics-Informed Neural Networks (PINNs) for Heat Transfer Problems** - Cai et al.. *Journal of Heat Transfer 2021*. [[Paper](https://doi.org/10.1115/1.4050542)]
- **Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations** - Maziar Raissi, Paris Perdikaris, George Em Karniadakis. *Journal of Computational Physics 2019*. [[Paper](https://doi.org/10.1016/j.jcp.2018.10.045)]

### Deep Learning for Topology Optimization

- **Multiscale topology optimization of compressible and nearly incompressible anisotropic hyperelastic structures using physics-augmented neural networks** - Asghar A. Jadoon, Aryan Tyagi, L. River Spencer et al. *arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2604.06519)]
- **Physics-Informed Transformer for Real-Time High-Fidelity Topology Optimization** - Aaron Lutheran, Srijan Das, Alireza Tabarraei. *arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2604.03522)]
- **Variational Quantum Latent Encoding for Topology Optimization** - Alireza Tabarraei. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2506.17487)]
- **Transformer-Based Topology Optimization** - Aaron Lutheran, Srijan Das, Alireza Tabarraei. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2509.05800)]
- **A Foundation Model for Shape- and Resolution-Free Structural Topology Optimization** - Amin Heyrani Nobari, Lyle Regenwetter, Cyril Picard et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2510.23667)]
- **Latent Space Diffusion for Topology Optimization** - Aaron Lutheran, Srijan Das, Alireza Tabarraei. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2508.05624)]
- **Accelerating Metamaterial Topology Optimization Using Deep Super-Resolution Networks** - Ajendra Singh, Shubham Saurabh, Abhinav Gupta et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2511.04795)]
- **Diverse Topology Optimization Using Modulated Neural Fields (TOM)** - Andreas Radler, Eric Volkmann, Johannes Brandstetter et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2502.13174)]
- **Multi-scale Topology Optimization using Neural Networks** - Chen et al.. *SIGGRAPH 2024*. [[Paper](https://arxiv.org/abs/2404.08708)]
- **Consistent Machine Learning for Topology Optimization with Microstructure-Dependent Neural Network Material Models** - Harikrishnan Vijayakumaran, Jonathan B. Russ, Glaucio H. Paulino et al. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2408.13843)]
- **Neural Topology Optimization** - Suryanarayanan Manoj Sanu, Alejandro M. Aragon, Miguel A. Bessa. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2407.13954)]
- **A Dual Physics-Informed Neural Network for Topology Optimization (DPNN-TO)** - Ajendra Singh, Souvik Chakraborty, Rajib Chowdhury. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2410.14342)]
- **Gradient-Free Neural Topology Optimization** - Gawel Kus, Miguel A. Bessa. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2403.04937)]
- **Simultaneous and Meshfree Topology Optimization with Physics-Informed Gaussian Processes** - Amin Yousefpour, Shirin Hosseinmardi, Carlos Mora et al. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2408.03490)]
- **TopoDiff: Diffusion Models Beat GANs on Topology Optimization** - Maze and Ahmed. *AAAI 2023*. [[Paper](https://arxiv.org/abs/2208.09591)]
- **GANTL: Towards Practical and Real-Time Topology Optimization with Conditional GANs and Transfer Learning** - Mohammad Mahdi Behzadi, Horea Ilies. *Structural and Multidisciplinary Optimization 2022*. [[Paper](https://doi.org/10.1115/1.4052757)]
- **Accelerated Topology Optimization Design of 3D Structures Based on Deep Learning** - Xiang Cheng, Dalei Wang, Yue Pan et al. *Structural and Multidisciplinary Optimization 2022*. [[Paper](https://doi.org/10.1007/s00158-022-03194-0)]
- **TOuNN: Topology Optimization using Neural Networks** - Chandrasekhar and Suresh. *Structural and Multidisciplinary Optimization 2021*. [[Paper](https://doi.org/10.1007/s00158-020-02748-4)]

### Generative and LLM-Driven Topology Optimization

- **Multi-Material Multi-Physics Topology Optimization with Physics-Informed Gaussian Process Priors** - Xiangyu Sun, Shirin Hosseinmardi, Amin Yousefpour et al. *arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2602.17783)]
- **Toward Large Language Model-Driven Symbolic Topology Optimisation for Rapid Structural Concept Generation in Manufacturable Design** - Musaddiq Al Ali. *Journal of Manufacturing and Materials Processing 2026*. [[Paper](https://doi.org/10.3390/jmmp10040117)]
- **Using Hand-Drawn Inputs for Diffusion-Based Topology Optimization** - Shuyue Feng, Cedric Caremel, Yoshihiro Kawahara. *arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2603.18960)]
- **Censored Sampling for Topology Design: Guiding Diffusion with Human Preferences** - Euihyun Kim, Keun Park, Yeoneung Kim. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2508.01589)]
- **Two-Stage Multiobjective Topology Optimization Method via SwinUnet with Enhanced Generalization** - Xiang Cheng, Airong Chen, Hua Li et al. *Scientific Reports 2025*. [[Paper](https://doi.org/10.1038/s41598-025-92793-0)]
- **Diffusion Models for Topology Optimization in 3D Printing Applications** - Amanali Bekbolat, Syuhei KUROKAWA, Fadhlan Hafizhelmi Kamaruzaman et al. *Journal of Applied Physics 2025*. [[Paper](https://doi.org/10.1063/5.0246189)]
- **Multiphysics Design Optimization via Generative Adversarial Networks** - Hesaneh Kazemi, Carolyn Conner Seepersad, H. Alicia Kim. *Journal of Mechanical Design 2022*. [[Paper](https://doi.org/10.1115/1.4055377)]

### AI-Driven Generative Design

- **DUCTILE: Agentic LLM Orchestration of Engineering Analysis in Product Development Practice** - Alejandro Pradas-Gomez, Arindam Brahma, Ola Isaksson. *arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2603.10249)]
- **SimuAgent: An LLM-Based Simulink Modeling Assistant Enhanced with Reinforcement Learning** - Yanchang Liang, Xiaowei Zhao. *arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2601.05187)]
- **An LLM-Driven Multi-Agent Framework for Autonomous Construction of Deep Learning Surrogate Models in Subsurface Flow** - Jiale Liu, Nanzhe Wang. *arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2604.11945)]
- **Large Language Model-Empowered Next-Generation Computer-Aided Engineering** - Jiachen Guo, Chanwook Park, Dong Qian et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2509.11447)]
- **Automating Data-Driven Modeling and Analysis for Engineering Applications using Large Language Model Agents** - Yang Liu, Zaid Abulawi, Abhiram Garimidi et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2510.01398)]
- **Large Language Models for Combinatorial Optimization of Design Structure Matrix** - Shuo Jiang, Min Xie, Jianxi Luo. *ICED 2025*. [[Paper](https://arxiv.org/abs/2506.09749)]
- **Bayesian and Non-Bayesian Multi-Fidelity Surrogate Models for Multi-Objective Aerodynamic Optimization Under Extreme Cost Imbalance** - Marc Schouler, Anca Belme, Paola Cinnella. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2505.17279)]
- **Benchmarking Generative AI Against Bayesian Optimization for Constrained Multi-Objective Inverse Design** - Muhammad Bilal Awan, Abdul Razzaq, Abdul Shahid. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2511.00070)]
- **Towards Generative Design Using Optimal Transport for Shape Exploration and Solution Field Interpolation** - Sergio Torregrosa, David Munoz, Hector Navarro et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2511.17111)]
- **Accelerating Inverse Materials Design using Generative Diffusion Models with Reinforcement Learning** - Junwu Chen, Jeff Guo, Edvin Fako et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.03112)]
- **Heterogeneous Metamaterials Design via Multiscale Neural Implicit Representation** - Hongrui Chen, Liwei Wang, Levent Burak Kara. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.03012)]
- **Inverse Design of Metamaterials with Manufacturing-Guiding Spectrum-to-Structure Conditional Diffusion Model** - Li et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2506.07083)]
- **Algebraic Language Models for Inverse Design of Metamaterials via Diffusion Transformers** - Li Zheng, Siddhant Kumar, Dennis M. Kochmann. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2507.15753)]
- **Evaluation of Architectural Synthesis Using Generative AI** - Jingfei Huang, Alexandros Haridis. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.02861)]
- **An Evolutionary Multi-objective Optimization for Replica-Exchange-based Physics-informed Neural Operator Learning Networks** - Binghang Lu, Changhong Mou, Guang Lin. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.00663)]
- **Fast and Accurate Bayesian Optimization with Pre-trained Transformers for Constrained Engineering Problems** - Rosen, Yu, Cyril Picard et al. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2404.04495)]
- **Multi-Objective Generative Design Framework and Realization for Quasi-Serial Manipulator** - Sumin Lee, Sunwoong Yang, Namwoo Kang. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2402.00032)]
- **Generative Optimization: A Perspective on AI-Enhanced Problem Solving in Engineering** - Lyle Regenwetter, Cyril Picard, Amin Heyrani Nobari et al. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2412.13281)]
- **Generative AI-Based Prompt Evolution Engineering Design Optimization with Vision-Language Model** - Melvin Wong, Thiago Rios, Stefan Menzel et al. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2406.09143)]
- **An Uncertainty-aware Deep Learning Framework-based Robust Design Optimization of Metamaterial Units** - Zihan Wang, Anindya Bhaduri, Hongyi Xu et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2407.20251)]
- **Structural Design Through Reinforcement Learning** - Thomas Rochefort-Beaudoin, Aurelian Vadean, Niels Aage et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2407.07288)]
- **Differentiable Finite Element Analysis Solver for Structural Optimization and Seamless Integration with Neural Networks** - Gaoyuan Wu. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2407.20026)]
- **Real-time design of architectural structures with differentiable mechanics and neural networks** - Rafael Pastrana, Eder Medina, Isabel M. de Oliveira et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2409.02606)]
- **Data-Driven Design for Metamaterials and Multiscale Systems: A Review** - Doksoo Lee, Wei Wayne Chen, Liwei Wang et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2307.05506)]
- **Towards Goal, Feasibility, and Diversity-Oriented Deep Generative Models in Design** - Lyle Regenwetter, Faez Ahmed. *Journal of Mechanical Design 2022*. [[Paper](https://arxiv.org/abs/2206.07170)]
- **Evolving Through the Looking Glass: Learning Improved Search Spaces with Variational Autoencoders** - Peter J. Bentley, Soo Ling Lim, Adam Gaier et al. *Autodesk Research 2020*. [[Paper](https://doi.org/10.1007/978-3-031-14714-2_26)]

---

## Manufacturing-Aware Design

Design for manufacturing, additive manufacturing, assembly planning, and CAD/CAM integration.

**Representative anchors:** MeshCNN for mesh-based learning applicable to manufacturing; InverseCSG for reverse engineering; recent DfAM methods that integrate topology optimization with additive-manufacturing constraints.

### Design for Manufacturing (DFM)

- **Kolmogorov-Arnold Networks-Based Tolerance-Aware Manufacturability Assessment Integrating Design-for-Manufacturing Principles** - Masoud Deylami, Negar Izadipour, Adel Alaeddini. *arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2601.06334)]
- **Enhancing the Product Quality of the Injection Process Using eXplainable Artificial Intelligence** - Jisoo Hong, Yongmin Hong, Jung-Woo Baek et al. *arXiv preprint / Processes 2025*. [[Paper](https://arxiv.org/abs/2503.02338)]
- **Machine Learning-Based Manufacturing Cost Prediction from 2D Engineering Drawings via Geometric Features** - Ahmet Bilal Arkan, Sener Ozonder, Mustafa Taha Kocyigit et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2508.12440)]
- **Data-Driven Prediction of Casting Defects in Magnesium High-Pressure Die Casting Using Machine Learning** - Slava Pachandrin, Norbert Hoffmann, Klaus Dilger et al. *International Journal of Metalcasting 2025*. [[Paper](https://doi.org/10.1007/s40962-025-01592-w)]
- **An Artificial Intelligence Application for In-Process Springback Control of Sheet Metal Bending** - Kuang-Jau Fann, Li Chen, Chun-Yen Yang et al. *ASME J. Manufacturing Science and Engineering 2025*. [[Paper](https://doi.org/10.1115/1.4067740)]
- **DRL-Based Injection Molding Process Parameter Optimization for Adaptive and Profitable Production** - Joon-Young Kim, Jecheon Yu, Heekyu Kim et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2505.10988)]
- **Advancing Welding Defect Detection in Maritime Operations via Adapt-WeldNet** - Kamal Basha S, Athira Nambiar. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2508.00381)]
- **Adapting OpenAI's CLIP Model for Few-Shot Image Inspection in Manufacturing Quality Control: An Expository Case Study with Multiple Application Examples** - Fadel M. Megahed, Ying-Ju Chen, Bianca Maria Colosimo et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2501.12596)]
- **Fully-Synthetic Training for Visual Quality Inspection in Automotive Production** - Christoph Huber, Dino Knoll, Michael Guthe. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2503.09354)]
- **Material Combination Optimization for Brazed Ceramic-Metal Composites Using Artificial Intelligence** - Sunita Khod, Vinay Kamma, Ravi Kumar Verma et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2510.10128)]
- **Adapting OpenAI's CLIP Model for Few-Shot Image Inspection in Manufacturing Quality Control** - Fadel M. Megahed, Ying-Ju Chen, Bianca Maria Colosimo et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2501.12596)]
- **Critical Analysis and Best Practices for Visual Industrial Anomaly Detection** - Aimira Baitieva, Yacine Bouaouni, Alexandre Briot et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.23451)]
- **AI-Driven Multi-Stage Computer Vision System for Defect Detection in Laser-Engraved Industrial Nameplates** - Adhish Anitha Vilasan, Stephan Jager, Noah Klarmann. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.03395)]
- **A Comprehensive Survey for Real-World Industrial Defect Detection** - Yuqi Cheng, Yunkang Cao, Haiming Yao et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2507.13378)]
- **Improved Training Strategies for Physics-Informed Neural Networks using Real Experimental Data in Aluminum Spot Welding** - Jan A. Zak, Christian Weienfels. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.04595)]
- **Out of Distribution Detection for Efficient Continual Learning in Quality Prediction for Arc Welding** - Yannik Hahn, Jan Voets, Antonin Koenigsfeld et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.16832)]
- **Explainable AI for Correct Root Cause Analysis of Product Quality in Injection Moulding** - Muhammad Muaz, Sameed Sajid, Tobias Schulze et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.01445)]
- **Improving Industrial Injection Molding Processes with Explainable AI for Quality Classification** - Georg Rottenwalter, Marcel Tilly, Victor Owolabi. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.08108)]
- **Automated Plan Refinement for Improving Efficiency of Robotic Layup of Composite Sheets** - Rutvik Patel, Alec Kanyuck, Zachary McNulty et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2506.18160)]
- **Deep Operator Learning with Domain-informed Features for Fatigue Life Prediction** - Chenyang Li, Tanmay Sunil Kapure, Prokash Chandra Roy et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.22475)]
- **A Certifiable Machine Learning-Based Pipeline to Predict Fatigue Life of Aircraft Structures** - Angel Ladron, Miguel Sanchez-Dominguez, Javier Rozalen et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.10227)]
- **Physics-based Machine Learning for Fatigue Lifetime Prediction under Non-uniform Loading Scenarios** - Abedulgader Baktheer, Fadi Aldakheel. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.05419)]
- **Predictive Modeling and Uncertainty Quantification of Fatigue Life in Metal Alloys using Machine Learning** - Jiang Chang, Deekshith Basvoju, Aleksandar Vakanski et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2501.15057)]
- **Toward Knowledge-Guided AI for Inverse Design in Manufacturing** - Hugon Lee, Hyeonbin Moon, Junhyeong Lee et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2506.00056)]
- **Deep Generative Design for Mass Production** - Kim et al.. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2403.12098)]
- **McGAN: Generating Manufacturable Designs by Embedding Manufacturing Rules into Conditional Generative Adversarial Network** - Zhichao Wang, Xiaoliang Yan, Shreyes Melkote et al. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2407.16943)]
- **Springback prediction using machine learning: an application for simplified automotive body-in-white structures** - Satchit Ramnath, Alex Adrian, Abhishek Bolar et al. *NSF PAR 2024*. [[Paper](https://doi.org/10.1007/s00170-025-15958-1)]
- **Unsupervised Welding Defect Detection Using Audio and Video** - Georg Stemmer, Jose A. Lopez, Juan A. Del Hoyo Ontiveros et al. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2409.02290)]
- **Evaluating Vision Transformer Models for Visual Quality Control in Industrial Manufacturing** - Miriam Alber, Christoph Hones, Patrick Baier. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2411.14953)]
- **Multimodal Object Detection using Depth and Image Data for Manufacturing Parts** - Nazanin Mahjourian, Vinh Nguyen. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2411.09062)]
- **Advancements in Point Cloud-Based 3D Defect Detection and Classification for Industrial Systems** - Anju Rani, Daniel Ortiz-Arroyo, Petar Durdevic. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2402.12923)]
- **Single and Multi-Objective Real-Time Optimisation of an Industrial Injection Moulding Process via Bayesian Adaptive Design of Experiment** - Mandana Kariminejad, David Tormey, Caitriona Ryan et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2402.12077)]
- **Graph Neural Networks for Scalable Prediction of Grain-Level Fatigue Indicator Parameters** - Gyu-Jang Sim, Myoung-Gyu Lee, Marat I. Latypov. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2406.08682)]
- **Real-time prediction and adaptive adjustment of continuous casting based on deep learning** - Ziqing Lu, Neng Ren, Xiaowei Xu et al. *Communications Engineering (Nature) 2023*. [[Paper](https://doi.org/10.1038/s44172-023-00084-1)]
- **Hybrid Deep Learning Cost Evaluation Using CNN with ANN for the Plastic Injection Industry** - Athakorn Kengpol, Pornthip Tabkosai. *Neural Computing and Applications 2023*. [[Paper](https://doi.org/10.1007/s00521-023-08947-6)]
- **An Incremental Unified Framework for Small Defect Inspection** - Jiaqi Tang, Hao Lu, Xiaogang Xu et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2312.08917)]
- **Towards a Deep Learning-based Online Quality Prediction System for Welding Processes** - Yannik Hahn, Robert Maack, Guido Buchholz et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2310.12632)]
- **Investigating the ability of deep learning to predict Welding Depth and Pore Volume in Hairpin Welding** - Amena Darwish, Stefan Ericson, Rohollah Ghasemi et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2312.01606)]
- **Surrogate Modelling for Injection Molding Processes Using Machine Learning** - Arsenii Uglov, Sergei Nikolaev, Sergei Belov et al. *arXiv preprint 2021*. [[Paper](https://arxiv.org/abs/2107.14574)]
- **Deep Neural Networks based Predictive-Generative Framework for Designing Composite Materials** - Ashank, Soumen Chakravarty, Pranshu Garg et al. *arXiv 2021*. [[Paper](https://arxiv.org/abs/2105.01384)]
- **Explainable Artificial Intelligence for Manufacturing Cost Estimation and Machining Feature Visualization** - Soyoung Yoo, Namwoo Kang. *arXiv preprint 2020*. [[Paper](https://arxiv.org/abs/2010.14824)]
- **A Machine-Learning Framework for Design for Manufacturability** - Aditya Balu, Sambit Ghadai, Gavin Young et al. *arXiv preprint 2017*. [[Paper](https://arxiv.org/abs/1703.01499)]
- **Learning Localized Geometric Features Using 3D-CNN: An Application to Manufacturability Analysis of Drilled Holes** - Aditya Balu, Sambit Ghadai, Kin Gwn Lore et al. *arXiv preprint 2016*. [[Paper](https://arxiv.org/abs/1612.02141)]

### Design for Additive Manufacturing (DFAM)

- **Discovery of Feasible 3D Printing Configurations for Metal Alloys via AI-Driven Adaptive Experimental Design** - Azza Fadhel, Nathaniel W. Zuckschwerdt, Aryan Deshwal et al. *arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2601.17587)]
- **Graph Neural Network-Based Topology Optimization for Self-Supporting Structures in Additive Manufacturing** - Alireza Tabarraei, Saquib Ahmad Bhuiyan. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2508.19169)]
- **Generative Artificial Intelligence in Lattice Structure Design for Additive Manufacturing: A Critical Review** - Jinlong Su, Y. L. Mo, Swee Leong Sing. *eScience of Additive Manufacturing 2025*. [[Paper](https://doi.org/10.36922/esam025110006)]
- **Additive Manufacturing Processes Protocol Prediction by Artificial Intelligence using X-ray Computed Tomography Data** - Sunita Khod, Akshay Dvivedi, Mayank Goswami. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2501.14306)]
- **Sample-Efficient Bayesian Transfer Learning for Online Machine Parameter Optimization** - Philipp Wagner, Tobias Nagel, Philipp Leube et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2503.15928)]
- **Real-Time Decision-Making for Digital Twin in Additive Manufacturing with Model Predictive Control** - Yi-Ping Chen, Vispi Karkaria, Ying-Kuan Tsai et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2501.07601)]
- **Digital Twin Synchronization: Bridging the Sim-RL Agent to a Real-Time Robotic Additive Manufacturing Control** - Matsive Ali, Sandesh Giri, Sen Liu et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2501.18016)]
- **Computational, Data-Driven, and Physics-Informed Machine Learning Approaches for Microstructure Modeling in Metal Additive Manufacturing** - D. Patel, R. Sharma, Y. B. Guo. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2505.01424)]
- **Multimodal Learning of Melt Pool Dynamics in Laser Powder Bed Fusion** - Satyajit Mojumder, Pallock Halder, Tiana Tonge. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.03029)]
- **An Efficient and Uncertainty-aware Reinforcement Learning Framework for Quality Assurance in Extrusion Additive Manufacturing** - Li et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.00971)]
- **Learning Actionable World Models for Industrial Process Control** - Peng Yan, Ahmed Abdulkadir, Gerrit A. Schatte et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.01411)]
- **Advancing Additive Manufacturing through Deep Learning: A Comprehensive Review of Current Progress and Future Challenges** - Amirul Islam Saimon, Emmanuel Yangue, Xiaowei Yue et al. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2403.00669)]
- **Learn to Rotate: Part Orientation for Reducing Support Volume via Generalizable Reinforcement Learning** - Peizhi Shi, Qunfen Qi, Yuchu Qin et al. *University of Huddersfield 2024*. [[Paper](https://doi.org/10.1109/tii.2023.3249751)]
- **Multiscale Topology Optimization of Functionally Graded Lattice Structures Based on Physics-Augmented Neural Network Material Models** - Jonathan Stollberg, Tarun Gangwar, Oliver Weeger et al. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2408.00510)]
- **LatticeGraphNet: A Two-Scale Graph Neural Operator for Simulating Lattice Structures** - Ayush Jain, Ehsan Haghighat, Sai Nelaturi. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2402.01045)]
- **Deep Learning for Melt Pool Depth Contour Prediction From Surface Thermal Images via Vision Transformers** - Francis Ogoke, Peter Myung-Won Pak, Alexander Myers et al. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2404.17699)]
- **Holistic Review on Design for Additive Manufacturing** - Sakthivel Murugan R., S. Vinodh. *Progress in Additive Manufacturing (Springer) 2024*. [[Paper](https://doi.org/10.1007/s40964-024-00887-4)]
- **An Additive Manufacturing Optimal Control Framework Demonstrated in Minimizing Layer-Level Thermal Variance in Electron Beam Powder Bed Fusion** - Mikhail Khrenov, William Frieden Templeton, Sneha Prabha Narra. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2406.07408)]
- **LLM-3D Print: Large Language Models to Monitor and Control 3D Printing** - Yayati Jadhav, Peter Pak, Amir Barati Farimani. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2408.14307)]
- **Deep Neural Operator Enabled Digital Twin Modeling for Additive Manufacturing** - Ning Liu, Xuxiao Li, Manoj R. Rajanna et al. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2405.09572)]
- **Towards Reproducible Machine Learning-based Process Monitoring and Quality Prediction Research for Additive Manufacturing** - Jiarui Xie, Mutahar Safdar, Andrei Mircea et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2407.04031)]
- **In-situ Process Monitoring and Adaptive Quality Enhancement in Laser Additive Manufacturing** - Lequn Chen, Guijun Bi, Xiling Yao et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2404.13673)]
- **Deep Learning based Optical Image Super-Resolution via Generative Diffusion Models for Layerwise in-situ LPBF Monitoring** - Francis Ogoke, Sumesh Kalambettu Suresh, Jesse Adamczyk et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2409.13171)]
- **Sparse Attention-driven Quality Prediction for Production Process Optimization in Digital Twins** - Yanlei Yin, Lihua Wang, Dinh Thai Hoang et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2405.11895)]
- **Digital Twins in Additive Manufacturing: A Systematic Review** - Md Manjurul Ahsan, Yingtao Liu, Shivakumar Raman et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2409.00877)]
- **Investigation on Domain Adaptation of Additive Manufacturing Monitoring Systems to Enhance Digital Twin Reusability** - Jiarui Xie, Zhuo Yang, Chun-Chun Hu et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2409.12785)]
- **Concurrent Build Direction, Part Segmentation, and Topology Optimization for Additive Manufacturing Using Neural Networks** - Hongrui Chen, Aditya Joglekar, Kate S. Whitefoot et al. *ASME J. Mechanical Design 2023*. [[Paper](https://arxiv.org/abs/2210.01315)]
- **Predictive Modeling of Lattice Structure Design for 316L Stainless Steel Using Machine Learning in the L-PBF Process** - Karim Asami, S. Roth, Michel Krukenberg et al. *Journal of Laser Applications 2023*. [[Paper](https://doi.org/10.2351/7.0001174)]
- **Computational Discovery of Microstructured Composites with Optimal Stiffness-Toughness Trade-Offs** - Beichen Li, Bolei Deng, Wan Shou et al. *Science Advances 2023*. [[Paper](https://arxiv.org/abs/2302.01078)]
- **A Reinforcement Learning Approach for Process Parameter Optimization in Additive Manufacturing** - Susheel Dharmadhikari, Nandana Menon, Amrita Basak. *arXiv preprint 2022*. [[Paper](https://arxiv.org/abs/2211.09545)]
- **Accelerated Discovery of 3D Printing Materials Using Data-Driven Multiobjective Optimization** - Timothy Erps, Michael Foshey, Mina Konakovic Lukovic et al. *Science Advances 2021*. [[Paper](https://doi.org/10.1126/sciadv.abf7435)]
- **Self-supporting Topology Optimization for Additive Manufacturing** - Dengyang Zhao, Ming Li, Yusheng Liu. *arXiv preprint 2017*. [[Paper](https://arxiv.org/abs/1708.07364)]

### Assembly Planning and Tolerance

- **Learning-Based Strategy for Composite Robot Assembly Skill Adaptation** - Khalil Abuibaid, Aleksandr Sidorenko, Achim Wagner et al. *arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2604.06949)]
- **Connector-Aware General Robotic Assembly from Instruction Manuals via Vision-Language Models** - Chenrui Tie, Shengxiang Sun, Yudi Lin et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2510.16344)]
- **AssemMate: Graph-Based LLM for Robotic Assembly Assistance** - Qi Zheng, Chaoran Zhang, Zijian Liang et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2509.11617)]
- **Fabrica: Dual-Arm Assembly of General Multi-Part Objects via Integrated Planning and Learning** - Tian et al.. *CoRL 2025 (Best Paper Award)*. [[Paper](https://arxiv.org/abs/2506.05168)]
- **Hierarchical Hybrid Learning for Long-Horizon Contact-Rich Robotic Assembly** - Sun et al.. *CoRL 2025*. [[Paper](https://arxiv.org/abs/2409.16451)]
- **REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly** - Daniel Sliwowski, Shail Jadav, Sergej Stanovcic et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2502.05086)]
- **Tolerance Allocation of Complex Systems Based on Supervised Machine Learning and Adaptive Sampling** - Jean-Yves Dantan, Wahb Zouhri. *International Journal of Advanced Manufacturing Technology 2025*. [[Paper](https://doi.org/10.1007/s00170-025-17336-3)]
- **Contact-Rich Robotic Assembly in Construction via Diffusion Policy Learning** - Salma Mozaffari, Daniel Ruan, William van den Bogert et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2511.17774)]
- **Query-Centric Diffusion Policy for Generalizable Robotic Assembly** - Ziyi Xu, Haohong Lin, Shiqi Liu et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2509.18686)]
- **Planning for Multi-Robot Reaching with Graph Neural Networks and Reinforcement Learning** - Matthew Lai, Keegan Go, Zhibin Li et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.05397)]
- **Robotic Grinding Skills Learning Based on Geodesic Length Dynamic Motion Primitives** - Shuai Ke, Huan Zhao, Xiangfei Li et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2504.17216)]
- **Physics-Aware Combinatorial Assembly Sequence Planning using Data-free Action Masking** - Ruixuan Liu, Alan Chen, Weiye Zhao et al. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2408.10162)]
- **3D Combinatorial Construction with Deep Reinforcement Learning** - Alan Chen, Changliu Liu. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2410.15469)]
- **Learning to Generate Fine-Grained Robotic Assembly Instructions from Multi-View Images** - Hongyu Yan, Yadong Mu. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2404.16423)]
- **From Imitation to Refinement: Residual RL for Precise Visual Assembly** - Lars Ankile, Anthony Simeonov, Idan Shenfeld et al. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2407.16677)]
- **Stackelberg Game-Theoretic Learning for Collaborative Assembly Task Planning** - Yuhan Zhao, Lan Shi, Quanyan Zhu. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2404.12570)]
- **Data-Efficient Imitation Learning for Robotic Assembly** - Lars Ankile, Anthony Simeonov, Idan Shenfeld et al. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2404.03729)]
- **On the Role of Artificial Intelligence Methods in Modern Force-Controlled Manufacturing Robotic Tasks** - Vincenzo Petrone, Enrico Ferrentino, Pasquale Chiacchio. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2409.16828)]
- **RoboGrind: Intuitive and Interactive Surface Treatment with Industrial Robots** - Alt et al.. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2402.16542)]
- **GRACE: Efficient and Feasible Robotic Assembly Sequence Planning via Graph Representation Learning** - Matan Atad, Jianxiang Feng, Ismael Rodriguez et al. *ICRA 2024*. [[Paper](https://arxiv.org/abs/2303.10135)]
- **Deep Reinforcement Learning Applied to an Assembly Sequence Planning Problem with User Preferences** - Miguel Neves, Pedro Neto. *arXiv preprint 2023*. [[Paper](https://arxiv.org/abs/2304.06567)]
- **ASAP: Automated Sequence Planning for Complex Robotic Assembly with Physical Feasibility** - Yunsheng Tian, Karl D. D. Willis, Bassel Al Omari et al. *arXiv preprint 2023*. [[Paper](https://arxiv.org/abs/2309.16909)]
- **Optimal Robotic Assembly Sequence Planning: A Sequential Decision-Making Approach** - Kartik Nagpal, Negar Mehr. *arXiv preprint 2023*. [[Paper](https://arxiv.org/abs/2310.17115)]
- **Genetic Algorithm Optimization Based on Manufacturing Prediction for an Efficient Tolerance Allocation Approach** - Maroua Ghali, Sami Elghali, Nizar Aifaoui. *Journal of Intelligent Manufacturing 2023*. [[Paper](https://doi.org/10.1007/s10845-023-02132-1)]
- **Large-Scale Multi-Robot Assembly Planning for Autonomous Manufacturing** - Kyle Brown, Dylan M. Asmar, Mac Schwager et al. *arXiv preprint 2023*. [[Paper](https://arxiv.org/abs/2311.00192)]
- **Statistical Tolerance Allocation Design Considering Form Errors Based on Rigid Assembly Simulation and Deep Q-Network** - Ci He, Shuyou Zhang, Lemiao Qiu et al. *International Journal of Advanced Manufacturing Technology 2021*. [[Paper](https://doi.org/10.1007/s00170-020-06283-w)]

### CAD/CAM Integration

- **Self-Supervised Masked BRep Autoencoders for Machining Feature Recognition** - Can Yao, Kang Wu, Zuheng Zheng et al. *arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2602.22701)]
- **DeepMill: Neural Accessibility Learning for Subtractive Manufacturing** - Fanchao Zhong, Yang Wang, Peng-Shuai Wang et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2502.06093)]
- **Implicit Neural Field-Based Process Planning for Multi-Axis Manufacturing** - Neelotpal Dutta, Tianyu Zhang, Tao Liu et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2511.17578)]
- **Knowledge Graph Fusion with Large Language Models for Accurate, Explainable Manufacturing Process Planning** - Danny Hoang, David Gorsich, Matthew P. Castanier et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2506.13026)]
- **Implicit Neural Fields for Collision-Free Multi-Axis 3D Printing** - Jiasheng Qu, Zhuo Huang, Dezhao Guo et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2509.05345)]
- **A Cutting Mechanics-Based Machine Learning Modeling Method to Discover Governing Equations of Machining Dynamics** - Alisa Ren, Mason Ma, Jiajie Wu et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2501.14817)]
- **Deep Neural Implicit Representation of Accessibility for Multi-Axis Manufacturing** - George P. Harabin, Amir Mirzendehdel, Morad Behandish. *Computer-Aided Design 2024*. [[Paper](https://arxiv.org/abs/2409.02115)]
- **Automatic Feature Recognition and Dimensional Attributes Extraction From CAD Models for Hybrid Additive-Subtractive Manufacturing** - Muhammad Tayyab Khan, Wenhe Feng, Lequn Chen et al. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2408.06891)]
- **BrepMFR: Enhancing Machining Feature Recognition in B-rep Models through Deep Learning and Domain Adaptation** - Zhang et al.. *Computer Aided Geometric Design 2024*. [[Paper](https://doi.org/10.1016/j.cagd.2024.102318)]
- **BRepGAT: Graph Neural Network to Segment Machining Feature Faces in a B-rep Model** - Jinwon Lee, Changmo Yeo, Sang-Uk Cheon et al. *ResearchGate / Journal 2024*. [[Paper](https://doi.org/10.1093/jcde/qwad106)]
- **Real-Time Tool-Path Planning Using Deep Learning for Subtractive Manufacturing** - Yifei Feng, Hong-Yu Ma, LiYong Shen et al. *ResearchGate / Journal 2024*. [[Paper](https://doi.org/10.1109/tii.2023.3342474)]
- **Large Language Models for Manufacturing** - Yiwei Li, Huaqin Zhao, Hanqi Jiang et al. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2410.21418)]
- **Co-Optimization of Tool Orientations, Kinematic Redundancy, and Waypoint Timing for Robot-Assisted Manufacturing** - Yongxue Chen, Tianyu Zhang, Yuming Huang et al. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2409.13448)]
- **Learning-Based Toolpath Planner on Diverse Graphs for 3D Printing** - Yuming Huang, Yuhu Guo, Renbo Su et al. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2408.09198)]
- **Reinforcement Learning-Based Cutting Parameter Dynamic Decision Method Considering Tool Wear for a Turning Machining Process** - Xikun Zhao, Congbo Li, Ying Tang et al. *International Journal of Precision Engineering and Manufacturing-Green Technology 2023*. [[Paper](https://doi.org/10.1007/s40684-023-00582-9)]
- **Making Informed Decisions in Cutting Tool Maintenance in Milling** - Revati M. Wahul, Aditya M. Rahalkar, Om M. Khare et al. *arXiv preprint 2023*. [[Paper](https://arxiv.org/abs/2310.14629)]
- **Data-driven Modelling of Machine Tool Feedrate Behavior with Neural Networks** - Chao Sun, Javier Dominguez-Caballero, Rob Ward et al. *arXiv preprint 2021*. [[Paper](https://arxiv.org/abs/2106.09719)]

---

## Challenges and Future Directions

Papers analyzing open problems, technical challenges, and long-term research directions for AI in CAD.

### Data and Representation Challenges

- **DreamCAD: Scaling Multi-modal CAD Generation using Differentiable Parametric Surfaces** - Khan et al.. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.05607)]
- **CADEvolve: Creating Realistic CAD via Program Evolution** - Elistratov et al.. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.16317)]
- **Learning From Design Procedure To Generate CAD Programs for Data Augmentation** - Chen et al.. *NeurIPS 2025 Workshop*. [[Paper](https://arxiv.org/abs/2603.06894)]
- **GenCAD-3D: CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing** - Yu et al.. *ASME J. Mechanical Design 2025*. [[Paper](https://arxiv.org/abs/2509.15246)]
- **CADmium: Fine-Tuning Code Language Models for Text-Driven Sequential CAD Design** - Govindarajan et al.. *TMLR 2026*. [[Paper](https://arxiv.org/abs/2507.09792)]

### Technical Challenges

- **Mamba-CAD: State Space Model For 3D Computer-Aided Design Generative Modeling** - Li et al.. *AAAI 2025*. [[Paper](https://arxiv.org/abs/2603.00439)]
- **GeoFusion-CAD: Structure-Aware Diffusion with Geometric State Space for Parametric 3D Design** - Zhou et al.. *CVPR 2026*. [[Paper](https://arxiv.org/abs/2603.21978)]
- **ArtiCAD: Articulated CAD Assembly Design via Multi-Agent Code Generation** - Shui et al.. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.10992)]
- **MamTiff-CAD: Multi-Scale Latent Diffusion with Mamba+ for Complex Parametric Sequence** - Deng et al.. *ICCV 2025*. [[Paper](https://arxiv.org/abs/2511.17647)]
- **Aligning Constraint Generation with Design Intent in Parametric CAD** - Casey et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2504.13178)]
- **RLCAD: Reinforcement Learning Training Gym for Revolution Involved CAD Command Sequence Generation** - Yin et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.18549)]

### Engineering and Deployment Challenges

- **neuralCAD-Edit: An Expert Benchmark for Multimodal-Instructed 3D CAD Model Editing** - Perrett et al.. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.16170)]
- **Toward AI-driven Multimodal Interfaces for Industrial CAD Modeling** - Choi et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.16824)]
- **From Intent to Execution: Multimodal Chain-of-Thought Reinforcement Learning for Precise CAD Code Generation** - Niu et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.10118)]

### Ecosystem Challenges

- **Human-in-the-Loop: Quantitative Evaluation of 3D Models Generation by Large Language Models** - Sadik et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.07010)]
- **3DGen-Bench: Comprehensive Benchmark Suite for 3D Generative Models** - Zhang et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.21745)]

### Near-Term Directions

- **Agent-Aided Design for Dynamic CAD Models** - Adler et al.. *CAIS 2026*. [[Paper](https://arxiv.org/abs/2604.15184)]
- **BrepCoder: A Unified Multimodal Large Language Model for Multi-task B-rep Reasoning** - Kim et al.. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.22284)]
- **cadrille: Multi-modal CAD Reconstruction with Online Reinforcement Learning** - Kolodiazhnyi et al.. *ICLR 2026 (Oral)*. [[Paper](https://arxiv.org/abs/2505.22914)]
- **CADFusion: Text-to-CAD Generation Through Infusing Visual Feedback in Large Language Models** - Wang et al.. *ICML 2025*. [[Paper](https://arxiv.org/abs/2501.19054)]
- **CAD-GPT: Synthesising CAD Construction Sequence with Spatial Reasoning-Enhanced Multimodal LLMs** - Wang et al.. *AAAI 2025*. [[Paper](https://arxiv.org/abs/2412.19663)]
- **CADDreamer: CAD Object Generation from Single-view Images** - Li et al.. *CVPR 2025*. [[Paper](https://arxiv.org/abs/2502.20732)]
- **CAD-Assistant: Tool-Augmented VLLMs as Generic CAD Task Solvers** - Mallis et al.. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2412.13810)]

### Mid-Term Directions

- **VideoCAD: A Dataset and Model for Learning Long-Horizon 3D CAD UI Interactions from Video** - Man et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.24838)]
- **QueryCAD: Grounded Question Answering for CAD Models** - Kienle et al.. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2409.08704)]

### Long-Term Vision

- **The Dawn of Agentic EDA: A Survey of Autonomous Digital Chip Design** - Zang et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.23189)]
- **Intelligent CAD 2.0** - Zou et al.. *Visual Informatics 2024*. [[Paper](https://arxiv.org/abs/2410.03759)]

---

## Datasets and Benchmarks

Major datasets and benchmarks used across the AI for CAD research community.

### Dataset Papers

- **Zero-to-CAD: Agentic Synthesis of Interpretable CAD Programs at Million-Scale Without Real Data** - Mohammadmehdi Ataei, Farzaneh Askari, Kamal Rahimi Malekshan et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.24479)]
- **Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding** - Aleksei Kondratenko, Mussie Birhane, Houssame E. Hsain et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.04819)]
- **HistCAD: A Constraint-Aware Parametric History-Based CAD Representation, Dataset, and Benchmark with Industrial Complexity** - Xintong Dong, Chuanyang Li, Peng Zheng et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2602.19171)]
- **Objaverse++: Curated 3D Object Dataset with Quality Annotations** - Chendi Lin, Heshan Liu, Qunshu Lin et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2504.07334)]
- **ArchCAD-400K: A Large-Scale CAD drawings Dataset and New Baseline for Panoptic Symbol Spotting** - Ruifeng Luo, Zhengjie Liu, Tianxiao Cheng et al. *NeurIPS 2025*. [[Paper](https://arxiv.org/abs/2503.22346)]
- **Enginuity: Building an Open Multi-Domain Dataset of Complex Engineering Diagrams** - Ethan Seefried, Prahitha Movva, Naga Harshita Marupaka et al. *NeurIPS 2025*. [[Paper](https://arxiv.org/abs/2601.13299)]
- **VideoCAD: A Dataset and Model for Learning Long-Horizon 3D CAD UI Interactions from Video** - Brandon Man, Ghadi Nehme, Md Ferdous Alam et al. *NeurIPS 2025*. [[Paper](https://arxiv.org/abs/2505.24838)]
- **SldprtNet: A Large-Scale Multimodal Dataset for CAD Generation in Language-Driven 3D Design** - Ruogu Li, Sikai Li, Yao Mu et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.13098)]
- **A Cascade MAR with Topology Predictor for Multimodal Conditional CAD Generation** - Jianyu Wu, Yizhou Wang, Xiangyu Yue et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2504.20830)]
- **mrCAD: Multimodal Refinement of Computer-aided Designs** - McCarthy et al.. *EMNLP 2025 Findings*. [[Paper](https://arxiv.org/abs/2504.20294)]
- **Reinforcement Learning Training Gym for Revolution Involved CAD Command Sequence Generation** - Yin et al.. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.18549)]
- **Synthetic Generation Tool of Digital Measurement Device CAD Model Datasets for Fine-tuning Large Vision-Language Models** - Joao Valente, Atabak Dehban, Rodrigo Ventura. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.21732)]
- **A Large-Scale CAD Drawings Dataset and New Baseline for Panoptic Symbol Spotting** - Ruifeng Luo, Zhengjie Liu, Tianxiao Cheng et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.22346)]
- **IEC3D-AD: A 3D Dataset of Industrial Equipment Components for Unsupervised Point Cloud Anomaly Detection** - Bingyang Guo, Hongjie Li, Ruiyun Yu et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.03267)]
- **CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM** - Xu et al.. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2411.04954)]
- **Text2CAD: Generating Sequential CAD Models from Beginner-to-Expert Level Text Prompts** - Khan et al.. *NeurIPS 2024 Spotlight*. [[Paper](https://arxiv.org/abs/2409.17106)]
- **Slice-100K: A Multimodal Dataset for Extrusion-based 3D Printing** - Anushrut Jignasu, Kelly O. Marshall, Ankush Kumar Mishra et al. *NeurIPS 2024 D&B Track*. [[Paper](https://arxiv.org/abs/2407.04180)]
- **From Engineering Diagrams to Graphs** - Jan Marius Sturmer, Marius Graumann, Tobias Koch. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2411.13929)]
- **Objaverse: A Universe of Annotated 3D Objects** - Deitke et al.. *CVPR 2023*. [[Paper](https://arxiv.org/abs/2212.08051)]
- **Objaverse-XL: A Universe of 10M+ 3D Objects** - Deitke et al.. *NeurIPS 2023*. [[Paper](https://arxiv.org/abs/2307.05663)]
- **DeepPatent2: A Large-Scale Benchmarking Corpus for Technical Drawing Understanding** - Kehinde Ajayi, Xin Wei, Martin Gryder et al. *Scientific Data 2023*. [[Paper](https://arxiv.org/abs/2311.04098)]
- **FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting** - Fan et al.. *ICCV 2021 / TPAMI 2022*. [[Paper](https://arxiv.org/abs/2105.07147)]
- **DeepCAD: A Deep Generative Network for Computer-Aided Design Models** - Wu et al.. *ICCV 2021*. [[Paper](https://arxiv.org/abs/2105.09492)]
- **Fusion 360 Gallery: A Dataset and Environment for Programmatic CAD Construction from Human Design Sequences** - Willis et al. *SIGGRAPH 2021*. [[Paper](https://arxiv.org/abs/2010.02392)]
- **AutoMate: A Dataset and Learning Approach for Automatic Mating of CAD Assemblies** - Jones et al.. *SIGGRAPH 2021*. [[Paper](https://arxiv.org/abs/2105.12238)]
- **Synthetic 3D Data Generation Pipeline for Geometric Deep Learning in Architecture** - Stanislava Fedorova, Alberto Tono, Meher Shashwat Nigam et al. *arXiv 2021*. [[Paper](https://arxiv.org/abs/2104.12564)]
- **SketchGraphs: A Large-Scale Dataset for Modeling Relational Geometry in Computer-Aided Design** - Seff et al.. *ICML 2020 Workshop*. [[Paper](https://arxiv.org/abs/2007.08506)]
- **A Large-Scale Annotated Mechanical Components Benchmark for Classification and Retrieval Tasks with Deep Neural Networks** - Kim et al.. *ECCV 2020*. [[Paper](https://doi.org/10.1007/978-3-030-58523-5_11)]
- **MFCAD: A Dataset of 3D CAD Models with Machining Feature Labels** - Cao et al.. *CAD Journal 2020*. [[Paper](https://github.com/hducg/MFCAD)]
- **ABC: A Big CAD Model Dataset For Geometric Deep Learning** - Koch et al.. *CVPR 2019*. [[Paper](https://arxiv.org/abs/1812.06216)]
- **ShapeNet: An Information-Rich 3D Model Repository** - Chang et al.. *arXiv 2015*. [[Paper](https://arxiv.org/abs/1512.03012)]
- **3D ShapeNets: A Deep Representation for Volumetric Shapes** - Wu et al.. *CVPR 2015*. [[Paper](https://arxiv.org/abs/1406.5670)]
- **SESYD: A Synthetic Document Database for Performance Evaluation** - Delalandre et al.. *DAS 2010*. [[Paper](http://mathieu.delalandre.free.fr/projects/sesyd/)]

### Evaluation Metrics

- **Quantitative Evaluation of 3D Models Generation by Large Language Models** - Ahmed R. Sadik, Mariusz Bujny. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.07010)]
- **CAD-Judge: Toward Efficient Morphological Grading and Verification for Text-to-CAD Generation** - Zheyuan Zhou, Jiayi Han, Liang Du et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.04002)]
- **Generating CAD Code with Vision-Language Models for 3D Designs** - Kamel Alrashedy, Pradyumna Tambwekar, Zulfiqar Zaidi et al. *ICLR 2025*. [[Paper](https://arxiv.org/abs/2410.05340)]
- **Advancing 3D Generation Evaluation with Hierarchical Validity** - Yuhan Zhang, Long Zhuo, Ziyang Chu et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.05609)]
- **CadVLM: Bridging Language and Vision in the Generation of Parametric CAD Sketches** - Sifan Wu, Amir Khasahmadi, Mor Katz et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2409.17457)]

### Benchmark Challenges

- **CAD Arena: Open Benchmark for AI-Generated Parametric CAD** - CAD Arena Team. *Online Platform 2025*. [[Paper](https://cadarena.dev/)]
- **Mamba-CAD: State Space Model For 3D Computer-Aided Design Generative Modeling** - Xueyang Li, Yunzhong Lou, Yu Song et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.00439)]
- **BlenderLLM: Training Large Language Models for Computer-Aided Design with Self-improvement** - Yuhao Du, Shunian Chen, Wenbo Zan et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2412.14203)]
- **Geometric Deep Learning for Computer-Aided Design: A Survey** - Negar Heidari, Alexandros Iosifidis. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2402.17695)]

---

## Tools and Platforms

### Commercial CAD with AI Features

- **Dassault Systemes Virtual Companions: AI-Powered Experts on 3DEXPERIENCE Platform** - Dassault Systemes. *Technical Platform 2026*. [[Paper](https://www.3ds.com/newsroom/press-releases/dassault-systemes-unveils-new-way-working-industry-ai-powered-virtual-companions)]
- **AI-Assisted Analysis and Synthesis of Engineering Systems from Multimodal Engineering Data** - H. Sinan Bank, Daniel R. Herber. *IISE 2026*. [[Paper](https://arxiv.org/abs/2603.00251)]
- **Large Language Models for Computer-Aided Design: A Survey** - Zhang et al.. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2505.08137)]
- **A Multidisciplinary Design and Optimization (MDO) Agent Driven by Large Language Models** - Guo et al.. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2511.17511)]
- **Automated CAD Modeling Sequence Generation from Text Descriptions via Transformer-Based Large Language Models** - Liao et al.. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2505.19490)]
- **AI-Driven Digital Twins for Manufacturing: A Review Across Hierarchical Manufacturing System Levels** - Nguyen et al.. *Sensors 2025*. [[Paper](https://doi.org/10.3390/s26010124)]
- **Autodesk Neural CAD: 3D Generative AI Foundation Models for Design-to-Make** - Autodesk. *Technical Report 2025*. [[Paper](https://www.autodesk.com/solutions/autodesk-ai/neural-technology)]
- **Siemens Design Copilot NX: AI Copilot for Product Engineering** - Siemens Digital Industries Software. *Technical Platform 2025*. [[Paper](https://news.siemens.com/en-us/siemens-designcenter-nx-summer-2025/)]
- **Siemens Digital Twin Composer for Industrial Metaverse Digital Twins** - Siemens Digital Industries Software. *Technical Platform 2026*. [[Paper](https://news.siemens.com/en-us/digital-twin-composer-ces-2026/)]
- **A Survey of AI Methods for Geometry Preparation and Mesh Generation in Engineering Simulation** - Steven Owen, Nathan Brown, Nikos Chrisochoides et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.23719)]
- **MotionAnymesh: Physics-Grounded Articulation for Simulation-Ready Digital Twins** - WenBo Xu, Liu Liu, Li Zhang et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.12936)]
- **NVIDIA Omniverse Blueprint for Real-Time Computer-Aided Engineering Digital Twins** - NVIDIA. *Technical Platform 2024*. [[Paper](https://nvidianews.nvidia.com/news/nvidia-announces-omniverse-real-time-physics-digital-twins-with-industry-software-leaders)]
- **A Survey on AI-Driven Digital Twins in Industry 4.0: Smart Manufacturing and Advanced Robotics** - Huang et al.. *Sensors 2021*. [[Paper](https://doi.org/10.3390/s21196340)]

### AI-Native CAD Platforms

- **Neural Concept: Physics- and Geometry-Aware AI Design Copilot for Engineering** - Neural Concept. *Technical Platform 2025*. [[Paper](https://www.neuralconcept.com/post/neural-concept-introduces-a-physics--and-geometry-aware-ai-design-copilot-extending-its-established-engineering-ai-platform)]
- **Adam: AI-Native CAD Platform for Text-to-Parametric Design** - Adam (YC W25). *Technical Platform 2025*. [[Paper](https://adam.new/)]
- **Leo AI: Large Mechanical Model for CAD-Aware Engineering Assistance** - Leo AI. *Technical Platform 2025*. [[Paper](https://www.getleo.ai/)]
- **Zoo.dev Text-to-CAD: Parametric CAD Generation via KCL Programming Language** - Zoo (formerly KittyCAD). *Technical Platform 2024*. [[Paper](https://zoo.dev/docs/faq)]
- **MecAgent: AI Copilot for Mechanical CAD Software Automation** - MecAgent. *Technical Platform 2024*. [[Paper](https://mecagent.com/)]
- **Luminary Cloud: Physics AI Factory for Real-Time Engineering Simulation** - Luminary Cloud. *Technical Platform 2024*. [[Paper](https://luminary.ai/)]

### Open-Source Tools and Frameworks

- **TOOLCAD: Exploring Tool-Using Large Language Models in Text-to-CAD Generation with Reinforcement Learning** - Gong et al.. *arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2604.07960)]
- **Clarify Before You Draw: Proactive Agents for Robust Text-to-CAD Generation** - Yuan et al.. *arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2602.03045)]
- **PLLM: Pseudo-Labeling Large Language Models for CAD Program Synthesis** - Li et al.. *arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2602.12561)]
- **Exploring Tool-Using Large Language Models in Text-to-CAD Generation with Reinforcement Learning** - Yifei Gong, Xing Wu, Wenda Liu et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.07960)]
- **Procedural 3D Generation and Parametric Editing of 3D Shapes with Large Language Models** - Fadlullah Raji, Stefano Petrangeli, Matheus Gadelha et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.12234)]
- **From Idea to CAD: A Language Model-Driven Multi-Agent System for Collaborative Design** - Ocker et al.. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2503.04417)]
- **Text-to-CadQuery: A New Paradigm for CAD Generation with Scalable Large Model Capabilities** - Xie and Ju. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2505.06507)]
- **CAD-Coder: An Open-Source Vision-Language Model for Computer-Aided Design Code Generation** - Doris et al.. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2505.14646)]
- **CADDesigner: Conceptual CAD Model Generation with a General-Purpose Agent** - Fengxiao Fan, Jingzhe Ni, Xiaolong Yin et al. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2508.01031)]
- **Generative AI for CAD Automation: Leveraging Large Language Models for 3D Modelling** - Kumar et al.. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2508.00843)]
- **CAD-Llama: Leveraging Large Language Models for Computer-Aided Design Parametric 3D Model Generation** - Li et al.. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2505.04481)]
- **Text-to-CAD Generation Through Infusing Visual Feedback in Large Language Models** - Wang et al.. *arXiv preprint 2025*. [[Paper](https://arxiv.org/abs/2501.19054)]
- **Autodesk and Model Context Protocol: Making MCP Enterprise-Ready for CAD** - Autodesk. *Technical Blog 2025*. [[Paper](https://www.autodesk.com/autodesk-university/class/Equip-AI-with-Access-to-Your-Design-Data-and-Projects-Model-Context-Protocol-Autodesk-Platform-Services-2025)]
- **FreecadMCP: Model Context Protocol Server for AI-Driven CAD Design** - bonninr (open-source). *GitHub 2025*. [[Paper](https://github.com/bonninr/freecad_mcp)]
- **The Power of Small LLMs in Geometry Generation for Physical Simulations** - Ossama Shafiq, Bahman Ghiassi, Alessio Alexiadis. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.18178)]
- **DreamCAD: Scaling Multi-modal CAD Generation using Differentiable Parametric Surfaces** - Mohammad Sadil Khan, Muhammad Usama, Rolandos Alexandros Potamias et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.05607)]
- **Towards High-Fidelity CAD Generation via LLM-Driven Program Generation and Text-Based B-Rep Primitive Grounding** - Jiahao Li, Qingwang Zhang, Qiuyu Chen et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.11831)]
- **Generating Human-AI Collaborative Design Sequence for 3D Assets via Differentiable Operation Graph** - Xiaoyang Huang, Bingbing Ni, Wenjun Zhang. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.17645)]
- **A Solver-Aided Hierarchical Language for LLM-Driven CAD Design** - Benjamin T. Jones, Felix Hahnlein, Zihan Zhang et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2502.09819)]
- **Multimodal Chain-of-Thought Reinforcement Learning for Precise CAD Code Generation** - Ke Niu, Haiyang Yu, Zhuofan Chen et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.10118)]
- **Generative Parametric Design: A Framework for Real-time Geometry Generation and On-the-fly Multiparametric Approximation** - Mohammed El Fallaki Idrissi, Jad Mounayer, Sebastian Rodriguez et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.11748)]
- **Designing a Human-AI Collaborative Ideation System for Concept Designers** - Wen-Fan Wang, Chien-Ting Lu, Nil Ponsa Campanya et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2502.14747)]
- **Query2CAD: Generating CAD models using natural language queries** - Badagabettu et al.. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2406.00144)]
- **CADCodeVerify: Generating CAD Code with Vision-Language Models for 3D Designs** - Alrashedy et al.. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2410.05340)]
- **CADgpt: Harnessing Natural Language Processing for 3D Modelling to Enhance Computer-Aided Design Workflows** - Timo Kapsalis. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2401.05476)]
- **Experiments on Generative AI-Powered Parametric Modeling and BIM for Architectural Design** - Jaechang Ko, John Ajibefun, Wei Yan. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2308.00227)]

### Research on AI Tools and Deployment

- **Supervising Ralph Wiggum: Exploring a Metacognitive Co-Regulation Agentic AI Loop for Engineering Design** - Xu et al.. *arXiv preprint 2026*. [[Paper](https://arxiv.org/abs/2603.24768)]
- **AI for Better UX in Computer-Aided Engineering: Is Academia Catching Up with Industry Demands? A Multivocal Literature Review** - Choro Ulan Uulu, Mikhail Kulyabin, Layan Etaiwi et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2507.16586)]
- **Beyond Development: Challenges in Deploying Machine Learning Models for Structural Engineering Applications** - Zaker Esteghamati et al.. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2404.12544)]
- **Naming the Pain in Machine Learning-Enabled Systems Engineering** - Kalinowski et al.. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2406.04359)]
- **Towards a Framework for Deep Learning Certification in Safety-Critical Applications Using Inherently Safe Design and Run-Time Error Detection** - Valentin. *arXiv preprint 2024*. [[Paper](https://arxiv.org/abs/2403.14678)]
- **Artificial Intelligence for Safety-Critical Systems in Industrial and Transportation Domains: A Survey** - Jon Perez, Jaume Abella, Markus Borg et al. *ACM Computing Surveys 2023*. [[Paper](https://doi.org/10.1145/3626314)]
- **Challenges in Deploying Machine Learning: A Survey of Case Studies** - Paleyes et al.. *ACM Computing Surveys 2022*. [[Paper](https://doi.org/10.1145/3533378)]

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
