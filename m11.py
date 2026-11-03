"""Module 11: Big life goals."""
from common import lesson, module, link, fence, table, inr, ASOF, CHECK

M = 11


def pmt(p, a, n):
    r = a / 12
    return p * r * (1 + r) ** n / ((1 + r) ** n - 1)


def fv(pv, rate, years):
    return pv * (1 + rate) ** years


def pmt_needed(target, annual_rate, months):
    r = annual_rate / 12
    return target * r / ((1 + r) ** months - 1)


def rent_vs_buy(price, house_growth, inv_return, years=10, rent0=12000, rate=0.085):
    down, other = 0.2 * price, 0.08 * price
    loan = price - down
    emi = pmt(loan, rate, 240)
    r = rate / 12
    k = years * 12
    out = loan * (1 + r) ** k - emi * ((1 + r) ** k - 1) / r
    buy_nw = price * (1 + house_growth) ** years - out
    inv, rent, upkeep, ri = down + other, rent0, 20000 / 12, inv_return / 12
    for m in range(k):
        if m and m % 12 == 0:
            rent *= 1.05
        inv = inv * (1 + ri) + max(emi + upkeep - rent, 0)
    return emi, buy_nw, inv


RB_EMI, RB_BUY_A, RB_RENT_A = rent_vs_buy(4000000, 0.04, 0.08)
_, RB_BUY_B, RB_RENT_B = rent_vs_buy(4000000, 0.07, 0.06)

CAR_PRICE = 650000
CAR_LOAN = CAR_PRICE * 0.8
CAR_EMI = pmt(CAR_LOAN, 0.095, 60)

L1 = lesson(
    M, 1,
    title='Planning big goals: weddings, vehicles and sinking funds',
    weeks=(23, 23), hours=1.5,
    outcome='Turn a wedding, a vehicle or any big purchase into a funded goal with a real budget, a total cost of ownership and a monthly saving that fits your plan.',
    split='20 minutes reading, 20 minutes resources, 50 minutes action',
    core=f"""
Big goals break budgets when they are treated as emergencies or as one-off "special" spending. Weddings, vehicles, house repairs and big family events are **known in advance**, so they can be planned like any other goal (Module 2): a price, a date, a monthly saving and a place for the money to wait (Modules 8 and 9).

### Weddings

Kerala weddings can cost several years of income: gold, the venue, food for hundreds of guests, clothes, photos and travel. Families often borrow, pledge gold or sell land for them.

- **Decide the budget before the planning starts,** together with the people paying, and write it down. Social pressure (Module 1) grows once relatives start suggesting.
- **List costs by category** and decide where to cut: a smaller venue, a shorter guest list, less gold.
- **Gold:** jewellery bought for a wedding is part of the family's wealth only at its buyback value (Module 2). Buying less, or holding part of it as gold ETFs, keeps more of the value.
- **Dowry is illegal.** Under the Dowry Prohibition Act, 1961, giving, taking or helping with dowry is punishable with imprisonment of at least five years and a fine of at least ₹15,000 or the value of the dowry, whichever is more; presents given without any demand, listed and not excessive are excluded ({link('dowry-act', 'Ministry of Women and Child Development')}). A financial plan should never include a dowry, and you have the law on your side if anyone demands one.
- **Don't borrow for the celebration.** Loans for a single day can take years to repay and delay every other goal.

### Vehicles: the total cost of ownership

The price is only the start. **Total cost of ownership** includes:

> **Monthly cost = EMI (or saving) + insurance ÷ 12 + fuel + servicing and repairs ÷ 12 + parking and tolls + the fall in value**

**Worked example:** a car priced {inr(CAR_PRICE)} on road, 20% down, the rest as a 5-year loan at 9.5%: EMI {inr(CAR_EMI)}. Add insurance (say ₹18,000 a year), fuel (₹4,000 a month) and servicing (₹12,000 a year), and it costs about **{inr(CAR_EMI + 18000 / 12 + 4000 + 12000 / 12)} a month**, before the value it loses each year. A simple rule some people use: keep total vehicle costs under about 10–15% of take-home pay. Compare a two-wheeler, a used car or public transport honestly.

### Sinking funds for big goals

For each big goal: future cost (Module 2), monthly saving with PMT, and the right place for the money by time horizon:

- Under 3 years: RD, FDs, post office deposits.
- 3–7 years: mostly safe, with a small growth part, per your Investment Policy Statement.

When the goal arrives, the money is there, and nobody has to pledge gold.
""",
    example=f"""
**Anu's** parents had always expected her wedding to cost "around ₹15 lakh, like her cousin's". Anu asked for a family meeting with the numbers from her Goals tab.

Together they listed what they really wanted: a simple ceremony at the local hall for 300 guests, a lunch, photos, and her grandmother's jewellery plus 5 new pavan. Their estimate came to about ₹7.5 lakh. Her parents had ₹4 lakh saved and the gold; Anu's share would be ₹1.5 lakh over four years, about ₹2,800 a month in an RD.

Two decisions changed the most: no new gold beyond the 5 pavan (her grandmother's jewellery mattered more to her), and no loan. When a relative asked about "what the groom's family expects", her father said firmly that the family doesn't do dowry. "Having the plan on paper made it easier to say no," he said afterwards.
""",
    resources=[
        ('dowry-act', 'The Dowry Prohibition Act, 1961: what is prohibited, penalties and the exclusion for unrequested presents', '10 minutes'),
        ('ncfe', 'The long-term planning module (revision), with your big goals in mind', '10 minutes'),
    ],
    steps=[
        'Make a **Big Goals** tab with the template. List every big goal in the next 10 years: wedding, vehicle, house repairs, a family event, a business start-up, further study.',
        'For each, write a realistic cost today, ideally from quotes or recent family experience.',
        'For a vehicle goal, fill in the total cost of ownership calculator.',
        'Use the formulas to get future cost and monthly saving; choose where each goal\'s money waits.',
        'For any goal involving family (such as a wedding), share the numbers and agree a budget with the people paying. Write the agreed budget.',
    ],
    proof='Your Big Goals tab with costs, monthly savings and places, a vehicle cost calculation if relevant, and the agreed budget for any family goal, saved in 11 Big goals.',
    templates=[
        ('Big Goals tab', """
Row 1: Goal,Cost today (₹),Years away,Inflation,Future cost (₹),Saved so far (₹),Return while saving,Monthly saving (₹),Where it waits,Who pays (me / family / shared),Agreed?
E2: =B2*(1+D2)^C2
H2: =IF(G2=0,(E2-F2)/(C2*12),PMT(G2/12,C2*12,-F2,E2)*-1)
""", ''),
        ('vehicle total cost of ownership', """
B2: on-road price (₹)           B3: down payment (₹)       B4: loan rate (e.g. 0.095)    B5: loan months
B6: EMI (₹)                     =IF(B2-B3>0,PMT(B4/12,B5,-(B2-B3)),0)
B7: insurance per year (₹)      B8: fuel per month (₹)     B9: servicing per year (₹)    B10: parking, tolls per month (₹)
B11: monthly cost               =B6+B7/12+B8+B9/12+B10
B12: as % of take-home pay      =B11/take_home*100
""", ''),
    ],
    mistakes=[
        ('Letting the guest list set the budget.', 'Set the budget first, then plan the event to fit it.'),
        ('Comparing vehicles by EMI alone.', 'Insurance, fuel, servicing and depreciation often add more than half again.'),
        ('Borrowing for a celebration.', 'A loan for one day can delay your goals for years.'),
        ('Treating wedding gold as savings at the buying price.', 'Value it at the buyback rate; making charges are gone.'),
    ],
    quiz=[
        {'q': 'What does "total cost of ownership" of a vehicle include?', 'o': ['EMI, insurance, fuel, servicing, other running costs and loss of value', 'Only the EMI', 'Only the on-road price', 'Only fuel'], 'a': 'A', 'why': 'All the costs of having the vehicle, not just buying it.'},
        {'q': 'Under the Dowry Prohibition Act, 1961, what is the minimum prison term for giving or taking dowry?', 'o': ['Five years', 'One month', 'There is none', 'Ten years'], 'a': 'A', 'why': 'At least five years, plus a fine (the court can reduce it for special reasons).'},
        {'q': 'A goal costs ₹3 lakh today, 4 years away, 5% inflation. About how much will it cost?', 'o': ['₹3.65 lakh', '₹3 lakh', '₹3.6 lakh exactly', '₹4.5 lakh'], 'a': 'A', 'why': '₹3,00,000 × 1.05⁴ ≈ ₹3,64,652.'},
        {'q': 'When should the wedding budget be decided?', 'o': ['Before planning starts, with the people paying', 'After the guest list is final', 'After the wedding', 'Never; it is unpredictable'], 'a': 'A', 'why': 'A written budget first makes it easier to resist pressure later.'},
    ],
    study='The Dowry Prohibition Act page and the NCFE long-term planning module',
    action='Build your Big Goals tab, calculate a vehicle\'s total cost if relevant, and agree a written budget for one family goal',
)

L2 = lesson(
    M, 2,
    title='A house: rent or buy?',
    weeks=(23, 23), hours=2,
    outcome='Compare renting and buying a home with a spreadsheet that includes the down payment, all costs, the EMI, the money you could invest instead, and your own assumptions.',
    split='25 minutes reading, 25 minutes resources, 70 minutes action',
    core=f"""
Owning a home is deeply valued in Kerala, and it brings real security. It is also usually the biggest financial decision of a life. This lesson separates the **emotional** decision (where and how you want to live) from the **financial** one (what it costs compared with renting).

### The real costs of buying

- **Down payment:** banks lend only part of the value; you pay the rest from savings.
- **Stamp duty and registration:** set by the state, paid when you buy. Check the current rates with the Kerala registration department before planning.
- **Interiors, furniture, moving.**
- **The loan:** EMI for 15–25 years. On a floating rate, the EMI or tenure rises when rates rise (FIN-M06-L03); prepayment penalties aren't allowed on individuals' floating-rate home loans sanctioned from 2026 ({link('prepay', 'Angel One')}, {CHECK}).
- **Every year:** property tax, maintenance, repairs, home insurance (FIN-M07-L04).

### The costs of renting

Rent, rising over time, and a deposit. In exchange: flexibility (useful if your job may transfer you, as many government jobs do), no repairs, and the down payment and extra monthly money stay free to invest.

### A fair comparison

Compare **wealth after 10 years** under both choices:

- **Buy:** the house's value then, minus the loan still outstanding.
- **Rent:** invest the down payment and purchase costs, and every month invest the difference between the cost of owning (EMI plus upkeep) and the rent.

**Worked example** (made-up): a ₹40 lakh house, 20% down, 8% for stamp duty, registration and other costs, a ₹32 lakh loan at 8.5% for 20 years (EMI {inr(RB_EMI)}), upkeep ₹20,000 a year; rent of ₹12,000 a month rising 5% a year.

{table(['Assumptions', 'Wealth after 10 years: buy', 'Wealth after 10 years: rent and invest'], [
    ('House grows 4% a year; investments earn 8%', inr(RB_BUY_A), inr(RB_RENT_A)),
    ('House grows 7% a year; investments earn 6%', inr(RB_BUY_B), inr(RB_RENT_B)),
])}

The answer **flips with the assumptions**. Nobody knows future house prices or investment returns, so test several. The rent path only wins if you **really invest the difference every month**; most people who rent don't, and then buying wins by default, as forced saving.

### Questions that matter as much as the numbers

1. **Will I live here at least 7–10 years?** Buying and selling within a few years usually loses money to costs.
2. **Is the EMI under about a third of take-home pay,** with the emergency fund intact (Module 5)?
3. **Is the property legally clean?** Title, encumbrance, approvals; for builder projects, **K-RERA registration**, which you can search on the K-RERA website ({link('krera', 'K-RERA')}).
4. **Does it fit my other goals?** A house that stops retirement saving is too expensive.

### Tax, briefly

Under the old regime, home loan principal and stamp duty count within section 123 (FIN-M10-L02) and interest has its own deduction within limits; the new regime mostly doesn't give these for a home you live in. Don't let tax decide the house.
""",
    example=f"""
**Rahul** was offered a 2BHK flat near Vatakara for ₹42 lakh by a builder. His family urged him to buy "before prices go up". He ran the rent-or-buy sheet with three sets of assumptions and asked two questions first.

**Will he stay 10 years?** His department can transfer him across the district or beyond. Probably not.
**Is the project on K-RERA?** He searched the K-RERA site: it was registered, with an expected completion date two years away.

The EMI would be about {inr(pmt(3360000, 0.085, 240))}, almost all of his take-home pay. His numbers showed renting and investing ahead in two of three scenarios, and buying ahead only if prices rose fast. He decided to wait: keep renting near his office, build his down payment in a mix of safe and growth investments per his IPS, and revisit in three years when his pay and posting are clearer. "Waiting isn't losing," he wrote. "Buying a house I can't afford would be."
""",
    resources=[
        ('krera', 'K-RERA: search a project\'s registration and see how complaints work', '15 minutes'),
        ('prepay', 'No prepayment charges on individuals\' floating-rate home loans from 2026', '5 minutes'),
        ('openstax', 'Chapter 9, "Time Value of Money III: Unequal Multiple Payment Values": skim how uneven cash flows are compared', '20 minutes'),
    ],
    steps=[
        'Write your honest answers to the four questions for your situation (or for your family\'s next house decision).',
        'Build the rent-or-buy calculator from the template with your own or realistic local numbers: price, down payment, costs, loan rate and term, rent.',
        'Run at least three scenarios: low, middle and high house price growth, with matching investment returns.',
        'Check the EMI as a share of your take-home pay and against your other goals.',
        'If a specific project is involved, search for it on K-RERA and note its registration details.',
        'Write your decision (buy now, buy later with a date, or rent) and the reasons.',
    ],
    proof='Your rent-or-buy calculator with three scenarios, the four answers and your written decision, saved in 11 Big goals.',
    templates=[
        ('rent or buy calculator (yearly version)', """
INPUTS: B2 price  B3 down % (0.2)  B4 buying costs % (0.08)  B5 loan rate  B6 loan years  B7 upkeep per year
        B8 rent per month now  B9 rent growth (0.05)  B10 house growth  B11 investment return  B12 years to compare (10)
B14: loan        =B2*(1-B3)
B15: EMI         =PMT(B5/12,B6*12,-B14)
B16: loan left after B12 years   =-FV(B5/12,B12*12,-B15,B14)
B17: BUY wealth  =B2*(1+B10)^B12-B16
RENT path (one row per year, years 1..B12 in A20:A29):
B20: rent this year     =$B$8*12*(1+$B$9)^(A20-1)
C20: owning cost        =$B$15*12+$B$7
D20: invested this year =MAX(C20-B20,0)
E20: investment value   =(E19+D20)*(1+$B$11)     (E19 = starting amount: =B2*(B3+B4))
B30: RENT wealth  =E29
(The yearly version is simpler than monthly; results are close.)
""", ''),
    ],
    mistakes=[
        ('Comparing EMI with rent only.', 'Include the down payment\'s lost returns, buying costs, upkeep and what you would invest when renting.'),
        ('Assuming prices always rise fast.', 'Test low-growth scenarios. Some areas stay flat for years.'),
        ('Buying before job location is stable.', 'Transfers and job changes turn a dream home into a burden.'),
        ('Skipping legal checks.', 'Check title, encumbrance and K-RERA registration before paying any advance.'),
    ],
    quiz=[
        {'q': 'What does the "rent and invest" path assume?', 'o': ['You invest the down payment and the monthly difference every month', 'You spend the difference', 'Rent never rises', 'House prices fall'], 'a': 'A', 'why': 'Renting builds wealth only if the money saved is actually invested.'},
        {'q': 'Where can you check whether a builder\'s project in Kerala is registered?', 'o': ['The K-RERA website', 'The builder\'s brochure', 'A WhatsApp group', 'Your bank passbook'], 'a': 'A', 'why': 'K-RERA lets you search registered projects and file complaints.'},
        {'q': 'Why does living in a place only a few years usually favour renting?', 'o': ['Buying and selling costs eat into any gain over a short period', 'Rent is always cheaper', 'Banks refuse short loans', 'Houses lose value in 3 years'], 'a': 'A', 'why': 'Stamp duty, registration and selling costs need years of growth to recover.'},
        {'q': 'In the worked example, what changed which option won?', 'o': ['The assumptions for house price growth and investment returns', 'The colour of the house', 'The bank\'s name', 'Nothing; buying always wins'], 'a': 'A', 'why': 'Test several scenarios because the future is unknown.'},
    ],
    study='K-RERA project search, the prepayment rule and OpenStax chapter 9\'s overview',
    action='Run a rent-or-buy comparison with three scenarios and write your decision',
)

EDU_TODAY = 800000
EDU_FUT = fv(EDU_TODAY, 0.07, 12)
EDU_PMT = pmt_needed(EDU_FUT, 0.08, 144)

L3 = lesson(
    M, 3,
    title='Children\'s education',
    weeks=(24, 24), hours=1.5,
    outcome='Estimate the future cost of a child\'s education, choose a saving mix by time horizon, and plan how loans and scholarships fit without sacrificing your retirement.',
    split='20 minutes reading, 20 minutes resources, 50 minutes action',
    core=f"""
Education is the goal Kerala families care about most, and costs can rise faster than general inflation. A plan made early turns a frightening number into a monthly habit.

### Step 1: the future cost

Pick a realistic course (engineering, medicine, nursing, a degree plus coaching) and find **today's total cost**: fees for all years, hostel, books, travel. Then grow it to the year it starts. This course uses **7% a year** for education in examples; it is an assumption, not a forecast.

**Worked example:** a course costing {inr(EDU_TODAY)} in total today, starting in 12 years, at 7% education inflation, will cost about **{inr(EDU_FUT)}**. Saving for it at an assumed 8% a year needs about **{inr(EDU_PMT)} a month** for 12 years (=PMT(0.08/12, 144, 0, -{EDU_FUT:.0f})).

### Step 2: the saving mix, by time horizon

- **More than 7 years away:** a larger growth share is reasonable (Module 8), such as equity index funds, plus safe options. As the date nears, move money step by step to safe options so a market fall in the last years can't wreck the plan.
- **Sukanya Samriddhi (SSA)** for a daughter: **8.2%** in October to December 2026, ₹250 to ₹1.5 lakh a year, deposits for 15 years ({link('small-rates', 'rates')}, {link('om-small', 'limits')}, {CHECK}). Government-backed and tax-free interest, but money is locked; it suits part of a daughter's education and marriage plan.
- **PPF** (FIN-M09-L04): safe and tax-free, with a 15-year term.
- **3 years or less away:** safe options only.

### Step 3: loans and scholarships are part of the plan

You don't have to fund every rupee in advance. **Education loans** exist; under **PM-Vidyalaxmi**, students at eligible institutions can get collateral-free, guarantor-free loans, with interest subvention for families earning up to ₹8 lakh on loans up to ₹10 lakh ({link('pmvl', 'PIB')}, {CHECK}). Merit and need-based scholarships help too. Plan to fund, say, 60–80% and leave room for these.

### Step 4: don't sacrifice retirement

There are loans for education; there are no loans for retirement. A common saying among planners is "fix your own oxygen mask first". If money is tight, keep your retirement saving going (Module 12) and fund education with what remains, plus loans and scholarships if needed.

### Involve the child, when old enough

A teenager who knows the family's budget makes different choices: a government college, an entrance coaching that fits, a part-time job. Money talk is part of education too.
""",
    example=f"""
**Nisha**, who runs Nisha's Oven, has a daughter, Ammu, aged 6. Nisha wanted Ammu to have the choice of a professional course in 12 years. She estimated today's cost of a four-year course with hostel at ₹8 lakh, which grows to about {inr(EDU_FUT)} at 7%.

Her plan: ₹3,000 a month into SSA for Ammu (safe, tax-free, locked), and ₹4,000 a month into an equity index fund through a SIP (after writing her Investment Policy Statement), moving it step by step to safe options from Ammu's age 15. Together, at her assumed returns, they cover about 80% of the estimate; the rest can come from a scholarship, an education loan or her savings at the time.

She kept her own retirement contribution (₹2,500 a month) running alongside. "Ammu will have choices," she said, "and I won't be a burden on her later."
""",
    resources=[
        ('small-rates', 'The current Sukanya Samriddhi rate', '5 minutes'),
        ('om-small', 'SSA and PPF deposit limits and terms', '10 minutes'),
        ('pmvl', 'PM-Vidyalaxmi: who is eligible and what support is available', '10 minutes'),
    ],
    steps=[
        'If you have or plan children, choose one education goal per child (or for a younger sibling or niece/nephew you support, or a future child).',
        'Find today\'s total cost of a realistic course, from college websites or families who have done it.',
        'Calculate the future cost and monthly saving with the template.',
        'Choose the saving mix by horizon and write when you will move money to safe options.',
        'Write what share you plan to cover from savings, and the backup: loans, scholarships.',
        'No children and no plans? Write "not applicable now" and calculate the example for practice.',
    ],
    proof='Your education goal calculation, saving mix and backup plan (or the practice calculation), saved in 11 Big goals.',
    templates=[
        ('education goal', """
B2: child's name / goal             B3: years until the course starts
B4: total cost today (₹)            B5: education inflation (e.g. 0.07)
B6: future cost (₹)                 =B4*(1+B5)^B3
B7: share to fund from savings      (e.g. 0.8)
B8: target (₹)                      =B6*B7
B9: assumed return while saving     (e.g. 0.08; lower it as the date nears)
B10: monthly saving (₹)             =PMT(B9/12,B3*12,0,-B8)
Glide path: from (year) ____ move ___% a year to safe options.
""", ''),
    ],
    mistakes=[
        ('Guessing the cost.', 'Use real fee lists and add hostel, books and travel.'),
        ('Keeping education money in equity until the last year.', 'Move it to safe options gradually in the final 3–5 years.'),
        ('Stopping retirement saving for education.', 'Education can be partly borrowed; retirement can\'t.'),
        ('Buying an "education insurance plan" without calculating its return.', 'Check any bundled plan with the RATE method from FIN-M07-L01.'),
    ],
    quiz=[
        {'q': 'A course costs ₹8 lakh today, starting in 12 years, at 7% inflation. About how much will it cost?', 'o': ['About ₹18 lakh', 'About ₹8.6 lakh', 'About ₹12 lakh', 'About ₹40 lakh'], 'a': 'A', 'why': '₹8,00,000 × 1.07¹² ≈ ₹18 lakh.'},
        {'q': 'What was the Sukanya Samriddhi interest rate for October to December 2026?', 'o': ['8.2%', '7.1%', '4%', '6.7%'], 'a': 'A', 'why': 'SSA was at 8.2% (check current rates).'},
        {'q': 'Why move education savings to safe options in the last few years?', 'o': ['A market fall close to the date could leave too little time to recover', 'Safe options always earn more', 'It is required by law', 'Equity funds close after 10 years'], 'a': 'A', 'why': 'The goal date is fixed; protect the money as it nears.'},
        {'q': 'If money is tight, what should usually continue alongside education saving?', 'o': ['Your own retirement saving', 'A new car loan', 'Expensive coaching for every subject', 'Nothing else'], 'a': 'A', 'why': 'Education can be partly funded by loans and scholarships; retirement can\'t.'},
    ],
    study='The SSA rate and limits and the PM-Vidyalaxmi scheme',
    action='Calculate one education goal\'s future cost and monthly saving and write the saving mix and backup plan',
)

L4 = lesson(
    M, 4,
    title='Supporting your parents',
    weeks=(24, 24), hours=1.5,
    outcome='Map your parents\' finances with them, close the most dangerous gaps (health cover, emergencies, scams), and agree how support is shared among siblings.',
    split='20 minutes reading, 20 minutes resources, 50 minutes action',
    core=f"""
In Kerala, many parents live on small pensions, savings, farm income or help from children, and Kerala's population is older than India's on average. Supporting parents is a value for most families. It works best with **a plan made together**, not with emergencies handled alone.

### Step 1: the parents' money map

With your parents' permission, write down:

- **Income:** pension, interest, rent, farm income, support from children
- **Savings and where they are:** banks, post office, co-operative societies, chitties, gold
- **Insurance and schemes:** health cover, KASP or Medisep eligibility (FIN-M07-L04)
- **Debts:** gold loans, family loans
- **Documents and nominees:** where the papers are, who the nominees are (Module 13)
- **Monthly expenses,** especially medicines

### Step 2: close the dangerous gaps first

1. **Health cover:** the biggest risk for older parents. Check scheme eligibility (KASP, Medisep if a parent is a government pensioner), existing policies and options for seniors (FIN-M07-L03). Note that Ayushman Vaya Vandana was reported as not implemented in Kerala as of November 2025 ({link('om-seniors', 'Onmanorama')}); check its current status.
2. **An emergency fund for parents,** even small, kept where they or you can reach it quickly.
3. **Regular income from savings:** safe options such as SCSS (for 60+, 8.2% in October to December 2026) and MIS, rather than one large co-operative deposit (FIN-M09-L03).
4. **Scam protection:** older people are targeted by "digital arrest", KYC and lottery frauds. Share the fraud response card (FIN-M04-L02) and Module 15.
5. **Nominations and documents:** check every account has a nominee and that someone knows where papers are.

### Step 3: share fairly among siblings

When several children support parents, money becomes a source of quiet resentment unless it is discussed. Agree: who contributes how much each month (by income, not equally), who handles which tasks (hospital visits, paperwork), and how big expenses will be shared. Write it down and review it yearly.

### Step 4: protect your own plan too

Support from a full emergency fund and a budget line, not from your retirement savings or a loan. If parents need more than you can give, look at schemes, siblings and their own assets (gold, land) before borrowing.

### Talking about money with parents

Start with care, not control: "I want to make sure you are protected if something happens." Ask questions, listen, and let them decide about their own money. A respectful conversation now prevents a frantic search for documents in a hospital corridor later.
""",
    example=f"""
**Rahul** sat down with his parents and his sister on a Sunday. His father, a retired KSRTC conductor, drew a small pension; his mother had no income. Their money map showed: ₹3.5 lakh in a co-operative society, 11 pavan of gold (4 already pledged for an old loan), no private health insurance, and Rahul's father's pension papers in "the steel almirah, somewhere".

They agreed four things:

{table(['Gap', 'Action', 'Who'], [
    ('Health cover', 'Check KASP eligibility at a hospital helpdesk; check whether his father\'s pension comes with any health scheme; compare a senior policy for his mother', 'Rahul'),
    ('Gold loan', 'Repay it over 10 months from Rahul\'s budget line for parents, so the gold isn\'t auctioned', 'Rahul'),
    ('Co-operative deposit', 'Confirm membership and the Kerala guarantee; move part to SCSS when the deposit matures', 'Father, with Rahul'),
    ('Documents', 'Make one file with pension papers, bank passbooks and policies; check nominees', 'Sister'),
])}

Rahul contributes ₹5,000 a month and his sister, who earns less, ₹2,000; big medical costs are shared in the same proportion. They wrote it in a shared note and put a yearly review in December.
""",
    resources=[
        ('om-seniors', 'Health cover options for seniors in Kerala, including KASP and the Karunya fund', '15 minutes'),
        ('indiapost', 'SCSS and MIS rates for parents\' regular income', '5 minutes'),
        ('kp-1930', 'The 1930 helpline, to share with your parents', '5 minutes'),
    ],
    steps=[
        'Ask your parents for a money conversation, explaining why. Choose a calm time.',
        'Fill in the parents\' money map together, writing only what they are comfortable sharing.',
        'Mark the dangerous gaps: health cover, emergency money, risky deposits, debts, missing nominees or documents.',
        'Agree one action for each gap, with who does it and by when.',
        'If you have siblings, agree contributions and tasks in writing.',
        'Add the support to your own Budget tab as a planned line.',
    ],
    proof='The parents\' money map (with private numbers covered or left out), the gaps and actions, and any sibling agreement, saved in 11 Big goals.',
    templates=[
        ('parents\' money map', """
Income (monthly): pension ____ interest ____ rent/farm ____ from children ____
Savings: bank ____ post office ____ co-op ____ chitty ____ gold (pavan) ____
Health cover: scheme ____ private policy ____ eligible for KASP? ____ Medisep (pensioners)? ____
Debts: ____
Documents kept at: ____   Nominees checked? ____
Monthly expenses: ____ of which medicines ____
Biggest worry (in their words): ____
""", ''),
        ('sibling support agreement', """
Monthly contribution:  ____ ₹____   ____ ₹____   ____ ₹____
Big expenses (medical, repairs) shared in proportion: ___% / ___% / ___%
Tasks: hospital visits ____ paperwork ____ bills ____
Review every year in ____ (month)
""", ''),
    ],
    mistakes=[
        ('Taking over without asking.', 'It is their money. Offer help; let them decide.'),
        ('Waiting for a crisis to talk.', 'In a hospital corridor there is no time to find papers or compare options.'),
        ('Funding parents from your retirement savings.', 'Use a budget line and an emergency fund; protect your own future too.'),
        ('Unspoken sibling arrangements.', 'Write the agreement down. Clarity protects relationships.'),
    ],
    quiz=[
        {'q': 'What is usually the biggest financial risk for older parents?', 'o': ['A large health expense', 'A small electricity bill', 'Too much gold', 'Low phone balance'], 'a': 'A', 'why': 'Hospital costs can wipe out savings; health cover comes first.'},
        {'q': 'Which scheme is meant for regular income for people aged 60 and above?', 'o': ['SCSS', 'SSA', 'KVP', 'ELSS'], 'a': 'A', 'why': 'The Senior Citizens Savings Scheme pays quarterly interest (8.2% in October to December 2026).'},
        {'q': 'How should siblings share support fairly?', 'o': ['Agree contributions by ability and tasks in writing, and review yearly', 'Always equally, regardless of income', 'Whoever lives closest pays everything', 'Never discuss it'], 'a': 'A', 'why': 'A written, fair agreement prevents resentment.'},
        {'q': 'Where should support for parents come from in your own plan?', 'o': ['A planned budget line and your emergency fund', 'Your retirement savings', 'A personal loan', 'A loan app'], 'a': 'A', 'why': 'Protect your own future while you help.'},
    ],
    study='Kerala\'s senior health cover options, SCSS and MIS rates and the 1930 helpline',
    action='Make a money map with your parents, agree actions for the dangerous gaps and, if relevant, a sibling agreement',
)

LESSONS = [L1, L2, L3, L4]

MODULE = module(
    M,
    title='Big life goals',
    weeks=(23, 24), hours=7.5,
    overview="""
Plan the big things life brings: a wedding, a vehicle, a home, children's education and support for your parents, with real numbers, without debt traps, and in agreement with your family.

Big goals are where families most often borrow, pledge gold or sell land, usually because the cost arrived before the plan did. This module turns each one into a funded goal: a realistic cost, a future value, a monthly saving and a place for the money to wait, chosen by time horizon.

It also covers the decisions that numbers alone can't settle, such as whether to buy a house now or keep renting, how to talk about a wedding budget, and how siblings can share support for parents fairly. Your **Big Goals** tab becomes part of your final plan.
""",
    outcomes=[
        'Turn weddings, vehicles and other big purchases into funded goals with total costs',
        'Compare renting and buying a home with several scenarios',
        'Plan a child\'s education with a saving mix, a glide path and backup options',
        'Map your parents\' finances with them and close the dangerous gaps',
        'Agree family money decisions in writing',
    ],
    lessons=LESSONS,
    project='My big goals plan',
    project_steps=[
        'Complete the Big Goals tab: every big goal with future cost, monthly saving and where the money waits.',
        'Add up the monthly savings for all big goals and compare with what your budget allows. Use the four levers (later, less, more income, drop) until it fits.',
        'Attach your rent-or-buy decision and your parents\' plan (or "not applicable now").',
        'Update your Budget tab with the new monthly savings lines and your standing instructions.',
        'Share the plan with the family members it affects.',
    ],
    project_proof='Your Big Goals tab with totals that fit your budget, the rent-or-buy decision and the parents\' plan, saved in 11 Big goals.',
    rubric=[
        ('Costs', 'Guesses', 'Some quotes', 'Real costs, total cost of ownership where relevant, inflation applied'),
        ('Funding', 'None', 'Monthly amounts, not in the budget', 'Monthly savings in the budget with standing instructions'),
        ('House decision', 'Emotional only', 'One scenario', 'Three scenarios plus the four questions'),
        ('Education', 'Not planned', 'Amount only', 'Saving mix, glide path and backup (or not applicable)'),
        ('Family', 'Not discussed', 'Discussed', 'Agreed in writing with the people affected'),
    ],
    short=[
        'List your big goals with costs and monthly savings (FIN-M11-L01).',
        'Answer the four house questions (FIN-M11-L02).',
        'Fill in the parents\' money map, even partly (FIN-M11-L04).',
    ],
    flashcards=[
        ('Total cost of ownership (vehicle)', 'EMI + insurance + fuel + servicing + running costs + loss of value.'),
        ('Dowry Prohibition Act, 1961', 'Giving or taking dowry: at least 5 years\' imprisonment and a fine.'),
        ('Rent-or-buy comparison', 'Wealth after 10 years: house value minus loan left, vs investments from renting and investing the difference.'),
        ('Four house questions', 'Will I stay 7–10 years? EMI under a third of pay? Legally clean, K-RERA registered? Fits my other goals?'),
        ('Education inflation in this course\'s examples', '7% a year (an assumption).'),
        ('Education glide path', 'Move education money step by step to safe options in the last 3–5 years.'),
        ('First gap to close for parents', 'Health cover.'),
    ],
    mistakes=[
        ('Planning big goals alone when the family pays.', 'Agree budgets with the people involved, in writing.'),
        ('Borrowing for events and status.', 'Loans for celebrations and showy purchases delay every other goal.'),
        ('Giving up retirement for children or parents.', 'Help others from a planned budget line, not from your future.'),
    ],
    project_week=24,
)
