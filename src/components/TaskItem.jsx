import { useId, useState } from 'react'
import { KIND_LABEL, Markdown } from './Bits.jsx'

export default function TaskItem({ task, done, onToggle, context, overdue, note, onNoteChange }) {
  const id = useId()
  const [noteOpen, setNoteOpen] = useState(Boolean(note))
  const kind = KIND_LABEL[task.kind || 'task']
  return (
    <li className={`task${done ? ' done' : ''}${task.kind ? ` kind-${task.kind}` : ''}`}>
      <div className="task-main">
        <input id={id} type="checkbox" checked={done} onChange={onToggle} />
        <label htmlFor={id} className="task-text">
          {kind && <span className="tag">{kind}</span>}
          {task.text}
        </label>
      </div>
      {(context || overdue) && (
        <p className="task-context">
          {overdue && <span className="overdue">From an earlier week. </span>}
          {context}
        </p>
      )}
      {task.detail && <Markdown source={task.detail} className="prose task-detail" />}
      {onNoteChange && (
        <div className="task-note">
          {noteOpen ? (
            <label className="field">
              <span>Your note</span>
              <textarea
                rows={3}
                value={note || ''}
                placeholder="Links to your work, what you learned, what to fix"
                onChange={(e) => onNoteChange(e.target.value)}
              />
            </label>
          ) : (
            <button type="button" className="link-button" onClick={() => setNoteOpen(true)}>
              Add a note
            </button>
          )}
        </div>
      )}
    </li>
  )
}
