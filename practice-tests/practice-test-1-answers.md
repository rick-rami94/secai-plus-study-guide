# CompTIA SecAI+ — Practice Test 1: Answer Key & Explanations (Unofficial / Community)

> ⚠️ **UNOFFICIAL & COMMUNITY-MAINTAINED.** Study aid only — not affiliated with, endorsed by, or sourced from CompTIA. Reconcile against the official CompTIA SecAI+ objectives. Questions: [`practice-test-1.md`](practice-test-1.md) • Blueprint: [`../exam-objectives.md`](../exam-objectives.md).

## Answer key (for fast self-scoring)

| Q | A | Q | A | Q | A | Q | A | Q | A |
|---|---|---|---|---|---|---|---|---|---|
| 1 | B | 19 | A | 37 | B | 55 | B | 73 | C |
| 2 | A | 20 | D | 38 | B | 56 | D | 74 | B |
| 3 | D | 21 | B | 39 | D | 57 | B | 75 | B |
| 4 | A | 22 | C | 40 | C | 58 | C | 76 | D |
| 5 | B | 23 | A | 41 | B | 59 | D | 77 | B |
| 6 | D | 24 | D | 42 | A | 60 | A | 78 | C |
| 7 | A | 25 | B | 43 | D | 61 | B | 79 | A |
| 8 | B | 26 | C | 44 | A | 62 | A | 80 | D |
| 9 | C | 27 | D | 45 | B | 63 | C | 81 | B |
| 10 | D | 28 | A | 46 | C | 64 | D | 82 | A |
| 11 | C | 29 | A | 47 | D | 65 | A | 83 | C |
| 12 | C | 30 | B | 48 | A | 66 | C | 84 | D |
| 13 | A | 31 | C | 49 | C | 67 | D | 85 | A |
| 14 | C | 32 | A | 50 | C | 68 | A | 86 | C |
| 15 | D | 33 | D | 51 | D | 69 | C | 87 | D |
| 16 | B | 34 | C | 52 | A | 70 | B | 88 | B |
| 17 | B | 35 | D | 53 | C | 71 | D | 89 | B |
| 18 | C | 36 | A | 54 | B | 72 | A | 90 | C |

Community pass guide: **~750/900 ≈ 83% correct** (≈ 75 of 90).

---

## Explanations

**1.** Correct: **B** — [1.3] AI adds non-determinism and a data-centric attack surface, so untrusted input at inference can change behavior. A is false (perimeter controls still matter); C is wrong (the surface expands, not shrinks); D ignores inference-time and supply-chain risk.

**2.** Correct: **A** — [2.2] The malicious instructions arrive *inside data the model processes* (the ticket), making this indirect prompt injection. Direct injection (B) is typed by the user into the prompt; poisoning (C) corrupts training data; inversion (D) reconstructs training data.

**3.** Correct: **D** — [3.3] An AI gateway centralizes authentication, rate limiting, and content filtering for LLM traffic. A vector DB (A) stores embeddings, a feature store (B) serves features, and a model registry (C) versions model artifacts.

**4.** Correct: **A** — [4.3] Employment/worker-selection systems are explicitly High risk under the EU AI Act. It is regulated but not Prohibited (D), and clearly above Limited (B) or Minimal (C).

**5.** Correct: **B** — [5.3] Containment comes first: disable the agent/tool and revoke its credentials to stop active abuse. A post-incident review (A) and retraining (C) come later; regulator notification (D) follows assessment, not as the first containment action.

**6.** Correct: **D** — [2.1] Determining whether a specific record was in the training set is membership inference. Extraction (A) clones the model, inversion (B) reconstructs data, and evasion (C) fools inference with crafted inputs.

**7.** Correct: **A** — [1.4] The NIST AI RMF functions are Govern, Map, Measure, Manage. B is the NIST CSF, C is the PDCA cycle, and D is from the NIST RMF for systems (SP 800-37).

**8.** Correct: **B** — [3.5] Enforcing document-level authorization at retrieval ensures users only get chunks they may see. Encryption at rest (A) protects stored data confidentiality but still returns chunks to any querent; a system-prompt instruction (C) is bypassable and is not real access control; output moderation (D) filters content categories but does not enforce per-user permissions.

**9.** Correct: **C** — [5.1] Investigating agent misuse requires prompt, response, and tool-call traces, with privacy-aware redaction. Outputs only (A) or network metadata only (B) miss the key evidence, and disabling logging (D) defeats investigation.

**10.** Correct: **D** — [2.2] Driving up cost and exhausting compute via heavy requests is LLM10 Unbounded Consumption (model DoS / cost harvesting). Not injection (A), poisoning (B), or output handling (C).

**11.** Correct: **C** — [4.1] ISO/IEC 42001 defines requirements for an AI management system (AIMS). 27001 (A) is for ISMS, 800-53 (B) is a control catalog, and 9001 (D) is quality management.

**12.** Correct: **C** — [3.6] LLM output must be treated as untrusted and validated/encoded before use to prevent injection and XSS (LLM05). Trusting it (A/B) or storing it raw (D) is unsafe.

**13.** Correct: **A** — [1.1] RAG retrieves external documents at query time without changing weights. Fine-tuning (B) and RLHF (C) update weights; quantization (D) compresses the model.

**14.** Correct: **C** — [5.2] A guardrail classifier that flags injection patterns and feeds the SIEM gives real-time detection. Relying on the model alone (A) is unreliable, blocking all external traffic (B) is impractical, and output encoding (D) is a valid control but addresses output-handling/XSS rather than detecting injection attempts.

**15.** Correct: **D** — [2.3] Loading an untrusted pickle can execute arbitrary code during deserialization. Bias (A), file size (B), and embedding misalignment (C) are not the primary security risk.

**16.** Correct: **B** — [3.2] Loading untrusted artifacts in a sandboxed, network-isolated environment with least privilege and resource limits contains any code execution that a malicious file attempts on load. Loading directly on a production GPU host (A) maximizes blast radius; a `.bin` extension (C) implies nothing about safety — serialized formats can still execute code; disabling endpoint security (D) removes a key detection layer.

**17.** Correct: **B** — [4.2] A model card documents intended use, performance, limitations, and ethical considerations. An SBOM (A) lists components, a DPA (C) governs data processing, and a pen-test report (D) covers security testing.

**18.** Correct: **C** — [1.5] With a SaaS LLM, the deployer still controls what data goes into prompts and how outputs are handled. The provider owns GPU firmware (A), training infrastructure (B), and model architecture (D).

**19.** Correct: **A** — [2.4] A privileged agent misused via user input to reach unauthorized data is the confused-deputy problem driven by excessive agency. The others (B, C, D) are unrelated attack classes.

**20.** Correct: **D** — [5.3] Rolling back to the last known-good model immediately stops the regression. Rate limits (A) and disabling logging (C) do not fix the leak, and retraining (B) is too slow for active exposure.

**21.** Correct: **B** — [3.4] On-behalf-of (OBO) delegation scopes downstream access to the requesting user's permissions. Shared accounts (A), global admin (C), and disabling auth (D) all violate least privilege.

**22.** Correct: **C** — [2.5] Reconstructing source text from stored vectors is embedding inversion. Membership inference (A) tests set membership, poisoning (B) corrupts data, and injection (D) manipulates prompts.

**23.** Correct: **A** — [4.6] Unsanctioned use of public AI tools with confidential data is shadow AI. Extraction (B), data residency (C), and federated learning (D) describe different concepts.

**24.** Correct: **D** — [1.2] A vector database stores embeddings and performs similarity search. A registry (A) versions models, a feature store (B) serves ML features, and a gateway (C) brokers/secures calls.

**25.** Correct: **B** — [5.4] Serving reduced/cached functionality during an outage is graceful degradation with failover. Autoscaling (A) and blue-green (C) are deployment/scaling tactics; differential privacy (D) is a privacy technique.

**26.** Correct: **C** — [2.2] Exposing the hidden system instructions (the model's internal rules and guidelines) is LLM07 System Prompt Leakage. Prompt injection (A) may be the vector but is not the exposure itself; LLM02 Sensitive Information Disclosure (B) covers leakage of user/training data or secrets — here only the instructions leak, not embedded data; misinformation (D) is unrelated.

**27.** Correct: **D** — [3.1] Provenance and lineage tracking with integrity verification confirms data came from trusted sources untampered — the core poisoning defense. Differential privacy (A) protects individual records' privacy, not source integrity; inference rate-limiting (B) addresses consumption; output encoding (C) handles model responses — none verify training-data trust.

**28.** Correct: **A** — [4.3] Government social scoring is a Prohibited (unacceptable-risk) practice under the EU AI Act. Spam filtering (B), disclosed chatbots (C), and game NPCs (D) are minimal/limited risk.

**29.** Correct: **A** — [2.1] Imperceptible perturbations that cause misclassification at inference are evasion (adversarial examples). Poisoning (B) corrupts training, inversion (C) reconstructs data, membership inference (D) tests set membership.

**30.** Correct: **B** — [5.5] Combining red and blue teams in a continuous feedback loop is purple teaming. A bug bounty (A), chaos engineering (C), and canary deployment (D) are different practices.

**31.** Correct: **C** — [3.3] Output guardrails / content moderation on responses block disallowed content and secret leakage. Input-side prompt filtering and rate limiting (A) act before the model and do not screen what it returns; network segmentation/egress filtering (B) controls connectivity, not response content; model signing (D) verifies artifact integrity — none moderate outputs.

**32.** Correct: **A** — [1.4] MITRE ATLAS catalogs adversary tactics/techniques against AI/ML. ATT&CK (B) covers enterprise IT broadly; CVE (C) and CWE (D) catalog vulnerabilities/weaknesses.

**33.** Correct: **D** — [2.6] Executing unsanitized model output that causes injection is LLM05 Improper Output Handling. Prompt injection (A) is the input side, excessive agency (B) is over-permissioned action, and unbounded consumption (C) is resource exhaustion.

**34.** Correct: **C** — [4.4] Explainability (XAI) lets the system provide a meaningful reason for a decision. Robustness (A) concerns resistance to perturbed inputs, reproducibility (B) concerns consistent results across runs, and availability (D) concerns uptime — none deliver a human-understandable rationale for a denial.

**35.** Correct: **D** — [5.2] Unique planted records that should never appear legitimately are canary tokens (honeytokens) used for exfiltration detection. DP noise (A), adversarial examples (B), and feature flags (C) serve other purposes.

**36.** Correct: **A** — [3.7] Systematically probing an LLM for jailbreaks and harmful outputs is AI red teaming. Unit (B), load (C), and static analysis (D) do not target adversarial model behavior.

**37.** Correct: **B** — [2.3] A deliberately misspelled lookalike model name to catch typos is typosquatting. Inversion (A), sponge (C), and injection (D) are different attacks.

**38.** Correct: **B** — [1.1] Temperature controls randomness/creativity of sampling. Context window (A) and token limit (C) govern length; embedding size (D) is a representation dimension.

**39.** Correct: **D** — [5.3] A PII exposure requires executing the data-leak playbook, including breach assessment and notification obligations. Rotating API keys and calling it resolved (A) ignores those obligations; deleting logs (B) destroys evidence; disabling explainability (C) is irrelevant to the breach response.

**40.** Correct: **C** — [2.2] An over-permissioned assistant taking a real-world action (issuing a refund) is LLM06 Excessive Agency. Sensitive disclosure (A), misinformation (B), and unbounded consumption (D) do not fit the over-permissioning root cause.

**41.** Correct: **B** — [3.5] Retrieved content can carry indirect injections, so treat it as untrusted and sanitize/filter before prompting. Encrypting the index at rest (A) addresses storage confidentiality; document-level access control (C) is a real RAG control but addresses authorization, not hidden instructions inside authorized documents; raising top-k (D) pulls in more potentially malicious content — none neutralize injection payloads.

**42.** Correct: **A** — [4.5] Verifying producer, license, and signatures addresses model provenance and licensing risk. Latency (B), cost (C), and context limits (D) are operational, not governance, concerns here.

**43.** Correct: **D** — [2.4] Coercing an agent's fetch tool to hit the cloud metadata endpoint is SSRF via the agent. Membership inference (A), poisoning (B), and extraction (C) are unrelated.

**44.** Correct: **A** — [1.3] Autonomous tool-chaining at machine speed without human checkpoints scales harm rapidly. HTTPS (B), databases (C), and deterministic rules (D) do not characterize agentic risk.

**45.** Correct: **B** — [5.1] Silent accuracy decline from shifting input distributions is detected by drift/performance monitoring. Rate limiting (A), output encoding (C), and canaries (D) address other concerns.

**46.** Correct: **C** — [3.6] Human-in-the-loop approval for high-impact actions (like wire transfers) limits damage from errors or manipulation. Output encoding (A) handles response rendering; verbose logging (B) is detective, not preventive; input rate limiting (D) throttles request volume but still permits a single damaging transfer — none gate the high-impact action itself.

**47.** Correct: **D** — [2.2] Leaking another customer's data from context is LLM02 Sensitive Information Disclosure. Prompt injection (A), improper output handling (B), and unbounded consumption (C) do not describe the cross-tenant data leak.

**48.** Correct: **A** — [4.1] Policies, accountability, and risk culture are the Govern function of the NIST AI RMF. Map (B) frames context, Measure (C) analyzes/tracks, and Manage (D) acts on prioritized risks.

**49.** Correct: **C** — [3.4] Restricting an agent to a vetted, explicit set of tools is tool allow-listing. Rate limiting (A) caps request volume, output encoding (B) sanitizes responses, and network egress filtering (D) restricts outbound destinations — none define which tools the agent may call.

**50.** Correct: **C** — [5.4] Per-user rate limits, quotas, and spending caps with alerting defend against cost-bombing/unbounded consumption. Signing API responses (A), output content moderation (B), and endpoint differential privacy (D) are legitimate controls for integrity, content, and privacy respectively but place no bound on request volume or cost.

**51.** Correct: **D** — [2.1] Cloning a model from query input/output pairs is model extraction (stealing). Membership inference (A), evasion (B), and poisoning (C) are different attacks.

**52.** Correct: **A** — [1.4] Google SAIF (Secure AI Framework) provides a secure-by-design conceptual approach for AI. PCI DSS (B), COBIT (C), and ITIL (D) are not AI-specific security frameworks.

**53.** Correct: **C** — [3.2] Cryptographic model signing and integrity verification proves authenticity and detects tampering. Encrypted-bucket storage (A) protects confidentiality at rest but not authenticity through the pipeline; output moderation (B) screens responses; antivirus scanning (D) catches known malware signatures but does not prove the artifact is the genuine, unaltered model.

**54.** Correct: **B** — [4.2] Documenting potential harms and mitigations before deploying a high-risk system is an AI impact assessment. A pen test (A), DR plan (C), and SLA (D) serve different purposes.

**55.** Correct: **B** — [2.5] Reproducing secrets verbatim from training data is memorization and regurgitation. Extraction (A), evasion (C), and sponge (D) are unrelated.

**56.** Correct: **D** — [5.5] Subscribing to feeds tracking new attack methods is threat intelligence for AI. Differential privacy (A), load testing (B), and data lineage (C) are different practices.

**57.** Correct: **B** — [3.3] Network segmentation with egress filtering prevents the inference server from reaching arbitrary hosts. Input guardrails (A) screen prompts, output encoding (C) handles responses, and model signing (D) verifies artifact integrity — none restrict outbound network connections.

**58.** Correct: **C** — [2.2] A persona prompt that bypasses safety guidelines is a jailbreak. Inversion (A), poisoning (B), and membership inference (D) are different attacks.

**59.** Correct: **D** — [1.2] Training learns/updates weights from data; inference applies the fixed model to produce outputs. A reverses the two, B is false, and C mischaracterizes label requirements.

**60.** Correct: **A** — [4.3] GDPR (Art. 22) grants rights over solely automated decisions with significant effects, including human review. HIPAA (B), PCI DSS (C), and SOX (D) do not.

**61.** Correct: **B** — [5.2] Unusual usage spikes and prompt patterns are surfaced by anomaly detection on usage/prompt telemetry. Differential privacy (A), model signing (C), and output encoding (D) are not detection methods here.

**62.** Correct: **A** — [3.1] Differential privacy adds calibrated statistical noise to limit what can be learned about any individual. Federated learning (B) keeps training data decentralized but adds no noise (and can still leak via updates); homomorphic encryption (C) computes over encrypted data without adding noise; rate limiting (D) is unrelated to training-data privacy.

**63.** Correct: **C** — [2.3] Replacing a production model in the registry with a backdoored one is a model registry (supply-chain) compromise. Injection (A), membership inference (B), and sponge (D) do not fit.

**64.** Correct: **D** — [1.5] Self-hosting shifts responsibility for securing/patching inference infrastructure and protecting model weights to the enterprise. Prompts (A), AUP (B), and UI (C) are already the enterprise's regardless of hosting.

**65.** Correct: **A** — [5.3] A kill switch lets operators immediately disable an autonomous agent during an incident. An incident-response runbook (B) guides the process but does not itself stop the agent; per-user rate limiting (C) throttles but does not halt active actions; a model card (D) is documentation — none provide an immediate stop.

**66.** Correct: **C** — [3.7] Running automated jailbreak/safety evals on every prompt or model change is continuous evaluation in CI/CD. Differential privacy (A), pen testing (B), and data lineage (D) do not catch safety regressions automatically.

**67.** Correct: **D** — [2.4] Planting false facts into persistent agent memory is memory (conversation) poisoning. Extraction (A), evasion (B), and sponge (C) are different attacks.

**68.** Correct: **A** — [4.4] Bias inherited from biased historical hiring data is historical/data bias in the training set. Latency (B), tokenization errors (C), and test-set overfitting (D) are not the source.

**69.** Correct: **C** — [4.5] Open weights give transparency and control but move security, patching, and provenance responsibility to the adopter. A, B, and D are overstated or false generalizations.

**70.** Correct: **B** — [5.1] Redacting/tokenizing sensitive fields with retention limits balances observability and privacy. Plaintext-forever (A) is risky, disabling logging (C) kills observability, and client-only logging (D) loses server-side evidence.

**71.** Correct: **D** — [3.5] Vetting and trust-scoring ingestion sources with integrity checks before indexing defends against index poisoning. Encrypting the index at rest (A) protects stored data, output content moderation (B) screens responses, and raising the similarity threshold (C) only changes ranking — none establish whether the ingested source is trustworthy.

**72.** Correct: **A** — [1.1] Confidently asserting a false, fabricated fact is hallucination. Overfitting (B), drift (C), and quantization (D) are different phenomena.

**73.** Correct: **C** — [4.6] DLP that inspects and blocks sensitive data sent to GenAI services prevents regulated-data leakage. Output content moderation (A) screens model responses, model signing (B) verifies artifact integrity, and SSO/MFA (D) authenticates users to the internal tool — none stop employees pasting regulated data into external services.

**74.** Correct: **B** — [2.2] A user typing override instructions directly into the prompt is direct prompt injection. Indirect (A) comes via processed data; inversion (C) and poisoning (D) are different attacks.

**75.** Correct: **B** — [5.4] Versioned backups of models, indexes, and configs enable fast rollback after corruption or a bad deploy. Autoscaling (A) adds capacity but cannot restore a corrupted index, disabling guardrails (C) is harmful, and encrypting the index at rest (D) protects confidentiality — none provide a known-good state to recover to.

**76.** Correct: **D** — [3.6] Prompt hardening with structured templates and delimiters separates trusted instructions from untrusted input, reducing injection. Output encoding (A) handles responses, input rate limiting (B) caps volume, and fine-tuning on more data (C) does not structurally distinguish system instructions from user input.

**77.** Correct: **B** — [2.5] Cross-tenant leakage in a shared vector store points to missing tenant isolation — namespace or partition separation so one customer's queries cannot retrieve another's chunks. Output encoding (A) handles rendering, unbounded consumption (C) is a resource concern, and model extraction (D) is a cloning attack — none describe the multi-tenancy isolation failure.

**78.** Correct: **C** — [4.5] Reviewing data licensing and EULA/usage rights before commercial fine-tuning prevents license violations. Penetration testing (A), bias/fairness auditing (B), and threat modeling (D) are all valuable reviews but address security, fairness, and architecture risk — not the legal right to use the dataset commercially.

**79.** Correct: **A** — [1.4] As Domain 1 frames it, AI trustworthiness extends the CIA triad with safety, privacy, and fairness. AAA (B) is a classic access-control model, not an AI-specific extension; scalability/latency/throughput (C) and portability/redundancy/elasticity (D) are performance and architecture attributes.

**80.** Correct: **D** — [5.3] The first step for a leaked key is to revoke and rotate it immediately. Retraining (A), future rate limiting (B), and reporting before acting (C) do not stop active abuse now.

**81.** Correct: **B** — [3.4] Per-agent identity with scoped least-privilege credentials enables attribution and limits blast radius. Shared accounts (A), no auth (C), and admin-for-all (D) violate least privilege.

**82.** Correct: **A** — [2.1] Normal behavior except on a hidden trigger is a backdoor (trojan) model. Membership inference (B), extraction (C), and sponge (D) describe other attacks.

**83.** Correct: **C** — [4.2] Formally documenting and signing off on tolerating a residual risk is risk acceptance, recorded in the risk register. Avoidance (A), transference (B), and "exploitation" (D) are different (or invalid) treatments.

**84.** Correct: **D** — [5.5] A post-incident review that feeds lessons into detections and controls most improves future resilience. Deleting logs (A) destroys evidence, deploying a new model version without root-cause analysis (B) risks reintroducing the issue, and disabling monitoring (C) reduces visibility — all weaken resilience.

**85.** Correct: **A** — [3.3] Input guardrails validate and filter prompts before they reach the model. Output guardrails (B) act on the model's responses (the wrong side for pre-screening prompts), cryptographic model signing (C) verifies artifact integrity, and a model card (D) is documentation — none filter inbound prompts.

**86.** Correct: **C** — [2.2] The root issue is the developer's overreliance on a model-fabricated (hallucinated) dependency, which OWASP maps to LLM09 Misinformation ("package hallucination"/slopsquatting). LLM03 Supply Chain (B) is the tempting distractor, but it covers compromise of *legitimate* third-party components, models, or data — here no real package was tampered with; the model invented a non-existent one and the developer trusted it. Prompt injection (A) and system-prompt leakage (D) do not fit the hallucination-plus-overreliance pattern.

**87.** Correct: **D** — [1.3] A capability useful for both defense and attack is dual-use. Non-determinism (A), overfitting (B), and drift (C) describe other properties.

**88.** Correct: **B** — [4.4] Comparing true-positive rates across groups evaluates a fairness metric (e.g., equalized odds / equal opportunity). Latency (A), throughput (C), and embedding size (D) are not fairness measures.

**89.** Correct: **B** — [5.2] Mapping AI-specific detections to MITRE ATLAS aligns them to a recognized taxonomy of adversary techniques against ML. PCI DSS (A), the OSI model (C), and ITIL (D) are not AI-attack taxonomies.

**90.** Correct: **C** — [3.7] Running automated evals/benchmarks against a curated test and regression set objectively compares safety and accuracy. File size (A), release date (B), and context window (D) are not measures of model quality.
