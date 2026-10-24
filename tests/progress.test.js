import { test } from 'node:test'
import assert from 'node:assert/strict'
import { readFileSync } from 'node:fs'
import { courseProgress, toggleTask, setNote, currentWeek, sectionsInWeek, tasksForWeek, weekStartDate, parseLocalDate, toLocalDateString, emptyCourseProgress } from '../src/lib/progress.js'

const course = JSON.parse(readFileSync(new URL('../public/courses/ai-generalist.json', import.meta.url), 'utf8'))
const at = (y, m, d) => new Date(y, m - 1, d, 15, 30)

test('progress counts only tasks that exist in the course', () => {
  const p = courseProgress(course, { 'l0-p1': '2026-10-24T00:00:00Z', 'removed-task': 'x' })
  assert.equal(p.done, 1)
  assert.equal(p.total, 41)
  assert.equal(p.percent, 2)
  assert.deepEqual(p.bySection['level-0'], { done: 1, total: 2, percent: 50 })
  assert.deepEqual(p.bySection.intro, { done: 0, total: 0, percent: 0 })
})

test('toggling a task on and off', () => {
  let p = emptyCourseProgress()
  p = toggleTask(p, 'l0-p1', new Date('2026-10-24T10:00:00Z'))
  assert.equal(p.done['l0-p1'], '2026-10-24T10:00:00.000Z')
  p = toggleTask(p, 'l0-p1')
  assert.deepEqual(p.done, {})
})

test('notes are saved and blank notes are removed', () => {
  let p = setNote(emptyCourseProgress(), 'l0-p1', 'Link: https://x')
  assert.equal(p.notes['l0-p1'], 'Link: https://x')
  p = setNote(p, 'l0-p1', '   ')
  assert.deepEqual(p.notes, {})
})

test('dates are read as local calendar days', () => {
  const d = parseLocalDate('2026-11-01')
  assert.equal(d.getDate(), 1)
  assert.equal(toLocalDateString(d), '2026-11-01')
  assert.equal(parseLocalDate('01/11/2026'), null)
})

test('current week at full pace: start day is Week 0', () => {
  const p = { ...emptyCourseProgress(), pace: 'full', startDate: '2026-11-01' }
  assert.deepEqual(currentWeek(course, p, at(2026, 11, 1)), { week: 0, status: 'running' })
  assert.deepEqual(currentWeek(course, p, at(2026, 11, 7)), { week: 0, status: 'running' })
  assert.deepEqual(currentWeek(course, p, at(2026, 11, 8)), { week: 1, status: 'running' })
  assert.deepEqual(currentWeek(course, p, at(2027, 4, 18)).week, 24)
  assert.equal(currentWeek(course, p, at(2027, 6, 1)).status, 'finished')
})

test('light pace takes two calendar weeks per course week', () => {
  const p = { ...emptyCourseProgress(), pace: 'light', startDate: '2026-11-01' }
  assert.equal(currentWeek(course, p, at(2026, 11, 14)).week, 0)
  assert.equal(currentWeek(course, p, at(2026, 11, 15)).week, 1)
  assert.equal(weekStartDate(course, p, 2).getDate(), 29)
})

test('before the start date and with no date', () => {
  const p = { ...emptyCourseProgress(), startDate: '2026-11-10' }
  assert.equal(currentWeek(course, p, at(2026, 11, 1)).status, 'not-yet')
  assert.equal(currentWeek(course, p, at(2026, 11, 1)).daysToStart, 9)
  assert.equal(currentWeek(course, emptyCourseProgress()).status, 'not-started')
})

test('sections active in week 14 include Level 4, the gate and the business track', () => {
  const ids = sectionsInWeek(course, 14).map((s) => s.id)
  assert.deepEqual(ids, ['level-4', 'decision-gate', 'business-track'])
})

test('tasks for a week: current business phase only, overdue first', () => {
  const p = { ...emptyCourseProgress(), done: {} }
  const w6 = tasksForWeek(course, p, 6).map((t) => t.id)
  assert.ok(w6.includes('l2-p1'))
  assert.ok(w6.includes('bt-w3-4'), 'earlier business phase is overdue and shown')
  assert.ok(w6.includes('bt-w5-7'), 'current business phase shown')
  assert.ok(!w6.includes('bt-w8-10'), 'future business phase hidden')
  assert.equal(w6[0], 'bt-w3-4')
  const done = tasksForWeek(course, { done: { 'bt-w3-4': 'x' } }, 6).map((t) => t.id)
  assert.ok(!done.includes('bt-w3-4'))
})
