# Fractal Vocabulary Extension Procedure v0.1

> **CANONICAL SPECIFICATION (registry-entry class) — how a sovereign instance extends an inherited checker vocabulary without forking it.** Closes the gap the first simulated stranger named precisely (RF1-2, High): *"I know I MAY change my copy; I don't know HOW to do it governedly."* The Schema says new roles are added *"by registering them here in a later version"* (§3.3) — true for the mother, useless for an instance that inherited `verify.py` with the role set hard-coded and every document warning against the hand-fork anti-pattern. This standard is the governed door. Versioned artifact (C-040 class): frozen at issue; substantive change is a new version.

**Version:** 0.1 · **Status:** Ratified (2026-08-17, in-conversation per C-033 — Max: *"ratified and close"*; decision C-114, per Protocol v0.50) · **Domain:** GOV · **Author:** Claude · **Date:** 2026-08-17 · **Provenance:** RF1-2 (`Flight_2026-08-17_Refinement.md`, the researcher persona's second High friction) · **Document ID:** DOC-01M084YKXXS2XQRNMW31042913 (minted 2026-08-17 via `close.py --create`; stamped by the post-mint revise)

---

## 1 · Scope — what is extensible, and what deliberately is not

- **Placement roles** — extensible by this procedure. Roles are pure vocabulary: the fold treats every role identically (a placement key); adding one changes what an instance can *say*, never how the log replays. Meaning stays human, as everywhere in the graph.
- **Verbs, alias kinds, id grammar, fold rules** — **not extensible by this procedure.** A new verb changes replay semantics; a new alias kind changes fold behavior. Those are interchange-layer moves (GENESIS §7 — the frozen wire format): they require a Schema reissue, adopted from upstream by recorded decision — or a knowing fork, which this procedure exists to make unnecessary for the common case.

## 2 · The mechanism (the checker half — ships with this standard)

`verify.py` reads an optional **`vocabulary_local.json`** beside the store (same directory as the checker). Shape:

```json
{
  "roles": {
    "supports":    "P-012 — argumentation pack adopted for the literature review; a claim placement that argues for its target",
    "contradicts": "P-012 — the counter-edge of the same pack"
  }
}
```

Rules, enforced by the checker:

1. Each key is a role token: lowercase, hyphenated, `^[a-z][a-z0-9-]*[a-z0-9]$` — the inherited tokens' grammar.
2. Each value **names the adopting decision** (`P-…` or your prefix) plus a one-line meaning. An empty or missing rationale is an **error** — the gate: no vocabulary grows silently.
3. A token colliding with an inherited role is an error (extension, never redefinition).
4. Absent file = inherited vocabulary exactly. The mother's own store carries no file; nothing changes for anyone who does nothing.

The file is an **instance value, not kernel** (the parameterized class — kernel rule: *the vocabulary is extensible through the governed hook*; instance value: *what you extended it with*). Genesis does not write one; a kernel migration preserves yours untouched, because the kernel never ships the file — only the hook that reads it.

## 3 · The procedure (the prose half)

1. **Name the need** — an observed placement you cannot express with the inherited seven (`about, in, cites, by, member-of, is-a, derived-from`). An anticipated need is not a need (C-079's rule of thumb).
2. **Check the registry first** (C-092 via the Registry contract) — an existing pack (e.g. the argumentation role pack, once forged) beats a private invention; adopting a shared pack keeps future federation legible (OQ-31).
3. **Decide** — one recorded decision in your Register: the tokens, their one-line meanings, the need that fired.
4. **Write the file** citing that decision, one entry per role.
5. **Run `verify.py`** — green confirms shape, rationale presence, and no collision; the checker's info line lists your local roles, so conformance is visible in every subsequent run.
6. **Use the roles.** They are ordinary placement vocabulary from that commit forward. Optionally: upstream the pack through the fieldnote door (C-100) — a proven pack is registry material.

## 4 · Conformance

An instance is conformant when every local role carries its adopting decision in the file, the decision exists in its Register, and `verify.py` runs green. This standard ships **prose + checker complete** — the hook is the checker half, landed in the same release (beta-0.5).

---

**Refresh triggers:** a second vocabulary class proving extension-worthy in the field (the alias-kind question would reopen §1 deliberately); the argumentation pack shipping (it becomes this procedure's worked example); a federation-side namespace rule (OQ-31) touching role tokens.
**Sources:** RF1-2 (the finding of record); Node & Event Schema v0.6 §3.3 (the mother-side registration rule this door complements); GENESIS §5/§7 (tiering, sovereignty, the interchange layer); C-092 (adopt before invent); the Registry contract (`Registry/README.md`).
**Revision history:** v0.1 (2026-08-17) first issue — the beta-0.5 registry release: scope split (roles extensible, interchange frozen), the `vocabulary_local.json` mechanism with the decision-ref gate, the six-step procedure.
