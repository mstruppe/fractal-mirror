# Fractal Node Template

> **CANONICAL companion to `Fractal_Node_and_Event_Schema_v0.1.md` (Domain KG).** Copy-paste starting points for writing nodes and log lines by hand, at zero infrastructure. Comments explain each field; delete them in real nodes. This template is a derived convenience of the schema — the schema is the source of truth.

**Fractal_Node_Template** · **Version:** 0.1 · **Status:** Draft (Proposal) · **Updated:** 2026-08-07 · **Domain:** KG · **Author:** Claude · **Parent:** Fractal Node & Event Schema v0.1

> **SUPERSEDED (2026-08-12):** reissued as `Fractal_Node_Template_v0.2.md` (C-040, per Protocol v0.9). Retained as history under C-012 — its agent codes and ULID placeholders are invalid; never copy from this version.

---

## A. Entity node — blank template

Save as `<id>--<slug>.md`. Fill the four required identity fields; add placements as they become true.

```yaml
---
# ── Identity (immutable) ─────────────────────────────────────────
id:          TYPE-ULID              # e.g. DOC-01J9Z3K8QF7Q2A6M  (TYPE ∈ DOC NUM FN PER IMG TBL SET TOP)
type:        TYPE                   # must equal the id prefix
created:     2026-08-07T00:00:00Z   # ISO-8601 UTC
created_by:  AGENT.MAX              # agent-facet code

# ── Version / integrity (optional) ───────────────────────────────
content_hash: ~                     # sha256:… of this version's body; omit for TOP / pure identity
version_of:   ~                     # living id this file snapshots, if it is a frozen version

# ── Aliases (mutable, human-facing) ──────────────────────────────
title:   ""                         # human label — an alias, not identity
aliases: []                         # other labels / routing codes

# ── Placements — materialized fold of the log (log is canonical) ─
# one edge each:  this entity --role--> (facet, code) @ weight
placements: []                      # e.g. { facet: topic, code: PHY.QM.QFT, role: about, weight: 1.0 }
---

<!-- body: human content for DOC / TOP; may be empty for NUM, PER, IMG … -->
```

---

## B. Concept (TOP) node — a coordinate in a facet

A topic is just an Entity of type `TOP`. It is born with a `mint` event (§C) and carries its own facet + code.

```yaml
---
id:          TOP-01J9ZQFT4RK2N7QM
type:        TOP
created:     2026-08-07T14:00:00Z
created_by:  AGENT.MAX
title:       "Quantum Field Theory"    # display name — an alias; rename never touches placements
aliases:     ["route:QFT"]             # optional routing code, kind: route
code:        PHY.QM.QFT                # this concept's own coordinate (mirrors its `mint`)
                                       # parent = the code prefix PHY.QM — no separate edge
placements:  []                        # only CROSS-facet edges if any (e.g. by AGENT.MAX); parentage is the prefix
---

Scope note: what belongs under PHY.QM.QFT and what is merely adjacent.
```

---

## C. Event-log lines — worked example (the nuclear paper)

Append to `_events/2026-08.jsonl`, one object per line. This is the canonical record; the `placements:` blocks above are the fold of these lines. Below: mint two concepts, create the paper, place it in two facets at honest depth, then reclassify by superseding.

```jsonl
{"ev":"mint","id":"EVT-01J9ZQ0001","ts":"2026-08-07T14:00:00Z","actor":"AGENT.MAX","subject":"TOP-01J9ZQFT4RK2N7QM","facet":"topic","code":"PHY.QM.QFT","parent":"PHY.QM","label":"Quantum Field Theory"}
{"ev":"mint","id":"EVT-01J9ZQ0002","ts":"2026-08-07T14:01:00Z","actor":"AGENT.MAX","subject":"TOP-01J9ZQEN5ENERGY0","facet":"topic","code":"ECON.ENERGY","parent":"ECON","label":"Energy economics"}
{"ev":"create","id":"EVT-01J9ZQ0003","ts":"2026-08-07T14:32:00Z","actor":"AGENT.MAX","subject":"DOC-01J9Z3K8QF7Q2A6M","type":"DOC","content_hash":"sha256:9f2b…","title":"Neutron cross-section of U-235"}
{"ev":"place","id":"EVT-01J9ZQ0004","ts":"2026-08-07T14:32:05Z","actor":"AGENT.MAX","subject":"DOC-01J9Z3K8QF7Q2A6M","facet":"topic","code":"PHY.QM.QFT","role":"about","weight":1.0}
{"ev":"place","id":"EVT-01J9ZQ0005","ts":"2026-08-07T14:32:06Z","actor":"AGENT.MAX","subject":"DOC-01J9Z3K8QF7Q2A6M","facet":"topic","code":"ECON.ENERGY","role":"about","weight":0.4,"note":"peripheral — cost implications only"}
{"ev":"place","id":"EVT-01J9ZQ0006","ts":"2026-08-07T14:32:07Z","actor":"AGENT.MAX","subject":"DOC-01J9Z3K8QF7Q2A6M","facet":"source-type","code":"SRC.PAPER.PREPRINT","role":"is-a","weight":1.0}
{"ev":"place","id":"EVT-01J9ZQ0007","ts":"2026-08-07T14:32:08Z","actor":"AGENT.MAX","subject":"DOC-01J9Z3K8QF7Q2A6M","facet":"agent","code":"AGENT.MAX","role":"by","weight":1.0}
{"ev":"unplace","id":"EVT-01J9ZR0001","ts":"2026-08-09T09:00:00Z","actor":"AGENT.MAX","subject":"DOC-01J9Z3K8QF7Q2A6M","facet":"topic","code":"PHY.QM.QFT","role":"about","supersedes":"EVT-01J9ZQ0004","note":"wrong branch — nuclear, not QFT"}
{"ev":"place","id":"EVT-01J9ZR0002","ts":"2026-08-09T09:00:05Z","actor":"AGENT.MAX","subject":"DOC-01J9Z3K8QF7Q2A6M","facet":"topic","code":"PHY.NUC.FISSION","role":"about","weight":1.0}
```

**Reading the fold:** after these lines the paper's current placements are `PHY.NUC.FISSION` (about, 1.0), `ECON.ENERGY` (about, 0.4), `SRC.PAPER.PREPRINT` (is-a, 1.0), `AGENT.MAX` (by, 1.0). The retracted `PHY.QM.QFT` edge stays in the log as history — nothing is lost. The materialized node front-matter for `DOC-01J9Z3K8QF7Q2A6M` would list exactly those four current edges.

**Tracing by reading, zero infra:**
- *Where does this paper sit?* → read its node's `placements:`, or `grep DOC-01J9Z3K8QF7Q2A6M _events/*.jsonl` and fold.
- *Everything under physics?* → prefix scan `PHY.` across node front-matter / the log.
- *Who authored it?* → the `by → AGENT.MAX` edge.
- *How was a derived number made?* → follow its `derived-from` edges (written by `run`) back to sources.

---

## D. Operator run — provenance in one line

```jsonl
{"ev":"run","id":"EVT-01J9ZS0001","ts":"2026-08-09T10:00:00Z","actor":"AGENT.CLAUDE","subject":"FN-01J9ZSOP4CROSSFIT","operator":"FN-01J9ZSOP4CROSSFIT","inputs":["NUM-01J9ZSIN0A","NUM-01J9ZSIN0B"],"outputs":["NUM-01J9ZSOUT01"],"note":"fit cross-section curve"}
```

The fold materializes `derived-from` edges on `NUM-01J9ZSOUT01` pointing at both inputs, so the output's node shows its full derivation and a backward trace reaches the sources.

---

**Sources:** Fractal Node & Event Schema v0.1; Fractal Knowledge Path Foundation v0.1.
**Revision history:** v0.1 (2026-08-07) initial templates + worked example.
