"""Assemble the personal finance course JSON from the module files.

Usage: python3 build.py [--out PATH]
"""
import importlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import common  # noqa: E402

OUT = '/home/claude/vidhyarambham/public/courses/personal-finance.json'
if '--out' in sys.argv:
    OUT = sys.argv[sys.argv.index('--out') + 1]

modules = []
for m in range(1, 18):
    name = f'm{m:02d}'
    if os.path.exists(os.path.join(HERE, f'{name}.py')):
        mod = importlib.import_module(name)
        modules.append((m, mod))

extras = importlib.import_module('extras')

sections = []
sections += extras.front(modules)
for m, mod in modules:
    sections.append(mod.MODULE)
    sections += mod.LESSONS
sections += extras.back(modules)

course = {
    'format': 'vidhyarambham-course',
    'formatVersion': 1,
    'id': 'personal-finance',
    'version': 1,
    'title': 'Practical Personal Finance for India: Budget, Protect, Invest and Plan',
    'summary': 'Build a working budget, a net-worth tracker, an emergency fund plan, an insurance checklist, a written investment policy, a tax checklist, scam-proof habits and a complete personal financial plan, using your own money, free tools and official sources. Kerala examples, rupee calculations and copy-ready spreadsheet templates throughout. Educational only: no product tips. Part-time: 30 weeks at about 5 hours a week. Full-time: about 10 weeks.',
    'language': 'en',
    'updated': common.VDATE,
    'totalWeeks': 30,
    'paces': [
        {'id': 'part-time', 'label': 'Part-time', 'hoursPerWeek': 5, 'weekLength': 1,
         'note': 'Alongside PSC prep or a job: 30 weeks at about 5 hours a week'},
        {'id': 'full-time', 'label': 'Full-time', 'hoursPerWeek': 14, 'weekLength': 0.33,
         'note': 'About 10 calendar weeks at about 14 hours a week. The 30-day expense tracking still takes 30 real days; see the weekly schedule.'},
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
