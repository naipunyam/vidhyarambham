"""Course-level sections: start here, schedule, week 0, baseline, money habits
track, final checklist, what next, glossary and the sources page."""
from common import R, STATUS, VDATE, ASOF, CHECK, link, rules, fence, bullets, numbered, table, use, fmt_hours

MODULE_MAP = [
    (1, 'Money mindset', 'Your money story, values, the biases that cost money, needs and wants, lifestyle inflation', 'Values tab and spending rules'),
    (2, 'Goals and tracking', 'Goals with amounts and dates, net-worth statement, cash-flow statement, savings rate', 'Goals, Net Worth and Cash Flow tabs'),
    (3, 'Budgeting', 'Reading your 30-day log, 50/30/20, zero-based, envelopes, a formula budget, irregular income', 'Budget system'),
    (4, 'Banking and payments', 'Account types, KYC, UPI and card safety, fraud liability rules, FDs, RDs, deposit insurance', 'Accounts tab and safety audit'),
    (5, 'Emergency fund', 'How much, where to keep it, how to build it on a small income', 'Emergency fund plan'),
    (6, 'Debt and credit', 'Interest and EMIs, credit cards, loans, credit reports, payoff methods, loan-app traps', 'Debts tab and payoff plan'),
    (7, 'Insurance', 'Term, health, accident, vehicle and home cover, government schemes, claims, complaints', 'Insurance checklist and comparison'),
    (8, 'Investing fundamentals', 'Inflation, compounding, risk and return, asset classes, allocation, rebalancing', 'Calculators and Allocation tabs'),
    (9, 'Investment options in India', 'Mutual funds, index funds, small savings, EPF, PPF, NPS, stocks, gold, REITs, KSFE, co-ops, crypto', 'Fund comparison and shortlist'),
    (10, 'Taxes', 'Income-tax Act 2025, both regimes, capital gains, TDS, filing your ITR, GST for freelancers', 'Tax tab and tax checklist'),
    (11, 'Big life goals', 'Marriage, vehicle, house (rent or buy), children\'s education, supporting parents', 'Big Goals tab'),
    (12, 'Retirement and independence', 'Corpus estimate, pensions, FIRE ideas', 'Retirement tab'),
    (13, 'Estate basics', 'Nominations, joint accounts, wills, a document system', 'Documents tab and nomination audit'),
    (14, 'Kerala government employee', 'Pay slip, DA, NPS and pension status, GPF, Medisep, the first-year plan', 'Government-job money plan'),
    (15, 'Scams and fraud protection', 'Ponzi, MLM, fake apps, finfluencers, UPI and OTP fraud, digital arrest, reporting', 'Scam-proof habits and family briefing'),
    (16, 'Growing income', 'Career, freelancing and business income, linked to the other courses', 'Income growth plan'),
    (17, 'Capstone', 'Investment Policy Statement, one-page financial plan, yearly money review', 'Your complete financial plan'),
]

# Money habits checkpoints: (task id, due week, text, evidence)
CHECKPOINTS = [
    ('fin-habit-day7', 1, '30-day log: day 7 done, every expense logged', 'Expenses tab with 7 days of rows'),
    ('fin-habit-day14', 2, '30-day log: day 14 done', 'Expenses tab with 14 days of rows and a first category total'),
    ('fin-habit-day21', 3, '30-day log: day 21 done', 'Expenses tab with 21 days of rows'),
    ('fin-habit-day30', 5, '30-day log: all 30 days done', 'Expenses tab with 30 days of rows, cash included'),
    ('fin-review-1', 9, 'Monthly money review 1', 'Review tab row: net worth, budget vs actual, emergency fund, one decision'),
    ('fin-review-2', 13, 'Monthly money review 2', 'Review tab row, with debts and insurance updated'),
    ('fin-review-3', 17, 'Monthly money review 3', 'Review tab row, with your allocation checked'),
    ('fin-review-4', 21, 'Monthly money review 4', 'Review tab row, with the tax checklist updated'),
    ('fin-review-5', 25, 'Monthly money review 5', 'Review tab row, with goal savings updated'),
    ('fin-review-6', 29, 'Monthly money review 6', 'Review tab row, ready for your one-page plan'),
]


def habit_hours(w):
    """Hours for the money habits track outside lessons, by part-time week."""
    if 1 <= w <= 4:
        return 1.0  # about 10 minutes a day of logging
    if w == 5:
        return 0.5
    if w in (9, 13, 17, 21, 25, 29):
        return 0.5  # the monthly money review
    return 0


TOOLKIT = [
    ('fin-final-workbook', 'Money Workbook with every tab filled in and dated', 'Week 0, used all course'),
    ('fin-final-budget', 'Budget system: 30-day log, Budget tab with formulas, monthly routine', 'Module 3'),
    ('fin-final-networth', 'Net-worth tracker and cash-flow statement, updated this month', 'Module 2'),
    ('fin-final-ef', 'Emergency fund plan: target, where it is kept, monthly transfer, progress', 'Module 5'),
    ('fin-final-debt', 'Debt list with true costs, payoff plan and a checked credit report', 'Module 6'),
    ('fin-final-insurance', 'Insurance checklist and a policy comparison done without buying', 'Module 7'),
    ('fin-final-ips', 'Investment Policy Statement, signed and dated', 'Modules 8, 9 and 17'),
    ('fin-final-tax', 'Tax checklist and the two-regime calculator', 'Module 10'),
    ('fin-final-goals', 'Goal funding plans and a retirement estimate', 'Modules 11 and 12'),
    ('fin-final-docs', 'Document register, nominations checked on every account, will decision', 'Module 13'),
    ('fin-final-scam', 'Scam-proof habits checklist, shared with your family', 'Module 15'),
    ('fin-final-plan', 'One-page financial plan and the yearly money-review checklist', 'Module 17'),
]


def _mods(modules):
    for m, mod in modules:
        yield m, mod.MODULE, mod.LESSONS


def total_hours(modules):
    h = 4 + 1  # week 0 (with the baseline) and the final checklist
    for _, overview, _lessons in _mods(modules):
        h += overview['hours']
    h += sum(habit_hours(w) for w in range(0, 32))
    return h


def week_plan(modules):
    """Return {week: (items, hours)} at part-time pace."""
    plan = {0: (['Week 0: Money Folder, Money Workbook, security and baseline'], 4)}

    def add(w, item, hrs):
        items, h = plan.get(w, ([], 0))
        if item and item not in items:
            items.append(item)
        plan[w] = (items, h + hrs)

    for m, overview, lessons in _mods(modules):
        for s in lessons:
            a, b = s['weeks']
            code = s['title'].split(':')[0]
            for w in range(a, b + 1):
                label = code if a == b else f'{code} (weeks {a}–{b})'
                add(w, label, s['hours'] / (b - a + 1))
        project_hours = overview['hours'] - sum(s['hours'] for s in lessons)
        pw = next(t['week'] for t in overview['tasks'] if t['id'].endswith('-project'))
        add(pw, f'Module {m} project and rubric', project_hours)
    for w in range(1, 32):
        if 1 <= w <= 5:
            add(w, '30-day expense log', habit_hours(w))
        elif habit_hours(w):
            add(w, 'monthly money review', habit_hours(w))
    add(31, 'final self-assessment and checklist', 1)
    return plan


def full_time_rows(modules):
    """Calendar weeks at full-time pace (weekLength 0.33)."""
    names = {m: name for m, name, _, _ in MODULE_MAP}
    mod_weeks = {m: ov['weeks'] for m, ov, _ in _mods(modules)}
    notes = {
        1: 'Week 0 setup, then start the 30-day expense log on day 1 of course week 1. It runs in real days, to about calendar week 5.',
        2: 'Module 3 arrives before your 30 days are done: build the budget from the days you have, and redo the numbers when day 30 is done.',
        5: 'Your 30-day log ends this week. Update the Budget tab with all 30 days.',
        6: 'First monthly money review at the end of your first real month.',
        10: 'Second monthly money review.',
        11: 'The capstone and the final self-assessment.',
    }
    rows = []
    for c in range(1, 12):
        lo = int((c - 1) / 0.33)
        hi = min(int(c / 0.33 - 0.01), 31)
        if c == 11:
            hi = 31
        focus = [f'M{m:02d} {names[m]}' for m, (s, e) in sorted(mod_weeks.items()) if s <= hi and e >= lo]
        if lo == 0:
            focus.insert(0, 'Week 0')
        rows.append((str(c), f'{lo}–{hi}', '; '.join(focus) or '—', notes.get(c, '')))
    return rows


def start_section(modules):
    total = total_hours(modules)
    weeks_of = {m: ov['weeks'] for m, ov, _ in _mods(modules)}
    map_rows = []
    for m, name, does, output in MODULE_MAP:
        w = weeks_of.get(m)
        wl = '' if not w else (f'{w[0]}' if w[0] == w[1] else f'{w[0]}–{w[1]}')
        map_rows.append((f'{m}. {name}', wl, does, output))
    content = f"""
## What this course is

A free, practical personal finance course for India, written for Kerala. You learn by doing it with your own money: every lesson ends with a task on your real accounts, bills, policies or tax, and you keep proof of it. Lesson by lesson, the tasks build one complete personal financial plan.

It is written for a beginner near Kuttiady in Kozhikode district who is preparing for Kerala PSC exams, has an Android phone and an old laptop, and has ₹0 to spend on learning. Your income may one day come from a government job, freelancing or your own business, so the course covers salaried, irregular and business income. It works just as well for anyone in a similar situation.

Rules, rates and limits change often. Every rate, limit and rule in this course was checked against an official source or a dated news report on {VDATE} and is marked **{ASOF}**. Where it matters, it also says **{CHECK}**: open the linked source before you act.

## By the end you will have

- **A working budget system:** 30 days of real spending, a budget sheet with formulas and a monthly routine
- **A net-worth tracker** and a cash-flow statement you update every month
- **An emergency fund plan** with a target, a place and a monthly transfer that has already started
- **An insurance checklist** and a comparison of real policies, done without buying anything
- **A written Investment Policy Statement:** your rules for investing, before you invest
- **A tax checklist** and a calculator that compares both tax regimes for your income
- **Scam-proof habits** written down and shared with your family
- **A complete personal financial plan** on one page, with a yearly review checklist

All of it lives in one spreadsheet, the **Money Workbook**, and one Google Drive folder, the **Money Folder**.

## How long it takes

{table(['Pace', 'Calendar time', 'Hours a week', 'Total work'], [
    ('Part-time (the default)', 'Week 0, then 31 weeks: about 7 months', 'About 5 (4 to 6)', f'About {total:.0f} hours'),
    ('Full-time', 'About 10 weeks', 'About 14', f'About {total:.0f} hours'),
])}

Pick your pace and start date on the course page; the app then shows which week you are in and what is due. The 30-day expense log takes 30 real days at either pace.

## Educational only: no tips, no selling

- **No product recommendations.** This course never tells you which fund, stock, policy, bank or insurer to choose. It teaches you how to compare them with official data, so you can decide for yourself.
- **Examples are made up.** Anu, Rahul, Fathima and their numbers are invented to show how the methods work. Product names appear only as examples of a type, never as advice.
- **It is not legal, tax or investment advice.** When your situation is complex, or a lot of money is involved, use a professional: a SEBI-registered investment adviser for investment advice (Module 9 shows how to check registration), a chartered accountant or tax practitioner for difficult tax returns, and a lawyer for wills and property.
- **Risks are shown honestly,** including the risks of popular products such as endowment policies, chitties, co-operative deposits, real estate, stocks, gold and crypto.

## Honest expectations

- **Money progress is slow, then fast.** The first months feel small: ₹500 here, ₹2,000 there. Habits compound like interest does.
- **Your income matters more than any tip.** On a small income, the biggest wins are avoiding expensive debt, insuring against disasters and growing your income (Module 16).
- **Nobody can promise returns.** Anyone who promises high, fixed or "guaranteed" returns on an investment is the first warning sign of a scam (Module 15).
- **Mistakes are normal.** You will overspend some months. The monthly review is where you notice and adjust, without guilt.

## How each lesson works

Every lesson has the same parts, in this order:

1. **ID, title, outcome and time** at the top, such as FIN-M01-L01
2. **Core lesson:** the idea, explained simply, with worked calculations in rupees
3. **Local example:** the idea applied by people like you in Kozhikode district
4. **Free resources:** exactly what to study, how long it takes and when the link was checked
5. **Action task:** real work on your own money, and the **proof to record**
6. **Template:** copy-ready sheet headers, formulas and checklists that work in Google Sheets and LibreOffice Calc
7. **Common mistakes** and how to avoid them
8. **Quiz:** 3 to 5 questions, with the answers at the very bottom
9. **Progress checklist:** the ticks under **Your tasks**

Each module starts with an overview page: outcomes, total time, the module project, a self-assessment rubric, a "short on time?" version and revision flashcards.

## Privacy: what proof means here

Proof is a screenshot, a filled-in tab or a short note, saved in your Money Folder. **Never** put full account numbers, card numbers, CVVs, PINs, passwords or OTPs in your proof, your notes, this app or an AI chat. Cover them, or write only the last four digits. Your progress in this app is saved on your phone only.

## Module map

{table(['Module', 'Part-time weeks', 'What you do', 'Output for your plan'], map_rows)}

## Key assumptions

These decisions were made for you when the course was written. Change them if your situation is different.

1. **Pace:** part-time, about 5 hours a week next to PSC study. The full-time pace does the same work in about 10 weeks.
2. **Money:** learning costs ₹0. The course never asks you to buy a product. Where a task involves money (opening a deposit, starting your emergency fund), the amount is yours to choose, and ₹100 is enough to learn the steps.
3. **Income:** you may have little or irregular income now. Every lesson works with any amount, including pocket money, part-time work or family support. Module 14 assumes a future Kerala government job; Module 3 and Module 10 cover freelance and business income.
4. **Devices:** an Android phone does almost everything with Google Sheets. The old laptop is useful for longer spreadsheet work in Google Sheets or LibreOffice Calc.
5. **Family:** in Kerala, money is often a family matter. Tasks that involve parents, a spouse or siblings say so; share only what you are comfortable sharing.
6. **Rules and rates** were checked on {VDATE}. The Income-tax Act, 2025 replaced the 1961 Act from 1 April 2026, so tax lessons use the new law's section numbers, with the old names (such as "80C") in brackets because people still use them.
7. **Not advice.** The course explains Indian rules simply. For complex cases, use a qualified, registered professional.

## The running examples (all made up)

- **Anu**, 27, a PSC aspirant in Kakkattil who tutors students and earns about ₹14,000 a month, irregularly
- **Rahul**, 29, from Thottilpalam, newly appointed as an LD clerk in a Kerala government office after a PSC exam
- **Fathima**, 31, a freelance graphic designer in Kuttiady with clients in Kozhikode and the Gulf
- **Nisha's Oven**, a home bakery in Kuttiady (you may know Nisha from the Entrepreneurship course)
- **Joseph and Mary**, Anu's neighbours, a retired couple in their sixties with a pension and an FD habit

## Other courses in this app

This course links to the others instead of repeating them:

- **Practical Entrepreneurship** for business bookkeeping (ENT-M08-L01), profit and break-even (ENT-M08-L02), business GST and income tax (ENT-M08-L03), funding and loans for a business (ENT-M08-L04), pricing (ENT-M05-L03) and avoiding scams (ENT-M13-L02)
- **Practical Social Media Marketing** for earning from a skill: packages, clients and contracts (Module 15) and account security (SMM-M14-L04)
- **Free AI Generalist Course** for using AI tools well (Level 1) and finding first clients (Capstone)
"""
    return {
        'id': 'fin-start',
        'title': 'Start here: how this course works',
        'kind': 'intro',
        'summary': 'What you will build, how long it takes, why the course gives no tips, how every lesson works, privacy rules for proof, and the assumptions behind the course.',
        'content': content.strip(),
    }


def schedule_section(modules):
    plan = week_plan(modules)
    rows = []
    for w in sorted(plan):
        items, hrs = plan[w]
        rows.append((str(w), '; '.join(items), f'{hrs:.1f}'.rstrip('0').rstrip('.')))
    ft = full_time_rows(modules)
    content = f"""
## Part-time: about 5 hours a week

One course week is one calendar week. This is the default pace on the course page. The **30-day expense log** in weeks 1–5 takes about 10 minutes a day; the **monthly money review** takes about 30 minutes.

{table(['Week', 'What you do', 'Hours'], rows)}

## Full-time: about 14 hours a week

Choose **Full-time** on the course page. The app then moves about three course weeks every calendar week (one course week is 0.33 of a calendar week). Real-day tasks don't speed up:

- **The 30-day expense log** still takes 30 days. Start it on day 1 and keep it going while you study Modules 1–4.
- **Module 3** comes before your log is finished: build the budget from the days you have, then redo it when day 30 is done.
- **Monthly reviews** happen at the end of each real month, so you do two during the course instead of six.

{table(['Calendar week', 'Course weeks', 'Modules', 'Real-day notes'], ft)}

## A weekly rhythm that fits around PSC study

- **Daily, 5–10 minutes:** log the day's spending before you sleep. Check your bank app's UPI history so nothing is missed.
- **Weekdays:** 30–40 minutes for a lesson, after your PSC study block, not before it, so the exam keeps your best hours.
- **Saturday, 90 minutes:** the action task. Most tasks need your bank app, statements or documents, so do them in one sitting.
- **First Sunday of the month, 30 minutes:** your money date. From week 9 this is the monthly money review.

## When you fall behind

- **This week** shows earlier open tasks as overdue. Do the action tasks first; readings can wait.
- More than two weeks behind? Set a new start date on the course page so the weeks match your real progress. Your ticks are kept.
- Use each module's "short on time?" version when you need it.

## Exam mode

In the four weeks before a PSC exam: keep only the 5-minute daily log (if it is running) and the monthly review, and pause the lessons. Move your start date later by the same number of weeks. Money habits keep running; the course waits for you.
"""
    return {
        'id': 'fin-schedule',
        'title': 'Weekly schedule: part-time and full-time',
        'kind': 'reference',
        'summary': 'What to do each week at both paces, how the 30-day log fits the full-time pace, and a weekly rhythm around PSC study.',
        'content': content.strip(),
    }


EXPENSE_HEADERS = 'Date,Amount (₹),Category,Need or want,Paid by,Paid to,Note'

CATEGORIES = [
    'Food and groceries', 'Eating out and snacks', 'Transport and fuel', 'Phone and internet',
    'Rent and housing', 'Electricity, water and gas', 'Health and medicines', 'Education and PSC',
    'Clothes and personal care', 'Family support', 'Gifts, functions and festivals',
    'Subscriptions and apps', 'Loan EMIs and card payments', 'Savings and investments', 'Other',
]

COACH_PROMPT = """
You are my patient personal-finance tutor for India. I live near Kuttiady, Kozhikode, Kerala, and I am a beginner taking a self-study course. Explain in simple English, with a short Malayalam word for key terms. Use rupee examples. Never recommend a specific fund, stock, insurance policy, bank or app; instead, teach me how to compare options using official sources (RBI, SEBI, AMFI, IRDAI, the Income Tax Department). Tell me when a rule may have changed and which official page to check. If my question needs a professional (tax, legal or investment advice for my exact case), say so. Ask me one question at a time to check I understood.
"""

MONEY_RULES = [
    '**Never share an OTP, UPI PIN, card PIN, CVV or password** with anyone, including people who say they are from your bank, the police, RBI or a courier company. Banks and government agencies never ask for them.',
    '**Don\'t buy any financial product during this course just because a lesson discusses it.** Compare first, decide later, and only after your emergency fund and insurance basics are in place.',
    '**Don\'t borrow to invest,** and don\'t take a loan from an app you found through an ad or a message (Module 6 shows how to check a lender).',
    '**Ignore tips** from WhatsApp and Telegram groups, YouTube "gurus" and strangers. Anyone advising you on investments for a fee must be registered with SEBI (Module 9).',
    '**Keep your proof private.** Cover account and card numbers in every screenshot, and never paste them into this app or an AI chat.',
    '**Talk before you sign.** For any policy, loan, chitty or investment, take the documents home, read them, and sleep on it. Good offers don\'t expire tonight.',
]


def setup_section():
    content = f"""
Week 0 takes about 4 hours, including the baseline self-assessment on the next page. You set up free tools once, so every lesson has a place to save its work, and you start the habit the whole course depends on: writing down where your money goes.

## 1. A Money Folder in Google Drive

Make a folder called **Money Folder** with these subfolders: 00 Baseline, 01 Mindset, 02 Goals, 03 Budget, 04 Banking, 05 Emergency, 06 Debt, 07 Insurance, 08 Basics, 09 Investing, 10 Tax, 11 Big goals, 12 Retirement, 13 Estate, 14 Govt job, 15 Scams, 16 Income, 17 Plan. Every lesson's proof goes into one of them.

- Keep the folder **private**: don't share it with anyone except, if you choose, a spouse or parent.
- Store screenshots with account numbers covered. Keep original documents (PAN, Aadhaar, policy papers) in DigiLocker or a safe place at home, not in a shared folder. Module 13 builds a proper document system.

## 2. The Money Workbook

Make one spreadsheet called **Money Workbook** in Google Sheets (phone or laptop). If you prefer working offline on the laptop, the free {link('libreoffice', 'LibreOffice Calc')} opens and saves the same file as .xlsx or .ods. Start with two tabs; each module adds its own tab, so by week 31 the workbook is your whole plan.

**Tab 1: Expenses.** Put these headings in row 1:

{fence(EXPENSE_HEADERS, 'csv')}

- **On the laptop:** paste the line into cell A1, then choose **Data → Split text to columns** (Google Sheets) or **Data → Text to Columns** (LibreOffice).
- **On the phone:** type the seven headings into A1 to G1.
- **Categories** (type them exactly the same way every time, so formulas can add them up): {', '.join(CATEGORIES)}.

**Tab 2: Baseline.** You fill it on the next page.

**Formulas in this course** work in both Google Sheets and LibreOffice Calc. One difference: LibreOffice may expect semicolons (;) instead of commas (,) between the parts of a formula, depending on its settings ({link('lo-separators', 'Tools → Options → LibreOffice Calc → Formula → Separators')}). If a formula from this course shows an error in LibreOffice, change the commas to semicolons.

## 3. Get your phone ready

- **Your bank's official app:** install it only from the link on your bank's own website. Turn on SMS and email alerts for every transaction; alerts are how you catch fraud early (Module 4).
- **Google Sheets and Google Drive** for the workbook and folder.
- **Screen lock** on the phone, and app lock on payment apps if they offer it.
- **Update** the phone's software when updates arrive; they fix security holes.

## 4. Lock your accounts

Turn on 2-Step Verification for the Google account that holds your Money Folder (Google Account → Security). Use a different, long password for your email and for each banking app. Save backup codes on paper at home. Module 15 goes deeper into fraud protection.

## 5. Rules from day 1

These protect you while you learn. Each one is explained fully later in the course:

{bullets(MONEY_RULES)}

## 6. An AI assistant as your tutor (optional)

The free plans of common AI chat tools are enough to ask "explain this simply" questions. Save this prompt and paste it at the start of a chat:

{fence(COACH_PROMPT)}

AI tools can be wrong about Indian rules, especially recent ones. Check every rate or rule against the official link in the lesson. Never give an AI tool your account numbers, PAN, Aadhaar number or documents.

## 7. Your calendar and a money buddy

Block your weekly slots in your calendar, plus a **money date** on the first Sunday of every month. Choose a money buddy: a friend, sibling or spouse who asks you every Sunday, "Did you log everything this week?"

## 8. Start the 30-day expense log

Your log starts on day 1 of week 1, the day after you finish this page. The **Money habits track** page explains the rules. Log everything, including cash, tea and small UPI payments. It takes 5 to 10 minutes a day.

Every link on this page was checked on {VDATE}. The **Sources and verification log** at the end of the course lists each one with its status.
"""
    tasks = [
        ('fin-w0-folder', 'Money Folder made in Google Drive, private, with its 18 subfolders'),
        ('fin-w0-workbook', 'Money Workbook made, with the Expenses tab headings and the category list'),
        ('fin-w0-phone', 'Bank app from the official link, transaction alerts on, screen lock on'),
        ('fin-w0-security', '2-Step Verification on for the Google account; unique passwords for email and banking'),
        ('fin-w0-rules', 'Rules from day 1 read and saved as a note on your phone'),
        ('fin-w0-calendar', 'Weekly slots and a monthly money date in your calendar; money buddy chosen'),
    ]
    return {
        'id': 'fin-w0',
        'title': 'Week 0: Money Folder, Money Workbook and rules from day 1',
        'kind': 'setup',
        'weeks': [0, 0],
        'hours': 3.5,
        'summary': 'One private Drive folder, one workbook, a secure phone, rules that protect you from day 1, and everything ready for the 30-day expense log.',
        'content': content.strip(),
        'tasks': [{'id': i, 'text': t, 'kind': 'task', 'week': 0} for i, t in tasks],
    }


SKILLS = [
    'Say where my money goes each month, in rupees',
    'Tell needs from wants and spot lifestyle inflation',
    'Set a money goal with an amount, a date and a monthly saving',
    'Build a net-worth statement',
    'Build a monthly budget in a spreadsheet with formulas',
    'Budget an irregular or freelance income',
    'Use UPI, cards and net banking safely, and know what to do after a fraud',
    'Size an emergency fund and choose where to keep it',
    'Calculate the true cost of a loan or a credit-card balance',
    'Read my credit report and get an error fixed',
    'Work out how much term and health cover I need, without being sold to',
    'Make an insurance claim, and complain if it is rejected',
    'Explain inflation, compounding and real return with numbers',
    'Choose an asset allocation and rebalance it',
    'Compare mutual funds using official data',
    'Explain PPF, EPF, NPS, FDs and small savings, and when each fits',
    'Calculate income tax under both regimes and file my own return',
    'Plan a big goal: house, vehicle, education or parents\' care',
    'Spot and report an investment or payment scam',
    'Write and review a personal financial plan',
]

LEVELS = [
    ('1', 'Never heard of it, or can\'t do it'),
    ('2', 'Understand it, but haven\'t done it'),
    ('3', 'Can do it with help or a guide open'),
    ('4', 'Can do it alone, reliably'),
    ('5', 'Can explain it to my family and do it for them'),
]


def baseline_section():
    rows = [(str(i), s, '', '') for i, s in enumerate(SKILLS, 1)]
    content = f"""
Before you start, record where you are. You'll take exactly the same self-assessment in week 31 and compare. Be honest: low scores now make your progress visible later. It takes about 30 minutes.

## Part 1: rate 20 skills from 1 to 5

{table(['Score', 'Means'], LEVELS)}

Copy this table into the **Baseline** tab of your Money Workbook. Fill in the **Start** column now; leave **End** for week 31.

{table(['No', 'Skill', 'Start (week 0)', 'End (week 31)'], rows)}

## Part 2: your money snapshot

Rough numbers are fine; guesses are allowed and useful. You will compare them with real numbers later, and the gap between guess and reality is one of the most useful things this course shows you. Write them in the same tab.

{fence('''MONEY SNAPSHOT (date: ____)
Monthly income after deductions, roughly: ₹____ (0 is a fine answer)
Monthly spending, your best guess: ₹____
Savings and investments, total: ₹____
Loans, card dues and money owed to people, total: ₹____
If my income stopped today, I could cover about ____ months of expenses
Health insurance: yes / no / don't know   Cover: ₹____
Life insurance: yes / no   Type, if known: ____
I know my credit score: yes / no
Nominees on all my accounts: yes / no / don't know
I have filed an income tax return before: yes / no
I have been offered a "scheme", app or tip that promised big returns: yes / no''')}

## Part 3: three sentences

1. Why I am doing this course: ____
2. What I want my money life to look like in week 31: ____
3. What usually stops me finishing things, and my plan for it: ____

Save a screenshot of the Baseline tab (numbers you consider private can be covered) in **00 Baseline**.
"""
    return {
        'id': 'fin-baseline',
        'title': 'Baseline self-assessment (you repeat it at the end)',
        'kind': 'setup',
        'weeks': [0, 0],
        'hours': 0.5,
        'summary': 'Rate 20 money skills, write a rough money snapshot and say why you are doing this. You take the same assessment in week 31.',
        'content': content.strip(),
        'tasks': [
            {'id': 'fin-baseline-skills', 'text': 'Baseline: 20 skills rated, Start column filled in', 'kind': 'task', 'week': 0},
            {'id': 'fin-baseline-snapshot', 'text': 'Baseline: money snapshot and three sentences written', 'kind': 'task', 'week': 0},
        ],
    }


REVIEW_HEADERS = 'Month,Income (₹),Spent (₹),Saved (₹),Savings rate %,Net worth (₹),Emergency fund (₹),Debt left (₹),Biggest overspend,One decision for next month'


def habits_section():
    cp_rows = [(str(w), t, ev) for _, w, t, ev in CHECKPOINTS]
    content = f"""
Two habits run underneath the whole course. **This week** on the course page shows one checkpoint at a time.

## Habit 1: the 30-day expense log (weeks 1–5)

For 30 days in a row, write down every rupee that leaves your hands or your accounts, in the **Expenses** tab. This is the most important task in the course: every budget, goal and plan later is built on these real numbers.

**Rules for the 30 days**

1. **Everything counts:** tea, bus fare, mobile recharge, a ₹10 UPI payment, money given to family, a gift at a wedding. Cash too.
2. **Log daily,** before you sleep. Open your bank app's UPI history and your wallet: anything missing? It takes 5 to 10 minutes.
3. **One row per payment.** Date, amount, category from the list in Week 0, need or want (your honest call), how you paid, who you paid, and a short note if useful.
4. **Don't change your life for the log.** The aim is to see your real spending, not a "good month". If you notice a leak, write it in the note; you fix it in Module 3.
5. **Missed a day?** Fill it from your UPI history and memory the next morning. Don't restart; just keep going.
6. **Shared family spending:** if you pay for the household, log what you pay. If parents pay for you, you can add a note of rough amounts; it helps you plan for the day you take over.

**A formula to watch your total grow** (put it in any empty cell, such as J1):

{fence('=SUM(B2:B500)')}

## Habit 2: the monthly money review (from week 9)

On your money date, spend 30 minutes updating your numbers and making one decision. Add a **Review** tab with these headings:

{fence(REVIEW_HEADERS, 'csv')}

Savings rate % formula, for row 2: `=IF(B2>0, D2/B2*100, 0)`

**The review routine:** update Net Worth (Module 2), compare budget with actual spending (Module 3), check the emergency fund and debts, then write **one decision** for next month, such as "cancel one unused subscription" or "move ₹500 more to the emergency fund on salary day". One decision a month is enough; twelve good decisions a year change your life.

## Checkpoints

{table(['Due by week', 'Checkpoint', 'Evidence'], cp_rows)}

## When a checkpoint is missed

Missing one is information, not failure. Ask why: no fixed time, too many categories, embarrassment about a spend, exam pressure? Fix that one thing. For the log, fill the gap from your UPI history and carry on.
"""
    return {
        'id': 'fin-habits',
        'title': 'Money habits track: the 30-day log and monthly reviews',
        'kind': 'track',
        'weeks': [1, 29],
        'summary': 'Log every rupee for 30 days in weeks 1–5, then review your money for 30 minutes every month. Ten checkpoints keep you on track.',
        'content': content.strip(),
        'tasks': [
            {'id': tid, 'text': text, 'kind': 'project', 'week': w,
             'detail': f'**Evidence:** {ev}. Save a screenshot in your Money Folder (03 Budget for the log, 17 Plan for reviews).'}
            for tid, w, text, ev in CHECKPOINTS
        ],
    }


def front(modules):
    return [start_section(modules), schedule_section(modules), setup_section(), baseline_section(), habits_section()]


# ---------------------------------------------------------------- back matter

def final_section():
    rows = [(t, where) for _, t, where in TOOLKIT]
    content = f"""
Two things to finish the course: retake the baseline self-assessment, and check that every part of your plan exists.

## 1. Retake the self-assessment

Open the **Baseline** tab and fill in the **End** column for all 20 skills, without looking at your start scores first. Then compare:

- Which three skills grew the most? Write them in your one-page plan's notes.
- Any skill still at 1 or 2? Note which module covers it and plan one practice task for next month.
- Rewrite the **money snapshot** with real numbers now, next to your week 0 guesses. Where was your guess furthest from reality?

## 2. Check your toolkit

Each item should be a tab, a file or a note in your Money Folder that you could show a family member tomorrow. If something is missing, the module listed has its template.

{table(['Toolkit item', 'Where the template is'], rows)}

## Before you call the course done

- Save a backup of your progress from **Backup and courses** in this app, and keep it in your Money Folder.
- Download a copy of your Money Workbook (File → Download) and keep it offline too.
- Put your next monthly money date and your yearly review month in your calendar. The course ends; your money system doesn't.
"""
    tasks = [
        {'id': 'fin-final-reassess', 'text': 'Final self-assessment: End column filled in and compared with week 0', 'kind': 'exit', 'week': 31},
        {'id': 'fin-final-snapshot', 'text': 'Money snapshot rewritten with real numbers, next to the week 0 guesses', 'kind': 'task', 'week': 31},
    ] + [{'id': i, 'text': t, 'kind': 'task', 'week': 31} for i, t, _ in TOOLKIT]
    return {
        'id': 'fin-final',
        'title': 'Final self-assessment and toolkit checklist',
        'kind': 'capstone',
        'weeks': [31, 31],
        'hours': 1,
        'summary': 'Retake the baseline self-assessment, compare your real money snapshot with your week 0 guesses, and check that every part of your plan exists.',
        'content': content.strip(),
        'tasks': tasks,
    }


def next_section():
    content = f"""
Finishing the course is the start of running your own money. Here is a sensible order for the next twelve months.

## Every month (30 minutes)

- The monthly money review on your money date: update the numbers, make one decision.
- Keep the 50/30/20 or zero-based budget you chose; log spending at least for one week each quarter, so you don't drift.

## Every quarter (1 hour)

- Small savings rates are announced every quarter: check if they changed ({link('indiapost', 'India Post rates page')}).
- Check your allocation against your Investment Policy Statement; rebalance only if it has drifted beyond your limits.
- Download your mutual fund and demat statement ({link('amfi-cas', 'CAS')}) and check that nominations and KYC show as complete.

## Every year (one weekend, in the same month every year)

Use the yearly money-review checklist from FIN-M17-L03: insurance renewals and cover, nominations, the will decision, the free credit reports, tax regime choice and ITR, goals and their timelines, and the one-page plan.

## When life changes, revisit these modules

{table(['When this happens', 'Revisit'], [
    ('You get a Kerala government job', 'Module 14: the first-year plan, then Modules 7, 10 and 12'),
    ('You start freelancing or a business', 'FIN-M03-L04 and FIN-M10-L05, plus the Entrepreneurship course, Module 8'),
    ('Marriage or a child', 'Modules 7, 11 and 13: cover, goals and nominations'),
    ('You plan to buy a house or vehicle', 'FIN-M11-L02 and FIN-M06-L03'),
    ('A big windfall: arrears, bonus, inheritance, sale of gold or land', 'Your Investment Policy Statement first, then Modules 8 and 9; wait 30 days before deciding'),
    ('Someone offers a "great scheme"', 'Module 15, before you pay anything'),
])}

## When to pay for advice

You don't need an adviser to follow this course. Consider a fee-only SEBI-registered investment adviser when your investments become large or complicated, after a windfall, or before retirement. Check registration on the {link('sebi-ia-list', 'SEBI list of registered investment advisers')} first, and read about fee limits in FIN-M09-L02. For tax notices or business accounts, use a chartered accountant.

## Keep learning, free

- {link('ncfe', 'NCFE\'s free e-LMS course')}: about 5 hours on banking, insurance, pensions, investing and scams
- {link('varsity', 'Zerodha Varsity')}: the Personal Finance, Mutual Funds, Insurance and NPS modules, read as education, not as product advice
- {link('openstax', 'OpenStax Principles of Finance')}: chapters 3, 7, 8, 15 and 20 for the theory behind interest, time value and risk
- {link('sebi-investor', 'SEBI investor website')} and {link('rbi-fe', 'RBI Financial Education')} for new rules and fraud warnings
- {link('nse-iap', 'NSE\'s free investor awareness programmes')} (with study material) and {link('nism-fe', 'NISM\'s financial education programmes')}; SEBI\'s Saa₹thi app for learning on your phone
- For Kerala government employees: the {link('kl-fin', 'Finance Department website')} for DA, pay and pension orders

## Keep up with rule changes

The Union Budget (usually on 1 February) can change tax rules; RBI changes rates through the year; Kerala announces DA and pay decisions by government order. Once a month, spend 15 minutes on the official pages linked in this course's sources log, and update your plan when something changes.

Every link on this page was checked on {VDATE}; see the **Sources and verification log** for each one's status.
"""
    return {
        'id': 'fin-next',
        'title': 'What next: your 12-month money routine',
        'kind': 'reference',
        'summary': 'How to keep your money system running after the course: monthly, quarterly and yearly routines, life events, when to pay for advice and where to keep learning.',
        'content': content.strip(),
    }


GLOSSARY = [
    ('Budget', 'ബജറ്റ് (വരവുചെലവ് പദ്ധതി)', 'A plan for how you will use the money you expect to receive'),
    ('Income', 'വരുമാനം', 'Money you receive: salary, fees, business profit, interest'),
    ('Expense', 'ചെലവ്', 'Money you spend'),
    ('Savings', 'സമ്പാദ്യം', 'The part of income you don\'t spend'),
    ('Savings rate', 'സമ്പാദ്യ നിരക്ക്', 'Savings as a percentage of income'),
    ('Needs and wants', 'ആവശ്യങ്ങളും ആഗ്രഹങ്ങളും', 'What you must pay for, and what you would like to have'),
    ('Lifestyle inflation', 'ജീവിതശൈലി ചെലവ് വർധന', 'Spending rising every time income rises, so saving never grows'),
    ('Asset', 'ആസ്തി', 'Something you own that has money value'),
    ('Liability', 'ബാധ്യത', 'Money you owe'),
    ('Net worth', 'അറ്റ ആസ്തി', 'Everything you own minus everything you owe'),
    ('Cash flow', 'പണമൊഴുക്ക്', 'Money coming in and going out over a period'),
    ('Emergency fund', 'അടിയന്തര നിധി', 'Savings kept ready for job loss, illness or urgent repairs'),
    ('Inflation', 'വിലക്കയറ്റം (പണപ്പെരുപ്പം)', 'Prices rising over time, so each rupee buys less'),
    ('Interest', 'പലിശ', 'The price of borrowing money, or the reward for lending it'),
    ('Principal', 'മുതൽ', 'The original amount borrowed or invested'),
    ('Compound interest', 'കൂട്ടുപലിശ', 'Interest earned on earlier interest as well as on the principal'),
    ('EMI', 'മാസത്തവണ (ഇ.എം.ഐ.)', 'Equated monthly instalment: a fixed monthly loan payment'),
    ('Loan', 'വായ്പ', 'Money borrowed that must be repaid with interest'),
    ('Debt', 'കടം', 'Money you owe to anyone'),
    ('Collateral', 'ഈട്', 'Something pledged to a lender, such as gold, that can be taken if you don\'t repay'),
    ('Guarantor', 'ജാമ്യക്കാരൻ', 'A person who promises to repay if the borrower doesn\'t'),
    ('Credit score', 'ക്രെഡിറ്റ് സ്കോർ (വായ്പാ വിശ്വാസ്യത സ്കോർ)', 'A number that shows lenders how reliably you have repaid'),
    ('Savings account', 'സേവിങ്സ് അക്കൗണ്ട്', 'A bank account for keeping money safely, with some interest'),
    ('Fixed deposit (FD)', 'സ്ഥിര നിക്ഷേപം', 'A lump sum kept with a bank for a fixed time at a fixed rate'),
    ('Recurring deposit (RD)', 'ആവർത്തന നിക്ഷേപം', 'A fixed amount deposited every month for a fixed time'),
    ('KYC', 'ഉപഭോക്താവിനെ തിരിച്ചറിയൽ (കെ.വൈ.സി.)', 'Know Your Customer: proving your identity and address'),
    ('Nominee', 'നോമിനി (നാമനിർദ്ദേശം ചെയ്യപ്പെട്ടയാൾ)', 'The person who receives the money in an account if you die'),
    ('Will', 'വിൽപ്പത്രം', 'A written document saying who gets your property after you die'),
    ('Insurance', 'ഇൻഷുറൻസ്', 'Paying a small, certain amount to be protected from a large, uncertain loss'),
    ('Premium', 'പ്രീമിയം (ഇൻഷുറൻസ് തവണ)', 'The amount you pay for insurance'),
    ('Sum insured or sum assured', 'ഇൻഷുറൻസ് തുക (പരിരക്ഷാ തുക)', 'The most the insurer will pay'),
    ('Claim', 'ക്ലെയിം (നഷ്ടപരിഹാര അപേക്ഷ)', 'Asking the insurer to pay under your policy'),
    ('Term insurance', 'ടേം ഇൻഷുറൻസ് (കാലാവധി ലൈഫ് ഇൻഷുറൻസ്)', 'Pure life cover for a fixed period, with no maturity payout'),
    ('Waiting period', 'കാത്തിരിപ്പ് കാലയളവ്', 'Time after buying health cover before some illnesses are covered'),
    ('Investment', 'നിക്ഷേപം', 'Putting money into something you expect to grow or pay income'),
    ('Risk', 'നഷ്ടസാധ്യത (റിസ്ക്)', 'The chance that results differ from what you expect, including losses'),
    ('Return', 'ആദായം (റിട്ടേൺ)', 'What an investment earns, as a percentage'),
    ('Real return', 'യഥാർത്ഥ ആദായം', 'Return after subtracting inflation'),
    ('Asset allocation', 'ആസ്തി വിന്യാസം', 'How your money is split between equity, debt, gold and cash'),
    ('Diversification', 'വൈവിധ്യവൽക്കരണം', 'Spreading money across many investments so one failure hurts less'),
    ('Rebalancing', 'പുനഃസന്തുലനം', 'Bringing your allocation back to its target'),
    ('Mutual fund', 'മ്യൂച്വൽ ഫണ്ട്', 'A pool of many people\'s money invested by a professional manager'),
    ('SIP', 'വ്യവസ്ഥാപിത നിക്ഷേപ പദ്ധതി (എസ്.ഐ.പി.)', 'Systematic investment plan: investing a fixed amount regularly'),
    ('NAV', 'അറ്റ ആസ്തി മൂല്യം (എൻ.എ.വി.)', 'Net asset value: the price of one unit of a mutual fund'),
    ('Expense ratio', 'ചെലവ് അനുപാതം', 'The yearly fee a fund takes, as a percentage of your money'),
    ('Index fund', 'ഇൻഡക്സ് ഫണ്ട് (സൂചിക ഫണ്ട്)', 'A fund that simply copies a market index'),
    ('Share or stock', 'ഓഹരി', 'A small part-ownership of a company'),
    ('Demat account', 'ഡീമാറ്റ് അക്കൗണ്ട്', 'An account that holds shares and other securities electronically'),
    ('Dividend', 'ലാഭവിഹിതം', 'Part of a company\'s or fund\'s profit paid to investors'),
    ('Capital gain', 'മൂലധന നേട്ടം', 'Profit from selling an investment for more than you paid'),
    ('Income tax', 'ആദായ നികുതി', 'Tax on your yearly income'),
    ('Tax regime', 'നികുതി സമ്പ്രദായം', 'The set of rates and deductions you choose: old or new'),
    ('Deduction', 'കിഴിവ്', 'An amount subtracted from income before tax is worked out'),
    ('TDS', 'ഉറവിടത്തിൽ നികുതി പിടിക്കൽ (ടി.ഡി.എസ്.)', 'Tax deducted at source by the payer before paying you'),
    ('Income tax return (ITR)', 'ആദായ നികുതി റിട്ടേൺ', 'The yearly statement of your income and tax filed with the department'),
    ('GST', 'ചരക്ക് സേവന നികുതി (ജി.എസ്.ടി.)', 'Goods and Services Tax, charged on most sales of goods and services'),
    ('Provident fund', 'പ്രൊവിഡന്റ് ഫണ്ട് (ഭാവിനിധി)', 'A long-term savings account for retirement, such as EPF, GPF or PPF'),
    ('Pension', 'പെൻഷൻ', 'Regular income after retirement'),
    ('Dearness allowance (DA)', 'ക്ഷാമബത്ത', 'An allowance added to pay to offset rising prices'),
    ('Retirement corpus', 'വിരമിക്കൽ നിധി', 'The total savings you need to live on after you stop working'),
    ('Chitty', 'ചിട്ടി (കുറി)', 'A group saving and borrowing scheme where members bid for the monthly prize'),
    ('Co-operative society', 'സഹകരണ സംഘം', 'A member-owned organisation; some take deposits, but not all are licensed banks'),
    ('Ponzi scheme', 'പോൻസി തട്ടിപ്പ്', 'A fraud that pays old investors with new investors\' money until it collapses'),
    ('Phishing', 'ഫിഷിങ് (വ്യാജ സന്ദേശ തട്ടിപ്പ്)', 'Fake messages or sites that trick you into giving passwords or OTPs'),
    ('Investment Policy Statement', 'നിക്ഷേപ നയരേഖ', 'Your written rules for investing: goals, allocation, what you will and won\'t do'),
    ('Financial plan', 'സാമ്പത്തിക പദ്ധതി', 'Your goals and the steps, numbers and dates to reach them'),
]


def glossary_section():
    rows = [(f'**{en}**', ml, meaning) for en, ml, meaning in GLOSSARY]
    content = f"""
Key words from the course, roughly in the order you meet them. Many English words, such as EMI, SIP and KYC, are used as they are in Malayalam conversation; the Malayalam is given so you can explain them to family.

{table(['English', 'മലയാളം (Malayalam)', 'Simple meaning'], rows)}
"""
    return {
        'id': 'fin-glossary',
        'title': 'Glossary with Malayalam meanings',
        'kind': 'reference',
        'summary': f'{len(GLOSSARY)} key personal finance terms in English and Malayalam, with simple meanings.',
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
    order = ['Income tax and GST', 'RBI, banking and credit', 'SEBI, AMFI and investing',
             'Small savings, EPF, NPS and pensions', 'Insurance', 'Kerala', 'Scams, safety and complaints',
             'Nominations, documents and wills', 'Law and family', 'Free courses and books', 'Free tools', 'Other']
    parts = [f"""
Every link in this course is listed here with the date it was checked. Links were opened and read on {VDATE}; nothing here was copied from memory. If a link stops working, search for its title on the same website.

- **verified {VDATE}:** the page was opened on that date and its content matched what the course says.
- **verified {VDATE}; check current rules:** as above, but it is a rate, limit or rule that changes often. Open the source before you act.
- **verified {VDATE} (headline checked):** the page could not be opened in full, so only its headline and date were checked in a web search. The course uses it only for what the headline itself says.
- **unverified:** the site blocks automated checks, so the page could not be opened for this course. The address is the official one named by other government sources; type it yourself and check that it is the real site.

Government and regulator pages are preferred. Where an official page could not be opened or doesn't exist in plain text, a dated news report or a bank's official page is used instead, and its date is in the title. OpenStax *Principles of Finance* is licensed CC BY 4.0, and this course only links to it.
"""]
    for g in order:
        if g not in groups:
            continue
        rows = []
        for key in groups[g]:
            r = R[key]
            where = ', '.join(used_in[key][:6]) + (' and more' if len(used_in[key]) > 6 else '')
            rows.append((f"[{r['title']}]({r['url']})", where, STATUS[r['s']]))
        parts.append(f'## {g}\n\n' + table(['Resource', 'Used in', 'Status'], rows))
    unverified = [k for k in used_in if R[k]['s'] == 'u']
    headline = [k for k in used_in if R[k]['s'] == 'vt']
    rules_keys = [k for k in used_in if R[k]['s'] == 'vr']
    parts.append('## Marked "unverified"\n\n' + bullets([f"[{R[k]['title']}]({R[k]['url']})" for k in unverified]))
    parts.append('## Headline checked only\n\n' + bullets([f"[{R[k]['title']}]({R[k]['url']})" for k in headline]))
    parts.append('## Marked "check current rules"\n\n' + bullets([f"[{R[k]['title']}]({R[k]['url']})" for k in rules_keys]))
    sections.append({
        'id': 'fin-sources',
        'title': 'Sources and verification log',
        'kind': 'reference',
        'summary': f'Every link in the course, where it is used and when it was checked ({VDATE}).',
        'content': '\n\n'.join(p.strip() for p in parts),
    })
