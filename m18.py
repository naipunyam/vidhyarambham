from common import lesson, module, link, rules, xref, table, fence, Q, RULE, ASOF, CHECK

NOREC = 'This module teaches you **how to evaluate** strategies. It makes **no recommendation** to buy any property, REIT or product, and it is not investment advice. Numbers are illustrations.'

STRATS = [
    ('Buy-and-hold rental', 'Buy a house, flat or shop, let it, hold for years', 'Large (₹20 lakh+ plus costs)', 'Low yields (often 2% to 4% gross locally), vacancies, repairs, tenant problems, illiquidity'),
    ('Land banking', 'Buy land and hold for price growth, no income', 'Large', 'No income, holding costs, illiquidity, title and encroachment risk, land-type or ESA changes'),
    ('Flipping', 'Buy below value, improve or wait briefly, sell', 'Large plus repair money', 'Buying and selling costs (10%+), short-term gains taxed at slab rates, may not sell quickly'),
    ('REITs', 'Buy listed units of trusts that own rent-earning commercial property', 'Small (one unit)', 'Market price swings; distributions vary; mostly office and mall property outside Kerala'),
    ('Service businesses (this course)', 'Earn fees from brokerage, rentals and property care', 'Very small', 'Income depends on your work; reputation risk'),
]

L1 = lesson(
    18, 1,
    outcome='You can compare buy-and-hold, land banking and flipping on capital, returns, liquidity and risk, and evaluate a deal with honest numbers.',
    split='20 minutes reading, 40 minutes on deal analysis',
    core=f"""
{NOREC}

{table(['Strategy', 'How it works', 'Capital', 'Main risks'], STRATS)}

**Buy-and-hold rental.** Return = rent (after costs) + price growth − interest and costs. As RE-M08-L02 showed, local residential yields are often below loan interest rates, so a loan-funded rental can have **negative cash flow**: the owner pays from salary and hopes prices rise. It can work for people with stable income who buy carefully and hold for many years, but it is not "passive income".

**Land banking.** Buying land and waiting. Popular in Kerala because land feels safe. Reality: no income; land tax and upkeep; money locked for years; encroachment risk if you live away; rules can change (ESA drafts, data bank status, road plans). Selling can take months or years, especially interior plots. Price growth varies widely by location; there is no reliable public index for small Kerala towns.

**Flipping.** Buying below market (distress sales, family partitions, old houses), sometimes improving, and selling within a year or two. Needs: a deep local market knowledge, cash, renovation skill and fast selling. Buying and selling costs often take 12% to 15% (RE-M02-L02), and short-term gains are taxed at slab rates (RE-M09-L01).

**Liquidity, legal and market risks (all strategies):**
- **Illiquidity:** you can't sell a plot in a day; in a weak market, you may wait years or sell at a loss.
- **Legal:** title defects, heirs' claims, boundary disputes and land-type issues can freeze property for years.
- **Market:** prices can stagnate for long periods (for example after demand from Gulf remittances weakens or interest rates rise).
- **Concentration:** one property can be most of a family's wealth.

**How often do small investors lose money?** There is no reliable public data on returns for small Kerala property investors, so this course does not give a figure. What we do know from the calculations in this course: high buying costs, low yields and long holding periods mean that many purchases earn **less than a fixed deposit** after costs, interest and tax, even when the price rises. Run the numbers on every deal.

**Before any investment:** emergency fund and no high-interest debt ({xref('fin', 'fin-m05', 'Personal Finance: emergency fund')}); money you won't need for 7 to 10 years; an advocate's title opinion; a full analysis with a downside case; and diversification ({xref('fin', 'fin-m08-l03', 'asset allocation')}).
""",
    example="""
**Evaluating a "bargain" (fictional):** an old house on 10 cents in Kakkattil, offered at ₹28 lakh because the heirs want a quick sale. Comparables suggest ₹34 to ₹36 lakh after ₹3 lakh of repairs.
- Buy ₹28 lakh + costs ₹3 lakh + repairs ₹3 lakh + holding (1 year, lost FD interest at 7% on ₹34 lakh) ₹2.4 lakh = **₹36.4 lakh**.
- Sell at ₹35 lakh − 2% brokerage = ₹34.3 lakh → **loss of ₹2.1 lakh**. At ₹36 lakh: ₹35.28 lakh − 36.4 = **loss of ₹1.1 lakh**. Even at the top of the range it loses money after costs, before tax.
- Plus risks: all heirs must sign; the house may need more repairs.
The "bargain" is not one. The right move might be to help the heirs sell it to a buyer who wants to live there (earning commission).
""",
    calc="""
- Flip result: `=sale*(1-brokerage) - (buy + buy_costs + repairs + holding)`
- Break-even sale price: `=(buy + buy_costs + repairs + holding)/(1-brokerage)`
- Land bank IRR: year 0 `= -(price+costs)`, years 1..n `= -land_tax`, final year add `sale*(1-brokerage)`; `=IRR(range)`.
""",
    resources=[
        ('mit-re', 'Optional: lecture notes on investment analysis and risk', '20 minutes'),
        ('lt-fin', 'Chapters on risk and return', '20 minutes'),
    ],
    steps=[
        'Pick 3 real properties from your Comps sheet: one rental, one plot and one possible flip.',
        'Analyse each with the right strategy: yield and cash flow; land-bank IRR over 5 years; flip result and break-even.',
        'For each, write the main liquidity, legal and market risks.',
        'Compare each result with a fixed deposit at a current rate you looked up (with the date).',
    ],
    proof='Three analyses with risks and the FD comparison.',
    templates=[('Strategy comparison sheet', """STRATEGY COMPARISON (tab "Strategy")   date ______ ; FD rate used ___% (bank ______)
Property | Strategy | Own cash | Expected return (IRR or yield) | Downside case | Liquidity (months to sell) | Legal risk | Market risk | Better than FD after costs? Y/N
Downside case: price growth 0% and one extra vacant month a year
Decision rule I follow: no deal without an advocate's opinion, a downside case and money I can lock for 7-10 years""")],
    mistakes=[
        ('Believing land always goes up.', 'Prices can stagnate; costs and time reduce returns.'),
        ('Calling rentals passive income.', 'They need management and often have negative cash flow with loans.'),
        ('Skipping the downside case.', 'Always test 0% growth.'),
    ],
    fraud="""
**Investment schemes with property "backing".** Schemes promising monthly returns from "land development" or "rubber plantations" have cost many Kerala families their savings. If returns are guaranteed and high, walk away and check with SEBI and RBI lists before anyone invests.
""",
    quiz=[
        Q('What is the main drawback of land banking?', 'No income and money locked for years, with legal and market risks', 'It always loses money', 'It is illegal', 'It needs no due diligence', why='Illiquidity and holding costs.'),
        Q('Why can a loan-funded rental have negative cash flow?', 'Local yields are often below loan interest rates', 'Rents are always zero', 'Banks pay the owner', 'EMIs are tiny', why='Run the numbers.'),
        Q('What is a downside case?', 'A test with poor outcomes, such as 0% price growth', 'The best case', 'The broker\'s promise', 'A legal document', why='Shows what could go wrong.'),
        Q('Does this course give a statistic for how often small investors lose money?', 'No; there is no reliable public data, so it teaches you to run the numbers', 'Yes, 90%', 'Yes, 10%', 'Yes, 50%', why='Never invent statistics.'),
    ],
    study='read the lesson and the strategy table',
    action='analyse three real properties with the right strategy and compare with a fixed deposit',
)

L2 = lesson(
    18, 2,
    outcome='You can explain REITs and other low-capital ways to get property exposure, how to evaluate them and their real risks.',
    split='20 minutes reading, 35 minutes on research',
    core=f"""
{NOREC}

**REITs (real estate investment trusts).** A REIT owns rent-earning property (mostly offices, malls and warehouses in India's big cities), is listed on the stock exchanges and distributes most of its income to unitholders. SEBI cut the minimum application to **₹10,000 to ₹15,000** and the trading lot to **one unit** in 2021 ({link('week-reit', 'The Week')}; {CHECK}). You need a demat and trading account ({xref('fin', 'fin-m09-l05', 'Personal Finance: stocks and demat basics')}).

**How to evaluate a REIT** (from its public filings and the exchange website):
- What it owns: type, cities, occupancy, tenants, lease lengths.
- Distribution yield: distributions in the last year ÷ unit price. Check how much is interest, dividend or repayment of capital (taxed differently; ask a CA).
- Debt: how much the REIT has borrowed.
- Price vs net asset value (NAV).
- Fees and the sponsor's track record.
Units trade daily, so prices go up and down like shares. Distributions are not guaranteed.

**Comparing with buying property:**
| | Buying a rental house | REIT units |
| --- | --- | --- |
| Capital | ₹20 lakh+ plus costs | ₹10,000 to ₹15,000 |
| Buying cost | 10%+ | Brokerage and taxes, small |
| Liquidity | Months to years | Daily on the exchange |
| Management | You or a manager | Professional managers |
| Control | Full | None |
| Risk | Concentrated in one property | Spread over many buildings, but price swings daily |

**Other low-capital options:**
- **Real estate services** (this course): the lowest-capital way to earn from property.
- **Real estate company shares or funds:** more volatile; outside this course.
- **Fractional ownership platforms:** investors buy small shares of a property; some are regulated under SEBI's newer small and medium REIT rules and some are not (unverified in this course which platforms are regulated); check registration with SEBI before investing.
- **Co-buying land with friends or family:** high risk of disputes; only with a registered, advocate-drafted agreement.

For the place of real estate in a portfolio, see the {xref('fin', 'fin-m09-l06', 'Personal Finance lesson on gold, REITs and real estate')}.
""",
    example="""
**Evaluating a REIT (fictional numbers):** unit price ₹350; last year's distributions ₹22 per unit; distribution yield = 22 ÷ 350 = **6.3%**. Occupancy 88%; offices in Bengaluru and Mumbai; debt about 30% of asset value.
Compare with the Kakkattil rental house (RE-M08-L02): gross yield 3.6%, net 2.6%, ₹40 lakh needed, months to sell.
Neither is "better" in general: the REIT is liquid and diversified but its price can fall; the house gives control and is a home, but is concentrated and illiquid. Sachin's notes for a client: "Decide by your goal, time horizon and need for cash; talk to a SEBI-registered adviser for personal advice."
""",
    rules_rows=[
        ('REIT minimum application', '₹10,000 to ₹15,000; trading lot one unit (SEBI, 2021)', 'The Week'),
    ],
    pro="""
- **SEBI-registered investment adviser:** personal investment advice.
- **CA:** tax on REIT distributions and gains.
""",
    resources=[
        ('week-reit', 'Read about the SEBI changes for REITs', '10 minutes'),
        ('lt-fin', 'Read the chapter on risk and return', '20 minutes'),
    ],
    steps=[
        'Find the list of listed REITs on a stock exchange website and pick one to study (not to buy).',
        'From its latest public report, note what it owns, occupancy, distributions, debt and fees.',
        'Calculate its distribution yield at today\'s price (date it).',
        'Fill in the comparison table with one real local rental from your ROI tab.',
    ],
    proof='Your REIT study notes with sources and dates, the yield calculation and the comparison table.',
    templates=[('REIT evaluation sheet', """REIT EVALUATION (study only; not a recommendation)   date ______
Name ______  Source (exchange / annual report) ______
Assets: type ______ cities ______ occupancy ___%  top tenants ______  average lease left ___ years
Unit price ₹ ___   Distributions last 12 months ₹ ___   Distribution yield =dist/price ___%
Split: interest ___ dividend ___ capital repayment ___ (ask a CA about tax)
Debt to asset value ___%   Price vs NAV ______   Fees ______
Risks: price swings | vacancy | interest rates | sponsor | concentration in a few cities
Compared with my local rental (ROI tab): yield ___ vs ___ ; liquidity ___ vs ___""")],
    mistakes=[
        ('Treating REIT distributions as fixed.', 'They vary; prices swing.'),
        ('Buying through unregulated platforms.', 'Check SEBI registration.'),
        ('Recommending products to clients.', 'Teach evaluation; refer to a SEBI-registered adviser.'),
    ],
    fraud="""
**Unregistered "property funds".** Chit-style or WhatsApp "land funds" promising fixed monthly returns are common scams. Check SEBI and RBI registration, ask for audited accounts, and walk away from guaranteed returns.
""",
    quiz=[
        Q('What is the minimum REIT application after SEBI\'s 2021 change?', '₹10,000 to ₹15,000', '₹10 lakh', '₹100', '₹1 crore', why='Trading lot one unit.'),
        Q('Distribution yield equals:', 'Distributions in the last year ÷ unit price', 'Price ÷ distributions', 'NAV × 12', 'Rent ÷ EMI', why='Date it; prices change.'),
        Q('What is a key advantage of REITs over buying a house?', 'Liquidity and low entry capital', 'Guaranteed returns', 'No price changes', 'Full control', why='Prices still swing.'),
        Q('Who gives personal investment advice?', 'A SEBI-registered investment adviser', 'A broker on WhatsApp', 'Anyone', 'The REIT\'s sales agent', why='Regulated advice.'),
    ],
    study='read the lesson and the comparison table',
    action='study one listed REIT from its public report and compare it with a local rental',
)

LESSONS = [L1, L2]

MODULE = module(
    18,
    overview=f"""
Investing strategies: buy-and-hold rentals, land banking, flipping, REITs and other low-capital options, with honest analysis of liquidity, legal and market risks.

This is a **later stage**. The course makes no investment recommendations; it teaches you to evaluate. Your first real estate income should come from services, not from buying property. Everything is {RULE}.
""",
    outcomes=[
        'Compare strategies on capital, return, liquidity and risk.',
        'Analyse a deal with a downside case.',
        'Evaluate a REIT from public information.',
        'Explain honestly why many small investments disappoint.',
    ],
    lessons=LESSONS,
    project='an investment evaluation pack (study only)',
    project_steps=[
        'Three property analyses (rental, plot, flip) with downside cases.',
        'One REIT evaluation.',
        'A one-page personal investing rule set: when you would and wouldn\'t invest.',
    ],
    project_proof='The analyses, the REIT sheet and your rule set.',
    rubric=[
        ('Analysis', 'Price only', 'Some costs', 'Full costs, IRR or yield, downside case'),
        ('Risk', 'Ignored', 'Listed', 'Liquidity, legal and market risks for each'),
        ('REIT', 'Not studied', 'Basic facts', 'Assets, yield, debt and risks from public sources'),
        ('Honesty', 'Hype', 'Some caution', 'Clear rules and FD comparison'),
    ],
    short=[
        'Analyse one flip with the formula.',
        'Calculate one REIT distribution yield.',
    ],
    flashcards=[
        ('Land banking', 'Hold land for growth; no income; illiquid.'),
        ('Flip break-even', '(buy + costs + repairs + holding) ÷ (1 − brokerage).'),
        ('Downside case', '0% growth, extra vacancy.'),
        ('REIT minimum', '₹10,000 to ₹15,000; one unit.'),
        ('Distribution yield', 'Distributions ÷ price.'),
        ('Personal advice', 'SEBI-registered adviser.'),
    ],
    mistakes=[
        ('Investing before your service income is steady.', 'Services first.'),
        ('Borrowing to invest in land.', 'High risk; usually avoid.'),
        ('Recommending specific investments.', 'Teach evaluation.'),
    ],
    tools=[
        'Strategy comparison sheet (RE-M18-L01).',
        'REIT evaluation sheet (RE-M18-L02).',
    ],
    toolkit=[
        'Strategy comparison sheet.',
        'REIT evaluation sheet.',
    ],
)
