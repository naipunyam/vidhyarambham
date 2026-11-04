from common import lesson, module, link, rules, xref, table, fence, Q, RULE, ASOF, CHECK

RISKS = [
    ('Legal and title', 'One defect in the mother title affects every plot buyer; heirs\' claims; land type problems', 'Advocate\'s title opinion on the whole parcel before buying'),
    ('Approvals', 'Layout approval, land-type checks, RERA registration above the threshold; delays of months or years', 'Engineer/town planning advice; realistic timeline'),
    ('Infrastructure cost', 'Internal roads, drainage, electricity lines, water and retaining walls cost more than expected', 'Contractor quotes; 20% contingency'),
    ('Lost area', 'Roads, setbacks and open space reduce saleable area by a large share', 'Draft layout before buying'),
    ('Market and time', 'Plots sell slowly in a weak market; interest and holding costs grow', 'Conservative sales pace'),
    ('Money', 'Capital locked; loans for land are hard; partners fall out', 'Written partnership; no borrowed money you can\'t repay'),
    ('Reputation', 'Buyers blame the developer for every delay or defect', 'Honest disclosure; deliver what you promise'),
]

L1 = lesson(
    16, 1,
    outcome='You can explain the steps in plotting and developing land in Kerala (layout approval, land checks, roads and utilities), work out a simple development budget and explain why it is high-risk for beginners.',
    split='25 minutes reading, 50 minutes on a sample feasibility',
    core=f"""
**What plotting is.** Buying a larger parcel (for example 1 acre), dividing it into house plots with an internal road and utilities, getting approvals and selling the plots. Many Kerala investors have tried it; some did well, many got stuck.

**Steps (simplified; every step needs professionals):**
1. **Land due diligence on the whole parcel:** title chain, EC, land type (purayidam, not nilam or data bank land), CRZ and ESA, hazard maps, access (RE-M04, RE-M06).
2. **Feasibility:** a draft layout by an engineer or town planner showing roads, plot sizes, setbacks and any open space required; saleable area; costs; prices.
3. **Approvals:** layout or sub-division approval from the local body (and the town planning office where needed) under the building rules ({link('kpbr', 'KPBR 2019')}); **RERA registration** if the land is above 500 sq m (or other thresholds) before advertising ({link('om-rera', 'Onmanorama')}; {CHECK}); any conversion or land-type permissions (which may be impossible for data bank land; RE-M04-L03).
4. **Infrastructure:** internal road (width as per rules), drainage, retaining walls on slopes, electricity (KSEB line extension), water.
5. **Sales:** honest marketing with the RERA number; agreements and registration for each plot; buyers' due diligence.

**Why it is high-risk:** see the table below. A single title defect or an approval delay can freeze all the money for years. **Do not try this as a beginner or with borrowed money.** Learn it by working as a marketing or sales partner for an established, RERA-registered developer first.

{table(['Risk', 'What can go wrong', 'How professionals reduce it'], RISKS)}
""",
    example="""
**Sample feasibility (fictional, illustrative numbers):** 1 acre (100 cents) near a panchayat road 3 km from Kuttiady, offered at ₹1.2 lakh per cent.
- Land: 100 × 1,20,000 = ₹1,20,00,000. Buying costs (10%): ₹12,00,000.
- Draft layout: internal 5 m road and drainage take about 18 cents; a slope corner of 7 cents is unusable. Saleable: **75 cents** (12 plots of about 6.25 cents).
- Infrastructure (road, drainage, retaining wall, electricity): ₹28,00,000 (quotes) + 20% contingency = ₹33,60,000.
- Approvals, RERA, engineer, advocate, marketing: ₹6,00,000.
- Holding cost (interest or lost FD income, 2 years at 7% on about ₹1.7 crore): ≈ ₹24,00,000.
- **Total cost ≈ ₹1.96 crore** → cost per saleable cent ≈ **₹2.61 lakh**.
- Local plots of 6 cents sell at ₹2.4 to ₹2.8 lakh per cent. Profit at ₹2.8 lakh: 75 × 2,80,000 − 1,95,60,000 = ₹14.4 lakh (about 7% over two years, before tax); at ₹2.4 lakh: a **loss of about ₹16 lakh**.
Conclusion: thin margin, high risk. A professional developer would negotiate the land price down, or walk away.
""",
    calc="""
- Saleable cents: `=total_cents - road_cents - unusable_cents`
- Total cost: `=land + buying_costs + infrastructure*1.2 + approvals + holding`
- Cost per saleable cent: `=total_cost / saleable_cents`
- Profit at price P: `=saleable_cents*P - total_cost`
- Break-even price per cent: `=total_cost / saleable_cents`
""",
    rules_rows=[
        ('RERA for plotted projects', 'Projects above the threshold (reported: more than 500 sq m of land) must register before advertising', 'Onmanorama'),
        ('Building rules', 'Layouts and roads must follow KPBR / KMBR 2019 as amended', 'LSGD PDF'),
        ('Paddy land', 'Data bank land is very hard to convert', 'LiveLaw summary of the 2025 decision'),
    ],
    pro="""
- **Advocate:** title of the whole parcel and plot agreements.
- **Licensed engineer or town planner:** layout and approvals.
- **Surveyor:** measuring and sub-dividing.
- **CA:** tax on plot sales (it may be business income).
""",
    resources=[
        ('kpbr', 'Search the rules for "layout" and "sub-division" to see the main requirements', '20 minutes'),
        ('krera', 'Find one registered plotted project in Kozhikode and read what it lists', '15 minutes'),
        ('om-rera', 'RERA thresholds', '5 minutes'),
    ],
    steps=[
        'Find one plotted layout project (registered on K-RERA, or a local one) and note: total area, number of plots, road width, prices and approvals shown.',
        'Ask a local engineer or broker how long layout approvals take and what usually goes wrong.',
        'Build the feasibility sheet with the formulas and run the sample, then change land price, sale price and timeline to see how profit moves.',
        'Write a half-page "why I won\'t do plotting yet, and what I\'d need first".',
    ],
    proof='Project notes, the professional\'s answers, the feasibility sheet with three scenarios and your half-page.',
    templates=[('Plotting feasibility sheet', """PLOTTING FEASIBILITY (tab "Plotting")   illustrative; professionals must check
B1 Total cents            B2 Land price per cent      B3 Land cost =B1*B2
B4 Buying costs (10%)     =B3*0.10
B5 Road and drainage cents   B6 Unusable cents        B7 Saleable cents =B1-B5-B6
B8 Infrastructure quotes  B9 With 20% contingency =B8*1.2
B10 Approvals, RERA, professionals, marketing
B11 Holding cost =(B3+B4+B9+B10)*rate*years
B12 TOTAL COST =B3+B4+B9+B10+B11
B13 Break-even per cent =B12/B7
B14 Expected sale per cent (from comps)   B15 Profit =B7*B14-B12   B16 Margin =B15/B12
Scenarios: sale price -15% | base | +10% ; timeline 1 / 2 / 4 years""")],
    mistakes=[
        ('Counting all land as saleable.', 'Roads, slopes and setbacks take a big share.'),
        ('Ignoring holding costs.', 'Two years of interest or lost income is large.'),
        ('Advertising before RERA registration.', 'Register first if required.'),
    ],
    fraud="""
**Unapproved layouts.** Plots sold without layout approval, on nilam or with only a "private road" are a common trap: buyers can't get permits or loans. Check approvals and RERA registration before any plot purchase, and warn clients.
""",
    quiz=[
        Q('Why is plotting high-risk for beginners?', 'Title, approvals, infrastructure, slow sales and locked money', 'It is always profitable', 'It needs no approvals', 'Plots sell in a day', why='Many things can go wrong.'),
        Q('In the sample, why was saleable area only 75 cents?', 'Roads, drainage and an unusable slope took 25 cents', 'The seller kept some', 'RERA took it', 'It was a typo', why='Draft the layout first.'),
        Q('What must happen before advertising a plotted project above the threshold?', 'RERA registration', 'Nothing', 'A token from buyers', 'A WhatsApp post', why='RERA rules.'),
        Q('What is the safest way to learn plotting?', 'Work with an established, registered developer first', 'Buy 5 acres with a loan', 'Borrow from friends', 'Skip due diligence', why='Learn before risking capital.'),
    ],
    study='read the lesson and the risk table',
    action='study a real plotted project and run a feasibility sheet with three scenarios',
)

LESSONS = [L1]

MODULE = module(
    16,
    overview=f"""
Plotting and development basics: land checks for the whole parcel, layouts and approvals, RERA, roads and utilities, a simple feasibility budget and an honest look at why development is high-risk.

This is a **later-stage** path that needs large capital, a professional team and experience. The goal now is to understand it well enough to warn clients, judge plotted projects and maybe work as a marketing partner. Everything is {RULE}.
""",
    outcomes=[
        'Explain the steps and approvals for plotting.',
        'Build a feasibility sheet with scenarios.',
        'Explain the main risks and how professionals reduce them.',
        'Spot unapproved layouts.',
    ],
    lessons=LESSONS,
    project='a plotting feasibility study',
    project_steps=[
        'Run the feasibility sheet for the sample or a real (public) parcel.',
        'Test three scenarios.',
        'Write a one-page conclusion with the risks.',
    ],
    project_proof='The sheet and the one-page conclusion.',
    rubric=[
        ('Steps', 'Unclear', 'Main steps known', 'Steps with approvals and professionals'),
        ('Numbers', 'Land and price only', 'Most costs', 'All costs, holding cost and scenarios'),
        ('Risk', 'Ignored', 'Listed', 'Listed with mitigations and an honest conclusion'),
    ],
    short=[
        'Read the risk table.',
        'Run the sample feasibility once.',
    ],
    flashcards=[
        ('Saleable area', 'Total minus roads, drainage and unusable land.'),
        ('Break-even per cent', 'Total cost ÷ saleable cents.'),
        ('RERA for plots', 'Register above the threshold before advertising.'),
        ('Biggest single risk', 'A defect in the mother title.'),
        ('Unapproved layout risk', 'No permits or loans for buyers.'),
    ],
    mistakes=[
        ('Starting with development.', 'Start with services; develop later, if ever.'),
        ('Optimistic sales prices.', 'Use comparables and a downside case.'),
        ('Informal partnerships.', 'Written agreements with an advocate.'),
    ],
    tools=[
        'Plotting feasibility sheet (RE-M16-L01).',
    ],
    toolkit=[
        'Plotting feasibility sheet with scenarios.',
    ],
)
