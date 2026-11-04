from common import lesson, module, link, rules, xref, table, fence, Q, RULE

PATHS = [
    ('Broker / agent (sales)', 'Very low (phone, travel, K-RERA fee if required)', 'Local knowledge, networking, negotiation, documents', 'Irregular income; deals fall through; legal exposure if careless', '3–12 months to first sale'),
    ('Rental broker', 'Very low', 'Tenant screening, agreements, quick follow-up', 'Small fees; tenant problems', 'Weeks'),
    ('Property management', 'Low', 'Reliability, maintenance contacts, accounts', 'Owner and tenant disputes; money handling', '1–3 months'),
    ('NRI property care', 'Low', 'Trust, reporting, office work, maintenance', 'Responsibility for others\' assets; misuse of authority', '1–3 months'),
    ('Real estate marketing / content', 'Low (phone, free tools)', 'Photography, video, copywriting, social media', 'Clients delay payment; competition', 'Weeks'),
    ('Consulting (due-diligence coordination, valuation help)', 'Low', 'Deep knowledge plus professional network', 'Must not cross into licensed legal or valuation work', '6–12 months'),
    ('Plotting and development', 'Very high', 'Land law, approvals, construction, finance', 'Approvals fail, money stuck, legal liability', 'Years'),
    ('Buy-and-hold rentals', 'High (down payment, loan)', 'Analysis, tenant management', 'Low yields, vacancies, illiquidity, repairs', 'Years'),
    ('Flipping', 'High', 'Buying below market, renovation, fast resale', 'Transaction costs (about 10%+), slow resale, taxes', '6–24 months per deal'),
    ('Land banking', 'High', 'Patience, legal checks', 'Money locked for years; prices may not rise; encroachment', 'Years'),
]

L1 = lesson(
    2, 1,
    outcome='You can compare the low-capital real estate paths (brokerage, rentals, property management, NRI property care, marketing) by money, skills, risk and time to first income, and pick one or two to start.',
    split='15 minutes reading, 40 minutes of research and planning',
    core=f"""
With little capital, you earn in real estate by **providing services**, not by owning property. Five low-capital paths suit a beginner in Kerala:

**1. Sales brokerage.** You help owners sell and buyers buy, for a commission. Income per deal can be large, but deals are slow and many fail. You need a written mandate from the owner (RE-M10-L02), K-RERA registration where the law requires it (RE-M10-L01), and strong honesty, because buyers rely on what you say.

**2. Rental brokerage.** You find tenants for owners (or homes for tenants) for a fee, often a portion of one month's rent (local norms vary). Rentals move faster than sales and teach you the whole process: listing, visits, screening, agreements.

**3. Property management.** You manage rented properties for owners: rent collection, repairs, tenant issues, statements. Income is small but recurring (a percentage of rent or a fixed monthly fee).

**4. NRI property care.** Many Kerala homes are owned by people working abroad. They need someone trustworthy to visit, photograph, pay taxes and bills, arrange repairs, deal with tenants, and collect documents from offices. This is one of the best fits for a reliable beginner in Malabar (RE-M15-L02).

**5. Real estate marketing and content.** Owners and brokers need good photos, walkthrough videos, listing copy and social posts. If you build skill here (Module 12), you can serve many brokers and builders without handling transactions. The {xref('smm', 'smm-m11', 'Social Media Marketing course module on local business')} covers the marketing side in depth.

**Consulting** (coordinating due diligence, helping buyers compare properties) becomes possible later, once you have deep knowledge and a network of advocates and surveyors. Be careful never to present yourself as giving legal opinions or formal valuations.

**How to choose:** list your strengths (trust in your community, photography, follow-up, office work), your time (5 to 7 hours a week now), your network (NRI families? landlords?), and the local demand you found in Module 1. Many people combine two paths, for example rental brokerage plus NRI property care.
""",
    example="""
Sachin has five to seven hours a week, a phone, a motorbike and many relatives with family members in the Gulf. His options:

- **Rental brokerage** around Kuttiady: teachers and government staff are often posted to the area and need small houses; migrant workers need rooms. Owners often don't want the hassle of finding tenants.
- **NRI property care:** at least six families he knows have houses that stay empty or are rented informally while the owners work abroad. They worry about leaks, encroachment, unpaid taxes and tenants not paying.
- **Sales brokerage:** slower, needs more knowledge first.

He chooses rental brokerage plus NRI property care for the first six months, while studying the sales side. His first step is a written service menu (RE-M15-L02) and two conversations with NRI families during their next visit home.
""",
    resources=[
        ('krera', 'Read the agent registration section headings to see what registration involves', '10 minutes'),
        ('nobroker', 'Study how rental listings are presented and what owners must provide', '15 minutes'),
    ],
    steps=[
        'Score each of the five low-capital paths 1–5 on: fits my time, fits my skills, local demand, my network, and risk (5 = low risk).',
        'Talk to one owner (a landlord or an NRI family) and ask: "What is your biggest headache with your property?" Write the answer word for word.',
        'Choose one or two paths and write a one-paragraph reason.',
        'Write the first three concrete steps for your chosen path (for example: make a service menu, talk to five NRI families, list one rental).',
    ],
    proof='Your scored comparison of the five paths, the owner\'s answer, your chosen path with reasons and three next steps.',
    templates=[('Path chooser', """PATH CHOOSER (score 1-5)       Time  Skills  Demand  Network  Risk(5=low)  Total
Sales brokerage                 __     __      __      __       __          __
Rental brokerage                __     __      __      __       __          __
Property management             __     __      __      __       __          __
NRI property care               __     __      __      __       __          __
Marketing / content             __     __      __      __       __          __
Owner's biggest headache (quote): "______________________"
My path(s): ______  Why: ______
First three steps: 1 ______ 2 ______ 3 ______""")],
    mistakes=[
        ('Starting with investing because it sounds bigger.', 'With little capital, services build income, knowledge and a network first.'),
        ('Trying every path at once.', 'Pick one or two; do them well.'),
        ('Underestimating trust.', 'NRI care and property management are trust businesses; one mistake with money ends them.'),
    ],
    fraud="""
**"Join our network, pay ₹10,000 to become a franchise broker."** Some schemes sell "real estate agent franchises" or "training with guaranteed leads". You don't need to pay anyone to start a legal service business; check any such offer with the red-flag check from the Mind, Body and People course (PD-M32-L01 there) and never pay for "guaranteed" income.
""",
    quiz=[
        Q('Why do low-capital paths suit a beginner?', 'They earn from services, so you don\'t need money to buy property', 'They always pay the most', 'They need no knowledge', 'They are risk-free', why='Services build income, skill and network before investing.'),
        Q('Which path gives small but recurring income?', 'Property management', 'One-off land sale brokerage', 'Flipping', 'Land banking', why='Management fees recur monthly.'),
        Q('What must a broker never do?', 'Give legal title opinions or draft deeds without the required licence', 'Arrange site visits', 'Take a written mandate', 'Market a property honestly', why='That work belongs to advocates and licensed document writers.'),
        Q('Why is NRI property care a good fit in Malabar?', 'Many homes are owned by families working abroad who need trustworthy local help', 'NRIs never visit', 'It needs a large investment', 'It requires a law degree', why='Demand plus low capital needs.'),
    ],
    study='read the lesson and the path table',
    action='score the five low-capital paths, talk to one owner and choose your path with three next steps',
)

L2 = lesson(
    2, 2,
    outcome='You can explain the capital, skills and risks of plotting, buy-and-hold investing, flipping and land banking, with honest numbers, and decide when (if ever) to move into them.',
    split='15 minutes reading, 35 minutes of calculation and notes',
    core=f"""
**Capital-heavy paths** involve buying property with your own money and usually loans. They can build wealth, but they also lose people money regularly. Here is the full comparison of all paths:

{table(['Path', 'Capital needed', 'Key skills', 'Main risks', 'Time to income'], PATHS)}

**Why small investors lose money in property:**
1. **Bad title or illegal land** (data bank paddy land, encroached land, unapproved layouts, disputed inheritance): the property can't be sold, built on or financed.
2. **Transaction costs:** in Kerala, buying costs roughly 10% or more on top of the price (8% stamp duty, 2% registration fee on the higher of price or fair value, plus document, legal and brokerage fees, RE-M04-L01). A flip must beat that before any profit.
3. **Illiquidity:** land in interior areas can take a year or more to sell, at a lower price than hoped.
4. **Low rental yields:** houses in Kerala often rent for well under 3% to 4% of their price a year, often less than a fixed deposit, before repairs and vacancies (RE-M08-L02).
5. **Over-borrowing:** EMIs continue even when tenants leave or prices fall.
6. **Disputes:** boundary, access-road and family disputes can take years in court.

**When to consider them:** after you have (a) an emergency fund and no high-interest debt (see {xref('fin', 'fin-m05', 'Personal Finance, emergency fund')}), (b) a few years of service experience and a trusted advocate and surveyor, (c) a full analysis showing returns after all costs, taxes and risks (Module 18), and (d) money you can leave locked for years. For many people, low-cost listed REITs are a simpler way to get property exposure (RE-M18-L02).
""",
    example="""
Sachin's cousin Rasheed wants to "flip" a 10-cent plot: buy at ₹18 lakh and sell within a year at ₹21 lakh.

Rough costs: stamp duty and registration on ₹18 lakh at 10% (assuming the fair value is not higher): ₹1.8 lakh; document writer, EC and other fees: about ₹25,000; brokerage at 1% on purchase: ₹18,000; brokerage at 1% on sale: ₹21,000. Total costs: about ₹2.44 lakh. Profit before tax: ₹21 lakh − ₹18 lakh − ₹2.44 lakh = **about ₹56,000**, about 3% on ₹18 lakh, before short-term capital gains tax, and only if he sells at ₹21 lakh within the year. If it takes two years to sell at ₹20 lakh, he loses money. Rasheed decides to keep his savings in his emergency fund and help with Sachin's rental work instead.
""",
    calc="""
**Break-even price for a flip:**
- Purchase price P = ₹18,00,000
- Purchase costs (stamp duty 8% + registration 2% + fees + brokerage) ≈ 10% + ₹25,000 + 1% ≈ ₹2,23,000
- Sale costs (brokerage 1%) ≈ ₹21,000 at the target price
- Break-even sale price ≈ P + purchase costs + sale costs ≈ **₹20,44,000**, roughly 13.6% above the purchase price, before tax and holding costs (interest you could have earned, land tax, maintenance).
- In Google Sheets: `=B1*1.11+25000+B2*0.01` where B1 is the purchase price and B2 the target sale price (rates as of November 2026; check current rules).
""",
    resources=[
        ('sy-stamp', 'Read the stamp duty and registration table to confirm the 8% + 2% used in the example', '10 minutes'),
        ('mit-re', 'Optional: skim the syllabus to see how professionals think about real estate investment', '15 minutes'),
        ('week-reit', 'Read how small investors can buy REIT units (more in RE-M18-L02)', '5 minutes'),
    ],
    steps=[
        'Find one real land listing in your area. Calculate the purchase costs and the break-even resale price using the calculation above.',
        'Ask one person who has bought land as an investment: "How long did it take to sell, and at what price compared with what you hoped?" Note the answer.',
        'Write your rule for when you would consider a capital-heavy path (savings, experience, analysis, time).',
        'Add your chosen low-capital path and your "later" rule to your toolkit folder.',
    ],
    proof='One break-even calculation on a real listing, notes from one investor conversation and your written rule.',
    templates=[('Flip break-even calculator', """FLIP BREAK-EVEN (rates as of November 2026; check current rules)
B1 Purchase price (Rs)                     [type]
B2 Fair value (Rs)                         [type]
B3 Duty base                               =MAX(B1,B2)
B4 Stamp duty + registration (10%)         =B3*0.10
B5 Fees (document writer, EC, misc.)       [type]
B6 Brokerage on purchase                   =B1*[rate]
B7 Target sale price                       [type]
B8 Brokerage on sale                       =B7*[rate]
B9 Holding costs (interest lost, taxes, maintenance) [type]
B10 Break-even sale price                  =B1+B4+B5+B6+B8+B9
B11 Profit before tax at target price      =B7-B10""")],
    mistakes=[
        ('Ignoring transaction costs.', 'About 10% or more goes to costs on purchase; a flip must clear that first.'),
        ('Counting the asking price as profit.', 'Use realistic sale prices and times from real deals.'),
        ('Using emergency money or loans for land speculation.', 'Money locked in illiquid land can\'t help you in an emergency.'),
    ],
    fraud="""
**"Guaranteed doubling" land and plot schemes.** Ads promising that a plot will double in value in two or three years, often in "upcoming" layouts far from town, are a classic trap. Unapproved layouts may never get permits or roads (RE-M16-L01). No one can guarantee property returns.
""",
    quiz=[
        Q('About how much do stamp duty and registration add to a Kerala sale deed, as of November 2026?', 'About 10% (8% + 2%) of the higher of price or fair value', 'About 1%', 'About 25%', 'Nothing', why='Plus document, legal and brokerage costs; check current rules.'),
        Q('Why do many small property investors lose money?', 'Bad titles, high transaction costs, illiquidity, low yields and over-borrowing', 'Property always rises', 'Taxes are zero', 'Banks pay their EMIs', why='These risks are common and often ignored.'),
        Q('What should you have before investing in property?', 'An emergency fund, no high-interest debt, experience, a full analysis and money you can lock away', 'A tip from a friend', 'A credit card', 'A guaranteed-return scheme', why='Investing comes after financial safety and skill.'),
        Q('A flip bought at ₹18 lakh needs roughly what sale price to break even?', 'About ₹20.4 lakh after costs', '₹18 lakh', '₹18.5 lakh', '₹30 lakh', why='Purchase and sale costs add roughly 13.6%.'),
    ],
    study='read the lesson and the path comparison table',
    action='calculate the break-even resale price for one real listing and write your rule for capital-heavy paths',
)

LESSONS = [L1, L2]

MODULE = module(
    2,
    overview=f"""
Business paths in real estate: brokerage, rental brokerage, property management, NRI property care, marketing and consulting (low capital), and plotting, buy-and-hold, flipping and land banking (high capital), with the money, skills, risks and time to income of each, and honest numbers on why small investors often lose money.

You choose your starting path here. With little capital and 5 to 7 hours a week, the course recommends starting with services (often rental brokerage plus NRI property care, or marketing) and treating investing as a later stage.

This decision is not final: you will revisit it in Module 18 (investing) and Module 22 (capstone).
""",
    outcomes=[
        'Compare all real estate paths by capital, skills, risk and time to income.',
        'Explain with numbers why small investors often lose money.',
        'Calculate a break-even price for a flip.',
        'Choose one or two starting paths with three next steps.',
    ],
    lessons=LESSONS,
    project='your chosen path with risks and a 90-day start plan',
    project_steps=[
        'Complete the path chooser (RE-M02-L01) and the break-even calculation (RE-M02-L02).',
        'Write a one-page 90-day plan for your chosen path: services, target clients, first three steps, what you must learn first (which modules).',
        'List the risks of your path and how you will reduce each.',
        'Share the plan with one experienced person and note their comments.',
    ],
    project_proof='The path chooser, the break-even calculation, your 90-day plan with risks, and the feedback.',
    rubric=[
        ('Comparison', 'One path considered', 'Several paths scored', 'All paths compared with local evidence'),
        ('Numbers', 'No calculation', 'Rough numbers', 'Break-even calculation on a real listing'),
        ('Plan', 'Vague', 'Steps without dates', '90-day plan with steps, learning and risks'),
        ('Honesty about risk', 'Ignores risks', 'Lists risks', 'Lists risks with ways to reduce each'),
    ],
    short=[
        'Score the five low-capital paths and pick one.',
        'Write three first steps.',
    ],
    flashcards=[
        ('Five low-capital paths', 'Sales brokerage, rental brokerage, property management, NRI property care, marketing.'),
        ('Purchase transaction costs in Kerala (approx.)', 'About 10%+ (8% stamp duty, 2% registration, fees, brokerage); check current rules.'),
        ('Why flips often fail', 'Costs, slow resale, taxes, holding costs.'),
        ('Main risk of land banking', 'Money locked for years with no guarantee of rising prices.'),
        ('When to consider investing', 'After an emergency fund, experience, a full analysis and money you can lock away.'),
        ('Simpler property exposure', 'Listed REITs (Module 18).'),
    ],
    mistakes=[
        ('Following hype.', 'Use numbers and local evidence.'),
        ('Skipping the written plan.', 'A 90-day plan turns a choice into action.'),
        ('Mixing personal and client money.', 'Keep them separate from day one (Module 20).'),
    ],
    tools=[
        'The path chooser (RE-M02-L01).',
        'The flip break-even calculator (RE-M02-L02).',
    ],
    toolkit=[
        'Path chooser and 90-day start plan.',
        'Flip break-even calculator (Cost tab).',
    ],
)
