"""Course-level sections: start here, schedule, week 0, capstone milestones,
final checklist, what next, glossary and the sources page."""
from common import R, STATUS, VDATE, link, rules, fence, bullets, numbered, mistakes_list, use

MODULE_MAP = [
    (1, 'Founder foundations', 'Learn what founders really do, choose a path, set money and time limits', 'Founder Fit Sheet'),
    (2, 'Problems and ideas', 'Collect 20 real problems, turn them into ideas, score and choose one', 'Idea shortlist and test hypothesis'),
    (3, 'Customer discovery', 'Interview at least 10 people who have the problem', 'Customer discovery report, persona, job statements'),
    (4, 'Validation and MVP', 'Map the business, run smoke tests and pre-sales, deliver a no-code MVP', 'Validation evidence pack and go / pivot / stop decision'),
    (5, 'Business models and pricing', 'Pick a revenue model, work out profit per sale, set prices', 'Offer sheet: value proposition, unit economics, price list'),
    (6, 'Marketing', 'Position and brand the business, post useful content, get found locally', 'Marketing kit and live profiles'),
    (7, 'Sales', 'Build a pipeline, use scripts, handle objections, close', 'Sales kit and your first paying customers'),
    (8, 'Money and finance', 'Keep books, forecast cash, find break-even, learn tax basics and funding', 'Finance sheet'),
    (9, 'Legal and compliance', 'Choose a structure, register what you need, use simple agreements', 'Compliance checklist and legal pack'),
    (10, 'Operations and systems', 'Write SOPs, run stock, delivery and customer service, automate', 'Operations manual v1'),
    (11, 'AI for entrepreneurs', 'Use free AI tools for research, content, support and operations, safely', 'AI playbook'),
    (12, 'Growth and scaling', 'Keep customers, track KPIs, delegate and decide when to scale', 'KPI dashboard and growth plan'),
    (13, 'Resilience and ethics', 'Make good decisions, handle failure, avoid burnout and scams', 'Founder operating rules'),
    (14, 'Capstone: launch', 'Plan and run your launch, win paying customers, write your plan and pitch', 'Launch report, one-page business plan, pitch'),
]

MILESTONES = [
    (4, 'Milestone 1: one idea chosen, with a test hypothesis and a kill signal', 'Hypothesis paragraph in the Ideas tab', 'Module 2'),
    (7, 'Milestone 2: 10 real conversations with people who have the problem', 'Tagged notes for 10 or more interviews', 'Module 3'),
    (10, 'Milestone 3: first money or a clear answer', 'At least 3 pre-orders, deposits or paid trials, or a written pivot or stop decision', 'Module 4'),
    (12, 'Milestone 4: your offer and price shown to at least 20 potential customers', 'Price test log with 20 or more people', 'Module 5'),
    (15, 'Milestone 5: customers can find you', 'WhatsApp Business profile plus one public listing or page, with real reviews or posts', 'Module 6'),
    (18, 'Milestone 6: 50 sales conversations logged, with paying customers who are not friends or family', 'Pipeline in the Customers tab', 'Module 7'),
    (21, 'Milestone 7: every rupee in and out recorded for 4 weeks', 'Cash book and your first monthly P&L', 'Module 8'),
    (23, 'Milestone 8: the registrations your business needs are done or applied for', 'Compliance checklist with dates and receipts', 'Module 9'),
    (26, 'Milestone 9: your top 3 repeated jobs have SOPs, and one is automated or delegated', 'SOP documents and a time-saved note', 'Modules 10–11'),
    (29, 'Milestone 10: monthly KPI review done, with at least one repeat or referred customer', 'KPI dashboard and review notes', 'Modules 12–13'),
    (32, 'Milestone 11: launch done, with 10 paying customers in total or your own written target', 'Launch report, one-page plan and 90-day plan', 'Module 14'),
]

TOOLKIT = [
    ('ent-final-idea', 'Chosen idea, with its test hypothesis and the reasons you chose it', 'Module 2'),
    ('ent-final-evidence', 'Validation evidence: interview notes, experiment log and pre-sales or payments', 'Modules 3–4'),
    ('ent-final-plan', 'One-page business plan, updated with your launch numbers', 'Module 14'),
    ('ent-final-brand', 'Brand kit and live profiles (WhatsApp Business, Google or Instagram)', 'Module 6'),
    ('ent-final-offer', 'Offer sheet: value proposition, unit economics and price list', 'Module 5'),
    ('ent-final-scripts', 'Sales scripts, objection playbook and pipeline', 'Module 7'),
    ('ent-final-finance', 'Finance sheet: cash book, P&L, break-even and 13-week cash forecast', 'Module 8'),
    ('ent-final-compliance', 'Compliance checklist with the status of every registration and licence', 'Module 9'),
    ('ent-final-launch', 'Launch plan and launch report', 'Module 14'),
]


def _lessons(modules):
    for m, mod in modules:
        yield m, mod.MODULE, mod.LESSONS


def total_hours(modules):
    h = 3 + 2  # week 0 and the final checklist
    for _, overview, _lessons_ in _lessons(modules):
        h += overview['hours']
    return h


def week_plan(modules):
    """Return {week: (items, hours)} at part-time pace."""
    plan = {0: (['Week 0: set up your free founder toolkit'], 3)}
    for m, overview, lessons in _lessons(modules):
        for s in lessons:
            a, b = s['weeks']
            for w in range(a, b + 1):
                items, hrs = plan.get(w, ([], 0))
                items.append(s['title'])
                plan[w] = (items, hrs + s['hours'] / (b - a + 1))
        project_hours = overview['hours'] - sum(s['hours'] for s in lessons)
        w = overview['weeks'][1]
        items, hrs = plan.get(w, ([], 0))
        items.append(f"Module {m} project and rubric")
        plan[w] = (items, hrs + project_hours)
    for w, title, _, _ in MILESTONES:
        if w in plan:
            items, hrs = plan[w]
            items.append(title.split(':')[0] + ' due')
    if 32 in plan:
        items, hrs = plan[32]
        items.append('Final checklist')
        plan[32] = (items, hrs + 2)
    return plan


def start_section(modules):
    total = total_hours(modules)
    toolkit_rows = '\n'.join(f'| {item} | {where} |' for item, where in [
        ('Chosen idea with a test hypothesis', 'Module 2'),
        ('Validation evidence: interviews, experiments, pre-sales', 'Modules 3–4'),
        ('Offer: value proposition, unit economics, price list', 'Module 5'),
        ('Brand and marketing kit', 'Module 6'),
        ('Sales scripts, objection playbook and pipeline', 'Module 7'),
        ('Finance sheet: cash book, P&L, break-even, cash forecast', 'Module 8'),
        ('Compliance checklist and legal pack', 'Module 9'),
        ('Operations manual (SOPs) and AI playbook', 'Modules 10–11'),
        ('KPI dashboard and growth plan', 'Module 12'),
        ('Founder operating rules', 'Module 13'),
        ('Launch plan, launch report, one-page business plan and pitch', 'Module 14'),
    ])
    weeks_of = {m: ov['weeks'] for m, ov, _ in _lessons(modules)}
    map_rows = []
    for m, name, does, output in MODULE_MAP:
        w = weeks_of.get(m)
        wl = '' if not w else (f'{w[0]}' if w[0] == w[1] else f'{w[0]}–{w[1]}')
        map_rows.append(f'| {m}. {name} | {wl} | {does} | {output} |')
    content = f"""
## What this course is

A free, practical course for starting a small, profitable business in Kerala with almost no money. It follows the methods taught by Y Combinator's Startup School, Steve Blank's customer development and the Lean Startup: talk to customers, test cheaply, sell before you build, and let evidence decide. Every lesson ends with a real task in your area or online, so by the end you will have done the work, not just read about it.

It is written for a beginner near Kuttiady in Kozhikode district who is preparing for Kerala PSC exams, has an Android phone, an old laptop and no business budget, and wants to use AI tools. It works just as well for anyone in a similar situation.

## By the end you will have

- A tested idea, backed by at least 10 customer conversations and real pre-orders or payments
- A launched micro-business with paying customers (the target is 10)
- Your founder toolkit, built one module at a time:

| Toolkit item | Built in |
| --- | --- |
{toolkit_rows}

## How long it takes

| Pace | Calendar time | Hours a week | Total work |
| --- | --- | --- | --- |
| Part-time (the default) | Week 0, then 32 weeks: about 7.5 months | About 6 | About {total} hours |
| Full-time | About 8 weeks | About 24 | About {total} hours |

Pick your pace and start date on the course page. The app then shows which week you are in and what is due. The hours are honest estimates; talking to customers often takes longer than you expect, so leave some slack.

## How each lesson works

Every lesson has the same parts, in this order:

1. **ID, title, outcome and time** at the top of the page
2. **Core lesson:** one framework, explained simply
3. **Local example:** the framework applied to a Kerala business, with rupee numbers
4. **Free resources:** exactly what to study, how long it takes and when the link was checked
5. **Action task:** real work in your area or online, and the **proof to record**
6. **Template:** a copy-ready script, sheet or checklist
7. **Common mistakes** and how to avoid them
8. **Quiz:** 4 or 5 questions, with the answers at the very bottom
9. **Progress checklist:** the ticks under **Your tasks**

Each module starts with an overview page: outcomes, total time, the module project, a self-assessment rubric and a "short on time?" minimum version.

## How to use the app for this course

- Tick each task under **Your tasks** when it is done. Ticks are saved on this phone, so save a backup now and then from **Backup and courses**.
- Paste the link to your proof (a Google Drive file, sheet or photo) into the task's note.
- **This week**, on the course page, lists what is due, plus one capstone milestone at a time.
- Exam coming? Switch to exam mode (about 1 hour a week; see ENT-M01-L03) and move your start date later so the schedule matches. Your ticks are kept.

## Module map

| Module | Part-time weeks | What you do | Output for your toolkit |
| --- | --- | --- | --- |
{chr(10).join(map_rows)}

## Key assumptions

These decisions were made for you when the course was written. Change them if your situation is different.

1. You start part-time, about 6 hours a week next to PSC study. The full-time pace does the same work in about 8 weeks.
2. Learning costs ₹0. The business budget is your own risk limit, set in ENT-M01-L03; most learners need ₹2,000–₹10,000 for the first three months.
3. You work mainly on an Android phone and use the laptop for spreadsheets and longer writing.
4. Your business path is not decided yet. Module 1 helps you choose between freelancing → agency, a local business, digital products and online services.
5. The people and businesses in the examples (Arun, Nisha, Fathima, Meera and others) are made up. Their numbers are illustrative, so always check real local prices.
6. Laws, schemes, fees and limits were checked on 24 October 2026, and they change often. Anything marked **check current rules** links to the official source; check it before you act.
7. Nothing here is legal, tax or financial advice. Use a chartered accountant, tax practitioner or lawyer for filings, contracts and loans.
8. Every resource is free. A few need a free sign-up (Udacity, HubSpot, LEANSpark, NCFE).
9. Explanations are in simple English. Key scripts and the glossary include Malayalam.

## Honest odds

Most new businesses don't last. In the best long-run data available, from the US Bureau of Labor Statistics, about half of the new business establishments that opened in 2014 had closed within five years. This course can't remove that risk, but it shrinks it: you spend little until customers pay, and you decide in advance which results mean change course or stop. ENT-M01-L01, Module 4 and Module 13 cover when not to start, when to pivot and when to stop.

## The running examples

- **Arun's ShopAssist** (freelance → agency): sets up WhatsApp Business and Google Business Profiles for shops in Kuttiady and Vatakara.
- **Nisha's Oven** (local business): home-made cakes and snacks in Kuttiady, ordered on WhatsApp.
- **Fathima's PSC Sprint** (digital product): original Kerala PSC practice packs and weekly mock tests.
- **Meera's CV Makeover** (online service): a fixed-price CV and LinkedIn rewrite for nurses and engineers applying for Gulf jobs.
"""
    return {
        'id': 'ent-start',
        'title': 'Start here: how this course works',
        'kind': 'intro',
        'summary': 'What you will build, how long it takes, how every lesson works, and the assumptions behind the course.',
        'content': content.strip(),
    }


def schedule_section(modules):
    plan = week_plan(modules)
    rows = ['| Week | What you do | Hours |', '| --- | --- | --- |']
    for w in sorted(plan):
        items, hrs = plan[w]
        rows.append(f"| {w} | {'; '.join(items)} | {hrs:.0f} |")
    names = {m: name for m, name, _, _ in MODULE_MAP}
    mod_weeks = {m: ov['weeks'] for m, ov, _ in _lessons(modules)}
    ft = ['| Calendar week | Course weeks | Focus | Hours |', '| --- | --- | --- | --- |']
    for c in range(1, 10):
        a, b = 4 * (c - 1), min(4 * c - 1, 32)
        if a > 32:
            break
        focus = [f'Module {m}: {names[m]}' for m, (s, e) in sorted(mod_weeks.items()) if s <= b and e >= a]
        if a == 0:
            focus.insert(0, 'Week 0 setup')
        if b >= 32:
            focus.append('final checklist')
        hrs = sum(plan.get(w, ([], 0))[1] for w in range(a, b + 1))
        ft.append(f"| {c} | {a}–{b} | {'; '.join(focus)} | {hrs:.0f} |")
    content = f"""
## Part-time: about 6 hours a week

One course week is one calendar week. This is the default pace on the course page.

{chr(10).join(rows)}

## Full-time: about 24 hours a week

Four course weeks every calendar week. Choose **Full-time** on the course page and the app counts the weeks for you. Talking to customers and waiting for replies take calendar time, so keep at least half of each day for real-world work: interviews, sales visits, deliveries.

{chr(10).join(ft)}

The ninth calendar week only holds the last course week, so the full-time pace takes about 8 weeks.

## A daily rhythm that fits around PSC study

- **Weekdays:** 45 minutes after your PSC study block, not before it, so the exam keeps your best hours.
- **Saturday:** 1 hour to plan the week and prepare content.
- **Sunday:** 2 hours with customers: interviews, sales visits, deliveries.
- **Sunday evening:** a 15-minute review. What did I do? What did I learn? What is next?

## When you fall behind

- **This week** shows earlier open tasks as overdue. Do the action tasks first; readings can wait.
- More than two weeks behind? Set a new start date on the course page so the weeks match your real progress. Your ticks are kept.
- Use each module's "short on time?" version when you need it.
- In the 4 weeks before a PSC exam, switch to exam mode: reply to customers and keep records, nothing new.
"""
    return {
        'id': 'ent-schedule',
        'title': 'Weekly schedule: part-time and full-time',
        'kind': 'reference',
        'summary': 'What to do each week at both paces, plus a daily rhythm that fits around PSC study.',
        'content': content.strip(),
    }


WORKBOOK_HEADERS = """
Ideas:
No,Date,Who has it,Problem statement,How often,Pain (1-5),Current workaround,Do they pay now? (amount),Source

Interviews:
Code,Date,Who (role and place),Had the problem in the last month? (Y/N),How often,Last-time story (facts),What they did,What it cost (time or money),Pays for a workaround now? (amount),Best quote,Commitment offered,Tags,My own thoughts

Experiments:
Date,Experiment,Assumption tested,Success criterion,People reached,Replies,Sign-ups,Payments,Result,Decision

Customers:
Code,Name,Phone (with consent),Source,Stage,Last contact,Next step,Next date,Offer,Value (Rs),Paid (Rs),Notes

Cashbook:
Date,Description,Category,Money in (Rs),Money out (Rs),Mode (UPI/cash/bank),Receipt link,Balance

Unit economics:
Item,Amount per unit (Rs),Notes

KPIs:
Week,Orders or sales,Revenue (Rs),Contribution (Rs),New customers,Repeat customers,Conversations,Conversion %,Cash in bank (Rs),Notes

Compliance:
Item,Needed? (Y/N),How to get it,Cost,Official link,Status,Renewal date
"""

COACH_PROMPT = """
You are my small-business coach. I live near Kuttiady,
Kozhikode, Kerala, and I am a beginner. I am taking a
practical entrepreneurship course and have about 6 hours
a week. Rules for you:
1. Ask me one question at a time.
2. Push me to talk to real customers instead of guessing.
3. Use rupee examples and Kerala context.
4. If you are not sure about a law, scheme or number,
   say so and tell me to check the official source.
5. Don't write my answers for me unless I ask.
Today I am working on: [lesson ID and task].
"""


def setup_section():
    content = f"""
Week 0 takes about 3 hours. You set up free tools once, so every lesson after this has a place to save its work. Everything works on an Android phone; the laptop helps with spreadsheets.

## 1. A Founder Toolkit folder in Google Drive

Make a folder called **Founder Toolkit** with these subfolders: 01 Founder, 02 Ideas, 03 Interviews, 04 Validation, 05 Offer, 06 Marketing, 07 Sales, 08 Money, 09 Legal, 10 Operations, 11 AI, 12 Growth, 13 Founder rules, 14 Launch. Every lesson's proof goes into one of them. When a task asks for proof, copy the file's link and paste it into that task's note in this app.

## 2. The Founder Workbook

Make one Google Sheets file called **Founder Workbook**, with eight tabs: Ideas, Interviews, Experiments, Customers, Cashbook, Unit economics, KPIs and Compliance. Put each tab's header row (below) in row 1. Lessons give you the same rows again when you need them.

- **On the laptop:** copy a header line, paste it into cell A1, then choose Data → Split text to columns.
- **On the phone:** type the headings into row 1, or do this step once on the laptop.

{fence(WORKBOOK_HEADERS, 'csv')}

## 3. WhatsApp Business

{link('wa-business', 'WhatsApp Business')} is free to download and gives you a business profile, a product catalogue, quick replies, labels and away messages. A separate number for the business is best; a second SIM and its recharges are a running cost, so count them in your risk limit. If you move your personal number to WhatsApp Business, back up your chats first and follow the steps in the app. You will set up the profile properly in ENT-M06-L01; for now, install it or decide which number you will use.

## 4. Canva (free plan)

Use Canva for posts, posters and price lists. Read the {link('canva-license')} once: you may use its free photos and graphics in posts, ads and printed material, but not in your logo, trademark or business name.

## 5. Office tools on the old laptop

Google Sheets and Docs work in the browser. {link('libreoffice')} works offline and is free and open source. {link('gnucash')} is optional for bookkeeping later; it runs on the laptop, not on Android. Keep the laptop light: one browser, few tabs, few extensions.

## 6. An AI assistant as your coach

The free plans of {link('gemini-plans', 'Gemini')}, {link('chatgpt-plans', 'ChatGPT')} and {link('claude-plans', 'Claude')} are enough for this course (limits change; check current rules). Save this prompt and paste it at the start of a session:

{fence(COACH_PROMPT)}

Never paste customers' names, phone numbers or private details into an AI tool. For example, Google's {link('gemini-api-terms', 'Gemini API terms')} say that on free tiers your inputs may be used to improve Google's products and may be read by human reviewers.

## 7. Calendar and an accountability buddy

Block your weekly business slots in Google Calendar (you will fine-tune them in ENT-M01-L03). Choose an accountability buddy: a friend who is also building something, or a family member who will ask you every Sunday, "What did you do this week?"
"""
    tasks = [
        ('ent-w0-folder', 'Founder Toolkit folder made in Google Drive, with its 14 subfolders'),
        ('ent-w0-workbook', 'Founder Workbook made, with all 8 tabs and their header rows'),
        ('ent-w0-whatsapp', 'WhatsApp Business installed, or the business number decided'),
        ('ent-w0-canva', 'Canva free account ready and the free media licence read'),
        ('ent-w0-ai', 'AI coach prompt saved and tried once'),
        ('ent-w0-calendar', 'Weekly slots in your calendar and an accountability buddy chosen'),
    ]
    return {
        'id': 'ent-w0',
        'title': 'Week 0: set up your free founder toolkit',
        'kind': 'setup',
        'weeks': [0, 0],
        'hours': 3,
        'summary': 'Free tools, one Drive folder and one workbook, so every lesson has a place to save its work.',
        'content': content.strip(),
        'tasks': [{'id': i, 'text': t, 'kind': 'task', 'week': 0} for i, t in tasks],
    }


def milestones_section():
    rows = ['| Due by week | Milestone | Evidence | Built in |', '| --- | --- | --- | --- |']
    for w, title, ev, where in MILESTONES:
        t = title.split(': ', 1)[1]
        rows.append(f'| {w} | {t[0].upper() + t[1:]} | {ev} | {where} |')
    content = f"""
The capstone is your real business. It doesn't wait until the end: it runs alongside every module, and each milestone is a real-world result, not a document. **This week** on the course page shows one milestone at a time, from the week after the previous one until its due week.

{chr(10).join(rows)}

## How to use the milestones

- Tick a milestone only when the evidence exists, and paste a link to it in the milestone's note.
- Missing a milestone is information, not failure. Ask why: the wrong customer, the wrong offer, the wrong channel, or not enough attempts? Then adjust and try again before the next milestone.
- If Milestone 3 shows no real demand after two honest tests, use the go / pivot / stop decision in ENT-M04-L04 before you go further. It is cheaper to change course in week 10 than in week 30.

## Why "first money" comes so early

Pre-orders, deposits and paid trials in Module 4 are the strongest evidence that your idea works. They also mean your first revenue usually arrives around week 9 or 10, long before the formal launch in Module 14.
"""
    return {
        'id': 'ent-milestones',
        'title': 'Capstone milestones: your real business, step by step',
        'kind': 'track',
        'weeks': [1, 32],
        'summary': 'Eleven real-world milestones, from choosing an idea to a launch with paying customers. One shows in "This week" at a time.',
        'content': content.strip(),
        'tasks': [
            {'id': f'ent-ms-{i:02d}', 'text': title, 'kind': 'project', 'week': w,
             'detail': f'**Evidence:** {ev}. Paste the link to it in this note.'}
            for i, (w, title, ev, _) in enumerate(MILESTONES, 1)
        ],
    }


def front(modules):
    return [start_section(modules), schedule_section(modules), setup_section(), milestones_section()]


# ---------------------------------------------------------------- back matter

def final_section():
    rows = ['| Toolkit item | Where the template is |', '| --- | --- |'] + [f'| {t} | {where} |' for _, t, where in TOOLKIT]
    content = f"""
Go through this list at the end of the course. Each item should be a file in your Founder Toolkit folder that you could show a bank manager, a partner or a mentor tomorrow. If something is missing, the module listed has its template.

{chr(10).join(rows)}

## Before you call the course done

- Save a backup of your progress from **Backup and courses** in this app, and keep it in your Founder Toolkit folder.
- Download a copy of your Founder Workbook (File → Download) so you have it offline.
- Put your next Sunday review in your calendar. The course ends; the weekly rhythm doesn't.
"""
    return {
        'id': 'ent-final',
        'title': 'Final checklist: your founder toolkit',
        'kind': 'capstone',
        'weeks': [32, 32],
        'hours': 2,
        'summary': 'Check that every part of your toolkit exists, is up to date and is saved where you can find it.',
        'content': content.strip(),
        'tasks': [{'id': i, 'text': t, 'kind': 'task', 'week': 32} for i, t, _ in TOOLKIT],
    }


def next_section():
    content = f"""
Finishing the course is the start of the real work. Here is a sensible order for the next twelve months.

## The next 90 days: steady

- Keep the weekly rhythm: Sunday review, KPI dashboard, follow-ups with every open lead.
- Aim for a steady monthly profit, then your next target: the business paying your survival number from ENT-M01-L03, which is "ramen profitable".
- Ask every customer for feedback and a referral, and track your repeat customers.

## Months 4–6: solid

- Formalise what you need: a bank current account, Udyam registration if not done, GST when you near the threshold or a compulsory case applies, and the licences your activity needs (check current rules).
- Write an SOP for everything you repeat, and delegate one more task.
- Review your prices every three months, using your unit economics sheet.

## Months 7–12: choose how to grow

| If your numbers show | Consider |
| --- | --- |
| More demand than you can meet | More capacity: equipment, a helper or a partner |
| Steady profit from one customer group | A second group, or a nearby town |
| Clients asking for the same thing again and again | A fixed-price package, then a digital product |
| A tech-based idea that could grow fast | {link('ksum', 'KSUM')} programmes, {link('startupindia', 'Startup India')} recognition and the full {link('yc-ss', 'YC Startup School')} course |
| No growth after three honest tries | A pivot (ENT-M13-L01) or a backup idea from Module 2 |

## Keep learning, free

- {link('yc-ss')}: the full course, about 7 weeks at 1–2 hours a week
- {link('mit-390')}: the remaining lectures, and {link('mit-s21', 'MIT 15.S21 on business plans')}
- {link('os-book')}: chapters you skipped, especially 12 (networks and teams) and 14 (resources)
- {link('blank-udacity')}: the lessons you haven't done
- {link('hubspot-sales')} and {link('hubspot-content')}, with their free certificates
- The **Free AI Generalist Course** in this app, to add AI services or automation to your business

## Where to get help in Kerala

- {link('kerala-dic', 'District Industries Centre')} and your Taluk Industries Office: schemes, project reports and {link('kerala-clinic', 'MSME Clinic')} experts
- {link('kied')}: entrepreneurship programmes
- {link('ksum', 'Kerala Startup Mission')}: incubation, grants and events for tech and innovation startups
- {link('kudumbashree')}: support and markets for women's micro-enterprises
- Your bank's MSME desk, for Mudra and other loans (check current rules)
"""
    return {
        'id': 'ent-next',
        'title': 'What next: your 12-month roadmap',
        'kind': 'reference',
        'summary': 'How to keep going after the course: steady, then solid, then grow, with free resources and local help.',
        'content': content.strip(),
    }


GLOSSARY = [
    ('Entrepreneur', 'സംരംഭകൻ / സംരംഭക', 'A person who starts and runs a business and takes the risk'),
    ('Startup', 'സ്റ്റാർട്ടപ്പ് (പുതുസംരംഭം)', 'A new company built to grow fast, often with investors'),
    ('Micro-enterprise', 'സൂക്ഷ്മ സംരംഭം', 'A very small business; Udyam sets the official limits'),
    ('Customer', 'ഉപഭോക്താവ്', 'The person who buys from you'),
    ('Early adopter', 'ആദ്യകാല ഉപഭോക്താവ്', 'One of the first, most eager customers, who feels the problem most'),
    ('Problem statement', 'പ്രശ്ന പ്രസ്താവന', 'A sentence saying who has what problem and what it costs them'),
    ('Hypothesis', 'അനുമാനം', 'A guess you can prove wrong with a test'),
    ('Customer interview', 'ഉപഭോക്തൃ അഭിമുഖം', 'A short talk about a customer\'s real past behaviour'),
    ('Persona', 'ഉപഭോക്തൃ മാതൃക', 'A profile of a typical customer, built from interviews'),
    ('Job to be done', 'നിറവേറ്റേണ്ട ആവശ്യം', 'The progress a customer wants to make in a situation'),
    ('Value proposition', 'മൂല്യ വാഗ്ദാനം', 'Why a customer should choose you, in one clear sentence'),
    ('MVP (minimum viable product)', 'ഏറ്റവും ചെറിയ പ്രവർത്തന പതിപ്പ്', 'The smallest version that delivers the core value'),
    ('Prototype', 'മാതൃക', 'An early model used to test an idea'),
    ('Validation', 'സാധൂകരണം', 'Evidence that customers want your offer and will pay for it'),
    ('Pre-order', 'മുൻകൂർ ഓർഡർ', 'A customer pays or commits before the product is ready'),
    ('Pivot', 'ദിശ മാറ്റൽ', 'Changing one big part of the plan because of evidence'),
    ('Revenue', 'വരുമാനം', 'All the money customers pay you'),
    ('Profit', 'ലാഭം', 'What is left after all costs'),
    ('Loss', 'നഷ്ടം', 'When costs are more than revenue'),
    ('Fixed cost', 'സ്ഥിര ചെലവ്', 'A cost that stays the same each month, like rent'),
    ('Variable cost', 'മാറുന്ന ചെലവ്', 'A cost that rises with each sale, like ingredients'),
    ('Contribution margin', 'ഓരോ വിൽപനയിലെയും മിച്ചം', 'Price minus variable cost, for one unit'),
    ('Unit economics', 'ഒരു വിൽപനയുടെ ലാഭനഷ്ടക്കണക്ക്', 'Revenue, cost and profit for one sale or one customer'),
    ('Break-even', 'ലാഭവും നഷ്ടവും ഇല്ലാത്ത നില', 'The sales level where revenue just covers all costs'),
    ('Cash flow', 'പണമൊഴുക്ക്', 'Money coming in and going out over time'),
    ('Working capital', 'പ്രവർത്തന മൂലധനം', 'Money needed for day-to-day running: stock, credit, bills'),
    ('Capital', 'മൂലധനം', 'Money put into the business'),
    ('Bootstrapping', 'സ്വന്തം വരുമാനത്തിൽ വളർത്തൽ', 'Growing with your own money and customers\' money'),
    ('Runway', 'പിടിച്ചുനിൽക്കാവുന്ന കാലം', 'How many months your money will last'),
    ('Risk limit', 'നഷ്ടപരിധി', 'The most money and time you will risk'),
    ('Loan', 'വായ്പ', 'Borrowed money you repay with interest'),
    ('Interest', 'പലിശ', 'The cost of borrowing money'),
    ('Collateral', 'ഈട്', 'Property pledged against a loan'),
    ('Subsidy', 'സബ്സിഡി (സഹായധനം)', 'Part of a cost that the government pays'),
    ('Grant', 'ധനസഹായം', 'Money given to you that you don\'t repay'),
    ('Investor', 'നിക്ഷേപകൻ', 'Someone who puts in money for a share of the business'),
    ('Equity (shares)', 'ഓഹരി', 'Part-ownership of a company'),
    ('Bookkeeping', 'കണക്കെഴുത്ത്', 'Recording every rupee in and out'),
    ('Cash book', 'പണപ്പുസ്തകം', 'A daily record of money in and out'),
    ('Invoice', 'ബിൽ (ഇൻവോയ്സ്)', 'A bill you give a customer'),
    ('Receipt', 'രസീത്', 'Proof that someone paid'),
    ('Expense', 'ചെലവ്', 'Money spent to run the business'),
    ('Profit and loss statement (P&L)', 'ലാഭ-നഷ്ട കണക്ക്', 'Revenue minus costs for a month or a year'),
    ('Balance sheet', 'ആസ്തി-ബാധ്യതാ പട്ടിക', 'What the business owns and owes on a date'),
    ('Asset', 'ആസ്തി', 'Something of value the business owns'),
    ('Liability', 'ബാധ്യത', 'Something the business owes'),
    ('Depreciation', 'മൂല്യശോഷണം', 'The fall in value of equipment over time'),
    ('Turnover', 'വിറ്റുവരവ്', 'Total sales in a year'),
    ('Tax', 'നികുതി', 'Money paid to the government on income or sales'),
    ('GST', 'ചരക്ക് സേവന നികുതി', 'Goods and Services Tax, charged on sales once you are registered'),
    ('Presumptive taxation', 'അനുമാന നികുതി', 'A simple scheme where profit is taken as a set percentage of turnover'),
    ('TDS', 'ഉറവിടത്തിൽ നികുതി കിഴിവ്', 'Tax a client deducts before paying you'),
    ('Licence', 'ലൈസൻസ് (അനുമതിപത്രം)', 'Official permission to carry on an activity'),
    ('Registration', 'രജിസ്ട്രേഷൻ', 'Recording your business with an authority'),
    ('Compliance', 'നിയമപാലനം', 'Following the rules that apply to you'),
    ('Sole proprietorship', 'ഏകാംഗ ഉടമസ്ഥത', 'One person owns the business, with unlimited liability'),
    ('Partnership', 'പങ്കാളിത്തം', 'Two or more people own the business under a written deed'),
    ('Limited liability', 'പരിമിത ബാധ്യത', 'Owners\' personal property is protected from the business\'s debts'),
    ('Contract', 'കരാർ', 'A promise between people that the law can enforce'),
    ('Trademark', 'വ്യാപാരമുദ്ര', 'A protected brand name or logo'),
    ('Copyright', 'പകർപ്പവകാശം', 'Ownership of original creative work'),
    ('Consumer rights', 'ഉപഭോക്തൃ അവകാശങ്ങൾ', 'Rights the law gives to buyers'),
    ('Personal data', 'വ്യക്തിഗത വിവരങ്ങൾ', 'Information that identifies a person, such as a phone number'),
    ('Market', 'വിപണി', 'All the people who might buy what you sell'),
    ('Marketing', 'വിപണനം', 'Helping the right people know, like and trust your offer'),
    ('Sales', 'വിൽപന', 'Helping a customer decide and pay'),
    ('Positioning', 'സ്ഥാനനിർണയം', 'The place your business holds in customers\' minds'),
    ('Brand', 'ബ്രാൻഡ്', 'How people recognise and remember your business'),
    ('Pricing', 'വില നിർണയം', 'Deciding what to charge'),
    ('Discount', 'കിഴിവ്', 'A reduction in price'),
    ('Competitor', 'എതിരാളി', 'Another business or option customers could choose'),
    ('Supplier', 'വിതരണക്കാരൻ', 'A business you buy materials from'),
    ('Inventory (stock)', 'ചരക്കുശേഖരം (സ്റ്റോക്ക്)', 'Goods you hold to sell or use'),
    ('SOP (standard operating procedure)', 'പ്രവർത്തന നടപടിക്രമം', 'Written steps for doing a task the same way every time'),
    ('Automation', 'ഓട്ടോമേഷൻ (സ്വയംപ്രവർത്തനം)', 'Letting tools do repeated tasks'),
    ('KPI (key performance indicator)', 'പ്രധാന പ്രകടന സൂചകം', 'A key number you track to see how the business is doing'),
    ('Retention', 'നിലനിർത്തൽ', 'Keeping customers coming back'),
    ('Churn', 'കൊഴിഞ്ഞുപോക്ക്', 'Customers who stop buying'),
    ('Referral', 'ശുപാർശ', 'A customer recommending you to someone else'),
    ('Review', 'അഭിപ്രായം (റിവ്യൂ)', 'A customer\'s public opinion of your business'),
    ('Delegation', 'ചുമതല ഏൽപ്പിക്കൽ', 'Giving a task to someone else to do'),
    ('Scaling', 'വിപുലീകരണം', 'Growing sales faster than costs grow'),
    ('Ethics', 'ധാർമ്മികത', 'Doing business honestly and fairly'),
    ('Scam', 'തട്ടിപ്പ്', 'A trick to take your money or data'),
    ('Burnout', 'അമിതജോലി മൂലമുള്ള തളർച്ച', 'Exhaustion from working too long without rest'),
    ('Pitch', 'അവതരണം (പിച്ച്)', 'A short talk that explains your business and asks for something'),
    ('Business plan', 'ബിസിനസ് പദ്ധതി', 'A written plan for how the business will work and grow'),
]


def glossary_section():
    rows = ['| English | മലയാളം (Malayalam) | Simple meaning |', '| --- | --- | --- |']
    for en, ml, meaning in GLOSSARY:
        rows.append(f'| **{en}** | {ml} | {meaning} |')
    content = f"""
Key words from the course, in the order you are likely to meet them in business conversations. Some English words, such as GST, startup and brand, are used as they are in Malayalam conversation too; the Malayalam is given so you can explain them to customers and family.

{chr(10).join(rows)}
"""
    return {
        'id': 'ent-glossary',
        'title': 'Glossary with Malayalam meanings',
        'kind': 'reference',
        'summary': f'{len(GLOSSARY)} key business terms in English and Malayalam, with simple meanings.',
        'content': content.strip(),
    }


def back(modules):
    return [final_section(), next_section(), glossary_section()]


def finish(course):
    """Add the sources page, built from every link the course actually uses."""
    sections = course['sections']
    used_in = {}
    for s in sections:
        texts = [s.get('content', ''), s.get('summary', '')] + [t.get('detail', '') for t in s.get('tasks', [])]
        blob = '\n'.join(texts)
        code = s['title'].split(':')[0]
        for key, r in R.items():
            if f"]({r['url']})" in blob:
                used_in.setdefault(key, [])
                if code not in used_in[key]:
                    used_in[key].append(code)
    groups = {}
    for key in used_in:
        groups.setdefault(R[key]['group'], []).append(key)
    order = ['Courses and talks', 'OpenStax Entrepreneurship (CC BY-NC-SA 4.0)', 'Frameworks and articles', 'Free tools', 'AI tools', 'Money', 'Government of India', 'Kerala', 'Help and safety', 'Statistics', 'Other']
    parts = [f"""
Every link in this course is listed here with the date it was checked. Links were opened and read on {VDATE}; nothing here was copied from memory. If a link stops working, search for its title on the same website.

- **verified {VDATE}:** the page was opened and its content matched what the course says.
- **check current rules:** a law, scheme, fee or limit that changes often. Open the official source before you act.
- **unverified:** the official site blocks automated checks, so the page could not be opened for this course. The address is the one named by other official sources; type it yourself and check that it is the government site.

OpenStax *Entrepreneurship* is licensed CC BY-NC-SA 4.0 and this course only links to it. Strategyzer's Business Model Canvas may be used with credit to Strategyzer.com, as their usage page explains.
"""]
    for g in order:
        if g not in groups:
            continue
        rows = ['| Resource | Used in | Status |', '| --- | --- | --- |']
        keys = groups[g]
        if g.startswith('OpenStax'):
            keys = sorted(keys, key=lambda k: (k != 'os-book', int(k[2:]) if k[2:].isdigit() else 0))
        for key in keys:
            r = R[key]
            where = ', '.join(used_in[key][:6]) + (' and more' if len(used_in[key]) > 6 else '')
            rows.append(f"| [{r['title']}]({r['url']}) | {where} | {STATUS[r['s']]} |")
        parts.append(f'## {g}\n\n' + '\n'.join(rows))
    unverified = [k for k in used_in if R[k]['s'] == 'u']
    rules_keys = [k for k in used_in if R[k]['s'] == 'vr']
    parts.append('## Marked "unverified"\n\n' + bullets([f"[{R[k]['title']}]({R[k]['url']})" for k in unverified]))
    parts.append('## Marked "check current rules"\n\n' + bullets([f"[{R[k]['title']}]({R[k]['url']})" for k in rules_keys]))
    sections.append({
        'id': 'ent-sources',
        'title': 'Sources and verification log',
        'kind': 'reference',
        'summary': f'Every link in the course, where it is used and when it was checked ({VDATE}).',
        'content': '\n\n'.join(p.strip() for p in parts),
    })
