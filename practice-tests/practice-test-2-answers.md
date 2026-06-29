# CompTIA SecAI+ (CY0-001) — Practice Test 2: Answer Key & Explanations (Unofficial / Community)

> ⚠️ **UNOFFICIAL & COMMUNITY-MAINTAINED.** Study aid only — not affiliated with, endorsed by, or sourced from CompTIA. Reconcile against the official CompTIA SecAI+ objectives; where they differ, the official document wins. Questions: [`practice-test-2.md`](practice-test-2.md) · Blueprint: [`../exam-objectives.md`](../exam-objectives.md).

## Answer key (for fast self-scoring)

| Q | A | Q | A | Q | A | Q | A |
|---|---|---|---|---|---|---|---|
| 1 | A | 16 | A | 31 | A | 46 | B |
| 2 | C | 17 | B | 32 | B | 47 | D |
| 3 | D | 18 | D | 33 | D | 48 | A |
| 4 | B | 19 | C | 34 | C | 49 | C |
| 5 | A | 20 | C | 35 | A | 50 | C |
| 6 | B | 21 | A | 36 | D | 51 | B |
| 7 | D | 22 | C | 37 | B | 52 | A |
| 8 | C | 23 | B | 38 | D | 53 | B |
| 9 | A | 24 | A | 39 | D | 54 | C |
| 10 | B | 25 | D | 40 | A | 55 | A |
| 11 | D | 26 | B | 41 | B | 56 | D |
| 12 | C | 27 | C | 42 | C | 57 | B |
| 13 | B | 28 | A | 43 | C | 58 | D |
| 14 | A | 29 | B | 44 | D | 59 | C |
| 15 | D | 30 | C | 45 | A | 60 | D |

Study heuristic: aim for **~75%+ (≈ 45 of 60)** before sitting the exam. Answer distribution: A×15, B×15, C×15, D×15.

---

## Explanations

**1.** Correct: **A** — [1.1] Two networks trained against each other — a generator versus a discriminator — is the defining structure of a GAN, commonly used to synthesize realistic data for augmentation. Reinforcement learning (B) optimizes actions via rewards; federated learning (C) trains across distributed data without centralizing it; linear regression (D) is a single supervised estimator, not an adversarial pair.

**2.** Correct: **C** — [2.1] The MIT AI Risk Repository is a public, regularly updated database of 1,000+ AI risks distilled from existing frameworks and literature, organized by causal and domain taxonomies — exactly a seed for an enterprise risk assessment. OWASP LLM Top 10 (A) is a focused list of LLM app risks; ATLAS (B) is an adversary TTP knowledge base; the CVE AI Working Group (D) standardizes vulnerability identifiers.

**3.** Correct: **D** — [1.3] Requiring a person to review and approve each AI output before it acts is the textbook definition of human-in-the-loop. Data lineage (A) tracks data flow; federated learning (B) and quantization (C) are training/optimization techniques, not oversight controls.

**4.** Correct: **B** — [2.2] Model guardrails that enforce and validate a structured output schema (rejecting/regenerating malformed responses) directly constrain output format and reduce insecure output handling. Rate limiting (A) controls volume, not structure; encryption at rest (C) protects stored data; network segmentation (D) isolates hosts — none enforce schema conformance.

**5.** Correct: **A** — [3.1] A Model Context Protocol (MCP) server exposes external tools/data to an LLM through a standardized interface so the model can call them. A vector database (B) stores embeddings; a GAN (C) generates data; a reverse proxy (D) routes HTTP traffic but is not a model tool-access standard.

**6.** Correct: **B** — [4.1] A centralized, cross-functional body that sets standards, shares best practices, and steers responsible adoption is an AI Center of Excellence. A SOC (A) handles security operations; a change advisory board (C) reviews IT changes; a DLP team (D) focuses on data-loss prevention.

**7.** Correct: **D** — [2.3] Scoping the agent's tool to least-privilege, per-user credentials ties each data access back to the requesting user's authorization, enforcing the boundary technically. A shared admin account (A) violates least privilege; prompt instructions (B) are not an enforcement control; in-transit encryption (C) protects confidentiality, not authorization scope.

**8.** Correct: **C** — [1.2] Documenting the origin, ownership, and chain of custody of data is data provenance, which supports lawful-sourcing claims. Augmentation (A) creates synthetic variants; balancing (B) adjusts class proportions; masking (D) obscures sensitive values.

**9.** Correct: **A** — [2.4] Encryption in use — via confidential computing/trusted execution environments — keeps data protected while it is processed, so plaintext never appears in host memory. TLS (B) covers data in transit; AES-256 disk encryption (C) covers data at rest; hashing (D) is one-way and unusable for inference over the original values.

**10.** Correct: **B** — [3.2] Cloning a real person's voice with generative AI to impersonate them in a fraudulent call is a deepfake (voice) impersonation attack. SQL injection (A) targets databases; membership inference (C) and model theft (D) are attacks against ML models, not social-engineering voice fraud.

**11.** Correct: **D** — [4.2] Employees using unsanctioned AI tools outside IT governance is Shadow AI (a form of shadow IT), creating data-leak and compliance exposure. Model inversion (A), data poisoning (B), and differential-privacy loss (C) describe technical attacks/properties, not unsanctioned-tool usage.

**12.** Correct: **C** — [2.5] AI cost and token-usage monitoring tracks consumption per prompt/response/processing and surfaces the spend anomaly driving the bill. Hallucination (A) and bias/fairness (B) auditing assess output quality, not cost; log sanitization (D) redacts sensitive log data.

**13.** Correct: **B** — [2.6] Corrupting the training set with mislabeled samples to degrade behavior on a target class is data poisoning. Model inversion (A) reconstructs training data; prompt injection (C) manipulates inference-time input; membership inference (D) tests whether a record was in the training set.

**14.** Correct: **A** — [1.1] Providing several labeled examples before the real input is multi-shot (few-shot) prompting. Zero-shot (B) gives no examples; system-role assignment (C) sets the model's persona; "chain-of-custody prompting" (D) is not a prompting technique.

**15.** Correct: **D** — [3.3] Automatically checking dependencies for known vulnerabilities is software composition analysis (SCA). Unit (A) and regression (B) testing validate behavior; linting (C) checks style/quality — none specifically inventory third-party components for CVEs.

**16.** Correct: **A** — [4.3] The NIST AI RMF core functions are Govern, Map, Measure, and Manage. "Identify/Protect/Detect/Respond" (B) is the NIST CSF; PDCA (C) is a quality cycle; "Categorize/Select/Implement/Assess" (D) borrows from the NIST RMF (SP 800-37), not the AI RMF.

**17.** Correct: **B** — [2.1] Attacker-controlled content overriding system instructions is LLM01:2025 Prompt Injection in the OWASP Top 10 for LLM Applications (2025). Sensitive Information Disclosure (A, LLM02) covers leaking secrets; Data and Model Poisoning (C, LLM04) targets training; Excessive Agency (D, LLM06) is over-permissioned actions — though injection may trigger them, the override itself is prompt injection.

**18.** Correct: **D** — [2.2] Per-key rate limits and token quotas cap request volume and size, directly mitigating model denial-of-service from request floods. Output-schema validation (A) governs format; data anonymization (B) and model watermarking (C) do not throttle abusive traffic.

**19.** Correct: **C** — [1.2] Embedding an imperceptible, detectable marker to prove machine origin is watermarking. Masking (A) hides sensitive values; tokenization (B) substitutes surrogate values; quantization (D) reduces model precision.

**20.** Correct: **C** — [3.1] Baselining normal behavior and flagging statistically rare deviations without signatures is anomaly detection. Signature matching (A) relies on known patterns; code linting (B) checks source quality; translation (D) converts languages.

**21.** Correct: **A** — [2.3] Issuing short-lived, narrowly scoped tokens to each authenticated service is least-privilege, scoped API access. Defense in depth (B) is a broader layering concept; data minimization (C) limits collected data; air-gapping (D) physically isolates systems and is not described here.

**22.** Correct: **C** — [4.1] The MLOps engineer operationalizes models — deployment, monitoring, versioning, retraining, and rollback in production pipelines. An AI auditor (A) reviews compliance; a data scientist (B) builds/experiments with models; an AI risk analyst (D) assesses risk.

**23.** Correct: **B** — [2.4] Detecting and replacing identifiers like SSNs and card numbers before training is PII redaction/masking of the training data. Augmentation (A) expands data; differential privacy (C) adds calibrated noise rather than removing specific fields; encryption at rest (D) protects stored data but would still expose PII to the training process when decrypted.

**24.** Correct: **A** — [1.3] Testing a trained model on a held-out set to measure accuracy, bias, and generalization is the model evaluation stage. Data preparation (B) precedes training; feedback and iteration (C) follows deployment; business use-case definition (D) is the earliest planning stage.

**25.** Correct: **D** — [2.5] Log sanitization redacts secrets/PII before logs are stored, preventing the logs from becoming a leak vector. Longer retention (A) increases exposure; rate monitoring (B) and response-confidence scoring (C) address abuse and output quality, not log content safety.

**26.** Correct: **B** — [3.2] Using AI to fuse disparate sources into target dossiers at scale is AI-driven automated reconnaissance and data correlation. Output-integrity (A), model skewing (C), and transfer-learning (D) attacks target the model itself rather than enhancing recon.

**27.** Correct: **C** — [2.6] Limiting tool permissions to least privilege and gating destructive actions behind human approval directly shrinks the blast radius of excessive agency. Enlarging the context window (A) or adding examples (B) does not constrain authority; encrypting logs (D) protects records but not actions.

**28.** Correct: **A** — [4.2] Differential privacy mathematically bounds any single record's influence on released outputs. Explainability (B) clarifies decisions; federated learning (C) decentralizes training; watermarking (D) marks generated content — none provide that formal privacy guarantee.

**29.** Correct: **B** — [1.1] A small language model (SLM) trades breadth for a smaller footprint and lower latency, making it suitable for on-device, privacy-sensitive use. A cloud LLM (A) needs connectivity and more compute; a GAN (C) generates data; a federated LLM ensemble (D) is heavier, not on-device-friendly.

**30.** Correct: **C** — [2.1] The CVE AI Working Group standardizes publicly disclosed vulnerability identifiers for AI/ML software, which is what "track and reference standardized identifiers" requires. The MIT AI Risk Repository (A) catalogs risks broadly; OWASP ML Top 10 (B) lists threat categories; ATLAS (D) maps adversary TTPs.

**31.** Correct: **A** — [3.3] Visually chaining pre-built actions without writing code describes a low-code/no-code automation (SOAR) platform, ideal for a developer-light SOC. Rewriting the SIEM in assembly (B) is the opposite extreme; manual triage (C) is no automation; a GAN (D) does not automate playbooks.

**32.** Correct: **B** — [2.2] Deliberately probing safety guardrails with adversarial/jailbreak prompts before launch is guardrail testing and validation. Network pen testing (A) targets infrastructure; load testing (C) measures performance; data balancing (D) adjusts datasets.

**33.** Correct: **D** — [2.4] Requiring data to remain stored and processed within a specific jurisdiction is data sovereignty. Differential privacy (A) bounds record influence; third-party attestation (B) is external verification; data minimization (C) limits how much data is collected, not where it resides.

**34.** Correct: **C** — [2.3] Network egress filtering/segmentation lets the model reach the vector store while blocking outbound internet connections, even if compromised. Rate limiting (A) throttles volume; guardrails (B) shape content; output-schema validation (D) governs response format — none restrict network egress.

**35.** Correct: **A** — [1.2] Free-text emails have no predefined schema, making them unstructured data. Structured data (B) is tabular/relational; semi-structured data (C, e.g., JSON logs) carries tags but no rigid schema; "tokenized data" (D) is not a data-type category here.

**36.** Correct: **D** — [2.4] Collecting and retaining only the fields needed for the task is data minimization, which shrinks breach impact. Augmentation (A) and balancing (B) modify datasets; masking (C) obscures values but does not reduce how much is collected.

**37.** Correct: **B** — [3.1] Inline detection of insecure patterns as the developer types is delivered by an IDE plug-in. A browser plug-in (A) operates in the browser; a standalone chatbot (C) is not inline in the editor; an MCP ticketing server (D) connects tools, not in-editor linting.

**38.** Correct: **D** — [2.5] Response confidence-level scoring lets the system flag low-certainty answers for human review instead of presenting them as fact. Rate monitoring (A) and cost monitoring (B) track usage/spend; log protection (C) secures logs — none gauge answer certainty.

**39.** Correct: **D** — [4.1] Governance starts with establishing AI policies and procedures that define acceptable use before broad adoption. Buying GPUs (A), fine-tuning a model (B), or deploying SOAR (C) are implementation steps that should follow, not precede, governance.

**40.** Correct: **A** — [2.6] Using a model's outputs to reconstruct recognizable training-data subjects is model inversion. Membership inference (B) only reveals whether a record was in training; model theft (C) clones functionality; data poisoning (D) corrupts training data.

**41.** Correct: **B** — [3.1] Autonomously enumerating, chaining weaknesses, and proposing exploit paths is AI-assisted automated penetration testing. Linting (A) checks code; translation (C) and summarization (D) are language tasks, not offensive testing.

**42.** Correct: **C** — [2.1] For classical (non-LLM) ML pipelines, the OWASP Machine Learning Security Top 10 is the tailored threat list covering input manipulation, poisoning, and model theft. The LLM Top 10 (A) targets generative apps; ATLAS (B) is a TTP knowledge base; the EU AI Act (D) is regulation, not a threat model.

**43.** Correct: **C** — [3.2] Using AI to automatically rewrite malware each build so signatures never match is AI-generated polymorphic malware (automated obfuscation). Deepfake disinformation (A) is content manipulation; membership inference (B) and model inversion (D) are model attacks, not malware generation.

**44.** Correct: **D** — [2.2] A maximum file size is an input size quota and a PNG/JPEG-only rule is a modality (file-type) limit — both are gateway input controls. Output watermarking (A) marks responses; differential privacy (B) protects data; prompt templates (C) shape model behavior, not upload constraints.

**45.** Correct: **A** — [4.2] Treating AI output as authoritative without human verification, leading to harm, is overreliance. Data sovereignty (B) concerns jurisdiction; membership inference (C) is a privacy attack; model denial of service (D) is an availability attack.

**46.** Correct: **B** — [2.3] Requiring a human approval (authorization gate) before the agent finalizes high-value actions enforces oversight on privileged operations. Encrypting the database (A) protects data, not authorization; rate limiting (C) throttles volume; adding examples (D) does not gate actions.

**47.** Correct: **D** — [3.3] Auto-enriching, categorizing, routing tickets, and drafting initial steps is AI-assisted incident-response ticket management. SCA (A) inspects dependencies; regression testing (B) validates code; deepfake detection (C) analyzes media.

**48.** Correct: **A** — [2.4] Tagging datasets as Public/Internal/Confidential/Restricted to drive handling is data classification labeling. Augmentation (B) expands data; watermarking (C) marks generated content; quantization (D) compresses models.

**49.** Correct: **C** — [1.1] Learning a sequence of actions purely from rewards and penalties, with no labeled dataset, is reinforcement learning. Supervised learning (A) needs labels; unsupervised learning (B) finds structure without rewards; federated learning (D) decentralizes training.

**50.** Correct: **C** — [2.5] Detecting disparate outcomes across demographic groups is bias and fairness auditing. Hallucination auditing (A) checks factual accuracy; cost monitoring (B) tracks spend; rate monitoring (D) tracks request rates.

**51.** Correct: **B** — [4.3] Government social scoring of citizens is an explicitly Prohibited (unacceptable-risk) practice under the EU AI Act. It is not merely High risk (A), and clearly above Limited (C) or Minimal (D) tiers.

**52.** Correct: **A** — [2.6] Harvesting many input/output pairs to train a functionally equivalent clone is model theft (model extraction). Membership inference (B) reveals training membership; model inversion (C) reconstructs data; prompt injection (D) manipulates inference-time behavior.

**53.** Correct: **B** — [3.1] Condensing a long report into a short brief is summarization. Signature matching (A) detects known patterns; fraud detection (C) flags suspicious activity; penetration testing (D) probes for weaknesses.

**54.** Correct: **C** — [3.2] Mass-producing fabricated news to manipulate public opinion is an AI-generated disinformation campaign. Spear-phishing payloads (A) target individuals; adversarial-example evasion (B) fools classifiers; automated vulnerability scanning (D) finds technical flaws.

**55.** Correct: **A** — [1.3] Watching a deployed model for performance decay (drift) and triggering retraining is the monitoring and maintenance lifecycle activity. Use-case definition (B), data collection (C), and model selection (D) all occur earlier in the lifecycle.

**56.** Correct: **D** — [3.2] Using an LLM and a target's personal data to auto-generate tailored phishing at scale is AI-generated spear-phishing (social engineering at scale). Model inversion (A), data poisoning (B), and membership inference (C) are model-targeted attacks, not phishing generation.

**57.** Correct: **B** — [4.1] Assessing, quantifying, tracking, and reporting AI-specific risks (bias, drift, compliance gaps) is the AI risk analyst's focus. A data engineer (A) builds pipelines; a platform engineer (C) maintains infrastructure; a machine-learning engineer (D) builds and ships models.

**58.** Correct: **D** — [4.2] A model trained on raw data that then emits other customers' personal details is accidental data leakage. Model denial of service (A) is availability; excessive agency (B) is over-permissioned actions; data sovereignty (C) concerns jurisdiction of storage/processing.

**59.** Correct: **C** — [3.3] Evaluating deployment risk and automatically reverting on error-rate spikes is automated deployment with AI-driven rollback (AI-assisted change management). SCA (A) inspects dependencies; data anonymization (B) protects data; penetration testing (D) probes for weaknesses.

**60.** Correct: **D** — [4.3] ISO/IEC 42001 is the international standard for an AI management system (AIMS), enabling formal certification of AI governance. ISO/IEC 27001 (A) governs information security; the NIST AI RMF (B) is a voluntary framework, not a certifiable standard; the OECD AI Principles (C) are high-level principles, not a certification standard.
