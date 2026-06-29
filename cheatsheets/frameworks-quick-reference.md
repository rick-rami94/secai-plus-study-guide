# Frameworks Quick Reference — AI Threat-Modeling & Governance Cheat Sheet

> Unofficial study material aligned to CompTIA SecAI+ CY0-001 V1 objectives. See [../exam-objectives.md](../exam-objectives.md).

Covers the official named resources in **2.1** (threat modeling) and **4.3** (compliance), plus a **2.2–2.4 controls** quick list. No fabricated IDs, clause numbers, or stats; uncertain items flagged **(verify)**.

---

## OWASP Top 10 for LLM Applications (2025)

| ID | Name | One-liner |
|---|---|---|
| **LLM01** | Prompt Injection | Crafted input overrides intended instructions (direct or indirect). |
| **LLM02** | Sensitive Information Disclosure | Model leaks PII, secrets, or proprietary data in output. |
| **LLM03** | Supply Chain | Compromised third-party models, datasets, or components. |
| **LLM04** | Data and Model Poisoning | Tampered training/fine-tuning/RAG data or model weights. |
| **LLM05** | Improper Output Handling | Downstream systems trust unsanitized model output (XSS/SQLi/RCE). |
| **LLM06** | Excessive Agency | Too much functionality, permissions, or autonomy granted. |
| **LLM07** | System Prompt Leakage | System-prompt contents exposed/relied on for security. |
| **LLM08** | Vector and Embedding Weaknesses | Flaws in RAG vector stores/embeddings (injection, leakage). |
| **LLM09** | Misinformation | Hallucinated/false output, including unsafe overreliance. |
| **LLM10** | Unbounded Consumption | Resource exhaustion / Model DoS / runaway cost. |

## OWASP Machine Learning Security Top 10 (brief)

Separate ML-focused list (distinct from the LLM list). Themes include: **Input Manipulation** (adversarial examples), **Data Poisoning**, **Model Inversion**, **Membership Inference**, **Model Theft/Stealing**, **AI Supply Chain**, **Transfer Learning Attack**, **Model Skewing**, **Output Integrity Attack**, and corrupted-package/environment risks. Exact ordering/IDs **(verify)** against the current OWASP ML Security Top 10.

---

## Threat-modeling resources (2.1)

| Resource | What it is | Why / how you use it |
|---|---|---|
| **MIT AI Risk Repository** | A consolidated, searchable database/taxonomy of documented AI risks from many sources. | Common reference of risk categories/causes; a checklist to ensure broad risk coverage. |
| **MITRE ATLAS** | Adversarial Threat Landscape for AI Systems — ATT&CK-style knowledge base of real-world AI attacks. | Map adversary behavior across **tactics** (below) to techniques and case studies. |
| **CVE AI Working Group** | Effort to adapt CVE/vulnerability disclosure practices to AI/ML systems. | Standardizes how AI vulnerabilities are identified, named, and tracked. |
| **Threat-modeling frameworks** | General methods applied to AI (e.g., **STRIDE**, **attack trees**). | Systematically enumerate threats to AI components (model, data, pipeline, plug-ins). |

**MITRE ATLAS tactics (by name — no AML.T IDs invented):** Reconnaissance · Resource Development · Initial Access · ML Model Access · Execution · Persistence · Privilege Escalation · Defense Evasion · Credential Access · Discovery · Collection · ML Attack Staging · Exfiltration · Impact. *(Tactic set evolves — verify current list.)*

**STRIDE for AI:** Spoofing · Tampering (data/model integrity) · Repudiation · Information disclosure (inversion, membership inference, sensitive disclosure) · Denial of service (model DoS) · Elevation of privilege (excessive agency). **Attack trees:** decompose a goal (e.g., "exfiltrate model") into branching attacker steps.

---

## Governance & compliance (Domain 4)

| Resource | What it is | Key structure / why it matters |
|---|---|---|
| **NIST AI RMF (AIRMF)** | Voluntary AI Risk Management Framework (AI RMF 1.0). | Four core functions: **Govern · Map · Measure · Manage** (Govern is cross-cutting). |
| **EU AI Act** | EU risk-based AI regulation. | Risk tiers: **Prohibited (unacceptable) · High · Limited · Minimal**, plus **GPAI** (general-purpose AI) obligations. |
| **OECD AI Principles** | Intergovernmental values-based AI principles. | Promote trustworthy AI: inclusive growth, human-centered values/fairness, transparency, robustness/safety, accountability. |
| **ISO/IEC 42001** | AI Management System (**AIMS**) standard. | Certifiable management-system standard for governing AI (plan-do-check-act style); specific clauses **(verify)**. |
| **ISO/IEC 23894** | AI **risk management** guidance. | Applies ISO 31000 risk principles to AI; guidance (not certifiable); specific clauses **(verify)**. |

**Other Domain-4 concepts**
- **Data sovereignty** — data is subject to the laws/jurisdiction where it is collected/stored; constrains where AI data/models may reside or be processed.
- **Sanctioned vs. unsanctioned / Shadow AI** — approved/governed AI tools vs. unapproved AI use (a form of Shadow IT); shadow AI risks data leakage and ungoverned exposure.
- **Private vs. public models** — self-hosted/internal models with data kept in-org vs. third-party hosted models where prompts/data may leave the boundary.

---

## Securing-AI controls quick list (2.2–2.4)

| Category | Official controls | Purpose |
|---|---|---|
| **Model controls (2.2)** | Model evaluation · Model guardrails · **Prompt templates** · Guardrail testing & validation | Constrain and validate model behavior at the model layer. |
| **Gateway controls (2.2)** | **Prompt firewalls** · Rate limits · Token limits · Input quotas (data size, quantity) · Modality limits · Endpoint access controls | Filter/throttle traffic in front of the model; blunt injection and DoS. |
| **Access controls (2.3)** | Model access · Data access · Agent access · Network/API access | Enforce **least privilege** across who/what can reach model, data, agents, APIs. |
| **Encryption (2.4)** | In transit · At rest · **In use** | Protect data confidentiality/integrity across all states. |
| **Data safety (2.4)** | Anonymization · Classification labels · Redaction · Masking · Minimization | Reduce sensitive-data exposure before/around model use. |

**Mnemonic:** *Model guards behavior · Gateway guards traffic · Access guards reach · Encryption guards state · Data-safety guards content.*

---

**Verify before exam day:** OWASP ML Security Top 10 exact IDs/ordering, current MITRE ATLAS tactic list, and ISO 42001/23894 clause specifics. These cheat sheets use names/structures only, never invented IDs, clause numbers, or statistics.
