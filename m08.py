from common import lesson, module, link, rules, xref, table, fence, Q, RULE, ASOF, CHECK
import tools

NOTE = f'Interest rates, fees and bank rules change and differ by bank. The 8.5% rate used here is an **illustration only**; get current rates from banks. This is education, not financial advice. Rules are {RULE}.'

LTV = [
    ('Up to ₹30 lakh', 'Up to 90% of the property value'),
    ('Above ₹30 lakh up to ₹75 lakh', 'Up to 80%'),
    ('Above ₹75 lakh', 'Up to 75%'),
]

L1 = lesson(
    8, 1,
    outcome='You can explain home loans and loans against property, estimate a buyer\'s loan eligibility and down payment, and calculate EMIs in Sheets.',
    split='20 minutes reading, 40 minutes on calculations and a bank visit',
    core=f"""
{NOTE}

**Home loan.** A loan to buy or build a house, or to buy a plot and build on it. Banks, housing finance companies and cooperative banks lend. Key terms:
- **Loan-to-value (LTV):** the maximum share of the property value the bank can lend. RBI limits for housing loans (as reported in 2015, {link('bs-ltv', 'Business Standard')}; {CHECK}):
{table(['Loan amount', 'Maximum LTV'], LTV)}
  Stamp duty and registration costs are usually **not** included in the value for LTV, so the buyer pays them from savings.
- **Eligibility:** banks look at income, existing EMIs, age, job stability, credit score and the property's legal and technical check. Many banks keep total EMIs within roughly 40% to 60% of net monthly income (this ratio varies by bank and is not a fixed rule).
- **Interest:** floating rates linked to a benchmark are common; the rate changes over the loan's life.
- **Fees:** processing fee, legal and valuation charges, and mortgage registration costs.
- **Process:** application → documents → sanction letter → bank's legal check (title, 13 to 30 year EC) and technical valuation → agreement → registration of the sale deed and mortgage → disbursement to the seller.
- **Plot loans** (for land only) usually have lower LTV and stricter rules; agricultural or nilam land generally won't qualify.

**Loan against property (LAP).** A loan secured on property you already own, used for business or other needs. Interest is usually higher than home loans, and you can **lose the property** if you can't repay.

**EMI.** Equated monthly instalment. In Sheets or LibreOffice:
{fence(tools.EMI)}

**Leverage risk.** A loan lets you control a bigger property, but EMIs are fixed while rents and prices are not. If the tenant leaves, rates rise or prices fall, the borrower still pays. Many families in Kerala have been stretched by loans for houses built bigger than their income could support. The {xref('fin', 'fin-m06-l03', 'Personal Finance lesson on home and other loans')} and {xref('fin', 'fin-m11-l02', 'rent-or-buy lesson')} go deeper.
""",
    example="""
**A teacher couple** with a combined net income of ₹45,000 a month and an existing vehicle EMI of ₹5,000 want a house worth ₹25 lakh near Kuttiady.
- If the bank allows total EMIs of 50% of net income: 45,000 × 0.5 = ₹22,500; minus ₹5,000 existing = **₹17,500** for the new EMI.
- Maximum loan at 8.5% for 20 years: `=-PV(0.085/12, 240, 17500)` ≈ **₹20.2 lakh**.
- LTV limit: ₹25 lakh is below ₹30 lakh, so up to 90% = ₹22.5 lakh. Income is the tighter limit: about **₹20.2 lakh**.
- Down payment: 25 − 20.2 = **₹4.8 lakh**, plus stamp duty and fee (about ₹2.5 lakh at 10%) and other costs: they need about **₹7.5 lakh** of their own money.
Sachin tells them this before showing houses, so they don't fall in love with a house they can't afford.
""",
    calc="""
- EMI on ₹20 lakh at 8.5% for 20 years: `=-PMT(0.085/12, 240, 2000000)` ≈ **₹17,357**
- Total paid: 17,357 × 240 ≈ ₹41.7 lakh; total interest ≈ **₹21.7 lakh**, more than the loan itself.
- Same loan for 15 years: `=-PMT(0.085/12, 180, 2000000)` ≈ ₹19,695; total interest ≈ ₹15.5 lakh.
- If the rate rises to 10% (20 years): ≈ ₹19,300 a month, about ₹1,950 more.
""",
    rules_rows=[
        ('RBI LTV limits for housing loans', 'Up to ₹30 lakh: 90%; ₹30–75 lakh: 80%; above ₹75 lakh: 75%', 'Business Standard, October 2015'),
    ],
    pro="""
- **Bank\'s advocate and valuer:** do the legal and technical checks for the loan.
- **Chartered accountant:** tax benefits on home loans, which depend on the tax regime and current law.
""",
    resources=[
        ('bs-ltv', 'Read the LTV rules', '5 minutes'),
        ('lt-fin', 'Read the time value of money chapter on loans and annuities (chapters 7 to 9)', '30 minutes'),
        ('os-fin', 'Use the OpenStax book as the reference for the formulas', '10 minutes'),
    ],
    steps=[
        'Add the EMI formulas to your workbook and check that ₹25 lakh at 8.5% for 20 years gives about ₹21,700.',
        'Visit or call one bank and one cooperative bank near you and ask: current home loan rate range, processing fee, documents needed, how long sanction takes, and whether they finance plots. Note the date.',
        'Work out the eligibility and down payment for a sample buyer (or a real client with permission).',
        'Write a one-page "home loan basics" sheet for your clients.',
    ],
    proof='Your EMI sheet, notes from two lenders with dates, one eligibility calculation and your client sheet.',
    templates=[('Loan eligibility calculator', """LOAN ELIGIBILITY (tab "Loan")    rates as of ______ (ask the bank)
B1 Net monthly income            B2 Existing EMIs
B3 EMI ratio allowed (e.g. 0.5)  B4 Max new EMI          =B1*B3-B2
B5 Interest rate (e.g. 0.085)    B6 Years (e.g. 20)
B7 Max loan by income            =-PV(B5/12, B6*12, B4)
B8 Property value                B9 LTV limit            =IF(B8<=3000000,0.9,IF(B8<=7500000,0.8,0.75))
B10 Max loan by LTV              =B8*B9
B11 Loan possible                =MIN(B7,B10)
B12 Down payment                 =B8-B11
B13 Stamp duty + fee (10%)       =MAX(B8,fair_value)*0.10
B14 Own money needed             =B12+B13+other_costs""")],
    mistakes=[
        ('Showing houses before checking affordability.', 'Work out eligibility first.'),
        ('Forgetting that stamp duty is not financed.', 'Plan for it in own money.'),
        ('Assuming rates stay fixed.', 'Test a higher rate.'),
    ],
    fraud="""
**Loan "agents" promising guaranteed sanction.** Some take fees to "arrange" loans on property with title problems or fake income papers. Fake income documents are fraud. Send clients directly to banks and never touch fake papers.
""",
    quiz=[
        Q('What is the maximum LTV for a ₹25 lakh home loan under the RBI limits?', '90%', '50%', '100%', '75%', why='Up to ₹30 lakh: 90%.'),
        Q('Which formula gives the monthly EMI in Sheets?', '=-PMT(rate/12, years*12, loan)', '=SUM(loan)', '=loan/12', '=PV(loan)', why='PMT gives the payment.'),
        Q('Why is a loan against property risky?', 'You can lose the property if you can\'t repay', 'It has no interest', 'It can\'t be repaid early', 'It is illegal', why='The property is security.'),
        Q('What costs does a buyer usually pay from own money?', 'Down payment plus stamp duty and registration', 'Only the EMI', 'Nothing', 'Only the broker', why='Banks lend on property value, not duty.'),
    ],
    study='read the lesson and the EMI formulas',
    action='build the EMI and eligibility sheets and collect loan terms from two lenders',
)

L2 = lesson(
    8, 2,
    outcome='You can calculate the full cost of buying and owning a property, gross and net rental yield, cap rate, cash-on-cash return and a basic IRR, and explain why many small investors earn less than they expect.',
    split='20 minutes reading, 70 minutes on calculations for 5 real properties',
    core=f"""
{NOTE}

**Total cost of buying** (cost tab in your toolkit; RE-M04-L01):
- Price + stamp duty (8%) + registration fee (2%) on the higher of price or fair value, + document writer or advocate fee + EC and copies + brokerage (often 1% to 2%, plus 18% GST if the broker is registered) + loan fees.
- In Kerala, buying costs often add **10% to 12%** to the price, so a property must rise that much just to break even.
- TDS (1% if the value is ₹50 lakh or more) is not an extra cost: it is part of the price paid to the government on the seller's behalf (RE-M09-L01).

**Cost of owning:** land tax, building tax, maintenance, repairs, insurance, electricity and water when vacant, caretaking if you live away, and the **opportunity cost** (what the money could earn elsewhere, for example in a fixed deposit).

**Returns:**
- **Gross yield** = annual rent ÷ price.
- **Net yield (cap rate)** = NOI ÷ price (RE-M07-L02).
- **Cash-on-cash return** = annual cash flow after EMI ÷ own cash invested.
- **IRR (internal rate of return):** the yearly return that accounts for all cash in and out over time, including the final sale. In Sheets: `=IRR(range)`.

**Honest truth about small investors.** Returns often disappoint because of: high buying costs (10%+), low rental yields, vacancies, repairs, illiquidity (land can take months or years to sell), legal disputes, and buying at peaks. Many people count only the price rise and ignore costs, interest and time. Always compare with a simple alternative such as a fixed deposit or an index fund ({xref('fin', 'fin-m09-l06', 'Personal Finance: gold, REITs and real estate')}).

The full Cost and ROI calculators with working formulas are in the templates below and in your toolkit.
""",
    example="""
**A rented house near Kuttiady, bought with a loan** (illustrative):
- Price ₹40 lakh; buying costs about ₹4.1 lakh; total ₹44.1 lakh.
- Rent ₹12,000 a month. Gross yield: 1,44,000 ÷ 40,00,000 = **3.6%**.
- NOI: rent for 11 months (1 vacant) ₹1,32,000, minus taxes ₹6,000, maintenance ₹20,000, insurance ₹3,000 = **₹1,03,000**. Net yield: **2.6%**.
- Loan ₹25 lakh at 8.5% for 20 years: EMI ≈ ₹21,700 (₹2.6 lakh a year).
- Own cash: 44.1 − 25 = ₹19.1 lakh. Cash flow: 1,03,000 − 2,60,400 ≈ **−₹1.57 lakh a year**. Cash-on-cash: **−8.2%**.
The owner pays ₹13,000 a month from salary and hopes prices rise. That is a bet on price growth, not an income investment.

**Land held for 5 years, no loan:** buy ₹20 lakh + ₹2.2 lakh costs = ₹22.2 lakh. Sell for ₹27 lakh after 5 years, minus 2% brokerage = ₹26.46 lakh. IRR ≈ **3.6% a year before capital gains tax**: likely less than a fixed deposit, and with much more risk.
""",
    calc="""
**IRR in Sheets** for the land example: A1 `-2220000`, A2 to A5 `0` (or minus yearly land tax), A6 `2646000`. Then `=IRR(A1:A6)` ≈ 3.6%.
**Check by hand:** (26.46 ÷ 22.2) ^ (1/5) − 1 = 1.192 ^ 0.2 − 1 ≈ 0.036.
**Break-even rise needed** just to cover buying and selling costs: (22.2 ÷ 0.98) ÷ 20 − 1 ≈ **13.3%**.
""",
    resources=[
        ('lt-fin', 'Read the chapter on net present value and IRR in Principles of Finance', '30 minutes'),
        ('mit-re', 'Optional: lecture notes on investment returns', '20 minutes'),
        ('sy-stamp', 'Check current stamp duty for the cost tab', '5 minutes'),
    ],
    steps=[
        'Build the Cost and ROI tabs in your workbook from the templates.',
        'Calculate the full cost of one purchase using current official stamp duty and fee rates (date-stamped) and real quotes for the writer\'s fee.',
        'Choose 5 real properties (houses or shops for sale where you can estimate rent from local rental listings) and calculate gross yield, net yield, cash-on-cash (with and without a loan) and a 5-year IRR for each.',
        'Write a half-page conclusion: which property type has the best yield locally, and how each compares with a fixed deposit rate you looked up.',
    ],
    proof='The Cost tab for one purchase and the ROI tab for 5 properties with sources and dates, plus your conclusion.',
    templates=[('Full cost of a purchase', tools.COST_CALC), ('Rental yield and return calculator', tools.ROI_CALC)],
    mistakes=[
        ('Counting only the price rise.', 'Include buying, owning and selling costs, interest and time.'),
        ('Using asking rent.', 'Use actual rents from local listings and brokers.'),
        ('Ignoring vacancy.', 'Allow at least one vacant month a year.'),
    ],
    fraud="""
**"Guaranteed return" schemes.** Some projects and agents promise guaranteed rent or returns ("12% assured"). Real property returns are not guaranteed; such promises are often unsustainable or fraudulent. Check who guarantees it, in writing, and with what assets.
""",
    quiz=[
        Q('About how much do buying costs often add to a Kerala property\'s price?', '10% to 12%', '1%', '50%', 'Nothing', why='8% + 2% plus fees and brokerage.'),
        Q('Rent ₹10,000 a month on a ₹30 lakh house. Gross yield?', '4%', '10%', '0.4%', '40%', why='1,20,000 ÷ 30,00,000.'),
        Q('What is cash-on-cash return?', 'Annual cash flow after EMI ÷ own cash invested', 'Rent ÷ price', 'Price ÷ rent', 'EMI ÷ rent', why='It shows the return on your own money.'),
        Q('Why do many small investors earn less than expected?', 'High costs, low yields, vacancies, illiquidity and disputes', 'Property always doubles', 'There are no costs', 'Banks pay them', why='Count everything.'),
        Q('Which Sheets function gives IRR?', '=IRR(range)', '=PMT()', '=SUM()', '=MEDIAN()', why='List yearly cash flows first.'),
    ],
    study='read the lesson and both worked examples',
    action='calculate the full cost of one purchase and yield and returns for 5 real properties',
    fulltime='Do 10 properties and add a sensitivity table (rent ±10%, price growth 0%, 3%, 6%).',
)

LESSONS = [L1, L2]

MODULE = module(
    8,
    overview=f"""
Real estate finance: home loans and loans against property, eligibility, EMIs, leverage risk, the full cost of buying and owning, rental yield, cap rate, cash-on-cash return and basic IRR, with honest numbers on why small investors often earn less than they expect.

These numbers let you advise clients honestly and, later, judge your own investments. Interest rates and bank rules change: rates here are illustrations; get current ones from banks. Rules are {RULE}.
""",
    outcomes=[
        'Estimate loan eligibility, down payment and EMI.',
        'Calculate the full cost of buying and owning.',
        'Calculate yields, cash-on-cash and IRR.',
        'Explain leverage and the honest risks of property investing.',
    ],
    lessons=LESSONS,
    project='an affordability and return pack: one buyer and 5 properties',
    project_steps=[
        'Work out eligibility, down payment and own money needed for one buyer (sample or real with permission).',
        'Complete the Cost tab for one purchase with current official rates.',
        'Complete the ROI tab for 5 real properties.',
        'Write one page comparing the results with a fixed deposit and an index fund (from the Personal Finance course).',
    ],
    project_proof='The Loan, Cost and ROI tabs and the one-page comparison.',
    rubric=[
        ('Loans', 'No calculation', 'EMI only', 'Eligibility, LTV, down payment and own money'),
        ('Costs', 'Price only', 'Some costs', 'All buying and owning costs with dated rates'),
        ('Returns', 'Gross yield only', 'Net yield', 'Net yield, cash-on-cash and IRR for 5 properties'),
        ('Honesty', 'Promises returns', 'Mentions risk', 'Compares with alternatives and states risks plainly'),
    ],
    short=[
        'Calculate one EMI and one gross yield.',
        'Fill in the Cost tab for one purchase.',
    ],
    flashcards=[
        ('LTV up to ₹30 lakh', '90% (RBI).'),
        ('EMI formula', '=-PMT(rate/12, years*12, loan).'),
        ('LAP', 'Loan against property you own; risk of losing it.'),
        ('Gross yield', 'Annual rent ÷ price.'),
        ('Net yield / cap rate', 'NOI ÷ price.'),
        ('Cash-on-cash', 'Cash flow after EMI ÷ own cash.'),
        ('IRR', 'Yearly return including all cash flows and the sale.'),
        ('Kerala buying costs', 'About 10% to 12% of price.'),
    ],
    mistakes=[
        ('Ignoring interest costs.', 'Total interest can exceed the loan.'),
        ('Recommending investments.', 'Teach clients to evaluate; don\'t recommend.'),
        ('Using old rates.', 'Date-stamp rates and check banks.'),
    ],
    tools=[
        'EMI formulas and loan eligibility calculator (RE-M08-L01).',
        'Full cost of a purchase (RE-M08-L02).',
        'Rental yield and return calculator (RE-M08-L02).',
    ],
    toolkit=[
        'Loan tab (eligibility and EMI).',
        'Cost tab (full purchase cost).',
        'ROI tab with 5 properties.',
    ],
)
