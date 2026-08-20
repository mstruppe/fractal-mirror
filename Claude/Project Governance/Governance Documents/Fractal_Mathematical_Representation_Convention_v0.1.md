# Fractal Mathematical Representation Convention v0.1 (MRC)

> **CANONICAL SPECIFICATION (registry-entry class — a behaviour convention, C-132).** The rule-set for **how mathematical content is represented** in any governed document an agent produces: model descriptions, derivations, specifications that will become code. A **behaviour convention** is summoned into a scope, sandbox style — *"apply the MRC to this document"* — where it binds the named task completely; it composes with the instance's Conversation Settings and never overrides them, and it releases when the task ends (the C-132 invocation law). Shortcut: **MRC** (`/mrc`, or the plain word on any client — words work where slash menus don't). Versioned artifact (C-040 class): frozen at issue; substantive change is a new version.

**Version:** 0.1 · **Status:** Ratified (2026-08-20, in-conversation per C-033 — Max's commission of record, the KNet Codex friction: *"I let codex create a description of a mathematical model using equations. Those were not explained. Therefore I want codex to know that it has to use a certain rule set in how information is represented"*; the five rules his own, near-verbatim; the MRC shortcut his naming) · **Reviewed By:** Max (2026-08-20) · **Domain:** GOV · **Author:** Claude (from Max's rules) · **Parent:** C-132 (the behaviour-convention class) · Fractal_Scholarly_Source_Convention_v0.1 (the class's first member, C-115 — retroactively so named) · **Document ID:** DOC-01M0FY1ZBZ87Q01F2ZTK8EYPQV (minted at this close via `close.py --create`; stamped by the post-mint revise)

---

## 1 · What this convention is for

An equation that arrives unexplained is data without knowledge: a reader — human or agent — must reverse-engineer what every symbol means, what shape every quantity has, and what the expression is actually doing, before any of it can be verified or coded. This convention makes mathematical writing **self-carrying**: every document that binds it can be read cold, checked term by term, and translated to running code without a single guess. The commissioning specimen is real: a model description whose equations carried no definitions, produced in a governed instance — the friction this rule-set cures at source.

## 2 · The five rules (normative)

1. **Define every symbol.** State what each variable and constant means **before** it is used in an equation. No symbol appears in an expression whose meaning has not already been given in prose.
2. **Specify data types.** For every quantity, say whether it is a **scalar** (a single number), a **vector** (a list of numbers), or a **matrix** (a grid of numbers) — and by extension any richer type the document needs, named just as plainly.
3. **Show explicit operations.** Write multiplication signs out (`a · b`, `a * b`) rather than hiding them in juxtaposition (`ab`), so no reader — agent or human — can confuse a product with a two-letter name. The same explicitness applies to any operation a notation habit usually hides.
4. **State dimensions and ranges.** Every input and output carries its size limits (dimensions for vectors and matrices) and its expected number range. A quantity without a stated range cannot be validated.
5. **Derive before coding.** The mathematical steps are written out fully **in text** before any of them are translated into code for an agent to run. Code implements a derivation the reader has already been able to follow; it never substitutes for one.

## 3 · Invocation (the sandbox mechanic — C-132)

- **Summon by name:** `/mrc` (or the plain words *"apply the MRC"* / *"apply the Mathematical Representation Convention"*), naming the scope — a document, a section, a task. Within that scope the five rules are binding; outside it nothing changes.
- **Composition:** the convention adds representation rules; it never loosens or overrides the instance's Conversation Settings or any other standing rule. Where two summoned conventions both bind a scope, both apply; a genuine conflict is a finding, not a silent choice.
- **Release:** the binding ends with the task. A document that was written under the MRC says so once (a line in its banner or sources), so later readers know the rules it was built to.

## 4 · Adoption and the class

A **behaviour convention** (C-132) is an adoptable, invocable rule-set shaping how one class of output is represented — the class kernel doctrine, the members shelf-tier: an instance adopts a convention from the Registry by its own recorded decision (Registry rule 5), on felt need, exactly as it adopts any standard. This convention is the class's **second member**; the Scholarly Source Convention (C-115) is retroactively its first. The commissioning instance's path: the friction arose in KNet's Codex sessions — the mother holds the spec seat (the C-127/OQ-35 sorting), the convention travels to KNet as an interface offer, and KNet's adoption is its own decision.

## 5 · The checker half (named, not built)

Prose-first (Registry rule 2). The checker, when built, lints a bound document mechanically: every symbol in an equation preceded by a definition (rule 1), a type stated per quantity (rule 2), no bare juxtaposition products (rule 3), ranges present for inputs/outputs (rule 4). **Build trigger:** the first governed intake of a math document from another instance, or a conformance dispute the prose cannot settle by inspection — whichever comes first (the `fieldnote.py` graduation precedent, C-094/C-100).

---

**Refresh triggers (for the series, not this frozen version):** a bound document contradicting a rule in practice (new version, distilled from the case); the checker's trigger firing; a new member joining the class with a shape this document should mirror.
**Sources:** Max's commission and five rules (2026-08-20, the thirty-first Code session — verbatim core); C-132 (the behaviour-convention class + the invocation law); C-115 / `Fractal_Scholarly_Source_Convention_v0.1` (the class precedent); C-127 (adoption categories); C-021 (the command tier built on the commissioner's word, not ahead of it); Registry rules 1–5.
**Revision history:** v0.1 (2026-08-20) first issue — commissioned from the KNet Codex friction in the Scan #6 session; the five rules Max's own, the MRC shortcut his naming; the behaviour-convention class ratified in the same act (C-132), the site's Behaviour sandbox section and the `/mrc` command landing with it.
