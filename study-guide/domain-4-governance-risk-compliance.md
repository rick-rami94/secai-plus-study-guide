# Domain 4.0 — AI Governance, Risk & Compliance (18%)

> ⚠️ **UNOFFICIAL / COMMUNITY-MAINTAINED study guide.** Not affiliated with, endorsed by, or sourced from CompTIA. Reconcile against the official objectives before exam day. See [`../exam-objectives.md`](../exam-objectives.md) for the full blueprint and disclaimer.

---

## What this domain is about

Domain 4 is the **GRC layer** of AI security: how organizations *govern* AI, *measure and treat AI risk*, comply with *laws and standards*, build *fair and trustworthy* systems, manage *supply-chain/vendor* exposure, and enforce *policies and acceptable use*. It is the least "hands-on-keyboard" domain and the most **vocabulary- and framework-heavy** — which is exactly why it is so testable. CompTIA loves to make you **distinguish lookalikes**: NIST AI RMF vs ISO/IEC 42001, model card vs system card vs datasheet, EU AI Act risk tiers, and competing fairness metrics.

At 18% of a 90-question exam, expect **roughly 16 questions** drawn from this domain, with a strong chance of at least one **performance-based question** (PBQ) — e.g., dragging scenarios onto the correct EU AI Act risk tier, or matching a control to a NIST AI RMF function.

### Objectives covered

| # | Objective | Focus |
|---|-----------|-------|
| **4.1** | Apply **AI governance frameworks** | NIST AI RMF (Govern/Map/Measure/Manage), ISO/IEC 42001 (AIMS), OECD AI Principles, responsible-AI programs |
| **4.2** | Manage **AI risk** | Risk & impact assessment, risk register, third-party/model risk, model cards/system cards/datasheets, risk acceptance |
| **4.3** | Apply **laws, regulations, standards** | EU AI Act risk tiers, GDPR & automated decisions, transparency/disclosure, sector rules, record-keeping |
| **4.4** | Address **ethics, fairness, bias, trust** | Bias types & sources, fairness metrics, explainability/XAI, accountability, contestability |
| **4.5** | Manage **AI supply-chain & vendor risk** | Provenance, licensing, open vs closed models, third-party assessment, EULA/usage rights |
| **4.6** | Establish **policies & acceptable use** | Enterprise AI usage policy, shadow AI, data classification, DLP for GenAI, approval workflows |

**Mental model:** *Govern* (4.1) sets the structure → *Risk* (4.2) and *Law* (4.3) define what you must manage → *Ethics* (4.4) defines what "good" looks like → *Supply chain* (4.5) and *Policy* (4.6) operationalize it.

---

## 4.1 — Apply AI governance frameworks

**AI governance** = the people, processes, and structures that direct and control how an organization develops, buys, and uses AI so that it stays aligned with objectives, risk appetite, law, and values. Governance is **organizational and ongoing**, not a one-time project.

### NIST AI Risk Management Framework (AI RMF 1.0)

The **NIST AI RMF** is a **voluntary, risk-based** framework (not a regulation, not certifiable). Its goal is to help organizations build **trustworthy AI**. The framework is organized around **four core functions**:

| Function | Plain-English purpose | Examples of activities |
|----------|----------------------|------------------------|
| **GOVERN** | *Cross-cutting* culture, policies, accountability, and oversight that apply to all other functions | Define roles, risk tolerance, policies, oversight committee, third-party policy |
| **MAP** | Establish **context** and frame risks; understand where/how AI is used | Identify intended use, stakeholders, impacts, the AI's place in the larger system |
| **MEASURE** | **Assess, analyze, and track** risks using metrics and testing | Evaluate trustworthiness characteristics, run evals/red-team, quantify risk |
| **MANAGE** | **Prioritize and act on** risks; allocate resources; respond and monitor | Treat/mitigate risks, document residual risk, monitor in production, plan response |

> 🎯 **Exam tip — memorize the four functions and that GOVERN is cross-cutting.** A classic trap is to list "Identify, Protect, Detect, Respond, Recover" — those are the **NIST Cybersecurity Framework (CSF)** functions, *not* the AI RMF. AI RMF = **Govern, Map, Measure, Manage (G-M-M-M)**. Govern wraps the other three.

NIST also publishes supporting material the exam may reference:
- **NIST AI 600-1 — Generative AI Profile**: a companion *profile* applying the AI RMF specifically to **generative AI** risks (e.g., confabulation/hallucination, CBRN/dangerous-content, data privacy, harmful bias, intellectual property).
- **Trustworthy AI characteristics** NIST associates with good AI: *valid & reliable, safe, secure & resilient, accountable & transparent, explainable & interpretable, privacy-enhanced, and fair (with harmful bias managed).*

### ISO/IEC 42001:2023 — AI Management System (AIMS)

**ISO/IEC 42001:2023** is the international standard for an **AI Management System (AIMS)**. Think of it as **"ISO 27001 but for AI."** Key facts the exam tests:

- It is a **management-system standard** built on the **Plan-Do-Check-Act (PDCA)** continual-improvement cycle.
- It is **certifiable** — an accredited body can audit an organization and certify conformance. (NIST AI RMF is *not* certifiable.)
- It emphasizes **AIMS scope, leadership commitment, objectives, risk treatment, operational controls, and continual improvement.**

> 🎯 **Exam tip — NIST AI RMF vs ISO/IEC 42001.** This comparison is almost guaranteed:
>
> | | **NIST AI RMF** | **ISO/IEC 42001** |
> |---|---|---|
> | Type | Voluntary **framework** / guidance | **Management-system standard** |
> | Certifiable? | **No** | **Yes** (auditable certification) |
> | Structure | 4 functions (Govern/Map/Measure/Manage) | **PDCA** management system (AIMS) |
> | Origin | U.S. NIST | International (ISO/IEC) |
> | Best answer when question says… | "risk-based, flexible, U.S. guidance" | "certifiable management system / like ISO 27001 for AI" |

### Other governance references

| Framework | What to know |
|-----------|--------------|
| **OECD AI Principles** | International, values-based principles (e.g., inclusive growth, human-centered values & fairness, transparency, robustness/safety, accountability). Influenced the **G7 / Hiroshima process** and many national policies. Principles, not controls. |
| **ISO/IEC 23894** | Guidance on **AI risk management** (complements 42001; aligns with ISO 31000 risk vocabulary). |
| **Google SAIF** | *Secure AI Framework* — vendor framework of security best practices for AI systems. |
| **Responsible-AI (RAI) program** | Internal program: an **AI governance committee / review board**, an **AI policy**, an **AI inventory/register**, defined **roles** (AI ethics officer, model owners, data owners), and **gates** in the lifecycle. |

> 🎯 **Exam tip — governance ≠ a single tool.** "Governance" answers usually involve **people + process + accountability** (committee, policy, oversight, documented roles), not a single technical control. If an option says "deploy a WAF" to a governance question, it's a distractor.

### Responsible-AI roles (who does what)

| Role | Responsibility |
|------|----------------|
| **AI governance board / committee** | Sets policy and risk appetite; approves/blocks use cases; oversight |
| **AI ethics officer / responsible-AI lead** | Owns fairness, transparency, and ethical-review process |
| **Model owner** | Accountable for a specific model's behavior, metrics, and lifecycle |
| **Data owner / steward** | Accountable for the data feeding the model (quality, classification, consent) |
| **Risk / compliance** | Maps systems to obligations; maintains the risk register; sign-offs |
| **Security / red team** | Threat modeling, adversarial testing, monitoring |

**Worked example.** A bank wants to deploy an LLM assistant for loan officers. Governance fit: the **AI committee** approves the use case as in-scope; a **model owner** is named; the use case is logged in the **AI inventory**; a **risk + impact assessment** (4.2) runs because credit decisions can be **legally significant** (GDPR Art. 22 / fair-lending law in 4.3); and the policy mandates **human-in-the-loop** sign-off on any denial. That single scenario touches 4.1, 4.2, 4.3, and 4.4 — exactly how PBQs are built.

---

## 4.2 — Manage AI risk

AI risk management adapts traditional risk practice (identify → assess → treat → monitor) to AI-specific harms: **bias, drift, hallucination, opacity, autonomy, data leakage, and model/supply-chain compromise.**

### Risk assessment vs impact assessment

| Term | Question it answers | Notes |
|------|---------------------|-------|
| **AI risk assessment** | "What could go wrong, how likely, how bad — to *us*?" | Likelihood × impact to the org; feeds the **risk register**. |
| **AI impact assessment** (AIA) | "What is the effect on *people, rights, and society*?" | Broader, stakeholder/rights-focused. Often required for high-risk or rights-affecting AI. Related: **DPIA** (Data Protection Impact Assessment under GDPR) for privacy. |

### The AI risk register

A **risk register** is the living inventory of identified risks. Typical columns: risk ID, description, affected AI system, **likelihood**, **impact**, inherent risk, existing controls, **residual risk**, **risk owner**, treatment decision, and status. Every fielded AI system should map to entries here.

### Risk treatment options (same four as classic risk management)

| Option | Meaning | AI example |
|--------|---------|-----------|
| **Mitigate / reduce** | Add controls to lower likelihood or impact | Add output guardrails + human-in-the-loop |
| **Transfer / share** | Shift risk to a third party | Cyber-insurance; contractual indemnity from a model vendor |
| **Avoid** | Don't do the risky thing | Decide *not* to deploy facial recognition for hiring |
| **Accept** | Knowingly tolerate the residual risk | Documented **risk acceptance** signed by an accountable owner |

> 🎯 **Exam tip — "risk acceptance" needs an accountable owner.** Accepting risk is only valid when an authorized person **formally documents and signs off** on the residual risk against a defined **risk appetite/tolerance**. "The engineer decided it was fine" is the wrong answer.

### Inherent vs residual risk (and risk appetite)

- **Inherent risk** = risk *before* controls (raw exposure of the activity).
- **Residual risk** = risk *remaining after* controls are applied — this is what gets **accepted, mitigated further, or escalated**.
- **Risk appetite / tolerance** = the amount of risk leadership is willing to accept to pursue objectives. Residual risk is compared against appetite to decide treatment.

> 🎯 **Exam tip — you treat *residual* risk, not inherent.** A common distractor accepts or reports **inherent** risk. The decision point is always **residual risk vs risk appetite**.

### Third-party / model risk

AI introduces **model risk** (the model behaves wrongly, drifts, or is biased) and **third-party risk** (you depend on an external model/API/dataset). Treat foundation-model providers like any critical vendor: assess them, monitor them, and have a fallback. (Deep-dive in **4.5**.)

**AI-specific risk categories to recognize on the exam:**

| Risk | Description | Example treatment |
|------|-------------|-------------------|
| **Model drift / degradation** | Accuracy decays as the world changes vs training data | Monitoring + retraining triggers (5.1) |
| **Hallucination / confabulation** | Confident but false output | Grounding/RAG, output validation, human review |
| **Bias / discrimination** | Unfair outcomes across groups | Fairness testing (4.4), diverse data |
| **Data leakage / privacy** | Sensitive data exposed via outputs or training | DLP, minimization, redaction (4.6) |
| **Opacity** | Can't explain a decision | XAI tooling, interpretable models (4.4) |
| **Excessive autonomy** | Agent takes harmful actions unsupervised | Human-in-the-loop, tool allow-listing (3.4) |
| **Supply-chain compromise** | Poisoned model/dataset/dependency | Provenance, signing, scanning (4.5) |

### AI documentation artifacts — the testable trio

CompTIA heavily tests the distinction between three transparency/documentation artifacts:

| Artifact | Describes… | Typical contents | Analogy |
|----------|-----------|------------------|---------|
| **Model card** | A **single model** | Intended use & out-of-scope uses, training data summary, **performance metrics broken out by group**, limitations, ethical considerations | "Nutrition label for a model" |
| **System card** | An **end-to-end system** (model + surrounding components, guardrails, human oversight) | How models combine, safety mitigations, system-level behavior and limitations | "Spec sheet for the whole product" |
| **Datasheet for datasets** | A **dataset** | Motivation, **composition**, collection process, **provenance**, preprocessing, recommended/【not-recommended】uses, maintenance | "Provenance & ingredients label for data" |

> 🎯 **Exam tip — match the scope to the artifact.**
> - Asking *"what data trained this and where did it come from?"* → **datasheet for datasets**.
> - Asking *"what is this one model's intended use, metrics, and limitations?"* → **model card**.
> - Asking *"how does the whole deployed system behave, including guardrails and human oversight?"* → **system card**.
>
> Provenance/composition = **datasheet**. Per-model metrics & intended use = **model card**. Whole-system safety = **system card**.

---

## 4.3 — Apply laws, regulations, and standards

You don't need to be a lawyer, but you must know the **shape** of the major regimes and which obligation attaches to which category.

### EU AI Act — the risk-tier model

The **EU AI Act** takes a **risk-based, tiered** approach. Obligations scale with the risk category. From highest to lowest risk:

| Tier | What it covers (illustrative) | Core obligation |
|------|-------------------------------|-----------------|
| **Unacceptable / Prohibited** | Practices deemed a clear threat to safety/rights — e.g., government **social scoring**, certain manipulative or exploitative systems, some biometric practices | **Banned** — may not be placed on the market or used |
| **High-risk** | AI in sensitive contexts — e.g., critical infrastructure, education, employment/hiring, essential services, law enforcement, certain medical/safety components | **Strict requirements**: risk management, data governance, **technical documentation & record-keeping/logging**, transparency, **human oversight**, accuracy/robustness/cybersecurity, conformity assessment |
| **Limited risk** | Systems that interact with people or generate/manipulate content — e.g., chatbots, **deepfakes/synthetic media** | **Transparency obligations**: disclose that users are interacting with AI / that content is AI-generated |
| **Minimal risk** | The vast majority — e.g., AI spam filters, AI in video games | **No mandatory obligations** (voluntary codes encouraged) |

**General-Purpose AI (GPAI) / foundation models** are handled **separately** from the four use-case tiers. GPAI providers have their own obligations (e.g., technical documentation, copyright-related policy, and a **public summary of training-data content**), with **additional** obligations for GPAI models deemed to carry **systemic risk**.

> 🎯 **Exam tip — order and obligation are the trap.** Memorize the ladder **Prohibited → High → Limited → Minimal**, and pin the right obligation to each:
> - **Prohibited** = banned outright (social scoring is the textbook example).
> - **High-risk** = the heavy paperwork (risk mgmt, **human oversight**, logging, conformity assessment).
> - **Limited** = **transparency only** (chatbot disclosure, deepfake labeling).
> - **Minimal** = essentially nothing required.
> - **GPAI** is a **separate track**, not one of the four tiers. Don't invent specific article numbers on the exam — reason from the tier.

**Worked classification example.** A company builds AI to screen job applicants and auto-reject low scorers. Employment/hiring is a sensitive context → **high-risk** under the EU AI Act (risk management, logging, human oversight, conformity assessment). If the rejection is **solely automated with significant effect** on the person, **GDPR Article 22** also applies, requiring safeguards and human-review options. One scenario, two regimes — read the *use* and the *effect*, not just the technology.

### GDPR and automated decision-making

The **EU GDPR** governs personal-data processing and matters whenever AI touches EU residents' data.

- **Article 22** gives individuals rights regarding decisions **based *solely* on automated processing** (including profiling) that produce **legal or similarly significant effects** — e.g., automated loan denial or automated hiring rejection. Generally such solely-automated decisions are restricted unless an exception applies (e.g., explicit consent, contractual necessity, or authorizing law), and safeguards such as the ability to **obtain human intervention, express one's view, and contest the decision** must be available.
- **DPIA** (Data Protection Impact Assessment) is required for high-risk processing — often the case for large-scale or sensitive AI.
- Core GDPR principles that bite on AI: **lawful basis, purpose limitation, data minimization, accuracy, storage limitation**, and **data-subject rights** (access, erasure, rectification).

> 🎯 **Exam tip — Article 22 = solely-automated + significant effect.** The keywords are **"solely automated"** and **"legal or similarly significant effects,"** and the remedy theme is a **right to human review / contestability**. If a human meaningfully reviews the decision, Article 22's core restriction may not apply.

### Other regimes and standards to recognize

| Regime / standard | One-liner |
|-------------------|-----------|
| **NIST AI RMF / AI 600-1** | Voluntary U.S. guidance (see 4.1). |
| **ISO/IEC 42001 / 23894** | International AIMS & AI-risk standards (4.1). |
| **U.S. sectoral laws** | No single federal AI law; sector rules apply — e.g., **HIPAA** (health), **GLBA/ECOA/FCRA** (finance/credit & anti-discrimination), **COPPA** (children). State laws (e.g., privacy acts, NYC's automated-employment-tool rules) add requirements. |
| **EU AI Act** | The flagship horizontal AI regulation (above). |
| **Sector/AI-specific guidance** | Aviation, medical-device (FDA), and financial regulators issue AI-specific expectations. |

> 🎯 **Exam tip — record-keeping & traceability are compliance controls.** "Maintain logs/technical documentation" shows up under EU AI Act high-risk, GDPR accountability, and ISO 42001. When a scenario asks *how to demonstrate compliance after the fact*, the answer is usually **documentation, logging, and audit trails**.

---

## 4.4 — Ethics, fairness, bias, and trustworthiness

### Sources and types of bias

**Bias** = systematic error that produces unfair or skewed outcomes. It can enter at *any* lifecycle stage:

| Bias type | Where it comes from | Example |
|-----------|--------------------|---------|
| **Historical / training-data bias** | The world (and thus the data) already reflects inequity | A hiring model trained on past hires learns past discrimination |
| **Sampling / representation bias** | Training data doesn't represent the deployment population | Vision model trained mostly on one skin tone performs worse on others |
| **Measurement bias** | The chosen feature/proxy mismeasures the true target | Using "arrests" as a proxy for "crime" |
| **Labeling / annotation bias** | Human labelers inject subjective or inconsistent judgments | Toxicity labels reflecting one cultural norm |
| **Aggregation bias** | One model forced to fit distinct subgroups equally | A single clinical model that ignores group-specific physiology |
| **Deployment / feedback-loop bias** | The model's own outputs shape future inputs/data | Predictive policing sends patrols to areas it already flagged, generating more data there |
| **Automation / confirmation bias** (human) | Humans over-trust the model's output | A reviewer rubber-stamps AI recommendations |

> 🎯 **Exam tip — name the *stage* to name the bias.** Data collected from a skewed population = **sampling/representation**. The world being unfair = **historical**. Bad proxy/feature = **measurement**. Inconsistent human labels = **labeling**. The model reinforcing itself over time = **feedback-loop/deployment**.

### Fairness metrics — and why they conflict

There is **no single "fairness" number.** Common notions:

| Fairness notion | Rough definition |
|-----------------|------------------|
| **Demographic / statistical parity** | Positive-outcome rate is equal across groups |
| **Equal opportunity** | Equal **true-positive rate** across groups (qualified people treated equally) |
| **Equalized odds** | Equal **TPR *and* FPR** across groups |
| **Predictive parity** | Equal **precision** (positive predictive value) across groups |
| **Individual fairness** | Similar individuals receive similar outcomes |
| **Counterfactual fairness** | Outcome unchanged if a protected attribute were different |

> 🎯 **Exam tip — fairness metrics can be mathematically incompatible.** It is **provably impossible** to satisfy all fairness definitions at once when base rates differ across groups (the classic **impossibility result**: you generally can't have equal precision *and* equal FPR/TPR simultaneously). The exam wants you to know fairness is a **deliberate trade-off chosen for context**, not a checkbox. "Just optimize all fairness metrics together" is a **wrong** answer.

### Where bias is mitigated (pre-, in-, post-processing)

| Stage | Technique class | Example |
|-------|-----------------|---------|
| **Pre-processing** | Fix the **data** before training | Reweighting/resampling under-represented groups; relabeling; removing leaky proxies |
| **In-processing** | Constrain the **model** during training | Fairness constraints/regularizers in the objective; adversarial debiasing |
| **Post-processing** | Adjust the **outputs** after training | Group-specific decision thresholds; output calibration |

> 🎯 **Exam tip — match the mitigation to the lifecycle stage.** "Reweight the dataset" = **pre-processing**. "Add a fairness constraint to the loss" = **in-processing**. "Adjust the decision threshold per group" = **post-processing**. And mitigation requires **measurement first** — you can't fix bias you don't track (ties back to NIST AI RMF **Measure**).

### Explainability, transparency, accountability, contestability

| Concept | Meaning | Tool/example |
|---------|---------|--------------|
| **Explainability / interpretability (XAI)** | Humans can understand *why* the model produced an output | **SHAP**, **LIME**, feature importance, attention/saliency, surrogate models |
| **Transparency** | Disclosure about the system's existence, purpose, data, and limits | Model/system cards, "you're talking to AI" notices |
| **Accountability** | A **named human/owner** is answerable for outcomes | Model owner, governance committee sign-off |
| **Safety** | The system avoids causing harm under normal and adversarial conditions | Guardrails, red-teaming, kill switch |
| **Contestability** | Affected people can **challenge/appeal** a decision and get redress | Human-review channel, appeals process (ties to **GDPR Art. 22**) |
| **Robustness** | Stable, correct behavior under noise, drift, and attack | Adversarial testing, monitoring |

> 🎯 **Exam tip — explainability ≠ transparency.** *Explainability* is about understanding a **specific output/decision** (often via SHAP/LIME). *Transparency* is about **disclosing** the system and its properties. *Contestability* is the right to **appeal** a decision. Keep these three crisp.

> 🎯 **Exam tip — interpretable vs post-hoc.** A **simple/interpretable model** (e.g., a small decision tree or linear model) is understandable by design. A **black-box model** needs **post-hoc explanation tools** (SHAP/LIME) to approximate why it decided. "Use SHAP on a linear regression" is usually unnecessary — note when a model is *already* interpretable.

---

## 4.5 — AI supply-chain and vendor risk

Modern AI is assembled from **third-party models, datasets, frameworks, and APIs.** Each is a supply-chain dependency that can be compromised, mislicensed, or abandoned.

### Open vs closed (proprietary) models

| Dimension | **Open / open-weight models** | **Closed / proprietary models** |
|-----------|-------------------------------|--------------------------------|
| Weights | Downloadable; can self-host | Hidden behind a vendor API |
| Control & customization | High — fine-tune, inspect, run on-prem | Low — limited to vendor's knobs |
| Data residency | You control where data goes (can stay on-prem) | Data typically sent to the vendor |
| Supply-chain risk | **You** vet the artifact (poisoning, unsafe pickles, typosquats) | You inherit the **vendor's** controls/opacity |
| Maintenance burden | Patching/hosting is **yours** | Vendor patches, but **lock-in** and abrupt deprecation risk |
| "Open" caveat | "Open weights" ≠ open data or OSI-approved license — **read the license** | License = vendor EULA |

> 🎯 **Exam tip — "open-weight" is not automatically "open source."** Many popular models publish *weights* under a **custom/community license** with **use restrictions** (acceptable-use clauses, scale caps, no-redistribution, or "not for training other models"). Don't assume MIT/Apache — **read the model license** and check field-of-use limits.

### Provenance, integrity, and licensing

- **Model provenance & lineage**: where did the model/dataset come from, who produced it, what was it trained on? Prefer artifacts from **trusted sources** with **signatures**.
- **Integrity controls**: **model signing**, hashes, and an **AI/ML BOM (MLBOM/SBOM)** listing model + dataset + dependency components. Prefer **safe serialization** (e.g., **safetensors**) over formats that execute code on load (e.g., **pickle**).
- **Data licensing**: training/RAG data may carry **copyright, privacy, or contractual** limits. Scraped or "found" data can create IP and compliance liability.
- **Output/usage rights**: who owns the model's outputs? Can you use them commercially? Check the **EULA / terms of service**.

### Third-party AI vendor assessment

When onboarding a foundation-model API or AI SaaS, assess:

| Area | Questions to ask |
|------|------------------|
| **Data handling** | Is our input used to **train** their models? Retention period? Data residency/region? Sub-processors? |
| **Security & compliance** | SOC 2 / ISO 27001 / **ISO 42001**? Pen-test & red-team results? Vulnerability disclosure? |
| **Model transparency** | Model/system cards? Known limitations and eval results? Update/deprecation policy? |
| **Contractual** | **EULA / acceptable-use**, **indemnification** (esp. IP), SLA/uptime, liability, exit/portability terms |
| **Continuity** | What if the vendor changes the model, raises price, or shuts down? **Fallback** model/abstraction layer? |

> 🎯 **Exam tip — "does the vendor train on our data?" is the signature GenAI procurement question.** Enterprise concern #1 with hosted LLMs is **data retention and whether prompts/outputs feed vendor training**. The mitigation is a **zero-retention / no-training contractual term** (or self-hosting an open-weight model).

**License red flags to spot in a model/vendor EULA:** *field-of-use restrictions* (no medical/legal/military use), *scale caps* (above N users you need a separate license), *no-redistribution*, *"outputs may not train competing models,"* unclear *output ownership/commercial-use* rights, and *no indemnification for IP claims*. Any of these can block an intended deployment regardless of the model's technical quality.

> 🎯 **Exam tip — typosquatting & poisoned hubs are supply-chain attacks, governed by 4.5 controls.** Pulling `meta-llama` vs a malicious `meta-llamaa` from a model hub, or loading an untrusted **pickle**, is mitigated by **provenance verification, signing, scanning, and safetensors** — the supply-chain answers, not "train longer."

---

## 4.6 — Policies and acceptable use

Governance becomes real through **policy** that tells employees what they may and may not do with AI, and **controls** that enforce it.

### The enterprise AI usage / acceptable-use policy (AUP)

A good AI AUP typically covers:

- **Approved tools** — which AI services/models are sanctioned, and for what data.
- **Data classification rules** — what data classes (public/internal/confidential/restricted) may be entered into which tools. *Never paste secrets, PII, regulated, or restricted data into unapproved/public tools.*
- **Prohibited uses** — e.g., generating malware, harassing content, or relying on AI for high-stakes decisions without human review.
- **Human oversight / review** requirements for consequential outputs.
- **Attribution & verification** — users must verify AI output (hallucination/overreliance) and disclose AI use where required.
- **Roles & approval workflow** — who approves new AI tools/use cases (intake → review → sign-off).
- **Training & awareness** — periodic education on safe AI use and the policy itself.

### Shadow AI

**Shadow AI** = employees using **unsanctioned** AI tools (personal ChatGPT accounts, browser extensions, unapproved APIs) outside IT/governance visibility — the AI-era cousin of shadow IT.

- **Risks**: confidential/PII/IP leakage into third-party models, compliance violations, unvetted/insecure tools, no audit trail.
- **Controls**: discovery (CASB/proxy/network monitoring to find AI traffic), a clear **sanctioned-tool** list, **easy approved alternatives** (so people don't go around you), and policy + training.

> 🎯 **Exam tip — shadow AI is solved with discovery + a sanctioned path, not just a ban.** Pure prohibition drives usage underground. The exam-favored mix is **detect (CASB/DLP), provide an approved tool, and enforce policy** — give people a safe way to do what they need.

### DLP for generative AI

**Data Loss Prevention** adapted for GenAI inspects and controls what users **send to** (and receive from) AI services:

- **Egress inspection** at an **AI gateway / proxy / CASB**: block or redact prompts containing secrets, PII, source code, or classified data before they reach an external model.
- **Redaction/tokenization** of sensitive fields in prompts.
- **Blocking or warning** when an unsanctioned AI domain is accessed.
- **Logging** prompts/responses for audit (privacy-aware — don't over-collect).

> 🎯 **Exam tip — the AI gateway is where 4.6 enforcement lives.** Acceptable-use policy is the *rule*; the **AI gateway / CASB / DLP** is the *enforcement*. A scenario about "stop employees pasting customer PII into a public chatbot" wants **DLP/egress controls at a gateway + policy + sanctioned tooling**, not "tell them not to."

### Approval workflow (intake → review → deploy)

A typical sanctioned path: **request/intake → risk & impact assessment (4.2) → security/privacy/legal review → governance committee sign-off (4.1) → approved with conditions → inventory & monitor.** This is how 4.1–4.6 connect into one operating model.

---

## Putting it together — the GRC operating loop

1. **Govern (4.1):** stand up policy, a committee, and roles.
2. **Identify & assess (4.2):** inventory AI, run risk/impact assessments, log to the register.
3. **Comply (4.3):** map each system to legal/standard obligations (EU AI Act tier, GDPR, sector rules); keep records.
4. **Build trust (4.4):** measure bias/fairness, add explainability, ensure contestability.
5. **Manage the chain (4.5):** vet models/data/vendors; verify provenance, licensing, integrity.
6. **Operationalize (4.6):** publish the AUP, kill shadow AI, enforce with DLP/AI gateway, train people.
7. **Monitor & improve:** loop back — PDCA (ISO 42001) / Manage (NIST AI RMF).

---

## ✅ Check yourself

**Q1.** Name the four core functions of the NIST AI RMF and say which one is cross-cutting.
> **A.** **Govern, Map, Measure, Manage.** **Govern** is the cross-cutting function that informs the other three. (Don't confuse with NIST CSF's Identify/Protect/Detect/Respond/Recover.)

**Q2.** A vendor advertises a *certifiable* "AI management system built on Plan-Do-Check-Act." Which standard is that, and how does it differ from NIST AI RMF?
> **A.** **ISO/IEC 42001:2023 (AIMS)** — a certifiable management-system standard using **PDCA**. NIST AI RMF is **voluntary guidance** and is **not certifiable**. (ISO 42001 ≈ "ISO 27001 for AI.")

**Q3.** Under the EU AI Act, into which risk tier does a customer-service **chatbot** fall, and what is its main obligation?
> **A.** **Limited risk** → **transparency obligation**: disclose to users that they are interacting with an AI (same theme covers labeling deepfakes/synthetic media). High-risk paperwork and the prohibited ban do **not** apply.

**Q4.** A document describes a dataset's **motivation, composition, collection process, and provenance**. Is that a model card, a system card, or a datasheet?
> **A.** A **datasheet for datasets.** (Model card = one model's intended use/metrics/limitations; system card = the whole deployed system's behavior and safety mitigations.)

**Q5.** Why can't a team simply "satisfy all fairness metrics at once," and what's the right framing?
> **A.** Key fairness definitions (e.g., equal precision vs equal TPR/FPR — predictive parity vs equalized odds) are **mathematically incompatible** when group base rates differ (the impossibility result). Fairness is a **context-driven trade-off** chosen deliberately, not a metric you can max out simultaneously.

---

## Cross-references

- **Frameworks crosswalk:** [`frameworks-crosswalk.md`](frameworks-crosswalk.md) — NIST AI RMF ↔ ISO 42001 ↔ OWASP ↔ ATLAS mapping.
- **Domain 1.0 — Foundations** [`domain-1-foundations.md`](domain-1-foundations.md): §1.4 introduces NIST AI RMF, ISO 42001, OWASP, ATLAS, SAIF, and the GenAI Profile; §1.5 covers the **shared responsibility model** (model provider vs deployer vs app vs user) that underpins vendor risk in **4.5**.
- **Domain 3.0 — Securing the Lifecycle** [`domain-3-securing-lifecycle.md`](domain-3-securing-lifecycle.md): §3.1 data provenance/lineage, §3.2 **MLBOM/model signing/safetensors** (integrity controls referenced in **4.5**), §3.3 the **AI gateway** (enforcement point for **4.6** DLP).
- **Domain 5.0 — SecOps & IR** [`domain-5-secops-incident-response.md`](domain-5-secops-incident-response.md): §5.1 audit/record-keeping (supports **4.3** compliance), §5.5 vulnerability disclosure and post-incident review (feeds the **4.1/4.2** governance loop).
- **Glossary & acronyms:** [`glossary.md`](glossary.md), [`acronyms.md`](acronyms.md) — AIMS, AIA, DPIA, GPAI, RAI, XAI, SHAP/LIME, MLBOM, CASB, DLP.

---

*Unofficial community study guide. Verify all legal/regulatory specifics (EU AI Act articles, GDPR provisions, standard clause numbers) against primary sources before relying on them — this chapter intentionally describes concepts rather than citing exact article/clause numbers where precision matters.*
