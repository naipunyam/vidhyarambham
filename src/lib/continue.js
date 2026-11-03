// Which course to show in "Continue where you left off" on the library page.
// Pure functions: the caller passes in the state and today's date.

import { currentWeek, lastWeekOf, tasksForWeek } from './progress.js'
import { getProgress } from './state.js'

// Returns the running course you ticked something in most recently (or the
// first running course if nothing is ticked yet), with its week and the
// number of tasks still open this week. Returns null when no course is running.
export function pickContinue(entries, state, today = new Date()) {
  const running = []
  for (const { course } of entries || []) {
    const progress = getProgress(state, course.id)
    if (!progress.startDate) continue
    const now = currentWeek(course, progress, today)
    if (now.status !== 'running') continue
    const ticks = Object.values(progress.done || {}).filter((v) => typeof v === 'string')
    const lastTick = ticks.length ? ticks.sort()[ticks.length - 1] : ''
    running.push({
      course,
      week: now.week,
      lastWeek: course.totalWeeks || lastWeekOf(course),
      open: tasksForWeek(course, progress, now.week).length,
      lastTick,
    })
  }
  if (running.length === 0) return null
  // Most recent tick first; ties keep the library order.
  return running.reduce((best, item) => (item.lastTick > best.lastTick ? item : best))
}
