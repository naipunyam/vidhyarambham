import { test } from 'node:test'
import assert from 'node:assert/strict'
import { pickContinue } from '../src/lib/continue.js'

const course = (id, weeks = 10) => ({
  id,
  title: id,
  sections: [
    { id: `${id}-a`, title: 'A', weeks: [1, 2], tasks: [{ id: `${id}-t1`, text: 'One' }, { id: `${id}-t2`, text: 'Two' }] },
    { id: `${id}-b`, title: 'B', weeks: [3, weeks], tasks: [{ id: `${id}-t3`, text: 'Three' }] },
  ],
})

const today = new Date(2026, 10, 3) // 3 Nov 2026
const entries = [{ course: course('first') }, { course: course('second') }, { course: course('third') }]

test('no running course: nothing to continue', () => {
  assert.equal(pickContinue(entries, { progress: {}, imported: {} }, today), null)
})

test('picks the running course with the most recent tick', () => {
  const state = {
    imported: {},
    progress: {
      first: { done: { 'first-t1': '2026-11-01T10:00:00.000Z' }, notes: {}, pace: null, startDate: '2026-10-30' },
      second: { done: { 'second-t1': '2026-11-02T09:00:00.000Z' }, notes: {}, pace: null, startDate: '2026-10-30' },
      third: { done: {}, notes: {}, pace: null, startDate: '2027-01-01' },
    },
  }
  const pick = pickContinue(entries, state, today)
  assert.equal(pick.course.id, 'second')
  assert.equal(pick.week, 1)
  assert.equal(pick.lastWeek, 10)
  assert.equal(pick.open, 1)
})

test('without ticks, the first running course in library order', () => {
  const state = {
    imported: {},
    progress: {
      second: { done: {}, notes: {}, pace: null, startDate: '2026-10-30' },
      third: { done: {}, notes: {}, pace: null, startDate: '2026-10-29' },
    },
  }
  assert.equal(pickContinue(entries, state, today).course.id, 'second')
})
