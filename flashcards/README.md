# SecAI+ Flashcards (Unofficial / Community)

> Community-built Anki deck for the **unofficial** "CompTIA SecAI+" AI-security study repo. Not affiliated with, endorsed by, or sourced from CompTIA. Aligned to the community blueprint in [`../exam-objectives.md`](../exam-objectives.md).

## What's in the deck

`secai-plus-flashcards.tsv` contains **222 cards** spanning all five domains, weighted to mirror the community exam estimate:

| Domain | Topic | Cards |
|---|---|:---:|
| 1 | AI & Security Foundations | 36 |
| 2 | AI Threats, Attacks & Vulnerabilities | 56 |
| 3 | Securing the AI/ML Lifecycle | 50 |
| 4 | AI Governance, Risk & Compliance | 40 |
| 5 | AI Security Operations & Incident Response | 40 |
| | **Total** | **222** |

The mix includes definition cards, attack-to-defense cards, "which-framework" cards, and compare/contrast cards covering the OWASP LLM Top 10 (2025), NIST AI RMF, MITRE ATLAS, ISO/IEC 42001, EU AI Act, GDPR, and more.

### File format

Tab-separated, **3 columns, no header row**: `Front` (TAB) `Back` (TAB) `Tags`. Each card is one line. Line breaks inside a field (rare) use the HTML `<br>` tag.

### Tagging

Every card carries `SecAIplus` plus its domain tag (`Domain1`–`Domain5`), and most add topic tags such as `OWASP`, `LLM01`, `PromptInjection`, `NISTAIRMF`, `EUAIAct`, `RAG`, `Agents`, or `Defense`. Example: `SecAIplus Domain2 PromptInjection OWASP LLM01`.

## Import into Anki (desktop)

1. Open **Anki desktop**.
2. (Optional) Create or select a target deck first, e.g. "SecAI+".
3. **File -> Import** and select `secai-plus-flashcards.tsv`.
4. In the import dialog set:
   - **Type / Note type:** Basic
   - **Field separator:** Tab
   - **Allow HTML in fields:** ON (so any `<br>` renders as a line break instead of literal text)
5. **Map the fields:** Field 1 -> **Front**, Field 2 -> **Back**, Field 3 -> **Tags**.
6. Click **Import**.

## Study by domain using tags

After import, use Anki's Browser/search to drill into a domain or topic:

- `tag:Domain2` — only Domain 2 (Threats & Attacks) cards
- `tag:Domain3 tag:Defense` — Domain 3 defensive-control cards
- `tag:OWASP` — every OWASP LLM Top 10 card
- `deck:SecAI+ tag:Domain5` — Domain 5 within your chosen deck

You can also create Filtered Decks from any of these searches for focused cramming.

## Mobile / sync

Sign in to **AnkiWeb** (free) in Anki desktop and click **Sync**. Your deck then syncs to **AnkiMobile** (iOS) or **AnkiDroid** (Android) so you can review cards on your phone.

## Verify before relying on this

This is **community-maintained study content**, not official CompTIA material, and may contain errors or drift from the real exam. Reconcile against the official CompTIA SecAI+ objectives and authoritative primary sources (OWASP, NIST, MITRE, ISO, the EU AI Act text) before exam day. Where they differ, the official sources win.

---

## Optional: build a one-click `.apkg`

The TSV imports directly, but if you prefer a single double-click deck file:

```bash
pip install genanki
python build_apkg.py      # -> secai-plus.apkg
```

Then in Anki: **File → Import → `secai-plus.apkg`** (or just double-click it). Re-running updates the same deck instead of duplicating.
