"""Module 12: Retirement and financial independence."""
import math
from common import lesson, module, link, fence, table, inr, ASOF, CHECK

M = 12

E_TODAY = 12000 * 12
YRS = 33
G, R_RET, N_RET = 0.05, 0.07, 25
E_60 = E_TODAY * (1 + G) ** YRS
CORPUS = E_60 * (1 - ((1 + G) / (1 + R_RET)) ** N_RET) / (R_RET - G) * (1 + R_RET)
_i = 0.08 / 12
_n = YRS * 12
LEVEL_SIP = CORPUS * _i / (((1 + _i) ** _n - 1) * (1 + _i))


def stepup_value(start, step=0.10, years=YRS):
    v, m = 0.0, start
    for _ in range(years):
        for _k in range(12):
            v = (v + m) * (1 + _i)
        m *= 1 + step
    return v


def stepup_start(target):
    lo, hi = 100.0, 100000.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if stepup_value(mid) < target:
            lo = mid
        else:
            hi = mid
    return hi


STEP_2000 = stepup_value(2000)
STEP_START = stepup_start(CORPUS)
COAST = CORPUS / 1.08 ** YRS


def years_to_fi(sr, real=0.05, mult=25):
    target = mult * (1 - sr)
    return math.log(target * real / sr + 1) / math.log(1 + real)


L1 = lesson(
    M, 1,
    title='How much is enough? Estimating your retirement corpus',
    weeks=(25, 25), hours=2,
    outcome='Estimate the retirement corpus you need from your own expenses, inflation and life expectancy, subtract expected pensions, and find the monthly saving, including a step-up plan.',
    split='25 minutes reading, 25 minutes resources, 70 minutes action',
    core=f"""
Retirement is the longest goal you will ever fund: 20 to 30 years of living costs, with no salary. It is also the goal most often left "for later". This lesson gives you a number and a monthly plan, so later becomes now.

### Step 1: retirement expenses in today's rupees

Start from your current essential and comfortable spending (Module 3), then adjust: no work travel or EMIs, possibly no rent, but **higher health costs**. Many people use 70–100% of current spending; use your own judgement and keep health in mind.

### Step 2: grow it to your retirement year

> **Yearly expense at retirement = monthly expense today × 12 × (1 + inflation) ^ years to retirement**

### Step 3: the corpus that pays it for life

You need enough to pay a rising expense (inflation continues) for the whole retirement, while the remaining money earns a return. A formula for a growing payment at the start of each year:

> **Corpus = E × (1 − ((1 + g) ÷ (1 + r)) ^ N) ÷ (r − g) × (1 + r)**

where E = first year's expense, g = inflation, r = return during retirement, N = years in retirement. (If r and g are equal, the corpus is simply E × N.)

**Worked example** (Anu, made-up, all assumptions): ₹12,000 a month today, retiring at 60 in {YRS} years, inflation 5%, a 7% return during retirement, 25 years of retirement (to 85).

- First-year expense at 60: ₹1,44,000 × 1.05^{YRS} = **{inr(E_60)}** a year.
- Corpus needed: about **{inr(CORPUS)}**, roughly {CORPUS / E_60:.0f} times the first year's expense.
- To reach it with a fixed monthly SIP at an assumed 8% a year for {YRS} years: about **{inr(LEVEL_SIP)} a month**.

### Step 4: subtract what pensions will pay

Pensions reduce the corpus you must build: a government pension, EPS pension from EPF, an NPS annuity, Atal Pension Yojana (FIN-M12-L02). Convert each expected pension to a yearly amount at retirement and subtract it from E before calculating the corpus.

### Step 5: start where you are, and step up

₹7,447 a month may be impossible today on Anu's income. That is normal. A **step-up SIP** starts smaller and raises the amount every year as income grows (the raise rule from Module 1):

- Starting at ₹2,000 a month and raising it 10% a year for {YRS} years grows to about **{inr(STEP_2000)}** at 8%.
- Starting at about **{inr(STEP_START)}** with 10% yearly increases reaches the full target.

### The honest caveats

Every number here depends on assumptions: inflation, returns, how long you live, health costs. Small changes move the answer a lot. So: use cautious assumptions, recalculate every year in your review, and treat the result as a direction, not a promise. The biggest risk isn't a wrong assumption; it is not starting.

### How long to plan for

Plan to at least 85, and test 90. Running out of money at 82 is far worse than leaving some behind.
""",
    example=f"""
**Fathima**, 31, did the calculation for herself: ₹18,000 a month today (including higher health costs later), retiring at 60, inflation 5%, 7% in retirement, to 88. The corpus came to about ₹2.2 crore in future rupees. Her first reaction: "Impossible."

Then she broke it down. Her PPF and NPS (FIN-M09-L04) would cover part of it. A step-up plan starting at ₹3,500 a month and rising 10% a year was within reach of her average income. And two levers made a big difference: retiring at 62 instead of 60, and keeping some freelance work in her early sixties. Her final plan: ₹3,500 a month now (PPF ₹2,000 and NPS ₹1,500), raised every April, and a yearly recalculation. "It's a big number," she wrote, "but it's a number I can walk towards."
""",
    resources=[
        ('openstax', 'Chapter 8, "Time Value of Money II: Equal Multiple Payments": the sections on annuities and growing annuities', '30 minutes'),
        ('ncfe', 'The long-term planning and pension module', '15 minutes'),
    ],
    steps=[
        'Make a **Retirement** tab with the template.',
        'Enter your monthly retirement expenses in today\'s rupees, your current age, retirement age and the age to plan to (at least 85).',
        'Enter cautious assumptions: inflation, return before retirement, return during retirement. Write why you chose them.',
        'Enter what you already have for retirement (EPF, PPF, NPS) and any expected pensions.',
        'Read the corpus and the monthly saving needed, both level and with a yearly step-up.',
        'Test two changes: retiring two years later, and a 1% lower return. Write how much each changes the answer.',
    ],
    proof='A screenshot of your Retirement tab with your assumptions, corpus, monthly saving (level and step-up) and the two tests, saved in 12 Retirement.',
    templates=[
        ('Retirement tab', """
INPUTS
B2: monthly expenses in retirement, today's ₹      B3: current age      B4: retirement age      B5: plan to age
B6: inflation (e.g. 0.05)    B7: return before retirement (e.g. 0.08)    B8: return in retirement (e.g. 0.07)
B9: retirement savings today (₹)    B10: expected yearly pensions at retirement, in today's ₹
CALCULATIONS
B12: years to retirement     =B4-B3
B13: years in retirement     =B5-B4
B14: first-year expense      =(B2*12-B10)*(1+B6)^B12
B15: corpus needed           =IF(B8=B6,B14*B13,B14*(1-((1+B6)/(1+B8))^B13)/(B8-B6)*(1+B8))
B16: today's savings grown   =B9*(1+B7)^B12
B17: still to build          =MAX(B15-B16,0)
B18: level monthly saving    =PMT(B7/12,B12*12,0,-B17,1)
STEP-UP CHECK (yearly table; A21 = year 1 ... ; C = monthly saving that year)
B21: starting monthly saving    C21: =B21    C22: =C21*1.10   (copy down for each year)
D21: value at year end          =FV($B$7/12,12,-C21,0,1)     D22: =D21*(1+$B$7/12)^12+FV($B$7/12,12,-C22,0,1)
Compare the last year's value with B17.
""", ''),
    ],
    mistakes=[
        ('Planning retirement in today\'s rupees.', 'Inflate expenses to the retirement year; prices may be several times higher.'),
        ('Planning to 75.', 'Plan to at least 85 and test 90.'),
        ('Using optimistic returns.', 'Use cautious returns; a plan that works with lower returns is a strong plan.'),
        ('Waiting for a bigger income.', 'Start small and step up; time matters more than the starting amount.'),
    ],
    quiz=[
        {'q': 'Why must retirement expenses be inflated to the retirement year?', 'o': ['Prices will be much higher by then', 'Banks require it', 'Expenses fall after retirement', 'It doesn\'t matter'], 'a': 'A', 'why': 'At 5% inflation, prices more than quadruple in 30 years.'},
        {'q': 'In the formula, what happens to the corpus if the return in retirement equals inflation?', 'o': ['Corpus = first-year expense × years in retirement', 'Corpus = 0', 'Corpus doubles', 'The formula can\'t be used at all'], 'a': 'A', 'why': 'With zero real return, you simply need N years of expenses.'},
        {'q': 'What is a step-up SIP?', 'o': ['A SIP that increases by a fixed percentage every year', 'A SIP that stops after a year', 'A loan for investing', 'A tax-saving deposit'], 'a': 'A', 'why': 'It starts smaller and grows with your income.'},
        {'q': 'To what age should a retirement plan usually run, at least?', 'o': ['85, and test 90', '65', '70', 'Retirement age only'], 'a': 'A', 'why': 'Running out of money late in life is the worst outcome.'},
    ],
    study='OpenStax chapter 8 on annuities and the NCFE long-term planning module',
    action='Build your Retirement tab, estimate your corpus and monthly saving, and test two changes',
)

FI_ROWS = [(f'{int(sr * 100)}%', f'about {years_to_fi(sr):.0f} years') for sr in (0.1, 0.2, 0.3, 0.4, 0.5, 0.6)]

L2 = lesson(
    M, 2,
    title='Pension options, and financial independence (FIRE)',
    weeks=(25, 25), hours=2,
    outcome='Compare the main pension sources in India, plan how to draw money in retirement, and understand FIRE with your own years-to-independence calculation.',
    split='25 minutes reading, 25 minutes resources, 70 minutes action',
    core=f"""
### Where retirement income can come from

{table(['Source', 'Who', 'What it gives', 'As of'], [
    ('Government pension', 'Government employees under the old pension or as decided for their scheme', 'Monthly pension with dearness relief (Module 14)', 'Check your scheme'),
    ('EPS pension (part of EPF)', 'EPF members', 'A monthly pension based on service and salary rules', 'Check with EPFO'),
    ('NPS annuity and lump sum', 'NPS subscribers', 'Non-government: up to 80% lump sum and at least 20% to buy an annuity at normal exit; full withdrawal if the corpus is ₹8 lakh or less', 'December 2025 rules'),
    ('Atal Pension Yojana (APY)', 'Ages 18–40 with a bank or post office account; not for income-tax payers (from October 2022)', 'Guaranteed ₹1,000 to ₹5,000 a month from 60, then to the spouse, then the corpus to the nominee', 'PFRDA FAQs'),
    ('Your own corpus', 'Everyone', 'PPF, deposits, SCSS (after 60), mutual funds, rent', 'Module 9'),
])}

Sources: {link('bs-nps-exit', 'NPS exit rules')}, {link('apy-faq', 'PFRDA APY FAQs')}, {link('indiapost', 'SCSS rate')}; {CHECK}.

**APY** is valuable for informal workers and low earners who don't pay income tax: small monthly contributions by auto-debit, a **guaranteed** pension amount. Its fixed pension doesn't rise with inflation, so it is a base, not the whole plan.

**Annuities** (the NPS annuity, or ones bought from insurers) turn a lump sum into a lifelong income. Most pay a fixed amount, which inflation erodes; compare the rates and options (with or without return of the purchase price to nominees) before choosing.

### Drawing money in retirement: the bucket idea

A simple way to manage a retirement corpus:

1. **Bucket 1, the next 2–3 years of expenses:** savings, FDs, SCSS and MIS (safe, income).
2. **Bucket 2, years 3–10:** debt options and some balanced investments.
3. **Bucket 3, after 10 years:** growth investments, to keep up with inflation.

Refill bucket 1 from the others once a year, taking from whichever has grown. This protects you from **selling growth investments in a crash** in the early years, the most damaging risk for new retirees.

### FIRE: Financial Independence, Retire Early

FIRE is a movement built on one idea: if your investments can pay your expenses for life, work becomes optional. Its common rule of thumb: you are financially independent when your investments reach about **25 to 33 times your yearly expenses** (a withdrawal rate of 4% to 3% a year). People who follow FIRE save 40–70% of income.

**The savings rate decides the timeline.** With a 5% real return and a 25× target, starting from zero:

{table(['Savings rate', 'Years to financial independence'], FI_ROWS)}

Variants: **Lean FIRE** (a frugal life), **Fat FIRE** (a comfortable one), **Coast FIRE** (save enough early that it grows to your retirement corpus by 60 with no further saving, then only cover current expenses), **Barista FIRE** (part-time work covers part of expenses).

**India-specific cautions:** health insurance without an employer (Module 7), inflation that has often been higher than in the countries where FIRE began, family responsibilities (parents, weddings, education), and the need to plan for 40+ years of retirement if you stop early.

Even if early retirement isn't your aim, the FIRE maths is useful: **a higher savings rate shortens every goal**, and "financial independence" can mean the freedom to choose work you like, take a break or survive a job loss.

**Worked example (Coast FIRE):** Anu's corpus target of {inr(CORPUS)} at 60 would be reached, at an assumed 8% a year, from about **{inr(COAST)} invested today** with nothing more added. She is far from that, but each ₹1 lakh she invests at 27 grows to about {inr(100000 * 1.08 ** YRS)} by 60 at that rate.
""",
    example=f"""
**Rahul** has a government job, so his retirement is partly covered by his pension scheme (Module 14), but the scheme's future is uncertain in Kerala as of 2026, so he planned as if it might give less than hoped. He added a personal corpus: NPS contributions through his job plus a small equity SIP.

His colleague **Joby**, 32, a software tester in Kozhikode, is attracted to FIRE. He earns well and lives with his parents. His savings rate is 45%, so the table suggests about 19 years to independence: around 51. Rahul asked him the India questions: health cover after leaving his job? His parents' care? A wedding? Joby added a family floater plus super top-up to his plan, kept his target at 33× expenses (a 3% withdrawal rate) instead of 25×, and called it "FI at 50, then choose".
""",
    resources=[
        ('apy-faq', 'Atal Pension Yojana: who can join, pension amounts, what happens after death, exit', '15 minutes'),
        ('bs-nps-exit', 'NPS exit and annuity rules from December 2025', '10 minutes'),
        ('protean-nps', 'Tax on the NPS lump sum', '5 minutes'),
        ('varsity', 'Module 17, "NPS: National Pension System": the chapters on exit and annuities', '30 minutes'),
    ],
    steps=[
        'List every pension source you have or can expect, with the rules from this lesson. Add their expected yearly amounts to your Retirement tab.',
        'If you (or a parent or relative under 40) don\'t pay income tax, check whether APY fits, and write the decision.',
        'Write your future bucket plan: what goes in each bucket at retirement.',
        'Calculate your own years to financial independence with the template, using your savings rate from Module 2.',
        'Write your position on FIRE in two sentences: what independence means for you, and the age or savings rate you are aiming for.',
    ],
    proof='Your pension sources list, bucket plan, years-to-FI calculation and FIRE statement, saved in 12 Retirement.',
    templates=[
        ('years to financial independence', """
B2: yearly expenses (₹)            B3: yearly savings (₹)
B4: investments today (₹)          B5: real return (e.g. 0.05)
B6: multiple (25 = 4% withdrawal, 33 = 3%)
B7: FI target (₹)                  =B2*B6
B8: years to FI                    =NPER(B5,-B3,-B4,B7)
B9: savings rate %                 =B3/(B2+B3)*100
Coast check: amount needed today to reach the target in N years at return r:  =B7/(1+r)^N
""", ''),
        ('bucket plan at retirement', """
Bucket 1 (years 1-3): ₹____ in ____ (savings, FDs, SCSS, MIS)
Bucket 2 (years 3-10): ₹____ in ____
Bucket 3 (10+ years): ₹____ in ____
Refill rule: once a year, top up Bucket 1 from ____
""", ''),
    ],
    mistakes=[
        ('Relying on one pension source.', 'Schemes change; combine a pension, your own corpus and safe income options.'),
        ('Treating a fixed annuity as inflation-proof.', 'A fixed pension buys less every year; keep growth assets for later years.'),
        ('Copying FIRE numbers from other countries.', 'Use Indian inflation, health and family costs, and a cautious withdrawal rate.'),
        ('Selling growth investments in a crash early in retirement.', 'The bucket method keeps 2–3 years of expenses safe so you never have to.'),
    ],
    quiz=[
        {'q': 'Who can join the Atal Pension Yojana, as of November 2026?', 'o': ['People aged 18–40 with a bank or post office account who don\'t pay income tax', 'Anyone over 60', 'Only government employees', 'Only income-tax payers'], 'a': 'A', 'why': 'Income-tax payers can\'t join from 1 October 2022 (check current rules).'},
        {'q': 'What does the FIRE rule of thumb of 25× yearly expenses correspond to?', 'o': ['A 4% yearly withdrawal rate', 'A 25% withdrawal rate', 'Retiring at 25', 'A 25% savings rate'], 'a': 'A', 'why': '1 ÷ 25 = 4%.'},
        {'q': 'Why keep 2–3 years of expenses in safe options in retirement?', 'o': ['So you never have to sell growth investments in a crash', 'They earn the most', 'Banks require it', 'To avoid all tax'], 'a': 'A', 'why': 'Selling after a crash early in retirement does lasting damage.'},
        {'q': 'According to the table, about how long to financial independence at a 50% savings rate?', 'o': ['About 17 years', 'About 51 years', 'About 5 years', 'Never'], 'a': 'A', 'why': 'Higher savings rates shorten the path sharply.'},
    ],
    study='APY rules, NPS exit and tax rules, and Varsity\'s NPS chapters on exit',
    action='List your pension sources, write a bucket plan and calculate your years to financial independence',
)

LESSONS = [L1, L2]

MODULE = module(
    M,
    title='Retirement and financial independence',
    weeks=(25, 25), hours=5,
    overview="""
Estimate how much you need to retire, what pensions will cover, and how much to save each month, and use the ideas of financial independence to see what a higher savings rate can buy you.

Retirement is decades away for many learners, which is exactly why it matters now: time does most of the work (Module 8). This module turns a vague worry into a number, then into a monthly plan you can start small and raise every year.

You also compare the pension sources in India (government pensions, EPS, NPS, APY, annuities) and learn a simple bucket method for drawing money safely in retirement. FIRE (Financial Independence, Retire Early) is explained honestly, with the cautions that matter in India. Your **Retirement** tab joins your final plan.
""",
    outcomes=[
        'Estimate a retirement corpus from your own expenses with inflation and life expectancy',
        'Subtract expected pensions and find the level and step-up monthly saving',
        'Compare government pensions, EPS, NPS, APY and annuities',
        'Plan retirement withdrawals with the bucket method',
        'Calculate your years to financial independence and explain FIRE\'s India-specific cautions',
    ],
    lessons=LESSONS,
    project='My retirement estimate and plan',
    project_steps=[
        'Complete the Retirement tab with cautious assumptions and your pension sources.',
        'Choose your monthly retirement saving: a starting amount and a yearly step-up, and the accounts it goes to (from FIN-M09-L04).',
        'Set up the standing instruction or SIP for the starting amount (even a small one), or write the date you will start.',
        'Write your FIRE statement and your target savings rate.',
        'Put "recalculate retirement" in your yearly review.',
    ],
    project_proof='Your Retirement tab, the chosen saving plan with proof of the first contribution (or the start date) and your FIRE statement, saved in 12 Retirement.',
    rubric=[
        ('Expenses', 'A guess', 'Today\'s rupees only', 'Inflated to the retirement year, with health costs considered'),
        ('Corpus', 'Not calculated', 'Calculated with optimistic numbers', 'Calculated with cautious assumptions and tested'),
        ('Pensions', 'Ignored', 'Listed', 'Listed with rules and subtracted from the need'),
        ('Saving plan', 'None', 'An amount', 'Starting amount, step-up and accounts, with the first contribution made'),
        ('Independence', 'Not considered', 'Read about FIRE', 'Own years-to-FI calculated and a savings-rate target set'),
    ],
    short=[
        'Calculate your corpus with the Retirement tab (FIN-M12-L01, steps 2–5).',
        'Start any amount for retirement, even ₹500 a month, with a 10% yearly step-up.',
        'Check APY eligibility if you don\'t pay income tax.',
    ],
    flashcards=[
        ('Corpus formula (growing withdrawals)', 'E × (1 − ((1+g)/(1+r))^N) ÷ (r − g) × (1 + r).'),
        ('Plan retirement to at least', 'Age 85, and test 90.'),
        ('Step-up SIP', 'A SIP raised by a fixed % every year as income grows.'),
        ('APY', 'Ages 18–40, non-taxpayers; guaranteed ₹1,000–5,000 a month from 60.'),
        ('NPS exit (non-government)', 'Up to 80% lump sum, at least 20% annuity; full withdrawal if corpus ≤ ₹8 lakh.'),
        ('FIRE target', '25–33 × yearly expenses (4%–3% withdrawal).'),
        ('Bucket method', 'Safe money for 2–3 years, medium-term money for 3–10, growth for later; refill yearly.'),
        ('Coast FIRE', 'Enough invested early to grow to your target by retirement with no more saving.'),
    ],
    mistakes=[
        ('Leaving retirement for later.', 'Each decade of delay roughly doubles the monthly saving needed.'),
        ('Assuming one scheme will cover everything.', 'Combine sources and plan your own corpus too.'),
        ('Forgetting health costs.', 'Medical costs rise with age; keep insurance and a health buffer in the plan.'),
    ],
    project_week=25,
)
