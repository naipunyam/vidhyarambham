import { useState } from 'react'
import {
  courseProgress,
  currentWeek,
  lastWeekOf,
  tasksForWeek,
  weekStartDate,
  pickPace,
  toLocalDateString,
  toggleTask,
} from '../lib/progress.js'
import { hrefFor } from '../lib/routes.js'
import { splitCourseTitle, splitSectionTitle } from '../lib/look.js'
import { BackLink, KindIcon, ProgressRing, SectionTitle, weeksLabel, hoursLabel, shortDate } from './Bits.jsx'
import TaskItem from './TaskItem.jsx'

const LONG_SUMMARY = 180

export default function CoursePage({ entry, progress, onChange }) {
  const { course, source } = entry
  const total = courseProgress(course, progress.done)
  const now = currentWeek(course, progress)
  const pace = pickPace(course, progress.pace)
  const lastWeek = course.totalWeeks || lastWeekOf(course)
  const running = now.status === 'running'
  // Tasks ticked during this visit stay in the list (shown as done) until you
  // leave the page, so you can see the tick and undo a mistaken tap.
  const [tickedHere, setTickedHere] = useState([])
  const openDone = { ...progress.done }
  for (const id of tickedHere) delete openDone[id]
  const weekTasks = running ? tasksForWeek(course, { ...progress, done: openDone }, now.week) : []
  const openCount = weekTasks.filter((t) => !progress.done[t.id]).length
  const { main, sub } = splitCourseTitle(course.title)
  const [summaryOpen, setSummaryOpen] = useState(false)
  const longSummary = course.summary && course.summary.length > LONG_SUMMARY

  const setPace = (id) => onChange((p) => ({ ...p, pace: id }))
  const setStart = (value) => onChange((p) => ({ ...p, startDate: value || null }))
  const toggle = (taskId) => {
    if (!progress.done[taskId] && !tickedHere.includes(taskId)) setTickedHere([...tickedHere, taskId])
    onChange((p) => toggleTask(p, taskId))
  }

  const schedule = (
    <section className="panel" aria-labelledby="schedule-h">
      <h2 id="schedule-h">Your schedule</h2>
      {course.paces && course.paces.length > 1 && (
        <fieldset className="pace-choice">
          <legend>Pace</legend>
          {course.paces.map((p) => (
            <label key={p.id} className={p.id === pace.id ? 'pace on' : 'pace'}>
              <input type="radio" name="pace" value={p.id} checked={p.id === pace.id} onChange={() => setPace(p.id)} />
              <span className="pace-label">{p.label}</span>
              {p.hoursPerWeek ? <span className="pace-hours">About {p.hoursPerWeek} hours a week</span> : null}
            </label>
          ))}
        </fieldset>
      )}
      {pace.note && <p className="hint">{pace.note}</p>}
      <div className="start-row">
        <label className="field">
          <span>Start date</span>
          <input type="date" value={progress.startDate || ''} onChange={(e) => setStart(e.target.value)} />
        </label>
        {!progress.startDate && (
          <button type="button" className="button primary" onClick={() => setStart(toLocalDateString(new Date()))}>
            Start today
          </button>
        )}
      </div>
      <WeekLine course={course} progress={progress} now={now} />
    </section>
  )

  return (
    <>
      <BackLink to={{ name: 'library' }}>All courses</BackLink>

      <header className="hero">
        <div className="hero-top">
          <div className="hero-titles">
            <h1 className="hero-title">{main}</h1>
            {sub && <p className="hero-sub">{sub}</p>}
          </div>
          <ProgressRing percent={total.percent} size={78} stroke={8} label="Course progress" />
        </div>
        <p className="hero-count">
          {total.done} of {total.total} tasks done
        </p>
        <p className="hero-pills">
          {running && (
            <span className="pill">
              Week {now.week}
              {lastWeek ? ` of ${lastWeek}` : ''}
            </span>
          )}
          {now.status === 'not-yet' && <span className="pill">Starts in {now.daysToStart} {now.daysToStart === 1 ? 'day' : 'days'}</span>}
          {now.status === 'finished' && <span className="pill">Planned weeks over</span>}
          {course.paces && course.paces.length > 1 && <span className="pill">{pace.label}</span>}
        </p>
      </header>

      {course.summary && (
        <div className={`summary${longSummary && !summaryOpen ? ' clamped' : ''}`}>
          <p>{course.summary}</p>
          {longSummary && (
            <button type="button" className="link-button" aria-expanded={summaryOpen} onClick={() => setSummaryOpen(!summaryOpen)}>
              {summaryOpen ? 'Show less' : 'Read more'}
            </button>
          )}
        </div>
      )}

      {!running && schedule}

      {running && (
        <section className="panel this-week" aria-labelledby="week-h">
          <div className="panel-head">
            <h2 id="week-h">This week</h2>
            <span className="count">
              Week {now.week}, {openCount} open
            </span>
          </div>
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
                    <a href={hrefFor({ name: 'section', courseId: course.id, sectionId: t.sectionId })}>{t.sectionTitle}</a>
                  }
                  overdue={t.overdue}
                  foldDetail
                />
              ))}
            </ul>
          )}
        </section>
      )}

      {running && schedule}

      <section aria-labelledby="sections-h">
        <h2 id="sections-h" className="list-title">
          Course plan
        </h2>
        <ol className="plan">
          {course.sections.map((s) => {
            const p = total.bySection[s.id]
            const active = running && s.weeks && s.weeks[0] <= now.week && now.week <= s.weeks[1]
            const complete = p.total > 0 && p.done === p.total
            const { label } = splitSectionTitle(s.title)
            const group = label && /^(Module|Level|Part|Unit)\s/.test(label)
            const meta = [weeksLabel(s.weeks), hoursLabel(s.hours)].filter(Boolean).join(', ')
            return (
              <li key={s.id} className={active ? 'now' : undefined}>
                <a
                  className={`plan-row kind-${s.kind || 'level'}${group ? ' group' : ''}${complete ? ' complete' : ''}`}
                  href={hrefFor({ name: 'section', courseId: course.id, sectionId: s.id })}
                >
                  <span className="plan-icon">
                    <KindIcon kind={s.kind} />
                  </span>
                  <span className="plan-main">
                    <SectionTitle title={s.title} className="plan-title" />
                    {(meta || active) && (
                      <span className="plan-meta">
                        {active && <span className="pill now-pill">Now</span>}
                        {meta}
                      </span>
                    )}
                  </span>
                  {p.total > 0 && (
                    <span className="plan-status">
                      {complete ? (
                        <span className="done-badge" aria-label={`All ${p.total} done`}>
                          <svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true">
                            <path d="M3.5 8.5 6.5 11.5 12.5 4.5" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round" />
                          </svg>
                        </span>
                      ) : (
                        <ProgressRing percent={(p.done / p.total) * 100} size={30} stroke={4} showText={false} label={`${p.done} of ${p.total} done`} />
                      )}
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
