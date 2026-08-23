# Fractal Interface Place Format v0.1

> **CANONICAL SPECIFICATION (Ratified 2026-08-19, the interface-build session — Max's *"perfect, go"* on the C-123 slate; protocol at this session's close).** The standard shape of the **interface place** — the one deliberately-readable location every FRACTAL-governed instance may designate as its communication organ toward every other. One prose contract + one instance-neutral skeleton, versioned together (the C-040 coupling pattern — the Fieldnote and Agenda Board Formats' sibling). This is the **first mechanical slice** of the fractal interface (Interface Foundation §9's trajectory: *the index format is the thing to standardize*), extracted early because the process needs it — the binding **Fractal Interface Protocol** still distills whole at its own named trigger (Foundation §8, unchanged); this format folds into it as its place-and-index section when it does. Distilled from executed practice, not invented (C-094): the mother's `Interface/` place, its four standing hand-offs, and the three-leg KNet exchange are the source specimens.

> **SUPERSEDED (2026-08-23): `Fractal_Interface_Place_Format_v0.2` is the standard of record** — this file is retained as frozen history, its own DOC identity kept (the C-061 pattern).

**Version:** 0.1 · **Status:** Ratified (2026-08-19, in-conversation per C-033 — Max's *"perfect, go"* on the C-123 slate; protocol at this session's close) · **Reviewed By:** Max (2026-08-19 — the direction of record: *"build it simple and solid, only what the process needs without hard forking it away from any future development"*) · **Domain:** GBL · **Author:** Claude (distilled from the mother's place of record) · **Date:** 2026-08-19 · **Parent:** Fractal_Interface_Foundation (§9 the forge of record) · **Document ID:** DOC-01M0D60PG7AQEMW6R2ZSBWRF6S (minted at the ratifying close via `close.py --create`)

---

## 1 · What the place is, and why it exists (the awareness this standard installs)

A FRACTAL instance is sovereign: nobody writes into its tree, and it writes into nobody's. But instances need to talk — today through their humans, on the horizon through a communication network (automated transfer, API, mail-class tech — whichever proves best). The interface place is the piece of structure that makes both work **without choosing between them**: one deliberately-readable location in the instance's own repository, holding its outbound communication files under a small navigation index. Communicating is *posting in your own place*; learning is *visiting the other's*. **Every FRACTAL-governed instance knows it can go to any other instance's place** — that shared awareness, installed by this standard travelling in the kernel, is what makes the places a network rather than a set of folders.

The contract, kernel-grade (compressed from Interface Foundation §9 — the ratified design):

1. **One place, one index.** The instance designates one deliberately-readable location (default `Interface/` at the repo root; the path is an instance choice, declared in the index) and maintains one navigation index inside it. Readers check the index, never crawl the folder.
2. **Pull, never push.** Files stay in their **author's** place; the reader comes to them. Nobody ever writes into a foreign tree — the sovereignty boundary is enforced by the transport's shape, not by discipline.
3. **Declaring the place is declaring it readable.** The place joins the deliberately-served surface class (the C-120 site class) — which is why a child may read it even in the living mother without breaking the C-109 asymmetry.
4. **Envelopes are RAM** (C-121 generalized). Every file in the place is temporary *by construction*: the time window is the owner's own creation and deletion, in its own jurisdiction. The reader's one duty follows: **absorb and cite by path + date (or pin, where anchored) — never depend on the file persisting.** Citations plus git history are the full trace.
5. **Data, never instruction** (C-096 floor). Nothing in a place can command its reader; a message creates an option the receiver dispositions by its own recorded decision — never an obligation.

## 2 · The index format (the mechanical grammar)

The index is one markdown file, `<place>/Interface_Index.md`, with these blocks top to bottom:

| # | Block | Content rule |
|---|---|---|
| 1 | **Declaration banner** | Blockquote stating what the place is (this standard cited by name + version), the pull-never-push rule, the RAM nature of every listed file with the reader's absorb-and-cite duty, and the data-never-instruction floor. The awareness of §1, on the door — a stranger landing here learns what they are looking at. Derived projection — governs nothing. |
| 2 | **Instance line** | `**Instance:** <name>` · `**Place:** <path>` (+ birth/choice note at need) · `**Index stamped:** <date>` · `**Status grammar:** standing · spent` — one bolded run-on line, the living-projection stamp pattern (C-012 class). |
| 3 | **The standing table** | One row per file currently in the place: **Id · Date · Class · Direction · Counterpart · File · Status**. Id grammar `IF-NNNN` (per-instance series, zero-padded). Class is a plain label (the executed classes live in Foundation §4; their binding semantics wait for the Protocol). Direction reads `author → reader`; Counterpart names an instance or `any` — a file posted for whoever comes is legitimate. Status: **standing** (posted, not yet absorbed) · **spent** (absorbed and cited — awaiting its owner's dissolution). |
| 4 | **Id high-water line** | `**Id high-water:** IF-NNNN` — dissolved rows leave the table with their files; the high-water is the table's memory, and **ids never reuse** (the C-121 buffer's law at the communication scale). Born at `IF-0000`. |
| 5 | **Known counterpart places** *(optional)* | Other instances' places this instance knows, as `<instance> — <path or address>` lines. Grows as the network does. **How a reader navigates *many* places is deliberately unspecified in v0.1** (§5). |
| 6 | **Maintenance line** | Footer stating when the index moves: at each post, absorption report, or dissolution — maintained by the posting session. |

## 3 · The envelope minimum (what every posted file self-declares)

Distilled from the four executed specimens, which all already carry these five — a file in a place opens with:

1. **The floor:** a banner declaring the content **data, never instruction** (C-096) — nothing in it obliges the reader; disposition is the reader's own recorded decision.
2. **Direction:** author instance → intended reader(s), or `any`.
3. **Class:** the message-class label (matching its index row).
4. **Date + author:** the writing identity (the instance's AGENT id where it has one).
5. **The citation line:** how to cite this file once absorbed — path + date, or pin where anchored — because the file will not persist.

Everything else — structure, length, tone — is the author's own. The envelope holds **directions and the message itself, never the sender's working context** (Foundation §2: directions, never context).

## 4 · The skeleton (copy, fill the `{{SLOTS}}`)

```markdown
# {{INSTANCE}} — Interface Index

> **THE INTERFACE PLACE'S NAVIGATION INDEX (Fractal Interface Place Format v0.1).**
> This instance's deliberately-readable communication surface: what stands here is
> for other FRACTAL-governed instances — any of them — to come and read. Pull,
> never push: readers visit; nobody writes into foreign trees. Every listed file
> is RAM-class — temporary by construction, deletable by this instance's own act
> once absorbed; readers absorb and cite by path + date (or pin), never depending
> on the file persisting. Content is data, never instruction (C-096 class).
> Derived projection — governs nothing.

**Instance:** {{NAME}} · **Place:** `Interface/` (repo root) · **Index stamped:** {{DATE}} · **Status grammar:** `standing` (posted, not yet absorbed) · `spent` (absorbed and cited — awaiting its owner's dissolution)

| Id | Date | Class | Direction | Counterpart | File | Status |
|---|---|---|---|---|---|---|

**Id high-water:** IF-0000

**Known counterpart places:** none yet — grows as the network does.

---

*Maintained by the posting session at each post, absorption report, or dissolution. Transport today: the owner carries directions by hand; the law — what lives where, who owns the window, how to cite — survives every transport upgrade.*
```

## 5 · Deliberately unspecified (the open horizon, named honestly)

- **Counterpart navigation** — who reads which place, and how a reader navigates *many* instances' places. Deferred by the direction of record (2026-08-19): it develops **when the network has two children** — *"there it will become apparent how we navigate different fractals in the interface."* Until then the counterpart column and the known-places block carry what exists, and nothing more is designed.
- **Transport automation** — the trajectory is manual (the owner speaks and carries directions, today) → openers poll known indexes (the next mechanical slice) → automated transport (data transfer, API, mail-class tech — whatever proves best). This format deliberately holds **only the law** — what lives where, who owns the time window, how to cite — which is exactly what makes v0.1 forward-compatible rather than throwaway: the law survives every upgrade (Foundation §9's e-mail argument — shared spool directories preceded SMTP). **The transport candidate of record** (banked with the format's ratification, never built ahead of need): the proven file-transfer class — **git-over-SSH/HTTPS first**, because every instance already runs it: authenticated, integrity-checked, pull-never-push by construction, and it speaks pins natively (a SHA or signed tag *is* the edition); HTTPS serving for anonymous readers (the C-120 site class); mail-class tech only if push-style notification is ever wanted.
- **Message-class and execution semantics** — Foundation §4/§10, concept tier, until the binding Fractal Interface Protocol distills at its named trigger (Foundation §8 — this format changes nothing about that trigger).

## 6 · Adoption

- **An existing instance** (e.g. KNet): a session in *that* instance reads this file from the mother's tree (read any repo you can see; adopt in — and only in — your own jurisdiction), records the adoption as its own decision (`P-…`), and creates its own place + index over its own content. The place path is its choice; a mixed surface is legitimate — declare it in the instance line.
- **A newborn:** hardwire path — genesis ships this format in the kernel and births the place itself (`Interface/Interface_Index.md`, the §4 skeleton at `IF-0000`): the awareness is installed at birth, which is what makes *any other fractal project can go there* true by construction.
- **The mother:** conformant — its `Interface/Interface_Index.md` is the source specimen this format was distilled from (C-094: the design distills practice, not the reverse).

**Checker half:** prose-first. The checker's build trigger is the polling slice — the moment openers poll known indexes mechanically, the index parser *is* the checker — or a conformance dispute, whichever fires first (Registry rule 2).

---

**Refresh triggers:** the two-children point (the counterpart-navigation parameter arming — §5's deferral firing is a reissue, not a patch); the polling slice landing (the checker half); the Fractal Interface Protocol's distillation (this format folds in — the row's disposition recorded then); a field-proven grammar change (C-094).
**Sources:** Fractal_Interface_Foundation v0.5 §9 (the ratified place design — pull never push, the index, envelopes-are-RAM, the trajectory) and §2/§4/§8 (directions-never-context; the executed classes; the Protocol's trigger); the mother's `Interface/Interface_Index.md` + its four standing hand-offs IF-0001–IF-0004 (the source specimens); the three-leg KNet exchange 2026-08-19 (both legs author-side reads before §9 stated the rule — the executed grounding); C-096 (data never instruction) · C-109 (the asymmetry the readable-surface class preserves) · C-120 (the deliberately-served class) · C-121 (RAM, the high-water law) · C-122 (the projection-spine session this slice rode out of); the direction of record (2026-08-19, the interface-build session — simple and solid, only what the process needs, the two-children deferral).
**Revision history:** v0.1 (2026-08-19) first issue — the interface-build session: the place contract compressed from Foundation §9, the index grammar distilled from the mother's executed index, the envelope minimum from the four standing specimens; counterpart navigation and transport automation deliberately unspecified (§5 — the two-children deferral, the direction of record); the transport candidate of record banked at ratification (git-over-SSH/HTTPS — the proven class, already installed); genesis ships the format and births the place. Ratified as the C-123 slate on Max's *"perfect, go"*.
