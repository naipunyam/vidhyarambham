import { useCallback, useEffect, useMemo, useState } from 'react'
import { useRoute } from './lib/router.js'
import { loadShippedCourses } from './lib/loader.js'
import { loadState, saveState, mergeCourses, getProgress, withProgress, withImportedCourse, withoutImportedCourse } from './lib/state.js'
import Library from './components/Library.jsx'
import CoursePage from './components/CoursePage.jsx'
import SectionPage from './components/SectionPage.jsx'
import BackupPage from './components/BackupPage.jsx'
import AddCoursePage from './components/AddCoursePage.jsx'
import NotFound from './components/NotFound.jsx'

function browserStorage() {
  try {
    return window.localStorage
  } catch {
    return null
  }
}

export default function App() {
  const route = useRoute()
  const [state, setState] = useState(() => loadState(browserStorage()))
  const [shipped, setShipped] = useState({ status: 'loading', courses: [], problems: [] })
  const [saveFailed, setSaveFailed] = useState(false)

  useEffect(() => {
    let cancelled = false
    loadShippedCourses(import.meta.env.BASE_URL, (url, opts) => fetch(url, opts)).then((result) => {
      if (!cancelled) setShipped({ status: 'ready', ...result })
    })
    return () => {
      cancelled = true
    }
  }, [])

  useEffect(() => {
    const storage = browserStorage()
    setSaveFailed(!storage || !saveState(storage, state))
  }, [state])

  const entries = useMemo(() => mergeCourses(shipped.courses, state.imported), [shipped.courses, state.imported])

  const updateProgress = useCallback((courseId, change) => {
    setState((s) => withProgress(s, courseId, change(getProgress(s, courseId))))
  }, [])

  const addCourse = useCallback((course) => setState((s) => withImportedCourse(s, course)), [])
  const removeCourse = useCallback((courseId) => setState((s) => withoutImportedCourse(s, courseId)), [])
  const replaceState = useCallback((next) => setState(next), [])

  const findEntry = (id) => entries.find((e) => e.course.id === id)
  const loading = shipped.status === 'loading'

  let page
  if (route.name === 'library') {
    page = <Library entries={entries} state={state} loading={loading} problems={shipped.problems} offline={shipped.offline} />
  } else if (route.name === 'add') {
    page = <AddCoursePage entries={entries} onAdd={addCourse} />
  } else if (route.name === 'backup') {
    page = <BackupPage state={state} entries={entries} onRestore={replaceState} onRemoveCourse={removeCourse} />
  } else {
    const entry = findEntry(route.courseId)
    if (!entry) {
      page = loading ? <p className="loading">Loading the course…</p> : <NotFound what="course" />
    } else {
      const progress = getProgress(state, entry.course.id)
      const onChange = (change) => updateProgress(entry.course.id, change)
      if (route.name === 'course') {
        page = <CoursePage entry={entry} progress={progress} onChange={onChange} />
      } else {
        const section = entry.course.sections.find((s) => s.id === route.sectionId)
        page = section ? (
          <SectionPage course={entry.course} section={section} progress={progress} onChange={onChange} />
        ) : (
          <NotFound what="section" />
        )
      }
    }
  }

  return (
    <div className="app">
      {saveFailed && (
        <p className="banner" role="alert">
          Your progress can't be saved in this browser, so ticks will be lost when you close it. Turn off private
          browsing, or free up storage, and reload.
        </p>
      )}
      <main className="page">{page}</main>
    </div>
  )
}
