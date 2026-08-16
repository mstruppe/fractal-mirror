# Return Package — 2026-08-15 · Arc 1 complete (C-081–C-083; the genesis tool gated, an instance closed, OQ-16 resolved)

> **DERIVED PROJECTION — conversation handover record (C-001).** Sources: Local Context v0.46; Decision Register v0.32; Governance Protocol — Claude Series v0.31; Architecture State v0.12; `GENESIS.md` v0.2; `genesis.py`; `verify.py` + `check_versions.py` runs of this close (both PASS).

**Parent:** Return_Package_2026-08-15_Instantiation-Program.md · **Local Context:** v0.45 → **v0.46**

---

## 1. Handover (C-059 auditable line)

**Previous package queued:** *review `drone/genesis-tool` — read the hand-back, run the gate yourself inside a birthed instance, merge or send back, delete the branch per C-075; then the real acceptance test and OQ-16.* **This conversation did exactly that, in that order, and finished arc 1.** Sixth Code session; opened by `/fractal`; every decision Max's call, offered with a recommendation (C-031 held throughout).

## 2. Acts of record

- **The first act found the premise false.** The handover recorded flight 3 as *launched* — true — but the drone was **still flying**: zero commits, no hand-back, a live process whose log grew 75 KB in 20 seconds while being watched. Reviewing then would have been reviewing an empty branch. It landed mid-conversation.
- **The hand-back was honest; both failures were the governing surface's.** The drone could not commit — a linked worktree's index sits in the parent repo, outside its sandbox (**C-082**) — and could not pass a gate `GENESIS.md` §6 never asked for (**C-081**). It reported both verbatim rather than weakening the test.
- **C-081 — the gate, and the measurement.** `verify.py` alone gates a newborn. Reproducing the checker failure split 76 errors into **9 registry** + **67 inherited-biography citations**: kernel documents citing FRACTAL's own history, which *frozen* status does not exempt (rule B pierces frozen by design). **The kernel is not biography-free.** Both cures — an `INHERITED` source class, or stripping revision histories on copy — deliberately deferred on Max's call: a 27-file newborn has no drift to detect.
- **C-082 — flights run in a full clone**, never a linked worktree. Corollary: a hand-back is *verified*, never assumed. This is the **second consecutive flight** with a launch defect only inspection caught.
- **C-083 — OQ-16 resolved by subtraction.** The queued `SKILL.md` is **retired unbuilt**: it would place a second compressed projection of Conversation Settings beside `CLAUDE.md` on one surface — the drift class **C-067** closed, and what C-065's own header forbids. The skill tier had landed slice by slice without being named done. `genesis.py` now writes the adapter and a tier-0 `/orient`; `/close` stays tier-1 because it drives `close.py`.
- **The acceptance test — run twice, the second a control.** *Lyra* closed green and reported three gaps (no handover home, no adapter, a genesis commit authored by a dotted code). *Nova*, born after the fixes, closed green **creating no scaffolding by hand**. Fixing the generator and re-testing on a fresh instance is what makes it a control rather than a patch.
- **Currency cures.** Template → **v0.5**; `genesis.py`'s KERNEL tuple updated in the same pass — the version coupling firing on its first opportunity. **C-040's coupling amended:** the Schema→Template walk checks **pointers**, not only content. `Fractal_Conversation_Settings.md`'s stale *"grandfathered, C-012"* line cured as **C-080 execution remainder**. And the inheritance clause in both `GENESIS.md` and `genesis.py` extended **C-079 → C-083** — without it, every future instance would have inherited a constitution that stopped four decisions short.

## 3. Change summary

**New:** Protocol v0.31 (minted `DOC-01M02GB3Y3RMCWRZJDJGS0AVHQ`) · Node Template v0.5 (minted `DOC-01M02GC8TXFX4GM1Z5DVZEKRDX`, series pointer re-aimed per C-061) · `genesis.py` (fifth store tool, drone-authored) · this package. **Living docs:** Register → **v0.32** · Rule Overview → **v0.27** · Architecture State → **v0.12** · Context Index → **v0.22** · `GENESIS.md` → **v0.2** · Local Context → **v0.46** · BOOTSTRAP (§2.2 rewritten) · Board regenerated. **Store:** 79 → **81 nodes**, 407 → **425 events**. **Unchanged:** Global Context v0.3 (deliberately) · Conversation Settings v0.6 (edited, not versioned — C-080 remainder) · `CLAUDE.md` v0.4 · `AGENTS.md` v0.5 · Schema v0.6 · Navigation Contract v0.1.

## 4. Refresh list

The C-059 checklist was walked — see Local Context v0.46 §Standing refresh items. Three rows repay reading: the **Schema→Template coupling** fired on an *amended* trigger rather than a Schema reissue; **Conversation Settings** was edited without a version bump, with the reasoning recorded (a completed C-080 pass, not a new rule, so no adapter restamp cascade); and **Global Context stayed v0.3 deliberately** — FRACTAL has now birthed instances, but every one was a test of itself.

## 5. Unresolved / carried

- **Arc 2 is the queue's head** — the portfolio live tracker, the first instance of FRACTAL that is not a test of FRACTAL. Expect to open with **OQ-30** (secrets, before the first key exists); **OQ-29** (code as governed artifact) forged there; **OQ-4** expected to *resolve*; **Global §2 moves there**, not before.
- **OQ-28 carries two measurements, no verdict** — ~20,000 words of mandatory kernel prose (~100 minutes, ~30k tokens) and 67 inherited citations. Arc 2 turns measurements into a judgement. It remains the live risk of record.
- **OQ-16:** packaging half resolved (C-083); the **vendor-held half** passed to **OQ-9** — nothing repo-resident can write into a vendor's instructions field.
- **Open review finding:** one — **S3-2.2**, held open *deliberately*, grounds recorded: `Reviewed By: Max` cannot be supplied on Max's behalf, and reissuing two kernel specs for a header field adds weight exactly where OQ-28 says weight is the risk. Likely occasion: arc 2.
- **The inherited-biography question** (C-081) is left standing **without an OQ number**, deliberately — it belongs to the first instance whose corpus wants `check_versions.py`.
- **Pending on Max: nothing.** Branch protection stays dormant (C-075).

## 6. Next — open arc 2

Open with **`/fractal`** (loads Global + Local v0.46 + this package). The queue's head is **arc 2 — the portfolio live tracker**. Arc 1 proved the kernel can be *copied* and that the loop survives instantiation; arc 2 asks the harder question, which is whether the kernel is worth carrying for a project whose value is throughput rather than reasoning. That is OQ-28's real test, and the reason arc 2 was always the one that would move Global §2.

---

*Author: Claude (AGENT.AI.CLAUDE) · Conversation surface: Claude Code, in-repo — sixth session on the default surface, opened by `/fractal`, closed by `/close`; frozen at issue (C-058-class handover record, not minted — C-042 mint-on-reuse).*
