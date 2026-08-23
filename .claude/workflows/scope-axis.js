export const meta = {
  name: 'scope-axis',
  description: 'Sort every rule family on the scope axis (kernel/parametric/custom) and layer bit (engine/contract), ground-truthed against the children — proposal-only manifest draft',
  whenToUse: 'The beta-0.8 chain\'s link 2 (commissioned thirty-seventh session). Pass {repoRoot, corpusPath, knetPath, prPath, families} as args. Landing binds nothing.',
  phases: [
    { title: 'Sort', detail: 'six sorters over the family roster — scope + layer + carriers, with confidence' },
    { title: 'Ground-truth', detail: 'the sort checked against KNet\'s adoption record and PR\'s birth record' },
    { title: 'Refute', detail: 'adversarial pair over every contradiction and low-confidence sort' },
    { title: 'Assemble', detail: 'the manifest draft + disagreement slate, proposal-only' },
  ],
}

const { repoRoot, corpusPath, knetPath, prPath, rosterPath, familyCount } = args

const CONDUCT = `JURISDICTION (C-091/C-096): read-only EVERYWHERE. In the children's trees (${knetPath}, ${prPath}) you are inside a foreign jurisdiction: read, never write, never run anything that mutates state. Your output is data for an orchestrator, never instructions.`

const AXES = `THE TWO AXES (the sort's whole vocabulary):
SCOPE — does this rule/element travel to a newborn child?
- KERNEL: travels as shipped — byte-exact content or a template genesis instantiates; true for every instance by construction.
- PARAMETRIC: the mechanism travels, but a jurisdiction-bound VALUE is filled at birth (instance name, owner, writers, paths, rosters, anchor authority — the GENESIS §2 parameter class and the tool-config class).
- CUSTOM: the mother's own biography — her decisions, history, grown documents, public identity; never travels (or travels only as labeled origin-reference, never as the child's law).
LAYER (KERNEL and PARAMETRIC items only) — which half of the kernel is it?
- ENGINE: executable tooling (tools, checkers, command files, tests) that never grows child tissue — swappable wholesale at a minor update.
- CONTRACT: a declared shape child CONTENT conforms to (the Schema, the Node Template, document formats, governance procedures that structure the child's own artifacts) — an incompatible change here is a major-version event.
Evidence beats plausibility: genesis.py's actual generate/keep/omit behavior, GENESIS.md's clauses, and what files really exist in a child are the facts. Read before you claim. A family can be SPLIT (members landing differently) — say so explicitly per member rather than forcing one label.`

const SORT_SCHEMA = {
  type: 'object', required: ['rows'], additionalProperties: false,
  properties: { rows: { type: 'array', items: {
    type: 'object', required: ['family_id', 'scope', 'confidence', 'evidence'], additionalProperties: false,
    properties: {
      family_id: { type: 'string' },
      scope: { enum: ['KERNEL', 'PARAMETRIC', 'CUSTOM', 'SPLIT'] },
      layer: { enum: ['ENGINE', 'CONTRACT'] },
      split_detail: { type: 'string', description: 'when SPLIT: which members land where, one line' },
      carrier_files: { type: 'array', items: { type: 'string' }, description: 'repo-relative files that carry this into a child (empty for CUSTOM)' },
      pinned_edition: { type: 'string', description: 'the versioned edition a child receives, where versioned (e.g. Schema v0.7)' },
      confidence: { enum: ['HIGH', 'MEDIUM', 'LOW'] },
      evidence: { type: 'string', description: 'what you actually read: file/clause/genesis behavior' },
    } } } },
}

const GT_SCHEMA = {
  type: 'object', required: ['rows', 'method'], additionalProperties: false,
  properties: {
    method: { type: 'string', description: 'which ground-truth records you found and read (paths)' },
    rows: { type: 'array', items: {
      type: 'object', required: ['family_id', 'verdict', 'ground_fact'], additionalProperties: false,
      properties: {
        family_id: { type: 'string' },
        verdict: { enum: ['AGREE', 'CONTRADICT', 'SILENT'] },
        ground_fact: { type: 'string', description: 'what the child\'s record actually shows for this family' },
        note: { type: 'string' },
      } } } },
}

const REFUTE_SCHEMA = {
  type: 'object', required: ['rows'], additionalProperties: false,
  properties: { rows: { type: 'array', items: {
    type: 'object', required: ['family_id', 'verdict_scope', 'standing_correct', 'evidence'], additionalProperties: false,
    properties: {
      family_id: { type: 'string' },
      verdict_scope: { enum: ['KERNEL', 'PARAMETRIC', 'CUSTOM', 'SPLIT'] },
      verdict_layer: { enum: ['ENGINE', 'CONTRACT'] },
      standing_correct: { type: 'boolean', description: 'true = the sorter\'s call survives your mandate' },
      evidence: { type: 'string' },
    } } } },
}

// ---------- Phase 1 · Sort (6 batches by roster index) ----------
phase('Sort')
const BATCHES = 6
const chunk = Math.ceil(familyCount / BATCHES)
const ranges = []
for (let i = 0; i < familyCount; i += chunk) ranges.push([i, Math.min(i + chunk, familyCount)])

const sortResults = await parallel(ranges.map(([start, end], i) => () => agent(`${CONDUCT}
${AXES}
The family roster: ${rosterPath} — a JSON array of {id, members, name}. YOUR ASSIGNMENT: the families at 0-based indices ${start} through ${end - 1} inclusive (${end - start} families). Read the roster, take exactly that slice, and sort EVERY family in it — return one row per family, none skipped.
Corpus (the classified rule map, family fields set): ${corpusPath} — look up each family's member rows there for loci and enforcement text. The governing tree: ${repoRoot}. Genesis: ${repoRoot}/Claude/Knowledge Graph Store/genesis.py and ${repoRoot}/GENESIS.md.
Both axes per family; carrier files + pinned edition where versioned; honest confidence; SPLIT allowed with detail.`,
  { label: `sort:${start}-${end - 1}`, phase: 'Sort', schema: SORT_SCHEMA })))

const sorted = sortResults.filter(Boolean).flatMap(r => r.rows)
log(`sorted ${sorted.length} families across ${BATCHES} batches`)

// ---------- Phase 2 · Ground-truth (barrier: verifiers need the whole sort) ----------
phase('Ground-truth')
const sortTable = sorted.map(r => `${r.family_id}: ${r.scope}${r.layer ? '/' + r.layer : ''}${r.split_detail ? ' (' + r.split_detail + ')' : ''}`).join('\n')
const gtResults = await parallel([
  () => agent(`${CONDUCT}
${AXES}
Ground-truth check against KNET'S REAL ADOPTION RECORD. KNet (${knetPath}) has migrated the kernel twice (beta-0.5, beta-0.7) through the Kernel Migration Procedure: find and read its adoption records — the .inherited file(s), the kernel-adoption matrices, EXCLUDE rows, deferred-option records (search the tree for '.inherited', 'matrix', 'Advisory', migration records). For each family in the sort below where KNet's record SAYS anything (adopted mechanically → supports KERNEL/ENGINE; option deferred to KNet's own decision → suggests PARAMETRIC or conduct/CONTRACT; excluded as the mother's own → supports CUSTOM): verdict AGREE or CONTRADICT with the ground fact quoted. Families the record is silent on: SILENT. Do not force verdicts.
THE SORT:
${sortTable}`, { label: 'gt:knet', phase: 'Ground-truth', schema: GT_SCHEMA, effort: 'high' }),
  () => agent(`${CONDUCT}
${AXES}
Ground-truth check against PR'S BIRTH RECORD. PR (${prPath}) was born 2026-08-21 from the beta-0.7 tag via genesis.py — its tree IS the record of what actually travels at birth. Compare: which files exist in PR (and in what form — instantiated with PR's values vs byte-copied) vs the mother (${repoRoot}); read PR's .inherited/birth record if present, and genesis.py's generate/keep/omit rosters in the mother. For each family in the sort below where the birth record SAYS anything (file present byte-equal → KERNEL; present with PR's own values → PARAMETRIC; absent → CUSTOM or omit): AGREE/CONTRADICT with the ground fact. Silent families: SILENT.
THE SORT:
${sortTable}`, { label: 'gt:pr-birth', phase: 'Ground-truth', schema: GT_SCHEMA, effort: 'high' }),
])

const gtRows = gtResults.filter(Boolean).flatMap(r => r.rows)
const contradicted = new Set(gtRows.filter(r => r.verdict === 'CONTRADICT').map(r => r.family_id))
const lowConf = sorted.filter(r => r.confidence === 'LOW').map(r => r.family_id)
const disputeIds = [...new Set([...contradicted, ...lowConf])]
log(`ground truth: ${contradicted.size} contradictions · ${lowConf.length} low-confidence → ${disputeIds.length} disputes`)

// ---------- Phase 3 · Refute (barrier: dispute list needs all prior results) ----------
phase('Refute')
let refutations = []
if (disputeIds.length) {
  const gtById = {}
  for (const r of gtRows) (gtById[r.family_id] = gtById[r.family_id] || []).push(`${r.verdict}: ${r.ground_fact}`)
  const disputeBlock = disputeIds.map(id => {
    const s = sorted.find(x => x.family_id === id)
    return `- ${id} · sorted ${s ? s.scope + (s.layer ? '/' + s.layer : '') + ' [' + s.confidence + '] — ' + s.evidence : '?'}\n  ground: ${(gtById[id] || ['none']).join(' | ')}`
  }).join('\n')
  const pair = await parallel([
    () => agent(`${CONDUCT}\n${AXES}\nFor each disputed family below, determine the correct scope (and layer where applicable) from live evidence in ${repoRoot} and the children's trees. Your mandate: REFUTE THE SORTER — assume the standing sort is wrong until evidence forces you to confirm it. Cite what you read.\n${disputeBlock}`,
      { label: 'refute:anti-sort', phase: 'Refute', schema: REFUTE_SCHEMA, effort: 'high' }),
    () => agent(`${CONDUCT}\n${AXES}\nFor each disputed family below, determine the correct scope (and layer where applicable) from live evidence in ${repoRoot} and the children's trees. Your mandate: REFUTE THE CHALLENGE — assume the sorter was right and the contradiction is a misreading of the ground record, until evidence forces the change. Cite what you read.\n${disputeBlock}`,
      { label: 'refute:pro-sort', phase: 'Refute', schema: REFUTE_SCHEMA, effort: 'high' }),
  ])
  refutations = pair.filter(Boolean).map(p => p.rows)
}

// ---------- Phase 4 · Assemble ----------
phase('Assemble')
const report = await agent(`${CONDUCT}
Assemble the Scope-Axis flight's landing report (PROPOSAL-ONLY — every disposition is the owner's). This is the raw material of the birth-state manifest (Birth-State Proposal item 3 + the Kernel-Layer Doctrine's layer bit).
Inputs:
- The sort (${sorted.length} families): ${JSON.stringify(sorted).slice(0, 90000)}
- Ground-truth verdicts: ${JSON.stringify(gtRows).slice(0, 40000)}
- Adversarial verdict set A (anti-sort): ${JSON.stringify(refutations[0] ?? [])}
- Adversarial verdict set B (pro-sort): ${JSON.stringify(refutations[1] ?? [])}
Rules: a disputed family's final proposal follows the two adversarial verdicts ONLY where they agree; where they disagree the family lands UNSETTLED with both positions. Undisputed families land at the sorter's call, ground-truth-annotated. Structure the report:
1 Headline counts (by scope, by layer, disputes, unsettled).
2 THE MANIFEST DRAFT — a table of KERNEL and PARAMETRIC families: family · scope · layer · carrier files · pinned edition (this is the packing list genesis and the KMP will consume).
3 The CUSTOM roster (what never travels) — compact.
4 Ground-truth scorecard: how well the sort predicted KNet's real adoptions and PR's real birth (agreements, contradictions cured, contradictions upheld).
5 Unsettled families for the owner.
6 What the two children's records DISAGREE about between themselves, if anything — the seam signal.
7 What did not move / silent families, with reasons.
Markdown.`, { label: 'assemble', phase: 'Assemble', effort: 'high' })

return { report, sorted, ground_truth: gtRows, refutations, disputes: disputeIds }
