// Route parsing for hash URLs (#/course/x). Pure functions, no React.

export function parseRoute(hash) {
  const parts = String(hash || '')
    .replace(/^#\/?/, '')
    .split('/')
    .filter(Boolean)
    .map((p) => {
      try {
        return decodeURIComponent(p)
      } catch {
        return p
      }
    })
  if (parts[0] === 'course' && parts[1] && parts[2]) return { name: 'section', courseId: parts[1], sectionId: parts[2] }
  if (parts[0] === 'course' && parts[1]) return { name: 'course', courseId: parts[1] }
  if (parts[0] === 'backup') return { name: 'backup' }
  if (parts[0] === 'add') return { name: 'add' }
  return { name: 'library' }
}

export function hrefFor(route) {
  switch (route.name) {
    case 'section':
      return `#/course/${encodeURIComponent(route.courseId)}/${encodeURIComponent(route.sectionId)}`
    case 'course':
      return `#/course/${encodeURIComponent(route.courseId)}`
    case 'backup':
      return '#/backup'
    case 'add':
      return '#/add'
    default:
      return '#/'
  }
}
