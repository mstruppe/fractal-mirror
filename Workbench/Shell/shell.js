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
  tierPublic: document.getElementById('tier-public'),
  tierLocal: document.getElementById('tier-local'),
  explorerWrap: document.getElementById('explorer-wrap'),
  explorer: document.getElementById('explorer'),
  rootName: document.getElementById('root-name'),
  cockpit: document.getElementById('cockpit'),
  cockpitToggle: document.getElementById('cockpit-toggle'),
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

const cp = {                                     // cockpit state (summonable-pane #1)
  open: false, live: false, es: null, turn: false,
  layout: 'cr',           // 'cr' = reader left · cockpit right; 'cl' = the mirror
  agentEl: null,          // the streaming agent-text element of the current turn
};

const rd = {                                     // reader state (the document window)
  open: true, reopen: null, station: null,
};

/* ── boot ── */
buildQuest();
els.tierPublic.addEventListener('click', usePublicTier);
els.tierLocal.addEventListener('click', useLocalTier);
initTheme();
initNavResize();
initCockpit();
initLayoutMenu();
initReader();
setStatus(`public tier · root ${state.publicBase.pathname}`);

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

/* ── tiers ── */
function usePublicTier() {
  state.tier = 'public';
  reflectTier();
  setStatus(`public tier · root ${state.publicBase.pathname}`);
}

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
    setStatus(`local tier · reading “${handle.name}” (nothing is ever written)`);
  } catch (e) {
    if (e.name !== 'AbortError') setStatus('folder grant failed: ' + e.message, true);
  }
}

function reflectTier() {
  els.tierPublic.classList.toggle('active', state.tier === 'public');
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
    if (st.kind === 'html') {
      if (state.tier === 'public') showFrameSrc(publicUrl(st.path));
      else showFrameDoc(await readLocalText(st.path));
    } else {
      const text = state.tier === 'public' ? await fetchPublic(st.path) : await readLocalText(st.path);
      showMarkdown(text);
    }
    readerShowing(() => openStation(st, btn), state.tier === 'public' ? st : null);
    setStatus(`${state.tier} tier · ${st.path}`);
  } catch (e) {
    showMessage(`Could not open <b>${escapeHtml(st.title)}</b>`, e.message +
      (state.tier === 'public'
        ? '<br><span class="hint">The public tier reads relative paths beside the served shell — this station may not be published at this address. Try the local tier.</span>'
        : '<br><span class="hint">Is the granted folder the estate root (the folder holding README.md and GENESIS.md)?</span>'));
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
    setStatus(`local tier · ${path}`);
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
      Rituals stay words: /fractal and /close are typed, never buttons. ── */
function initCockpit() {
  const KEY = 'fractal-shell-cockpit';
  els.cockpitSend.disabled = true;               // enabled by the first snapshot — live seats only
  try { cp.layout = localStorage.getItem('fractal-shell-layout') === 'cl' ? 'cl' : 'cr'; } catch {}
  applyLayout();
  els.cockpitToggle.addEventListener('click', () => cockpitSetOpen(!cp.open));
  els.cockpitForm.addEventListener('submit', e => { e.preventDefault(); cockpitSend(); });
  els.cockpitInput.addEventListener('keydown', e => {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); cockpitSend(); }
  });
  els.cockpitStop.addEventListener('click', () => enginePost('/engine/interrupt', {}));
  initCockpitResize();
  let openAtBoot = false;
  try { openAtBoot = localStorage.getItem(KEY) === 'open'; } catch {}
  if (openAtBoot) cockpitSetOpen(true);
}

/* ── the layout menu — the split icon picks a default arrangement (Max's two).
      Direction of record: every window is the same shell — open, close, arrange;
      settings grow as need appears, never sooner. ── */
function initLayoutMenu() {
  els.layoutBtn.addEventListener('click', e => {
    e.stopPropagation();
    const show = els.layoutMenu.hidden;
    els.layoutMenu.hidden = !show;
    els.layoutBtn.setAttribute('aria-expanded', String(show));
  });
  for (const b of els.layoutMenu.querySelectorAll('button')) {
    b.addEventListener('click', () => {
      cp.layout = b.dataset.layout === 'cl' ? 'cl' : 'cr';
      try { localStorage.setItem('fractal-shell-layout', cp.layout); } catch {}
      applyLayout();
      if (!cp.open) cockpitSetOpen(true);        // choosing a split means wanting the split
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

function applyLayout() {
  document.body.classList.toggle('cockpit-left', cp.layout === 'cl');
  els.layoutBtn.textContent = cp.layout === 'cl' ? '◧' : '◨';
}

function cockpitSetOpen(open) {
  cp.open = open;
  document.body.classList.toggle('cockpit-open', open);
  els.cockpit.hidden = !open;
  try { localStorage.setItem('fractal-shell-cockpit', open ? 'open' : 'closed'); } catch {}
  if (open && !cp.es) cockpitConnect();
  if (!open && cp.es) { cp.es.close(); cp.es = null; cp.live = false; }
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
