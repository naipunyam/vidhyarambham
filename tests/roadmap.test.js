import { test } from 'node:test'
import assert from 'node:assert/strict'
import { readFileSync } from 'node:fs'
import { buildRoadmap } from '../src/lib/roadmap.js'
import { validateCourse } from '../src/lib/courseFormat.js'

const course = JSON.parse(readFileSync(new URL('../public/courses/ai-generalist.json', import.meta.url), 'utf8'))

test('roadmap lists the steps in course order, like the document', () => {
  const { rows, track } = buildRoadmap(course)
  assert.deepEqual(rows.map((r) => r.id), ['week-0', 'level-0', 'level-1', 'level-2', 'level-3', 'level-4', 'decision-gate', 'level-5', 'capstone'])
  assert.equal(track.id, 'business-track')
})

test('the business track runs beside Level 1 to the capstone, with each phase next to its level', () => {
  const { rows } = buildRoadmap(course)
  const by = Object.fromEntries(rows.map((r) => [r.id, r]))
  assert.equal(by['level-0'].inTrack, false)
  assert.equal(by['level-1'].inTrack, true)
  assert.equal(by.capstone.inTrack, true)
  assert.deepEqual(by['level-1'].trackItems.map((t) => t.id), ['bt-w3-4'])
  assert.deepEqual(by['level-4'].trackItems.map((t) => t.id), ['bt-w11-14'])
  assert.deepEqual(by['decision-gate'].trackItems, [])
  assert.deepEqual(by['level-5'].trackItems.map((t) => t.id), ['bt-w15-18'])
})

test('roadmap shows ticks', () => {
  const { rows } = buildRoadmap(course, { 'l0-p1': 'x', 'l0-exit': 'x', 'bt-w3-4': 'x' })
  const by = Object.fromEntries(rows.map((r) => [r.id, r]))
  assert.equal(by['level-0'].done, by['level-0'].total)
  assert.equal(by['level-1'].trackItems[0].done, true)
})

test('roadmap settings are checked', () => {
  const c = structuredClone(course)
  c.sections[0].roadmap = 'yes'
  assert.match(validateCourse(c)[0], /roadmap/)
  c.sections[0].roadmap = { title: 5 }
  assert.match(validateCourse(c)[0], /roadmap.title/)
})

test('a course with no track still gets a roadmap', () => {
  const c = { sections: [{ id: 'a', kind: 'level', title: 'A', weeks: [1, 1] }, { id: 'b', kind: 'reference', title: 'B' }] }
  const r = buildRoadmap(c)
  assert.equal(r.rows.length, 1)
  assert.equal(r.track, null)
})
