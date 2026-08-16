# Fractal Governance Protocol — Claude Series v0.28

**Topic:** The custody session (C-074–C-076) — the OQ-27 → OQ-26 → OQ-25 cluster worked as one calibration, on Max's pick from the robust-ordering proposal: the **committer field declared mechanical** (attribution = author, custody = signature), **signing scoped to custody** with the sign-without-verify gap cured (`.allowed_signers` — every commit in history now verifies `G`), the **drone-branch lifecycle pinned** (delete after gated merge; both flight branches removed), and the **restore-drill cadence set** (rides every canonical Scan; ad-hoc on custody change). Two OQs resolved, one annotated; per-writer keys and GitHub branch protection recorded as armed/pending — not performed.
**Status:** Ratified (2026-08-14 — ratified in the conversation it records, per C-033) · **Date:** 2026-08-14 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.27

---

## 1. Context

Third Claude Code session, opened by `/fractal` on a queued-empty handover (C-031 honoured — the G offers stood). Max asked for the open-question ledger, then for "the most robust order to work those OQs up." The proposal sorted the ten open OQs into three classes — work now (observed data exists), ride planned work, fire-on-trigger — and front-loaded a single custody session (OQ-27 committer pin → OQ-26 ladder calibration → OQ-25 drill cadence) on the strength of the flight-2 committer datum and the imminence of a third drone flight (the KG index server standing as the prime brief candidate). Max: **"ok let's do OQ27 to OQ25."** The evidence pass sharpened the questions (§2); the option space per decision was walked at Max's request; his four calls came back explicit (§5).

## 2. Evidence of record (what the repo showed, 2026-08-14)

- **Signing live but half-built:** every commit — Max, Claude, both drone commits — carries an SSH signature (`commit.gpgsign=true` since the C-066 arming), but all three writer identities sign with **one key** (Max's `~/.ssh/id_ed25519`), and **no `gpg.ssh.allowedSignersFile` existed** — signatures that nothing could verify (`git log --show-signature` errored). Sign-only custody: "evident-and-reversible" half true at layer 3.
- **Committer inconsistent repo-wide, not just across flights:** flight 1 `b043982` author Codex / committer Max; flight 2 `99c4aa3` author Codex / committer Codex (fast-forward merge preserved the drone's commit object); and every Claude-authored Code-surface commit carries committer Max — the field tracks whichever configured environment ran `git commit`, nothing more.
- **Branch hygiene:** both merged drone branches still existed (`drone/first-flight-stats` local; `drone/close-tool` local + origin) — stale writable surfaces with no lifecycle rule.

## 3. Decisions of record

- **C-074 — Committer is mechanical; a signature attests custody (the OQ-27 pins).** **(a)** The git **committer field is mechanical plumbing** — it records which configured environment created the commit object and carries **no governance meaning**. Attribution lives solely in the author field (C-037's "attributes, never authenticates" extended to its neighbour); custody lives in the signature. Both flight patterns and the Code surface's Claude-author/Max-committer pattern are conformant — there is no committer rule to violate, and none is added. **(b)** **Signing is custody-scoped:** one key per custody environment; a signature attests *created inside Max's custody environment*, never which writer — the three writer identities share the custody key deliberately (on one machine, separate keys would be indistinguishable in threat terms: theater). **Per-writer keys are the armed next rung** — trigger: the **first writer operating outside Max's custody** (cloud drone, collaborator machine); not before. **(c)** **Verification cured:** `.allowed_signers` at the repo root (infrastructure file, C-006 exception class like `.gitignore`, not DOC-minted), all three writer emails as principals over the one custody key, bound via repo-local `gpg.ssh.allowedSignersFile`; the whole history verifies `G`. Rehydrate binding documented in BOOTSTRAP §4. *(Working Decision.)*
- **C-075 — Drone-branch lifecycle (extends C-066).** A `drone/<task>` branch is **deleted — local and remote — once its gated merge lands.** The work lives in `main`'s history; the protocol series is the flight record; a lingering branch is a stale writable surface a future flight could resume, diverge, or double-merge. Executed this close on both flight branches. **GitHub `main` branch protection** (block force-push/deletion) is recorded as a **standing recommendation, pending Max's vendor-side visit** — plan-dependent, account-holder-only, deliberately non-blocking. *(Working Decision.)*
- **C-076 — Restore-drill cadence (OQ-25 resolved).** The C-038 restore drill is a **standing section of every canonical Loose-Ends Scan** — next execution: Scan #3, already penciled — plus an **ad-hoc trigger on any custody or host change** (remote migration, new custody environment, new writer machine). No calendar cadence: the drill inherits the Scans' rhythm, so its trigger is owned by an existing, checker-enforced ritual rather than a date nobody watches (the S2-3.1 lesson applied forward). *(Working Decision.)*

## 4. Executed this close (one `[GOV]` commit, C-037; push = Claude, C-064)

- **Mechanical:** `.allowed_signers` created + config bound — historical verification confirmed `G` across the log; `drone/close-tool` (local + origin) and `drone/first-flight-stats` (local) deleted after merge-confirmation.
- **Store:** this protocol's DOC minted via `close.py --create`; ledger/context revises via the changed-doc pass. Register → v0.25 (C-074–C-076; OQ-25/OQ-26 resolved, OQ-27 annotated); Rule Overview → v0.23 (protection-model, commit-convention, drone-tier rows; §5 caveat); BOOTSTRAP → v0.12 (§4 rewrite: verification binding, drill cadence; §2.3 lifecycle); Context Index → v0.20 (PROT series range); Local Context → v0.38; board restamped; Return Package issued.
- **Checked — unchanged:** Global Context v0.3; Architecture State v0.7 (its C-057 sentence stays true); Schema v0.6/Template v0.4/Contract v0.1; store tools; **Conversation Settings v0.6 — the C-071 row walked: no conduct-touching decision this close** (no C-008 promotion, no surface/writer change, no close-ritual change — repo rituals only); all three adapter stamps current.

## 5. Calls recorded (Max, 2026-08-14, this conversation)

1. Session scope: **"ok let's do OQ27 to OQ25."**
2. After the option walkthrough, verbatim: **"Decision 1: option A · Decision 2: option A · Decision 3: Move 2 and delete after merge · Decision 4: Option A"** — i.e. committer mechanical (C-074a); custody-scoped signing with the per-writer trigger armed (C-074b, the verification cure riding as stated in the walkthrough); drone branches deleted after merge (C-075); the drill rides the Scans (C-076).
3. The branch-protection deferral (recommended, pending Max's GitHub visit) was proposed as part of the OQ-26 package and accepted within Decision 3's scope.

## 6. Ratification record (2026-08-14, in-conversation per C-033)

Max chose the session from the robust-ordering proposal, requested the full option walkthrough, and made all four calls explicitly. The governing surface executed the mechanical cures, verified them (history-wide `G`), and issued this record. Ratified in the conversation it records; no caveats.

## 11. Open Questions (TBD)

*(Per C-034 these are entered in the Register's cumulative ledger.)*

- **OQ-25 resolved** (C-076 — the drill rides the Scans). **OQ-26 resolved** (calibration done: current rung named, verification cured, branch lifecycle pinned; branch protection a recorded standing recommendation; second-machine and public-sharing postures unchanged with their C-056/C-057 triggers). **OQ-27 annotated, stays open** — committer and custody semantics pinned (C-074), branch lifecycle pinned (C-075); the remaining scope is the outside-custody world: per-writer keys (trigger armed), drone provenance and revocation once a writer leaves Max's custody. None opened. The review ledger stays fully green.

---

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.28 |
| Document Type | Governance Protocol (historical artifact, dated identity — C-012) |
| Version | v0.28 |
| Status | Ratified (2026-08-14, in-conversation per C-033) |
| Domain | GOV |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-14, this conversation) |
| Date | 2026-08-14 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.27 |
| Related Documents | `.allowed_signers` (infrastructure, C-006 exception, not minted); BOOTSTRAP.md (stamp inside); Decision Register (stamp inside); Rule Overview (stamp inside); Local Context v0.38; Protocols v0.22 (C-066), v0.24–v0.27 |
| Document ID | DOC-01M014Y4NCGWNP3GNW9VKHKH4D (minted 2026-08-14 via `close.py --create`; stamped in by the post-mint revise, per the v0.27 precedent — first stamp carried the dry-run preview's id, corrected in the same close) |
