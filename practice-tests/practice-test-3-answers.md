# CompTIA SecAI+ — Practice Test 3 Answer Key & Explanations (Unofficial)

> ⚠️ **UNOFFICIAL / COMMUNITY-MAINTAINED.** Not affiliated with, endorsed by, or sourced from CompTIA. Explanations reference community-blueprint objectives in [`../exam-objectives.md`](../exam-objectives.md) and well-established public frameworks (OWASP, NIST, MITRE ATLAS, ISO, EU AI Act). Reconcile against official CompTIA materials before exam day.

Questions: [`practice-test-3.md`](practice-test-3.md). Target pass ≈ **750/900 (~83%)**, roughly **75/90**.

---

## Answer key

| Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|---|-----|
| 1 | B | 19 | D | 37 | B | 55 | D | 73 | B |
| 2 | C | 20 | B | 38 | A | 56 | A | 74 | C |
| 3 | D | 21 | C | 39 | C | 57 | C | 75 | D |
| 4 | A | 22 | A | 40 | D | 58 | B | 76 | B |
| 5 | B | 23 | D | 41 | A | 59 | D | 77 | A |
| 6 | A | 24 | A | 42 | C | 60 | B | 78 | C |
| 7 | D | 25 | A | 43 | D | 61 | A | 79 | D |
| 8 | A | 26 | C | 44 | B | 62 | C | 80 | B |
| 9 | B | 27 | D | 45 | A | 63 | D | 81 | B |
| 10 | D | 28 | A | 46 | C | 64 | B | 82 | C |
| 11 | A | 29 | C | 47 | B | 65 | A | 83 | A |
| 12 | C | 30 | B | 48 | A | 66 | C | 84 | A |
| 13 | C | 31 | D | 49 | D | 67 | D | 85 | D |
| 14 | D | 32 | A | 50 | B | 68 | A | 86 | C |
| 15 | B | 33 | B | 51 | C | 69 | B | 87 | B |
| 16 | C | 34 | C | 52 | A | 70 | C | 88 | D |
| 17 | B | 35 | D | 53 | D | 71 | D | 89 | A |
| 18 | C | 36 | B | 54 | C | 72 | A | 90 | C |

**Distribution:** A = 23, B = 22, C = 23, D = 22 (total 90).

---

## Explanations

**1.** Correct: **B** — [1.1] Temperature and related sampling parameters control output randomness/diversity. Wrong: (A) context window sets how much text fits, not randomness; (C) parameter count is fixed model capacity; (D) embedding dimensionality affects representations, not per-call variance.

**2.** Correct: **C** — [2.1] Inference-time crafted input that fools a classifier without touching the model/data is an evasion (adversarial example). Wrong: (A) poisoning corrupts training data; (B) backdoor needs a trained-in trigger; (D) inversion reconstructs training data.

**3.** Correct: **D** — [3.2] safetensors stores tensors only with no code execution on load. Wrong: (A) pickle and (B) joblib can execute arbitrary code on deserialization; (C) HDF5 with custom/Lambda layers can also smuggle code.

**4.** Correct: **A** — [4.1] NIST AI RMF functions are Govern, Map, Measure, Manage. Wrong: (B) is the NIST CSF; (C) is PDCA; (D) is the NIST RMF for systems (SP 800-37).

**5.** Correct: **B** — [5.3] Immediate containment = revoke the agent's capability (disable tool, revoke keys / kill switch). Wrong: (A), (C) are later phases; (D) leaving it running prolongs harm.

**6.** Correct: **A** — [2.2] Malicious instructions delivered via content the model ingests (an email body) = indirect prompt injection. Wrong: (B) direct injection comes from the user's own prompt; (C) output handling is downstream trust; (D) is a privacy inference attack.

**7.** Correct: **D** — [3.6] Output must be treated as untrusted and context-encoded/sanitized before rendering to stop XSS. Wrong: (A) input validation guards the prompt, not the rendered output that carries the XSS; (B) prompt instructions are not a security boundary; (C) rate limiting doesn't stop XSS.

**8.** Correct: **A** — [5.1] Full prompt/response plus tool-call logs (args + results) are essential to reconstruct agent misuse. Wrong: (B), (C), (D) are too narrow to investigate behavior.

**9.** Correct: **B** — [4.2] A model card documents intended use, data characteristics, performance, and limitations. Wrong: (A) SBOM lists components; (C) DPA is contractual; (D) pentest is security testing.

**10.** Correct: **D** — [1.5] Even with SaaS LLMs, the customer owns what data is sent and how outputs are used. Wrong: (A), (B), (C) are provider-side responsibilities.

**11.** Correct: **A** — [2.3] A `__reduce__` payload executing on load is unsafe deserialization of a pickled model. Wrong: (B), (C), (D) describe unrelated attack classes.

**12.** Correct: **C** — [3.5] Enforce document-level authorization at retrieval time, scoped to the user. Wrong: (A) tuning the threshold doesn't gate access; (B) encryption-at-rest protects stored data but not who can retrieve it; (D) output redaction doesn't stop unauthorized chunks from being retrieved and used.

**13.** Correct: **C** — [5.4] Token/rate limits and per-user quotas directly bound cost and consumption. Wrong: (A) harms security and doesn't limit cost; (B) removing the system prompt weakens controls; (D) an output content filter screens content but doesn't bound request cost.

**14.** Correct: **D** — [4.3] Government social scoring is a Prohibited (unacceptable-risk) practice under the EU AI Act. Wrong: (A), (B), (C) are lower tiers.

**15.** Correct: **B** — [2.2] Exposing the hidden system/developer instructions themselves is LLM07 System Prompt Leakage. Wrong: (A) injection may be the vector but the *disclosure* is LLM07; (C), (D) are unrelated categories.

**16.** Correct: **C** — [1.4] MITRE ATLAS is the ATT&CK-style knowledge base of adversary TTPs against AI/ML. Wrong: (A) governance risk framework; (B) AIMS standard; (D) ML risk list, not a TTP knowledge base.

**17.** Correct: **B** — [3.3] An AI gateway is the central choke point for authn, rate limiting, guardrails, and logging. Wrong: (A), (C), (D) are storage/registry components, not policy enforcement points.

**18.** Correct: **C** — [5.2] A unique planted string watched for in egress/logs is a canary token / honeytoken. Wrong: (A) privacy technique; (B) availability control; (D) recovery action.

**19.** Correct: **D** — [2.1] Using confidence to decide if a record was in the training set is membership inference. Wrong: (A) extraction clones the model; (B) evasion fools classification; (C) poisoning is training-time.

**20.** Correct: **B** — [4.4] Explainability (XAI) supports giving applicants reasons for a decision. Wrong: (A), (C), (D) are performance traits, not transparency.

**21.** Correct: **C** — [3.7] Systematic adversarial probing for failure modes pre-release is AI red teaming. Wrong: (A) functional correctness; (B) privacy technique; (D) deployment strategy.

**22.** Correct: **A** — [1.1] Embeddings are numeric vectors of text used for semantic similarity search in RAG. Wrong: (B), (C), (D) misdescribe embeddings.

**23.** Correct: **D** — [5.3] First steps for a PII leak: contain the feature, preserve logs, and scope exposure before notifying. Wrong: (A) premature/extreme; (B) worsens exposure; (C) a rollback doesn't undo an already-disclosed record or replace containment and scoping.

**24.** Correct: **A** — [2.4] An agent coerced into fetching the cloud metadata endpoint is SSRF / confused-deputy via tool use. Wrong: (B), (C), (D) describe different attack classes.

**25.** Correct: **A** — [3.1] Data provenance/lineage with source validation is the foundational poisoning defense. Wrong: (B) encryption-at-rest protects confidentiality, not training-data integrity; (C) an output filter is downstream of training; (D) inference rate-limiting doesn't touch the poisoned upstream feed.

**26.** Correct: **C** — [4.5] License/usage-rights review catches commercial-use restrictions before adoption. Wrong: (A), (B), (D) are technical tests, not licensing.

**27.** Correct: **D** — [2.2] A model able to take high-impact actions beyond what's needed is LLM06 Excessive Agency. Wrong: (A), (B), (C) describe different failure modes.

**28.** Correct: **A** — [5.1] Gradual accuracy loss as data distribution shifts is detected by drift/performance monitoring. Wrong: (B), (C), (D) monitor infrastructure, not model quality.

**29.** Correct: **C** — [1.2] The model registry is the system of record for versioned, approved model artifacts. Wrong: (A) stores vectors; (B) stores features; (D) is a runtime gateway.

**30.** Correct: **B** — [3.4] Tool allow-listing restricts an agent to a vetted set of tools. Wrong: (A) broadening network access widens the blast radius; (C) logging is detective, not a constraint on which tools can be called; (D) transport encryption doesn't limit tool access.

**31.** Correct: **D** — [4.6] Unsanctioned AI use is Shadow AI; address with an AI usage policy plus DLP for generative AI. Wrong: (A), (B), (C) pair the wrong term and control.

**32.** Correct: **A** — [2.1] Querying an API en masse to clone a model is model extraction/stealing. Wrong: (B) membership inference; (C) poisoning; (D) prompt injection.

**33.** Correct: **B** — [5.4] Rolling back to the last validated model version is the fastest safe recovery. Wrong: (A), (C), (D) reduce safety or destroy evidence.

**34.** Correct: **C** — [3.6] Output PII redaction/filtering stops SSNs even when present in context. Wrong: (A) input-side injection filtering doesn't stop an SSN already in retrieved context from being emitted; (B) transport encryption doesn't redact content; (D) RBAC controls who can chat, not whether an SSN leaks in the answer.

**35.** Correct: **D** — [1.3] Non-deterministic, data-centric behavior expands/shifts the attack surface — the key distinction from deterministic software. Wrong: (A), (B), (C) are false generalizations.

**36.** Correct: **B** — [2.2] Inputs that maximize compute/cost map to LLM10 Unbounded Consumption. Wrong: (A), (C), (D) are different categories.

**37.** Correct: **B** — [4.2] A structured pre-deployment evaluation of societal/individual harms is an AI impact assessment. Wrong: (A), (C), (D) don't assess harm.

**38.** Correct: **A** — [5.2] Detection engineering that pipes guardrail signals into the SIEM enables jailbreak/canary alerting. Wrong: (B), (C), (D) reduce visibility or are irrelevant.

**39.** Correct: **C** — [3.2] Cryptographic model signing with verification on load proves integrity. Wrong: (A) TLS protects transit only, not tampering in storage or at load; (B) a private registry is access control, not tamper detection; (D) a CRC32 catches accidental corruption but is trivially forged by an attacker.

**40.** Correct: **D** — [2.3] Installing a misspelled package that exfiltrates on import is a typosquatted package attack. Wrong: (A), (B), (C) are different attack classes.

**41.** Correct: **A** — [1.1] Confidently producing a non-existent citation is a hallucination. Wrong: (B), (C), (D) are training-side concepts.

**42.** Correct: **C** — [4.1] ISO/IEC 42001 specifies a certifiable AI management system (AIMS). Wrong: (A) is an ISMS standard; (B) is a control catalog; (D) is payment-card security.

**43.** Correct: **D** — [5.5] A continuous loop where red-team findings feed blue-team defenses is purple teaming. Wrong: (A), (B), (C) are unrelated techniques.

**44.** Correct: **B** — [3.5] Sanitize retrieved content and delimit it as untrusted data to defend against indirect injection. Wrong: (A), (C), (D) don't neutralize embedded instructions.

**45.** Correct: **A** — [2.5] Reconstructing source text from stored vectors is embedding inversion. Wrong: (B) clones a model; (C) is an input attack; (D) targets availability.

**46.** Correct: **C** — [1.1] MCP standardizes how LLMs/agents connect to external tools and data sources. Wrong: (A), (B), (D) are unrelated functions.

**47.** Correct: **B** — [2.2] Trusting model output (a SQL string) without sanitizing it is LLM05 Improper Output Handling. Wrong: (A) injection is input-side; (C), (D) don't fit.

**48.** Correct: **A** — [3.4] Per-agent identity with on-behalf-of (OBO) delegation carries the user's scope so the agent only sees that user's data. Wrong: (B), (C), (D) over-grant access.

**49.** Correct: **D** — [4.3] GDPR Art. 22 grants a right not to be subject to solely automated decisions with legal effect, including human review. Wrong: (A), (B), (C) are other GDPR provisions.

**50.** Correct: **B** — [5.2] Thousands of near-identical boundary-probing queries are best caught by behavioral anomaly/abuse detection. Wrong: (A) spell-checking is irrelevant; (C) output filtering screens responses but doesn't surface the probing query pattern; (D) disabling the gateway removes visibility.

**51.** Correct: **C** — [2.1] Injecting mislabeled samples into training data is data poisoning at training time. Wrong: (A), (B), (D) are inference-time attacks.

**52.** Correct: **A** — [3.3] Running model-generated code in an isolated, least-privilege sandbox limits damage. Wrong: (B) a secondary-LLM review may miss malicious code and doesn't contain execution; (C) signing proves origin, not safety; (D) transport encryption doesn't constrain what the code can do when run.

**53.** Correct: **D** — [5.3] Prepare; detect/analyze; contain; eradicate; recover; lessons learned is the standard IR lifecycle. Wrong: (A), (B), (C) are out of order.

**54.** Correct: **C** — [4.4] Bias here originates from biased historical training data reflecting past human decisions. Wrong: (A), (B), (D) are unrelated to outcome bias.

**55.** Correct: **D** — [1.4] The OWASP Machine Learning Security Top 10 targets classical ML risks (evasion, poisoning, etc.). Wrong: (A) is LLM-app focused; (B) governance; (C) regulation.

**56.** Correct: **A** — [2.4] Planting false data into an agent's persistent memory is memory/conversation poisoning. Wrong: (B), (C), (D) are different attacks.

**57.** Correct: **C** — [3.7] Automated safety regression tests/evals in CI/CD prevent silent reintroduction of a fixed jailbreak. Wrong: (A), (B), (D) reduce assurance.

**58.** Correct: **B** — [5.1] Privacy-aware logging with PII redaction/tokenization and access controls balances investigation and privacy. Wrong: (A) blinds responders; (C), (D) are unsafe/insufficient.

**59.** Correct: **D** — [4.5] Self-hosting open weights means you inherit responsibility for securing, patching, and validating the artifact. Wrong: (A), (B), (C) are risks of the closed/hosted option.

**60.** Correct: **B** — [2.6] Poisoning a dataset used to train a victim model maps to ATLAS *Poison Training Data*. Wrong: (A), (C), (D) describe other ATLAS techniques.

**61.** Correct: **A** — [1.1] Permanently changing model behavior by updating weights on curated examples is fine-tuning. Wrong: (B) few-shot prompting, (C) RAG, and (D) prompt engineering all steer behavior at runtime without updating the weights.

**62.** Correct: **C** — [3.1] Differential privacy provably bounds any single record's influence on the model. Wrong: (A), (B), (D) don't provide that guarantee.

**63.** Correct: **D** — [5.4] Continuing limited service when a provider fails is graceful degradation / failover. Wrong: (A), (B), (C) are unrelated concepts.

**64.** Correct: **B** — [2.1] Normal behavior except on a trained-in trigger is a backdoor/trojan. Wrong: (A) evasion has no embedded trigger; (C), (D) are privacy/IP attacks.

**65.** Correct: **A** — [4.1] A committee setting responsible-AI policy and oversight maps to the NIST AI RMF Govern function. Wrong: (B) Measure assesses; (C) Map contextualizes; (D) Manage acts on risk.

**66.** Correct: **C** — [3.3] A content moderation/filtering guardrail at the I/O boundary blocks disallowed content. Wrong: (A), (B), (D) are storage/scheduling components.

**67.** Correct: **D** — [1.4] SAIF (Secure AI Framework) is Google's conceptual AI security framework. Wrong: (A) ISO AIMS; (B) regulation; (C) NIST risk framework.

**68.** Correct: **A** — [5.1] Monitoring token consumption and request-cost trends per user/key catches cost bombing early. Wrong: (B), (C), (D) are irrelevant metrics.

**69.** Correct: **B** — [2.2] Revealing sensitive data (a salary) with no system prompt involved is LLM02 Sensitive Information Disclosure. Wrong: (A) is for the system prompt specifically; (C), (D) don't fit.

**70.** Correct: **C** — [3.4] Store secrets in a managed vault, inject at runtime, and scan repos to prevent leaked-key recurrence. Wrong: (A) base64 is encoding, not protection; (B) making the repo private doesn't stop hard-coding secrets; (D) .gitignore after the fact leaves the key in history and still allows future hard-coding.

**71.** Correct: **D** — [4.2] Formally signing off to proceed with a residual risk is risk acceptance. Wrong: (A) avoid the activity; (B) shift to a third party; (C) reduce the risk.

**72.** Correct: **A** — [2.2] A user-typed instruction to bypass safety is direct prompt injection (a jailbreak). Wrong: (B) indirect comes via ingested content; (C), (D) are unrelated.

**73.** Correct: **B** — [5.3] AI incidents need unique actions (rollback, prompt-injection containment, key/tool revocation) generic plans omit. Wrong: (A), (C), (D) are incorrect rationales.

**74.** Correct: **C** — [1.2] Training learns/updates weights; inference uses the fixed model to produce outputs. Wrong: (A) reverses them; (B), (D) are false.

**75.** Correct: **D** — [3.1] Minimizing and classifying data and masking unnecessary PII most reduces privacy exposure before fine-tuning. Wrong: (A) encrypting weights protects storage, not the PII baked into the training set; (B) limiting notebook access helps insider risk but the model still learns the PII; (C) an output filter is downstream and leaves the training data exposed.

**76.** Correct: **B** — [4.6] An AI use-case approval/intake workflow enforces sign-off before deployment. Wrong: (A), (C), (D) are technical controls, not governance gates.

**77.** Correct: **A** — [2.4] One compromised agent steering others into harmful actions is multi-agent collusion / trust abuse. Wrong: (B), (C), (D) describe different problems.

**78.** Correct: **C** — [5.2] Map AI detections to MITRE ATLAS tactics and techniques. Wrong: (A), (D) aren't AI adversary taxonomies; (B) is a risk list, not detection TTPs.

**79.** Correct: **D** — [3.2] An ML/AI bill of materials (MLBOM/SBOM) tracks models, datasets, and dependencies for supply-chain transparency. Wrong: (A), (B), (C) don't enumerate the full supply chain.

**80.** Correct: **B** — [1.5] Self-hosting shifts securing/patching the serving infrastructure and weights to you. Wrong: (A), (C), (D) are always your responsibility regardless of model choice.

**81.** Correct: **B** — [2.2] Acting on a fabricated AI output without verification implicates LLM09 Misinformation and overreliance. Wrong: (A), (C), (D) pair unrelated categories.

**82.** Correct: **C** — [4.4] Comparing positive-prediction rates across protected groups uses a fairness metric (e.g., demographic parity). Wrong: (A), (B), (D) measure performance/integrity, not fairness.

**83.** Correct: **A** — [5.3] A kill switch that disables agent execution/tool access instantly halts autonomous actions. Wrong: (B) a rate limit slows but doesn't stop actions; (C) an audit log is detective; (D) a nightly retraining job doesn't halt the agent now.

**84.** Correct: **A** — [3.7] Evals are repeatable, scored quality/safety tests on benchmark data that gate releases. Wrong: (B), (C), (D) are unrelated checks.

**85.** Correct: **D** — [2.3] Replacing a hub checkpoint with a backdoored one is LLM03 Supply Chain. Wrong: (A), (B), (C) are different categories.

**86.** Correct: **C** — [1.3] Autonomous AI taking many high-impact actions rapidly with minimal human checks explains the speed/scale of impact. Wrong: (A), (B), (D) are false.

**87.** Correct: **B** — [4.3] Limited-risk systems (e.g., chatbots) carry transparency obligations — disclose that users are interacting with AI. Wrong: (A), (C), (D) are not EU AI Act requirements for this tier.

**88.** Correct: **D** — [5.5] A coordinated vulnerability disclosure process with tracking, remediation, and patching is the best response. Wrong: (A) ignores the issue; (B) is hostile to good-faith research; (C) silently patching with no tracking or disclosure skips remediation governance and verification.

**89.** Correct: **A** — [3.5] Source vetting/trust controls and validating ingested content before indexing reduce index poisoning. Wrong: (B) re-indexing more often just ingests the poisoned content faster; (C) removing rate limits and (D) granting more tools don't address tainted sources.

**90.** Correct: **C** — [2.6] Exploiting the inference server's web framework to gain host access is an AI-infrastructure attack, not an ML or LLM-prompt attack. Wrong: (A), (B), (D) misclassify an infrastructure compromise.
