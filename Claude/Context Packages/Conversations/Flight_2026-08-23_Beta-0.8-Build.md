# Flight Record — 2026-08-23 · The Beta-0.8 Build Flight (review → build → test)

> **FLIGHT RECORD (C-058 class, under the Ultracode Flight Protocol v0.2 container).** A dated observation, frozen at landing — never revised; corrections land in later records or the Register's ledger. DOC-minted at first commit: **DOC-01M0Q5GQBERYYK0W52D13EPY8M**. The three workflow runs (`wf_4ed02c3f-a49` · `wf_81e441e4-1db` · `wf_333501a6-2b6`) hold the full per-agent transcripts; this record is the citable landing.

**Commission (Max, the thirty-ninth session, verbatim):** *"let's do it with an ultracode flight procedure. review all deltas from beta 0.7. what is already done. what needs building. the building is part of the flight and will be discussed with/authorised after your game plan proposal. then run a test flight if the system is sound."* · **Contract:** proposed 2026-08-23, agreed on his *"let's go"*; **gated mode**, three phases, each launched on his word (*"let's go"* · *"go"* · *"let's go"*) — the two-turn rule held at every gate. · **Subject:** the governing repo — the beta-0.7..HEAD delta (11 commits, 106 files), the ratified 0.8 build slate (Update Plan v0.16 rows 4–5), the Interface Place Format v0.2. · **Author:** Claude (orchestrator) · **Domain:** GOV

---

## 1 · As-flown vs contract

| Phase | Contracted | As-flown | Verification tier | Landing |
|---|---|---|---|---|
| 1 · Delta Review | 9 agents, default (synthesis high) | **9 agents, 717k tokens, 0 failures** | adversarial-lite (every claim by live tool execution) | proposal-only — the gate report |
| 2 · Build | 8 agents, high on kernel-touchers | **8 agents, 1,205k tokens, 0 failures** | work-over single-pass (2 independent verifiers) | authorized slate in-tree (the gate word the adopting decision) |
| 3 · Test Flight | 5 agents, judge high | **6 agents, 513k tokens, 0 failures** | work-over single-pass + judge spot-verification | sandbox-only; judgment proposal-only |

**Deviation (recorded per §2):** Phase 3 flew 6 agents against the contracted 5 — the envelope loop's turn-taking (pull-never-push: the initiator must return after the counterpart's receipt) required three sim runs, not two; declared at launch, before the go. **Gas:** estimate ≈3.5M (range 2.5–5M; basis: Audit #1 / scope-axis / rule-corpus as-flown) → **as-flown 2,435k in-band subagent tokens (0.70× — under estimate; 23 agents, 548 tool uses)**. Orchestrator-side tokens not metered in this figure (the OQ-28 convention).

## 2 · Phase 1 — the delta review (landed 2026-08-23)

**42/42 done-claims CONFIRMED, 0 refuted, 0 partial** (governance 8/8 · kernel-tools 10/10 · site-stories 6/6 · interface-seams 5/5 · store-corpus 5/5 · slate-gaps 8/8). Store counts exact (163/1066). All 8 build gaps real and unbuilt at HEAD `5d2ed4e`. All four gates PASS at baseline. Findings **DR-1…DR-9** (1 Medium: the uncommitted session layer, protected through the build; 8 Low, incl. DR-2 the corpus lagging the Register by C-134–C-138, DR-4 the receipt/frictions distinction, DR-9 buffer 8/10). Byproducts handed to the commissioner's triage (KMP site copy · spent envelopes IF-0008/9/10 · guide's stale beta-0.5 mock · cosmetics).

## 3 · Phase 2 — the build (landed 2026-08-23, both verifiers SOUND)

Six lanes, two collision-free waves; all landed:

- **A — the ratification ripple:** Interface Place Format v0.2 → **Ratified** (C-033, Max's words of record in the banner) · v0.1 superseded-rider · Context Index v0.55 · **Interface Foundation v0.7** (new §11 the connection layer; §8 counterpart parameter CLOSED; faces + E2E note) · Rule Overview v0.58 (connection-gate row + grown-edition banner) · Registry v0.12.
- **B — `postman.py`** (poll · post · receipt · check; stdlib-only; the parser doubles as the format checker) + `test_postman.py` (19 green) + the reader-side cursor + the `/fractal` opener's poll step.
- **F/I — `close.py`:** the birth-state-manifest pack-gate (fail-closed, two distinct negative proofs verified) + the C-135 release-class row **armed-inactive** (`SEMVER_ACTIVE=False`, exit-code-neutral, proven).
- **C/E/H — genesis:** the v0.2 place template + **CN-0001 mother seed** + postman shipped to newborns · the mother's Rule Overview byte-copy replaced by a **generated seed** (the C-134 seed-body law) · the **day-one receipt** (SET-BY-FOUNDER vs DEFAULTED-ON-SILENCE) · **GENESIS v0.20** · Onboarding v0.7 + `/begin` re-projected · manifest rows + KMP pin v0.2.
- **G — KMP v0.2** (the C-135 minor/major fork; the manifest-read step; first-touch converter named armed-inactive) · v0.1 rider · Registry cell · Site projection refreshed.
- **D — the mother's reshape:** `Interface/Interface_Index.md` on the v0.2 grammar (check exit 0; 14 rows · 2 connections CN-0001 KNet / CN-0002 PR, codes honestly pending) · the domestic routing map · **IF-0014/IF-0015** posted (the retroactive pair offers, postman's first live exercise; byte-author Claude per C-084).

Verifier 1 (scratch-birth battery): **SOUND 8/8** — defaults-on-silence proven, seed-body law grep empty, newborn gates green. Verifier 2 (mother-side battery): **SOUND 11/11** with the declared transparency: `verify.py` (8 external-hash rows) and `check_versions.py` (2 LC→GENESIS ERRs) red **exactly and only** with the close-ripple transient class — the store hashes and the LC re-point are close acts by design (C-004). Scope guard clean. Builder deviations all declared in the run transcripts (notably: CN codes/fingerprints never invented — counterpart declarations are the children's own acts; the manifest's new rows defer family ids to the next classification audit).

## 4 · Phase 3 — the test flight (landed 2026-08-23)

**Judge's verdict: SOUND WITH FINDINGS.** Two genesis-born scratch instances (Alpha founder-flagged, Beta defaults-on-silence) executed **the complete v0.2 mechanism from the ratified standard's text alone**: the conscious ceremony (identity exchange → the connection code computed **independently on both sides and matching**, judge-recomputed `795b-1e34-5681` — with divergent-alternative probes proving the match unforced) → mutual lock-in (P-rows cross-citing) → the law-6 gate proven **both ways** (the Gamma refusal verbatim + zero side effects; every addressed act riding a standing CN) → post → the filtered header-diff notification (16 candidate rows → exactly the 2 addressed/broadcast ones, zero body bytes) → absorb + cite → receipt → spent → dissolve, **the full RAM cycle closed** (id held in high-water, citation trail surviving the dissolved bytes). All 10 loop stages PASS, spot-verified. Seven laws: 1/3/6/7 held **by construction**, 2 by construction at the tool + discipline at the ceremony, 4 exercised end-to-end, 5 by discipline (banner by construction). Governing tree bit-identical throughout (proven by hash manifest).

**Findings TF-1…TF-9** (4 Medium · 5 Low, all confirmed by the judge, all routed to the generator lane — nothing hand-patched in flight):

| Id | Sev | Finding (compressed) |
|---|---|---|
| TF-1 | Med | §2.2 code construction under-pinned (blob unit, separator, hex case, collation) — cross-vendor honest divergence possible |
| TF-2 | Med | postman stamps raw git identity as envelope Author — cross-instance attribution leak vs C-084/§5's AGENT id |
| TF-6 | Med | no `spent`/`dissolve` postman lane — §6.1's mandatory closing acts are unguarded hand edits |
| TF-7 | Med | the RAM trace clause assumes a commit between post and dissolve; nothing requires one |
| TF-3/4/5/8/9 | Low | fingerprint bytes unspecified · Code cell unlinted · `any`-prefix broadcast match · spent-visibility window unstated · H1 id mangling |

**Not covered (honest scope):** real cross-machine transport · real signing keys/custody · the commit/close seam in newborns · the KNet/PR retroactive lock-ins (their own acts; IF-0014/IF-0015 stand) · a live v0.2↔v0.2 poll (PR still v0.1-grammar, KNet placeless) · the §2.5 stranger lane walked · volume/concurrency/adversarial input · private faces · cross-vendor execution.

## 5 · Landing state + the standing offers (C-031)

**Executed in-tree (the authorized slate):** everything in §3. **Proposal-only:** the DR/TF findings slates; the TF-Medium cure set (four small generator-lane cures: two sentences in the Format's next touch, two postman lanes + the author resolution) stands as the flight's first offer. **What did not move, with reasons:** KNet's and PR's trees (their jurisdictions) · the mirror and `gh-pages` (no serving act commissioned) · store canon and DOC mints (close acts) · the Update Plan pair beyond the pre-flight v0.16 (regenerates at the close) · the protocol series (frozen). The close-ripple transients (store hashes, the LC's GENESIS pointer) wait on the close by design.

---

*Orchestrator: Claude (AGENT.AI.CLAUDE) · Commissioned, gated, and landed on Max's words of record. The judgment's full text and every agent return live in the three workflow transcripts; the scratch instances stood for the judge's spot-verification and dissolve with the session scratchpad.*
