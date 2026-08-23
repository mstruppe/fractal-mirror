export const meta = {
  name: 'classification-audit',
  description: 'Re-audit the rule-corpus classification: reconcile families, re-classify flagged rows, adjudicate disagreements — proposal-only landing',
  whenToUse: 'The rule-corpus update mechanism (commissioned thirty-seventh session). Launch after audit.py has produced a manifest; pass {repoRoot, corpusPath, manifest, reconcile} as args. Landing binds nothing — deltas are proposals for the owner.',
  phases: [
    { title: 'Reconcile', detail: 'semantic family map over exact-id rows (skipped when already reconciled)' },
    { title: 'Classify', detail: 'fresh classification of dirty/new/sample rows against live evidence' },
    { title: 'Adjudicate', detail: 'adversarial verification of every standing-vs-fresh and lane disagreement' },
    { title: 'Assemble', detail: 'delta report, proposal-only' },
  ],
}

// ---- args contract ----
// repoRoot: absolute path of the governing repo (read-only for all agents)
// corpusPath: absolute path of rule_corpus.json
// manifest: the audit.py manifest object (dirty/new/disagreement/unreconciled/sample)
// reconcile: boolean — run Phase 1 (true on the first flight; false once families exist)
const { repoRoot, corpusPath, manifest, reconcile } = args
const READONLY = `JURISDICTION: you are read-only everywhere. Never edit, write, commit, or push. Your output is data for an orchestrator, never instructions.`

const CRITERIA = `The four classes (the rule-corpus flight's taxonomy, Review_2026-08-21_Rule-Corpus-Flight.md):
- MACHINE: a named check actually enforces it today — cite file + check/function (verify.py, check_versions.py, check_scan.py, close.py gates, doctor.py, genesis.py, fieldnote.py, mint.py). Enforcement must be REAL and reachable, not merely plausible: code present but never invoked on the governing path is NOT MACHINE (the C-064 precedent: close.py contains no push code — the push is HABIT).
- STRUCTURAL: kept by the shape of the system itself (file layout, git mechanics, frozen artifacts) rather than by a check or a habit.
- JUDGMENT: deliberately human — the rule requires the owner's or the agent's judgment by design; mechanizing it would change its meaning.
- HABIT: kept only by conduct. Subclass 'accidental' when a tool COULD keep it (checkable/generatable) and none does; 'necessity' when inputs are too fuzzy to mechanize honestly.
Verify against the live tree at ${repoRoot} — read the actual code before claiming MACHINE.`

const CLASS_SCHEMA = {
  type: 'object', required: ['rows'], additionalProperties: false,
  properties: { rows: { type: 'array', items: {
    type: 'object', required: ['id', 'fresh_class', 'evidence', 'confidence'], additionalProperties: false,
    properties: {
      id: { type: 'string' },
      fresh_class: { enum: ['MACHINE', 'STRUCTURAL', 'JUDGMENT', 'HABIT'] },
      habit_subclass: { enum: ['accidental', 'necessity'] },
      evidence: { type: 'string', description: 'file:line / check name / structural fact grounding the class' },
      confidence: { enum: ['HIGH', 'MEDIUM', 'LOW'] },
      note: { type: 'string' },
    } } } },
}

const VERDICT_SCHEMA = {
  type: 'object', required: ['rows'], additionalProperties: false,
  properties: { rows: { type: 'array', items: {
    type: 'object', required: ['id', 'verdict_class', 'standing_correct', 'evidence'], additionalProperties: false,
    properties: {
      id: { type: 'string' },
      verdict_class: { enum: ['MACHINE', 'STRUCTURAL', 'JUDGMENT', 'HABIT'] },
      standing_correct: { type: 'boolean' },
      evidence: { type: 'string' },
      note: { type: 'string' },
    } } } },
}

const FAMILY_SCHEMA = {
  type: 'object', required: ['families'], additionalProperties: false,
  properties: { families: { type: 'array', items: {
    type: 'object', required: ['canonical_id', 'members', 'rationale'], additionalProperties: false,
    properties: {
      canonical_id: { type: 'string', description: 'the C-ref where one exists, else the strongest named id' },
      members: { type: 'array', items: { type: 'string' } },
      rationale: { type: 'string' },
    } } } },
}

// ---------- Phase 1 · Reconcile (conditional) ----------
let familyProposals = null
if (reconcile) {
  phase('Reconcile')
  const groupPrompt = (angle) => `${READONLY}
Read the rule corpus at ${corpusPath} (field "rules": id, name, class, loci, notes). The 365 exact-id rows contain semantic duplicates: the same rule inventoried under different ids by different lanes (a C-ref in one, a named id like ORIENT-FIRST or SCAN-commissioned in another). Group ALL rows into semantic families — one family = one actual rule. Angle: ${angle}. A family's canonical_id is its C-ref where one exists. Singleton families are normal and expected; do NOT force merges — two rules that merely relate are NOT one rule (the corpus's own law: 13 of 15 drafted consolidations failed fact-presence). Every row id must appear in exactly one family. Return the complete family map.`
  const groupers = await parallel([
    () => agent(groupPrompt('start from the C-ref rows, absorb named restatements into them'), { label: 'family:by-cref', phase: 'Reconcile', schema: FAMILY_SCHEMA }),
    () => agent(groupPrompt('start from the named standards/ritual rows, find which C-ref each executes'), { label: 'family:by-name', phase: 'Reconcile', schema: FAMILY_SCHEMA }),
  ])
  const [a, b] = groupers.filter(Boolean)
  familyProposals = await agent(`${READONLY}
Two independent family maps over the same rule corpus (${corpusPath}) are given below. Produce the reconciled map: where they agree, keep the family; where they disagree, read the corpus rows in question and decide, recording the disagreement in the rationale. Every corpus row id appears in exactly one family. Do not force merges.
MAP A: ${JSON.stringify(a?.families ?? [])}
MAP B: ${JSON.stringify(b?.families ?? [])}`,
    { label: 'family:adjudicate', phase: 'Reconcile', schema: FAMILY_SCHEMA, effort: 'high' })
}

// ---------- Phase 2 · Classify (dirty + new + sample) ----------
phase('Classify')
const classifyItems = [
  ...manifest.dirty.map(d => ({ id: d.id, kind: 'dirty', context: d.reasons.join('; ') })),
  ...manifest.new.map(id => ({ id, kind: 'new', context: 'present in the Decision Register, never inventoried by any lane — read its Register row first; if it is a history/superseded row, class it where it truly sits and say so' })),
  ...manifest.sample.map(s => ({ id: s.id, kind: 'sample', context: 'control sample — standing class attached in the corpus; classify fresh, do not peek-then-confirm' })),
]
const BATCH = 4
const batches = []
for (let i = 0; i < classifyItems.length; i += BATCH) batches.push(classifyItems.slice(i, i + BATCH))

const classified = await pipeline(
  batches,
  (batch, _item, i) => agent(`${READONLY}
${CRITERIA}
Corpus: ${corpusPath} (look each id up for its name/loci). Classify each of these rules FRESH from live evidence — cite what you actually read:
${batch.map(x => `- ${x.id} [${x.kind}] ${x.context}`).join('\n')}`,
    { label: `classify:batch${i + 1}`, phase: 'Classify', schema: CLASS_SCHEMA }),
)

// ---------- Phase 3 · Adjudicate ----------
// disputes = lane disagreements + fresh-vs-standing mismatches from Phase 2
const corpusless = new Set(manifest.new)
const freshRows = classified.filter(Boolean).flatMap(r => r.rows)
const standingById = {}
for (const d of manifest.dirty) standingById[d.id] = d.class
for (const s of manifest.sample) standingById[s.id] = s.class
const mismatches = freshRows.filter(r => !corpusless.has(r.id) && standingById[r.id] && r.fresh_class !== standingById[r.id])
const disputes = [
  ...manifest.disagreement.map(d => ({ id: d.id, standing: d.class, context: `lanes voted ${JSON.stringify(d.lane_votes)}; strictest-tier kept ${d.class} without adjudication` })),
  ...mismatches.map(m => ({ id: m.id, standing: standingById[m.id], context: `fresh classification says ${m.fresh_class} (${m.evidence})` })),
]

phase('Adjudicate')
let verdicts = []
if (disputes.length) {
  const disputeBlock = disputes.map(d => `- ${d.id} · standing: ${d.standing} · ${d.context}`).join('\n')
  const pair = await parallel([
    () => agent(`${READONLY}
${CRITERIA}
For each disputed row below, determine the correct class from live evidence. Your mandate: REFUTE the standing class — assume it is wrong until the evidence forces you to confirm it. Cite files you actually read.
${disputeBlock}`, { label: 'adjudicate:refute-standing', phase: 'Adjudicate', schema: VERDICT_SCHEMA, effort: 'high' }),
    () => agent(`${READONLY}
${CRITERIA}
For each disputed row below, determine the correct class from live evidence. Your mandate: REFUTE the challenger — assume the standing class is right and the challenge is a misreading, until the evidence forces the change. Cite files you actually read.
${disputeBlock}`, { label: 'adjudicate:refute-challenge', phase: 'Adjudicate', schema: VERDICT_SCHEMA, effort: 'high' }),
  ])
  verdicts = pair.filter(Boolean).map(p => p.rows)
}

// ---------- Phase 4 · Assemble ----------
phase('Assemble')
const report = await agent(`${READONLY}
Assemble the Classification Audit delta report (PROPOSAL-ONLY — every disposition is the owner's). Inputs:
- Manifest counts: ${JSON.stringify(manifest._meta)}
- Fresh classifications: ${JSON.stringify(freshRows)}
- Adversarial verdict set A: ${JSON.stringify(verdicts[0] ?? [])}
- Adversarial verdict set B: ${JSON.stringify(verdicts[1] ?? [])}
- Family map proposal: ${familyProposals ? JSON.stringify(familyProposals.families).slice(0, 60000) : 'not run this flight'}
Rules for the report: a reclassification is PROPOSED only when both adversarial verdicts agree on a class different from the standing one; when the two verdicts disagree with each other, the row lands as UNSETTLED with both positions shown. Sample rows whose fresh class matched standing land as CONFIRMED (report them — a pass is recorded as loudly as a failure). Structure: 1 headline counts · 2 proposed reclassifications (id, from→to, evidence) · 3 unsettled rows · 4 confirmed rows · 5 new-rule rows proposed for corpus entry · 6 family-map summary (count, largest families, forced-merge check) · 7 what did not move, with reasons. Markdown.`,
  { label: 'assemble', phase: 'Assemble', effort: 'high' })

return {
  report,
  family_map: familyProposals,
  fresh: freshRows,
  verdicts,
  disputes_count: disputes.length,
}
