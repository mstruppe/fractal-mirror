# Fractal Governance Protocol — Claude Series v0.33

**Topic:** The vision-whiteboard session (seventh Code session). Arc 2 **deferred and re-framed** by Max at open — it becomes the *shippable-beta test case*, not the immediate next step — and the session spent deliberately on clarification, strategy, and vision: the monetization/SWOT/landscape assessment (with a live web scan), the **network thesis** captured presentably from Max's notebook, the **public gate drafted** (`README.md` + the website), and three far-vision layers gathered with armed triggers (**profiles**, the **social extension**, **log-ins**). **No new C-decision** — the session decided artifact classes and agenda, not rules. **OQ-32 opened** (profiles & roles doctrine).
**Status:** Ratified (2026-08-15 — ratified in the conversation it records, per C-033) · **Date:** 2026-08-15 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.32

---

## 1. Context

The Arc1-Complete handover queued arc 2 as the head of the program. Max opened the seventh session by exercising C-031's primacy rule instead: *"I want to push arc 2 for later. We can use this as test case for the shippable beta version. For now I want to take a step back, and see what we have accomplished so far."* The session that followed was declared idea-gathering — *"I want to use this conversation just for clarifying, idea gathering, visions"* — and this protocol records its dispositions, because the agenda and the open-question ledger both changed even though no rule did.

## 2. Acts of the session

- **The kernel/instance question answered conceptually before any building:** Max asked whether working *inside* FRACTAL (his "hood open" picture) is a capability a shipped instance loses. Answer of record: the hood is never mechanically closed — no layer of an instance is locked (C-018 substrate); what closes is **jurisdiction**: inherited kernel documents have no amendment path in an instance (editing them is forking), and the learning loop (friction → kernel change) natively terminates in this repo either way. The arc-1 Lyra/Nova control already demonstrated the ship-to-ourselves feedback loop works.
- **Strategy laid out** (nothing decided): SWOT; the wheel verdict (the spokes exist — markdown+git, ADRs, event sourcing, adapter files, claim-units; the assembled vehicle does not); a monetization ladder (methodology → open-core, where **C-079's tiering is accidentally an open-core model** → compliance vertical → consulting); the three-layer pitch (warm start / audit-grade provenance / network scaling law).
- **The network thesis entered capture:** Max's notebook paragraph (superlinear scaling; the marginal-increment hypothesis; angle-dependent extraction at node faces) rewritten into presentable prose **with his permission**, the notebook cited as source and idea provenance (C-085 respected — the original wording lives only there). Live web scan grounded it: nanopublications, ORKG, and Discourse Graphs share the vision and share one failure mode — **extraction labor** — which FRACTAL uniquely answers (the increment as a byproduct of the governed session).
- **The public gate drafted:** `README.md` at the root (audience: the stranger at the repo gate) and the **website** — explanation + GENESIS-faithful setup guide, published as a private artifact (`claude.ai/code/artifact/d163f249-ec79-4d5f-84da-af31f9e43783`), design iterated to Max's direction (floating-in-space, minimal-luxury, the self-similar constellation kept). Browser-verified before each publish.
- **Four far-vision layers gathered, each entered as armed triggers, not machinery** (the corpus's standing anticipation mechanism): **profiles** (descriptive roles as folds of the log vs granted roles as placement events; the responsibility collapse — every non-owner authority traces to an owner grant — already latent in C-084/C-064); the **social extension** (public profiles as gates to knowledge worlds; reputation as a fold; selective disclosure native to the facet layer); **log-ins** (fires at the first FRACTAL-owned serving process or the first outside-custody reader grant; identity = profile key; nothing canonical holds a secret); and — arriving at the close's edge — **the economic layer** (*knowledge mining*: verifiable contribution as currency issuance; the oracle problem answered socially by rewarding **registration** rather than submission; strictly behind the social layer it monetizes — full assessment in the vision capture).
- **The open-items map drawn** for Max's "close all before shipping": 12 open rows split into three honest classes — items that close *by* shipping (OQ-4, OQ-28, OQ-29, S3-2.2), standing-by-design trigger rows (OQ-9, OQ-17, OQ-20, OQ-23, OQ-27, OQ-31), and a genuine pre-ship punch list (OQ-30; the C-081 inherited-biography question; OQ-16's vendor-held half as a posture call; OQ-18 bundled at the next Schema touch; plus the un-ledgered ship-boundary items: naming/trademark check, public flip vs curated mirror, branch protection's C-075 trigger).
- **`doctor.py` conceived** — a sixth-store-tool candidate and natural drone brief (the `close.py`/`genesis.py` class, gated per C-081/C-082): configures the deterministic (git identities per C-084, remote binding, `.allowed_signers` rebind), *reports* the privileged (device encryption, host 2FA — never performed). Design principle: **the doctor diagnoses by tier**. Sequenced deliberately *behind* OQ-30, which grew three clients in one session (broker keys, profile key material, login credentials).

## 3. Dispositions (Max's calls, asked and answered at close)

1. **Protocol:** this document — the light-protocol option.
2. **`README.md` = committed derived projection** (C-035 class): stamped, Index-routed, **not** DOC-minted — a display surface in the Agenda Board's class, machine-guarded by `check_versions.py`'s existing STRICT registry row.
3. **The site HTML is committed** (`Site/fractal-site.html`, new root folder): durability doctrine — the artifact URL stays the published face, the repo holds the source.
4. **OQ-32 opened** — profiles & roles doctrine (ledger row in the Register).
5. Standing from the session itself: the **vision capture** (`Claude/Context Packages/Conversations/Vision_2026-08-15_Network-Thesis.md`) is **pre-canon** (C-062 class applied at first contact), frozen at issue, never orientation-loaded; the arc-2 re-frame lands on the agenda.

## 4. Ratification record (2026-08-15, in-conversation per C-033)

The four dispositions above put to Max as explicit questions at close; all four answered with the recommended option. No new C-number: artifact-class calls and agenda changes execute existing decisions (C-012, C-020, C-035, C-048, C-056, C-062, C-078); nothing here binds future conduct beyond what those already bind. Register → v0.34 (OQ-32 entered; OQ-30 annotated). Rule Overview, Settings, Architecture State, BOOTSTRAP, both adapters: **unchanged** — no rule, no conduct, no architecture accepted, no surface doctrine touched (the C-077 walk: stamps current at Settings v0.6, content conformant).

## 11. Open Questions (TBD)

- **OQ-32 opened — profiles & roles doctrine.** A creator (AI or human) as a first-class node with two role categories: *descriptive* (author, committer — folds of the event log, never assigned fields) and *granted* (owner, co-owner, editor, reader — placement events, revocable, auditable). Carries the responsibility-collapse principle and the taxonomy-kernel/holders-instance split (a candidate eighth parameterized decision). Intersects OQ-27 (per-writer keys attach to profiles), OQ-30 (key hygiene), OQ-31 (the reader tier is the federation-facing role). Resolution wants arc 2's multi-writer reality; the full sketch lives in the vision capture.
- **OQ-30 annotated** — its scope grew three clients in one session: broker/market API keys (arc 2), profile key material (OQ-32), login credentials (the armed log-in trigger). It remains the recorded first decision of the next working session, now load-bearing under three future layers.
- **Recorded for the ship boundary, not yet ledgered:** naming/trademark check ("Fractal" is crowded), the public-flip-vs-curated-mirror decision (BOOTSTRAP §4 defers it to "when sharing becomes real"), branch protection's dormant trigger (C-075).

## Document identity

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.33 |
| Document Type | Governance Protocol (historical artifact, dated identity — C-012) |
| Version | v0.33 |
| Status | Ratified (2026-08-15, in-conversation per C-033) |
| Domain | GOV |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-15, this conversation) |
| Date | 2026-08-15 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.32 |
| Related Documents | Decision Register (stamp inside — OQ-32/OQ-30 rows); Local Context (stamp inside); Context Index (stamp inside); `README.md`; `Site/fractal-site.html`; `Claude/Context Packages/Conversations/Vision_2026-08-15_Network-Thesis.md` (pre-canon); `GENESIS.md` (stamp inside); Protocols v0.30 (C-078 program), v0.31 (arc 1), v0.32 (C-084/C-085) |
| Document ID | DOC-01M02QT9RKJWNWXHXAM7MQ4B72 (minted 2026-08-15 via `close.py --create`; stamped by the post-mint revise) |
