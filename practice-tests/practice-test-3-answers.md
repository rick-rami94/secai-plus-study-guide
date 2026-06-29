# CompTIA SecAI+ (CY0-001) — Practice Test 3: Answer Key & Explanations (Unofficial)

> ⚠️ **UNOFFICIAL / COMMUNITY-MAINTAINED.** Study aid only — not affiliated with, endorsed by, or sourced from CompTIA. Reconcile against the official CompTIA SecAI+ objectives. Questions: [`practice-test-3.md`](practice-test-3.md) • Blueprint: [`../exam-objectives.md`](../exam-objectives.md).

## Answer key (for fast self-scoring)

| Q | A | Q | A | Q | A | Q | A | Q | A | Q | A |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | A | 11 | C | 21 | A | 31 | C | 41 | D | 51 | D |
| 2 | C | 12 | D | 22 | D | 32 | B | 42 | A | 52 | C |
| 3 | D | 13 | B | 23 | C | 33 | A | 43 | C | 53 | B |
| 4 | A | 14 | C | 24 | B | 34 | C | 44 | A | 54 | A |
| 5 | C | 15 | D | 25 | C | 35 | D | 45 | B | 55 | C |
| 6 | B | 16 | B | 26 | D | 36 | B | 46 | C | 56 | D |
| 7 | D | 17 | C | 27 | B | 37 | C | 47 | D | 57 | B |
| 8 | B | 18 | D | 28 | A | 38 | A | 48 | D | 58 | A |
| 9 | A | 19 | B | 29 | A | 39 | A | 49 | A | 59 | C |
| 10 | B | 20 | A | 30 | D | 40 | B | 50 | B | 60 | D |

Study heuristic: aim for **~75%+ correct (≈ 45 / 60)**. Official passing score is **600 / 900**.

**Domain coverage:** D1 (Basic AI Concepts) = 10 · D2 (Securing AI Systems) = 24 · D3 (AI-assisted Security) = 14 · D4 (AI GRC) = 12.

---

## Explanations

**1.** Correct: **A** — [1.1] Placing a few labeled examples directly in the prompt is few-shot (multi-shot) prompting; weights are unchanged. Fine-tuning (B) and RLHF (C) update weights; federated learning (D) is a distributed training method.

**2.** Correct: **C** — [2.6] A hidden trigger implanted during training that forces attacker-chosen behavior is a backdoor/trojan attack. Inversion (A) reconstructs training data, membership inference (B) tests set membership, and extraction (D) clones the model.

**3.** Correct: **D** — [2.1] MITRE ATLAS is the ATT&CK-style knowledge base of adversary tactics/techniques against AI/ML systems. OWASP LLM Top 10 (A) lists risk categories, the MIT AI Risk Repository (B) catalogs risks, and NIST AI RMF (C) is a governance framework.

**4.** Correct: **A** — [4.3] AI used as a safety component in healthcare (patient triage) is a High-risk system under the EU AI Act. It is regulated, not Prohibited (D), and well above Limited (B) or Minimal (C).

**5.** Correct: **C** — [3.3] Auto-triaging, enriching, routing, and drafting tickets is AI-assisted incident-response ticket management. Penetration testing (A) and deepfakes (B) are unrelated; differential privacy (D) is a privacy technique.

**6.** Correct: **B** — [2.2] A component that inspects and blocks malicious instructions in inbound prompts is a prompt firewall (input guardrail). A model registry (A) versions artifacts, a vector DB (C) stores embeddings, and a token bucket (D) handles rate/billing.

**7.** Correct: **D** — [2.3] On-behalf-of (OBO) delegation carries each user's identity and scope so the agent accesses only that user's permitted data. Shared admin accounts (A), static keys (B), and disabling auth (C) all violate least privilege.

**8.** Correct: **B** — [1.2] Proving which datasets and transformations produced a model is data lineage/provenance. Augmentation (A) and balancing (C) shape datasets; quantization (D) compresses models.

**9.** Correct: **A** — [3.2] Synthesizing the CFO's voice to authorize a transfer is deepfake voice impersonation for social engineering. Membership inference (B), extraction (C), and poisoning (D) are model-targeted attacks, not the vishing technique described.

**10.** Correct: **B** — [4.1] A central body that sets standards, shares best practices, and vets use cases is an AI Center of Excellence. A bug-bounty (A), SOC (C), and CAB (D) serve different functions.

**11.** Correct: **C** — [2.4] Replacing real identifiers with realistic fictitious values is data masking/anonymization. Classification labeling (A) tags sensitivity, encryption (B) protects confidentiality without removing identity, and rate limiting (D) is unrelated.

**12.** Correct: **D** — [2.5] Attributing spend per key and catching abuse is AI cost monitoring (token/prompt/response usage). TLS (A), disk SMART (B), and linting (C) don't track inference spend.

**13.** Correct: **B** — [1.3] Verifying trustworthiness/authenticity of inputs is most critical at data collection, before bad data enters the pipeline. Deployment (A), feedback (C), and use-case definition (D) occur at other phases.

**14.** Correct: **C** — [2.6] Harvesting input/output pairs to clone a model is model extraction (theft); rate limiting and query throttling most directly limit it. The other pairings misidentify either the attack or the control.

**15.** Correct: **D** — [3.2] Using an LLM to mutate malware so every build has a unique signature is automated obfuscation / polymorphic payload generation. Membership inference (A), differential privacy (B), and federated learning (C) are unrelated.

**16.** Correct: **B** — [4.2] Consistent behavior that avoids dangerous failures maps to the Responsible AI principle of reliability and safety. Portability (A), lock-in (C), and throughput (D) are not the safety concern.

**17.** Correct: **C** — [2.2] Capping per-request tokens and per-user request rates is implemented with token limits and rate limits at the gateway. Anonymization (A), signing (B), and embedding encryption (D) address other risks.

**18.** Correct: **D** — [2.5] Detecting fabricated or low-confidence answers is hallucination/accuracy auditing with response-confidence review. GPU temp (A), TLS latency (B), and packet loss (C) are infrastructure metrics.

**19.** Correct: **B** — [2.1] For classical ML risks (evasion, poisoning, inversion), the OWASP Machine Learning Security Top 10 is the right reference. The LLM Top 10 (A) targets LLM apps; PCI DSS (C) and ISO 27001 (D) are not ML-threat catalogs.

**20.** Correct: **A** — [4.2] Giving denied applicants a meaningful reason requires explainability/transparency. Throughput (B), latency (C), and context window (D) don't address interpretability.

**21.** Correct: **A** — [3.1] Inline insecure-pattern flagging in the editor is an IDE security plug-in (AI code assistant). A vector DB (B), model registry (C), and honeypot (D) don't provide inline code review.

**22.** Correct: **D** — [1.1] A generator and a discriminator trained in competition describe a generative adversarial network (GAN). Transformers (A), RL agents (B), and SVMs (C) are different architectures.

**23.** Correct: **C** — [2.3] Restricting which authenticated apps can call the endpoint and what each may do is API/endpoint access control with authn/authz. Output redaction (A), data balancing (B), and watermarking (D) don't gate endpoint access.

**24.** Correct: **B** — [3.2] Scraping and correlating public posts to profile targets is automated reconnaissance and data correlation. Differential privacy (A), watermarking (C), and federated learning (D) are defenses/techniques, not the offensive capability shown.

**25.** Correct: **C** — [2.6] A trigger phrase implanted via malicious training samples is a backdoor/trojan introduced through data poisoning; training-data integrity and provenance validation are the right compensating controls. The other options misclassify the attack or pair an ineffective control.

**26.** Correct: **D** — [4.3] Keeping EU residents' data stored and processed within the EU is data sovereignty/residency. Differential privacy (A), watermarking (B), and federated learning (C) don't define jurisdictional storage requirements.

**27.** Correct: **B** — [2.2] A strict system prompt with embedded rules and a per-request template is a model guardrail via prompt templates/system prompts. A vector index (A), token bucket (C), and lineage tracking (D) serve other purposes.

**28.** Correct: **A** — [2.5] Redacting/tokenizing PII in logs and protecting access (log sanitization) preserves investigative value while limiting exposure. Disabling logging (B), public buckets (C), and logging only post-incident (D) are unsafe or useless.

**29.** Correct: **A** — [1.2] Embeddings are numeric vector representations of text that enable semantic similarity search. They are not encrypted weights (B), a scheduling policy (C), or a prompt template (D).

**30.** Correct: **D** — [3.3] Auto-running scored safety/quality tests against a benchmark and blocking regressions is automated model evals as a release gate. Manual checks (A), thermal throttling (B), and TLS rotation (C) don't gate model quality.

**31.** Correct: **C** — [4.1] Designing and operating controls, policies, and monitoring that keep AI compliant is the AI governance engineer's role. A front-end dev (A), DBA (B), and help-desk tech (D) don't own AI governance.

**32.** Correct: **B** — [2.6] Using confidence outputs to decide whether a specific record was in the training set is membership inference. Inversion (A) reconstructs data, extraction (C) clones the model, and prompt injection (D) manipulates instructions.

**33.** Correct: **A** — [3.2] Mass-producing realistic fake articles and personas to push a false narrative is AI-generated misinformation/disinformation at scale. Membership inference (B), extraction (C), and differential privacy (D) are unrelated.

**34.** Correct: **C** — [2.4] Keeping data encrypted while it is processed in memory is encryption in use via confidential computing / a trusted execution environment. TLS (A) protects transit, AES on disk (B) protects at rest, and watermarking (D) is not encryption.

**35.** Correct: **D** — [1.3] Requiring human approval before an AI decision takes effect is human-in-the-loop oversight. Federated learning (A), zero-shot prompting (B), and augmentation (C) are not oversight controls.

**36.** Correct: **B** — [2.1] A categorized catalog of documented AI risks by cause/domain/subdomain is the MIT AI Risk Repository. The OWASP LLM Top 10 (A) is a focused risk list, while PCI DSS (C) and the EU AI Act (D) are not risk catalogs.

**37.** Correct: **C** — [4.2] Employees using unsanctioned AI tools that leak IP is Shadow AI. Model inversion (A) and membership inference (B) are attacks; differential privacy (D) is a defense.

**38.** Correct: **A** — [3.1] Surfacing deviations from learned baselines to flag intrusions is AI-driven anomaly detection. Watermarking (B), deepfakes (C), and token limits (D) don't perform behavioral detection.

**39.** Correct: **A** — [2.3] Granting an agent only the tools and scopes it needs is least privilege (with tool allow-listing). Encryption (B), obscurity (C), and fail-open design (D) don't constrain agent capability.

**40.** Correct: **B** — [2.1] The authoritative list of application-layer LLM risks (prompt injection, improper output handling, etc.) is the OWASP Top 10 for LLM Applications (2025). ATLAS (A) is adversary TTPs, ISO 42001 (C) is a management standard, and NIST 800-53 (D) is a controls catalog.

**41.** Correct: **D** — [1.1] A confident, fabricated citation is a hallucination. Overfitting (A), data drift (B), and gradient explosion (C) are training-related phenomena, not fabricated outputs at inference.

**42.** Correct: **A** — [4.1] In the NIST AI RMF, the Govern function establishes culture, policies, accountability, and oversight that cut across Map, Measure, and Manage. The others are the cross-cut targets, not the cross-cutting function.

**43.** Correct: **C** — [3.3] Letting non-developers build automations via drag-and-drop is low-code/no-code security automation. Kernel modules (A), manual runbooks (B), and recompiling the model (D) don't match.

**44.** Correct: **A** — [2.5] Thousands of near-identical probing prompts are caught by rate monitoring / behavioral anomaly detection on query patterns. Disk (B), certificate-transparency logs (C), and watermark checks (D) don't surface query abuse.

**45.** Correct: **B** — [2.6] Reconstructing a recognizable training-data image from confidence gradients is model inversion. Membership inference (A) only tests set membership, extraction (C) clones the model, and evasion (D) fools inference with crafted inputs.

**46.** Correct: **C** — [1.1] Asking the model to perform a task with no examples and no fine-tuning is zero-shot prompting. Multi-shot (A) supplies examples, fine-tuning (B) updates weights, and RL (D) is a training paradigm.

**47.** Correct: **D** — [2.2] Stored XSS from model output is prevented by treating output as untrusted and context-encoding/sanitizing it before rendering (improper-output-handling mitigation). Context window (A), temperature (B), and rate limits (C) don't stop XSS.

**48.** Correct: **D** — [3.3] Executing model-generated code in an isolated, least-privilege sandbox limits damage if it is malicious. Encrypting in transit (A), lowering temperature (B), and raising permissions (C) don't contain execution.

**49.** Correct: **A** — [4.3] Real-time remote biometric identification for indiscriminate public surveillance is generally Prohibited (unacceptable risk) under the EU AI Act, subject to narrow exceptions. It is not merely High (B), Limited (C), or Minimal (D).

**50.** Correct: **B** — [3.1] A standardized open interface connecting LLM assistants to external tools and data is the Model Context Protocol (MCP). TLS (A), OAuth device flow (C), and gRPC reflection (D) are not tool-connection protocols for LLMs.

**51.** Correct: **D** — [2.6] An assistant able to take high-impact actions far beyond its need (mass-delete, mass-email) is LLM06 Excessive Agency. Prompt injection (A) may be the trigger, but the root-cause category for excessive permissions/autonomy is LLM06; (B) and (C) describe different failures.

**52.** Correct: **C** — [3.3] Automatically analyzing third-party/open-source dependencies for known vulnerabilities is software composition analysis (SCA). Unit (A) and regression (B) testing check functionality; quantization (D) compresses models.

**53.** Correct: **B** — [4.2] A hiring model that favors a group most likely inherited bias from biased historical training data reflecting past human decisions. GPU firmware (A), TLS cipher (C), and tokenizer vocabulary size (D) don't drive demographic bias.

**54.** Correct: **A** — [2.3] Returning unauthorized chunks is fixed by enforcing document-level authorization at retrieval time, scoped to the user. Encrypting embeddings (B), prompt notes (C), and threshold tuning (D) don't enforce per-user access.

**55.** Correct: **C** — [3.1] Enumerating attack paths and auto-attempting exploitation in an authorized environment is AI-assisted/automated penetration testing. Summarization (A), translation (B), and watermarking (D) don't describe this.

**56.** Correct: **D** — [1.2] Embedding an imperceptible, detectable marker to identify AI-generated content is watermarking. Data minimization (A), differential privacy (B), and tokenization (C) don't tag generated media.

**57.** Correct: **B** — [4.1] Building and maintaining ingestion, cleansing, and transformation pipelines at scale is the data engineer's role. An AI auditor (A), AI security architect (C), and AI risk analyst (D) focus on oversight, security, and risk respectively.

**58.** Correct: **A** — [1.3] Detecting degradation and drift in production is ongoing monitoring and maintenance. Use-case definition (B), initial data collection (C), and model selection (D) occur earlier in the lifecycle.

**59.** Correct: **C** — [3.2] An AI system that adapts probing/payloads in real time to discover attack vectors is adversarial AI for automated attack generation / vector discovery. Differential privacy (A), federated learning (B), and data balancing (D) are not offensive automation.

**60.** Correct: **D** — [4.3] Intergovernmental, values-based principles (inclusive growth, human-centered values, transparency, accountability) describe the OECD AI Principles. PCI DSS (A) and ISO/IEC 27001 (B) are security standards; the EU AI Act (C) is binding regulation, not principles adopted across member countries.
