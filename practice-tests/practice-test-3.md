# CompTIA SecAI+ (CY0-001) — Practice Test 3 (Unofficial)

> ⚠️ **UNOFFICIAL / COMMUNITY-MAINTAINED.** This practice test is a study aid. It is **not** affiliated with, endorsed by, or sourced from CompTIA. Questions are original, exam-*realistic* items written against the official blueprint in [`../exam-objectives.md`](../exam-objectives.md) — not actual exam content. Where the official CompTIA objectives differ, the official document wins.

---

## Instructions

- **60 questions**, single best answer (A–D) each.
- Suggested time limit: **60 minutes** (matches the real exam length).
- Official passing score: **600** on a scale of 100–900. As a study heuristic, aim for **~75%+ correct (≈ 45 / 60)** before sitting the exam.
- Each question is tagged with its official objective, e.g., `[2.6]`.
- Answer key and explanations: [`practice-test-3-answers.md`](practice-test-3-answers.md). Try the whole test before checking.

---

**1.** [1.1] A security team wants an LLM to classify phishing emails using only a handful of labeled examples placed directly into the prompt, without changing the model's weights. Which technique are they using?
- A. Few-shot (multi-shot) prompting
- B. Fine-tuning
- C. Reinforcement learning from human feedback
- D. Federated learning

**2.** [2.6] An organization's image-based door-access system begins granting entry whenever a badge photo contains a specific small sticker pattern. Forensics show the behavior was implanted during training via mislabeled samples tied to that trigger. Which attack does the evidence indicate?
- A. Model inversion
- B. Membership inference
- C. Backdoor (trojan) attack
- D. Model extraction

**3.** [2.1] A security architect wants a MITRE ATT&CK-style knowledge base of real-world adversary tactics and techniques specifically targeting AI/ML systems to drive threat modeling. Which resource fits BEST?
- A. OWASP Top 10 for LLM Applications
- B. MIT AI Risk Repository
- C. NIST AI RMF
- D. MITRE ATLAS

**4.** [4.3] A medical-device company deploys an AI system that triages emergency-room patients and prioritizes their order of care. Under the EU AI Act, which risk tier most likely applies?
- A. High risk
- B. Limited risk
- C. Minimal risk
- D. Prohibited (unacceptable risk)

**5.** [3.3] A SOC wants to automatically triage and enrich incoming alerts, route them to the correct analyst queue, and have an LLM draft the initial incident write-up. Which use case BEST describes this?
- A. Automated penetration testing
- B. Deepfake generation
- C. AI-assisted incident-response ticket management
- D. Differential privacy

**6.** [2.2] To stop an LLM customer-service bot from being coerced into producing disallowed content, a team deploys a dedicated component that inspects and blocks malicious instructions in incoming prompts before they reach the model. Which control is this?
- A. Model registry
- B. Prompt firewall (input guardrail)
- C. Vector database
- D. Token bucket for billing

**7.** [2.3] An AI agent acts on behalf of many users and must access only the data each user is individually entitled to. Which access-control approach BEST enforces this?
- A. A single shared service account with admin rights for all users
- B. A static API key hard-coded into the agent
- C. Disabling authentication to reduce latency
- D. On-behalf-of (OBO) delegation that carries each user's identity and scope

**8.** [1.2] A regulated bank must be able to prove, for any production model, exactly which source datasets and transformations produced it. Which data-security concept satisfies this?
- A. Data augmentation
- B. Data lineage / provenance
- C. Data balancing
- D. Vector quantization

**9.** [3.2] An attacker clones a CFO's voice from public earnings-call recordings and phones the finance team to authorize an urgent wire transfer. Which AI-enabled attack technique is this?
- A. Deepfake voice impersonation for social engineering
- B. Membership inference
- C. Model extraction
- D. Data poisoning

**10.** [4.1] An organization wants a centralized body to set AI standards, share best practices, vet new use cases, and coordinate responsible-AI adoption across business units. Which structure is this?
- A. A bug-bounty program
- B. An AI Center of Excellence
- C. A security operations center
- D. A change advisory board

**11.** [2.4] Before using production customer records to fine-tune a model, a team replaces direct identifiers (names, SSNs) with realistic but fictitious values so the dataset remains useful while no longer mapping to real people. Which data-safety technique is this?
- A. Data classification labeling
- B. Encryption in transit
- C. Data masking (anonymization)
- D. Rate limiting

**12.** [2.5] A deployed LLM's monthly API bill spikes unexpectedly, and security wants to attribute spend by key and catch abuse early. Which monitoring capability is MOST directly relevant?
- A. TLS certificate-expiry monitoring
- B. Disk SMART monitoring
- C. Source-code linting
- D. AI cost monitoring (token/prompt/response usage per key)

**13.** [1.3] At which point in the AI lifecycle is verifying the trustworthiness and authenticity of incoming data MOST critical to prevent poisoned inputs from entering the pipeline?
- A. Model deployment
- B. Data collection
- C. Feedback and iteration
- D. Business use-case definition

**14.** [2.6] A competitor sends millions of crafted queries to a company's public prediction API and uses the input/output pairs to train a near-functional clone of the proprietary model. Which attack is this, and which control most directly limits it?
- A. Membership inference; differential privacy
- B. Data poisoning; input validation
- C. Model extraction (theft); rate limiting and query throttling
- D. Prompt injection; output encoding

**15.** [3.2] A threat actor uses an LLM to rapidly mutate malware source so that each build carries a unique signature, defeating hash-based detection. Which capability is the AI providing to the attacker?
- A. Membership inference
- B. Differential privacy
- C. Federated learning
- D. Automated obfuscation / polymorphic payload generation

**16.** [4.2] A hospital wants assurance that its diagnostic AI behaves consistently and does not fail in ways that endanger patients. Which Responsible AI principle is MOST directly at stake?
- A. Data portability
- B. Reliability and safety
- C. Vendor lock-in avoidance
- D. Throughput optimization

**17.** [2.2] A team wants to cap how many tokens a single request can consume and how many requests a user may send per minute to its LLM endpoint, mitigating denial-of-wallet abuse. Which gateway controls implement this?
- A. Data anonymization and masking
- B. Model signing and verification
- C. Token limits and rate limits
- D. Embedding encryption at rest

**18.** [2.5] An auditor must verify whether a deployed LLM is producing fabricated or low-confidence answers in regulated workflows. Which monitoring/auditing dimension addresses this?
- A. GPU temperature
- B. TLS handshake latency
- C. Packet-loss rate
- D. Hallucination/accuracy auditing with response-confidence review

**19.** [2.1] A team building a classical ML fraud model (not an LLM app) wants a threat-modeling reference focused on risks like evasion, data poisoning, and model inversion specific to ML systems. Which resource is the BEST fit?
- A. OWASP Top 10 for LLM Applications
- B. OWASP Machine Learning Security Top 10
- C. PCI DSS
- D. ISO/IEC 27001

**20.** [4.2] A bank's loan model must let denied applicants receive a meaningful reason for the decision. Which Responsible AI property MOST directly supports this?
- A. Explainability / transparency
- B. Higher token throughput
- C. Lower inference latency
- D. A larger context window

**21.** [3.1] A developer wants AI assistance that flags insecure code patterns and suggests fixes inline as they type, directly inside their editor. Which tool category provides this?
- A. An IDE security plug-in (AI code assistant)
- B. A vector database
- C. A model registry
- D. A honeypot

**22.** [1.1] Two neural networks—one generating synthetic samples and one trying to distinguish real from fake—are trained in competition to produce highly realistic outputs. Which architecture is described?
- A. Transformer
- B. Reinforcement-learning agent
- C. Support vector machine
- D. Generative adversarial network (GAN)

**23.** [2.3] A company wants to ensure that only specific authenticated applications can invoke its internal model endpoint and that each caller is limited to approved operations. Which control set BEST applies?
- A. Output PII redaction
- B. Data balancing
- C. API/endpoint access controls with authentication and authorization
- D. Watermarking the model outputs

**24.** [3.2] An attacker uses an LLM to scrape and correlate employees' public social-media posts, building detailed target profiles to craft convincing spear-phishing lures at scale. Which AI-enabled capability is this?
- A. Differential privacy
- B. Automated reconnaissance and data correlation
- C. Model watermarking
- D. Federated learning

**25.** [2.6] A model returns normal results except when a request contains the rare phrase "blue_orchid_42," at which point it leaks internal data. The phrase was inserted with malicious samples during training. Which attack is this, and which compensating control fits BEST?
- A. Evasion; output encoding
- B. Membership inference; rate limiting
- C. Backdoor/trojan via data poisoning; training-data integrity controls and provenance validation
- D. Model theft; query throttling

**26.** [4.3] A multinational must keep EU citizens' personal data physically stored and processed within the EU to satisfy regulatory requirements. Which concept governs this constraint?
- A. Differential privacy
- B. Model watermarking
- C. Federated learning
- D. Data sovereignty / data residency

**27.** [2.2] To keep an LLM assistant on-task and refuse out-of-scope or unsafe requests, a team defines a strict system prompt with embedded behavioral rules and a structured template applied to every request. Which control is this?
- A. A vector index
- B. Model guardrails via prompt templates / system prompts
- C. A token bucket
- D. Data-lineage tracking

**28.** [2.5] A privacy team is concerned that storing full prompts and responses for monitoring will retain customer PII indefinitely. Which practice balances investigative value with privacy?
- A. Log sanitization (PII redaction/tokenization) with protected, access-controlled storage
- B. Disabling all logging
- C. Writing logs to a public bucket for transparency
- D. Logging only after an incident is declared

**29.** [1.2] In a retrieval-augmented generation (RAG) system, what are embeddings?
- A. Numeric vector representations of text that enable semantic similarity search
- B. Encrypted copies of the model weights
- C. The GPU scheduling policy
- D. The system-prompt template

**30.** [3.3] A team wants every model release to automatically run scored safety and quality tests against a benchmark dataset, blocking promotion if results regress. Which CI/CD practice is this?
- A. Manual spot-checking
- B. GPU thermal throttling
- C. TLS rotation
- D. Automated model evals as a release gate

**31.** [4.1] An organization needs a professional accountable for designing and operating the controls, policies, and monitoring that keep AI systems compliant and risk-managed. Which role BEST fits?
- A. Front-end developer
- B. Database administrator
- C. AI governance engineer
- D. Help-desk technician

**32.** [2.6] By repeatedly querying a model and analyzing its confidence outputs, an attacker determines whether a specific person's medical record was included in the training set. Which attack is this?
- A. Model inversion
- B. Membership inference
- C. Model extraction
- D. Prompt injection

**33.** [3.2] A disinformation campaign uses generative AI to mass-produce realistic fake news articles and synthetic personas that amplify a false narrative across platforms. Which AI-enabled threat does this represent?
- A. AI-generated misinformation/disinformation at scale
- B. Membership inference
- C. Model extraction
- D. Differential privacy

**34.** [2.4] Sensitive fields must remain encrypted even while the model processes them in memory, protecting against a compromised host reading plaintext. Which protection addresses data "in use"?
- A. TLS for data in transit
- B. AES at rest on disk
- C. Confidential computing / encryption in use (e.g., a trusted execution environment)
- D. Output watermarking

**35.** [1.3] A bank requires that a human review and approve every AI-generated loan denial before it takes effect. Which human-centric design principle is this?
- A. Federated learning
- B. Zero-shot prompting
- C. Data augmentation
- D. Human-in-the-loop oversight

**36.** [2.1] A governance team wants a comprehensive, categorized catalog of documented AI risks—spanning causes, domains, and subdomains—to inform enterprise risk assessment. Which resource is designed for this?
- A. OWASP Top 10 for LLM Applications
- B. MIT AI Risk Repository
- C. PCI DSS
- D. The EU AI Act

**37.** [4.2] Employees are pasting proprietary source code into unsanctioned public chatbots, risking IP leakage outside the company's control. Which risk does this BEST describe?
- A. Model inversion
- B. Membership inference
- C. Shadow AI
- D. Differential privacy

**38.** [3.1] A SOC wants AI to surface unusual login and network patterns that deviate from learned baselines, flagging potential intrusions analysts would otherwise miss. Which use case is this?
- A. AI-driven anomaly detection
- B. Document watermarking
- C. Deepfake generation
- D. Token-limit enforcement

**39.** [2.3] To minimize the blast radius if an AI agent is compromised, the agent should be granted only the specific tools and data scopes it needs and nothing more. Which principle is this?
- A. Least privilege (with tool allow-listing)
- B. Defense in depth via encryption
- C. Security through obscurity
- D. Fail-open design

**40.** [2.1] A team building an LLM chatbot wants the authoritative list of the most critical application-layer risks specific to LLM applications (e.g., prompt injection, improper output handling). Which resource should anchor their threat model?
- A. MITRE ATLAS
- B. OWASP Top 10 for LLM Applications (2025)
- C. ISO/IEC 42001
- D. NIST SP 800-53

**41.** [1.1] A legal-research assistant confidently produces a citation to a court case that does not exist. What is this phenomenon called?
- A. Overfitting
- B. Data drift
- C. Gradient explosion
- D. Hallucination

**42.** [4.1] Within the NIST AI Risk Management Framework, which function establishes the organizational culture, policies, accountability, and oversight that cut across all of the other functions?
- A. Govern
- B. Map
- C. Measure
- D. Manage

**43.** [3.3] A platform team wants non-developers to build simple security automations (e.g., auto-disable a user when a SIEM alert fires) using a drag-and-drop workflow builder. Which approach is this?
- A. Writing custom kernel modules
- B. Manual runbooks only
- C. Low-code/no-code security automation
- D. Recompiling the model from source

**44.** [2.5] A single API key suddenly issues thousands of near-identical, boundary-probing prompts within minutes. Which monitoring capability BEST surfaces this abuse?
- A. Rate monitoring / behavioral anomaly detection on query patterns
- B. Disk-space monitoring
- C. Certificate-transparency logs
- D. Output-watermark verification

**45.** [2.6] An attacker repeatedly queries a face-recognition model and, using the returned confidence gradients, reconstructs a recognizable image of a person in the training data. Which attack is this?
- A. Membership inference
- B. Model inversion
- C. Model extraction
- D. Evasion

**46.** [1.1] A team asks a model to perform a translation task with no examples and no fine-tuning—just a clear instruction. Which prompting technique is this?
- A. Multi-shot prompting
- B. Fine-tuning
- C. Zero-shot prompting
- D. Reinforcement learning

**47.** [2.2] An LLM's output is inserted directly into a web page without sanitization, allowing script tags in the response to execute as stored XSS. Which control BEST prevents this?
- A. Increasing the model's context window
- B. Lowering temperature
- C. Adding a rate limit
- D. Treating model output as untrusted and context-encoding/sanitizing it before rendering

**48.** [3.3] An autonomous agent executes model-generated code as part of a remediation workflow. To limit damage if that code is malicious, which control is MOST important?
- A. Encrypt the code in transit
- B. Lower the model temperature
- C. Increase the agent's permissions for reliability
- D. Run the code in an isolated, least-privilege sandbox

**49.** [4.3] Under the EU AI Act, deploying a real-time remote biometric identification system for indiscriminate public surveillance generally falls into which category?
- A. Prohibited (unacceptable risk)
- B. High risk
- C. Limited risk
- D. Minimal risk

**50.** [3.1] A standardized open protocol lets LLM-based assistants connect to external tools and data sources (files, databases, APIs) through a uniform interface. Which is it?
- A. TLS 1.3
- B. Model Context Protocol (MCP)
- C. OAuth device flow
- D. gRPC reflection

**51.** [2.6] A support assistant was granted broad database-write and email-send permissions "to be helpful." A crafted prompt makes it mass-delete records and email customers. The root cause is that the model can take high-impact actions far beyond what it needs. Which OWASP LLM 2025 category applies?
- A. LLM01 Prompt Injection
- B. LLM02 Sensitive Information Disclosure
- C. LLM05 Improper Output Handling
- D. LLM06 Excessive Agency

**52.** [3.3] A DevSecOps pipeline should automatically analyze third-party and open-source dependencies for known vulnerabilities on every build. Which CI/CD capability is this?
- A. Unit testing
- B. Regression testing
- C. Software composition analysis (SCA)
- D. Model quantization

**53.** [4.2] A model trained on a company's historical hiring decisions systematically favors one demographic group. Where does this bias MOST likely originate?
- A. The GPU firmware
- B. Biased historical training data reflecting past human decisions
- C. The TLS cipher suite
- D. The tokenizer's vocabulary size

**54.** [2.3] A RAG chatbot occasionally returns document chunks the requesting user is not authorized to see, because retrieval ignores permissions. Which control BEST fixes this?
- A. Enforce document-level authorization at retrieval time, scoped to the requesting user
- B. Encrypt the embeddings at rest
- C. Add a system-prompt note asking the model not to reveal restricted content
- D. Lower the similarity threshold

**55.** [3.1] A red team wants AI assistance to enumerate likely attack paths and automatically attempt exploitation against an authorized test environment, accelerating coverage. Which use case is this?
- A. Document summarization
- B. Translation
- C. AI-assisted/automated penetration testing
- D. Watermarking

**56.** [1.2] A media company wants to embed an imperceptible, detectable marker into AI-generated images so the content can later be identified as machine-produced. Which technique is this?
- A. Data minimization
- B. Differential privacy
- C. Tokenization
- D. Watermarking

**57.** [4.1] Which role is primarily responsible for building and maintaining the data pipelines that feed AI systems—ingestion, cleansing, and transformation at scale?
- A. AI auditor
- B. Data engineer
- C. AI security architect
- D. AI risk analyst

**58.** [1.3] Once an AI model is in production, which lifecycle activity is MOST important for detecting performance degradation and drift over time?
- A. Ongoing monitoring and maintenance
- B. Business use-case definition
- C. Initial data collection
- D. Model selection

**59.** [3.2] An attacker deploys an AI-driven system that adapts its probing and payloads in real time based on a target's defensive responses, automating attack-vector discovery. Which describes this capability?
- A. Differential privacy
- B. Federated learning
- C. Adversarial AI for automated attack generation / vector discovery
- D. Data balancing

**60.** [4.3] An organization wants to align its AI practices with an intergovernmental set of values-based principles—such as inclusive growth, human-centered values, transparency, and accountability—adopted by many member countries. Which framework is this?
- A. PCI DSS
- B. ISO/IEC 27001
- C. The EU AI Act
- D. The OECD AI Principles
