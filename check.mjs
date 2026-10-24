// Validate the course with the app's own code and render every piece of
// Markdown, flagging anything that looks broken.
// Usage: node check.mjs /path/to/course.json /path/to/repo
import { readFileSync } from 'node:fs'
import { pathToFileURL } from 'node:url'

const [file, repo] = process.argv.slice(2)
const { validateCourse } = await import(pathToFileURL(`${repo}/src/lib/courseFormat.js`).href)
const { renderMarkdown } = await import(pathToFileURL(`${repo}/src/lib/markdown.js`).href)
const { tasksForWeek } = await import(pathToFileURL(`${repo}/src/lib/progress.js`).href)

const course = JSON.parse(readFileSync(file, 'utf8'))
const errors = validateCourse(course)
console.log(errors.length ? `INVALID:\n${errors.join('\n')}` : 'valid')

const problems = []
const check = (where, md) => {
  if (!md) return
  const html = renderMarkdown(md)
  const text = html.replace(/<[^>]+>/g, '')
  if (/\*\*/.test(text)) problems.push(`${where}: unrendered ** in "${text.match(/.{0,40}\*\*.{0,40}/)[0]}"`)
  if (/\]\(/.test(text)) problems.push(`${where}: broken link near "${text.match(/.{0,40}\]\(.{0,40}/)[0]}"`)
  if (/^\s*\|/m.test(text) && !/<table>/.test(html)) problems.push(`${where}: table did not render`)
  if (/undefined|NaN|\[object Object\]/.test(text)) problems.push(`${where}: undefined/NaN`)
  const links = [...md.matchAll(/\]\(([^)\s]+)\)/g)].map((m) => m[1])
  for (const l of links) if (!/^https?:\/\//.test(l)) problems.push(`${where}: non-http link ${l}`)
}
for (const s of course.sections) {
  check(`${s.id}.summary`, s.summary)
  check(`${s.id}.content`, s.content)
  for (const t of s.tasks || []) check(`${s.id}.${t.id}.detail`, t.detail)
}
console.log(problems.length ? `PROBLEMS (${problems.length}):\n${problems.slice(0, 40).join('\n')}` : 'markdown ok')

// Weekly load at part-time pace: section hours spread evenly over their weeks.
const load = {}
for (const s of course.sections) {
  if (!s.weeks || !s.hours || /^ent-m\d\d$/.test(s.id) || s.id === 'ent-final') continue
  const [a, b] = s.weeks
  for (let w = a; w <= b; w++) load[w] = (load[w] || 0) + s.hours / (b - a + 1)
}
// Module project hours (overview hours minus its lessons) land in the module's last week.
for (const s of course.sections) {
  const m = /^ent-m(\d\d)$/.exec(s.id)
  if (!m) continue
  const lessonHours = course.sections.filter((x) => x.id.startsWith(`${s.id}-l`)).reduce((n, x) => n + x.hours, 0)
  load[s.weeks[1]] = (load[s.weeks[1]] || 0) + (s.hours - lessonHours)
}
console.log('hours by week:', Object.entries(load).map(([w, h]) => `${w}:${h.toFixed(1)}`).join(' '))
const counts = []
for (let w = 0; w <= (course.totalWeeks || 0); w++) counts.push(`${w}:${tasksForWeek(course, { done: {} }, w).length}`)
console.log('open tasks shown per week:', counts.join(' '))
