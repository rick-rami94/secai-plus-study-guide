# SecAI+ — 4-Week Study Plan

*Unofficial / community plan. Adjust to your own pace and verify scope against the official CompTIA objectives — see [`../exam-objectives.md`](../exam-objectives.md).*

A balanced 4-week plan assuming ~1–1.5 hours/day on weekdays and a longer block on weekends. Front-loads the two heaviest domains (2.0 and 3.0). Flashcards are **daily throughout** — that's the spaced-repetition engine.

## Daily habit (all 4 weeks)
- 🗂️ **15–20 min Anki** every day ([flashcards](../flashcards/)). Filter by the domain you're currently studying.
- ✍️ Keep an "error log": every concept you miss, written in your own words.

---

## Week 1 — Foundations + start the heavy domain
**Goal:** vocabulary fluency and the threat landscape.

| Day | Focus |
|---|---|
| 1 | [`exam-objectives.md`](../exam-objectives.md) + [Domain 1](../study-guide/domain-1-foundations.md) §1.1–1.3 |
| 2 | [Domain 1](../study-guide/domain-1-foundations.md) §1.4–1.5; skim [frameworks crosswalk](../study-guide/frameworks-crosswalk.md) |
| 3 | [Domain 2](../study-guide/domain-2-threats-attacks.md) §2.1 adversarial ML (evasion/poisoning/inversion/extraction/membership inference) |
| 4 | [Domain 2](../study-guide/domain-2-threats-attacks.md) §2.2 LLM/GenAI attacks (prompt injection, output handling, excessive agency) |
| 5 | [Domain 2](../study-guide/domain-2-threats-attacks.md) §2.3–2.4 supply chain + agentic risks |
| 6 | [Domain 2](../study-guide/domain-2-threats-attacks.md) §2.5–2.6 data/privacy + OWASP/ATLAS mapping; [glossary](../study-guide/glossary.md) pass |
| 7 | **Review week 1.** Memorize OWASP LLM Top 10 (2025) cold. Drill Domain 1–2 flashcards. |

## Week 2 — Defenses + governance
**Goal:** "given attack X, what control stops it?" and the GRC frameworks.

| Day | Focus |
|---|---|
| 8 | [Domain 3](../study-guide/domain-3-securing-lifecycle.md) §3.1–3.2 data + training/dev security |
| 9 | [Domain 3](../study-guide/domain-3-securing-lifecycle.md) §3.3–3.4 deployment/inference + identity (AI gateway, guardrails, OBO, tool allow-listing) |
| 10 | [Domain 3](../study-guide/domain-3-securing-lifecycle.md) §3.5–3.7 RAG security, guardrails, red teaming/evals |
| 11 | [Domain 4](../study-guide/domain-4-governance-risk-compliance.md) §4.1–4.2 NIST AI RMF, ISO 42001, AI risk/impact assessment |
| 12 | [Domain 4](../study-guide/domain-4-governance-risk-compliance.md) §4.3–4.4 EU AI Act tiers, GDPR, ethics/fairness/bias |
| 13 | [Domain 4](../study-guide/domain-4-governance-risk-compliance.md) §4.5–4.6 vendor/supply-chain risk, policy/acceptable use, shadow AI |
| 14 | **Practice Test 1** (timed, closed-book). Score it; log every miss by domain. |

## Week 3 — SecOps/IR + first remediation pass
**Goal:** close gaps from Test 1 and finish the last domain.

| Day | Focus |
|---|---|
| 15 | Review **Test 1** explanations in full; re-study your two weakest domains |
| 16 | [Domain 5](../study-guide/domain-5-secops-incident-response.md) §5.1–5.2 logging/monitoring + detection |
| 17 | [Domain 5](../study-guide/domain-5-secops-incident-response.md) §5.3 AI-aware incident response (containment, kill switch, model rollback) |
| 18 | [Domain 5](../study-guide/domain-5-secops-incident-response.md) §5.4–5.5 resilience/recovery + vuln mgmt |
| 19 | **Practice Test 2** (timed). Score; compare domain breakdown to Test 1. |
| 20 | Review **Test 2** explanations; hammer flashcards on weak tags |
| 21 | [Cheat sheets](../cheatsheets/): memorize the attacks + frameworks quick references |

## Week 4 — Consolidate & exam-readiness
**Goal:** consistent ~83%+ and confidence.

| Day | Focus |
|---|---|
| 22 | Re-read [Domain 2](../study-guide/domain-2-threats-attacks.md) + [Domain 3](../study-guide/domain-3-securing-lifecycle.md) (the 46% of the exam) |
| 23 | **Practice Test 3** (timed). Score; you should be trending upward. |
| 24 | Review **Test 3** explanations; resolve every remaining error-log item |
| 25 | Frameworks day: NIST AI RMF functions, ISO 42001, EU AI Act tiers, OWASP LLM Top 10 — recall from memory |
| 26 | Re-attempt your **worst** earlier test; confirm you now clear ~83%+ |
| 27 | Light review only — [glossary](../study-guide/glossary.md) + [acronyms](../study-guide/acronyms.md) + cheat sheets. Don't cram new material. |
| 28 | **Rest / exam day.** Quick cheat-sheet skim, then go pass it. 🎯 |

---

### Readiness checklist before you book the exam
- [ ] I can recite the **OWASP LLM Top 10 (2025)** and give one defense for each.
- [ ] I can distinguish **model inversion vs membership inference vs model extraction**.
- [ ] I can distinguish **direct vs indirect prompt injection** and name a defense for each.
- [ ] I know the **NIST AI RMF** functions (Govern/Map/Measure/Manage) and what **ISO/IEC 42001** is.
- [ ] I can place a scenario in the correct **EU AI Act** risk tier.
- [ ] I can pick the right **containment** action for an AI incident (disable model/tool, revoke keys, rollback).
- [ ] I'm consistently scoring **≈ 83%+** across the practice tests.

*Reconcile scope with the official CompTIA SecAI+ objectives before exam day.*
