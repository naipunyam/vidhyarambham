import { test } from 'node:test'
import assert from 'node:assert/strict'
import { readFileSync, readdirSync } from 'node:fs'
import { validateCourse, parseCourseText, allTasks } from '../src/lib/courseFormat.js'

const minimal = () => ({
  format: 'vidhyarambham-course',
  formatVersion: 1,
  id: 'demo',
  version: 1,
  title: 'Demo',
  sections: [{ id: 's1', title: 'One', kind: 'level', tasks: [{ id: 't1', text: 'Do it' }] }],
})

test('a minimal course is valid', () => {
  assert.deepEqual(validateCourse(minimal()), [])
})

test('every shipped course file is valid and listed in index.json', () => {
  const dir = new URL('../public/courses/', import.meta.url)
  const index = JSON.parse(readFileSync(new URL('index.json', dir), 'utf8'))
  const files = readdirSync(dir).filter((f) => f.endsWith('.json') && f !== 'index.json')
  assert.deepEqual([...index.courses].sort(), files.sort(), 'index.json must list exactly the course files in the folder')
  const ids = new Set()
  for (const f of files) {
    const course = JSON.parse(readFileSync(new URL(f, dir), 'utf8'))
    assert.deepEqual(validateCourse(course), [], `${f} should be valid`)
    assert.ok(!ids.has(course.id), `course id ${course.id} is used by two files`)
    ids.add(course.id)
  }
})

test('rejects duplicate task ids across sections', () => {
  const c = minimal()
  c.sections.push({ id: 's2', title: 'Two', kind: 'level', tasks: [{ id: 't1', text: 'Again' }] })
  const errors = validateCourse(c)
  assert.equal(errors.length, 1)
  assert.match(errors[0], /"t1" is used twice/)
})

test('rejects bad ids, kinds, weeks and missing fields', () => {
  const c = minimal()
  c.id = 'Has Spaces'
  c.version = 0
  c.sections[0].kind = 'chapter'
  c.sections[0].weeks = [3, 1]
  c.sections[0].tasks[0].kind = 'quiz'
  delete c.title
  const errors = validateCourse(c).join('\n')
  for (const field of ['id', 'version', 'title', 'kind', 'weeks', 'tasks[0].kind']) assert.match(errors, new RegExp(field.replace(/[[\]]/g, '\\$&')))
})

test('rejects the wrong format marker, so backups are not mistaken for courses', () => {
  const c = minimal()
  c.format = 'vidhyarambham-backup'
  assert.match(validateCourse(c)[0], /format/)
})

test('parseCourseText reports broken JSON in plain words', () => {
  const r = parseCourseText('{ not json')
  assert.ok(r.errors[0].startsWith('This is not valid JSON'))
  assert.ok(parseCourseText(JSON.stringify(minimal())).course)
})

test('allTasks flattens tasks with their section id', () => {
  assert.deepEqual(allTasks(minimal()), [{ id: 't1', text: 'Do it', sectionId: 's1' }])
})
