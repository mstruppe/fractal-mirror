# Return Package — 2026-08-13 — Event-Log Layout (OQ-3)

> **DERIVED PROJECTION — conversation hand-off record.** Historical artifact, dated filename (C-012). Domain: KG (with GOV consequences). Author: Claude. Sources: this conversation (2026-08-13); Governance Protocol — Claude Series v0.15; Decision Register v0.11.

---

## 1. What this conversation was

The first G-offer taken up from the post-F standing agenda: Max opened on "what's on the agenda?", picked **OQ-3** (event-log partition interval), and drove it to resolution in three moves — reasonable-volume question → *why partition at all?* → scalability probe — then ratified the execution ("yes"). The resolution was decided from real data, as Max had asked when parking the question: 159 events / 46 KB (~290 B/event) after the heaviest month the store will plausibly ever see by hand.

## 2. Decision made (ratified in-conversation per C-033, recorded in Protocol v0.15)

- **C-055** — **Event-log physical layout: one file, tripwire, roll-by-ceremony.** One append-only active partition (`_events/part-0001.jsonl`); advisory **50,000-events-per-file tripwire** in `verify.py` (WARN, never fatal); a new partition opens **only by the roll ceremony** — one recorded commit on *merged* state (the C-049 ceremony pattern); automatic per-writer rolling excluded (divergent boundaries across unmerged clones). Closed partitions immutable; readers partition-agnostic; any future bracket applies forward, **no migration ever**; routine rolls = the C-008 trigger to automate, decided then. **Resolves OQ-3**; monthly illustration retired unchosen.

Max's structuring calls (recorded in v0.15 §3): no standing brackets; an "obnoxiously high" cap; brackets later *only if necessary* — with the explicit offer to keep monthly had it been the leaner version for an unseen reason (it wasn't).

## 3. Worth remembering (method notes)

- **Eliminating the specification is a valid resolution shape for an OQ.** OQ-3 asked "which interval?"; the answer was "no interval" — the credo applied to the log's own physique.
- **Ceremony converts an unsafe mechanism into a safe one.** The writer-divergence objection to volume caps applies only to *automatic* rolling; a roll that is one recorded commit on merged state cannot diverge. (Claude's initial yearly-brackets proposal was friction-free but not minimal — Max's challenge found the leaner floor.)
- **A cap must live in a tool, not in prose:** the tripwire rides `verify.py`, which already runs at every C-037 boundary — noticed by ritual at zero added cost.

## 4. Changes to the canonical layer (the repo)

| Artifact | Change |
|---|---|
| Node & Event Schema | v0.4 → **v0.5** (new file; §4.1 physical layout rewritten; §6/§7 updated; DOC node re-pathed + revised). |
| Governance Protocol Claude v0.15 | **New** — records C-055; Ratified in-conversation. DOC-minted. |
| Decision Register | v0.10 → **v0.11** (C-055; OQ-3 resolved). |
| Rule Overview | v0.8 → **v0.9** (event-log row: one active file, tripwire, roll ceremony). |
| `mint.py` | Monthly bucket derivation → append to the single active partition (lexically last `_events/*.jsonl`). |
| `verify.py` | Per-file event counts + the 50,000-event advisory tripwire (WARN). |
| `_events/2026-08.jsonl` | **Renamed** `part-0001.jsonl` (git-tracked rename; log lines untouched). |
| Store README | Layout, rules-in-force (C-055), spec pointer → v0.5. |
| KG Store | **+7 events (166), +1 node (45):** 1 DOC mint (Protocol v0.15) with route alias + 2 placements; 3 living-doc revisions (Schema re-pathed, Register, Rule Overview). `verify.py` green. |
| Local Context (KG) | v0.15 → **v0.16** (OQ-3 leaves the G offers). |
| Agenda Board | Regenerated file-first (C-048), stamp v0.16; artifact republished. |

Commit (C-037, author Claude): one coherent change-set `[KG]`; `verify.py` green before the commit (C-050 duty).

## 5. Refresh list (project mirrors, per C-004)

Refreshed this conversation: `Fractal_Decision_Register.md`, `Fractal_Rule_Overview.md`, `Fractal_Local_Context_Knowledge_Graph.md`. The F-close pending item (v0.4 Custom-Instructions paste) was **observed done** in this session's project instructions — discharged.

## 6. Unresolved / carried

- Carried: OQ-4 (genuine transition — candidate observed: consolidation complete + architecture map live), OQ-18, OQ-21; C-038 acceptance test unexercised.
- **WS is the declared open part** — forge on observed need (Architecture State §4).
- The repo-resident **skill** (shipping tier 1) and the **KG index** (C-021 step 3, spec = `verify.py` invariants) stand as offers.

## 7. Next

**Nothing is force-queued.** Next conversation follows Max: **G** (OQ-4, OQ-21, C-038 test) or **H** (the build track: skill / index / interface). Open with Global + Local Context v0.16 + this package.
