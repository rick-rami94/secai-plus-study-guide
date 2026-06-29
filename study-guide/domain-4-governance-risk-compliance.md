# Domain 4.0 — AI Governance, Risk, and Compliance (19%)

Unofficial study material aligned to CompTIA SecAI+ CY0-001 V1 objectives — verify against the official objectives. See [`../exam-objectives.md`](../exam-objectives.md).

---

## What this domain is about

Domain 4 is the **governance, risk, and compliance (GRC)** layer of AI security. It is the least "hands-on-keyboard" domain and the most **vocabulary- and framework-heavy** — which is exactly why it is so testable. It covers three things: how an organization **structures itself to govern AI** (4.1), the **risks AI introduces and the responsible-AI principles** that counter them (4.2), and the **laws, frameworks, and standards** that constrain how AI is built and used (4.3).

At **19%** of a maximum-60-question exam, expect **roughly 12 questions** from this domain. CompTIA loves to make you **distinguish lookalikes**: NIST AI RMF functions vs ISO/IEC 42001, EU AI Act risk tiers, differential privacy vs anonymization, explainability vs transparency, and sanctioned vs shadow AI.

### Objectives covered

| # | Objective | Focus |
|---|-----------|-------|
| **4.1** | Explain organizational **governance structures** that support AI | AI Center of Excellence, AI policies/procedures, AI-related roles |
| **4.2** | Explain **risks** associated with AI | Responsible AI principles, AI risk categories, Shadow AI |
| **4.3** | Summarize the impact of **compliance** on business use and development of AI | EU AI Act, OECD, ISO, NIST AI RMF, corporate policy, third-party evals, data sovereignty |

**Mental model:** *Govern* (4.1) sets up who is accountable → *Risk* (4.2) names what can go wrong and what "responsible" looks like → *Compliance* (4.3) is the external law and standards layer you must satisfy.

**How to study this domain efficiently:**

- **Memorize the closed lists** — NIST AI RMF's four functions, the EU AI Act's four tiers (+ GPAI), and the responsible-AI principles. These are the most directly testable items.
- **Drill the look-alike pairs** (see the table near the end) — differential privacy vs anonymization, explainability vs transparency, sanctioned vs shadow, private vs public, sovereignty vs residency, ISO 42001 vs 23894, law vs framework.
- **Practice sorting** — expect PBQs that ask you to drag scenarios onto EU AI Act tiers, NIST functions, or AI roles. The worked examples in this chapter mirror that format.

---

## 4.1 Explain organizational governance structures that support AI

**AI governance** = the people, processes, and structures that direct and control how an organization develops, buys, and uses AI so it stays aligned with objectives, risk appetite, law, and values. Governance is **organizational and ongoing**, not a one-time project.

Across the AI life cycle, a governance program typically: **inventories** AI systems → **classifies** each by risk → **approves** use cases through a defined workflow → **assigns** ownership and controls → **monitors** behavior and drift → and **audits** for compliance. Structure (this objective) is what makes that loop repeatable instead of ad hoc.

### Organizational structures

- **AI Center of Excellence (CoE)** — a centralized, cross-functional team that sets AI **standards, reusable patterns, tooling, and guardrails** for the whole organization. It is the hub that coordinates data science, engineering, security, legal, and business stakeholders; vets use cases; curates approved models and platforms; and spreads best practices so every team is not reinventing (or re-risking) AI on its own. The CoE is about **consistency and enablement** — making the secure, compliant path the easy path.
- **AI policies and procedures** — the **written rules** that govern AI across its life cycle. *Policies* state intent and requirements; *procedures* are the step-by-step "how." Together they turn governance principles into enforceable, auditable practice. Common documents include:
  - **AI acceptable-use policy (AUP)** — what tools may be used, by whom, for what.
  - **Data-handling / classification rules** — what data may be entered into which model.
  - **Model-approval and review workflow** — how a use case gets vetted and signed off.
  - **Procurement / third-party requirements** — what vendors must attest to before adoption.
  - **Human-oversight and incident-response expectations** — where a human must stay in the loop and what to do when AI fails.

**Why these structures exist.** Without a central structure, every team negotiates AI risk independently — different tools, different data-handling habits, duplicated mistakes, and no single owner when something goes wrong. The CoE plus written policy gives the organization **one accountable structure**, a **known-good set of tools/models**, and a **repeatable approval path**, so adoption is fast *and* governed instead of fast *or* governed.

**What lives inside the CoE / governance program (typical):**

- **An AI governance committee or board** — cross-functional decision-makers (security, legal/privacy, data, business, ethics) who approve high-risk use cases and own risk acceptance.
- **A model/use-case registry** — an inventory of every AI system in use, its data, owner, risk tier, and approval status (you cannot govern what you cannot see).
- **Approved tooling and reference patterns** — vetted models, gateways, guardrails, and prompt templates teams reuse instead of rebuilding.
- **Clear ownership (RACI)** — who is *Responsible*, *Accountable*, *Consulted*, and *Informed* for each AI decision.

**Policy vs. procedure, precisely.** A **policy** is a binding statement of intent and requirement ("sensitive customer data must never be entered into a public model"). A **procedure** is the ordered steps to comply ("to request a new AI tool: submit form → security review → privacy review → CoE approval → onboarding"). A **standard** sits between them (specific mandatory choices, e.g., "approved models are X and Y"), and a **guideline** is recommended-but-optional. Exam stems often hinge on this hierarchy: intent = policy, steps = procedure.

> 🎯 **Exam tip — CoE = enablement hub, policy = the rules.** If a question describes a *central team that standardizes and accelerates safe AI adoption*, that's the **Center of Excellence**. If it describes *documented rules and approval steps*, that's **AI policies and procedures**. Intent statement = **policy**; ordered how-to steps = **procedure**.

### AI-related roles

Many of these titles overlap in the real world, but CompTIA expects you to match each to its **primary** responsibility and its **security relevance**. A useful way to group them:

- **Data layer** — *Data engineer* (pipelines), *Data scientist* (modeling/experimentation).
- **Engineering layer** — *ML engineer* (productionize models), *MLOps engineer* (automate the life cycle), *Platform engineer* (the compute beneath it).
- **Design layer** — *AI architect* (the overall solution), *AI security architect* (the security design).
- **Governance/assurance layer** — *AI governance engineer* (implement governance), *AI risk analyst* (assess risk), *AI auditor* (independently verify).

| Role | Primary responsibility | Security relevance |
|---|---|---|
| **Data scientist** | Frames the problem, explores data, selects algorithms, builds and experiments with models, interprets results. | Choices about features, training data, and metrics drive **bias, leakage, and accuracy** risk; first line to catch skewed or poisoned data. |
| **AI architect** | Designs the **end-to-end AI solution** — components, data flows, model selection, integration patterns, and how AI fits the broader enterprise architecture. | Sets the security and trust **boundaries** (where guardrails, gateways, and human oversight live); architectural decisions shape the whole attack surface. |
| **Machine learning (ML) engineer** | Turns models into **production-grade, scalable software** — training pipelines, optimization, serving, and performance. | Owns the **integrity of the training/serving pipeline**; bad pipeline hygiene enables poisoning, model theft, and supply-chain risk. |
| **Platform engineer** | Builds and maintains the **underlying compute/infrastructure platform** (clusters, GPUs, containers, networking) that AI workloads run on. | Responsible for **host/infra hardening, isolation, and tenancy** controls beneath the models. |
| **MLOps engineer** | Automates the ML **life cycle** — CI/CD for models, versioning, deployment, rollback, and **monitoring/retraining**. | Enables **drift detection, reproducibility, rollback, and auditability**; the discipline that catches model skewing and silent degradation. |
| **AI security architect** | Designs the **security controls** for AI systems — threat models, guardrails, gateways, access controls, encryption, monitoring. | Directly owns **AI-specific defenses** (prompt firewalls, model guardrails, least privilege for agents). |
| **AI governance engineer** | Implements governance **in practice** — policy-as-code, approval workflows, model registries, documentation (model cards), and control evidence. | Operationalizes **accountability and compliance**; makes governance enforceable and auditable rather than aspirational. |
| **AI risk analyst** | **Identifies, assesses, and tracks** AI risks (bias, leakage, reliability, third-party) and maintains the risk register. | Translates technical issues into **business risk**; drives risk acceptance, mitigation, and treatment decisions. |
| **AI auditor** | **Independently verifies** that AI systems meet policy, regulatory, and ethical requirements; tests controls and reviews evidence. | Provides **independent assurance**; checks for bias, hallucinations, access, and compliance gaps (ties to Domain 2.5 auditing). |
| **Data engineer** | Builds and maintains **data pipelines** — ingestion, cleansing, transformation, storage — that feed models. | Owns **data lineage, provenance, quality, and access**; a weak data pipeline is the root cause of bias, leakage, and poisoning. |

> 🎯 **Exam tip — build vs secure vs assure.** *Build* roles (data scientist, ML engineer, data/platform/MLOps engineer, AI architect) make AI work. *Secure* roles (AI security architect, AI governance engineer) design and implement controls. *Assure* roles (AI risk analyst, AI auditor) independently measure and verify. When a stem asks "who is responsible," map the verb — design, build, secure, assess, or independently verify.

**Worked example — assigning the right role.** Map each scenario to the role that *owns* it:

- *Model in production silently loses accuracy as data shifts; who detects it and triggers retraining?* → **MLOps engineer** (monitoring, versioning, retraining pipelines).
- *Who independently checks that the model meets policy and isn't biased?* → **AI auditor** (independent assurance), informed by the **AI risk analyst**'s assessment.
- *Who designs the prompt firewall and guardrails?* → **AI security architect**.
- *Who keeps the data pipeline's lineage and quality clean?* → **data engineer**.
- *Who decides how the model integrates with enterprise systems and where trust boundaries sit?* → **AI architect**.
- *Who stands up the GPU clusters and container platform the workloads run on?* → **platform engineer**.

---

## 4.2 Explain risks associated with AI

This objective has three parts that work as a matched set: the **responsible-AI principles** (what "good" looks like), the **risks** (what goes wrong when those principles are absent), and **Shadow AI** (the single most common real-world risk in enterprises). Learn the principles and risks as **opposites** of each other.

### Responsible AI principles

Responsible AI is the set of principles that make AI systems trustworthy. They are the **positive controls** that counter the risks below. Microsoft, Google, the OECD, and NIST all publish overlapping versions of these — CompTIA's list blends them, so know each by its one-line definition.

- **Fairness** — the system treats individuals and groups **equitably** and does not produce discriminatory or biased outcomes across protected attributes. *Example:* a résumé-screening model that does not down-rank candidates by gender or ethnicity.
- **Reliability and safety** — the system performs **consistently and as intended** under expected and edge conditions, and fails safely without causing harm. *Example:* a medical-triage model is validated on edge cases and defers to a human when uncertain.
- **Transparency** — stakeholders can understand **that** AI is being used, **how** it generally works, and what data and limitations apply (model cards, disclosures, documentation). *Example:* a chatbot states "I'm an AI assistant" and publishes a model card.
- **Privacy and security** — personal and sensitive data is **protected** throughout the life cycle, and the system resists misuse and attack. *Example:* encryption in use, access controls, and prompt firewalls protect training data and prompts.
- **Differential privacy** — a **mathematical technique** that adds calibrated statistical noise so the output of an analysis is essentially the same whether or not any single individual's data is included. It gives a **provable, quantifiable** privacy guarantee, letting you learn population-level patterns without exposing individuals.
- **Explainability** — the ability to **explain a specific decision or output** in human-understandable terms (why *this* input produced *that* result). Distinct from transparency, which is about overall openness. *Example:* a loan-denial includes the top factors that drove the decision (explainable AI / XAI).
- **Inclusiveness** — the system is designed to **work for and include diverse populations**, including accessibility and representation across the people it affects. *Example:* speech recognition is tested across accents and dialects.
- **Accountability** — **identifiable people and structures are answerable** for the AI's behavior and outcomes; there is clear ownership and recourse. *Example:* a named owner and governance board sign off on each high-risk model.
- **Consistency** — the system produces **stable, repeatable** behavior for equivalent inputs over time, rather than arbitrary or drifting results. *Example:* the same application data yields the same decision today and next quarter.
- **Awareness training** — **educating staff and users** on responsible AI use, risks, policies, and their obligations so governance actually reaches the people using the tools. *Example:* mandatory training on what data may never be entered into a public AI tool.

**How the principles connect.** These are not ten unrelated buzzwords — they reinforce each other. *Transparency* and *explainability* enable *accountability* (you can't hold anyone answerable for a decision no one can see or explain). *Fairness* and *inclusiveness* together prevent discriminatory and exclusionary outcomes. *Privacy and security* plus *differential privacy* protect the data subjects. *Reliability/safety* and *consistency* keep behavior trustworthy over time. *Awareness training* is what makes all of the above actually reach the humans operating the system.

> 🎯 **Exam tip — differential privacy vs anonymization.** *Anonymization* strips or generalizes identifiers from a dataset, but can be **re-identified** by linking with other data. *Differential privacy* injects **mathematical noise** to give a **provable** guarantee that any single person's presence can't be detected from the results. If the stem says "provable/quantifiable privacy guarantee" or "statistical noise," choose **differential privacy**.

> 🎯 **Exam tip — explainability vs transparency.** *Transparency* = **openness about the system overall** (it's AI, here's the model card, here are the limits). *Explainability* = **explaining a particular output/decision** in human terms. Transparency is "we tell you it's a model and how it generally works"; explainability is "here's *why* it denied your specific loan."

### Risks

These are the failure modes governance exists to prevent. Each pairs with a responsible-AI principle (see the mapping table below).

- **Introduction of bias** — training data, features, labels, or human design choices cause the model to produce **systematically unfair or skewed** outcomes for certain groups. Bias can be accidental (unrepresentative data) or introduced through attack (data poisoning, model skewing). *Example:* a hiring model trained mostly on one demographic learns to favor it.
- **Accidental data leakage** — sensitive data is **unintentionally exposed** — pasted into a public model, memorized and regurgitated in outputs, surfaced through RAG without proper authorization, or written to logs. A leading driver behind enterprise AI policy. *Example:* an employee pastes a customer list into a public chatbot and it becomes training data.
- **Reputational loss** — public **harm to brand and trust** from biased outputs, hallucinations, offensive content, privacy violations, or a publicized AI failure or breach. *Example:* a company's support bot gives confidently wrong, harmful advice that goes viral.
- **Accuracy and performance of the model** — the model is **wrong, degrades over time (drift), or hallucinates**, leading to bad decisions. Performance risk also includes latency, cost, and availability under load. *Example:* a fraud model's accuracy quietly decays as fraud patterns shift (model drift/skewing).
- **Intellectual property (IP)-related risks** — exposure on **both sides**: feeding proprietary code/data into third-party models (loss of your IP), and models generating output that **infringes** others' copyright or violates licensing — plus uncertainty over who **owns** AI-generated content. *Example:* a code assistant emits a near-verbatim copy of a copyleft-licensed snippet into your proprietary product.
- **Autonomous systems** — AI that **acts without sufficient human oversight** (agents that take real actions, make decisions, or trigger downstream effects). Risk grows with **excessive agency** — too much autonomy, permission, or trust placed in the system. Mitigated with **human-in-the-loop / human oversight**, least-privilege tool access, and approval gates on consequential actions.

**Risk → responsible-AI principle → control.** CompTIA often asks "which principle/control addresses this risk." Map them:

| AI risk | Responsible-AI principle that counters it | Example control |
|---|---|---|
| Introduction of bias | Fairness, Inclusiveness | Balanced/representative data, bias testing, fairness metrics, audit |
| Accidental data leakage | Privacy and security, Differential privacy | Data minimization/redaction, private models, DLP, output filtering |
| Reputational loss | Reliability and safety, Transparency, Accountability | Guardrails, human review, disclosure, clear ownership |
| Accuracy and performance | Reliability and safety, Consistency | Model evaluation, monitoring for drift, retraining, confidence thresholds |
| IP-related risks | Accountability, Transparency | Usage policy, license review, no proprietary data into public models |
| Autonomous systems / excessive agency | Accountability, Reliability and safety | Human oversight, least privilege, action approval gates |

### Shadow IT → Shadow AI

- **Shadow IT** — technology (apps, services, devices) adopted by employees **without IT/security approval or visibility**. It is the broader parent concept; Shadow AI is its fastest-growing, highest-data-risk subset.
- **Shadow AI** — the AI-specific case: **unsanctioned use of AI tools** (public chatbots, browser plug-ins, unapproved APIs, embedded "AI features" in SaaS) without governance oversight. The danger is twofold — **sensitive data leaving the organization** into systems with unknown retention/training practices, and **ungoverned, unaccountable outputs** (hallucinations, biased or non-compliant content) feeding real business decisions.

**Why Shadow AI is worse than classic Shadow IT.** A rogue SaaS app is a contained exposure; a public LLM can **absorb whatever you type into model training or vendor logs**, so a single paste of source code, customer PII, or strategy can leak permanently and irretrievably. The data also tends to be **unstructured and high-value** (the exact text employees are working on), which is harder to detect than a rogue database.

**How to find and fix it (defense-in-depth, not a ban):**

1. **Discover** — use CASB, secure web gateway, and DLP to see which AI domains/APIs employees actually reach.
2. **Offer a sanctioned path** — give people an **approved, private/enterprise model** so they don't need the public one. Removing the *reason* for Shadow AI works better than blocking.
3. **Policy + classification** — define what data may go to which model, backed by data classification labels.
4. **Enforce** — DLP/prompt-firewall controls to block sensitive data from leaving; awareness training so users understand *why*.
5. **Monitor and iterate** — keep the inventory current; new "AI features" appear constantly.

> 🎯 **Exam tip — Shadow AI is unsanctioned AI.** If a stem describes employees using public/free AI tools the org **never approved or can't see**, that's **Shadow AI**. The most cited harm is **accidental data leakage** of sensitive data into a public model. Remediate by **offering a sanctioned tool** plus monitoring — not just by banning.

---

## 4.3 Summarize the impact of compliance on business use and development of AI

Compliance is the **external constraint** layer: laws you *must* obey, plus standards and frameworks you *choose* (or are pressured) to adopt to prove due diligence. The distinction matters on the exam — a **law** (EU AI Act) carries legal penalties; a **framework/standard** (NIST AI RMF, ISO, OECD) is voluntary but demonstrates good practice and is increasingly referenced in contracts and by regulators. Compliance shapes **what you can build, where you can run it, what data you can feed it, and what you must disclose**.

### EU AI Act

The **European Union (EU) AI Act** is the first comprehensive, **risk-based** AI law. It classifies AI systems into tiers and applies obligations proportional to risk. It is **extraterritorial** — it can apply to organizations outside the EU whose AI affects people in the EU.

| Tier | Meaning | Obligation (in plain terms) |
|---|---|---|
| **Prohibited / Unacceptable risk** | Uses considered a clear threat to safety, rights, or livelihoods (e.g., social scoring by governments, certain manipulative or exploitative systems). | **Banned outright.** |
| **High risk** | AI used in sensitive domains (e.g., critical infrastructure, employment, education, essential services, law enforcement, biometrics). | **Strict obligations** — risk management, data governance, technical documentation, logging, transparency, human oversight, accuracy/robustness, and conformity assessment before market. |
| **Limited risk** | Systems that interact with people or generate content (e.g., chatbots, deepfakes/synthetic media). | **Transparency obligations** — users must be told they are interacting with AI or that content is AI-generated. |
| **Minimal risk** | The vast majority of AI (e.g., spam filters, AI in games). | **No mandatory obligations** beyond existing law; voluntary codes encouraged. |

**What "high-risk obligations" actually involve** (recognize these, don't memorize article numbers): a **risk-management system**, **data governance** (quality, representativeness to reduce bias), **technical documentation** and **automatic logging/record-keeping**, **transparency** to deployers, **human oversight** by design, appropriate **accuracy, robustness, and cybersecurity**, and a **conformity assessment** before the system is placed on the market.

- **General-Purpose AI (GPAI) obligations** — foundation/general-purpose models carry their **own** layer of duties (technical documentation, transparency, copyright/training-data summary), with **additional obligations for the most capable models** that may pose systemic risk.

**Enforcement and reach.** The Act is **enforced by EU authorities** and carries **tiered administrative fines** — the most severe penalties apply to **prohibited-use** violations, with smaller bands for high-risk non-compliance and for supplying incorrect information. (Know that penalties are *tiered and substantial*; don't memorize a specific euro figure for the exam unless the official objectives list one.) Because the Act applies based on **where the AI's effects land, not where the provider sits**, a U.S. company whose AI is used by people in the EU can be in scope — a key reason it influences global product decisions.

**Tier-classification practice.** Treat a stem as a sorting exercise: *Is it banned outright?* (social scoring, manipulative/exploitative systems) → **Prohibited**. *Is it a consequential, regulated-domain decision?* (hiring, credit, medical, critical infrastructure, biometrics, law enforcement) → **High**. *Does it just talk to people or generate media?* (chatbot, deepfake) → **Limited (disclose)**. *Everything else* (spam filter, game AI) → **Minimal**.

> 🎯 **Exam tip — EU AI Act has four tiers + GPAI.** Memorize **Prohibited/Unacceptable → High → Limited → Minimal**, risk *decreasing* down the list. *Prohibited* = banned (social scoring). *High* = heavy controls + conformity assessment. *Limited* = **transparency/disclosure** (tell users it's AI / it's a deepfake). *Minimal* = essentially unregulated. **GPAI/foundation models** get a separate obligation layer on top.

**Worked example — sorting scenarios into tiers:**

- *Government social-credit scoring* → **Prohibited / Unacceptable** (banned).
- *AI that screens job applicants or scores creditworthiness* → **High** (consequential decision about people; needs risk management, documentation, human oversight, conformity assessment).
- *A customer-service chatbot or an AI-generated promotional video* → **Limited** (must disclose it's AI / synthetic media).
- *An email spam filter or in-game AI* → **Minimal** (no mandatory obligations).
- *A foundation model offered as an API* → **GPAI** obligations regardless of the deployer's tier.

### OECD AI Principles / standards

The **Organisation for Economic Co-operation and Development (OECD) AI Principles** are an **intergovernmental, values-based** standard (adopted by member and partner countries) promoting **trustworthy AI**. The value-based principles emphasize:

- **Inclusive growth, sustainable development, and well-being.**
- **Human-centered values and fairness** — respect for rights, dignity, and democratic values.
- **Transparency and explainability** — meaningful information so people understand and can challenge AI outcomes.
- **Robustness, security, and safety** — systems function reliably and risks are continually managed.
- **Accountability** — organizations and individuals are answerable for proper functioning.

They are **non-binding** but highly influential — they were among the first intergovernmental AI principles and shaped national strategies and much of the vocabulary later codified in laws like the EU AI Act. Think of OECD as the **principle layer**, not an enforcement regime.

### ISO AI standards

International Organization for Standardization (ISO) — often jointly with the International Electrotechnical Commission (IEC) — publishes voluntary, **certifiable** AI standards:

- **ISO/IEC 42001 — AI management system (AIMS)** — a **management-system standard** (the "how do we run AI responsibly as an ongoing program" standard, in the same family as ISO/IEC 27001 for information security). It specifies requirements for **establishing, implementing, maintaining, and continually improving** an AI management system — policies, roles, AI risk and **impact assessments**, operational controls, and continual improvement. Like other ISO management-system standards it follows a **Plan-Do-Check-Act (PDCA)** continual-improvement cycle, so governance is a living loop rather than a one-time certification. Organizations can be **independently certified** against it, which is increasingly used to demonstrate responsible-AI maturity to customers and regulators.
- **ISO/IEC 23894 — AI risk management guidance** — **guidance** (not a certifiable requirements spec) on **managing risk** specific to AI, aligning AI risk practices with the broader ISO 31000 risk-management approach. It helps organizations identify, analyze, evaluate, and treat AI risk throughout the life cycle.

> 🎯 **Exam tip — ISO 42001 = the AI *management system*.** If a question asks for a **certifiable management-system standard** for running AI responsibly, it's **ISO/IEC 42001 (AIMS)** — the AI counterpart to ISO/IEC 27001. **ISO/IEC 23894** is AI **risk guidance**. (Don't memorize fabricated clause numbers; know what each standard *is*.)

### NIST AI Risk Management Framework (AI RMF / AIRMF)

The U.S. **National Institute of Standards and Technology (NIST) AI Risk Management Framework** is a **voluntary, non-regulatory** framework for managing AI risk and building trustworthy AI. It frames trustworthy AI around characteristics that echo the responsible-AI principles — **valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair (with harmful bias managed)**. Its operational core is **four functions** (memorize these):

| Function | What it does |
|---|---|
| **Govern** | Cultivates a **culture of risk management** — policies, roles, accountability, oversight. It is **cross-cutting** and informs all the others. |
| **Map** | **Establishes context** and identifies risks — frames the use case, stakeholders, and where AI risks could arise. |
| **Measure** | **Analyzes, assesses, and tracks** identified risks using quantitative and qualitative methods (metrics, testing, evaluation). |
| **Manage** | **Prioritizes and acts** on risks — allocates resources, treats/mitigates, monitors, and responds. |

NIST also publishes a companion **Generative AI Profile** that maps the four functions to risks specific to generative AI. The AI RMF is **voluntary** in itself, but it is widely adopted as the *de facto* baseline and is often referenced contractually or by regulators as evidence of due diligence.

> 🎯 **Exam tip — NIST AI RMF = Govern, Map, Measure, Manage.** Order matters: **Govern** is the cross-cutting culture/oversight function; then **Map** (context & identify) → **Measure** (assess & track) → **Manage** (prioritize & act). If you see "Identify/Protect/Detect/Respond/Recover," that's the **NIST CSF**, *not* the AI RMF — don't confuse the two.

### Putting the frameworks side by side

| Framework / law | Type | Binding? | Core idea |
|---|---|---|---|
| **EU AI Act** | Law (EU) | **Yes** (legally enforceable, extraterritorial) | Risk-tiered obligations + GPAI rules |
| **OECD AI Principles** | Intergovernmental principles | No (influential, non-binding) | Values for trustworthy AI |
| **ISO/IEC 42001 (AIMS)** | Management-system standard | Voluntary, **certifiable** | Run AI responsibly as an ongoing program |
| **ISO/IEC 23894** | Guidance standard | Voluntary | How to manage AI **risk** (aligns to ISO 31000) |
| **NIST AI RMF** | Framework (U.S.) | Voluntary | Manage AI risk via Govern/Map/Measure/Manage |

> 🎯 **Exam tip — law vs framework vs standard.** Only the **EU AI Act** is a *law* with legal penalties. **OECD** is non-binding *principles*. **ISO/IEC 42001** is a *certifiable management-system standard*. **NIST AI RMF** is a *voluntary framework*. Match the question's wording ("legally required," "certifiable," "voluntary framework," "principles") to the right category.

### Corporate policies

Internal rules that operationalize compliance for day-to-day AI use:

- **Sanctioned vs. unsanctioned** — *sanctioned* tools/models are **vetted and approved** for specified data and use cases; *unsanctioned* use is everything outside that — i.e., **Shadow AI**. Policy defines what is approved, for which data classifications, and how to **request additions** (so the answer to "I need a new tool" is a process, not a workaround). *Example:* the enterprise copilot on your private tenant is **sanctioned**; a personal free chatbot used to summarize an internal doc is **unsanctioned**.
- **Private vs. public models** — *private/internal* models (self-hosted or contractually isolated, e.g., a dedicated enterprise tenant) keep prompts and data **inside the organization's control**, with no third-party training on your inputs. *Public* models (consumer chatbots, shared APIs) may **retain, log, or train on inputs** and expose data outside your boundary. Policy maps **data sensitivity to model type** — sensitive data goes only to private/approved models. The trade-off:

| | Public model | Private / internal model |
|---|---|---|
| **Data exposure** | May be retained, logged, or used for training | Stays within your control boundary |
| **Cost / effort** | Low — just consume the API | Higher — hosting, ops, fine-tuning, GPU |
| **Capability** | Often the newest, largest models | May lag or require self-hosting effort |
| **Best for** | Public/low-sensitivity tasks | Confidential/regulated data and IP |
- **Sensitive data governance** — rules for **classifying, handling, and protecting** sensitive data in AI contexts: what may be entered into which model, redaction/minimization requirements, retention, and DLP enforcement. It starts with **data classification labels** (e.g., Public / Internal / Confidential / Restricted) and binds each label to allowed AI destinations and handling rules.

A common policy pattern maps **data sensitivity → permitted model**:

| Data classification | Public model (consumer chatbot/API) | Private/enterprise model (isolated, no training on inputs) |
|---|---|---|
| Public | Allowed | Allowed |
| Internal | Discouraged / with caution | Allowed |
| Confidential | **Prohibited** | Allowed with controls (redaction, logging) |
| Restricted/Regulated (PII, PHI, secrets) | **Prohibited** | Allowed only if contract + region + controls meet the regulation |

This is the operational core of "sanctioned vs unsanctioned" and "private vs public" — the policy is what stops Confidential/Restricted data from reaching a public model.

> 🎯 **Exam tip — private vs public models = where your data goes.** *Public* models may **retain/train on** your inputs and sit outside your control → keep sensitive data out. *Private/internal* models keep data **within your boundary**. The right answer usually ties **data sensitivity** to **model type** (sensitive → private/sanctioned only).

> 🎯 **Exam tip — sanctioned vs unsanctioned (= shadow).** *Sanctioned* = approved for defined data/use. *Unsanctioned* = ungoverned = **Shadow AI**. Governance converts unsanctioned use into sanctioned use by **providing approved options + monitoring**.

### Third-party compliance evaluations

When you adopt vendor AI (models, APIs, platforms), you must **assess the vendor's** security, privacy, and compliance posture before and during use. The vendor's risk becomes **your** risk — third-party evaluation is how you inherit assurance instead of inheriting unmanaged exposure. A practical evaluation checklist:

- **Certifications/attestations** — ISO/IEC 42001 (AIMS), ISO/IEC 27001, SOC 2; alignment to NIST AI RMF.
- **Data handling** — *Will they train on your inputs?* Retention periods, deletion rights, and whether prompts/outputs are logged or human-reviewed.
- **Model provenance and documentation** — model cards, training-data sources, known limitations, evaluation results, and update/versioning practices.
- **Sub-processors and hosting** — who else touches the data, and **in which regions** (ties to data sovereignty).
- **Security and incident terms** — encryption, access controls, vulnerability management, and **breach notification** commitments.
- **Contractual/usage rights** — IP ownership of outputs, indemnification, and acceptable-use constraints.

Evaluation is **continuous**, not one-time: re-assess on contract renewal, on material model/version changes, and after any vendor incident.

### Data sovereignty

**Data sovereignty** = data is subject to the **laws and regulations of the country/jurisdiction where it is collected, stored, or processed**. For AI, this constrains **where models, training data, prompts, and logs may physically reside** and which providers' regions you may use. Two related terms to keep straight:

- **Data residency** — the **physical/geographic location** where data is stored (a where-it-sits fact).
- **Data localization** — a **legal requirement** that certain data must **stay within** a country's borders.

Cross-border AI processing can violate sovereignty rules — for example, sending EU personal data to a model hosted in a region without adequate protections, or routing prompts to an API that processes them in a restricted jurisdiction. Because LLM prompts and outputs are themselves data that gets transmitted, logged, and sometimes used for training, **every prompt is a potential cross-border transfer**. Policy must therefore control **model region selection, data location, prompt/log retention location, and lawful transfer mechanisms**, and procurement must confirm where a vendor (and its sub-processors) actually processes data.

### Net impact of compliance — on *use* and on *development*

The objective is about impact on both sides of the AI life cycle:

- **Impact on business *use*** — restricts which tools employees may use (sanctioned only), which data may be entered (sensitive-data governance), which regions may process it (sovereignty), and what must be disclosed to end users (EU AI Act limited-risk transparency).
- **Impact on *development*** — shapes how teams build: **data minimization and lawful basis** for training data, **documentation and record-keeping** (model cards, technical files), **bias testing and human-oversight** design, **conformity assessment** before a high-risk system goes to market, and **vendor/component vetting** for the AI supply chain.

The practical effect: compliance turns "ship fast" into "ship governed" — it adds gates (approval, documentation, assessment) that, done well, are absorbed into the normal life cycle rather than bolted on at the end.

> 🎯 **Exam tip — data sovereignty = jurisdiction's laws follow the data.** If a stem worries about **which country's law applies** or **where data/prompts are stored and processed**, that's **data sovereignty**. *Residency* = merely *where* data sits; *localization* = a *legal must-stay-in-country* rule. The control is choosing **compliant regions**, confirming vendor/sub-processor locations, and restricting cross-border transfer of prompts, training data, and logs.

---

---

## How 4.1, 4.2, and 4.3 fit together

Picture a single AI decision flowing top-down. **Governance (4.1)** decides *who is accountable* and sets the policies — the CoE approves the use case, assigns an owner, and the AI risk analyst and auditor stand by to assess and verify. **Risk (4.2)** asks *what could go wrong* — bias, leakage, reputational loss, inaccuracy, IP exposure, runaway autonomy, or someone quietly using Shadow AI — and the responsible-AI principles define what "doing it right" looks like. **Compliance (4.3)** imposes the *external rules* — the EU AI Act tier sets mandatory obligations, NIST/ISO/OECD provide the methods to manage and prove it, corporate policy maps sensitive data to private vs. public models, third-party evaluations vet vendors, and data sovereignty constrains where it all runs. Strong programs run all three continuously: govern, assess risk, comply, monitor, repeat.

---

## Common look-alikes (don't get tricked)

| If the stem says… | Pick… | Not… |
|---|---|---|
| "provable guarantee via added statistical noise" | **Differential privacy** | Anonymization |
| "remove identifiers; could be re-identified" | **Anonymization** | Differential privacy |
| "explain *this specific* decision/output" | **Explainability** | Transparency |
| "be open that it's AI / publish a model card" | **Transparency** | Explainability |
| "central team that standardizes safe AI adoption" | **AI Center of Excellence** | Governance committee alone |
| "Govern / Map / Measure / Manage" | **NIST AI RMF** | NIST CSF (IPDRR) |
| "certifiable AI management system" | **ISO/IEC 42001 (AIMS)** | ISO/IEC 23894 |
| "guidance for managing AI risk" | **ISO/IEC 23894** | ISO/IEC 42001 |
| "risk tiers: Prohibited/High/Limited/Minimal" | **EU AI Act** | NIST AI RMF |
| "employees using unapproved public AI tools" | **Shadow AI** | Sanctioned use |
| "data is governed by the law of where it lives" | **Data sovereignty** | Data residency (location only) |

## 🎯 Exam tips (rapid review)

- **NIST AI RMF functions:** **Govern, Map, Measure, Manage** (Govern is cross-cutting). Not CSF's IPDRR.
- **EU AI Act tiers:** **Prohibited/Unacceptable → High → Limited → Minimal**, plus a **GPAI** obligation layer. Limited = transparency/disclosure.
- **Differential privacy vs anonymization:** differential privacy = **provable mathematical noise**; anonymization = remove identifiers (re-identifiable).
- **Explainability vs transparency:** explainability = explain **a specific output**; transparency = **overall openness** about the system.
- **Sanctioned vs unsanctioned / Shadow AI:** unsanctioned = ungoverned = **Shadow AI**; fix by offering sanctioned tools + monitoring.
- **Private vs public models:** public may **retain/train on inputs** → keep sensitive data out; private keeps data in your boundary.
- **Data sovereignty:** the **jurisdiction's laws** govern data wherever it lives → use compliant regions, control transfers.
- **ISO/IEC 42001 = AI management system (AIMS), certifiable;** ISO/IEC 23894 = AI **risk guidance**.
- **Law vs framework:** only the **EU AI Act** carries legal penalties; OECD/ISO/NIST are voluntary (but expected).
- **OECD = non-binding principles;** the first major intergovernmental trustworthy-AI values that shaped later law.
- **AI Center of Excellence = central enablement hub;** governance committee/board = the approval/risk-acceptance body.
- **Roles:** build (data/ML/MLOps/platform engineers, data scientist, AI architect) vs secure (AI security/governance) vs assure (risk analyst, auditor).
- **EU AI Act is extraterritorial** — non-EU companies are in scope if their AI affects people in the EU.
- **Third-party/vendor risk = your risk** — vet certifications, training-on-your-data terms, region/sub-processors; re-assess continuously.
- **Autonomous systems / excessive agency** → counter with **human-in-the-loop, least privilege, and action approval gates**.
- **Awareness training** is itself a responsible-AI principle — it's how policy reaches the people typing the prompts.

---

## ✅ Check yourself

1. **Q:** An employee pastes proprietary source code into a free public chatbot to debug it. Name the governance problem and its top risk.
   **A:** This is **Shadow AI** (unsanctioned AI use). The top risk is **accidental data leakage** of IP into a public model that may retain or train on the input — also an **IP-related risk**. Remediate with a **sanctioned/private** tool plus DLP and policy.

2. **Q:** Which NIST AI RMF function "establishes context and identifies risks," and which "analyzes and tracks" them?
   **A:** **Map** establishes context and identifies risks; **Measure** analyzes, assesses, and tracks them. (**Govern** is cross-cutting; **Manage** prioritizes and acts.)

3. **Q:** Under the EU AI Act, a customer-facing chatbot and AI-generated marketing images fall into which tier, and what is required?
   **A:** **Limited risk** — the obligation is **transparency/disclosure**: users must be told they are interacting with AI and that content is AI-generated.

4. **Q:** A vendor claims its analytics give a "provable guarantee that no individual can be identified from the results, using added statistical noise." Which responsible-AI concept is this — and how does it differ from anonymization?
   **A:** **Differential privacy.** It provides a **mathematical, quantifiable** guarantee via calibrated noise, whereas **anonymization** merely removes/generalizes identifiers and can be **re-identified** by linking datasets.

5. **Q:** A bank wants to deploy a model that decides loan approvals for EU customers. Which EU AI Act tier, what is required, and which responsible-AI principles are most at stake?
   **A:** **High risk** (a consequential decision about people). It requires risk management, data governance, technical documentation, logging, **human oversight**, accuracy/robustness, and conformity assessment before deployment. The principles most at stake are **fairness** (no discriminatory denials), **explainability** (tell applicants why), and **accountability** (a named owner answerable for outcomes). *(Bonus: a **certifiable management-system standard** to run this program continuously is **ISO/IEC 42001 (AIMS)**, with **ISO/IEC 23894** as AI risk guidance.)*

---

## Cross-references

- **Governance protects against these threats:** [`./domain-2-securing-ai-systems.md`](./domain-2-securing-ai-systems.md) — bias, poisoning, leakage, model theft.
- **Auditing for quality and compliance (hallucinations, bias, access):** Domain 2.5 in [`./domain-2-securing-ai-systems.md`](./domain-2-securing-ai-systems.md).
- **AI life cycle, human oversight, data security foundations:** [`./domain-1-ai-concepts.md`](./domain-1-ai-concepts.md).
- **AI-assisted security operations:** [`./domain-3-ai-assisted-security.md`](./domain-3-ai-assisted-security.md).
- **Frameworks & ID crosswalk:** [`./frameworks-crosswalk.md`](./frameworks-crosswalk.md) · **Glossary:** [`./glossary.md`](./glossary.md) · **Acronyms:** [`./acronyms.md`](./acronyms.md)
- **Blueprint & objective numbering:** [`../exam-objectives.md`](../exam-objectives.md)

> ⚠️ Reminder: community-authored study aid. Where it differs from the official CompTIA SecAI+ objectives, the official document wins.
