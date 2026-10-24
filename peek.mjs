import { readFileSync } from 'node:fs'
const { renderMarkdown } = await import('/home/claude/vidhyarambham/src/lib/markdown.js')
const [file, id, from, len] = process.argv.slice(2)
const c = JSON.parse(readFileSync(file, 'utf8'))
const s = c.sections.find((x) => x.id === id)
const html = renderMarkdown(s.content)
const i = html.indexOf(from)
console.log(html.slice(Math.max(0, i), i + Number(len || 1500)))
