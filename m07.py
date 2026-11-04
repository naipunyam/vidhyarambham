from common import lesson, module, link, rules, xref, table, fence, Q, RULE, ASOF, CHECK
import tools

NOTE = 'All prices in this module\'s examples are **illustrative numbers for practice**, not real market data or recommendations. Your own comparables sheet gives you the real local numbers.'

DRIVERS = [
    ('Road frontage and width', 'Plots on a wide tarred road sell far higher than plots on a narrow path', 'Strong'),
    ('Distance to town, bus stand, school, hospital', 'Closer is usually higher', 'Strong'),
    ('Title quality', 'Clean, simple title sells faster and higher; doubtful title sells at a big discount', 'Strong'),
    ('Land type', 'Purayidam vs nilam or data bank land; nilam can be worth a fraction', 'Very strong'),
    ('Shape and level', 'Regular, level plots are easier to build on', 'Medium'),
    ('Flood and slope risk', 'Flood-prone or steep land is discounted, more so since 2018', 'Medium to strong'),
    ('Size', 'Small plots (5 to 10 cents) often have a higher price per cent than large ones', 'Medium'),
    ('Surroundings', 'Quarries, power lines and garbage sites reduce value; good neighbours and views add', 'Medium'),
    ('Water and utilities', 'A good well and KWA water add value', 'Medium'),
    ('Infrastructure plans', 'New roads, bypasses, rail or institutions can raise prices; also risk of acquisition', 'Variable'),
]

L1 = lesson(
    7, 1,
    outcome='You can explain fair value versus market value, build a comparables sheet with price per cent and per sq ft, and adjust comparables to estimate a fair range.',
    split='20 minutes reading, 40 minutes on comparables',
    core=f"""
{NOTE}

**Fair value vs market value.**
- **Fair value** is the government's notified minimum value per are for each survey number, used for stamp duty (RE-M03-L03, RE-M04-L01). It was raised by 20% from 1 April 2023 ({link('om-fv2023', 'Onmanorama')}; {CHECK}). It is usually **below** the market price in Kerala and changes only when the government revises it.
- **Market value** is the price a willing buyer would pay a willing seller, both well informed and under no pressure. Asking prices are **not** market value: they are what sellers hope for. Actual sale prices are better, but are hard to find (deeds sometimes show the fair value rather than the real price).
- A bank's **valuation** for a loan is a third figure, made by its empanelled valuer.

**The comparables method (sales comparison).** The main way to value land and houses:
1. Collect recent **comparable** listings and, wherever possible, actual sale prices (ask brokers and document writers) in the same area.
2. Calculate **price per cent** for land and **price per sq ft** for buildings (state the area basis).
3. **Adjust** each comparable for differences from the subject property: road, distance, size, shape, flood risk, title.
4. Use the **median** of the adjusted prices (less affected by extremes than the average) and give a **range**, not a single number.

**Value drivers in Kerala:**
{table(['Driver', 'Effect', 'Strength'], DRIVERS)}

**Asking vs selling.** In many Kozhikode localities, final prices may settle below asking prices, and some listings never sell. Ask local brokers what discount is typical and note it in your sheet.

The comparables sheet with working formulas is in the templates below and in your toolkit.
""",
    example="""
A 10-cent plot (subject) on a 4 m panchayat road, 2 km from Kuttiady town. Four comparables:

| Comp | Details | Asking per cent | Adjustment | Adjusted |
| --- | --- | --- | --- | --- |
| A | 8 cents, same road, 1.8 km | ₹2,40,000 | −5% (smaller plot, closer) | ₹2,28,000 |
| B | 12 cents, 6 m road, 1.5 km | ₹2,80,000 | −15% (better road, closer) | ₹2,38,000 |
| C | 15 cents, narrow path, 3 km | ₹1,60,000 | +20% (worse road, farther) | ₹1,92,000 |
| D | 10 cents, same road, 2.2 km, sold last month | ₹2,10,000 (sold) | 0% | ₹2,10,000 |

Median of adjusted values: (₹2,10,000 + ₹2,28,000) ÷ 2 = **₹2,19,000** per cent. Range about ₹2.0 to ₹2.35 lakh per cent, so the 10-cent plot is roughly ₹20 to ₹23.5 lakh. Comparable D (an actual sale) deserves extra weight. The adjustment percentages are judgement: learn them from local brokers and actual sales.
""",
    resources=[
        ('hc-fv', 'Re-read how to search fair value', '5 minutes'),
        ('magicbricks', 'Search land and house listings for Kozhikode district', '15 minutes'),
        ('99acres', 'Search the same, to compare portals', '10 minutes'),
        ('housing', 'Search the same', '10 minutes'),
    ],
    steps=[
        'Create the Comps tab in your workbook with the header row and formulas.',
        'Add your first 10 real listings (land and houses) around Kuttiady and Kozhikode from portals, local brokers, newspaper adverts and WhatsApp groups (record the source; don\'t copy personal phone numbers you weren\'t given).',
        'Choose one subject plot and adjust 3 to 4 comparables for it, as in the example.',
        'Ask one broker what discount from asking price is typical in your area.',
    ],
    proof='The Comps sheet with 10 rows and working formulas, one adjustment table and the broker\'s answer.',
    templates=[('Comparables sheet', tools.COMPS_HEADER + '\n\n' + tools.COMPS_FORMULAS), ('Comparable adjustment table', """COMPARABLE ADJUSTMENT    Subject: ______ cents, road ___ m, ___ km to town
Comp | Source | Size | Road | Distance | Other | Price/cent | Adj % | Adjusted
A    |        |      |      |          |       |            |       | =G2*(1+H2)
B ...
Median adjusted: =MEDIAN(I2:I6)   Range: low ______ high ______
Weight actual sales more than asking prices. Typical asking-to-sale discount here: ___%""")],
    mistakes=[
        ('Treating asking prices as market value.', 'Find actual sales and note the usual discount.'),
        ('Comparing unlike properties.', 'Adjust for road, distance, size and risk.'),
        ('Giving one exact number.', 'Give a range and explain it.'),
    ],
    fraud="""
**Fake comparables.** Some sellers and brokers quote "the plot next door sold for ₹3 lakh per cent" to push prices. Ask for proof (a deed copy or a broker who handled it) or treat it as a claim only.
""",
    quiz=[
        Q('What is fair value in Kerala?', 'The government\'s notified minimum value for stamp duty', 'The market price', 'The bank\'s valuation', 'The asking price', why='It usually lags the market.'),
        Q('Why use the median of adjusted comparables?', 'It is less affected by extreme values', 'It is always higher', 'It is the law', 'It is easier to type', why='One odd listing can distort an average.'),
        Q('A comparable has a much better road than the subject. How do you adjust it?', 'Adjust its price down to compare with the subject', 'Adjust it up', 'No adjustment', 'Remove all comparables', why='The subject is worse on that driver.'),
        Q('Which is better evidence of market value?', 'A recent actual sale price', 'An asking price on a portal', 'A WhatsApp forward', 'The seller\'s hope', why='Actual sales show what buyers paid.'),
    ],
    study='read the lesson and the value drivers table',
    action='build your Comps sheet with 10 real listings and adjust comparables for one plot',
)

L2 = lesson(
    7, 2,
    outcome='You can value a rented property by the income method (cap rate) and a house by the cost method, and cross-check them with comparables.',
    split='20 minutes reading, 35 minutes on calculations',
    core=f"""
{NOTE}

**Income method (capitalisation).** For property bought for rent (shops, offices, rental houses):
- **Net operating income (NOI)** = annual rent after vacancy, minus property and land tax, maintenance, insurance and management (not loan payments).
- **Capitalisation rate (cap rate)** = NOI ÷ value. If similar properties sell at a cap rate of, say, 4%, then **value = NOI ÷ 0.04**.
- Residential rental yields in Kerala are often low compared with interest rates (many investors earn more from price growth than from rent; check local numbers in your own ROI sheet, RE-M08-L02).

**Cost method.** Value = **land value** (from comparables) + **cost to build the building today** − **depreciation** (age, wear, outdated design).
- Construction cost per sq ft depends on quality and changes with material and labour costs (RE-M17). Ask two local contractors or engineers for current rates.
- Depreciation: a simple method is straight-line over the building's useful life (for example 60 years for a concrete house); older, poorly maintained houses lose more.
- Useful for **new or unique houses** where few comparables exist, and to check that a house price is not far above what it would cost to build.

**Cross-checking.** A good valuation uses two or three methods. If the comparables say ₹48 lakh, the cost method says ₹52 lakh and the income method says ₹30 lakh, the house is priced as a home to live in, not as an investment.

Further study: the {link('mit-re', 'MIT OCW real estate finance course')} explains valuation and cap rates in depth (advanced; read the lecture notes on valuation when you are ready). The {xref('fin', 'fin-m09-l06', 'Personal Finance lesson on gold, REITs and real estate')} covers real estate inside a personal portfolio.
""",
    example="""
**A shop room in Kuttiady town** rents for ₹18,000 a month.
- Gross rent: 18,000 × 12 = ₹2,16,000
- Vacancy 1 month: −₹18,000; building tax and maintenance: −₹20,000
- NOI: 2,16,000 − 18,000 − 20,000 = **₹1,78,000**
- If similar shops sell at a 5% cap rate: value = 1,78,000 ÷ 0.05 = **₹35.6 lakh**
- At a 6% cap rate: 1,78,000 ÷ 0.06 = **₹29.7 lakh**. A one-point change in cap rate changes the value by about ₹6 lakh.

**A 5-year-old house on 8 cents** near Kakkattil, 1,400 sq ft:
- Land: 8 × ₹2,20,000 = ₹17,60,000 (from comparables)
- Building cost new (illustrative ₹2,200 per sq ft): 1,400 × 2,200 = ₹30,80,000
- Depreciation over 60 years, 5 years used: 30,80,000 × 5 ÷ 60 = ₹2,56,667
- Cost-method value: 17,60,000 + 30,80,000 − 2,56,667 ≈ **₹45.8 lakh**
If it is listed at ₹62 lakh, either comparables support a premium (location, finish) or it is overpriced.
""",
    calc="""
**In Google Sheets or LibreOffice:**
- NOI: `=B1*(12-B2)-B3-B4` (B1 monthly rent, B2 vacancy months, B3 taxes, B4 maintenance)
- Value at cap rate: `=NOI/B5` (B5 cap rate such as 0.05)
- Cost method: `=land + build_cost_new - build_cost_new*age/useful_life`
- Sensitivity: put cap rates 0.04, 0.05, 0.06, 0.07 in a column and `=$NOI/A2` beside each.
""",
    resources=[
        ('mit-re', 'Open the course and skim the lecture notes list for valuation topics (advanced, optional)', '15 minutes'),
        ('lt-fin', 'Look at the chapter list; time value of money chapters support income valuation', '10 minutes'),
    ],
    steps=[
        'Find one rented property locally (shop or house) where the owner or broker will tell you the rent.',
        'Value it by the income method at three cap rates.',
        'Find one house listing and value it by the cost method, using land comparables and a construction cost from a local contractor.',
        'Compare both results with the asking prices and write what you conclude.',
    ],
    proof='Two calculations with sources for each input, and your conclusion.',
    templates=[('Income and cost valuation sheet', """INCOME METHOD               COST METHOD
B1 Monthly rent             C1 Land cents
B2 Vacancy months           C2 Land price per cent (comps)
B3 Taxes per year           C3 Land value         =C1*C2
B4 Maintenance per year     C4 Built-up sq ft
B5 Other costs              C5 Build cost per sq ft (2 contractor quotes)
B6 NOI =B1*(12-B2)-B3-B4-B5 C6 Cost new           =C4*C5
B7 Cap rate                 C7 Age (years)  C8 Useful life (years)
B8 Value =B6/B7             C9 Depreciation       =C6*C7/C8
                            C10 Value             =C3+C6-C9
Comparables value: ______   Asking price: ______   Conclusion: ______""")],
    mistakes=[
        ('Including loan EMIs in NOI.', 'NOI is before financing.'),
        ('Using a builder\'s marketing cost per sq ft.', 'Get quotes from local contractors.'),
        ('Relying on one method.', 'Cross-check with comparables.'),
    ],
    fraud="""
**Inflated rent claims.** Sellers of "investment" shops or houses sometimes show inflated rent (a relative as tenant, a short-term agreement) to raise the value. Ask for the rental agreement, bank statements of rent received and the tenant's history.
""",
    quiz=[
        Q('Value by the income method equals:', 'NOI ÷ cap rate', 'Rent × 100', 'Price per cent × cents', 'EMI × 12', why='Lower cap rates mean higher values.'),
        Q('What is NOI?', 'Annual rent after vacancy minus operating costs, before loan payments', 'Monthly rent', 'Rent minus EMI', 'The asking price', why='Financing is separate.'),
        Q('When is the cost method most useful?', 'For new or unique houses with few comparables', 'For empty land only', 'For shares', 'Never', why='It shows the replacement cost.'),
        Q('If NOI is ₹1,20,000 and the cap rate is 4%, what is the value?', '₹30 lakh', '₹4.8 lakh', '₹1.2 crore', '₹3 lakh', why='1,20,000 ÷ 0.04.'),
    ],
    study='read the lesson and both worked examples',
    action='value one rented property by the income method and one house by the cost method',
)

L3 = lesson(
    7, 3,
    outcome='You can complete a local market study with 20+ real listings, compare government fair values with market prices, and summarise prices by locality.',
    split='10 minutes reading, 60 minutes of market work (spread over the week)',
    core=f"""
{NOTE}

This is one of the course's key practical tasks: a **local market study** of Kuttiady and Kozhikode with **at least 20 real listings** (land and houses), plus the **government fair value** for several of them.

**Where to find listings:**
- Free portals: MagicBricks, 99acres, Housing.com, NoBroker (filter by Kozhikode, locality and property type).
- OLX and Facebook Marketplace (verify carefully; many are outdated).
- Local brokers and their WhatsApp status updates; newspaper classifieds (Mathrubhumi and Malayala Manorama classifieds).
- Boards on plots ("land for sale" with a phone number).
Record the source and date for each. Never collect or share personal data you have not been given for this purpose.

**What to record:** follow the comps header (date, source, locality, type, land area, built-up area, asking price, road, distance, flood or slope notes, status).

**Fair value comparison:** for at least 5 listings where you know the village and survey number (or a nearby one), look up the fair value on the official portal and calculate:
- Fair value per cent = fair value per are ÷ 2.471
- **Gap** = (asking per cent − fair value per cent) ÷ fair value per cent

**Summary by locality:** median price per cent for land and median price per sq ft for houses, with the count of listings. Note what drives the differences (road, distance, town).

**Use it every week:** add 3 new listings in your weekly log (re-system track) so your sheet stays current.
""",
    example="""
Sachin's sheet after two weeks (illustrative figures):

| Locality | Land listings | Median per cent | Houses | Median per sq ft (incl. land) |
| --- | --- | --- | --- | --- |
| Kuttiady town (within 1 km) | 4 | ₹4.5 lakh | 2 | ₹4,800 |
| Kuttiady (2 to 5 km) | 6 | ₹2.1 lakh | 3 | ₹3,600 |
| Kayakkody / Velom | 4 | ₹1.6 lakh | 1 | ₹3,100 |
| Kozhikode city (Mavoor Road area) | 3 | ₹18 lakh | 2 | ₹7,500 |

Fair value check for five listings: fair values were 25% to 45% of asking prices. A seller who says "fair value is ₹70,000 per cent, so ₹1.6 lakh is cheap" is mixing two different things.
""",
    resources=[
        ('magicbricks', 'Search Kozhikode listings', '15 minutes'),
        ('99acres', 'Search Kozhikode listings', '15 minutes'),
        ('housing', 'Search Kozhikode listings', '15 minutes'),
        ('nobroker', 'Search owner listings', '10 minutes'),
        ('hc-fv', 'Fair value search steps', '5 minutes'),
    ],
    steps=[
        'Bring your Comps sheet to at least 20 real listings (land and houses) around Kuttiady and Kozhikode, with sources and dates.',
        'Look up fair values for at least 5 of them on the official portal and calculate the gap.',
        'Make a summary table by locality (median per cent, median per sq ft, counts).',
        'Write a half-page market note: what drives prices here, what surprised you and the typical asking-to-sale discount you were told.',
    ],
    proof='The Comps sheet with 20+ rows, the fair value comparison for 5 listings, the summary table and your market note.',
    templates=[('Market study summary', """MARKET STUDY SUMMARY      Area ______  Period ______  Listings ___ (target 20+)
Locality | Land count | Median ₹/cent =MEDIAN(FILTER(Comps!J:J,Comps!D:D=A2,Comps!F:F="land")) | House count | Median ₹/sq ft
FAIR VALUE CHECK
Listing | Village | Survey | Fair value per are | per cent (=x/2.471) | Asking per cent | Gap % (=(asking-fv)/fv)
NOTES: price drivers ______ ; typical discount from asking ___% ; sources used ______""")],
    mistakes=[
        ('Counting duplicates.', 'The same plot often appears on several portals; list it once.'),
        ('Using old listings.', 'Record dates and remove stale ones.'),
        ('Mixing land and house prices per sq ft.', 'Keep land per cent and house per sq ft separate.'),
    ],
    fraud="""
**Fake listings to collect leads.** Some portal ads show attractive "properties" that don't exist, to collect buyer numbers. If the details are vague and the poster won't share the location, treat it as unreliable.
""",
    quiz=[
        Q('How many listings should your market study include?', 'At least 20', '2', '5', '1,000', why='Enough to see a pattern.'),
        Q('How do you convert a fair value per are to per cent?', 'Divide by 2.471', 'Multiply by 100', 'Divide by 435.6', 'Multiply by 40.47', why='1 are = 2.471 cents.'),
        Q('Why record the date of each listing?', 'So you can remove stale listings and see trends', 'For tax', 'It is not needed', 'For the seller', why='Markets change.'),
        Q('A seller says "fair value is low, so my price is cheap." What is wrong?', 'Fair value is a duty minimum, not a measure of market price', 'Nothing', 'Fair value is always the market price', 'Fair value is always higher', why='Compare with comparables instead.'),
    ],
    study='read the lesson and plan your sources',
    action='complete a market study with 20+ listings and fair value comparisons',
    fulltime='Aim for 40 listings and visit 5 localities in person.',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    7,
    overview=f"""
Valuation: fair value and market value, the comparables method with adjustments, the income and cost methods, the value drivers in Kerala, and a local market study of 20+ real listings with fair value comparisons.

Valuation is how you stay honest with owners ("your price is 20% above comparable sales") and protect buyers. You will not give formal valuations (banks use their own licensed valuers); you will give clients evidence-based price ranges. Rates and rules are {RULE}.
""",
    outcomes=[
        'Explain fair value, market value and bank valuation.',
        'Value land and houses by comparables with adjustments.',
        'Use the income and cost methods.',
        'Run a local market study with 20+ listings.',
    ],
    lessons=LESSONS,
    project='a local market study report',
    project_steps=[
        'Complete the Comps sheet (20+ listings) and fair value comparison.',
        'Value one subject property by comparables and one other method.',
        'Write a 1 to 2 page market report for Kuttiady (or your area): medians by locality, drivers, discount, risks.',
        'Share it with one broker you interviewed and note their feedback.',
    ],
    project_proof='The Comps sheet, the valuation and the report with the broker\'s feedback.',
    rubric=[
        ('Data', 'Under 10 listings', '10 to 19 listings', '20+ listings with sources and dates'),
        ('Method', 'Asking prices only', 'Comparables without adjustments', 'Adjusted comparables plus a second method'),
        ('Fair value', 'Not checked', '1 to 4 checked', '5+ checked with gap calculated'),
        ('Report', 'No report', 'Numbers only', 'Clear medians, drivers, discount and risks'),
    ],
    short=[
        'Collect 10 listings and calculate price per cent.',
        'Check fair value for 2 of them.',
    ],
    flashcards=[
        ('Fair value', 'Government minimum value for stamp duty.'),
        ('Market value', 'What a willing, informed buyer pays a willing seller.'),
        ('Comparables method', 'Value from adjusted recent similar sales and listings.'),
        ('Median', 'Middle value; less affected by extremes.'),
        ('NOI', 'Rent after vacancy minus operating costs, before loans.'),
        ('Cap rate', 'NOI ÷ value.'),
        ('Cost method', 'Land + building cost new − depreciation.'),
        ('Strongest Kerala value drivers', 'Road, distance, land type, title.'),
    ],
    mistakes=[
        ('Calling yourself a valuer.', 'Banks use licensed valuers; you give evidence-based ranges.'),
        ('Ignoring risks in value.', 'Flood, title and land type reduce value.'),
        ('Not updating your sheet.', 'Add 3 listings each week.'),
    ],
    tools=[
        'Comparables sheet and adjustment table (RE-M07-L01).',
        'Income and cost valuation sheet (RE-M07-L02).',
        'Market study summary (RE-M07-L03).',
    ],
    toolkit=[
        'Comps tab with formulas and 20+ listings.',
        'Valuation sheet (income and cost).',
        'Market study report.',
    ],
)
