import { sectionProgress, toggleTask, setNote } from '../lib/progress.js'
import { hrefFor } from '../lib/routes.js'
import { splitCourseTitle, splitSectionTitle, capitalise } from '../lib/look.js'
import { BackLink, Markdown, ProgressBar, SectionTitle, weeksLabel, hoursLabel } from './Bits.jsx'
import TaskItem from './TaskItem.jsx'
import Roadmap from './Roadmap.jsx'

export default function SectionPage({ course, section, progress, onChange }) {
  const p = sectionProgress(section, progress.done)
  const tasks = section.tasks || []
  const index = course.sections.findIndex((s) => s.id === section.id)
  const prev = course.sections[index - 1]
  const next = course.sections[index + 1]
  const { label, text } = splitSectionTitle(section.title)
  const pills = [weeksLabel(section.weeks), section.hours ? capitalise(`${hoursLabel(section.hours)} at full pace`) : null].filter(Boolean)

  return (
    <>
      <BackLink to={{ name: 'course', courseId: course.id }}>{splitCourseTitle(course.title).main}</BackLink>

      <header className="section-head">
        {label && (
          <p className="section-label" aria-hidden="true">
            {label}
          </p>
        )}
        <h1 className="page-title">
          {label && <span className="visually-hidden">{label}: </span>}
          {text}
        </h1>
        {pills.length > 0 && (
          <p className="pills">
            {pills.map((pill) => (
              <span key={pill} className="pill soft">
                {pill}
              </span>
            ))}
          </p>
        )}
        {section.summary && <Markdown source={section.summary} className="prose lede" />}
      </header>

      {tasks.length > 0 && (
        <section className="panel tasks-panel" aria-labelledby="tasks-h">
          <div className="panel-head">
            <h2 id="tasks-h">Your tasks</h2>
            <span className="count">
              {p.done} of {p.total} done
            </span>
          </div>
          <ProgressBar percent={p.percent} label={`${section.title} progress`} />
          <ul className="tasks">
            {tasks.map((t) => (
              <TaskItem
                key={t.id}
                task={t}
                done={Boolean(progress.done[t.id])}
                onToggle={() => onChange((pr) => toggleTask(pr, t.id))}
                note={progress.notes[t.id]}
                onNoteChange={(value) => onChange((pr) => setNote(pr, t.id, value))}
              />
            ))}
          </ul>
        </section>
      )}

      {section.roadmap && <Roadmap course={course} settings={section.roadmap} done={progress.done} />}

      <Markdown source={section.content} />

      <nav className="pager" aria-label="Sections">
        {prev ? (
          <a className="pager-prev" href={hrefFor({ name: 'section', courseId: course.id, sectionId: prev.id })}>
            <span className="pager-label">Previous</span>
            <SectionTitle title={prev.title} className="pager-title" />
          </a>
        ) : (
          <span />
        )}
        {next ? (
          <a className="pager-next" href={hrefFor({ name: 'section', courseId: course.id, sectionId: next.id })}>
            <span className="pager-label">Next</span>
            <SectionTitle title={next.title} className="pager-title" />
          </a>
        ) : (
          <a className="pager-next" href={hrefFor({ name: 'course', courseId: course.id })}>
            <span className="pager-label">Finished this part</span>
            <span className="pager-title">Back to the course plan</span>
          </a>
        )}
      </nav>
    </>
  )
}
