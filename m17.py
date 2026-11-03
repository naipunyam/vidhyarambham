"""Module 17: Capstone: your complete personal financial plan."""
from common import lesson, module, link, fence, table, inr, ASOF, CHECK

M = 17

L1 = lesson(
    M, 1,
    title='Write your Investment Policy Statement',
    weeks=(30, 30), hours=2,
    outcome='Write a one-to-two-page Investment Policy Statement: your goals, risk profile, target allocation, allowed and banned options, selection rules, contributions, rebalancing and behaviour rules, signed and dated.',
    split='20 minutes reading, 20 minutes resources, 80 minutes action',
    core=f"""
An **Investment Policy Statement (IPS)** is a short document of rules you write for yourself **when you are calm**, so you follow them when markets, friends or salespeople make you excited or afraid. Professional fund managers and pension funds use them. You need one more than they do, because nobody checks your decisions.

You already have almost everything from earlier modules. This lesson puts it in one place.

### The ten parts of a personal IPS

1. **Purpose:** what this money is for (your goals by horizon, from Modules 2, 11 and 12).
2. **Risk profile:** your capacity and tolerance scores and the profile you use (FIN-M08-L02).
3. **Target allocation** for each horizon, with allowed ranges (FIN-M08-L03).
4. **Allowed options** for each job: safety, income, growth, diversifiers (your Shortlist from Module 9).
5. **Banned options:** what you won't do, such as F&O trading, unregistered tips, unregulated "digital gold", schemes promising fixed high returns, borrowing to invest (Modules 9 and 15).
6. **Selection rules:** for example, direct plans only; index funds for core equity; an expense ratio limit; only SEBI-registered advisers paid by fee; check every product's regulator ({link('amfi-direct', 'AMFI on direct plans')}, {link('sebi-risko', 'SEBI riskometer')}).
7. **Contributions:** monthly amounts, dates, accounts and the yearly step-up (Module 12).
8. **Rebalancing rule:** date, drift limit and "new money first" (FIN-M08-L03).
9. **Behaviour rules:** what you will do in a market fall ("nothing for 30 days, then follow the rebalancing rule"), with windfalls ("wait 30 days, then follow the allocation"), with tips ("check registration, then ignore"), with a new product ("five questions and 24 hours").
10. **Review:** when you will review the IPS (yearly), and the life events that trigger a review (marriage, job change, a big windfall), plus when you will consult a SEBI-registered investment adviser ({link('sebi-ia-list', 'SEBI list')}).

### Keep it short and specific

Two pages at most. Every rule should be checkable: "Equity 50% ± 5%" is checkable; "moderate risk" is not. Sign and date it, and keep it in your Money Folder and on paper.

### The crash rule matters most

Markets fall sharply from time to time. People lose the most money not in the fall itself but by selling near the bottom and missing the recovery. Writing your crash rule now, with your long-term horizon in front of you, is the most valuable sentence in your IPS.
""",
    example=f"""
**Anu's** IPS (summary of her two pages):

{table(['Part', 'Anu\'s rule'], [
    ('Purpose', 'Emergency fund and short goals (safe); retirement from age 27 (long-term)'),
    ('Profile', 'Balanced (capacity 10, tolerance 11)'),
    ('Allocation, long-term money', 'Equity 50% (45–55%), debt 45% (PPF), gold 5% (gold ETF or fund)'),
    ('Allowed', 'Post office RD and TD, bank FDs within ₹5 lakh per bank, PPF, a broad equity index fund (direct plan), a gold ETF or fund'),
    ('Banned', 'F&O, tips from unregistered people, digital gold apps, private chitties, crypto, any scheme promising fixed high returns, loans to invest'),
    ('Selection', 'Direct plans; index funds with low expense ratios and long tracking records; check the regulator every time'),
    ('Contributions', '₹1,000 PPF and ₹1,000 index fund SIP monthly from the 5th; +10% every April'),
    ('Rebalancing', '1 April each year; act if drift > 5 points; new money first'),
    ('Crash rule', 'If markets fall 20% or more: do nothing for 30 days, keep the SIP going, then rebalance by rule'),
    ('Review', 'Every April; also after a PSC job offer, marriage or any windfall over ₹50,000'),
])}

She printed it, signed it, and asked her money buddy to sign as a witness, "so I'm embarrassed to break it".
""",
    resources=[
        ('amfi-direct', 'Revise direct plans for your selection rules', '5 minutes'),
        ('sebi-risko', 'Revise the riskometer for your risk rules', '5 minutes'),
        ('sebi-investor', 'Skim SEBI\'s investor guides for any rule you want to add', '10 minutes'),
    ],
    steps=[
        'Collect your inputs: Goals tab, risk profile, Allocation tab, the Shortlist from Module 9, your Retirement plan and your rules from Modules 9 and 15.',
        'Write your IPS using the template, in your own words, with every rule checkable.',
        'Write your crash rule and your windfall rule with special care.',
        'Read it aloud to your money buddy or a family member and change anything that is unclear.',
        'Sign and date it; save it in 17 Plan and keep a printed copy.',
        'Set up or adjust the contributions it describes, if you haven\'t already.',
    ],
    proof='Your signed and dated Investment Policy Statement (PDF or photo), saved in 17 Plan.',
    templates=[
        ('Investment Policy Statement', """
MY INVESTMENT POLICY STATEMENT    Name: ____    Date: ____    Next review: ____
1. PURPOSE: short goals (under 3 years): ____ | medium (3-7): ____ | long (over 7): ____
2. RISK PROFILE: capacity __/15, tolerance __/15 → profile: ____
3. TARGET ALLOCATION (long-term money): equity ___% (range __-__) | debt ___% | gold ___% | cash ___%
   Medium-term money: ____    Short-term money: safe options only
4. ALLOWED: safety ____ | income ____ | growth ____ | diversifiers ____
5. BANNED: ____ (e.g. F&O, unregistered tips, unregulated digital gold, schemes promising fixed high returns, borrowing to invest)
6. SELECTION RULES: direct plans [ ] expense ratio below ___% [ ] regulator checked [ ] advisers SEBI-registered and fee-only [ ]
7. CONTRIBUTIONS: ₹____ to ____ on the __th; ₹____ to ____ ; step-up ___% every ____
8. REBALANCING: every ____ ; if drift > ___ points; new money first
9. BEHAVIOUR: in a crash: ____ | windfalls: ____ | tips: ____ | new products: five questions + 24 hours
10. REVIEW: yearly in ____ ; also after: ____ ; consult a SEBI RIA when: ____
Signed: ____    Witness (optional): ____
""", ''),
    ],
    mistakes=[
        ('Writing vague rules.', '"Be careful" can\'t be checked. "Equity 50% ± 5%" can.'),
        ('Copying someone else\'s IPS.', 'Your goals, profile and family are yours; the rules must be too.'),
        ('Skipping the crash rule.', 'It is the rule you will need most, at the moment you least want to think.'),
        ('Never reading it again.', 'Read it before every investment decision and at every yearly review.'),
    ],
    quiz=[
        {'q': 'What is an Investment Policy Statement?', 'o': ['Your written rules for investing, made calmly in advance', 'A bank statement', 'A tax form', 'A list of hot stocks'], 'a': 'A', 'why': 'It guides decisions when emotions run high.'},
        {'q': 'Which is a checkable IPS rule?', 'o': ['Equity 50%, allowed range 45–55%', 'Invest wisely', 'Take moderate risk', 'Avoid bad funds'], 'a': 'A', 'why': 'You can measure it and know when to act.'},
        {'q': 'Why write a crash rule in advance?', 'o': ['Fear in a fall leads to selling near the bottom', 'Crashes never happen', 'Banks require it', 'To pay less tax'], 'a': 'A', 'why': 'A rule written calmly beats a decision made in panic.'},
        {'q': 'Which belongs in the "banned" section for most beginners, per this course?', 'o': ['F&O trading and schemes promising fixed high returns', 'PPF', 'Direct index funds', 'Post office deposits'], 'a': 'A', 'why': 'Modules 9 and 15 showed their risks.'},
    ],
    study='Revision of direct plans, the riskometer and SEBI\'s investor guides',
    action='Write, sign and date your Investment Policy Statement',
)

L2 = lesson(
    M, 2,
    title='Your one-page financial plan',
    weeks=(30, 30), hours=2.5,
    outcome='Pull every module\'s work into a one-page financial plan with live numbers from your Money Workbook and a dated list of actions for the next 12 months.',
    split='15 minutes reading, 15 minutes resources, 120 minutes action',
    core=f"""
Your Money Workbook now holds everything: budget, net worth, goals, emergency fund, debts, insurance, allocation, tax, retirement, documents and more. A **one-page plan** puts the most important numbers and decisions where you, and your family, can see them at a glance.

### What goes on the page

{table(['Section', 'What to show', 'Comes from'], [
    ('Where I am', 'Net worth, liquid net worth, monthly take-home, savings rate', 'Modules 2 and 3'),
    ('Protection', 'Emergency fund (target, current, months covered); life, health and accident cover', 'Modules 5 and 7'),
    ('Debt', 'Total debt, payoff order, debt-free date, credit report checked on', 'Module 6'),
    ('Goals', 'Top goals with amounts, dates, monthly saving and progress', 'Modules 2, 11 and 12'),
    ('Investing', 'Allocation now vs target; IPS signed on; contributions', 'Modules 8, 9 and 17'),
    ('Tax', 'Regime, expected tax, due dates', 'Module 10'),
    ('Estate', 'Nominations checked on, will status, money file location', 'Module 13'),
    ('Safety', 'Scam-proof habits done, family briefing date', 'Module 15'),
    ('Income', '90-day income plan and result', 'Module 16'),
    ('Next 12 months', 'Five to eight dated actions', 'This lesson'),
])}

### Live numbers, not copies

Make a **Plan** tab whose numbers come from the other tabs by formula, so it stays current when you update them. In Google Sheets a reference to another tab looks like `='Net Worth'!I4`; in LibreOffice it looks like `=$'Net Worth'.I4`. The safest way in both is to type `=`, click the other tab's cell, and press Enter.

### The next 12 months

The most important part of the plan is the action list: what you will do, by when. Good actions are specific and small: "Raise SIP by 10% on 5 April", "Renew parents' health policy by 12 March with a super top-up", "File ITR by 15 July", "Family scam briefing at Onam".

### Share it

Show the plan to the people it affects: a spouse, parents, your money buddy. A plan that your family understands is a plan that survives a crisis.
""",
    example=f"""
**Rahul's** one-page plan, at the end of the course (made-up numbers):

{table(['Section', 'Rahul'], [
    ('Where I am', 'Net worth ₹2.9 lakh (liquid ₹96,000); take-home ₹30,600; savings rate 24%'),
    ('Protection', 'Emergency fund ₹62,000 of ₹99,000 (3.8 months); Medisep for him and parents; term cover ₹25 lakh chosen, buying in January; PMSBY'),
    ('Debt', 'Phone EMI cleared with arrears; sister\'s education loan as co-borrower from 2030; card paid in full monthly; report checked in May'),
    ('Goals', 'Emergency fund by July; two-wheeler in 2028 (₹2,800/month RD); house decision in 2029'),
    ('Investing', 'IPS signed 4 November; contributory pension plus ₹1,500 SIP, +10% yearly; allocation 55/40/5'),
    ('Tax', 'New regime; tax ₹0 this year; ITR by 31 July; AIS check in June'),
    ('Estate', 'Nominations checked September; will "after marriage"; money file with sister'),
    ('Safety', 'Habits checklist done; family briefing at Onam'),
    ('Income', 'Department exam for promotion in 2027'),
    ('Next 12 months', 'Term policy (Jan); emergency fund full (Jul); ITR (Jul); SIP step-up (Apr); yearly review (Nov)'),
])}

He printed it, put it on the inside of his cupboard door, and gave a copy to his sister.
""",
    resources=[
        ('ncfe', 'Optional revision: retake the NCFE course quizzes you found hardest', '15 minutes'),
    ],
    steps=[
        'Make a **Plan** tab with the template headings.',
        'Link each number by formula from its tab, so it updates itself.',
        'Write the short text parts: protection, debt plan, estate status, safety, income plan.',
        'Write five to eight dated actions for the next 12 months and add them to your calendar.',
        'Print or save the page as a PDF, and share it with the people it affects.',
    ],
    proof='Your one-page plan (PDF or screenshot of the Plan tab, private numbers covered if you share it) and the calendar entries for its actions, saved in 17 Plan.',
    templates=[
        ('one-page plan (Plan tab)', """
MY FINANCIAL PLAN    Updated: ____
WHERE I AM: net worth ='Net Worth'!I4 | liquid ='Net Worth'!I7 | take-home ____ | savings rate ____%
PROTECTION: emergency fund =Emergency!B6 of =Emergency!B4 (=Emergency!B7 %) | life cover ____ | health cover ____ | accident ____
DEBT: total ____ | order ____ | debt-free by ____ | credit report checked on ____
GOALS (top 3): ____ ₹____ by ____ (₹____/month) | ____ | ____
INVESTING: IPS signed on ____ | allocation now __/__/__ vs target __/__/__ | contributions ₹____/month
TAX: regime ____ | expected tax ₹____ | ITR due ____
ESTATE: nominations checked ____ | will ____ | money file at ____ (who knows: ____)
SAFETY: habits checklist ____ | family briefing on ____
INCOME: 90-day plan ____ | result ____
NEXT 12 MONTHS: 1. ____ by ____  2. ____  3. ____  4. ____  5. ____
(Links: type = then click the other tab's cell; LibreOffice shows it as $'Sheet name'.A1)
""", ''),
    ],
    mistakes=[
        ('Typing numbers into the plan by hand.', 'Link them, so the plan updates itself.'),
        ('A plan with no dates.', 'Every action needs a month; put them in your calendar.'),
        ('Keeping the plan secret.', 'Share it with the people it affects.'),
        ('Waiting for perfect numbers.', 'A good plan now, improved yearly, beats a perfect plan never finished.'),
    ],
    quiz=[
        {'q': 'Why link the Plan tab\'s numbers by formula?', 'o': ['So the plan updates when the other tabs change', 'To hide the numbers', 'Because typing is not allowed', 'To make the file bigger'], 'a': 'A', 'why': 'A plan that updates itself stays useful.'},
        {'q': 'What is the most important part of the one-page plan?', 'o': ['The dated actions for the next 12 months', 'The colours', 'The font', 'Last year\'s returns'], 'a': 'A', 'why': 'Actions with dates are what change your money.'},
        {'q': 'Which is a good action for the plan?', 'o': ['Raise SIP by 10% on 5 April', 'Save more', 'Be better with money', 'Invest wisely'], 'a': 'A', 'why': 'It is specific and dated.'},
    ],
    study='Optional revision of the NCFE quizzes you found hardest',
    action='Build your one-page plan with linked numbers and dated actions, and share it',
)

L3 = lesson(
    M, 3,
    title='The yearly money review: keeping the system running',
    weeks=(31, 31), hours=1.5,
    outcome='Run a complete yearly money review with a checklist, record it in a review log, and schedule your monthly, quarterly and yearly routines.',
    split='15 minutes reading, 15 minutes resources, 60 minutes action',
    core=f"""
A financial plan is not a document; it is a habit. Rules change, your life changes and markets move. A short yearly review keeps your plan true. Choose **one month** you will review every year (many people choose the month after their birthday, or April, when the tax year starts) and protect one weekend for it.

### The yearly review checklist

**Numbers**
1. Net worth and liquid net worth, compared with last year
2. A year of cash flow: income, spending, savings rate
3. Budget: categories that drifted; adjust the plan

**Protection**
4. Emergency fund: still the right size for this year's essential expenses?
5. Insurance: renewals, cover amounts (life, health for you and parents, accident, vehicle, home); any new dependants?
6. Free credit reports: download from a different bureau each time (FIN-M06-L04)

**Debt and goals**
7. Debts: progress against the payoff plan; any new debt and why
8. Goals: costs, dates and monthly savings updated; anything achieved, dropped or added

**Investing and retirement**
9. Allocation against the IPS; rebalance by rule
10. Retirement estimate recalculated; contributions stepped up
11. IPS reread; anything to change after a life event

**Tax and rules**
12. Tax regime choice for the new year; ITR due date and AIS check; advance tax if needed
13. Rule changes this year: the Union Budget (usually 1 February), small savings rates (every quarter), RBI decisions, SEBI and IRDAI changes; for Kerala government employees: DA orders, pension scheme news, Medisep renewal, GPF statement

**Estate and safety**
14. Nominations on every account; will; family money file updated
15. Family scam briefing; scam-proof habits checklist

**Income and next year**
16. Income growth: what worked, next 90-day test
17. The one-page plan updated, with next year's dated actions

### Smaller routines

- **Monthly (30 minutes):** the money review from the habits track: numbers, budget vs actual, one decision.
- **Quarterly (1 hour):** check small savings rates ({link('indiapost', 'India Post')}), your CAS ({link('amfi-cas', 'AMFI')}), AIS for TDS ({link('it-ais', 'AIS')}) and allocation drift.

### Keep a review log

One row per review: date, net worth, savings rate, the three biggest changes, and the decisions you made. In five years, this log will be the best record of how far you have come.
""",
    example=f"""
**Fathima** chose November for her yearly review, because her freelance work is quieter then. Her first review, at the end of this course, took four hours over a weekend:

- Net worth up from −₹40,000 (her two-wheeler loan) a year ago to ₹1,85,000.
- Savings rate 26% on average, despite two slow months, thanks to the holding account.
- Rule changes she noted: new EPF withdrawal rules didn't affect her; NPS exit rules from December 2025 did; she reread them.
- Insurance: her mother's health policy renewed with a super top-up added; her own term cover deferred until marriage, with a note to revisit.
- Credit report: from a second bureau this time; clean.
- Decisions: raise PPF to ₹2,500 a month, keep the IPS unchanged, hold the family scam briefing at Christmas.

She added one row to her review log and booked the same weekend for next November.
""",
    resources=[
        ('indiapost', 'The small savings rates to check every quarter', '5 minutes'),
        ('amfi-cas', 'How to get your consolidated account statement for the review', '5 minutes'),
        ('it-ais', 'Opening your AIS before filing', '5 minutes'),
    ],
    steps=[
        'Choose your yearly review month and block a weekend in your calendar, repeating every year.',
        'Add a **Review Log** to your Review tab with the template columns.',
        'Do a first full yearly review now with the checklist (it is the end of your course year); write the first log row.',
        'Put the monthly money date and the four quarterly checks in your calendar as repeating events.',
        'Save the checklist in your Money Folder and on your phone.',
    ],
    proof='Your first completed yearly review checklist, the first review log row and screenshots of the repeating calendar events, saved in 17 Plan.',
    templates=[
        ('yearly review checklist', """
YEARLY MONEY REVIEW    Date: ____
NUMBERS:      [ ] net worth  [ ] cash flow and savings rate  [ ] budget adjusted
PROTECTION:   [ ] emergency fund size  [ ] insurance renewals and cover  [ ] free credit report (bureau: ____)
DEBT, GOALS:  [ ] payoff progress  [ ] goals updated
INVESTING:    [ ] allocation vs IPS, rebalanced?  [ ] retirement recalculated, step-up done  [ ] IPS reread
TAX, RULES:   [ ] regime for the new year  [ ] ITR date and AIS  [ ] Budget and other rule changes noted
              [ ] (govt employee) DA, pension news, Medisep, GPF statement
ESTATE, SAFETY: [ ] nominations  [ ] will  [ ] money file  [ ] family scam briefing
INCOME:       [ ] last 90-day test result  [ ] next test
PLAN:         [ ] one-page plan updated with next year's dated actions
""", ''),
        ('review log', """
Date,Net worth (₹),Liquid net worth (₹),Savings rate %,Emergency fund months,Debt (₹),Biggest changes this year,Decisions for next year
""", 'csv'),
    ],
    mistakes=[
        ('Reviewing only when things go wrong.', 'Fix the month in advance; regular reviews catch problems early.'),
        ('Changing the IPS after a good or bad market year.', 'Change it for life events, not for market moods.'),
        ('Ignoring rule changes.', 'Tax, savings rates and scheme rules change; note them every year.'),
        ('Skipping the log.', 'The log turns years of small steps into visible progress.'),
    ],
    quiz=[
        {'q': 'How often does the course suggest a full money review?', 'o': ['Once a year, in a fixed month', 'Every day', 'Only when markets fall', 'Every five years'], 'a': 'A', 'why': 'A fixed yearly review plus short monthly and quarterly checks.'},
        {'q': 'When should you change your IPS?', 'o': ['After life events such as marriage, a job change or a big windfall', 'After every market fall', 'After a friend\'s tip', 'Every month'], 'a': 'A', 'why': 'The IPS follows your life, not market moods.'},
        {'q': 'Which is a quarterly check in the course routine?', 'o': ['Small savings rates, CAS, AIS and allocation drift', 'Writing a will', 'Changing your bank', 'Buying insurance'], 'a': 'A', 'why': 'These change during the year and take an hour to check.'},
    ],
    study='The quarterly check sources: India Post rates, the CAS and AIS',
    action='Schedule your routines, run your first yearly review and start the review log',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    M,
    title='Capstone: your complete personal financial plan',
    weeks=(30, 31), hours=8,
    overview="""
Bring everything together: a signed Investment Policy Statement, a one-page financial plan with live numbers and dated actions, and a yearly review routine that keeps it all working.

Over 31 weeks you have built every part of a personal financial plan on your own money: a budget system, a net-worth tracker, an emergency fund, a debt plan, insurance checks, investment rules, a tax checklist, retirement and goal plans, an estate file and scam-proof habits. The capstone turns those parts into a system you can run for the rest of your life.

Write your Investment Policy Statement, build the one-page plan that pulls numbers from every tab, and run your first yearly review. Then finish the course with the final self-assessment.
""",
    outcomes=[
        'Write and sign a personal Investment Policy Statement',
        'Build a one-page financial plan with linked numbers and dated actions',
        'Run a complete yearly money review and keep a review log',
        'Schedule monthly, quarterly and yearly money routines',
        'Explain your plan to the people it affects',
    ],
    lessons=LESSONS,
    project='My complete personal financial plan',
    project_steps=[
        'Check that every tab in your Money Workbook is filled in and dated: Expenses, Baseline, Values, Goals, Net Worth, Cash Flow, Budget, Accounts, Emergency, Debts, Insurance, Calculators, Allocation, Funds, Tax, Big Goals, Retirement, Documents, Pay Slip (if relevant), Scam Check, Plan and Review.',
        'Attach your signed IPS and your one-page plan.',
        'Present the plan to your money buddy or family in 15 minutes: where you started (your week 0 snapshot), where you are, and the next 12 months.',
        'Write a short reflection: the three most valuable changes the course made to your money, and one thing still to improve.',
        'Do the final self-assessment and toolkit checklist on the next page.',
    ],
    project_proof='Your complete Money Workbook (downloaded copy), signed IPS, one-page plan and reflection, saved in 17 Plan.',
    rubric=[
        ('Completeness', 'Several parts missing', 'Most parts present', 'Every part present, dated and consistent'),
        ('IPS', 'Not written', 'Written but vague', 'Signed, specific, with crash and windfall rules'),
        ('One-page plan', 'None', 'Typed numbers, no actions', 'Linked numbers and dated actions in the calendar'),
        ('Routine', 'None', 'Intentions', 'Monthly, quarterly and yearly routines scheduled; review log started'),
        ('Shared', 'Kept private', 'Mentioned', 'Presented to the people it affects'),
    ],
    short=[
        'Write the IPS with at least allocation, banned options and the crash rule (FIN-M17-L01).',
        'Fill in the one-page plan, even with some numbers typed (FIN-M17-L02).',
        'Book next year\'s review weekend (FIN-M17-L03).',
    ],
    flashcards=[
        ('Investment Policy Statement', 'Your written investing rules: goals, profile, allocation, allowed and banned options, contributions, rebalancing, behaviour, review.'),
        ('The crash rule', 'What you will do (and not do) when markets fall sharply, written in advance.'),
        ('One-page plan', 'Key numbers linked from your workbook plus dated actions for 12 months.'),
        ('Yearly review', 'One fixed month: numbers, protection, debt, goals, investing, tax and rules, estate, safety, income, plan.'),
        ('Quarterly checks', 'Small savings rates, CAS, AIS and allocation drift.'),
        ('Monthly check', 'The 30-minute money review with one decision.'),
    ],
    mistakes=[
        ('Treating the plan as finished.', 'It is a living system; the review keeps it true.'),
        ('Changing everything after the course.', 'Keep the routines simple enough to keep for decades.'),
        ('Forgetting why you started.', 'Reread your week 0 three sentences at every yearly review.'),
    ],
    project_week=31,
)
