import { courseProgress, currentWeek, tasksForWeek, weekStartDate, pickPace, toLocalDateString, toggleTask } from '../lib/progress.js'
import { hrefFor } from '../lib/routes.js'
import { BackLink, ProgressBar, weeksLabel, shortDate } from './Bits.jsx'
import TaskItem from './TaskItem.jsx'

export default function CoursePage({ entry, progress, onChange }) {
  const { course, source } = entry
  const total = courseProgress(course, progress.done)
  const now = currentWeek(course, progress)
  const pace = pickPace(course, progress.pace)
  const weekTasks = now.status === 'running' ? tasksForWeek(course, progress, now.week) : []

  const setPace = (id) => onChange((p) => ({ ...p, pace: id }))
  const setStart = (value) => onChange((p) => ({ ...p, startDate: value || null }))
  const toggle = (taskId) => onChange((p) => toggleTask(p, taskId))

  return (
    <>
      <BackLink to={{ name: 'library' }}>All courses</BackLink>

      <header className="course-head">
        <h1 className="page-title">{course.title}</h1>
        {course.summary && <p className="lede">{course.summary}</p>}
        <div className="score">
          <span className="score-number">{total.percent}%</span>
          <span className="score-label">
            {total.done} of {total.total} tasks done
          </span>
        </div>
        <ProgressBar percent={total.percent} label="Course progress" />
      </header>

      <section className="panel" aria-labelledby="schedule-h">
        <h2 id="schedule-h">Your schedule</h2>
        {course.paces && course.paces.length > 1 && (
          <fieldset className="pace-choice">
            <legend>Pace</legend>
            {course.paces.map((p) => (
              <label key={p.id} className={p.id === pace.id ? 'chip on' : 'chip'}>
                <input type="radio" name="pace" value={p.id} checked={p.id === pace.id} onChange={() => setPace(p.id)} />
                <span>
                  {p.label}
                  {p.hoursPerWeek ? `, about ${p.hoursPerWeek} hours a week` : ''}
                </span>
              </label>
            ))}
          </fieldset>
        )}
        {pace.note && <p className="hint">{pace.note}</p>}
        <label className="field">
          <span>Start date</span>
          <input
            type="date"
            value={progress.startDate || ''}
            onChange={(e) => setStart(e.target.value)}
          />
        </label>
        {!progress.startDate && (
          <button type="button" className="button small" onClick={() => setStart(toLocalDateString(new Date()))}>
            Start today
          </button>
        )}
        <WeekLine course={course} progress={progress} now={now} />
      </section>

      {now.status === 'running' && (
        <section className="panel this-week" aria-labelledby="week-h">
          <h2 id="week-h">This week: Week {now.week}</h2>
          {weekTasks.length === 0 ? (
            <p className="hint">Nothing left for this week. Read ahead, or review your notes.</p>
          ) : (
            <ul className="tasks">
              {weekTasks.map((t) => (
                <TaskItem
                  key={t.id}
                  task={t}
                  done={Boolean(progress.done[t.id])}
                  onToggle={() => toggle(t.id)}
                  context={
                    <a href={hrefFor({ name: 'section', courseId: course.id, sectionId: t.sectionId })}>
                      {t.sectionTitle}
                    </a>
                  }
                  overdue={t.overdue}
                />
              ))}
            </ul>
          )}
        </section>
      )}

      <section aria-labelledby="sections-h">
        <h2 id="sections-h" className="list-title">
          Course plan
        </h2>
        <ol className="section-list">
          {course.sections.map((s) => {
            const p = total.bySection[s.id]
            const active = now.status === 'running' && s.weeks && s.weeks[0] <= now.week && now.week <= s.weeks[1]
            return (
              <li key={s.id} className={active ? 'active' : undefined}>
                <a className="section-row" href={hrefFor({ name: 'section', courseId: course.id, sectionId: s.id })}>
                  <span className="section-row-title">{s.title}</span>
                  <span className="section-row-meta">
                    {[weeksLabel(s.weeks), s.hours ? `about ${s.hours} hours` : null, active ? 'now' : null]
                      .filter(Boolean)
                      .join(', ')}
                  </span>
                  {p.total > 0 && (
                    <span className="section-row-count" aria-label={`${p.done} of ${p.total} done`}>
                      {p.done === p.total ? 'Done' : `${p.done}/${p.total}`}
                    </span>
                  )}
                </a>
              </li>
            )
          })}
        </ol>
      </section>

      <p className="footnote">
        Version {course.version}
        {course.updated ? `, updated ${course.updated}` : ''}
        {source === 'imported' ? ', added from a file on this device' : ''}.
      </p>
    </>
  )
}

function WeekLine({ course, progress, now }) {
  if (now.status === 'not-started') return <p className="hint">Set a start date to see which week you're in.</p>
  if (now.status === 'not-yet') {
    return (
      <p className="hint">
        You start in {now.daysToStart} {now.daysToStart === 1 ? 'day' : 'days'}.
      </p>
    )
  }
  if (now.status === 'finished') return <p className="hint">Your planned weeks are over. Finish any open tasks at your own speed.</p>
  const next = weekStartDate(course, progress, now.week + 1)
  return (
    <p className="hint">
      You're in Week {now.week}. Week {now.week + 1} starts {shortDate(next)}.
    </p>
  )
}

