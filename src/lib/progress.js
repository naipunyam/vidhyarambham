// Progress and schedule maths. Pure functions, no browser APIs.

const DAY_MS = 24 * 60 * 60 * 1000

export function emptyCourseProgress() {
  return { done: {}, notes: {}, pace: null, startDate: null }
}

// Counts only tasks that exist in the current version of the course,
// so ticks for removed tasks are kept but never counted.
export function sectionProgress(section, done = {}) {
  const tasks = section.tasks || []
  const completed = tasks.filter((t) => Boolean(done[t.id])).length
  return { done: completed, total: tasks.length, percent: percentOf(completed, tasks.length) }
}

export function courseProgress(course, done = {}) {
  let completed = 0
  let total = 0
  const bySection = {}
  for (const section of course.sections || []) {
    const p = sectionProgress(section, done)
    bySection[section.id] = p
    completed += p.done
    total += p.total
  }
  return { done: completed, total, percent: percentOf(completed, total), bySection }
}

export function percentOf(part, whole) {
  if (!whole) return 0
  return Math.round((part / whole) * 100)
}

export function toggleTask(progress, taskId, now = new Date()) {
  const done = { ...progress.done }
  if (done[taskId]) delete done[taskId]
  else done[taskId] = now.toISOString()
  return { ...progress, done }
}

export function setNote(progress, taskId, text) {
  const notes = { ...progress.notes }
  if (text && text.trim()) notes[taskId] = text
  else delete notes[taskId]
  return { ...progress, notes }
}

export function pickPace(course, paceId) {
  const paces = course.paces || []
  return paces.find((p) => p.id === paceId) || paces[0] || { id: 'default', label: 'Standard', weekLength: 1 }
}

// Parses YYYY-MM-DD as a local calendar date (not UTC), so the week
// never shifts by a day on phones in India or anywhere else.
export function parseLocalDate(value) {
  if (typeof value !== 'string') return null
  const m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(value)
  if (!m) return null
  const d = new Date(Number(m[1]), Number(m[2]) - 1, Number(m[3]))
  return Number.isNaN(d.getTime()) ? null : d
}

export function toLocalDateString(date) {
  const y = date.getFullYear()
  const m = String(date.getMonth() + 1).padStart(2, '0')
  const d = String(date.getDate()).padStart(2, '0')
  return `${y}-${m}-${d}`
}

// Which course week you are in. Week 0 is the start day's week when the
// course has a Week 0; otherwise counting starts at week 1.
// Returns { week, status } where status is 'not-started', 'not-yet', 'running' or 'finished'.
export function currentWeek(course, progress, today = new Date()) {
  const start = parseLocalDate(progress && progress.startDate)
  if (!start) return { week: null, status: 'not-started' }
  const pace = pickPace(course, progress.pace)
  const firstWeek = (course.sections || []).some((s) => s.weeks && s.weeks[0] === 0) ? 0 : 1
  const startOfToday = new Date(today.getFullYear(), today.getMonth(), today.getDate())
  const days = Math.round((startOfToday - start) / DAY_MS)
  if (days < 0) return { week: firstWeek, status: 'not-yet', daysToStart: -days }
  const week = firstWeek + Math.floor(days / (7 * pace.weekLength))
  const lastWeek = course.totalWeeks || lastWeekOf(course)
  if (lastWeek !== null && week > lastWeek) return { week: lastWeek, status: 'finished' }
  return { week, status: 'running' }
}

export function lastWeekOf(course) {
  let last = null
  for (const s of course.sections || []) {
    if (s.weeks && (last === null || s.weeks[1] > last)) last = s.weeks[1]
  }
  return last
}

export function sectionsInWeek(course, week) {
  if (week === null || week === undefined) return []
  return (course.sections || []).filter((s) => s.weeks && s.weeks[0] <= week && week <= s.weeks[1])
}

// Tasks to focus on this week: open tasks in active sections whose week is
// this week or earlier (overdue first), plus open tasks without a week.
export function tasksForWeek(course, progress, week) {
  const done = (progress && progress.done) || {}
  const out = []
  for (const section of sectionsInWeek(course, week)) {
    for (const task of section.tasks || []) {
      if (done[task.id]) continue
      const due = task.week === undefined ? section.weeks[1] : task.week
      if (section.kind === 'track' && task.week !== undefined && task.week > week) {
        // Track tasks belong to a phase; show only the current or overdue phase.
        const phaseStart = phaseStartOf(section, task)
        if (phaseStart > week) continue
      }
      out.push({ ...task, sectionId: section.id, sectionTitle: section.title, due, overdue: due < week })
    }
  }
  return out.sort((a, b) => a.due - b.due)
}

function phaseStartOf(section, task) {
  const tasks = section.tasks || []
  const i = tasks.indexOf(task)
  if (i <= 0) return section.weeks[0]
  const prev = tasks[i - 1]
  return prev.week === undefined ? section.weeks[0] : prev.week + 1
}

// Calendar date when a course week starts, for showing "Week 5 starts 3 Dec".
export function weekStartDate(course, progress, week) {
  const start = parseLocalDate(progress && progress.startDate)
  if (!start) return null
  const pace = pickPace(course, progress.pace)
  const firstWeek = (course.sections || []).some((s) => s.weeks && s.weeks[0] === 0) ? 0 : 1
  const d = new Date(start)
  d.setDate(d.getDate() + Math.round((week - firstWeek) * 7 * pace.weekLength))
  return d
}
