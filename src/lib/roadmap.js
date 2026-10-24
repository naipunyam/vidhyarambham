// Builds the course roadmap from the course itself: the steps run top to
// bottom, and a track section (such as a weekly business track) runs beside
// them, with each track task placed next to the step whose weeks it falls in.

export const ROADMAP_STEP_KINDS = ['setup', 'level', 'gate', 'capstone']

export function buildRoadmap(course, done = {}) {
  const sections = course.sections || []
  const steps = sections.filter((s) => ROADMAP_STEP_KINDS.includes(s.kind))
  const track = sections.find((s) => s.kind === 'track') || null

  const rows = steps.map((s) => {
    const tasks = s.tasks || []
    return {
      id: s.id,
      title: s.title,
      kind: s.kind,
      weeks: s.weeks || null,
      hours: s.hours || null,
      total: tasks.length,
      done: tasks.filter((t) => done[t.id]).length,
      trackItems: [],
      inTrack: false,
    }
  })

  if (track && track.weeks) {
    const [from, to] = track.weeks
    for (const row of rows) {
      if (row.weeks && row.weeks[1] >= from && row.weeks[0] <= to) row.inTrack = true
    }
    for (const task of track.tasks || []) {
      if (task.week === undefined) continue
      // The first step whose weeks contain the task's week gets it.
      const row = rows.find((r) => r.weeks && r.weeks[0] <= task.week && task.week <= r.weeks[1])
      if (row) row.trackItems.push({ id: task.id, text: task.text, done: Boolean(done[task.id]) })
    }
  }

  return {
    rows,
    track: track ? { id: track.id, title: track.title, weeks: track.weeks || null } : null,
  }
}
