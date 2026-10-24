// A small, safe Markdown renderer for course content.
// Every piece of text is HTML-escaped before tags are added, and links must be
// http, https or mailto, so a course file from anywhere cannot inject scripts.
//
// Supports: paragraphs, headings, **bold**, *italic*, `code`, [links](https://...),
// bullet and numbered lists (nested with 2+ spaces), tables, fenced code blocks
// and > quotes.

export function escapeHtml(text) {
  return String(text)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;')
}

const SAFE_URL = /^(https?:\/\/|mailto:)/i

export function renderInline(text) {
  const slots = []
  const hold = (html) => `\u0000${slots.push(html) - 1}\u0000`
  let s = String(text)

  // Code spans first, so nothing inside them is formatted.
  s = s.replace(/`([^`]+)`/g, (_, code) => hold(`<code>${escapeHtml(code)}</code>`))

  // Links. The link text can itself contain bold or italic.
  s = s.replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, (_, label, url) => {
    const inner = formatEmphasis(escapeHtml(label))
    if (!SAFE_URL.test(url)) return hold(inner)
    return hold(`<a href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer">${inner}</a>`)
  })

  s = formatEmphasis(escapeHtml(s))
  return s.replace(/\u0000(\d+)\u0000/g, (_, i) => slots[Number(i)])
}

function formatEmphasis(escaped) {
  return escaped
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/(^|[^*\w])\*(?!\s)([^*]+?)\*(?![*\w])/g, '$1<em>$2</em>')
}

const FENCE = /^```/
const HEADING = /^(#{1,6})\s+(.*)$/
const LIST_ITEM = /^(\s*)([-*+]|\d+[.)])\s+(.*)$/
const TABLE_SEPARATOR = /^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$/
const QUOTE = /^>\s?(.*)$/

function startsBlock(line, next) {
  return (
    FENCE.test(line) ||
    HEADING.test(line) ||
    LIST_ITEM.test(line) ||
    QUOTE.test(line) ||
    (line.trim().startsWith('|') && next !== undefined && TABLE_SEPARATOR.test(next))
  )
}

export function renderMarkdown(source) {
  if (!source) return ''
  const lines = String(source).replace(/\r\n?/g, '\n').split('\n')
  const out = []
  let i = 0

  while (i < lines.length) {
    const line = lines[i]

    if (line.trim() === '') {
      i++
      continue
    }

    if (FENCE.test(line)) {
      const code = []
      i++
      while (i < lines.length && !FENCE.test(lines[i])) code.push(lines[i++])
      i++ // closing fence
      out.push(`<pre><code>${escapeHtml(code.join('\n'))}</code></pre>`)
      continue
    }

    const heading = HEADING.exec(line)
    if (heading) {
      // Course headings sit under the page title, so # becomes h3.
      const level = Math.min(6, heading[1].length + 2)
      out.push(`<h${level}>${renderInline(heading[2])}</h${level}>`)
      i++
      continue
    }

    if (line.trim().startsWith('|') && i + 1 < lines.length && TABLE_SEPARATOR.test(lines[i + 1])) {
      const rows = [line]
      i += 2
      while (i < lines.length && lines[i].trim().startsWith('|')) rows.push(lines[i++])
      out.push(renderTable(rows))
      continue
    }

    if (LIST_ITEM.test(line)) {
      const block = []
      while (i < lines.length) {
        const l = lines[i]
        if (l.trim() === '') {
          // A blank line ends the list unless the next line continues it.
          const next = lines[i + 1]
          if (next !== undefined && (LIST_ITEM.test(next) || /^\s{2,}\S/.test(next))) {
            i++
            continue
          }
          break
        }
        if (!LIST_ITEM.test(l) && !/^\s{2,}\S/.test(l) && block.length && startsBlock(l, lines[i + 1])) break
        if (!LIST_ITEM.test(l) && !/^\s/.test(l)) break
        block.push(l)
        i++
      }
      out.push(renderList(block))
      continue
    }

    if (QUOTE.test(line)) {
      const quoted = []
      while (i < lines.length && QUOTE.test(lines[i])) quoted.push(QUOTE.exec(lines[i++])[1])
      out.push(`<blockquote>${renderMarkdown(quoted.join('\n'))}</blockquote>`)
      continue
    }

    const para = [line.trim()]
    i++
    while (i < lines.length && lines[i].trim() !== '' && !startsBlock(lines[i], lines[i + 1])) {
      para.push(lines[i].trim())
      i++
    }
    out.push(`<p>${renderInline(para.join(' '))}</p>`)
  }

  return out.join('\n')
}

function splitRow(row) {
  let r = row.trim()
  if (r.startsWith('|')) r = r.slice(1)
  if (r.endsWith('|')) r = r.slice(0, -1)
  return r.split('|').map((c) => c.trim())
}

function renderTable(rows) {
  const [head, ...body] = rows.map(splitRow)
  const th = head.map((c) => `<th scope="col">${renderInline(c)}</th>`).join('')
  const trs = body
    .map((cells) => `<tr>${head.map((_, k) => `<td>${renderInline(cells[k] || '')}</td>`).join('')}</tr>`)
    .join('')
  return `<div class="table-wrap"><table><thead><tr>${th}</tr></thead><tbody>${trs}</tbody></table></div>`
}

function indentOf(line) {
  return line.match(/^\s*/)[0].replace(/\t/g, '    ').length
}

function renderList(lines) {
  const first = LIST_ITEM.exec(lines[0])
  const base = indentOf(lines[0])
  const ordered = /\d/.test(first[2])
  const items = []
  for (const line of lines) {
    const m = LIST_ITEM.exec(line)
    if (m && indentOf(line) <= base) {
      items.push({ text: m[3], children: [] })
    } else if (items.length) {
      items[items.length - 1].children.push(line)
    }
  }
  const lis = items
    .map((item) => {
      let html = renderInline(item.text)
      const child = item.children.filter((l) => l.trim() !== '')
      if (child.length) {
        const nested = LIST_ITEM.test(child[0]) ? renderList(child) : `<p>${renderInline(child.map((l) => l.trim()).join(' '))}</p>`
        html += nested
      }
      return `<li>${html}</li>`
    })
    .join('')
  const start = ordered ? parseInt(first[2], 10) : 1
  if (ordered) return `<ol${start !== 1 ? ` start="${start}"` : ''}>${lis}</ol>`
  return `<ul>${lis}</ul>`
}
