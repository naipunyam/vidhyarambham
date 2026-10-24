import { sectionProgress, toggleTask, setNote } from '../lib/progress.js'
import { hrefFor } from '../lib/routes.js'
import { BackLink, Markdown, ProgressBar, weeksLabel } from './Bits.jsx'
import TaskItem from './TaskItem.jsx'

export default function SectionPage({ course, section, progress, onChange }) {
  const p = sectionProgress(section, progress.done)
  const tasks = section.tasks || []
  const index = course.sections.findIndex((s) => s.id === section.id)
  const prev = course.sections[index - 1]
  const next = course.sections[index + 1]
  const meta = [weeksLabel(section.weeks), section.hours ? `about ${section.hours} hours at full pace` : null].filter(Boolean)

  return (
    <>
      <BackLink to={{ name: 'course', courseId: course.id }}>{course.title}</BackLink>

      <header className="section-head">
        <h1 className="page-title">{section.title}</h1>
        {meta.length > 0 && <p className="meta">{meta.join(', ')}</p>}
        {section.summary && <Markdown source={section.summary} className="prose lede" />}
      </header>

      {tasks.length > 0 && (
        <section className="panel" aria-labelledby="tasks-h">
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
                onNoteChange={(text) => onChange((pr) => setNote(pr, t.id, text))}
              />
            ))}
          </ul>
        </section>
      )}

      <Markdown source={section.content} />

      <nav className="pager" aria-label="Sections">
        {prev ? (
          <a href={hrefFor({ name: 'section', courseId: course.id, sectionId: prev.id })}>
            <span className="pager-label">Previous</span>
            {prev.title}
          </a>
        ) : (
          <span />
        )}
        {next && (
          <a className="pager-next" href={hrefFor({ name: 'section', courseId: course.id, sectionId: next.id })}>
            <span className="pager-label">Next</span>
            {next.title}
          </a>
        )}
      </nav>
    </>
  )
}
