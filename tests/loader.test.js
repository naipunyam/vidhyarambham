import { test } from 'node:test'
import assert from 'node:assert/strict'
import { readFileSync } from 'node:fs'
import { loadShippedCourses, loadCourseFromUrl } from '../src/lib/loader.js'

// Every course listed in index.json, read from disk, served by a fake fetch.
const indexText = readFileSync(new URL('../public/courses/index.json', import.meta.url), 'utf8')
const files = { '/b/courses/index.json': indexText }
for (const name of JSON.parse(indexText).courses) {
  files[`/b/courses/${name}`] = readFileSync(new URL(`../public/courses/${name}`, import.meta.url), 'utf8')
}
const fakeFetch = (map) => async (url) => {
  if (!(url in map)) return { ok: false, status: 404, json: async () => ({}), text: async () => '' }
  const body = map[url]
  return { ok: true, status: 200, json: async () => JSON.parse(body), text: async () => body }
}

test('loads shipped courses listed in index.json', async () => {
  const r = await loadShippedCourses('/b/', fakeFetch(files))
  assert.deepEqual(r.problems, [])
  assert.deepEqual(r.courses.map((c) => c.id), ['ai-generalist', 'entrepreneurship'])
})

test('a broken course file is skipped with a clear problem, others still load', async () => {
  const map = { ...files, '/b/courses/index.json': JSON.stringify({ courses: ['ai-generalist.json', 'broken.json', '../evil.json'] }), '/b/courses/broken.json': '{"format":"vidhyarambham-course"}' }
  const r = await loadShippedCourses('/b/', fakeFetch(map))
  assert.equal(r.courses.length, 1)
  assert.equal(r.problems.length, 2)
  assert.match(r.problems.join(' '), /broken.json has/)
  assert.match(r.problems.join(' '), /not a course file name/)
})

test('offline: no course list', async () => {
  const r = await loadShippedCourses('/b/', async () => { throw new Error('offline') })
  assert.equal(r.offline, true)
  assert.deepEqual(r.courses, [])
})

test('import from a link', async () => {
  const map = { 'https://raw.example/c.json': files['/b/courses/ai-generalist.json'] }
  assert.equal((await loadCourseFromUrl('https://raw.example/c.json', fakeFetch(map))).course.id, 'ai-generalist')
  assert.match((await loadCourseFromUrl('http://insecure', fakeFetch(map))).errors[0], /https/)
  assert.match((await loadCourseFromUrl('https://raw.example/missing.json', fakeFetch(map))).errors[0], /HTTP 404/)
})
