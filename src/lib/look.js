// Presentation helpers: each course's colour, and how titles are split for
// display. Pure functions, no React, no browser APIs.

// Every course gets one bright colour ("tone") that it keeps on every screen.
// The courses that ship with the app have fixed tones; any other course gets
// a stable tone from its id, so it never changes colour between visits.
export const TONES = ['raspberry', 'indigo', 'teal', 'orange', 'blue', 'purple', 'green']

const FIXED_TONES = {
  'social-media-marketing': 'raspberry',
  'ai-generalist': 'indigo',
  entrepreneurship: 'teal',
}

export function toneFor(courseId) {
  const id = String(courseId || '')
  if (FIXED_TONES[id]) return FIXED_TONES[id]
  let h = 0
  for (const ch of id) h = (h * 31 + ch.codePointAt(0)) >>> 0
  return TONES[h % TONES.length]
}

// "Practical Entrepreneurship: From Idea to First Revenue"
//   -> { main: 'Practical Entrepreneurship', sub: 'From Idea to First Revenue' }
export function splitCourseTitle(title) {
  const text = String(title || '')
  const i = text.indexOf(': ')
  if (i <= 0) return { main: text, sub: null }
  return { main: text.slice(0, i), sub: text.slice(i + 2) }
}

// "SMM-M01-L01: How social platforms work" -> { label: 'SMM-M01-L01', text: 'How social platforms work' }
// "Module 1: Foundations" -> { label: 'Module 1', text: 'Foundations' }
// Only a short lead-in (up to 3 words, 20 characters) becomes a label, so
// ordinary titles that happen to contain a colon stay whole.
export function splitSectionTitle(title) {
  const text = String(title || '')
  const i = text.indexOf(': ')
  if (i <= 0) return { label: null, text }
  const label = text.slice(0, i)
  const rest = text.slice(i + 2)
  if (label.length > 20 || label.split(/\s+/).length > 3 || !rest) return { label: null, text }
  return { label, text: rest.charAt(0).toUpperCase() + rest.slice(1) }
}

// The first sentence of a summary, for short previews.
export function firstSentence(text) {
  const t = String(text || '').trim()
  const m = /^(.+?[.!?])(\s|$)/.exec(t)
  return m ? m[1] : t
}

// Shortens text to at most `max` characters at a word break, adding "…".
export function clip(text, max) {
  const t = String(text || '').trim()
  if (t.length <= max) return t
  const cut = t.slice(0, max + 1)
  const space = cut.lastIndexOf(' ')
  return `${(space > max * 0.6 ? cut.slice(0, space) : t.slice(0, max)).replace(/[\s,;:.]+$/, '')}…`
}

export function capitalise(text) {
  const t = String(text || '')
  return t.charAt(0).toUpperCase() + t.slice(1)
}
