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

OUT = '/home/claude/vidhyarambham/public/courses/kerala-real-estate.json'
if '--out' in sys.argv:
    OUT = sys.argv[sys.argv.index('--out') + 1]

modules = []
for m in range(1, 23):
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
    'id': 'kerala-real-estate',
    'version': 1,
    'title': 'Kerala Real Estate Business: From Token Advance to Registration',
    'summary': (f'A practical course in running a legal, honest real estate service business in Kerala: land records, law, documents, '
                f'due diligence, valuation, finance and taxes, then agent registration, sourcing, marketing, sales, transactions, rentals, '
                f'NRI property care, development, investing, tech and fraud prevention, ending with a first real deal or a full business plan. '
                f'Low-capital paths first; rules dated and marked "check current rules". Part-time: {FINAL} weeks at about 5 to 6 hours a week. '
                f'Full-time: about {len(extras.full_time_rows())} weeks.'),
    'language': 'en',
    'updated': common.VDATE,
    'totalWeeks': FINAL,
    'paces': [
        {'id': 'part-time', 'label': 'Part-time', 'hoursPerWeek': 6, 'weekLength': 1,
         'note': f'Alongside PSC study or a job: {FINAL} weeks at about 5 to 6 hours a week'},
        {'id': 'full-time', 'label': 'Full-time', 'hoursPerWeek': 15, 'weekLength': extras.FULL_TIME_WEEK,
         'note': f'About {len(extras.full_time_rows())} calendar weeks at about 15 hours a week. The capstone deal still needs real calendar time.'},
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
