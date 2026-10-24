// Loads the courses shipped in public/courses/. The list lives in index.json.

import { validateCourse, parseCourseText } from './courseFormat.js'

// fetchFn is window.fetch in the app; tests pass a fake.
export async function loadShippedCourses(baseUrl, fetchFn) {
  const problems = []
  let index
  try {
    const res = await fetchFn(`${baseUrl}courses/index.json`, { cache: 'no-cache' })
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    index = await res.json()
  } catch (err) {
    return { courses: [], problems: [`Could not load the course list (${err.message}).`], offline: true }
  }

  const files = Array.isArray(index && index.courses) ? index.courses : []
  const results = await Promise.all(
    files.map(async (entry) => {
      const file = typeof entry === 'string' ? entry : entry && entry.file
      if (typeof file !== 'string' || !/^[a-z0-9][a-z0-9-]*\.json$/.test(file)) {
        problems.push(`index.json has an entry that is not a course file name: ${JSON.stringify(entry)}`)
        return null
      }
      try {
        const res = await fetchFn(`${baseUrl}courses/${file}`, { cache: 'no-cache' })
        if (!res.ok) throw new Error(`HTTP ${res.status}`)
        const course = await res.json()
        const errors = validateCourse(course)
        if (errors.length) {
          problems.push(`${file} has ${errors.length} problem(s). First: ${errors[0]}`)
          return null
        }
        return course
      } catch (err) {
        problems.push(`Could not load ${file} (${err.message}).`)
        return null
      }
    }),
  )
  return { courses: results.filter(Boolean), problems, offline: false }
}

// Import from a link, such as a raw GitHub or Gist URL. Returns { course } or { errors }.
export async function loadCourseFromUrl(url, fetchFn) {
  if (!/^https:\/\//i.test(url)) return { errors: ['Use a link that starts with https://'] }
  let text
  try {
    const res = await fetchFn(url)
    if (!res.ok) return { errors: [`The link answered with HTTP ${res.status}. Check that the file is public.`] }
    text = await res.text()
  } catch {
    return { errors: ['Could not download that link. Check your connection, and use a raw file link (for GitHub, tap "Raw" and copy that address).'] }
  }
  return parseCourseText(text)
}
