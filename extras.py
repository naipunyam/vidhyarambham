"""Course-level sections for the Kerala Real Estate Business course."""
from common import (R, STATUS, VDATE, CHECK, ASOF, RULE, GROUP_ORDER, FOLDERS, WEEKS, PROJECT_WEEK,
                    LAST_WEEK, LOAD, TOOLKIT_ITEMS, link, rules, xref, fence, bullets, numbered, table, fmt_hours, code_of)
import plan
import tests
import tools

FULL_TIME_WEEK = 0.4
FINAL = LAST_WEEK


def wk(m, l):
    return WEEKS[(m, l)][0]


def milestones():
    out = [
        ('re-sys-comps10', 'Market study: 10 real listings in your Comps sheet', wk(7, 1), 'the Comps sheet with 10 rows'),
        ('re-sys-comps20', 'Market study: 20+ real listings (land and houses), price per cent and per sq ft', wk(7, 3), 'the Comps sheet with 20+ rows and the summary cells'),
        ('re-sys-fv', 'Fair value looked up on the official portal for 3 properties and compared with asking prices', wk(7, 1) + 1, 'screenshots or notes with dates'),
        ('re-sys-interviews', 'Interviews: 3 local brokers and 1 document writer or advocate', wk(11, 1) + 1, 'your interview notes'),
        ('re-sys-dd', 'Due-diligence checklist run on a real property (with permission) or the sample case', PROJECT_WEEK[6], 'the filled checklist'),
        ('re-sys-roi', 'Rental yield and ROI analysis for 5 real properties', wk(8, 2) + 1, 'the ROI tab with 5 properties'),
        ('re-sys-listing', 'One real listing (with the owner\'s written permission) posted on free portals and social media', PROJECT_WEEK[12], 'the owner\'s permission, the listing links and screenshots'),
        ('re-sys-crm', 'CRM sheet in use: every lead tracked with next action dates', wk(19, 1), 'a CRM screenshot with personal details blurred'),
        ('re-sys-visit', 'A real site visit conducted or shadowed', PROJECT_WEEK[13], 'your site-visit checklist'),
    ]
    for letter, title, a, z in plan.PARTS:
        end = max(PROJECT_WEEK[m] for m in range(a, z + 1))
        if letter != 'C':
            out.append((f're-sys-part-{letter.lower()}', f'Part {letter} review', end, f'half a page on what you learned in Part {letter} and what you will do next'))
    return sorted(out, key=lambda x: x[2])


MODULE_MAP = [
    (1, 'Property types, players, cycles, Kerala demand drivers', 'A local market snapshot'),
    (2, 'Broker, rentals, NRI care, marketing, plotting, investing, flipping', 'Your chosen path with risks'),
    (3, 'Cents, ares, sq ft; survey numbers; thandaper; certificates; portals', 'A land-records walk-through for one plot'),
    (4, 'TPA, Registration Act, stamp duty, RERA, paddy land, land reforms, building rules, CRZ, ESA, rent control, benami, cash limits', 'A one-page legal map'),
    (5, 'Agreement for sale, sale deed, gift, partition, settlement, POA, rental, permits, OC, NOCs', 'Annotated sample documents'),
    (6, 'Title chain, EC, litigation, physical checks, flood and zoning, professionals', 'A full due-diligence run'),
    (7, 'Fair value vs market value, comparables, income and cost methods', '20+ listing comparables sheet'),
    (8, 'Loans, EMI, yield, cap rate, cash-on-cash, IRR, total cost', 'ROI analysis of 5 properties'),
    (9, 'TDS, capital gains, rent tax, GST, brokerage income tax', 'A tax checklist for buyers, sellers and you'),
    (10, 'K-RERA agent registration, mandates, commission, inventory', 'A mandate template and 5 inventory entries'),
    (11, 'Local, NRI, builder and online sourcing; broker interviews', 'Interview notes and a sourcing plan'),
    (12, 'Photos, video, virtual tours, listings, portals, social, WhatsApp, GBP', 'A real listing, live'),
    (13, 'Client needs, site visits, objections, negotiation, closing, token', 'A site visit and a negotiation plan'),
    (14, 'Token to agreement, loans, stamp duty, SRO registration, mutation, handover', 'A transaction timeline'),
    (15, 'Tenant screening, agreements, verification, rent, maintenance, NRI care', 'A rental management package'),
    (16, 'Layouts, conversion, roads, utilities, development risk', 'A development feasibility screen'),
    (17, 'Cost per sq ft, contracts, quality checks, permits', 'A construction cost estimate'),
    (18, 'Rentals, land banking, flipping, REITs, risks', 'An investment comparison'),
    (19, 'CRM in Sheets, Google Earth, QGIS, AI', 'A working CRM and a map of your listings'),
    (20, 'Structure, registration, GST, bookkeeping, pricing, partnerships', 'A one-page business setup plan'),
    (21, 'Fake titles, double sales, forged POAs, encroachment, black money, ethics', 'A fraud checklist and ethics code'),
    (22, 'A first legal deal, or an investment analysis plus business plan', 'Your complete toolkit'),
]

SAFETY = f"""
**This course is educational only. It is not legal, tax or investment advice.** Property law, rates, fees and portals change; every rule in this course is dated "{ASOF}" and marked "{CHECK}". Before any real transaction, check the official source and use licensed professionals: an **advocate** for title opinions and legal disputes, a **licensed surveyor** for measurement and boundary questions, a **chartered accountant** for tax, and a **licensed document writer or advocate** to draft deeds. Never do work that needs a licence you don't hold. This course never recommends a specific property or investment; it teaches you how to evaluate them.
"""


def total_hours():
    return sum(LOAD.values())


def week_plan():
    plan_ = {0: (['Week 0: setup and baseline quiz'], LOAD[0])}

    def add(w, item, hrs):
        items, h = plan_.get(w, ([], 0))
        if item and item not in items:
            items.append(item)
        plan_[w] = (items, h + hrs)

    for m, (title, lessons, ph) in enumerate(plan.MODULES, 1):
        for l, (lt, h) in enumerate(lessons, 1):
            a, b = WEEKS[(m, l)]
            label = code_of(m, l) + ('' if a == b else f' (weeks {a}–{b})')
            for w in range(a, b + 1):
                add(w, label, h / (b - a + 1))
        add(PROJECT_WEEK[m], f'M{m:02d} project', ph)
    for w in range(1, FINAL + 1):
        add(w, '', plan.REVIEW_H)
    add(FINAL, 'final retest and checklist', 1.5)
    return plan_


def full_time_rows():
    rows = []
    c = 1
    while True:
        lo = int((c - 1) / FULL_TIME_WEEK + 0.999) if c > 1 else 0
        hi = min(int(c / FULL_TIME_WEEK - 0.001), FINAL)
        mods = []
        for m in range(1, len(plan.MODULES) + 1):
            ws = [WEEKS[(m, l)] for l in range(1, len(plan.MODULES[m - 1][1]) + 1)]
            s, e = min(x[0] for x in ws), max(max(x[1] for x in ws), PROJECT_WEEK[m])
            if s <= hi and e >= lo:
                mods.append(f'M{m:02d}')
        note = ''
        if c == 1:
            note = 'Week 0 setup and baseline quiz, then Part A.'
        if mods and 'M22' in mods and not note:
            note = 'The capstone needs real calendar time (about a month) for a deal or a full plan.'
        rows.append((str(c), f'{lo}–{hi}', ', '.join(mods) or '—', note))
        if hi >= FINAL:
            break
        c += 1
    return rows


def start_section():
    n_lessons = sum(len(x[1]) for x in plan.MODULES)
    part_rows = []
    for letter, title, a, z in plan.PARTS:
        hrs = sum(sum(h for _, h in plan.MODULES[m - 1][1]) + plan.MODULES[m - 1][2] for m in range(a, z + 1))
        part_rows.append((f'**{letter}: {title}**', f'Modules {a}–{z}', f'{wk(a, 1)}–{max(PROJECT_WEEK[m] for m in range(a, z + 1))}', f'about {round(hrs)} h'))
    content = f"""
## What this course is

A practical course in running a legal, honest real estate service business in Kerala, written for a beginner near Kuttiady, Kozhikode, with an Android phone, an old laptop, ₹0 for learning and very little capital. It focuses first on **low-capital paths**: brokerage, rentals and property management, NRI property care and real estate marketing. Buying property to invest is treated as a later stage.

By the end you will understand how a property deal works from token advance to registration and mutation, be able to do due diligence and valuation, know the main Kerala and central laws, run your service with written agreements, and have either **closed a first real deal** (a rental or a sale) legally, or produced a complete investment analysis and business plan.

## What you will be able to do

- Convert cents, ares and square feet; read survey numbers, thandaper, certificates, EC and deeds.
- Explain the main laws (Transfer of Property Act, Registration Act, stamp duty, RERA, paddy land, land reforms, building rules, CRZ, ESA, rent control, benami, cash limits) and when each matters.
- Run a full due-diligence checklist and know exactly when to bring in an advocate or surveyor.
- Value property with comparables, fair value and income methods; calculate the full cost of buying, rental yield, cap rate, cash-on-cash and IRR.
- Understand TDS, capital gains, rental income tax and GST at the level a broker needs (and when to call a CA).
- Register as an agent if required, take written mandates, source, market, negotiate and manage transactions and rentals.
- Spot the common frauds in Kerala and protect your clients.

## Duration

- **{len(plan.MODULES)} modules, {n_lessons} lessons** in three parts; lessons take 10 to 25 minutes to read, plus a real-world task in your local market.
- **Part-time:** {FINAL} weeks at about 5 to 6 hours a week (about {round(total_hours())} hours), alongside PSC preparation.
- **Full-time:** about {len(full_time_rows())} calendar weeks at about 15 hours a week. The capstone deal needs real calendar time.

## The three parts

Each part works on its own; its part page says what to set up if you start there.

{table(['Part', 'Modules', 'Part-time weeks', 'Study time'], part_rows)}

## How every lesson works

Core lesson with a Kozhikode or Kerala example → worked calculation where numbers matter → key rules with the date checked and the source → when you need a licensed professional → free resources (what to study, how long) → an action task in your local market with proof → a copy-ready template → common mistakes → a local fraud warning → a short quiz with answers → a progress checklist. Each module has a project, a rubric, a "short on time" version, flashcards and tools for your **Real Estate Toolkit**.

## Legal, accuracy and ethics

{SAFETY.strip()}

**Ethics rules you follow in every task:** act only with the owner's consent (written for listings); never misrepresent a property; follow K-RERA rules; avoid cash and black-money dealings; respect clients' privacy (blur ID numbers and phone numbers in anything you share).

**Honest risk warning:** property is illiquid (it can take months or years to sell), legal disputes are common and slow, prices can stagnate or fall, and many small investors lose money through bad titles, unapproved layouts, over-borrowing and fraud. This course shows you how to reduce those risks, not how to avoid them completely.

## Key assumptions made for this course

- No real estate course existed in the app, so this is a new course with stable IDs (RE-M01-L01 and so on).
- You will start with a service business (brokerage, rentals, NRI care, marketing) and treat buying to invest as later.
- Rates and rules were checked on {VDATE}; the Kerala Registration, Revenue and Ente Bhoomi portals block automated checks, so for them the course gives the official addresses and cross-checks details with secondary guides, clearly marked.
- From 1 April 2026 the Income-tax Act, 2025 replaced the 1961 Act, and many section numbers changed; the course explains tax rules by what they do and names old and new numbers only where checked.
- Topics covered by other courses in this app are cross-referenced: sales skills in {xref('ent', 'ent-m07', 'Entrepreneurship')}, social media in {xref('smm', 'smm-m11', 'Social Media Marketing')}, and investing basics in {xref('fin', 'fin-m08', 'Personal Finance')}.
- All names in examples are fictional.

## The course map

{table(['Module', 'What it covers', 'What you build'], [(f'M{m:02d}', what, build) for m, what, build in MODULE_MAP])}

## Start here

1. Read the **Weekly schedule**.
2. Do **Week 0: setup** (about 1 hour) and the **Baseline quiz** (20 minutes).
3. Start Module 1 in week 1 and the **Weekly market track** (20 minutes every Sunday).
"""
    return {'id': 're-start', 'title': 'Start here: Kerala Real Estate Business', 'kind': 'intro',
            'summary': f'What the course covers, how it works, the legal and ethics rules, and the course map. {len(plan.MODULES)} modules, {n_lessons} lessons, {FINAL} weeks part-time.',
            'content': content.strip()}


def schedule_section():
    wp = week_plan()
    rows = []
    for w in range(0, FINAL + 1):
        items, h = wp.get(w, ([], 0))
        part = ''
        for letter, title, a, z in plan.PARTS:
            if wk(a, 1) == w:
                part = f'**Part {letter} starts.** '
        rows.append((str(w), part + (', '.join(items) or 'catch-up week'), f'{h:.1f}'))
    content = f"""
The app's **This week** view follows the part-time schedule. If you study full-time, switch the pace to **Full-time** on the course page.

## Part-time schedule (about 5 to 6 hours a week)

{table(['Week', 'Lessons and projects', 'Hours'], rows)}

## A typical part-time week

- Two or three lesson evenings after PSC study.
- **Saturday or Sunday morning:** the field task (a site visit, an office visit, a broker interview, photographing a property). Village and sub-registrar offices work on weekdays, so plan office visits for a weekday morning when you can.
- **Sunday:** the 20-minute weekly market log.

## Full-time schedule (about 15 hours a week)

{table(['Calendar week', 'Course weeks', 'Modules', 'Notes'], full_time_rows())}
"""
    return {'id': 're-schedule', 'title': 'Weekly schedule: part-time and full-time', 'kind': 'reference',
            'summary': f'{FINAL} weeks part-time at about 5 to 6 hours, or about {len(full_time_rows())} weeks full-time.',
            'content': content.strip()}


def setup_section():
    tabs = table(['Tab', 'Added in', 'Row 1 headings or contents'], [
        ('Units', 'Module 3', 'Area conversion formulas'),
        ('Comps', 'Module 7 (start collecting listings in week 1)', '`' + tools.COMPS_HEADER + '`'),
        ('Cost', 'Module 4', 'Full cost of a purchase (calculator)'),
        ('ROI', 'Module 8', 'Rental yield and return calculator'),
        ('Loan', 'Module 8', 'Loan eligibility and EMI'),
        ('Income', 'Module 9', 'Your invoices, income and expenses'),
        ('Network', 'Module 11', 'Brokers, professionals and partners (with consent)'),
        ('Leads', 'Module 19 (start earlier if you get leads)', '`' + tools.CRM_HEADER + '`'),
        ('Inventory', 'Module 10', 'Properties you have a mandate for'),
        ('Dashboard', 'Module 19', 'Counts by stage and source, conversion'),
        ('Log', 'Week 1', 'Weekly market log numbers'),
    ])
    content = f"""
About one hour. Everything is free.

## The free tool stack

- {link('gsheets', 'Google Sheets')} (phone app) or {link('libreoffice', 'LibreOffice Calc')} (laptop): your **Real Estate Workbook** with the tabs below.
- **Google Drive** or a phone folder called **Real Estate Toolkit**, with sub-folders: {', '.join(FOLDERS[:3])} … {FOLDERS[-1]}.
- **Phone camera** and a free video editor for listings (Module 12).
- **Google Maps** and {link('gearth', 'Google Earth')} for locations and rough measurements; {link('qgis', 'QGIS')} on the laptop later (Module 19).
- **WhatsApp Business** (free) for client communication, if you choose (Module 12).
- {link('canva', 'Canva')} (free plan) for simple listing graphics, if you want them (Module 12).
- A **notebook** for office visits and interviews.

## Workbook tabs

{tabs}

## Steps

1. Create the workbook and folders.
2. Add the **Log** tab and the Sunday reminder for the weekly market log.
3. Save the official portal addresses in your phone browser: K-RERA, Kerala Registration, IGR fair value, Revenue (ReLIS), Ente Bhoomi, e-Rekha, KSDMA hazard maps (links in Modules 3 and 4).
4. Write down your **local area**: the panchayats and towns you will study (for example Kuttiady, Velom, Kayakkody, Maruthonkara, Kunnummal, Nadapuram and Kozhikode city). Changing these names for your own area is fine.
5. Decide your privacy rule: you never post anyone's ID, phone number or documents publicly, and you blur personal details in screenshots.
"""
    tasks = [('re-setup-workbook', 'Real Estate Workbook created with tabs'), ('re-setup-folders', 'Toolkit folders made'),
             ('re-setup-portals', 'Official portal addresses saved'), ('re-setup-area', 'Your local study area written down')]
    return {'id': 're-setup', 'title': 'Week 0: free tool setup', 'kind': 'setup', 'weeks': [0, 0], 'hours': 1.0,
            'summary': 'Create your Real Estate Workbook in Google Sheets or LibreOffice, your toolkit folders, saved portal links and your local study area.',
            'content': content.strip(), 'tasks': [{'id': i, 'text': t, 'kind': 'task', 'week': 0} for i, t in tasks]}


def quiz_text(form):
    qs, key = tests.mcq(tests.QUIZ_A if form == 'A' else tests.QUIZ_B, form)
    skills = table(['No', 'Statement (rate 1 = not at all, 5 = fully)', 'Start', 'End'], [(str(i), s, '', '') for i, s in enumerate(tests.SKILLS, 1)])
    return f"""
## Knowledge quiz, form {form} (12 questions, 15 minutes)

Answer without looking anything up; guessing is fine. Score 1 per correct answer, out of 12. Cover the answers first.

{qs}

### Answers, form {form}

{key}

## Skills self-rating (5 minutes)

{skills}

Add the scores (10 to 50).
"""


def baseline_section():
    content = f"""
Take this in week 0 and write your scores in the **Log** tab. You will take form B at the end. Don't worry about a low score: that is the point of a baseline.

{quiz_text('A').strip()}
"""
    return {'id': 're-baseline', 'title': 'Baseline quiz: where you start', 'kind': 'setup', 'weeks': [0, 0], 'hours': 0.5,
            'summary': 'A 12-question knowledge quiz (form A) and a 10-item skills self-rating. You repeat both at the end with form B.',
            'content': content.strip(), 'tasks': [
                {'id': 're-base-quiz', 'text': 'Baseline: knowledge quiz form A scored', 'kind': 'task', 'week': 0},
                {'id': 're-base-skills', 'text': 'Baseline: skills self-rating totalled', 'kind': 'task', 'week': 0}]}


def system_section():
    ms = milestones()
    content = f"""
Two things run underneath the course: a **weekly market log** (20 minutes every Sunday) and a set of **practical milestones** that build your local knowledge and your toolkit. **This week** on the course page shows each one when it is due.

## The weekly market log

Every week, add about three real listings to your Comps sheet, meet or call at least one new person in the property world, update your leads, and check one rule or rate on an official source.

{fence(tools.WEEKLY_LOG)}

## Milestones

{table(['Due by week', 'Milestone', 'Evidence'], [(str(w), t, ev) for _, t, w, ev in ms])}

## Rules for field work

- Always ask permission before photographing a property or a person; get the owner's **written** permission before listing.
- Visit offices politely, during working hours, and never pretend to be a buyer or an officer.
- Don't collect or share anyone's personal documents. Use your own property or a family property (with permission) for record practice, or the sample case in the course.
"""
    tasks = [{'id': f're-log-w{w:02d}', 'text': f'Weekly market log, week {w}', 'kind': 'project', 'week': w,
              'detail': '**Evidence:** the week\'s row in the Log tab.'} for w in range(1, FINAL + 1)]
    tasks += [{'id': i, 'text': t, 'kind': 'project', 'week': w, 'detail': f'**Evidence:** {ev}.'} for i, t, w, ev in ms]
    tasks.sort(key=lambda t: (t['week'], t['id']))
    return {'id': 're-system', 'title': 'Weekly market track: market log and practical milestones', 'kind': 'track',
            'weeks': [1, FINAL],
            'summary': 'A 20-minute Sunday market log, plus milestones: 20+ comparables, fair-value checks, broker interviews, a due-diligence run, ROI for 5 properties, a real listing, a CRM and a site visit.',
            'content': content.strip(), 'tasks': tasks}


def toolkit_section():
    parts = ['Every copy-ready tool in one place. Copy them into your workbook or toolkit folder; the lesson named under each explains how to use it.']
    for name, body, where in tools.TOOLKIT:
        parts.append(f'## {name}\n\nFrom {where}.\n\n' + fence(body))
    return {'id': 're-toolkit', 'title': 'Toolkit: every template and calculator in one place', 'kind': 'reference',
            'summary': 'Comparables sheet, cost calculator, ROI and EMI formulas, due-diligence and document checklists, mandate, intake, site-visit, listing, CRM, timeline, rental agreement checklist, NRI care menu and the weekly log.',
            'content': '\n\n'.join(parts)}


PART_INFO = {
    'A': ('How the Kerala property market works and which business path suits you.', ['Baseline quiz'], ['Real Estate Workbook']),
    'B': ('Land records, law, documents, due diligence, valuation, finance and taxes: the knowledge every professional needs.', ['Baseline quiz (questions 1–9)'], ['Real Estate Workbook with Cost, Comps and ROI tabs']),
    'C': ('Running the business: registration, mandates, sourcing, marketing, sales, transactions, rentals, development, construction, investing, tech, setup, fraud and the capstone.', ['Baseline quiz (questions 6, 10, 12) and skills rating'], ['Workbook with Leads and Inventory tabs', 'Phone camera']),
}


def part_section(letter):
    _, title, a, z = [p for p in plan.PARTS if p[0] == letter][0]
    what, base, tools_ = PART_INFO[letter]
    start = wk(a, 1)
    end = max(PROJECT_WEEK[m] for m in range(a, z + 1))
    mods = [(f'Module {m}', plan.MODULES[m - 1][0], str(len(plan.MODULES[m - 1][1]))) for m in range(a, z + 1)]
    extra = ''
    if letter == 'C':
        extra = '\n\n**Before you take clients:** read RE-M04-L01, RE-M06-L01 and RE-M21-L01 even if you skip the rest of Part B. They contain the minimum legal and fraud knowledge needed to deal safely.'
    content = f"""
## What this part covers

{what}

{table(['Module', 'Title', 'Lessons'], mods)}

Part-time: weeks {start}–{end}.

## Taking this part on its own

1. Read **Start here**, especially the legal and ethics box.
2. Set up: {', '.join(tools_)}.
3. Take: {', '.join(base)}.
4. Start the weekly market log.{extra}
"""
    return {'id': f're-part-{letter.lower()}', 'title': f'Part {letter}: {title}', 'kind': 'gate', 'weeks': [start, start],
            'summary': f'Part {letter} overview: Modules {a}–{z}, weeks {start}–{end}, and how to take it on its own.',
            'content': content.strip(),
            'tasks': [{'id': f're-part-{letter.lower()}-start', 'text': f'Part {letter}: overview read; standalone setup done if starting here', 'kind': 'task', 'week': start}]}


def front():
    return [start_section(), schedule_section(), setup_section(), baseline_section(), system_section(), toolkit_section()]


FINAL_ITEMS = [
    ('re-final-comps', 'Comparables sheet with 20+ local listings and price per cent / per sq ft', 'RE-M07-L03'),
    ('re-final-fv', 'Fair value compared with market prices for at least 3 properties', 'RE-M07-L01'),
    ('re-final-interviews', 'Interview notes from 3 brokers and 1 document writer or advocate', 'RE-M11-L01'),
    ('re-final-docs', 'Annotated sale deed, EC and rental agreement samples', 'Module 5'),
    ('re-final-dd', 'A completed due-diligence checklist on a real or sample property', 'RE-M06-L03'),
    ('re-final-cost', 'A full purchase cost calculation using current official rates', 'RE-M04-L01'),
    ('re-final-roi', 'ROI analysis for 5 real properties', 'RE-M08-L02'),
    ('re-final-listing', 'A real listing with the owner\'s written permission, live on free portals and social media', 'Module 12'),
    ('re-final-crm', 'CRM sheet with every lead tracked', 'RE-M19-L01'),
    ('re-final-visit', 'A real site visit conducted or shadowed', 'RE-M13-L01'),
    ('re-final-toolkit', 'All toolkit templates adapted to your area', 'Toolkit page'),
    ('re-final-capstone', 'Capstone: a first legal deal with written agreements, or an investment analysis plus business plan', 'Module 22'),
]


def final_section():
    content = f"""
Take **form B** of the quiz and the skills rating, compare them with your baseline, and tick the final checklist.

{quiz_text('B').strip()}

## Compare

{table(['Measure', 'Start', 'End', 'Change'], [('Knowledge quiz (out of 12)', '', '', ''), ('Skills self-rating (10–50)', '', '', ''), ('Listings in your Comps sheet', '0', '', ''), ('Property professionals you know', '', '', ''), ('Leads in your CRM', '0', '', '')])}

## Final checklist

{table(['Item', 'Built in'], [(t, w) for _, t, w in FINAL_ITEMS])}
"""
    tasks = [{'id': 're-final-quiz', 'text': 'Final: knowledge quiz form B scored and compared', 'kind': 'task', 'week': FINAL},
             {'id': 're-final-skills', 'text': 'Final: skills self-rating compared', 'kind': 'task', 'week': FINAL}]
    tasks += [{'id': i, 'text': t, 'kind': 'task', 'week': FINAL} for i, t, _ in FINAL_ITEMS]
    tasks.append({'id': 're-final-reflection', 'text': 'Final reflection written: what you can do now and your next 12 months', 'kind': 'exit', 'week': FINAL})
    return {'id': 're-final', 'title': 'Final retest and checklist', 'kind': 'capstone', 'weeks': [FINAL, FINAL], 'hours': 1.5,
            'summary': 'Quiz form B, skills rating, comparison with your baseline and the final checklist of your real estate toolkit.',
            'content': content.strip(), 'tasks': tasks}


def next_section():
    content = f"""
## The next 12 months

{table(['When', 'Focus', 'How'], [
    ('Months 1–3', 'Get to 10 active mandates or rental listings', 'Weekly market log, owner outreach, honest listings'),
    ('Months 1–3', 'Register with K-RERA if your work requires it', 'RE-M10-L01; check current rules'),
    ('Months 3–6', 'Close 2–4 rentals and 1 sale, or sign 3 NRI care clients', 'Written mandates, transaction timeline, CRM'),
    ('Months 6–9', 'Build referral partners: an advocate, a surveyor, a CA, a document writer, two banks', 'RE-M11 and RE-M14'),
    ('Months 9–12', 'Decide: grow a small agency, specialise (NRI, rentals, land), or start a small investment', 'RE-M18 and RE-M20; keep an emergency fund first'),
    ('Every month', 'Update comparables and check one rule on an official source', 'Weekly market log'),
])}

## Go deeper (free)

- {link('mit-re', 'MIT OCW Real Estate Finance and Investment')}: lecture notes and problem sets (about 2 hours per topic).
- {link('os-fin', 'OpenStax Principles of Finance')}: chapters 7–9 on time value of money (about 2 hours each).
- Other courses in this app: {xref('ent', 'ent-start', 'Practical Entrepreneurship')} for business basics, {xref('smm', 'smm-m11', 'Social Media Marketing for local business')}, {xref('fin', 'fin-m09', 'Personal Finance investment options')}.

## Stay legal

Laws, rates and portals change. Before every deal, check stamp duty and fees, K-RERA rules and tax rules on official sources, and keep your advocate, surveyor and CA in the loop.
"""
    return {'id': 're-next', 'title': 'What next: your 12-month roadmap', 'kind': 'reference',
            'summary': 'A 12-month plan to grow from first deals to a small agency or specialist service, with free resources to go deeper.',
            'content': content.strip()}


GLOSSARY = [
    ('Cent', 'സെന്റ്', 'One-hundredth of an acre, about 435.6 sq ft (40.47 sq m)'),
    ('Are', 'ആർ', '100 square metres, about 2.47 cents'),
    ('Hectare', 'ഹെക്ടർ', '100 ares, about 2.47 acres'),
    ('Survey number', 'സർവേ നമ്പർ', 'The number identifying a parcel in survey records'),
    ('Resurvey number', 'റീസർവേ നമ്പർ', 'The parcel number from the resurvey (block and number)'),
    ('Thandaper', 'തണ്ടപ്പേര്', 'The landholder\'s account number in village revenue records'),
    ('Village office', 'വില്ലേജ് ഓഫീസ്', 'The lowest revenue office, which keeps land records and issues certificates'),
    ('Land tax', 'ഭൂനികുതി / കരം', 'The annual tax on land paid to the Revenue Department'),
    ('Possession certificate', 'കൈവശ സർട്ടിഫിക്കറ്റ്', 'Village office certificate that a person is in possession of a property'),
    ('Location certificate', 'ലൊക്കേഷൻ സർട്ടിഫിക്കറ്റ്', 'Certificate of where a property is located'),
    ('Ownership certificate', 'ഉടമസ്ഥാവകാശ സർട്ടിഫിക്കറ്റ്', 'Local body certificate of who owns a building'),
    ('Title deed', 'ആധാരം', 'The registered document that transfers ownership'),
    ('Prior deeds', 'മുന്നാധാരങ്ങൾ', 'Earlier deeds showing how the property passed to the seller'),
    ('Encumbrance certificate (EC)', 'ബാധ്യതാ സർട്ടിഫിക്കറ്റ് (കുടിക്കട സർട്ടിഫിക്കറ്റ്)', 'Certificate listing registered transactions on a property for a period'),
    ('Mutation', 'പോക്കുവരവ്', 'Changing the owner\'s name in revenue records after a transfer'),
    ('Sketch / FMB', 'സ്കെച്ച് / എഫ്.എം.ബി.', 'Survey map of a parcel showing boundaries and measurements'),
    ('Purayidam (dry land)', 'പുരയിടം', 'Garden or dry land, generally usable for houses'),
    ('Nilam (wet land / paddy land)', 'നിലം', 'Paddy or wet land, protected by law'),
    ('Data bank', 'ഡാറ്റാ ബാങ്ക്', 'The official list of paddy and wetlands under the 2008 Act'),
    ('Puramboke', 'പുറമ്പോക്ക്', 'Government land not assigned to anyone (roadsides, river banks)'),
    ('Pattayam', 'പട്ടയം', 'A government grant of land to a person'),
    ('Sub-Registrar Office (SRO)', 'സബ് രജിസ്ട്രാർ ഓഫീസ്', 'The office where property documents are registered'),
    ('Document writer', 'ആധാരം എഴുത്തുകാരൻ', 'A licensed professional who drafts deeds'),
    ('Stamp duty', 'മുദ്രവില', 'Tax paid to the state on a document such as a sale deed'),
    ('Registration fee', 'രജിസ്ട്രേഷൻ ഫീസ്', 'Fee paid to register a document'),
    ('Fair value', 'ന്യായവില', 'The government-notified minimum land value used for stamp duty'),
    ('Market value', 'വിപണി വില', 'The price a willing buyer and seller agree on'),
    ('Token advance', 'ടോക്കൺ അഡ്വാൻസ്', 'A small first payment to hold a deal'),
    ('Agreement for sale', 'വിൽപ്പന കരാർ', 'A contract promising a future sale; does not transfer ownership'),
    ('Sale deed', 'വിലയാധാരം', 'The registered document transferring ownership for a price'),
    ('Gift deed', 'ദാനാധാരം', 'A registered transfer without payment'),
    ('Settlement deed', 'ധനനിശ്ചയാധാരം', 'A registered transfer, usually within a family, sometimes keeping a life interest'),
    ('Release deed', 'ഒഴിമുറി', 'A co-owner gives up their share in favour of the others'),
    ('Will', 'ഒസ്യത്ത്', 'A document that takes effect after death; can be challenged'),
    ('Partition deed', 'ഭാഗപത്രം', 'A registered division of jointly owned property'),
    ('Power of attorney', 'മുക്ത്യാർ', 'A document authorising someone to act for another'),
    ('Release deed', 'ഒഴിവുകുറി', 'A document giving up a share or right in property'),
    ('Mortgage', 'പണയം', 'Property pledged as security for a loan'),
    ('Building permit', 'കെട്ടിട നിർമ്മാണ പെർമിറ്റ്', 'Local body permission to construct'),
    ('Occupancy certificate', 'ഒക്യുപൻസി സർട്ടിഫിക്കറ്റ്', 'Local body certificate that a building can be used'),
    ('Building number', 'കെട്ടിട നമ്പർ', 'The number a local body assigns to a building'),
    ('Building tax', 'കെട്ടിട നികുതി', 'The property tax on buildings paid to the local body'),
    ('NOC', 'നിരാക്ഷേപ പത്രം', 'No objection certificate from an authority'),
    ('Access road', 'വഴി', 'The road or path to the property; legal right of way matters'),
    ('Encroachment', 'കയ്യേറ്റം', 'Unlawful occupation of someone else\'s or government land'),
    ('Commission / brokerage', 'കമ്മീഷൻ / ബ്രോക്കറേജ്', 'The fee paid to an agent'),
    ('Mandate', 'അധികാരപത്രം', 'Written authority from an owner to market a property'),
    ('Rental agreement', 'വാടക കരാർ', 'Contract between landlord and tenant'),
    ('Security deposit', 'സുരക്ഷാ നിക്ഷേപം', 'Refundable money held by the landlord'),
    ('Rental yield', 'വാടക ആദായം', 'Annual rent as a percentage of the price'),
    ('Capital gains', 'മൂലധന നേട്ടം', 'Profit on selling a capital asset such as property'),
    ('TDS', 'ഉറവിടത്തിൽ നികുതി പിടിക്കൽ', 'Tax deducted at source by the buyer and paid to the government'),
    ('Benami property', 'ബിനാമി സ്വത്ത്', 'Property held in another person\'s name while someone else paid and benefits'),
    ('Layout', 'ലേഔട്ട്', 'A plan dividing land into plots with roads'),
    ('CRZ', 'തീരദേശ പരിപാലന മേഖല', 'Coastal Regulation Zone, where building is restricted'),
    ('ESA', 'പരിസ്ഥിതി ലോല പ്രദേശം', 'Ecologically sensitive area'),
    ('REIT', 'റിയൽ എസ്റ്റേറ്റ് നിക്ഷേപ ട്രസ്റ്റ്', 'A listed trust that owns income-producing property'),
]


def glossary_section():
    rows = [(f'**{en}**', ml, meaning) for en, ml, meaning in GLOSSARY]
    content = f"""
Key terms, including common Kerala land and document words. Local usage varies between districts and between older and newer documents; if your deeds use a different word, note it next to the entry.

{table(['English', 'മലയാളം (Malayalam)', 'Simple meaning'], rows)}
"""
    return {'id': 're-glossary', 'title': 'Glossary with Malayalam terms', 'kind': 'reference',
            'summary': f'{len(GLOSSARY)} key real estate and land-record terms in English and Malayalam.', 'content': content.strip()}


def back():
    return [final_section(), next_section(), glossary_section()]


def finish(course):
    sections = course['sections']
    used_in = {}
    for s in sections:
        blob = '\n'.join([s.get('content', ''), s.get('summary', '')] + [t.get('detail', '') for t in s.get('tasks', [])])
        code = s['title'].split(':')[0]
        for key, r in R.items():
            if f"]({r['url']})" in blob:
                used_in.setdefault(key, [])
                if code not in used_in[key]:
                    used_in[key].append(code)
    groups = {}
    for key in used_in:
        groups.setdefault(R[key]['group'], []).append(key)
    parts = [f"""
Every link in the course with where it is used and when it was checked ({VDATE}).

- **verified:** the page was opened and matched what the course says.
- **verified; check current rules:** the page was checked, but it describes something that changes (a rate, a fee, a rule, a portal).
- **verified through a secondary source:** the figure was checked on a reputable secondary guide, not the official page. Confirm on the official source before relying on it.
- **unverified:** the official site blocks automated checks (most Kerala Registration and Revenue portals do), or the address came only from a search. Type the address yourself and check you are on the real government site (it ends in **.gov.in**).

No law, section number, rate or statistic in this course was written from memory without a check; where a check wasn't possible the point is described in general terms and marked "check current rules".
"""]
    for g in GROUP_ORDER:
        if g not in groups:
            continue
        rows = []
        for key in groups[g]:
            r = R[key]
            where = ', '.join(used_in[key][:6]) + (' and more' if len(used_in[key]) > 6 else '')
            rows.append((f"[{r['title']}]({r['url']})", where, STATUS[r['s']]))
        parts.append(f'## {g}\n\n' + table(['Resource', 'Used in', 'Status'], rows))
    unver = [k for k in used_in if R[k]['s'] in ('u', 's')]
    rul = [k for k in used_in if R[k]['s'] in ('vr', 'vt')]
    parts.append('## Marked "unverified"\n\n' + (bullets([f"[{R[k]['title']}]({R[k]['url']})" for k in unver]) or 'None.'))
    parts.append('## Marked "check current rules"\n\n' + (bullets([f"[{R[k]['title']}]({R[k]['url']})" for k in rul]) or 'None.'))
    sections.append({'id': 're-sources', 'title': 'Sources and verification log', 'kind': 'reference',
                     'summary': 'Every link in the course, where it is used and when it was checked.',
                     'content': '\n\n'.join(p.strip() for p in parts)})
