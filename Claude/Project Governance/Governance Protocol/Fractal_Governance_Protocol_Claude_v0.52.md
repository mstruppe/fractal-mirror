# Fractal Governance Protocol — Claude Series v0.52

**Topic:** The twentieth session, second act (2026-08-17) — **C-116, the mirror rides every beta.** With the TF1 ratification landed (v0.51) and KNet's migration running at Gate 3 in parallel, Max asked the standing question: *"how do we deal with the fractal-mirror. this will host the public repo of fractal. it should update with every beta."* The mother-side inspection that answered it found the doctrine half-built and the practice failing exactly where he pointed: C-105 gives the mirror its identity (permanent public home, own anchor chain under `fractal@knet.network`) and two rebuilds had been executed by hand (beta-0.3, beta-0.4) — but the *push* waited on Max each time, and the pending pile had quietly aged into a **two-release backlog** (the beta-0.4 rebuild + anchor commits unpushed, GitHub still at beta-0.3; the beta-0.5 rebuild not yet begun). The proposal: make the mirror update a **standing rider of every C-090 pack, Claude-executed end-to-end including the push** — the C-064 pattern extended — with the flip remaining Max's single manual act. His word: *"ratified."*
**Status:** Ratified (2026-08-17, in-conversation per C-033 — Max's *"ratified"* on the two-part proposal: the standing authorization and the immediate catch-up) · **Date:** 2026-08-17 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.51 · **Document ID:** DOC-01M0B1VSF26SHRHX86AJNBHJHQ (minted retro 2026-08-18, the C-041 lapse cured per Scan #5 S5-2.1; stamped by the paired revise)

---

## 1 · The decision

### C-116 — The mirror rides every beta (the standing update ritual + the extended push authorization)

Every tagging close (C-090) gains a mirror rider, executed by Claude under standing authorization: **sync** the curated tree from the fresh `beta-X.Y` tag into the mirror working copy → **one rebuild commit** → the mirror's own **`beta-X.Y` tag signed under the public identity** (custody stays key G) → **OTS attestation + receipt** (the public chain continues) → **anchor commit** → **push `main` + tag**. The reasoning that carried the ratification: while the mirror is private the push publishes nothing, and after the flip the per-beta push *is* the desired "update with every beta" behavior; custody is the signature either way (C-074b logic); and the conservative prepare-then-Max-pushes shape had just demonstrated its failure mode — the backlog. Two boundaries stated in the decision: **the flip act (visibility switch → Pages → DNS) remains Max's own hand, untouched**, and **between betas the mirror deliberately lags** — the public sees anchored releases, never the living tree, the C-109 grant asymmetry applied to the public itself. No new tool ships at ratification (C-092/C-112 — the two hand-executions are the ritual's evidence base; mechanization joins the C-110 tool work or UF1's update standard on observed drag). Full decision text: Register C-116.

## 2 · Executed with the ratification

The **first execution is the catch-up** in the same session: push the mirror's beta-0.4 backlog (rebuild + anchor commits, the beta-0.4 tag), rebuild the mirror from **beta-0.5** (the registry release — `Registry/`, the two new standards, GENESIS v0.8, the C-114 hook), anchor it on the public chain (signed tag + OTS receipt, pending state disclosed per the C-090 practice), and push. Mirror-only artifacts are preserved by the sync (`README-BETA.md`, the public-chain `*-public` receipt pairs); the curated set remains the tag's export tree (`Site/`, `Workbench/`, and the working layers stay out, per the `.gitattributes` rules). The execution record is the mirror's own commit chain; the mother-side record is this issue.

## 3 · Ripple

Register → **v0.70** (the C-116 row + history). The Rule Overview row and the adapter's ritual line (a repo-ritual change on this surface — the C-084/C-090/C-098 precedent class: no conduct rule moves, Settings stays v0.8) land at this session's close walk per C-077. The Local Context's pending-on-Max list loses the mirror-push item at the same walk — the item's failure mode is what this decision retires.

---

*Author: Claude (AGENT.AI.CLAUDE) · Reviewed and ratified by Max in-conversation (C-033). Parent: v0.51. The session continues; the close will carry the walk.*
