# Attacks Quick Reference — AI/LLM Attack Cheat Sheet

> ⚠️ **UNOFFICIAL / COMMUNITY-MAINTAINED** study aid — not affiliated with or endorsed by CompTIA or any standards body. OWASP LLM IDs use the **2025** list; ATLAS is referenced by tactic **name**, never by invented `AML.T####` IDs. Verify against primary sources before exam day. Blueprint: [`../exam-objectives.md`](../exam-objectives.md).

**Lifecycle stages:** `data` (collection/curation) · `train` (training/fine-tuning) · `deploy` (build/serve/supply chain) · `inference` (runtime prompts & outputs).

---

## AI/LLM attacks at a glance

| Attack | One-line definition | Lifecycle stage hit | OWASP LLM 2025 | Primary defense |
|---|---|---|---|---|
| **Direct prompt injection** | Attacker-controlled prompt overrides the app's intended instructions. | inference | **LLM01** | Instruction/data separation; input filtering & guardrails; least-privilege tools. |
| **Indirect prompt injection** | Malicious instructions ride in content the model ingests (web page, doc, email, tool output). | inference (via data) | **LLM01** (+ **LLM08** if RAG-borne) | Treat retrieved/external content as untrusted; sanitize; sandbox tools; HITL for high-impact actions. |
| **Jailbreak** | Crafted prompt bypasses safety/guardrail alignment to elicit disallowed output. | inference | **LLM01** | Layered guardrails, jailbreak detection/classifiers, refusal training, red-teaming. |
| **Evasion / adversarial example** | Perturbed input fools a trained model into misclassifying at inference. | inference | *(ML01; LLM09-adjacent)* | Adversarial training, input preprocessing/detection, robustness testing. |
| **Data poisoning** | Tainted training/fine-tuning/RAG data degrades integrity, injects bias. | data, train | **LLM04** | Provenance/lineage, data validation & anomaly detection, trusted pipelines. |
| **Backdoor / trojan** | Hidden trigger makes the model misbehave only on attacker-chosen inputs. | data, train | **LLM04** | Trigger/red-team testing, provenance, model integrity checks, retrain from trusted data. |
| **Model inversion** | Reconstruct sensitive **training inputs** from model behavior/outputs. | inference | *(ML03; LLM02-adjacent)* | Limit confidence detail, differential privacy, output/rate limits, access control. |
| **Model extraction / stealing** | Query the model to clone its parameters/behavior (steal IP). | inference | *(ML05; no direct LLM ID)* | Rate limiting, query/anomaly monitoring, watermarking, output throttling. |
| **Membership inference** | Determine whether a specific record was in the training set. | inference | *(ML04; LLM02-adjacent)* | Differential privacy, regularization, restrict confidence outputs. |
| **System prompt leakage** | System prompt (may hold secrets/guardrail logic) is exposed, aiding bypass. | inference | **LLM07** | No secrets in prompts; enforce controls server-side; assume prompt is extractable. |
| **Improper / insecure output handling** | Downstream system trusts model output → XSS, SQLi, SSRF, RCE. | inference | **LLM05** | Treat output as untrusted; context-aware encode/escape; parameterized queries; sandbox executed output. |
| **Excessive agency** | Over-permissioned/autonomous agent takes harmful actions beyond intent. | deploy, inference | **LLM06** | Least privilege & tool allow-listing, minimize functionality, scoped per-agent identity, human approval gates. |
| **Unbounded consumption** | Uncontrolled resource use — model DoS, "denial of wallet," cost harvesting. | inference | **LLM10** | Rate limits & quotas, input/output size caps, cost monitoring/alerting, timeouts, autoscaling guards. |
| **Sensitive information disclosure** | Model reveals PII, secrets, or proprietary data via output/memorization. | data, inference | **LLM02** | Data minimization/sanitization, output redaction (DLP), retrieval access controls. |
| **Supply-chain / model poisoning** | Compromise via poisoned/tampered/typosquatted models, datasets, plugins, deps. | deploy | **LLM03** (+ **LLM04**) | Vet sources, verify provenance & signatures, MLBOM/SBOM, model & dependency scanning. |
| **Unsafe deserialization (pickle)** | Loading a malicious serialized model executes attacker code (RCE). | deploy | **LLM03** | Prefer safe formats (safetensors); scan artifacts; never load untrusted pickles; sandbox loading. |
| **RAG indirect injection / broken doc-level authz** | Poisoned index content injects instructions, or retrieval crosses authorization/tenant boundaries. | data, inference | **LLM08** (+ **LLM01**) | Per-document/tenant retrieval authz, vet & monitor indexed content, secure the vector DB. |
| **Embedding inversion** | Reconstruct original text/PII from stored embedding vectors. | inference | **LLM08** | Access-control & encrypt embeddings, minimize sensitive data indexed, monitor vector DB access. |

---

## By attacker goal (CIA + safety lens)

| Goal | Attacks that serve it |
|---|---|
| **Confidentiality** (steal data/model) | Model inversion, membership inference, model extraction/stealing, embedding inversion, sensitive info disclosure, system prompt leakage. |
| **Integrity** (corrupt behavior/output) | Data poisoning, backdoor/trojan, supply-chain/model poisoning, evasion/adversarial example, prompt injection (direct & indirect), jailbreak. |
| **Availability** (deny/exhaust service) | Unbounded consumption (model DoS / denial of wallet / cost harvesting). |
| **Safety / abuse of action** | Excessive agency, improper output handling, RAG indirect injection, unsafe deserialization (RCE). |

---

## Triage cheats & traps

- **LLM app (chatbot/RAG/agent)?** → reach for OWASP **LLM** Top 10 first. **Classical trained model (classifier/CV)?** → OWASP **ML** Top 10.
- **Model extraction** and standalone **bias** have **no dedicated OWASP LLM ID** — don't force one (extraction ≈ ML05).
- **System prompts are not a security boundary** — that's exactly why **LLM07** exists; never store secrets there.
- **Pickle ≠ safe.** Unsafe deserialization is RCE on model load — prefer **safetensors**.
- Output handling (**LLM05**) is about what happens **downstream** of the model; injection (**LLM01**) is about what reaches the model.

---

## Easy-to-confuse pairs

| Pair / set | Key distinction |
|---|---|
| **Model inversion** vs **membership inference** vs **model extraction** | Inversion → reconstruct the **training data content**. Membership inference → only **was record X in the training set?** (yes/no). Extraction → clone the **model itself** (params/behavior), not the data. |
| **Direct** vs **indirect** prompt injection | Direct → attacker types the malicious prompt themselves. Indirect → payload hides in **third-party content** (web/doc/email/tool output) the model later reads. Both = **LLM01**. |
| **Data poisoning** vs **evasion (adversarial example)** | Poisoning corrupts the model at **train time** (persistent). Evasion fools an already-trained model at **inference time** (per-input, no model change). |
| **Backdoor/trojan** vs **(plain) data poisoning** | Backdoor = poisoning with a **specific hidden trigger** for targeted misbehavior; otherwise behaves normally. Plain poisoning aims at **general** degradation/bias. |
| **System prompt leakage (LLM07)** vs **sensitive info disclosure (LLM02)** | LLM07 = the **system/instruction prompt** itself leaks. LLM02 = **user/PII/secret/proprietary data** leaks via output or memorization. |
| **Model card** vs **system card** vs **datasheet** | Model card → documents one **model** (intended use, metrics, limits). System card → the **end-to-end system/product** and its safety evaluations. Datasheet → documents a **dataset** (provenance, composition, collection, bias). |

---

*Reconcile against the official CompTIA SecAI+ objectives and primary framework sources before exam day. See also [`frameworks-quick-reference.md`](frameworks-quick-reference.md) and [`../study-guide/frameworks-crosswalk.md`](../study-guide/frameworks-crosswalk.md).*
