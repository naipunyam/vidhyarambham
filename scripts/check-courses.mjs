// Checks every course file in public/courses before the site is built.
// Run with: npm run check-courses
import { readFileSync, readdirSync } from 'node:fs'
import { validateCourse } from '../src/lib/courseFormat.js'

const dir = new URL('../public/courses/', import.meta.url)
const index = JSON.parse(readFileSync(new URL('index.json', dir), 'utf8'))
const listed = new Set(index.courses)
const files = readdirSync(dir).filter((f) => f.endsWith('.json') && f !== 'index.json')
let failed = false

for (const f of files) {
  if (!listed.has(f)) {
    console.error(`✗ ${f} is in public/courses but not listed in index.json`)
    failed = true
  }
}
for (const f of listed) {
  if (!files.includes(f)) {
    console.error(`✗ index.json lists ${f}, but there is no such file`)
    failed = true
    continue
  }
  let course
  try {
    course = JSON.parse(readFileSync(new URL(f, dir), 'utf8'))
  } catch (err) {
    console.error(`✗ ${f} is not valid JSON: ${err.message}`)
    failed = true
    continue
  }
  const errors = validateCourse(course)
  if (errors.length) {
    failed = true
    console.error(`✗ ${f}`)
    for (const e of errors) console.error(`    ${e}`)
  } else {
    const tasks = course.sections.reduce((n, s) => n + (s.tasks || []).length, 0)
    console.log(`✓ ${f}: "${course.title}" v${course.version}, ${course.sections.length} sections, ${tasks} tasks`)
  }
}
process.exit(failed ? 1 : 0)
