import { describe, it, expect } from 'vitest'
import { compareTalents, loadRuleset, LEGACY_BASELINE, listRulesets } from './rulesets'
import { decode, encode } from '../url/codec'
import { buildHash, classHash, parseHash } from '../url/route'
import { parseImport } from '../url/import'
import { add, canAdd, pointsInTree, totalPoints } from '../rules'
import { readLastBuild, writeLastBuild } from '../ui/storage'

const study = { ruleset: 'shaman-investment-study', revision: 1 }
describe('immutable ruleset contexts', () => {
  it('preserves a fixed legacy allocation and isolates equal encoding versions', async () => {
    const baseline = await loadRuleset('shaman')
    const custom = await loadRuleset('shaman', study)
    expect(baseline.manifest.id).toBe(LEGACY_BASELINE.ruleset)
    const old = decode(baseline.cls, '5', 1, baseline.registry)
    expect(old.notices).toEqual([])
    expect(old.build).toEqual({ 'elemental-combat': { convection: 5 } })
    const alternative = decode(custom.cls, '2', 1, custom.registry)
    expect(alternative.build).toEqual({ 'elemental-combat': { 'earths-grasp': 2 } })
    expect(encode(baseline.cls, old.build, baseline.registry)).toBe('5')
    expect((await loadRuleset('shaman')).cls).toBe(baseline.cls)
    expect(custom.cls).not.toBe(baseline.cls)
  })
  it('computes additions, modifications, moves and removals against the pinned baseline', async () => {
    const c = await loadRuleset('shaman', study)
    expect(Object.fromEntries(c.changes.map((x) => [x.id, x.kinds]))).toEqual({
      'earths-grasp': ['Moved'],
      'totemic-focus': ['Modified'],
      'totemic-relay': ['Added'],
      'improved-reincarnation': ['Removed'],
    })
    expect(c.changes.every((x) => x.intent.length > 0)).toBe(true)
    const b = await loadRuleset('shaman')
    const reordered = structuredClone(b.cls)
    reordered.trees.reverse()
    expect(compareTalents(b.cls, reordered, {})).toEqual([])
  })
  it('keeps the 51-point pool and explains new prerequisite costs', async () => {
    const { cls } = await loadRuleset('shaman', study)
    expect(cls.rules.maxPoints).toBe(51)
    expect(canAdd(cls, {}, 'elemental-combat', 'totemic-relay')).toMatchObject({ ok: false, reason: 'row-locked' })
    let build = {}
    for (const [id, n] of [
      ['convection', 5],
      ['concussion', 5],
    ] as const)
      for (let i = 0; i < n; i++) build = add(cls, build, 'elemental-combat', id)
    expect(canAdd(cls, build, 'elemental-combat', 'totemic-relay')).toMatchObject({ ok: false, reason: 'prereq' })
    build = add(cls, build, 'elemental-combat', 'elemental-focus')
    expect(canAdd(cls, build, 'elemental-combat', 'totemic-relay')).toEqual({ ok: true })
    build = add(cls, build, 'elemental-combat', 'totemic-relay')
    expect(pointsInTree(build, 'elemental-combat')).toBe(12)
    expect(totalPoints(build)).toBe(12)
    expect(canAdd(cls, { 'elemental-combat': { convection: 51 } }, 'elemental-combat', 'concussion')).toMatchObject({
      ok: false,
      reason: 'no-points',
    })
  })
  it('never falls back for an unknown identity, revision or unsupported class', async () => {
    await expect(loadRuleset('shaman', { ...study, revision: 99 })).rejects.toThrow('unavailable')
    await expect(loadRuleset('warrior', study)).rejects.toThrow('not available')
    await expect(loadRuleset('shaman', { ruleset: 'missing', revision: 1 })).rejects.toThrow('unavailable')
    expect(listRulesets('shaman').map((m) => m.id)).toEqual(
      expect.arrayContaining([LEGACY_BASELINE.ruleset, study.ruleset]),
    )
    expect(listRulesets('warrior').some((m) => m.id === study.ruleset)).toBe(false)
  })
})
describe('portable ruleset identity', () => {
  it('keeps identity on empty builds and view state', () => {
    const empty = classHash('shaman', 1, '', study)
    expect(empty).toBe('#/shaman?ruleset=shaman-investment-study&rev=1')
    expect(parseHash(empty)).toMatchObject({ ruleset: study.ruleset, revision: 1 })
    const full = classHash('shaman', 1, '2', { ...study, sel: 'earths-grasp', embed: true })
    expect(buildHash(parseHash(full))).toBe(full)
    expect(parseImport(`https://example.com/fork/${full}`)).toMatchObject({ kind: 'link', identity: study, build: '2' })
    expect(classHash('shaman', 1, '5')).toBe('#/shaman?v=1&t=5')
  })
  it.each([
    'ruleset=x',
    'rev=1',
    'ruleset=x&rev=0',
    'ruleset=x&rev=1.5',
    'ruleset=x&rev=1&rev=2',
    'ruleset=x&rev=1&ruleset=y',
    'ruleset=x&rev=9007199254740992',
  ])('rejects malformed identity %s', (query) => {
    expect(parseHash(`#/shaman?${query}`)).toMatchObject({ kind: 'unknown' })
    expect(parseImport(`#/shaman?${query}`)).toMatchObject({ kind: 'error' })
  })
  it('preserves identity in continue storage while accepting old baseline entries', () => {
    let raw: string | null = null
    const storage = {
      getItem: () => raw,
      setItem: (_key: string, value: string) => {
        raw = value
      },
      removeItem: () => {
        raw = null
      },
    }
    const entry = { classId: 'shaman', v: 1, t: '2', className: 'Shaman', spread: '2/0/0', ...study }
    writeLastBuild(entry, storage)
    expect(readLastBuild(storage)).toMatchObject(entry)
    raw = JSON.stringify({ ...entry, revision: undefined })
    expect(readLastBuild(storage)).toBeUndefined()
    raw = JSON.stringify({ classId: 'shaman', v: 1, t: '5', className: 'Shaman', spread: '5/0/0', savedAt: 1 })
    expect(readLastBuild(storage)?.ruleset).toBeUndefined()
  })
})
