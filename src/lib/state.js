// App state: progress per course and the courses imported on this device.
// Saved in the browser's localStorage. Pure helpers take the storage object
// as an argument so they can be tested without a browser.

import { validateCourse } from './courseFormat.js'
import { emptyCourseProgress } from './progress.js'

export const STORAGE_KEY = 'vidhyarambham.state.v1'
export const BACKUP_FORMAT = 'vidhyarambham-backup'
export const BACKUP_FORMAT_VERSION = 1

export function emptyState() {
  return { schema: 1, progress: {}, imported: {} }
}

export function loadState(storage) {
  try {
    const raw = storage && storage.getItem(STORAGE_KEY)
    if (!raw) return emptyState()
    return normaliseState(JSON.parse(raw))
  } catch {
    return emptyState()
  }
}

// Returns true when saved. False means the browser refused (private mode or full storage).
export function saveState(storage, state) {
  try {
    storage.setItem(STORAGE_KEY, JSON.stringify(state))
    return true
  } catch {
    return false
  }
}

function normaliseState(data) {
  const state = emptyState()
  if (!data || typeof data !== 'object') return state
  if (data.progress && typeof data.progress === 'object') {
    for (const [id, p] of Object.entries(data.progress)) {
      if (!p || typeof p !== 'object') continue
      state.progress[id] = {
        ...emptyCourseProgress(),
        done: isPlainObject(p.done) ? p.done : {},
        notes: isPlainObject(p.notes) ? p.notes : {},
        pace: typeof p.pace === 'string' ? p.pace : null,
        startDate: typeof p.startDate === 'string' ? p.startDate : null,
      }
    }
  }
  if (data.imported && typeof data.imported === 'object') {
    for (const [id, course] of Object.entries(data.imported)) {
      if (validateCourse(course).length === 0 && course.id === id) state.imported[id] = course
    }
  }
  return state
}

function isPlainObject(v) {
  return v !== null && typeof v === 'object' && !Array.isArray(v)
}

export function getProgress(state, courseId) {
  return state.progress[courseId] || emptyCourseProgress()
}

export function withProgress(state, courseId, progress) {
  return { ...state, progress: { ...state.progress, [courseId]: progress } }
}

export function withImportedCourse(state, course) {
  return { ...state, imported: { ...state.imported, [course.id]: course } }
}

// Removing a course file keeps its progress, so re-importing it brings the ticks back.
export function withoutImportedCourse(state, courseId) {
  const imported = { ...state.imported }
  delete imported[courseId]
  return { ...state, imported }
}

// Combines courses shipped with the app and courses imported on this device.
// When both have the same id, the higher version wins; on a tie the shipped one wins.
export function mergeCourses(shipped, imported) {
  const byId = new Map()
  for (const c of shipped) byId.set(c.id, { course: c, source: 'shipped' })
  for (const c of Object.values(imported || {})) {
    const existing = byId.get(c.id)
    if (!existing || c.version > existing.course.version) byId.set(c.id, { course: c, source: 'imported' })
    else if (existing.source === 'shipped') existing.alsoImported = true
  }
  return [...byId.values()]
}

export function makeBackup(state, now = new Date()) {
  return {
    format: BACKUP_FORMAT,
    formatVersion: BACKUP_FORMAT_VERSION,
    app: 'Vidhyarambham',
    exportedAt: now.toISOString(),
    state,
  }
}

// Returns { state } or { error }.
export function readBackup(text) {
  let data
  try {
    data = JSON.parse(text)
  } catch {
    return { error: 'This file is not a Vidhyarambham backup. It is not valid JSON.' }
  }
  if (!data || data.format !== BACKUP_FORMAT) {
    if (data && data.format === 'vidhyarambham-course') {
      return { error: 'This is a course file, not a backup. Use "Add a course" on the home screen.' }
    }
    return { error: 'This file is not a Vidhyarambham backup.' }
  }
  if (data.formatVersion !== BACKUP_FORMAT_VERSION) {
    return { error: `This backup uses format version ${data.formatVersion}, which this version of the app cannot read.` }
  }
  return { state: normaliseState(data.state) }
}

export function backupFileName(now = new Date()) {
  const d = now.toISOString().slice(0, 10)
  return `vidhyarambham-backup-${d}.json`
}
