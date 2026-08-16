# Review — Stranger Test #1 (2026-08-17)

> **CANONICAL REVIEW (C-058 family — commissioned; the family's third execution shape: the simulated stranger run).** Commissioned by Max before the public flip: *"we lack the stranger test. let's simulate an onboarding, so we can review the process."* Frozen at issue; dispositions live in the Decision Register's review-findings ledger (`ST1-…` rows).

**Date:** 2026-08-17 · **Commissioned by:** Max (in-conversation, sixteenth Code session) · **Executed by:** Claude (governing surface) + one sandboxed simulation agent · **Author:** Claude · **Domain:** GOV · **Document ID:** DOC-01M06E63435V3BEPV4Y4E3BJ6D (minted at this close via `close.py --create`; stamped by the post-mint revise)

---

## 1 · Method

The first onboarding of the **public artifact by a stranger's hands** — every prior birth ran from the mother's tags; this one ran from the curated mirror tree the flip will actually publish.

- **The subject:** the mirror at tag `beta-0.3` (commit `c75c990`), cloned by the README quickstart line verbatim into an isolated sandbox, checked out at the newest tag (detached HEAD, as the quickstart instructs). One substitution, recorded honestly: the clone source was the local mirror repository rather than the still-private GitHub remote — byte-identical content, authentication being environmental rather than part of the test.
- **The stranger:** a scripted persona — *Jonas*, economics doctoral student, non-programmer but comfortable pasting terminal commands, project "CREDIT-CYCLES" (dissertation: literature notes, model drafts, data decisions).
- **The simulation:** a fresh agent session whose world was ONLY the clone (hard jurisdiction constraints; improvisation-on-ambiguity recorded as findings), playing the session side of `/welcome` → `/begin` → the interview → the real `genesis.py` birth → the newborn's first-session opening. In parallel, the governing surface audited the mirror tree mechanically (commands, tools, context packages, `verify.py` inside the store).
- **Boundary note:** the mirror's governance documents end at the beta-0.3 release boundary (no Agenda Board Format — C-104 postdates the tag). Release-lag by design; carried into the beta-0.4 delta rather than counted as a finding.

## 2 · Result

**The stranger path held end-to-end.** `/welcome` correctly identified the reference surface (C-091) and scripted first contact; the interview ran one question at a time per the Onboarding Protocol; the birth completed on the first `--write` (45 files, five root mints, staging self-cleaned); the midwife exited at the jurisdiction line without entering the child. Inside the newborn: `verify.py` **PASS** (23 events / 14 entities, 0 warnings) and `check_versions.py` **PASS at 0 errors with 104 upstream citations exempted** — the C-088 inherited-biography machinery proven in the field. The mother-side audit: all six commands shipped, all store tools present, the full public record travels, `verify.py` PASS in the mirror store (601/101, the beta-0.3-era counts).

**The green datum (ST1-7):** *no outside knowledge was needed at any step* — every question the simulation faced resolved from files inside the clone. The GENESIS §0 acceptance test held under stranger conditions against the public tree.

## 3 · Findings

| # | Finding | Severity |
|---|---|---|
| ST1-1 | **The interview's vision text is thrown away by the tool.** Onboarding §0/§1.1 promise the §1.1 answer *becomes* Global Context §1 ("nothing is asked twice, nothing is thrown away") — but `genesis.py` had no vision parameter; the newborn's Global/Local Contexts were placeholders, and jurisdiction (correctly) forbids the midwife patching the child post-birth. The script's central promise mechanically unfulfilled at the artifact everything orients from. | High |
| ST1-2 | **Project-name grammar undocumented.** `genesis.py` rejects hyphens (`NAME_RE`), so the literal ask "CREDIT-CYCLES" bounces REFUSED at dry-run; neither GENESIS §2 nor Onboarding §1.2 warned first. | Med |
| ST1-3 | **The human's email is collected, then persisted nowhere.** §1.3 delivers the email doctrine, but the tool took no address and nothing told the user to set the newborn's git config — their manual commits would carry the machine's default identity, the very mismatch the rule exists to prevent. | Med |
| ST1-4 | **The newborn's first close is hand-rolled.** Tier-0 ships no `/close` (by design); only `Conversations/README.md` plus GENESIS §3.8's three lines described a handover record — a stall risk with a weaker client. | Med |
| ST1-5 | **No default for the AI collaborator's name.** §1.3 mandates "their pick," but "defaults are fine" had no scripted fallback; the simulation improvised well (proposed *Minsky* from the project's domain). | Low |
| ST1-6 | **The secrets answer has no landing place.** A non-"none" answer to §1.6's credentials question had no documented destination in the newborn. | Low |
| ST1-7 | **Green datum:** self-containment held — no step required knowledge from outside the clone. Recorded as the acceptance test's stranger-conditions pass. | — |

An eighth observation (the store's `stats.py` vs the "seven tools" count) reduced on inspection to the already-ledgered **CAP1-PROD-3** (status recorded-deliberate since the first drone flight); the store README now names both `fieldnote.py` and `stats.py`'s convenience status in the same pass.

## 4 · Verdict

Jonas ends the day with a working, self-governing instance and knows his next step (real work, P-001, the first close — "the instance is real at its first close"). The single most valuable change — carrying the interview's answers into the newborn mechanically — plus the inline pre-answers were **executed as the generator-side cure slate the same session** (C-094: fixes land in the generator, never the field): `genesis.py` gained `--vision` / `--focus` / `--human-email` and the C-104 board rider; GENESIS reissued to v0.7 (clause current to C-105 — CAP1-PROD-1/PROD-2 cured in the same touch); the Onboarding Protocol reissued to v0.2 (findings 2–6 pre-answered inline); the rail gained the handover skeleton. Re-gated by two scratch births: full-flag (vision verbatim in Global §1, identity bound, board shipped, clause current, both checkers PASS) and flagless (placeholders and fallbacks intact, both checkers PASS).

---

*Frozen at issue. Sources: the simulation agent's transcript and friction log (sandbox `stranger-test/`, 2026-08-17); the mechanical audit commands of the same session; genesis.py / GENESIS.md / Fractal_Onboarding_Protocol.md at the states before and after the cure slate; the two gate births (`GateOne`, `GateTwo`). Dispositions: Decision Register, review-findings ledger.*
