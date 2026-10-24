"""Assemble the entrepreneurship course JSON from the module files.

Usage: python3 build.py [--out PATH]
"""
import importlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import common  # noqa: E402

OUT = '/home/claude/vidhyarambham/public/courses/entrepreneurship.json'
if '--out' in sys.argv:
    OUT = sys.argv[sys.argv.index('--out') + 1]

modules = []
for m in range(1, 15):
    name = f'm{m:02d}'
    if os.path.exists(os.path.join(HERE, f'{name}.py')):
        mod = importlib.import_module(name)
        modules.append((m, mod))

have_extras = os.path.exists(os.path.join(HERE, 'extras.py'))
extras = importlib.import_module('extras') if have_extras else None

sections = []
if extras:
    sections += extras.front(modules)
for m, mod in modules:
    sections.append(mod.MODULE)
    sections += mod.LESSONS
if extras:
    sections += extras.back(modules)

course = {
    'format': 'vidhyarambham-course',
    'formatVersion': 1,
    'id': 'entrepreneurship',
    'version': 1,
    'title': 'Practical Entrepreneurship: From Idea to First Revenue',
    'summary': 'Go from no idea to a tested idea, a launched micro-business and your first paying customers, using only free resources. Kerala examples, rupee numbers, scripts and templates throughout. Part-time: 32 weeks at about 6 hours a week. Full-time: about 8 weeks.',
    'language': 'en',
    'updated': common.VDATE,
    'totalWeeks': 32,
    'paces': [
        {'id': 'part-time', 'label': 'Part-time', 'hoursPerWeek': 6, 'weekLength': 1,
         'note': 'Alongside PSC prep or a job: 32 weeks at about 6 hours a week'},
        {'id': 'full-time', 'label': 'Full-time', 'hoursPerWeek': 24, 'weekLength': 0.25,
         'note': 'About 8 calendar weeks: four course weeks every week, about 24 hours a week'},
    ],
    'sections': sections,
}

if extras and hasattr(extras, 'finish'):
    extras.finish(course)

with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(course, f, ensure_ascii=False, indent=1)
    f.write('\n')

size = os.path.getsize(OUT)
tasks = sum(len(s.get('tasks', [])) for s in sections)
print(f'wrote {OUT}: {size/1024:.0f} KB, {len(sections)} sections, {tasks} tasks, {len(common.USED)} links used')
