# CompTIA SecAI+ (CY0-001) — Practice Test 1 (Unofficial / Community)

> ⚠️ **UNOFFICIAL & COMMUNITY-MAINTAINED.** This practice test is **aligned to CY0-001 V1** but is a study aid only. It is **not** affiliated with, endorsed by, or sourced from CompTIA, and contains **no official or actual exam questions** — every item is original. Always reconcile with the official CompTIA SecAI+ objectives. Blueprint: [`../exam-objectives.md`](../exam-objectives.md).

**Instructions:** 60 questions • 60 minutes • single best answer (choose ONE). Each question is tagged with its official objective in brackets, e.g., `[2.6]`. The real exam passes at **600 on a 100–900 scale**; as a study heuristic, aim for **~75%+ correct (about 45/60)**. Answers and explanations are in [`practice-test-1-answers.md`](practice-test-1-answers.md) — try the whole test before checking.

---

**1.** [1.3] A security architect is embedding security into each phase of an AI system's life cycle. Which of the following BEST explains why security must begin at the *business use case* and *data collection* phases rather than at deployment?

- A. Inference-time controls such as prompt firewalls fully compensate for any weakness introduced earlier in the life cycle.
- B. Threats such as poisoned or untrustworthy training data and misaligned objectives are introduced early and become far costlier to remediate after a model is trained and deployed.
- C. Regulators only audit the data-collection phase, so other phases carry no security obligations.
- D. Model evaluation and monitoring are optional once a model has passed initial validation.

**2.** [2.6] A security analyst reviewing an LLM's logs finds that a customer-support summarizer began exfiltrating internal data after processing a vendor email that contained hidden instructions in white-on-white text. Which attack does this evidence MOST likely indicate?

- A. Membership inference
- B. Training-data poisoning
- C. Indirect prompt injection
- D. Model inversion

**3.** [3.1] A penetration tester wants an AI-enabled tool that runs locally in the terminal, chains reconnaissance and exploitation steps, and lets a model invoke external tools through a standardized interface. Which of the following BEST fits this need?

- A. A CLI plug-in connected to an MCP server that exposes pentest tools to the model
- B. A browser plug-in that summarizes web pages
- C. A static signature-matching antivirus engine
- D. A spreadsheet macro that formats scan output

**4.** [2.2] A security engineer must stop an internal chatbot from answering questions outside HR policy and from returning disallowed content. Which control set BEST implements this requirement at the model layer?

- A. Model guardrails enforced with constrained system-prompt templates plus output content filtering
- B. Network segmentation of the inference cluster
- C. At-rest encryption of the vector database
- D. Increasing the size of the model's context window

**5.** [4.3] A multinational deploys a résumé-screening model that decides who advances in hiring. Under the EU AI Act's risk-based tiers, this use case is MOST likely classified as which of the following?

- A. Minimal-risk, with no specific obligations
- B. High-risk, requiring conformity assessment, risk management, and human oversight
- C. Unacceptable-risk, and therefore prohibited outright
- D. Limited-risk, requiring only a transparency disclosure

**6.** [1.1] A data scientist needs a learning approach where labeled examples teach a model to map inputs to known outputs for a spam-classification task. Which technique is being described?

- A. Reinforcement learning
- B. Unsupervised learning
- C. Federated learning
- D. Supervised learning

**7.** [2.6] An attacker repeatedly queries a deployed image classifier with crafted inputs and uses the returned confidence scores to train a near-identical copy of the proprietary model. Which attack is this, and which control MOST directly limits it?

- A. Data poisoning; mitigated by data-lineage tracking
- B. Membership inference; mitigated by differential privacy
- C. Model inversion; mitigated by output encoding
- D. Model theft (extraction); mitigated by rate limiting and query/endpoint access controls

**8.** [2.1] A threat-modeling team wants an authoritative, regularly updated knowledge base of real-world adversary tactics and techniques *specific to AI/ML systems* to structure their analysis. Which resource is the BEST fit?

- A. OWASP Application Security Verification Standard (ASVS)
- B. The CIS Critical Security Controls
- C. MITRE ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)
- D. The OWASP API Security Top 10

**9.** [3.2] A red team uses generative AI to clone an executive's voice and leaves a phone message instructing finance to wire funds urgently. This use of AI MOST directly enhances which attack vector?

- A. Deepfake-enabled impersonation for social engineering
- B. Distributed denial of service
- C. SQL injection
- D. Cross-site scripting

**10.** [4.2] A CISO is cataloging risks of a customer-facing generative assistant. Employees have begun pasting confidential roadmaps into a public consumer chatbot to draft emails. Which risk does this BEST illustrate?

- A. Model skewing
- B. Accidental data leakage via shadow AI
- C. Reputational loss from biased outputs
- D. Intellectual-property infringement in generated images

**11.** [2.4] A healthcare AI team must let a model compute over patient records on an untrusted cloud host without ever exposing plaintext to the host. Which data-security control BEST meets this requirement?

- A. TLS 1.3 for data in transit
- B. AES-256 for data at rest
- C. Role-based access control on the API
- D. Encryption in use (e.g., confidential computing / homomorphic techniques)

**12.** [1.2] A team building a RAG application needs to store document chunks so that semantically similar passages can be retrieved at query time. Which pair of concepts BEST describes this mechanism?

- A. Embeddings stored in a vector database, retrieved by similarity search
- B. Plaintext logs indexed by timestamp
- C. Relational foreign keys joining normalized tables
- D. Signed hashes compared for exact byte matches

**13.** [2.3] A company exposes an internal LLM to several departments. Finance must reach payroll data while marketing must not. Which access-control approach BEST enforces this for the AI system's data layer?

- A. Give every department the same service account to simplify auditing
- B. Apply least-privilege, role-based data-access controls so each identity reaches only authorized data sources
- C. Rely on the model's guardrails alone to refuse unauthorized requests
- D. Encrypt all data at rest and grant broad read access

**14.** [3.3] A SOC wants to automate first-line triage so that low-severity alerts are enriched, deduplicated, and assigned tickets without analyst action, while high-severity cases still route to a human. Which approach BEST achieves this?

- A. Disable alerting for low-severity events to reduce noise
- B. Replace all analysts with a single autonomous agent that closes tickets
- C. An AI agent integrated into the incident-response/ticketing workflow with human-in-the-loop escalation for high severity
- D. A nightly batch report emailed to the team

**15.** [2.6] After a model update, a fraud-detection system begins approving a specific pattern of fraudulent transactions that it previously blocked. Investigation shows attackers slowly fed crafted "legitimate" feedback into the online-learning pipeline. Which attack does this BEST describe?

- A. Prompt injection
- B. Model inversion
- C. Model skewing through feedback/data poisoning
- D. Insecure output handling

**16.** [4.1] An enterprise wants a centralized body to set AI standards, share reusable patterns, vet tools, and coordinate governance across business units. Which organizational structure BEST describes this?

- A. A bug-bounty program
- B. A security operations center (SOC)
- C. A change advisory board (CAB)
- D. An AI Center of Excellence (CoE)

**17.** [2.5] A platform engineer must detect when a deployed LLM begins returning low-confidence, likely-hallucinated answers so the system can flag or withhold them. Which monitoring signal is MOST directly useful?

- A. CPU utilization of the inference nodes
- B. Response confidence-level monitoring
- C. At-rest storage growth of the model registry
- D. Number of open firewall ports

**18.** [1.3] A bank deploys a loan-decisioning model but requires that a qualified employee review and can override every adverse automated decision before it is finalized. Which human-centric design principle does this BEST represent?

- A. Human-in-the-loop oversight
- B. Unsupervised learning
- C. Zero-shot prompting
- D. Data minimization

**19.** [2.2] A security team finds users bypassing a chatbot's safety rules with elaborate role-play prompts. Which gateway-layer control is MOST appropriate to inspect and block malicious prompts *before* they reach the model?

- A. Increasing the model's temperature setting
- B. Encrypting the prompt logs at rest
- C. Adding more GPUs to the inference cluster
- D. A prompt firewall that screens inbound prompts against injection/jailbreak patterns

**20.** [3.1] A developer wants real-time, in-editor suggestions that flag insecure code patterns and propose fixes as they type. Which AI-enabled tool BEST provides this?

- A. An IDE plug-in performing AI-assisted code analysis and linting
- B. A network IDS appliance
- C. A SIEM correlation rule
- D. A disk-encryption agent

**21.** [4.3] An organization wants a voluntary, function-based framework to govern, map, measure, and manage AI risk across the life cycle. Which framework BEST matches this description?

- A. PCI DSS
- B. The NIST AI Risk Management Framework (AI RMF)
- C. The EU AI Act
- D. ISO/IEC 27001 only

**22.** [2.6] A model returns verbatim chunks of its proprietary system prompt and an internal API key when a user asks it to "repeat the text above." Which OWASP LLM (2025) risk category does this BEST map to?

- A. LLM06: Excessive Agency
- B. LLM04: Data and Model Poisoning
- C. LLM07: System Prompt Leakage / LLM02: Sensitive Information Disclosure
- D. LLM03: Supply Chain

**23.** [1.1] A team wants a model that learns useful structure from a large corpus of *unlabeled* logs by grouping similar events together. Which learning paradigm is being used?

- A. Supervised learning
- B. Reinforcement learning from human feedback
- C. Federated learning
- D. Unsupervised learning (clustering)

**24.** [2.1] A security lead wants a continuously expanding, peer-reviewed taxonomy of AI risks—organized by cause, domain, and life-cycle stage—to ensure the threat model is comprehensive. Which resource is the BEST fit?

- A. The MIT AI Risk Repository
- B. The CVE database of a single product
- C. The OWASP Top 10 for web applications
- D. A vendor's marketing whitepaper

**25.** [3.2] An attacker uses an LLM to automatically scan a target's public footprint, correlate employee data from multiple breaches, and draft tailored spear-phishing messages at scale. Which capability does this BEST illustrate?

- A. Watermarking of generated content
- B. Federated learning across victims
- C. AI-automated reconnaissance and data correlation for social engineering
- D. Differential privacy

**26.** [2.4] A data-protection engineer must let analysts work with a customer dataset for model training while ensuring no individual can be re-identified, even though aggregate patterns must remain usable. Which technique BEST meets this goal?

- A. Adding more replicas of the database
- B. Base64-encoding the records
- C. Data anonymization (with minimization of identifiers)
- D. Compressing the dataset

**27.** [4.2] A governance team is enumerating responsible-AI principles. A model produces consistent decisions for similar inputs and can explain the factors behind each decision. Which two principles are PRIMARILY demonstrated?

- A. Federated learning and quantization
- B. Throughput and latency
- C. Prompt engineering and fine-tuning
- D. Consistency and explainability

**28.** [2.3] An AI agent can call payment, email, and database tools. Security review finds the agent's service identity holds broad admin rights "to be safe." Which access-control change BEST reduces blast radius if the agent is hijacked via prompt injection?

- A. Scope the agent's credentials to least privilege—only the specific tools and records each task requires
- B. Give the agent a longer-lived API token to avoid re-auth
- C. Share one admin key across all agents for consistency
- D. Disable logging to improve agent performance

**29.** [3.3] A DevSecOps team wants AI to scan code, run software composition analysis, and execute model tests automatically on every commit, blocking merges that fail. Where does this capability BEST belong?

- A. In a quarterly manual review meeting
- B. In the model's system prompt
- C. Integrated into the CI/CD pipeline as automated gates
- D. In the end-user documentation

**30.** [3.3] An organization wants a low-code/no-code way for analysts to build automated security workflows (e.g., enrich an indicator, then open a ticket) without writing full applications. Which approach BEST fits?

- A. Hand-coding each workflow in assembly language
- B. A low-code/no-code automation platform orchestrating the steps
- C. Manually emailing each step to teammates
- D. Disabling automation to reduce risk

**31.** [1.2] An AI team must prove, for audit, exactly where each training record originated and every transformation it underwent. Which two data concepts are MOST relevant?

- A. Quantization and pruning
- B. Embeddings and vector storage
- C. One-shot and zero-shot prompting
- D. Data provenance and data lineage

**32.** [2.5] A security team needs to retain LLM prompt-and-response logs for investigations but must ensure those logs cannot be altered and do not themselves leak secrets that users submitted. Which combination BEST addresses this?

- A. Store logs in plaintext on a shared drive with open permissions
- B. Log protection (integrity/immutability and access control) plus log sanitization/redaction of sensitive fields
- C. Delete all logs immediately after each session
- D. Encrypt only the model weights and ignore logs

**33.** [4.1] An organization is assigning AI-related roles. Which role is PRIMARILY responsible for designing the secure architecture of AI systems and the controls that protect them?

- A. Data engineer
- B. AI security architect
- C. AI auditor
- D. MLOps engineer

**34.** [2.2] A guardrail team has written prompt templates and content filters. Before relying on them in production, what should they do FIRST to ensure the guardrails actually hold?

- A. Conduct guardrail testing and validation, including adversarial red-team prompts against the defined policies
- B. Increase the model's maximum token limit
- C. Publish the system prompt publicly for transparency
- D. Remove rate limits so testers can iterate faster

**35.** [3.1] A SOC analyst wants AI to baseline normal user and entity behavior and surface statistically unusual activity that signatures would miss. Which use case BEST describes this?

- A. Code linting
- B. Document translation
- C. Signature matching
- D. Anomaly detection / pattern recognition

**36.** [2.6] A computer-vision model in a self-checkout misclassifies a specific sticker pattern as a cheaper item every time the pattern is present, though it behaves normally otherwise. Which attack does this evidence MOST strongly suggest?

- A. A backdoor/trojan triggered by a specific input pattern
- B. Membership inference
- C. Model denial of service
- D. Sensitive information disclosure

**37.** [1.3] During which life-cycle activity is it MOST appropriate to confirm a model still performs acceptably against current real-world data and to detect drift after release?

- A. Business use-case definition
- B. Data preparation
- C. Monitoring and maintenance
- D. Model selection

**38.** [2.1] A working group coordinates how vulnerabilities in AI components are identified, numbered, and disclosed so defenders can track them consistently. Which resource is being described?

- A. The MIT AI Risk Repository
- B. The CVE AI Working Group
- C. MITRE ATLAS case studies
- D. The OWASP ML Security Top 10

**39.** [4.3] A company hosts customer data for EU residents and must ensure that data—and the AI processing of it—remains within specific national borders. Which compliance concept does this MOST directly address?

- A. Differential privacy
- B. Model quantization
- C. Data sovereignty
- D. Token-based rate limiting

**40.** [2.4] A logging pipeline must keep AI prompt logs useful for debugging while ensuring credit-card numbers that users paste in never persist in readable form. Which data-safety technique is the BEST fit?

- A. Increasing log retention to one year
- B. Replicating logs to a second region
- C. Compressing logs with gzip
- D. Data redaction/masking of sensitive fields before storage

**41.** [3.2] Adversaries increasingly use generative models to mutate malware so each sample has a unique signature while preserving behavior. Which AI-enabled attack enhancement does this BEST describe?

- A. Honeypot deployment
- B. AI-driven obfuscation / polymorphic payload generation
- C. Data lineage tracking
- D. Differential privacy

**42.** [1.1] A team fine-tunes a base LLM. They reduce the numeric precision of weights to shrink the model and speed inference. Which fine-tuning-related technique are they applying?

- A. Quantization
- B. Reinforcement learning
- C. Zero-shot prompting
- D. Data balancing

**43.** [3.2] A defender deploys a deceptive, AI-generated environment that mimics a vulnerable internal service to attract and study attackers. Which use of AI is this?

- A. Adversarial example generation
- B. Differential privacy enforcement
- C. An AI-generated honeypot for deception and threat intelligence
- D. Membership inference

**44.** [1.1] A research team trains a model across many hospitals' data *without centralizing the raw records*—each site computes updates locally and only shares model parameters. Which technique is this?

- A. Reinforcement learning
- B. Supervised fine-tuning
- C. Transfer learning
- D. Federated learning

**45.** [2.5] A finance team is alarmed by unpredictable LLM bills. They want to track spend by prompts, processing, response generation, and storage to catch abuse and runaway costs. Which monitoring capability BEST addresses this?

- A. Disk SMART monitoring
- B. AI cost monitoring across prompt, processing, response, and storage
- C. TLS certificate expiry monitoring
- D. Physical badge-access logging

**46.** [3.3] A change-management team wants AI to pre-screen low-risk infrastructure changes, recommend approval, and trigger automated deployment with rollback if health checks fail. Which capability BEST describes this?

- A. Manually paging an on-call engineer for every change
- B. Freezing all changes indefinitely
- C. AI-assisted change approvals with automated deployment/rollback
- D. Disabling health checks to speed deployment

**47.** [4.2] A board asks the security team to define "shadow AI." Which description is MOST accurate?

- A. AI features that are formally approved but temporarily disabled
- B. Open-source models that have been security-reviewed
- C. The extra cooling load cast by GPU clusters in the data center
- D. AI tools and services used by employees without organizational approval, oversight, or governance

**48.** [2.2] An LLM-backed app must cap how much any single user can send and how large each request may be, to blunt model-DoS and abuse. Which gateway controls BEST implement this?

- A. At-rest encryption and key rotation
- B. Rate limits, token limits, and input quotas (data size/quantity)
- C. Data anonymization and masking
- D. Federated learning across users

**49.** [2.3] A security engineer must restrict which networks and applications can call a sensitive model's inference API, allowing only an approved internal service. Which control is MOST appropriate?

- A. Increasing the model's context window
- B. Watermarking model outputs
- C. Network/API access controls (allowlisting and authenticated endpoints)
- D. Adding more training epochs

**50.** [3.1] An analyst wants to feed a long, multi-document incident report to an AI tool and receive a concise, accurate brief for leadership. Which AI use case is this?

- A. Summarization
- B. Fraud detection
- C. Signature matching
- D. Penetration testing

**51.** [4.1] An organization needs a role focused specifically on evaluating AI systems for compliance with policy, regulation, and control effectiveness—independent of the build team. Which role BEST fits?

- A. Machine learning engineer
- B. Platform engineer
- C. Data scientist
- D. AI auditor

**52.** [1.2] A team augments a small training set by rotating, cropping, and adding noise to existing images to improve robustness. Which data-processing technique are they using?

- A. Data augmentation
- B. Data redaction
- C. Quantization
- D. Watermarking

**53.** [2.1] A security architect wants a structured method to enumerate trust boundaries, data flows, and threats for a new RAG application *before* coding. Which of the following is the BEST first step?

- A. Apply a threat-modeling framework to the system's data flows and trust boundaries
- B. Purchase a larger GPU cluster
- C. Increase the model's temperature for creativity
- D. Skip modeling and rely on post-deployment monitoring

**54.** [3.2] A nation-state group uses generative AI to produce thousands of convincing fake news articles and social posts to sway public opinion before an election. Which AI-enabled threat does this BEST illustrate?

- A. Membership inference
- B. AI-generated disinformation/misinformation at scale
- C. Model inversion
- D. Insecure plug-in design

**55.** [2.4] A privacy engineer must ensure that a dataset shared with a vendor reveals only the data strictly necessary for the task and nothing more. Which principle BEST captures this requirement?

- A. Data augmentation
- B. Data balancing
- C. Data minimization
- D. Data provenance

**56.** [4.3] Leadership wants to distinguish "sanctioned vs. unsanctioned" and "private vs. public" model usage in policy. Which statement BEST reflects sound corporate AI policy?

- A. Sensitive data should be processed only with sanctioned, private models under governance—not pasted into unsanctioned public models.
- B. Any public model is acceptable as long as it is popular.
- C. Sanctioning models is unnecessary if employees are trustworthy.
- D. Private models require no governance because they are internal.

**57.** [2.5] A compliance auditor must continuously check a deployed model for hallucination rate, accuracy drift, and signs of biased outputs across protected groups. Which monitoring/auditing activity BEST covers this?

- A. Monitoring only API latency percentiles
- B. Tracking only data-center power usage
- C. Counting open TCP connections
- D. Auditing for quality and compliance—hallucinations, accuracy, and bias/fairness

**58.** [3.3] A security team wants AI to draft incident-response ticket updates and synthesize post-incident summaries from chat and log data to speed reporting. Which capability is this?

- A. Signature matching
- B. Adversarial training
- C. Document synthesis/summarization and IR ticket management
- D. Network segmentation

**59.** [4.1] A company is staffing AI governance. Which role is PRIMARILY responsible for translating regulatory and ethical requirements into enforceable AI policies and governance processes?

- A. Data engineer
- B. Platform engineer
- C. MLOps engineer
- D. AI governance engineer

**60.** [4.2] A model trained largely on data from one region performs poorly and unfairly for users in another region. Which AI risk does this BEST illustrate?

- A. Excessive agency
- B. Introduction of bias affecting fairness and model performance
- C. Insecure output handling
- D. Model theft
