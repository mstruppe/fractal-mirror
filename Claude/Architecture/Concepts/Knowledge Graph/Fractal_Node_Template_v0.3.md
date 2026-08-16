# Fractal Node Template

> **CANONICAL companion to `Fractal_Node_and_Event_Schema_v0.3.md` (Domain KG).** Copy-paste starting points for writing nodes and log lines by hand, at zero infrastructure. Comments explain each field; delete them in real nodes. This template is a derived convenience of the schema — the schema is the source of truth.

**Fractal_Node_Template** · **Version:** 0.3 · **Status:** Ratified (2026-08-13, in-conversation per C-033) · **Updated:** 2026-08-13 · **Domain:** KG · **Author:** Claude · **Parent:** Fractal Node & Event Schema v0.3 · **Supersedes:** Fractal_Node_Template_v0.2.md

> **v0.3 additions (workstream D):** the reparent-by-redirect worked example (§E) — re-mint on the same subject + `alias` of `kind: redirect`, per C-045; alias kinds `label`/`route`/`redirect` noted where they appear; facet tokens now resolve to minted `FACET.*` concepts (C-043) — nothing changes in how you *write* a `facet:` field. Root codes are globally unique across facets (C-044): check existing roots (`grep '"parent": null' _events/*.jsonl`) before minting a new root.

---

## A. Entity node — blank template

Save as `<id>--<slug>.md`. Fill the four required identity fields; add placements as they become true.

```yaml
---
# ── Identity (immutable) ─────────────────────────────────────────
id:          TYPE-ULID              # e.g. DOC-01KZEA6NR0XPH7DXTGMSB9NF3E  (TYPE ∈ DOC NUM FN PER IMG TBL SET TOP EVT)
type:        TYPE                   # must equal the id prefix
created:     2026-08-07T00:00:00Z   # ISO-8601 UTC (the ULID's prefix must decode into this second)
created_by:  AGENT.HUMAN.MAX        # agent-facet code — always kind-branched: AGENT.HUMAN.* / AGENT.AI.*

# ── Version / integrity (optional) ───────────────────────────────
content_hash: ~                     # sha256:… per Schema §3.7 (body bytes after the closing ---); omit for TOP
version_of:   ~                     # living id this file snapshots, if it is a frozen version

# ── Aliases (mutable, human-facing) ──────────────────────────────
title:   ""                         # human label — the NEWEST label-kind alias (Schema §4.3), not identity
aliases: []                         # all bound labels / routing codes / redirects (fold of alias events)

# ── Placements — materialized fold of the log (log is canonical) ─
# one edge each:  this entity --role--> (facet, code) @ weight
# entity target (Schema §3.5): put the TYPE-ULID in code and omit facet
# codes are materialized at their CURRENT canonical form (redirects resolved, Schema §5.3 rule 6)
placements: []                      # e.g. { facet: topic, code: PHY.QM.QFT, role: about, weight: 1.0 }
                                    #      { code: DOC-01KZEA6NR0XPH7DXTGMSB9NF3E, role: cites, weight: 1.0 }
---

<!-- body: human content for DOC / TOP; may be empty for NUM, PER, IMG … -->
```

---

## B. Concept (TOP) node — a coordinate in a facet

A topic is just an Entity of type `TOP`. It is born with a `mint` event (§C) and carries its own facet + code (both mirror the `mint`; the log wins on disagreement). The facet token (`topic`, `agent`, …) itself resolves to a minted `FACET.*` concept (C-043).

```yaml
---
id:          TOP-01KZE8C2R0MK9JVYV67Z1YRHAT
type:        TOP
created:     2026-08-07T14:00:00Z
created_by:  AGENT.HUMAN.MAX
title:       "Quantum Field Theory"    # display name — newest label alias; rename never touches placements
aliases:     ["route:QFT"]             # optional routing code (kind: route); redirects appear as "redirect:OLD.CODE"
code:        PHY.QM.QFT                # this concept's own CURRENT coordinate (newest mint, Schema §5.3 rule 6)
facet:       topic                     # the facet the code lives in (mirrors its `mint`; token → FACET.TOPIC)
                                       # parent = the code prefix PHY.QM — no separate edge
placements:  []                        # only CROSS-facet edges if any (e.g. by AGENT.HUMAN.MAX); parentage is the prefix
---

Scope note: what belongs under PHY.QM.QFT and what is merely adjacent.
```

---

## C. Event-log lines — worked example (the nuclear paper)

Append to `_events/2026-08.jsonl`, one object per line. This is the canonical record; the `placements:` blocks above are the fold of these lines. Below: mint two concepts, create the paper, place it in two facets at honest depth, then reclassify by superseding. Every `id` is a real ULID whose prefix decodes into its `ts` second.

```jsonl
{"ev":"mint","id":"EVT-01KZE8C2R0NDHYXXVRX4ETGY2Q","ts":"2026-08-07T14:00:00Z","actor":"AGENT.HUMAN.MAX","subject":"TOP-01KZE8C2R0MK9JVYV67Z1YRHAT","facet":"topic","code":"PHY.QM.QFT","parent":"PHY.QM","label":"Quantum Field Theory"}
{"ev":"mint","id":"EVT-01KZE8DXB017MY637XKSNP3GW5","ts":"2026-08-07T14:01:00Z","actor":"AGENT.HUMAN.MAX","subject":"TOP-01KZE8DXB0TE68EC1TCHEM1X9R","facet":"topic","code":"ECON.ENERGY","parent":"ECON","label":"Energy economics"}
{"ev":"create","id":"EVT-01KZEA6NR0VF40EDHVSWT7F2TF","ts":"2026-08-07T14:32:00Z","actor":"AGENT.HUMAN.MAX","subject":"DOC-01KZEA6NR0XPH7DXTGMSB9NF3E","type":"DOC","content_hash":"sha256:9f2b…","title":"Neutron cross-section of U-235"}
{"ev":"place","id":"EVT-01KZEA6TM8TSRX5M2Q1037NNGM","ts":"2026-08-07T14:32:05Z","actor":"AGENT.HUMAN.MAX","subject":"DOC-01KZEA6NR0XPH7DXTGMSB9NF3E","facet":"topic","code":"PHY.QM.QFT","role":"about","weight":1.0}
{"ev":"place","id":"EVT-01KZEA6VKG4VQ2KFEKM8W0ZJEP","ts":"2026-08-07T14:32:06Z","actor":"AGENT.HUMAN.MAX","subject":"DOC-01KZEA6NR0XPH7DXTGMSB9NF3E","facet":"topic","code":"ECON.ENERGY","role":"about","weight":0.4,"note":"peripheral — cost implications only"}
{"ev":"place","id":"EVT-01KZEA6WJR5066JHEVSD0GDHVV","ts":"2026-08-07T14:32:07Z","actor":"AGENT.HUMAN.MAX","subject":"DOC-01KZEA6NR0XPH7DXTGMSB9NF3E","facet":"source-type","code":"SRC.PAPER.PREPRINT","role":"is-a","weight":1.0}
{"ev":"place","id":"EVT-01KZEA6XJ0YY1V4TJDYQSV273K","ts":"2026-08-07T14:32:08Z","actor":"AGENT.HUMAN.MAX","subject":"DOC-01KZEA6NR0XPH7DXTGMSB9NF3E","facet":"agent","code":"AGENT.HUMAN.MAX","role":"by","weight":1.0}
{"ev":"mint","id":"EVT-01KZJVYC108VWEWAFRW4CR3RJW","ts":"2026-08-09T08:59:00Z","actor":"AGENT.HUMAN.MAX","subject":"TOP-01KZJVYC10JHB8270PJD9VSPSE","facet":"topic","code":"PHY.NUC.FISSION","parent":"PHY.NUC","label":"Nuclear fission"}
{"ev":"unplace","id":"EVT-01KZJW06M0GY3GPVQYR66VCD25","ts":"2026-08-09T09:00:00Z","actor":"AGENT.HUMAN.MAX","subject":"DOC-01KZEA6NR0XPH7DXTGMSB9NF3E","facet":"topic","code":"PHY.QM.QFT","role":"about","supersedes":"EVT-01KZEA6TM8TSRX5M2Q1037NNGM","note":"wrong branch — nuclear, not QFT"}
{"ev":"place","id":"EVT-01KZJW0BG83QTQYNYGDYXXSP25","ts":"2026-08-09T09:00:05Z","actor":"AGENT.HUMAN.MAX","subject":"DOC-01KZEA6NR0XPH7DXTGMSB9NF3E","facet":"topic","code":"PHY.NUC.FISSION","role":"about","weight":1.0}
```

**Reading the fold:** after these lines the paper's current placements are `PHY.NUC.FISSION` (about, 1.0), `ECON.ENERGY` (about, 0.4), `SRC.PAPER.PREPRINT` (is-a, 1.0), `AGENT.HUMAN.MAX` (by, 1.0). The retracted `PHY.QM.QFT` edge stays in the log as history — nothing is lost. The materialized node front-matter for `DOC-01KZEA6NR0XPH7DXTGMSB9NF3E` would list exactly those four current edges. *(Note the mint-before-use line for `PHY.NUC.FISSION` — v0.1's example placed against it unminted.)*

**Tracing by reading, zero infra:**
- *Where does this paper sit?* → read its node's `placements:`, or `grep DOC-01KZEA6NR0XPH7DXTGMSB9NF3E _events/*.jsonl` and fold.
- *Everything under physics?* → prefix scan `PHY.` across node front-matter / the log — after checking the redirect list (§E) if concepts have moved.
- *Who authored it?* → the `by → AGENT.HUMAN.MAX` edge.
- *How was a derived number made?* → follow its `derived-from` edges (written by `run`) back to sources.

---

## D. Operator run — provenance in one line

```jsonl
{"ev":"run","id":"EVT-01KZJZE2803M5ENPW7KD7F4430","ts":"2026-08-09T10:00:00Z","actor":"AGENT.AI.CLAUDE","subject":"FN-01KZJZ4X90D1RZAES697N522A5","operator":"FN-01KZJZ4X90D1RZAES697N522A5","inputs":["NUM-01KZJYVRA0A2DH8TGCCMXFG1J7","NUM-01KZJYVS982278X51ZD5269YRW"],"outputs":["NUM-01KZJZE2804T00X7DV2BMBJ22C"],"note":"fit cross-section curve"}
```

The fold materializes `derived-from` edges on `NUM-01KZJZE2804T00X7DV2BMBJ22C` pointing at both inputs (entity targets, Schema §3.5), so the output's node shows its full derivation and a backward trace reaches the sources.

---

## E. Reparent by redirect — worked example (C-045, Schema §5.3 rule 6)

Suppose `PHY.QM.QFT` was the wrong branch: QFT belongs under a (minted) `PHY.FIELD`. A reparent is **two lines in one commit** — a `mint` on the **same subject** (the new code is parent-validated and uniqueness-checked like any other), plus an explicit `redirect` alias on the old code:

```jsonl
{"ev":"mint","id":"EVT-01KZKA8Q20W6QN3M0V64K7T9XE","ts":"2026-08-09T15:30:00Z","actor":"AGENT.HUMAN.MAX","subject":"TOP-01KZE8C2R0MK9JVYV67Z1YRHAT","facet":"topic","code":"PHY.FIELD.QFT","parent":"PHY.FIELD","label":"Quantum Field Theory","note":"reparent from PHY.QM.QFT (C-045)"}
{"ev":"alias","id":"EVT-01KZKA8R1GJ4X2C8ZD5B0N7HMV","ts":"2026-08-09T15:30:01Z","actor":"AGENT.HUMAN.MAX","subject":"TOP-01KZE8C2R0MK9JVYV67Z1YRHAT","alias":"PHY.QM.QFT","kind":"redirect","note":"superseded code; resolves to this subject forever"}
```

**What changes and what doesn't:** zero log events are edited or re-placed — every historical line naming `PHY.QM.QFT` stays valid. The **fold resolves through the redirect**: the concept's node now reads `code: PHY.FIELD.QFT` with `aliases: ["redirect:PHY.QM.QFT"]`, and any *other* node whose materialized `placements:` named the old code is regenerated at the canonical code on its next refold. A prefix scan under `PHY.FIELD.` finds the concept and its placements in materialized state; a reader who greps the raw log for the old code finds the redirect alias in the same grep. Chains (a second reparent) are walked hop by hop — each hop is one `redirect` line.

---

**Sources:** Fractal Node & Event Schema v0.3; Fractal Knowledge Path Foundation v0.1.
**Revision history:** v0.1 (2026-08-07) initial templates + worked example. · v0.2 (2026-08-12) agent codes kind-branched per C-026; valid coherent ULIDs throughout; `EVT` in the TYPE list; `facet:` in the TOP example; entity-target placement syntax (C-040/C-041, per Protocol v0.9). · v0.3 (2026-08-13) reparent-by-redirect worked example (§E, C-045); alias-kind annotations (label/route/redirect); facet-token and global-root notes (C-043/C-044, per Protocol v0.10).
