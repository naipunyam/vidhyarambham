import { test } from 'node:test'
import assert from 'node:assert/strict'
import { parseRoute, hrefFor } from '../src/lib/routes.js'

test('routes parse and round-trip', () => {
  for (const r of [{ name: 'library' }, { name: 'backup' }, { name: 'add' }, { name: 'course', courseId: 'ai-generalist' }, { name: 'section', courseId: 'ai-generalist', sectionId: 'level-0' }]) {
    assert.deepEqual(parseRoute(hrefFor(r)), r)
  }
  assert.deepEqual(parseRoute(''), { name: 'library' })
  assert.deepEqual(parseRoute('#/nonsense'), { name: 'library' })
  assert.deepEqual(parseRoute('#/course/%E0%B4%85'), { name: 'course', courseId: 'അ' })
  assert.deepEqual(parseRoute('#/course/%E0'), { name: 'course', courseId: '%E0' })
})
