import { buildRoadmap } from '../lib/roadmap.js'
import { hrefFor } from '../lib/routes.js'
import { weeksLabel } from './Bits.jsx'

export default function Roadmap({ course, settings, done }) {
  const { rows, track } = buildRoadmap(course, done)
  if (rows.length === 0) return null
  const title = settings.title || 'Course roadmap'
  const first = rows.findIndex((r) => r.inTrack)
  const last = rows.length - 1 - [...rows].reverse().findIndex((r) => r.inTrack)
  const hasTrack = Boolean(track) && first !== -1

  return (
    <figure className="roadmap" aria-labelledby="roadmap-title">
      <h2 id="roadmap-title" className="roadmap-title">
        {title}
      </h2>
      {settings.note && <p className="roadmap-note">{settings.note}</p>}

      <ol className={hasTrack ? 'roadmap-grid with-track' : 'roadmap-grid'}>
        {rows.map((row, i) => {
          const meta = [weeksLabel(row.weeks), row.hours ? `about ${row.hours} hours` : null].filter(Boolean).join(', ')
          const complete = row.total > 0 && row.done === row.total
          const inBand = hasTrack && i >= first && i <= last
          return (
            <li key={row.id} className="roadmap-row">
              <a
                className={`roadmap-step kind-${row.kind}${complete ? ' complete' : ''}`}
                href={hrefFor({ name: 'section', courseId: course.id, sectionId: row.id })}
              >
                <span className="roadmap-step-title">{row.title}</span>
                {meta && <span className="roadmap-step-meta">{meta}</span>}
                {complete && <span className="roadmap-step-done">Done</span>}
              </a>
              {hasTrack && (
                <div className={`roadmap-track${inBand ? ' in-band' : ''}${i === first ? ' band-start' : ''}${i === last ? ' band-end' : ''}`}>
                  {i === first && (
                    <a className="roadmap-track-head" href={hrefFor({ name: 'section', courseId: course.id, sectionId: track.id })}>
                      <span className="roadmap-track-title">{track.title}</span>
                      {settings.trackNote && <span className="roadmap-track-note">{settings.trackNote}</span>}
                    </a>
                  )}
                  {row.trackItems.map((item) => (
                    <span key={item.id} className={item.done ? 'roadmap-track-item done' : 'roadmap-track-item'}>
                      {item.text}
                    </span>
                  ))}
                </div>
              )}
            </li>
          )
        })}
      </ol>

      {settings.caption && <figcaption className="roadmap-caption">{settings.caption}</figcaption>}
    </figure>
  )
}
