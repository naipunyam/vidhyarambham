import { courseProgress } from '../lib/progress.js'
import { getProgress } from '../lib/state.js'
import { hrefFor } from '../lib/routes.js'
import { Flame, ProgressBar } from './Bits.jsx'

export default function Library({ entries, state, loading, problems, offline }) {
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

      {entries.length > 0 && (
        <ul className="course-list">
          {entries.map(({ course, source }) => {
            const p = courseProgress(course, getProgress(state, course.id).done)
            return (
              <li key={course.id}>
                <a className="course-row" href={hrefFor({ name: 'course', courseId: course.id })}>
                  <span className="course-row-title">{course.title}</span>
                  {course.summary && <span className="course-row-summary">{course.summary}</span>}
                  <ProgressBar percent={p.percent} label={`${course.title} progress`} />
                  <span className="course-row-meta">
                    {p.done} of {p.total} tasks done{source === 'imported' ? ', added from a file' : ''}
                  </span>
                </a>
              </li>
            )
          })}
        </ul>
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
