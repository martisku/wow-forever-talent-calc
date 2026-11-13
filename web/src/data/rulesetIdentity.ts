/** Small identity metadata for the landing page; no class loaders or encoding registries. */
import current from '../../../data/current-reference.json'

export interface RulesetIdentity {
  ruleset: string
  revision: number
}
export interface CurrentReference extends RulesetIdentity {
  source?: { version: string; retrievedAt: string }
}
export const LEGACY_BASELINE = { ruleset: 'reference-2026-11-10', revision: 1 }
export const currentReference: CurrentReference = current
