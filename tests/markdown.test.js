import { test } from 'node:test'
import assert from 'node:assert/strict'
import { renderMarkdown, renderInline } from '../src/lib/markdown.js'

test('escapes HTML so course files cannot inject markup', () => {
  const html = renderMarkdown('<script>alert(1)</script> and <img src=x onerror=alert(1)>')
  assert.ok(!html.includes('<script'))
  assert.ok(!html.includes('<img'))
  assert.match(html, /&lt;script&gt;/)
})

test('only http, https and mailto links become links', () => {
  assert.match(renderInline('[ok](https://example.com)'), /<a href="https:\/\/example.com" target="_blank" rel="noopener noreferrer">ok<\/a>/)
  const bad = renderInline('[bad](javascript:alert(1))')
  assert.ok(!bad.includes('<a'))
  assert.ok(!bad.includes('href'))
})

test('a link url cannot break out of the href attribute', () => {
  const html = renderInline('[x](https://a.com/"onmouseover="alert(1))')
  assert.ok(!html.includes('"onmouseover'))
})

test('bold, italic and code', () => {
  assert.equal(renderInline('**Build, don\'t binge.** Spend'), '<strong>Build, don&#39;t binge.</strong> Spend')
  assert.equal(renderInline('an *italic* word'), 'an <em>italic</em> word')
  assert.equal(renderInline('use `a < b`'), 'use <code>a &lt; b</code>')
  assert.equal(renderInline('2 * 3 * 4'), '2 * 3 * 4')
})

test('bold inside link text', () => {
  assert.equal(renderInline('[**Bold** link](https://x.io)'), '<a href="https://x.io" target="_blank" rel="noopener noreferrer"><strong>Bold</strong> link</a>')
})

test('tables', () => {
  const html = renderMarkdown('| A | B |\n| --- | --- |\n| 1 | [x](https://x.io) |\n| 2 |  |')
  assert.match(html, /<table><thead><tr><th scope="col">A<\/th><th scope="col">B<\/th><\/tr><\/thead>/)
  assert.match(html, /<td>1<\/td><td><a href="https:\/\/x.io"/)
  assert.match(html, /<tr><td>2<\/td><td><\/td><\/tr>/)
})

test('lists, numbered lists and nesting', () => {
  assert.equal(renderMarkdown('- a\n- b'), '<ul><li>a</li><li>b</li></ul>')
  assert.equal(renderMarkdown('1. a\n2. b'), '<ol><li>a</li><li>b</li></ol>')
  assert.equal(renderMarkdown('1. a\n    - x\n2. b'), '<ol><li>a<ul><li>x</li></ul></li><li>b</li></ol>')
})

test('paragraph then list without a blank line, and list then paragraph', () => {
  const html = renderMarkdown('**You learn:**\n- one\n- two\n\nAfter.')
  assert.equal(html, '<p><strong>You learn:</strong></p>\n<ul><li>one</li><li>two</li></ul>\n<p>After.</p>')
})

test('fenced code is escaped and kept as written', () => {
  const html = renderMarkdown('```\nYou are my tutor.\n1. Ask <me>\n```')
  assert.equal(html, '<pre><code>You are my tutor.\n1. Ask &lt;me&gt;</code></pre>')
})

test('headings start at h3', () => {
  assert.equal(renderMarkdown('# Title'), '<h3>Title</h3>')
  assert.equal(renderMarkdown('### Small'), '<h5>Small</h5>')
})

test('the shipped course renders without leftover Markdown markers', async () => {
  const { readFileSync } = await import('node:fs')
  const course = JSON.parse(readFileSync(new URL('../public/courses/ai-generalist.json', import.meta.url), 'utf8'))
  for (const s of course.sections) {
    for (const text of [s.summary, s.content, ...(s.tasks || []).map((t) => t.detail)]) {
      if (!text) continue
      const html = renderMarkdown(text)
      const plain = html.replace(/<pre>[\s\S]*?<\/pre>/g, '').replace(/<[^>]+>/g, '')
      assert.ok(!plain.includes('**'), `stray ** in ${s.id}: ${plain.slice(plain.indexOf('**') - 40, plain.indexOf('**') + 40)}`)
      assert.ok(!/\]\(http/.test(plain), `unrendered link in ${s.id}`)
      assert.ok(!/^\|/m.test(plain), `unrendered table in ${s.id}`)
    }
  }
})
