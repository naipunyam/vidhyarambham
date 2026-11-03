"""Module 8: Investing fundamentals."""
from common import lesson, module, link, fence, table, inr, ASOF, CHECK

M = 8


def fv_sip(m, r, years):
    i = r / 12
    n = years * 12
    return m * ((1 + i) ** n - 1) / i * (1 + i)


EARLY = fv_sip(2000, 0.08, 33)
LATE = fv_sip(2000, 0.08, 23)
LATE2 = fv_sip(4000, 0.08, 23)

L1 = lesson(
    M, 1,
    title='Inflation and compounding: the two forces on your money',
    weeks=(15, 15), hours=1.5,
    outcome='Calculate real returns, the future value of a lump sum and a SIP, and what a future amount is worth in today\'s rupees, in a Calculators tab.',
    split='25 minutes reading, 25 minutes resources, 40 minutes action',
    core=f"""
Two forces act on every rupee you save: **inflation** quietly shrinks what it can buy, and **compounding** can make it grow. Investing is the art of making compounding beat inflation without taking risks you can't handle.

### Inflation

Inflation is the general rise in prices, measured in India mainly by the **consumer price index (CPI)**. The official target is **4%, within a band of 2% to 6%**, until March 2031 ({link('om-target', 'Outlook Money, March 2026')}). CPI inflation was **4.8% in August 2026**, and RBI raised its policy repo rate to 5.50% in October 2026 to keep prices in check ({link('rbi-repo', 'SCC Online, October 2026')}).

At 5% inflation, something that costs ₹1,000 today costs about ₹1,629 in 10 years. Put the other way, **₹10,00,000 received 20 years from now buys only what about {inr(1000000 / 1.05 ** 20)} buys today**:

> **Today's value of a future amount = future amount ÷ (1 + inflation) ^ years**

### Real return

The return that matters is what you earn **after** inflation:

> **Real return ≈ return − inflation** (exactly: (1 + return) ÷ (1 + inflation) − 1)

- Savings account at 3%, inflation at 5%: real return about **−1.9%**. The balance grows; its buying power shrinks.
- A deposit at 7%, inflation at 5%: real return about **+1.9%**, before tax on the interest.

Money for the next few years should be safe even if its real return is small. Money for 10 or 20 years needs a positive real return, or your goals keep running away from you.

### Compounding

Compounding means earning returns on your earlier returns:

> **Future value = amount today × (1 + yearly return) ^ years**

₹1,00,000 at 8% a year grows to about {inr(100000 * 1.08 ** 10)} in 10 years, {inr(100000 * 1.08 ** 20)} in 20 years and {inr(100000 * 1.08 ** 30)} in 30 years. The last 10 years add more than the first 20, because the base is bigger. **Time is the most powerful part of the formula.**

The **rule of 72** is a quick check: money doubles in about **72 ÷ return** years. At 8%, about 9 years; at 6%, about 12; at 12%, about 6.

### A SIP: investing every month

A **systematic investment plan (SIP)** puts in a fixed amount every month. The spreadsheet FV function gives the future value:

{fence('=FV(0.08/12, 33*12, -2000, 0, 1)')}

**Worked example:** starting at 27, ₹2,000 a month at an assumed 8% a year until 60 (33 years) grows to about **{inr(EARLY)}**, from {inr(2000 * 12 * 33)} paid in. Starting at 37 (23 years), it grows to only about **{inr(LATE)}**, from {inr(2000 * 12 * 23)}. To catch up, the late starter would need ₹4,000 a month, and would still end with about {inr(LATE2)}.

### A warning about assumed returns

Every number above uses an **assumed** return. Real investments don't grow at a steady 8%: some years they fall, some years they jump, and the average over your period is unknown in advance. Use calculators to understand the effect of time and amounts, not to promise yourself a result. When anyone shows you a calculator with a high return to sell you something, ask what happens in a bad decade (FIN-M08-L02).
""",
    example=f"""
**Anu**, 27, and her friend **Sreeja**, 37, compared notes after a PSC class. Sreeja had saved nothing for retirement: "I'll start when I have a government job, with a bigger amount."

Anu put both of them into her new Calculators tab, at an assumed 8%: ₹2,000 a month from Anu's age until 60 gave about {inr(EARLY)}; the same amount from Sreeja's age gave about {inr(LATE)}. Sreeja would need to put in twice as much each month just to come close.

Then they did the inflation step: at 5% inflation, Anu's {inr(EARLY)} in 33 years would buy what about {inr(EARLY / 1.05 ** 33)} buys today. "So the big number isn't as big as it looks," Sreeja said. "But starting late makes it much smaller." She started a small recurring deposit that week, planning to move it to a proper retirement plan after Module 12.
""",
    resources=[
        ('openstax', 'Chapter 3, "Economic Foundations: Money and Rates" (inflation and interest) and chapter 7 (future value): read the sections on inflation and compounding', '30 minutes'),
        ('om-target', 'India\'s inflation target until 2031', '5 minutes'),
        ('rbi-repo', 'The October 2026 policy decision: repo rate and recent CPI inflation', '5 minutes'),
    ],
    steps=[
        'Make a **Calculators** tab with the template: lump-sum future value, SIP future value, today\'s value of a future amount, real return and the rule of 72.',
        'Test each calculator with the worked examples from this lesson and check you get the same answers.',
        'Calculate the real return on your own savings account and on one FD rate from Module 4, using 5% inflation.',
        'Put your own numbers into the SIP calculator: the monthly amount you could invest, and the years until a long-term goal. Then try starting 5 years later.',
        'Write two sentences: what surprised you, and what you will do differently.',
    ],
    proof='A screenshot of your working Calculators tab with your own numbers and your two sentences, saved in 08 Basics.',
    templates=[
        ('Calculators tab (labels in column A, inputs in B)', """
LUMP SUM
B2: amount today (₹)   B3: yearly return (e.g. 0.08)   B4: years
B5: future value   =B2*(1+B3)^B4

SIP (monthly, invested at the start of each month)
B8: monthly amount (₹)   B9: yearly return   B10: years
B11: future value  =FV(B9/12,B10*12,-B8,0,1)
B12: total paid    =B8*B10*12
B13: growth        =B11-B12

TODAY'S VALUE OF A FUTURE AMOUNT
B16: future amount (₹)   B17: inflation (e.g. 0.05)   B18: years
B19: in today's rupees  =B16/(1+B17)^B18

REAL RETURN
B22: return (e.g. 0.07)   B23: inflation (e.g. 0.05)
B24: real return %  =((1+B22)/(1+B23)-1)*100

RULE OF 72
B27: yearly return in % (e.g. 8)
B28: years to double, about  =72/B27
""", ''),
    ],
    mistakes=[
        ('Ignoring inflation.', 'A goal 20 years away needs future rupees. Always convert both ways: future cost, and today\'s value of a future amount.'),
        ('Treating an assumed return as a promise.', 'Calculators show the effect of time and amounts. Real returns vary year to year.'),
        ('Waiting for a bigger income to start.', 'Time does more work than amount. Start small now and raise the amount later.'),
        ('Keeping long-term money in a savings account.', 'A negative real return slowly eats it. Long-term money needs growth (FIN-M08-L03).'),
    ],
    quiz=[
        {'q': 'A deposit pays 7% and inflation is 5%. What is the real return, roughly?', 'o': ['About 2%', '12%', '7%', '−2%'], 'a': 'A', 'why': 'Real return ≈ 7% − 5%; exactly (1.07 ÷ 1.05) − 1 ≈ 1.9%.'},
        {'q': 'By the rule of 72, how long does money take to double at 6% a year?', 'o': ['About 12 years', 'About 6 years', 'About 72 years', 'About 3 years'], 'a': 'A', 'why': '72 ÷ 6 = 12.'},
        {'q': 'Which formula gives the future value of ₹2,000 a month for 20 years at 8%, invested at the start of each month?', 'o': ['=FV(0.08/12, 20*12, -2000, 0, 1)', '=2000*20*12', '=PMT(0.08, 20, 2000)', '=2000*(1+0.08)^20'], 'a': 'A', 'why': 'FV with a monthly rate, the number of months, the payment and type 1.'},
        {'q': 'What is India\'s CPI inflation target for 2026 to 2031?', 'o': ['4%, with a band of 2% to 6%', '8%', '0%', '10% to 12%'], 'a': 'A', 'why': 'The target was kept at 4% ± 2% until March 2031.'},
        {'q': 'Why does starting 10 years earlier make such a big difference?', 'o': ['Compounding has more years to work, and the last years add the most', 'Banks pay more to young people', 'Inflation is lower for young people', 'It doesn\'t make a difference'], 'a': 'A', 'why': 'Time is the exponent in the compounding formula.'},
    ],
    study='OpenStax chapters 3 and 7 on inflation and compounding, the inflation target and the October 2026 policy decision',
    action='Build a Calculators tab, test it, and run your own numbers for real return and a SIP',
)

L2 = lesson(
    M, 2,
    title='Risk, return and the main asset classes',
    weeks=(15, 15), hours=1.5,
    outcome='Explain the main kinds of investment risk, describe each asset class honestly, and score your own risk profile.',
    split='25 minutes reading, 25 minutes resources, 40 minutes action',
    core=f"""
### Risk is more than "losing money"

{table(['Risk', 'What it means', 'Example'], [
    ('Market risk', 'Prices go up and down, sometimes a lot', 'Share prices fall sharply in a bad year'),
    ('Inflation risk', 'Returns don\'t keep up with prices', 'A savings account at 3% when prices rise 5%'),
    ('Credit (default) risk', 'The borrower doesn\'t pay you back', 'A company or society fails to repay a deposit or bond'),
    ('Interest-rate risk', 'Bond and debt fund prices fall when rates rise', 'A long-term bond fund dips after a rate rise'),
    ('Liquidity risk', 'You can\'t sell quickly at a fair price', 'Land that takes a year to sell'),
    ('Concentration risk', 'Too much in one thing', 'All savings in one stock, one plot or one society'),
    ('Fraud risk', 'The product or the seller is a scam', 'A "scheme" promising 5% a month (Module 15)'),
])}

There is no investment without risk; even "safe" deposits carry inflation risk.

### The main asset classes

{table(['Asset class', 'Examples', 'Return potential', 'Main risks'], [
    ('Cash and deposits', 'Savings, FDs, RDs', 'Low; may not beat inflation after tax', 'Inflation; credit risk above insurance limits'),
    ('Debt (lending)', 'Government small savings, PPF, EPF, bonds, debt mutual funds', 'Low to moderate', 'Interest-rate and credit risk; government-backed schemes have very low credit risk'),
    ('Equity (ownership)', 'Shares, equity mutual funds, index funds', 'Highest over long periods', 'Large falls in bad years; years to recover'),
    ('Gold', 'Gold ETFs, gold mutual funds, jewellery', 'Varies; often rises when other assets fall', 'Long flat periods; jewellery has making charges and purity issues'),
    ('Real estate', 'Land, a house, REITs', 'Varies by place', 'Illiquid, large amounts, legal issues, costs'),
    ('Speculative', 'Crypto, derivatives (F&O)', 'Uncertain', 'Very high volatility; SEBI found about 91% of individual F&O traders lost money in 2024-25 (' + link('sebi-fno', 'Moneylife') + ')'),
])}

### The risk–return trade-off

Higher possible returns come with higher risk. It never works the other way: **"high returns with no risk" doesn't exist**. When someone offers it, you are looking at a misunderstanding or a fraud.

Equity's long-term return potential is higher because investors are paid for living through its falls. If you will panic and sell in a fall, you get the falls without the long-term reward.

### The riskometer

Every mutual fund in India shows a **riskometer**, SEBI's standard risk scale with six levels: **Low, Low to Moderate, Moderate, Moderately High, High and Very High** ({link('amfi-risko', 'AMFI')}). It is based on the fund's holdings, volatility, and credit and interest-rate risk, and must appear in factsheets and promotional material ({link('sebi-risko', 'SEBI investor site')}). You will use it to compare funds in FIN-M09-L02.

### Your risk profile: two different things

- **Risk capacity:** how much loss your finances can survive. A full emergency fund, stable income, insurance, no expensive debt and a long time horizon all raise it.
- **Risk tolerance:** how much loss you can live with emotionally without panicking.

Invest according to the **lower** of the two. A government employee with a pension may have high capacity but low tolerance; a young freelancer may feel brave but have low capacity.

### Time horizon changes everything

Money needed in 2 years can't wait for a market to recover; money needed in 20 years can. So the same person can have safe money for short goals and growth money for long ones. That is the idea behind asset allocation, in the next lesson.
""",
    example=f"""
**Fathima** scored herself with the risk profile in this lesson. Her **tolerance** came out high: she enjoys reading about markets and wasn't worried by the idea of a 30% fall. But her **capacity** came out low: irregular income, an emergency fund only half built, and a two-wheeler loan.

Her conclusion: "My head says high risk, my situation says not yet." She decided that until her emergency fund was full and her loan cleared, new long-term money would go mostly to safer options, with only a small share in equity, rising once her capacity improved. She wrote the rule in her Calculators tab so she wouldn't change her mind after a good month in the markets.
""",
    resources=[
        ('amfi-risko', 'The six riskometer levels', '5 minutes'),
        ('sebi-risko', 'How the riskometer is decided and where you will see it', '10 minutes'),
        ('sebi-fno', 'SEBI\'s study of losses in futures and options trading', '10 minutes'),
        ('openstax', 'Chapter 15, "How to Think about Investing": read the opening sections on risk and return', '25 minutes'),
    ],
    steps=[
        'Answer the 10 risk-profile questions honestly and add up your capacity and tolerance scores.',
        'Write your profile: the lower of the two scores decides it.',
        'In your Goals tab, add a column "time horizon" and mark each goal short (under 3 years), medium (3 to 7) or long (over 7).',
        'For each risk in the table, write one place it already exists in your family\'s money (for example, concentration: all savings in one co-op society).',
        'Write one rule that follows from your profile, like Fathima\'s.',
    ],
    proof='Your scored risk profile, the horizon column in your Goals tab and your one rule, saved in 08 Basics.',
    templates=[
        ('risk profile (score each answer 1 to 3)', """
CAPACITY (what your finances can survive)
1. Emergency fund: none (1) / partly built (2) / full (3)
2. Income: irregular (1) / steady private job (2) / permanent or very secure (3)
3. Expensive debt (cards, personal loans): yes (1) / some (2) / none (3)
4. Health and life cover in place: no (1) / partly (2) / yes (3)
5. Years until you need this money: under 3 (1) / 3 to 7 (2) / over 7 (3)
Capacity score: ____ / 15

TOLERANCE (what you can live with)
6. If your investment fell 25% in a year, you would: sell everything (1) / wait, worried (2) / hold or add more (3)
7. You prefer: certain small growth (1) / some ups and downs (2) / big ups and downs for more growth (3)
8. You check investments: daily and worry (1) / monthly (2) / a few times a year (3)
9. Past loss experience: panicked (1) / no experience (2) / stayed calm (3)
10. Sleep test: losses would keep you awake (1) / sometimes (2) / no (3)
Tolerance score: ____ / 15

Profile = the LOWER score:  5-8 cautious   9-11 balanced   12-15 growth
""", ''),
    ],
    mistakes=[
        ('Thinking deposits are risk-free.', 'They carry inflation risk, and credit risk above insurance limits or in unlicensed societies.'),
        ('Judging risk by last year\'s returns.', 'A great year says nothing about the next one. Look at what can go wrong.'),
        ('Investing by tolerance alone.', 'Courage doesn\'t pay bills in a crisis. Capacity decides too.'),
        ('Believing "guaranteed high returns".', 'High return and no risk never come together. It is the first sign of a scam.'),
    ],
    quiz=[
        {'q': 'Which risk does a savings account carry even though the balance never falls?', 'o': ['Inflation risk', 'Market risk', 'Liquidity risk', 'No risk at all'], 'a': 'A', 'why': 'If interest is below inflation, buying power shrinks.'},
        {'q': 'How many levels does SEBI\'s riskometer have?', 'o': ['Six', 'Three', 'Ten', 'Two'], 'a': 'A', 'why': 'Low, Low to Moderate, Moderate, Moderately High, High, Very High.'},
        {'q': 'Your tolerance score is high but your capacity is low. What should decide your investments?', 'o': ['The lower one: capacity', 'The higher one: tolerance', 'Whatever friends do', 'Last year\'s best fund'], 'a': 'A', 'why': 'Invest by the lower of the two so a bad year doesn\'t break your plan.'},
        {'q': 'What did SEBI\'s study find about individual F&O traders in 2024-25?', 'o': ['About 91% lost money', 'Most made steady profits', 'Half doubled their money', 'Nobody traded'], 'a': 'A', 'why': 'Net losses were over ₹1 lakh crore in the year.'},
    ],
    study='The riskometer (AMFI and SEBI), SEBI\'s F&O loss study and OpenStax chapter 15\'s opening sections',
    action='Score your risk profile, mark each goal\'s time horizon and write one rule',
)

L3 = lesson(
    M, 3,
    title='Asset allocation, diversification and rebalancing',
    weeks=(15, 15), hours=1.5,
    outcome='Set a target asset allocation for your long-term money based on your goals and risk profile, and use a formula to know when to rebalance.',
    split='25 minutes reading, 20 minutes resources, 45 minutes action',
    core=f"""
### Asset allocation

**Asset allocation** is how you split your investments between asset classes: equity, debt, gold and cash. It matters more for your long-term result than which individual fund or stock you pick, because it decides how much your money can grow and how far it can fall.

### Allocation by goal

The simplest method follows the time horizons you marked in FIN-M08-L02:

{table(['Goal horizon', 'Typical allocation', 'Why'], [
    ('Under 3 years', 'All safe: deposits, RDs, small savings, very low-risk debt', 'No time to recover from a fall'),
    ('3 to 7 years', 'Mostly safe, some equity (for example 20–40%)', 'Some growth, limited damage in a bad year'),
    ('Over 7 years (retirement, a child\'s education)', 'More equity (for example 50–70%), the rest debt, perhaps some gold', 'Time to ride out falls; needs to beat inflation'),
])}

These are examples to think with, not recommendations. Adjust them for your risk profile: a cautious profile uses the lower equity numbers or less. One rule of thumb some people use for long-term money is "100 minus your age" in equity; treat it as a starting point for thinking, not an answer.

Remember money you already have in **EPF, GPF or PPF**: it is debt. If you are a government employee with GPF or NPS contributions (Module 14), count them in your allocation.

### Diversification

**Don't put all your eggs in one basket**, within and across asset classes:

- **Across classes:** equity, debt and gold rarely all fall at the same time.
- **Within a class:** one company's shares can go to zero; an index fund holding many companies is far less likely to. One co-operative society can fail; deposits spread across insured banks and government schemes are safer.
- **Kerala's common concentration:** most family wealth in one plot of land, one house and gold. Diversifying doesn't mean selling the house; it means new savings go elsewhere.

### Rebalancing

Over time, the assets that grew fastest become a bigger share than you planned. If equity rises, your portfolio becomes riskier without you deciding it. **Rebalancing** brings it back to target:

1. **Check once a year**, on a fixed date (your yearly review, FIN-M17-L03).
2. **Rebalance if any class has drifted more than 5 percentage points** from its target (your rule; some use 10).
3. **First, direct new money** to the asset class that is below target. This avoids selling.
4. **Only if needed, sell** some of what is above target and buy what is below, thinking about tax (Module 10) and exit loads.

**Worked example:** Rahul's target is 60% equity, 35% debt, 5% gold. After a strong year his ₹2,00,000 long-term money is ₹1,36,000 equity (68%), ₹56,000 debt (28%) and ₹8,000 gold (4%). Equity has drifted 8 points over. He sends his next six months of new investments entirely to debt, which brings him back near target without selling.

Rebalancing feels wrong: it means adding to what has done badly and slowing what has done well. That is exactly why it works: it makes you buy low and sell high by rule, not by feeling.
""",
    example=f"""
**Anu** set her first allocation. Her short goals (emergency fund, course fees, two-wheeler) stay 100% safe in her savings account, RD and FDs. Her only long goal is retirement, starting small after Module 12.

For the retirement money, her risk profile came out **balanced**, so she wrote a target of **50% equity (through index funds, once she has studied them in Module 9), 45% debt (PPF), 5% gold**. Her rule: rebalance on 1 April each year if anything drifts more than 5 points, by sending new money to the lagging class first.

She noticed her family's wealth was mostly land and gold jewellery. She didn't try to change her parents' choices; she wrote, "My own new savings go to what our family doesn't have yet: insured deposits, PPF and, later, diversified equity."
""",
    resources=[
        ('openstax', 'Chapter 15, "How to Think about Investing": the sections on diversification and portfolios', '20 minutes'),
        ('ncfe', 'The long-term planning module (revision) with allocation in mind', '10 minutes'),
    ],
    steps=[
        'In your Goals tab, add the target allocation for each goal\'s money using its horizon and your profile.',
        'Make an **Allocation** tab with the template: list what you already hold (deposits, PPF, EPF, gold, any funds or shares), with asset class and value.',
        'Enter your target percentages for long-term money and let the formulas show actual percentages and drift.',
        'Write your rebalancing rule: date, drift limit, and "new money first".',
        'Write one sentence on your biggest concentration risk and what you will do about it with new savings.',
    ],
    proof='A screenshot of your Allocation tab with targets, actuals and the drift formula, and your rebalancing rule, saved in 08 Basics.',
    templates=[
        ('Allocation tab', """
Holdings (rows 2-30): Holding,Asset class (Equity/Debt/Gold/Cash),Value (₹),For which goal
Summary (columns F-J):
F2: Equity   F3: Debt   F4: Gold   F5: Cash
G: actual value   G2: =SUMIF($B$2:$B$30,F2,$C$2:$C$30)   (copy to G3:G5)
H: actual %       H2: =IF(SUM($G$2:$G$5)>0,G2/SUM($G$2:$G$5)*100,0)
I: target %       (type: e.g. 60, 35, 5, 0)
J: drift          J2: =H2-I2
K: action         K2: =IF(ABS(J2)>5,IF(J2>0,"Over: send new money elsewhere","Under: send new money here"),"OK")
""", ''),
        ('my rebalancing rule', """
I check my allocation every year on ____ (date).
If any asset class is more than ___ percentage points away from target, I rebalance.
First I send new money to the class below target. I sell only if that isn't enough, after checking tax and exit loads.
""", ''),
    ],
    mistakes=[
        ('Choosing funds before choosing an allocation.', 'Decide the split first; picking products comes after (Module 9).'),
        ('Forgetting EPF, GPF and PPF.', 'They are debt. Count them, or you may hold more debt than you think.'),
        ('Rebalancing too often.', 'Once a year with a drift limit is enough; frequent changes add costs and taxes.'),
        ('Mistaking many products for diversification.', 'Five funds that hold the same companies aren\'t diversified. Look at what they own.'),
    ],
    quiz=[
        {'q': 'Money for a goal in 2 years should usually be…', 'o': ['All in safe options', 'Mostly in equity', 'In crypto', 'In one stock'], 'a': 'A', 'why': 'There is no time to recover from a fall.'},
        {'q': 'Target 60% equity; actual 68%. With a 5-point rule, what do you do first?', 'o': ['Send new money to debt (and gold) until it is back near target', 'Sell everything', 'Buy more equity', 'Do nothing ever'], 'a': 'A', 'why': 'Drift is 8 points; new money first avoids selling.'},
        {'q': 'Which is an example of diversification?', 'o': ['An index fund holding many companies, plus deposits and some gold', 'All savings in one company\'s shares', 'All savings in one co-op society', 'Five funds holding the same stocks'], 'a': 'A', 'why': 'Spreading across and within asset classes reduces the damage from any one failure.'},
        {'q': 'Your EPF balance belongs to which asset class?', 'o': ['Debt', 'Equity', 'Gold', 'Real estate'], 'a': 'A', 'why': 'It earns a declared interest rate; count it as debt in your allocation.'},
    ],
    study='OpenStax chapter 15 on diversification and the NCFE long-term planning module',
    action='Set target allocations, build the Allocation tab with drift formulas and write your rebalancing rule',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    M,
    title='Investing fundamentals',
    weeks=(15, 15), hours=5.5,
    overview="""
Learn the few ideas that decide almost every investment result: inflation, compounding, risk, asset classes, allocation, diversification and rebalancing.

Before any product, you need the principles. This module explains why money left idle loses value, why time matters more than the amount, what risk really means, and how to split long-term money so it can grow without breaking your sleep or your plans.

You build two tabs that the rest of the course uses: **Calculators** (future value, SIP, today's value, real return) and **Allocation** (targets, actuals and drift). Your risk profile and rebalancing rule become the core of your Investment Policy Statement in Module 17.
""",
    outcomes=[
        'Calculate real returns, future values and today\'s value of future money',
        'Show with numbers why starting early matters',
        'Explain the main risks and asset classes honestly, including the riskometer',
        'Score your risk capacity and tolerance',
        'Set a target allocation by goal horizon and rebalance by rule',
    ],
    lessons=LESSONS,
    project='My calculators and my target allocation',
    project_steps=[
        'Check that every calculator in the Calculators tab works with the worked examples.',
        'Write your risk profile result and the one rule that follows from it.',
        'In the Allocation tab, set targets for your long-term money and record what you hold now.',
        'Write your rebalancing rule and put the yearly check date in your calendar.',
        'Write a short paragraph, in your own words, explaining compounding and diversification to a family member, and read it to them.',
    ],
    project_proof='Screenshots of the Calculators and Allocation tabs, your risk profile and your paragraph, saved in 08 Basics.',
    rubric=[
        ('Calculators', 'Missing', 'Some work', 'All five work and match the worked examples'),
        ('Inflation', 'Ignored', 'Mentioned', 'Real return and today\'s value calculated for your own savings'),
        ('Risk profile', 'Not done', 'One score only', 'Capacity and tolerance scored; the lower one used'),
        ('Allocation', 'None', 'Targets without holdings', 'Targets by horizon, holdings listed, drift formula working'),
        ('Rebalancing', 'No rule', 'Vague', 'Date, drift limit and "new money first" written'),
    ],
    short=[
        'Build the SIP and real-return calculators (FIN-M08-L01).',
        'Score your risk profile (FIN-M08-L02).',
        'Write one target allocation for your longest goal (FIN-M08-L03).',
    ],
    flashcards=[
        ('Real return', '(1 + return) ÷ (1 + inflation) − 1, roughly return minus inflation.'),
        ('Rule of 72', 'Years to double ≈ 72 ÷ yearly return %.'),
        ('SIP future value formula', '=FV(rate/12, years*12, -monthly, 0, 1)'),
        ('Today\'s value of a future amount', 'Future amount ÷ (1 + inflation) ^ years.'),
        ('Risk capacity vs tolerance', 'What your finances can survive vs what you can live with; use the lower.'),
        ('Riskometer levels', 'Low, Low to Moderate, Moderate, Moderately High, High, Very High.'),
        ('Rebalancing rule of the course', 'Yearly check; act if drift > 5 points; new money first.'),
        ('India\'s inflation target to 2031', '4% within a 2% to 6% band.'),
    ],
    mistakes=[
        ('Skipping the theory to pick products.', 'Without allocation and risk rules, product choices become guesses driven by tips.'),
        ('Believing calculator returns.', 'Assumed returns are for planning; real ones vary.'),
        ('Taking more risk after a good year.', 'That is when risk feels smallest and is often largest. Stick to your rule.'),
    ],
    project_week=15,
)
