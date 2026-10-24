import { test } from 'node:test'
import assert from 'node:assert/strict'
import { loadState, saveState, emptyState, mergeCourses, makeBackup, readBackup, withImportedCourse, withoutImportedCourse, withProgress, getProgress, STORAGE_KEY } from '../src/lib/state.js'

const memoryStorage = () => {
  const m = new Map()
  return { getItem: (k) => (m.has(k) ? m.get(k) : null), setItem: (k, v) => m.set(k, String(v)), map: m }
}
const course = (id, version = 1) => ({ format: 'vidhyarambham-course', formatVersion: 1, id, version, title: id, sections: [{ id: 's', title: 's', kind: 'level', tasks: [{ id: 't', text: 't' }] }] })

test('state saves and loads', () => {
  const s = memoryStorage()
  let state = withProgress(emptyState(), 'a', { done: { t: 'x' }, notes: {}, pace: 'full', startDate: '2026-11-01' })
  state = withImportedCourse(state, course('b'))
  assert.equal(saveState(s, state), true)
  assert.deepEqual(loadState(s), state)
})

test('broken or missing saved data gives an empty state instead of crashing', () => {
  const s = memoryStorage()
  assert.deepEqual(loadState(s), emptyState())
  s.setItem(STORAGE_KEY, '{oops')
  assert.deepEqual(loadState(s), emptyState())
  assert.deepEqual(loadState(null), emptyState())
})

test('saveState reports failure when the browser refuses', () => {
  assert.equal(saveState({ setItem() { throw new Error('full') } }, emptyState()), false)
})

test('invalid imported courses are dropped on load', () => {
  const s = memoryStorage()
  s.setItem(STORAGE_KEY, JSON.stringify({ progress: {}, imported: { bad: { id: 'bad' }, good: course('good') } }))
  assert.deepEqual(Object.keys(loadState(s).imported), ['good'])
})

test('merge: higher version wins, ties keep the shipped copy', () => {
  const merged = mergeCourses([course('a', 2), course('b', 1)], { a: course('a', 2), b: course('b', 3), c: course('c') })
  const byId = Object.fromEntries(merged.map((m) => [m.course.id, m]))
  assert.equal(byId.a.source, 'shipped')
  assert.equal(byId.a.alsoImported, true)
  assert.equal(byId.b.source, 'imported')
  assert.equal(byId.b.course.version, 3)
  assert.equal(byId.c.source, 'imported')
})

test('removing an imported course keeps its progress', () => {
  let state = withImportedCourse(emptyState(), course('x'))
  state = withProgress(state, 'x', { done: { t: 'y' }, notes: {}, pace: null, startDate: null })
  state = withoutImportedCourse(state, 'x')
  assert.deepEqual(state.imported, {})
  assert.equal(getProgress(state, 'x').done.t, 'y')
})

test('backup round trip', () => {
  const state = withProgress(withImportedCourse(emptyState(), course('z')), 'z', { done: { t: '1' }, notes: { t: 'n' }, pace: 'light', startDate: '2026-11-01' })
  const text = JSON.stringify(makeBackup(state, new Date('2026-10-24T00:00:00Z')))
  assert.deepEqual(readBackup(text).state, state)
})

test('reading the wrong file as a backup explains what happened', () => {
  assert.match(readBackup('nope').error, /not valid JSON/)
  assert.match(readBackup(JSON.stringify(course('q'))).error, /course file, not a backup/)
  assert.match(readBackup(JSON.stringify({ format: 'vidhyarambham-backup', formatVersion: 9 })).error, /version 9/)
})
