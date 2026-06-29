# CompTIA SecAI+ (CY0-001) — Practice Test 1 — Answer Key & Explanations (Unofficial)

> ⚠️ **UNOFFICIAL & COMMUNITY-MAINTAINED.** Aligned to **CY0-001 V1**; **no official or actual exam questions** are reproduced. Not affiliated with or endorsed by CompTIA. Verify against the current official objectives: [`../exam-objectives.md`](../exam-objectives.md). Questions: [`practice-test-1.md`](practice-test-1.md).

---

## Answer key

| Q | A | Q | A | Q | A | Q | A | Q | A | Q | A |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | B | 11 | D | 21 | B | 31 | D | 41 | B | 51 | D |
| 2 | C | 12 | A | 22 | C | 32 | B | 42 | A | 52 | A |
| 3 | A | 13 | B | 23 | D | 33 | B | 43 | C | 53 | A |
| 4 | A | 14 | C | 24 | A | 34 | A | 44 | D | 54 | B |
| 5 | B | 15 | C | 25 | C | 35 | D | 45 | B | 55 | C |
| 6 | D | 16 | D | 26 | C | 36 | A | 46 | C | 56 | A |
| 7 | D | 17 | B | 27 | D | 37 | C | 47 | D | 57 | D |
| 8 | C | 18 | A | 28 | A | 38 | B | 48 | B | 58 | C |
| 9 | A | 19 | D | 29 | C | 39 | C | 49 | C | 59 | D |
| 10 | B | 20 | A | 30 | B | 40 | D | 50 | A | 60 | B |

**Distribution:** A=15, B=15, C=15, D=15. Domain mix: D1=10, D2=24, D3=14, D4=12.

---

## Explanations

**1.** Correct: **B** — [1.3] Security is a life-cycle property; poisoned/untrustworthy data and misaligned objectives enter at the use-case and data-collection stages and are expensive to fix later. **A** is wrong because inference-time controls mitigate but never fully compensate for upstream flaws. **C** is false—every phase carries obligations. **D** is false—evaluation and monitoring remain essential.

**2.** Correct: **C** — [2.6] Malicious instructions hidden in *content the model later processes* (a vendor email) is **indirect** prompt injection (OWASP LLM01). Membership inference (**A**) probes training-set membership; poisoning (**B**) corrupts training data; model inversion (**D**) reconstructs training inputs—none match exfiltration triggered by embedded text.

**3.** Correct: **A** — [3.1] A CLI plug-in backed by an MCP server gives a local, tool-calling model a standardized interface to invoke pentest tools. A browser plug-in (**B**) summarizes pages; signature AV (**C**) and a spreadsheet macro (**D**) cannot orchestrate exploitation steps.

**4.** Correct: **A** — [2.2] Model-layer guardrails—constrained system-prompt templates plus output filtering—keep the bot on-policy. Network segmentation (**B**) and at-rest encryption (**C**) are valid controls but don't shape model behavior; enlarging the context window (**D**) does nothing for safety.

**5.** Correct: **B** — [4.3] Employment/recruitment decision systems are **high-risk** under the EU AI Act, triggering risk management, conformity assessment, and human oversight. It is neither minimal/limited-risk (**A**, **D**) nor prohibited (**C**)—prohibited uses include things like social scoring.

**6.** Correct: **D** — [1.1] Learning a mapping from **labeled** inputs to known outputs is **supervised** learning. Reinforcement (**A**) learns from reward signals; unsupervised (**B**) needs no labels; federated (**C**) describes *where* training happens, not labeling.

**7.** Correct: **D** — [2.6] Querying a model to clone it is **model theft/extraction**; rate limiting and query/endpoint access controls most directly curb it. Data poisoning (**A**), membership inference (**B**), and model inversion (**C**) are different attacks with different aims.

**8.** Correct: **C** — [2.1] **MITRE ATLAS** is the AI/ML-specific adversary TTP knowledge base. ASVS (**A**), CIS Controls (**B**), and the API Top 10 (**D**) are general security resources, not AI-adversary taxonomies.

**9.** Correct: **A** — [3.2] An AI-cloned voice used to deceive staff is **deepfake-enabled impersonation** for social engineering. DDoS (**B**), SQLi (**C**), and XSS (**D**) are unrelated technical attack classes.

**10.** Correct: **B** — [4.2] Staff pasting confidential data into an unsanctioned public tool is **accidental data leakage via shadow AI**. Model skewing (**A**), reputational loss from bias (**C**), and IP infringement in images (**D**) are different risks.

**11.** Correct: **D** — [2.4] Computing over data on an untrusted host without exposing plaintext requires **encryption in use** (confidential computing/homomorphic approaches). In transit (**A**) and at rest (**B**) leave plaintext exposed during processing; RBAC (**C**) is access control, not cryptographic protection of the compute.

**12.** Correct: **A** — [1.2] RAG stores text as **embeddings in a vector database** retrieved by similarity. Timestamped logs (**B**), relational keys (**C**), and exact-hash matching (**D**) don't capture semantic similarity.

**13.** Correct: **B** — [2.3] Enforce **least-privilege, role-based data-access** so each identity reaches only authorized sources. Shared accounts (**A**) destroy accountability; guardrails alone (**C**) aren't an access control; broad read access (**D**) defeats segmentation despite encryption.

**14.** Correct: **C** — [3.3] An AI agent embedded in IR/ticketing that auto-handles low severity but escalates high severity to a human implements human-in-the-loop automation. Disabling alerts (**A**), full autonomy (**B**), and a nightly report (**D**) don't meet the requirement.

**15.** Correct: **C** — [2.6] Slowly feeding crafted feedback to bend an online-learning model's decision boundary is **model skewing via data poisoning**. Prompt injection (**A**), inversion (**B**), and insecure output handling (**D**) don't fit the evidence.

**16.** Correct: **D** — [4.1] A central body setting standards, sharing patterns, and vetting tools is an **AI Center of Excellence**. A bug bounty (**A**), SOC (**B**), and CAB (**C**) serve other functions.

**17.** Correct: **B** — [2.5] **Response confidence-level monitoring** flags low-confidence, likely-hallucinated outputs. CPU/storage/port metrics (**A**, **C**, **D**) say nothing about answer reliability.

**18.** Correct: **A** — [1.3] A required human review/override of every adverse decision is **human-in-the-loop oversight**. The others (**B**, **C**, **D**) are unrelated ML/data concepts.

**19.** Correct: **D** — [2.2] A **prompt firewall** inspects and blocks injection/jailbreak prompts at the gateway before they reach the model. Raising temperature (**A**), encrypting logs (**B**), and adding GPUs (**C**) don't screen prompts.

**20.** Correct: **A** — [3.1] In-editor, real-time insecure-pattern detection and fixes is an **IDE plug-in** doing AI-assisted analysis/linting. An IDS (**B**), SIEM rule (**C**), and disk-encryption agent (**D**) don't operate in the editor.

**21.** Correct: **B** — [4.3] The **NIST AI RMF** is the voluntary, function-based (Govern, Map, Measure, Manage) framework for AI risk. PCI DSS (**A**) is payment-card scope; the EU AI Act (**C**) is binding law, not a voluntary RMF; ISO/IEC 27001 (**D**) is an ISMS standard.

**22.** Correct: **C** — [2.6] Leaking the system prompt and an embedded key maps to **LLM07 System Prompt Leakage** and **LLM02 Sensitive Information Disclosure** (2025 list). Excessive Agency (**A**), Poisoning (**B**), and Supply Chain (**D**) describe different risks.

**23.** Correct: **D** — [1.1] Grouping similar **unlabeled** events is **unsupervised** learning (clustering). Supervised (**A**) and RLHF (**B**) need labels/rewards; federated (**C**) describes distributed training, not the labeling paradigm.

**24.** Correct: **A** — [2.1] The **MIT AI Risk Repository** is a continually updated, peer-reviewed taxonomy organized by cause, domain, and life-cycle stage. A single product's CVEs (**B**), the web Top 10 (**C**), and a vendor whitepaper (**D**) aren't comprehensive AI-risk taxonomies.

**25.** Correct: **C** — [3.2] Auto-scanning footprints and correlating breach data to craft phishing is **AI-automated reconnaissance and data correlation**. Watermarking (**A**), federated learning (**B**), and differential privacy (**D**) are defensive/unrelated.

**26.** Correct: **C** — [2.4] **Data anonymization** (with identifier minimization) preserves aggregate utility while preventing re-identification. Replication (**A**), Base64 (**B**), and compression (**D**) provide no privacy.

**27.** Correct: **D** — [4.2] Same decisions for similar inputs = **consistency**; explaining the driving factors = **explainability**. The other pairs (**A**, **B**, **C**) are performance or ML-technique terms, not responsible-AI principles.

**28.** Correct: **A** — [2.3] Scope the agent's identity to **least privilege**—only the tools/records each task needs—so a hijack via injection has minimal blast radius. Longer tokens (**B**), shared admin keys (**C**), and disabled logging (**D**) increase risk.

**29.** Correct: **C** — [3.3] Code scanning, SCA, and model tests that gate every commit belong **in the CI/CD pipeline**. A quarterly review (**A**), the system prompt (**B**), and user docs (**D**) can't gate merges.

**30.** Correct: **B** — [3.3] A **low-code/no-code automation platform** lets analysts build workflows without full coding. Assembly (**A**), manual email (**C**), and disabling automation (**D**) miss the requirement.

**31.** Correct: **D** — [1.2] **Data provenance** (origin) and **data lineage** (transformations) provide the audit trail. Quantization/pruning (**A**), embeddings/vector storage (**B**), and prompting styles (**C**) are unrelated.

**32.** Correct: **B** — [2.5] **Log protection** (integrity/immutability + access control) keeps logs tamper-evident, while **log sanitization/redaction** strips secrets users submitted. Open plaintext storage (**A**), immediate deletion (**C**), and encrypting only weights (**D**) fail one or both goals.

**33.** Correct: **B** — [4.1] The **AI security architect** designs secure AI architecture and protective controls. A data engineer (**A**) builds pipelines; an AI auditor (**C**) assesses; an MLOps engineer (**D**) operationalizes models.

**34.** Correct: **A** — [2.2] FIRST **test and validate the guardrails** with adversarial red-team prompts before trusting them. Raising token limits (**B**), publishing the system prompt (**C**), and removing rate limits (**D**) weaken security.

**35.** Correct: **D** — [3.1] Baselining normal behavior and surfacing statistical outliers is **anomaly detection / pattern recognition**. Linting (**A**), translation (**B**), and signature matching (**C**) won't catch novel behavior.

**36.** Correct: **A** — [2.6] Consistent misclassification triggered only by a specific pattern indicates a **backdoor/trojan** with a planted trigger. Membership inference (**B**), DoS (**C**), and info disclosure (**D**) don't match.

**37.** Correct: **C** — [1.3] Confirming continued real-world performance and detecting drift after release is **monitoring and maintenance**. Use-case definition (**A**), data prep (**B**), and model selection (**D**) occur earlier.

**38.** Correct: **B** — [2.1] The **CVE AI Working Group** coordinates identifying, numbering, and disclosing AI-component vulnerabilities. The MIT repository (**A**), ATLAS case studies (**C**), and the ML Top 10 (**D**) serve other purposes.

**39.** Correct: **C** — [4.3] Keeping data and its processing within national borders is **data sovereignty**. Differential privacy (**A**), quantization (**B**), and rate limiting (**D**) are unrelated.

**40.** Correct: **D** — [2.4] **Data redaction/masking** of sensitive fields before storage keeps logs useful while removing readable card numbers. Longer retention (**A**), replication (**B**), and compression (**C**) don't protect the data.

**41.** Correct: **B** — [3.2] Generative mutation that changes signatures but preserves behavior is **AI-driven obfuscation / polymorphic payload generation**. Honeypots (**A**), lineage tracking (**C**), and differential privacy (**D**) are defensive/unrelated.

**42.** Correct: **A** — [1.1] Lowering weight precision to shrink and speed a model is **quantization**. RL (**B**), zero-shot prompting (**C**), and data balancing (**D**) are different concepts.

**43.** Correct: **C** — [3.2] A deceptive AI-generated fake service to lure and study attackers is an **AI-generated honeypot**. Adversarial examples (**A**), differential privacy (**B**), and membership inference (**D**) don't describe deception environments.

**44.** Correct: **D** — [1.1] Training across sites that share only parameters, not raw data, is **federated learning**. RL (**A**), supervised fine-tuning (**B**), and transfer learning (**C**) don't describe this decentralized scheme.

**45.** Correct: **B** — [2.5] Tracking spend across prompt, processing, response, and storage is **AI cost monitoring**. SMART (**A**), TLS-expiry (**C**), and badge logs (**D**) don't track AI spend.

**46.** Correct: **C** — [3.3] Pre-screening low-risk changes, recommending approval, and auto-deploy/rollback on failed health checks is **AI-assisted change approvals with automated deployment/rollback**. Paging for every change (**A**), freezing changes (**B**), and disabling health checks (**D**) don't fit.

**47.** Correct: **D** — [4.2] **Shadow AI** is AI tools/services used **without organizational approval, oversight, or governance**. Approved-but-disabled features (**A**), reviewed open-source models (**B**), and data-center cooling load (**C**) are not shadow AI.

**48.** Correct: **B** — [2.2] **Rate limits, token limits, and input quotas** cap per-user volume and request size to blunt model-DoS/abuse at the gateway. Encryption/key rotation (**A**), anonymization/masking (**C**), and federated learning (**D**) don't throttle requests.

**49.** Correct: **C** — [2.3] Restricting which networks/apps can call the inference API uses **network/API access controls** (allowlisting + authenticated endpoints). Context window (**A**), watermarking (**B**), and more epochs (**D**) don't restrict callers.

**50.** Correct: **A** — [3.1] Condensing long multi-document input into a concise brief is **summarization**. Fraud detection (**B**), signature matching (**C**), and pentesting (**D**) are different use cases.

**51.** Correct: **D** — [4.1] Independent evaluation of AI systems for policy/regulatory compliance and control effectiveness is the **AI auditor**. ML engineer (**A**), platform engineer (**B**), and data scientist (**C**) build rather than independently audit.

**52.** Correct: **A** — [1.2] Rotating, cropping, and adding noise to expand a training set is **data augmentation**. Redaction (**B**), quantization (**C**), and watermarking (**D**) serve other ends.

**53.** Correct: **A** — [2.1] FIRST apply a **threat-modeling framework** to map data flows and trust boundaries before coding. Buying GPUs (**B**), raising temperature (**C**), and skipping modeling (**D**) don't enumerate threats.

**54.** Correct: **B** — [3.2] Mass-producing convincing fake articles/posts to sway opinion is **AI-generated disinformation/misinformation at scale**. Membership inference (**A**), model inversion (**C**), and insecure plug-in design (**D**) are unrelated.

**55.** Correct: **C** — [2.4] Sharing only the data strictly necessary is **data minimization**. Augmentation (**A**), balancing (**B**), and provenance (**D**) don't limit disclosure.

**56.** Correct: **A** — [4.3] Sound policy processes sensitive data only with **sanctioned, private models under governance**, not unsanctioned public ones. Popularity (**B**), trust-based exemptions (**C**), and "private = no governance" (**D**) are unsafe.

**57.** Correct: **D** — [2.5] Continuously checking hallucination rate, accuracy drift, and bias/fairness is **auditing for quality and compliance**. Latency (**A**), power usage (**B**), and TCP counts (**C**) don't measure output quality or fairness.

**58.** Correct: **C** — [3.3] Drafting IR ticket updates and synthesizing post-incident summaries is **document synthesis/summarization and IR ticket management**. Signature matching (**A**), adversarial training (**B**), and segmentation (**D**) don't apply.

**59.** Correct: **D** — [4.1] Translating regulatory/ethical requirements into enforceable AI policy and governance is the **AI governance engineer**. Data/platform/MLOps engineers (**A**, **B**, **C**) are build/operate roles.

**60.** Correct: **B** — [4.2] A model that performs unfairly for an underrepresented region exhibits **introduction of bias** affecting fairness and performance. Excessive agency (**A**), insecure output handling (**C**), and model theft (**D**) describe different risks.
