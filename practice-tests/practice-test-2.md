# CompTIA SecAI+ (CY0-001) — Practice Test 2 (Unofficial / Community)

> ⚠️ **UNOFFICIAL & COMMUNITY-MAINTAINED.** This practice test is a study aid. It is **not** affiliated with, endorsed by, or sourced from CompTIA, and it is **exam-realistic, not exam-identical** — it contains no official or actual exam items. Always reconcile with the official CompTIA SecAI+ objectives. Blueprint: [`../exam-objectives.md`](../exam-objectives.md).

**Instructions:** 60 questions • 60 minutes • single best answer (choose ONE). Each question is tagged with its official objective in brackets, e.g., `[2.2]`. Passing score on the real exam is **600 on a 100–900 scale**; as a study heuristic, aim for **~75%+ correct (≈ 45 of 60)** before sitting the exam. Answers and explanations are in [`practice-test-2-answers.md`](practice-test-2-answers.md) — try the whole test before checking.

Domain mix (per the official weightings): Domain 1 = 10 • Domain 2 = 24 • Domain 3 = 14 • Domain 4 = 12.

---

**1.** [1.1] A fraud team has very few examples of confirmed fraudulent transactions. They train two neural networks together — one generates synthetic transaction records and the other tries to distinguish the synthetic records from real ones — until the generator produces realistic samples that augment the training set. Which AI technique is this?
- A. Generative adversarial network (GAN)
- B. Reinforcement learning
- C. Federated learning
- D. Supervised linear regression

**2.** [2.1] A security architect wants a community-maintained, openly published repository that catalogs over a thousand AI risks extracted from existing frameworks and academic literature, organized by causal factors and risk domains, to seed an enterprise AI risk assessment. Which resource BEST fits this need?
- A. OWASP Top 10 for LLM Applications
- B. MITRE ATLAS
- C. MIT AI Risk Repository
- D. CVE AI Working Group

**3.** [1.3] In a clinical decision-support deployment, every AI-generated treatment suggestion must be reviewed and explicitly approved by a licensed clinician before it can reach a patient. Which human-centric AI design principle does this requirement embody?
- A. Data lineage tracking
- B. Federated learning
- C. Model quantization
- D. Human-in-the-loop

**4.** [2.2] A development team needs an LLM endpoint to return only responses that conform to a fixed JSON schema, automatically rejecting or regenerating any output that deviates, to curb insecure output handling downstream. Which control BEST enforces this?
- A. Per-key rate limiting
- B. Model guardrails with output-schema validation
- C. Encryption of responses at rest
- D. Network segmentation of the inference host

**5.** [3.1] A SOC wants its LLM assistant to query and act on live security tooling — ticketing, EDR, and threat-intel platforms — through a single standardized interface so the model can call those systems as tools. Which technology provides this standardized tool-access layer?
- A. Model Context Protocol (MCP) server
- B. Vector database
- C. Generative adversarial network
- D. Reverse proxy

**6.** [4.1] An enterprise creates a centralized, cross-functional body that sets AI standards, shares best practices, evaluates tooling, and guides responsible AI adoption across all business units. Which organizational structure is this?
- A. Security operations center (SOC)
- B. AI Center of Excellence
- C. Change advisory board
- D. Data loss prevention team

**7.** [2.3] An AI agent must call an internal customer database tool, but only to read records belonging to the user who initiated the request. Which access-control approach BEST enforces this at the tool-call boundary?
- A. Give the agent a shared administrator service account for simplicity
- B. Rely on the system prompt to instruct the agent not to exceed its scope
- C. Encrypt the database connection in transit only
- D. Enforce least-privilege, per-user scoped credentials on the agent's tool calls

**8.** [1.2] A team must document the original source, ownership, and chain of custody of every dataset used to train a model, so it can prove the data was lawfully obtained. Which data-security concept does this describe?
- A. Data augmentation
- B. Data balancing
- C. Data provenance
- D. Data masking

**9.** [2.4] A bank wants to run model inference over customer records while keeping the data encrypted even while it is being processed, so plaintext never appears in host memory. Which encryption approach BEST satisfies this in-use requirement?
- A. Confidential computing using a trusted execution environment (encryption in use)
- B. TLS 1.3 for data in transit
- C. AES-256 full-disk encryption for data at rest
- D. SHA-256 hashing of the records

**10.** [3.2] An attacker harvests a CFO's voice from public earnings calls, synthesizes a convincing clone, and phones the finance team to authorize an urgent wire transfer. Which AI-enabled attack technique is this?
- A. SQL injection
- B. Deepfake voice impersonation
- C. Membership inference
- D. Model theft

**11.** [4.2] Employees routinely paste proprietary source code into an unsanctioned public chatbot to debug it, with no IT approval or oversight. Which risk does this behavior MOST directly represent?
- A. Model inversion
- B. Data poisoning
- C. Differential privacy loss
- D. Shadow AI

**12.** [2.5] Finance reports that the monthly LLM API bill tripled with no increase in legitimate users, and security suspects abuse. Which monitoring capability MOST directly surfaces the token-consumption anomalies driving the cost spike?
- A. Hallucination auditing
- B. Bias and fairness auditing
- C. AI cost and token-usage monitoring
- D. Log sanitization

**13.** [2.6] A deployed classifier's accuracy silently degrades on one specific output class after an attacker contributed many mislabeled samples to the public dataset the team uses for periodic retraining. Which attack does this evidence BEST indicate?
- A. Model inversion
- B. Data poisoning
- C. Prompt injection
- D. Membership inference

**14.** [1.1] To improve classification quality, a prompt provides the model with three labeled input→label examples before presenting the new input it should classify. Which prompt-engineering technique is being used?
- A. Multi-shot prompting
- B. Zero-shot prompting
- C. System-role assignment
- D. Chain-of-custody prompting

**15.** [3.3] A DevSecOps team wants AI to automatically inspect every pull request for known-vulnerable third-party dependencies before the code can be merged. Which CI/CD capability does this describe?
- A. Unit testing
- B. Regression testing
- C. Code linting
- D. Software composition analysis (SCA)

**16.** [4.3] Which set correctly lists the four core functions of the NIST AI Risk Management Framework (AI RMF)?
- A. Govern, Map, Measure, Manage
- B. Identify, Protect, Detect, Respond
- C. Plan, Do, Check, Act
- D. Categorize, Select, Implement, Assess

**17.** [2.1] An LLM application concatenates retrieved web content directly into its prompt, and an attacker's planted text overrides the system instructions to exfiltrate data. Using the OWASP Top 10 for LLM Applications (2025), which category BEST classifies this?
- A. LLM02:2025 Sensitive Information Disclosure
- B. LLM01:2025 Prompt Injection
- C. LLM04:2025 Data and Model Poisoning
- D. LLM06:2025 Excessive Agency

**18.** [2.2] To prevent a single API consumer from causing a model denial-of-service through floods of large, expensive requests, which gateway control is MOST appropriate?
- A. Output-schema validation
- B. Training-data anonymization
- C. Model watermarking
- D. Per-key rate limits and token quotas

**19.** [1.2] A media company wants to embed an imperceptible but detectable marker into AI-generated images so it can later prove the content was machine-produced. Which technique is this?
- A. Data masking
- B. Tokenization
- C. Watermarking
- D. Quantization

**20.** [3.1] A security team deploys an unsupervised model that baselines normal user login behavior and flags statistically rare deviations, with no predefined signatures. Which AI use case does this represent?
- A. Signature matching
- B. Code linting
- C. Anomaly detection
- D. Translation

**21.** [2.3] An organization exposes an internal LLM only to authenticated services, each issued short-lived tokens from its identity provider with narrowly scoped permissions. Which access-control principle is PRIMARILY being applied?
- A. Least-privilege, scoped API access via short-lived tokens
- B. Perimeter defense in depth
- C. Data minimization
- D. Physically air-gapping the model

**22.** [4.1] Which AI-related role is PRIMARILY responsible for operationalizing, deploying, monitoring, and maintaining machine-learning models in production pipelines, including versioning, retraining, and rollback?
- A. AI auditor
- B. Data scientist
- C. MLOps engineer
- D. AI risk analyst

**23.** [2.4] Before fine-tuning on customer support transcripts, a team automatically detects and replaces SSNs and card numbers with placeholder tokens so that sensitive identifiers never enter the training set. Which data-security control is this?
- A. Data augmentation
- B. PII redaction (data masking) of training data
- C. Differential-privacy budgeting
- D. Encryption at rest

**24.** [1.3] In the AI lifecycle, which stage tests a trained model against a held-out dataset to measure accuracy, bias, and generalization before it is released to production?
- A. Model evaluation
- B. Data preparation
- C. Feedback and iteration
- D. Business use-case definition

**25.** [2.5] A security team is concerned that the prompt/response logs they capture could themselves become a data-leak vector if they store customer secrets in plaintext. Which logging control BEST addresses this?
- A. Increase log retention
- B. Rate monitoring
- C. Response-confidence scoring
- D. Log sanitization that redacts sensitive data before storage

**26.** [3.2] An attacker uses an LLM to rapidly fuse breach dumps, social-media activity, and DNS records into detailed target dossiers at scale, accelerating the planning phase of an intrusion. Which AI-enhanced attack capability is this?
- A. Output-integrity attack
- B. AI-driven automated reconnaissance and data correlation
- C. Model skewing
- D. Transfer-learning attack

**27.** [2.6] An LLM agent with broad plugin permissions deletes production records because a crafted input convinced it the destructive action was authorized. Which combination of compensating controls BEST reduces the blast radius of such excessive-agency incidents?
- A. Increase the model's context-window size
- B. Add more few-shot examples to the system prompt
- C. Apply least privilege to tools and require human approval for destructive actions
- D. Encrypt the agent's logs at rest

**28.** [4.2] A research team wants to publish aggregate statistics derived from a model while mathematically bounding how much any single individual's record can influence the released output. Which responsible-AI technique provides this guarantee?
- A. Differential privacy
- B. Explainability
- C. Federated learning
- D. Watermarking

**29.** [1.1] A company needs a model that runs entirely on-device for a privacy-sensitive mobile app with limited compute, accepting narrower capability in exchange for lower latency and a smaller footprint. Which model type BEST fits?
- A. A frontier large language model (LLM) served via cloud API
- B. A small language model (SLM) deployed on-device
- C. A generative adversarial network (GAN)
- D. A federated ensemble of large language models

**30.** [2.1] An organization wants to track and reference standardized, publicly disclosed identifiers for vulnerabilities found in AI/ML software components and frameworks. Which resource is MOST relevant?
- A. MIT AI Risk Repository
- B. OWASP Machine Learning Security Top 10
- C. CVE AI Working Group
- D. MITRE ATLAS

**31.** [3.3] A small SOC with few developers wants to automate phishing-triage playbooks by visually chaining together pre-built actions without writing code. Which approach BEST fits this constraint?
- A. A low-code/no-code automation (SOAR) platform
- B. Rewriting the SIEM in assembly
- C. Manual ticket triage only
- D. Training a custom GAN

**32.** [2.2] Before launching a customer-facing assistant, a team systematically probes its content-safety guardrails with adversarial jailbreak prompts to confirm the guardrails hold under attack. Which activity is this?
- A. Network penetration testing
- B. Guardrail testing and validation
- C. Load testing
- D. Data balancing

**33.** [4.3] A multinational must ensure that training data from EU customers is stored and processed only within the EU to comply with local law. Which compliance concept governs this requirement?
- A. Differential privacy
- B. Third-party attestation
- C. Data minimization
- D. Data sovereignty

**34.** [2.3] An LLM service must be able to reach its internal vector database but must never be able to open outbound connections to the public internet, even if compromised. Which control BEST enforces this?
- A. Token rate limiting
- B. Model guardrails
- C. Network egress filtering/segmentation isolating the model from the internet
- D. Output-schema validation

**35.** [1.2] A pipeline ingests a mix of free-text customer emails, JSON application logs, and relational database tables. Which data type BEST describes the free-text emails specifically?
- A. Unstructured data
- B. Structured data
- C. Semi-structured data
- D. Tokenized data

**36.** [2.4] To reduce breach impact, a team configures its AI pipeline to collect and retain only the specific data fields required for the model's task and nothing more. Which data-security principle is this?
- A. Data augmentation
- B. Data balancing
- C. Data masking
- D. Data minimization

**37.** [3.1] A developer wants inline, AI-assisted detection of insecure code patterns — hardcoded secrets, unsanitized SQL concatenation — flagged as they type in their editor. Which AI tool form factor BEST delivers this?
- A. A browser plug-in
- B. An IDE plug-in
- C. A standalone public chatbot website
- D. An MCP server for ticketing

**38.** [2.5] An AI medical-coding assistant should flag answers it is uncertain about for human review rather than presenting them as authoritative. Which monitoring signal BEST supports routing low-certainty outputs to a human?
- A. Rate monitoring
- B. AI cost monitoring
- C. Log protection
- D. Response confidence-level scoring

**39.** [4.1] Before broadly adopting generative AI tools across the workforce, which governance action should an organization take FIRST?
- A. Purchase the most powerful available GPUs
- B. Fine-tune a custom in-house model
- C. Deploy a SOAR platform
- D. Establish AI policies and procedures defining acceptable use

**40.** [2.6] An attacker repeatedly queries a deployed facial-recognition model and uses its outputs to reconstruct recognizable images of individuals whose data was in the training set. Which attack is this?
- A. Model inversion
- B. Membership inference
- C. Model theft
- D. Data poisoning

**41.** [3.1] A red team uses an AI-driven tool to autonomously enumerate a target environment, chain discovered weaknesses, and propose viable exploit paths with minimal human input. Which AI use case does this BEST represent?
- A. Code linting
- B. Automated penetration testing
- C. Translation
- D. Summarization

**42.** [2.1] A team is building a traditional (non-LLM) image-classification pipeline and wants a threat list specifically tailored to classical ML risks such as input manipulation, data poisoning, and model theft. Which resource is MOST appropriate?
- A. OWASP Top 10 for LLM Applications
- B. MITRE ATLAS
- C. OWASP Machine Learning Security Top 10
- D. EU AI Act

**43.** [3.2] Attackers use an LLM to automatically rewrite malware source code on every build so that signatures never match, while preserving the malware's function. Which AI-enhanced capability does this describe?
- A. Deepfake disinformation
- B. Membership inference
- C. AI-generated polymorphic malware (automated obfuscation)
- D. Model inversion

**44.** [2.2] An image-to-text API should reject any uploaded file larger than 5 MB and accept only PNG and JPEG formats, to limit abuse and resource exhaustion. Which gateway controls do these rules represent?
- A. Output watermarking
- B. Differential privacy
- C. Model guardrail prompt templates
- D. Input size quotas and modality (file-type) limits

**45.** [4.2] A firm markets its AI assistant's outputs as authoritative legal advice; clients act on them without attorney review and suffer harm. Which AI risk is MOST directly illustrated?
- A. Overreliance on AI outputs
- B. Data sovereignty violation
- C. Membership inference
- D. Model denial of service

**46.** [2.3] An AI procurement agent may draft purchase orders, but no order above $10,000 may be finalized without a person approving it. Which access-control pattern BEST implements this requirement?
- A. Encrypt the purchase-order database
- B. Require human approval (an authorization gate) before the agent executes high-value actions
- C. Rate-limit the agent's prompts
- D. Add few-shot examples of well-formed purchase orders

**47.** [3.3] A security team wants AI to automatically enrich, categorize, and route incoming incident tickets and draft initial response steps, reducing analyst toil. Which automation use case is this?
- A. Software composition analysis
- B. Regression testing
- C. Deepfake detection
- D. AI-assisted incident-response ticket management

**48.** [2.4] Before any dataset may enter an AI training pipeline, the organization tags it as Public, Internal, Confidential, or Restricted to drive downstream handling rules. Which data-security control is this?
- A. Data classification labeling
- B. Data augmentation
- C. Watermarking
- D. Quantization

**49.** [1.1] An agent learns an optimal sequence of firewall-rule changes by receiving rewards when it blocks attacks and penalties when it blocks legitimate traffic, with no labeled training dataset provided. Which training paradigm is this?
- A. Supervised learning
- B. Unsupervised learning
- C. Reinforcement learning
- D. Federated learning

**50.** [2.5] An audit finds that a hiring model recommends male candidates at a substantially higher rate than equally qualified female candidates. Which auditing activity is specifically designed to detect this problem?
- A. Hallucination auditing
- B. AI cost monitoring
- C. Bias and fairness auditing
- D. Rate monitoring

**51.** [4.3] Under the EU AI Act, a government program that performs general "social scoring" of citizens is classified into which risk tier?
- A. High risk
- B. Prohibited (unacceptable risk)
- C. Limited risk
- D. Minimal risk

**52.** [2.6] A competitor systematically queries a paid prediction API with many crafted inputs and uses the input/output pairs to train a functionally equivalent clone, avoiding licensing fees. Which attack is this?
- A. Model theft (model extraction)
- B. Membership inference
- C. Model inversion
- D. Prompt injection

**53.** [3.1] A SOC lead wants AI to condense a 40-page threat-intelligence report into a one-page executive brief. Which AI use case is this?
- A. Signature matching
- B. Summarization
- C. Fraud detection
- D. Penetration testing

**54.** [3.2] A coordinated campaign uses generative AI to mass-produce convincing but fabricated news articles intended to manipulate public opinion ahead of an election. Which AI-enabled threat is this?
- A. Spear-phishing payload generation
- B. Adversarial-example evasion
- C. AI-generated disinformation campaign
- D. Automated vulnerability scanning

**55.** [1.3] After deployment, a fraud-detection model's precision steadily declines as customer spending patterns shift over time. Which AI lifecycle activity is designed to catch this drift and trigger retraining?
- A. Monitoring and maintenance (drift detection)
- B. Business use-case definition
- C. Data collection
- D. Model selection

**56.** [3.2] An attacker feeds a target's LinkedIn history and prior emails to an LLM to auto-generate highly personalized phishing messages at scale. Which AI-enhanced attack vector is this?
- A. Model inversion
- B. Data poisoning
- C. Membership inference
- D. AI-generated spear-phishing (social engineering at scale)

**57.** [4.1] Which AI-related role PRIMARILY focuses on assessing, quantifying, and tracking AI-specific risks — such as bias, drift, and compliance gaps — and reporting them to leadership?
- A. Data engineer
- B. AI risk analyst
- C. Platform engineer
- D. Machine-learning engineer

**58.** [4.2] A customer-facing chatbot was fine-tuned on raw support logs and now occasionally emits another customer's personal details in its responses. Which AI risk does this MOST directly represent?
- A. Model denial of service
- B. Excessive agency
- C. Data sovereignty violation
- D. Accidental data leakage

**59.** [3.3] A CI/CD pipeline uses AI to evaluate each deployment's risk and automatically reverts the release when post-deploy error rates spike beyond a threshold. Which automation capability is this?
- A. Software composition analysis
- B. Data anonymization
- C. Automated deployment with AI-driven rollback
- D. Penetration testing

**60.** [4.3] An organization wants to formally certify its AI management system against an international standard created specifically for governing AI. Which standard is MOST appropriate?
- A. ISO/IEC 27001
- B. NIST AI RMF
- C. OECD AI Principles
- D. ISO/IEC 42001

---

*End of Practice Test 2. Score yourself with [`practice-test-2-answers.md`](practice-test-2-answers.md).*
