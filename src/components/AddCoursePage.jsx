import { useState } from 'react'
import { parseCourseText } from '../lib/courseFormat.js'
import { loadCourseFromUrl } from '../lib/loader.js'
import { navigate } from '../lib/router.js'
import { BackLink } from './Bits.jsx'

export default function AddCoursePage({ entries, onAdd }) {
  const [errors, setErrors] = useState([])
  const [url, setUrl] = useState('')
  const [busy, setBusy] = useState(false)

  const accept = (result) => {
    if (result.errors) {
      setErrors(result.errors)
      return
    }
    const course = result.course
    const existing = entries.find((e) => e.course.id === course.id)
    if (existing && existing.course.version > course.version) {
      setErrors([
        `You already have "${existing.course.title}" version ${existing.course.version}. This file is the older version ${course.version}, so nothing was changed.`,
      ])
      return
    }
    onAdd(course)
    navigate({ name: 'course', courseId: course.id })
  }

  const fromFile = async (e) => {
    const file = e.target.files && e.target.files[0]
    e.target.value = ''
    if (!file) return
    setErrors([])
    accept(parseCourseText(await file.text()))
  }

  const fromLink = async (e) => {
    e.preventDefault()
    setErrors([])
    setBusy(true)
    const result = await loadCourseFromUrl(url.trim(), (u) => fetch(u))
    setBusy(false)
    accept(result)
  }

  return (
    <>
      <BackLink to={{ name: 'library' }}>All courses</BackLink>
      <h1 className="page-title">Add a course</h1>
      <p className="lede">
        A course is one <code>.json</code> file in the Vidhyarambham course format. Your ticks stay safe when you add a newer
        version of the same course.
      </p>

      <section className="panel" aria-labelledby="file-h">
        <h2 id="file-h">From a file on this phone</h2>
        <label className="button primary file-button">
          Choose a course file
          <input type="file" accept=".json,application/json" onChange={fromFile} />
        </label>
        <p className="hint">The course is saved on this device only.</p>
      </section>

      <section className="panel" aria-labelledby="link-h">
        <h2 id="link-h">From a link</h2>
        <form onSubmit={fromLink}>
          <label className="field">
            <span>Link to the file</span>
            <input
              type="url"
              inputMode="url"
              placeholder="https://raw.githubusercontent.com/…/course.json"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              required
            />
          </label>
          <button type="submit" className="button" disabled={busy}>
            {busy ? 'Downloading…' : 'Add from link'}
          </button>
        </form>
        <p className="hint">For a file on GitHub, open it, tap Raw, and copy that address.</p>
      </section>

      {errors.length > 0 && (
        <section className="panel error" role="alert">
          <h2>This course wasn't added</h2>
          <ul>
            {errors.slice(0, 8).map((err) => (
              <li key={err}>{err}</li>
            ))}
          </ul>
          {errors.length > 8 && <p>And {errors.length - 8} more problems.</p>}
          <p className="hint">COURSE_FORMAT.md in the app's GitHub repo explains every field.</p>
        </section>
      )}
    </>
  )
}
