"""Assemble the learning capabilities course JSON from the module files.

Usage: python3 build.py [--out PATH]
"""
import importlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import common  # noqa: E402

OUT = '/home/claude/vidhyarambham/public/courses/learning-capabilities.json'
if '--out' in sys.argv:
    OUT = sys.argv[sys.argv.index('--out') + 1]

modules = []
for m in range(1, 22):
    name = f'm{m:02d}'
    if os.path.exists(os.path.join(HERE, f'{name}.py')):
        modules.append((m, importlib.import_module(name)))

extras = importlib.import_module('extras')

sections = []
sections += extras.front()
for m, mod in modules:
    sections.append(mod.MODULE)
    sections += mod.LESSONS
sections += extras.back()

FINAL = common.LAST_WEEK
course = {
    'format': 'vidhyarambham-course',
    'formatVersion': 1,
    'id': 'learning-capabilities',
    'version': 1,
    'title': 'Practical Learning Capabilities: Learn Faster, Remember Longer, Focus Better',
    'summary': (f'An evidence-based "learn how to learn" course done on your own Kerala PSC material. Measure your memory, reading, '
                f'focus and digit span in week 0 and again at the end; build a 100-card AnkiDroid deck, a memory palace, five Feynman '
                f'recordings, a PYQ analysis and error log, a 12-week PSC study plan and a 30-day learning sprint. Honest evidence '
                f'ratings for every technique, free and open-source tools only. Part-time: {FINAL} weeks at about 6 hours a week. '
                f'Full-time: about {len(extras.full_time_rows())} weeks.'),
    'language': 'en',
    'updated': common.VDATE,
    'totalWeeks': FINAL,
    'paces': [
        {'id': 'part-time', 'label': 'Part-time', 'hoursPerWeek': 6, 'weekLength': 1,
         'note': f'Alongside PSC study or a job: {FINAL} weeks at about 6 hours a week (5 to 7)'},
        {'id': 'full-time', 'label': 'Full-time', 'hoursPerWeek': 15, 'weekLength': extras.FULL_TIME_WEEK,
         'note': f'About {len(extras.full_time_rows())} calendar weeks at about 15 hours a week. The 30-day AnkiDroid review and the 30-day sprint still take real days; see the weekly schedule.'},
    ],
    'sections': sections,
}

extras.finish(course)

with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(course, f, ensure_ascii=False, indent=1)
    f.write('\n')

size = os.path.getsize(OUT)
tasks = sum(len(s.get('tasks', [])) for s in sections)
print(f'wrote {OUT}: {size/1024:.0f} KB, {len(sections)} sections, {tasks} tasks, {len(common.USED)} links used, quiz letters {dict(common.QUIZ_LETTERS)}')
