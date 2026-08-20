# Fractal Agenda Board Format v0.3

> **CANONICAL SPECIFICATION (Ratified 2026-08-19, the twenty-ninth Code session — Max's "ratified" on the dedicated-folder direction; C-126; protocol at this session's close).** The standard format of the Agenda Board — the human's at-a-glance window on fast AI work (C-102's speed asymmetry). One prose contract + one working HTML skeleton, versioned together (the C-040 coupling pattern, the Fieldnote Format's sibling). Instance-neutral by design: the mother, every child, and every newborn render the same shape over their own content. **New in v0.3:** the board's home moves to the **`User Documents/` folder at the repo root** (C-126 — the human's own place in the folder system, openable without asking the AI; the Pair Procedure's location law), the user-document bar gains the **extension-pill provision** (banked at C-124, field-proven by the mother's fifth pill — the Update Plan — before entering this grammar, the C-094 path), and the done bar becomes a **rolling window** (C-128 — the newest ten chips on the surface; everything older falls verbatim to the board's **archive file**, one standing link away: nothing lost, nothing bulky).

**Version:** 0.3 · **Status:** Ratified (2026-08-19, in-conversation per C-033 — Max's "ratified" on the dedicated-folder proposal, C-126; the rolling window on his "go" the same session, C-128; protocol at this session's close) · **Reviewed By:** Max (2026-08-19 — the folder his direction of record: *"sometimes it would be simply easier to open the agenda board myself instead of asking you. therefore the user docs should have dedicated folder I can go to in the folder system"*) · **Domain:** CTX · **Author:** Claude (forged from the mother's board of record) · **Date:** 2026-08-19 · **Parent:** Fractal Context Index (routing) · C-104 (the canonization) · **Supersedes:** Fractal_Agenda_Board_Format_v0.2 (retained as history, its own DOC identity per C-061) · **Document ID:** DOC-01M0DJTAXKAVTH41267M6WBYK0 (minted at this close via `close.py --create`)

---

## 1 · The contract (rules, kernel-grade)

1. **The board is a derived projection and is never authoritative** (C-003 class). It projects the instance's Local Context (which draws on the Register and the protocols). When the board and its sources disagree, the sources are right and the board is stale.
2. **File-first** (C-048): the board is a repo-resident file at **`User Documents/<Instance>_Agenda_Board.html`** — the dedicated user-documents folder at the repo root (C-126: all user halves live together in the human's own folder, openable in the file system without asking the AI; governance originals stay in their natural homes — the Pair Procedure's location law). The file is the rendering of record; publishing it as a private web artifact is optional and additive (republish to the *same* artifact URL, never a second one — record the URL beside the board, the KNet Board-README pattern).
3. **Regenerated at close** — after the living-projection checklist is walked, not before, so it reflects the state the close actually landed on.
4. **Offered actively** (C-102): the agent surfaces the board **by name, unprompted**, when open threads accumulate — the board is the human's window; waiting for felt absence makes humans reinvent it.
5. **Stamped**: the header names the source projection and its version + date; a stale stamp *is* the divergence signal (C-035).

## 2 · The section grammar (top to bottom)

| # | Section | Marker | Content rule |
|---|---|---|---|
| 1 | **Header** | kicker + h1 + sub | Kicker: `<INSTANCE> · Agenda Board`. Sub: *Projection of <source> v<X>, <date> — derived, never authoritative*. |
| 2 | **User-document bar** *(v0.2; extension pills v0.3)* | `.trio` | The glance-path across the instance's user documents (C-122 — the board is the **dynamic pole** of the user spine): pill links in the standing order **board — the state · fieldnote buffer — the buffer · roadmap — the plan · handout — the manual**, the current page marked (`.here`). Board + buffer are the minimum every instance has; roadmap and handout link where they exist — delete absent entries. **Extension pairs (C-124) append their pills after the kernel four**, same grammar — `name — the <role>` — one pill per living extension, deleted when the pair retires (the mother's fifth: *update plan — the release lane*; field-proven 2026-08-19 per C-094 before entering this grammar). |
| 3 | **Done bar** | `.donebar` chips | Completed work as ✓ chips, chronological, with decision refs — the instance's visible biography. **The rolling window (C-128, v0.3):** the bar keeps only the **newest ten** chips; at each regeneration, anything older **falls verbatim** to the board's **archive** — a sibling file (`<Instance>_Agenda_Board_Archive.html`, same folder), append-only, newest-first — and the bar carries one standing link to it (*everything before — the archive*). The surface stays one glance; **nothing is lost twice over**: the archive keeps the chips verbatim, and the canonical history remains the protocol series. Already-compacted era chips fall as they are. (Replaces v0.2's compact-into-era-chips rule for the board surface; C-095 compaction stays the Local Context's own discipline. The archive is the board's attic, not a pair — no bar pill; a back-link to the board suffices.) |
| 4 | **The NEXT card** | `.card.next` (accent border) | **Default: exactly one** — the queue's head: what the next session opens onto. **The coequal-branch provision (v0.2, shipping-run FN-0005 — KNet's P-005 the specimen):** a project running coequal agenda branches (e.g. a literature arc beside an experimental arc) may carry **one NEXT-class card per branch, each ending in its own `.opening` resume line**. The split is an *agenda* shape, never a *session* shape — C-106's one-conversation-one-open-loop rule is untouched; each session still opens onto one branch's head. Context prose (`.sev`) quotes the human's own directives where they exist, then bullets. |
| 5 | **Program / workstream cards** | `.card` + badge | One card per running program or workstream. Badges: `Next` (accent) · `Queued` (warm) · `Parked` (grey) · `Offers` (violet). Bullets carry refs (`C-#`, `OQ-#`, findings) in `.ref` spans. |
| 6 | **Standing open questions** | `.card` + `Parked` badge | The OQ ledger's live rows, grouped, with their triggers. "Idle by design — non-blocking." |
| 7 | **Offers card** | `.card` + `Offers` badge | Everything on the human's call — the C-031 posture made visible: the queue is an offer, never a mandate. |
| 8 | **Legend** | `.card` | "Where the numbers root": what `C-#` / `OQ-#` / finding ids mean *in this instance*, and the one lookup home (the Register). |
| 9 | **Footer** | `.footer` | The stamp: source path, regeneration rule, active-offer note (C-102), and the instance's one-line state (store counts, checkers green, operating surface). |

**Voice:** second person to the owner ("your call", "your triage answered") — the board speaks to its human, not about them. **Severity/status coloring** comes only from the palette tokens below; no ad-hoc colors.

## 3 · The skeleton (the working half — copy, fill the `{{SLOTS}}`, delete unused cards)

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{INSTANCE}} — Agenda Overview</title>
<style>
  :root {
    --bg: #f7f6f3; --card: #ffffff; --ink: #1a1a1e; --muted: #6b6b74;
    --line: #e6e4de; --accent: #2f6fed; --done: #3a9d6e;
    --high: #c0563a; --med: #c78a2d; --low: #8a8a94; --offer: #7a5fb5;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #17171a; --card: #202024; --ink: #ececef; --muted: #9b9ba5;
      --line: #313138; --accent: #6b9bff; --done: #55b98a;
      --high: #e07a5c; --med: #d9a44a; --low: #8a8a94; --offer: #a68ae0;
    }
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
    background: var(--bg); color: var(--ink); line-height: 1.55; padding: 40px 24px 56px; }
  .wrap { max-width: 860px; margin: 0 auto; }
  header { margin-bottom: 28px; }
  .kicker { font-size: 12px; letter-spacing: 0.14em; text-transform: uppercase; color: var(--muted); margin-bottom: 6px; }
  h1 { font-size: 26px; font-weight: 650; letter-spacing: -0.01em; }
  .sub { color: var(--muted); font-size: 14px; margin-top: 6px; }
  .trio { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; margin: 0 0 20px; font-size: 12.5px; }
  .trio .lbl { color: var(--muted); font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase; margin-right: 2px; }
  .trio a, .trio .here { border: 1px solid var(--line); border-radius: 999px; padding: 4px 12px;
    color: var(--muted); text-decoration: none; background: var(--card); }
  .trio a:hover { color: var(--ink); border-color: var(--muted); }
  .trio .here { color: var(--accent); border-color: var(--accent); font-weight: 650; }
  .donebar { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; background: var(--card);
    border: 1px solid var(--line); border-radius: 12px; padding: 12px 16px; margin: 22px 0 26px; font-size: 13.5px; }
  .donebar .label { color: var(--muted); }
  .donebar .archive-link { color: var(--muted); font-size: 12.5px; text-decoration: none;
    border-bottom: 1px dotted var(--muted); }
  .donebar .archive-link:hover { color: var(--ink); border-bottom-color: var(--ink); }
  .chip { display: inline-flex; align-items: center; gap: 6px;
    background: color-mix(in srgb, var(--done) 12%, transparent); color: var(--done);
    border-radius: 999px; padding: 3px 11px; font-weight: 600; font-size: 12.5px; }
  .chip::before { content: "✓"; font-size: 11px; }
  .card { background: var(--card); border: 1px solid var(--line); border-radius: 14px; padding: 22px 24px; margin-bottom: 18px; }
  .card.next { border-left: 4px solid var(--accent); }
  .card-head { display: flex; align-items: baseline; gap: 12px; flex-wrap: wrap; margin-bottom: 4px; }
  .ws-letter { font-size: 13px; font-weight: 700; color: var(--muted); letter-spacing: 0.08em; }
  h2 { font-size: 17.5px; font-weight: 650; }
  .badge { font-size: 11px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase;
    border-radius: 999px; padding: 3px 10px; margin-left: auto; }
  .b-next { background: color-mix(in srgb, var(--accent) 14%, transparent); color: var(--accent); }
  .b-queued { background: color-mix(in srgb, var(--high) 13%, transparent); color: var(--high); }
  .b-parked { background: color-mix(in srgb, var(--low) 16%, transparent); color: var(--low); }
  .b-offer { background: color-mix(in srgb, var(--offer) 14%, transparent); color: var(--offer); }
  .b-done { background: var(--done); color: #fff; }
  .sev { font-size: 12.5px; color: var(--muted); margin-bottom: 12px; }
  ul { list-style: none; margin-top: 10px; }
  li { padding: 7px 0 7px 22px; position: relative; font-size: 14.5px;
    border-top: 1px solid color-mix(in srgb, var(--line) 55%, transparent); }
  li:first-child { border-top: none; }
  li::before { content: ""; position: absolute; left: 4px; top: 15px;
    width: 6px; height: 6px; border-radius: 50%; background: var(--muted); }
  .card.next li::before { background: var(--accent); }
  .ref { color: var(--muted); font-size: 13px; }
  .note { margin-top: 12px; font-size: 13.5px; color: var(--muted);
    background: color-mix(in srgb, var(--line) 40%, transparent); border-radius: 8px; padding: 9px 13px; }
  .opening { margin-top: 14px; font-size: 13.5px; border-top: 1px dashed var(--line); padding-top: 12px; color: var(--muted); }
  .opening b { color: var(--ink); font-weight: 600; }
  footer { margin-top: 26px; font-size: 12.5px; color: var(--muted); }
  code { font-family: ui-monospace, "SF Mono", Menlo, monospace; font-size: 0.92em;
    background: color-mix(in srgb, var(--line) 50%, transparent); padding: 1px 5px; border-radius: 5px; }
</style>
</head>
<body>
<div class="wrap">

  <header>
    <div class="kicker">{{INSTANCE}} · Agenda Board</div>
    <h1>Agenda Overview</h1>
    <div class="sub">Projection of {{SOURCE_PROJECTION}} <b>v{{SOURCE_VERSION}}</b>, {{DATE}} — derived, never authoritative; stale stamp = divergence</div>
  </header>

  <nav class="trio" aria-label="The user-document bar">
    <span class="lbl">Your documents</span>
    <span class="here">Board — the state</span>
    <a href="{{BUFFER_PATH — e.g. ../Site/Fieldnotes.md}}">Fieldnotes — the buffer</a>
    <a href="{{ROADMAP_FILE — delete this entry if the instance has none}}">Roadmap — the plan</a>
    <a href="{{HANDOUT_FILE — delete this entry if the instance has none}}">Handout — the manual</a>
    <a href="{{EXTENSION_FILE — one pill per living extension pair (C-124), after the kernel four; delete when none}}">{{Extension name — the role}}</a>
  </nav>

  <div class="donebar">
    <span class="label">Complete &amp; ratified:</span>
    <a class="archive-link" href="{{ARCHIVE_FILE — <Instance>_Agenda_Board_Archive.html; omit this link until the first chip falls}}">everything before — the archive</a>
    <span class="chip">{{DONE_CHIP — the newest ten, chronological, with refs; older chips fall verbatim to the archive}}</span>
  </div>

  <div class="card next">
    <div class="card-head">
      <h2>{{THE QUEUE'S HEAD — one sentence; one card per coequal branch if the agenda runs branches}}</h2>
      <span class="badge b-next">Next</span>
    </div>
    <div class="sev">{{CONTEXT PROSE — quote the owner's own directives where they exist}}</div>
    <ul>
      <li>{{NEXT ITEM — bold lead, refs in <span class="ref">…</span>}}</li>
    </ul>
    <div class="opening"><b>To open:</b> {{how a session opens onto this branch and where it lands; end with the close command}}</div>
  </div>

  <div class="card">
    <div class="card-head">
      <span class="ws-letter">{{LETTER (optional)}}</span>
      <h2>{{PROGRAM / WORKSTREAM NAME}}</h2>
      <span class="badge b-queued">{{Queued / Parked / Offers}}</span>
    </div>
    <div class="sev">{{one-line status}}</div>
    <ul><li>{{items}}</li></ul>
    <div class="note">{{optional standing note}}</div>
  </div>

  <div class="card">
    <div class="card-head"><h2>Standing open questions</h2><span class="badge b-parked">Parked</span></div>
    <div class="sev">Idle by design — non-blocking</div>
    <ul><li>{{OQ rows with triggers}}</li></ul>
  </div>

  <div class="card">
    <div class="card-head"><h2>Where the numbers root</h2><span class="badge b-parked">Legend</span></div>
    <ul><li>{{what C-# / OQ-# / finding ids mean in THIS instance; the one lookup home}}</li></ul>
  </div>

  <footer>
    Standing stamped projection — source file: <code>{{PATH}}</code>, regenerated file-first at close whenever the agenda changes; offered actively at tracking need (C-102 class) · {{INSTANCE_STATE_ONE_LINER — store counts, checkers, operating surface}}
  </footer>

</div>
</body>
</html>
```

## 4 · Adoption

- **An existing instance** (e.g. KNet): a session in *that* instance reads this file from the mother's tree (read any repo you can see; adopt in — and only in — your own jurisdiction), records the adoption as its own decision, and regenerates its board file in this format at its next close, over its own content and sources. **Adopting v0.3 includes the move:** the board (and every other user half) relocates to `User Documents/` at the repo root — one `git mv`, relative links re-based; until the instance adopts, its tooling pinned to an older kernel keeps the old path (the release seam's §8 advisory names the move, C-117). Rendering to a private web artifact stays that instance's option (keep its republish-URL note beside the board).
- **A newborn**: hardwire path — genesis ships this format so every instance is born with the board standard (the GENESIS §5 board row; complements C-102's active-offer duty). **The folder is not pre-scaffolded:** `User Documents/` appears the day the instance renders its first user half (C-126 — passive structure, born on use).
- **This instance** (the mother): already conformant — the skeleton above *is* its board of record, made instance-neutral; the bar rode the board one regeneration ahead of the v0.2 reissue (the field trial), and the fifth pill + the folder rode ahead of this one (the same C-094 path).

---

**Refresh triggers:** a change to the board contract (C-047/C-048/C-102 class), a section-grammar change proven in the field, a palette/skeleton change adopted by decision. Format changes are new versions of this file (C-040); instances adopt by their own decision — the constitution model applies to formats too.
**Sources:** Fractal_Agenda_Board_Format_v0.1 (the base, C-104 — Max's directive of record: the mother's format is the standard; hardwire it) and v0.2 (the bar + the branch provision); the mother's board of record (`User Documents/Fractal_Agenda_Board.html` — the trio bar's field trial, 2026-08-19, C-094); **C-126** (the dedicated folder — Max's direction of record) + the Pair Procedure's location law (`Fractal_User_Document_Pair_Procedure_v0.2` §2); **C-128** (the rolling window — Max's direction of record: *"only keeps a certain amount of latest complete & ratification, while the older ones fall… instead of the bulk of old checks there is a link to an archive. so nothing is lost but doesn't need to stay on the surface"*; the C-121 RAM pattern applied to the done bar); **C-122** (the mirror doctrine — the user spine, the board its dynamic pole); **C-121** (the buffer the bar links); **C-124** (the pair series — the extension-pill provision banked there, landed here); shipping-run FN-0005 (the two-path agenda pattern — dissolved into v0.2; frozen home `Site/Fieldnotes_2026-08-15_First-Shipping-Run.md`); C-106 (one conversation, one open loop — deliberately untouched by the branch provision); the KNet Board README (the republish-URL mechanics, observed through the C-096 window).
**Revision history:** v0.1 (2026-08-16) first issue — the mother's board canonized as the standard (C-104, per Protocol v0.46). · v0.2 (2026-08-19) **the work-down reissue (the C-121 buffer's first work-down, "full slate" on Max's word):** the **user-document bar** enters the grammar (§2 row 2 — the C-122 mirror's glance-path, field-proven on the mother's board the same day per C-094 before entering the standard) and the NEXT card gains the **coequal-branch provision** (§2 row 4 — shipping-run FN-0005 dissolved here: one NEXT-class card per coequal branch, each with its own resume line; an agenda shape, never a session shape — C-106 untouched). Contract and adoption rules unchanged in substance; skeleton updated with the bar; grammar renumbered 1–9. · v0.3 (2026-08-19) **the dedicated-folder reissue (C-126 — Max's direction of record: the user docs get a folder the human can open themselves):** rule 2's home becomes **`User Documents/<Instance>_Agenda_Board.html`** at the repo root (all user halves live together in the human's own folder; originals stay in their natural homes — the Pair Procedure v0.2's location law, this Format's rule 2 its board-shaped face); the bar gains the **extension-pill provision** (§2 row 2 — banked at C-124, the mother's fifth pill the field proof; one pill per living extension pair, deleted at retirement); §4 adoption gains the move mechanics (existing instances: one `git mv` + link re-base at adoption; newborns: the folder born on first use, never pre-scaffolded). Contract otherwise unchanged; skeleton's buffer-path example re-based, extension slot added. **In the same issue (C-128 — Max's "go", the same session):** the done bar becomes a **rolling window** (§2 row 3) — newest ten on the surface, older chips falling verbatim to the sibling archive file, the standing link in the bar; supersedes the v0.2 era-compaction rule for the board surface (C-095 stays the Local Context's discipline); the mother's board brought conformant in the same act (54 chips → 10 + the archive born with 44).
