import { courseProgress } from '../lib/progress.js'
import { getProgress } from '../lib/state.js'
import { hrefFor } from '../lib/routes.js'
import { pickContinue } from '../lib/continue.js'
import { toneFor, splitCourseTitle, firstSentence, clip } from '../lib/look.js'
import { Flame, ProgressRing } from './Bits.jsx'

function openTasksText(open) {
  if (open === 0) return 'nothing left this week'
  return `${open} ${open === 1 ? 'task' : 'tasks'} left this week`
}

export default function Library({ entries, state, loading, problems, offline }) {
  const next = pickContinue(entries, state)

  return (
    <>
      <header className="masthead">
        <Flame size={40} />
        <div>
          <h1 className="wordmark">Vidhyarambham</h1>
          <p className="tagline">Your courses and how far you've come</p>
        </div>
      </header>

      {loading && entries.length === 0 && <p className="loading">Loading your courses…</p>}

      {offline && (
        <p className="notice">
          You're offline and the course list couldn't load. Courses you added from a file are still here.
        </p>
      )}

      {next && (
        <section className="continue" aria-labelledby="continue-h">
          <div className="continue-text">
            <h2 id="continue-h" className="continue-kicker">
              Continue where you left off
            </h2>
            <p className="continue-title">{splitCourseTitle(next.course.title).main}</p>
            <p className="continue-meta">
              Week {next.week}
              {next.lastWeek ? ` of ${next.lastWeek}` : ''}, {openTasksText(next.open)}
            </p>
          </div>
          <a className="button sun" href={hrefFor({ name: 'course', courseId: next.course.id })}>
            Continue
          </a>
        </section>
      )}

      {entries.length > 0 && (
        <section aria-labelledby="courses-h">
          <h2 id="courses-h" className="list-title">
            Your courses
          </h2>
          <ul className="course-list">
            {entries.map(({ course, source }) => {
              const p = courseProgress(course, getProgress(state, course.id).done)
              const { main, sub } = splitCourseTitle(course.title)
              return (
                <li key={course.id}>
                  <a className={`course-card tone-${toneFor(course.id)}`} href={hrefFor({ name: 'course', courseId: course.id })}>
                    <ProgressRing percent={p.percent} size={64} stroke={7} decorative />
                    <span className="course-card-title">{main}</span>
                    {sub && <span className="course-card-sub">{sub}</span>}
                    {course.summary && <span className="course-card-summary">{clip(firstSentence(course.summary), 110)}</span>}
                    <span className="course-card-count">
                      {p.done} of {p.total} tasks done{source === 'imported' ? ', added from a file' : ''}
                    </span>
                  </a>
                </li>
              )
            })}
          </ul>
        </section>
      )}

      {!loading && entries.length === 0 && (
        <p className="empty">No courses yet. Add a course file to start.</p>
      )}

      <div className="actions">
        <a className="button primary" href={hrefFor({ name: 'add' })}>
          Add a course
        </a>
        <a className="button" href={hrefFor({ name: 'backup' })}>
          Backup and courses
        </a>
      </div>

      {problems && problems.length > 0 && !offline && (
        <details className="problems">
          <summary>Some course files could not be loaded</summary>
          <ul>
            {problems.map((p) => (
              <li key={p}>{p}</li>
            ))}
          </ul>
        </details>
      )}
    </>
  )
}
