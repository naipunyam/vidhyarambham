import { test } from 'node:test'
import assert from 'node:assert/strict'
import { TONES, toneFor, splitCourseTitle, splitSectionTitle, firstSentence, clip, capitalise } from '../src/lib/look.js'

test('shipped courses keep their fixed colours', () => {
  assert.equal(toneFor('social-media-marketing'), 'raspberry')
  assert.equal(toneFor('ai-generalist'), 'indigo')
  assert.equal(toneFor('entrepreneurship'), 'teal')
})

test('any other course gets a stable colour from the palette', () => {
  const a = toneFor('my-new-course')
  assert.ok(TONES.includes(a))
  assert.equal(toneFor('my-new-course'), a)
  assert.ok(TONES.includes(toneFor('')))
})

test('course titles split at the first colon', () => {
  assert.deepEqual(splitCourseTitle('Practical Entrepreneurship: From Idea to First Revenue'), {
    main: 'Practical Entrepreneurship',
    sub: 'From Idea to First Revenue',
  })
  assert.deepEqual(splitCourseTitle('Free AI Generalist Course'), { main: 'Free AI Generalist Course', sub: null })
})

test('short lead-ins in section titles become labels', () => {
  assert.deepEqual(splitSectionTitle('SMM-M01-L01: How social platforms work'), {
    label: 'SMM-M01-L01',
    text: 'How social platforms work',
  })
  assert.deepEqual(splitSectionTitle('Module 1: Foundations'), { label: 'Module 1', text: 'Foundations' })
  assert.deepEqual(splitSectionTitle('Start here: how this course works'), { label: 'Start here', text: 'How this course works' })
})

test('long lead-ins and titles without a colon stay whole', () => {
  const long = 'Skills first, a path in Week 14, clients later: the plan'
  assert.deepEqual(splitSectionTitle(long), { label: null, text: long })
  assert.deepEqual(splitSectionTitle('Decision gate and the three business paths'), {
    label: null,
    text: 'Decision gate and the three business paths',
  })
  assert.deepEqual(splitSectionTitle('Odd title:'), { label: null, text: 'Odd title:' })
})

test('first sentence of a summary', () => {
  assert.equal(firstSentence('Grow a real account. Then get clients.'), 'Grow a real account.')
  assert.equal(firstSentence('No full stop here'), 'No full stop here')
  assert.equal(firstSentence(''), '')
})

test('clip shortens at a word break', () => {
  assert.equal(clip('Short text', 50), 'Short text')
  assert.equal(clip('Grow a real account with measured results, run a real campaign', 40), 'Grow a real account with measured…')
  assert.equal(capitalise('about 3 hours'), 'About 3 hours')
})
