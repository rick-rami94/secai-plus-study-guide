# Frameworks Crosswalk — AI Security Standards & How They Map

> ⚠️ **UNOFFICIAL / COMMUNITY-MAINTAINED.** This is a study aid, **not** affiliated with or endorsed by CompTIA or any standards body. Framework details change between versions — always confirm against the primary source before relying on anything here. See [`../exam-objectives.md`](../exam-objectives.md) for the community blueprint this maps to.

This file is a single reference that explains and cross-maps the major AI-security frameworks the **SecAI+** body of knowledge draws on. It is heavy on tables by design. Where exact titles, clause numbers, or technique IDs are version-sensitive or uncertain, the concept is named and flagged **(verify)** rather than fabricated.

---

## 0. The framework landscape at a glance

| Framework | Owner | Type | Primary use | Voluntary / Mandatory |
|---|---|---|---|---|
| OWASP Top 10 for LLM Applications (2025) | OWASP | Risk list | Triage LLM-app risks | Voluntary |
| OWASP Machine Learning Security Top 10 | OWASP | Risk list | Triage classical ML risks | Voluntary |
| NIST AI RMF (AI 100-1) | NIST | Governance framework | Govern/manage AI risk | Voluntary |
| NIST GenAI Profile (AI 600-1) | NIST | RMF profile | Apply RMF to generative AI | Voluntary |
| MITRE ATLAS | MITRE | Threat knowledge base | Adversary TTPs for AI | Voluntary / reference |
| ISO/IEC 42001:2023 | ISO/IEC | Management system standard | Build an AI management system (AIMS) | Voluntary / certifiable |
| ISO/IEC 27001 | ISO/IEC | Management system standard | Information security mgmt (ISMS) | Voluntary / certifiable |
| EU AI Act | European Union | Regulation (law) | Legal obligations by risk tier | **Mandatory** (in scope) |
| Google SAIF | Google | Conceptual framework | Secure-by-design AI guidance | Voluntary |
| NIST SP 800-53 / CSF 2.0 | NIST | Control catalog / framework | Security controls & program structure | Voluntary (CSF) / required for US federal (800-53) |

**Mental model:** *Risk lists* (OWASP) tell you **what can go wrong**. *Threat knowledge bases* (ATLAS) tell you **how adversaries do it**. *Governance frameworks* (NIST AI RMF, ISO 42001) tell you **how to run a program** that manages it. *Regulations* (EU AI Act) tell you **what you are legally required to do**. *Control catalogs* (800-53, CSF) give you the **specific safeguards**.

---

## 1. OWASP Top 10 for LLM Applications (2025)

The flagship list for **LLM-based application** risk. Use it to classify findings in chatbots, RAG systems, and AI agents. Pairs directly with Domain 2 (threats) and Domain 3 (controls).

| ID | Name | One-line description | Example defense |
|---|---|---|---|
| **LLM01** | Prompt Injection | Crafted input (direct or indirect, e.g., via retrieved content) overrides intended instructions or manipulates model behavior. | Treat all input/retrieved text as untrusted; instruction/data separation, input filtering, guardrails, least-privilege tool access, human-in-the-loop for high-impact actions. |
| **LLM02** | Sensitive Information Disclosure | Model reveals PII, secrets, proprietary data, or other confidential content via outputs or memorization. | Data minimization & sanitization of training/RAG data, output filtering/redaction (DLP), access controls on retrieved documents, scoping what the model can see. |
| **LLM03** | Supply Chain | Vulnerabilities in third-party models, datasets, plugins, or dependencies (poisoned/tampered/typosquatted artifacts). | Vet sources, verify provenance & signatures, MLBOM/SBOM, model & dependency scanning, safe serialization formats (e.g., safetensors over pickle). |
| **LLM04** | Data and Model Poisoning | Tampering with pre-training, fine-tuning, or embedding data to introduce backdoors, bias, or degraded integrity. | Data provenance/lineage, validation & anomaly detection on training data, trusted pipelines, model integrity checks, red-team for backdoors. |
| **LLM05** | Improper Output Handling | Downstream systems trust model output without validation, enabling XSS, SQLi, SSRF, RCE, etc. | Treat output as untrusted; context-aware encoding/escaping, output validation, parameterized queries, sandboxing of executed output. |
| **LLM06** | Excessive Agency | Excessive permissions, autonomy, or functionality lets the LLM/agent take harmful actions beyond intent. | Least privilege on tools/APIs, minimize functionality, tool allow-listing, human approval gates, per-agent identity and scoped permissions. |
| **LLM07** | System Prompt Leakage | System prompts (which may contain secrets or guardrail logic) are exposed, aiding bypass. | Never put secrets/credentials in system prompts; enforce controls server-side not in the prompt; assume the system prompt can be extracted. |
| **LLM08** | Vector and Embedding Weaknesses | Flaws in how embeddings/vector stores are generated, stored, or retrieved (RAG) — e.g., poisoning, cross-tenant leakage, embedding inversion. | Per-document/tenant access control on retrieval, validate & vet indexed content, monitor the index for poisoning, secure the vector DB. |
| **LLM09** | Misinformation | Model produces false, fabricated (hallucinated), or misleading content that users overrely on. | Grounding/RAG with trusted sources, citations, confidence/uncertainty signaling, human review, user education against overreliance. |
| **LLM10** | Unbounded Consumption | Uncontrolled resource use — model DoS, cost harvesting/"denial of wallet," excessive inference. | Rate limiting & quotas, input/output size limits, cost monitoring & alerting, timeouts, throttling, autoscaling guards. |

---

## 2. OWASP Machine Learning Security Top 10

Focuses on **classical / traditional ML** systems (classifiers, regressors, CV/NLP models) rather than LLM apps. Useful for Domain 2.1 (adversarial ML).

> **Note:** OWASP ML Top 10 titles have varied across draft/release versions. The names below reflect the commonly cited set, but **(verify exact OWASP ML title)** against the current OWASP ML Security Top 10 document before quoting verbatim.

| ID | Risk (by name) | What it covers | Example defense |
|---|---|---|---|
| **ML01** | Input Manipulation / Adversarial Examples *(verify exact OWASP ML title)* | Perturbed inputs (evasion attacks) cause misclassification. | Adversarial training, input preprocessing/detection, robustness testing. |
| **ML02** | Data Poisoning *(verify exact OWASP ML title)* | Malicious training data corrupts the learned model. | Data validation, provenance, anomaly detection, trusted pipelines. |
| **ML03** | Model Inversion *(verify exact OWASP ML title)* | Attacker reconstructs sensitive training inputs from model behavior. | Limit output confidence detail, differential privacy, access controls. |
| **ML04** | Membership Inference *(verify exact OWASP ML title)* | Attacker determines whether a record was in the training set. | Differential privacy, regularization, restrict confidence outputs. |
| **ML05** | Model Theft / Extraction *(verify exact OWASP ML title)* | Querying the model to replicate (steal) its parameters/behavior. | Rate limiting, query monitoring, watermarking, output throttling. |
| **ML06** | AI Supply Chain Attacks *(verify exact OWASP ML title)* | Compromise via third-party models, datasets, or dependencies. | Provenance verification, signing, MLBOM/SBOM, dependency scanning. |
| **ML07** | Transfer Learning Attack *(verify exact OWASP ML title)* | Malicious behavior inherited from a tampered pre-trained base model. | Vet base models, fine-tune integrity checks, behavioral testing. |
| **ML08** | Model Skewing *(verify exact OWASP ML title)* | Feedback/retraining loop is manipulated to skew the model over time. | Validate feedback data, monitor drift, gate retraining data. |
| **ML09** | Output Integrity Attack *(verify exact OWASP ML title)* | Tampering with model outputs between model and consumer. | Integrity protection on output channel, signing, validation. |
| **ML10** | Model Poisoning *(verify exact OWASP ML title)* | Direct manipulation of model parameters/weights (vs. data). | Model integrity/signing, secure storage, access control on artifacts. |

> **LLM vs ML lists:** OWASP keeps **two** Top 10s. For chatbots/RAG/agents reach for the **LLM** list; for trained classifiers/CV/NLP pipelines reach for the **ML** list. Several threats (poisoning, supply chain, theft) appear on both.

---

## 3. NIST AI Risk Management Framework (AI RMF 1.0, NIST AI 100-1)

A **voluntary** framework to manage risks of AI systems across the lifecycle. It is organized around four core **functions**. Govern is cross-cutting and wraps the other three.

| Function | Purpose | What it covers (examples) |
|---|---|---|
| **GOVERN** | Cultivate a culture of risk management; cross-cutting and continuous. | Policies, roles & accountability, risk tolerance, oversight structures, workforce/training, third-party/supply-chain governance, documentation. |
| **MAP** | Establish context and frame risks. | Intended use & context, stakeholders, system categorization, capabilities & limitations, identifying potential impacts and benefits. |
| **MEASURE** | Analyze, assess, benchmark, and monitor risk. | Metrics & evaluation, testing/red-teaming, measuring trustworthiness characteristics (validity, safety, security, fairness, explainability, privacy), tracking over time. |
| **MANAGE** | Prioritize and act on risks. | Risk treatment/prioritization, resource allocation, response & recovery planning, incident handling, ongoing monitoring and improvement. |

Key points for the exam:
- The four functions are **Govern, Map, Measure, Manage** — memorize them.
- The RMF is **voluntary** and **outcome-based** (not a checklist of mandatory controls).
- It defines characteristics of **trustworthy AI**: valid & reliable, safe, secure & resilient, accountable & transparent, explainable & interpretable, privacy-enhanced, and fair (with managed bias).
- The **Generative AI Profile, NIST AI 600-1**, applies the RMF specifically to **generative AI** risks (a companion "profile," published 2024). Know that it **exists** and extends the RMF for GenAI.

---

## 4. MITRE ATLAS

**ATLAS** = *Adversarial Threat Landscape for Artificial-Intelligence Systems*. A **knowledge base of real-world adversary tactics and techniques against AI/ML systems**, modeled after (and complementary to) **MITRE ATT&CK**.

- **Relationship to ATT&CK:** ATLAS mirrors ATT&CK's **tactics → techniques** structure (the "why" vs. the "how") and reuses/extends ATT&CK concepts for the AI domain. Some ATLAS techniques are AI-specific; others bridge into traditional ATT&CK techniques. Use ATLAS for AI-specific attack stages and ATT&CK for the surrounding enterprise intrusion.
- **Use it for:** threat modeling AI systems, building **ATLAS-mapped detections** (Domain 5.2), red/purple-team planning, and placing a scenario in a kill-chain.
- ATLAS also publishes **case studies** of real AI incidents and a **mitigations** catalog.

**Tactic categories (by name)** — representative, not exhaustive; ATLAS mirrors ATT&CK's tactics and is updated over time, so confirm the current set against the live ATLAS matrix:

| Tactic | Adversary goal (plain English) |
|---|---|
| Reconnaissance | Gather information about the target AI system. |
| Resource Development | Acquire/build resources (data, models, infra) for the attack. |
| Initial Access | Gain a foothold into the AI system or its environment. |
| ML Model Access | Obtain access to the model (API, weights, or otherwise) to enable attacks. |
| Execution | Run malicious code or adversarial inputs. |
| Persistence | Maintain access/foothold over time. |
| Privilege Escalation | Gain higher-level permissions in the system/environment. |
| Defense Evasion | Avoid detection by defenses and monitoring. |
| Credential Access | Steal account names, keys, or tokens. |
| Discovery | Explore the environment and the model's properties. |
| Collection | Gather data of interest (e.g., training data, model outputs). |
| ML Attack Staging | Prepare attacks against the model (e.g., craft adversarial data, build proxy/surrogate models). |
| Exfiltration | Steal data, model artifacts, or extracted model information. |
| Impact | Degrade, disrupt, manipulate, or destroy the AI system or its outputs. |

> **Do not memorize fabricated technique IDs.** ATLAS techniques use `AML.T####` identifiers; refer to techniques by **name** (e.g., "evade ML model," "poison training data," "extract ML model") unless you can confirm the exact ID against the ATLAS site.

**Representative technique *names* you may see mapped under these tactics** (names only — confirm exact phrasing/IDs against the live ATLAS matrix):

| Tactic | Example technique concepts (by name) |
|---|---|
| Reconnaissance | Search for victim's publicly available research/artifacts; gather model metadata. |
| Resource Development | Acquire/develop adversarial ML capabilities; obtain or build a proxy/surrogate model; poison/acquire datasets. |
| Initial Access | Exploit a public-facing application; supply-chain compromise; valid accounts. |
| ML Model Access | ML model inference API access; full/white-box model access; physical environment access. |
| Execution | LLM prompt injection; user execution; command/script execution. |
| Persistence | Backdoor/poison the model; manipulate the training pipeline. |
| Defense Evasion | Evade ML model (adversarial examples); craft inputs to bypass filters/guardrails. |
| Discovery | Discover ML model family/ontology; discover ML artifacts. |
| Collection | Collect ML artifacts; gather data from information repositories. |
| ML Attack Staging | Craft adversarial data; create a proxy/surrogate model; verify the attack offline. |
| Exfiltration | Exfiltrate via the ML inference API; extract the ML model (steal weights/behavior). |
| Impact | Evade ML model in production; denial of ML service; erode/erase model integrity; spamming/cost. |

---

## 5. ISO/IEC 42001:2023 — AI Management System (AIMS)

The first international **management-system standard** for AI. It specifies requirements to **establish, implement, maintain, and continually improve** an **AI Management System (AIMS)** within an organization — certifiable like ISO/IEC 27001.

- **Structure:** Follows the ISO **Harmonized Structure** and the **PDCA (Plan-Do-Check-Act)** continual-improvement cycle, same management-system shape as ISO/IEC 27001 (context, leadership, planning, support, operation, performance evaluation, improvement).
- **Annex-style controls:** Includes an **Annex of controls and implementation guidance** covering things like AI policy, internal organization & roles, **AI impact assessment**, data management for AI, lifecycle/development controls, transparency to users, and third-party/supplier relationships. *(Describe these by theme; do not cite specific clause/control numbers unless verified against the standard.)*
- **Relationship to ISO/IEC 27001:**
  - **27001** governs an **ISMS** (information security management system).
  - **42001** governs an **AIMS** (AI management system) and is designed to **integrate with** 27001 and other management systems.
  - 27001 manages **information security risk**; 42001 adds AI-specific concerns (e.g., **AI impact on individuals/society, fairness, transparency, safety, intended use, and AI lifecycle governance**).
  - An organization can hold **both**; they share the same backbone (PDCA, risk treatment, internal audit, management review).

| Aspect | ISO/IEC 27001 (ISMS) | ISO/IEC 42001 (AIMS) |
|---|---|---|
| Manages | Information security | AI systems & their impacts |
| Core risk lens | Confidentiality, integrity, availability | + safety, fairness, transparency, societal impact, intended use |
| Distinctive artifact | Statement of Applicability (controls) | AI policy + **AI impact assessment** |
| Cycle | PDCA / continual improvement | PDCA / continual improvement |
| Certifiable | Yes | Yes |

> Related guidance commonly studied alongside 42001: **ISO/IEC 23894** (AI risk management guidance) and **ISO/IEC 22989** (AI concepts & terminology). *(verify scope before quoting.)*

---

## 6. EU AI Act

The EU's **horizontal regulation** for AI — **legally binding** (not voluntary) for in-scope providers/deployers, with extraterritorial reach. It uses a **risk-tiered** approach: the higher the risk, the heavier the obligations.

| Tier | What it means | Obligation level |
|---|---|---|
| **Prohibited / Unacceptable risk** | Practices banned outright (e.g., certain social scoring, manipulative or exploitative systems, certain biometric practices — *verify exact list*). | **Banned** |
| **High risk** | AI in sensitive domains (e.g., critical infrastructure, employment, biometrics, essential services, certain safety components — *verify exact list*). | Strict requirements: risk management, data governance, technical documentation, logging/record-keeping, transparency, human oversight, accuracy/robustness/cybersecurity, conformity assessment. |
| **Limited risk** | Systems with transparency concerns (e.g., chatbots, deepfakes/synthetic media). | **Transparency/disclosure** obligations (tell users they're interacting with AI; label AI-generated content). |
| **Minimal risk** | Most other AI (e.g., spam filters, AI in games). | No mandatory obligations; voluntary codes of conduct encouraged. |

**General-Purpose AI (GPAI) obligations** (foundation/general-purpose models) — layered on top of the tiers:
- Baseline GPAI: **technical documentation**, information for downstream providers, a **policy to respect EU copyright law**, and a **summary of training data** used. *(verify exact wording.)*
- GPAI deemed to pose **systemic risk** (very capable models, e.g., above a compute/capability threshold): additional duties such as **model evaluation/adversarial testing (red-teaming), systemic-risk assessment & mitigation, serious-incident reporting, and cybersecurity protections**. *(verify exact thresholds & wording.)*

> Obligations phase in over time and exact lists/thresholds are detailed in the regulation and its annexes — **(verify)** specifics before relying on them.

---

## 7. Google SAIF & NIST SP 800-53 / CSF 2.0

### Google SAIF (Secure AI Framework)

A **conceptual, secure-by-design framework** from Google for building security into AI systems. It extends established software-security best practices to AI and is organized around a set of core **elements/principles**, e.g.:

- Expand strong **security foundations** to the AI ecosystem.
- Extend **detection & response** to bring AI into the organization's threat universe.
- **Automate defenses** to keep pace with new and existing threats.
- **Harmonize platform-level controls** for consistency across the org.
- Adapt controls for **faster feedback loops** for AI deployment (test, monitor, iterate).
- Contextualize **AI system risks** in surrounding business processes (end-to-end risk).

**How it applies to AI:** SAIF is useful for **architecture and program design** — mapping where guardrails, supply-chain controls, monitoring, and IR fit across the AI lifecycle. It complements (not replaces) the risk lists and governance frameworks above. *(Element wording is paraphrased — verify against Google's SAIF site.)*

### NIST SP 800-53 & NIST CSF 2.0

- **SP 800-53** is a **catalog of security and privacy controls** (control families like AC, AU, SC, SI, RA, CM, IA, etc.). For AI, these controls still apply to the **infrastructure** around models: access control for AI gateways/registries, audit logging of prompts/tool calls, system & communications protection for inference endpoints, supply-chain risk management, and incident response. AI doesn't get its own control catalog — you **apply existing 800-53 controls** to AI components.
- **CSF 2.0** organizes a cybersecurity program around six functions: **Govern, Identify, Protect, Detect, Respond, Recover** (Govern was added in 2.0). It's a **program-structuring** framework; you can map AI security activities (monitoring, detection, IR, recovery from Domain 5) onto CSF functions, and CSF's **Govern** dovetails with NIST AI RMF's **Govern**.

| Framework | Granularity | Best used for |
|---|---|---|
| NIST CSF 2.0 | High-level functions/outcomes | Structuring the overall program (incl. AI) |
| NIST SP 800-53 | Specific controls | Implementing concrete safeguards on AI infra |
| NIST AI RMF | AI-specific risk functions | Managing AI-specific risk & trustworthiness |

---

## 8. Master crosswalk — AI threats across frameworks

Rows are common AI threats; columns map each to the major frameworks. Use this as the "Rosetta Stone" for Domain 2.6 (mapping attacks to frameworks). ATLAS entries are named by **tactic/technique concept**, not by fabricated IDs. *(Mappings are approximate — a single threat can touch multiple tactics/functions.)*

| Threat | OWASP LLM 2025 ID | MITRE ATLAS (by name) | NIST AI RMF function | EU AI Act relevance |
|---|---|---|---|---|
| **Prompt injection** (direct/indirect) | **LLM01** (and **LLM08** for RAG-borne) | Initial Access; Execution; Defense Evasion (e.g., "evade ML model," LLM prompt-injection technique) | **Measure** (test/red-team), **Manage** (mitigate) | High-risk: human oversight, robustness/cybersecurity; transparency for chatbots (Limited) |
| **Sensitive information disclosure** (PII/secret leakage) | **LLM02** (+ **LLM07** for system-prompt leakage) | Collection; Exfiltration | **Map** (context/impact), **Measure**, **Manage** | High-risk: data governance; intersects **GDPR**; transparency obligations |
| **Data / model poisoning** | **LLM04** | Resource Development; ML Attack Staging; Persistence (backdoor) | **Map**, **Measure**, **Manage**, **Govern** (supply chain) | High-risk: data governance, accuracy/robustness; GPAI evaluation duties |
| **Supply chain compromise** (models/datasets/deps) | **LLM03** | Resource Development; Initial Access | **Govern** (third-party), **Map**, **Manage** | High-risk: technical docs, record-keeping; GPAI downstream info/copyright/data-summary |
| **Excessive agency** (over-permissioned agents/tools) | **LLM06** | Execution; Impact (autonomous harmful action) | **Map**, **Manage**, **Govern** | High-risk: human oversight; risk-management & logging requirements |
| **Model theft / extraction** | **LLM10** (Unbounded Consumption — folds in functional model replication / model theft via mass querying); dedicated item is **OWASP ML05** | ML Model Access; ML Attack Staging; Exfiltration | **Measure**, **Manage**, **Govern** | High-risk: cybersecurity/robustness; GPAI cybersecurity protections |
| **Unbounded consumption** (model DoS / cost harvesting) | **LLM10** | Impact (degrade/disrupt availability) | **Measure**, **Manage** | High-risk: robustness/availability; resilience expectations |
| **Bias / fairness** (discriminatory outcomes) | **LLM09** (misinformation/harmful output is adjacent) | *(governance issue more than an ATLAS tactic)* — Impact where weaponized | **Map** (impacts), **Measure** (fairness metrics), **Govern** | High-risk: bias/data-governance, accuracy; fundamental-rights focus; **42001** AI impact assessment |

> **Reading the table:** **model extraction/theft** surfaces under **LLM10 (Unbounded Consumption)** via mass querying, and also has a dedicated item in the **ML** Top 10 (**ML05**); **bias** is not a standalone OWASP **LLM** Top 10 item (it's a governance/fairness concern) — flagged so you don't force a wrong mapping on the exam.

---

## 9. Which framework maps to which exam domain

A fast index of where each framework shows up in the [community blueprint](../exam-objectives.md):

| Framework | Primary domains | Where it's explicitly named |
|---|---|---|
| OWASP LLM Top 10 (2025) | D1.4, D2.2, D2.6, D3.6 | 1.4, 2.6 ("place a scenario in the OWASP LLM Top 10") |
| OWASP ML Security Top 10 | D1.4, D2.1 | 1.4 |
| NIST AI RMF (+ 600-1) | D1.4, D4.1 | 1.4, 4.1 (functions Govern/Map/Measure/Manage) |
| MITRE ATLAS | D2.6, D5.2 | 1.4, 2.6, 5.2 ("ATLAS-mapped detections") |
| ISO/IEC 42001 | D1.4, D4.1 | 1.4, 4.1 |
| EU AI Act | D4.3 | 4.3 ("EU AI Act risk tiers") |
| Google SAIF | D1.4 | 1.4 |
| NIST 800-53 / CSF 2.0 | D1.4, D3.x, D5.x | 1.4 (applied to AI infra & operations) |

---

## 10. Defense-in-depth: defenses mapped back to frameworks

A reverse view — pick a control, see which frameworks it satisfies. Useful for PBQ-style "which control mitigates X" items.

| Control / defense | Mitigates (OWASP LLM) | RMF function | Also satisfies |
|---|---|---|---|
| Input/output guardrails & filtering | LLM01, LLM05, LLM09 | Measure, Manage | SAIF (automate defenses); 800-53 SI/SC |
| Treat output as untrusted (encode/validate) | LLM05 | Manage | 800-53 SI |
| Least privilege + tool allow-listing | LLM06 | Manage, Govern | SAIF; 800-53 AC |
| Provenance, signing, MLBOM/SBOM | LLM03, LLM04 | Govern, Map | 42001 supplier controls; EU AI Act docs |
| Rate limiting, quotas, cost alerts | LLM10 | Measure, Manage | CSF Detect/Respond; 800-53 SC |
| Per-document/tenant retrieval authz | LLM02, LLM08 | Map, Manage | 800-53 AC; GDPR data minimization |
| Prompt/tool-call logging & monitoring | LLM01, LLM06 | Measure | CSF Detect; ATLAS-mapped detections; 800-53 AU |
| AI red-teaming & evals | LLM01–LLM10 (testing) | Measure | EU AI Act GPAI eval; SAIF feedback loops |
| Human-in-the-loop approval gates | LLM01, LLM06 | Manage, Govern | EU AI Act human oversight (High-risk) |

---

## 11. How to use these for the exam

**Quick triage when a scenario appears:**
1. **Is it an LLM app (chatbot/RAG/agent)?** → reach for **OWASP LLM Top 10 (2025)** IDs first.
2. **Is it a trained ML model (classifier/CV/NLP)?** → reach for **OWASP ML Top 10**.
3. **"Which attacker stage / how would a detection map?"** → **MITRE ATLAS** tactic by name.
4. **"Which governance function / how to manage program-wide?"** → **NIST AI RMF** (Govern/Map/Measure/Manage) or **ISO/IEC 42001** (AIMS).
5. **"Is this legally required / which risk tier?"** → **EU AI Act**.
6. **"Which concrete control implements the fix?"** → **NIST SP 800-53** / **CSF 2.0** / **Google SAIF** for architecture.

**High-yield memorization:**
- OWASP LLM **LLM01–LLM10** names and one defense each (Section 1).
- NIST AI RMF four functions: **Govern, Map, Measure, Manage** + that **AI 600-1** is the GenAI profile.
- EU AI Act tiers: **Prohibited → High → Limited → Minimal**, plus **GPAI** has its own obligations.
- ATLAS ≈ "**ATT&CK for AI**"; know the **tactic names**, not invented IDs.
- ISO **42001 = AIMS**, sibling to **27001 = ISMS**, both PDCA/certifiable.

**Common traps:**
- Don't confuse the **two OWASP lists** (LLM vs ML).
- **Bias** is **not** a distinct OWASP **LLM** Top 10 item; **model extraction/theft** is covered under **LLM10** (Unbounded Consumption) and has a dedicated **ML** Top 10 item (ML05) (Section 8 note).
- NIST AI RMF is **voluntary**; EU AI Act is **law**.
- System prompts are **not** a security boundary — **LLM07** exists precisely because they leak.

**Cross-references:**
- Threat detail → Domain 2 in [`../exam-objectives.md`](../exam-objectives.md) (esp. 2.6 "map attacks to frameworks").
- Controls/defenses → Domain 3.
- Governance/compliance → Domain 4 (4.1 RMF/42001, 4.3 EU AI Act/GDPR).
- Detection & IR → Domain 5 (5.2 ATLAS-mapped detections).
- See also: `glossary.md`, `acronyms.md` in this folder.

---

## 12. Version & source watch (verify before exam day)

Frameworks change. Track these and confirm against the primary source:

| Framework | What can shift | Where to confirm |
|---|---|---|
| OWASP LLM Top 10 | Yearly revisions; IDs/names can change (this file uses the **2025** set) | OWASP GenAI / LLM Top 10 project site |
| OWASP ML Top 10 | Title wording per draft/release | OWASP ML Security Top 10 project site |
| NIST AI RMF | Profiles & playbook updates (e.g., AI 600-1) | NIST AI Resource Center |
| MITRE ATLAS | New techniques, IDs, case studies | atlas.mitre.org |
| ISO/IEC 42001 | Amendments, related 23894/22989 | ISO / national standards body |
| EU AI Act | Phased applicability dates, annex lists, GPAI thresholds | EUR-Lex / EU AI Act text |
| Google SAIF | Element wording / risk map | Google SAIF site |
| NIST 800-53 / CSF | Control & function revisions (CSF 2.0) | NIST CSRC |

---

*Accuracy note: framework versions, EU AI Act annex lists/thresholds, OWASP ML titles, and ATLAS technique IDs evolve. Items flagged **(verify)** should be confirmed against the primary source before exam day. The official CompTIA objectives — once published — supersede this community mapping.*
