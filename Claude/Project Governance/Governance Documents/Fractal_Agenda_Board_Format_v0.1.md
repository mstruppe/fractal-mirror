# Fractal Agenda Board Format v0.1

> **CANONICAL SPECIFICATION (Ratified 2026-08-16, C-104, per Protocol v0.46).** The standard format of the Agenda Board — the human's at-a-glance window on fast AI work (C-102's speed asymmetry). One prose contract + one working HTML skeleton, versioned together (the C-040 coupling pattern, the Fieldnote Format's sibling). Instance-neutral by design: the mother, every child, and every newborn render the same shape over their own content.

**Version:** 0.1 · **Status:** Ratified (2026-08-16, in-conversation per C-033 — C-104, per Protocol v0.46) · **Reviewed By:** Max (2026-08-16 — the format directive of record: *"I really liked your version… definitely hardwire it into the system"*) · **Domain:** CTX · **Author:** Claude (forged from the mother's board of record) · **Date:** 2026-08-16 · **Document ID:** DOC-01M062T3RT8S846FT0K7S43FVS

---

## 1 · The contract (rules, kernel-grade)

1. **The board is a derived projection and is never authoritative** (C-003 class). It projects the instance's Local Context (which draws on the Register and the protocols). When the board and its sources disagree, the sources are right and the board is stale.
2. **File-first** (C-048): the board is a repo-resident file at `Claude/Context Packages/<Instance>_Agenda_Board.html`. The file is the rendering of record; publishing it as a private web artifact is optional and additive (republish to the *same* artifact URL, never a second one — record the URL beside the board, the KNet Board-README pattern).
3. **Regenerated at close** — after the living-projection checklist is walked, not before, so it reflects the state the close actually landed on.
4. **Offered actively** (C-102): the agent surfaces the board **by name, unprompted**, when open threads accumulate — the board is the human's window; waiting for felt absence makes humans reinvent it.
5. **Stamped**: the header names the source projection and its version + date; a stale stamp *is* the divergence signal (C-035).

## 2 · The section grammar (top to bottom)

| # | Section | Marker | Content rule |
|---|---|---|---|
| 1 | **Header** | kicker + h1 + sub | Kicker: `<INSTANCE> · Agenda Board`. Sub: *Projection of <source> v<X>, <date> — derived, never authoritative*. |
| 2 | **Done bar** | `.donebar` chips | Completed work as ✓ chips, chronological, with decision refs. Append-only in spirit — the instance's visible biography. Compact older eras into summary chips when the bar outgrows a screen (C-095 discipline). |
| 3 | **The NEXT card** | `.card.next` (accent border) | Exactly one. The queue's head: what the next session opens onto. Context prose (`.sev`) quoting the human's own directives where they exist, then bullets. Ends with the standing `.opening` line: how to open a session and where it lands. |
| 4 | **Program / workstream cards** | `.card` + badge | One card per running program or workstream. Badges: `Next` (accent) · `Queued` (warm) · `Parked` (grey) · `Offers` (violet). Bullets carry refs (`C-#`, `OQ-#`, findings) in `.ref` spans. |
| 5 | **Standing open questions** | `.card` + `Parked` badge | The OQ ledger's live rows, grouped, with their triggers. "Idle by design — non-blocking." |
| 6 | **Offers card** | `.card` + `Offers` badge | Everything on the human's call — the C-031 posture made visible: the queue is an offer, never a mandate. |
| 7 | **Legend** | `.card` | "Where the numbers root": what `C-#` / `OQ-#` / finding ids mean *in this instance*, and the one lookup home (the Register). |
| 8 | **Footer** | `.footer` | The stamp: source path, regeneration rule, active-offer note (C-102), and the instance's one-line state (store counts, checkers green, operating surface). |

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
  .donebar { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; background: var(--card);
    border: 1px solid var(--line); border-radius: 12px; padding: 12px 16px; margin: 22px 0 26px; font-size: 13.5px; }
  .donebar .label { color: var(--muted); }
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

  <div class="donebar">
    <span class="label">Complete &amp; ratified:</span>
    <span class="chip">{{DONE_CHIP — one per completed act, chronological, with refs}}</span>
  </div>

  <div class="card next">
    <div class="card-head">
      <h2>{{THE QUEUE'S HEAD — one sentence}}</h2>
      <span class="badge b-next">Next</span>
    </div>
    <div class="sev">{{CONTEXT PROSE — quote the owner's own directives where they exist}}</div>
    <ul>
      <li>{{NEXT ITEM — bold lead, refs in <span class="ref">…</span>}}</li>
    </ul>
    <div class="opening"><b>To open:</b> {{how a session opens in this instance and where it lands; end with the close command}}</div>
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

- **An existing instance** (e.g. KNet): a session in *that* instance reads this file from the mother's tree (read any repo you can see; adopt in — and only in — your own jurisdiction), records the adoption as its own decision, and regenerates its board file in this format at its next close, over its own content and sources. Rendering to a private web artifact stays that instance's option (keep its republish-URL note beside the board).
- **A newborn**: hardwire path — genesis ships this format so every instance is born with the board standard (queued as a kernel decision at the mother's next close; complements C-102's active-offer duty and GENESIS §5's board row).
- **This instance** (the mother): already conformant — the skeleton above *is* its board of record, made instance-neutral.

---

**Refresh triggers:** a change to the board contract (C-047/C-048/C-102 class), a section-grammar change proven in the field, a palette/skeleton change adopted by decision. Format changes are new versions of this file (C-040); instances adopt by their own decision — the constitution model applies to formats too.
**Sources:** the mother's board of record (`User Documents/Fractal_Agenda_Board.html` — path current since C-126; fourteenth-session issue, then at the Context Packages root); C-047/C-048 (the board, file-first); C-102 (offered actively — the speed asymmetry); C-095 (compaction discipline for the done bar); the KNet Board README (the republish-URL mechanics, observed through the C-096 window); Max's directive of record, 2026-08-16 (this session): the mother's format is the standard; hardwire it.
