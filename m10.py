"""Module 10: Taxes."""
from common import lesson, module, link, fence, table, inr, ASOF, CHECK

M = 10


def new_tax(gross, std=75000):
    ti = max(gross - std, 0)
    slabs = [(400000, 0), (800000, .05), (1200000, .10), (1600000, .15), (2000000, .20), (2400000, .25), (10 ** 12, .30)]
    tax, low = 0, 0
    for up, r in slabs:
        if ti > low:
            tax += (min(ti, up) - low) * r
        low = up
    tax = 0 if ti <= 1200000 else min(tax, ti - 1200000)
    return ti, tax * 1.04


def old_tax(gross, ded):
    ti = max(gross - ded, 0)
    slabs = [(250000, 0), (500000, .05), (1000000, .20), (10 ** 12, .30)]
    tax, low = 0, 0
    for up, r in slabs:
        if ti > low:
            tax += (min(ti, up) - low) * r
        low = up
    if ti <= 500000:
        tax = 0
    return ti, tax * 1.04


def breakeven(gross):
    """Smallest old-regime deductions (incl. ₹50,000 standard) at which old tax <= new tax."""
    target = new_tax(gross)[1]
    lo, hi = 0, gross
    for _ in range(100):
        mid = (lo + hi) / 2
        if old_tax(gross, mid)[1] <= target:
            hi = mid
        else:
            lo = mid
    return hi


OLD_DED = 50000 + 150000 + 25000 + 2500
ROWS = []
for g in (600000, 900000, 1300000, 1800000):
    n_ti, n_tax = new_tax(g)
    o_ti, o_tax = old_tax(g, OLD_DED)
    ROWS.append((inr(g), inr(n_ti), inr(n_tax), inr(o_ti), inr(o_tax), 'New' if n_tax < o_tax else ('Old' if o_tax < n_tax else 'Same'), inr(breakeven(g)) if new_tax(g)[1] > 0 else 'Old can\'t beat ₹0'))

L1 = lesson(
    M, 1,
    title='Income tax basics under the Income-tax Act, 2025',
    weeks=(20, 20), hours=2,
    outcome='Explain how income tax works in India under the new law: tax year, heads of income, slabs, rebate, cess, TDS, and where to see what the department already knows about you.',
    split='30 minutes reading, 40 minutes resources, 50 minutes action',
    core=f"""
### A new law from 1 April 2026

The **Income-tax Act, 2025** came into force on **1 April 2026**, replacing the Income-tax Act, 1961 ({link('it-act-2025', 'Income Tax Department')}). The government says the aim was to simplify the language and structure "without altering the underlying tax policy" ({link('it-press-2025', 'CBDT press release')}). So most rules you hear about still exist, under **new section numbers**. This course gives the new numbers with the old names in brackets, such as "section 123 (the old 80C)".

Returns filed during 2026 were for income earned in 2025-26 under the old law; your return for income earned from April 2026 onwards is under the new law. Form names and numbers may also change; the e-filing portal guides you.

### The basic idea

1. **Add up your income for the tax year** (1 April to 31 March) under five heads: **salary**, **house property**, **business or profession**, **capital gains**, and **other sources** (interest, dividends, gifts above limits and so on).
2. **Subtract the deductions your regime allows** to get **total (taxable) income**.
3. **Apply the slab rates** of your regime (FIN-M10-L02).
4. **Subtract any rebate**, then add **4% health and education cess** (and surcharge only on very high incomes) ({link('it-rates', 'tax rates page')}).
5. **Subtract tax already paid**: TDS, advance tax. The rest is payable; if you paid too much, you get a refund.

### The two regimes, in one line each

- **New regime** (the default): lower slab rates, very few deductions. With the **rebate under section 156**, resident individuals with total income up to **₹12 lakh** pay **no tax** ({link('it-s156', 'section 156')}); salaried people also get a **₹75,000 standard deduction** ({link('it-s19', 'section 19')}).
- **Old regime:** higher slab rates, but deductions such as section 123 (the old 80C) and health insurance (section 126, the old 80D).

Budget 2026 kept the slabs, the ₹12 lakh rebate and the ₹75,000 standard deduction unchanged ({link('sb18-budget26', 'Storyboard18')}). FIN-M10-L02 calculates both for you.

### TDS: tax deducted before you are paid

Employers deduct tax from salaries; banks deduct TDS on interest above a yearly limit; clients may deduct TDS from professional fees. **TDS is not an extra tax**: it is part of your tax, paid in advance. When you file, you add up your real tax, subtract all TDS, and pay the balance or get a refund. If you have no taxable income but TDS was deducted, **filing a return is how you get it back**.

### What the department already knows: AIS

The **Annual Information Statement (AIS)** on the e-filing portal shows what has been reported about you: TDS and TCS, specified financial transactions (such as large deposits or investments), tax payments, demands and refunds. Log in to the e-filing portal, go to **Services → Annual Information Statement (AIS)**, choose the year and open it; the **TIS** is a category-wise summary, and you can give feedback if something is wrong ({link('it-ais', 'Income Tax Department')}). Checking AIS before filing prevents most mismatch notices.

### Do you need to file?

You must file if your income is above the basic exemption limit, and in certain other situations defined in the law. Even if you don't have to, filing is useful: it claims TDS refunds, creates a record of income for loans and visas, and lets you carry forward some losses. The e-filing portal explains who must file.
""",
    example=f"""
**Anu** had never filed a return: "My income is below the limit, so tax isn't for me." Then she logged in to the e-filing portal with her PAN for the first time and opened her AIS.

It showed ₹2,840 of TDS: a coaching centre where she had taught weekend classes had deducted TDS from her fees, and her bank had reported FD interest. Her total income for the year was about ₹1,90,000, far below the taxable limit, so her tax was ₹0. The only way to get the ₹2,840 back was to file a return.

She also saw the coaching centre had reported her fees under her PAN, so the department knew about that income. "AIS is the department's diary about me," she wrote. "I'll read it every year before filing." She files her first return in FIN-M10-L04.
""",
    resources=[
        ('it-press-2025', 'The CBDT press release on the new Act: what changed and what didn\'t', '10 minutes'),
        ('it-s156', 'Section 156: the rebate, in the new Act\'s own words', '10 minutes'),
        ('it-ais', 'Steps to open your AIS and TIS', '10 minutes'),
        ('varsity', 'Module 7, "Markets and Taxation": the first chapters on how income is classified and taxed', '30 minutes'),
    ],
    steps=[
        'Check that your PAN is active and linked to Aadhaar (the e-filing portal shows the status on login or under your profile). Register on the portal if you haven\'t.',
        'Open your AIS and TIS for the latest year available. Note every item: TDS, interest, dividends, transactions.',
        'Check each item against your own records. Note anything wrong for feedback.',
        'Make a **Tax** tab and list your income for the current tax year by the five heads, even if it is small.',
        'Start your tax documents list using the template: what you have, what you need to collect.',
    ],
    proof='A screenshot of your AIS summary (PAN and account numbers covered), your income by head and your documents list, saved in 10 Tax.',
    templates=[
        ('income by head (Tax tab)', """
Head,Source,Amount for the tax year (₹),Proof or document,TDS deducted (₹)
Salary,,,(salary slips / employer's TDS certificate),
House property,,,,
Business or profession,(tuition, freelance fees),,(invoices, bank statement),
Capital gains,(sales of funds, shares, gold, land),,(CAS, broker statement),
Other sources,(savings and FD interest, dividends),,(bank interest certificate),
Total,,=SUM(C2:C6),,=SUM(E2:E6)
""", 'csv'),
        ('tax documents checklist', """
[ ] PAN active and linked to Aadhaar
[ ] e-filing portal login works; bank account pre-validated for refunds
[ ] Salary slips and employer's TDS certificate (if salaried)
[ ] Bank interest certificates for every account and FD
[ ] Mutual fund and demat capital gains statements (CAS, broker report)
[ ] Rent receipts, insurance premium receipts, PPF/ELSS/NPS proofs (only if using the old regime)
[ ] AIS and TIS downloaded and checked
[ ] Invoices and receipts register (freelance or business income)
""", ''),
    ],
    mistakes=[
        ('Thinking "no tax due" means "no return needed".', 'Filing claims TDS refunds and builds an income record. Check whether you must file.'),
        ('Ignoring AIS.', 'Mismatches between your return and AIS cause notices. Check it before filing.'),
        ('Treating TDS as the final tax.', 'TDS is an advance. Your real tax may be more (pay the rest) or less (claim a refund).'),
        ('Using old section numbers in new-law forms.', 'The rules mostly carried over, but numbers changed. Use the new Act\'s numbers for tax years from April 2026.'),
    ],
    quiz=[
        {'q': 'From when is the Income-tax Act, 2025 in force?', 'o': ['1 April 2026', '1 April 2025', '1 January 2027', 'It hasn\'t started'], 'a': 'A', 'why': 'It replaced the 1961 Act from 1 April 2026.'},
        {'q': 'Under the new regime, up to what total income does a resident individual pay no tax because of the rebate?', 'o': ['₹12 lakh', '₹5 lakh', '₹2.5 lakh', '₹7 lakh'], 'a': 'A', 'why': 'Section 156 gives a rebate of up to ₹60,000, so tax is nil up to ₹12 lakh of total income.'},
        {'q': 'Your bank deducted ₹2,000 TDS but your income is below the taxable limit. How do you get it back?', 'o': ['File an income tax return', 'Ask the bank branch for cash', 'It can\'t be recovered', 'Apply to RBI'], 'a': 'A', 'why': 'TDS credits are refunded through the return.'},
        {'q': 'Where can you see what TDS and transactions have been reported under your PAN?', 'o': ['The Annual Information Statement (AIS) on the e-filing portal', 'Your credit report', 'Your passbook only', 'Form 15G'], 'a': 'A', 'why': 'AIS shows TDS/TCS, specified transactions, tax paid, demands and refunds.'},
    ],
    study='The CBDT press release, section 156, the AIS steps and Varsity\'s taxation basics',
    action='Check your PAN and AIS, list your income by head and start your tax documents checklist',
)

L2 = lesson(
    M, 2,
    title='Old regime or new? Worked examples and your own calculator',
    weeks=(20, 20), hours=2.5,
    outcome='Calculate income tax under both regimes for sample incomes and your own, with a spreadsheet that applies slabs, rebate, marginal relief and cess, and choose the right regime.',
    split='30 minutes reading, 30 minutes resources, 90 minutes action',
    core=f"""
### New regime (section 202, the default)

{table(['Total income', 'Rate'], [
    ('Up to ₹4,00,000', 'Nil'), ('₹4,00,001 – ₹8,00,000', '5%'), ('₹8,00,001 – ₹12,00,000', '10%'),
    ('₹12,00,001 – ₹16,00,000', '15%'), ('₹16,00,001 – ₹20,00,000', '20%'), ('₹20,00,001 – ₹24,00,000', '25%'),
    ('Above ₹24,00,000', '30%'),
])}

({link('it-s202', 'section 202')}, {CHECK}.) Salaried people deduct a **₹75,000 standard deduction** first. The **rebate** makes tax nil up to ₹12 lakh of total income; just above ₹12 lakh, **marginal relief** limits the tax to the income above ₹12 lakh, so a small rise in income never costs more than the rise itself ({link('it-s156', 'section 156')}). Add 4% cess. Most other deductions aren't allowed; employer contributions to NPS are an important exception (FIN-M09-L04).

### Old regime

{table(['Total income (below 60)', 'Rate'], [
    ('Up to ₹2,50,000', 'Nil'), ('₹2,50,001 – ₹5,00,000', '5%'), ('₹5,00,001 – ₹10,00,000', '20%'), ('Above ₹10,00,000', '30%'),
])}

For residents aged 60 to 80 the nil band is ₹3 lakh, and for 80+ ₹5 lakh ({link('it-rates', 'tax rates')}). The rebate makes tax nil up to ₹5 lakh of total income. The standard deduction is ₹50,000. The main deductions:

- **Section 123 (the old 80C), up to ₹1.5 lakh:** EPF and PPF contributions, life insurance premiums, ELSS, NSC, 5-year tax-saving deposits, SCSS, tuition fees for two children, home loan principal, and stamp duty on a house ({link('it-sched15', 'Schedule XV')}, {link('bs-s123', 'Business Standard')}).
- **Section 126 (the old 80D):** health insurance, ₹25,000 for self and family and ₹25,000 for parents, ₹50,000 each for senior citizens ({link('it-s126', 'section 126')}).
- **NPS:** an extra ₹50,000 (the old 80CCD(1B)).
- Others with conditions: home loan interest, house rent allowance, professional tax, education loan interest.

### Who should choose which?

Your employer may ask you at the start of the year, for TDS. Individuals **without business income** can choose the regime **every year** when filing; those **with business or professional income** opt out of the new regime by the due date, and can switch back only once (section 202(4)) ({link('it-s202', 'section 202')}).

### Worked examples (salaried, under 60, tax year 2026-27 rates)

Old-regime deductions assumed: standard ₹50,000 + section 123 ₹1,50,000 + health insurance ₹25,000 + professional tax ₹2,500 = **{inr(OLD_DED)}**. Tax includes 4% cess; surcharge ignored.

{table(['Salary', 'New: taxable', 'New: tax', 'Old: taxable', 'Old: tax', 'Lower', 'Old wins only if deductions exceed'], ROWS)}

The pattern: **with the ₹12 lakh rebate, the new regime wins for most people** unless they have very large deductions (a big home loan interest, high rent with HRA, full section 123 and NPS). At ₹18 lakh, the old regime wins only if total deductions (including the standard deduction) exceed about {inr(breakeven(1800000))}.

### Do the calculation, don't guess

Your own numbers decide. The template builds both regimes with formulas, so you can test different deductions and see the break-even. Then cross-check your result with the Income Tax Department's own **income and tax calculator**, which compares the regimes for a chosen year, age and income ({link('it-calc', 'official calculator')}). Revisit it every year: rules, your income and your deductions all change.
""",
    example=f"""
**Rahul's** salary for the tax year is ₹4,20,000 (made-up). His office asked him to choose a regime for TDS.

- **New:** ₹4,20,000 − ₹75,000 = ₹3,45,000 taxable, below ₹4 lakh: **tax ₹0**.
- **Old:** he could claim his NPS contribution, his mother's money-back premium for him and Medisep (Module 14), but with income this low the old regime also gives **₹0** after the rebate.

Both are zero, so he chose the default new regime, which is simpler. He then played with the calculator for his future: at a salary of ₹13 lakh with his likely deductions, the new regime would cost {inr(new_tax(1300000)[1])} and the old {inr(old_tax(1300000, OLD_DED)[1])}. "I don't need to buy anything just to save tax," he noted. "I'll invest for my goals and let the regime follow the numbers."

**Fathima** (freelancer) has business income, so she can't switch freely every year: once she opts for the old regime she can come back to the new one only once. She decided to stay in the new regime unless her calculator shows a clear, lasting advantage.
""",
    resources=[
        ('it-s202', 'Section 202: new regime slabs and the rules for opting out', '15 minutes'),
        ('it-s156', 'Section 156: rebate and marginal relief', '10 minutes'),
        ('it-s19', 'Section 19: standard deduction and professional tax', '5 minutes'),
        ('it-rates', 'Old regime slabs, senior citizen limits, surcharge and cess', '10 minutes'),
        ('it-sched15', 'Schedule XV: what counts for section 123 (old 80C)', '10 minutes'),
        ('it-s126', 'Section 126: the health insurance deduction', '5 minutes'),
        ('it-calc', 'The official income and tax calculator: try the basic calculator with your income', '10 minutes'),
    ],
    steps=[
        'Build the two-regime calculator in your Tax tab from the template.',
        'Test it with the four worked examples in this lesson; your answers must match the table.',
        'Enter your own expected income for this tax year (salary, freelance, interest), and the deductions you really have (not ones you might buy).',
        'Read the result and the break-even: how much in deductions would make the old regime worth it?',
        'Cross-check your own case on the Income Tax Department\'s official income and tax calculator; if the answers differ, find out why (age, year or a deduction).',
        'Write your regime decision for this year and one sentence on why. If you have business income, note the switching rule.',
    ],
    proof='A screenshot of your Tax tab calculator showing the four test cases matching and your own result with your regime decision, saved in 10 Tax.',
    templates=[
        ('two-regime calculator (Tax tab)', """
INPUTS
B2: salary income (₹)                 B3: other income (interest, freelance profit, etc.) (₹)
B4: salaried? (1 = yes, 0 = no)       B5: old-regime deductions excluding standard deduction (₹)

NEW REGIME
B8: taxable        =MAX(B2+B3-75000*B4,0)
Slab table in D8:E14  (lower limit | extra rate):  0|0  400000|0.05  800000|0.05  1200000|0.05  1600000|0.05  2000000|0.05  2400000|0.05
B9: slab tax       =SUMPRODUCT((B8>D8:D14)*(B8-D8:D14)*E8:E14)
B10: after rebate  =IF(B8<=1200000,0,MIN(B9,B8-1200000))
B11: with 4% cess  =ROUND(B10*1.04,0)

OLD REGIME
B14: taxable       =MAX(B2+B3-50000*B4-B5,0)
Slab table in D17:E20 (lower limit | extra rate):  0|0  250000|0.05  500000|0.15  1000000|0.10
B15: slab tax      =SUMPRODUCT((B14>D17:D20)*(B14-D17:D20)*E17:E20)
B16: after rebate  =IF(B14<=500000,0,B15)
B17: with 4% cess  =ROUND(B16*1.04,0)

B20: lower regime  =IF(B11<B17,"New",IF(B17<B11,"Old","Same"))
B21: difference    =ABS(B11-B17)
Notes: surcharge (above ₹50 lakh) is not included. Seniors: change 250000 to 300000 (60-80) or 500000 (80+) in D18.
""", ''),
    ],
    mistakes=[
        ('Choosing the old regime out of habit.', 'Since the ₹12 lakh rebate, the new regime often wins. Calculate both every year.'),
        ('Buying products just to save tax.', 'An endowment policy or ELSS bought only for the deduction can cost more than the tax saved.'),
        ('Forgetting cess.', 'Add 4% to the tax. Small, but it should be in your plan.'),
        ('Switching freely with business income.', 'With business or professional income you can return to the new regime only once.'),
    ],
    quiz=[
        {'q': 'Salary ₹9 lakh, new regime: what is the tax?', 'o': ['₹0', '₹45,000', '₹25,000', '₹90,000'], 'a': 'A', 'why': '₹9,00,000 − ₹75,000 = ₹8,25,000, below ₹12 lakh, so the rebate makes it nil.'},
        {'q': 'In the old regime, what is the section 123 (old 80C) limit?', 'o': ['₹1.5 lakh', '₹50,000', '₹2.5 lakh', 'No limit'], 'a': 'A', 'why': 'The limit carried over unchanged into the new Act.'},
        {'q': 'Taxable income in the new regime is ₹12,25,000. What does marginal relief limit the tax to (before cess)?', 'o': ['₹25,000', '₹63,750', '₹0', '₹1,22,500'], 'a': 'A', 'why': 'Tax can\'t exceed the income above ₹12 lakh: ₹25,000.'},
        {'q': 'A salaried person with no business income: how often can they choose the regime?', 'o': ['Every year, when filing', 'Once in a lifetime', 'Never; the employer decides', 'Every month'], 'a': 'A', 'why': 'Only those with business income face the one-time switch-back rule.'},
        {'q': 'Which formula applies new-regime slabs from a slab table?', 'o': ['=SUMPRODUCT((B8>D8:D14)*(B8-D8:D14)*E8:E14)', '=B8*0.3', '=SUM(D8:D14)', '=VLOOKUP(B8,D8:E14,2)*B8'], 'a': 'A', 'why': 'It adds each slab\'s extra rate on the income above that slab\'s lower limit.'},
    ],
    study='Sections 202, 156 and 19, the old regime rates page, Schedule XV and section 126',
    action='Build the two-regime calculator, test it against the worked examples and choose your regime with your own numbers',
)

L3 = lesson(
    M, 3,
    title='Capital gains, TDS and advance tax',
    weeks=(21, 21), hours=2,
    outcome='Work out the tax on selling investments, gold or property, track TDS through the year, and pay advance tax on time if you need to.',
    split='30 minutes reading, 30 minutes resources, 60 minutes action',
    core=f"""
### Capital gains: what you pay when you sell

**Capital gain = sale price − purchase cost (and allowed expenses)**. Whether it is short-term or long-term depends on how long you held the asset. As of November 2026 ({CHECK}):

{table(['Asset', 'Long-term after', 'Short-term tax', 'Long-term tax'], [
    ('Listed shares, equity mutual funds (STT paid)', '12 months', '20% (section 196)', '12.5% on gains above ₹1.25 lakh a year (section 198)'),
    ('Debt mutual funds bought from 1 April 2023', 'Never: always short-term', 'Your slab rate (section 76)', '—'),
    ('Gold ETFs and other listed funds', '12 months', 'Your slab rate', '12.5%'),
    ('Physical gold, land, buildings, unlisted assets', '24 months', 'Your slab rate', '12.5%; for land or buildings bought before 23 July 2024, residents can choose 20% with indexation if lower (section 197)'),
    ('Crypto (virtual digital assets)', '—', '30% flat on gains; no loss set-off', '30% flat'),
])}

Sources: {link('it-s196', 'section 196')}, {link('it-s198', 'section 198')}, {link('it-s76', 'section 76')}, {link('it-s197', 'section 197')}, {link('it-cg', 'holding periods')}, {link('amfi-tax', 'AMFI tax corner')}, {link('it-vda', 'VDA taxation')}. From Budget 2026, money received in a company **buyback** is also taxed as capital gains ({link('om-budget26', 'Outlook Money')}).

**Worked example:** Fathima sells equity index fund units after 3 years, with a gain of ₹1,60,000. Long-term gains up to ₹1,25,000 a year are tax-free; tax is 12.5% of ₹35,000 = ₹4,375, plus 4% cess = **₹4,550**. Had she sold after 10 months, the whole ₹1,60,000 would be short-term: 20% = ₹32,000 plus cess.

Some long-term investors **use the ₹1.25 lakh yearly exemption** by selling and buying back units to raise their cost; it is legal, but check exit loads and costs, and keep records.

### TDS through the year

- **Salary:** your employer estimates your yearly tax under your chosen regime and deducts it monthly. Tell your employer about other income if you want TDS to cover it.
- **Interest:** banks deduct TDS when interest from that bank crosses a yearly limit, ₹50,000 for most people and higher for senior citizens ({link('fb26-notes', 'Finance Bill 2026 notes')}); if your total income is below the taxable limit, you can give the bank a self-declaration so it doesn't deduct.
- **Dividends and professional fees:** fund houses, companies and business clients may deduct TDS above small yearly limits.

All TDS shows in your AIS. Check it every quarter.

### Advance tax: paying as you earn

If your tax for the year, **after TDS**, will be **₹10,000 or more**, you pay it in instalments during the year, under sections 403 to 405 of the new Act ({link('sansa-advtax', 'Sansa Legal, June 2026')}, {CHECK}):

{table(['By', 'Cumulative share of your estimated tax'], [
    ('15 June', '15%'), ('15 September', '45%'), ('15 December', '75%'), ('15 March', '100%'),
])}

- People using **presumptive taxation** (FIN-M10-L05) can pay all of it by **15 March**.
- **Resident senior citizens without business income** don't have to pay advance tax.
- Late or short payment means interest. Most salaried people don't need advance tax, because TDS covers it; freelancers often do.

Pay through the e-filing portal's **e-Pay Tax** service, and keep the challan details.
""",
    example=f"""
**Fathima** estimated her tax for the year: about ₹38,000, with ₹6,000 already deducted as TDS by two Indian clients. The balance, ₹32,000, is above ₹10,000, so she needs advance tax.

Is she under presumptive taxation (FIN-M10-L05)? Yes, so she can pay it all by 15 March. But to avoid a big bill at once, she set up the planner anyway: ₹4,800 by 15 June, ₹14,400 by 15 September, ₹24,000 by 15 December, and the rest by 15 March, from the tax reserve in her holding account (FIN-M03-L04).

She also checked her AIS in October and found one client's TDS missing. She emailed the client, who had quoted her PAN wrongly; it was corrected before she filed.
""",
    resources=[
        ('it-s196', 'Section 196: short-term gains on equity', '5 minutes'),
        ('it-s198', 'Section 198: long-term gains on equity and the ₹1.25 lakh exemption', '5 minutes'),
        ('it-s197', 'Section 197: long-term gains on property and other assets', '5 minutes'),
        ('amfi-tax', 'AMFI\'s tax corner: how each type of fund is taxed', '15 minutes'),
        ('sansa-advtax', 'Advance tax under the new Act: who, when, how much', '10 minutes'),
        ('varsity', 'Module 7, "Markets and Taxation": the chapters on capital gains', '20 minutes'),
    ],
    steps=[
        'If you sold any investment, gold or property this tax year (or last), fill in the capital gains log for it and calculate the tax.',
        'Estimate your total tax for this tax year using your Tax tab calculator.',
        'Add up the TDS deducted so far (from AIS) and expected for the rest of the year.',
        'If tax after TDS is ₹10,000 or more, fill in the advance tax planner and put the four dates in your calendar.',
        'If you have FD interest and no taxable income, ask your bank for the self-declaration form so TDS isn\'t deducted.',
    ],
    proof='Your capital gains log (or "no sales"), your TDS total from AIS and your advance tax planner or a note that you don\'t need one, saved in 10 Tax.',
    templates=[
        ('capital gains log', """
Asset,Bought on,Sold on,Months held,Cost (₹),Sale value (₹),Gain (₹),Short or long?,Rate,Tax (₹)
D2: =DATEDIF(B2,C2,"M")     G2: =F2-E2
Equity long-term tax (after the ₹1.25 lakh yearly exemption, for all equity gains together):
=MAX(SUM(equity long-term gains)-125000,0)*0.125*1.04
""", ''),
        ('advance tax planner', """
Estimated tax for the year (₹):          B2
TDS expected for the year (₹):           B3
Tax after TDS:                           B4 =B2-B3     Need advance tax? =IF(B4>=10000,"Yes","No")
By 15 June (15%):                        =B4*0.15
By 15 September (45% total):             =B4*0.45
By 15 December (75% total):              =B4*0.75
By 15 March (100%):                      =B4
Paid so far (challan dates and amounts): ____
""", ''),
    ],
    mistakes=[
        ('Selling equity just before 12 months.', 'A few weeks can change the rate from 20% to 12.5% with a ₹1.25 lakh exemption. Check the date.'),
        ('Thinking debt funds still get long-term rates.', 'Units bought from April 2023 are taxed at your slab, however long you hold them.'),
        ('Ignoring advance tax as a freelancer.', 'Interest for late payment adds up. Use your tax reserve and the planner.'),
        ('Not checking AIS for TDS.', 'Missing or wrong TDS entries cost you money unless corrected before filing.'),
    ],
    quiz=[
        {'q': 'You sell equity fund units held 3 years with a ₹2,25,000 gain (no other gains). Tax before cess?', 'o': ['₹12,500', '₹28,125', '₹45,000', '₹0'], 'a': 'A', 'why': '(₹2,25,000 − ₹1,25,000) × 12.5% = ₹12,500.'},
        {'q': 'When are listed equity shares long-term, as of November 2026?', 'o': ['After 12 months', 'After 24 months', 'After 36 months', 'Never'], 'a': 'A', 'why': 'Listed securities and equity-oriented funds: more than 12 months.'},
        {'q': 'Your tax after TDS for the year is ₹8,000. Do you need advance tax?', 'o': ['No; the threshold is ₹10,000', 'Yes, always', 'Only if salaried', 'Only in March'], 'a': 'A', 'why': 'Advance tax applies when tax after TDS is ₹10,000 or more.'},
        {'q': 'By 15 September, how much of your estimated tax should be paid in total?', 'o': ['45%', '15%', '75%', '100%'], 'a': 'A', 'why': '15% by June, 45% by September, 75% by December, 100% by March.'},
    ],
    study='Sections 196, 197 and 198, AMFI\'s tax corner, the advance tax rules and Varsity\'s capital gains chapters',
    action='Log any capital gains, total your TDS from AIS and plan advance tax if you need it',
)

L4 = lesson(
    M, 4,
    title='File your own income tax return, step by step',
    weeks=(21, 21), hours=2,
    outcome='Choose the right return form, walk through the online filing flow on the e-filing portal, and e-verify on time, knowing the due dates and what happens if you are late.',
    split='20 minutes reading, 30 minutes resources, 70 minutes action',
    core=f"""
### Which form?

- **ITR-1 (Sahaj):** for resident individuals with total income up to **₹50 lakh** from salary or pension, up to two house properties, other sources such as interest, agricultural income up to ₹5,000, and long-term gains on listed equity up to ₹1.25 lakh. Not for business or professional income, short-term capital gains, or larger capital gains ({link('itr1-manual', 'ITR-1 user manual')}).
- **Other forms** cover capital gains beyond those limits, business and professional income (including presumptive taxation), and other cases. The portal asks questions and suggests the right form.

Form names and numbers may change for returns under the new Act; follow what the portal shows for your tax year.

### Before you start

- **PAN active and linked to Aadhaar**; a **bank account pre-validated** on the portal for refunds.
- **AIS checked** (FIN-M10-L01), all documents collected (your checklist).
- Your Tax tab result, so you know roughly what the answer should be.

### The online flow (from the ITR-1 user manual)

1. Log in to the e-filing portal: **e-File → Income Tax Returns → File Income Tax Return**.
2. Choose the **assessment/tax year** and **Online** mode, then your filing status (individual).
3. Choose the form (the portal can help you pick).
4. **Regime:** the new regime is the default; to use the old one, you opt out at this step (with business income, the opt-out has its own form and deadline).
5. **Review the pre-filled data**: your details, income, TDS and bank accounts come from your records and AIS. Correct and add what is missing (for example, savings interest).
6. Enter deductions (old regime only) and check the tax computation.
7. **Pay any tax due** through **e-Pay Tax**, then enter the challan details.
8. **Preview, validate and submit.**
9. **e-Verify within 30 days**: by Aadhaar OTP, net banking, a bank or demat account electronic verification code, or a digital signature. If you don't verify (or send the signed ITR-V by post to CPC Bengaluru) within 30 days, the return is treated as **invalid**.

({link('itr1-manual', 'ITR-1 user manual')}, {CHECK}.)

### Due dates and lateness

- **31 July:** individuals without business income and without audit.
- **31 August:** individuals with business or professional income that doesn't need an audit (from Finance Act 2026; AY 2026-27 returns of this type were due 31 August 2026) ({link('etv-itr27', 'ETV Bharat')}).
- **31 October:** cases needing an audit.
- **Late:** a **belated return** can still be filed within 9 months after the end of the tax year, with a late fee of **₹1,000 if total income is up to ₹5 lakh, and ₹5,000 otherwise**; a **revised return** to correct mistakes can be filed within 12 months after the end of the tax year ({link('it-s263', 'section 263')}, {link('fb26-notes', 'Finance Bill 2026 notes')}, {CHECK}).

### After filing

Track the status on the portal: processed, refund issued, or a notice. Read every notice on the portal itself. **Never click links in SMS or emails about "tax refunds"**: they are a common phishing trick (Module 15).
""",
    example=f"""
**Anu** filed her first return in July for the previous year's income of about ₹1,90,000 (tuition fees and interest), to claim back ₹2,840 of TDS.

Her tuition income counted as income from a profession, so ITR-1 wasn't right for her; the portal pointed her to the form for presumptive income (FIN-M10-L05). She followed the same flow: the pre-filled data showed the coaching centre's TDS and her bank interest; she added her home tuition receipts from her log; the tax computed was ₹0; the refund was ₹2,840.

She e-verified with an Aadhaar OTP the same evening. The refund arrived in her pre-validated bank account five weeks later. Total time: about two hours, most of it spent collecting her receipts. "Next year: 40 minutes," she wrote, "because my log already has everything."
""",
    resources=[
        ('itr1-manual', 'The ITR-1 user manual: eligibility, prerequisites, the step-by-step flow and e-verification', '30 minutes'),
        ('it-s263', 'Section 263: due dates, belated and revised returns', '10 minutes'),
        ('fb26-notes', 'Finance Bill 2026 notes on clauses: the 31 August date, revised returns and the late fee (search for "263" and "428")', '15 minutes'),
    ],
    steps=[
        'Log in to the e-filing portal. Check your profile: PAN–Aadhaar link, contact details and a pre-validated bank account (add one if missing).',
        'Find which form fits you this year, using the manual and the portal\'s questions.',
        'If you have income to report for a year whose return is due or still allowed, file it, following the flow, and e-verify the same day.',
        'If you have nothing to file now, do a **dry run**: open the filing flow for the latest year, go through the screens up to the preview without submitting, and note each step.',
        'Put the due date for next year\'s return in your calendar, with a reminder two weeks earlier to check AIS.',
    ],
    proof='Your filing acknowledgement and e-verification confirmation (PAN covered), or your dry-run notes with screenshots of the steps, saved in 10 Tax.',
    templates=[
        ('ITR filing checklist', """
BEFORE
[ ] PAN active, linked to Aadhaar
[ ] Bank account pre-validated for refunds
[ ] AIS/TIS checked; errors reported
[ ] Documents ready (salary TDS certificate, interest certificates, CAS, receipts)
[ ] Regime decided (Tax tab)
DURING
[ ] Correct form and tax year
[ ] Pre-filled data checked line by line; missing income added (savings interest!)
[ ] Tax computed matches my Tax tab roughly
[ ] Tax due paid through e-Pay Tax; challan entered
AFTER
[ ] Submitted on ____ (acknowledgement number saved)
[ ] e-Verified on ____ (within 30 days)
[ ] Status checked after 2-4 weeks; refund received on ____
""", ''),
    ],
    mistakes=[
        ('Forgetting savings account interest.', 'It is taxable income and appears in AIS; add it.'),
        ('Not e-verifying.', 'An unverified return becomes invalid after 30 days. Verify the same day.'),
        ('Filing at the last minute.', 'Portal delays and missing documents cause late fees. File in early July.'),
        ('Clicking "refund" links in messages.', 'Check refunds only on the portal itself.'),
    ],
    quiz=[
        {'q': 'Within how many days must you verify your return after filing?', 'o': ['30 days', '7 days', '120 days', 'There is no limit'], 'a': 'A', 'why': 'Otherwise the return is treated as invalid.'},
        {'q': 'Who can use ITR-1 (Sahaj), per the user manual?', 'o': ['Resident individuals with income up to ₹50 lakh from salary, up to two house properties and other sources', 'Anyone with business income', 'NRIs only', 'Companies'], 'a': 'A', 'why': 'Business income, short-term gains and larger capital gains need other forms.'},
        {'q': 'What is the late fee for a belated return if total income is ₹4 lakh, as of November 2026?', 'o': ['₹1,000', '₹5,000', '₹10,000', 'Nil'], 'a': 'A', 'why': '₹1,000 if total income is up to ₹5 lakh; ₹5,000 otherwise.'},
        {'q': 'Due date for an individual with freelance income who doesn\'t need an audit, from Finance Act 2026?', 'o': ['31 August', '31 July', '31 March', '31 December'], 'a': 'A', 'why': 'The new date for non-audit business and professional cases is 31 August.'},
    ],
    study='The ITR-1 user manual, section 263 and the Finance Bill 2026 notes on due dates and late fees',
    action='File your return and e-verify it, or do a full dry run of the filing flow',
)

FAT_RECEIPTS = 720000

L5 = lesson(
    M, 5,
    title='Freelancers and small businesses: presumptive tax and GST basics',
    weeks=(22, 22), hours=2,
    outcome='Decide whether presumptive taxation fits your freelance or business income, calculate your taxable income under it, and know when GST registration becomes necessary.',
    split='30 minutes reading, 30 minutes resources, 60 minutes action',
    core=f"""
### Business, profession or salary?

Tuition, freelance design, video editing, consulting, a home bakery: these are income from **business or profession**, not salary. You can either keep accounts and pay tax on actual profit (income minus expenses), or, if eligible, use **presumptive taxation**, which deems a fixed share of receipts to be your income, with much simpler records.

### Presumptive taxation (section 58 of the new Act)

({link('it-s58', 'section 58')}, {CHECK})

- **Small businesses** (resident individuals, HUFs and firms other than LLPs) with turnover up to **₹2 crore** (₹3 crore if cash receipts are no more than 5%): deemed profit is **6% of receipts through banking or digital modes plus 8% of other receipts**, or your actual profit if higher.
- **Specified professions** (listed in section 62(4)) with gross receipts up to **₹50 lakh** (₹75 lakh if cash receipts are no more than 5%): deemed income is **50% of receipts**, or actual if higher. Check whether your kind of work is on the list; if not, the business rule may apply.
- You don't need detailed books for the deemed income, but keep invoices and bank records. You can pay all advance tax by **15 March** (FIN-M10-L03).

**Worked example:** Fathima's receipts are {inr(FAT_RECEIPTS)} a year, all by bank transfer.

- If her work counts as a specified profession: deemed income 50% = {inr(FAT_RECEIPTS * 0.5)}.
- If it counts as a business: deemed profit 6% = {inr(FAT_RECEIPTS * 0.06)}.

Either way, her income plus about ₹20,000 of interest is far below ₹12 lakh, so under the new regime her tax is **₹0**. She still files, to claim back TDS her clients deducted and to keep a clean income record. (A tax practitioner helped her decide which rule applies to her work, which is worth paying for once.)

### GST: when do you need it?

GST is charged on most sales of goods and services. You must **register** when your **aggregate turnover** in a year crosses the limit: **₹20 lakh for services** (₹10 lakh in special category states), as per CBIC's registration guidance ({link('cbic-reg', 'CBIC')}, {CHECK}). Registration is online on the GST portal with PAN, email and mobile.

- After the GST Council's decisions effective **22 September 2025**, the main rates are **5%, 18% and 40%** ({link('gst-56', 'GST Council')}, {CHECK}); many professional services are at 18%.
- Once registered, you charge GST on invoices, file regular GST returns and pay the GST collected (after input credits). **GST collected is not your income**: keep it aside in your holding account.
- Selling services to clients **outside India** (like Fathima's Gulf clients) follows special export rules; ask a GST practitioner before your turnover approaches the limit.
- Some situations need registration regardless of turnover. Check the rules for your exact business.

For business bookkeeping, GST invoices and income tax for a small business, the **Practical Entrepreneurship** course covers more (ENT-M08-L01 and ENT-M08-L03).

### Records that protect you

Keep for every payment: invoice number, client, date, amount, TDS deducted, how it was paid. Your holding account statement and invoice register are your proof if the department ever asks.
""",
    example=f"""
**Nisha's Oven**, the home bakery in Kuttiady, sells cakes and snacks worth about ₹9 lakh a year, about 70% through UPI and 30% in cash. Nisha (the owner) compared presumptive and actual-profit taxation:

- **Presumptive (business):** 6% of ₹6,30,000 (digital) + 8% of ₹2,70,000 (cash) = ₹37,800 + ₹21,600 = **₹59,400** deemed profit.
- **Actual profit** from her records: about ₹1,80,000 after ingredients, gas, packaging and a helper's wages.

The presumptive figure is lower than her actual profit, and the rule says "6%/8% **or actual, if higher**", so her income for tax purposes is the higher figure, her actual ₹1,80,000. It is still well below the tax limit, so her tax is ₹0. The value of presumptive taxation for her is simpler records, not lower tax. And with ₹9 lakh of turnover in goods, she is below the GST limits for now; she put a reminder in her review to check when turnover approaches ₹20 lakh, and to confirm the limit for goods in Kerala.
""",
    resources=[
        ('it-s58', 'Section 58: presumptive taxation limits and rates', '15 minutes'),
        ('cbic-reg', 'When GST registration is required and how to register', '10 minutes'),
        ('gst-56', 'The September 2025 GST rate changes', '10 minutes'),
        ('etv-itr27', 'The 31 August due date for business and professional returns (news)', '5 minutes'),
    ],
    steps=[
        'If you have (or expect) freelance, tuition or business income, list last year\'s receipts by month and mode (digital or cash).',
        'Calculate deemed income under the specified-profession rule and the business rule, and compare with your actual profit.',
        'Write which rule you think applies to your work and what to confirm with a tax practitioner.',
        'Add your yearly turnover to a GST watch line: the limit, your current turnover and the month you would cross it at your growth rate.',
        'Set up an invoice register (template) if you don\'t have one.',
        'No freelance income? Do steps 2 and 4 with Fathima\'s or Nisha\'s numbers, and note when you would need this.',
    ],
    proof='Your presumptive-tax comparison, your GST watch line and your invoice register (or the worked practice), saved in 10 Tax.',
    templates=[
        ('presumptive tax comparison', """
B2: receipts by bank/digital (₹)     B3: receipts in cash (₹)     B4: actual profit from records (₹)
Business rule:      B6: =MAX(B2*0.06+B3*0.08,B4)
Profession rule:    B7: =MAX((B2+B3)*0.5,B4)     (only if your profession is listed in section 62(4))
Limits: business turnover up to ₹2 crore (₹3 crore if cash ≤ 5%); professional receipts up to ₹50 lakh (₹75 lakh if cash ≤ 5%)
Cash share:         B9: =IF(B2+B3>0,B3/(B2+B3)*100,0)
""", ''),
        ('invoice register and GST watch', """
Invoice no,Date,Client,Description,Amount (₹),GST charged (₹),TDS deducted (₹),Received on,Mode (bank/UPI/cash)
GST watch: limit ₹2000000 (services; check yours) | turnover this year =SUM(E2:E200) | % of limit =SUM(E2:E200)/2000000*100
""", ''),
    ],
    mistakes=[
        ('Assuming all freelance work is a "specified profession".', 'Check the list in section 62(4). If yours isn\'t on it, the business rule applies.'),
        ('Thinking presumptive tax always lowers tax.', 'It is the deemed amount or actual profit, whichever is higher. Its main benefit is simpler records.'),
        ('Spending GST you collected.', 'It belongs to the government. Keep it separate until you pay it.'),
        ('Crossing the GST limit without noticing.', 'Track turnover monthly with the watch line.'),
    ],
    quiz=[
        {'q': 'Under the business presumptive rule, what is the deemed profit on ₹10 lakh received fully by UPI?', 'o': ['₹60,000 (6%)', '₹80,000 (8%)', '₹5 lakh (50%)', '₹0'], 'a': 'A', 'why': '6% of digital receipts, unless actual profit is higher.'},
        {'q': 'What is the deemed income for a specified profession with ₹8 lakh receipts?', 'o': ['₹4 lakh (50%)', '₹48,000', '₹8 lakh', '₹64,000'], 'a': 'A', 'why': '50% of gross receipts, or actual if higher.'},
        {'q': 'When must a service provider in Kerala register for GST, per CBIC\'s guidance?', 'o': ['When aggregate turnover exceeds ₹20 lakh in a year', 'From the first rupee', 'Only above ₹1 crore', 'Never for freelancers'], 'a': 'A', 'why': '₹20 lakh for services (₹10 lakh in special category states); check current rules and special cases.'},
        {'q': 'What should you do with GST collected from clients?', 'o': ['Keep it aside and pay it to the government', 'Spend it as income', 'Invest it in shares', 'Return it to clients'], 'a': 'A', 'why': 'GST collected is the government\'s money, held by you until you pay it.'},
    ],
    study='Section 58, CBIC\'s GST registration guidance, the September 2025 GST changes and the business due date',
    action='Compare presumptive and actual tax on your freelance or business income and set up a GST watch and invoice register',
)

LESSONS = [L1, L2, L3, L4, L5]

MODULE = module(
    M,
    title='Taxes',
    weeks=(20, 22), hours=12,
    overview="""
Understand income tax under the new Income-tax Act, 2025, choose the right regime with your own numbers, handle capital gains, TDS and advance tax, file your own return, and know the basics of tax and GST for freelancing and small business.

Tax feels frightening mostly because it is unfamiliar. In this module you meet the new law (in force from 1 April 2026), build a calculator that applies both regimes' slabs, rebate, marginal relief and cess, open your Annual Information Statement to see what the department knows, and walk through filing a return step by step.

For a beginner on a modest income, the honest news is good: with the ₹12 lakh rebate in the new regime, many people pay no income tax at all, but filing still matters for TDS refunds and an income record. Freelancers and small business owners get presumptive taxation and the GST threshold explained, with links to the Entrepreneurship course for the business side. Your **tax checklist** is one of the eight parts of your final plan.
""",
    outcomes=[
        'Explain income tax under the Income-tax Act, 2025: heads, slabs, rebate, cess, TDS and AIS',
        'Calculate tax under both regimes with a spreadsheet and choose your regime',
        'Work out capital gains tax and plan advance tax',
        'File and e-verify a return, knowing the due dates and late fees',
        'Apply presumptive taxation and the GST registration threshold to freelance or business income',
    ],
    lessons=LESSONS,
    project='My tax checklist and two-regime calculator',
    project_steps=[
        'Check that your Tax tab has: income by head, the two-regime calculator (tested), and your regime decision for this year.',
        'Complete your tax documents checklist and the ITR filing checklist.',
        'Put the year\'s tax dates in your calendar: advance tax dates (if needed), the return due date and a reminder to check AIS before filing.',
        'If you have freelance or business income, add your presumptive-tax comparison, invoice register and GST watch.',
        'Write a one-paragraph tax plan: "This year I expect tax of ₹__ under the __ regime. TDS covers ₹__. I will pay __ by __, file by __, and keep records in __."',
    ],
    project_proof='Your Tax tab, both checklists, calendar screenshot and one-paragraph tax plan, saved in 10 Tax.',
    rubric=[
        ('Basics', 'Can\'t explain TDS or AIS', 'Knows the terms', 'Checked own AIS and listed income by head'),
        ('Regimes', 'Guesses', 'Compared roughly', 'Calculator built, tested and used for a decision'),
        ('Gains and advance tax', 'Ignored', 'Knows the rates', 'Logged sales, totalled TDS, advance tax planned if needed'),
        ('Filing', 'Never tried', 'Read the steps', 'Filed and e-verified, or completed a full dry run'),
        ('Freelance and GST', 'Not considered', 'Knows the limits', 'Compared presumptive options and set up a GST watch (if relevant)'),
    ],
    short=[
        'Open your AIS and check TDS (FIN-M10-L01).',
        'Run your income through the two-regime calculator (FIN-M10-L02).',
        'Put the return due date and an AIS reminder in your calendar (FIN-M10-L04).',
    ],
    flashcards=[
        ('New Act in force from', '1 April 2026: the Income-tax Act, 2025 replaced the 1961 Act.'),
        ('New regime nil-tax limit with rebate', 'Total income up to ₹12 lakh (₹12.75 lakh salary with the ₹75,000 standard deduction).'),
        ('Section 123 / 126', 'The old 80C (₹1.5 lakh) and 80D (health insurance), old regime only.'),
        ('Equity capital gains', 'Short-term (≤12 months) 20%; long-term 12.5% above ₹1.25 lakh a year.'),
        ('Advance tax dates', '15 June 15%, 15 September 45%, 15 December 75%, 15 March 100%; needed if tax after TDS ≥ ₹10,000.'),
        ('e-Verification', 'Within 30 days of filing, or the return is invalid.'),
        ('Due dates', '31 July (no business income), 31 August (business without audit), 31 October (audit).'),
        ('Presumptive taxation', 'Business: 6% digital + 8% other receipts; specified professions: 50% of receipts (or actual if higher).'),
    ],
    mistakes=[
        ('Avoiding tax because it is confusing.', 'Late filing costs fees and refunds. Start with AIS and the calculator; it gets easier every year.'),
        ('Letting tax decide investments.', 'Invest for goals; choose the regime afterwards by calculation.'),
        ('Trusting messages about refunds or notices.', 'Everything real appears on the e-filing portal when you log in yourself.'),
    ],
    project_week=22,
)
