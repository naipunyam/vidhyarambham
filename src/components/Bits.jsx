import { renderMarkdown } from '../lib/markdown.js'
import { hrefFor } from '../lib/routes.js'

// The lamp flame lit at Vidyarambham. Same drawing as the app icon.
export function Flame({ size = 28 }) {
  return (
    <svg className="flame" width={size} height={size} viewBox="0 0 64 64" aria-hidden="true">
      <path d="M32 6c7 10 16 18 16 30a16 16 0 0 1-32 0C16 24 25 16 32 6z" fill="var(--brass)" />
      <path d="M32 26c3.5 5 7 8.5 7 13a7 7 0 0 1-14 0c0-4.5 3.5-8 7-13z" fill="var(--flame-core)" />
    </svg>
  )
}

// Progress drawn like a kasavu border: a gold band between two fine gold lines.
export function ProgressBar({ percent, label }) {
  const p = Math.max(0, Math.min(100, percent || 0))
  return (
    <div className="kasavu" role="progressbar" aria-valuemin={0} aria-valuemax={100} aria-valuenow={p} aria-label={label}>
      <div className="kasavu-fill" style={{ width: `${p}%` }} />
    </div>
  )
}

export function Markdown({ source, className = 'prose' }) {
  if (!source) return null
  return <div className={className} dangerouslySetInnerHTML={{ __html: renderMarkdown(source) }} />
}

export function BackLink({ to, children }) {
  return (
    <a className="back" href={hrefFor(to)}>
      <svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true">
        <path d="M10 3 5 8l5 5" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" />
      </svg>
      {children}
    </a>
  )
}

export function weeksLabel(weeks) {
  if (!weeks) return null
  const [a, b] = weeks
  return a === b ? `Week ${a}` : `Weeks ${a}–${b}`
}

export function shortDate(date) {
  return date.toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' })
}

export const KIND_LABEL = { project: 'Project', exit: 'Exit test', task: null }
