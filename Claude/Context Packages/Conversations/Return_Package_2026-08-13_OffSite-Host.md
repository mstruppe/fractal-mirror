# Return Package — 2026-08-13 — Off-site Host & Protection Model (OQ-21)

> **DERIVED PROJECTION — conversation hand-off record.** Historical artifact, dated filename (C-012). Domain: GOV (substrate). Author: Claude. Sources: this conversation (2026-08-13); Governance Protocol — Claude Series v0.16; Decision Register v0.12; Vision thought scramble.docx (repo first layer, pre-canon).

---

## 1. What this conversation was

Max opened directly on the standing G offers: **OQ-4 and OQ-21**. OQ-4 was reaffirmed open in one move ("we will most likely still leave as it is" — recorded as the self-consistent choice: one observed candidate is too few to define from). OQ-21 then pivoted from a backup question to an engineering one when Max introduced the **Vision thought scramble** — its part 2 describes a network of nodes mirroring scientific consensus — and asked what the host trade-offs mean *for an infrastructure that is supposed to become a network*. The resolution ("ok that settles it: go ahead with a private GitHub repo") was followed by the protection question ("how can I reassure that only I can alter anything?"), whose answer Max ratified into canon ("yes go ahead").

## 2. Decisions made (ratified in-conversation per C-033, recorded in Protocol v0.16)

- **C-056** — **Off-site copy = private GitHub repository** (working name `fractal`, remote `origin`); the push **rides the C-037 ritual** (every commit ends with `git push`). Chosen network-first; host pinned as a **C-018 swappable convenience** (migration = one URL change); second-machine clone deferred to observed need; public sharing stays open (flip-to-public vs. curated mirror — decided when real). **Resolves OQ-21; arms the C-038 acceptance test.** *Caveat: repo creation + first push are Max's terminal actions, pending at ratification.*
- **C-057** — **Protection model (doctrine):** layered custody — device (FileVault) / account (2FA-passkey; minimal tokens) / authorship (the git author field **attributes, never authenticates**; commit-signing **trigger = first second writer**; branch protection on observed need) / knowledge layer (append-only + hashes + verify ritual + no-rewrite = **evident and reversible, never hidden**). Practical checklist: BOOTSTRAP §4.
- **OQ-4 reaffirmed open** (recorded call, disposition annotated). **OQ-22 opened:** where does the network ambition enter canon?

## 3. Worth remembering (method notes)

- **Good architecture makes big decisions small.** The host choice felt important; C-018/C-019/C-020 had already engineered it into a one-URL convenience — and the genuinely network-critical decisions (decentralized ULID identity, first-mint-wins as a mechanical consensus primitive, the hash-frozen append-only log) were already settled and network-compatible. Worth saying out loud when a decision *feels* heavier than the register says it is.
- **Attribution ≠ authentication.** C-037's author convention names the author; only signing proves it. Recording the hardening step *with its trigger* (first second writer) is C-008 applied to security — the lock arrives with the threat, not before.
- **Evident-and-reversible beats locked** for a knowledge corpus: it also survives mistakes.
- **A vision document outside canon quietly steered a canonical decision** — observed, named, and turned into OQ-22 rather than left implicit.

## 4. Changes to the canonical layer (the repo)

| Artifact | Change |
|---|---|
| Governance Protocol Claude v0.16 | **New** — records C-056/C-057; Ratified in-conversation (first-push caveat). DOC-minted. |
| Decision Register | v0.11 → **v0.12** (C-056/C-057; OQ-21 resolved; OQ-4 reaffirmed; OQ-22 opened). |
| Rule Overview | v0.9 → **v0.10** (off-site-copy + protection-model rows; C-038 caveat re-armed; ledger caveat → OQ-22). |
| BOOTSTRAP.md | v0.1 → **v0.2** — §4 rewritten from "recommended, not yet mandated" to the C-056 ritual + C-057 checklist; acceptance test armed. Its DOC title cured versionless (C-045 label event). |
| KG Store | **+8 events (174), +1 node (46):** 1 DOC mint (Protocol v0.16) with route alias + 2 placements; 3 living-doc revisions (Register, Rule Overview, Bootstrap); 1 label alias. `verify.py` green. |
| Local Context (KG) | v0.16 → **v0.17** (OQ-21 leaves the G offers; C-038 test armed; OQ-22 enters). |
| Agenda Board | Regenerated file-first (C-048), stamp v0.17; artifact republished. |

Commit (C-037, author Claude): one coherent change-set `[GOV]`; `verify.py` green before the commit (C-050 duty).

## 5. Refresh list (project mirrors, per C-004)

Refreshed this conversation: `Fractal_Decision_Register.md`, `Fractal_Rule_Overview.md`, `Fractal_Local_Context_Knowledge_Graph.md`.

## 6. Unresolved / carried

- **Pending on Max (completes C-056):** create the private GitHub repo + first push — two terminal commands, provided in-conversation (`gh repo create fractal --private --source . --remote origin --push`, or web UI + `git remote add` / `git push -u`). From then on: every commit ends with a push.
- **Then armed:** the C-038 acceptance test — first exercise = clean clone + rehydrate from BOOTSTRAP.md; a cloud-session clone (fine-grained read token) would exercise the test and the network property in one move.
- Carried: OQ-4 (reaffirmed), OQ-18, OQ-22; protection ladder triggers (signing at first second writer).
- **WS is the declared open part** — forge on observed need (Architecture State §4). The repo-resident **skill** and the **KG index** stand as H offers.

## 7. Next

**Nothing is force-queued.** Next conversation follows Max: **G** (OQ-4 · C-038 test, now armed · OQ-22) or **H** (the build track: skill / index / interface). Open with Global + Local Context v0.17 + this package.

---

## 8. Postscript (same conversation, after the close)

Two further calls by Max, executed in a second change-set:

- **OQ-22 resolved:** the Vision scramble does **not** enter canon — it is biographical context, informing decisions the way any of Max's past informs how he thinks ("what we build … [is] influenced by this just as much as anything is influenced by my past"). Pre-canon material **informs, never governs**; its influence is captured in protocol reasoning. Register → **v0.13**; Rule Overview → **v0.11**.
- **Queued Next: "architecture integrity and safety"** — Max's explicit agenda call, stronger than an offer: one conversation to scope the item and decide **postpone vs. act immediately** (that call belongs to the conversation itself). Local Context → **v0.18**; board stamp **v0.18**; store 46 nodes / **176 events** (+2 revises); `verify.py` green.
