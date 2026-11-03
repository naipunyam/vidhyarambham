"""Module 6: Debt and credit."""
from common import lesson, module, link, fence, table, inr, ASOF, CHECK

M = 6


def pmt(p, annual, n):
    r = annual / 12
    return p * r * (1 + r) ** n / ((1 + r) ** n - 1)


def rate(n, pay, pv):
    lo, hi = 1e-9, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if pay * (1 - (1 + mid) ** -n) / mid > pv:
            lo = mid
        else:
            hi = mid
    return mid


FLAT_EMI = (100000 + 100000 * 0.12 * 2) / 24
FLAT_EFF = rate(24, FLAT_EMI, 100000) * 12 * 100
PL_EMI = pmt(100000, 0.14, 36)
PL_INT = PL_EMI * 36 - 100000
PL_FEE = 2360
PL_EFF = rate(36, PL_EMI, 100000 - PL_FEE) * 12 * 100


def card_sim(balance, monthly_rate, pct=None, floor=0, fixed=None):
    months, interest = 0, 0.0
    while balance > 0.5 and months < 1200:
        i = balance * monthly_rate
        pay = fixed if fixed else max(balance * pct, floor)
        pay = min(pay, balance + i)
        balance = balance + i - pay
        interest += i
        months += 1
    return months, interest


MIN_M, MIN_I = card_sim(50000, 0.035, pct=0.05, floor=500)
FIX_M, FIX_I = card_sim(50000, 0.035, fixed=5000)

L1 = lesson(
    M, 1,
    title='How interest works, and good and bad debt',
    weeks=(10, 10), hours=2,
    outcome='Calculate the EMI, total interest and true yearly cost of any loan, spot a "flat rate" trap, and decide whether a debt is worth taking.',
    split='30 minutes reading, 30 minutes resources, 60 minutes action',
    core=f"""
### Interest is the price of using someone else's money

- **Simple interest** is charged only on the original amount: ₹10,000 at 10% a year for 2 years = ₹2,000.
- **Compound interest** is charged on the amount plus earlier interest. It makes savings grow (Module 8) and makes unpaid debts grow fast.
- **Reducing-balance interest**, used for most bank loans, is charged each month only on the amount still owed. As you repay, the interest part of each EMI falls and the principal part rises.

### The EMI

An **EMI** (equated monthly instalment) is the fixed monthly payment that clears a loan over its term. The spreadsheet function PMT calculates it:

{fence('=PMT(annual_rate/12, months, -loan_amount)')}

**Worked example:** a ₹1,00,000 personal loan at 14% a year for 36 months: `=PMT(0.14/12, 36, -100000)` = **{inr(PL_EMI)}** a month. Total paid = {inr(PL_EMI)} × 36 = {inr(PL_EMI * 36)}, so the **total interest is {inr(PL_INT)}**.

### The flat-rate trap

Some shops, finance companies and private lenders quote a **flat rate**: interest on the full amount for the whole term, even though you repay every month. It sounds cheap.

**Worked example:** ₹1,00,000 at "12% flat" for 2 years means interest of ₹24,000, so EMI = ₹1,24,000 ÷ 24 = {inr(FLAT_EMI)}. The same EMI on a normal reducing-balance loan works out to about **{FLAT_EFF:.1f}% a year**. Always ask for the reducing-balance rate (often shown as the annual percentage rate, APR), or calculate it:

{fence('=RATE(24, -5166.67, 100000)*12')}

### The true cost includes fees

Processing fees, documentation charges and bundled insurance are part of the cost. They reduce what you actually receive while the EMI stays the same.

**Worked example:** the ₹1,00,000 loan above, with a ₹{PL_FEE:,} processing fee taken from the amount paid out. You receive ₹{100000 - PL_FEE:,} but pay {inr(PL_EMI)} for 36 months. The true yearly cost is `=RATE(36, -{PL_EMI:.2f}, {100000 - PL_FEE})*12` = about **{PL_EFF:.1f}%**, not 14%. A Key Facts Statement from a regulated lender must show the charges; a lender can't charge fees that aren't in it ({link('bs-dla', 'Business Standard, July 2025')}).

### Good debt and bad debt: four questions

There is no perfect rule, but these questions help:

1. **Does it build income or lasting value?** An education loan for a course that leads to a job, or a sensible home loan, can. A loan for a phone, a holiday or a wedding beyond your means doesn't.
2. **Is the true cost reasonable?** 9% for a bank gold loan is very different from 3% a month on a credit card or 1% a day from an illegal app.
3. **Can you repay from normal income, with your emergency fund untouched?** Many planners suggest keeping **all EMIs together below about a third of take-home pay**.
4. **What happens if things go wrong?** Collateral such as gold or a house can be lost; a guarantor's credit is affected too.

Debt for wants that lose value is almost always bad debt. Debt itself is a tool: dangerous when used for the wrong job.
""",
    example=f"""
A mobile shop in Kuttiady offered **Anu** a ₹24,000 phone on "easy EMI: just ₹2,400 a month for 12 months, 0 down payment". She used the formulas from this lesson:

- Total paid: ₹2,400 × 12 = ₹28,800, so ₹4,800 more than the price.
- True yearly rate: `=RATE(12, -2400, 24000)*12` = about **35%** a year, before a ₹499 "file charge".

She also asked herself the four questions. The phone was an upgrade of a working phone (a want), the cost was high, and the EMI would be 17% of her income in a slow month. She decided to save ₹2,000 a month for the phone instead (a sinking fund) and buy it in a year. "The shop's EMI would have paid for almost two extra months of the phone," she wrote in her log.
""",
    resources=[
        ('gs-pmt', 'The PMT function, used for loan EMIs', '5 minutes'),
        ('openstax', 'Chapter 8, "Time Value of Money II: Equal Multiple Payments": read the opening sections on loans and annuities', '30 minutes'),
        ('bs-dla', 'What a Key Facts Statement is and why fees outside it are not allowed', '10 minutes'),
    ],
    steps=[
        'Make a **Debts** tab and copy the loan true-cost calculator from the template.',
        'Enter each loan or EMI you have now: card balances, phone EMIs, gold, education, vehicle or personal loans, and money owed to family. Use the statements for the real rate, term and fees.',
        'If you have no loans, enter one real offer instead: a phone EMI, a "no-cost EMI" at checkout or a gold loan quote from a bank.',
        'Find the EMI, total interest and true yearly rate of each, including fees.',
        'Run the four good-debt questions on each loan and write one line per loan: "good", "acceptable" or "bad", and why.',
        'Add up all EMIs and compare with your take-home pay.',
    ],
    proof='A screenshot of your Debts tab with EMI, total interest, true rate and a good/acceptable/bad verdict for each loan or offer, saved in 06 Debt.',
    templates=[
        ('loan true-cost calculator', """
Row 1: Loan,Amount borrowed (₹),Annual rate (e.g. 0.14),Months,Fees deducted (₹),EMI (₹),Total paid (₹),Total interest (₹),True yearly rate %,Verdict and why
Row 2:
F2: =PMT(C2/12,D2,-B2)
G2: =F2*D2
H2: =G2-B2
I2: =RATE(D2,-F2,B2-E2)*12*100
Flat-rate check (when a lender quotes a flat rate in C2):
EMI = (B2+B2*C2*D2/12)/D2      true yearly rate % = RATE(D2,-EMI,B2)*12*100
All EMIs as % of take-home: =SUM(F2:F10)/take_home*100
""", ''),
    ],
    mistakes=[
        ('Looking only at the EMI.', 'A small EMI over a long time can cost far more. Check total interest and the true rate.'),
        ('Believing "flat" or "per month" rates are small.', '12% flat is about 21.6% a year on a reducing balance; 3% a month is 36% a year before compounding.'),
        ('Ignoring fees.', 'Fees taken from the loan raise the true cost. Use the amount you actually receive.'),
        ('Borrowing for wants because the EMI "fits".', 'An EMI for a want turns a want into a need for months or years.'),
    ],
    quiz=[
        {'q': 'Which formula gives the EMI of a ₹2,00,000 loan at 12% a year for 24 months?', 'o': ['=PMT(0.12/12, 24, -200000)', '=200000*0.12*2', '=PMT(0.12, 24, 200000)', '=200000/24'], 'a': 'A', 'why': 'Monthly rate, number of months, and the loan as a negative present value.'},
        {'q': 'A lender quotes "12% flat" for 2 years. Roughly what is the reducing-balance rate?', 'o': ['About 21.6% a year', '12% a year', '6% a year', '24% a year exactly'], 'a': 'A', 'why': 'Flat interest is charged on the full amount even as you repay, so the true rate is much higher.'},
        {'q': 'Why does a processing fee raise the true cost of a loan?', 'o': ['You receive less money but pay the same EMI', 'It lowers the EMI', 'It is refunded at the end', 'It doesn\'t; fees don\'t matter'], 'a': 'A', 'why': 'The true rate is calculated on what you actually receive.'},
        {'q': 'Which is most likely to be bad debt?', 'o': ['A personal loan for a holiday', 'A reasonably priced education loan for a job-oriented course', 'A home loan within your means', 'None; all debt is the same'], 'a': 'A', 'why': 'It pays for a want that leaves no lasting value, at a high cost.'},
    ],
    study='The PMT help page, OpenStax chapter 8\'s opening sections and the Key Facts Statement explainer',
    action='Build a Debts tab with the true cost of every loan you have (or one real loan offer) and a verdict for each',
)

L2 = lesson(
    M, 2,
    title='Credit cards, EMIs and Buy Now Pay Later',
    weeks=(10, 11), hours=2,
    outcome='Read a credit card statement, see why paying only the minimum is so expensive, check "no-cost EMI" offers, and use your rights under RBI\'s card rules.',
    split='25 minutes reading, 30 minutes resources, 65 minutes action',
    core=f"""
A credit card is a short loan every month. Used well, it is free: you pay the full bill by the due date and pay no interest. Used badly, it is one of the most expensive debts in India.

### How a card bill works

- **Statement date:** the bill is made, listing everything spent in the billing cycle.
- **Due date:** usually a few weeks later. Pay the **total amount due** by this date and you pay no interest.
- **Minimum amount due:** a small part of the bill. Paying it avoids a late fee, but interest is charged on the rest, at a high monthly rate written in your card's terms (look for "finance charges" in the Most Important Terms and Conditions, or MITC).
- **Lost interest-free period:** if any part of the last bill is unpaid, new purchases also start paying interest from the day you buy.

### RBI rules that protect you

RBI's card rules, as amended in March 2024 ({link('rbi-cards', 'RBI')}, {CHECK}), include:

- The statement must warn that paying only the minimum due stretches repayment and raises interest.
- **Late payment charges** apply only to the amount still unpaid after the due date, and interest only to what is outstanding after payments and refunds.
- You can **change your billing cycle** at least once.
- If you ask to **close your card** and have no dues, the issuer must close it within 7 working days or pay you ₹500 for every day of delay.
- No card can be issued or upgraded **without your consent**.

### The minimum-due trap, in numbers

**Worked example** (made-up but typical): a ₹50,000 balance at 3.5% a month, with no new spending.

{table(['How you repay', 'Months to clear', 'Total interest'], [
    ('Only the minimum: 5% of the balance (at least ₹500)', f'{MIN_M} months (about {MIN_M // 12} years)', inr(MIN_I)),
    ('A fixed ₹5,000 every month', f'{FIX_M} months', inr(FIX_I)),
])}

Paying the minimum, you would pay **more in interest than you borrowed**, and take about {MIN_M // 12} years. The rule: **pay the full bill every month**. If you can't, the card balance is your first debt to attack (FIN-M06-L05), and the card goes in a drawer until it is cleared.

### "No-cost EMI"

A "no-cost EMI" usually means the interest is hidden: the seller gives the lender a discount you would otherwise have got, or you pay a processing fee. Before choosing it, compare: (a) the price if you pay in full, (b) the total of all EMIs plus fees. If (b) is higher, it isn't no-cost.

### Buy Now Pay Later (BNPL) and small app credit

BNPL lets you pay later or in parts for online shopping. It is still a loan: missed payments bring late fees and are reported to credit bureaus, hurting your credit score (FIN-M06-L04). Many BNPL purchases are small wants, exactly the spending Module 1 asked you to choose carefully.

### Using a card well

Use one card, set up auto-pay for the **full amount**, keep spending far below the limit, and treat the card as a payment tool, not extra money. If you can't trust yourself with it yet, don't get one; a debit card and UPI do almost everything.
""",
    example=f"""
**Rahul** got a credit card six months into his job. By month five, his statement showed ₹38,000: a phone accessory, flight tickets for a friend's wedding in Bengaluru, and many small restaurant bills. He paid the minimum twice "because salary was tight that month".

In his third statement he saw finance charges of ₹1,200 and new purchases were charging interest from day one. He read the MITC, found the monthly rate, and put his balance into the payoff simulator from this lesson: paying ₹4,000 a month would clear it in about 12 months; ₹6,500 a month in about 7, with about ₹3,700 less interest.

He chose ₹6,500, took the card off his phone's payment apps, and set auto-pay to "total amount due" for after it was cleared. He kept the card: closing it wasn't necessary once he trusted himself again.
""",
    resources=[
        ('rbi-cards', 'The March 2024 amendment: minimum-due warning, late charges, billing cycle, closure in 7 working days and consent rules', '20 minutes'),
        ('ncfe', 'The e-LMS module on money and transactions: the part on cards and credit', '15 minutes'),
    ],
    steps=[
        'If you have a credit card, open your latest statement and the MITC. Find: statement date, due date, total due, minimum due, monthly interest rate and late fee. Write them down.',
        'Copy the card payoff simulator into your Debts tab and enter your balance and rate (if you have no card, use the ₹50,000 example).',
        'Compare paying the minimum with a fixed amount you can afford.',
        'Check one "no-cost EMI" offer on a shopping site or in a shop: price paid in full vs total of EMIs plus fees.',
        'If you have a card: set auto-pay to the total amount due, or write down the date you will pay in full each month.',
    ],
    proof='Your filled-in statement facts (card number covered), the simulator result comparing minimum and fixed payments, and your no-cost EMI comparison, saved in 06 Debt.',
    templates=[
        ('card payoff simulator (one row per month)', """
B1: monthly interest rate (e.g. 0.035)    D1: minimum due % (e.g. 0.05)    F1: minimum amount (e.g. 500)    H1: fixed payment (0 to use minimum)
Row 3 headings: Month,Opening balance,Interest,Payment,Closing balance
Row 4: A4: 1   B4: (your balance)
C4: =B4*$B$1
D4: =MIN(IF($H$1>0,$H$1,MAX(B4*$D$1,$F$1)),B4+C4)
E4: =B4+C4-D4
Row 5: A5: =A4+1   B5: =E4   then copy C4:E4 down to row 5
Copy row 5 down until the closing balance reaches 0.
Total interest: =SUM(C4:C200)     Months: =COUNTIF(B4:B200,">0.5")
""", ''),
        ('no-cost EMI check', """
Price if paid in full today (after any discount): ₹____
EMI ₹____ × ____ months = ₹____
Processing fee and other charges: ₹____
Total through EMI: ₹____
Is the EMI total higher than the full price? Yes / No  →  if yes, it is not "no-cost"
""", ''),
    ],
    mistakes=[
        ('Paying only the minimum due.', 'It keeps the card active but the debt alive for years. Pay the total amount due.'),
        ('Treating the credit limit as money you have.', 'The limit is the bank\'s risk appetite, not your budget.'),
        ('Missing that new purchases charge interest after a partial payment.', 'Once a bill is partly unpaid, the interest-free period is lost until you clear it.'),
        ('Collecting cards.', 'One card used well is enough. More cards mean more fees and more temptation.'),
    ],
    quiz=[
        {'q': 'What should you pay each month to avoid card interest?', 'o': ['The total amount due, by the due date', 'The minimum amount due', 'Half the bill', 'Nothing until the next bill'], 'a': 'A', 'why': 'Only paying the full bill keeps the card interest-free.'},
        {'q': 'Under RBI\'s rules, how fast must an issuer close a card with no dues after you ask?', 'o': ['Within 7 working days, or pay ₹500 a day for the delay', 'Within 90 days', 'Only after a year', 'Whenever it likes'], 'a': 'A', 'why': 'The rule includes a ₹500-a-day penalty for delays.'},
        {'q': 'In the course example, how does paying only the minimum compare with a fixed ₹5,000 a month?', 'o': ['Years longer and many times more interest', 'About the same', 'Cheaper in total', 'Faster'], 'a': 'A', 'why': 'The minimum shrinks as the balance shrinks, so repayment drags on for years.'},
        {'q': 'When is a "no-cost EMI" not really no-cost?', 'o': ['When the EMIs plus fees add up to more than the full price', 'Never', 'When you pay by UPI', 'When the shop is in Kerala'], 'a': 'A', 'why': 'Hidden interest shows up as a lost discount or a fee.'},
    ],
    study='RBI\'s March 2024 card rules and the NCFE section on cards and credit',
    action='Read your card statement (or the example), run the payoff simulator and check one no-cost EMI offer',
)

GOLD_VALUE = 216000

L3 = lesson(
    M, 3,
    title='Personal, gold, education, home and vehicle loans',
    weeks=(11, 11), hours=2,
    outcome='Compare the main loan types in India on cost, risk and rules, read a Key Facts Statement, and know your rights on prepayment, gold loans and education loans.',
    split='25 minutes reading, 30 minutes resources, 65 minutes action',
    core=f"""
### The main loans, side by side

{table(['Loan', 'Usually for', 'Security', 'What to check'], [
    ('Personal loan', 'Anything; often wants', 'None (unsecured), so rates are higher', 'True rate with fees; avoid for wants'),
    ('Gold loan', 'Short-term needs; emergencies', 'Your gold jewellery', 'Loan-to-value, interest method, renewal and auction rules'),
    ('Education loan', 'Course fees and costs', 'Sometimes none, under government schemes', 'Moratorium, interest during study, subsidy eligibility'),
    ('Home loan', 'Buying or building a house', 'The house', 'Floating vs fixed rate, tenure, prepayment, the builder\'s RERA registration'),
    ('Vehicle loan', 'Two-wheeler or car', 'The vehicle', 'Total cost; the vehicle loses value every year'),
])}

### Read the Key Facts Statement (KFS)

Before signing, ask for the **Key Facts Statement**: a short summary with the annual percentage rate (APR), all fees, the EMI schedule and penalties. For loans through apps, the KFS also names the actual regulated lender, and the lender can't charge fees that aren't in it ({link('bs-dla', 'Business Standard, July 2025')}). If a lender won't give you a KFS, walk away.

### Gold loans

Gold loans are common in Kerala and can be a sensible short-term fallback, far better than app loans. Key points:

- **Loan-to-value (LTV):** the loan as a share of the gold's value. RBI raised the LTV limit to **85% for small gold loans up to ₹2.5 lakh** in June 2025 ({link('bs-goldltv', 'Business Standard headline')}, {CHECK}). A higher LTV means more cash now and less cushion if gold prices fall.
- **How interest is paid:** monthly, or all at the end. With "bullet" repayment, interest builds up; know the total before you sign.
- **If you don't repay,** the lender can auction your gold after notices. Keep the renewal and closing dates in your calendar.
- Compare banks, NBFCs and co-operative banks on the rate, valuation, charges and auction rules.

### Education loans and PM-Vidyalaxmi

Under **PM-Vidyalaxmi**, approved in November 2024, students admitted to quality higher education institutions (based on NIRF rankings: the top 100 overall, by category or by domain, state government institutions ranked 101 to 200, and all central government institutions) can get **collateral-free, guarantor-free education loans** through a unified "PM-Vidyalaxmi" portal. The government gives a 75% credit guarantee on loans up to ₹7.5 lakh, and students with family income up to ₹8 lakh who aren't covered by other schemes get **3% interest subvention during the moratorium on loans up to ₹10 lakh** ({link('pmvl', 'PIB, November 2024')}, {CHECK}).

In most education loans, interest builds up during the course and the moratorium, then EMIs start. Calculate the EMI on the full amount you will owe when repayment starts, and compare it with the starting salary of the job the course leads to.

### Home loans and prepayment

- **Floating rate:** changes with the lender's benchmark. Many floating loans are linked to an external benchmark such as RBI's repo rate, which RBI raised from 5.25% to 5.50% in October 2026 ({link('rbi-repo', 'SCC Online')}); when it rises, your EMI or tenure can rise too.
- **Prepayment:** under RBI's directions, lenders can't charge **prepayment penalties on floating-rate loans to individuals for non-business purposes** sanctioned or renewed from 1 January 2026, whether you prepay part or all ({link('prepay', 'Angel One')}, {CHECK}). Prepaying even small amounts early in a home loan saves a lot of interest.

**Worked example:** a ₹20 lakh home loan for 20 years at 8.5% has an EMI of {inr(pmt(2000000, 0.085, 240))}. If the rate rises to 8.75%, the EMI rises by about {inr(pmt(2000000, 0.0875, 240) - pmt(2000000, 0.085, 240))} a month, or the lender extends the tenure instead.

FIN-M11-L02 covers whether to buy a house at all.

### Vehicle loans

A vehicle loses value from the day you buy it, and the loan adds interest on top. Prefer a bigger down payment and a shorter loan; include insurance, fuel and maintenance in the monthly cost (FIN-M11-L01).
""",
    example=f"""
**Rahul's** younger sister got admission to a nursing course, and the family needed ₹1,60,000 for the first year. His mother suggested a gold loan on 3 pavan (24 grams). The jeweller's valuation was {inr(GOLD_VALUE)} (made-up rate).

Rahul compared two options with the KFS of each:

{table(['', 'Gold loan from a bank', 'Education loan'], [
    ('Amount', '₹1,60,000 (about 74% of the gold\'s value)', '₹1,60,000 for year 1, more for later years'),
    ('Repayment starts', 'Interest monthly; principal within the loan term', 'After the course and moratorium'),
    ('Risk', 'The gold can be auctioned if unpaid', 'Debt in his sister\'s name, Rahul as co-borrower'),
    ('Subsidy', 'None', 'Check: does the college qualify under PM-Vidyalaxmi, and is the family income within the limit?'),
])}

They found the college wasn't on the PM-Vidyalaxmi list, but a bank education loan was still possible with Rahul as co-borrower. They chose the education loan for the course and kept the gold, because a gold loan for a four-year course would have meant renewing and worrying for four years. Rahul added the expected EMI to his Debts tab under "starts in 2030".
""",
    resources=[
        ('pmvl', 'PM-Vidyalaxmi: eligibility, guarantee and interest subvention', '10 minutes'),
        ('prepay', 'Prepayment charges: which loans, from when', '10 minutes'),
        ('bs-goldltv', 'Gold loan LTV change (headline)', '2 minutes'),
        ('rbi-repo', 'The October 2026 repo rate decision', '5 minutes'),
        ('bs-dla', 'The Key Facts Statement and checking an app lender', '10 minutes'),
    ],
    steps=[
        'For every loan in your Debts tab, find the KFS or sanction letter and note: type (floating or fixed), APR, prepayment rules and what happens if you miss a payment.',
        'If you have a floating-rate loan, check whether its rate has changed after the October 2026 repo rate decision.',
        'Fill in the loan comparison template for one real decision: two ways to borrow for the same need (for example a bank gold loan vs a personal loan), or two lenders for the same loan.',
        'If education may be in your family\'s plans, check whether the institutions you are considering qualify under PM-Vidyalaxmi, using the official portal named in the PIB release.',
        'Write a rule for gold loans: when you would use one, and which dates go in your calendar.',
    ],
    proof='Your loan comparison with KFS details for both options and your gold-loan rule, saved in 06 Debt.',
    templates=[
        ('loan comparison', """
Need: ____  Amount: ₹____
,Option A,Option B
Lender (regulated? name on KFS),,
Type (personal / gold / education / home / vehicle),,
APR from the KFS,,
Fees (₹),,
EMI (₹) =PMT(rate/12,months,-amount),,
Total interest (₹),,
Prepayment rules,,
Security (gold / house / vehicle / none),,
What happens if I miss a payment,,
Decision and why:
""", 'csv'),
    ],
    mistakes=[
        ('Signing without a KFS.', 'The KFS is your one-page truth. No KFS, no loan.'),
        ('Forgetting gold loan dates.', 'Missed renewals can lead to auction notices. Put dates in your calendar.'),
        ('Ignoring interest during an education loan\'s moratorium.', 'Interest usually builds up during the course; plan the EMI on the full amount.'),
        ('Never prepaying.', 'On floating-rate personal (non-business) loans from 2026 there is no prepayment penalty; small prepayments save a lot.'),
    ],
    quiz=[
        {'q': 'What did RBI change for small gold loans in June 2025, per the course\'s source?', 'o': ['LTV up to 85% for loans up to ₹2.5 lakh', 'Gold loans were banned', 'LTV cut to 50%', 'No interest on gold loans'], 'a': 'A', 'why': 'The headline reports an 85% LTV for small gold loans up to ₹2.5 lakh.'},
        {'q': 'Under PM-Vidyalaxmi, who gets 3% interest subvention?', 'o': ['Students with family income up to ₹8 lakh, on loans up to ₹10 lakh, during the moratorium', 'Everyone, on any loan', 'Only students abroad', 'Only government employees'], 'a': 'A', 'why': 'Those are the conditions in the PIB release (check current rules).'},
        {'q': 'You have a floating-rate home loan sanctioned in 2026 for your own house. Can the bank charge a penalty if you prepay part of it?', 'o': ['No, under RBI\'s directions for individuals\' non-business floating loans', 'Yes, always 2%', 'Only if you prepay in cash', 'Only in the first year'], 'a': 'A', 'why': 'Prepayment charges are not allowed on such loans sanctioned or renewed from 1 January 2026.'},
        {'q': 'What is a Key Facts Statement?', 'o': ['A short summary of a loan\'s APR, fees, schedule and penalties', 'Your credit report', 'An income tax form', 'A gold valuation certificate'], 'a': 'A', 'why': 'It lets you compare loans on one page, and fees outside it can\'t be charged.'},
    ],
    study='PM-Vidyalaxmi, the prepayment rules, the gold loan LTV change, the repo rate decision and the KFS explainer',
    action='Note KFS details for your loans and compare two ways to borrow for one real need',
)

L4 = lesson(
    M, 4,
    title='Credit scores and credit reports',
    weeks=(12, 12), hours=1.5,
    outcome='Get your free credit report, read it, dispute any error, and know what builds or damages a credit score.',
    split='20 minutes reading, 20 minutes resources, 50 minutes action',
    core=f"""
### What a credit report is

A **credit report** is your borrowing history: every loan and card in your name, the limits and balances, and whether each payment was on time. **Credit information companies** (often called credit bureaus) collect it from lenders. India has four: **TransUnion CIBIL, Equifax, Experian and CRIF High Mark** ({link('sc-freereport', 'StudyCafe, September 2026')}).

A **credit score** is a three-digit summary of the report; higher is better. Lenders use it to decide whether to lend and at what rate. Some employers and landlords look at reports too.

### Your rights, as of November 2026

- **One free full credit report (with score) a year from each of the four bureaus,** requested on the bureau's own website with your PAN, date of birth and mobile number. Never pay a third party for it ({link('sc-freereport', 'StudyCafe')}).
- **Fresher data:** from January 2025, lenders report your credit information **every 15 days**, so corrections and repayments show up faster ({link('ml-fortnight', 'Moneylife')}).
- **Alerts:** bureaus must alert you by SMS or email when lenders and other specified users check your report ({link('om-cic-alert', 'Outlook Money, January 2025')}). An alert you didn't expect can mean someone is applying for credit in your name.
- **Fixing errors:** lenders must send corrections to the bureau within 21 days, and bureaus must resolve complaints within 30 days, or pay you **₹100 a day** for the delay ({link('ml-cic30', 'Moneylife')}, {CHECK}).

### What builds a good score

- **Paying every EMI and card bill on time.** This matters most. One missed payment can stay visible for years.
- **Using a small part of your card limits.** A card that is always near its limit looks risky.
- **A long, clean history.** Keep your oldest well-run account open.
- **Not applying for many loans or cards at once.** Each application can lead to a lender enquiry on your report.

### What damages it

- Late or missed payments, including small ones such as BNPL or a phone EMI
- "Settled" loans: when a lender accepts less than the full amount, the report says so, and future lenders notice
- Being a **guarantor or co-borrower** on a loan that isn't repaid: it is your debt too
- **Loans you never took:** identity fraud. Check your report for accounts you don't recognise.

### No history is not bad history

If you have never borrowed, you may have no score. That is fine. Don't take a loan just to "build a score". If you want a history, one card used lightly and paid in full every month builds it safely.
""",
    example=f"""
**Fathima** downloaded her free report from one bureau. Most of it was correct: her two-wheeler loan, closed in 2024, and her credit card. But it also showed a **personal loan of ₹40,000 from an NBFC she had never heard of**, marked overdue.

She remembered sharing her PAN and Aadhaar photos with a "loan agent" on WhatsApp two years earlier, for a loan she never took. She raised a dispute on the bureau's website, reported the identity misuse to the lender in writing, and filed a complaint on the cyber crime portal. The lender confirmed it couldn't verify the loan; the entry was removed within the 30-day limit.

She now checks one bureau every four months (rotating between the four, so she gets three free reports a year), and she never sends ID photos on WhatsApp.
""",
    resources=[
        ('sc-freereport', 'How to get one free report a year from each bureau, step by step', '10 minutes'),
        ('ml-fortnight', 'Why your credit data now updates every 15 days', '5 minutes'),
        ('om-cic-alert', 'Alerts when your report is accessed', '5 minutes'),
        ('ml-cic30', 'The 21-day and 30-day complaint timelines and ₹100-a-day compensation', '5 minutes'),
    ],
    steps=[
        'Request your free full credit report from one bureau on its official website. Type the address yourself; don\'t use ads or links from messages.',
        'Check every account in the report: is it yours, are the balances and limits right, are the payment records correct?',
        'List anything wrong in the credit report checklist. If something is wrong, raise a dispute on the bureau\'s website and keep the reference number.',
        'Note your score (if shown), and the date. Set reminders to check the next bureau in four months.',
        'If you have no credit history, write that down: it is a valid result.',
    ],
    proof='A screenshot of your report\'s summary page (PAN and account numbers covered), your completed checklist and any dispute reference number, saved in 06 Debt.',
    templates=[
        ('credit report checklist', """
Bureau: ____  Date: ____  Score (if shown): ____
[ ] My name, date of birth, PAN and addresses are correct
[ ] Every loan and card listed is mine
[ ] No accounts I don't recognise (if any: dispute + report identity misuse)
[ ] Balances and limits match my statements
[ ] Payment history is correct (no wrong "late" marks)
[ ] Closed loans show as closed, not "settled" (unless they really were)
[ ] Loans where I am a guarantor or co-borrower: ____
Disputes raised (reference numbers): ____
Next free report: bureau ____ on ____
""", ''),
    ],
    mistakes=[
        ('Paying for your credit report.', 'You get one free full report a year from each bureau on its own website.'),
        ('Sharing ID documents with "loan agents" on messaging apps.', 'Your PAN and Aadhaar can be misused to take loans in your name.'),
        ('Settling a loan for less to "close the matter".', 'It shows as settled, which can hurt future borrowing. Talk to the lender about restructuring first.'),
        ('Becoming a guarantor casually.', 'If the borrower doesn\'t pay, it is your debt and your report.'),
    ],
    quiz=[
        {'q': 'How many free full credit reports can you get each year in India, as of November 2026?', 'o': ['One from each of the four credit bureaus', 'None', 'One in total', 'Unlimited from any app'], 'a': 'A', 'why': 'Each of the four bureaus gives one free full report a year.'},
        {'q': 'A bureau doesn\'t resolve your complaint within 30 days. What does RBI\'s framework provide?', 'o': ['Compensation of ₹100 a day for the delay', 'Nothing', 'A free loan', 'Your score is reset to the maximum'], 'a': 'A', 'why': 'The rule sets ₹100 a day after 30 days (check current rules).'},
        {'q': 'You get an alert that a lender checked your report, but you didn\'t apply for anything. What could it mean?', 'o': ['Someone may be applying for credit in your name', 'Your score went up', 'Your loan was waived', 'Nothing at all'], 'a': 'A', 'why': 'Unexpected checks can be a sign of identity misuse; investigate.'},
        {'q': 'Which hurts a credit score?', 'o': ['A missed EMI, even a small one', 'Checking your own free annual report', 'Having no loans', 'Paying your card bill in full'], 'a': 'A', 'why': 'Payment history matters most; a missed payment stays visible.'},
    ],
    study='The free annual report guide, fortnightly reporting, access alerts and the complaint timelines',
    action='Download one free credit report, check it with the checklist and dispute any error',
)


def payoff(order):
    debts = [dict(n='Credit card', b=30000.0, r=0.42, m=1500), dict(n='Personal loan', b=80000.0, r=0.16, m=2800), dict(n='Gold loan', b=60000.0, r=0.095, m=600)]
    budget, months, interest = 8900, 0, 0.0
    while any(d['b'] > 0.5 for d in debts) and months < 600:
        months += 1
        for d in debts:
            if d['b'] > 0:
                i = d['b'] * d['r'] / 12
                d['b'] += i
                interest += i
        left = budget
        for d in debts:
            if d['b'] > 0:
                p = min(d['m'], d['b'])
                d['b'] -= p
                left -= p
        for d in sorted([d for d in debts if d['b'] > 0], key=order):
            p = min(left, d['b'])
            d['b'] -= p
            left -= p
            if left <= 0:
                break
    return months, interest


AV_M, AV_I = payoff(lambda d: -d['r'])
SN_M, SN_I = payoff(lambda d: d['b'])

L5 = lesson(
    M, 5,
    title='Getting out of debt, and loan-app traps',
    weeks=(12, 12), hours=2,
    outcome='Choose the avalanche or snowball method, build a month-by-month payoff plan, and recognise and escape illegal loan apps.',
    split='25 minutes reading, 25 minutes resources, 70 minutes action',
    core=f"""
### Step 1: stop digging

While you pay off debt, take **no new debt for wants**. Put cards away, delete shopping and BNPL apps, and keep a starter emergency fund (Module 5), so the next surprise doesn't go on a card.

### Step 2: list every debt

In your Debts tab: lender, balance, interest rate, minimum payment. Include family loans and chitty prizes you still owe instalments on.

### Step 3: pay every minimum, then attack one debt

Pay the minimum on all debts. Put **every extra rupee** on one target debt. When it is cleared, add its payment to the next one. Two ways to choose the order:

- **Avalanche:** highest interest rate first. Saves the most money.
- **Snowball:** smallest balance first. Gives quick wins that keep you going.

**Worked example** (made-up): three debts and a total of ₹8,900 a month for debt payments.

{table(['Debt', 'Balance', 'Rate', 'Minimum'], [
    ('Credit card', '₹30,000', '42% a year', '₹1,500'),
    ('Personal loan', '₹80,000', '16% a year', '₹2,800'),
    ('Gold loan', '₹60,000', '9.5% a year', '₹600 (interest)'),
])}

{table(['Method', 'Order', 'Months to debt-free', 'Total interest'], [
    ('Avalanche', 'Card, personal loan, gold loan', str(AV_M), inr(AV_I)),
    ('Snowball', 'Card, gold loan, personal loan', str(SN_M), inr(SN_I)),
])}

Here the avalanche saves {inr(SN_I - AV_I)}. Because the smallest debt was also the most expensive, both start with the card. Choose the avalanche if you are motivated by numbers, the snowball if you need early wins; either beats paying minimums forever.

### Step 4: lower the rate where you safely can

- Ask your card issuer about converting the balance to a lower-rate EMI, and compare the true rate (FIN-M06-L01).
- Replacing card or app debt with a cheaper loan, such as a bank gold loan, can help, but only if you stop using the card. Otherwise you end up with both.
- If you truly can't pay, **talk to the lender early** about restructuring. Avoid settlements unless there is no other way (FIN-M06-L04).

### Loan-app traps

Illegal digital lenders target people who need small amounts fast. Warning signs ({link('bs-dla', 'Business Standard, July 2025')}):

- Money given **without proper KYC**, or a loan you didn't fully apply for
- Charges of **10% to 20% a month**, upfront "processing" fees, very short terms
- The app asks for access to your **contacts, photos and gallery**, then threatens to message your family or post edited photos
- **No Key Facts Statement** naming a regulated lender

**Check before borrowing:** RBI publishes a directory of digital lending apps reported by regulated lenders (RBI homepage → Citizen's corner → "DLA deployed by regulated entities") ({link('rbi-dla', 'RBI press release, May 2025')}, {link('mn-dla', 'MediaNama')}). Check the exact app name and that the lender named in the KFS is the regulated entity. The directory shows what lenders report; RBI says it doesn't validate each app, so still read the KFS.

**If you are already trapped:**

1. Don't borrow from another app to repay the first; that is how the trap deepens.
2. Pay what you legitimately owe only through the lender's official channels, and keep records.
3. Revoke the app's permissions and uninstall it after saving your loan details.
4. If you are harassed or threatened, report it to the police and to **1930** or the cyber crime portal. Tell your family before the app does; it takes away the threat's power.
5. If the lender is regulated, complain to it, and then to the RBI Ombudsman (FIN-M04-L02).

Private moneylenders who charge very high daily or weekly interest ("blade" lenders) are a similar trap offline. A bank gold loan or help from family is almost always cheaper.
""",
    example=f"""
In a slow month, **Anu's** cousin Vishnu, 24, borrowed ₹5,000 through an app he found in an Instagram ad. ₹3,800 reached his account after "processing fees", and the app demanded ₹6,500 in 7 days. He couldn't pay, so a second app "helped" him repay the first. Within a month he owed four apps ₹31,000, and one of them sent messages to his contacts calling him a thief.

Anu helped him take four steps: they listed every app and amount; checked each on RBI's directory (two weren't there at all); Vishnu told his parents the whole story before the apps could; and they reported the harassment on 1930 and the cyber crime portal. His father paid off the two apps linked to regulated lenders through their official channels, and Vishnu repaid his father over six months, interest-free. He stopped paying the unlisted apps' demands, kept all records, and gave them to the police.

"The shame was worse than the debt," Vishnu said. "Once my family knew, the threats stopped working."
""",
    resources=[
        ('rbi-dla', 'RBI\'s Digital Lending Directions, 2025 and the public directory of lending apps', '10 minutes'),
        ('bs-dla', 'How to check an app on RBI\'s list, and the warning signs', '10 minutes'),
        ('mn-dla', 'How the directory works and what it does and doesn\'t verify', '5 minutes'),
        ('kp-1930', 'Reporting harassment and fraud: 1930 and the portal', '5 minutes'),
    ],
    steps=[
        'Complete the debt list in your Debts tab: balance, rate and minimum payment for each debt.',
        'Decide how much you can put towards debts each month in total (from your budget).',
        'Choose avalanche or snowball, sort the list with the RANK formula in the template and write your order.',
        'Build the month-by-month payoff plan for your first target debt (or the example, if you have no debts) and find the month you will be debt-free.',
        'Check any loan app on your phone against RBI\'s directory. Remove apps you don\'t need and revoke contacts and gallery permissions from finance apps that don\'t need them.',
        'Write your loan-app rule: for example, "I never borrow from an app I found through an ad or a message, and I check every lender in RBI\'s directory first."',
    ],
    proof='Your sorted debt list with payoff order and debt-free month (or the worked example if you have no debts), and your loan-app rule, saved in 06 Debt.',
    templates=[
        ('payoff order (Debts tab)', """
Row 1: Debt,Balance (₹),Annual rate,Minimum (₹),Avalanche order,Snowball order
E2: =RANK(C2,$C$2:$C$10,0)     (1 = highest rate)
F2: =RANK(B2,$B$2:$B$10,1)     (1 = smallest balance)
Total minimums: =SUM(D2:D10)    Extra for the target debt: =total_for_debts-SUM(D2:D10)
""", ''),
        ('target-debt payoff (one row per month)', """
Row 1: Month,Opening balance,Interest,Payment,Closing balance
Row 2: 1, (balance), =B2*annual_rate/12, (minimum + extra), =B2+C2-D2
Row 3: =A2+1, =E2, =B3*annual_rate/12, (same payment), =B3+C3-D3   ... copy down until 0
When it reaches 0: add its payment to the next debt's payment.
""", ''),
        ('loan-app check', """
App name exactly as in the store: ____
Listed in RBI's directory (Citizen's corner → "DLA deployed by regulated entities")? Yes / No
Regulated lender named in the KFS: ____
Permissions it asks for (contacts / photos / location): ____
Upfront fee or no KYC?  Yes / No
Decision: ____
""", ''),
    ],
    mistakes=[
        ('Paying debts without a plan.', 'Spreading extra money thinly means every debt lasts longer. Pick one target.'),
        ('Borrowing from a new app to repay an old one.', 'It deepens the trap. Stop, list, tell family, report.'),
        ('Moving card debt to a loan and keeping the card in use.', 'You end up with both. Put the card away until you are clear.'),
        ('Hiding debt from family out of shame.', 'Lenders who harass rely on secrecy. Telling your family takes away their power.'),
    ],
    quiz=[
        {'q': 'Which debt does the avalanche method attack first?', 'o': ['The one with the highest interest rate', 'The smallest balance', 'The oldest loan', 'The gold loan always'], 'a': 'A', 'why': 'Highest rate first saves the most interest.'},
        {'q': 'Why might someone choose the snowball method instead?', 'o': ['Quick wins from clearing small debts keep them motivated', 'It always saves more money', 'Banks require it', 'It removes interest'], 'a': 'A', 'why': 'Motivation matters; the snowball trades a little money for momentum.'},
        {'q': 'Which is a warning sign of an illegal loan app?', 'o': ['It asks for access to your contacts and photos and charges 10% a month', 'It gives a Key Facts Statement naming a regulated lender', 'It appears in RBI\'s directory with the right lender', 'It asks for KYC'], 'a': 'A', 'why': 'Contact access, huge charges and no KFS are classic signs.'},
        {'q': 'Where can you check whether a lending app is reported by a regulated lender?', 'o': ['RBI\'s directory of digital lending apps (Citizen\'s corner)', 'The app\'s own reviews only', 'A WhatsApp group', 'Nowhere'], 'a': 'A', 'why': 'RBI publishes the directory; still read the KFS.'},
        {'q': 'A loan app threatens to message your contacts. What is a good first step?', 'o': ['Tell your family yourself and report to 1930 or the cyber crime portal', 'Borrow from another app to pay', 'Send more personal documents', 'Delete all records'], 'a': 'A', 'why': 'Telling family removes the threat\'s power; reporting starts action against the harassers.'},
    ],
    study='RBI\'s digital lending directions and app directory, the warning signs, and how to report harassment',
    action='Build your payoff order and plan, check your loan apps and write your loan-app rule',
)

LESSONS = [L1, L2, L3, L4, L5]

MODULE = module(
    M,
    title='Debt and credit',
    weeks=(10, 12), hours=11,
    overview="""
Understand what borrowing really costs, use credit cards safely, compare loans, read your credit report, and get out of debt with a clear plan, without falling into loan-app traps.

Debt can build a life (a sensible education or home loan) or eat one (card balances, flat-rate EMIs, illegal apps). The difference is usually the true cost and whether you can repay from normal income. This module gives you the formulas to see the real cost of any loan, the rules that protect you as a borrower, and a step-by-step way out of debt.

You also download your free credit report and check it for errors and fraud, and you learn how to check any lending app against RBI's public directory. Your Debts tab becomes part of your final plan, even if it shows ₹0 (that is a great result).
""",
    outcomes=[
        'Calculate EMI, total interest and the true yearly rate of any loan, including fees',
        'Explain how credit card interest works and why paying the minimum is so expensive',
        'Compare personal, gold, education, home and vehicle loans and read a Key Facts Statement',
        'Get, read and dispute your credit report',
        'Plan a debt payoff with the avalanche or snowball method and avoid illegal loan apps',
    ],
    lessons=LESSONS,
    project='The true cost of my loans and my debt payoff plan',
    project_steps=[
        'Complete the Debts tab: every debt with EMI, total interest, true rate and verdict (or one real loan offer if you have no debts).',
        'Add your payoff order and the month you will be debt-free, with the monthly amount from your budget.',
        'Note your credit report check: date, bureau, errors found and disputes.',
        'Write your three borrowing rules, for example: "I pay my card in full every month", "I never borrow for wants", "I check every lender in RBI\'s directory and read the KFS first".',
        'Add total debt to your Net Worth tab and debt payments to your Budget tab.',
    ],
    project_proof='A screenshot of your completed Debts tab with payoff plan and your three borrowing rules, saved in 06 Debt.',
    rubric=[
        ('True cost', 'EMIs only', 'Interest calculated, fees ignored', 'EMI, total interest and true rate including fees, for every loan'),
        ('Cards', 'Not reviewed', 'Statement read', 'Payoff simulated and full-payment habit set'),
        ('Loan knowledge', 'Can\'t compare', 'Knows the types', 'Compared two options for a real need using the KFS'),
        ('Credit report', 'Not checked', 'Downloaded', 'Checked line by line, with disputes raised if needed'),
        ('Payoff plan', 'None', 'Order chosen', 'Monthly plan with a debt-free date, and loan-app rules written'),
    ],
    short=[
        'List every debt with balance, rate and minimum (FIN-M06-L05, step 1).',
        'Calculate the true rate of your most expensive debt (FIN-M06-L01).',
        'Download one free credit report and check it (FIN-M06-L04).',
        'Write your loan-app rule.',
    ],
    flashcards=[
        ('EMI formula in a spreadsheet', '=PMT(annual_rate/12, months, -loan_amount)'),
        ('"12% flat" for 2 years is roughly', 'About 21.6% a year on a reducing balance.'),
        ('Credit card rule', 'Pay the total amount due, every month, by the due date.'),
        ('Card closure rule', 'Within 7 working days if no dues, or ₹500 a day for the delay.'),
        ('Prepayment rule from 2026', 'No prepayment charges on individuals\' floating-rate loans for non-business purposes sanctioned or renewed from 1 January 2026.'),
        ('Free credit reports', 'One full report a year from each of the four bureaus, on their own websites.'),
        ('Avalanche vs snowball', 'Avalanche: highest rate first, saves most. Snowball: smallest balance first, quick wins.'),
        ('Checking a lending app', 'RBI directory of digital lending apps (Citizen\'s corner) and the lender named in the KFS.'),
    ],
    mistakes=[
        ('Thinking "everyone has EMIs, so it\'s fine".', 'Common doesn\'t mean cheap. Calculate the true cost of each one.'),
        ('Ignoring small debts.', 'BNPL and phone EMIs affect your credit report as much as big loans.'),
        ('Facing debt alone.', 'Talk to the lender early and tell family; secrecy makes every debt worse.'),
    ],
    project_week=12,
)
