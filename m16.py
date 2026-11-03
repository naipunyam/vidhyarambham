"""Module 16: Growing income (brief, with cross-references)."""
from common import lesson, module, link, fence, table, inr, ASOF, CHECK

M = 16

L1 = lesson(
    M, 1,
    title='Growing your income: the biggest lever, used wisely',
    weeks=(29, 29), hours=1.5,
    outcome='Choose one realistic way to grow your income in the next year, using the other courses in this app, and set money rules so extra income becomes progress, not lifestyle.',
    split='20 minutes reading, 20 minutes resources, 50 minutes action',
    core=f"""
On a small income, cutting costs helps, but only up to a point: you can't save more than you earn. **Growing income is the biggest lever in personal finance.** This short module points you to the courses in this app that teach the skills, and adds the money rules that make extra income count.

### Four paths, and where this app teaches them

{table(['Path', 'What it takes', 'Where to learn it in this app'], [
    ('A government job through Kerala PSC', 'Steady preparation; then Module 14 of this course for the money side', 'Your PSC study plan; FIN-M14'),
    ('Freelancing with a skill', 'A skill clients pay for, a portfolio, a price and a way to find clients', 'Social Media Marketing course: packages and pricing (SMM-M15-L01), finding clients (SMM-M15-L02), contracts and reports (SMM-M15-L03); Free AI Generalist Course: Level 1 and the Capstone on first clients'),
    ('Your own small business', 'A tested idea, pricing, bookkeeping, registrations', 'Practical Entrepreneurship: pricing (ENT-M05-L03), bookkeeping and cash flow (ENT-M08-L01), registrations in Kerala (ENT-M09-L02), funding (ENT-M08-L04)'),
    ('Growing in a job', 'Skills, results you can show, and asking for more', 'Any course that builds a skill your employer values'),
])}

### The money rules for extra income

1. **Separate it:** freelance or business money goes into a holding account (FIN-M03-L04), with tax and costs set aside from every payment.
2. **Know the tax:** small freelance incomes often owe no income tax under the new regime, but presumptive taxation, TDS refunds, advance tax and the GST threshold apply as income grows ({link('it-s58', 'section 58')}, {link('cbic-reg', 'GST registration')}; FIN-M10-L05).
3. **Use the raise rule:** at least half of any increase in income goes to your goals and emergency fund (Module 1).
4. **Budget for learning:** a course or tool that raises income can be a good use of money; calculate the payback first.

> **Payback in months = cost of the course or tool ÷ extra income per month it should bring**

A ₹6,000 course that realistically adds ₹2,000 a month pays back in 3 months. A ₹60,000 "trading mastery" course promising ₹1 lakh a month is a red flag, not an investment (Module 15).

### What doesn't grow income

- **"Business opportunities"** that need you to pay to join and recruit others (pyramid schemes, Module 15)
- **Task and "work from home" schemes** that ask for deposits
- **Trading futures and options as a "job"**: about 91% of individual traders lost money in 2024-25 ({link('sebi-fno', 'SEBI study')})
- **Borrowing to start** something you haven't tested with real customers

### Start small and test

Pick **one** path for the next 90 days. Do the smallest real test: one paying client, one product sold, one certification finished. Measure the result in rupees, then decide whether to grow it.
""",
    example=f"""
**Anu** earns about ₹14,000 a month from tuition while preparing for PSC exams. She looked at the four paths and chose one for the next 90 days, without hurting her PSC preparation: **freelance social media management for local shops**, using the Social Media Marketing course she had started.

Her 90-day plan: finish the course's earning module (SMM-M15), offer a ₹3,000-a-month starter package to two shops in Kakkattil (one already knew her from tuition), and track hours so her PSC study time stayed protected. Money rules: a second savings account as her holding account; 10% of every payment set aside for tax until she checks her position in FIN-M10-L05; half of the extra income to her emergency fund until it is full.

After 90 days she had one paying client (₹3,000 a month) and a case study. Her income rose by about 20%; her savings rate rose by more, because the new income followed her rules from day one.
""",
    resources=[
        ('ncfe', 'Revise the managing income and expenditure module with extra income in mind', '10 minutes'),
        ('it-s58', 'How small freelance and business income can be taxed (presumptive scheme)', '10 minutes'),
        ('cbic-reg', 'When GST registration becomes necessary', '5 minutes'),
        ('sebi-fno', 'Why trading derivatives is not an income plan', '5 minutes'),
    ],
    steps=[
        'Choose one income path for the next 90 days and write why it fits your time, skills and PSC plans.',
        'Open the matching course and module in this app and note the lessons you will use.',
        'Write the smallest real test you can do in 90 days, with a rupee target.',
        'Set your money rules for the extra income: holding account, tax set-aside, raise rule.',
        'Calculate the payback of any course or tool you plan to pay for.',
    ],
    proof='Your one-page income growth plan with the 90-day test, money rules and payback calculation, saved in 16 Income.',
    templates=[
        ('income growth plan (one page)', """
Path chosen: ____   Why it fits me: ____
Course and lessons in this app: ____
90-day test: ____ (e.g. 2 paying clients at ₹3,000 a month)
Hours per week, protected around PSC study: ____
Money rules: holding account ____ | tax set-aside ___% | ___% of extra income to goals
Spending on learning or tools: ₹____ ; payback =cost/extra_monthly_income = ____ months
Review date: ____  Result in rupees: ____  Next step: ____
""", ''),
    ],
    mistakes=[
        ('Chasing several paths at once.', 'One focused 90-day test teaches more than four half-started ideas.'),
        ('Spending extra income before it is regular.', 'Let extra income follow your rules for a few months first.'),
        ('Paying for "get rich" courses.', 'Calculate the payback; promises of huge incomes are a warning sign.'),
        ('Forgetting tax on side income.', 'Set aside a share of every payment and check your position in Module 10.'),
    ],
    quiz=[
        {'q': 'A ₹9,000 course should realistically add ₹3,000 a month. What is its payback period?', 'o': ['3 months', '9 months', '27 months', '1 month'], 'a': 'A', 'why': '₹9,000 ÷ ₹3,000 = 3 months.'},
        {'q': 'Where should freelance income go first?', 'o': ['A holding account, with tax and costs set aside', 'Straight into spending', 'Into F&O trading', 'Into a chitty'], 'a': 'A', 'why': 'The salary system from FIN-M03-L04 keeps irregular income under control.'},
        {'q': 'Which of these is NOT a real way to grow income?', 'o': ['Paying to join a scheme that rewards recruiting', 'Learning a skill clients pay for', 'Testing a small business with real customers', 'Earning a promotion with better skills'], 'a': 'A', 'why': 'Recruitment-based schemes are pyramids (Module 15).'},
        {'q': 'What is the course\'s rule for extra income?', 'o': ['At least half goes to goals and the emergency fund', 'Spend it all to enjoy it', 'Keep it secret', 'Invest it all in one stock'], 'a': 'A', 'why': 'The raise rule turns extra income into progress.'},
    ],
    study='The NCFE income module, presumptive taxation, the GST threshold and SEBI\'s F&O study',
    action='Write a one-page income growth plan with a 90-day test and money rules',
)

LESSONS = [L1]

MODULE = module(
    M,
    title='Growing income',
    weeks=(29, 29), hours=2,
    overview="""
Use the biggest lever in personal finance, your income, by choosing one realistic path for the next 90 days and setting money rules so extra income becomes progress.

This module is deliberately short, because the skills live in the other courses in this app: Practical Entrepreneurship for a business, Practical Social Media Marketing and the Free AI Generalist Course for freelancing, and your PSC preparation for a government job. Here you choose one path, plan a small real test, and connect it to your budget, tax and goals.

The result is a one-page income growth plan, which becomes part of your final financial plan.
""",
    outcomes=[
        'Choose one income path that fits your time and skills',
        'Plan a 90-day test with a rupee target',
        'Set money rules for extra income: holding account, tax set-aside, raise rule',
        'Judge courses and tools by their payback, and avoid "get rich" traps',
    ],
    lessons=LESSONS,
    project='My income growth plan',
    project_steps=[
        'Finish the one-page plan from FIN-M16-L01.',
        'Put the 90-day review date in your calendar.',
        'Add the expected extra income to your Cash Flow tab as a separate line, marked "planned".',
    ],
    project_proof='Your one-page income growth plan and the review date, saved in 16 Income.',
    rubric=[
        ('Path', 'None chosen', 'Several half-chosen', 'One path with a clear reason'),
        ('Test', 'Vague', 'A goal without numbers', 'A 90-day test with a rupee target'),
        ('Money rules', 'None', 'Some', 'Holding account, tax set-aside and raise rule written'),
    ],
    short=[
        'Write the path, the 90-day test and the money rules in five lines.',
    ],
    flashcards=[
        ('The biggest lever on a small income', 'Growing income.'),
        ('Payback of a course', 'Cost ÷ extra monthly income it should bring.'),
        ('First home for freelance income', 'A holding account, with tax and costs set aside.'),
        ('Not an income plan', 'Pyramid schemes, deposit-based "tasks" and F&O trading.'),
        ('Where to learn earning skills in this app', 'Entrepreneurship (ENT-M05, M08, M09), Social Media Marketing (SMM-M15), AI Generalist (Level 1, Capstone).'),
    ],
    mistakes=[
        ('Waiting for the perfect idea.', 'A small real test beats a perfect plan on paper.'),
        ('Letting side income disappear into lifestyle.', 'Apply the raise rule from the first payment.'),
    ],
    project_week=29,
)
