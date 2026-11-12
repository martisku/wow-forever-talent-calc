import { createContext, useContext } from 'react'
import type { RulesetContext } from '../data/rulesets'

export const ExperimentContext = createContext<RulesetContext | undefined>(undefined)
export function useCustomTalent(id: string) {
  const context = useContext(ExperimentContext)
  return context?.changes.find((c) => c.id === id)
}
export function useExperiment() {
  return useContext(ExperimentContext)
}
