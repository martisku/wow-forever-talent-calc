import { LEGACY_BASELINE, type RulesetIdentity } from './rulesetIdentity'
export { LEGACY_BASELINE, currentReference } from './rulesetIdentity'
export type { RulesetIdentity } from './rulesetIdentity'
/** Immutable ruleset contexts. Encoding version numbers are local to a revision. */
import type { ClassData, Talent } from './schema'
import { buildRegistry, type EncodingFile, type EncodingRegistry, type MigrationFile } from './encoding'
import { hasClass, loadClass } from './load'
import { loadRegistry } from './encoding'

export interface ReferenceSource {
  provider: 'wowhead'
  pageUrl: string
  dataUrl: string
  version: string
  dataRevision: string
  retrievedAt: string
  dataSha256: string
}
export interface RulesetManifest {
  schemaVersion: 1
  kind: 'baseline' | 'experiment'
  id: string
  revision: number
  name: string
  classes: string[]
  intent: string
  source?: ReferenceSource
  baseline?: { id: string; revision: number }
  changes?: Record<string, Record<string, string>>
}
const manifests = import.meta.glob('../../../data/rulesets/*/r*/manifest.json', {
  eager: true,
  import: 'default',
}) as Record<string, RulesetManifest>
const datasets = import.meta.glob('../../../data/rulesets/*/r*/classes/*.json', { import: 'default' }) as Record<
  string,
  () => Promise<ClassData>
>
const encodings = import.meta.glob('../../../data/rulesets/*/r*/encoding/v*.json', { import: 'default' }) as Record<
  string,
  () => Promise<EncodingFile>
>
const migrations = import.meta.glob('../../../data/rulesets/*/r*/encoding/migrations/*.json', {
  import: 'default',
}) as Record<string, () => Promise<MigrationFile>>

export function listRulesets(classId: string): RulesetManifest[] {
  return Object.values(manifests)
    .filter((m) => m.classes.includes(classId))
    .sort((a, b) => a.kind.localeCompare(b.kind) || a.name.localeCompare(b.name) || a.revision - b.revision)
}
export function manifestFor(identity: RulesetIdentity): RulesetManifest {
  const m = Object.values(manifests).find((m) => m.id === identity.ruleset && m.revision === identity.revision)
  if (!m)
    throw new Error('This ruleset revision is unavailable. Choose the reference snapshot or an available experiment.')
  return m
}
export function rulesetLabel(m: RulesetManifest): string {
  return `${m.name} · revision ${m.revision}`
}

export interface TalentChange {
  id: string
  name: string
  kinds: ('Added' | 'Modified' | 'Moved' | 'Removed')[]
  intent: string
  before?: string
  after?: string
}
function stable(value: unknown): string {
  if (Array.isArray(value)) return `[${value.map(stable).join(',')}]`
  if (value !== null && typeof value === 'object')
    return `{${Object.entries(value)
      .sort(([a], [b]) => a.localeCompare(b))
      .map(([k, v]) => `${k}:${stable(v)}`)
      .join(',')}}`
  return JSON.stringify(value)
}
export function compareTalents(
  baseline: ClassData,
  experiment: ClassData,
  intent: Record<string, string>,
): TalentChange[] {
  const entries = (c: ClassData) =>
    new Map(c.trees.flatMap((tree) => tree.talents.map((t) => [t.id, { tree, t }] as const)))
  const a = entries(baseline),
    b = entries(experiment)
  const describe = (x: NonNullable<ReturnType<typeof a.get>>) =>
    `${x.tree.name}, row ${x.t.row + 1}, column ${x.t.col + 1}; ${x.t.maxRank} rank${x.t.maxRank === 1 ? '' : 's'}${x.t.requires ? `; requires ${x.t.requires.map((r) => `${r.talent} ${r.rank}`).join(', ')}` : ''}`
  const result: TalentChange[] = []
  for (const id of new Set([...a.keys(), ...b.keys()])) {
    const old = a.get(id),
      next = b.get(id)
    const kinds: TalentChange['kinds'] = []
    if (!old) kinds.push('Added')
    else if (!next) kinds.push('Removed')
    else {
      if (old.tree.id !== next.tree.id || old.t.row !== next.t.row || old.t.col !== next.t.col) kinds.push('Moved')
      const content = (t: Talent) =>
        Object.fromEntries(
          Object.entries(t).filter(
            ([key]) =>
              !['source', 'ranksSource', 'ranksObserved', 'ranksPrior', 'ranksNote', 'row', 'col'].includes(key),
          ),
        )
      if (stable(content(old.t)) !== stable(content(next.t))) kinds.push('Modified')
    }
    if (kinds.length)
      result.push({
        id,
        name: (next ?? old)!.t.name,
        kinds,
        intent: intent[id] ?? '',
        before: old ? describe(old) : undefined,
        after: next ? describe(next) : undefined,
      })
  }
  return result
}
export interface RulesetContext {
  cls: ClassData
  registry: EncodingRegistry
  manifest: RulesetManifest
  baseline?: RulesetManifest
  changes: TalentChange[]
}
const cache = new Map<string, Promise<RulesetContext>>()
export async function loadRuleset(
  classId: string,
  identity: RulesetIdentity = LEGACY_BASELINE,
): Promise<RulesetContext> {
  const key = `${identity.ruleset}/${identity.revision}/${classId}`
  let pending = cache.get(key)
  if (!pending) {
    pending = resolve(classId, identity)
    cache.set(key, pending)
  }
  return pending
}
async function resolve(classId: string, identity: RulesetIdentity): Promise<RulesetContext> {
  const manifest = manifestFor(identity)
  // Fictional examples keep their original development-only path and registry.
  if (!manifest.classes.includes(classId)) {
    if (
      identity.ruleset === LEGACY_BASELINE.ruleset &&
      identity.revision === 1 &&
      hasClass(classId) &&
      !listRulesets(classId).length
    ) {
      return { cls: await loadClass(classId), registry: loadRegistry(), manifest, changes: [] }
    }
    throw new Error('This class is not available in this ruleset revision.')
  }
  const prefix = `../../../data/rulesets/${manifest.id}/r${manifest.revision}/`
  const raw = await datasets[`${prefix}classes/${classId}.json`]!()
  const cls = import.meta.env.DEV
    ? (await import('./schema.zod')).parseClass(raw, `${manifest.id}/r${manifest.revision}/${classId}`)
    : raw
  const [versions, steps] = await Promise.all([
    Promise.all(
      Object.entries(encodings)
        .filter(([p]) => p.startsWith(prefix))
        .map(([, load]) => load()),
    ),
    Promise.all(
      Object.entries(migrations)
        .filter(([p]) => p.startsWith(prefix))
        .map(([, load]) => load()),
    ),
  ])
  const registry = buildRegistry(versions, steps)
  // A published class must have explicit coverage; derived-order fallback is for examples only.
  if (!registry.versions[cls.dataVersion]?.classes[classId]) throw new Error('This ruleset encoding is unavailable.')
  if (manifest.kind === 'baseline') return { cls, registry, manifest, changes: [] }
  const pin = manifest.baseline!
  const baseline = await loadRuleset(classId, { ruleset: pin.id, revision: pin.revision })
  return {
    cls,
    registry,
    manifest,
    baseline: baseline.manifest,
    changes: compareTalents(baseline.cls, cls, manifest.changes?.[classId] ?? {}),
  }
}
