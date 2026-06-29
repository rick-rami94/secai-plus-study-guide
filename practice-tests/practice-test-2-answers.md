# CompTIA SecAI+ — Practice Test 2: Answer Key & Explanations (Unofficial)

> ⚠️ **UNOFFICIAL / COMMUNITY-MAINTAINED.** Not affiliated with, endorsed by, or sourced from CompTIA. Use alongside the official objectives; where they differ, the official document wins. Questions: [`practice-test-2.md`](practice-test-2.md) · Blueprint: [`../exam-objectives.md`](../exam-objectives.md).

## Answer key

| Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|---|-----|
| 1 | A | 19 | D | 37 | A | 55 | D | 73 | B |
| 2 | B | 20 | C | 38 | C | 56 | A | 74 | C |
| 3 | D | 21 | A | 39 | D | 57 | C | 75 | D |
| 4 | C | 22 | B | 40 | A | 58 | C | 76 | B |
| 5 | B | 23 | D | 41 | C | 59 | B | 77 | A |
| 6 | A | 24 | C | 42 | D | 60 | D | 78 | A |
| 7 | D | 25 | A | 43 | B | 61 | B | 79 | C |
| 8 | C | 26 | B | 44 | B | 62 | C | 80 | A |
| 9 | A | 27 | D | 45 | A | 63 | D | 81 | B |
| 10 | B | 28 | C | 46 | C | 64 | A | 82 | C |
| 11 | D | 29 | B | 47 | D | 65 | A | 83 | A |
| 12 | C | 30 | A | 48 | B | 66 | C | 84 | D |
| 13 | B | 31 | C | 49 | B | 67 | B | 85 | D |
| 14 | C | 32 | A | 50 | A | 68 | A | 86 | C |
| 15 | A | 33 | D | 51 | D | 69 | B | 87 | D |
| 16 | D | 34 | C | 52 | A | 70 | C | 88 | B |
| 17 | A | 35 | D | 53 | C | 71 | D | 89 | B |
| 18 | B | 36 | B | 54 | B | 72 | D | 90 | A |

**Distribution:** A = 23, B = 23, C = 22, D = 22 (total 90).

---

## Explanations

**1.** Correct: **A** — [1.1] A nonzero temperature introduces probabilistic sampling over the token distribution, so identical prompts can yield different completions. B/C are unrelated to run-to-run variation; D (RLHF) shapes behavior but does not cause per-call randomness.

**2.** Correct: **B** — [2.1] Small, near-imperceptible perturbations that cause misclassification at inference, with no retraining, are classic evasion / adversarial examples. Poisoning (A) corrupts training; inversion (C) reconstructs training data; membership inference (D) tests dataset membership.

**3.** Correct: **D** — [3.1] Provenance and lineage records (with integrity checks) document which datasets/transformations produced a model. A/B/C are legitimate security/ops controls (encryption at rest, API-key access, load testing) but none records which data and transformations produced the model.

**4.** Correct: **C** — [4.1] *Map* establishes context and identifies risks/intended use. Govern sets culture/policy, Measure analyzes/tracks, Manage prioritizes and responds.

**5.** Correct: **B** — [5.1] Tool-call (function-invocation) logs with tool names and arguments let responders reconstruct agent actions. A omits tool activity; C/D are irrelevant to tool reconstruction.

**6.** Correct: **A** — [1.2] The vector database stores embeddings and serves nearest-neighbor search. Model registry tracks model versions, feature store serves ML features, AI gateway brokers/secures traffic.

**7.** Correct: **D** — [2.2] Malicious instructions hidden in attacker-controlled content that the model later ingests is indirect prompt injection. The victim never intended it (not direct), and there's no roleplay (jailbreak) or query-based copying (extraction).

**8.** Correct: **C** — [3.2] safetensors stores tensors only and cannot execute code on load. Pickle-based formats (A/B) and executables (D) can run arbitrary code.

**9.** Correct: **A** — [4.2] A model card summarizes intended use, data, performance, and limitations. A risk register tracks risks, an SBOM lists components, a EULA is a license.

**10.** Correct: **B** — [5.2] A prompt-injection/jailbreak detection classifier on inputs is the targeted control. A/C/D monitor infrastructure or code, not prompt content.

**11.** Correct: **D** — [1.3] Non-deterministic, data-centric behavior expands and shifts the attack surface, undermining fixed signatures/oracles. A/B/C are false generalizations.

**12.** Correct: **C** — [2.3] Code executing when a `.bin` model loads is unsafe deserialization (pickle) leading to RCE. The other options don't run code on load.

**13.** Correct: **B** — [3.3] Rate limiting and per-user quotas at the gateway curb floods. A (signup CAPTCHA) and C (TLS in transit) are real controls that don't throttle authenticated request floods; D harms observability without mitigating abuse.

**14.** Correct: **C** — [4.3] Safety functions in critical infrastructure fall under the EU AI Act's high-risk tier. Prohibited is for unacceptable uses; limited/minimal are lower.

**15.** Correct: **A** — [5.3] Revoking/rotating the abused key and disabling the tool stops active abuse first. Retraining, raising limits, or deferring review do not contain it.

**16.** Correct: **D** — [1.4] MITRE ATLAS catalogs adversary tactics/techniques against AI/ML. RMF and ISO 42001 are governance frameworks; OWASP LLM Top 10 is a risk list.

**17.** Correct: **A** — [2.4] An over-privileged agent coaxed into misusing its access on the attacker's behalf is excessive agency / confused-deputy misuse. The other options are unrelated attack classes.

**18.** Correct: **B** — [3.4] Per-agent identity with on-behalf-of (OBO) delegation preserves least privilege and accountability. Shared accounts, disabled auth, or embedded admin tokens violate it.

**19.** Correct: **D** — [4.4] SHAP/LIME provide per-prediction explanations for individual decisions. A/B/C provide aggregate or procedural information (overall accuracy, audit trails, intended-use docs), not per-prediction reasoning.

**20.** Correct: **C** — [5.4] Graceful degradation with failover to a backup model keeps reduced service available. Hard-failing (B) defeats the goal; A/D don't provide continuity.

**21.** Correct: **A** — [1.5] For a hosted closed model, the provider secures the weights and serving infrastructure. The consumer secures its own prompts, data, and integration.

**22.** Correct: **B** — [2.5] Determining whether a specific record was in the training set is membership inference. Inversion reconstructs data, extraction copies the model, evasion fools inference.

**23.** Correct: **D** — [3.5] Document-level authorization at retrieval enforces who may see which sources. A/B/C (encryption at rest, response disclaimers, retrieval logging) don't restrict who may retrieve which documents.

**24.** Correct: **C** — [4.5] Confirming the license/usage rights permit commercial deployment comes first. The other items are irrelevant to legal usage.

**25.** Correct: **A** — [5.5] Offense and defense collaborating with feedback loops to improve detections is purple teaming. B/C/D lack the collaborative detection-improvement loop.

**26.** Correct: **B** — [1.1] RAG grounds answers in retrieved authoritative data, reducing (not eliminating) hallucination. A overstates; C is false (access controls still matter); D is false (outputs still need monitoring).

**27.** Correct: **D** — [2.6] In OWASP LLM Top 10 (2025), Prompt Injection is LLM01. LLM02 is Sensitive Information Disclosure; LLM10 is Unbounded Consumption.

**28.** Correct: **C** — [3.6] Treat model output as untrusted: encode/validate before rendering to prevent XSS. Trusting it (B) is the vulnerability; A/D don't address output handling.

**29.** Correct: **B** — [4.6] Unsanctioned tool use with company data is shadow AI; address it with an AUP plus DLP for generative AI. The other pairings misdiagnose the issue.

**30.** Correct: **A** — [5.1] Drift and performance monitoring detects accuracy decline as data shifts. B/C/D monitor unrelated infrastructure/licensing.

**31.** Correct: **C** — [1.2] The AI gateway is the single chokepoint for auth, rate limiting, filtering, and logging. Feature store, vector DB, and model registry serve other roles.

**32.** Correct: **A** — [2.1] Injecting mislabeled samples to corrupt the trained model is data poisoning. Evasion/inversion/membership inference target inference or privacy, not training labels.

**33.** Correct: **D** — [3.7] Structured adversarial probing for jailbreaks and policy bypasses is AI red teaming. A/B/C test different properties.

**34.** Correct: **C** — [4.1] ISO/IEC 42001 specifies an AI management system (AIMS) for certification. 27001 is ISMS, 800-53 is controls, SOC 2 is an attestation.

**35.** Correct: **D** — [5.2] A planted secret that signals exfiltration when it appears is a canary token / honeytoken. A/B/C are unrelated controls.

**36.** Correct: **B** — [1.3] Dual-use means the same capability can serve benign or malicious ends. A/C/D mischaracterize the concept.

**37.** Correct: **A** — [2.2] Roleplay framing to bypass safety policy is a jailbreak. Indirect injection comes from external content; poisoning/extraction are different attacks.

**38.** Correct: **C** — [3.1] Differential privacy with calibrated noise bounds any single individual's influence on the model. Hashing identifiers (A), encrypting the dataset (B), and gradient clipping for stability (D) don't provide a formal bound on individual influence.

**39.** Correct: **D** — [4.2] An AI impact assessment evaluates effects on individuals' rights/opportunities before launch. A/B/C test other concerns.

**40.** Correct: **A** — [5.3] A kill switch immediately halts a harmful autonomous agent. The other options do not stop active harm.

**41.** Correct: **C** — [1.4] Google's Secure AI Framework (SAIF) guides building security into AI by design. ATLAS, RMF, and ISO 42001 are different frameworks.

**42.** Correct: **D** — [2.3] Uploading a near-identical model name to trick downloads is typosquatting. The other options are unrelated attack classes.

**43.** Correct: **B** — [3.2] Cryptographic model signing with verification before load proves integrity and origin. A/C/D don't establish authenticity.

**44.** Correct: **B** — [4.3] Government social scoring is prohibited (unacceptable risk) under the EU AI Act. The other tiers are less restrictive.

**45.** Correct: **A** — [5.4] Quotas, rate limits, and budget alerts together defend against cost-bombing/unbounded consumption. B and D increase exposure; C (mutual TLS) secures transport but doesn't limit consumption.

**46.** Correct: **C** — [1.5] Self-hosting shifts responsibility for patching the model and serving stack to the deploying organization. Provider/user/marketplace are not responsible for your deployment.

**47.** Correct: **D** — [2.4] An agent fetching an attacker-supplied URL to reach an internal metadata endpoint is SSRF/lateral movement via the agent's tool. The others are unrelated.

**48.** Correct: **B** — [3.3] Sandboxed, isolated execution limits the blast radius of malicious generated code. A linter (A) won't contain execution; trusting the code (C) or running it with admin rights (D) is dangerous.

**49.** Correct: **B** — [4.4] Differing approval rates across protected groups without justification is disparate impact, measured with fairness metrics. The other options misdiagnose it.

**50.** Correct: **A** — [5.5] An AI vulnerability disclosure program gives researchers a responsible reporting channel. The other options discourage or obstruct disclosure.

**51.** Correct: **D** — [2.5] Verbatim reproduction of training text and secrets is training-data memorization and regurgitation. A/B/C are different attack classes.

**52.** Correct: **A** — [3.4] A tool allow-list scopes which functions the agent may call. Wildcard permissions or logging-without-enforcement do not restrict the agent.

**53.** Correct: **C** — [4.5] With a closed model you cannot inspect weights/training data, so you rely more on vendor controls and attestations — making assessment essential. A/B/D are false.

**54.** Correct: **B** — [5.1] Privacy-aware logging with PII redaction/minimization balances observability and privacy. Plaintext-forever or no-logging are extremes; laptop-only logging is insecure.

**55.** Correct: **D** — [1.1] An embedding is a dense numeric vector capturing semantic meaning. A/B/C describe unrelated concepts.

**56.** Correct: **A** — [2.6] Unbounded Consumption is LLM10 in OWASP LLM Top 10 (2025). LLM01 is Prompt Injection; the others are different categories.

**57.** Correct: **C** — [3.5] Sanitizing/scanning retrieved content and treating it as untrusted defends against indirect prompt injection. Encryption at rest (A), retrieval authentication (B), and audit logging (D) don't neutralize malicious instructions embedded in otherwise-authorized content.

**58.** Correct: **C** — [4.6] DLP tuned for generative AI can programmatically block regulated data from reaching AI tools. Awareness emails alone don't enforce; A/B/D don't apply.

**59.** Correct: **B** — [5.2] Mapping detections to MITRE ATLAS techniques aligns alerts with a shared AI adversary taxonomy. The other options use unrelated signals.

**60.** Correct: **D** — [2.1] Using API responses to train an equivalent local copy is model extraction/stealing. Membership inference, poisoning, and evasion are distinct.

**61.** Correct: **B** — [3.6] Human-in-the-loop approval before high-impact actions (like wire transfers) reduces erroneous/manipulated actions. Full autonomy or removing logging increases risk.

**62.** Correct: **C** — [4.1] *Measure* analyzes, assesses, and tracks AI risks via metrics/tests. Govern/Map/Manage cover policy, context, and response respectively.

**63.** Correct: **D** — [5.3] Rolling back to the last known-good version is the fastest safe recovery from a poisoned deployment. A/B/C don't remove the poisoned model.

**64.** Correct: **A** — [1.2] Training learns parameters from data; inference applies the trained model to new inputs. B inverts the definitions; C/D are false.

**65.** Correct: **A** — [2.2] Coaxing the model to reveal its hidden instructions is system-prompt leakage. The other options are unrelated attack classes.

**66.** Correct: **C** — [3.7] Integrating automated safety evals into CI/CD runs safety/jailbreak tests on every change. A/B/D defer or remove testing.

**67.** Correct: **B** — [4.2] A risk register tracks each risk with owner, likelihood, impact, and treatment status. Model card, SBOM, and EULA serve other purposes.

**68.** Correct: **A** — [5.4] Backing up model weights, vector indexes, and configuration enables recovery of the AI service. The other options omit the critical assets.

**69.** Correct: **B** — [2.3] An MLBOM/SBOM inventories model components, datasets, and dependencies for supply-chain analysis. The others don't provide a component inventory.

**70.** Correct: **C** — [3.1] Validating, sanitizing, and vetting data sources/contributors reduces poisoning before training. A/B/D don't address input trust.

**71.** Correct: **D** — [4.3] GDPR Article 22 grants rights regarding solely automated decision-making, including human intervention. PCI/HIPAA and the EU AI Act minimal tier don't grant this right.

**72.** Correct: **D** — [5.5] AI-specific threat intelligence keeps defenses current against newly published attacks. A/B/C don't track emerging techniques.

**73.** Correct: **B** — [1.3] AI increases the speed and scale at which attacks can be produced and executed. A/C/D are false reassurances.

**74.** Correct: **C** — [2.4] One agent writing deceptive content that another reads/acts on is memory/conversation poisoning between agents. The other options are unrelated.

**75.** Correct: **D** — [3.3] Network segmentation isolates GPU/inference servers so a compromise can't reach core systems. A/B/C don't provide isolation.

**76.** Correct: **B** — [4.4] Contestability lets individuals challenge and seek redress for AI decisions. Latency/throughput/determinism are performance properties.

**77.** Correct: **A** — [5.1] Cost/usage monitoring flags anomalous token consumption/spend. B/C/D monitor unrelated signals.

**78.** Correct: **A** — [2.5] Reconstructing recognizable training images from model outputs is model inversion. Membership inference only tests presence; evasion/typosquatting are different.

**79.** Correct: **C** — [3.4] Move credentials to a secrets manager, rotate them, and remove them from code. Commenting out, base64, or relocating to the prompt all still expose the keys.

**80.** Correct: **A** — [2.5] Reconstructing original text from a stored embedding is embedding inversion. The other options are unrelated attacks.

**81.** Correct: **B** — [2.2] Passing raw LLM output into a shell without validation is improper/insecure output handling (OWASP LLM Improper Output Handling). The others don't fit the root cause.

**82.** Correct: **C** — [2.6] Sensitive Information Disclosure is LLM02 in OWASP LLM Top 10 (2025). LLM01 is Prompt Injection; the others are different categories.

**83.** Correct: **A** — [3.5] Apply authentication/access control to the exposed vector database first. Encrypting embeddings (B), reducing indexed documents (C), and query logging (D) leave the unauthenticated network access open.

**84.** Correct: **D** — [3.6] Prompt templating that separates trusted instructions from untrusted input hardens against injection. Direct concatenation (B) is the weakness; A/C don't help.

**85.** Correct: **D** — [5.3] After containment, assess the scope of exposed data and trigger breach-notification procedures. Deleting logs or staying silent is improper; adjusting the safety-filter threshold doesn't address breach obligations.

**86.** Correct: **C** — [2.1] Normal behavior except on a hidden trigger that forces attacker-chosen output is a backdoor/trojan model. Evasion, membership inference, and extraction differ.

**87.** Correct: **D** — [3.6] Applying PII redaction to outputs strips SSNs and similar identifiers before display. A/B/C don't redact.

**88.** Correct: **B** — [1.4] The OWASP Top 10 for LLM Applications (2025) enumerates the top LLM-application risks. The ML Top 10 targets classic ML, RMF is governance, ATT&CK is enterprise TTPs.

**89.** Correct: **B** — [5.4] Input size/complexity limits plus rate limiting and autoscaling caps resist resource-exhaustion (sponge/DoS). A/C/D increase exposure.

**90.** Correct: **A** — [2.2] Acting on unverified, fabricated AI output is overreliance. Poisoning, deserialization, and membership inference describe different problems.
