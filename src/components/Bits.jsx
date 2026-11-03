import { useEffect, useRef } from 'react'
import { renderMarkdown } from '../lib/markdown.js'
import { hrefFor } from '../lib/routes.js'
import { splitSectionTitle } from '../lib/look.js'

// The lamp flame lit at Vidyarambham. Same drawing as the app icon.
export function Flame({ size = 28 }) {
  return (
    <svg className="flame" width={size} height={size} viewBox="0 0 64 64" aria-hidden="true">
      <path d="M32 6c7 10 16 18 16 30a16 16 0 0 1-32 0C16 24 25 16 32 6z" fill="var(--flame)" />
      <path d="M32 26c3.5 5 7 8.5 7 13a7 7 0 0 1-14 0c0-4.5 3.5-8 7-13z" fill="var(--flame-core)" />
    </svg>
  )
}

function clampPercent(percent) {
  return Math.max(0, Math.min(100, Math.round(percent || 0)))
}

// A straight progress bar in the course's colour.
export function ProgressBar({ percent, label }) {
  const p = clampPercent(percent)
  return (
    <div className="bar" role="progressbar" aria-valuemin={0} aria-valuemax={100} aria-valuenow={p} aria-label={label}>
      <div className="bar-fill" style={{ width: `${p}%` }} />
    </div>
  )
}

// A progress ring. With `decorative`, screen readers skip it because the
// same number is written out next to it.
export function ProgressRing({ percent, size = 64, stroke = 7, label, showText = true, decorative = false }) {
  const p = clampPercent(percent)
  const r = (size - stroke) / 2
  const c = 2 * Math.PI * r
  const centre = size / 2
  const a11y = decorative
    ? { 'aria-hidden': true }
    : { role: 'progressbar', 'aria-valuemin': 0, 'aria-valuemax': 100, 'aria-valuenow': p, 'aria-label': label }
  return (
    <span className="ring" style={{ width: size, height: size }} {...a11y}>
      <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`} aria-hidden="true">
        <circle className="ring-track" cx={centre} cy={centre} r={r} strokeWidth={stroke} fill="none" />
        {p > 0 && (
          <circle
            className="ring-fill"
            cx={centre}
            cy={centre}
            r={r}
            strokeWidth={stroke}
            fill="none"
            strokeLinecap="round"
            strokeDasharray={`${(p / 100) * c} ${c}`}
            transform={`rotate(-90 ${centre} ${centre})`}
          />
        )}
      </svg>
      {showText && <span className="ring-text">{p}%</span>}
    </span>
  )
}

// A section title with its short lead-in ("SMM-M01-L01", "Module 1") shown
// as a small label. Screen readers still hear the whole title.
export function SectionTitle({ title, className }) {
  const { label, text } = splitSectionTitle(title)
  return (
    <span className={className}>
      {label && (
        <span className="title-label">
          {label}
          <span className="visually-hidden">: </span>
        </span>
      )}
      <span className="title-text">{text}</span>
    </span>
  )
}

async function copyText(text) {
  try {
    await navigator.clipboard.writeText(text)
    return true
  } catch {
    // Older browsers: copy through a hidden text box.
  }
  try {
    const box = document.createElement('textarea')
    box.value = text
    box.setAttribute('readonly', '')
    box.style.position = 'fixed'
    box.style.opacity = '0'
    document.body.appendChild(box)
    box.select()
    const ok = document.execCommand('copy')
    box.remove()
    return ok
  } catch {
    return false
  }
}

// Course text. Every template (code block) gets a Copy button.
export function Markdown({ source, className = 'prose' }) {
  const ref = useRef(null)
  const html = source ? renderMarkdown(source) : ''

  useEffect(() => {
    const root = ref.current
    if (!root) return undefined
    for (const pre of root.querySelectorAll('pre')) {
      if (pre.querySelector('button.copy')) continue
      const button = document.createElement('button')
      button.type = 'button'
      button.className = 'copy'
      button.textContent = 'Copy'
      pre.prepend(button)
    }
    const timers = []
    const onClick = async (event) => {
      const button = event.target.closest('button.copy')
      if (!button || !root.contains(button)) return
      const code = button.parentElement.querySelector('code')
      const ok = await copyText(code ? code.textContent : '')
      button.textContent = ok ? 'Copied' : "Couldn't copy"
      button.classList.toggle('copied', ok)
      timers.push(
        setTimeout(() => {
          button.textContent = 'Copy'
          button.classList.remove('copied')
        }, 2000),
      )
    }
    root.addEventListener('click', onClick)
    return () => {
      root.removeEventListener('click', onClick)
      timers.forEach(clearTimeout)
    }
  }, [html])

  if (!source) return null
  return <div ref={ref} className={className} dangerouslySetInnerHTML={{ __html: html }} />
}

// The bar at the top of inner pages, with the way back.
export function BackLink({ to, children }) {
  return (
    <nav className="topbar" aria-label="Back">
      <a className="topbar-back" href={hrefFor(to)}>
        <svg width="20" height="20" viewBox="0 0 20 20" aria-hidden="true">
          <path d="M12.5 4 6.5 10l6 6" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round" />
        </svg>
        <span className="topbar-text">{children}</span>
      </a>
    </nav>
  )
}

// Small pictures for each kind of section in the course plan.
const KIND_PATHS = {
  intro: 'M5 17V3.5M5 4h9.5l-2.2 3 2.2 3H5',
  setup: 'M3.5 6.5h13M3.5 13.5h13M7.5 4.5v4M12.5 11.5v4',
  level: 'M10 6c-2-1.6-4.5-1.9-6.5-1.2v10.5c2-.7 4.5-.4 6.5 1.2 2-1.6 4.5-1.9 6.5-1.2V4.8C14.5 4.1 12 4.4 10 6zM10 6v10.5',
  gate: 'M10 2.8 17.2 10 10 17.2 2.8 10z',
  track: 'M3.5 15.5c3.5 0 3.5-5.5 6.5-5.5s3-5.5 6.5-5.5',
  capstone: 'M10 2.9l2.1 4.4 4.8.6-3.5 3.3.9 4.8L10 13.7 5.7 16l.9-4.8-3.5-3.3 4.8-.6z',
  reference: 'M6 3.2h8v13.6l-4-3-4 3z',
}

export function KindIcon({ kind }) {
  const d = KIND_PATHS[kind] || KIND_PATHS.level
  return (
    <svg width="20" height="20" viewBox="0 0 20 20" aria-hidden="true">
      <path d={d} fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  )
}

export function weeksLabel(weeks) {
  if (!weeks) return null
  const [a, b] = weeks
  return a === b ? `Week ${a}` : `Weeks ${a}–${b}`
}

export function hoursLabel(hours) {
  if (!hours) return null
  return `about ${hours} ${hours === 1 ? 'hour' : 'hours'}`
}

export function shortDate(date) {
  return date.toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' })
}

export const KIND_LABEL = { project: 'Project', exit: 'Exit test', task: null }
