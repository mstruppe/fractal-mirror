---
id: DOC-01KZVNA1710NXFC07PPK18X9C5
type: DOC
created: 2026-08-12T18:56:12Z
created_by: AGENT.AI.CLAUDE
content_hash: sha256:374896581097f6f014e159a7338c651f8f0b7d8ba630aa6e8d7f76a14cd7685f
title: "Facet Registry — C-026/C-027"
placements:
  - {facet: topic, code: KG,              role: about, weight: 1.0}
  - {facet: topic, code: GOV,             role: about, weight: 0.6}
  - {facet: agent, code: AGENT.AI.CLAUDE, role: by,    weight: 1.0}
  - {code: DOC-01KZVYPW5GQRZM0QV6450B8T3T, role: cites, weight: 1.0}
  - {code: DOC-01KZVYQQGGYJ0WZYZG3RY02W57, role: cites, weight: 1.0}
---

First real document placed in the FRACTAL Knowledge Graph store. Records the C-026/C-027
decision: the facet registry is the browsable, log-derived set of coordinate-concepts
(TOP nodes) grouped by facet; the agent facet is branched by kind at its root
(AGENT.HUMAN.* / AGENT.AI.*) so human vs AI is a one-grep prefix filter.

The `placements:` block above is a materialized fold of this document's `place` events in
_events/2026-08.jsonl — the log is canonical (C-024).
