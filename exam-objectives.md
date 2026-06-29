# CompTIA SecAI+ — Community Exam Blueprint (Unofficial)

> ⚠️ **UNOFFICIAL / COMMUNITY-MAINTAINED.** This blueprint is a study aid built from CompTIA's *announced* positioning of **SecAI+** and the broader, well-established AI-security body of knowledge (OWASP, NIST, MITRE, ISO). **It is not affiliated with, endorsed by, or sourced from CompTIA.** Domain names, weightings, objective numbering, question count, time, and passing score below are **community estimates** intended to make studying productive — they are **not** the official exam objectives.
>
> ✅ **Before you rely on this, download the official exam objectives from CompTIA and reconcile any differences.** Where the official document differs, the official document wins. See [`README.md`](README.md) for how to use this repo and the full disclaimer.

---

## Exam snapshot (community estimate)

| Attribute | Estimate (verify with CompTIA) |
|---|---|
| Exam code | SecAI+ (e.g., AI0-001 — *placeholder*, confirm official code) |
| Format | Multiple choice (single & multiple response) + performance-based questions (PBQs) |
| Max questions | **90** |
| Time | **165 minutes** |
| Passing score | **~750 on a 100–900 scale** (community estimate) |
| Recommended experience | Security+ (or equivalent) plus hands-on exposure to AI/ML systems; ~2–3 years security/IT |
| Audience | Security analysts/engineers, AI/ML engineers, GRC, and architects securing AI systems |

> These mirror the *style* of CompTIA professional exams (e.g., Security+/SecurityX). Treat the practice tests in this repo as **exam-realistic**, not exam-identical.

---

## Domains & weightings (community estimate)

| # | Domain | Weight |
|---|--------|:------:|
| 1.0 | AI & Security Foundations | **16%** |
| 2.0 | AI Threats, Attacks & Vulnerabilities | **24%** |
| 3.0 | Securing the AI/ML Lifecycle | **22%** |
| 4.0 | AI Governance, Risk & Compliance | **18%** |
| 5.0 | AI Security Operations & Incident Response | **20%** |
| | **Total** | **100%** |

Practice-test question counts are allocated by weight (per 90-question test): D1 ≈ 14, D2 ≈ 22, D3 ≈ 20, D4 ≈ 16, D5 ≈ 18.

---

## Domain 1.0 — AI & Security Foundations (16%)

- **1.1** Explain AI/ML concepts relevant to security: supervised/unsupervised/reinforcement learning; deep learning & neural networks; **LLMs, generative AI, foundation models, transformers**; embeddings/vectors; tokens; **RAG**; **AI agents, tool use, and MCP (Model Context Protocol)**; fine-tuning vs prompting; **RLHF**; temperature/sampling; hallucination; context windows.
- **1.2** Compare AI system components and architectures: training vs inference; **model serving & inference endpoints**; ML/LLM pipelines and **MLOps/LLMOps**; data pipelines; **model registry, feature store, vector database, AI gateway**; orchestration frameworks.
- **1.3** Summarize the AI threat landscape and how AI changes the security model: expanded/novel attack surface; non-determinism; data-centric risk; the **AI/ML supply chain**; dual-use; autonomy and agency; speed/scale of impact.
- **1.4** Explain core AI security principles and frameworks: CIA triad applied to AI (plus safety, privacy, fairness); **secure-by-design / Secure AI**; **NIST AI RMF**, **OWASP Top 10 for LLM Applications (2025)**, **OWASP ML Security Top 10**, **MITRE ATLAS**, **ISO/IEC 42001**, **Google SAIF**, NIST GenAI Profile (AI 600-1).
- **1.5** Identify roles, responsibilities, and the **shared responsibility model** for AI: model provider vs platform/deployer vs application vs end user; data owners; AI governance roles; what changes for SaaS LLMs vs self-hosted models.

## Domain 2.0 — AI Threats, Attacks & Vulnerabilities (24%)

- **2.1** Analyze **adversarial machine-learning** attacks: **evasion / adversarial examples**, **data poisoning**, **backdoor/trojan** models, **model inversion**, **model extraction/stealing**, **membership inference**, perturbation/transferability, sponge attacks.
- **2.2** Analyze **LLM/GenAI-specific** attacks: **direct and indirect prompt injection**, **jailbreaks**, **system-prompt leakage**, **insecure output handling**, **sensitive information disclosure**, training-data extraction/memorization, **excessive agency**, overreliance, **unbounded consumption** (model DoS / cost harvesting).
- **2.3** Analyze attacks on the **AI supply chain and infrastructure**: poisoned/malicious **pretrained models** and datasets, **unsafe deserialization** (e.g., pickle), model-format risks, **model registry / hub compromise**, typosquatted models/packages, compromised dependencies, GPU/host and inference-server attacks.
- **2.4** Analyze **agentic and tool-use** risks: excessive agency/permissions, **tool misuse and confused-deputy**, **MCP/tool-server** abuse, **SSRF and lateral movement via agents**, autonomous action abuse, memory/conversation poisoning, multi-agent collusion.
- **2.5** Analyze **data and privacy** risks: PII/secret leakage, **memorization & regurgitation**, re-identification, data exfiltration via outputs, **RAG data leakage / broken document-level authorization**, embedding inversion.
- **2.6** Map attacks to frameworks: place a given scenario in the **OWASP LLM Top 10 (2025)** and in **MITRE ATLAS** tactics/techniques; distinguish ML vs LLM vs infrastructure attacks.

## Domain 3.0 — Securing the AI/ML Lifecycle (22%)

- **3.1** Secure **data**: governance, **provenance & lineage**, sanitization/validation, **poisoning defenses**, **differential privacy**, PII handling/minimization, data classification, dataset access control.
- **3.2** Secure **training & development**: secure MLOps environments and isolation, secrets management, reproducibility, **model signing/integrity**, **MLBOM/SBOM**, dependency & model scanning, safe model serialization (e.g., safetensors).
- **3.3** Secure **deployment & inference**: **AI gateway**, **input/output guardrails**, content filtering/moderation, **rate limiting & quotas**, sandboxing/isolation, least privilege, hardening of model-serving endpoints, network segmentation for AI.
- **3.4** Implement **identity & access control for AI**: authentication/authorization, **per-agent identity and on-behalf-of (OBO)**, API-key and token hygiene, **tool allow-listing**, RBAC/ABAC, secrets and key management, scoping model/tool permissions.
- **3.5** Secure **RAG and knowledge systems**: **vector-database security**, **retrieval/document-level authorization**, embedding security, source vetting/trust, **indirect-prompt-injection defenses** in retrieved content, data freshness/poisoning of the index.
- **3.6** Apply **guardrails and defensive controls**: prompt hardening/templating, **output validation/encoding** (treat output as untrusted), PII redaction, canary tokens, **prompt-injection detection**, allow/deny lists, **human-in-the-loop** approvals for high-impact actions.
- **3.7** **Test and evaluate** AI security: **AI red teaming**, adversarial/jailbreak testing, automated **evals** and benchmarks, model validation, regression testing for safety, continuous evaluation in CI/CD.

## Domain 4.0 — AI Governance, Risk & Compliance (18%)

- **4.1** Apply **AI governance frameworks**: **NIST AI RMF** functions (**Govern, Map, Measure, Manage**), **ISO/IEC 42001** (AI management system), OECD AI Principles, responsible-AI programs and committees.
- **4.2** Manage **AI risk**: AI risk assessment, **AI impact assessment**, risk register, **third-party/model risk**, **model cards / system cards / datasheets**, acceptable-risk and risk acceptance.
- **4.3** Apply **laws, regulations, and standards**: **EU AI Act risk tiers** (prohibited/high/limited/minimal), **GDPR and automated decision-making**, transparency/disclosure obligations, sector requirements, record-keeping.
- **4.4** Address **ethics, fairness, bias, and trustworthiness**: bias types and sources, **fairness metrics**, **explainability/XAI**, transparency, accountability, safety, contestability.
- **4.5** Manage **AI supply-chain and vendor risk**: model provenance and licensing, **open vs closed/proprietary models**, data licensing, third-party AI vendor assessment, EULA/usage-rights review.
- **4.6** Establish **policies and acceptable use**: enterprise AI usage policy, **shadow AI**, data classification for AI, **DLP for generative AI**, training/awareness, approval workflows.

## Domain 5.0 — AI Security Operations & Incident Response (20%)

- **5.1** **Monitor and log** AI systems: prompt/response and **tool-call logging**, observability/telemetry, audit trails, **drift and performance monitoring**, cost/usage monitoring, privacy-aware logging.
- **5.2** **Detect** AI threats: anomaly detection, **prompt-injection and jailbreak detection**, abuse/misuse detection, **detection engineering and SIEM integration**, **ATLAS-mapped detections**, canaries/honeytokens.
- **5.3** **Respond** to AI incidents: AI-aware **IR lifecycle**, containment (**disable model/tool, revoke keys, kill switch**), **model rollback**, jailbreak/prompt-injection response, **data-leak and PII-exposure** response, playbooks and comms.
- **5.4** Ensure **AI resilience and recovery**: model versioning/rollback, backups of models/indexes/configs, failover and **graceful degradation**, defense against **DoS / unbounded consumption / cost bombing**, business continuity for AI services.
- **5.5** Manage **vulnerabilities and continuous improvement**: AI vulnerability management and disclosure, patching/updating models and dependencies, **threat intelligence for AI**, post-incident reviews, **purple teaming** and feedback loops.

---

## How everything in this repo maps to the blueprint

- [`study-guide/`](study-guide/) — one file per domain (1.0–5.0) plus a [frameworks crosswalk](study-guide/frameworks-crosswalk.md), [glossary](study-guide/glossary.md), and [acronyms](study-guide/acronyms.md).
- [`practice-tests/`](practice-tests/) — 3 variants × 90 questions, allocated by the weightings above; each question is tagged to a domain objective (e.g., `2.2`).
- [`flashcards/`](flashcards/) — Anki deck tagged by domain.
- [`cheatsheets/`](cheatsheets/) and [`study-plan/`](study-plan/) — quick references and a 4-week plan keyed to these domains.

*Last reviewed by maintainer: see git history. Reconcile against the official CompTIA SecAI+ objectives before exam day.*
