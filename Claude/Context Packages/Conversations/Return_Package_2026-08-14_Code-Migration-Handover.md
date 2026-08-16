# Return Package — 2026-08-14 · Code-Migration Handover (checker baseline green; operating surface → Claude Code)

> **DERIVED PROJECTION — conversation handover record (C-001).** Sources: Local Context v0.24; Decision Register v0.17 (unchanged); `verify.py` + `check_versions.py` runs of 2026-08-14 (both PASS).

**Parent:** Return_Package_2026-08-14_Spec-Version-Identity.md · **Local Context:** v0.23 → **v0.24**

---

## 1. Handover (C-059 auditable line)

**Previous package queued:** nothing (queue empty; G offers + H roadmap standing). **This conversation did:** an execution-only bridge close — ran both checkers against the live repo as a pre-migration baseline (both PASS), confirmed the operating surface moves from Cowork to **Claude Code working directly in the repo** (C-018 swappable-clients doctrine *exercised*, not amended — no new decision needed), and queued the first Code session's work list. Nothing was decided of record; no canonical content changed beyond this close's own projections.

## 2. Acts of record

- **Checker baseline (pre-migration, 2026-08-14):** `verify.py` **PASS** — 253 events · 60 entities · 19 codes · 7 roots · 36 route tokens · 0 collisions. `check_versions.py` **PASS** — 121 files scanned, 1085 version claims attributed (all attributable agree), 93 path references OK, 0 warnings; all living stamps current. No drift since the spec-version-identity close.
- **Operating surface: Cowork (device bridge) → Claude Code (in-repo).** Observed rationale, recorded per C-018's swappable-clients doctrine: the Cowork bridge **cannot delete files** (the open hygiene findings S2-6.2/S2-6.3 are un-executable from it — the `_to_delete/` convention exists *because* of this) and **has no network** (push always deferred to Max). Claude Code runs in the repo natively: delete, commit, and push are all first-class. Cowork remains an available surface; nothing binds to either client.
- **Deliberately not decided (Max's calls):** **OQ-10 left untouched** — the archive-move call is to be decided, executed, and recorded *in one pass* in the Code session (Max's stated inclination in this conversation: **go**; the call of record belongs to that session). **OQ-6** and **OQ-25** examined and deliberately kept open, unspent.
- **No protocol issued — recorded reason (C-059):** execution-only close; no decision of record. The first Code session issues the next protocol in the series, covering its own decided-and-executed batch.

## 3. Change summary (one `[GOV]` commit, Claude-authored per C-037; push = Max — the bridge has no network)

Local Context → **v0.24** · this Return Package (new) · Agenda Board regenerated file-first (stamp → v0.24) + Cowork artifact republished. **Nothing else touched:** Register v0.17, Rule Overview v0.15, Context Index v0.12, BOOTSTRAP v0.6, Architecture State v0.4, Schema v0.5 / Template v0.4, store (60 nodes / 253 events) — all unchanged. `check_versions.py` re-run green after the edits.

## 4. Refresh list

The C-059 checklist was walked — see Local Context v0.24 §Standing refresh items for every row's mark (only Local Context, the board, and this package changed; every other row **checked — unchanged**). Project mirror refreshed: Local Context. Register/Rule Overview/Index/Global mirrors untouched (their sources didn't change).

## 5. Unresolved / carried

- **Open findings (review ledger):** S2-6.2 / S2-6.3 — **now queued for execution** in the first Code session (previously "Max's manual hygiene"; the surface change makes them Claude-executable).
- **Standing OQs (unchanged):** OQ-4, OQ-6, OQ-9, OQ-10 (queued for the call of record), OQ-13, OQ-16, OQ-17, OQ-18, OQ-20, OQ-23, OQ-25, OQ-26, OQ-27.
- **Pending on Max:** review this close's commit and `git push` (the last bridge-era manual push, if the Code session takes over the ritual).
- **Standing note (carried):** the next Schema reissue documents the C-061 store treatment in the spec's own text (C-059 Schema→Template coupling rides along).

## 6. Next — queued: the first Claude Code session

1. **Open in the repo** (Claude Code, working directory `Desktop/FRACTAL/`); load Global Context + Local Context v0.24 + this package. BOOTSTRAP §2's client-adapter pattern applies to the new surface.
2. **Hygiene batch:** empty `_to_delete/` (S2-6.2) · delete the `~$*.docx` owner-files at the root (S2-6.3) → dispositions to **Fixed** in the Register's review-findings ledger.
3. **OQ-10 — the call of record** (inclination: go): if go, `git mv` the ChatGPT-era material into the archive subfolder, update the Context Index paths (*the one place paths are maintained*, per C-012/Index), and let `check_versions.py`'s path pass verify the sweep. C-029 pointer-only status and C-007 preservation are untouched by a move.
4. **Record and close:** issue the next Governance Protocol in the series (OQ-10 disposition + hygiene fixes + any push-ritual note), bump the Register, walk the full C-059 checklist, run both checkers, one commit per coherent change-set (C-037: author = actual author). **Push:** Code can push directly — per C-008 manual-first, confirm with Max before the first Claude-executed push, or record his standing authorization in that protocol.

---

*Author: Claude (AGENT.AI.CLAUDE) · Conversation surface: Cowork (device bridge) — the closing act of this surface as the default; frozen at issue (C-058-class handover record, not minted — C-042 mint-on-reuse).*
