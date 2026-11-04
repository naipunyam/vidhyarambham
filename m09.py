from common import lesson, module, link, rules, xref, table, fence, Q, RULE, ASOF, CHECK

TAXNOTE = f'**Not tax advice.** The Income-tax Act, 2025 replaced the 1961 Act from 1 April 2026 and renumbered most sections. This lesson describes rules by what they do, giving old and new section numbers only where a source was checked. A **chartered accountant (CA)** must advise on any real case. Everything is {RULE}.'

CG = [
    ('Holding period for land and buildings', 'More than 24 months = long-term; otherwise short-term', 'Patron Accounting'),
    ('Long-term capital gains (LTCG) rate', '12.5% without indexation (from 23 July 2024)', 'Housing.com'),
    ('Choice for older property', 'Resident individuals and HUFs who bought before 23 July 2024 can choose 20% with indexation instead', 'Housing.com'),
    ('Short-term gains', 'Added to income and taxed at slab rates', 'General rule; check with a CA'),
    ('Reinvest in a house (old s.54, s.54F; s.54F is s.86 in the 2025 Act)', 'Buy a house 1 year before or 2 years after, or build within 3 years; exemption capped at ₹10 crore', 'Patron Accounting; Taxscan'),
    ('Specified bonds (old s.54EC)', 'Invest gains from land or building within 6 months; up to ₹50 lakh a year; 5-year lock-in', 'Patron Accounting'),
]

L1 = lesson(
    9, 1,
    outcome='You can explain TDS on property purchases, how capital gains on property are taxed, and the main exemptions, and work through a simple example.',
    split='25 minutes reading, 30 minutes on the worked example and action task',
    core=f"""
{TAXNOTE}

**TDS on buying property.** When the value of immovable property (other than agricultural land) is **₹50 lakh or more**, the **buyer** must deduct **1%** of the higher of the price or the stamp duty value as TDS, pay it to the government and give the seller a certificate. No TAN is needed; the buyer pays online with the seller's PAN ({link('it-tds', 'Income Tax Department')}). Under the 2025 Act this is reported as section 393 and the form as Form 141 (earlier Form 26QB) ({link('tg-tds2025', 'TaxGuru')}). If the seller is an **NRI**, much higher TDS rules apply and the buyer needs a TAN: always involve a CA.

TDS is **part of the price**, not an extra cost: on a ₹60 lakh house, the buyer pays ₹59.4 lakh to the seller and ₹60,000 to the government.

**Reporting.** Registration offices report property purchases above a threshold to the tax department (reported as ₹45 lakh from FY 2026-27, {link('taxscan-sft', 'Taxscan')}). Undervalued deeds and cash deals are easily caught.

**Capital gains on selling property:**
{table(['Rule', 'What it means', 'Source'], CG)}

**How the gain is worked out (basic):** sale price (or stamp duty value, if higher) − selling costs (brokerage, legal) − cost of purchase (price plus stamp duty and registration paid) − cost of improvements = **capital gain**. With indexation (where chosen), the cost is raised using the government's cost inflation index.

**Inherited property:** the cost and holding period of the previous owner are generally used. Ask a CA.

**Agricultural land** in rural areas (outside specified distances from municipalities) is not a capital asset for tax; whether a Kerala village qualifies depends on population and distance rules; {CHECK} with a CA.

The {xref('fin', 'fin-m10-l03', 'Personal Finance lesson on capital gains, TDS and advance tax')} covers the general rules.
""",
    example="""
**Selling a plot bought in 2018** (illustrative; ask a CA in a real case):
- Bought for ₹10 lakh in 2018; paid stamp duty and fee ₹1 lakh. Cost = ₹11 lakh.
- Sold in 2026 for ₹18 lakh; brokerage 2% = ₹36,000.
- Gain without indexation: 18,00,000 − 36,000 − 11,00,000 = **₹6,64,000**.
- Tax at 12.5% (plus cess): about **₹83,000** before cess.
- The seller, a resident individual who bought before 23 July 2024, can compare this with the 20%-with-indexation option and choose the lower tax.
- If the seller buys a house within the time limits, an exemption may apply (old section 54F for non-house assets, now section 86, if conditions are met).

Value was below ₹50 lakh, so the buyer did not deduct TDS.
""",
    calc="""
**TDS in Sheets:** `=IF(MAX(B1,B2)>=5000000, MAX(B1,B2)*0.01, 0)` (B1 price, B2 stamp duty value).
**Simple LTCG (no indexation):** `=(sale - selling_costs - purchase_cost - improvements)*0.125`.
Add cess and compare the indexed option with a CA.
""",
    rules_rows=[
        ('TDS on purchase', '1% if ₹50 lakh or more; buyer deducts; no TAN for resident sellers', 'Income Tax Department'),
        ('TDS under the 2025 Act', 'Reported as section 393, Form 141 (was Form 26QB)', 'TaxGuru'),
        ('LTCG', '12.5% without indexation; 20% with indexation option for property bought before 23 July 2024', 'Housing.com'),
        ('House reinvestment exemption', 'Capped at ₹10 crore; time limits apply', 'Patron Accounting, April 2026'),
    ],
    pro="""
- **Chartered accountant:** every capital gains calculation, exemptions, NRI sellers, inherited property and agricultural land status.
""",
    resources=[
        ('it-tds', 'Read the official TDS on property page', '10 minutes'),
        ('tg-tds2025', 'Read how TDS works under the 2025 Act', '10 minutes'),
        ('hc-ltcg', 'Read the LTCG options', '10 minutes'),
        ('pa-cg', 'Read the exemption conditions', '15 minutes'),
    ],
    steps=[
        'Add TDS and simple LTCG formulas to your Cost tab.',
        'Work through the example above with a property price from your Comps sheet.',
        'Ask one CA (or a tax practitioner) the three questions sellers most often get wrong about capital gains, and note their answers.',
        'Write a "tax questions to ask your CA" sheet for clients.',
    ],
    proof='The formulas, one worked example and notes from the CA conversation, plus your client sheet.',
    templates=[('Tax questions for buyers and sellers', """TAX QUESTIONS TO TAKE TO A CA (date ______; rules change)
BUYER
1 Is the value ₹50 lakh or more? -> TDS 1%; who files the form and when?
2 Is the seller an NRI? -> different TDS; TAN needed; CA must handle.
3 Any GST? (under-construction property from a builder)
SELLER
1 Bought when? held more than 24 months? cost including stamp duty?
2 LTCG at 12.5%, or 20% with indexation (bought before 23 July 2024)?
3 Planning to buy a house or bonds? time limits and caps?
4 Inherited? previous owner's cost and date?
5 Agricultural land: is it a capital asset in this village?""")],
    mistakes=[
        ('Treating TDS as an extra cost.', 'It is part of the price.'),
        ('Forgetting stamp duty in the cost of purchase.', 'It is part of the cost.'),
        ('Giving clients tax advice.', 'Explain the basics and send them to a CA.'),
    ],
    fraud="""
**"Show a lower price to save capital gains tax."** This is tax evasion. It also means the buyer\'s future cost is understated, so the buyer pays more tax later. Reporting systems catch many such deals.
""",
    quiz=[
        Q('Who deducts TDS on a property purchase of ₹50 lakh or more?', 'The buyer', 'The seller', 'The broker', 'The SRO', why='1% of the higher of price or stamp duty value.'),
        Q('What is the LTCG rate on property without indexation?', '12.5%', '1%', '30%', '0%', why='From 23 July 2024.'),
        Q('How long must land be held for gains to be long-term?', 'More than 24 months', '6 months', '10 years', '1 day', why='For land and buildings.'),
        Q('Is TDS an extra cost to the buyer?', 'No, it is part of the price paid to the government for the seller', 'Yes', 'Only for NRIs', 'Only for flats', why='The buyer pays less to the seller.'),
    ],
    study='read the lesson and the capital gains table',
    action='add TDS and LTCG formulas, work one example and talk to a CA',
)

L2 = lesson(
    9, 2,
    outcome='You can explain how rental income and brokerage income are taxed, when GST applies to property and to brokerage, and what records to keep.',
    split='20 minutes reading, 30 minutes on your own tax plan',
    core=f"""
{TAXNOTE}

**Tax on rental income (for your clients and your future self).**
- Rent from a house or shop is taxed as **income from house property**.
- From the annual rent, the owner deducts **municipal (building) taxes paid**, then a flat **30% standard deduction** for repairs; the new Act keeps this, applied after municipal taxes ({link('bt-hp', 'Business Today')}). Interest on a loan for a let-out property can also be deducted (subject to limits and the regime chosen).
- Large rents paid by tenants may require the tenant to deduct TDS; ask a CA about current thresholds.

**Example:** annual rent ₹1,44,000; building tax ₹4,000; net annual value ₹1,40,000; 30% deduction ₹42,000; income from house property **₹98,000** (before loan interest), added to other income and taxed at slab rates.

**Tax on your brokerage or service income.**
- Commission from brokerage, property management or NRI property care is **business or professional income**, taxed at slab rates after allowable expenses (phone, travel, marketing). Keep receipts.
- Presumptive tax schemes may not apply to commission or brokerage income; ask a CA before using one (see the {xref('fin', 'fin-m10-l05', 'Personal Finance lesson on freelancers and small businesses')}).
- Builders or companies paying you commission may deduct TDS; it shows in your tax statement and you claim credit when filing.

**GST.**
- **Under-construction property** from a builder: GST **5%** on residential units (without input tax credit), **1%** on affordable housing (up to ₹45 lakh and up to 60 sq m carpet area in metros or 90 sq m elsewhere) ({link('bf-gst', 'Bajaj Finserv')}; {CHECK}).
- **No GST** on completed property with an occupancy or completion certificate, or on resale between owners, or on land sales.
- **Brokerage and real estate services:** GST **18%**. GST registration is required once your turnover from services exceeds **₹20 lakh** a year (lower thresholds apply in some states; Kerala uses ₹20 lakh), or earlier if you choose to register ({link('rp-gst', 'Razorpay')}). See also the {xref('ent', 'ent-m08-l03', 'Entrepreneurship lesson on GST and income tax')}.

**Records to keep:** every invoice and receipt, bank statements, mandates and agreements, a simple income and expense sheet (RE-M20-L01).
""",
    example="""
**Sachin's first year (illustrative):** commission from 6 rental deals (one month's rent each, average ₹9,000) = ₹54,000; 2 land sales at 2% of ₹15 lakh = ₹60,000; NRI property care for 3 owners at ₹1,500 a month = ₹54,000. Total ₹1,68,000.
- Expenses: phone and data ₹6,000, travel ₹18,000, printing and portal fees ₹4,000 = ₹28,000.
- Net professional income: **₹1,40,000**, added to any other income. With no other income, under the new regime this is likely below the taxable limit, but he still files a return to build a record (ask a CA).
- Turnover ₹1.68 lakh, far below ₹20 lakh, so GST registration is not required; he does not charge GST.
""",
    rules_rows=[
        ('House property deduction', '30% standard deduction after municipal taxes, kept in the 2025 Act', 'Business Today'),
        ('GST on under-construction homes', '5% (1% affordable); no GST on completed or resale property', 'Bajaj Finserv, July 2026'),
        ('GST on brokerage', '18%; registration above ₹20 lakh turnover', 'Razorpay'),
    ],
    pro="""
- **Chartered accountant:** your own returns, whether to register for GST, TDS by tenants and any client\'s rental tax.
""",
    resources=[
        ('bt-hp', 'Read the house property rules', '10 minutes'),
        ('bf-gst', 'Read the GST rates on housing', '10 minutes'),
        ('rp-gst', 'Read GST on brokerage and commission', '10 minutes'),
    ],
    steps=[
        'Work out the house property income for one rented property from your ROI tab.',
        'Estimate your own first-year service income and expenses, as in the example, in an "Income" tab.',
        'Check whether you would need GST registration.',
        'Ask a CA (or tax practitioner) what records they want from a small broker each year, and note their answer.',
    ],
    proof='The house property calculation, your income estimate and the CA\'s records list.',
    templates=[('Income and tax tracker', """INCOME AND TAX TRACKER (tab "Income")   Financial year ______
Date | Client | Deal | Invoice no. | Amount ₹ | Received by (UPI/bank) | TDS deducted? | Notes
EXPENSES: Date | Item | Amount | Receipt saved?
Totals: income =SUM(E:E)  expenses =SUM(...)  net =income-expenses
GST check: turnover this year =SUM(E:E); register if near ₹20 lakh (ask a CA)
Rental income (client or own): rent ______ - building tax ______ = NAV ______ ; 30% ______ ; taxable ______""")],
    mistakes=[
        ('Charging GST without registration.', 'Only registered persons can collect GST.'),
        ('Mixing personal and business money.', 'Use a separate account for business income.'),
        ('Not keeping receipts.', 'Expenses without receipts are hard to claim.'),
    ],
    fraud="""
**Fake GST invoices.** Some people offer "GST bills" for a fee without real services. Using or issuing fake invoices is a serious offence. Issue invoices only for real services.
""",
    quiz=[
        Q('What deduction is allowed from rental income after municipal taxes?', 'A flat 30% standard deduction', '50%', 'Nothing', '100%', why='Kept in the 2025 Act.'),
        Q('What GST applies to resale of a completed house between owners?', 'None', '18%', '5%', '12%', why='GST applies to under-construction units from builders.'),
        Q('What GST rate applies to brokerage services?', '18%', '1%', '5%', '0%', why='Once registered.'),
        Q('When must a broker register for GST (services)?', 'When turnover exceeds ₹20 lakh a year (or voluntarily)', 'From the first deal', 'Never', 'Only for NRIs', why='Check current thresholds.'),
    ],
    study='read the lesson and the GST rules',
    action='work out rental income tax for one property and your own first-year income and GST position',
)

LESSONS = [L1, L2]

MODULE = module(
    9,
    overview=f"""
Property taxes: TDS on purchase, capital gains and exemptions, tax on rental income, tax on brokerage income, and GST on under-construction property and on brokerage services.

The Income-tax Act, 2025 took effect on 1 April 2026 and renumbered most sections, so this module describes rules by what they do. You will learn enough to warn clients and plan your own taxes, and always send real cases to a CA. Everything is {RULE}.
""",
    outcomes=[
        'Explain TDS on property purchases.',
        'Work through a basic capital gains example and name the exemptions.',
        'Explain tax on rent and on your own service income.',
        'Explain when GST applies to property and brokerage.',
    ],
    lessons=LESSONS,
    project='a tax cheat sheet for clients and a tax plan for your business',
    project_steps=[
        'Combine the TDS, capital gains, rental and GST rules into a one-page cheat sheet, each with its source and date.',
        'Add your "tax questions to ask your CA" list.',
        'Set up the Income tab and estimate your first-year tax position.',
        'Have a CA check the cheat sheet for errors, if they agree.',
    ],
    project_proof='The cheat sheet with sources and dates, and the Income tab.',
    rubric=[
        ('TDS', 'Unknown', 'Knows the 1% rule', 'Explains threshold, who deducts and the NRI exception'),
        ('Capital gains', 'Unknown', 'Knows the rate', 'Works an example and names exemptions with limits'),
        ('Rent and brokerage', 'Unknown', 'Knows they are taxed', 'Calculates house property income and own income'),
        ('GST', 'Confused', 'Knows the 18% rate', 'Explains when GST applies and the registration threshold'),
    ],
    short=[
        'Learn the TDS and LTCG rules.',
        'Learn when GST applies.',
    ],
    flashcards=[
        ('TDS on purchase', '1% if ₹50 lakh or more; buyer deducts.'),
        ('TDS form under the 2025 Act', 'Form 141 (was 26QB); section 393 (reported).'),
        ('LTCG on property', '12.5% without indexation.'),
        ('Long-term holding', 'More than 24 months.'),
        ('House reinvestment exemption cap', '₹10 crore.'),
        ('House property deduction', '30% after municipal taxes.'),
        ('GST on resale homes', 'None.'),
        ('GST on brokerage', '18%; register above ₹20 lakh.'),
    ],
    mistakes=[
        ('Using old section numbers without checking.', 'The 2025 Act renumbered them.'),
        ('Advising on tax.', 'Send clients to a CA.'),
        ('Ignoring your own taxes.', 'Track income and expenses from day 1.'),
    ],
    tools=[
        'TDS and LTCG formulas (RE-M09-L01).',
        'Tax questions for buyers and sellers (RE-M09-L01).',
        'Income and tax tracker (RE-M09-L02).',
    ],
    toolkit=[
        'Tax cheat sheet with sources and dates.',
        'Income tab for your business.',
    ],
)
