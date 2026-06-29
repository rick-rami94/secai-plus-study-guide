# SecAI+ (CY0-001) — 4-Week Study Plan

*Unofficial study plan aligned to the official CompTIA SecAI+ CY0-001 V1 objectives. Adjust to your pace; verify scope against the official objectives. See [`../exam-objectives.md`](../exam-objectives.md).*

A balanced 4-week plan assuming ~1–1.5 hrs/day on weekdays and a longer weekend block. **Domain 2 is 40% of the exam, so it gets the most time.** Flashcards are **daily throughout** — that's the spaced-repetition engine.

## Daily habit (all 4 weeks)
- 🗂️ **15–20 min Anki** every day ([flashcards](../flashcards/)). Filter by the domain you're studying (e.g., `tag:Domain2`).
- ✍️ Keep an "error log": every concept you miss, in your own words.

---

## Week 1 — Foundations + into Securing AI
**Goal:** AI vocabulary fluency, data/lifecycle security, and the threat-modeling resources.

| Day | Focus |
|---|---|
| 1 | [`exam-objectives.md`](../exam-objectives.md) + [Domain 1](../study-guide/domain-1-ai-concepts.md) §1.1 (AI types, training, prompt engineering) |
| 2 | [Domain 1](../study-guide/domain-1-ai-concepts.md) §1.2 data security + §1.3 AI life cycle & human-centric design |
| 3 | [Domain 2](../study-guide/domain-2-securing-ai-systems.md) §2.1 threat-modeling resources (OWASP LLM/ML Top 10, MIT AI Risk Repository, MITRE ATLAS, CVE AI WG); skim [frameworks crosswalk](../study-guide/frameworks-crosswalk.md) |
| 4 | [Domain 2](../study-guide/domain-2-securing-ai-systems.md) §2.2 security controls (model/gateway guardrails, rate/token/modality limits) |
| 5 | [Domain 2](../study-guide/domain-2-securing-ai-systems.md) §2.3 access controls + §2.4 data security (encryption in transit/at rest/**in use**, data safety) |
| 6 | [Domain 2](../study-guide/domain-2-securing-ai-systems.md) §2.5 monitoring & auditing (prompt monitoring, log sanitization, AI cost monitoring, bias/hallucination auditing) |
| 7 | **Review week 1.** Memorize the OWASP LLM Top 10 (2025) and the §2.1 resources cold. Drill Domain 1–2 flashcards. |

## Week 2 — Attacks & compensating controls + AI-assisted security
**Goal:** master Domain 2.6 (the biggest single objective) and Domain 3.

| Day | Focus |
|---|---|
| 8 | [Domain 2](../study-guide/domain-2-securing-ai-systems.md) §2.6 attacks part 1 (backdoor, trojan, prompt injection, poisoning, jailbreaking, input manipulation, guardrail circumvention) |
| 9 | [Domain 2](../study-guide/domain-2-securing-ai-systems.md) §2.6 attacks part 2 (model inversion, model theft, membership inference, insecure output handling, model DoS, sensitive info disclosure, insecure plug-in, excessive agency, overreliance) + compensating controls |
| 10 | [Domain 3](../study-guide/domain-3-ai-assisted-security.md) §3.1 AI-enabled tools for security tasks (IDE/CLI/browser plug-ins, MCP server, automated pentest, anomaly detection) |
| 11 | [Domain 3](../study-guide/domain-3-ai-assisted-security.md) §3.2 how AI enables attacks (deepfakes, social engineering, automated attack generation) |
| 12 | [Domain 3](../study-guide/domain-3-ai-assisted-security.md) §3.3 automating security with AI (low/no-code, CI/CD, AI agents, IR ticketing) |
| 13 | [Cheat sheets](../cheatsheets/): drill the attacks + frameworks quick references |
| 14 | **Practice Test 1** (timed, 60 min, closed-book). Score it; log every miss by domain. |

## Week 3 — Governance/Risk/Compliance + remediation
**Goal:** finish Domain 4 and close Test 1 gaps.

| Day | Focus |
|---|---|
| 15 | Review **Test 1** explanations in full; re-study your two weakest domains |
| 16 | [Domain 4](../study-guide/domain-4-governance-risk-compliance.md) §4.1 governance structures & AI roles |
| 17 | [Domain 4](../study-guide/domain-4-governance-risk-compliance.md) §4.2 responsible AI & risks (bias, data leakage, shadow AI) |
| 18 | [Domain 4](../study-guide/domain-4-governance-risk-compliance.md) §4.3 compliance (EU AI Act tiers, OECD, ISO 42001/23894, NIST AIRMF, data sovereignty) |
| 19 | **Practice Test 2** (timed). Score; compare domain breakdown to Test 1 |
| 20 | Review **Test 2** explanations; hammer flashcards on weak tags |
| 21 | Re-read [Domain 2](../study-guide/domain-2-securing-ai-systems.md) end-to-end (it's 40% of the exam) |

## Week 4 — Consolidate & exam-readiness
**Goal:** consistent ~75%+ and confidence.

| Day | Focus |
|---|---|
| 22 | Frameworks day: OWASP LLM Top 10, MIT AI Risk Repository, MITRE ATLAS, NIST AIRMF (Govern/Map/Measure/Manage), EU AI Act tiers — recall from memory |
| 23 | **Practice Test 3** (timed). Score; you should be trending upward |
| 24 | Review **Test 3** explanations; resolve every remaining error-log item |
| 25 | Re-attempt your **worst** earlier test; confirm you now clear ~75%+ |
| 26 | [Glossary](../study-guide/glossary.md) + [acronyms](../study-guide/acronyms.md) + cheat-sheet review |
| 27 | Light review only — don't cram new material |
| 28 | **Rest / exam day.** Quick cheat-sheet skim, then go pass it. 🎯 |

---

### Readiness checklist before you book the exam
- [ ] I can name the **§2.1 threat-modeling resources** (OWASP LLM/ML Top 10, MIT AI Risk Repository, MITRE ATLAS, CVE AI Working Group) and what each is for.
- [ ] I can recite the **OWASP LLM Top 10 (2025)** and give one defense for each.
- [ ] For a **2.6 attack** (e.g., model inversion, membership inference, model theft, prompt injection), I can name the evidence and the **compensating control**.
- [ ] I can distinguish **model inversion vs membership inference vs model theft**, and **excessive agency vs overreliance**.
- [ ] I know the **encryption states** (in transit / at rest / **in use**) and the **data-safety** controls.
- [ ] I can explain how AI both **assists defenders** and **enables attackers** (Domain 3).
- [ ] I know **NIST AIRMF** (Govern/Map/Measure/Manage), **EU AI Act** tiers, and **shadow AI**.
- [ ] I'm consistently scoring **~75%+** across the practice tests.

*Reconcile scope with the official CompTIA SecAI+ CY0-001 objectives before exam day.*
