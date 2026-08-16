# Fractal Governance Protocol — Claude Series v0.35

**Topic:** The punch-list close (eighth Code session). Max's directive at open: *"let's close all open ends which are closable in this session (some … are meant to be triggered by need)."* The whole open-ends ledger was triaged into closable-now vs standing-by-design, and every closable item closed: **C-087 — the secrets doctrine** (OQ-30 resolved before the first key exists); **C-088 — inherited kernel biography is provenance, not defect** (the C-081 question closed; `INHERITED` source class chosen, strip-on-copy rejected; machinery rides the queued flight); **C-089 — the Cowork surface retired** (supersedes C-072; OQ-16 leaves the ledger entirely). **OQ-17** closed by observation and **OQ-18** by answer (no Schema touch needed). The **naming check executed** with its posture recorded, and the **public posture recorded** (private until the beta proves the kernel). The **`doctor.py` drone brief** was written and **flight 4 launched** in a full clone (C-082).
**Status:** Ratified (2026-08-15 — ratified in the conversation it records, per C-033) · **Date:** 2026-08-15 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.34

---

## 1. Context

The session opened by `/fractal` onto the queue the whiteboard close left: the pre-ship punch list, OQ-30 first. Max's opening directive widened it deliberately — close *everything* closable, leaving standing only what stands by design. The triage (full ledger loaded — Register v0.35, all open OQs, the findings ledger, the un-ledgered ship-boundary items) sorted every open end into three classes: **closable now** (OQ-30 · the C-081 question · OQ-16's vendor-held half · OQ-17 · OQ-18 · the naming check · the public posture), **standing by design on named triggers** (OQ-4, OQ-9, OQ-20, OQ-23, OQ-27, OQ-28, OQ-29, OQ-31, OQ-32, S3-2.2, branch protection), and **queued work unblocked by the closes** (the `doctor.py` brief, sequenced behind OQ-30 by v0.33's call).

Max decided the slate in one structured pass: secrets doctrine **adopted as proposed**; inherited biography **doctrine now, machinery in flight**; all four minor closes **taken** (OQ-17, OQ-18, naming posture, public posture). On the Cowork question he answered with a condition — *"I suggest to retire it completely for a clean slate, unless we may profit from the documents, but these are mirrored projections anyways, correct?"* — and the condition resolved affirmatively on the record: everything the surface held was a projection (the instructions field a C-035 compression of Settings; the Project mirrors already retired by C-067; the board artifact a display surface per C-048). Retirement loses nothing and hardens the walk. S3-2.2 was deliberately **not** forced closed: its recorded grounds (Max must actually read the two specs; two kernel-spec reissues for a header field buy weight where OQ-28 says weight is the risk) survive this session's test, and OQ-18's resolution as *no* removed the last pressure toward an out-of-cycle Schema touch.

## 2. C-087 — the secrets doctrine (OQ-30 resolved)

**Decided before the first key exists, as the row demanded.** Five clauses, one decision:

1. **No canonical artifact ever holds a secret value** — not the store, the log, a governed document, or committed config. The complement of *knowledge is never ignored*: a secret value is not knowledge, it is access.
2. **The fact of a credential is knowledge and is recorded:** name, purpose, scope, holder, and lifecycle events (issued / rotated / revoked) — the value never.
3. **Values live in the environment layer:** a `.gitignore`d env file (`.env`, `.env.*`, `secrets/` — the ignore entries ship in the kernel and landed in this repo's `.gitignore` in this close) or the OS keychain; governed config refers to secrets by name, resolved at runtime. The mechanism is a **kernel rule**; *which* secrets exist — the credential inventory — is an **instance value**: C-087 is the **eighth parameterized decision** (GENESIS §2).
4. **Secrets are deliberately non-durable:** excluded from the off-site copy by construction, so the "laptop in the ocean" test *loses* them and rebuild = **re-issue against the recorded facts**, which become the re-issue checklist. Credentials are re-issuable; knowledge is not.
5. **The machine guard rides `doctor.py`** (§7): a known-format/entropy scan over tracked files plus verification that the ignore entries exist.

**All three clients covered:** broker/market keys (arc 2 — env layer), profile key material (OQ-32 — private keys never leave the writer's custody environment, exactly as the C-074b custody key already lives; `.allowed_signers` holds only public halves), login credentials (the armed log-in trigger — vendor keychain, facts recorded). Normative homes: BOOTSTRAP §4 item 5 (custody checklist) and GENESIS §2 row 8 + §3.1 (the kernel rule and its parameter).

## 3. C-088 — inherited kernel biography is provenance, not defect (the C-081 question closed)

The whiteboard already observed that "shippable beta" is arguably C-081's trigger arriving; this close takes the question on that ground — **doctrine now, machinery in flight** (Max's pick of the three offered dispositions; *implement this session* and *leave for arc 2* both declined).

**The doctrine:** the 67 citations a birthed kernel carries into FRACTAL's history are **provenance** — the constitution legitimately cites the history that produced it, the way inherited law carries its own case history. The cure is therefore an **`INHERITED` source class** in `check_versions.py`: citations *from* inherited kernel documents *into* the upstream history they came from are exempt from the phantom rule, while intra-instance claims still check. **Strip-on-copy is rejected** — it buys silence at the cost of the constitution's *why* and the byte-identical provenance arc 1 verified. The 9 registry errors are `genesis.py` re-pointing work (the newborn's checker registry parameterized to its own spine), and genesis writes the **inherited manifest** the class reads. **Machinery rides flight 4** (§7), gated per C-081/C-082: both checkers green in this repo, and in a birthed scratch instance `verify.py` green plus `check_versions.py` at **0 errors** (from the measured 76). Until the flight lands, the posture is unchanged — a newborn does not run the tier-1 checker at all (GENESIS §6, C-081).

## 4. C-089 — the Cowork surface is retired (supersedes C-072)

**Max's call, on a verified premise:** everything the Cowork Project held was a projection — nothing lives only there, so retirement is a pure simplification. Effects, all executed this close: **Settings → v0.7** (§2 scope = Code surface + drone tier; the vendor-held adapter becomes a pattern with no member; the C-071 ordering held — the source moved first); **both adapters re-projected** (`CLAUDE.md` → v0.6, `AGENTS.md` → v0.7 — restamp plus the C-087 content line, C-077's third exercise); **BOOTSTRAP → v0.16** (§2.1 names Claude Code the reference client outright; §2.4 keeps the generic vendor pattern for the future); the **C-059 walk becomes fully repo-verifiable** — its last vendor-held, unverifiable row is gone, completing what C-067 started when it retired the mirrors. The board stays exactly as C-048 left it minus the republish step: the repo file is now the only rendering. **OQ-16 leaves the ledger entirely:** its packaging half was C-083; its vendor-held half is mooted — there is no vendor field left to sync, and OQ-9 no longer carries the remainder. Vendor-side cleanup (deleting the Cowork Project and artifact in the app) is cosmetic, Max's at leisure — the retirement is effective from this record regardless. Classification: **instance decision** (FRACTAL's surface roster is biography; a future instance decides its own surfaces).

## 5. Two ledger rows closed without new numbers (the OQ-22 pattern)

- **OQ-17 — offer-once calibration: resolved by observation.** Open since v0.5 as *calibrate in use*; roughly fifteen sessions have exercised C-031c without one steering complaint, including sessions where Max diverged from the queued item and the divergence was followed without friction (v0.33's arc-2 deferral being the sharpest case). Closed as **calibrated**; re-open trigger: the first time a nudge reads as steering.
- **OQ-18 — time placements do not auto-derive: resolved as *no*.** `created` records *when written*; a `time` placement asserts *aboutness* — a document about 2023 belongs to 2023 regardless of when recorded. Auto-derivation would mechanically conflate the two and dilute the facet's meaning (C-026). No Schema change is needed to decide this — the Schema never promised derivation; the question was whether to add it, and the answer is no. Consequence: the OQ-18 + S3-2.2 bundle dissolves — S3-2.2 keeps its own named trigger (each spec's next *real* reissue) with no pressure toward an artificial one.

## 6. Ship-boundary postures recorded (still un-numbered by design)

- **Naming check — executed this session.** The "Fractal" name space in software is crowded: GNOME **Fractal** (active Matrix client), **Fractal Analytics** (major AI company), **Fractal Software** (SaaS venture studio), the **Fractal Analytics Platform** (bioimage framework), and — closest to home — a GitHub project literally named *fractal-knowledge* (a knowledge-management system). A bare-word "FRACTAL" trademark in software classes is effectively unavailable and the bare name invites confusion at any public boundary. **Posture recorded (Max's call):** FRACTAL stays the working title while private; at the public flip the name is **qualified or compounded** (a distinctive compound can be protected where a bare word cannot) — an ordinary decision at that boundary, now with its evidence on file.
- **Public flip vs curated mirror — postured, not decided.** **Private until the shippable beta proves the kernel** (arc 2's re-framing); the flip-vs-mirror choice is made then, with the naming decision and branch protection's C-075 trigger firing at the same boundary. What was an un-ledgered worry is now a deliberate, recorded posture.

## 7. Flight 4 — `doctor.py` (launched, landed, gated and merged in this same session)

The queued brief, unblocked the moment C-087 and C-088 landed, flew as **drone flight 4** on `drone/doctor-tool` in a **full clone** (C-082). **The launch itself misfired once** — an invalid flag combination — and was caught within seconds because the launch was verified rather than assumed: the third consecutive flight whose launch had a defect only inspection caught, confirming C-082's corollary as a standing pattern, not an anecdote. The corrected flight ran ~25 minutes and handed back one clean commit (`598a21c`, author *and* committer Codex per C-084c, worktree clean, no unreported deviations).

**The governing-surface gate, run independently:** code review of all 512 inserted lines (the `INHERITED` implementation returns FRACTAL's registry objects untouched when no manifest exists — behavioral identity by construction; displaced upstream aliases still *error* when cited by the instance's own documents; `doctor.py` redacts every hit and treats tier-1 absence as information, C-081) · both checkers green on the branch · `doctor.py` green in clone and newborn · an **independent scratch birth** (separate from the drone's own test instance) at `verify.py` green and `check_versions.py` **PASS, 0 errors, 0 warnings** — C-081's 76 all gone, the exempted upstream citations *counted* (114) rather than hidden. **Merged** `17636e1` (author Claude, committer Max — the merge rode Max's ratified wait-then-merge plan, C-084b), signed `G`; **branch retired**, local and remote-never-created (C-075). `doctor.py` is the **sixth store tool**; the store README records it.

**Two findings from the landing, recorded honestly:** **(a)** the flight widened the copied kernel set — `genesis.py` now ships `check_versions.py` and `doctor.py` into a newborn, *ready to adopt, never demanded*; C-081's gate rule is untouched (carrying a checker is not being required to run it), and GENESIS §1/§5 record the new shape. **(b)** **A full-clone drone commit arrives unsigned** — a clone does not inherit the repo-local signing config, so `598a21c` is `N` inside the signing era, the first exception to the drill's "everything after `b043982` is `G`" shape. Custody is intact in substance (the clone lives in Max's environment; the signed gated merge attests the work) but the *shape statement* was false as written: BOOTSTRAP §4 now carries the dated exception class with its rule — **a flight commit's custody attestation is the signed gated-merge commit** — and the forward cure: launch procedure configures signing in the clone (same custody key, same environment — C-074b conformant), so the exception stays dated rather than growing.

## 8. What this close deliberately does not do

S3-2.2 stays open on its recorded grounds (reading is real work; no artificial spec reissue). OQ-4, OQ-28, OQ-29 still resolve *at* arc 2; OQ-31, OQ-32 at their arcs; OQ-9, OQ-20, OQ-23, OQ-27 on their named triggers. Branch protection stays dormant (C-075). Global Context §2 is untouched for the fourth consecutive close — the realisation moves when FRACTAL governs a project that is not itself. No route is minted; the Knowledge Network Foundation is untouched.

## 11. Open Questions (TBD)

- **OQ-9 annotated:** no longer carries OQ-16's vendor-held remainder (mooted by C-089); the per-case promotion question stands alone again.
- **OQ-28 annotated:** the kernel gained its eighth parameter (C-087) — the weight dial's baseline moves by one small, deliberate increment; arc 2 remains the verdict's source.
- ~~Flight 4 open at close~~ — **resolved within the session**: Max chose to wait for the landing; the hand-back was verified, gated (76 → 0 in an independent scratch birth) and merged before the close (§7). Nothing of the flight is carried forward except the two recorded findings.
- Ship-boundary decisions remain un-numbered by design, now *postured*: naming qualification at the flip; flip-vs-mirror at beta; branch protection rides the flip.

## Ratification record (2026-08-15, in-conversation per C-033)

The full slate was put to Max as an explicit decision set after the triage; his answers of record: **"Adopt as proposed"** (C-087) · **"Doctrine now, machinery in flight"** (C-088) · *"I suggest to retire it completely for a clean slate … these are mirrored projections anyways, correct?"* — condition verified, retirement executed (C-089) · all four minor closes selected (OQ-17, OQ-18, naming posture, public posture). Max's further call mid-session: *"I'll wait until the flight lands then we close?"* — the wait-then-merge course ratified in advance, executed as §7 records. Ripple: Settings → v0.7 (source first, C-071) · `CLAUDE.md` → v0.6 · `AGENTS.md` → v0.7 · BOOTSTRAP → v0.16 (secrets item + the drill-shape exception) · GENESIS → v0.3 (eighth parameter; copied-checker shape) · `.gitignore` + secrets layer (landed via the merge) · Architecture State → v0.13 (§6 partition maintenance: kernel ~68 · parameterized 8 · instance 15; C-088 executed) · Register → v0.36 · Rule Overview → v0.30 · Context Index → v0.25 · Local Context → v0.50 · store README (sixth tool) · board regenerated · **flight 4 merged (`17636e1`) and its branch retired**.

## Document identity

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.35 |
| Document Type | Governance Protocol (historical artifact, dated identity — C-012) |
| Version | v0.35 |
| Status | Ratified (2026-08-15, in-conversation per C-033) |
| Domain | GOV |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-15, this conversation) |
| Date | 2026-08-15 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.34 |
| Related Documents | Conversation Settings (stamp inside — v0.7 this close); CLAUDE.md + AGENTS.md (stamps inside); BOOTSTRAP.md (stamp inside); GENESIS.md (stamp inside); Architecture State (stamp inside); Decision Register (stamp inside); Rule Overview (stamp inside); Context Index (stamp inside); Local Context (stamp inside); the flight-4 brief (session artifact, not repo-resident) |
| Document ID | DOC-01M02Y7QMQ6H7V79HVGDE1Q6H7 (minted 2026-08-15 via `close.py --create`; stamped by the post-mint revise) |
