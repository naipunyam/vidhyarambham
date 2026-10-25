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
let words = 0
const lessonWords = []
for (const s of course.sections) {
  check(`${s.id}.summary`, s.summary)
  check(`${s.id}.content`, s.content)
  for (const t of s.tasks || []) check(`${s.id}.${t.id}.detail`, t.detail)
  const w = (s.content || '').split(/\s+/).length
  words += w
  if (/^smm-m\d\d-l\d\d$/.test(s.id)) lessonWords.push([s.id, w])
}
console.log(problems.length ? `PROBLEMS (${problems.length}):\n${problems.slice(0, 40).join('\n')}` : 'markdown ok')
console.log(`words: ${words}; lessons: ${lessonWords.length}; lesson words min ${Math.min(...lessonWords.map((x) => x[1]))} max ${Math.max(...lessonWords.map((x) => x[1]))}`)
const short = lessonWords.filter((x) => x[1] < 1400).map((x) => `${x[0]}:${x[1]}`)
if (short.length) console.log('short lessons:', short.join(' '))

// Weekly load at part-time pace: section hours spread evenly over their weeks.
const load = {}
for (const s of course.sections) {
  if (!s.weeks || !s.hours || /^smm-m\d\d$/.test(s.id)) continue
  const [a, b] = s.weeks
  for (let w = a; w <= b; w++) load[w] = (load[w] || 0) + s.hours / (b - a + 1)
}
// Module project hours (overview hours minus its lessons) land in the module project's week.
for (const s of course.sections) {
  const m = /^smm-m(\d\d)$/.exec(s.id)
  if (!m) continue
  const lessonHours = course.sections.filter((x) => x.id.startsWith(`${s.id}-l`)).reduce((n, x) => n + x.hours, 0)
  const wk = s.tasks.find((t) => t.id.endsWith('-project')).week
  load[wk] = (load[wk] || 0) + (s.hours - lessonHours)
}
console.log('hours by week:', Object.entries(load).map(([w, h]) => `${w}:${h.toFixed(1)}`).join(' '))
const total = Object.values(load).reduce((a, b) => a + b, 0)
console.log(`total hours: ${total.toFixed(0)}`)
const counts = []
for (let w = 0; w <= (course.totalWeeks || 0); w++) counts.push(`${w}:${tasksForWeek(course, { done: {} }, w).length}`)
console.log('open tasks shown per week:', counts.join(' '))
