from common import lesson, module, link, rules, xref, table, fence, Q, RULE, ASOF, CHECK

SAFE = f'This lesson explains the law so you can spot issues and ask good questions. It is **not legal advice**. Only an advocate can advise on a specific property, and only licensed professionals can draft, survey or certify. Everything here is {RULE}.'

L1 = lesson(
    4, 1,
    outcome='You can explain how property is legally transferred in Kerala (Transfer of Property Act, Registration Act, Kerala stamp duty) and calculate the stamp duty and registration fee on a typical sale.',
    split='25 minutes reading, 30 minutes on the calculation and the action task',
    core=f"""
{SAFE}

**1. Transfer of Property Act, 1882 (TPA).** The central law on transferring property between living persons in India.
- **Section 54** defines sale as a transfer of ownership for a price. For tangible immovable property worth **₹100 or more**, a sale can be made **only by a registered instrument** ({link('tpa-54', 'Section 54 on Indian Kanoon')}).
- The same section says a **contract for sale** (an agreement to sell) **does not by itself create any interest** in the property. That is why an agreement and a token advance do not make the buyer the owner: only the registered sale deed does.
- The TPA also covers mortgages, leases, exchanges and gifts (each is a different kind of transfer with its own document; RE-M05).

**2. Registration Act, 1908.** It says which documents must be registered and what happens if they are not ({link('reg-act', 'iPleaders explainer')}).
- **Section 17 (compulsory registration):** includes gift deeds of immovable property, other documents that create or transfer rights in immovable property worth ₹100 or more, leases for more than one year, and (since a 2001 amendment) agreements relied on for part-performance under TPA section 53A.
- **Section 49 (effect of non-registration):** an unregistered document that should have been registered does not affect the property and generally cannot be used as evidence of the transaction (with narrow exceptions).
- **Section 23:** documents should be presented for registration within **four months** of execution.
- Registration happens at the **Sub-Registrar Office (SRO)** that has jurisdiction over the property, with the parties, two witnesses, ID proofs and photographs, and the stamp duty and fee paid.

**3. Kerala stamp duty and registration fee** (Kerala Stamp Act and the Registration Department's fee table; rates reported by {link('sy-stamp', 'Square Yards, updated July 2026')}; {CHECK}):
- **Sale deed:** stamp duty **8%** plus registration fee **2%**, charged on the **higher of the sale price or the government fair value**.
- **Flats or apartments** transferred within six months of getting the building number: stamp duty raised to **7%** in the 2023 Kerala Budget ({link('om-flat7', 'Onmanorama')}).
- **Gift or settlement to family members:** lower rates (reported as 2% stamp duty); non-family gifts are charged like a sale.
- **Lease up to one year:** reported as 1% of the rent; longer leases cost more.
- **General power of attorney** for sale: reported as a fixed amount (₹1,000).
- Stamp duty is paid by **e-stamp** (online or through licensed vendors). The buyer usually pays, but the agreement can say otherwise.

**4. Fair value.** The government notifies a minimum value per are for each survey number (RE-M03-L03, RE-M07-L01). If the declared price is below the fair value, duty is still charged on the fair value. Declaring a lower price than actually paid (and paying the rest in cash) is **tax evasion and creates black money**: never take part in it (RE-M21).
""",
    example="""
A buyer agrees to buy 10 cents in Kakkattil for **₹22 lakh** (₹2.2 lakh per cent). The fair value for the survey number works out to ₹68,000 per cent, so ₹6.8 lakh for the plot. Duty is charged on the higher figure, ₹22 lakh.

Someone suggests "showing ₹7 lakh in the deed and paying the rest in cash to save stamp duty". That is illegal: it understates the price to the government, breaks cash limits (RE-M04-L05), makes the seller hide capital gains, and leaves the buyer with a deed showing a false price (a problem for loans and future resale). A professional broker refuses and explains why.
""",
    calc="""
**Cost of registering a ₹22 lakh sale deed** (illustrative rates; check current rules):
- Stamp duty 8%: 22,00,000 × 0.08 = **₹1,76,000**
- Registration fee 2%: 22,00,000 × 0.02 = **₹44,000**
- Total government charges: **₹2,20,000** (10% of the price)
- Plus the document writer's or advocate's fee, EC and copy charges (ask locally).

**Higher of price or fair value:** if the price were ₹6 lakh but fair value ₹6.8 lakh, duty would be on ₹6.8 lakh: 6,80,000 × 0.10 = ₹68,000.

Sheets: `=MAX(B1,B2)*0.08` for stamp duty, `=MAX(B1,B2)*0.02` for the fee, where B1 is the price and B2 is the fair value (the full cost calculator is in RE-M08-L02).
""",
    rules_rows=[
        ('TPA s.54', 'Sale of immovable property worth ₹100+ only by registered instrument; an agreement to sell creates no interest', 'Indian Kanoon'),
        ('Registration Act s.17, s.49, s.23', 'Compulsory registration; unregistered documents don\'t affect property; present within 4 months', 'iPleaders'),
        ('Stamp duty and fee on sale', '8% + 2% on the higher of price or fair value', 'Square Yards, July 2026'),
        ('Flats within 6 months of building number', '7% stamp duty', 'Onmanorama, February 2023'),
    ],
    pro="""
- **Registered document writer or advocate:** drafts the sale deed. In Kerala, licensed document writers and advocates prepare documents for registration; a broker must not draft deeds.
- **Advocate:** any question on whether a past document was valid, registered correctly or properly stamped.
""",
    resources=[
        ('tpa-54', 'Read section 54 slowly; note "registered instrument" and "contract for sale"', '10 minutes'),
        ('reg-act', 'Read the parts on sections 17 and 49', '15 minutes'),
        ('sy-stamp', 'Read the Kerala stamp duty table; note which rates apply to sale, gift, lease and POA', '10 minutes'),
    ],
    steps=[
        'Write in your own words (5 to 8 lines) why a token advance and an agreement do not make someone the owner.',
        'Using the stamp duty formula, calculate total government charges for three local listings (price and an estimated fair value).',
        'Visit or call a document writer\'s office near your SRO (Kuttiady, Nadapuram or Vadakara, whichever is yours) and ask: what papers they need for a sale deed, their fee range and the usual time. Use this as the first part of your document-writer interview (RE-M11-L01).',
        'Note where your local SRO is and its working days.',
    ],
    proof='Your explanation, three calculations and notes from the document writer conversation.',
    templates=[('Registration cost quick sheet', """REGISTRATION COST QUICK SHEET (rates as of ______; check current rules)
B1 Sale price ₹        B2 Fair value ₹ (cents x fair value per cent)
B3 Duty base           =MAX(B1,B2)
B4 Stamp duty (8%)     =B3*0.08
B5 Registration (2%)   =B3*0.02
B6 Writer/advocate fee (ask locally)
B7 EC and copies
B8 TOTAL               =SUM(B4:B7)
SRO for this village: ______   Document writer: ______ (fee ______)""")],
    mistakes=[
        ('Thinking an agreement makes you the owner.', 'Only a registered sale deed transfers ownership.'),
        ('Calculating duty on the price when fair value is higher.', 'Duty is on the higher figure.'),
        ('Agreeing to undervalue the deed.', 'It is illegal, creates black money and hurts the buyer later.'),
    ],
    fraud="""
**Unregistered "sale" papers.** Some sellers offer land on a stamp-paper agreement, a notarised affidavit or a power of attorney "instead of registration to save money". None of these transfers ownership. Buyers lose their money when the real owner sells to someone else.
""",
    quiz=[
        Q('Under TPA section 54, how is a sale of immovable property worth ₹100 or more made?', 'Only by a registered instrument', 'By an oral agreement', 'By paying a token advance', 'By a notarised affidavit', why='A contract for sale creates no interest.'),
        Q('On what amount is Kerala stamp duty on a sale charged?', 'The higher of the sale price or the fair value', 'Always the fair value', 'Always the price', 'Half the price', why='Fair value sets the minimum.'),
        Q('What are the reported stamp duty and registration fee on a sale deed in Kerala?', '8% and 2%', '5% and 1%', '2% and 1%', '12% and 2%', why='Square Yards, July 2026; check current rules.'),
        Q('Within how long should a document normally be presented for registration?', 'Four months of execution', 'One week', 'Two years', 'There is no limit', why='Registration Act section 23.'),
    ],
    study='read the lesson and TPA section 54',
    action='calculate registration costs for three listings and talk to a document writer',
)

L2 = lesson(
    4, 2,
    outcome='You can explain what the RERA Act and K-RERA require of builders and agents, when a project must register, and how buyers can check a project and complain.',
    split='20 minutes reading, 35 minutes on the K-RERA site',
    core=f"""
{SAFE}

**The Real Estate (Regulation and Development) Act, 2016 (RERA)** was passed in March 2016 and came fully into force on **1 May 2017** ({link('wp-rera', 'Wikipedia summary')}). Each state has an authority; Kerala's is **K-RERA** ({link('krera', 'rera.kerala.gov.in')}).

**For projects (builders and promoters):**
- Projects above the threshold must register before advertising or selling. In Kerala, projects with land **above 500 sq m or more than 8 apartments** must register ({link('om-rera', 'Onmanorama')}, {CHECK}).
- **70%** of buyers' money must go into a separate bank account and be used only for that project's land and construction.
- Prices must be quoted on **carpet area**.
- The promoter must give project details (approvals, layout, schedule) on the RERA website and is liable for structural defects for five years after possession.
- Buyers can complain to K-RERA about delays, defects or false promises.

**For real estate agents:**
- An agent who facilitates the sale of units in RERA-registered projects must **register with K-RERA** and quote the registration number in every advert and deal ({link('wp-rera', 'Wikipedia')}).
- Reported K-RERA agent fees: **₹25,000** for an individual; ₹2 lakh to ₹2.5 lakh for firms or companies (sources differ: {link('tg-krera', 'TaxGuru')}, {link('om-rera', 'Onmanorama')}). Registration is valid for a fixed period and must be renewed.
- Penalty for an unregistered agent: reported as **₹10,000 per day** of default ({link('om-rera', 'Onmanorama')}).
- Agent duties: keep books of account, not mislead buyers, give buyers project information and help them with documents.
- How to register: RE-M10-L01.

**What RERA does not cover:** resale of individual plots and houses between owners, and small projects below the threshold. Most of the deals you start with (resale land, houses and rentals) fall outside RERA, but you must still act honestly under general law, and you need K-RERA registration before handling units in registered projects.
""",
    example="""
A builder in Kozhikode city advertises "2 BHK from ₹48 lakh, 1,150 sq ft" for a 40-flat project. Sachin checks:
1. Is the project on the K-RERA site? A 40-flat project must be.
2. Does the advert show the K-RERA project number?
3. Is the price on carpet area? The project page shows carpet area 780 sq ft for that flat, so the "1,150 sq ft" is super built-up. Real price per carpet sq ft: 48,00,000 ÷ 780 ≈ **₹6,150**, not ₹4,170.
4. Are the approvals and completion date listed?

If he wants to bring buyers to this project and earn commission, he needs his own K-RERA agent registration first.
""",
    rules_rows=[
        ('RERA in force', 'Fully from 1 May 2017', 'Wikipedia'),
        ('Kerala project threshold', 'More than 500 sq m of land or more than 8 apartments', 'Onmanorama'),
        ('Agent registration fee', 'Individual ₹25,000; firms reported ₹2 lakh to ₹2.5 lakh', 'TaxGuru; Onmanorama'),
        ('Unregistered agent penalty', 'Reported ₹10,000 per day', 'Onmanorama'),
        ('Separate account', '70% of buyer payments in a project account', 'Wikipedia'),
    ],
    pro="""
- **Advocate:** for complaints, disputes with builders or interpreting an agreement for sale with a builder.
""",
    resources=[
        ('krera', 'Explore the project search, agent search and complaint sections', '20 minutes'),
        ('wp-rera', 'Read the sections on obligations of promoters and agents', '15 minutes'),
        ('om-rera', 'Read the Kerala thresholds and fees', '5 minutes'),
    ],
    steps=[
        'On the K-RERA site, find two registered projects in Kozhikode district and note: project number, promoter, approvals shown and completion date.',
        'Search the agent list for registered agents in Kozhikode and note how many you find (names don\'t need to be shared).',
        'Find one flat or villa advert (newspaper, portal or social media) and check whether it shows a K-RERA number and carpet area.',
        'Write a 5-point "RERA check" you will use for every project.',
    ],
    proof='Notes on two projects, the agent count, one advert check and your RERA check.',
    templates=[('RERA project check', """RERA PROJECT CHECK            Project ______ Date ______
1 Registered with K-RERA? number ______ (from rera.kerala.gov.in, not from the brochure)
2 Promoter name matches the brochure and agreement?  Y/N
3 Approvals shown (permit, layout, NOCs)? ______
4 Carpet area of this unit ______ sq ft; price per carpet sq ft ______
5 Completion date ______; any complaints or orders listed? ______
Agent: my K-RERA registration no. ______ quoted on all adverts?  Y/N""")],
    mistakes=[
        ('Marketing project units without K-RERA registration.', 'Register first (RE-M10-L01).'),
        ('Trusting the brochure\'s RERA number.', 'Check it on the K-RERA site.'),
        ('Comparing super built-up prices.', 'Compare on carpet area.'),
    ],
    fraud="""
**Fake or borrowed RERA numbers.** Some unregistered projects print another project's RERA number or a "RERA applied" note. Always look the number up and check the promoter and location match.
""",
    quiz=[
        Q('Which projects must register with K-RERA?', 'Projects above 500 sq m of land or with more than 8 apartments', 'Every plot sale', 'Only government projects', 'Only commercial buildings', why='Thresholds reported by Onmanorama; check current rules.'),
        Q('What share of buyer payments must go into a separate project account?', '70%', '10%', '50%', '100%', why='RERA requires it to be used for the project.'),
        Q('What must a registered agent show in adverts?', 'Their K-RERA registration number', 'Their Aadhaar number', 'The seller\'s phone number', 'Nothing', why='Agents must quote the registration number.'),
        Q('Does RERA cover a resale of a single house between two owners?', 'Generally no; general law applies', 'Yes, always', 'Only in cities', 'Only if a broker is involved', why='RERA mainly covers projects and their agents.'),
    ],
    study='read the lesson and the RERA summary',
    action='check two K-RERA projects and one advert, and write your RERA check',
)

L3 = lesson(
    4, 3,
    outcome='You can explain the basics of the Paddy Land and Wetland Act (data bank, conversion, fees) and the Kerala Land Reforms Act, and why they matter for buying land in Kerala.',
    split='25 minutes reading, 30 minutes on the action task',
    core=f"""
{SAFE}

**Kerala Conservation of Paddy Land and Wetland Act, 2008.** Kerala protects paddy fields and wetlands because they matter for food, water and flood control.
- **Paddy land and wetland** cannot be filled, converted or used for other purposes without permission.
- A **data bank** lists land recorded as paddy land or wetland in each local body. Land in the data bank is very hard to convert.
- **Land not in the data bank** but recorded as "nilam" (paddy land) in revenue records can apply for a change of land type through the Revenue Department (the RDO), under **section 27A**, with a fee.
- **Conversion fee:** for land above **25 cents** (up to 1 acre), a fee of 10% of the fair value applies; the Supreme Court in 2025 held that holdings above 25 cents cannot claim the exemption for the first 25 cents ({link('sc-paddy', 'LiveLaw on State of Kerala v. Moushmi Ann Jacob')}). Rules for smaller holdings and larger areas differ; {CHECK}.
- Filling paddy land without permission can lead to restoration orders and penalties, and building permits will be refused.

**Why it matters:** much cheap land in Kozhikode district is cheap because it is **nilam** or in the data bank. A buyer may be told "it can be converted easily". The land type in the tax receipt and the data bank status must be checked, and an advocate consulted.

**Kerala Land Reforms Act, 1963 (as amended in 1969)** ({link('klr-act', 'Act on India Code')}; {link('wp-landreform', 'history on Wikipedia')}):
- Abolished landlord-tenant (jenmi) systems and gave ownership to cultivating tenants and **kudikidappukars** (hutment dwellers).
- Set a **ceiling** on how much land a family can hold (roughly 12 to 15 standard acres depending on family size, with exemptions such as plantations).
- Some land carries a history: purchase certificates from the Land Tribunal, land assigned by the government with conditions on sale (patta land), or plantation land with restrictions. These need an advocate's check.

**Other land-type flags:**
- **Puramboke:** government land (road margins, river banks); cannot be bought from a private seller.
- **Assigned land (patta):** often has restrictions on sale for a period.
- **Plantation land:** may be exempt from ceilings but restricted from conversion or fragmentation.
- **Forest and ecologically fragile land:** RE-M04-L04.
""",
    example="""
A WhatsApp message offers "25 cents near Kuttiady river at ₹60,000 per cent, very cheap, house can be built". Sachin asks for the land tax receipt: land type **nilam**. He checks with the village office whether it is in the paddy land data bank. It is.

Result: no building permit, no conversion, and the "cheap" price reflects that. If someone bought it to build a house, the money would be stuck. Sachin tells his contact clearly: "This land is in the data bank. It can be used for farming; you can't build on it under current rules. Please talk to an advocate before paying anything."
""",
    calc="""
**Conversion fee (illustrative, if conversion is allowed):** 40 cents of nilam not in the data bank; fair value ₹70,000 per cent.
- Fair value of 40 cents: 40 × 70,000 = ₹28,00,000
- Fee at 10% of fair value (holding above 25 cents): 28,00,000 × 0.10 = **₹2,80,000**
- Plus time (months), the advocate's fee and the risk that permission is refused.
Rules on how the fee is calculated change; check with the RDO and an advocate.
""",
    rules_rows=[
        ('Paddy Land Act data bank', 'Data bank land is very hard to convert; filling without permission is illegal', 'Act and LiveLaw summary'),
        ('Section 27A conversion fee', '10% of fair value for holdings above 25 cents up to 1 acre; no exemption for the first 25 cents', 'LiveLaw, Supreme Court 2025'),
        ('Land Reforms Act', 'Tenancy abolished; ceiling on holdings; restrictions on some land types', 'India Code; Wikipedia'),
    ],
    pro="""
- **Advocate:** for any land typed nilam, in the data bank, assigned (patta), plantation or with a Land Tribunal history.
- **Revenue office (RDO):** for conversion applications, but go with an advocate's advice.
""",
    resources=[
        ('sc-paddy', 'Read the summary of the Supreme Court decision on conversion fees', '10 minutes'),
        ('wp-landreform', 'Read the history and main effects of land reform in Kerala', '15 minutes'),
        ('klr-act', 'Skim the contents of the Act to see its scope (don\'t try to read all of it)', '10 minutes'),
    ],
    steps=[
        'Ask your village office or panchayat how a person can check whether a survey number is in the paddy land data bank, and note the answer.',
        'Find two listings in your area that mention "nilam", "vayal", "paddy" or "conversion possible" and note what the listing claims.',
        'Ask one local broker how often buyers get stuck with nilam land and what they check (part of your broker interviews, RE-M11-L01).',
        'Write a "land type check" for your toolkit.',
    ],
    proof='The data bank procedure, two listings with notes and your land type check.',
    templates=[('Land type check', """LAND TYPE CHECK       Survey/resurvey ______ Village ______
Land type in tax receipt: purayidam / nilam / other ______
In the paddy land data bank?  Y/N (source and date ______)
If nilam not in data bank: conversion needed; fee estimate ______; advocate consulted? Y/N
Puramboke strip or road margin included?  Y/N
Assigned (patta) / Land Tribunal / plantation history?  Y/N -> advocate
Ecologically sensitive or CRZ? (RE-M04-L04)  Y/N
Decision: OK to proceed / advocate first / reject""")],
    mistakes=[
        ('Believing "conversion is easy".', 'Data bank land is very hard to convert; check first.'),
        ('Ignoring the land type in the tax receipt.', 'It is one of the first things to check.'),
        ('Advising buyers on conversion yourself.', 'Send them to an advocate.'),
    ],
    fraud="""
**Selling nilam as building land.** Some sellers fill paddy land and sell it as "purayidam" plots; buyers later face restoration orders and no permits. Check the land type in revenue records and the data bank, not what the land looks like now.
""",
    quiz=[
        Q('What does the paddy land data bank list?', 'Land recorded as paddy land or wetland that is protected', 'All land for sale', 'Builders\' projects', 'Fair values', why='Data bank land is very hard to convert.'),
        Q('Under the 2025 Supreme Court decision, what conversion fee applies to holdings above 25 cents (up to 1 acre)?', '10% of fair value, with no exemption for the first 25 cents', 'No fee', '50% of market value', '1% of price', why='State of Kerala v. Moushmi Ann Jacob.'),
        Q('What is puramboke land?', 'Government land such as road margins and river banks', 'Private garden land', 'Plantation land', 'Flat land', why='It cannot be bought from a private seller.'),
        Q('What did the Kerala Land Reforms Act do?', 'Abolished landlord-tenant systems and set land ceilings', 'Set stamp duty', 'Created RERA', 'Regulated rent', why='It reshaped land ownership in Kerala.'),
    ],
    study='read the lesson and the Supreme Court summary',
    action='find the data bank procedure, check two listings and write your land type check',
)

L4 = lesson(
    4, 4,
    outcome='You can explain how Kerala building rules, the building-permit system, CRZ and ecologically sensitive areas affect what can be built on a plot.',
    split='25 minutes reading, 30 minutes on the action task',
    core=f"""
{SAFE}

**Kerala building rules.** Construction is controlled by the **Kerala Panchayat Building Rules, 2019 (KPBR)** in grama panchayats and the **Kerala Municipality Building Rules, 2019 (KMBR)** in municipalities and corporations ({link('kpbr', 'KPBR 2019 PDF from LSGD')}; amended since; {CHECK}). They set:
- **Setbacks:** minimum distance from the plot boundary and from roads (wider for main roads).
- **Coverage and FAR** (floor area ratio): how much of the plot can be built on and the total floor area allowed.
- **Access:** minimum road width for certain building types.
- **Parking, rainwater harvesting, sanitation** and other requirements.
- **Low-risk buildings** (small houses) may follow a simplified permit process.

**Permit systems.** Building permits come from the local body. Kerala moved from **Sanketham** (the old online permit system) to **K-SMART**: Sanketham stopped taking new applications from grama panchayats from 29 March 2025 ({link('sanketham', 'Sanketham notice')}), and K-SMART was rolled out to all panchayats in April 2025 (earlier to municipalities and corporations) ({link('week-ksmart', 'The Week')}). Plans are prepared and submitted by a **licensed engineer, architect or building designer** (empanelled with the local body), not by a broker.

After construction, the local body issues an **occupancy certificate** (OC) or completion approval, then a **building number** and property tax assessment (RE-M05-L04).

**Coastal Regulation Zone (CRZ).** Land near the sea, backwaters and tidal rivers falls under the CRZ Notification, 2019, applied through Kerala's **Coastal Zone Management Plan (CZMP)**. The revised CZMP was approved in September 2024; in many CRZ-III A areas the no-development zone was reduced from 200 m to 50 m ({link('om-czmp', 'Onmanorama')}). Rules differ by category and area; a CRZ clearance or check may be needed before building.

**Ecologically sensitive areas (ESA).** The Western Ghats ESA has gone through several draft notifications; the sixth draft (August 2024) covered about 56,800 sq km across six states, including many Kerala villages, and restricts mining, quarrying and large construction ({link('air-esa', 'All India Radio')}). It is a **draft**, not final. Some hill villages in Kozhikode district (for example in the Kuttiady and Thamarassery areas) may be listed; {CHECK}.

**Disaster risk.** The **KSDMA hazard maps** show flood and landslide zones ({link('ksdma', 'KSDMA')}). After the 2018 and 2019 floods and landslides, this check is essential for buyers.
""",
    example="""
A buyer from the Gulf wants to build a two-storey house on a 6-cent plot in a panchayat near Kuttiady. The plot fronts a narrow panchayat road. Sachin cannot say whether the house is permitted (that is the engineer's job), but he can warn early:
- Setbacks from the road and boundaries will reduce the usable area of a 6-cent plot.
- The road width affects what can be built.
- He checks the KSDMA map: the plot is outside mapped flood zones but near a landslide-susceptible slope 2 km uphill.
- The village is listed in the draft ESA notification; he notes that a house is usually not the target of the restrictions, but the buyer should check with an advocate and the panchayat.

He recommends a licensed engineer look at the plot before the buyer pays an advance.
""",
    rules_rows=[
        ('Building rules', 'KPBR 2019 (panchayats) and KMBR 2019 (municipalities), as amended', 'LSGD PDF'),
        ('Permit system', 'Sanketham closed to new panchayat applications from 29 March 2025; K-SMART in all panchayats from April 2025', 'Sanketham notice; The Week'),
        ('CZMP 2024', 'Revised plan approved September 2024; CRZ-III A no-development zone 200 m to 50 m in many areas', 'Onmanorama'),
        ('Western Ghats ESA', 'Sixth draft notification August 2024, about 56,800 sq km; not final', 'All India Radio'),
    ],
    pro="""
- **Licensed engineer, architect or building designer:** checks setbacks, FAR and permits and prepares plans. A broker must never promise "you can build X".
- **Advocate:** for CRZ, ESA or other environmental issues.
""",
    resources=[
        ('kpbr', 'Skim the contents and find the setback and coverage rules (search the PDF)', '15 minutes'),
        ('ksdma', 'Open the hazard maps and find your own area', '15 minutes'),
        ('week-ksmart', 'Read about the K-SMART roll-out', '5 minutes'),
        ('air-esa', 'Read about the ESA draft', '5 minutes'),
    ],
    steps=[
        'Open the KSDMA flood and landslide maps for your panchayat and note which areas are marked.',
        'Ask at your panchayat (or check its K-SMART information) what papers a low-risk house permit needs and how long it takes.',
        'Ask one licensed building designer or engineer what they check first on a small plot, and their fee range for a permit drawing.',
        'Add the results to a "can it be built?" checklist for your toolkit.',
    ],
    proof='Hazard map notes, permit requirements and notes from the engineer or designer.',
    templates=[('Can it be built? checklist', """CAN IT BE BUILT? (early warning only; engineer decides)
Local body: panchayat / municipality / corporation ______  Rules: KPBR / KMBR
Plot area ______ cents; road width ______ m; frontage ______ m
Setbacks likely to reduce buildable area?  Y/N (engineer check)
KSDMA flood zone? Y/N   Landslide zone? Y/N   (map date ______)
CRZ (near sea, backwater, tidal river)?  Y/N -> CZMP check
Western Ghats ESA village (draft)?  Y/N -> advocate
Land type purayidam? (RE-M04-L03)  Y/N
Engineer/designer consulted: ______ ; fee ______""")],
    mistakes=[
        ('Promising buyers they can build a certain house.', 'Only a licensed engineer can check that.'),
        ('Skipping the hazard map.', 'Check flood and landslide risk on every plot.'),
        ('Treating the ESA draft as final, or ignoring it.', 'Note it, explain it\'s a draft and send the buyer to an advocate.'),
    ],
    fraud="""
**"Permit guaranteed" plots.** Some sellers promise a permit, or show an old permit for a different plan or plot. Permits are specific to a plot and plan; ask for the permit number and verify it with the local body.
""",
    quiz=[
        Q('Which building rules apply in grama panchayats?', 'Kerala Panchayat Building Rules, 2019', 'Kerala Municipality Building Rules only', 'RERA rules', 'The Rent Control Act', why='KMBR apply in municipalities.'),
        Q('Which system replaced Sanketham for new panchayat building permits in 2025?', 'K-SMART', 'PEARL', 'ReLIS', 'e-Rekha', why='Rolled out in April 2025.'),
        Q('Is the 2024 Western Ghats ESA notification final?', 'No, it is a draft', 'Yes', 'It was cancelled in 2017', 'It applies only to cities', why='Sixth draft, August 2024.'),
        Q('Who should check setbacks and FAR for a plot?', 'A licensed engineer, architect or building designer', 'The broker', 'The seller', 'A friend', why='Brokers give early warnings only.'),
    ],
    study='read the lesson and open the hazard maps',
    action='check hazard maps, permit requirements and an engineer\'s view for your area',
)

L5 = lesson(
    4, 5,
    outcome='You can explain the key points of the Kerala Rent Control Act, the Benami Act and cash-transaction limits, and refuse any deal that breaks them.',
    split='25 minutes reading, 30 minutes on the action task',
    core=f"""
{SAFE}

**Kerala Buildings (Lease and Rent Control) Act, 1965** ({link('rent-act', 'Act on India Code')}). It covers buildings let for rent in areas where it applies.
- **Fair rent:** the **Rent Control Court** can fix a fair rent on application (section 5).
- **Advance:** the Act allows a landlord to take an advance of **up to one month's rent** (section 8). In practice, large deposits (several months, or "lease" deals with big lump sums) are common in Kerala; tell clients the law's limit and send disputes to an advocate.
- **Eviction:** a landlord can evict a tenant only through the Rent Control Court on grounds listed in **section 11** (for example non-payment of rent, subletting without consent, damage, the landlord's own bona fide need). Cutting water or electricity, or locking out a tenant, is not allowed.
- **Rental agreements:** leases over one year must be registered (Registration Act, RE-M04-L01). Many owners use 11-month agreements; these still need proper stamping (RE-M05-L03).
- The Centre published a Model Tenancy Act (2021) as a model law for states; whether Kerala has adopted anything based on it is unverified in this course, so treat the 1965 Act as the law and {CHECK}.

**Benami Transactions (Prohibition) Amendment Act, 2016.** A benami transaction is buying property in someone else's name while the real buyer pays and benefits (for example to hide black money). It is illegal; penalties include **rigorous imprisonment of 1 to 7 years and a fine up to 25% of the fair market value**, and the property can be confiscated ({link('bb-benami', 'BankBazaar explainer')}). Buying in a spouse's or child's name using known, taxed income is **not** benami. A broker who knowingly helps arrange a benami deal is at risk too.

**Cash limits under income tax law.** Since the Income-tax Act, 2025 replaced the 1961 Act from 1 April 2026, section numbers have changed; the rules below are described by what they do ({CHECK}):
- **Property advances and deposits:** accepting **₹20,000 or more in cash** as an advance or deposit for a property transfer is prohibited (old section 269SS), with a penalty equal to the amount.
- **Any receipt:** receiving **₹2 lakh or more in cash** in a single transaction or day is prohibited (old section 269ST), with a penalty equal to the amount.
- Large property deals are also reported to the tax department (registration offices report purchases above a threshold: reported as ₹45 lakh from FY 2026-27, {link('taxscan-sft', 'Taxscan')}).
**Your rule:** all token advances, advances and commission are paid by bank transfer, UPI or cheque, with receipts.
""",
    example="""
An owner in Kuttiady town wants to let a shop room for ₹15,000 a month with a ₹3 lakh "advance in cash" and no written agreement. Sachin explains:
1. The Rent Control Act allows an advance of up to one month's rent; large deposits are common but legally risky for the landlord if challenged. An advocate should draft the terms.
2. ₹3 lakh in cash breaks the cash limits; the deposit must go by bank transfer.
3. A written agreement, properly stamped (and registered if longer than one year), protects both sides.
4. If the tenant later fails to pay, eviction needs the Rent Control Court; the agreement and bank records will be the evidence.

The owner agrees to an advocate-drafted 11-month agreement and a bank-transfer deposit. Sachin's commission is also by UPI with a receipt.
""",
    rules_rows=[
        ('Rent Control Act s.5, s.8, s.11', 'Fair rent fixed by the Rent Control Court; advance up to one month\'s rent; eviction only on listed grounds through the court', 'India Code PDF'),
        ('Benami Act penalties', 'Rigorous imprisonment 1 to 7 years; fine up to 25% of fair market value', 'BankBazaar'),
        ('Cash advance limit for property', '₹20,000 or more in cash prohibited (old s.269SS; renumbered in the 2025 Act)', 'Income-tax Act, 1961 (old section); new section number unverified'),
        ('Cash receipt limit', '₹2 lakh or more in cash prohibited (old s.269ST; renumbered)', 'Income-tax Act, 1961 (old section); new section number unverified'),
        ('Reporting of property purchases', 'Reported threshold ₹45 lakh from FY 2026-27', 'Taxscan'),
    ],
    pro="""
- **Advocate:** rental agreements with unusual terms, any eviction, deposit disputes or a client who wants to buy "in someone else's name".
- **Chartered accountant:** questions about cash, reporting or the source of funds.
""",
    resources=[
        ('rent-act', 'Read sections 5, 8 and 11 (search the PDF for "fair rent", "advance" and "eviction")', '20 minutes'),
        ('bb-benami', 'Read what counts as benami and the exceptions', '10 minutes'),
        ('taxscan-sft', 'Read the FY 2026-27 property tax compliance summary', '10 minutes'),
    ],
    steps=[
        'Ask two local landlords or brokers what deposit is usual for houses and shops in your town, and whether agreements are written and stamped.',
        'Compare what they say with the Act\'s limit and write down the gap.',
        'Write a short "my money rules" statement for your business: no cash above legal limits, receipts for everything, no undervaluation, no benami.',
        'Add it to your owner mandate and client intake templates (RE-M10).',
    ],
    proof='Deposit notes from two people, the gap you found and your money rules.',
    templates=[('My money rules', """MY MONEY RULES (put on my website, cards and agreements)
1 All advances, deposits and commission by bank transfer, UPI or cheque, with receipts.
2 No cash advance of ₹20,000 or more for any property deal; no cash receipt of ₹2 lakh or more (check current rules).
3 I do not take part in undervalued deeds or "part in cash" deals.
4 I do not arrange purchases in another person's name to hide the real buyer.
5 Rental agreements are written, stamped and, if over one year, registered.
6 Disputes and evictions go to an advocate and the proper court.""")],
    mistakes=[
        ('Accepting a cash token "just this once".', 'Cash limits apply to every deal; use UPI or bank transfer.'),
        ('Promising landlords they can evict quickly.', 'Eviction needs the Rent Control Court.'),
        ('Ignoring a client\'s request to buy in a relative\'s name.', 'Ask why and send them to an advocate; refuse if it\'s to hide money.'),
    ],
    fraud="""
**Cash-heavy "deals".** A buyer who insists on paying mostly in cash is a red flag for black money or benami; a seller who wants cash may be hiding income or even not be the real owner. Insist on banking channels and walk away if they refuse.
""",
    quiz=[
        Q('Under the Kerala Rent Control Act, how can a landlord evict a tenant?', 'Only through the Rent Control Court on grounds in section 11', 'By cutting the electricity', 'By changing the locks', 'By a phone call', why='Self-help eviction is not allowed.'),
        Q('What advance does the 1965 Act allow a landlord to take?', 'Up to one month\'s rent', 'Up to ten months\' rent', 'Any amount', 'No advance at all', why='Section 8; large deposits are common but legally risky.'),
        Q('Which of these is NOT benami?', 'Buying in your spouse\'s name with your own taxed income', 'Buying in a driver\'s name to hide black money', 'Buying through a friend so the real buyer stays hidden', 'Paying for property held by a fake person', why='The Act has this exception.'),
        Q('What is the cash limit for advances for a property transfer?', 'Below ₹20,000; ₹20,000 or more in cash is prohibited', '₹5 lakh', 'No limit', '₹50,000', why='Renumbered in the 2025 Act; check current rules.'),
    ],
    study='read the lesson and sections 5, 8 and 11 of the Rent Act',
    action='compare local deposit practice with the law and write your money rules',
)

LESSONS = [L1, L2, L3, L4, L5]

MODULE = module(
    4,
    overview=f"""
The legal framework of Kerala real estate: the Transfer of Property Act, the Registration Act and stamp duty; RERA and K-RERA; the Paddy Land and Wetland Act and Land Reforms Act; building rules, permits, CRZ and ecologically sensitive areas; and the Rent Control Act, Benami Act and cash limits.

This is the longest and most important knowledge module. You are not learning to be a lawyer: you are learning enough to spot red flags, ask the right questions and know when an advocate, surveyor or engineer is needed. Everything is {RULE}.
""",
    outcomes=[
        'Explain how ownership legally transfers and calculate stamp duty and registration fees.',
        'Apply RERA and K-RERA rules for projects and agents.',
        'Spot land-type and land-reform risks.',
        'Explain how building rules, CRZ, ESA and hazard maps limit construction.',
        'Follow rent control, benami and cash rules in every deal.',
    ],
    lessons=LESSONS,
    project='a legal red-flag checklist for Kerala property',
    project_steps=[
        'Combine the registration cost sheet, RERA check, land type check, "can it be built?" checklist and money rules into one legal red-flag checklist.',
        'Test it on two local listings (one land, one house or flat) using public information only.',
        'For each red flag, write which professional you would call.',
        'Ask a local advocate or document writer to look at your checklist for 5 minutes, if they agree (or ask during your interview in RE-M11).',
    ],
    project_proof='The combined checklist and two tested listings with notes.',
    rubric=[
        ('Transfer and registration', 'Confuses agreement and sale', 'Knows the difference', 'Explains TPA s.54 and calculates duty correctly'),
        ('Land-type law', 'Not checked', 'Knows nilam is risky', 'Checks data bank, land type and land-reform flags'),
        ('Construction limits', 'Promises what can be built', 'Mentions rules', 'Checks hazard maps, CRZ, ESA and sends to an engineer'),
        ('Money and ethics', 'Accepts cash', 'Knows the limits', 'Has written money rules used in every deal'),
    ],
    short=[
        'Learn TPA s.54 and the 8% + 2% stamp duty rule.',
        'Write your money rules.',
    ],
    flashcards=[
        ('TPA s.54', 'Sale of ₹100+ immovable property only by registered instrument; an agreement creates no interest.'),
        ('Kerala sale duty', '8% stamp duty + 2% registration on the higher of price or fair value.'),
        ('K-RERA project threshold', 'More than 500 sq m or more than 8 apartments.'),
        ('K-RERA agent fee (individual)', '₹25,000 (reported).'),
        ('Paddy land data bank', 'Protected paddy land and wetland; very hard to convert.'),
        ('Building rules', 'KPBR 2019 (panchayats), KMBR 2019 (municipalities).'),
        ('Rent Act eviction', 'Only through the Rent Control Court on section 11 grounds.'),
        ('Cash advance limit', '₹20,000 or more in cash for property is prohibited.'),
    ],
    mistakes=[
        ('Trying to memorise every rule.', 'Learn the main ideas and where to check.'),
        ('Giving legal opinions.', 'Spot issues and refer to an advocate.'),
        ('Using old rates.', 'Date-stamp and check current rules every time.'),
    ],
    tools=[
        'Registration cost quick sheet (RE-M04-L01).',
        'RERA project check (RE-M04-L02).',
        'Land type check (RE-M04-L03).',
        '"Can it be built?" checklist (RE-M04-L04).',
        'My money rules (RE-M04-L05).',
    ],
    toolkit=[
        'Legal red-flag checklist (combining the five templates).',
        'My money rules, to be printed on agreements and cards.',
    ],
)
