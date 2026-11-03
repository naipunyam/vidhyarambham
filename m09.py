"""Module 9: Investment options in India."""
from common import lesson, module, link, fence, table, inr, ASOF, CHECK

M = 9


def fv_sip(m, r, years):
    i = r / 12
    n = years * 12
    return m * ((1 + i) ** n - 1) / i * (1 + i)


LOW_COST = fv_sip(5000, 0.097, 20)
HIGH_COST = fv_sip(5000, 0.087, 20)


def npv(r, cfs):
    return sum(c / (1 + r) ** t for t, c in enumerate(cfs))


def irr(cfs, lo=-0.5, hi=0.5):
    flo = npv(lo, cfs)
    for _ in range(300):
        mid = (lo + hi) / 2
        fm = npv(mid, cfs)
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return mid


CH_N, CH_INST = 50, 4250
_early = [-CH_INST] * CH_N
_early[1] += 175000
_late = [-CH_INST] * CH_N
_late[49] += 237500
CH_EARLY = ((1 + irr(_early)) ** 12 - 1) * 100
CH_LATE = ((1 + irr(_late)) ** 12 - 1) * 100

L1 = lesson(
    M, 1,
    title='Mutual funds and SIPs: how they work',
    weeks=(16, 16), hours=2,
    outcome='Explain how a mutual fund works, the difference between direct and regular plans, what the expense ratio costs you over 20 years, and how SIPs, KYC and statements work.',
    split='30 minutes reading, 30 minutes resources, 60 minutes action',
    core=f"""
### What a mutual fund is

A **mutual fund** pools money from many investors and invests it in shares, bonds or other assets, managed by an **asset management company (AMC)** and regulated by SEBI. You buy **units**; the price of one unit is the **NAV** (net asset value), worked out every business day after expenses. If the fund's holdings rise, the NAV rises.

Main families of funds:

- **Equity funds:** mostly shares. Higher long-term potential, big ups and downs.
- **Debt funds:** bonds and money-market instruments. Lower ups and downs, with interest-rate and credit risk (FIN-M09-L03).
- **Hybrid funds:** a mix.
- **Index funds and ETFs:** copy a market index instead of picking stocks (FIN-M09-L02).
- **ELSS (tax-saver) funds:** equity funds with a **three-year lock-in**, counted per instalment for SIPs ({link('elss-lockin', 'Edelweiss Mutual Fund')}); their tax deduction (section 123, the old 80C) is available only under the old tax regime.

### Direct and regular plans

Every scheme comes in two plans with **the same portfolio and the same fund manager** ({link('amfi-direct', 'AMFI')}):

- **Regular plan:** bought through a distributor (an agent, a bank, some apps), who is paid a commission from your money every year.
- **Direct plan:** bought straight from the fund house, without commission, so its **expense ratio is lower and its NAV higher**. You can invest directly through the fund house's website or office, the exchange platforms, MF Utility or the registrar's offices. Banks act as distributors, so bank portals don't sell direct plans.

AMFI says direct plans suit people who can choose funds themselves; if you want advice, a fee-only SEBI-registered investment adviser (FIN-M09-L02) is the alternative to commission-based selling.

### The expense ratio: the fee you never see

The **total expense ratio (TER)** is the yearly cost of running the fund, as a percentage of your money: management, registrar, custody, audit, marketing and other costs. It is taken out every day before the NAV is published, so you never see a bill. Funds must publish their TER daily on their websites and AMFI's website ({link('amfi-ter', 'AMFI')}). SEBI announced in December 2025 a new **base expense ratio** framework from 1 April, with caps for open-ended equity schemes falling from 2.10% for the smallest funds to 0.95% for the largest, and statutory levies such as STT shown separately ({link('bs-ber', 'Business Standard')}, {CHECK}).

**Worked example:** ₹5,000 a month for 20 years. If the fund's investments earn 10% a year before costs, a 0.3% expense ratio leaves 9.7% and a 1.3% expense ratio leaves 8.7%. The results: about **{inr(LOW_COST)}** versus **{inr(HIGH_COST)}**. One percentage point of cost takes away about **{inr(LOW_COST - HIGH_COST)}**, from {inr(5000 * 240)} invested.

### SIPs

A **systematic investment plan** invests a fixed amount on a fixed date each month. It builds the habit, removes the temptation to "time the market", and buys more units when prices are low and fewer when they are high. It doesn't guarantee profit; in a falling market, a SIP also falls.

### KYC, statements and safety

- **KYC** is done once with PAN and Aadhaar-based verification or documents.
- **CAS:** a consolidated account statement lists every fund you hold, by PAN, each month you transact; you can request one from the registrars or MFCentral ({link('amfi-cas', 'AMFI')}). It also shows nomination and KYC status.
- **Nominees:** for demat accounts and fund folios, up to three nominees under SEBI's circular of 29 May 2026, effective 1 September 2026 (Module 13).
- **Paying safely:** SEBI-registered intermediaries now collect money through **"@valid" UPI handles** (fund houses use ".mf"), and you can verify a UPI ID or bank account with **SEBI Check** before paying ({link('sebi-valid', 'Moneylife')}).
- Past returns don't guarantee future returns, and no mutual fund guarantees returns.
""",
    example=f"""
**Fathima's** bank relationship manager suggested "a top-rated fund" for ₹3,000 a month. She looked it up on the fund house's website and found two NAVs for the same scheme: the regular plan and the direct plan. The factsheet showed a TER of 1.62% for regular and 0.58% for direct (made-up numbers for this example).

She asked the manager why he hadn't mentioned the direct plan. He said, honestly, that the bank sells regular plans and is paid by the fund house. Fathima thanked him and decided that she would choose funds herself using FIN-M09-L02, and invest only after writing her Investment Policy Statement (Module 17). "The same fund, the same manager, a 1% difference every year for 20 years," she wrote. "That's my money, not a detail."
""",
    resources=[
        ('amfi-direct', 'Direct and regular plans: what is the same, what differs, and how to invest directly', '10 minutes'),
        ('amfi-ter', 'What the expense ratio covers and where it is disclosed', '10 minutes'),
        ('varsity', 'Module 11, "Personal Finance: Mutual Funds": the first chapters on how funds work', '30 minutes'),
        ('amfi-cas', 'How the consolidated account statement works', '5 minutes'),
        ('sebi-valid', 'The @valid UPI handles and SEBI Check', '5 minutes'),
    ],
    steps=[
        'Pick any one well-known equity index fund (as a learning example, not a recommendation). On its fund house\'s website, find the direct and regular plans and write down both NAVs and both TERs.',
        'Put the two TERs into the expense calculator template with your own SIP amount and 20 years, and write the difference in rupees.',
        'If you already hold mutual funds, request your CAS and check which plan (direct or regular) each holding is, and its nomination status.',
        'Write down how you would pay safely: through the fund house\'s official site or app, and checking the @valid UPI handle.',
        'Write three sentences explaining a mutual fund, a SIP and the expense ratio to a family member.',
    ],
    proof='Your direct-vs-regular comparison (NAVs, TERs and the rupee difference over 20 years) and, if you have funds, your CAS check, saved in 09 Investing.',
    templates=[
        ('expense ratio calculator', """
B2: monthly SIP (₹)                      5000
B3: years                                20
B4: return before costs (e.g. 0.10)      0.10
B5: expense ratio, plan A (e.g. 0.003)   0.003
B6: expense ratio, plan B (e.g. 0.013)   0.013
B7: value with plan A  =FV((B4-B5)/12,B3*12,-B2,0,1)
B8: value with plan B  =FV((B4-B6)/12,B3*12,-B2,0,1)
B9: cost of the difference  =B7-B8
""", ''),
    ],
    mistakes=[
        ('Buying a regular plan without knowing it.', 'Check the plan name on your statement; "Direct" appears in direct plans.'),
        ('Judging a fund by last year\'s return.', 'One good year says little. FIN-M09-L02 shows what to compare.'),
        ('Ignoring the expense ratio.', 'It is taken every day, every year. Small percentages become lakhs over decades.'),
        ('Paying to unknown UPI IDs or accounts.', 'Use official channels and check @valid handles or SEBI Check.'),
    ],
    quiz=[
        {'q': 'What is the difference between direct and regular plans of the same scheme?', 'o': ['Same portfolio and manager; direct has no distributor commission, so a lower expense ratio', 'Different portfolios', 'Direct plans are riskier', 'Regular plans are guaranteed'], 'a': 'A', 'why': 'Only the cost (and so the NAV) differs.'},
        {'q': 'How is the expense ratio charged?', 'o': ['Deducted daily before the NAV is published', 'As a yearly bill', 'Only when you sell', 'It is never charged'], 'a': 'A', 'why': 'You don\'t see it; it reduces the NAV every day.'},
        {'q': 'What is the lock-in of an ELSS fund, for a SIP?', 'o': ['Three years for each instalment', 'Three years from the first instalment only', 'Five years', 'No lock-in'], 'a': 'A', 'why': 'Each unit is locked for three years from its allotment.'},
        {'q': 'Where can you see all your mutual funds in one statement?', 'o': ['A consolidated account statement (CAS)', 'Your bank passbook', 'Your credit report', 'Form 16'], 'a': 'A', 'why': 'The CAS lists all your holdings by PAN.'},
    ],
    study='AMFI on direct plans and expense ratios, Varsity\'s mutual fund basics, the CAS and safe payments',
    action='Compare a fund\'s direct and regular plans and calculate the 20-year cost of the difference',
)

L2 = lesson(
    M, 2,
    title='Index funds, comparing funds with official data, and when to pay an adviser',
    weeks=(16, 16), hours=2.5,
    outcome='Compare mutual funds using official data (category, plan, expense ratio, riskometer, returns against the benchmark) in a fund-comparison sheet, and know when and how to use a SEBI-registered investment adviser.',
    split='30 minutes reading, 40 minutes resources, 80 minutes action',
    core=f"""
### Active and passive funds

- An **active fund** has a manager who picks stocks to try to beat a benchmark index. Higher costs; some years it beats the index, many years it doesn't.
- An **index fund** (or index ETF) simply holds the shares in an index, such as the Nifty 50 or the Sensex, in the same proportions. Low costs, no manager skill needed, and you get the market's return minus a small cost. The gap between the fund's return and its index is the **tracking difference**; lower is better.

Many beginners start long-term equity investing with a broad index fund because it is cheap, diversified and easy to understand. This course doesn't tell you which fund to buy; it shows you how to compare.

### What to compare, and where to find it

Use **official sources**: the fund's **factsheet**, the **scheme information document** and the **Key Information Memorandum** on the fund house's website, and AMFI's website for expense ratios.

{table(['What', 'Why it matters', 'Where'], [
    ('Category', 'Compare like with like: a large-cap fund with large-cap funds', 'Factsheet, scheme documents'),
    ('Plan', 'Direct plans cost less', 'Scheme name'),
    ('Expense ratio (TER)', 'The cost you pay every year', 'Fund website, AMFI website'),
    ('Riskometer', 'SEBI\'s six-level risk scale', 'Factsheet'),
    ('Benchmark', 'The index the fund should be judged against', 'Factsheet'),
    ('Returns vs benchmark over 3, 5 and 10 years', 'Consistency matters more than one great year', 'Factsheet'),
    ('Tracking difference (index funds)', 'How closely it follows the index after costs', 'Factsheet or fund website'),
    ('Fund size (AUM) and age', 'Very small or very new funds have less history', 'Factsheet'),
    ('Exit load', 'A charge for selling early', 'Scheme documents'),
    ('Portfolio', 'What it actually owns; overlap with your other funds', 'Factsheet, monthly portfolio'),
])}

**What not to use as the main guide:** star ratings, "top fund" lists, social media posts, and last year's return.

### When to pay for advice

You can manage simple investments yourself with this course. Consider a **SEBI-registered investment adviser (RIA)** when the sums are large, your situation is complex (business income, a big inheritance, NRI status, retirement), or you want a second opinion on your plan.

- **RIAs charge a fee** and must not earn commissions from products they recommend. SEBI caps their fees: a fixed fee of up to about ₹1.51 lakh per family per year, or up to 2.5% a year of the assets they advise on ({link('ria-fees', 'Cafemutual, January 2025')}, {CHECK}).
- **Verify registration** on SEBI's website before paying anyone: search the {link('sebi-ia-list', 'list of registered investment advisers')} by name or registration number, and match the details. SEBI has long asked people to deal only with registered advisers and research analysts and to beware of tips by SMS and social media ({link('sebi-ia-caution', 'SEBI')}).
- **Finfluencers:** since 2024, SEBI-regulated entities can't have any association with unregistered people who give advice or make return claims ({link('bt-finfluencer', 'Business Today, August 2024')}). A YouTuber or Telegram channel recommending specific funds or stocks for money must be registered; most aren't.
- A distributor (an agent paid by commission) can sell you products but is not an adviser; ask how they are paid.
- **Learn more, free:** SEBI's **Saa₹thi** app (launched in January 2022) is its mobile app for investor education ({link('saarthi', 'SEBI press release')}); NSE runs free investor awareness programmes and publishes study material ({link('nse-iap', 'NSE')}).
""",
    example=f"""
**Anu** practised comparing three index funds that track the same index (names hidden here; she used real ones from fund house websites, as a learning exercise):

{table(['', 'Fund 1 (direct)', 'Fund 2 (direct)', 'Fund 3 (direct)'], [
    ('Category', 'Index fund', 'Index fund', 'Index fund'),
    ('Benchmark', 'Same index', 'Same index', 'Same index'),
    ('Expense ratio', '0.20%', '0.45%', '0.18%'),
    ('Riskometer', 'Very High', 'Very High', 'Very High'),
    ('Tracking difference, 1 year', '−0.25%', '−0.60%', '−0.40%'),
    ('Fund age', '8 years', '3 years', '1 year'),
    ('Exit load', 'None', 'None', 'None'),
])}

(The numbers are made up for the example.) Fund 3 was cheapest, but too new to judge its tracking. Fund 2 cost more and tracked worse. Fund 1 had a long, close-tracking record. She noted that all three were "Very High" on the riskometer, like all equity funds, which is why only her long-term money (FIN-M08-L03) would go into equity. She didn't buy yet; the comparison goes into her Investment Policy Statement in Module 17.
""",
    resources=[
        ('sebi-risko', 'How to read the riskometer in a factsheet', '5 minutes'),
        ('amfi-ter', 'Where expense ratios are published', '5 minutes'),
        ('ria-fees', 'SEBI\'s fee limits for registered investment advisers', '5 minutes'),
        ('sebi-ia-list', 'Search the list of registered investment advisers; try searching one name you have seen online', '10 minutes'),
        ('bt-finfluencer', 'SEBI\'s rules on finfluencers', '10 minutes'),
        ('varsity', 'Module 11, "Personal Finance: Mutual Funds": the chapters on index funds and choosing funds', '40 minutes'),
    ],
    steps=[
        'Make a **Funds** tab with the template.',
        'Choose a category that fits your long-term allocation (for example, a broad equity index fund) and find three funds in it.',
        'Fill in every column from official documents only: factsheets, scheme documents and the fund websites. Note the date of each factsheet.',
        'Use the formulas to compare returns with the benchmark.',
        'Write which fund ranks best on your criteria and why, without buying.',
        'Search SEBI\'s adviser list for any adviser, finfluencer or "guru" whose advice you have followed or considered. Write whether they are registered.',
    ],
    proof='A screenshot of your Funds tab with three funds compared from official data (with factsheet dates) and your SEBI registration check, saved in 09 Investing.',
    templates=[
        ('Funds tab', """
Row 1: Fund name,Plan (Direct/Regular),Category,Benchmark,Expense ratio %,Riskometer,AUM (₹ crore),Fund age (years),Exit load,3-yr return %,3-yr benchmark %,Difference,5-yr return %,5-yr benchmark %,Difference,Factsheet date,Notes
L2: =J2-K2      O2: =M2-N2
Cheapest: =INDEX(A2:A10,MATCH(MIN(E2:E10),E2:E10,0))
Average expense ratio: =AVERAGE(E2:E10)
""", ''),
        ('adviser check', """
Name and firm: ____
SEBI registration number (from them): ____
Found on SEBI's list? Yes / No   Details match (name, address)? Yes / No
How are they paid? Fixed fee / % of assets / commission
Do they promise returns? (a red flag) Yes / No
""", ''),
    ],
    mistakes=[
        ('Choosing by star ratings or last year\'s return.', 'Compare category, cost, risk and long-term returns against the benchmark.'),
        ('Comparing funds from different categories.', 'A small-cap fund and a large-cap fund aren\'t competitors; compare within a category.'),
        ('Following unregistered tipsters.', 'Check SEBI\'s list. No registration, no advice.'),
        ('Owning many similar funds.', 'Several funds with the same holdings add complexity, not diversification.'),
    ],
    quiz=[
        {'q': 'What is the best way to judge an equity fund\'s returns?', 'o': ['Against its benchmark over 3, 5 and 10 years', 'Last year\'s return only', 'Its star rating', 'Its advertisements'], 'a': 'A', 'why': 'Consistency against the right benchmark matters most.'},
        {'q': 'How can you check that an investment adviser is genuine?', 'o': ['Search SEBI\'s list of registered investment advisers', 'Check their follower count', 'Ask in a WhatsApp group', 'Trust a certificate they send'], 'a': 'A', 'why': 'SEBI\'s list is the official record of registration.'},
        {'q': 'What is the fee cap for SEBI-registered investment advisers, as of November 2026?', 'o': ['About ₹1.51 lakh per family per year fixed, or 2.5% of assets advised', 'No limit', '10% of profits', '₹500 per tip'], 'a': 'A', 'why': 'SEBI set these limits in January 2025 (check current rules).'},
        {'q': 'Why do many beginners start with a broad index fund?', 'o': ['It is low-cost, diversified and simple to understand', 'It is guaranteed', 'It never falls', 'It has no risk'], 'a': 'A', 'why': 'It still carries market risk (Very High on the riskometer) but is cheap and diversified.'},
    ],
    study='The riskometer, expense ratio disclosure, RIA fees, SEBI\'s adviser list, finfluencer rules and Varsity\'s fund-choice chapters',
    action='Compare three funds in one category from official data in a Funds tab and check one adviser\'s registration',
)

L3 = lesson(
    M, 3,
    title='Safe options: small savings, deposits and debt funds',
    weeks=(17, 17), hours=2,
    outcome='Compare post office small savings schemes, bank deposits and debt mutual funds on rate, safety, lock-in and tax, and choose the right one for each short or medium goal.',
    split='25 minutes reading, 30 minutes resources, 65 minutes action',
    core=f"""
### Small savings schemes

These schemes are run by the Government of India through post offices and authorised banks; interest rates are set every quarter. Rates for **October to December 2026** (unchanged for the tenth quarter in a row) ({link('small-rates', 'Indian Bank table')}, {link('fpj-small', 'Free Press Journal')}, {CHECK}):

{table(['Scheme', 'Rate', 'Key features'], [
    ('Post office savings account', '4.0%', 'Basic account'),
    ('Recurring deposit (5 years)', '6.7%', 'From ₹100 a month'),
    ('Time deposit (1, 2, 3, 5 years)', '6.9%, 7.0%, 7.1%, 7.5%', 'The 5-year TD qualifies for the old-regime section 123 deduction'),
    ('Monthly Income Scheme (MIS)', '7.4%', 'Monthly interest; up to ₹9 lakh single, ₹15 lakh joint'),
    ('National Savings Certificate (NSC)', '7.7%', '5 years; interest paid at maturity'),
    ('Kisan Vikas Patra (KVP)', '7.5%', 'Money doubles in 115 months'),
    ('Public Provident Fund (PPF)', '7.1%', '15 years; tax-free interest (FIN-M09-L04)'),
    ('Sukanya Samriddhi (SSA)', '8.2%', 'For a girl child; ₹250 to ₹1.5 lakh a year'),
    ('Senior Citizens Savings Scheme (SCSS)', '8.2%', 'For 60+; up to ₹30 lakh; quarterly interest'),
])}

Limits are from {link('om-small', 'Outlook Money (January 2024)')} and {link('indiapost', 'India Post')}; check current limits before you invest. Interest on most of these is **taxable at your slab** (PPF and SSA are the main exceptions), and the government backing means very low credit risk.

### Bank FDs

Covered in FIN-M04-L03: rates vary by bank, ₹5 lakh deposit insurance per bank, taxed at your slab, penalties for breaking early.

### Debt mutual funds

Debt funds lend to governments and companies. Types include overnight and liquid funds (very short loans), short-duration funds, corporate bond funds and gilt funds (government bonds).

- **Interest-rate risk:** when interest rates rise, existing bonds lose value, so debt fund NAVs dip; longer-duration funds dip more.
- **Credit risk:** a borrower may fail to repay; funds that chase higher yields hold riskier borrowers.
- **Tax:** units of "specified mutual funds" (investing more than 65% in debt) bought on or after 1 April 2023 are taxed as **short-term gains at your slab rate, however long you hold them** (section 76 of the Income-tax Act, 2025) ({link('it-s76', 'section 76')}, {CHECK}). So their old tax advantage over FDs is gone; compare them on liquidity and post-tax return.

For most beginners, **post office schemes and insured bank deposits** cover short and medium goals simply. Debt funds become useful when amounts grow and you understand their risks.

### Choosing by goal

{table(['Goal', 'Good fits', 'Why'], [
    ('Emergency fund', 'Savings account + FD ladder (Module 5)', 'Access within a day'),
    ('Sinking funds (yearly costs)', 'RD matching the date', 'Monthly deposits, known maturity'),
    ('1–5 year goals', 'Post office TD, NSC, FDs, RDs', 'Safety and a known return'),
    ('Parents\' regular income', 'SCSS (60+), MIS, payout FDs', 'Regular interest, government backing'),
    ('Daughter\'s education', 'SSA, alongside other long-term options', 'High fixed rate, long term'),
])}

### Post-tax return

Compare what you keep: **post-tax return = rate × (1 − your tax slab)**. At 7.5% and a 20% slab, you keep 6%. For someone with no taxable income, the full 7.5%.
""",
    example=f"""
**Joseph and Mary** (both over 60) wanted monthly income from ₹10 lakh of savings. With their son, they compared, using the October to December 2026 rates:

{table(['Option', 'Rate', 'Yearly interest on the amount', 'Notes'], [
    ('SCSS, ₹8 lakh in Joseph\'s name', '8.2%', '₹65,600', 'Quarterly payout; within the ₹30 lakh limit'),
    ('Post office MIS, ₹2 lakh in Mary\'s name', '7.4%', '₹14,800', 'Monthly payout'),
    ('Total', '', '₹80,400 a year, about ₹6,700 a month', 'Both government-backed'),
])}

Their earlier plan, one big FD at a co-operative society, would have paid a little more but without deposit insurance (FIN-M04-L03). They kept ₹1 lakh in an FD ladder at their bank as an emergency fund, and noted that the SCSS rate is fixed for an account when opened, while rates for new accounts change every quarter.
""",
    resources=[
        ('indiapost', 'The current interest rates for every post office scheme', '10 minutes'),
        ('small-rates', 'The quarterly rates table for October to December 2026', '5 minutes'),
        ('om-small', 'Deposit limits and features of each scheme (January 2024)', '15 minutes'),
        ('it-s76', 'Section 76: why debt fund gains are now taxed at your slab', '10 minutes'),
        ('amfi-tax', 'AMFI\'s tax corner: how debt and other funds are taxed', '10 minutes'),
    ],
    steps=[
        'List your short and medium goals from the Goals tab (horizon under 7 years).',
        'For each, choose two possible options from this lesson and compare them in the template: rate, lock-in, safety, tax and post-tax return.',
        'Check the current quarter\'s rates on India Post\'s page, as rates may have changed since November 2026.',
        'Pick the option for each goal and add it to the "Where the money waits" column in your Goals tab.',
        'If you help parents or grandparents with money, check whether SCSS or MIS could fit their needs and write it down for a family conversation.',
    ],
    proof='Your safe-options comparison with post-tax returns and the updated "Where the money waits" column, saved in 09 Investing.',
    templates=[
        ('safe options comparison', """
Row 1: Goal,Option,Rate (e.g. 0.075),Lock-in or tenure,Safety (govt / insured bank / fund),Taxed at slab? (Yes/No),My slab (e.g. 0.05),Post-tax rate %,Decision
H2: =IF(F2="Yes",C2*(1-G2),C2)*100
""", ''),
    ],
    mistakes=[
        ('Ignoring tax on interest.', 'Compare post-tax returns, especially if your slab is 20% or 30%.'),
        ('Thinking debt funds are "like FDs".', 'Their NAV can fall when rates rise or a borrower defaults.'),
        ('Locking money in a long scheme for a short goal.', 'Match the lock-in to the goal date.'),
        ('Using old rates.', 'Small savings rates change quarterly for new deposits. Check before investing.'),
    ],
    quiz=[
        {'q': 'What was the PPF interest rate for October to December 2026?', 'o': ['7.1%', '8.2%', '4%', '12%'], 'a': 'A', 'why': 'PPF stayed at 7.1% (check current rates).'},
        {'q': 'How are gains on a debt mutual fund bought after 1 April 2023 taxed?', 'o': ['As short-term gains at your slab rate, however long you hold', 'Always tax-free', 'At 12.5% after 2 years', 'At a flat 1%'], 'a': 'A', 'why': 'Section 76 treats specified mutual fund gains as short-term.'},
        {'q': 'A deposit pays 7.5% and your slab is 20%. What is the post-tax return?', 'o': ['6%', '7.5%', '5.5%', '9%'], 'a': 'A', 'why': '7.5 × (1 − 0.2) = 6%.'},
        {'q': 'Which scheme is meant for people aged 60 and above?', 'o': ['Senior Citizens Savings Scheme (SCSS)', 'Sukanya Samriddhi', 'KVP', 'NSC'], 'a': 'A', 'why': 'SCSS paid 8.2% in October to December 2026, with quarterly interest.'},
    ],
    study='Current small savings rates and limits, section 76 and AMFI\'s tax corner',
    action='Choose a safe option for each short and medium goal by comparing post-tax returns',
)

L4 = lesson(
    M, 4,
    title='Retirement accounts: EPF, PPF and NPS',
    weeks=(17, 17), hours=2,
    outcome='Explain how EPF, PPF and NPS work, their withdrawal rules and tax treatment as of November 2026, and decide which fit your work situation.',
    split='30 minutes reading, 30 minutes resources, 60 minutes action',
    core=f"""
These three accounts are designed for the long term, with rules that make early withdrawal hard. That is a feature: they protect retirement money from today's wants.

### EPF (Employees' Provident Fund)

For employees of establishments covered by EPFO: you and your employer contribute every month from your salary.

- **Interest:** 8.25% for 2025-26, the third year in a row at that rate ({link('bt-epf', 'Business Today, July 2026')}).
- **Withdrawals (from October 2025):** 13 rules were merged into 3 categories: essential needs (illness, education, marriage), housing, and special circumstances. Members can withdraw **up to 100% of the eligible balance**, but **25% of contributions must stay** in the account; the minimum service is 12 months; education withdrawals are allowed up to 10 times and marriage up to 5. After leaving a job, **full withdrawal (premature final settlement) needs 12 months** without a job (earlier 2 months), and the pension part (EPS) **36 months** ({link('epf-withdraw', 'Onmanorama, October 2025')}, {CHECK}).
- **Voluntary PF (VPF):** you can contribute extra to EPF through your employer.
- **Change jobs, keep the account:** transfer your balance to the new employer instead of withdrawing; withdrawing early is the most common way people lose retirement savings.

### PPF (Public Provident Fund)

Open to anyone, at a post office or bank ({link('ppf-cbi', 'Central Bank of India')}, {CHECK}):

- **₹500 to ₹1.5 lakh a year**, one account per person; 7.1% for October to December 2026.
- **15 years**, extendable in 5-year blocks.
- **Partial withdrawal** once a year after 5 years (up to 50% of an earlier balance); **premature closure** after 5 years only for serious illness, higher education or a change to NRI status, with 1% less interest.
- **Interest is tax-free**, and deposits count for the section 123 deduction under the old regime.
- If you miss the ₹500 minimum in a year, the account is "discontinued" and can be revived with a small penalty.

### NPS (National Pension System)

Regulated by PFRDA, open to citizens aged 18 to 85 ({link('sbi-nps', 'SBI\'s NPS page')}, {CHECK}):

- **Tier I** (the pension account with tax benefits and withdrawal limits) and **Tier II** (optional, flexible, no tax benefit). ₹250 to open.
- You choose a pension fund manager and how much goes to equity, corporate bonds and government bonds (or an automatic mix by age), and can change them during the year.
- **Tax:** an extra ₹50,000 deduction under the old regime (the old "80CCD(1B)"), on top of the ₹1.5 lakh limit; **employer contributions** are deductible up to 10% of basic plus DA in the old regime and 14% in the new regime.
- **Exit rules for non-government subscribers (December 2025 changes):** at normal exit, up to **80% as a lump sum** and at least **20% in an annuity** (it was 60:40); if the corpus is ₹8 lakh or less, you can take it all ({link('bs-nps-exit', 'Business Standard')}, {CHECK}). Partial withdrawals are allowed for specific needs such as a house or medical treatment.
- **Tax on the lump sum:** only **60% is explicitly tax-free**; the record-keeper notes that the extra 20% is taxable at your slab unless the government clarifies otherwise ({link('protean-nps', 'Protean')}, {CHECK}).

Government employees have their own NPS rules (Module 14).

### Which fits you?

{table(['Situation', 'Typical fit'], [
    ('Salaried in a covered private job', 'EPF (automatic), perhaps VPF; NPS through the employer if offered'),
    ('Freelancer, business owner, PSC aspirant', 'PPF as a safe base; NPS for long-term growth with a lock-in'),
    ('Kerala government employee', 'NPS (contributory pension) and GPF rules from Module 14'),
    ('Low income, no tax', 'PPF for safety and flexibility; the Atal Pension Yojana (Module 12)'),
])}
""",
    example=f"""
**Fathima** has no employer, so no EPF. She had a PPF account opened by her father when she was 20, with irregular deposits; one year had no deposit, so the account was discontinued. She revived it at the post office with the small penalty and the missed ₹500.

She decided on two retirement accounts: **PPF**, with ₹2,000 a month by standing instruction, as the safe base (tax-free interest, government-backed); and **NPS Tier I** for growth, with ₹1,500 a month, once she finishes Module 12. She read the exit rules carefully: most of the NPS money is locked until 60, which she sees as protection from herself in good freelance years.

Her note: "EPF rules changed in 2025 and NPS rules in December 2025. I'll check both every year in my review."
""",
    resources=[
        ('ppf-cbi', 'PPF rules: limits, maturity, withdrawals, closure and revival', '15 minutes'),
        ('epf-withdraw', 'The October 2025 EPF withdrawal changes', '10 minutes'),
        ('bt-epf', 'EPF interest for 2025-26', '5 minutes'),
        ('sbi-nps', 'NPS: tiers, contributions, tax benefits and exit summary', '15 minutes'),
        ('bs-nps-exit', 'The December 2025 NPS exit and withdrawal changes', '10 minutes'),
        ('varsity', 'Module 17, "NPS: National Pension System": the first chapters', '25 minutes'),
    ],
    steps=[
        'Write down which of EPF, PPF and NPS you already have. For EPF, check your passbook through EPFO\'s online member services (or ask your employer); for PPF, your passbook; for NPS, your statement.',
        'For each account you have, check: nominee, last contribution, balance. Add them to your Net Worth and Allocation tabs (as debt, or split for NPS).',
        'For the accounts you don\'t have, write whether they fit you, using the table.',
        'Write one rule about your EPF if you have one, for example: "When I change jobs, I transfer my EPF; I never withdraw it for wants."',
        'Note the next check date for these rules in your yearly review.',
    ],
    proof='Your retirement accounts summary (accounts held, balances, nominees, fit for the others) and your EPF rule, saved in 09 Investing.',
    templates=[
        ('retirement accounts summary', """
Account,Have it? (Yes/No),Balance (₹),Monthly contribution (₹),Nominee updated?,Withdrawal rule I must remember,Fits me? Why
EPF,,,,,"12 months' service; 25% stays; final settlement after 12 months without a job",
VPF,,,,,,
PPF,,,,,"15 years; ₹500 minimum each year; partial after 5 years",
NPS Tier I,,,,,"Mostly locked to 60; up to 80% lump sum, 20%+ annuity (non-govt)",
NPS Tier II,,,,,"Flexible; no tax benefit",
""", 'csv'),
    ],
    mistakes=[
        ('Withdrawing EPF when changing jobs.', 'Transfer it. Early withdrawal destroys decades of compounding.'),
        ('Missing the ₹500 PPF minimum.', 'Set a standing instruction for at least ₹500 in April every year.'),
        ('Choosing NPS only for the tax deduction.', 'Choose it if the lock-in and rules fit your retirement plan; the deduction is old-regime only.'),
        ('Forgetting nominees on retirement accounts.', 'Check them now; Module 13 explains why.'),
    ],
    quiz=[
        {'q': 'What EPF interest rate was set for 2025-26?', 'o': ['8.25%', '7.1%', '12%', '4%'], 'a': 'A', 'why': 'It was 8.25%, the third year in a row.'},
        {'q': 'Under the October 2025 EPF rules, how long after leaving a job before full withdrawal?', 'o': ['12 months', '2 months', '5 years', 'Never'], 'a': 'A', 'why': 'Premature final settlement moved from 2 to 12 months.'},
        {'q': 'What is the PPF deposit range per year?', 'o': ['₹500 to ₹1.5 lakh', '₹100 to ₹50,000', 'No limit', '₹10,000 minimum'], 'a': 'A', 'why': 'One account per person, ₹500 minimum, ₹1.5 lakh maximum.'},
        {'q': 'After the December 2025 changes, how much can a non-government NPS subscriber take as a lump sum at normal exit?', 'o': ['Up to 80%', 'Up to 40%', 'Nothing', '100% always'], 'a': 'A', 'why': 'At least 20% goes to an annuity; full withdrawal only if the corpus is ₹8 lakh or less.'},
    ],
    study='PPF rules, EPF withdrawal changes and interest, NPS features and exit changes, and Varsity\'s NPS chapters',
    action='Summarise your EPF, PPF and NPS position, update nominees and balances, and write your EPF rule',
)

L5 = lesson(
    M, 5,
    title='Stocks and demat basics: ownership, costs and honest risks',
    weeks=(18, 18), hours=2,
    outcome='Explain what shares, demat and trading accounts are, what investing in single stocks costs and risks, and why most beginners lose money trading derivatives.',
    split='30 minutes reading, 40 minutes resources, 50 minutes action',
    core=f"""
### Shares and the market

A **share** is a small part of a company. When the company grows its profits over years, its share price tends to follow; when it struggles, the price falls, sometimes to nothing. Shares are bought and sold on stock exchanges (NSE and BSE) through a **SEBI-registered stockbroker**.

### The accounts you need

- **Demat account:** holds your shares and other securities electronically, with a depository participant. Your holdings appear in your consolidated account statement along with mutual funds ({link('amfi-cas', 'AMFI CAS')}).
- **Trading account:** with a broker, to place buy and sell orders.
- **Bank account** linked to both. Pay brokers only through official channels; registered brokers' UPI handles now use the "@valid" format with ".brk", and SEBI Check verifies them ({link('sebi-valid', 'Moneylife')}).

### Costs

Brokerage, securities transaction tax (STT), exchange and depository charges, stamp duty and GST on fees all reduce returns. Frequent trading multiplies them. Budget 2026 raised STT on futures from 0.02% to 0.05% and on options from 0.10% to 0.15% ({link('om-budget26', 'Outlook Money')}, {CHECK}).

### Tax, briefly

For listed shares (and equity funds): gains on shares held **12 months or less** are short-term and taxed at **20%**; longer holdings are long-term, taxed at **12.5% on gains above ₹1.25 lakh a year** (sections 196 and 198 of the Income-tax Act, 2025) ({link('it-s196', 'section 196')}, {link('it-s198', 'section 198')}, {CHECK}). Dividends are added to your income. Module 10 covers the details.

### Single stocks: honest risks

- **Concentration:** one company can collapse through fraud, debt or competition. A few stocks are not a diversified portfolio.
- **Time and skill:** picking stocks well needs reading annual reports and understanding businesses, for years. Professionals with full-time teams often fail to beat the index.
- **Emotions:** watching prices daily leads to panic selling and greed buying (Module 1).

### Derivatives (F&O): the numbers

Futures and options are short-term bets on price moves, with leverage. SEBI's study of 2024-25 found that **about 91% of individual F&O traders lost money**, with net losses of **₹1,05,603 crore** in the year, about **₹1.1 lakh per person on average** ({link('sebi-fno', 'Moneylife')}). Courses, Telegram groups and apps that promise daily income from "option trading" are selling you the 9% dream.

### Tips and "gurus"

Only SEBI-registered research analysts and investment advisers may recommend specific stocks for a fee ({link('sebi-ia-caution', 'SEBI')}). SEBI's investor site warns about fake trading apps, "stock market guru" scams, pump-and-dump schemes and illegal dabba trading ({link('sebi-investor', 'SEBI investor site')}). If a group shows screenshots of big profits and asks you to install an app or pay a fee, it is almost certainly a scam (Module 15).

### A sensible path

Many people start equity investing through **diversified index funds** (FIN-M09-L02), and treat direct stock investing, if at all, as a small, separate part of their long-term money that they research properly. Your Investment Policy Statement (Module 17) can set a limit, such as "single stocks: at most 10% of my equity".
""",
    example=f"""
**Rahul's** office colleague, Suresh, joined a Telegram group called "Daily 5% Nifty Options Profit". The group shared screenshots of huge gains and offered a "premium plan" for ₹9,999. Suresh paid, followed the tips, and lost ₹62,000 in five weeks, including money from a personal loan.

Rahul shared SEBI's F&O study with him and checked the group's "analyst" on SEBI's registered intermediaries list: not registered. Suresh stopped trading and reported the group on the SEBI investor site's channels and the cyber crime portal.

Rahul wrote two rules in his own plan: "No F&O trading, ever, until I can explain why 91% lose," and "Any single stock buy must be researched for at least a month and stay under 10% of my equity money."
""",
    resources=[
        ('varsity', 'Module 1, "Introduction to Stock Markets": the first five chapters', '40 minutes'),
        ('sebi-fno', 'SEBI\'s study of F&O losses in 2024-25', '10 minutes'),
        ('sebi-investor', 'The fraud warnings: fake trading apps, "stock market guru" scams, pump and dump, dabba trading', '15 minutes'),
        ('om-budget26', 'Budget 2026 changes to STT and buyback tax', '5 minutes'),
    ],
    steps=[
        'If you have a demat account, log in and check: holdings, nominee, linked bank, and any unknown charges in the last statement. If you don\'t, write whether you need one now (most index-fund investors don\'t).',
        'List every stock tip source you follow (groups, channels, apps). For each, check on SEBI\'s registered intermediaries list whether it is registered.',
        'Leave or mute any unregistered tip source.',
        'Write your stock rules for your Investment Policy Statement: whether you will hold single stocks, the maximum share of equity money, and your F&O rule.',
        'Read one company\'s annual report summary (any listed company you use, such as a bank or a telecom company) and write three things you learned. This is practice in what "research" means.',
    ],
    proof='Your demat check (or "not needed yet" note), your tip-source registration checks and your written stock rules, saved in 09 Investing.',
    templates=[
        ('stock rules (for your IPS)', """
Single stocks: Yes / Not now
If yes: at most ___% of my equity money; at most ___% in any one company
Research before buying: at least ___ weeks; I must be able to explain the business in 3 sentences
F&O: ____ (e.g. "No trading in futures and options")
Tips: I act only on SEBI-registered advisers I pay directly, after checking their registration
""", ''),
        ('tip source check', """
Source (group, channel, app),Person or firm named,SEBI registration number shown?,Found on SEBI's list?,Promises returns?,Decision (leave / mute / keep)
""", 'csv'),
    ],
    mistakes=[
        ('Treating trading as investing.', 'Investing is owning good assets for years; trading is short-term betting with costs and taxes.'),
        ('Following screenshot profits.', 'Losses are rarely posted. SEBI\'s data shows how most traders really do.'),
        ('Buying a few "safe" stocks.', 'Even large companies can fall a lot. Diversify, or limit single stocks.'),
        ('Paying for tips.', 'Only registered advisers and research analysts may give paid stock advice, and none can guarantee returns.'),
    ],
    quiz=[
        {'q': 'What share of individual F&O traders lost money in 2024-25, per SEBI\'s study?', 'o': ['About 91%', 'About 10%', 'About 50%', 'None'], 'a': 'A', 'why': 'Net losses were over ₹1 lakh crore that year.'},
        {'q': 'How are long-term gains on listed shares taxed, as of November 2026?', 'o': ['12.5% on gains above ₹1.25 lakh a year', '30% on all gains', 'Tax-free', '1% of the sale value'], 'a': 'A', 'why': 'Section 198 of the Income-tax Act, 2025 (check current rules).'},
        {'q': 'What does a demat account do?', 'o': ['Holds your shares and securities electronically', 'Lends you money', 'Pays you interest', 'Files your tax return'], 'a': 'A', 'why': 'It is the electronic holding account; the trading account places orders.'},
        {'q': 'A Telegram "guru" offers daily option-trading profits for a fee. What should you check first?', 'o': ['Whether they are on SEBI\'s list of registered advisers or analysts', 'Their follower count', 'Their profit screenshots', 'Nothing; just pay'], 'a': 'A', 'why': 'Unregistered paid advice is illegal; most such groups are scams.'},
    ],
    study='Varsity\'s introduction to stock markets, SEBI\'s F&O study, SEBI\'s fraud warnings and Budget 2026 STT changes',
    action='Check your demat (or decide you don\'t need one), check your tip sources\' registration and write your stock rules',
)

L6 = lesson(
    M, 6,
    title='Gold, REITs and real estate',
    weeks=(18, 19), hours=2,
    outcome='Compare ways to own gold, understand REITs, and judge a land or house purchase as an investment, with the costs, taxes and risks of each.',
    split='30 minutes reading, 30 minutes resources, 60 minutes action',
    core=f"""
### Gold: four ways to hold it

{table(['Form', 'Good', 'Watch out'], [
    ('Jewellery', 'Useful, culturally valued, can be pledged for a loan', 'Making charges and wastage you don\'t get back; purity questions; theft'),
    ('Gold ETFs and gold mutual funds', 'Regulated by SEBI; no making charges; small amounts; easy to sell', 'Expense ratio; market price moves; ETFs need a demat account'),
    ('Sovereign Gold Bonds (SGBs)', 'Paid 2.5% a year interest on top of gold\'s price', 'No new issues since February 2024; the government said no further tranches (' + link('ob-sgb', 'Outlook Business, February 2025') + ')'),
    ('"Digital gold" on apps', 'Small amounts', 'SEBI warned in November 2025 that it operates outside SEBI\'s regulation, with no investor protection'),
])}

- **Hallmarking:** gold jewellery must carry a **6-digit HUID** (hallmark unique ID) since April 2023 ({link('gjepc-huid', 'GJEPC')}), and the **BIS CARE app** lets you check a HUID ({link('om-biscare', 'Outlook Money')}). Check it before you buy.
- **SGBs you already hold:** RBI publishes dates for premature redemption (for example, a calendar for April to September 2026) ({link('rbi-sgb', 'RBI press release')}).
- **Digital gold:** SEBI's regulated alternatives are gold ETFs, electronic gold receipts and exchange-traded commodity derivatives ({link('sebi-digigold', 'Moneylife')}).
- **Tax:** gold ETFs and funds count as long-term after 12 months (listed) at 12.5% ({link('amfi-tax', 'AMFI tax corner')}); physical gold is long-term after 24 months ({link('it-cg', 'Income Tax Department')}). {CHECK.capitalize()}.

**How much gold?** Many people treat gold as a diversifier, a small share (often 5–10%) of long-term money, not the main investment. Kerala families often already hold a lot of gold as jewellery; count it before adding more.

### REITs

A **real estate investment trust (REIT)** owns income-producing commercial property, such as office parks, and pays most of its rental income to unitholders. REIT units trade on the stock exchange; SEBI cut the minimum application to **₹10,000–15,000** and the trading lot to **one unit** in 2021 ({link('ml-reit', 'Moneylife')}, {CHECK}). Risks: vacancies, interest rates and market price swings. A REIT gives property exposure without buying a plot.

### Land and houses as investments

Real estate is the biggest store of wealth for many Kerala families. As an **investment** (not your own home, which is FIN-M11-L02):

- **Illiquid:** selling can take months or years, often at a discount when you need cash.
- **Big, single bets:** a plot concentrates wealth in one place.
- **Costs:** stamp duty and registration on buying, brokerage, maintenance and property tax every year.
- **Legal checks:** title deeds, encumbrance certificate, approvals. For projects, check registration with **K-RERA**, where you can search registered projects and file complaints ({link('krera', 'K-RERA')}).
- **Returns:** rent is often a small percentage of the price; most of the hoped-for return is price growth, which varies a lot by place and time.
- **Tax:** long-term after 24 months at 12.5%; for land or buildings bought before 23 July 2024, resident individuals can pay 20% with indexation if that is lower ({link('it-s197', 'section 197')}, {CHECK}).

Compare a plot's expected return honestly with alternatives, using the template, before borrowing for it.
""",
    example=f"""
**Anu's** family planned to buy 5 cents of land near Kuttiady as "an investment for Anu's future", using a ₹4 lakh gold loan plus savings. Anu used the template with made-up but realistic numbers:

- Price ₹12 lakh, plus about ₹1 lakh for registration, stamp duty and brokerage.
- No rent (empty plot); yearly costs small.
- Hoped-for price in 8 years: ₹18 lakh. That is a yearly return of about 4.4% on ₹13 lakh, **before** the gold loan interest and before tax.

Meanwhile the gold loan would cost about 9% a year. The plot looked less like an investment and more like a bet on one location. The family decided not to borrow for it. Anu's father kept the idea of buying land later, with savings only, if a plot near family made sense for living, not as an investment.
""",
    resources=[
        ('sebi-digigold', 'SEBI\'s warning on digital gold, and the regulated alternatives', '10 minutes'),
        ('ob-sgb', 'Why there are no new Sovereign Gold Bond issues', '5 minutes'),
        ('gjepc-huid', 'HUID hallmarking became mandatory (headline)', '2 minutes'),
        ('om-biscare', 'Checking jewellery purity with the BIS CARE app (headline)', '2 minutes'),
        ('ml-reit', 'REIT minimum investment and trading lot', '5 minutes'),
        ('krera', 'K-RERA: search registered projects', '10 minutes'),
        ('it-s197', 'Section 197: long-term gains on property and the pre-July 2024 option', '10 minutes'),
    ],
    steps=[
        'List the gold your family holds (jewellery by weight, any ETFs, SGBs or "digital gold") and its approximate buyback value. Add your share to your Net Worth and Allocation tabs.',
        'Check the HUID on one piece of jewellery with the BIS CARE app (if it was bought after April 2023).',
        'If anyone holds "digital gold" on an app, write down what protection it has, using SEBI\'s warning.',
        'Fill in the property investment check for any land or flat purchase your family is considering (or a made-up one).',
        'Write your gold rule for your IPS: the maximum share of long-term money in gold and the forms you will use.',
    ],
    proof='Your gold list, HUID check (or note), property investment check and gold rule, saved in 09 Investing.',
    templates=[
        ('property investment check', """
B2: purchase price (₹)
B3: buying costs (stamp duty, registration, brokerage) (₹)
B4: yearly rent received (₹)       B5: yearly costs (tax, upkeep) (₹)
B6: expected sale price (₹)        B7: years held
B8: total invested   =B2+B3
B9: yearly return %  =((B6+(B4-B5)*B7)/B8)^(1/B7)*100-100     (rough; ignores timing of rent)
B10: loan interest rate if borrowing (e.g. 9)
Is B9 well above B10 and above safe options? Yes / No
Legal checks: title [ ] encumbrance [ ] approvals [ ] K-RERA (for projects) [ ]
""", ''),
        ('gold rule (for your IPS)', """
Gold as a share of my long-term money: at most ___%
Forms I use: ____ (e.g. gold ETF or gold fund; jewellery only for use)
I don't buy: ____ (e.g. unregulated digital gold)
Before buying jewellery: check HUID with BIS CARE
""", ''),
    ],
    mistakes=[
        ('Counting jewellery as an investment at the buying price.', 'Making charges are gone the day you buy; value it at the buyback rate.'),
        ('Buying "digital gold" as if it were regulated.', 'SEBI says it is outside its purview; use regulated forms.'),
        ('Borrowing to buy land as an investment.', 'Loan interest is certain; land price growth is not.'),
        ('Skipping legal checks.', 'Title problems can freeze property for years. Check documents and K-RERA registration.'),
    ],
    quiz=[
        {'q': 'What did SEBI say about "digital gold" products in November 2025?', 'o': ['They operate outside SEBI\'s regulation, with no investor protection', 'They are the safest gold', 'They pay 2.5% interest', 'They are government bonds'], 'a': 'A', 'why': 'SEBI pointed to gold ETFs, EGRs and exchange-traded derivatives as regulated options.'},
        {'q': 'What is the HUID on gold jewellery?', 'o': ['A 6-digit hallmark ID you can check with the BIS CARE app', 'A bank account number', 'A tax code', 'The shop\'s licence'], 'a': 'A', 'why': 'It identifies hallmarked jewellery; check it before buying.'},
        {'q': 'Are new Sovereign Gold Bonds being issued, as of November 2026?', 'o': ['No; the last issue was in February 2024', 'Yes, every month', 'Only for NRIs', 'Only in Kerala'], 'a': 'A', 'why': 'The government said no further tranches would be issued.'},
        {'q': 'What did SEBI change for REITs in 2021?', 'o': ['Minimum application cut to ₹10,000–15,000 and trading lot to one unit', 'REITs were banned', 'Minimum raised to ₹1 crore', 'REITs became tax-free'], 'a': 'A', 'why': 'This made REITs accessible to small investors.'},
    ],
    study='SEBI on digital gold, SGB status, HUID and BIS CARE, REIT rules, K-RERA and section 197',
    action='List your family\'s gold, check a HUID, run a property investment check and write your gold rule',
)

L7 = lesson(
    M, 7,
    title='KSFE chitty, co-operative societies and crypto: benefits and risks',
    weeks=(19, 19), hours=2,
    outcome='Explain how a chitty works and its real cost or return, judge the safety of co-operative deposits, and state crypto\'s tax treatment and risks honestly.',
    split='30 minutes reading, 30 minutes resources, 60 minutes action',
    core=f"""
### How a chitty works

A **chitty (kuri)** is a group saving-and-borrowing scheme. Each member pays a fixed instalment every month; each month one member gets the "prize", decided by auction. **KSFE**, owned by the Government of Kerala, runs chitties under the Central Chit Funds Act, 1982 ({link('ksfe-chitty', 'KSFE')}, {CHECK}):

- Tenures from **25 to 120 months**; instalments from **₹1,000 to ₹6,00,000 a month**.
- In each month's auction, the member who accepts the **biggest discount** on the chit amount wins the prize money. KSFE caps the discount at **30%, 35% or 40%**, depending on the chitty type.
- The discount, after the **foreman's commission** (the organiser's fee, stated in your chit agreement), is shared among members as a **dividend**, so everyone's instalment that month is lower.
- After winning, you must give **security** for the instalments still to come (a salaried person's surety, property, deposits, gold, insurance policies and others), or keep an equal amount in a KSFE deposit.

### Two roles, two costs

A chitty is a **loan** for early winners and a **saving** for late winners:

**Worked example** (illustrative numbers, not KSFE's): a ₹2,50,000 chitty of 50 months, 50 members, with net instalments averaging ₹4,250 after dividends.

- **Early winner:** bids the maximum discount in month 2 and receives ₹1,75,000, then keeps paying for the rest of the chitty. Total paid: about ₹2,12,500. The effective cost works out to about **{CH_EARLY:.0f}% a year**: like a loan.
- **Late winner:** waits until the last month and receives ₹2,37,500 (a small discount). The effective return is about **{CH_LATE:.1f}% a year**: like a deposit.

Your real numbers depend on actual auction discounts, which you only know as the chitty runs. Use the template to calculate yours.

**Benefits:** forced monthly saving; access to a lump sum without a credit history; KSFE is government-owned. **Risks:** money is locked; you can't plan the auction outcome; borrowing through a chitty can be expensive; the security rules can delay your prize. **Private chit funds** that are unregistered or run informally carry real fraud risk. Never join one without checking its registration.

### Co-operative banks and societies

Kerala's co-operative sector serves millions of families, often with good service and slightly higher rates. Know what protects your money:

- **Co-operative banks registered with DICGC:** deposits insured up to **₹5 lakh per depositor per bank** ({link('dicgc', 'DICGC')}).
- **Co-operative credit societies** that aren't licensed banks: RBI warned that some wrongly use the word "bank" and that **DICGC cover is not available** for their deposits ({link('rbi-coop', 'RBI')}).
- **Kerala's own guarantee:** the Kerala Co-operative Deposit Guarantee (Amendment) Scheme, 2026 (notified 9 January 2026) provides a guarantee for **members'** deposits in societies, reported as up to **₹10 lakh per member**, depending on the society having paid its contribution to the fund ({link('kl-dgf', 'TeamLease RegTech')}, {link('ic-dgf', 'Indian Cooperative')}, {CHECK}).
- Kerala has seen several co-operative and private finance failures. Spread deposits, stay within guarantee limits, and prefer institutions whose accounts and audit reports you can see.

### Crypto: not banned, not legal tender, heavily taxed

- **Legal status:** the government told Parliament in 2019 that India had **not banned** cryptocurrency and had no separate law for it ({link('inc42-crypto', 'Inc42, July 2019')}); in 2022 the Finance Secretary said crypto "will never become legal tender": you can buy it, but it has no government authorisation and the government is not responsible for losses ({link('quint-crypto', 'The Quint, February 2022')}). These are the latest official statements found for this course; {CHECK}, as crypto rules may change.
- **Tax:** income from transferring crypto (virtual digital assets) is taxed at a flat **30% plus surcharge and cess**, with **no deduction except the cost** of buying and **no set-off of losses** against other income; **1% TDS** applies on transfers above ₹50,000 a year (for most individuals) or ₹10,000 (others) ({link('it-vda', 'Income Tax Department')}, {CHECK}).
- **Protection:** there is no investor-protection system for crypto like the ones for bank deposits or mutual funds. Exchanges can be hacked or shut; wrong transfers can't be reversed.
- **Scams:** fake crypto apps and "trading bots" that show rising balances you can't withdraw are among the most common investment frauds (Module 15).

If you choose to hold crypto, treat it as speculation: a small amount you could lose completely, outside your goals and emergency fund, and declared in your tax return.
""",
    example=f"""
**Rahul** joined a ₹3,000-a-month KSFE chitty of 50 months (₹1,50,000), planning to use it for his sister's second-year fees. In month 9, he needed money and won the auction with a 28% discount: prize ₹1,08,000. He gave his salary certificate and a colleague's surety as security.

He calculated the real cost with the template: he had paid 9 instalments (averaging ₹2,600 after dividends), received ₹1,08,000, and would pay about 41 more instalments averaging ₹2,700. The effective cost came to about 19% a year, well above what a bank education loan would have cost, but he had no other quick option at the time. His lesson: "A chitty is a loan if you win early. Next time I'll compare it with a loan before I bid."

His mother, meanwhile, had ₹6 lakh in a primary co-operative society. They checked: it was not a licensed bank. They kept ₹3 lakh there (within the Kerala guarantee for members, after confirming her membership) and moved the rest to a post office MIS.
""",
    resources=[
        ('ksfe-chitty', 'How KSFE chitties work: tenures, auctions, discounts, security', '15 minutes'),
        ('rbi-coop', 'Co-operative societies, the word "bank" and deposit insurance', '5 minutes'),
        ('kl-dgf', 'The Kerala Co-operative Deposit Guarantee (Amendment) Scheme, 2026', '10 minutes'),
        ('ic-dgf', 'The ₹10 lakh guarantee for co-op members (January 2026)', '5 minutes'),
        ('it-vda', 'How crypto (virtual digital assets) is taxed', '10 minutes'),
    ],
    steps=[
        'List every chitty (KSFE or private) and co-operative deposit in your family: amount, institution, whether it is a licensed bank, and its insurance or guarantee.',
        'For any chitty, fill in the chitty calculator with real or expected numbers and find whether it is working as a loan or a saving for you.',
        'For private chitties, check the organiser\'s registration; if none, write a plan to stop at the next safe point.',
        'For co-operative deposits, check: licensed bank or society? DICGC or Kerala guarantee? Within limits? Write one action if not.',
        'Write your crypto rule for your IPS (for example, "none", or "at most 2% of long-term money, never borrowed").',
    ],
    proof='Your chitty and co-operative list with protection checks, one chitty calculation (or the example) and your crypto rule, saved in 09 Investing.',
    templates=[
        ('chitty calculator (one row per month)', """
Row 1: Month,Instalment paid (₹, after dividend),Prize received (₹),Cash flow
D2: =C2-B2     (copy down for every month)
Monthly rate: =IRR(D2:D121)       Yearly rate %: =((1+IRR(D2:D121))^12-1)*100
If you won early, the yearly rate is your borrowing cost; compare with a bank loan.
If you won late, it is your saving return; compare with an RD or FD.
""", ''),
        ('co-operative deposit check', """
Institution,Licensed bank or society?,DICGC insured?,Member? (for the Kerala guarantee),Amount (₹),Within ₹5 lakh (DICGC) or ₹10 lakh (Kerala guarantee)?,Audit report seen?,Action
""", 'csv'),
    ],
    mistakes=[
        ('Thinking a chitty is always a saving.', 'Win early and it is a loan, often an expensive one. Calculate both roles.'),
        ('Joining unregistered chitties on trust.', 'Trust is not a guarantee. Check registration.'),
        ('Putting large sums in one co-operative society.', 'Know which protection applies and stay within it.'),
        ('Treating crypto as an investment for goals.', 'It is taxed heavily, unprotected and volatile. Keep it to money you can lose.'),
    ],
    quiz=[
        {'q': 'In a chitty, who effectively borrows money?', 'o': ['Members who win the prize early', 'Members who win in the last month', 'The government', 'Nobody'], 'a': 'A', 'why': 'They receive a discounted lump sum early and keep paying instalments.'},
        {'q': 'What is KSFE\'s maximum chitty discount, per its website?', 'o': ['30%, 35% or 40%, depending on the chitty type', '5%', '100%', 'There is no limit'], 'a': 'A', 'why': 'The cap depends on the type of chitty (check current rules).'},
        {'q': 'Are deposits in a co-operative credit society that isn\'t a licensed bank covered by DICGC?', 'o': ['No', 'Yes, up to ₹5 lakh', 'Yes, unlimited', 'Only for senior citizens'], 'a': 'A', 'why': 'RBI says DICGC cover isn\'t available; Kerala\'s own guarantee scheme covers members\' deposits within its limits.'},
        {'q': 'How is income from selling crypto taxed, as of November 2026?', 'o': ['30% plus surcharge and cess, only cost deductible, no loss set-off', 'At your slab with all expenses deductible', 'Tax-free below ₹1 lakh', '12.5% after a year'], 'a': 'A', 'why': 'Virtual digital assets have a special flat rate; 1% TDS applies on transfers above the limit.'},
    ],
    study='KSFE chitty rules, RBI on co-operative societies, the Kerala deposit guarantee scheme and crypto taxation',
    action='List and check your family\'s chitties and co-operative deposits, calculate one chitty and write your crypto rule',
)

LESSONS = [L1, L2, L3, L4, L5, L6, L7]

MODULE = module(
    M,
    title='Investment options in India',
    weeks=(16, 19), hours=16,
    overview="""
Learn how each common investment in India works, what it costs, how it is taxed and what can go wrong, and compare options with official data, without anyone selling you anything.

This is the longest module, because India offers many choices: mutual funds and index funds, post office schemes and deposits, EPF, PPF and NPS, shares, gold in several forms, REITs and property, and the Kerala favourites: KSFE chitties and co-operative deposits. Plus crypto, which you will be asked about.

The aim is not to pick products. It is to know, for each option, **what job it can do in your plan** (safety, income, growth, diversification), what it costs and how it can fail. You build a fund-comparison sheet from official data, check every adviser and tip source against SEBI's list, and write rules for gold, stocks, chitties and crypto. All of it feeds your Investment Policy Statement in Module 17.
""",
    outcomes=[
        'Explain mutual funds, direct vs regular plans and the long-term cost of expense ratios',
        'Compare funds with official data and verify an adviser\'s SEBI registration',
        'Choose safe options for short and medium goals by post-tax return',
        'Explain EPF, PPF and NPS rules and tax as of November 2026',
        'Describe the honest risks of stocks, F&O, gold forms, REITs, property, chitties, co-operative deposits and crypto',
    ],
    lessons=LESSONS,
    project='My investment shortlist, by job, not by product',
    project_steps=[
        'Make one page called **Shortlist** in your workbook with four sections: safety (emergency and short goals), income (if needed), long-term growth, and diversifiers (gold, REITs).',
        'For each section, write the type of option that fits (for example, "post office TD and RD", "broad equity index fund, direct plan", "PPF", "gold ETF") and the evidence: your comparisons from this module.',
        'List what you have decided **not** to use and why (for example, F&O, digital gold, unregistered chitties, endowment plans).',
        'Write your rules for single stocks, gold, chitties, co-op deposits and crypto in one place.',
        'Don\'t buy anything new yet unless it is a safe option for a short goal. You will write your Investment Policy Statement in Module 17 first.',
    ],
    project_proof='Your Shortlist page with evidence, exclusions and rules, saved in 09 Investing.',
    rubric=[
        ('Mutual funds', 'Can\'t explain them', 'Understands basics', 'Compared direct and regular, and three funds from official data'),
        ('Safe options', 'Not matched to goals', 'Some goals matched', 'Every short and medium goal matched by post-tax return'),
        ('Retirement accounts', 'Unknown', 'Listed', 'Balances, nominees and rules checked; fit decided'),
        ('Risky options', 'Not considered', 'Some rules', 'Written rules for stocks, F&O, gold, chitties, co-ops and crypto'),
        ('Advice', 'Follows tips', 'Some checks', 'Every adviser and tip source checked on SEBI\'s list'),
    ],
    short=[
        'Compare direct and regular plans of one fund (FIN-M09-L01).',
        'Match each short goal to a safe option using the rates table (FIN-M09-L03).',
        'Check your EPF/PPF/NPS nominees and balances (FIN-M09-L04).',
        'Check one tip source on SEBI\'s list (FIN-M09-L05).',
    ],
    flashcards=[
        ('Direct vs regular plan', 'Same fund and manager; direct has no commission, so lower cost and higher NAV.'),
        ('Where to check an adviser', 'SEBI\'s list of registered investment advisers.'),
        ('Small savings rates, Oct–Dec 2026', 'PPF 7.1%, NSC 7.7%, SCSS 8.2%, SSA 8.2%, MIS 7.4%, KVP 7.5%, RD 6.7%.'),
        ('Debt fund tax (bought from April 2023)', 'Gains taxed at your slab, however long you hold.'),
        ('EPF rate for 2025-26', '8.25%.'),
        ('NPS exit for non-government subscribers', 'Up to 80% lump sum, at least 20% annuity; full withdrawal if corpus ≤ ₹8 lakh.'),
        ('F&O reality', 'About 91% of individual traders lost money in 2024-25 (SEBI).'),
        ('Crypto tax', '30% plus surcharge and cess; only cost deductible; no loss set-off; 1% TDS above limits.'),
    ],
    mistakes=[
        ('Starting with products instead of jobs.', 'Decide what each rupee is for, then choose the type of option.'),
        ('Trusting "safe" labels.', 'Check what actually protects the money: government backing, insurance, regulation, or nothing.'),
        ('Doing everything at once.', 'Most people need only a few options: a safe place, a retirement account and a diversified growth option.'),
    ],
    project_week=19,
)
