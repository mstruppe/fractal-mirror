/* FRACTAL · The Shell — hangar prototype (Workspace Foundation §6–§7, v0.3).
   Static, dependency-free, read-only. Two tiers, one frame:
   public tier = relative fetch beside the served shell; local tier = the browser's folder grant. */
'use strict';

/* ── the quest map (curated; paths relative to the estate root) ── */
const QUEST = [
  { chapter: 'User Documents', stations: [
    { title: 'The board', path: 'User Documents/Fractal_Agenda_Board.html', kind: 'html',
      blurb: 'State of work, session grain' },
    { title: 'The roadmap', path: 'User Documents/Fractal_Roadmap.html', kind: 'html',
      blurb: 'The trajectory, phase grain' },
    { title: 'The release lane', path: 'User Documents/Fractal_Update_Plan.html', kind: 'html',
      blurb: 'What ships next' },
    { title: 'The gas gauge', path: 'User Documents/Fractal_Gas_Gauge.html', kind: 'html',
      blurb: 'What the work costs' },
    { title: 'Field notes', path: 'User Documents/Fractal_Fieldnote_Handout.html', kind: 'html',
      blurb: 'The buffer & how to feed it' },
    { title: 'The birth guide', path: 'User Documents/Fractal_Birth_Guide.html', kind: 'html',
      blurb: 'Start your own instance, guided' },
  ]},
  { chapter: 'Help', sub: [
    { chapter: 'I · Orient', stations: [
      { title: 'What is this place?', path: 'README.md', kind: 'md',
        blurb: 'The gate — FRACTAL compressed' },
      { title: 'The vision', path: 'Claude/Context Packages/Global/Fractal_Global_Context.md', kind: 'md',
        blurb: 'Why it exists · where it stands' },
    ]},
    { chapter: 'II · The Law', stations: [
      { title: 'The rules at a glance', path: 'Claude/Project Governance/Governance Documents/Fractal_Rule_Overview.md', kind: 'md',
        blurb: 'The one-page rule-book' },
      { title: 'Where we look right now', path: 'Claude/Context Packages/Local/Fractal_Local_Context_Knowledge_Graph.md', kind: 'md',
        blurb: 'The active Local Context' },
    ]},
    { chapter: 'III · The Machine', stations: [
      { title: 'The architecture map', path: 'Claude/Architecture/Architecture State/Fractal_Architecture_State.md', kind: 'md',
        blurb: 'The living canonical model' },
      { title: 'The birth door', path: 'GENESIS.md', kind: 'md',
        blurb: 'Start your own instance' },
    ]},
  ]},
];

const SKIP_DIRS = new Set(['node_modules', '.git', '.claude', '__pycache__']);
const TEXT_EXT = new Set(['txt', 'py', 'json', 'yml', 'yaml', 'csv', 'sh', 'css', 'js', 'ots', 'asc', 'sig', 'gitignore']);

const els = {
  quest: document.getElementById('quest'),
  content: document.getElementById('content'),
  status: document.getElementById('status'),
  tierLocal: document.getElementById('tier-local'),
  explorerWrap: document.getElementById('explorer-wrap'),
  explorer: document.getElementById('explorer'),
  rootName: document.getElementById('root-name'),
  cockpit: document.getElementById('cockpit'),
  cockpitHead: document.getElementById('cockpit-head'),
  rider: document.getElementById('rider'),
  riderMini: document.getElementById('rider-mini'),
  riderPane: document.getElementById('rider-pane'),
  winShadow: document.getElementById('win-shadow'),
  cpToPane: document.getElementById('cp-to-pane'),
  cpHome: document.getElementById('cp-home'),
  cpToWindow: document.getElementById('cp-to-window'),
  cpFold: document.getElementById('cp-fold'),
  readerBtn: document.getElementById('reader-btn'),
  layoutBtn: document.getElementById('layout-btn'),
  layoutMenu: document.getElementById('layout-menu'),
  cockpitState: document.getElementById('cockpit-state'),
  cockpitLog: document.getElementById('cockpit-log'),
  cockpitForm: document.getElementById('cockpit-form'),
  cockpitInput: document.getElementById('cockpit-input'),
  cockpitSend: document.getElementById('cockpit-send'),
  cockpitStop: document.getElementById('cockpit-stop'),
};

const state = {
  tier: 'public',                                // 'public' | 'local'
  root: null,                                    // FileSystemDirectoryHandle once granted
  publicBase: new URL('../../', location.href),  // the estate root, when served beside it
  activeBtn: null,
};

/* the rider grammar (Max's sketch, 2026-08-27; simplified same day): the workspace
   BORDERS are the dock — all four magnetic, for the rider and for the window's edges;
   no bar object. One cockpit, three states — rider (folded, resting on a border) ·
   window (floating; "mini" = the same window with one border held on a workspace
   border, a corner held by two) · pane (in the layout flow). */
const TOPBAR = 46, SNAP = 37;                    // px — the magnetic reach (32 +15%, Max's call)
const WIN_DEF = { w: 400, h: 460 };              // the one default window size (button unfolds)
const WIN_MIN = { w: 300, h: 260 };

let dragV = 0;                                   // smoothed pointer speed of the live drag, px/ms
let reflowInput = () => {};                      // re-clamps the composer; bound by initInputResize
/* the magnet's ATTACH reach grows with drag intensity — a fling toward a border
   docks from further out; detach thresholds stay at base SNAP, so pulling off
   stays predictable (velocity reads intent, length would punish deliberate moves) */
function reach() { return SNAP * (1 + Math.min(dragV / 2, 1) * 0.75); }

const dk = { edge: 'bottom', t: 0.8 };           // the rider's home: which border, how far along

const cp = {                                     // cockpit state (summonable-pane #1)
  state: 'rider',         // 'rider' | 'window' | 'pane'
  attSides: [],           // window sub-property: borders currently held (≤2 — one per axis)
  win: { x: 0, y: 0, w: 400, h: 460 },
  live: false, es: null, turn: false,
  layout: 'cr',           // derived by the position law at each unfold; feeds the split glyphs
  agentEl: null,          // the streaming agent-text element of the current turn
};

const rd = {                                     // reader state (the document window)
  open: true, reopen: null, station: null,
};

/* ── boot ── */
buildQuest();
els.tierLocal.addEventListener('click', useLocalTier);
initTheme();
initNavResize();
initCockpit();
initLayoutMenu();
initReader();
setStatus(`published estate · root ${state.publicBase.pathname}`);

/* ── the rail's width (drag 180–300px; the text keeps its design width and clips) ── */
function initNavResize() {
  const KEY = 'fractal-shell-navw';
  const MIN = 180, MAX = 300;
  const root = document.documentElement;
  const handle = document.getElementById('nav-resize');
  let w = 300;
  try { w = parseInt(localStorage.getItem(KEY), 10) || 300; } catch {}
  const set = v => {
    w = Math.max(MIN, Math.min(MAX, v));
    root.style.setProperty('--nav-w', w + 'px');
  };
  const remember = () => { try { localStorage.setItem(KEY, String(w)); } catch {} };
  set(w);
  let startX = 0, startW = 0;
  handle.addEventListener('pointerdown', e => {
    startX = e.clientX; startW = w;
    handle.setPointerCapture(e.pointerId);
    document.body.classList.add('resizing');
  });
  handle.addEventListener('pointermove', e => {
    if (!handle.hasPointerCapture(e.pointerId)) return;
    set(startW + e.clientX - startX);
  });
  const end = e => {
    if (handle.hasPointerCapture(e.pointerId)) handle.releasePointerCapture(e.pointerId);
    document.body.classList.remove('resizing');
    remember();
  };
  handle.addEventListener('pointerup', end);
  handle.addEventListener('pointercancel', end);
  handle.addEventListener('dblclick', () => { set(300); remember(); });
}

/* ── appearance (auto ◐ → light ○ → dark ●; remembered locally, never written to the estate) ── */
function initTheme() {
  const btn = document.getElementById('theme');
  const KEY = 'fractal-shell-theme';
  const GLYPH = { auto: '◐', light: '○', dark: '●' };
  let mode;
  try { mode = localStorage.getItem(KEY) || 'auto'; } catch { mode = 'auto'; }
  const apply = () => {
    if (mode === 'auto') document.documentElement.removeAttribute('data-theme');
    else document.documentElement.setAttribute('data-theme', mode);
    btn.textContent = GLYPH[mode];
    btn.title = 'Appearance: ' + mode;
  };
  apply();
  btn.addEventListener('click', () => {
    mode = mode === 'auto' ? 'light' : mode === 'light' ? 'dark' : 'auto';
    try { localStorage.setItem(KEY, mode); } catch {}
    apply();
  });
}

/* ── tiers — the published estate is the GROUND STATE, not a mode (Max's call,
      2026-08-27): no button switches to it; the shell stands on it before any
      grant, and a granted read that misses falls back to it by itself.
      Reload = back on the ground (a folder grant is per-session by design). ── */
async function useLocalTier() {
  if (!window.showDirectoryPicker) {
    setStatus('this browser has no folder-grant API — the local tier needs a Chromium browser (Chrome, Edge, Arc) for now', true);
    return;
  }
  try {
    const handle = await window.showDirectoryPicker({ mode: 'read' });
    state.root = handle;
    state.tier = 'local';
    reflectTier();
    els.rootName.textContent = '· ' + handle.name;
    els.explorer.replaceChildren(await dirNode(handle, ''));
    setStatus(`your instance · reading “${handle.name}” (nothing is ever written)`);
  } catch (e) {
    if (e.name !== 'AbortError') setStatus('folder grant failed: ' + e.message, true);
  }
}

function reflectTier() {
  els.tierLocal.classList.toggle('active', state.tier === 'local');
  els.explorerWrap.hidden = state.tier !== 'local';
}

/* ── quest nav (groups closed by default — only the headlines; openings remembered locally; nests) ── */
function buildQuest() {
  const KEY = 'fractal-shell-open';
  let opened = new Set();
  try { opened = new Set(JSON.parse(localStorage.getItem(KEY) || '[]')); } catch {}
  try { localStorage.removeItem('fractal-shell-collapsed'); } catch {}   // pre-inversion key, retired
  const make = ch => {
    const det = document.createElement('details');
    det.className = 'chapter';
    det.open = opened.has(ch.chapter);
    const sum = document.createElement('summary');
    sum.textContent = ch.chapter;
    det.appendChild(sum);
    for (const sc of ch.sub || []) det.appendChild(make(sc));
    for (const st of ch.stations || []) {
      const b = document.createElement('button');
      b.className = 'station';
      b.innerHTML = `${escapeHtml(st.title)}<span class="blurb">${escapeHtml(st.blurb)}</span>`;
      b.addEventListener('click', () => openStation(st, b));
      det.appendChild(b);
    }
    det.addEventListener('toggle', () => {
      if (det.open) opened.add(ch.chapter); else opened.delete(ch.chapter);
      try { localStorage.setItem(KEY, JSON.stringify([...opened])); } catch {}
    });
    return det;
  };
  for (const ch of QUEST) els.quest.appendChild(make(ch));
}

async function openStation(st, btn) {
  if (state.activeBtn) state.activeBtn.classList.remove('active');
  state.activeBtn = btn || null;
  if (btn) btn.classList.add('active');
  try {
    setStatus('opening ' + st.path + ' …');
    let read = state.tier === 'local' ? 'your instance' : 'published';
    if (st.kind === 'html') {
      if (state.tier === 'public') showFrameSrc(publicUrl(st.path));
      else {
        try { showFrameDoc(await readLocalText(st.path)); }
        catch { showFrameSrc(publicUrl(st.path)); read = 'published (not in your folder)'; }
      }
    } else {
      let text;
      if (state.tier === 'public') text = await fetchPublic(st.path);
      else {
        try { text = await readLocalText(st.path); }
        catch { text = await fetchPublic(st.path); read = 'published (not in your folder)'; }
      }
      showMarkdown(text);
    }
    readerShowing(() => openStation(st, btn), state.tier === 'public' ? st : null);
    setStatus(`${read} · ${st.path}`);
  } catch (e) {
    showMessage(`Could not open <b>${escapeHtml(st.title)}</b>`, e.message +
      (state.tier === 'public'
        ? '<br><span class="hint">This station may not be published at this address. Granting your instance folder (“My instance…”) reads it from your own machine.</span>'
        : '<br><span class="hint">Not in the granted folder, and not published beside this shell either. Is the granted folder the estate root (the folder holding README.md and GENESIS.md)?</span>'));
    setStatus(e.message, true);
  }
}

/* ── data: public tier ── */
function publicUrl(path) {
  return new URL(path.split('/').map(encodeURIComponent).join('/'), state.publicBase).href;
}
async function fetchPublic(path) {
  const r = await fetch(publicUrl(path));
  if (!r.ok) throw new Error(`${r.status} ${r.statusText} — ${path}`);
  return r.text();
}

/* ── data: local tier ── */
async function readLocalText(path) {
  if (!state.root) throw new Error('no instance folder granted yet — click “My instance…”');
  const parts = path.split('/');
  let dir = state.root;
  for (let i = 0; i < parts.length - 1; i++) dir = await dir.getDirectoryHandle(parts[i]);
  const fh = await dir.getFileHandle(parts[parts.length - 1]);
  return (await fh.getFile()).text();
}

/* ── explorer (local tier) ── */
async function dirNode(handle, path) {
  const frag = document.createDocumentFragment();
  const entries = [];
  for await (const e of handle.values()) entries.push(e);
  entries.sort((a, b) => (a.kind !== b.kind) ? (a.kind === 'directory' ? -1 : 1) : a.name.localeCompare(b.name));
  for (const e of entries) {
    if (e.name.startsWith('.DS_Store') || SKIP_DIRS.has(e.name)) continue;
    const childPath = path ? path + '/' + e.name : e.name;
    if (e.kind === 'directory') {
      const det = document.createElement('details');
      const sum = document.createElement('summary');
      sum.textContent = e.name;
      det.appendChild(sum);
      let loaded = false;
      det.addEventListener('toggle', async () => {
        if (det.open && !loaded) { loaded = true; det.appendChild(await dirNode(e, childPath)); }
      });
      frag.appendChild(det);
    } else {
      const b = document.createElement('button');
      b.className = 'file-btn';
      b.textContent = e.name;
      b.title = childPath;
      b.addEventListener('click', () => openLocalFile(childPath, e.name));
      frag.appendChild(b);
    }
  }
  return frag;
}

async function openLocalFile(path, name) {
  if (state.activeBtn) { state.activeBtn.classList.remove('active'); state.activeBtn = null; }
  const ext = (name.split('.').pop() || '').toLowerCase();
  try {
    if (ext === 'html' || ext === 'htm') showFrameDoc(await readLocalText(path));
    else if (ext === 'md') showMarkdown(await readLocalText(path));
    else if (TEXT_EXT.has(ext) || !name.includes('.')) showPlain(await readLocalText(path));
    else showMessage(escapeHtml(name), 'No renderer for this file type yet — the shell is a prototype; the quest map is its paved road.');
    readerShowing(() => openLocalFile(path, name), null);
    setStatus(`your instance · ${path}`);
  } catch (e) { setStatus(e.message, true); }
}

/* ── renderers ── */
function showFrameSrc(url) {
  const f = document.createElement('iframe');
  f.src = url;
  els.content.replaceChildren(f);
}
function showFrameDoc(text) {
  const f = document.createElement('iframe');
  f.sandbox = 'allow-same-origin';   // static render; scripts off in locally-read docs
  f.srcdoc = text;
  els.content.replaceChildren(f);
}
function showMarkdown(text) {
  const wrap = document.createElement('div');
  wrap.className = 'reader';
  const art = document.createElement('article');
  art.innerHTML = mdToHtml(text);
  wrap.appendChild(art);
  els.content.replaceChildren(wrap);
  wrap.scrollTop = 0;
}
function showPlain(text) {
  const wrap = document.createElement('div');
  wrap.className = 'reader';
  const art = document.createElement('article');
  const pre = document.createElement('pre');
  pre.textContent = text;
  art.appendChild(pre);
  wrap.appendChild(art);
  els.content.replaceChildren(wrap);
}
function showMessage(title, html) {
  const wrap = document.createElement('div');
  wrap.className = 'reader welcome';
  wrap.innerHTML = `<article><h1>${title}</h1><p>${html}</p></article>`;
  els.content.replaceChildren(wrap);
}
function showVoid() {
  // the reader closed or empty → the bare background (Max's call, 2026-08-26).
  // #screen-idle is the mount for the subtle graphics that may live here later.
  const idle = document.createElement('div');
  idle.id = 'screen-idle';
  els.content.replaceChildren(idle);
}

/* ── the reader — the document window (Max's naming, 2026-08-26): one estate
      artifact at a time, rendered readable; everything the rail points at
      opens in it. A window like every other: open, close, arrange —
      closing yields the screen to the void; opening restores what was read. ── */
function initReader() {
  els.readerBtn.addEventListener('click', readerToggle);
  let saved = null;
  try { saved = JSON.parse(localStorage.getItem('fractal-shell-reader') || 'null'); } catch {}
  if (saved && saved.open === false) rd.open = false;
  if (saved && saved.station) {            // remember the station even while closed,
    rd.station = saved.station;            // so close → reload → open restores it
    rd.reopen = () => openStation(saved.station, null);
  }
  if (rd.open && rd.reopen) rd.reopen();    // opening restores what was read
  else showVoid();
  reflectReader();
}

function readerToggle() {
  rd.open = !rd.open;
  if (!rd.open) {
    if (state.activeBtn) { state.activeBtn.classList.remove('active'); state.activeBtn = null; }
    showVoid();
    setStatus('reader closed');
  } else if (rd.reopen) {
    rd.reopen();
  } else {
    setStatus('reader open — choose a station from the rail');
  }
  reflectReader();
  readerRemember();
}

function reflectReader() { els.readerBtn.classList.toggle('on', rd.open); }

function readerRemember() {
  try {
    localStorage.setItem('fractal-shell-reader',
      JSON.stringify({ open: rd.open, station: rd.station }));
  } catch {}
}

function readerShowing(reopen, station) {
  // every successful render reports here — the reader knows what it holds
  rd.open = true;
  rd.reopen = reopen;
  rd.station = station || null;
  reflectReader();
  readerRemember();
}

/* ── status ── */
function setStatus(msg, isErr) {
  els.status.textContent = msg;
  els.status.classList.toggle('err', !!isErr);
}

/* ── the cockpit — summonable-pane #1, speaking the vendor-neutral /engine/* seam.
      Live only when this page is served by the engine room (same origin, by design);
      anywhere else the seat is a door, never an engine. The pane writes nothing —
      the engine's agent acts, and only through the in-pane C-008 permission moment.
      Rituals stay words: /fractal and /close are typed, never buttons.

      The rider grammar (2026-08-27): the cockpit's home is a RIDER on a general DOCK.
      Buttons are the fixed layer — deterministic paths, the one default window size;
      drags are the free layer — slide, detach, attach, move, resize, all magnetic.
      Position is law: where the cockpit sits decides the side it unfolds to. ── */
function initCockpit() {
  els.cockpitSend.disabled = true;               // enabled by the first snapshot — live seats only
  els.cockpitForm.addEventListener('submit', e => { e.preventDefault(); cockpitSend(); });
  els.cockpitInput.addEventListener('keydown', e => {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); cockpitSend(); }
  });
  els.cockpitStop.addEventListener('click', () => enginePost('/engine/interrupt', {}));
  initCockpitResize();
  initRider();
  initWindowChrome();
  initInputResize();

  // restore the home + the state (migrates the pre-rider keys: layout → home, open → pane)
  try {
    const d = JSON.parse(localStorage.getItem('fractal-shell-dock') || 'null');
    if (d && ['top', 'bottom', 'left', 'right'].includes(d.edge)) {
      dk.edge = d.edge; dk.t = clamp01(+d.t || 0);
    } else if (localStorage.getItem('fractal-shell-layout') === 'cl') dk.t = 0.2;
  } catch {}
  let s = null, raw = null;
  try { raw = localStorage.getItem('fractal-shell-cockpit'); } catch {}
  if (raw === 'open') s = { state: 'pane' };
  else if (raw && raw !== 'closed') { try { s = JSON.parse(raw); } catch {} }
  if (s && ['rider', 'window', 'pane'].includes(s.state)) {
    cp.attSides = Array.isArray(s.attSides)
      ? s.attSides.filter(x => ['top', 'bottom', 'left', 'right'].includes(x)) : [];
    if (s.layout === 'cl' || s.layout === 'cr') cp.layout = s.layout;   // the decided side survives
    if (s.win && +s.win.w) cp.win = {
      x: +s.win.x || 0, y: +s.win.y || 0,
      w: +s.win.w || WIN_DEF.w, h: +s.win.h || WIN_DEF.h,
    };
    setState(s.state);
  } else setState('rider');
}

function clamp01(v) { return Math.max(0, Math.min(1, v)); }
function clampN(v, lo, hi) { return Math.max(lo, Math.min(hi, v)); }
function horizontal() { return dk.edge === 'top' || dk.edge === 'bottom'; }

/* the workspace box — below the topbar, beside the rail; its four borders are the dock */
function workspace() {
  const navw = window.innerWidth <= 760 ? 0 :
    (parseInt(getComputedStyle(document.documentElement).getPropertyValue('--nav-w'), 10) || 300);
  return { x: navw, y: TOPBAR, w: window.innerWidth - navw, h: window.innerHeight - TOPBAR };
}

/* one generic drag engine — a gesture may change its meaning mid-flight (rider → window);
   it also meters the pointer's smoothed velocity, which feeds the magnet's reach */
function startDrag(e, handlers) {
  e.preventDefault();
  document.body.classList.add('dragging');
  let lx = e.clientX, ly = e.clientY, lt = performance.now();
  dragV = 0;
  const move = ev => {
    const t = performance.now(), dt = Math.max(1, t - lt);
    dragV = 0.75 * dragV + 0.25 * (Math.hypot(ev.clientX - lx, ev.clientY - ly) / dt);
    lx = ev.clientX; ly = ev.clientY; lt = t;
    handlers.onMove && handlers.onMove(ev);
  };
  const up = ev => {
    window.removeEventListener('pointermove', move);
    window.removeEventListener('pointerup', up);
    window.removeEventListener('pointercancel', up);
    document.body.classList.remove('dragging');
    handlers.onEnd && handlers.onEnd(ev);
    dragV = 0;
  };
  window.addEventListener('pointermove', move);
  window.addEventListener('pointerup', up);
  window.addEventListener('pointercancel', up);
}

/* ── state — rider disconnects; window and pane share the living connection ── */
function setState(s) {
  cp.state = s;
  if (s !== 'rider' && !cp.es) cockpitConnect();
  if (s === 'rider' && cp.es) { cp.es.close(); cp.es = null; cp.live = false; }
  renderCockpit();
  rememberCockpit();
}

function rememberCockpit() {
  try {
    localStorage.setItem('fractal-shell-cockpit',
      JSON.stringify({ state: cp.state, attSides: cp.attSides, win: cp.win, layout: cp.layout }));
  } catch {}
}
function rememberHome() {
  try { localStorage.setItem('fractal-shell-dock', JSON.stringify({ edge: dk.edge, t: dk.t })); } catch {}
}

/* the position law — where the cockpit sits decides the side it unfolds to
   (a corner seat counts by its left/right member: bottom-left unfolds left) */
function paneSide() {
  if (cp.state === 'window') {
    if (cp.attSides.includes('left')) return 'cl';
    if (cp.attSides.includes('right')) return 'cr';
    const ws = workspace();
    return (cp.win.x + cp.win.w / 2) < (ws.x + ws.w / 2) ? 'cl' : 'cr';
  }
  if (dk.edge === 'left') return 'cl';
  if (dk.edge === 'right') return 'cr';
  return dk.t < 0.5 ? 'cl' : 'cr';
}

function applyLayout() {
  document.body.classList.toggle('cockpit-left', cp.layout === 'cl');
  els.layoutBtn.textContent = cp.layout === 'cl' ? '◧' : '◨';
}

/* ── rendering — one element, its presentation per state ── */
function renderCockpit() {
  const pane = cp.state === 'pane', win = cp.state === 'window';
  els.cockpit.hidden = cp.state === 'rider';
  els.cockpit.classList.toggle('as-pane', pane);
  els.cockpit.classList.toggle('as-window', win);
  const att = win && cp.attSides.length > 0;
  els.cockpit.classList.toggle('attached', att);
  if (att) els.cockpit.dataset.att = cp.attSides.join(' ');
  else delete els.cockpit.dataset.att;
  document.body.classList.toggle('cockpit-open', pane);
  const st = els.cockpit.style;
  if (win) {
    for (const s of cp.attSides) snapWinTo(s);   // held borders stay flush (a corner holds two)
    clampWin();
    st.left = cp.win.x + 'px'; st.top = cp.win.y + 'px';
    st.width = cp.win.w + 'px'; st.height = cp.win.h + 'px';
    els.cpToPane.textContent = paneSide() === 'cl' ? '◧' : '◨';
  } else {
    st.left = st.top = st.width = st.height = '';
  }
  if (pane) applyLayout();     // the side was decided at the unfold (unfoldPane) — apply only
  if (!els.cockpit.hidden) reflowInput();      // the composer honors its caps live
  renderRider();
}

/* every unfold passes here: the law reads the seat BEFORE the state flips —
   a rider unfolds by its home, a window by where it stands right now */
function unfoldPane() {
  cp.layout = paneSide();
  setState('pane');
}

function renderRider() {
  els.rider.dataset.edge = dk.edge;
  els.rider.hidden = cp.state !== 'rider';
  if (els.rider.hidden) return;
  els.riderPane.textContent = paneSide() === 'cl' ? '◧' : '◨';   // the side the law will pick
  const ws = workspace();
  if (horizontal()) {
    els.rider.style.top = '';                    // the edge's own CSS holds the cross coordinate
    const span = Math.max(0, ws.w - els.rider.offsetWidth);
    els.rider.style.left = Math.round(ws.x + dk.t * span) + 'px';
  } else {
    els.rider.style.left = '';
    const span = Math.max(0, ws.h - els.rider.offsetHeight);
    els.rider.style.top = Math.round(ws.y + dk.t * span) + 'px';
  }
}

/* flush onto one workspace border, leaving the other axis alone */
function snapWinTo(side) {
  const ws = workspace();
  if (side === 'bottom') cp.win.y = ws.y + ws.h - cp.win.h;
  else if (side === 'top') cp.win.y = ws.y;
  else if (side === 'left') cp.win.x = ws.x;
  else cp.win.x = ws.x + ws.w - cp.win.w;
}

function clampWin() {
  if (!window.innerWidth || !window.innerHeight) return;   // a zero-sized moment
  cp.win.w = clampN(cp.win.w, WIN_MIN.w, window.innerWidth);
  cp.win.h = clampN(cp.win.h, WIN_MIN.h, window.innerHeight - TOPBAR);
  cp.win.x = clampN(cp.win.x, 0, window.innerWidth - cp.win.w);
  cp.win.y = clampN(cp.win.y, TOPBAR, window.innerHeight - cp.win.h);
}

/* the magnetic law, per axis: a border within reach holds its side of the window —
   one border makes the "mini", a corner holds two; forcing away releases each.
   Judged on the clamped (on-screen) rect: pushing past an edge IS arriving at it.
   attReach counts every border in reach: at three the window spans a full axis
   and has become a pane in all but name — the caller unfolds it (Max's rule). */
function magnetize() {
  if (!window.innerWidth || !window.innerHeight) return;   // never judge a zero viewport
  clampWin();
  const ws = workspace();
  const r = reach();
  const dl = Math.abs(cp.win.x - ws.x);
  const dr = Math.abs((ws.x + ws.w) - (cp.win.x + cp.win.w));
  const dt = Math.abs(cp.win.y - ws.y);
  const db = Math.abs((ws.y + ws.h) - (cp.win.y + cp.win.h));
  cp.attReach = (dl < r) + (dr < r) + (dt < r) + (db < r);
  const att = [];
  if (Math.min(dl, dr) < r) att.push(dl <= dr ? 'left' : 'right');
  if (Math.min(dt, db) < r) att.push(dt <= db ? 'top' : 'bottom');
  cp.attSides = att;
  for (const s of att) snapWinTo(s);
}

/* one window-move step: follow the pointer, magnetize — and at three borders in
   reach the window spans a full axis: it unfolds into the pane by itself (the
   gesture ends there; later pointer events find no window and do nothing) */
function moveWinTo(x, y) {
  if (cp.state !== 'window') return;
  cp.win.x = x; cp.win.y = y;
  magnetize();
  if (cp.attReach >= 3) { unfoldPane(); return; }
  renderCockpit();
}

/* folding home — an ATTACHED window already stands on the dock, so it folds where
   it is (the rider takes that spot as the new home); a FREE window folds back to
   the remembered home ("the position it was before it got detached"). */
function foldHome() {
  if (cp.state === 'window' && cp.attSides.length) {
    const side = cp.attSides[0];
    const ws = workspace();
    dk.edge = side;
    dk.t = (side === 'top' || side === 'bottom')
      ? clamp01((cp.win.x + cp.win.w / 2 - ws.x) / Math.max(1, ws.w))
      : clamp01((cp.win.y + cp.win.h / 2 - ws.y) / Math.max(1, ws.h));
    rememberHome();
  }
  setState('rider');
}

/* the button unfold — the fixed layer: the default-size window at the rider's home;
   whichever border(s) are in reach there take hold (a corner home is held by two) */
function openWindowAtHome() {
  cp.win.w = WIN_DEF.w; cp.win.h = WIN_DEF.h;
  const ws = workspace();
  if (horizontal()) {
    const cx = ws.x + dk.t * ws.w;
    cp.win.x = clampN(cx - cp.win.w / 2, ws.x, Math.max(ws.x, ws.x + ws.w - cp.win.w));
    cp.win.y = dk.edge === 'top' ? ws.y : ws.y + ws.h - cp.win.h;
  } else {
    const cy = ws.y + dk.t * ws.h;
    cp.win.y = clampN(cy - cp.win.h / 2, ws.y, Math.max(ws.y, ws.y + ws.h - cp.win.h));
    cp.win.x = dk.edge === 'left' ? ws.x : ws.x + ws.w - cp.win.w;
  }
  magnetize();
  setState('window');
}

/* ── the rider: ONE drag — slide along a border, carry it around corners to any
      other border, or pull it past every border's reach: there the rider stays in
      the hand and the window's SHADOW appears — the deferred morph (Max's step).
      Release in the open → the shadow becomes the window; drift back into a
      border's reach → the shadow vanishes and the rider simply redocks. ── */
function shadowShow(ev) {
  els.winShadow.hidden = false;
  els.winShadow.style.left = Math.round(ev.clientX - WIN_DEF.w / 2) + 'px';
  els.winShadow.style.top = Math.round(ev.clientY - 18) + 'px';
  els.winShadow.style.width = WIN_DEF.w + 'px';
  els.winShadow.style.height = WIN_DEF.h + 'px';
}
function shadowHide() { els.winShadow.hidden = true; }

function initRider() {
  els.rider.addEventListener('pointerdown', e => {
    if (e.target.closest('button')) return;      // the quick-actions are not drag handles
    let mode = 'tap';                            // tap → stick | free (the shadow step)
    const p0 = { x: e.clientX, y: e.clientY };
    startDrag(e, {
      onMove: ev => {
        if (mode === 'tap' && Math.hypot(ev.clientX - p0.x, ev.clientY - p0.y) <= 4) return;
        els.rider.classList.add('lift');         // picked up — the depth grammar
        const ws = workspace();
        const d = {
          left: ev.clientX - ws.x, right: ws.x + ws.w - ev.clientX,
          top: ev.clientY - ws.y, bottom: ws.y + ws.h - ev.clientY,
        };
        const edge = Object.keys(d).reduce((a, b) => (d[a] < d[b] ? a : b));
        if (d[edge] <= SNAP) {
          mode = 'stick';                        // a border holds the rider — no morph
          shadowHide();
          els.rider.classList.remove('free');
          dk.edge = edge;
          const horiz = edge === 'top' || edge === 'bottom';
          const rl = horiz ? els.rider.offsetWidth : els.rider.offsetHeight;
          const span = Math.max(1, (horiz ? ws.w : ws.h) - rl);
          dk.t = clamp01(((horiz ? ev.clientX - ws.x : ev.clientY - ws.y) - rl / 2) / span);
          renderRider();
        } else {
          mode = 'free';                         // in the hand — the ghost says what release makes
          els.rider.classList.add('free');
          els.rider.style.left = Math.round(ev.clientX - els.rider.offsetWidth / 2) + 'px';
          els.rider.style.top = Math.round(ev.clientY - els.rider.offsetHeight / 2) + 'px';
          shadowShow(ev);
        }
      },
      onEnd: ev => {
        els.rider.classList.remove('lift');
        shadowHide();
        if (mode === 'tap') { unfoldPane(); return; }        // the click unfold
        if (mode === 'stick') { rememberHome(); return; }
        if (mode === 'free') {
          // released in the open — the shadow becomes the window, right where it stood
          els.rider.classList.remove('free');
          els.rider.style.left = ''; els.rider.style.top = '';
          cp.win.w = WIN_DEF.w; cp.win.h = WIN_DEF.h;
          cp.win.x = ev.clientX - WIN_DEF.w / 2;
          cp.win.y = ev.clientY - 18;
          cp.attSides = [];
          setState('window');
          rememberCockpit();
        }
      },
    });
  });
  els.rider.addEventListener('keydown', e => {
    if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); unfoldPane(); }
  });
  els.riderMini.addEventListener('pointerdown', e => e.stopPropagation());
  els.riderMini.addEventListener('click', () => openWindowAtHome());
  els.riderPane.addEventListener('pointerdown', e => e.stopPropagation());
  els.riderPane.addEventListener('click', () => unfoldPane());

  // the rail's width and the viewport move the borders — the rider and window follow
  new ResizeObserver(() => renderCockpit()).observe(document.getElementById('nav'));
  window.addEventListener('resize', () => renderCockpit());
}

/* ── the window's chrome: quick actions, the header move, the eight handles ── */
function initWindowChrome() {
  els.cpToPane.addEventListener('click', () => unfoldPane());
  els.cpHome.addEventListener('click', () => foldHome());          // the homing button
  els.cpFold.addEventListener('click', () => foldHome());
  els.cpToWindow.addEventListener('click', () => openWindowAtHome());

  // move — drag the head (buttons excluded); magnetic against every border
  els.cockpitHead.addEventListener('pointerdown', e => {
    if (cp.state !== 'window' || e.target.closest('button')) return;
    const off = { x: e.clientX - cp.win.x, y: e.clientY - cp.win.y };
    els.cockpit.classList.add('in-hand');        // deeper shadow while it rides the hand
    startDrag(e, {
      onMove: ev => moveWinTo(ev.clientX - off.x, ev.clientY - off.y),
      onEnd: () => { els.cockpit.classList.remove('in-hand'); rememberCockpit(); },
    });
  });

  // resize — a HELD border's handle is a pull-away grip (moving an attached border
  // IS the detach gesture; the rule is the geometry); free borders resize normally,
  // and a held border keeps itself flush while the opposite one resizes
  const CHAR = { bottom: 's', top: 'n', left: 'w', right: 'e' };
  for (const h of els.cockpit.querySelectorAll('.win-h')) {
    h.addEventListener('pointerdown', e => {
      if (cp.state !== 'window') return;
      const dir = h.classList[1];
      const held = cp.attSides.find(s => dir.includes(CHAR[s]));
      const s0 = { px: e.clientX, py: e.clientY, x: cp.win.x, y: cp.win.y, w: cp.win.w, h: cp.win.h };
      let mode = held ? 'pull' : 'resize';
      let off = null;
      startDrag(e, {
        onMove: ev => {
          const dx = ev.clientX - s0.px, dy = ev.clientY - s0.py;
          if (mode === 'pull') {
            if (Math.hypot(dx, dy) <= SNAP) return;
            mode = 'move';                       // forced off — the border grab becomes a move
            if (held === 'bottom') cp.win.y = ev.clientY - cp.win.h;
            else if (held === 'top') cp.win.y = ev.clientY;
            else if (held === 'left') cp.win.x = ev.clientX;
            else cp.win.x = ev.clientX - cp.win.w;
            magnetize(); renderCockpit();
            off = { x: ev.clientX - cp.win.x, y: ev.clientY - cp.win.y };
            return;
          }
          if (mode === 'move') {
            moveWinTo(ev.clientX - off.x, ev.clientY - off.y);
            return;
          }
          if (cp.state !== 'window') return;
          if (dir.includes('e')) cp.win.w = s0.w + dx;
          if (dir.includes('s')) cp.win.h = s0.h + dy;
          if (dir.includes('w')) {
            const w2 = clampN(s0.w - dx, WIN_MIN.w, s0.x + s0.w);
            cp.win.x = s0.x + s0.w - w2; cp.win.w = w2;
          }
          if (dir.includes('n')) {
            const h2 = clampN(s0.h - dy, WIN_MIN.h, s0.y + s0.h - TOPBAR);
            cp.win.y = s0.y + s0.h - h2; cp.win.h = h2;
          }
          renderCockpit();
        },
        onEnd: () => {
          // a resize can bring a border into reach — the magnet takes it on release,
          // and at three borders the window unfolds into the pane (Max's rule)
          if (cp.state === 'window') {
            magnetize();
            if (cp.attReach >= 3) { unfoldPane(); return; }
            renderCockpit();
          }
          rememberCockpit();
        },
      });
    });
  }
}

/* ── the composer's growth — the input's top edge is a drag seam (Max's call):
      grow up to 12 rows, and never closer than 3 text lines to the cockpit's own
      top border (head included) — the lower cap governs. Shrinking the cockpit
      re-clamps live; growing it back restores the wanted height. ── */
function initInputResize() {
  const KEY = 'fractal-shell-inputh';
  const seam = document.getElementById('input-seam');
  const inp = els.cockpitInput;
  let want = null;
  try { want = parseInt(localStorage.getItem(KEY), 10) || null; } catch {}
  const bounds = () => {
    const cs = getComputedStyle(inp);
    const l = parseFloat(cs.lineHeight) || 22;
    const extra = parseFloat(cs.paddingTop) + parseFloat(cs.paddingBottom)
                + parseFloat(cs.borderTopWidth) + parseFloat(cs.borderBottomWidth);
    const min = Math.round(2 * l + extra);
    const formExtra = els.cockpitForm.offsetHeight - inp.offsetHeight;
    const byWin = els.cockpit.clientHeight - els.cockpitHead.offsetHeight - 3 * l - formExtra;
    return { min, max: Math.max(min, Math.round(Math.min(12 * l + extra, byWin))) };
  };
  const apply = () => {
    if (want == null) { inp.style.height = ''; return; }
    const b = bounds();
    inp.style.height = clampN(want, b.min, b.max) + 'px';
  };
  reflowInput = apply;
  apply();
  seam.addEventListener('pointerdown', e => {
    const h0 = inp.getBoundingClientRect().height, y0 = e.clientY;
    startDrag(e, {
      onMove: ev => { want = Math.round(h0 + (y0 - ev.clientY)); apply(); },
      onEnd: () => { try { localStorage.setItem(KEY, String(want)); } catch {} },
    });
  });
  seam.addEventListener('dblclick', () => {
    want = null; apply();
    try { localStorage.removeItem(KEY); } catch {}
  });
}

/* ── the layout menu — the split icon stays (the later custom-layout menu grows here).
      Its two defaults now act by moving the cockpit's HOME: the position law stays the
      one source of truth — the menu mirrors the home, the home decides the side. ── */
function initLayoutMenu() {
  els.layoutBtn.addEventListener('click', e => {
    e.stopPropagation();
    const show = els.layoutMenu.hidden;
    els.layoutMenu.hidden = !show;
    els.layoutBtn.setAttribute('aria-expanded', String(show));
  });
  for (const b of els.layoutMenu.querySelectorAll('button')) {
    b.addEventListener('click', () => {
      const want = b.dataset.layout === 'cl' ? 'cl' : 'cr';
      if (dk.edge === 'left' || dk.edge === 'right') {
        dk.edge = want === 'cl' ? 'left' : 'right';
      } else if ((dk.t < 0.5 ? 'cl' : 'cr') !== want) {
        dk.t = 1 - dk.t;                         // mirror the home along its border
      }
      rememberHome();
      cp.layout = want;                          // the menu named the side; the home now agrees
      setState('pane');                          // choosing a split means wanting the split
      els.layoutMenu.hidden = true;
      els.layoutBtn.setAttribute('aria-expanded', 'false');
    });
  }
  document.addEventListener('click', e => {
    if (!els.layoutMenu.hidden && !els.layoutMenu.contains(e.target)) {
      els.layoutMenu.hidden = true;
      els.layoutBtn.setAttribute('aria-expanded', 'false');
    }
  });
}

async function cockpitConnect() {
  cockpitStateLine('looking for the engine room…');
  try {
    const r = await fetch('/engine/health');           // same origin only — the seam's law
    if (!r.ok) throw new Error();
    await r.json();
  } catch {
    cp.live = false;
    cockpitStateLine('no engine');
    cockpitDoor();
    return;
  }
  cp.es = new EventSource('/engine/events');
  cp.es.onmessage = e => { try { cockpitHandle(JSON.parse(e.data)); } catch {} };
  cp.es.onerror = () => { cp.live = false; cockpitStateLine('engine lost — retrying…'); };
}

function cockpitDoor() {
  els.cockpitLog.replaceChildren();
  const d = document.createElement('div');
  d.className = 'note';
  d.innerHTML = 'The seat is a door here — no engine room is serving this page.' +
    '<br><br>To sit in the cockpit, start the engine on your machine:' +
    '<br><code>python3 Workbench/engine_room.py</code>' +
    '<br>then open <code>http://127.0.0.1:8124/Workbench/Shell/</code>.' +
    '<br><br><span class="hint">Localhost only · no keys held · your own Claude login drives it.</span>';
  els.cockpitLog.appendChild(d);
  cockpitControls();
}

/* one handler for the seam's whole event language */
function cockpitHandle(ev) {
  switch (ev.type) {
    case 'state': {                                    // snapshot — every (re)connect rebuilds
      cp.live = true;
      cp.turn = !!ev.turn_active;
      cp.agentEl = null;
      els.cockpitLog.replaceChildren();
      for (const t of ev.transcript || []) {
        cockpitWho(t.who === 'user' ? 'you' : 'agent');
        cockpitText(t.who === 'user' ? 'you-text' : 'agent-text md', t.text, t.who !== 'user');
      }
      if (ev.turn_active && ev.text_so_far) {
        cockpitWho('agent');
        cp.agentEl = cockpitText('agent-text', ev.text_so_far);
      }
      for (const g of ev.pending || []) cockpitGate(g);
      cockpitStateLine((ev.session ? 'session ' + ev.session.slice(0, 8) : 'fresh session') +
                       (ev.turn_active ? ' · turn running' : ''), true);
      cockpitControls();
      break;
    }
    case 'turn.start':
      cp.turn = true; cp.agentEl = null;
      cockpitControls();
      break;
    case 'turn.meta':
      cockpitStateLine('session ' + (ev.session || '').slice(0, 8) +
                       (ev.model ? ' · ' + ev.model : ''), true);
      break;
    case 'text.delta':
      if (!cp.agentEl) { cockpitWho('agent'); cp.agentEl = cockpitText('agent-text', ''); }
      cp.agentEl.textContent += ev.text;
      cockpitScroll();
      break;
    case 'action': {
      const d = document.createElement('div');
      d.className = 'act';
      if (ev.id) d.dataset.actId = ev.id;
      d.innerHTML = `▸ <b>${escapeHtml(ev.title || '')}</b> · ${escapeHtml(ev.detail || '')}`;
      els.cockpitLog.appendChild(d);
      cp.agentEl = null;            // the next text starts a fresh block after the action
      cockpitScroll();
      break;
    }
    case 'action.result': {
      const line = ev.id && els.cockpitLog.querySelector(`[data-act-id="${ev.id}"]`);
      if (line) line.innerHTML += ev.ok ? ' — ok' : ' — <b>failed</b>';
      break;
    }
    case 'permission.request':
      cockpitGate(ev);
      break;
    case 'permission.resolved': {
      const card = els.cockpitLog.querySelector(`[data-gate-id="${ev.id}"]`);
      if (card) card.querySelector('.gate-verdict').textContent =
        ev.decision === 'allow' ? '→ allowed' : '→ denied';
      break;
    }
    case 'turn.end':
      cp.turn = false;
      if (cp.agentEl) {             // re-render the finished text as markdown
        const md = cp.agentEl.textContent;
        cp.agentEl.classList.add('md');
        cp.agentEl.innerHTML = mdToHtml(md);
        cp.agentEl = null;
      }
      if (!ev.ok) cockpitNote('turn ended: ' + (ev.reason || 'error'), true);
      cockpitControls();
      cockpitScroll();
      break;
    case 'error':
      cockpitNote(ev.message || 'engine error', true);
      break;
  }
}

/* the C-008 moment, rendered */
function cockpitGate(g) {
  const card = document.createElement('div');
  card.className = 'gate-card';
  card.dataset.gateId = g.id;
  const tool = document.createElement('div');
  tool.className = 'gate-tool';
  tool.textContent = 'The agent asks: ' + (g.tool || '?');
  const detail = document.createElement('div');
  detail.className = 'gate-detail';
  detail.textContent = g.detail || '';
  const verdict = document.createElement('div');
  verdict.className = 'gate-verdict';
  const allow = document.createElement('button');
  allow.className = 'gate-btn allow'; allow.type = 'button'; allow.textContent = 'Allow';
  const deny = document.createElement('button');
  deny.className = 'gate-btn'; deny.type = 'button'; deny.textContent = 'Deny';
  const decide = d => { enginePost('/engine/permission', { id: g.id, decision: d });
                        verdict.textContent = '…'; allow.remove(); deny.remove(); };
  allow.addEventListener('click', () => decide('allow'));
  deny.addEventListener('click', () => decide('deny'));
  verdict.append(allow, deny);
  card.append(tool, detail, verdict);
  els.cockpitLog.appendChild(card);
  cp.agentEl = null;
  cockpitScroll();
}

async function cockpitSend() {
  const text = els.cockpitInput.value.trim();
  if (!text || !cp.live || cp.turn) return;
  const r = await enginePost('/engine/message', { text });
  if (r && r.status === 409) { cockpitNote('a turn is already running', true); return; }
  cockpitWho('you');
  cockpitText('you-text', text);
  els.cockpitInput.value = '';
  cockpitScroll();
}

async function enginePost(path, body) {
  try {
    return await fetch(path, { method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body) });
  } catch { cockpitNote('engine unreachable', true); return null; }
}

/* small renderers */
function cockpitWho(who) {
  const d = document.createElement('div');
  d.className = 'who'; d.textContent = who;
  els.cockpitLog.appendChild(d);
}
function cockpitText(cls, text, asMd) {
  const d = document.createElement('div');
  d.className = cls;
  if (asMd) d.innerHTML = mdToHtml(text); else d.textContent = text;
  els.cockpitLog.appendChild(d);
  return d;
}
function cockpitNote(msg, isErr) {
  const d = document.createElement('div');
  d.className = 'note' + (isErr ? ' err' : '');
  d.textContent = msg;
  els.cockpitLog.appendChild(d);
  cockpitScroll();
}
function cockpitStateLine(msg, live) {
  els.cockpitState.textContent = msg;
  els.cockpitState.classList.toggle('live', !!live);
}
function cockpitScroll() { els.cockpitLog.scrollTop = els.cockpitLog.scrollHeight; }
function cockpitControls() {
  els.cockpitSend.disabled = !cp.live || cp.turn;
  els.cockpitStop.hidden = !cp.turn;
}

/* the cockpit's width — the rail resizer's mirror, from the right edge */
function initCockpitResize() {
  const KEY = 'fractal-shell-cockpitw';
  const MIN = 300, MAX = 560;
  const root = document.documentElement;
  const handle = document.getElementById('cockpit-resize');
  let w = 380;
  try { w = parseInt(localStorage.getItem(KEY), 10) || 380; } catch {}
  const set = v => {
    w = Math.max(MIN, Math.min(MAX, v));
    root.style.setProperty('--cockpit-w', w + 'px');
  };
  const remember = () => { try { localStorage.setItem(KEY, String(w)); } catch {} };
  set(w);
  let startX = 0, startW = 0;
  handle.addEventListener('pointerdown', e => {
    startX = e.clientX; startW = w;
    handle.setPointerCapture(e.pointerId);
    document.body.classList.add('resizing');
  });
  handle.addEventListener('pointermove', e => {
    if (!handle.hasPointerCapture(e.pointerId)) return;
    const dir = cp.layout === 'cl' ? 1 : -1;     // the seam widens toward the screen
    set(startW + dir * (e.clientX - startX));
  });
  const end = e => {
    if (handle.hasPointerCapture(e.pointerId)) handle.releasePointerCapture(e.pointerId);
    document.body.classList.remove('resizing');
    remember();
  };
  handle.addEventListener('pointerup', end);
  handle.addEventListener('pointercancel', end);
  handle.addEventListener('dblclick', () => { set(380); remember(); });
}

/* ── minimal markdown (headers, lists, tables, quotes, fences, inline) ── */
function escapeHtml(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}
function inline(s) {
  return s
    .replace(/`([^`]+)`/g, (_, c) => `<code>${c}</code>`)
    .replace(/!\[([^\]]*)\]\(([^)\s]+)\)/g, '<a href="$2" target="_blank" rel="noopener">🖼 $1</a>')
    .replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>')
    .replace(/\[\[([^\]]+)\]\]/g, '<span class="wikiref">$1</span>')
    .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
    .replace(/(^|[\s(>])\*([^*\n]+)\*/g, '$1<em>$2</em>');
}
function mdToHtml(src) {
  const fences = [];
  src = src.replace(/```[^\n]*\n([\s\S]*?)```/g, (_, code) => {
    fences.push(code);
    return '@@FENCE' + (fences.length - 1) + '@@';
  });
  const lines = escapeHtml(src).split('\n');
  const out = [];
  let list = null, table = null, para = [];

  const flushPara = () => { if (para.length) { out.push('<p>' + inline(para.join(' ')) + '</p>'); para = []; } };
  const flushList = () => { if (list) { out.push(`</${list}>`); list = null; } };
  const flushTable = () => {
    if (!table) return;
    const [head, ...rows] = table;
    let h = '<table><thead><tr>' + head.map(c => `<th>${inline(c)}</th>`).join('') + '</tr></thead><tbody>';
    for (const r of rows) h += '<tr>' + r.map(c => `<td>${inline(c)}</td>`).join('') + '</tr>';
    out.push(h + '</tbody></table>');
    table = null;
  };
  const flushAll = () => { flushPara(); flushList(); flushTable(); };

  for (const raw of lines) {
    const line = raw.replace(/\s+$/, '');
    const t = line.trim();

    if (/^@@FENCE\d+@@$/.test(t)) { flushAll(); out.push(t); continue; }
    if (t === '') { flushAll(); continue; }

    if (t.startsWith('|')) {
      flushPara(); flushList();
      const cells = t.replace(/^\|/, '').replace(/\|$/, '').split('|').map(c => c.trim());
      if (cells.every(c => /^:?-{3,}:?$/.test(c))) continue;      // separator row
      (table = table || []).push(cells);
      continue;
    }
    flushTable();

    const hm = t.match(/^(#{1,6})\s+(.*)$/);
    if (hm) { flushAll(); out.push(`<h${hm[1].length}>${inline(hm[2])}</h${hm[1].length}>`); continue; }
    if (/^(---+|\*\*\*+)$/.test(t)) { flushAll(); out.push('<hr>'); continue; }
    if (t.startsWith('&gt;')) { flushAll(); out.push(`<blockquote><p>${inline(t.replace(/^(&gt;\s?)+/, ''))}</p></blockquote>`); continue; }

    const ul = t.match(/^[-*+]\s+(.*)$/);
    const ol = t.match(/^\d+[.)]\s+(.*)$/);
    if (ul || ol) {
      flushPara(); flushTable();
      const want = ul ? 'ul' : 'ol';
      if (list !== want) { flushList(); out.push(`<${want}>`); list = want; }
      out.push(`<li>${inline((ul || ol)[1])}</li>`);
      continue;
    }
    flushList();
    para.push(t);
  }
  flushAll();

  return out.join('\n').replace(/@@FENCE(\d+)@@/g, (_, i) =>
    `<pre><code>${escapeHtml(fences[+i])}</code></pre>`);
}
