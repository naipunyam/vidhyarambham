"""Assemble the Mind, Body and People course JSON from the module files.

Usage: python3 build.py [--out PATH]
"""
import importlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import common  # noqa: E402

OUT = '/home/claude/vidhyarambham/public/courses/mind-body-people.json'
if '--out' in sys.argv:
    OUT = sys.argv[sys.argv.index('--out') + 1]

modules = []
for m in range(1, 37):
    name = f'm{m:02d}'
    if os.path.exists(os.path.join(HERE, f'{name}.py')):
        modules.append((m, importlib.import_module(name)))

extras = importlib.import_module('extras')

sections = []
sections += extras.front()
import plan  # noqa: E402
starts = {p[2]: p[0] for p in plan.PARTS}
for m, mod in modules:
    if m in starts:
        sections.append(extras.part_section(starts[m]))
    sections.append(mod.MODULE)
    sections += mod.LESSONS
sections += extras.back()

FINAL = common.LAST_WEEK
course = {
    'format': 'vidhyarambham-course',
    'formatVersion': 1,
    'id': 'mind-body-people',
    'version': 1,
    'title': 'Mind, Body and People: Win Over Yourself and Others',
    'summary': (f'A practical, evidence-based personal development and everyday-psychology course in five parts: understand your mind, '
                f'master yourself, strengthen your body, win with people ethically, and character and purpose. Real-world tasks with proof in '
                f'every lesson; baseline tests repeated at the end; 30-day meditation, journaling, rejection-therapy and fitness challenges; '
                f'honest evidence ratings, including what failed to replicate. Free resources only. Part-time: {FINAL} weeks at about 5 to 6 '
                f'hours a week. Full-time: about {len(extras.full_time_rows())} weeks.'),
    'language': 'en',
    'updated': common.VDATE,
    'totalWeeks': FINAL,
    'paces': [
        {'id': 'part-time', 'label': 'Part-time', 'hoursPerWeek': 6, 'weekLength': 1,
         'note': f'Alongside PSC study or a job: {FINAL} weeks at about 5 to 6 study hours a week, plus 10 to 40 minutes a day of practice'},
        {'id': 'full-time', 'label': 'Full-time', 'hoursPerWeek': 15, 'weekLength': extras.FULL_TIME_WEEK,
         'note': f'About {len(extras.full_time_rows())} calendar weeks at about 15 hours a week. The 30-day challenges still take 30 real days; see the weekly schedule.'},
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
