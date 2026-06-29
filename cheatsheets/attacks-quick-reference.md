# Attacks Quick Reference — AI/LLM Attack Cheat Sheet

> Unofficial study material aligned to CompTIA SecAI+ CY0-001 V1 objectives. See [../exam-objectives.md](../exam-objectives.md).

Covers every attack named in **objective 2.6**. The **Compensating control(s)** column draws only from the official 2.6 list:
**Prompt firewalls · Model guardrails · Access controls · Data integrity controls · Encryption · Prompt templates · Rate limiting · Least privilege.**

---

## 2.6 Attacks at a glance

| Attack | One-line definition | Tell-tale evidence | Compensating control(s) |
|---|---|---|---|
| **Backdoor attack** | Hidden trigger planted in a model that forces a chosen output when the trigger appears. | Specific rare input/phrase reliably flips the prediction; normal inputs behave fine. | Data integrity controls; model guardrails; access controls (training pipeline) |
| **Trojan attack** | Malicious logic smuggled into a model/artifact/dependency that activates on a condition. | Tampered weights or pickle/checkpoint; unexpected behavior tied to a hidden condition. | Data integrity controls (signing/hashing); access controls; least privilege |
| **Prompt injection (direct)** | User-supplied prompt overrides the app's intended system instructions. | "Ignore previous instructions" style input; output defies the system prompt. | Prompt firewalls; prompt templates; model guardrails |
| **Prompt injection (indirect)** | Malicious instructions hidden in external/retrieved content the model ingests. | Hostile text inside a web page, doc, email, or tool output drives the model's actions. | Prompt firewalls; model guardrails; least privilege (tools/integrations) |
| **Model poisoning** | Tampering with the model itself (weights/params/process) to corrupt behavior. | Behavior shift after a training/fine-tune run; integrity check on weights fails. | Data integrity controls; access controls; least privilege |
| **Data poisoning** | Corrupting the training/RAG **data** so the model learns attacker-desired behavior. | Mislabeled/injected samples in the corpus; provenance/lineage gaps. | Data integrity controls; access controls (data stores); encryption |
| **Jailbreaking** | Crafted prompt bypasses safety alignment to elicit disallowed output. | Refusals defeated by role-play/encoding tricks; policy-violating responses. | Model guardrails; prompt firewalls; prompt templates |
| **Input manipulation** | Adversarially perturbed input that causes misclassification/wrong output. | Tiny, often imperceptible input changes flip the result. | Model guardrails; prompt firewalls; data integrity controls |
| **Introducing biases** | Deliberately skewing data/feedback so outputs become unfair or slanted. | Skewed outcomes across groups; biased feedback/training contributions. | Data integrity controls; access controls; model guardrails |
| **Circumventing AI guardrails** | Evading the safety/policy filters layered around the model. | Guardrail logs show bypass patterns; disallowed output slips through. | Model guardrails (layered); prompt firewalls; rate limiting |
| **Manipulating application integrations** | Abusing connected tools/plug-ins/APIs/agents to act beyond intent. | Unexpected tool/API calls; actions outside the requested task. | Least privilege; access controls; model guardrails |
| **Model inversion** | Reconstructing sensitive **training inputs** by probing model outputs. | Many crafted queries reproduce attributes/records resembling training data. | Access controls; rate limiting; encryption (data protection) |
| **Model theft** | Stealing the model (weights) or cloning it via systematic querying. | Bulk/automated querying to replicate behavior; exfiltration of weights. | Access controls; rate limiting; encryption |
| **AI supply chain attacks** | Compromise via third-party models, datasets, libraries, or pipelines. | Malicious pretrained model/dataset/dependency from an untrusted source. | Data integrity controls; access controls; least privilege |
| **Transfer learning attack** | Malicious behavior baked into a pretrained base survives fine-tuning. | Inherited backdoor/bias traced to the upstream base model. | Data integrity controls; access controls; model guardrails |
| **Model skewing** | Feedback/online-learning loop nudged over time to drift the model. | Gradual drift in outputs correlated with attacker feedback/inputs. | Data integrity controls; rate limiting; access controls |
| **Output integrity attacks** | Tampering with model output in transit/processing before it reaches the user/app. | Response differs from what the model produced; integrity/MAC mismatch. | Encryption; data integrity controls; access controls |
| **Membership inference** | Determining whether a specific record was in the training set. | Confidence/output gap between member vs non-member probe queries. | Access controls; rate limiting; data integrity controls |
| **Insecure output handling** | Downstream app trusts model output unsafely (XSS, SQLi, command exec). | Model output reaches `eval`/SQL/shell/HTML sink unsanitized. | Model guardrails; least privilege; prompt templates |
| **Model denial of service (DoS)** | Resource-exhausting prompts/requests degrade or down the service. | Spikes in tokens/cost/latency; oversized or recursive prompts. | Rate limiting; access controls; model guardrails (input quotas) |
| **Sensitive information disclosure** | Model reveals secrets/PII/proprietary data in its output. | Output contains training secrets, PII, system prompt, or credentials. | Access controls; encryption; model guardrails |
| **Insecure plug-in design** | Plug-in accepts unsafe input/lacks validation, expanding attack surface. | Plug-in takes free-form params, over-broad scopes, no input validation. | Least privilege; access controls; model guardrails |
| **Excessive agency** | Model/agent granted too much functionality, permission, or autonomy. | Agent can take high-impact actions without scoping or approval. | Least privilege; access controls; model guardrails (HITL) |
| **Overreliance** | Humans trust model output without verification, acting on errors/hallucinations. | Decisions made on unverified output; no human validation step. | Model guardrails; access controls; (process) human oversight |

---

## Easy-to-confuse pairs

| Concept | What it targets / does | Quick discriminator |
|---|---|---|
| **Model inversion** | Reconstructs **training input data** from outputs. | "Rebuild the *data* that went in." |
| **Membership inference** | Tells if **one record was in** the training set. | "Was *this specific record* used?" (yes/no, not reconstruction) |
| **Model theft** | Steals/clones the **model itself**. | "Take the *model*, not the data." |
| | | |
| **Data poisoning** | Corrupts the **training/RAG data**. | Attack on the **inputs/dataset**. |
| **Model poisoning** | Tampers with the **model weights/process**. | Attack on the **model artifact** directly. |
| | | |
| **Poisoning (data/model)** | One-time corruption of data or model. | Deliberate tamper, often pre-deployment. |
| **Model skewing** | Gradual drift via **feedback/online learning**. | Slow nudge over time through the feedback loop. |
| **Transfer learning attack** | Malice inherited from an **upstream pretrained base**. | Problem rides in from the **base model**, survives fine-tuning. |
| | | |
| **Excessive agency** | Model/agent **has too much power/permission**. | A *capability/permission* problem (the AI can do too much). |
| **Overreliance** | **Humans over-trust** model output. | A *human-process* problem (people don't verify). |
| | | |
| **Insecure output handling** | Downstream app **fails to sanitize** model output (XSS/SQLi/RCE). | Defect is in how the *app consumes* output. |
| **Sensitive information disclosure** | Model **emits secrets/PII** in its output. | Defect is in *what the model reveals*. |

---

**Study tip:** map each attack to the smallest official control that stops it — most 2.6 scenario items hinge on choosing the *right* compensating control, not just naming the attack. Reconstruct = inversion; yes/no membership = inference; steal model = theft. Data vs model poisoning = inputs vs artifact. Capability = agency; trust = overreliance.
