# Return Package — 2026-08-14 · Custody Close (committer pinned, signing verifiable, drill cadence set — C-074–C-076)

> **DERIVED PROJECTION — conversation handover record (C-001).** Sources: Local Context v0.38; Decision Register v0.25; Governance Protocol — Claude Series v0.28; `verify.py` + `check_versions.py` runs of this close (both PASS).

**Parent:** Return_Package_2026-08-14_Navigation-Close.md · **Local Context:** v0.37 → **v0.38**

---

## 1. Handover (C-059 auditable line)

**Previous package queued:** nothing — the G offers and H roadmap stood open. **This conversation did:** on Max's request, sorted the ten open OQs into a **robust working order** (work now · ride planned work · fire-on-trigger — only the first step scheduled, everything else attached to existing triggers); Max took the front-loaded custody cluster (**"ok let's do OQ27 to OQ25"**), requested the full option walkthrough, and made four explicit calls, executed as **C-074–C-076** (Protocol v0.28). Third session opened by `/fractal`; the C-031 discipline held.

## 2. Acts of record

- **C-074 — committer mechanical; signature = custody.** The committer field carries no governance meaning (attribution = author, C-037 extended; both flight patterns and the Code surface's Claude-author/Max-committer pattern conformant). Signing is **custody-scoped** — one key = Max's custody environment; a signature attests *where* a commit was created, never *which writer*. The **sign-without-verify gap cured**: `.allowed_signers` at the repo root (infrastructure, C-006 exception, not minted; three writer emails as principals over the one custody key), bound via repo-local `gpg.ssh.allowedSignersFile` — **the whole history verifies `G`**. **Per-writer keys armed:** trigger = the first writer operating outside Max's custody.
- **C-075 — drone-branch lifecycle (extends C-066).** `drone/<task>` branches deleted — local and remote — once the gated merge lands; executed on both flight branches (`drone/close-tool` local + origin, `drone/first-flight-stats` local); no `drone/*` outstanding. **GitHub `main` branch protection recorded as a standing recommendation, pending Max's vendor visit** (plan-dependent, account-holder-only, non-blocking).
- **C-076 — drill cadence (OQ-25 resolved).** The C-038 restore drill is a standing section of **every canonical Loose-Ends Scan** (next: Scan #3) + ad-hoc on any custody/host change. No calendar cadence — the trigger is owned by an existing checker-enforced ritual.
- **Ledger movement:** OQ-25 **resolved** (C-076) · OQ-26 **resolved** (calibration done; future rungs fire from named triggers) · OQ-27 **annotated, open** — remaining scope is the outside-custody world (per-writer keys, drone provenance, revocation).
- **Protocol v0.28 issued and DOC-minted.** Max's calls recorded verbatim in §5: *"Decision 1: option A · Decision 2: option A · Decision 3: Move 2 and delete after merge · Decision 4: Option A."*

## 3. Change summary (one `[GOV]` commit, Claude-authored per C-037; push = Claude, C-064)

**New:** Protocol v0.28 · `.allowed_signers` (infrastructure) · this package. **Living docs:** Register → **v0.25** · Rule Overview → **v0.23** · BOOTSTRAP → **v0.12** · Context Index → **v0.20** · Local Context → **v0.38** · board restamped (v0.38). **Mechanical:** repo config `gpg.ssh.allowedSignersFile` bound; history-wide signature verification confirmed `G`; both merged drone branches deleted (local + origin). **Store:** +10 events — the protocol DOC minted via `close.py --create` (create, route alias, two placements) + changed-doc revises (Register, Rule Overview, BOOTSTRAP, Index, the protocol's post-mint ID stamp) + one **stamp-correction revise** (the footer's first stamp carried the dry-run preview's id rather than the minted one — caught and cured in-close; a candidate `close.py` hardening: print the minted id explicitly on `--write --create`) — **75 nodes / 359 events**. **Unchanged:** Global Context v0.3, Architecture State v0.7, Schema v0.6 / Template v0.4 / Contract v0.1, Settings v0.6 (row walked — no conduct-touching decision), all three adapter stamps, store tools.

## 4. Refresh list

The C-059 checklist was walked — see Local Context v0.38 §Standing refresh items for every row's mark. Both checkers green before commit.

## 5. Unresolved / carried

- **Open review findings:** none — the ledger stays fully green.
- **Standing OQs:** OQ-4, OQ-9 (decide after ~2–3 `/close` exercises), OQ-13 (rides Scan #3), OQ-16 (rides the shipping tier), OQ-17, OQ-18 (rides the next Schema touch), OQ-20 (candidate first use: the index server's canonization), OQ-23, OQ-27 (outside-custody scope only).
- **Pending on Max (standing recommendation, non-blocking):** the GitHub `main` branch-protection visit (C-075).

## 6. Next — nothing queued

Open the next conversation with **`/fractal`** (loads Global + Local v0.38 + this package). The **G offers and H roadmap stand** (C-031: offers, never mandates). Of note: the **KG index server** remains the prime candidate for the next drone brief — spec complete, trigger sharpened, and the C-075 lifecycle now governs the flight branch. The robust-ordering proposal's remaining steps are all trigger-attached: OQ-9 after `/close` accumulates use, OQ-13 + the drill at Scan #3, OQ-18/OQ-20/OQ-4 riding the build track. **Scan #3 stays penciled** after the build track.

---

## Postscript (2026-08-14, same conversation) — the stamp slip cured at the source; branch protection goes dormant

Max: **"go ahead"** on the recorded tool finding, plus a vendor datum. **(1) `close.py --create` output hardened** (C-073 tool-evolution path, the v0.27 §2 governing-surface-cure precedent): the dry-run header now labels its ids **illustrative** (they are regenerated at `--write`), and a successful `--write --create` prints **`MINTED: <id>` as the last line, after the gates** — the exact trap that produced this close's stamp-correction revise, closed at the source. Scratch-tested on a full repo copy before landing (dry-run/write id divergence reproduced; `MINTED` line cross-checked against the scratch log's create event); one `[KG]` commit (`e5c132b`, verified `G`), push per C-064. Execution-only — the tool's behaviour is unchanged, only its output; no decision of record (C-059 recorded reason). **(2) The C-075 branch-protection recommendation checked by Max:** *"rulesets won't be enforced on this private repository until you move to GitHub Team organization account"* — the recommendation goes **dormant** with a named trigger (Team/org migration or a public flip); **nothing is pending on Max**. Ledgers annotated: Register → **v0.26**, Rule Overview → **v0.24**, BOOTSTRAP → **v0.13**; Local Context → **v0.39**; board restamped; store **+3 revises (75 nodes / 362 events)**; both checkers green; one `[GOV]` commit; push per C-064.

*Author: Claude (AGENT.AI.CLAUDE) · Conversation surface: Claude Code, in-repo — third session on the default surface, opened by `/fractal`; frozen at issue including the postscript (C-058-class handover record, not minted — C-042 mint-on-reuse).*
