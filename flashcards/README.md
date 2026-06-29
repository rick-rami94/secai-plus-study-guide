# SecAI+ Flashcards (Unofficial / Community)

> Unofficial study material aligned to CompTIA SecAI+ CY0-001 V1 objectives. See [../exam-objectives.md](../exam-objectives.md).

Not affiliated with, authorized by, or endorsed by CompTIA. Contains no official or actual exam questions.

## What's in the deck

`secai-plus-flashcards.tsv` contains **213 cards** spanning the **four official domains**, weighted to mirror the official exam blueprint (Domain 2 dominates at 40%):

| Domain | Title | Weight | Cards |
|---|---|:---:|:---:|
| 1 | Basic AI Concepts Related to Cybersecurity | 17% | 35 |
| 2 | Securing AI Systems | 40% | 84 |
| 3 | AI-assisted Security | 24% | 50 |
| 4 | AI Governance, Risk, and Compliance | 19% | 44 |
| | **Total** | **100%** | **213** |

The mix includes definition cards, attack-to-compensating-control cards, "which resource/framework" cards, and compare/contrast cards. Content tracks the official sub-bullets, covering items such as data lineage vs. provenance, epoch/pruning/quantization, federated learning, GANs, SLM vs. LLM, zero/one/multi-shot prompting, watermarking, RAG (embeddings and vector storage), the OWASP LLM Top 10 (2025) and ML Security Top 10, MIT AI Risk Repository, MITRE ATLAS, the CVE AI Working Group, gateway and model controls, access and data-security controls, monitoring/auditing, the full Domain 2 attack list with compensating controls, MCP servers and AI agents, deepfakes/misinformation/disinformation, CI/CD, the AI Center of Excellence and AI roles, responsible-AI principles, differential privacy, explainability, shadow AI, the EU AI Act, OECD, ISO/IEC 42001 and 23894, the NIST AI RMF (Govern/Map/Measure/Manage), and data sovereignty.

### File format

Tab-separated, **exactly 3 columns, no header row**: `Front` (TAB) `Back` (TAB) `Tags`. One card per line. Any rare in-field line break uses the HTML `<br>` tag (none are currently used).

### Tagging

Every card carries `SecAIplus`, its domain tag (`Domain1`–`Domain4`), and a topic tag. **Only Domain1–Domain4 are used** (the exam has four domains). Example: `SecAIplus Domain2 ModelInversion`.

## Import into Anki (desktop)

1. Open **Anki desktop**. (Optional) create/select a target deck first, e.g. "SecAI+".
2. **File → Import** and select `secai-plus-flashcards.tsv`.
3. In the import dialog set:
   - **Note type / Type:** Basic
   - **Field separator:** Tab
   - **Allow HTML in fields:** ON
4. **Map the fields:** Field 1 → **Front**, Field 2 → **Back**, Field 3 → **Tags**.
5. Click **Import**.

## Study by tag

After import, use Anki's Browser/search to drill into a domain or topic:

- `tag:Domain2` — only Domain 2 (Securing AI Systems) cards — the 40% domain, study these most
- `tag:Domain2 tag:ModelInversion` — a specific topic within a domain
- `tag:Defense` — compensating-control cards
- `tag:OWASPLLM` — OWASP LLM Top 10 cards
- `tag:NISTAIRMF` — NIST AI RMF cards

You can also create Filtered Decks from any of these searches for focused cramming.

## Mobile / sync

Sign in to **AnkiWeb** (free) in Anki desktop and click **Sync**. Your deck then syncs to **AnkiMobile** (iOS) or **AnkiDroid** (Android).

## Optional: build a one-click `.apkg`

The TSV imports directly, but if you prefer a single double-click deck file, the optional `build_apkg.py` script can package it:

```bash
pip install genanki
python build_apkg.py      # -> secai-plus.apkg
```

Then in Anki: **File → Import → `secai-plus.apkg`** (or double-click it). Re-running updates the same deck instead of duplicating.

## Verify before relying on this

This is **community-maintained study content**, not official CompTIA material, and may contain errors or drift from the real exam. Reconcile against the official CompTIA SecAI+ CY0-001 objectives and authoritative primary sources (OWASP, NIST, MITRE, ISO, the EU AI Act text) before exam day. Where they differ, the official sources win.
