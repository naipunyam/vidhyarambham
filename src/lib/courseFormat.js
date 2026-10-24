// Course file format, version 1. See COURSE_FORMAT.md for the full guide.
// Plain JavaScript with no imports, so it runs in the app, in tests and in CI.

export const COURSE_FORMAT = 'vidhyarambham-course'
export const COURSE_FORMAT_VERSION = 1

export const SECTION_KINDS = ['intro', 'setup', 'level', 'gate', 'track', 'capstone', 'reference']
export const TASK_KINDS = ['task', 'project', 'exit']

const ID_PATTERN = /^[a-z0-9][a-z0-9-]{0,63}$/
const DATE_PATTERN = /^\d{4}-\d{2}-\d{2}$/

const isObject = (v) => v !== null && typeof v === 'object' && !Array.isArray(v)
const isText = (v) => typeof v === 'string' && v.trim().length > 0
const isWholeNumber = (v) => Number.isInteger(v) && v >= 0

// Returns a list of plain-English problems. An empty list means the course is valid.
export function validateCourse(course) {
  const errors = []
  const add = (where, problem) => errors.push(`${where}: ${problem}`)

  if (!isObject(course)) return ['The file is not a course object.']

  if (course.format !== COURSE_FORMAT) add('format', `must be "${COURSE_FORMAT}"`)
  if (course.formatVersion !== COURSE_FORMAT_VERSION) {
    add('formatVersion', `must be ${COURSE_FORMAT_VERSION}`)
  }
  if (typeof course.id !== 'string' || !ID_PATTERN.test(course.id)) {
    add('id', 'use lowercase letters, numbers and hyphens, up to 64 characters')
  }
  if (!Number.isInteger(course.version) || course.version < 1) {
    add('version', 'must be a whole number, 1 or more')
  }
  if (!isText(course.title)) add('title', 'is missing')
  if (course.summary !== undefined && typeof course.summary !== 'string') {
    add('summary', 'must be text')
  }
  if (course.updated !== undefined && !(typeof course.updated === 'string' && DATE_PATTERN.test(course.updated))) {
    add('updated', 'must be a date like 2026-10-21')
  }
  if (course.totalWeeks !== undefined && !(Number.isInteger(course.totalWeeks) && course.totalWeeks >= 1)) {
    add('totalWeeks', 'must be a whole number, 1 or more')
  }

  if (course.paces !== undefined) {
    if (!Array.isArray(course.paces) || course.paces.length === 0) {
      add('paces', 'must be a list with at least one pace')
    } else {
      const paceIds = new Set()
      course.paces.forEach((pace, i) => {
        const where = `paces[${i}]`
        if (!isObject(pace)) return add(where, 'must be an object')
        if (typeof pace.id !== 'string' || !ID_PATTERN.test(pace.id)) add(`${where}.id`, 'is not a valid id')
        else if (paceIds.has(pace.id)) add(`${where}.id`, `"${pace.id}" is used twice`)
        else paceIds.add(pace.id)
        if (!isText(pace.label)) add(`${where}.label`, 'is missing')
        if (!(typeof pace.weekLength === 'number' && pace.weekLength > 0 && pace.weekLength <= 8)) {
          add(`${where}.weekLength`, 'must be a number between 0 and 8 (1 means one calendar week per course week)')
        }
        if (pace.hoursPerWeek !== undefined && !(typeof pace.hoursPerWeek === 'number' && pace.hoursPerWeek > 0)) {
          add(`${where}.hoursPerWeek`, 'must be a positive number')
        }
      })
    }
  }

  if (!Array.isArray(course.sections) || course.sections.length === 0) {
    add('sections', 'must be a list with at least one section')
    return errors
  }

  const sectionIds = new Set()
  const taskIds = new Set()
  course.sections.forEach((section, i) => {
    const where = `sections[${i}]`
    if (!isObject(section)) return add(where, 'must be an object')
    const label = typeof section.id === 'string' ? `section "${section.id}"` : where

    if (typeof section.id !== 'string' || !ID_PATTERN.test(section.id)) add(`${where}.id`, 'is not a valid id')
    else if (sectionIds.has(section.id)) add(`${where}.id`, `"${section.id}" is used twice`)
    else sectionIds.add(section.id)

    if (!isText(section.title)) add(`${label}.title`, 'is missing')
    if (!SECTION_KINDS.includes(section.kind)) {
      add(`${label}.kind`, `must be one of: ${SECTION_KINDS.join(', ')}`)
    }
    if (section.weeks !== undefined) {
      const w = section.weeks
      if (!(Array.isArray(w) && w.length === 2 && isWholeNumber(w[0]) && isWholeNumber(w[1]) && w[0] <= w[1])) {
        add(`${label}.weeks`, 'must be [startWeek, endWeek], for example [1, 2]')
      }
    }
    if (section.hours !== undefined && !(typeof section.hours === 'number' && section.hours > 0)) {
      add(`${label}.hours`, 'must be a positive number')
    }
    for (const field of ['summary', 'content']) {
      if (section[field] !== undefined && typeof section[field] !== 'string') add(`${label}.${field}`, 'must be text')
    }
    if (section.tasks === undefined) return
    if (!Array.isArray(section.tasks)) return add(`${label}.tasks`, 'must be a list')

    section.tasks.forEach((task, j) => {
      const tw = `${label}.tasks[${j}]`
      if (!isObject(task)) return add(tw, 'must be an object')
      if (typeof task.id !== 'string' || !ID_PATTERN.test(task.id)) add(`${tw}.id`, 'is not a valid id')
      else if (taskIds.has(task.id)) add(`${tw}.id`, `"${task.id}" is used twice; task ids must be unique in the whole course`)
      else taskIds.add(task.id)
      if (!isText(task.text)) add(`${tw}.text`, 'is missing')
      if (task.kind !== undefined && !TASK_KINDS.includes(task.kind)) {
        add(`${tw}.kind`, `must be one of: ${TASK_KINDS.join(', ')}`)
      }
      if (task.detail !== undefined && typeof task.detail !== 'string') add(`${tw}.detail`, 'must be text')
      if (task.week !== undefined && !isWholeNumber(task.week)) add(`${tw}.week`, 'must be a whole number')
    })
  })

  return errors
}

// Parses text from a course file. Returns { course } or { errors }.
export function parseCourseText(text) {
  let data
  try {
    data = JSON.parse(text)
  } catch (err) {
    return { errors: [`This is not valid JSON: ${err.message}`] }
  }
  const errors = validateCourse(data)
  return errors.length ? { errors } : { course: data }
}

export function allTasks(course) {
  return (course.sections || []).flatMap((s) => (s.tasks || []).map((t) => ({ ...t, sectionId: s.id })))
}
