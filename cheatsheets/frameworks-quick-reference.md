# Frameworks Quick Reference — AI Security Frameworks Cheat Sheet

> ⚠️ **UNOFFICIAL / COMMUNITY-MAINTAINED** study aid — not affiliated with or endorsed by CompTIA or any standards body. No fabricated IDs, clause numbers, or stats; version-sensitive items flagged **(verify)**. Blueprint: [`../exam-objectives.md`](../exam-objectives.md). Deeper detail: [`../study-guide/frameworks-crosswalk.md`](../study-guide/frameworks-crosswalk.md).

---

## OWASP Top 10 for LLM Applications (2025)

| ID | Name | One-line | One defense |
|---|---|---|---|
| **LLM01** | Prompt Injection | Direct or indirect input overrides intended instructions. | Instruction/data separation, guardrails, least-privilege tools. |
| **LLM02** | Sensitive Information Disclosure | Model reveals PII/secrets/proprietary data via output/memorization. | Data minimization, output redaction (DLP), retrieval access control. |
| **LLM03** | Supply Chain | Poisoned/tampered/typosquatted models, datasets, plugins, deps. | Provenance & signature verification, MLBOM/SBOM, scanning. |
| **LLM04** | Data and Model Poisoning | Tainted training/fine-tuning/embedding data → backdoors, bias. | Data provenance/validation, anomaly detection, trusted pipelines. |
| **LLM05** | Improper Output Handling | Downstream trusts output → XSS/SQLi/SSRF/RCE. | Treat output as untrusted; encode/validate; parameterize; sandbox. |
| **LLM06** | Excessive Agency | Too much permission/autonomy → harmful agent actions. | Least privilege, tool allow-listing, scoped identity, human gates. |
| **LLM07** | System Prompt Leakage | System prompt (secrets/guardrail logic) exposed, aids bypass. | No secrets in prompts; enforce controls server-side. |
| **LLM08** | Vector and Embedding Weaknesses | RAG flaws — poisoning, cross-tenant leakage, embedding inversion. | Per-doc/tenant retrieval authz, vet index, secure vector DB. |
| **LLM09** | Misinformation | False/hallucinated/misleading output users overrely on. | Grounding/RAG with trusted sources, citations, human review. |
| **LLM10** | Unbounded Consumption | Resource abuse — model DoS, "denial of wallet," cost harvesting. | Rate limits/quotas, size caps, cost monitoring, timeouts. |

---

## NIST AI RMF (AI 100-1) — four functions

| Function | Purpose (plain English) |
|---|---|
| **GOVERN** | Cross-cutting culture, policies, roles, risk tolerance, oversight, supply-chain governance. |
| **MAP** | Establish context — intended use, stakeholders, categorization, capabilities/limits, impacts. |
| **MEASURE** | Analyze/assess/benchmark/monitor — metrics, testing/red-teaming, trustworthiness characteristics. |
| **MANAGE** | Prioritize and act — risk treatment, response/recovery, incident handling, ongoing improvement. |

- **Voluntary** and **outcome-based** (not a mandatory control checklist).
- **Govern** is cross-cutting and wraps the other three.
- **NIST AI 600-1** = the **Generative AI Profile** (companion that applies the RMF to GenAI) — know it exists.

---

## EU AI Act — risk tiers + GPAI

| Tier | Meaning | Obligation level |
|---|---|---|
| **Prohibited / Unacceptable** | Banned practices (e.g., certain social scoring, manipulative/exploitative systems — *verify exact list*). | **Banned** |
| **High** | Sensitive domains (critical infra, employment, biometrics, essential services — *verify list*). | Strict: risk mgmt, data governance, technical docs, logging, human oversight, accuracy/robustness/cybersecurity, conformity assessment. |
| **Limited** | Transparency-concern systems (chatbots, deepfakes/synthetic media). | **Transparency/disclosure** (tell users it's AI; label AI content). |
| **Minimal** | Most other AI (spam filters, AI in games). | No mandatory obligations; voluntary codes. |

- **GPAI (general-purpose AI):** baseline = technical docs, downstream info, EU copyright policy, training-data summary *(verify)*.
- **GPAI with systemic risk:** added duties — model evaluation/adversarial testing, systemic-risk assessment & mitigation, serious-incident reporting, cybersecurity *(verify thresholds)*.
- **Legally binding** (vs voluntary NIST AI RMF); extraterritorial reach; obligations phase in over time.

---

## ISO/IEC 42001:2023 — AIMS

- First international **management-system standard** for AI: establish/implement/maintain/improve an **AI Management System (AIMS)**; **certifiable** like ISO/IEC 27001.
- Follows the ISO **Harmonized Structure** and **PDCA (Plan-Do-Check-Act)** continual-improvement cycle.
- Annex-style controls by **theme** (AI policy, roles, **AI impact assessment**, data management, lifecycle/development, transparency, supplier relationships) — describe by theme, don't cite clause numbers unless verified.
- **42001 = AIMS** (AI) is the sibling of **27001 = ISMS** (information security); both share PDCA, risk treatment, internal audit, management review. Related: **23894** (AI risk mgmt guidance), **22989** (AI terminology) *(verify)*.

---

## MITRE ATLAS

- **ATLAS** = *Adversarial Threat Landscape for Artificial-Intelligence Systems* — a knowledge base of real-world adversary **tactics & techniques** against AI/ML, modeled on **MITRE ATT&CK** ("ATT&CK for AI"). Also publishes **case studies** and a **mitigations** catalog.
- Use for threat modeling, **ATLAS-mapped detections**, red/purple-team planning. Refer to techniques **by name**, not invented `AML.T####` IDs.

**Tactics (adversary goal at each stage):** Reconnaissance · Resource Development · Initial Access · ML Model Access · Execution · Persistence · Defense Evasion · Discovery · Collection · ML Attack Staging · Exfiltration · Impact.

---

## Documentation artifacts

| Artifact | Documents | Key contents |
|---|---|---|
| **Model card** | A single **model** | Intended use, performance metrics, limitations, ethical considerations. |
| **System card** | The end-to-end **system/product** | How components interact, system-level safety evaluations, mitigations. |
| **Datasheet** | A **dataset** | Provenance, composition, collection process, intended use, known bias. |

---

## Key defenses checklist for an LLM app

- [ ] Treat **all input and retrieved content as untrusted**; instruction/data separation (LLM01).
- [ ] **Input & output guardrails** — filtering, moderation, prompt-injection/jailbreak detection (LLM01/05/09).
- [ ] **Output is untrusted** — context-aware encode/escape, validate, parameterized queries, sandbox executed output (LLM05).
- [ ] **Least privilege + tool allow-listing**, scoped per-agent identity, human-in-the-loop for high-impact actions (LLM06).
- [ ] **No secrets in system prompts**; enforce controls server-side; assume the prompt leaks (LLM07).
- [ ] **Per-document/tenant retrieval authz**, vet & monitor indexed content, secure the vector DB (LLM02/08).
- [ ] **Supply-chain hygiene** — provenance, signing, MLBOM/SBOM, model/dependency scanning, safetensors over pickle (LLM03/04).
- [ ] **Rate limits, quotas, size caps, cost monitoring/alerting**, timeouts (LLM10).
- [ ] **Data minimization & sanitization**, PII redaction/DLP on training, RAG, and outputs (LLM02).
- [ ] **Prompt/tool-call logging & monitoring**; ATLAS-mapped detections; AI red-teaming & evals in CI/CD.

---

*Reconcile against official CompTIA SecAI+ objectives and primary sources before exam day. Items marked (verify) change between versions.*
