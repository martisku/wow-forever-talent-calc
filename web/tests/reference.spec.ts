import { expect, test } from '@playwright/test'
import current from '../../data/current-reference.json' with { type: 'json' }

const imported = '#/shaman?ruleset=wowhead-forever-1-60-1-1794343902-40a6e759692c&rev=1'

test('current reference cards open a versioned snapshot and class switching preserves it', async ({ page }) => {
  await page.goto('/#/')
  await expect(page.getByTestId('landing-caveat')).toContainText('Current reference: Wowhead Forever')
  await page.getByTestId('class-shaman').click()
  await expect(page).toHaveURL(new RegExp(`ruleset=${current.ruleset}&rev=${current.revision}`))
  await expect(page.getByTestId('reference-source')).toContainText('retrieved')
  await expect(page.getByTestId('class-ranks-line')).toContainText('published by Wowhead')
  await expect(page.getByTestId('changes-link')).toHaveCount(0)
  await expect(page.getByTestId('summary-hints')).not.toContainText('Highlight changes')
  await page.getByTestId('class-chip-mage').click()
  await expect(page).toHaveURL(new RegExp(`ruleset=${current.ruleset}&rev=${current.revision}`))
  await expect(page.getByTestId('reference-source')).toBeVisible()
})

test('imported allocations share and reload without losing snapshot identity', async ({ page }) => {
  await page.goto(`/${imported}`)
  const cell = page.locator('[data-talent][data-addable="true"]').first()
  const id = await cell.getAttribute('data-talent')
  await cell.click()
  await expect(page.getByTestId('points-left')).toHaveText('50')
  await expect(page.getByTestId('copy-code')).toBeDisabled()
  const url = await page.getByTestId('copy-link').getAttribute('data-link')
  expect(url).toContain('ruleset=wowhead-forever-1-60-1-1794343902-40a6e759692c&rev=1&v=1&t=')
  await page.reload()
  await expect(page.locator(`[data-talent="${id}"]`)).toHaveAttribute('data-rank', '1')
  await expect(page.getByTestId('reference-source')).toBeVisible()
})

test('unresolved publisher text is marked without fabricated values or video provenance', async ({ page }) => {
  await page.goto('/#/rogue?ruleset=wowhead-forever-1-60-1-1794343902-40a6e759692c&rev=1&sel=wh-110866')
  await expect(page.getByTestId('talent-wh-110866')).toHaveAccessibleName(/publisher formula not fully resolved/)
  const tooltip = page.getByTestId('tooltip-wh-110866')
  await expect(tooltip).toContainText('$mcrit')
  await expect(page.getByTestId('source-warning-wh-110866')).toBeVisible()
  await expect(tooltip).not.toContainText('Entered by hand.')
  await expect(tooltip).not.toContainText('Read from the stream')
})

test('legacy routes and the original design retain their original baseline after an update', async ({ page }) => {
  await page.goto('/#/shaman?v=1&t=5')
  await expect(page.getByTestId('talent-convection')).toHaveAttribute('data-rank', '5')
  await expect(page.getByTestId('reference-source')).toHaveCount(0)
  await expect(page.getByTestId('ruleset-name')).toContainText('Reference snapshot (2026-11-10)')
  await page.goto('/#/shaman?ruleset=shaman-investment-study&rev=1&v=1&t=2')
  await expect(page.getByTestId('talent-earths-grasp')).toHaveAttribute('data-rank', '2')
  await expect(page.getByTestId('ruleset-panel')).toContainText('Reference snapshot (2026-11-10)')
})
