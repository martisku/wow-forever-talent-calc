import { classHash } from '../url/route'
import { LEGACY_BASELINE, listRulesets, rulesetLabel, type RulesetContext } from '../data/rulesets'
import './rulesets.css'

export function RulesetPanel({ context, compact = false }: { context: RulesetContext; compact?: boolean }) {
  const { manifest: m, baseline, cls, changes } = context
  const current = `${m.id}/${m.revision}`
  return (
    <section className="panel ruleset-panel" aria-label="Ruleset" data-testid="ruleset-panel">
      <strong data-testid="ruleset-name">{rulesetLabel(m)}</strong>
      {m.source && (
        <p data-testid="reference-source">
          Published by <a href={m.source.pageUrl}>Wowhead Forever</a> · version {m.source.version} · retrieved{' '}
          {m.source.retrievedAt.slice(0, 10)}. May lag hotfixes; not independently verified in game.
        </p>
      )}
      {m.kind === 'experiment' && (
        <p>Experimental design · 51 shared points · structural legality, not proof of balance.</p>
      )}
      {baseline && <p>Compared with {rulesetLabel(baseline)}.</p>}
      {!compact && (
        <>
          <div className="ruleset-picker">
            <label htmlFor="ruleset-choice">Ruleset</label>
            <select
              id="ruleset-choice"
              value={current}
              aria-describedby="ruleset-switch-note"
              onChange={(e) => {
                const [ruleset, revision] = e.target.value.split('/')
                window.location.hash = classHash(cls.class, cls.dataVersion, '', {
                  ruleset: ruleset!,
                  revision: Number(revision),
                })
              }}
            >
              {listRulesets(cls.class).map((choice) => (
                <option key={`${choice.id}/${choice.revision}`} value={`${choice.id}/${choice.revision}`}>
                  {rulesetLabel(choice)}
                </option>
              ))}
            </select>
            {m.kind === 'experiment' && (
              <a className="btn" href={classHash(cls.class, 1, '', LEGACY_BASELINE)}>
                Reference snapshot
              </a>
            )}
          </div>
          <p id="ruleset-switch-note">Switching starts an empty build. Use Back to return to your previous build.</p>
          <p>{m.intent}</p>
          {changes.length > 0 && (
            <details data-testid="design-changes">
              <summary>Design changes ({changes.length}) and investment tradeoffs</summary>
              <ul>
                {changes.map((c) => (
                  <li key={c.id}>
                    <strong>
                      {c.kinds.join(' + ')}: {c.name}
                    </strong>
                    <p>{c.intent}</p>
                    {c.before && <p>Reference: {c.before}</p>}
                    {c.after && <p>Design: {c.after}</p>}
                  </li>
                ))}
              </ul>
            </details>
          )}
        </>
      )}
    </section>
  )
}
