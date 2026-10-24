import { useState } from 'react'
import { makeBackup, readBackup, backupFileName } from '../lib/state.js'
import { courseProgress } from '../lib/progress.js'
import { BackLink } from './Bits.jsx'

export default function BackupPage({ state, entries, onRestore, onRemoveCourse }) {
  const [message, setMessage] = useState(null)

  const exportBackup = () => {
    const blob = new Blob([JSON.stringify(makeBackup(state), null, 2)], { type: 'application/json' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = backupFileName()
    document.body.appendChild(a)
    a.click()
    a.remove()
    setTimeout(() => URL.revokeObjectURL(url), 1000)
    setMessage({ kind: 'ok', text: `Backup saved as ${backupFileName()}. Keep it in Google Drive or send it to yourself.` })
  }

  const importBackup = async (e) => {
    const file = e.target.files && e.target.files[0]
    e.target.value = ''
    if (!file) return
    const result = readBackup(await file.text())
    if (result.error) {
      setMessage({ kind: 'error', text: result.error })
      return
    }
    const ok = window.confirm('Restore this backup? It replaces all progress, notes and added courses on this device.')
    if (!ok) return
    onRestore(result.state)
    setMessage({ kind: 'ok', text: 'Backup restored.' })
  }

  const imported = Object.values(state.imported)
  const titleOf = (id) => {
    const e = entries.find((x) => x.course.id === id)
    return e ? e.course.title : id
  }

  return (
    <>
      <BackLink to={{ name: 'library' }}>All courses</BackLink>
      <h1 className="page-title">Backup and courses</h1>
      <p className="lede">
        Your progress lives in this browser on this phone. Clearing Chrome's data erases it, so save a backup now and then.
      </p>

      {message && (
        <p className={message.kind === 'error' ? 'notice error' : 'notice'} role="status">
          {message.text}
        </p>
      )}

      <section className="panel" aria-labelledby="backup-h">
        <h2 id="backup-h">Backup</h2>
        <div className="actions">
          <button type="button" className="button primary" onClick={exportBackup}>
            Save a backup file
          </button>
          <label className="button file-button">
            Restore from a backup
            <input type="file" accept=".json,application/json" onChange={importBackup} />
          </label>
        </div>
        <p className="hint">A backup holds your ticks, notes, start dates and any courses you added from files.</p>
      </section>

      <section className="panel" aria-labelledby="added-h">
        <h2 id="added-h">Courses added on this device</h2>
        {imported.length === 0 ? (
          <p className="hint">None yet. Courses that come with the app aren't listed here.</p>
        ) : (
          <ul className="plain-list">
            {imported.map((c) => {
              const p = courseProgress(c, (state.progress[c.id] || { done: {} }).done)
              return (
                <li key={c.id} className="row">
                  <span>
                    {c.title}, version {c.version}
                    <span className="hint"> {p.done} of {p.total} done</span>
                  </span>
                  <button
                    type="button"
                    className="button small"
                    onClick={() => {
                      if (window.confirm(`Remove "${c.title}" from this device? Your ticks are kept and come back if you add it again.`)) {
                        onRemoveCourse(c.id)
                      }
                    }}
                  >
                    Remove
                  </button>
                </li>
              )
            })}
          </ul>
        )}
      </section>

      <section className="panel" aria-labelledby="saved-h">
        <h2 id="saved-h">Progress saved on this device</h2>
        {Object.keys(state.progress).length === 0 ? (
          <p className="hint">Nothing ticked yet.</p>
        ) : (
          <ul className="plain-list">
            {Object.entries(state.progress).map(([id, p]) => (
              <li key={id}>
                {titleOf(id)}: {Object.keys(p.done).length} ticks, {Object.keys(p.notes).length} notes
              </li>
            ))}
          </ul>
        )}
      </section>

      <p className="footnote">Vidhyarambham {__APP_VERSION__}</p>
    </>
  )
}
