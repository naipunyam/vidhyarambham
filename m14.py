"""Module 14: Finance for a Kerala government employee."""
from common import lesson, module, link, fence, table, inr, ASOF, CHECK

M = 14

BASIC = 27000
DA_RATE = 0.37
DA = BASIC * DA_RATE
HRA = 1500
GROSS = BASIC + DA + HRA
CPS = round((BASIC + DA) * 0.10)
MEDISEP = 687
OTHER = 500
NET = GROSS - CPS - MEDISEP - OTHER

L1 = lesson(
    M, 1,
    title='Your pay slip decoded: basic pay, DA, deductions and SPARK',
    weeks=(27, 27), hours=2,
    outcome='Read a Kerala government pay slip line by line, track DA changes and arrears, and turn the take-home figure into your budget.',
    split='25 minutes reading, 25 minutes resources, 70 minutes action',
    core=f"""
This module is for the day your PSC result turns into an appointment order. If you aren't a government employee yet, do it as a "what-if" with a realistic entry post; it will make your first month in the job much easier. If a relative is a government employee, use their pay slip with permission.

### Earnings

- **Basic pay:** fixed by your post's pay scale and your stage in it; it rises with yearly increments and with pay revisions decided by government order.
- **Dearness allowance (DA):** a percentage of basic pay that compensates for price rises, revised by government order. Kerala raised **DA and dearness relief (for pensioners) from 35% to 37%** by an order dated 17 October 2026; the new DA came with the October salary paid in November 2026, and **arrears from 1 January 2026** are to follow by a separate order ({link('kl-da', 'Onmanorama, October 2026')}, {CHECK}).
- **House rent allowance (HRA)** and other allowances, depending on your post and place of work.

### Deductions

- **Pension contribution:** employees who joined from **1 April 2013** are in the **contributory pension scheme** (NPS) ({link('ml-cps', 'Moneylife')}); a share of basic pay plus DA is deducted, and the government also contributes (FIN-M14-L02). Employees in the older statutory pension contribute to the **General Provident Fund (GPF)** instead.
- **Medisep:** the state's health insurance scheme for employees and pensioners; the premium from February 2026 is **₹687 a month** (FIN-M14-L02).
- **Insurance schemes for employees,** such as the Group Personal Accident Insurance Scheme (GPAIS), whose policy year starts every January ({link('gpais', 'CUSAT circular')}); check the amounts on your pay slip.
- **Profession tax:** collected half-yearly through your employer for the local body; the maximum any state can levy is ₹2,500 a year ({link('kl-ptax', 'Kerala LSGD FAQs')}).
- **Income tax (TDS):** your drawing and disbursing officer (DDO) deducts it based on the regime you choose (Module 10).
- **Recoveries:** advances, loans from the government or from co-operative societies deducted from salary.

### A worked pay slip (made-up numbers except the DA rate and Medisep)

{table(['Line', 'Amount'], [
    ('Basic pay (made-up)', inr(BASIC)),
    (f'DA at {int(DA_RATE * 100)}% of basic', inr(DA)),
    ('HRA (made-up)', inr(HRA)),
    ('**Gross**', f'**{inr(GROSS)}**'),
    ('Pension contribution, 10% of basic + DA (check your slip)', f'−{inr(CPS)}'),
    ('Medisep premium', f'−{inr(MEDISEP)}'),
    ('Other insurance and small deductions (made-up)', f'−{inr(OTHER)}'),
    ('**Take-home** (before any income tax, profession tax months or recoveries)', f'**{inr(NET)}**'),
])}

### SPARK

**SPARK** is the Kerala government's payroll and service records system. Your pay slips, service details and several employee services, such as GPF nominations and closures, go through it ({link('ag-gpf', 'AG Kerala')}). Learn to read your own records there early, and keep personal details (bank account, nominees, address) correct.

### Budget on take-home, plan for arrears

Your budget starts from **take-home pay**, not gross. DA increases and arrears are **raises**: use the half-raise rule from Module 1 (at least half goes to your goals or emergency fund), and decide what the arrears will do **before** they arrive.
""",
    example=f"""
**Rahul** received his first full month's pay as an LD clerk and, like many new employees, felt confused by the slip. He copied every line into the pay slip tracker from this lesson. Three things became clear:

1. His take-home was about 20% below gross. He had budgeted on gross for a month before he noticed.
2. His pension deduction was going into the contributory pension scheme, because he joined after April 2013. He hadn't known that his pension would depend on those contributions and their returns (FIN-M14-L02).
3. Profession tax appeared only in some months; he added it to his sinking funds so those months didn't surprise him.

When the DA increase to 37% was announced in October 2026, his tracker showed the monthly rise (2% of his basic). He sent half of it to his emergency fund by standing instruction and decided that the DA arrears from January would go entirely to clearing his phone EMI and then his goals.
""",
    resources=[
        ('kl-da', 'The October 2026 DA and DR increase: rates and when they are paid', '10 minutes'),
        ('ml-cps', 'Why employees who joined from April 2013 are in the contributory pension scheme', '10 minutes'),
        ('ag-gpf', 'The AG Kerala GPF page, including what goes through SPARK', '15 minutes'),
        ('kl-ptax', 'Profession tax basics', '5 minutes'),
    ],
    steps=[
        'Get a pay slip: yours, a relative\'s (with permission and numbers covered), or build a what-if slip for the post you are preparing for, using a realistic basic pay from its notification.',
        'Make a **Pay Slip** tab with the template and enter every line.',
        'Check the DA line against the current DA rate; note any arrears due.',
        'Mark each deduction: savings (pension, GPF), insurance (Medisep, GPAIS), tax, or a loan recovery.',
        'Update your Budget tab so it starts from take-home pay, and write your plan for the next DA increase and any arrears.',
    ],
    proof='Your Pay Slip tab with every line classified, the DA check and your plan for DA increases and arrears, saved in 14 Govt job.',
    templates=[
        ('Pay Slip tab', """
B2: basic pay (₹)            B3: DA rate (e.g. 0.37)          B4: HRA (₹)        B5: other allowances (₹)
B6: DA (₹)                   =B2*B3
B7: gross (₹)                =B2+B6+B4+B5
B9: pension contribution     =ROUND((B2+B6)*0.10,0)     (or the GPF subscription, at least 6% of basic, if in GPF)
B10: Medisep (₹)             687
B11: GPAIS and other insurance (₹)
B12: profession tax this month (₹)     B13: income tax (TDS) this month (₹)     B14: recoveries (₹)
B15: total deductions        =SUM(B9:B14)
B16: take-home               =B7-B15
DA change check: new DA rate in B18 → monthly rise =B2*(B18-B3)
Arrears estimate: months due × monthly rise =B19*B2*(B18-B3)
""", ''),
    ],
    mistakes=[
        ('Budgeting on gross pay.', 'Your budget starts from take-home.'),
        ('Treating arrears as a bonus to spend.', 'Decide in advance; arrears are a perfect emergency fund or debt payoff boost.'),
        ('Ignoring pay slip errors.', 'Check every line every month; raise errors with your office early.'),
        ('Taking salary-recovery loans for wants.', 'Easy deductions from salary still cost interest and reduce take-home for years.'),
    ],
    quiz=[
        {'q': 'What was Kerala\'s DA rate after the October 2026 order?', 'o': ['37%', '35%', '50%', '12%'], 'a': 'A', 'why': 'It rose from 35% to 37%, with arrears from 1 January 2026 (check current rules).'},
        {'q': 'Basic pay ₹30,000 and DA rises by 2 percentage points. How much more DA per month?', 'o': ['₹600', '₹60', '₹2,000', '₹6,000'], 'a': 'A', 'why': '2% of ₹30,000 = ₹600.'},
        {'q': 'Kerala employees who joined service from 1 April 2013 are in which pension arrangement?', 'o': ['The contributory pension scheme', 'The old statutory pension with GPF only', 'No pension', 'The Atal Pension Yojana'], 'a': 'A', 'why': 'Kerala introduced the contributory pension scheme for employees joining from that date.'},
        {'q': 'Your budget should start from…', 'o': ['Take-home pay', 'Gross pay', 'Basic pay', 'Last year\'s DA'], 'a': 'A', 'why': 'Deductions never reach your account; plan with what does.'},
    ],
    study='The DA order report, the contributory pension background, the AG Kerala GPF page and profession tax basics',
    action='Decode a real or what-if pay slip in a Pay Slip tab and plan for DA increases and arrears',
)

L2 = lesson(
    M, 2,
    title='Pension, GPF, Medisep and your first-year money plan',
    weeks=(27, 27), hours=2,
    outcome='Understand where Kerala\'s pension arrangements stood in 2026, how GPF and Medisep work, and follow a first-year money plan for a new government job.',
    split='25 minutes reading, 25 minutes resources, 70 minutes action',
    core=f"""
### Pension: what is known, and what isn't, as of November 2026

- **Contributory pension (NPS) for those who joined from 1 April 2013:** the employee and the government contribute; the government's share is **10%**, and employee organisations have been demanding 14%, gratuity and a minimum pension ({link('kl-pension', 'Onmanorama, August 2026')}).
- **The Assured Pension Scheme (APS):** in March 2026, the then government gave in-principle sanction for an APS from 1 April 2026, with a pension of up to 50% of last basic pay (capped), dearness relief, and full pension after 30 years' qualifying service; new appointees were to choose between NPS and APS, and existing NPS members could switch ({link('kl-aps', 'Onmanorama, March 2026')}).
- **After the change of government:** an August 2026 report says the new UDF government announced that the earlier plans were cancelled and that the contributory scheme would be **reformed** instead; as of then, neither the reform nor the APS had been implemented, and there was **no option to move to the Centre's Unified Pension Scheme** ({link('kl-pension', 'Onmanorama, August 2026')}).

**What this means for your plan:** the rules may change again. Plan your retirement (Module 12) assuming your pension comes from your contributory account and its returns, and build an additional personal corpus. If a better guaranteed pension arrives, your plan simply becomes safer. **{CHECK.capitalize()}** before any decision such as switching schemes.

### GPF (for employees in pensionable service)

From the Accountant General (A&E) Kerala ({link('ag-gpf', 'AG Kerala')}, {CHECK}):

- For permanent employees in pensionable service (and others as the rules allow). If you are in the contributory scheme, ask your office whether GPF applies to you.
- Subscription of **at least 6% of basic pay**, up to the full basic pay; you can reduce it once and increase it twice a year.
- Interest at the rate the Government of India sets for GPF and Kerala adopts (**7.1%** in the recent periods shown on the page), credited at the end of the year. Interest on subscriptions above **₹5 lakh a year** is taxable.
- **Temporary advances** up to 75% of the balance; **non-refundable withdrawals** after 10 years' service or within 10 years of retirement.
- **Nominations and closure through SPARK** (family members only as nominees); the yearly account statement is on the AG's portal; report errors within 3 months. Help desk: 0471-2776650 / 0471-2330311.

### Medisep (phase 2 from 1 February 2026)

Kerala's medical insurance for state employees and pensioners: **₹5 lakh cover a year** (up from ₹3 lakh), premium **₹687 a month**, covering employees, pensioners, university and local body staff and dependants (about 32 lakh people), **with no age limit**; the insurer is Oriental Insurance, with 2,516 treatment packages, room rent up to ₹5,000 and cashless treatment at empanelled hospitals ({link('medisep2', 'Onmanorama, January 2026')}, {CHECK}). Check that your dependants are enrolled, and use the claim kit habits from FIN-M07-L05. Consider whether your family needs a super top-up above ₹5 lakh, and cover for any family members who aren't dependants under the scheme.

### Your first-year money plan

1. **Before joining:** a starter emergency fund; clear expensive debts (Module 6).
2. **First month:** decode your pay slip; set nominees for pension, GPF (if any), Medisep and insurance schemes through your office and SPARK; collect your Medisep card.
3. **Budget on take-home** with a half-raise rule for increments, DA and pay revisions (Module 1).
4. **Insurance:** Medisep is your health base. Add term cover if anyone depends on you (FIN-M07-L02). Say no to bundled policies sold at the office until you have calculated their return (FIN-M07-L01).
5. **Retirement:** start your own corpus alongside the pension contribution (Module 12).
6. **Tax:** choose your regime with your DDO using your calculator (FIN-M10-L02).
7. **Loans:** be careful with easy salary-recovery loans and co-operative loans for wants; they reduce take-home for years.
8. **Scams:** be wary of messages about "arrears", "pay fixation" or "pension portals" that ask for OTPs or payments (Module 15).
""",
    example=f"""
**Rahul's** first-year plan, written in his second month:

{table(['When', 'Action', 'Done?'], [
    ('Month 1', 'Pay slip decoded; nominees set through the office for pension, Medisep and GPAIS', 'Yes'),
    ('Month 2', 'Budget on take-home; emergency fund transfer ₹4,000 a month', 'Yes'),
    ('Month 3', 'Term cover compared (FIN-M07-L02); the office "investment-insurance plan" declined after calculating its return', 'Yes'),
    ('Month 4', 'Own retirement SIP started at ₹1,500 a month with 10% yearly step-up', 'Planned'),
    ('Every DA change', 'Half the rise to goals by standing instruction', 'Rule written'),
    ('Arrears', 'Phone EMI cleared, then emergency fund', 'Rule written'),
    ('Every year', 'Check the pension scheme news and Medisep renewal', 'In review checklist'),
])}

His colleague asked why he was saving separately for retirement "when the government gives a pension". Rahul showed her the two Onmanorama reports from March and August 2026: "Nobody knows yet what the final rules will be. My own corpus is the part I control."
""",
    resources=[
        ('kl-pension', 'The pension situation for Kerala employees as of August 2026', '15 minutes'),
        ('kl-aps', 'The Assured Pension Scheme announced in March 2026', '10 minutes'),
        ('ag-gpf', 'GPF rules: subscription, interest, advances, withdrawals, nominations', '15 minutes'),
        ('medisep2', 'Medisep phase 2: cover, premium, who is covered', '10 minutes'),
    ],
    steps=[
        'Write which pension arrangement applies to you (or to the post you are preparing for), and what is still uncertain.',
        'If you have or expect GPF, write your subscription plan (at least 6% of basic) and the advance/withdrawal rules you must remember.',
        'Check Medisep: are all your dependants enrolled? Is a top-up needed for your family? Add it to your Insurance tab.',
        'Fill in the first-year money plan template with dates, for your real job or a what-if.',
        'Add "pension scheme news, Medisep renewal and GPF statement" to your yearly review.',
    ],
    proof='Your pension note, GPF plan (if relevant), Medisep check and the first-year money plan, saved in 14 Govt job.',
    templates=[
        ('first-year money plan for a new government job', """
Before joining: starter emergency fund ₹____  | expensive debts cleared? ____
Month 1: pay slip decoded [ ]  nominees set (pension, GPF, Medisep, GPAIS) [ ]  Medisep card [ ]
Month 2: budget on take-home ₹____  | emergency fund transfer ₹____ on ____ (date)
Month 3: insurance: term cover needed? ____  | bundled office policies: return calculated ____
Month 4: own retirement saving ₹____ a month, step-up ___% a year, account ____
Tax: regime chosen with DDO: ____ (calculator result attached)
Rules: DA rise → ___% to goals | arrears → ____ | salary loans only for ____
Yearly: pension news, Medisep renewal, GPF statement, nominations
""", ''),
    ],
    mistakes=[
        ('Assuming the pension is settled.', 'As of 2026, Kerala\'s pension rules were still being debated. Build your own corpus too.'),
        ('Forgetting dependants in Medisep.', 'Check enrolment early, before anyone needs treatment.'),
        ('Saying yes to office insurance-investment plans.', 'Calculate the return first (FIN-M07-L01); most do both jobs badly.'),
        ('Using GPF advances for wants.', 'GPF is retirement money; use advances only for real needs.'),
    ],
    quiz=[
        {'q': 'As of the August 2026 report, what was the status of the Assured Pension Scheme announced in March 2026?', 'o': ['Not implemented; the new government said the contributory scheme would be reformed instead', 'Fully implemented for everyone', 'Replaced by the Centre\'s UPS', 'Never announced'], 'a': 'A', 'why': 'Neither the APS nor the reform had been implemented then (check current rules).'},
        {'q': 'What is the minimum GPF subscription, per AG Kerala?', 'o': ['6% of basic pay', '12% of gross pay', '₹500 a year', 'No minimum'], 'a': 'A', 'why': 'At least 6% of basic pay, up to the full basic pay.'},
        {'q': 'What does Medisep phase 2 cover from February 2026?', 'o': ['₹5 lakh a year for employees, pensioners and dependants, with no age limit', '₹1 lakh for employees only', 'Only accidents', 'Only pensioners over 80'], 'a': 'A', 'why': 'Cover rose from ₹3 lakh to ₹5 lakh, with a premium of ₹687 a month.'},
        {'q': 'Why should a new Kerala government employee build a personal retirement corpus too?', 'o': ['Pension rules were uncertain in 2026, and a personal corpus is the part they control', 'It is compulsory', 'GPF is closed', 'Medisep requires it'], 'a': 'A', 'why': 'Whatever the final scheme, an extra corpus makes the plan safer.'},
    ],
    study='The August 2026 and March 2026 pension reports, the AG Kerala GPF page and the Medisep phase 2 report',
    action='Write your pension note, GPF plan and Medisep check, and fill in the first-year money plan',
)

LESSONS = [L1, L2]

MODULE = module(
    M,
    title='Finance for a Kerala government employee',
    weeks=(27, 27), hours=5,
    overview="""
Prepare for the money side of a Kerala government job: read your pay slip, track DA and arrears, understand the pension situation honestly, use GPF and Medisep well, and follow a first-year plan.

If your PSC preparation succeeds, your first salary will be the biggest change in your money life. A government job brings stable income, DA increases, health cover through Medisep and retirement contributions, and also new traps: budgeting on gross pay, spending arrears, office insurance-investment plans and easy salary-recovery loans.

As of November 2026, Kerala's pension arrangements were in flux: a contributory scheme since 2013, an Assured Pension Scheme announced in March 2026, and a new government in August 2026 saying it would reform the contributory scheme instead. This module shows you how to plan sensibly under that uncertainty. If you aren't an employee yet, do it as a what-if; you'll thank yourself in your first month.
""",
    outcomes=[
        'Read every line of a Kerala government pay slip and budget on take-home pay',
        'Track DA changes and plan arrears with the half-raise rule',
        'Explain the 2026 pension situation and plan a personal corpus alongside it',
        'Use GPF and Medisep well, with nominations and dependants in order',
        'Follow a first-year money plan for a new government job',
    ],
    lessons=LESSONS,
    project='My government-job money plan (real or what-if)',
    project_steps=[
        'Complete the Pay Slip tab for your job or a what-if post.',
        'Write your pension note and your personal retirement saving plan.',
        'Complete the first-year money plan with dates.',
        'Update your Budget, Insurance and Retirement tabs with the pay slip numbers.',
        'Add the government-employee items to your yearly review checklist.',
    ],
    project_proof='The Pay Slip tab, pension note and first-year plan, saved in 14 Govt job.',
    rubric=[
        ('Pay slip', 'Not read', 'Earnings understood', 'Every line classified and budget based on take-home'),
        ('DA and arrears', 'No plan', 'Aware of DA', 'Rule for DA rises and arrears written'),
        ('Pension', 'Assumes it is settled', 'Knows the scheme name', 'Understands the 2026 uncertainty and plans a personal corpus'),
        ('GPF and Medisep', 'Unknown', 'Partly checked', 'Rules known, nominations and dependants checked'),
        ('First-year plan', 'None', 'A list', 'Dated plan with rules for loans and insurance offers'),
    ],
    short=[
        'Decode one pay slip (FIN-M14-L01).',
        'Write your pension note and start a small personal retirement saving (FIN-M14-L02).',
        'Check Medisep dependants and nominations.',
    ],
    flashcards=[
        ('Kerala DA and DR from the October 2026 order', '37% (from 35%), arrears from 1 January 2026.'),
        ('Contributory pension scheme in Kerala', 'For employees joining from 1 April 2013.'),
        ('Government contribution to the contributory scheme, 2026', '10% (employees have demanded 14%).'),
        ('Assured Pension Scheme status, August 2026', 'Announced in March 2026, not implemented; new government plans to reform the contributory scheme.'),
        ('GPF minimum subscription', '6% of basic pay.'),
        ('GPF nominations and closure', 'Through SPARK; family members only as nominees.'),
        ('Medisep phase 2', '₹5 lakh a year, ₹687 a month, no age limit, from 1 February 2026.'),
    ],
    mistakes=[
        ('Thinking a government job means no planning.', 'Stable income makes planning easier, not unnecessary.'),
        ('Letting lifestyle rise with every DA increase.', 'Use the half-raise rule every time.'),
        ('Ignoring pension news.', 'Check every year; decisions about switching schemes deserve careful reading.'),
    ],
    project_week=27,
)
