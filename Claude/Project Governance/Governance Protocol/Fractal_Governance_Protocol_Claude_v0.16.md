# Fractal Governance Protocol — Claude Series v0.16

**Topic:** OQ-21 resolved — the off-site copy is a **private GitHub repository**, chosen network-first against the Vision scramble's part-2 ambition; the protection model recorded as doctrine (layered custody, evident-and-reversible, hardening ladder with named triggers); the C-038 acceptance test armed. OQ-4 reaffirmed open; OQ-22 opened (canonical home for the network ambition).
**Status:** Ratified (2026-08-13 — ratified in the conversation it records, per C-033; caveat: first push pending Max's terminal action) · **Date:** 2026-08-13 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.15

---

## 1. Context

OQ-21 had stood open since C-038 (v0.8, 2026-08-12): where does the off-site copy live — second machine, private Git host, or both? It was deliberately non-blocking; C-018/C-019/C-020 had engineered the host choice into a swappable convenience, and the "laptop in the ocean" acceptance test waited on its resolution. Max opened this conversation directly on the standing G offers — OQ-4 and OQ-21 — expected per C-031. OQ-4 was dealt with first and briefly: leave it as it is (see §6). The pivot came when Max introduced the **Vision thought scramble** (`Vision thought scramble.docx`, repo first layer): its part 2 describes a connected web of nodes mirroring scientific consensus — verified knowledge sharing, repeated challenge as filter, the conceptual citation network made systematic. Max reframed the question: *hypothetically I build an infrastructure that is supposed to become a network — so we need to engineer this carefully; I don't know what the trade-offs really mean for me.* The host question was then read network-first, settled, and followed by the natural companion question: *how is the architecture itself protected — how can I be sure only I can alter anything?* Max ratified folding the answer into canon.

## 2. Questions Investigated

- What do the off-site-host trade-offs (second machine / private Git host / both / self-hosted) mean when the infrastructure is supposed to become a *network*, not just survive a lost laptop?
- Which decisions are actually network-critical and hard to change later — and are any of them still open?
- Can work shared from a private repository later be shared publicly, and at what cost?
- What protects the corpus at each layer — device, remote account, authorship, knowledge layer — and against which threat?
- What does "only I can alter anything" mean in a system that deliberately has two authors (C-037)?

## 3. Human Input (Max)

- **OQ-4:** "which we will most likely still leave as it is" — reaffirmed open by deliberate choice, not neglect.
- Introduced the Vision scramble as the decision's proper horizon: the infrastructure is *supposed to become a network*; asked for the trade-offs to be translated into what they mean for him.
- Settled the resolution: **"ok that settles it: go ahead with a private GitHub repo"** — with the follow-up question whether that path also allows sharing the work publicly on GitHub later.
- Asked the protection question: how is the architecture protected; how to ensure only he (this mac user) can alter anything.
- Ratified the close-the-loop package including the protection model in canon: **"yes go ahead."**

## 4. AI Input (Claude)

- **The register had already de-fanged the choice.** C-018 (host = swappable client), C-019 (plain text in git), C-020 (the repo *is* FRACTAL) make host migration a one-URL change. The genuinely network-critical decisions are already made and network-compatible: C-015/C-039 (decentralized identity — 80-bit ULID randomness needs no central authority), C-049 (first-mint-wins — a mechanical consensus primitive any participant can replay from the log alone), and the append-only, hash-frozen event log, which structurally carries the scramble's blockchain-adjacent properties (verifiable, tamper-evident history) minus the currency.
- **Network-first reading of the options:** a hosted remote is a network *seed*, not just a copy — clonable from anywhere (exactly the C-038 test's shape), reachable from cloud sessions, and one step from fork/pull-request mechanics, which are a working, battle-tested instance of the scramble's challenge-and-admit filter. Self-hosting buys custody at the price of becoming an infrastructure operator — complexity ahead of observed need. A second machine alone is the weakest fit: a copy, not a node.
- **Public sharing:** a private repo flips to public in one setting, but the flip exposes the *entire history*; the curated alternative is a second, public mirror repo — decided when sharing becomes real, closed off by nothing chosen now.
- **Protection layers:** device (macOS account, FileVault), remote account (private repo = exactly one identity; 2FA/passkey is the single highest-value action; tokens fine-grained/read-only/expiring), authorship (the git author field is a *claim*, not proof — commit signing + verified badges is the step that makes "only I" a verifiable property of the history; its natural trigger is the first second writer), knowledge layer (append-only log, C-040 hashes, `verify.py` ritual, no history rewrites — alteration is *evident and reversible*, never hidden).
- **The honest caveat:** FRACTAL deliberately has two authors. The guarantee today is "only this mac user *and what they explicitly delegate*" — every Claude change flows through per-session granted access and lands as an attributed, revertible commit. Branch protection (Claude proposes on branches; only Max merges `main`) exists the day a harder split is wanted.

## 5. Jointly Derived Conclusions

1. **The host choice was engineered into unimportance — so resolving it costs nothing and buys the acceptance test.** The load-bearing, hard-to-change network decisions (identity, consensus primitive, log physique) were already settled; the host is a rented parking spot for a vehicle built to drive off (C-018 escape hatch recorded inside the resolution itself).
2. **Network-first, the hosted remote is the only option that is a seed rather than a copy.** Fork/PR mechanics sit one step away from the scramble's part-2 filter; the second machine joins organically later as the first second-writer clone — which is also what gives C-049/C-050 their first live exercise.
3. **Attribution is not authentication.** C-037's author convention *attributes*; only commit signing *authenticates*. The ladder is recorded with its trigger (first second writer) so the hardening happens exactly when the threat materializes, not before — C-008 applied to security.
4. **For a knowledge corpus, evident-and-reversible beats locked.** Append-only log + content hashes + verify ritual + no-rewrite means alteration cannot hide and can always be undone — a property that also survives mistakes, which a lock does not.
5. **A vision gap was observed, not actioned:** the network ambition lives in the pre-Claude scramble, not in the canonical vision (Global Context §1 stops at a single-investigator environment). Where and when it enters canon is Max's call — opened as OQ-22.

## 6. Current Decisions

- **C-056 — Off-site copy = private GitHub repository (resolves OQ-21).** The repo's off-site copy lives on GitHub as a **private repository** (working name `fractal`), bound as git remote `origin`; the off-site push **rides the C-037 ritual** — every coherent-change-set commit ends with `git push`. Chosen network-first (Vision scramble pt. 2): a hosted remote is clonable from anywhere, reachable from cloud sessions, and adjacent to fork/PR mechanics if FRACTAL ever opens to a second participant. The host is pinned as a **C-018 swappable convenience** — no architecture, tool, or document may hard-bind to GitHub; migration is one remote-URL change. A **second-machine clone is deferred to observed need** and joins as an ordinary second clone when a real second machine or writer appears. Custody accepted knowingly: a third party holds the bytes — acceptable today for an architecture corpus, reversible the day it isn't. Public sharing stays open by design: flip-to-public (whole history becomes visible) or a curated public mirror — decided when sharing becomes real. **Arms the C-038 acceptance test:** "laptop in the ocean" is runnable from the first push. *Caveat:* repo creation + first push are Max's terminal actions, pending at ratification.

- **C-057 — Protection model: layered custody, evident-and-reversible (doctrine).** The corpus's protection is four layers, each named with its threat: **(1) device** — macOS account + FileVault (lost/stolen laptop); **(2) remote account** — the private repo is readable/writable by exactly one GitHub identity, so its protection *is* account security: 2FA/passkey is the standing recommendation; access tokens, if ever created (e.g. cloud-session read access), are fine-grained, single-repo, read-only, expiring; **(3) authorship** — the git author field attributes but never authenticates (C-037 scope note): the hardening step is **commit signing** (SSH-key signing + verified badge, optionally required by branch protection), with its **recorded trigger = the first second writer**; until then push access = account = Max; **(4) knowledge layer** — append-only log, C-040 content hashes, the C-050 verify ritual, and C-037's no-rewrite rule make any alteration **evident and reversible, never hidden**. Delegation stays explicit: Claude alters only through per-session granted access, always as attributed, revertible commits; branch protection (propose-on-branch, Max-merges-main) is the available harder split, on observed need. Practical checklist home: **BOOTSTRAP.md §4**.

- **OQ-4 reaffirmed open (recorded call).** One candidate transition stands observed (consolidation complete + architecture map live); a definition distilled from a single case would be specification ahead of need. Leaving OQ-4 open is the self-consistent choice — define when a second case forces comparison. Noted: an open OQ-4 does not freeze the Global §2 line; Max may declare a transition by fiat, and that case becomes the first datum.

- **Ratification record (2026-08-13, in-conversation per C-033).** The resolution followed Max's own calls: host settled explicitly ("ok that settles it: go ahead with a private GitHub repo") after the network-first trade-off walkthrough; the protection model's entry into canon confirmed explicitly ("yes go ahead") after the layered walkthrough. Caveat recorded: the first push is pending; C-056's execution completes at Max's terminal.

## 7. Alternatives Considered

- **Second machine only.** Full custody, no third party — but a copy, not a node: freshness by discipline, likely shared location risk, no clone-from-anywhere story, nothing for the network horizon. Rejected as primary; preserved as the organic later addition.
- **Self-hosted Git (e.g. Gitea on a small server).** Full custody *and* a remote — at the price of operating infrastructure (availability, security, backing up the backup). Complexity ahead of observed need; the C-018 escape hatch keeps it available if custody ever becomes a real constraint.
- **Both now.** The configuration the architecture almost asks for — rejected only in timing: the second clone has no machine to live on today; deferred, not refused.
- **Public repository now.** Would expose the full history immediately and decide the sharing question ahead of need; private-now closes no doors (flip or mirror later).

## 8. Assumptions

- The corpus currently contains nothing whose third-party custody is unacceptable; the day that changes, C-018 migration (self-host or second-machine-primary) is the recorded exit.
- GitHub's private-repo access model as of 2026-08: private = owner + explicitly invited collaborators only; visibility flip and fork/PR mechanics as commonly understood.
- Push discipline can ride the existing C-037 ritual without a new mechanism; if pushes are observed to be forgotten, that is the C-008 trigger to automate (hook or tool), decided then.
- The protection ladder's triggers (second writer → signing; harder split → branch protection) are recorded conventions, changeable by ordinary recorded decision.

## 9. Consequences

- **BOOTSTRAP.md → v0.2:** §4 rewritten from "recommended, not yet mandated" to the concrete C-056 ritual (private GitHub remote, push rides every commit) + the C-057 protection checklist; acceptance-test note updated (armed).
- Decision Register → **v0.12**: C-056/C-057; OQ-21 resolved; OQ-4 reaffirmed; OQ-22 opened. Rule Overview → **v0.10**: off-site-copy and protection-model rows; C-038 caveat re-armed; ledger caveat updated.
- Knowledge Graph Store: **+1 node (46), +8 events (174)** — one DOC mint (this protocol) with route alias + two placements; three living-doc revisions (Register, Rule Overview, Bootstrap Protocol — its DOC title also cured versionless per C-045); committed per C-037, `verify.py` green before the store commit (C-050 duty).
- Local Context → **v0.17**; Agenda Board regenerated file-first (C-048) and republished (stamp v0.17).
- **The C-038 acceptance test is armed:** first exercise = clone on a clean machine (or a cloud session with a fine-grained read token) + rehydrate from BOOTSTRAP.md. Scheduling is Max's call.

## 10. Decision Ledger Changes

Added **C-056** (off-site copy = private GitHub repository; **OQ-21 resolved**; C-038 test armed) and **C-057** (protection model — layered custody, evident-and-reversible, hardening ladder with named triggers). **OQ-4 reaffirmed open** (recorded call, no disposition change). **OQ-22 opened.**

## 11. Open Questions (TBD)

*(Per C-034 these are entered in the Register's cumulative ledger.)*

- **OQ-22 (new):** where does the part-2 network ambition (Vision scramble) enter canon — an update to Global Context §1, a dedicated Vision canonical, or deliberately nowhere yet? Max's call; no urgency — it quietly informed this decision and should not keep informing decisions from outside canon indefinitely.
- Standing items carry: OQ-4 (reaffirmed), OQ-6, OQ-9, OQ-10, OQ-13, OQ-16, OQ-17, OQ-18, OQ-20; C-038 acceptance test **armed, not exercised** (first push pending, then first clone-rehydrate).

## 12. Next Line of Research

The G offers now read: OQ-4 (reaffirmed, parked) · **C-038 acceptance test** (armed — the natural next micro-step after the first push; a cloud-session clone via read token would exercise both the test and the network property in one move) · OQ-22 (vision home). The H roadmap stands unchanged (KG index; entry-point interface tier; repo-resident skill → plugin).

---

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.16 |
| Document Type | Governance Protocol (reasoning / decision record) |
| Version | v0.16 |
| Status | Ratified (2026-08-13, in-conversation per C-033; first push pending) |
| Domain | Project Governance — Substrate / Off-site Copy & Protection |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-13, this protocol) |
| Date | 2026-08-13 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.15 |
| Related Documents | BOOTSTRAP.md v0.2; Fractal Decision Register v0.12; Fractal Rule Overview v0.10; Vision thought scramble.docx (repo first layer, pre-canon); Knowledge Path Foundation v0.1 (C-018–C-020) |
| Revision Trigger | Any change to C-056 (host, push ritual, second-clone status) or C-057 (protection layers, ladder triggers) |
| Document ID | DOC-01KZXZ009GA9A3P8TW9CVCBJRR |
