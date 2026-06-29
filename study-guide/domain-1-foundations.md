# Domain 1.0 — AI & Security Foundations

> ⚠️ **UNOFFICIAL / COMMUNITY STUDY MATERIAL.** Not affiliated with, endorsed by, or sourced from CompTIA. Built from the well-established AI-security body of knowledge (OWASP, NIST, MITRE, ISO, Google SAIF). Reconcile against the **official** CompTIA SecAI+ objectives before exam day. Blueprint: [`../exam-objectives.md`](../exam-objectives.md).

---

## What this domain tests

Domain 1 (**16%** of the exam) is the vocabulary-and-mental-model layer. You are not yet attacking or defending anything — you are proving you can **speak AI fluently** and **place AI inside a security frame**. Expect definition-matching, "which component does X" identification, framework-recognition, and shared-responsibility scenarios. Master this domain and Domains 2–5 become much easier, because every later attack and control is described in this language.

The five objectives:

- **1.1** — AI/ML concepts relevant to security (learning paradigms, deep learning, LLMs/GenAI/foundation models/transformers, embeddings, tokens, RAG, agents/tool use/MCP, fine-tuning vs prompting, RLHF, temperature, hallucination, context windows).
- **1.2** — AI system components and architectures (training vs inference, model serving, ML/LLM pipelines, MLOps/LLMOps, data pipelines, model registry, feature store, vector DB, AI gateway, orchestration).
- **1.3** — The AI threat landscape and how AI changes the security model (new attack surface, non-determinism, data-centric risk, AI/ML supply chain, dual-use, autonomy, speed/scale).
- **1.4** — Core AI security principles and frameworks (CIA + safety/privacy/fairness; secure-by-design; NIST AI RMF, OWASP LLM Top 10 (2025), OWASP ML Top 10, MITRE ATLAS, ISO/IEC 42001, Google SAIF, NIST GenAI Profile).
- **1.5** — Roles, responsibilities, and the **shared responsibility model** for AI (provider vs deployer vs application vs user; data owners; governance roles; SaaS LLM vs self-hosted).

---

## 1.1 AI/ML concepts relevant to security

### The learning paradigms

Machine learning systems "learn" a function from data instead of being explicitly programmed. The three classic paradigms:

| Paradigm | What it learns from | Typical output | Security-relevant example |
|---|---|---|---|
| **Supervised learning** | **Labeled** data (input → known correct output) | Classification or regression | Spam filter, malware classifier, phishing detector. Poisoning the **labels** flips its decisions. |
| **Unsupervised learning** | **Unlabeled** data; finds structure/patterns | Clusters, anomalies, dimensionality reduction | Network **anomaly detection**, user-behavior baselining (UEBA). |
| **Reinforcement learning (RL)** | **Reward signals** from interacting with an environment | A **policy** (what action to take) | Game agents, robotics; conceptually underlies **RLHF** alignment of LLMs. |

> Two often-tested middle categories: **semi-supervised** (small labeled set + large unlabeled set) and **self-supervised** (labels are generated from the data itself — the pretraining method behind most LLMs, e.g., "predict the next token").

**Deep learning** is a subset of ML that uses multi-layer **neural networks** (many "hidden layers") to learn hierarchical features. More layers/parameters → more capacity, but also more opacity (the "black box" problem that makes **explainability** hard — see 4.4).

Remember the nesting: **AI ⊃ Machine Learning ⊃ Deep Learning ⊃ (transformers/LLMs)**. Generative AI is an *application class*, not a strict subset level.

### Generative AI, foundation models, LLMs, and transformers

- **Generative AI (GenAI)** — models that *produce* new content (text, code, images, audio) rather than only classifying or scoring existing input.
- **Foundation model** — a large model **pretrained on broad data at scale** that can be **adapted** (fine-tuned/prompted) to many downstream tasks. LLMs are the text/code variety.
- **Large Language Model (LLM)** — a foundation model trained to predict tokens of natural language/code.
- **Transformer** — the dominant neural-network **architecture** behind modern LLMs. Its key mechanism is **self-attention**, which lets the model weigh the relevance of every token to every other token. You do **not** need the math; you *do* need to know "transformer = the architecture; attention = the core mechanism."

### Tokens, embeddings, and vectors

- **Token** — the unit an LLM reads/writes; roughly a word-piece (~4 characters of English on average). Models are billed and bounded in tokens. **Tokenization** converts text ↔ token IDs.
- **Embedding** — a numeric **vector** that represents the *meaning* of a token, sentence, or document in high-dimensional space. Similar meanings → nearby vectors. Embeddings power **semantic search** and **RAG**.
- **Vector** — the array of numbers itself. Stored and searched in a **vector database** (see 1.2). Security note: embeddings can be **inverted** to partially reconstruct sensitive source text (**embedding inversion** — OWASP **LLM08 Vector and Embedding Weaknesses**).

### Context window, temperature/sampling, hallucination

| Concept | Definition | Why security cares |
|---|---|---|
| **Context window** | The maximum tokens (prompt + history + retrieved data + output) the model can consider at once | Overflowing or stuffing it enables some injection/DoS effects; truncation can drop guardrail instructions. |
| **Temperature / sampling** | A knob (0 → deterministic-ish, higher → more random/creative) plus methods like top-k/top-p that pick the next token | Affects **reproducibility**; higher temperature widens unpredictable (and jailbreak-prone) outputs. |
| **Hallucination** | Confident output that is **fabricated or factually wrong** | Drives **misinformation (LLM09)** and **overreliance**; an integrity/trust risk, not a "bug" you can fully patch. |

> Even at temperature 0, LLMs are **not fully deterministic** across hardware/batching — a key point for 1.3's "non-determinism" theme.

### Adapting models: fine-tuning vs prompting vs RAG

You change a foundation model's behavior in three broad ways:

| Approach | What it changes | Data freshness | Cost/risk profile |
|---|---|---|---|
| **Prompting** (incl. few-shot, system prompts) | Nothing in the model — only the input instructions | Only what you paste in | Cheapest; vulnerable to **prompt injection**; system prompt can **leak (LLM07)**. |
| **Fine-tuning** | The model **weights** (further training on your data) | Frozen at training time | Costly; your private/PII training data can be **memorized and regurgitated**; poisoned fine-tune data = **LLM04**. |
| **RAG (Retrieval-Augmented Generation)** | Nothing in the weights; **retrieves** relevant documents at query time and inserts them into the prompt | **Fresh / updatable** without retraining | Retrieved content is untrusted → **indirect prompt injection** and **RAG data leakage** if document-level authZ is broken. |

**RAG vs fine-tuning** is one of the most-tested comparisons. Quick rule: need **current or proprietary facts with citations and access control** → **RAG**; need a **new style, format, or skill baked in** → **fine-tuning**. They are often combined.

- **RLHF (Reinforcement Learning from Human Feedback)** — an alignment technique that uses human preference rankings to train a reward model, then RL-tunes the LLM to be more helpful/harmless. It is *why* models refuse harmful requests; **jailbreaks** are attempts to defeat RLHF alignment.

### AI agents, tool use, and MCP

- **AI agent** — an LLM that can **plan and take actions** by calling **tools** (functions/APIs), reading results, and looping until a goal is met. Agency = autonomy = expanded blast radius.
- **Tool use / function calling** — the model emits a structured request to invoke an external capability (search the web, run code, query a DB, send email).
- **MCP (Model Context Protocol)** — an **open standard for connecting models/agents to tools and data sources** via servers. It standardizes tool exposure; security-wise it introduces **tool-server trust**, over-broad permissions, and **confused-deputy** risks (Domain 2.4). MCP is a *connector standard*, not a model.

> Agentic risk shows up repeatedly: **Excessive Agency (LLM06)** is granting an agent more **functionality, permissions, or autonomy** than the task needs.

**Worked example — how the pieces connect.** A support agent receives "Refund order #123." The text is **tokenized**; the model (a **transformer-based LLM**, a **foundation model** fine-tuned for support) decides to call a `lookup_order` **tool** over **MCP**, retrieves the policy via **RAG** (query **embedded** → matched in a **vector DB**), then calls `issue_refund`. Every hop is a trust boundary: the user message (LLM01), the retrieved policy doc (indirect injection), the tool's permissions (LLM06), and the model's output before it hits `issue_refund` (LLM05). One objective, five places to attack — that is why Domain 1 vocabulary matters.

> 🎯 **Exam tips — 1.1**
> - Match definitions precisely: **supervised = labeled**, **unsupervised = unlabeled/anomaly**, **RL = reward/policy**. Anomaly detection is the classic unsupervised security example.
> - **RAG ≠ fine-tuning.** Distractor traps: "RAG changes the model weights" (false), "fine-tuning gives real-time data" (false).
> - **Hallucination** is a property of how LLMs generate, not a virus or breach. Map it to **LLM09 Misinformation** and overreliance.
> - **Embeddings = vectors of meaning;** they can leak source data (LLM08). Don't confuse an embedding with encryption — embeddings are *not* a security control.
> - **MCP** is a tool/data **connector standard** (think "USB-C for AI tools"), not an attack and not a model.

---

## 1.2 AI system components and architectures

### Training vs inference — the two phases

| | **Training (build time)** | **Inference (run time / serving)** |
|---|---|---|
| Goal | Learn weights from data | Produce predictions/outputs for users |
| Inputs | Large datasets, labels | A single prompt/request |
| Cost driver | Massive compute, GPUs, time | Per-request latency and tokens |
| Key threats | **Data poisoning, backdoors**, training-data theft, supply-chain of datasets/base models | **Prompt injection, evasion/adversarial examples, model extraction, DoS/unbounded consumption, output handling** |
| Who touches it | Data scientists, ML engineers | End users, applications, agents |

Knowing *which phase a control or attack belongs to* is heavily tested. Poisoning is a **training-time** integrity attack; prompt injection is an **inference-time** attack.

### The components you must recognize

| Component | What it is | Security relevance |
|---|---|---|
| **Data pipeline** | Ingests, cleans, transforms, and labels data for training/inference | Entry point for **poisoning** and provenance/lineage gaps. |
| **Feature store** | Central repo of curated, reusable **features** for ML models | Integrity/consistency of features; access control; training/serving skew. |
| **Model registry** | Versioned catalog of trained models + metadata (lineage, stage) | **Integrity/signing**, provenance, rollback; a compromised registry ships malicious models (Domain 2.3). |
| **Model serving / inference endpoint** | The API that loads a model and returns predictions | The exposed attack surface: authN/Z, rate limiting, input/output handling, hardening. |
| **Vector database** | Stores embeddings; does similarity search for **RAG** | **LLM08** weaknesses; document-level authorization; index poisoning. |
| **AI gateway** | A proxy in front of model APIs | Central place for **guardrails, rate limiting/quotas, key management, logging, routing, content filtering**. A top control surface in Domain 3. |
| **Orchestration framework** | Coordinates multi-step chains/agents/tools (e.g., chains, graphs, agent loops) | Expands agentic attack surface; where tool allow-listing and HITL live. |

### MLOps vs LLMOps

**MLOps** is DevOps for ML: versioned data/models, reproducible pipelines, CI/CD, monitoring, and **drift** detection. **LLMOps** extends this for foundation models/LLMs: prompt management/versioning, **evals**, guardrails, **AI gateway**, token/cost monitoring, and RAG index management.

| | MLOps (classic ML) | LLMOps (LLM/GenAI) |
|---|---|---|
| Core artifact | Trained model + features | Prompts, base/fine-tuned model, RAG index |
| You usually | Train your own model | Consume a **third-party foundation model** |
| Eval focus | Accuracy/precision/recall, drift | Quality, safety, jailbreak/red-team **evals**, hallucination rate |
| Distinct controls | Feature store, model registry | **AI gateway, guardrails, prompt templates, vector DB, token quotas** |

A reference request path to memorize:
**User → AI gateway (authN/Z, guardrails, rate limit, logging) → orchestrator → [RAG: embed query → vector DB → retrieve] → LLM inference endpoint → output guardrails → user.**

> 🎯 **Exam tips — 1.2**
> - Pin every attack/control to **training vs inference.** Poisoning/backdoor = training; injection/evasion/extraction/DoS = inference.
> - **AI gateway** = the centralized choke point for rate limiting, guardrails, key management, and logging. If a question asks "where do you enforce org-wide LLM rate limits/quotas?" → AI gateway.
> - **Model registry** = integrity/versioning/provenance of *models*; **vector database** = storage/search of *embeddings* for RAG. Don't swap them.
> - **Feature store** ≠ vector database. Feature store serves ML features; vector DB serves embeddings for retrieval.
> - **MLOps ≠ LLMOps**, but LLMOps is an extension, not a replacement.

---

## 1.3 The AI threat landscape — how AI changes the security model

AI does not delete classic security; it **adds new dimensions on top of it**. The blueprint's themes:

| Shift | What it means | Concrete consequence |
|---|---|---|
| **Expanded / novel attack surface** | New inputs (prompts, training data, retrieved docs, tool outputs, model files) become attack vectors | Prompt injection, poisoning, malicious model files have **no analog** in traditional appsec. |
| **Non-determinism** | Same input can yield different outputs; behavior is **probabilistic** | Hard to test/repro, hard to write deterministic detections, guardrails can be bypassed by rewording. |
| **Data-centric risk** | The model **is** its training data; behavior is shaped by data, not just code | Data quality/poisoning/leakage become first-class security problems; **memorization** can regurgitate PII/secrets. |
| **AI/ML supply chain** | Heavy reliance on third-party **base models, datasets, weights, and ML libraries** | Poisoned models, **unsafe deserialization** (pickle), typosquatted models/packages, hub compromise (**LLM03 Supply Chain**). |
| **Dual-use** | The same capability helps defenders and attackers | LLMs assist with phishing, malware, and recon at scale; "jailbreak to misuse." |
| **Autonomy & agency** | Agents take real actions with real permissions | A single injection can trigger **lateral movement, SSRF, data exfiltration** (Excessive Agency, LLM06). |
| **Speed & scale of impact** | Automation compresses time-to-impact | One poisoned model or prompt template can affect **every** downstream user instantly. |

**The blurring of code and data.** In a classic app, instructions (code) and inputs (data) are separated. In an LLM, the **prompt is both** — the model cannot reliably tell a developer's instruction from attacker text embedded in a user message or a retrieved web page. This single property is the root cause of **prompt injection (LLM01)** and is the most important conceptual takeaway of Domain 1.

**Trust boundaries move.** Untrusted content now includes: user prompts, **retrieved documents** (RAG), **tool/function outputs**, and even prior conversation/memory. Treat **model output as untrusted** too (drives **Improper Output Handling, LLM05**).

**Classic vs AI security — what actually changes:**

| Dimension | Traditional software | AI / LLM system |
|---|---|---|
| Behavior | Deterministic, specified by code | **Probabilistic**, learned from data |
| Code vs data | Separated | **Fused in the prompt** — root cause of injection |
| Primary asset to protect | Source/credentials/data | **+ training data, weights, prompts, embeddings** |
| Failure mode | Crash / wrong-but-explainable result | **Confident hallucination**, silent drift, jailbreak |
| Patch | Fix code, redeploy | May require **retrain / re-tune / new guardrails** |
| Testing | Repeatable unit/integration tests | **Evals, red-teaming**, statistical thresholds |

Note that AI **does not remove** classic risks (authN/Z, injection into downstream systems, secrets, supply chain) — it **layers new ones on top**. Most real incidents combine both: e.g., a prompt injection (new) that triggers an SSRF (classic) via an over-permissioned tool (new).

> 🎯 **Exam tips — 1.3**
> - The flagship idea: LLMs **mix instructions and data in the same channel** → that is *why* prompt injection works and *why* you cannot fully "input-validate" it away.
> - **Non-determinism** is a defining property, not a defect. Watch distractors claiming AI behavior is "fully deterministic and testable like normal software."
> - "Data-centric" means risk lives in **data**, not only in code. Expect scenarios where the vuln is a poisoned dataset, not a software CVE.
> - **Dual-use** = same tech aids attacker and defender. **Speed/scale** = automated, instant, broad blast radius.
> - Treat **retrieved content and tool output as untrusted input**, and **model output as untrusted** before using it downstream.

---

## 1.4 Core AI security principles and frameworks

### Security principles applied to AI

The **CIA triad** still anchors everything, reinterpreted for AI, and is **extended** with properties AI forces into scope:

| Property | Classic meaning | AI-specific expression |
|---|---|---|
| **Confidentiality** | Prevent unauthorized disclosure | Protect training data, weights, prompts, embeddings; stop **sensitive info disclosure (LLM02)**, model **extraction**, membership inference. |
| **Integrity** | Prevent unauthorized modification | Defend against **poisoning, backdoors**, model/file tampering, **misinformation/hallucination**, prompt injection altering behavior. |
| **Availability** | Keep the system usable | Defend inference endpoints against **DoS / unbounded consumption (LLM10)** and cost/"sponge" attacks. |
| **+ Safety** | (new) | The model should not cause harm or take harmful actions (esp. agents). |
| **+ Privacy** | (new) | Minimize/protect PII; resist memorization, re-identification, regurgitation. |
| **+ Fairness** | (new) | Avoid biased/discriminatory outcomes; tied to ethics/XAI (Domain 4.4). |

**Secure-by-design / Secure AI** — bake security in from the start of the AI lifecycle (threat-model the data, training, deployment, and agent permissions) rather than bolting it on. This is the spirit behind Google **SAIF** and NIST guidance.

### The frameworks you must recognize (and not confuse)

| Framework | Type | One-line scope | Key fact to memorize |
|---|---|---|---|
| **NIST AI RMF** (AI 100-1) | Voluntary risk-management framework | Manage AI risk across the lifecycle | Core functions: **Govern, Map, Measure, Manage**. (Govern is cross-cutting.) |
| **NIST GenAI Profile** (**AI 600-1**) | Companion profile to the AI RMF | Applies the RMF to **generative AI** risks | A *profile of* the AI RMF — not a separate framework. |
| **OWASP Top 10 for LLM Applications (2025)** | Risk list | Top vulns in LLM apps | The 10 below — memorize IDs **LLM01–LLM10**. |
| **OWASP ML Security Top 10** | Risk list | Top vulns in **classic ML** (poisoning, evasion, inversion, etc.) | Distinct from the LLM list; ML-focused, not LLM-focused. |
| **MITRE ATLAS** | Adversarial-ML **knowledge base** (ATT&CK-style) | Real-world tactics/techniques against AI systems | Techniques use **AML.T####** IDs and tactics; ATT&CK for AI. |
| **ISO/IEC 42001** | Certifiable **management-system** standard | **AI Management System (AIMS)** — governance, like ISO 27001 for AI | It is a *governance/management* standard, not a control checklist. |
| **ISO/IEC 23894** | Guidance standard | AI **risk management** guidance | Pairs with ISO 31000; governance-side. |
| **Google SAIF** | Vendor framework | **Secure AI Framework** — secure-by-design conceptual framework + practices | Industry secure-by-design guidance. |

#### OWASP Top 10 for LLM Applications (2025) — memorize exactly

| ID | Name | Plain meaning |
|---|---|---|
| **LLM01** | **Prompt Injection** | Attacker text overrides intended instructions (direct or **indirect** via retrieved/tool content). |
| **LLM02** | **Sensitive Information Disclosure** | Model leaks PII, secrets, proprietary data. |
| **LLM03** | **Supply Chain** | Compromised models, datasets, weights, plugins, or dependencies. |
| **LLM04** | **Data and Model Poisoning** | Tampering with training/fine-tune/embedding data or the model itself (incl. backdoors). |
| **LLM05** | **Improper Output Handling** | Downstream systems trust model output → XSS, SSRF, code/command injection. |
| **LLM06** | **Excessive Agency** | Agent has too much functionality, permission, or autonomy. |
| **LLM07** | **System Prompt Leakage** | Secrets/logic in the system prompt are exposed or relied upon insecurely. |
| **LLM08** | **Vector and Embedding Weaknesses** | RAG/embedding flaws: inversion, poisoning, cross-tenant/doc-auth leakage. |
| **LLM09** | **Misinformation** | Confident, wrong, or fabricated output (hallucination) + overreliance. |
| **LLM10** | **Unbounded Consumption** | Resource/cost exhaustion, model DoS, model extraction via volume. |

**Which framework when (decision aid):**

- "We need to *stand up AI governance / get certified*" → **ISO/IEC 42001** (AIMS), supported by **NIST AI RMF**.
- "We need to *identify and manage AI risk across the lifecycle*" → **NIST AI RMF** (+ **AI 600-1** for GenAI specifics).
- "We need a *checklist of LLM-app vulnerabilities to test for*" → **OWASP Top 10 for LLM Applications (2025)**.
- "We need *classic-ML* vulnerabilities (poisoning/evasion/inversion)" → **OWASP ML Security Top 10**.
- "We need to *describe attacker tactics/techniques* or map an incident" → **MITRE ATLAS**.
- "We want *secure-by-design engineering practices* from industry" → **Google SAIF**.

> The frameworks split cleanly by **purpose**: **NIST AI RMF / ISO 42001 = govern & manage risk** (the "should we / how do we run this safely" layer); **OWASP lists / MITRE ATLAS = specific technical vulnerabilities & attacker techniques** (the "what goes wrong / how they hit us" layer); **SAIF = secure-by-design practices.** A frameworks crosswalk lives in [`frameworks-crosswalk.md`](frameworks-crosswalk.md).

> 🎯 **Exam tips — 1.4**
> - **NIST AI RMF functions = Govern, Map, Measure, Manage.** Classic distractor: swapping in **Identify/Protect/Detect/Respond/Recover** — that's the **NIST CSF**, not the AI RMF.
> - **ISO/IEC 42001 = AI management system (AIMS)** — the "ISO 27001 of AI." It is **governance**, not a vuln list.
> - **MITRE ATLAS = adversarial-ML knowledge base** (ATT&CK-style, **AML.T####**). Do **not** confuse with ATT&CK itself or with OWASP.
> - **OWASP ML Top 10 (classic ML) vs OWASP LLM Top 10 (2025)** are *different lists*. Poisoning/evasion/inversion lean ML; prompt injection/excessive agency are LLM.
> - **NIST AI 600-1** is the **Generative AI Profile** *of* the AI RMF, not a standalone framework.
> - Know that **CIA is extended** with **safety, privacy, fairness** for AI — a frequent "select all that apply" target.

---

## 1.5 Roles, responsibilities, and the shared responsibility model for AI

Security responsibility for an AI system is **split across layers**, similar to cloud's shared responsibility model — and *where the split sits depends on the deployment model.*

### The layers

| Layer / role | Owns | Typical security responsibility |
|---|---|---|
| **Model provider** | The foundation model: pretraining data, weights, base alignment/safety | Model-level safety/alignment, secure training, model card/disclosure, infra of the hosted API. |
| **Platform / deployer** | The environment hosting/serving the model (cloud, inference platform, AI gateway) | Hardening serving infra, network/isolation, key management, rate limiting, logging. |
| **Application / integrator** | The app built on the model (prompts, RAG, agents, tools, business logic) | **Prompt hardening, output handling, guardrails, tool allow-listing, authZ, RAG document-level access**, data sent to the model. |
| **End user** | How the system is used | Acceptable use, not pasting secrets, not over-relying on output. |
| **Data owner** | The datasets used for training/fine-tuning/RAG | Classification, consent/licensing, provenance, minimization, access control. |
| **AI governance roles** | Oversight | Policy, risk acceptance, impact assessments, compliance (Domain 4). Roles: AI/ML security engineer, **AI governance lead / responsible-AI officer**, data steward, risk owner, model owner. |

> **Key principle:** the **application/integrator** carries most of the *application-layer* AI security burden — **prompt injection, insecure output handling, excessive agency, and RAG authorization are almost always the deployer's/app's responsibility, not the model provider's.** This is a favorite exam scenario.

### SaaS LLM vs self-hosted — the responsibility line moves

| Aspect | **SaaS / hosted LLM API** (e.g., a managed model endpoint) | **Self-hosted / open-weights model** (you run it) |
|---|---|---|
| Model weights & training security | **Provider** | **You** (you obtain weights → supply-chain & integrity is yours) |
| Serving infrastructure & patching | **Provider** | **You** (host hardening, GPU/server, scaling) |
| Base safety alignment | **Provider** | **You** (you may need to add your own guardrails) |
| Data sent in prompts / data residency | **You** (don't send regulated data without contractual/technical controls) | **You** (but stays in your environment) |
| Prompts, RAG, agents, output handling, tool perms | **You** | **You** |
| Logging, monitoring, abuse detection | Shared (provider may log; you log your app) | **You** |

Mental model: **moving from SaaS to self-hosted shifts more responsibility onto you** — you gain control and data locality but inherit model integrity, infra hardening, and patching. Either way, the **application-layer** AI risks (LLM01/05/06/08) stay with **you**.

> A useful analogy: SaaS LLM ≈ **SaaS** (provider owns most of the stack, you own data/usage/config); self-hosted open-weights ≈ **IaaS/on-prem** (you own almost everything above the silicon).

> 🎯 **Exam tips — 1.5**
> - In a scenario, decide **which layer** owns the control. **Prompt injection, output handling, excessive agency, RAG authZ → application/deployer**, *not* the model provider.
> - **Self-hosting shifts responsibility toward you** (infra, weights integrity, patching, alignment). SaaS keeps those with the provider — but **your prompt/RAG/agent/data choices are always yours**.
> - **Data owner** ≠ model provider. Consent, licensing, classification, and provenance belong to whoever owns the data.
> - "The provider handles all our AI security" is a **trap** — shared responsibility never fully offloads the application layer.
> - Match governance titles to duties: **responsible-AI officer / AI governance lead** = policy & oversight; **data steward** = data quality/classification; **model owner** = lifecycle of a specific model.

---

## Key terms in this domain

| Term | Quick definition |
|---|---|
| **Supervised / unsupervised / RL** | Learn from labeled data / unlabeled patterns / reward signals. |
| **Foundation model** | Large model pretrained broadly, adapted to many tasks. |
| **LLM / transformer / attention** | Token-predicting foundation model / its architecture / its core mechanism. |
| **Token / embedding / vector** | Unit of text / numeric meaning-representation / the number array stored & searched. |
| **Context window** | Max tokens the model can consider at once (prompt + history + retrieval + output). |
| **Temperature** | Randomness/creativity knob for token sampling. |
| **Hallucination** | Confident but fabricated/incorrect output (→ LLM09). |
| **RAG** | Retrieve external docs at query time and inject into the prompt; fresh, updatable. |
| **Fine-tuning** | Further-train weights on your data; bakes in style/skill, can memorize data. |
| **RLHF** | Human-preference alignment; what jailbreaks try to defeat. |
| **AI agent / tool use** | LLM that plans and calls external functions/APIs to act. |
| **MCP** | Open standard connecting models/agents to tools & data sources. |
| **Training vs inference** | Build-time learning vs run-time serving. |
| **Model registry / feature store / vector DB / AI gateway** | Model catalog / ML-feature store / embedding store for RAG / control-plane proxy. |
| **MLOps / LLMOps** | Ops for classic ML / ops extended for LLMs (prompts, evals, guardrails, gateway). |
| **NIST AI RMF** | Govern, Map, Measure, Manage. |
| **OWASP LLM Top 10 (2025)** | LLM01–LLM10 (see table in 1.4). |
| **MITRE ATLAS** | Adversarial-ML knowledge base (AML.T#### techniques). |
| **ISO/IEC 42001** | AI management system (AIMS) — governance. |
| **Google SAIF** | Secure AI Framework — secure-by-design. |
| **Shared responsibility (AI)** | Risk split across provider / platform / app / user; shifts with SaaS vs self-hosted. |

---

## Check yourself

1. **Q: A bank wants its chatbot to answer using *today's* internal policy documents, with per-user access control, without retraining. RAG or fine-tuning — and why?**
   **A:** **RAG.** It retrieves current documents at query time (fresh, updatable) and lets you enforce **document-level authorization**; fine-tuning bakes in frozen data and cannot do per-user access control.

2. **Q: Name the four core functions of the NIST AI RMF. Which well-known set is the classic distractor?**
   **A:** **Govern, Map, Measure, Manage.** The trap is **Identify, Protect, Detect, Respond, Recover** — that's the **NIST Cybersecurity Framework (CSF)**, not the AI RMF.

3. **Q: An attacker hides instructions inside a web page that a RAG system later retrieves, causing the agent to exfiltrate data. Which OWASP LLM Top 10 (2025) item, and whose responsibility in the shared model?**
   **A:** **LLM01 Prompt Injection** (specifically *indirect* prompt injection). It's primarily the **application/deployer's** responsibility (guardrails, treating retrieved content as untrusted, tool/authZ scoping) — not the model provider's.

4. **Q: Is poisoning a training-time or inference-time attack? Is prompt injection?**
   **A:** **Poisoning = training-time** (integrity of data/model). **Prompt injection = inference-time** (run-time input).

5. **Q: What does MITRE ATLAS provide, and how is it different from ISO/IEC 42001?**
   **A:** **ATLAS** is an **adversarial-ML knowledge base** (ATT&CK-style tactics/techniques, AML.T#### IDs) describing *how AI systems are attacked*. **ISO/IEC 42001** is a certifiable **AI management-system (governance)** standard for *how to govern AI responsibly* — different layer entirely (technique catalog vs governance standard).

6. **Q: Your team migrates from a hosted SaaS LLM API to a self-hosted open-weights model. Which responsibilities newly land on you, and which were yours all along?**
   **A:** **Newly yours:** serving infrastructure hardening/patching, GPU/host security, **model weights integrity & provenance**, and base safety/alignment (you may need to add guardrails). **Yours all along (both models):** prompt design, RAG/agent/tool configuration, **output handling**, authorization, and what data you send to the model.

---

## Cross-references

- **Domain 2 — AI Threats, Attacks & Vulnerabilities:** [`domain-2-threats-attacks.md`](domain-2-threats-attacks.md) — the attacks named here in depth (poisoning, prompt injection, extraction, agentic abuse).
- **Domain 3 — Securing the AI/ML Lifecycle:** [`domain-3-securing-lifecycle.md`](domain-3-securing-lifecycle.md) — the controls (AI gateway, guardrails, RAG authZ, signing).
- **Domain 4 — AI Governance, Risk & Compliance:** [`domain-4-governance-risk-compliance.md`](domain-4-governance-risk-compliance.md) — NIST AI RMF, ISO 42001, EU AI Act, fairness/XAI.
- **Domain 5 — AI Security Operations & Incident Response:** [`domain-5-secops-incident-response.md`](domain-5-secops-incident-response.md) — monitoring, detection, IR, resilience.
- **Frameworks crosswalk:** [`frameworks-crosswalk.md`](frameworks-crosswalk.md) · **Glossary:** [`glossary.md`](glossary.md) · **Acronyms:** [`acronyms.md`](acronyms.md)
- **Practice tests:** [`../practice-tests/`](../practice-tests/) — Domain 1 ≈ 14 questions per 90-question test.
- **Blueprint:** [`../exam-objectives.md`](../exam-objectives.md)
