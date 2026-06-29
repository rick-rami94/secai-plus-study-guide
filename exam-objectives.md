# CompTIA SecAI+ (CY0-001) — Exam Objectives & Study Blueprint

> 📌 **Aligned to the official blueprint.** This study guide is structured to the **CompTIA SecAI+ Certification Exam Objectives, Exam CY0-001 V1** (Objectives Document v4.0, © 2025 CompTIA, Inc.). The domains, weightings, objective numbering, and exam format below match that official document.
>
> ⚠️ **Unofficial study aid.** This repository is **community-made and NOT affiliated with, authorized by, or endorsed by CompTIA**, and it contains **no official or actual exam questions** — all practice questions here are original. Objective titles are reproduced/paraphrased for study alignment only. CompTIA®, SecAI+®, and Security+® are trademarks of CompTIA, Inc. Always cross-check the current objectives at CompTIA's site, as exam content is periodically updated.

---

## Exam at a glance (official)

| Attribute | Value |
|---|---|
| Exam number | **CY0-001 V1** |
| Number of questions | **Maximum of 60** |
| Question types | **Multiple-choice and performance-based** |
| Length of test | **60 minutes** |
| Passing score | **600** (on a scale of 100–900) |
| Recommended experience | 3–4 years of IT experience and ~2 years of hands-on cybersecurity experience |

**What the exam certifies you can do:** understand important AI concepts; secure AI systems using various technical controls; leverage AI to enhance corporate security posture while automating security tasks; and understand how governance, risk, and compliance (GRC) impacts AI technologies globally.

---

## Domains & weightings (official)

| # | Domain | Weight |
|---|--------|:------:|
| 1.0 | Basic AI Concepts Related to Cybersecurity | **17%** |
| 2.0 | Securing AI Systems | **40%** |
| 3.0 | AI-assisted Security | **24%** |
| 4.0 | AI Governance, Risk, and Compliance | **19%** |
| | **Total** | **100%** |

**Practice-test allocation (per 60-question exam):** D1 ≈ 10, **D2 ≈ 24**, D3 ≈ 14, D4 ≈ 12. Domain 2 dominates — spend your study time accordingly.

---

## Domain 1.0 — Basic AI Concepts Related to Cybersecurity (17%)

### 1.1 Compare and contrast various AI types and techniques used in cybersecurity.
- **Types of AI:** Generative AI · Machine learning · Statistical learning · Transformers · Deep learning · Generative adversarial networks (GANs) · Natural language processing (NLP) — Large language models (LLMs), Small language models (SLMs)
- **Model training techniques:** Model validation · Supervised learning · Unsupervised learning · Reinforcement learning · Federated learning · Fine-tuning (Epoch, Pruning, Quantization)
- **Prompt engineering:** System prompts · User prompts · One-shot prompting · Multi-shot prompting · Zero-shot prompting · System roles · Templates

### 1.2 Explain the importance of data security in relation to AI.
- **Data processing:** Data cleansing · Data verification · Data lineage · Data integrity · Data provenance · Data augmentation · Data balancing
- **Data types:** Structured · Semi-structured · Unstructured
- **Watermarking**
- **Retrieval-augmented generation (RAG):** Vector storage · Embeddings

### 1.3 Explain the importance of security throughout the life cycle of AI.
- **Business use case** (Alignment with corporate objectives)
- **Data collection** (Trustworthiness, Authenticity)
- **Data preparation**
- **Model development/selection**
- **Model evaluation**
- **Deployment**
- **Validation**
- **Monitoring and maintenance**
- **Feedback and iteration**
- **Human-centric AI design principles:** Human-in-the-loop · Human oversight · Human validation

## Domain 2.0 — Securing AI Systems (40%)

### 2.1 Given a scenario, use AI threat-modeling resources.
- **OWASP Top 10** — LLM Top 10, Machine Learning (ML) Security Top 10
- **MIT AI Risk Repository**
- **MITRE Adversarial Threat Landscape for Artificial-Intelligence Systems (ATLAS)**
- **Common Vulnerabilities and Exposures (CVE) AI Working Group**
- **Threat-modeling frameworks**

### 2.2 Given a set of requirements, implement security controls for AI systems.
- **Model controls:** Model evaluation · Model guardrails (Prompt templates)
- **Gateway controls:** Prompt firewalls · Rate limits · Token limits · Input quotas (Data size, Quantity) · Modality limits · Endpoint access controls
- **Guardrail testing and validation**

### 2.3 Given a scenario, implement appropriate access controls for AI systems.
- Model access · Data access · Agent access · Network/application programming interface (API) access

### 2.4 Given a scenario, implement data security controls for AI systems.
- **Encryption requirements:** In transit · At rest · In use
- **Data safety:** Data anonymization · Data classification labels · Data redaction · Data masking · Data minimization

### 2.5 Given a scenario, implement monitoring and auditing for AI systems.
- **Prompt monitoring** (Query, Response)
- **Log monitoring · Log sanitization · Log protection**
- **Response confidence level**
- **Rate monitoring**
- **AI cost monitoring:** Prompts · Storage · Response · Processing
- **Auditing for quality and compliance:** Hallucinations · Accuracy · Bias and fairness · Access

### 2.6 Given a scenario, analyze the evidence of an attack and suggest compensating controls for AI systems.
- **Attacks:** Backdoor attacks · Trojan attacks · Prompt injection · Poisoning (Model poisoning, Data poisoning) · Jailbreaking · Input manipulation · Introducing biases · Circumventing AI guardrails · Manipulating application integrations · Model inversion · Model theft · AI supply chain attacks · Transfer learning attacks · Model skewing · Output integrity attacks · Membership inference · Insecure output handling · Model denial of service (DoS) · Sensitive information disclosure · Insecure plug-in design · Excessive agency · Overreliance
- **Compensating controls:** Prompt firewalls · Model guardrails · Access controls · Data integrity controls · Encryption · Prompt templates · Rate limiting · Least privilege

## Domain 3.0 — AI-assisted Security (24%)

### 3.1 Given a scenario, use AI-enabled tools to facilitate security tasks.
- **Tools/applications:** Integrated development environment (IDE) plug-ins · Browser plug-ins · Command-line interface (CLI) plug-ins · Chatbots · Personal assistants · Model Context Protocol (MCP) server
- **Use cases:** Signature matching · Code quality and linting · Vulnerability analysis · Automated penetration testing · Anomaly detection · Pattern recognition · Incident management · Threat modeling · Fraud detection · Translation · Summarization

### 3.2 Explain how AI enables or enhances attack vectors.
- **AI-generated content (deepfake):** Impersonation · Misinformation · Disinformation
- **Adversarial networks · Reconnaissance · Social engineering · Obfuscation · Automated data correlation**
- **Automated attack generation:** Attack vector discovery · Payloads · Malware · Honeypot · Distributed denial of service (DDoS)

### 3.3 Given a scenario, use AI to automate security tasks.
- **Scripting tools:** Low-code · No-code
- **Document synthesis and summarization**
- **Incident response ticket management**
- **Change management:** AI-assisted approvals · Automated deployment/rollback
- **AI agents**
- **Continuous integration and continuous deployment (CI/CD):** Code scanning · Software composition analysis · Unit testing · Regression testing · Model testing · Automated deployment/rollback

## Domain 4.0 — AI Governance, Risk, and Compliance (19%)

### 4.1 Explain organizational governance structures that support AI.
- **Organizational structures:** AI Center of Excellence · AI policies and procedures
- **AI-related roles:** Data scientist · AI architect · Machine learning engineer · Platform engineer · MLOps engineer · AI security architect · AI governance engineer · AI risk analyst · AI auditor · Data engineer

### 4.2 Explain risks associated with AI.
- **Responsible AI:** Fairness · Reliability and safety · Transparency · Privacy and security · Differential privacy · Explainability · Inclusiveness · Accountability · Consistency · Awareness training
- **Risks:** Introduction of bias · Accidental data leakage · Reputational loss · Accuracy and performance of the model · Intellectual Property (IP)-related risks · Autonomous systems
- **Shadow IT:** Shadow AI

### 4.3 Summarize the impact of compliance on business use and development of AI.
- **European Union (EU) AI Act**
- **Organisation for Economic Co-operation and Development (OECD) standards**
- **International Organization for Standardization (ISO) AI standards**
- **National Institute of Standards and Technology (NIST) AI Risk Management Framework (AIRMF)**
- **Corporate policies:** Sanctioned vs. unsanctioned · Private vs. public models · Sensitive data governance
- **Third-party compliance evaluations**
- **Data sovereignty**

---

## How everything in this repo maps to the blueprint

- [`study-guide/`](study-guide/) — one chapter per official domain (1.0–4.0) plus a [frameworks crosswalk](study-guide/frameworks-crosswalk.md), [glossary](study-guide/glossary.md), and [acronyms](study-guide/acronyms.md) (aligned to the official SecAI+ acronym list).
- [`practice-tests/`](practice-tests/) — 3 variants × **60 questions** (matching the real exam length), allocated by the official weightings; each question tagged to an objective (e.g., `2.6`).
- [`flashcards/`](flashcards/) — Anki deck tagged by domain.
- [`cheatsheets/`](cheatsheets/) and [`study-plan/`](study-plan/) — quick references and a study plan keyed to these domains.

*This blueprint mirrors CompTIA's published CY0-001 V1 objectives. CompTIA periodically updates exams — verify against the current objectives before exam day.*
