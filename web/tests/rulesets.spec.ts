import { expect, test } from '@playwright/test'
const study = '#/shaman?ruleset=shaman-investment-study&rev=1'

test('switch, edit, share and return to an unchanged reference build', async ({ page }) => {
  await page.goto('/#/shaman?v=1&t=5')
  await expect(page.getByTestId('talent-convection')).toHaveAttribute('data-rank', '5')
  await page.getByRole('combobox', { name: 'Ruleset', exact: true }).selectOption('shaman-investment-study/1')
  await expect(page).toHaveURL(new RegExp('ruleset=shaman-investment-study&rev=1$'))
  await expect(page.getByTestId('points-left')).toHaveText('51')
  const moved = page.getByTestId('talent-earths-grasp')
  await expect(moved).toHaveAccessibleName(/custom design/)
  await expect(moved.locator('.custom-flag')).toContainText('Moved')
  await expect(page.getByTestId('talent-improved-reincarnation')).toHaveCount(0)
  await moved.click()
  await expect(moved).toHaveAttribute('data-rank', '1')
  const link = await page.getByTestId('copy-link').getAttribute('data-link')
  expect(link).toContain('ruleset=shaman-investment-study&rev=1&v=1&t=1')
  await expect(page.getByTestId('copy-code')).toBeDisabled()
  await page.reload()
  await expect(moved).toHaveAttribute('data-rank', '1')
  await page.getByRole('combobox', { name: 'Ruleset', exact: true }).selectOption('reference-2026-11-10/1')
  await expect(page.getByTestId('points-left')).toHaveText('51')
  await page.goBack()
  await expect(moved).toHaveAttribute('data-rank', '1')
  await expect(page.getByTestId('ruleset-name')).toContainText('Shaman investment study')
})

test('shows design intent, removals and authored rank text without reference claims', async ({ page }) => {
  await page.goto(`/${study}&sel=totemic-relay`)
  await expect(page.getByTestId('tooltip-totemic-relay')).toContainText('refreshes your active totems')
  await expect(page.getByTestId('tooltip-totemic-relay')).toContainText('custom design')
  await expect(page.getByTestId('tooltip-totemic-relay')).not.toContainText('Not known yet')
  await page.getByTestId('design-changes').locator('summary').click()
  await expect(page.getByTestId('design-changes')).toContainText('Removed: Improved Reincarnation')
  await expect(page.getByTestId('design-changes')).toContainText('three ranks')
  await expect(page.getByTestId('changes-link')).toHaveCount(0)
  await expect(page.getByTestId('copy-link')).toHaveAttribute(
    'data-link',
    new RegExp('ruleset=shaman-investment-study&rev=1'),
  )
  await page.emulateMedia({ media: 'print' })
  await expect(page.getByTestId('ruleset-name')).toBeVisible()
})

test('full link import, continue and embed preserve ruleset identity', async ({ page }) => {
  await page.goto('/#/shaman')
  await page.getByTestId('open-import').click()
  await page.getByTestId('import-input').fill(`${study}&v=1&t=2`)
  await page.getByTestId('import-check').click()
  await expect(page.getByTestId('import-report')).toContainText('Shaman investment study')
  await page.getByTestId('import-apply').click()
  await expect(page.getByTestId('talent-earths-grasp')).toHaveAttribute('data-rank', '2')
  await page.goto('/#/')
  await expect(page.getByTestId('continue-link')).toHaveAttribute('href', `${study}&v=1&t=2`)
  await page.goto(`/${study}&v=1&t=2&embed=1`)
  await expect(page.getByTestId('ruleset-name')).toContainText('Shaman investment study')
  await expect(page.getByTestId('embed-open')).toHaveAttribute(
    'href',
    new RegExp('ruleset=shaman-investment-study&rev=1&v=1&t=2'),
  )
})

test('rejects ambiguous imports and unavailable revisions without a plausible baseline build', async ({ page }) => {
  await page.goto(`/${study}`)
  await page.getByTestId('open-import').click()
  await page.getByTestId('import-input').fill('2')
  await page.getByTestId('import-check').click()
  await expect(page.getByTestId('import-error')).toContainText('full build link')
  await page.goto('/#/shaman?ruleset=shaman-investment-study&rev=99&v=1&t=2')
  await expect(page.getByText('This ruleset revision is unavailable.', { exact: false })).toBeVisible()
  await expect(page.locator('[data-talent]')).toHaveCount(0)
  await page.goto(`/${study}&v=99&t=2`)
  await expect(page.getByText('This ruleset encoding is unavailable.', { exact: false })).toBeVisible()
  await expect(page.locator('[data-talent]')).toHaveCount(0)
})
