# SecAI+ Glossary (Unofficial / Community-Maintained)

> Unofficial study aid — not affiliated with or endorsed by CompTIA. Align terms with the [exam blueprint](../exam-objectives.md).

---

## A

**Adversarial example** — An input crafted with small, often human-imperceptible perturbations that causes a model to make a wrong prediction; the core of an evasion attack. (see also: Evasion attack, Perturbation)

**Adversarial machine learning (AML)** — The study of attacks against ML systems and the defenses against them, spanning evasion, poisoning, inference, and extraction.

**Agent (AI agent)** — An LLM-driven system that plans and takes actions toward a goal by invoking tools, calling APIs, or running code, often across multiple steps with memory. (see also: Tool use, Excessive agency, MCP)

**Agentic AI** — AI systems that act autonomously over multiple steps, making decisions and using tools with limited human intervention; expands the attack surface and impact speed.

**AI gateway** — A control/proxy layer between applications and models that enforces authentication, rate limiting, guardrails, logging, and policy for AI traffic. (see also: Guardrails, Rate limiting)

**AI impact assessment** — A structured evaluation of an AI system's potential effects on individuals, groups, and society (rights, safety, fairness) used to identify and mitigate risk. (see also: NIST AI RMF, EU AI Act)

**AI Management System (AIMS)** — The set of policies, processes, and controls for governing AI responsibly across its lifecycle; formalized by ISO/IEC 42001. (see also: ISO/IEC 42001)

**AI Risk Management Framework (AI RMF)** — NIST's voluntary framework for managing AI risks, organized around the functions Govern, Map, Measure, and Manage. (see also: NIST AI RMF)

**Alignment** — The degree to which a model's behavior matches intended human goals, values, and safety constraints. (see also: RLHF)

**Anomaly detection** — Identifying inputs, outputs, or behaviors that deviate from a learned baseline; used to flag prompt injection, abuse, or drift.

**Attention** — The transformer mechanism that weights the relevance of different tokens to one another, enabling context-aware processing. (see also: Transformer)

**Audit trail** — A tamper-evident record of prompts, responses, tool calls, and decisions used for accountability, investigation, and compliance.

## B

**Backdoor (trojan) attack** — A poisoning attack that implants a hidden trigger so the model behaves normally except when the attacker's specific input pattern is present, then misbehaves. (see also: Data poisoning, Trigger)

**Bias (ML)** — Systematic error in model outputs that unfairly favors or disadvantages groups, arising from data, labeling, algorithm design, or deployment context. (see also: Fairness)

**Benchmark** — A standardized dataset and task used to measure model capability, safety, or robustness; complements evals. (see also: Evals)

## C

**Canary token (honeytoken)** — A planted, fake secret or unique marker that triggers an alert when accessed or exfiltrated, revealing a compromise or data leak. (see also: Honeytoken)

**CIA triad** — Confidentiality, Integrity, and Availability; the foundational security goals, extended for AI to include safety, privacy, and fairness.

**Confused deputy** — An attack where a privileged component (e.g., an agent) is tricked into misusing its authority on an attacker's behalf. (see also: Excessive agency, SSRF)

**Content filtering / moderation** — Classifiers or rules that block or flag harmful, unsafe, or policy-violating inputs and outputs. (see also: Guardrails)

**Context window** — The maximum number of tokens a model can consider at once (prompt plus generated output); exceeding it truncates or drops context.

**Continuous evaluation** — Running evals and safety regression tests on an ongoing basis (e.g., in CI/CD) to catch capability or safety drift after changes. (see also: Evals, Drift)

## D

**Data poisoning** — Corrupting training, fine-tuning, or RAG-index data so the model learns attacker-chosen behavior, degraded accuracy, or hidden backdoors. (see also: Backdoor attack)

**Data provenance / lineage** — Records of where data originated and how it was transformed through the pipeline, supporting trust, reproducibility, and poisoning defense. (see also: MLBOM)

**Datasheet (for datasets)** — Standardized documentation describing a dataset's motivation, composition, collection, and recommended uses and limitations. (see also: Model card)

**Deep learning** — ML using multi-layer neural networks to learn hierarchical representations from large data.

**Differential privacy (DP)** — A mathematical guarantee that adding calibrated noise limits how much any single individual's data influences an output, bounding privacy leakage. (see also: Membership inference)

**Drift** — Degradation in model performance over time as production data (data drift) or input-output relationships (concept drift) diverge from training conditions. (see also: Observability)

**Denial of Service (DoS) on AI** — Overwhelming an AI system with expensive or numerous requests to exhaust compute, budget, or availability. (see also: Unbounded consumption, Sponge attack)

## E

**Embedding** — A dense numeric vector representing the meaning of text, images, or other data so similar items lie close together in vector space. (see also: Vector, Vector database)

**Embedding inversion** — Reconstructing original input (e.g., sensitive text) from its embedding vector, a privacy risk in RAG and vector stores. (see also: Model inversion)

**Epoch** — One complete pass of the training algorithm over the entire training dataset; models typically train for many epochs.

**Evals (evaluations)** — Structured, repeatable tests measuring a model or AI application's quality, safety, and robustness against defined criteria. (see also: Benchmark, Red teaming)

**Evasion attack** — Manipulating an input at inference time to cause misclassification or to bypass a model-based control, without changing the model. (see also: Adversarial example)

**Excessive agency** — An OWASP LLM risk where an agent has too much functionality, permission, or autonomy, enabling harmful actions when manipulated. (see also: Agent, Tool allow-listing, OBO)

**Explainability (XAI)** — Techniques and properties that make a model's decisions understandable to humans, supporting trust, debugging, and accountability. (see also: Interpretability)

## F

**Fairness** — The principle and metrics ensuring an AI system does not produce unjustified disparate outcomes across protected groups. (see also: Bias)

**Feature store** — A managed repository of curated, reusable input features for training and serving, requiring access control and integrity protection.

**Few-shot prompting** — Providing a few examples in the prompt to steer the model's behavior without changing its weights. (see also: Prompting)

**Fine-tuning** — Further training a pretrained model on a narrower dataset to specialize its behavior; adjusts weights, unlike prompting. (see also: RLHF, Foundation model)

**Foundation model** — A large model pretrained on broad data that can be adapted (via prompting or fine-tuning) to many downstream tasks. (see also: LLM)

## G

**General-Purpose AI (GPAI)** — Under the EU AI Act, a model capable of many tasks across contexts; large GPAI models carry added transparency and systemic-risk obligations. (see also: EU AI Act)

**Generative AI (GenAI)** — Models that create new content (text, images, code, audio) rather than only classifying or predicting. (see also: LLM, Foundation model)

**Gradient** — The vector of partial derivatives of the loss with respect to model parameters; training follows gradients to reduce error. (see also: Gradient descent)

**Gradient descent** — The optimization method that iteratively updates weights in the direction that reduces the loss. (see also: Gradient)

**Graceful degradation** — Designing an AI service to fall back to a safe, reduced-capability mode rather than failing completely under attack or overload.

**Guardrails** — Input/output controls (filters, validators, classifiers, policies) that constrain model behavior and block unsafe or out-of-policy content. (see also: AI gateway, Output validation)

## H

**Hallucination** — Plausible-sounding but false or fabricated model output not grounded in the input or facts. (see also: Overreliance, RAG)

**Honeytoken** — A decoy credential or data item planted to detect unauthorized access or exfiltration. (see also: Canary token)

**Human-in-the-loop (HITL)** — Requiring human review or approval before an AI system takes high-impact or irreversible actions. (see also: Excessive agency)

**Hyperparameter** — A configuration value set before training (e.g., learning rate, batch size, number of epochs) that controls how a model learns.

## I

**Indirect prompt injection** — A prompt injection where malicious instructions are hidden in external content (web pages, documents, emails, RAG sources) that the model later processes. (see also: Prompt injection, RAG)

**Inference** — Running a trained model on new inputs to produce predictions or generations; the production-time operation. (see also: Training, Model serving)

**Insecure output handling** — Trusting LLM output and passing it unsanitized to downstream systems (browsers, shells, SQL), enabling XSS, injection, or RCE. (see also: Output validation)

**Interpretability** — The extent to which the internal mechanics of a model can be understood by humans. (see also: Explainability)

**ISO/IEC 42001** — The international standard specifying requirements for an AI Management System (AIMS) to govern AI responsibly. (see also: AIMS)

## J

**Jailbreak** — A prompt-based attack that bypasses a model's safety guardrails or alignment to elicit restricted behavior or content. (see also: Prompt injection)

**Just-in-time (JIT) access** — Granting elevated permissions only for the moment they are needed and revoking them afterward, reducing standing privilege for agents and operators.

## K

**Kill switch** — A mechanism to immediately disable a model, agent, or tool integration to contain an incident. (see also: Incident response, Model rollback)

## L

**Large Language Model (LLM)** — A transformer-based foundation model trained on vast text to predict tokens, enabling generation, reasoning, and tool use. (see also: Foundation model, Transformer)

**LLMOps** — Practices and tooling for deploying, monitoring, evaluating, and governing LLM applications in production. (see also: MLOps)

**Loss function** — A measure of how far model predictions are from desired outputs; training minimizes it. (see also: Gradient descent)

## M

**Membership inference attack** — Determining whether a specific record was part of a model's training set, a privacy breach. (see also: Differential privacy)

**Model card** — Standardized documentation of a model's intended use, performance, limitations, and ethical considerations. (see also: System card, Datasheet)

**Model context protocol (MCP)** — An open protocol standardizing how AI applications connect to external tools, data sources, and context via MCP servers. (see also: Agent, Tool use)

**Model extraction (model stealing)** — Querying a model to reconstruct an approximate copy of its parameters or behavior, stealing IP and enabling further attacks. (see also: Model inversion)

**Model inversion** — Reconstructing sensitive training inputs or attributes by exploiting a model's outputs. (see also: Membership inference, Embedding inversion)

**Model registry** — A versioned catalog of models with metadata, lineage, and stage controls; a supply-chain asset requiring integrity and access control.

**Model rollback** — Reverting to a previously known-good model version to recover from a compromised, poisoned, or regressed deployment. (see also: Kill switch)

**Model serving** — Hosting a model behind an endpoint to handle inference requests; a hardening and least-privilege target. (see also: Inference)

**Model signing** — Cryptographically signing model artifacts so consumers can verify integrity and provenance before loading. (see also: MLBOM, Safetensors)

**MLBOM (Machine Learning Bill of Materials)** — An inventory of a model's components — datasets, weights, dependencies, and lineage — supporting supply-chain transparency. (see also: SBOM, Model signing)

**MLOps** — Practices for building, deploying, monitoring, and governing ML systems reliably and reproducibly. (see also: LLMOps)

**MITRE ATLAS** — A knowledge base of adversary tactics and techniques against AI/ML systems, modeled after MITRE ATT&CK. (see also: ATT&CK)

## N

**Neural network** — A model of interconnected layers of weighted nodes ("neurons") that learns to map inputs to outputs. (see also: Deep learning)

**NIST AI RMF** — NIST's AI Risk Management Framework (Govern, Map, Measure, Manage) for identifying and managing AI risks; includes a Generative AI Profile (AI 600-1). (see also: AI RMF)

**Non-determinism** — The property that AI models can produce different outputs for the same input (e.g., due to sampling), complicating testing and detection. (see also: Temperature)

## O

**Observability** — Instrumentation and telemetry (logs, metrics, traces of prompts, responses, tool calls) that make AI system behavior visible for monitoring and IR. (see also: Drift)

**On-behalf-of (OBO)** — A delegation pattern where an AI service acts using the requesting user's identity and permissions, preserving least privilege and authorization. (see also: Excessive agency, RBAC)

**Output validation / encoding** — Treating model output as untrusted and validating, sanitizing, or encoding it before use downstream. (see also: Insecure output handling)

**Overfitting** — When a model memorizes training data and noise, performing well on training but poorly on new data; also raises memorization/privacy risk. (see also: Memorization)

**Overreliance** — Users or systems trusting AI output without verification, propagating hallucinations or errors into decisions. (see also: Hallucination, Human-in-the-loop)

## P

**Perturbation** — A small, deliberate modification to an input designed to fool a model while appearing benign. (see also: Adversarial example)

**PII (Personally Identifiable Information)** — Data that can identify an individual; a key target for leakage, redaction, and minimization controls. (see also: DLP, Differential privacy)

**Poisoning defense** — Controls such as data validation, provenance checks, anomaly detection, and trusted curation that reduce data-poisoning risk. (see also: Data poisoning)

**Prompt injection** — An attack that inserts malicious instructions into a model's input to override the developer's intended instructions; direct (in user input) or indirect (in external content). (see also: Indirect prompt injection, Jailbreak)

**Prompt hardening / templating** — Structuring system prompts and delimiting untrusted input to reduce susceptibility to injection. (see also: Prompt injection)

**Purple teaming** — Collaborative red- and blue-team exercises that test attacks and immediately improve detections and defenses. (see also: Red teaming)

## Q

**Quantization** — Reducing the numeric precision of model weights to shrink size and speed inference, with potential accuracy and integrity trade-offs.

**Quota** — A configured cap on requests, tokens, or spend per user/key/time window to bound consumption and cost. (see also: Rate limiting, Unbounded consumption)

## R

**Rate limiting** — Restricting the number of requests over time to prevent abuse, DoS, and runaway cost. (see also: Quota, Unbounded consumption)

**Red teaming (AI)** — Structured adversarial testing of AI systems to discover jailbreaks, harmful outputs, and vulnerabilities before attackers do. (see also: Evals, Purple teaming)

**Regurgitation (memorization)** — A model reproducing verbatim training data, risking leakage of secrets, PII, or copyrighted content. (see also: Training data extraction, Overfitting)

**Reinforcement learning (RL)** — Training where an agent learns by maximizing reward signals from interacting with an environment.

**Responsible AI** — Programs, principles, and governance ensuring AI is developed and used ethically, safely, fairly, and transparently. (see also: AI governance)

**Retrieval-Augmented Generation (RAG)** — Augmenting an LLM with documents retrieved from an external knowledge base (often a vector DB) at query time to ground responses. (see also: Vector database, Indirect prompt injection)

**RLHF (Reinforcement Learning from Human Feedback)** — Fine-tuning a model using human preference signals to better align outputs with desired behavior. (see also: Alignment, Fine-tuning)

## S

**Safetensors** — A safe model-serialization format that stores tensors without executable code, avoiding the arbitrary-code-execution risk of pickle. (see also: Unsafe deserialization)

**Sampling** — Selecting the next token probabilistically during generation; controlled by parameters like temperature and top-p. (see also: Temperature)

**SBOM (Software Bill of Materials)** — A formal inventory of software components and dependencies, supporting supply-chain transparency and vulnerability tracking. (see also: MLBOM)

**Secure by design / Secure AI** — Building security and safety into AI systems from inception rather than bolting it on later. (see also: Google SAIF)

**Sensitive information disclosure** — An OWASP LLM risk where a model reveals secrets, PII, or proprietary data through its outputs. (see also: PII, System prompt leakage)

**Shadow AI** — Unsanctioned use of AI tools or models by employees outside governance, creating data-leakage and compliance risk. (see also: DLP, AI usage policy)

**SIEM (Security Information and Event Management)** — A platform that aggregates and correlates logs and events for detection and investigation, including AI prompt/tool-call telemetry. (see also: SOAR)

**Sponge attack** — Crafting inputs that maximize a model's compute or energy use to degrade availability. (see also: DoS, Unbounded consumption)

**SSRF (Server-Side Request Forgery)** — Tricking a server (or AI agent with fetch tools) into making unintended requests to internal resources. (see also: Confused deputy, Excessive agency)

**Supervised learning** — Training on labeled examples to learn input-to-output mappings. (see also: Unsupervised learning)

**System card** — Documentation describing a deployed AI system (beyond a single model), including capabilities, safety evaluations, and limitations. (see also: Model card)

**System prompt** — The developer-provided instructions that set a model's role, rules, and constraints, prepended ahead of user input. (see also: System prompt leakage)

**System prompt leakage** — An OWASP LLM risk where the hidden system prompt (and any secrets in it) is exposed to users via crafted queries. (see also: Sensitive information disclosure)

## T

**Temperature** — A sampling parameter controlling output randomness; higher values increase diversity and variability, lower values increase determinism. (see also: Sampling, Non-determinism)

**Threat intelligence (AI)** — Curated information about AI-specific adversaries, techniques, and indicators used to inform detection and defense. (see also: IOC, TTP)

**Token** — The basic unit of text a model processes (a word, subword, or character chunk); usage and limits are measured in tokens. (see also: Context window)

**Tool allow-listing** — Restricting an agent to a vetted, minimal set of approved tools/actions to limit blast radius. (see also: Excessive agency, Least privilege)

**Tool use (function calling)** — An LLM invoking external functions, APIs, or tools to retrieve data or take actions. (see also: Agent, MCP)

**Training** — The process of optimizing model weights on data to minimize loss. (see also: Inference, Epoch, Fine-tuning)

**Training data extraction** — Attacks that recover specific examples from a model's training data, leaking PII or secrets. (see also: Regurgitation, Membership inference)

**Transferability** — The property that an adversarial example crafted against one model often fools other models, enabling black-box attacks. (see also: Adversarial example)

**Transformer** — The neural-network architecture, based on self-attention, underpinning modern LLMs and many GenAI models. (see also: Attention, LLM)

**TTP (Tactics, Techniques, and Procedures)** — The behavioral patterns of an adversary; mapped for AI via MITRE ATLAS. (see also: MITRE ATLAS)

## U

**Unbounded consumption** — An OWASP LLM risk where uncontrolled inference requests exhaust resources or budget (model DoS, cost harvesting). (see also: Rate limiting, Quota, DoS)

**Unsafe deserialization** — Loading untrusted serialized objects (e.g., Python pickle in model files) that can execute arbitrary code. (see also: Safetensors)

**Unsupervised learning** — Learning structure or patterns from unlabeled data (e.g., clustering, dimensionality reduction). (see also: Supervised learning)

## V

**Vector** — An ordered list of numbers; in AI usually an embedding representing data in a high-dimensional space. (see also: Embedding)

**Vector database** — A store optimized for similarity search over embedding vectors, central to RAG; requires access control and integrity protection. (see also: RAG, Embedding)

## W

**Weights (parameters)** — The learned numeric values inside a model that determine its behavior; protecting them guards IP and integrity. (see also: Model extraction, Model signing)

## X

**XAI (Explainable AI)** — The field and techniques for making AI decisions interpretable and justifiable to humans. (see also: Explainability)

## Z

**Zero-shot prompting** — Asking a model to perform a task with no in-context examples, relying on pretrained knowledge. (see also: Few-shot prompting)

**Zero trust (for AI)** — Applying "never trust, always verify" to AI components: authenticate every request, scope every permission, treat model output as untrusted. (see also: OBO, Output validation)
