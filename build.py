"""Assemble the social media marketing course JSON from the module files.

Usage: python3 build.py [--out PATH]
"""
import importlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import common  # noqa: E402

OUT = '/home/claude/vidhyarambham/public/courses/social-media-marketing.json'
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
    'id': 'social-media-marketing',
    'version': 1,
    'title': 'Practical Social Media Marketing: Grow an Account, Run Campaigns, Get Clients',
    'summary': 'Grow a real account with measured results, run a real campaign for a local business, and finish with a portfolio, a service package and a price sheet, using free tools on an Android phone. Malayalam and English, Kerala examples, rupee numbers and copy-ready templates throughout. Part-time: 40 weeks at about 6 hours a week. Full-time: about 14 weeks.',
    'language': 'en',
    'updated': common.VDATE,
    'totalWeeks': 40,
    'paces': [
        {'id': 'part-time', 'label': 'Part-time', 'hoursPerWeek': 6, 'weekLength': 1,
         'note': 'Alongside PSC prep or a job: 40 weeks at about 6 hours a week'},
        {'id': 'full-time', 'label': 'Full-time', 'hoursPerWeek': 17, 'weekLength': 0.35,
         'note': 'About 14 calendar weeks at about 17 hours a week, posting every day. Real-day projects keep their length; see the weekly schedule.'},
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
