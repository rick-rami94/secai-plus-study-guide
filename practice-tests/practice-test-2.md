# CompTIA SecAI+ — Practice Test 2 (Unofficial)

> ⚠️ **UNOFFICIAL / COMMUNITY-MAINTAINED.** This practice test is a study aid. It is **not** affiliated with, endorsed by, or sourced from CompTIA. Questions are original, exam-*realistic* (not exam-identical), and mapped to the community [`../exam-objectives.md`](../exam-objectives.md). Where the official CompTIA objectives differ, the official document wins.

**Instructions**

- **90 questions**, single best answer (A–D).
- Suggested time limit: **165 minutes**.
- Target passing score: **~750/900 ≈ 83%** (community estimate) — aim for **75 / 90 correct**.
- Each question is tagged with its objective, e.g., `[2.2]`.
- Answers and explanations: [`practice-test-2-answers.md`](practice-test-2-answers.md).

---

**1.** [1.1] A developer submits the *identical* prompt to a production LLM twice within a minute and receives two materially different completions. Which factor MOST directly explains this nondeterministic behavior?

- A. A nonzero temperature/sampling setting introduces probabilistic token selection
- B. The model is retrained on each request, altering its weights between calls
- C. The tokenizer maps the identical prompt to different token IDs on each run
- D. RLHF was applied during the model's fine-tuning phase

**2.** [2.1] A security team observes that an image classifier reliably misidentifies stop signs after attackers place small, near-imperceptible sticker patterns on them. The model itself was never retrained. Which attack class BEST describes this?

- A. Data poisoning of the training set
- B. Evasion using adversarial examples at inference time
- C. Model inversion to reconstruct training images
- D. Membership inference against the training set

**3.** [3.1] A regulated lender must be able to prove, for any deployed model, exactly which datasets and transformations produced it. Which control BEST satisfies this requirement?

- A. Encrypting the model weights at rest in the registry
- B. Restricting inference access with per-user API keys
- C. Load-testing the model before each release
- D. Maintaining data provenance and lineage records with integrity verification

**4.** [4.1] An organization adopting the NIST AI RMF wants to first establish the context of an AI system and identify its risks and intended use before measuring anything. Which RMF function covers this activity?

- A. Govern
- B. Manage
- C. Map
- D. Measure

**5.** [5.1] An incident responder needs to reconstruct exactly which external tools an AI agent invoked, with what parameters, during a suspicious session. Which logging practice BEST enables this?

- A. Logging only the agent's final natural-language response to the user
- B. Capturing tool-call (function-invocation) logs including tool name and arguments
- C. Recording only aggregate request counts per hour
- D. Storing only the system prompt used to initialize the agent

**6.** [1.2] In a Retrieval-Augmented Generation (RAG) architecture, which component stores document embeddings and serves nearest-neighbor similarity search at query time?

- A. Vector database
- B. Model registry
- C. Feature store
- D. AI gateway

**7.** [2.2] An LLM-powered assistant summarizes web pages on request. An attacker publishes a page containing hidden text instructing the assistant to email the user's session data to an external address. When a victim summarizes the page, the assistant complies. Which attack is this?

- A. Direct prompt injection by the victim user
- B. A jailbreak using roleplay framing
- C. Model extraction via repeated queries
- D. Indirect prompt injection via attacker-controlled retrieved content

**8.** [3.2] A team distributes trained model weights and wants a serialization format that cannot execute arbitrary code when a file is loaded. Which format BEST meets this requirement?

- A. Python pickle (.pkl)
- B. A compressed pickle inside a ZIP archive
- C. safetensors
- D. A self-extracting executable bundling the weights

**9.** [4.2] A model owner must publish a concise document describing a model's intended use, training data characteristics, performance, and known limitations for downstream stakeholders. Which artifact is this?

- A. Model card
- B. Risk register entry
- C. Software bill of materials (SBOM)
- D. End-user license agreement (EULA)

**10.** [5.2] A SOC wants automated detection of inputs that attempt to override an LLM's system instructions or coax it into restricted behavior. Which capability is MOST appropriate?

- A. Disk-utilization threshold monitoring on the inference host
- B. A prompt-injection/jailbreak detection classifier applied to incoming prompts
- C. TLS certificate expiry monitoring for the API endpoint
- D. Static code analysis of the front-end application

**11.** [1.3] Compared with traditional software, which characteristic of AI systems MOST complicates signature-based defenses and fixed test oracles?

- A. AI systems always consume less compute than traditional software
- B. AI systems behave fully deterministically across all inputs
- C. AI systems never depend on third-party components
- D. Non-deterministic, data-centric behavior expands and shifts the attack surface

**12.** [2.3] A data scientist downloads a popular pretrained model as a `.bin` file from a public hub. Loading it immediately runs attacker code on the workstation. Which vulnerability was exploited?

- A. Membership inference against the model
- B. Adversarial perturbation of inputs
- C. Unsafe deserialization (e.g., pickle) leading to code execution on load
- D. Excessive agency in the model's tool permissions

**13.** [3.3] An LLM inference endpoint is being hit with floods of expensive requests, driving up cost and latency for legitimate users. Which deployment control BEST mitigates this?

- A. Adding a CAPTCHA only to the account-signup page
- B. Rate limiting and per-user quotas enforced at the AI gateway
- C. Encrypting request payloads in transit with TLS
- D. Disabling request logging to reduce overhead

**14.** [4.3] Under the EU AI Act, an AI system that controls safety functions in critical infrastructure is MOST likely categorized in which risk tier?

- A. Minimal risk
- B. Limited risk
- C. High risk
- D. Prohibited

**15.** [5.3] A monitoring alert shows an AI agent's API key is being abused from an unfamiliar IP, performing rapid privileged tool calls. What is the BEST FIRST containment action?

- A. Revoke/rotate the compromised API key and disable the affected tool
- B. Retrain the underlying model on clean data
- C. Increase the agent's rate limit to absorb the traffic
- D. Schedule a post-incident review for next quarter

**16.** [1.4] Which framework is specifically a curated knowledge base of real-world adversary tactics and techniques targeting AI/ML systems?

- A. NIST AI RMF
- B. ISO/IEC 42001
- C. OWASP Top 10 for LLM Applications
- D. MITRE ATLAS

**17.** [2.4] An autonomous agent holds broad internal permissions. An attacker crafts a request that causes the agent to use its privileged database tool to read records the *requesting user* should never access. Which risk does this BEST illustrate?

- A. Excessive agency / confused-deputy tool misuse
- B. Membership inference against training data
- C. A sponge attack on the inference server
- D. Model inversion of the embeddings

**18.** [3.4] A multi-tenant AI agent performs actions for many users. To preserve least privilege and accountability, how should it authorize downstream calls?

- A. Use one shared service account with full privileges for all users
- B. Carry per-agent identity with on-behalf-of (OBO) delegation of the user's scope
- C. Disable authentication on internal tool calls to reduce latency
- D. Embed a long-lived admin token directly in the system prompt

**19.** [4.4] A bank must explain to a regulator why its model denied a specific applicant. Which technique BEST provides per-prediction transparency?

- A. Reporting the model's aggregate accuracy on the test set
- B. Retaining immutable audit logs that a decision was made
- C. Publishing the model card's intended-use section
- D. Explainability methods such as SHAP or LIME for individual predictions

**20.** [5.4] An application depends on a single external LLM provider. Leadership wants the service to remain usable, with reduced capability, if that provider goes down. Which design BEST achieves this?

- A. Caching only static error pages to display during outages
- B. Hard-failing the entire application when the provider is unreachable
- C. Graceful degradation with automatic failover to a backup model
- D. Logging provider outages to a dashboard for later review

**21.** [1.5] An enterprise consumes a closed LLM purely through the provider's hosted API. Under the shared responsibility model, who is primarily responsible for securing the underlying model weights and serving infrastructure?

- A. The model provider
- B. The end user submitting prompts
- C. The enterprise's help-desk team
- D. The browser vendor

**22.** [2.5] An attacker repeatedly queries a deployed model to determine whether one specific person's record was part of its training data. Which attack is this?

- A. Model inversion
- B. Membership inference
- C. Model extraction/stealing
- D. Evasion via adversarial examples

**23.** [3.5] A RAG-based HR assistant returns salary documents to employees who lack clearance to view them. Which control MOST directly fixes this?

- A. Encrypting the documents at rest in the index
- B. Adding a confidentiality disclaimer to each chatbot response
- C. Logging which documents were retrieved for each query
- D. Enforcing document-level authorization at retrieval time

**24.** [4.5] Before deploying an open-weight model commercially, a company's legal team must confirm one thing FIRST. Which is it?

- A. Whether the model can be quantized for cheaper serving
- B. Which cloud region will host the workload
- C. The model license and usage rights permit commercial deployment
- D. How the model ranks on public benchmark leaderboards

**25.** [5.5] A security program pairs offensive testers and defensive analysts to collaboratively improve AI detections through shared findings. Which practice is this?

- A. Purple teaming with feedback loops to strengthen detections
- B. Penetration testing performed in isolation by an outside vendor
- C. A tabletop exercise with no technical execution
- D. Static application security testing (SAST) only

**26.** [1.1] In an enterprise knowledge assistant, what is the PRIMARY security-relevant benefit of using RAG instead of relying on the base model alone?

- A. It permanently removes the model's ability to hallucinate
- B. It grounds responses in retrieved, authoritative data, reducing hallucination
- C. It eliminates the need for any access controls on source documents
- D. It removes the need to monitor model outputs for accuracy

**27.** [2.6] In the OWASP Top 10 for LLM Applications (2025), which identifier corresponds to **Prompt Injection**?

- A. LLM10
- B. LLM06
- C. LLM02
- D. LLM01

**28.** [3.6] An LLM's response is rendered directly into a web page. To prevent stored/reflected XSS originating from model output, what should the application do?

- A. Store model outputs in an encrypted database
- B. Trust model output because it was generated internally
- C. Encode and validate model output as untrusted before rendering
- D. Authenticate users before showing model output

**29.** [4.6] Employees are pasting confidential customer data into a personal, unsanctioned public chatbot to draft emails. Which problem does this BEST represent, and what should address it?

- A. Model inversion, addressed by differential privacy
- B. Shadow AI, addressed by an AI acceptable-use policy and DLP for generative AI
- C. Membership inference, addressed by rate limiting
- D. Sponge attacks, addressed by autoscaling

**30.** [5.1] Over several weeks, a fraud-detection model's accuracy quietly declines as transaction patterns change. Which monitoring practice is designed to catch this?

- A. Drift and performance monitoring
- B. TLS handshake monitoring
- C. Disk fragmentation analysis
- D. Source-code license scanning

**31.** [1.2] An architecture team wants a single chokepoint to enforce authentication, rate limiting, content filtering, and logging across all LLM traffic. Which component provides this?

- A. Feature store
- B. Vector database
- C. AI gateway
- D. Model registry

**32.** [2.1] An attacker contributes mislabeled samples to a crowd-sourced dataset so that the resulting model systematically misclassifies a target category. Which attack is this?

- A. Data poisoning
- B. Evasion
- C. Model inversion
- D. Membership inference

**33.** [3.7] Before releasing a customer-facing chatbot, a team wants structured adversarial testing that probes for jailbreaks, harmful outputs, and policy bypasses. Which activity is this?

- A. Unit testing of UI components
- B. Load testing of the inference endpoint
- C. Spell-checking the system prompt
- D. AI red teaming with adversarial/jailbreak test suites

**34.** [4.1] Which international standard specifies requirements for an AI management system (AIMS) that an organization can be certified against?

- A. ISO/IEC 27001
- B. NIST SP 800-53
- C. ISO/IEC 42001
- D. SOC 2 Type II

**35.** [5.2] A defender seeds a fake but realistic credential into an internal knowledge base. If that exact secret ever appears in an LLM's output or in egress traffic, it signals data exfiltration. What is this control?

- A. Differential privacy noise injection
- B. Role-based access control
- C. Network address translation
- D. Canary tokens / honeytokens

**36.** [1.3] Which statement BEST captures the "dual-use" concern of generative AI from a security standpoint?

- A. The model can only be used by authorized administrators
- B. The same capability can serve benign purposes or be repurposed for malicious ones
- C. The model can be deployed either on-premises or in the cloud
- D. The model can be fine-tuned by more than one team

**37.** [2.2] A user wraps a restricted request inside an elaborate fictional roleplay ("You are an actor playing a hacker...") to coax the model into ignoring its safety policies. Which attack is this MOST precisely?

- A. Jailbreak
- B. Indirect prompt injection
- C. Data poisoning
- D. Model extraction

**38.** [3.1] A research team must train on sensitive records while provably limiting how much any single individual's data influences the model. Which technique BEST provides this guarantee?

- A. Hashing personal identifiers before training
- B. Encrypting the training dataset at rest
- C. Differential privacy with calibrated noise
- D. Gradient clipping for stability only

**39.** [4.2] An organization wants to evaluate, before launch, how a new AI hiring tool could affect individuals' rights and opportunities. Which assessment is MOST appropriate?

- A. A penetration test of the web front end
- B. A disaster-recovery tabletop exercise
- C. A static code review of the training scripts
- D. An AI impact assessment

**40.** [5.3] An autonomous trading agent begins executing harmful actions in real time. Which response capability is designed to stop it immediately?

- A. Activating a kill switch to halt the agent
- B. Filing a change request for the next sprint
- C. Sending an alert email to the security team
- D. Rotating the TLS certificate

**41.** [1.4] Which framework was published by Google to guide organizations in building security into AI systems by design?

- A. MITRE ATLAS
- B. NIST AI RMF
- C. Google Secure AI Framework (SAIF)
- D. ISO/IEC 42001

**42.** [2.3] An attacker uploads a model to a public hub under a name nearly identical to a widely used model, hoping developers fetch the wrong one. Which supply-chain attack is this?

- A. Membership inference
- B. Model inversion
- C. Insecure output handling
- D. Typosquatting of the model/package

**43.** [3.2] To ensure a model artifact has not been altered between training and deployment and originates from a trusted source, a team should implement which control?

- A. Storing the weights in a private cloud bucket
- B. Cryptographic model signing and signature verification before load
- C. Scanning the weights file with antivirus
- D. Renaming the file to include its training date and version

**44.** [4.3] Under the EU AI Act, government social-scoring systems that rank citizens' trustworthiness are MOST likely placed in which tier?

- A. High risk
- B. Prohibited (unacceptable risk)
- C. Limited risk
- D. Minimal risk

**45.** [5.4] To protect an AI service against cost-bombing and unbounded consumption, which combination of controls is BEST?

- A. Token/request quotas, rate limits, and budget/spend alerts
- B. Disabling all logging to save money
- C. Enforcing mutual TLS on the API endpoint
- D. Removing authentication to reduce overhead

**46.** [1.5] An organization self-hosts an open-weight model on its own infrastructure. Under the shared responsibility model, who is responsible for patching vulnerabilities in the model and its serving stack?

- A. The original model provider
- B. The end user submitting prompts
- C. The deploying organization itself
- D. The cloud marketplace listing the model

**47.** [2.4] A user-facing agent accepts a URL and fetches it with a built-in HTTP tool. An attacker supplies a link to the cloud metadata endpoint, and the agent retrieves internal credentials. Which risk is this?

- A. Membership inference
- B. Adversarial example evasion
- C. Differential privacy failure
- D. Server-side request forgery (SSRF) / lateral movement via the agent's tool

**48.** [3.3] A coding assistant generates and then executes code suggested by users. Which control BEST limits the blast radius of malicious generated code?

- A. Running a syntax linter over the code before executing it
- B. Executing generated code inside a sandboxed, isolated environment
- C. Trusting the code because the model produced it
- D. Logging the code but running it with admin rights

**49.** [4.4] An audit finds a loan model approves applicants at significantly different rates across protected groups with no business justification. Which concept describes this, and how is it measured?

- A. Hallucination, measured by perplexity
- B. Disparate impact, measured with fairness metrics
- C. Overfitting, measured by training loss only
- D. Latency, measured in milliseconds

**50.** [5.5] To let external security researchers responsibly report flaws discovered in a deployed model, an organization should establish which of the following?

- A. An AI vulnerability disclosure program
- B. A marketing bug-bounty press release only
- C. A policy forbidding any external contact
- D. A requirement that researchers sign over IP rights before reporting

**51.** [2.5] A general-purpose LLM, when prompted in a certain way, reproduces long verbatim passages of copyrighted text and an API key that appeared in its training corpus. Which phenomenon is this?

- A. Adversarial perturbation
- B. Confused-deputy escalation
- C. Sponge attack
- D. Training-data memorization and regurgitation

**52.** [3.4] An organization wants to strictly limit which external tools an AI agent is permitted to invoke. Which control implements this?

- A. Maintaining a tool allow-list that scopes the permitted functions
- B. Encrypting the agent's conversation history
- C. Giving the agent a wildcard permission to all tools
- D. Logging tool calls but enforcing no restrictions

**53.** [4.5] Why is third-party assessment especially important when adopting a *closed, proprietary* foundation model rather than an open one?

- A. Closed models always run faster and need no review
- B. Closed models never process sensitive data
- C. Limited visibility into the weights and training data increases reliance on vendor-provided controls and attestations
- D. Closed models are exempt from all regulation

**54.** [5.1] An AI assistant's prompt logs frequently contain customer PII. Which logging approach BEST balances observability with privacy obligations?

- A. Storing all prompts and responses in plaintext indefinitely
- B. Privacy-aware logging with PII redaction and data minimization
- C. Disabling all logging entirely
- D. Logging only to local developer laptops

**55.** [1.1] Which statement BEST describes what an *embedding* is in modern AI systems?

- A. A compression algorithm that losslessly shrinks model weights
- B. The system prompt prepended to every user request
- C. A cache of recent prompts and their responses
- D. A dense numeric vector representing the semantic meaning of text

**56.** [2.6] In the OWASP Top 10 for LLM Applications (2025), which identifier corresponds to **Unbounded Consumption**?

- A. LLM10
- B. LLM01
- C. LLM05
- D. LLM07

**57.** [3.5] A document retrieved by a RAG pipeline contains hidden instructions that, once placed in the prompt, hijack the model's behavior. Which defense MOST directly addresses this?

- A. Encrypting the vector database at rest
- B. Requiring user authentication before retrieval
- C. Sanitizing/scanning retrieved content and treating it as untrusted (indirect-injection defense)
- D. Logging the retrieved passages for later audit

**58.** [4.6] A company wants to stop employees from pasting regulated data into generative AI tools and to enforce that programmatically. Which control is MOST appropriate?

- A. A quarterly awareness email with no technical enforcement
- B. Rotating employee credentials more frequently
- C. Deploying DLP controls tuned for generative-AI usage
- D. Requiring VPN connections for all chatbot access

**59.** [5.2] A detection-engineering team wants its AI-specific alerts to align with a shared taxonomy of adversary techniques for AI systems. Which approach BEST supports this?

- A. Mapping detections to CPU performance counters
- B. Building detections mapped to MITRE ATLAS techniques
- C. Relying solely on antivirus signatures
- D. Alerting only on failed TLS handshakes

**60.** [2.1] An attacker with only API access sends a large, carefully chosen set of queries and uses the responses to train a near-equivalent local copy of a proprietary model. Which attack is this?

- A. Membership inference
- B. Data poisoning
- C. Evasion
- D. Model extraction/stealing

**61.** [3.6] An AI agent can initiate wire transfers. Which guardrail BEST reduces the risk of an erroneous or manipulated high-impact action?

- A. Allowing the agent to act fully autonomously to maximize speed
- B. Requiring human-in-the-loop approval before executing high-impact actions
- C. Letting the agent batch multiple transfers into one call
- D. Removing logging to reduce friction

**62.** [4.1] Which NIST AI RMF function is centered on analyzing, assessing, and tracking AI risks using metrics and test results?

- A. Govern
- B. Map
- C. Measure
- D. Manage

**63.** [5.3] A newly deployed model version turns out to have been poisoned and is producing attacker-favored outputs. Which response provides the FASTEST safe recovery?

- A. Lowering the API request quota for all users
- B. Restarting the inference servers
- C. Clearing the response cache
- D. Rolling back to the last known-good model version

**64.** [1.2] Which statement BEST distinguishes training from inference?

- A. Training learns model parameters from data; inference applies the trained model to new inputs
- B. Training serves predictions to users; inference adjusts the model's weights
- C. Training and inference are identical processes with different names
- D. Inference requires labeled data while training never does

**65.** [2.2] By repeatedly asking a chatbot to "repeat the text above" and "show your initial instructions," an attacker recovers the confidential system prompt. Which attack is this?

- A. System-prompt leakage
- B. Data poisoning
- C. Model inversion
- D. Sponge attack

**66.** [3.7] A team wants every code change to a safety-critical model to automatically run a battery of safety and jailbreak-resistance tests before merge. Which practice is this?

- A. Manual annual penetration testing only
- B. Disabling tests to keep the pipeline fast
- C. Integrating automated safety evals into CI/CD
- D. Reviewing logs after incidents only

**67.** [4.2] Where should an organization track each identified AI risk along with its owner, likelihood, impact, and treatment status?

- A. The model card
- B. A risk register
- C. The SBOM
- D. The end-user license agreement

**68.** [5.4] To recover an AI service after a destructive incident, which set of assets is MOST important to back up?

- A. Model weights, vector indexes, and configuration
- B. Only the marketing website
- C. Only the GPU driver version numbers
- D. Only the office network diagram

**69.** [2.3] A security team wants a complete inventory of a model's components, datasets, and dependencies to assess supply-chain exposure. Which artifact provides this?

- A. A model card describing intended use
- B. An MLBOM/SBOM for the model and its dependencies
- C. A privacy policy for end users
- D. A rate-limiting configuration file

**70.** [3.1] A model will be trained partly on untrusted, crowd-sourced contributions. Which control BEST reduces the risk of poisoning before training begins?

- A. Encrypting the training pipeline's network traffic
- B. Encrypting the final model at rest only
- C. Validating, sanitizing, and vetting data sources and contributors
- D. Placing the trained model behind an API gateway

**71.** [4.3] A customer subject to a *solely automated* loan decision wants meaningful human review of that decision. Which regulation MOST directly grants rights around solely automated decision-making?

- A. PCI DSS
- B. The EU AI Act's minimal-risk tier
- C. HIPAA Security Rule
- D. GDPR Article 22

**72.** [5.5] To keep defenses current against newly published attacks like novel jailbreak chains and poisoning techniques, a security team should MOST directly invest in which capability?

- A. Reducing the number of monitored log sources
- B. Disabling automatic updates to avoid breakage
- C. Reducing the logging retention period
- D. Consuming AI-specific threat intelligence feeds

**73.** [1.3] Which statement BEST describes how AI shifts the threat model in terms of impact?

- A. AI removes the need for monitoring because models self-heal
- B. AI increases the speed and scale at which attacks can be produced and executed
- C. AI guarantees that all outputs are safe by default
- D. AI eliminates supply-chain risk entirely

**74.** [2.4] In a multi-agent system, one agent writes deceptive content into a shared memory store that a second agent later reads and acts upon, corrupting its behavior. Which risk is this?

- A. Differential privacy leakage
- B. Adversarial example evasion
- C. Memory/conversation poisoning between agents
- D. Unsafe pickle deserialization

**75.** [3.3] An organization wants to isolate its GPU inference servers so a compromise there cannot reach core enterprise systems. Which control BEST accomplishes this?

- A. Enabling verbose request logging on the servers
- B. Storing weights in safetensors format
- C. Rotating the servers' TLS certificates regularly
- D. Network segmentation for the AI serving infrastructure

**76.** [4.4] Which trustworthy-AI property gives an individual the ability to challenge and seek redress for a decision an AI system made about them?

- A. Latency
- B. Contestability
- C. Throughput
- D. Determinism

**77.** [5.1] A sudden, sustained spike in token consumption and spend on an LLM API, outside normal patterns, is MOST likely surfaced by which monitoring capability?

- A. Cost/usage monitoring that flags anomalous consumption
- B. Endpoint antivirus scan reports
- C. TLS certificate expiry alerts
- D. License-compliance scanning

**78.** [2.5] An attacker uses a face-recognition model's confidence outputs to reconstruct recognizable images of individuals in its training set. Which attack is this?

- A. Model inversion
- B. Membership inference
- C. Evasion
- D. Typosquatting

**79.** [3.4] A code review finds long-lived API keys hardcoded directly in an agent's source. Which remediation is BEST?

- A. Commenting out the keys but leaving them in the file
- B. Encoding the keys in base64 within the source
- C. Storing credentials in a secrets manager and rotating them, removing them from code
- D. Moving the keys into the system prompt instead

**80.** [2.5] A team discovers that, given a stored embedding vector, an attacker can approximately reconstruct the original sensitive text it was derived from. Which attack does this describe?

- A. Embedding inversion
- B. Data poisoning
- C. Jailbreak
- D. Sponge attack

**81.** [2.2] An LLM's raw output is passed directly into a downstream shell command without validation, allowing injected commands to execute. Which OWASP LLM risk does this BEST represent?

- A. Unbounded consumption
- B. Improper/insecure output handling
- C. Model theft
- D. Excessive agency only

**82.** [2.6] In the OWASP Top 10 for LLM Applications (2025), which identifier corresponds to **Sensitive Information Disclosure**?

- A. LLM01
- B. LLM06
- C. LLM02
- D. LLM09

**83.** [3.5] An audit finds the vector database backing a RAG system is reachable on the network with no authentication. Which control should be applied FIRST?

- A. Apply authentication and access control to the vector database
- B. Encrypt the embeddings stored in the database
- C. Reduce the number of indexed documents
- D. Log all queries sent to the database

**84.** [3.6] To make prompt injection harder, an application should structure prompts so that trusted instructions are clearly separated from untrusted user/retrieved data. Which technique is this?

- A. Shortening every user message to a fixed length
- B. Concatenating user input directly into the instruction string
- C. Disabling output logging
- D. Prompt templating that separates trusted instructions from untrusted input

**85.** [5.3] A company confirms its support chatbot exposed customer PII in responses. After containing the issue, what is the MOST appropriate next action?

- A. Delete all logs to reduce liability
- B. Quietly redeploy and take no further action
- C. Raise the model's safety-filter threshold
- D. Assess the scope of exposed data and trigger breach-notification procedures

**86.** [2.1] A model behaves normally on ordinary inputs but produces an attacker-chosen output whenever a specific hidden trigger pattern is present. Which attack is this?

- A. Evasion via gradient noise
- B. Membership inference
- C. Backdoor/trojan model
- D. Model extraction

**87.** [3.6] Before returning chatbot responses to users, an organization wants to automatically strip out Social Security numbers and similar identifiers. Which guardrail accomplishes this?

- A. Encrypting the response payload in transit
- B. Authenticating the user before responding
- C. Disabling the content filter
- D. Applying PII redaction to model outputs

**88.** [1.4] Which resource is specifically designed to enumerate the most critical security risks for applications built on large language models?

- A. The OWASP ML Security Top 10
- B. The OWASP Top 10 for LLM Applications (2025)
- C. The NIST AI Risk Management Framework
- D. MITRE ATT&CK for Enterprise

**89.** [5.4] An attacker sends specially crafted, computationally expensive inputs designed to exhaust GPU resources and deny service. Which mitigation BEST improves resilience?

- A. Removing all input validation to speed processing
- B. Enforcing input size/complexity limits plus rate limiting and autoscaling caps
- C. Routing all traffic through a single inference node
- D. Disabling monitoring during peak load

**90.** [2.2] Users routinely accept a legal-research assistant's citations without verification and have filed briefs containing cases the model fabricated. Which risk does this BEST illustrate?

- A. Overreliance on AI-generated content
- B. Data poisoning of the training set
- C. Unsafe deserialization
- D. Membership inference
