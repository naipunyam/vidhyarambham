"""Module 2: Goals and tracking."""
from common import lesson, module, link, fence, table, inr, ASOF, CHECK

M = 2

# ---- worked numbers, computed so they are always right
def fv(pv, rate, years):
    return pv * (1 + rate) ** years


def pmt_needed(target, annual_rate, months):
    """Monthly saving (end of month) to reach target."""
    r = annual_rate / 12
    if r == 0:
        return target / months
    return target * r / ((1 + r) ** months - 1)


BIKE_TODAY = 120000
BIKE_FUTURE = fv(BIKE_TODAY, 0.05, 3)
BIKE_PMT = pmt_needed(BIKE_FUTURE, 0.065, 36)
BIKE_PMT_NOINT = BIKE_FUTURE / 36

L1 = lesson(
    M, 1,
    title='Money goals that work',
    weeks=(3, 3), hours=1.5,
    outcome='Write your money goals with an amount, a date and a priority, adjust each for inflation, and work out the monthly saving each one needs.',
    split='25 minutes reading, 25 minutes resources, 40 minutes action',
    core=f"""
"I want to save more" is a wish. "₹1,40,000 for a two-wheeler by November 2029, saving ₹3,500 a month" is a goal. A goal you can act on has five parts:

1. **What:** a clear thing, such as an emergency fund, a two-wheeler, a wedding, a house down payment, a course, retirement.
2. **How much, today:** the price in today's rupees. Find a real quote, not a guess.
3. **When:** a month and year.
4. **How much, then:** today's price grown by inflation to that date.
5. **Monthly saving:** what you must put aside each month to get there.

### Short, medium and long goals

{table(['Type', 'When', 'Examples', 'Where the money usually waits (Module 9)'], [
    ('Short', 'Within 3 years', 'Emergency fund, phone, course fees, festival and function costs', 'Savings account, FDs, RDs: safe, low growth'),
    ('Medium', '3 to 7 years', 'Vehicle, wedding, house down payment', 'A mix of safe and some growth investments'),
    ('Long', 'More than 7 years', 'Children\'s education, retirement', 'More growth investments, because there is time to recover from falls'),
])}

### The priority order

Goals compete for the same rupees. A safe order for most people:

1. **A starter emergency fund** (Module 5): even one month of expenses stops small shocks becoming debt.
2. **Health and life cover** where needed (Module 7): one hospital bill can wipe out years of saving.
3. **Pay off expensive debt** (Module 6): credit-card and app-loan interest is higher than any safe investment earns.
4. **Full emergency fund**, then your other goals, with retirement started early, even if small.

### Inflation makes goals bigger

Prices rise over time. India's target for consumer price inflation is 4%, with a band of 2% to 6%, until March 2031 ({link('om-target', 'Outlook Money, March 2026')}). Some costs, such as education and medical care, often rise faster than average. For planning, use an assumed rate and change it if it proves wrong; this course uses 5% for general goals and 7% for education in examples. These are assumptions for practice, not forecasts.

**Future cost = today's cost × (1 + inflation) ^ years**

**Worked example:** a two-wheeler costs {inr(BIKE_TODAY)} today. With 5% inflation, in 3 years it will cost about {inr(BIKE_TODAY)} × 1.05³ = **{inr(BIKE_FUTURE)}**.

### The monthly saving a goal needs

If the savings earn nothing, divide: {inr(BIKE_FUTURE)} ÷ 36 months = {inr(BIKE_PMT_NOINT)} a month. If they earn interest, you need a little less. The spreadsheet function **PMT** works it out. With 6.5% a year (an assumed recurring-deposit-like rate), the monthly saving is about **{inr(BIKE_PMT)}**:

{fence('=PMT(0.065/12, 36, 0, -138915)')}

PMT returns the payment needed for a loan or a savings target. Here the present value is 0 (you start from nothing) and the future value is the target, entered as a negative number so the answer comes out positive ({link('gs-pmt', 'Google Sheets help on PMT')}). The same formula works in LibreOffice Calc.

### When the numbers don't fit

Add up the monthly savings for all your goals. If the total is more than you can save, you have four levers: **later** (move the date), **less** (a cheaper version), **more income** (Module 16), or **drop** a goal. Choosing is the point of planning.
""",
    example=f"""
**Anu** listed six goals and found real prices for the nearest four: she asked a showroom in Kuttiady for an on-road two-wheeler quote, checked the fee for a typing and computer course, and asked her parents what they expected for her wedding (a long conversation).

{table(['Goal', 'Today\'s cost', 'Years', 'Inflation', 'Future cost', 'Monthly saving at 6.5%'], [
    ('Starter emergency fund', '₹30,000', '1', '0%', '₹30,000', inr(pmt_needed(30000, 0.065, 12))),
    ('Course fees', '₹12,000', '1', '5%', inr(fv(12000, 0.05, 1)), inr(pmt_needed(fv(12000, 0.05, 1), 0.065, 12))),
    ('Two-wheeler', inr(BIKE_TODAY), '3', '5%', inr(BIKE_FUTURE), inr(BIKE_PMT)),
    ('Her share of wedding costs', '₹2,00,000', '4', '5%', inr(fv(200000, 0.05, 4)), inr(pmt_needed(fv(200000, 0.05, 4), 0.065, 48))),
])}

The total came to about {inr(pmt_needed(30000, 0.065, 12) + pmt_needed(fv(12000, 0.05, 1), 0.065, 12) + BIKE_PMT + pmt_needed(fv(200000, 0.05, 4), 0.065, 48))} a month, but she could save only about ₹3,000. She kept the emergency fund first, moved the two-wheeler to 2030, and asked herself whether she really wanted to fund part of an expensive wedding at all. That question started a family talk she says was overdue. Her retirement goal comes later, in Module 12.
""",
    resources=[
        ('ncfe', 'In the e-LMS course, do the long-term planning module', '20 minutes'),
        ('openstax', 'Chapter 7, "Time Value of Money I: Single Payment Value": read the first two sections for the idea of future value', '30 minutes'),
        ('gs-pmt', 'The PMT function: syntax and the meaning of each argument', '5 minutes'),
    ],
    steps=[
        'List every money goal you have, big or small, for the next 30 years. Aim for 5 to 10.',
        'For the three nearest goals, find a real price today: a quote, a fee list or a shop visit. For others, use your best estimate.',
        'Make a **Goals** tab with the template headings and formulas. Fill in one row per goal.',
        'Put the goals in priority order using the safe order in the core lesson.',
        'Add up the monthly saving column. If it is more than you can save, use the four levers (later, less, more income, drop) and change the plan until it fits.',
    ],
    proof='A screenshot of your Goals tab with at least five goals, future costs and monthly savings, and the total that fits your budget, saved in 02 Goals.',
    templates=[
        ('Goals tab (headings in row 1, first goal in row 2)', """
A: Goal | B: Priority (1 = first) | C: Cost today (₹) | D: Years away | E: Inflation (e.g. 0.05)
F: Future cost (₹)        =C2*(1+E2)^D2
G: Return while saving (e.g. 0.065)
H: Monthly saving needed  =IF(G2=0,F2/(D2*12),PMT(G2/12,D2*12,0,-F2))
I: Saved so far (₹) | J: Target date | K: Where the money waits
L: Monthly saving after what you have
   =IF(G2=0,(F2-I2)/(D2*12),PMT(G2/12,D2*12,-I2,F2)*-1)
""", ''),
        ('goal card (one per goal)', """
GOAL: ____
Why it matters (which value from Module 1): ____
Cost today: ₹____  (source: quote / fee list / estimate)
Target date: ____  Future cost at ___% inflation: ₹____
Monthly saving: ₹____ starting ____
If it doesn't fit: later / less / more income / drop
""", ''),
    ],
    mistakes=[
        ('Guessing prices.', 'A real quote often surprises you, in both directions. Ten minutes of checking makes the whole goal reliable.'),
        ('Forgetting inflation.', 'A goal 10 years away at 5% inflation costs about 63% more than today. Use the future cost.'),
        ('Too many goals at once.', 'Funding ten goals a little means finishing none. Fund the top two or three properly.'),
        ('Skipping the emergency fund for exciting goals.', 'Without it, the first shock pushes you into debt and breaks every other goal.'),
    ],
    quiz=[
        {'q': 'Which is a complete money goal?', 'o': ['₹1,40,000 for a two-wheeler by November 2029, saving ₹3,500 a month', 'Save more money', 'Buy a vehicle someday', 'Be rich by 40'], 'a': 'A', 'why': 'It has what, how much, when and the monthly saving.'},
        {'q': 'Something costs ₹1,00,000 today. With 5% inflation, about how much will it cost in 2 years?', 'o': ['₹1,10,250', '₹1,05,000', '₹1,00,000', '₹1,50,000'], 'a': 'A', 'why': '₹1,00,000 × 1.05 × 1.05 = ₹1,10,250.'},
        {'q': 'In =PMT(0.065/12, 36, 0, -138915), why is the target negative?', 'o': ['So the payment comes out as a positive number', 'Because it is a loan', 'Because inflation is negative', 'It is a mistake'], 'a': 'A', 'why': 'PMT treats money in and out with opposite signs; a negative future value gives a positive payment.'},
        {'q': 'What usually comes first in the safe priority order?', 'o': ['A starter emergency fund', 'A new vehicle', 'Buying shares', 'A foreign trip'], 'a': 'A', 'why': 'It stops small shocks from becoming debt that breaks every other goal.'},
    ],
    study='The NCFE long-term planning module, OpenStax chapter 7 (first two sections) and the PMT help page',
    action='Build a Goals tab with at least five goals, future costs and monthly savings that fit your budget',
)

# ---- net worth example (made-up numbers)
NW_ASSETS = [
    ('Savings account balance', 18000),
    ('Fixed deposit', 25000),
    ('Gold jewellery, 3 pavan (24 g), at a made-up buyback rate', 216000),
    ('PF balance after the first months of service', 9500),
    ('Two-wheeler, resale value', 35000),
    ('Money lent to a cousin (likely to come back)', 10000),
]
NW_LIABS = [
    ('Phone EMI, amount still owed', 21000),
    ('Credit card bill outstanding', 6400),
    ('Gold loan taken for his sister\'s admission', 60000),
]
NW_A = sum(v for _, v in NW_ASSETS)
NW_L = sum(v for _, v in NW_LIABS)
NW = NW_A - NW_L
LIQUID = 18000 + 25000
LIQUID_NW = LIQUID - 6400

L2 = lesson(
    M, 2,
    title='Your net-worth statement',
    weeks=(3, 4), hours=2,
    outcome='List everything you own and owe at realistic values, calculate your net worth and liquid net worth with formulas, and set a date to update it.',
    split='25 minutes reading, 25 minutes resources, 70 minutes action',
    core=f"""
Your **net worth** is a snapshot of your money on one day:

> **Net worth = everything you own (assets) − everything you owe (liabilities)**

It is the single best number for tracking progress over years. Income shows what flows in; net worth shows what you keep. Someone earning ₹80,000 a month with a car loan, a personal loan and card debt can have a lower net worth than someone earning ₹20,000 who saves steadily.

### What counts as an asset

- **Cash and bank:** cash at home, savings accounts, current accounts.
- **Deposits:** FDs, RDs (the amount paid in so far plus interest), post office schemes.
- **Retirement accounts:** EPF, GPF, PPF, NPS. You can't spend them now, but they are yours.
- **Investments:** mutual funds and shares at today's value (your consolidated account statement, or {link('amfi-cas', 'CAS')}, shows all your mutual funds in one place).
- **Gold:** weight × today's **buyback** rate (what a jeweller would pay you, which is lower than what you would pay to buy). In Kerala, gold is often counted in pavan: 1 pavan = 8 grams.
- **Property:** land or a house at a realistic sale value, from recent sales nearby, not the price you hope for.
- **Vehicles:** today's resale value, which falls every year.
- **Money owed to you:** only if you really expect it back.
- **Chitty:** for a chitty you haven't won yet, count the instalments you have paid; once you have taken the prize, the future instalments become a liability (FIN-M09-L07).

### What counts as a liability

Every loan's **outstanding principal** (not the total of future EMIs): home, vehicle, education, personal, gold loans; credit card balances; Buy Now Pay Later dues; money borrowed from family, friends or a chitty prize already taken.

### Liquid net worth

Much of a Kerala family's wealth is in land and gold, which can't pay a hospital bill tomorrow without a sale or a loan. So also track **liquid net worth**:

> **Liquid net worth = cash, bank and deposits you can withdraw within a week − short-term debts (cards, personal loans, BNPL)**

This tells you how prepared you are for a shock.

### Values: be honest and boring

Use conservative values. Overvaluing land and gold makes you feel rich and take risks you can't afford. When unsure, take the lower number. The point is the **trend**: update your net worth on the same date every month or quarter, using the same method each time.

### Negative net worth

If you owe more than you own, especially with an education loan, your net worth is negative. That is common early in life and is not a judgement. Track it anyway: watching a negative number shrink is one of the most motivating things in personal finance.
""",
    example=f"""
**Rahul** made his first net-worth statement three months into his government job. (These numbers are made up, including the gold rate; use today's buyback rate for yours.)

{table(['Asset', 'Value'], [(a, inr(v)) for a, v in NW_ASSETS] + [('**Total assets**', f'**{inr(NW_A)}**')])}

{table(['Liability', 'Outstanding'], [(a, inr(v)) for a, v in NW_LIABS] + [('**Total liabilities**', f'**{inr(NW_L)}**')])}

His **net worth** is {inr(NW_A)} − {inr(NW_L)} = **{inr(NW)}**. Most of it is gold his mother gave him, which he doesn't intend to sell.

His **liquid net worth** is only the bank and FD ({inr(LIQUID)}) minus the card bill ({inr(6400)}) = **{inr(LIQUID_NW)}**. That surprised him: on paper he looked comfortable, but a ₹50,000 hospital bill would have meant another gold loan. It moved his emergency fund to the top of his goals list.
""",
    resources=[
        ('amfi-cas', 'How to get a consolidated account statement of all your mutual funds by PAN (if you have any)', '10 minutes'),
        ('ncfe', 'Any remaining part of the managing income and expenditure module; note how it lists assets and liabilities', '15 minutes'),
    ],
    steps=[
        'Make a **Net Worth** tab with the template headings.',
        'List every asset with today\'s realistic value. For gold, weigh or check the bill for the weight, and find today\'s buyback rate from a jeweller. For land, ask what similar plots near you sold for.',
        'List every liability with the outstanding principal. Your loan app or statement shows it; for cards, use the current balance; for family loans, the amount you owe.',
        'Add the totals and formulas: total assets, total liabilities, net worth and liquid net worth.',
        'Write the date at the top. Set a calendar reminder to update it on the same date next month.',
        'Write two sentences: what surprised you, and which number you most want to change.',
    ],
    proof='A screenshot of your Net Worth tab with the date, totals, net worth and liquid net worth (cover any account numbers), and your two sentences, saved in 02 Goals.',
    templates=[
        ('Net Worth tab', """
Row 1: Item,Type (Asset/Liability),Category,Liquid? (Yes/No),Value (₹),How I valued it,Date
Rows 2-40: one row per asset or liability

Totals (put them in column H and I):
H2: Total assets        I2: =SUMIF(B2:B40,"Asset",E2:E40)
H3: Total liabilities   I3: =SUMIF(B2:B40,"Liability",E2:E40)
H4: Net worth           I4: =I2-I3
H5: Liquid assets       I5: =SUMIFS(E2:E40,B2:B40,"Asset",D2:D40,"Yes")
H6: Short-term debts    I6: =SUMIFS(E2:E40,B2:B40,"Liability",D2:D40,"Yes")
H7: Liquid net worth    I7: =I5-I6

Categories: Cash and bank / Deposits / Retirement / Investments / Gold / Property / Vehicle / Owed to me / Loan / Card / Family loan
For liabilities, "Liquid? Yes" means due within a year (cards, personal loans, BNPL).
""", ''),
        ('net worth history (bottom of the tab or a new tab)', """
Date,Total assets,Total liabilities,Net worth,Liquid net worth,Change since last time,Note
""", 'csv'),
    ],
    mistakes=[
        ('Using the buying price of gold.', 'Use the buyback rate; after making charges and deductions, you get less than you paid.'),
        ('Counting total future EMIs as the debt.', 'Use the outstanding principal from the lender\'s statement; future interest isn\'t owed yet.'),
        ('Valuing land at a hoped-for price.', 'Use recent sales nearby, and the lower number when unsure.'),
        ('Updating only when things look good.', 'Fix a date and stick to it; the trend is what matters.'),
    ],
    quiz=[
        {'q': 'What is net worth?', 'o': ['Everything you own minus everything you owe', 'Your monthly salary', 'Your total income in a year', 'The value of your house'], 'a': 'A', 'why': 'It is a snapshot of assets minus liabilities on one day.'},
        {'q': 'How should 3 pavan of gold jewellery be valued in a net-worth statement?', 'o': ['24 grams × today\'s buyback rate', 'The price on the original bill', 'Today\'s selling price including making charges', 'It shouldn\'t be counted'], 'a': 'A', 'why': '1 pavan is 8 grams, and the realistic value is what a jeweller would pay you today.'},
        {'q': 'Why track liquid net worth separately?', 'o': ['Land and gold can\'t pay an urgent bill without a sale or a loan', 'Banks require it', 'It is always higher than net worth', 'It decides your tax'], 'a': 'A', 'why': 'It shows how ready you are for a shock with money you can actually use this week.'},
        {'q': 'For a loan, what goes in the liabilities list?', 'o': ['The outstanding principal', 'The total of all future EMIs', 'The original loan amount', 'Only the interest'], 'a': 'A', 'why': 'The outstanding principal is what you would need to repay today to close it.'},
    ],
    study='How to get a consolidated mutual fund statement (CAS) and the NCFE module section on assets and liabilities',
    action='Build your dated Net Worth tab with realistic values, net worth and liquid net worth',
)

# ---- cash flow example (made up)
F_INCOME = [('May', 41000), ('June', 12000), ('July', 26000), ('August', 55000), ('September', 18000), ('October', 40000)]
F_SPEND = [('May', 22000), ('June', 19500), ('July', 21000), ('August', 24500), ('September', 20000), ('October', 23000)]
F_AVG_IN = sum(v for _, v in F_INCOME) / 6
F_AVG_OUT = sum(v for _, v in F_SPEND) / 6
F_RATE = (F_AVG_IN - F_AVG_OUT) / F_AVG_IN * 100

L3 = lesson(
    M, 3,
    title='Cash-flow statement and savings rate',
    weeks=(4, 4), hours=2,
    outcome='Build a monthly cash-flow statement from your log, calculate your savings rate, and see how irregular income behaves over several months.',
    split='20 minutes reading, 20 minutes resources, 80 minutes action',
    core=f"""
Net worth is a photo; **cash flow** is a video. A cash-flow statement shows money coming in and going out over a period, usually a month:

> **Net cash flow = total money in − total money out**

If it is positive, you saved. If it is negative, you spent savings or borrowed. Over a year, positive cash flow is what makes net worth grow.

### Money in and money out

- **In:** salary after deductions, tuition or freelance fees, business profit you take home, interest, rent received, regular family support, gifts.
- **Out:** everything in your expense log: needs, wants, EMIs, family support you give, insurance premiums.
- **Not spending:** moving money to your own FD, RD or investments is **saving**, not an expense. Track it separately so your savings rate is honest.

### The savings rate

> **Savings rate = (money in − money spent) ÷ money in × 100**

It is the most useful single number for your progress, because it doesn't depend on how much you earn. A person earning ₹15,000 who saves ₹1,500 has a 10% savings rate; one earning ₹1,50,000 who saves ₹7,500 has only 5%. Many planners suggest aiming for **at least 20%** over time. If you are at 0% or below, getting to 5% is a real achievement. Raise it a little at a time, especially when income rises (the raise rule from Module 1).

### Irregular income: look at months, not one month

For freelancers, tutors, farmers and business owners, one month tells you little. Look at **the last six to twelve months**:

- **Average monthly income:** the total divided by the number of months
- **Lowest month:** your planning floor
- **Spending versus average income:** is the average enough?

FIN-M03-L04 turns this into a budget that survives slow months.

### Pulling numbers from your log with formulas

Your Expenses tab already has dates. **SUMIFS** adds amounts between two dates, so each month's spending fills itself in:

{fence('=SUMIFS(Expenses!B2:B500,Expenses!A2:A500,">="&DATE(2026,11,1),Expenses!A2:A500,"<"&DATE(2026,12,1))')}

This means: add column B in the Expenses tab where the date in column A is on or after 1 November 2026 and before 1 December 2026. It works in Google Sheets and LibreOffice Calc (use semicolons in LibreOffice if your settings need them). In LibreOffice, a reference to another sheet is written `$Expenses.B2:B500`; if the `Expenses!` form shows an error, click the cells instead of typing the reference.

### What a cash-flow statement tells you

- **Where money leaks:** categories that grew without a decision
- **Seasons:** in Kerala, Onam, Vishu, school reopening in June, weddings and the monsoon often bring higher spending; plan for them
- **Whether a goal is realistic:** the monthly saving from your Goals tab must fit your real net cash flow, not your hoped-for one
""",
    example=f"""
**Fathima's** freelance income over six months (made-up numbers):

{table(['Month', 'Money in', 'Money out', 'Net cash flow'], [(m, inr(i), inr(o), inr(i - o)) for (m, i), (_, o) in zip(F_INCOME, F_SPEND)])}

Her average income is {inr(F_AVG_IN)} a month and her average spending {inr(F_AVG_OUT)}, so her **average savings rate is about {F_RATE:.0f}%**, which is healthy. But June and September were negative: she spent more than she earned and took the gap from savings. Her lowest month was {inr(12000)}, well below her spending.

Two lessons for her: the savings rate looks good **on average**, but she needs a buffer for slow months (FIN-M03-L04), and she needs to set aside tax from the big months (FIN-M10-L05). Seeing June and September side by side also showed her that two clients paid late in those months; she now asks for 50% in advance (pricing and terms are covered in the Entrepreneurship course, ENT-M05-L03).
""",
    resources=[
        ('ncfe', 'Revise the managing income and expenditure module; then try one of the site\'s financial calculators', '15 minutes'),
        ('openstax', 'Chapter 3, "Economic Foundations: Money and Rates": skim the opening section on money and interest rates', '20 minutes'),
    ],
    steps=[
        'Make a **Cash Flow** tab with the template headings, one row per month.',
        'Fill in this month (or the days logged so far) from your Expenses tab using the SUMIFS formula. Add income from your bank statement or notes.',
        'Go back as many months as you can (up to six) using your bank statements and UPI history for money in and out. Rough is fine for old months.',
        'Add the savings rate formula and the averages at the bottom.',
        'Compare your average monthly saving with the total monthly saving your Goals tab needs. Write down the gap.',
        'Mark the months that were unusual (festivals, functions, fees) and note why.',
    ],
    proof='A screenshot of your Cash Flow tab with at least one full month (or your logged days so far), the savings rate formula and the gap between your goals and your real saving, saved in 02 Goals.',
    templates=[
        ('Cash Flow tab', """
Row 1: Month,Start date,End date,Income: salary or main,Income: other,Total in,Needs,Wants,EMIs and debt,Total spent,Saved or invested,Net cash flow,Savings rate %,Note
Row 2 example formulas (month starting in B2, ending before C2):
F2: =D2+E2
G2: =SUMIFS(Expenses!B2:B500,Expenses!A2:A500,">="&B2,Expenses!A2:A500,"<"&C2,Expenses!D2:D500,"Need")
H2: =SUMIFS(Expenses!B2:B500,Expenses!A2:A500,">="&B2,Expenses!A2:A500,"<"&C2,Expenses!D2:D500,"Want")
J2: =G2+H2+I2
L2: =F2-J2
M2: =IF(F2>0,L2/F2*100,0)
Averages (below the last month, for example row 14):
F14: =AVERAGE(F2:F13)    J14: =AVERAGE(J2:J13)    M14: =IF(F14>0,(F14-J14)/F14*100,0)
Lowest month of income: =MIN(F2:F13)
""", ''),
    ],
    mistakes=[
        ('Counting savings transfers as spending.', 'Moving money to your RD or emergency fund is saving. Keep it out of "spent", or your savings rate looks worse than it is.'),
        ('Judging irregular income by one month.', 'Use six to twelve months and plan on the lowest month, not the best.'),
        ('Forgetting yearly costs.', 'Insurance premiums, school fees and festival spending hit one month hard. Spread them with sinking funds (Module 3).'),
        ('Leaving out cash.', 'Cash spending is easy to forget and often the biggest leak. Your log must include it.'),
    ],
    quiz=[
        {'q': 'Income ₹25,000, spending ₹21,250. What is the savings rate?', 'o': ['15%', '85%', '25%', '3.75%'], 'a': 'A', 'why': '(25,000 − 21,250) ÷ 25,000 × 100 = 15%.'},
        {'q': 'You move ₹2,000 into your recurring deposit. In the cash-flow statement it is…', 'o': ['Saving, not spending', 'A want', 'A need', 'Income'], 'a': 'A', 'why': 'It is still your money, just in another place.'},
        {'q': 'For irregular income, what should a budget be built on?', 'o': ['Several months of data, planning on the lowest month', 'The best month', 'Last month only', 'What you hope to earn'], 'a': 'A', 'why': 'Slow months come; plans built on the best month fail.'},
        {'q': 'What does SUMIFS add in the course formula?', 'o': ['Amounts whose dates fall between two dates', 'All amounts in the sheet', 'Only the largest amount', 'The number of rows'], 'a': 'A', 'why': 'SUMIFS adds values that meet several conditions, here a start and an end date.'},
    ],
    study='The NCFE income and expenditure module (revision), one NCFE calculator and OpenStax chapter 3\'s opening section',
    action='Build a Cash Flow tab with your real months, savings rate and the gap to your goals',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    M,
    title='Goals and tracking',
    weeks=(3, 4), hours=6.5,
    overview="""
Turn wishes into goals with amounts and dates, and build the two statements that track your progress: net worth and cash flow.

You can't plan a journey without knowing where you are and where you want to go. This module gives you both. Your **Goals** tab says where you want to go, in rupees, with dates. Your **Net Worth** and **Cash Flow** tabs say where you are now and how fast you are moving.

The 30-day expense log keeps running in these weeks, and the Cash Flow tab reads from it with formulas, so the numbers fill in by themselves. By the end of week 4 you have your first money dashboard: three tabs that you update every month for the rest of the course, and after it.
""",
    outcomes=[
        'Write money goals with an amount, a date, a priority and an inflation-adjusted cost',
        'Calculate the monthly saving each goal needs with the PMT function',
        'Build a dated net-worth statement with net worth and liquid net worth',
        'Build a monthly cash-flow statement that reads from your expense log',
        'Calculate your savings rate and compare it with what your goals need',
    ],
    lessons=LESSONS,
    project='My money dashboard, version 1',
    project_steps=[
        'Check that your Goals, Net Worth and Cash Flow tabs are complete and dated.',
        'Add a small **Dashboard** area at the top of the Goals tab with four numbers pulled by formula from the other tabs: net worth, liquid net worth, this month\'s savings rate and the total monthly saving your goals need. For example, `=\'Net Worth\'!I4` in Google Sheets (in LibreOffice, click the cell on the other sheet instead of typing).',
        'Write a three-line summary: "My net worth is ___. My savings rate is ___%. To fund my top three goals I need ₹___ a month more or less than I save now."',
        'Decide one change for next month based on the dashboard, and write it in the Review tab (Money habits track).',
    ],
    project_proof='A screenshot of the dashboard numbers and your three-line summary, saved in 02 Goals.',
    rubric=[
        ('Goals', 'Wishes without numbers', 'Amounts but no dates or inflation', 'Amount, date, priority, future cost and monthly saving for each'),
        ('Net worth', 'Not built', 'Built with optimistic values', 'Dated, conservative values, net worth and liquid net worth'),
        ('Cash flow', 'Not built', 'One month typed by hand', 'Months filled by formula from the log, with savings rate'),
        ('Reality check', 'Not done', 'Gap noted', 'Gap noted and the goals plan changed to fit'),
        ('Routine', 'No date set', 'A vague intention', 'A calendar reminder for the monthly update'),
    ],
    short=[
        'Write your top three goals with amount, date and monthly saving (FIN-M02-L01).',
        'List assets and liabilities and calculate net worth, even roughly (FIN-M02-L02).',
        'Calculate one month\'s savings rate (FIN-M02-L03).',
    ],
    flashcards=[
        ('Five parts of a money goal', 'What, cost today, date, future cost, monthly saving.'),
        ('Future cost formula', 'Today\'s cost × (1 + inflation) ^ years.'),
        ('India\'s inflation target until 2031', '4%, with a band of 2% to 6% (as of November 2026).'),
        ('Net worth', 'Assets minus liabilities, on one date.'),
        ('Liquid net worth', 'Cash, bank and deposits you can use within a week, minus short-term debts.'),
        ('Savings rate', '(Money in − money spent) ÷ money in × 100.'),
        ('1 pavan of gold', '8 grams.'),
        ('Four levers when goals don\'t fit', 'Later, less, more income, drop.'),
    ],
    mistakes=[
        ('Optimistic numbers everywhere.', 'Use real quotes, buyback rates and the lowest income month. Plans fail from optimism, not pessimism.'),
        ('Building the tabs and never opening them again.', 'The monthly review exists so these numbers stay alive.'),
        ('Comparing your net worth with others.', 'Compare it only with your own number from last month and last year.'),
    ],
    project_week=4,
)
