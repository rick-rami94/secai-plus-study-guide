# Frameworks Crosswalk — AI Security Standards & How They Map

> Unofficial study material aligned to CompTIA SecAI+ CY0-001 V1 objectives — verify against the official objectives. See [`../exam-objectives.md`](../exam-objectives.md).

> ⚠️ **UNOFFICIAL / COMMUNITY-MAINTAINED.** This is a study aid, **not** affiliated with or endorsed by CompTIA or any standards body. Framework versions, IDs, clause numbers, annex lists, and thresholds change over time — always confirm against the primary source. Where an exact title, ID, clause, or statistic is version-sensitive or uncertain, the concept is named and flagged **(verify)** rather than fabricated.

This file cross-maps every framework and resource the **SecAI+ (CY0-001)** objectives name by name:
- **Objective 2.1 (threat-modeling resources):** OWASP Top 10 (LLM + ML Security), MIT AI Risk Repository, MITRE ATLAS, CVE AI Working Group, threat-modeling frameworks.
- **Objective 4.3 (compliance):** EU AI Act, OECD standards, ISO AI standards, NIST AI RMF (AIRMF).

It is heavy on tables by design.

---

## 0. The framework landscape at a glance

| Framework / resource | Owner | Type | Primary use | Objective | Voluntary / Mandatory |
|---|---|---|---|---|---|
| OWASP Top 10 for LLM Applications (2025) | OWASP | Risk list | Triage LLM-app risks | 2.1 | Voluntary |
| OWASP Machine Learning Security Top 10 | OWASP | Risk list | Triage classical ML risks | 2.1 | Voluntary |
| MIT AI Risk Repository | MIT (FutureTech et al.) | Risk database / taxonomy | Enumerate & classify AI risks | 2.1 | Voluntary / reference |
| MITRE ATLAS | MITRE | Threat knowledge base | Adversary TTPs for AI | 2.1 | Voluntary / reference |
| CVE AI Working Group | CVE Program (MITRE/CNAs) | Vuln-cataloging working group | Identify/catalog AI vulns in CVE | 2.1 | Voluntary / reference |
| Threat-modeling frameworks (STRIDE, PASTA, attack trees, …) | Various | Methodologies | Systematically find threats | 2.1 | Voluntary |
| NIST AI RMF (AIRMF, AI 100-1) + GenAI Profile (AI 600-1) | NIST | Governance framework | Govern/manage AI risk | 4.3 | Voluntary |
| EU AI Act | European Union | Regulation (law) | Legal obligations by risk tier | 4.3 | **Mandatory** (in scope) |
| OECD AI Principles | OECD | Principles / recommendation | Values-based AI policy guidance | 4.3 | Voluntary (intergovernmental) |
| ISO/IEC 42001 (AIMS), ISO/IEC 23894 (risk guidance) | ISO/IEC | Management std / guidance | Build & run an AI management system | 4.3 | Voluntary / certifiable (42001) |

**Mental model:** *Risk lists* (OWASP) tell you **what can go wrong**. A *risk repository* (MIT) gives you a **structured catalog** to make sure you didn't miss a category. A *threat knowledge base* (ATLAS) tells you **how adversaries do it**. *Threat-modeling methods* (STRIDE/PASTA/attack trees) give you a **process** to find threats. A *vuln-cataloging effort* (CVE AI WG) tells you **how AI flaws get tracked**. *Governance frameworks* (NIST AI RMF, ISO 42001) tell you **how to run a program**. *Regulations* (EU AI Act) tell you **what you are legally required to do**. *Principles* (OECD) set the **values** behind the policy.

---

## 1. OWASP Top 10 for LLM Applications (2025)  *(Obj. 2.1)*

The flagship list for **LLM-based application** risk. Use it to classify findings in chatbots, RAG systems, and AI agents. Pairs directly with Domain 2 threats (2.6) and controls (2.2–2.5).

| ID | Name | One-line description | Example defense |
|---|---|---|---|
| **LLM01** | Prompt Injection | Crafted input (direct or indirect, e.g., via retrieved content) overrides intended instructions or manipulates model behavior. | Treat all input/retrieved text as untrusted; instruction/data separation, prompt firewalls, input filtering, guardrails, least-privilege tool access, human-in-the-loop for high-impact actions. |
| **LLM02** | Sensitive Information Disclosure | Model reveals PII, secrets, proprietary data, or other confidential content via outputs or memorization. | Data minimization & sanitization of training/RAG data, output filtering/redaction (DLP), access controls on retrieved documents, scoping what the model can see. |
| **LLM03** | Supply Chain | Vulnerabilities in third-party models, datasets, plugins, or dependencies (poisoned/tampered/typosquatted artifacts). | Vet sources, verify provenance & signatures, MLBOM/SBOM, model & dependency scanning, safe serialization (e.g., safetensors over pickle). |
| **LLM04** | Data and Model Poisoning | Tampering with pre-training, fine-tuning, or embedding data to introduce backdoors, bias, or degraded integrity. | Data provenance/lineage, validation & anomaly detection on training data, data integrity controls, trusted pipelines, model integrity checks, red-team for backdoors. |
| **LLM05** | Improper Output Handling | Downstream systems trust model output without validation, enabling XSS, SQLi, SSRF, RCE, etc. | Treat output as untrusted; context-aware encoding/escaping, output validation, parameterized queries, sandboxing of executed output. |
| **LLM06** | Excessive Agency | Excessive permissions, autonomy, or functionality lets the LLM/agent take harmful actions beyond intent. | Least privilege on tools/APIs, minimize functionality, tool allow-listing, human approval gates, per-agent identity and scoped permissions. |
| **LLM07** | System Prompt Leakage | System prompts (which may contain secrets or guardrail logic) are exposed, aiding bypass. | Never put secrets/credentials in system prompts; enforce controls server-side, not in the prompt; assume the system prompt can be extracted. |
| **LLM08** | Vector and Embedding Weaknesses | Flaws in how embeddings/vector stores are generated, stored, or retrieved (RAG) — e.g., poisoning, cross-tenant leakage, embedding inversion. | Per-document/tenant access control on retrieval, validate & vet indexed content, monitor the index for poisoning, secure the vector DB. |
| **LLM09** | Misinformation | Model produces false, fabricated (hallucinated), or misleading content that users overrely on. | Grounding/RAG with trusted sources, citations, confidence/uncertainty signaling, human review, user education against overreliance. |
| **LLM10** | Unbounded Consumption | Uncontrolled resource use — model DoS, cost harvesting / "denial of wallet," excessive inference, and functional model extraction via mass querying. | Rate limiting & quotas, token/input/output size limits, cost monitoring & alerting, timeouts, throttling, autoscaling guards. |

---

## 2. OWASP Machine Learning Security Top 10  *(Obj. 2.1)*

Focuses on **classical / traditional ML** systems (classifiers, regressors, CV/NLP models) rather than LLM apps.

> **Note:** OWASP ML Top 10 titles have varied across draft/release versions. The names below reflect the commonly cited set, but **(verify exact OWASP ML title)** against the current OWASP ML Security Top 10 document before quoting verbatim. The IDs ML01–ML10 are the slot numbers; the *titles* are what shift.

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

> **LLM vs ML lists:** OWASP keeps **two** Top 10s. For chatbots/RAG/agents reach for the **LLM** list; for trained classifiers/CV/NLP pipelines reach for the **ML** list. Several threats (poisoning, supply chain, theft) appear on both — many of the named attacks in objective 2.6 map cleanly to ML01–ML10.

---

## 3. MIT AI Risk Repository  *(Obj. 2.1)*

**What it is:** a **structured, living database/taxonomy of AI risks** compiled by MIT (FutureTech and collaborators). It aggregates risks extracted from a large body of existing frameworks, papers, and reports into one searchable catalog, so teams can see the *full landscape* of documented AI risks in one place rather than re-deriving them per project. *(Exact counts of risks/source documents grow over time — **(verify)** the current figures before quoting numbers.)*

**Two taxonomies it organizes risks by (the key exam concept):**

| Taxonomy | Question it answers | Example dimensions (by name) |
|---|---|---|
| **Causal taxonomy** | *How and why* does the risk arise? | **Entity** (human vs. AI), **Intent** (intentional vs. unintentional), **Timing** (pre-deployment vs. post-deployment). |
| **Domain taxonomy** | *What kind* of risk is it? | Grouped into risk **domains** and **subdomains** — e.g., discrimination/toxicity, privacy/security, misinformation, malicious use, human-computer interaction, socioeconomic/environmental harms, AI system safety/limitations. *(verify exact domain set.)* |

**How to use it in threat modeling:**
- Use it as a **checklist / completeness aid** — walk the domain taxonomy to confirm you have not overlooked a risk *category* (e.g., societal, privacy, or misuse risks that a purely technical OWASP review might skip).
- Use the **causal taxonomy** to tag each identified risk by entity/intent/timing — which helps decide *where* in the lifecycle to place a control (pre- vs. post-deployment) and *who/what* is the source.
- Cross-walk repository entries to **OWASP** (technical specifics) and **ATLAS** (adversary behavior) so each catalog reinforces the others.

---

## 4. MITRE ATLAS  *(Obj. 2.1)*

**ATLAS** = *Adversarial Threat Landscape for Artificial-Intelligence Systems*. A **knowledge base of real-world adversary tactics and techniques against AI/ML systems**, modeled after (and complementary to) **MITRE ATT&CK**.

- **Relationship to ATT&CK:** ATLAS mirrors ATT&CK's **tactics → techniques** structure (the "why" vs. the "how") and reuses/extends ATT&CK concepts for the AI domain. Some ATLAS techniques are AI-specific; others bridge into traditional ATT&CK techniques. Use ATLAS for AI-specific attack stages and ATT&CK for the surrounding enterprise intrusion.
- **Use it for:** threat modeling AI systems, mapping detections to adversary behavior, red/purple-team planning, and placing a scenario in a kill-chain.
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
| ML Attack Staging | Prepare attacks against the model (craft adversarial data, build proxy/surrogate models). |
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

## 5. CVE AI Working Group  *(Obj. 2.1)*

**What it is:** a **working group within the CVE Program** (the community effort, coordinated by MITRE with CNAs, that assigns and publishes **CVE** identifiers for vulnerabilities). The AI Working Group exists to address **how AI/ML vulnerabilities are identified, described, and cataloged in the CVE ecosystem** — i.e., adapting CVE conventions to the realities of AI systems. *(verify specifics — scope and outputs of the group continue to evolve.)*

**Why it matters / what problem it tackles:**
- Traditional CVE conventions assume a discrete software artifact with a fixed version. **AI raises hard questions:** Does a poisoned dataset, a vulnerable *model*, a prompt-injection weakness, or a non-deterministic behavior count as a "vulnerability"? What is the affected "product" and "version" when a model is retrained or fine-tuned?
- The working group helps shape **guidance and conventions** so AI/ML weaknesses can be consistently reported, scoped, and tracked as CVEs (and related records), giving defenders the same vulnerability-tracking discipline for AI that they have for conventional software. *(verify specifics.)*

**How to use it in threat modeling:** treat it as the **vulnerability-cataloging** counterpart to the risk lists — OWASP/ATLAS tell you about *classes* of AI risk and attacker behavior; the CVE ecosystem (informed by this working group) is where **specific, identified vulnerabilities** in named AI components get tracked so you can patch/inventory them. Related, commonly studied alongside it: the **CWE** weakness taxonomy, which similarly is being extended for AI/ML weakness types. *(verify specifics.)*

---

## 6. Threat-modeling frameworks applied to AI  *(Obj. 2.1)*

Objective 2.1 lists **threat-modeling frameworks** as a resource. These are **methodologies** (a *process* for finding threats) rather than AI-specific risk catalogs — you apply them to AI systems, often feeding the results into OWASP/ATLAS/MIT classifications.

| Method | Core idea | Applied to AI (examples) |
|---|---|---|
| **STRIDE** | Enumerate threats by 6 categories: **S**poofing, **T**ampering, **R**epudiation, **I**nformation disclosure, **D**enial of service, **E**levation of privilege. | *Tampering* → data/model poisoning; *Information disclosure* → sensitive info disclosure, model inversion/membership inference; *DoS* → model/unbounded consumption; *Elevation of privilege* → excessive agency; *Spoofing* → deepfakes/impersonation. |
| **Attack trees** | Model an attacker goal as a root node, decomposed into AND/OR sub-goals and steps. | Root "extract the model" → branches: mass-query the inference API, steal weights from the registry, build a surrogate — exposes which paths your controls cover. |
| **PASTA** (Process for Attack Simulation and Threat Analysis) | A 7-stage, **risk-centric** method tying threats to business impact and attacker simulation. | Frames AI threats (poisoning, theft, prompt injection) against business objectives and likely adversaries; good for prioritizing AI risk by impact. |
| **DREAD** | A **rating/prioritization** scheme: Damage, Reproducibility, Exploitability, Affected users, Discoverability. | Score and rank AI findings (e.g., a prompt-injection path vs. a poisoning path) to decide remediation order. *(verify — usage/scoring varies.)* |
| **LINDDUN** | A **privacy**-focused threat-modeling method (linkability, identifiability, etc.). | Privacy threats in AI: training-data memorization, re-identification, membership inference. *(verify exact category names.)* |
| **MITRE ATT&CK / ATLAS as a lens** | Use an adversary-behavior knowledge base to drive the model. | Walk ATLAS tactics against your AI system to enumerate realistic attack stages (see Section 4). |

**Process (generic):** (1) decompose the AI system (data pipeline, training, model, inference API, agents/tools, RAG store); (2) identify threats with a method above; (3) map them to OWASP/ATLAS/MIT; (4) select compensating controls (Obj. 2.6); (5) validate (guardrail testing, red-teaming).

---

## 7. NIST AI Risk Management Framework (AIRMF, NIST AI 100-1)  *(Obj. 4.3)*

A **voluntary** framework to manage risks of AI systems across the lifecycle, organized around four core **functions**. **Govern** is cross-cutting and wraps the other three.

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

## 8. EU AI Act, OECD AI Principles, and ISO AI standards  *(Obj. 4.3)*

### 8a. EU AI Act

The EU's **horizontal regulation** for AI — **legally binding** (not voluntary) for in-scope providers/deployers, with extraterritorial reach. It uses a **risk-tiered** approach: the higher the risk, the heavier the obligations.

| Tier | What it means | Obligation level |
|---|---|---|
| **Prohibited / Unacceptable risk** | Practices banned outright (e.g., certain social scoring, manipulative/exploitative systems, certain biometric practices — *verify exact list*). | **Banned** |
| **High risk** | AI in sensitive domains (e.g., critical infrastructure, employment, biometrics, essential services, certain safety components — *verify exact list*). | Strict requirements: risk management, data governance, technical documentation, logging/record-keeping, transparency, human oversight, accuracy/robustness/cybersecurity, conformity assessment. |
| **Limited risk** | Systems with transparency concerns (e.g., chatbots, deepfakes/synthetic media). | **Transparency/disclosure** obligations (tell users they're interacting with AI; label AI-generated content). |
| **Minimal risk** | Most other AI (e.g., spam filters, AI in games). | No mandatory obligations; voluntary codes of conduct encouraged. |

**General-Purpose AI (GPAI) obligations** (foundation/general-purpose models) — layered on top of the tiers:
- Baseline GPAI: **technical documentation**, information for downstream providers, a **policy to respect EU copyright law**, and a **summary of training data** used. *(verify exact wording.)*
- GPAI deemed to pose **systemic risk** (very capable models, e.g., above a compute/capability threshold): additional duties such as **model evaluation/adversarial testing (red-teaming), systemic-risk assessment & mitigation, serious-incident reporting, and cybersecurity protections**. *(verify exact thresholds & wording.)*

> Obligations phase in over time and exact lists/thresholds are detailed in the regulation and its annexes — **(verify)** specifics before relying on them.

### 8b. OECD AI Principles

The **OECD AI Principles** are an **intergovernmental** set of values-based recommendations for trustworthy AI (adopted 2019, later updated; also the basis for the G20 AI principles). They are **voluntary** and influence national AI policy worldwide. The principles emphasize, by theme *(verify exact wording)*:

| Theme (value-based principle) | Plain-English intent |
|---|---|
| Inclusive growth, sustainable development & well-being | AI should benefit people and the planet. |
| Human-centered values & fairness | Respect rule of law, human rights, democratic values, fairness, privacy. |
| Transparency & explainability | People should understand and be able to challenge AI outcomes. |
| Robustness, security & safety | AI should function reliably and safely throughout its lifecycle, with risk management. |
| Accountability | Actors are responsible for AI systems functioning per the principles. |

> The OECD also maintains policy guidance and a definition of an "AI system" that has influenced other instruments (including the EU AI Act). The five OECD values-based principles are complemented by recommendations to policymakers. *(verify exact phrasing.)*

### 8c. ISO/IEC AI standards

| Standard | What it is | Use |
|---|---|---|
| **ISO/IEC 42001:2023 — AIMS** | The first international **management-system standard** for AI. Specifies requirements to establish, implement, maintain, and continually improve an **AI Management System (AIMS)** — certifiable like ISO/IEC 27001 (ISMS). | Run a governed AI program: AI policy, roles, **AI impact assessment**, data management, lifecycle controls, transparency, supplier/third-party management. Follows the ISO Harmonized Structure / **PDCA** cycle. *(Describe its Annex controls by theme; do **not** cite specific clause/control numbers unless verified.)* |
| **ISO/IEC 23894:2023 — AI risk management guidance** | **Guidance** (not a certifiable management-system standard) applying ISO 31000 risk-management principles to AI. | How to **identify, analyze, evaluate, and treat AI risk** across the lifecycle; complements 42001 (the management system) by detailing the risk process. *(verify scope; do not fabricate clauses.)* |
| **ISO/IEC 22989** *(commonly studied alongside)* | AI **concepts and terminology**. | Shared vocabulary for AI concepts. *(verify scope.)* |

> **27001 vs 42001:** 27001 governs an **ISMS** (information-security management); 42001 governs an **AIMS** (AI management) and is designed to **integrate with** 27001. 42001 adds AI-specific concerns (impact on individuals/society, fairness, transparency, safety, intended use, lifecycle governance). An organization can hold **both**; they share the same backbone (PDCA, risk treatment, internal audit, management review).

---

## 9. Master crosswalk — common AI threats (Obj. 2.6) across resources

Rows are the common AI threats called out in objective **2.6**; columns map each to its **OWASP LLM 2025 ID**, **MITRE ATLAS tactic(s) by name**, and the relevant **compensating control(s) from 2.6** (prompt firewalls · model guardrails · access controls · data integrity controls · encryption · prompt templates · rate limiting · least privilege). ATLAS entries are named by tactic/technique concept — **no fabricated `AML.T####` IDs**. *(Mappings are approximate; one threat can touch multiple tactics/controls.)*

| Threat (Obj. 2.6) | OWASP LLM 2025 ID | MITRE ATLAS (by name) | Compensating control(s) from 2.6 |
|---|---|---|---|
| **Prompt injection** (direct/indirect) | **LLM01** (+ **LLM08** for RAG-borne) | Initial Access; Execution; Defense Evasion (LLM prompt-injection / "evade ML model") | **Prompt firewalls**, **model guardrails**, **prompt templates** (instruction/data separation), **least privilege** on tools, **access controls** |
| **Poisoning** (data / model) | **LLM04** | Resource Development; Persistence (backdoor); ML Attack Staging | **Data integrity controls** (provenance/validation), **access controls** on pipelines, **least privilege** |
| **Model inversion** | (closest **LLM02**; classical → **ML03**) | ML Model Access; Collection; Exfiltration | **Access controls**, **rate limiting** (limit probing queries), **model guardrails** (limit confidence detail), **encryption** of stored data |
| **Model theft / extraction** | **LLM10** (mass-query extraction) *(dedicated item is ML05)* | ML Model Access; ML Attack Staging; Exfiltration ("extract ML model") | **Rate limiting**, **access controls** (model/API), **least privilege**, **encryption** of weights at rest |
| **Membership inference** | (closest **LLM02**; classical → **ML04**) | ML Model Access; Discovery; Collection | **Access controls**, **rate limiting**, **model guardrails** (restrict confidence outputs) |
| **Insecure output handling** | **LLM05** | Execution; Impact (downstream code exec) | **Model guardrails** / output validation, **prompt templates**, **least privilege** on downstream systems |
| **Model DoS** (unbounded consumption) | **LLM10** | Impact (denial of ML service / cost) | **Rate limiting** (+ token/input quotas), **prompt firewalls**, **access controls** |
| **Sensitive information disclosure** | **LLM02** (+ **LLM07** for system-prompt leakage) | Collection; Exfiltration | **Access controls**, **encryption** (in transit/at rest/in use), **model guardrails** (output redaction/DLP), **least privilege** |
| **Excessive agency** | **LLM06** | Execution; Impact (autonomous harmful action) | **Least privilege** (tool/API scoping), **access controls** (agent access), **model guardrails** / approval gates |
| **AI supply chain attacks** | **LLM03** | Resource Development; Initial Access (supply-chain compromise) | **Data integrity controls** (provenance/signing, MLBOM/SBOM), **access controls**, **least privilege** |

> **Reading the table:** **model inversion** and **membership inference** are *privacy* attacks against trained models — they have **dedicated items in the OWASP ML Top 10 (ML03/ML04)** and, in an LLM context, surface as **sensitive information disclosure (LLM02)**; there is no separate LLM-Top-10 slot for them, so don't force a wrong ID. **Model theft** surfaces under **LLM10** (mass querying) and has a dedicated **ML05** item.

---

## 10. Which resource maps to which exam objective

| Resource | Named in objective | Use it for |
|---|---|---|
| OWASP LLM Top 10 (2025) | **2.1** | Triage/classify LLM-app findings (chatbots, RAG, agents); pairs with 2.6 |
| OWASP ML Security Top 10 | **2.1** | Classify classical-ML/adversarial-ML risks |
| MIT AI Risk Repository | **2.1** | Completeness checklist; classify risks by causal + domain taxonomy |
| MITRE ATLAS | **2.1** | Adversary tactics/techniques; threat modeling; detection mapping |
| CVE AI Working Group | **2.1** | Understand how AI/ML vulnerabilities are cataloged in the CVE ecosystem |
| Threat-modeling frameworks (STRIDE/PASTA/attack trees) | **2.1** | The *process* for finding AI threats |
| NIST AI RMF (AIRMF) + 600-1 | **4.3** | Govern/Map/Measure/Manage AI risk; GenAI profile |
| EU AI Act | **4.3** | Legal obligations by risk tier; GPAI duties |
| OECD standards (AI Principles) | **4.3** | Values-based policy guidance |
| ISO AI standards (42001 / 23894) | **4.3** | Build/run an AIMS; AI risk-management guidance |

> Related supporting threads in the objectives: compensating controls (2.6), security controls/gateway & guardrails (2.2), access controls (2.3), data security/encryption (2.4), monitoring & auditing (2.5), governance roles & responsible-AI (4.1, 4.2).

---

## 11. How to use these on the exam

**Quick triage when a scenario appears:**
1. **Is it an LLM app (chatbot/RAG/agent)?** → reach for **OWASP LLM Top 10 (2025)** IDs first.
2. **Is it a trained ML model (classifier/CV/NLP)?** → reach for **OWASP ML Top 10**.
3. **"Did I miss a whole category of risk?"** → walk the **MIT AI Risk Repository** domain taxonomy; tag by its causal taxonomy (entity/intent/timing).
4. **"Which attacker stage / how would a detection map?"** → **MITRE ATLAS** tactic by name.
5. **"How do I systematically find threats?"** → a **threat-modeling framework** (STRIDE, attack trees, PASTA).
6. **"How does this AI flaw get tracked as a vulnerability?"** → the **CVE ecosystem** (informed by the **CVE AI Working Group**).
7. **"Which governance function / program-wide management?"** → **NIST AI RMF** (Govern/Map/Measure/Manage) or **ISO/IEC 42001** (AIMS).
8. **"Is this legally required / which risk tier?"** → **EU AI Act**; **OECD principles** for the underlying values.

**High-yield memorization:**
- OWASP LLM **LLM01–LLM10** names and one defense each (Section 1).
- NIST AI RMF four functions: **Govern, Map, Measure, Manage** + that **AI 600-1** is the GenAI profile.
- EU AI Act tiers: **Prohibited → High → Limited → Minimal**, plus **GPAI** has its own obligations.
- ATLAS ≈ "**ATT&CK for AI**"; know the **tactic names**, not invented IDs.
- MIT AI Risk Repository = two taxonomies: **causal** (entity/intent/timing) + **domain**.
- ISO **42001 = AIMS** (certifiable), **23894 = AI risk-management guidance**; OECD principles are **voluntary** values.

**Common traps:**
- Don't confuse the **two OWASP lists** (LLM vs ML).
- **Model inversion / membership inference** are not standalone OWASP **LLM** items — map them to **LLM02** (LLM context) or **ML03/ML04** (classical ML).
- **Model extraction/theft** is covered under **LLM10** (Unbounded Consumption) and has a dedicated **ML05** item.
- **NIST AI RMF and OECD principles are voluntary; the EU AI Act is law.**
- System prompts are **not** a security boundary — **LLM07** exists precisely because they leak; enforce controls server-side.
- The **CVE AI Working Group** catalogs *specific vulnerabilities*; it is **not** a risk taxonomy like OWASP/MIT.

**Cross-references:**
- Threat-modeling resources → objective **2.1** (this file's Sections 1–6).
- Map attacks to compensating controls → objective **2.6** (Section 9 master crosswalk).
- Security/gateway controls, access, data security, monitoring → objectives **2.2–2.5**.
- Governance, roles, responsible AI → objectives **4.1–4.2**.
- Compliance frameworks → objective **4.3** (Sections 7–8).
- See also: [`glossary.md`](glossary.md) and [`acronyms.md`](acronyms.md) in this folder; the blueprint in [`../exam-objectives.md`](../exam-objectives.md).

---

## 12. Version & source watch (verify before exam day)

Frameworks change. Track these and confirm against the primary source:

| Resource | What can shift | Where to confirm |
|---|---|---|
| OWASP LLM Top 10 | Yearly revisions; IDs/names (this file uses the **2025** set) | OWASP GenAI / LLM Top 10 project site |
| OWASP ML Top 10 | Title wording per draft/release | OWASP ML Security Top 10 project site |
| MIT AI Risk Repository | Risk/source counts, domain set, taxonomy updates | MIT AI Risk Repository site |
| MITRE ATLAS | New techniques, IDs, case studies | atlas.mitre.org |
| CVE AI Working Group | Scope, guidance, conventions for AI vulns | CVE Program / cve.org working-group pages |
| NIST AI RMF | Profiles & playbook updates (e.g., AI 600-1) | NIST AI Resource Center |
| EU AI Act | Phased applicability dates, annex lists, GPAI thresholds | EUR-Lex / EU AI Act text |
| OECD AI Principles | Updates to principles / definitions | OECD AI Policy Observatory |
| ISO/IEC 42001 / 23894 / 22989 | Amendments, related standards | ISO / national standards body |

---

*Accuracy note: framework versions, EU AI Act annex lists/thresholds, OWASP ML titles, MIT repository figures, and ATLAS technique IDs evolve. Items flagged **(verify)** should be confirmed against the primary source before exam day. The official CompTIA SecAI+ (CY0-001) objectives supersede this community mapping.*
