from common import lesson, module, link, rules, xref, table, fence, Q, RULE

L1 = lesson(
    1, 1,
    outcome='You can classify any Kerala property by type, name everyone involved in a typical deal and what each is paid for, and map the players in your own area.',
    split='15 minutes reading, 40 minutes of field notes',
    core=f"""
**Property types you will meet in Kerala:**

- **Land (plots):** the most traded asset in rural and semi-urban Kerala. Recorded in revenue records by land type: **purayidam** (garden or dry land, generally buildable), **nilam** (paddy or wet land, protected by law, RE-M04-L03), **thottam** or plantation land, and others. A plot's legal type matters more than how it looks today.
- **Residential:** independent houses (the most common), villas in gated projects, flats/apartments (mostly in towns and cities such as Kozhikode, Kochi and Thiruvananthapuram), and rooms or portions let to tenants.
- **Commercial:** shop rooms (very common on town roads and junctions), office spaces, godowns, hotels and lodges, petrol pumps, hospitals and schools.
- **Agricultural:** coconut, arecanut, rubber and mixed farmland; paddy fields.
- **Plantation:** large holdings of rubber, tea, coffee, cardamom or pepper, mostly in the hills; land reforms law gave plantations special treatment, so converting plantation land to other uses can be legally sensitive (RE-M04-L03).
- **Special categories:** government-assigned (pattayam) land with restrictions, temple or trust land, puramboke (government) land, and land in coastal (CRZ) or ecologically sensitive areas.

**Who is involved in a typical deal:**

| Player | Role | How they are paid |
| --- | --- | --- |
| Owner/seller | Holds title; signs the deed | Sale price |
| Buyer | Pays; usually needs a loan or NRI funds | — |
| Broker/agent | Finds the other side, arranges visits, helps negotiate and coordinate | Commission, often a percentage (local norms vary; RE-M10-L02) |
| Document writer | Licensed to draft deeds; prepares the sale deed and handles registration paperwork | Fee per document |
| Advocate | Gives the legal title opinion, handles disputes and complex documents | Fee |
| Licensed surveyor | Measures land and fixes boundaries | Fee |
| Sub-Registrar Office (SRO) | Registers the deed; collects stamp duty and fees | Government revenue |
| Village office and taluk | Keep revenue records; issue certificates; mutation | Government fees |
| Local body (panchayat/municipality) | Building permits, building numbers, building tax | Fees and taxes |
| Bank or housing finance company | Lends; does its own legal and technical checks | Interest and fees |
| Builder/developer | Builds and sells flats, villas or plots | Margin |

Your business will sit among these players, so knowing what each one does (and does **not** do) is the first skill. A broker who tries to act as an advocate or document writer risks breaking the law and harming clients.
""",
    example="""
Sachin's neighbour, Kunhammed, wants to sell 15 cents of purayidam with an old house on the Kuttiady–Thottilpalam road to fund his daughter's studies. The buyer is a nurse working in Kuwait who wants a plot to build on later, close to her parents in Velom.

In the deal: a local broker who knows both families; a document writer near the Kuttiady SRO who drafts the deed; an advocate in Vadakara engaged by the buyer's brother to check title; the village office, which issues the possession certificate and later records the mutation; the SRO, where the deed is registered; and a bank in Kozhikode that gives the buyer a loan against her salary. The buyer is abroad, so she signs a registered power of attorney in favour of her brother (RE-M05-L02).

Seven parties, at least five offices or professionals, and many places where things can go wrong. A good broker coordinates them; a bad one hides problems to close quickly.
""",
    resources=[
        ('krera', 'Browse the project search: see which project types (apartments, villas, plots, commercial) are registered in Kozhikode district', '15 minutes'),
        ('wp-rera', 'Read the summary of who RERA covers (promoters, agents, buyers)', '10 minutes'),
        ('nobroker', 'Look at how property types and sizes are listed (no account needed for browsing)', '10 minutes'),
    ],
    steps=[
        'Walk or ride one main road in your area (for example Kuttiady town to Thottilpalam) and note at least 15 properties by type: land, house, flat, shop, commercial building, farmland, plantation.',
        'Note every property sign you see ("For sale", "For rent", broker boards) with the phone number (for your private records only).',
        'List the players in your area by name or office: nearest SRO, village office, panchayat office, two banks, document writers near the SRO, two advocates, any builders.',
        'Write three lines: which property type you see most for sale, which for rent, and which seems hardest to sell.',
    ],
    proof='A note with 15+ properties by type, the sign board count, your local players list and the three-line summary.',
    templates=[('Local players map', """LOCAL PLAYERS MAP                           Area: ______
Sub-Registrar Office: ______  (address, working days)
Village office(s): ______        Taluk office: ______
Panchayat / municipality office: ______
Document writers near the SRO: 1 ______ 2 ______
Advocates (property): 1 ______ 2 ______
Licensed surveyors: 1 ______
Banks / HFCs doing home loans: 1 ______ 2 ______
Brokers seen (boards, ads): 1 ______ 2 ______ 3 ______
Builders / developers: 1 ______
PROPERTY TYPE COUNT (one road survey)
Land __ House __ Flat __ Shop/commercial __ Farmland __ Plantation __ For sale signs __ For rent signs __""")],
    mistakes=[
        ('Judging land by how it looks.', 'A green, dry plot may still be nilam in records. Legal type comes from the records, not the eye.'),
        ('Thinking a broker can do everything.', 'Title opinions are for advocates, deeds for licensed document writers or advocates, measurement for surveyors.'),
        ('Ignoring commercial and rental demand.', 'Shop rooms and rentals often move faster than land and suit a low-capital start.'),
    ],
    fraud="""
**"Clear title, ready for registration" boards.** Some sellers and brokers advertise land as "clear" without any check. A board or a WhatsApp message is not evidence. Until you have seen the deed, a 30-year EC and an advocate's opinion, treat every claim as unverified (Module 6).
""",
    quiz=[
        Q('Which land type in Kerala revenue records is generally buildable?', 'Purayidam (garden or dry land)', 'Nilam (paddy land) in the data bank', 'Puramboke (government land)', 'Forest land', why='Purayidam is dry land; nilam and puramboke have strong restrictions.'),
        Q('Who is licensed to draft a sale deed?', 'A licensed document writer or an advocate', 'Any broker', 'The village officer', 'The buyer\'s bank', why='Deed drafting is licensed work; brokers coordinate but don\'t draft.'),
        Q('Where is a sale deed registered?', 'At the Sub-Registrar Office (SRO)', 'At the village office', 'At the panchayat', 'At K-RERA', why='The SRO registers documents and collects stamp duty and fees.'),
        Q('What does the village office handle in a deal?', 'Revenue records, certificates and mutation', 'Building permits', 'Home loans', 'Stamp duty collection', why='Building permits are the local body\'s job; stamp duty goes through the SRO.'),
    ],
    study='read the lesson and browse K-RERA project search',
    action='survey one road for 15+ properties and map your local players',
)

L2 = lesson(
    1, 2,
    outcome='You can explain what drives property demand and prices in Kerala, recognise the stage of a market cycle, and write a short snapshot of your local market.',
    split='15 minutes reading, 40 minutes of research and conversations',
    core=f"""
**Property markets move in cycles.** A simple four-stage picture:
1. **Recovery:** after a slump, few deals, prices flat, sellers patient.
2. **Expansion:** demand grows (jobs, remittances, new roads), deals pick up, prices rise, new projects launch.
3. **Peak/oversupply:** prices outrun incomes, many unsold flats and plots, speculation ("prices only go up").
4. **Slowdown:** deals dry up, sellers cut asking prices quietly, builders offer discounts, some projects stall.

Real markets are messier, and Kerala's land market can stay "frozen" for years: owners keep asking old prices, few deals happen, and real prices are hidden. That is why you will track **actual** listings and, where you can, actual sale prices (Module 7).

**What drives demand in Kerala:**
- **NRI money (remittances):** Gulf and other overseas earnings have long funded house building and land purchases, especially in Malabar. When Gulf jobs or oil prices weaken, local demand often softens.
- **Migration and demographics:** young people moving to cities or abroad; ageing parents in large houses; small families wanting smaller, low-maintenance homes; migrant workers from other states needing cheap rentals.
- **Infrastructure:** new or widened roads (national highway widening, bypasses), railway improvements, airports (Kozhikode airport at Karipur is nearby), hospitals, colleges and IT parks raise nearby values; announcements move prices before work starts, sometimes too much.
- **Tourism:** homestays and resorts near beaches, backwaters and hill areas (Wayanad, Munnar, Kozhikode beaches), subject to CRZ, ESA and local rules.
- **Education and healthcare clusters:** demand for rentals near medical colleges and universities.
- **Interest rates and loan availability:** lower rates make loans cheaper and lift demand.
- **Disasters and climate risk:** the 2018 and 2019 floods and landslides changed what buyers ask about; flood history now affects value (RE-M06-L02).
- **Law and policy:** fair-value increases, stamp duty changes, paddy-land conversion rules and building rules all affect deals.

**Good questions for any local market:** Who is buying here (NRIs, local salaried, investors, migrants)? What are they buying (plots, houses, flats, shops)? How long do listings stay up? Are sellers cutting prices? What is changing nearby (roads, colleges, rules)?
""",
    example="""
In 2025 and 2026, brokers around Kuttiady describe a market like this (the course's fictional summary of common patterns; check your own area): demand for small residential plots of 5 to 10 cents near the town and main roads from NRIs and salaried families; slow demand for large plots in interior areas without good road access; strong rental demand for small houses and rooms from teachers, government staff and migrant workers; and almost no flats outside Kozhikode city.

Prices on roads leading to Kozhikode and near the bypass are higher per cent than interior roads, and plots with a history of water-logging in the 2018 monsoon now sell more slowly. Your task is to replace this fictional summary with real notes from your own conversations and listings.
""",
    resources=[
        ('krera', 'Count how many registered projects you can find in Kozhikode district by type; note any near you', '15 minutes'),
        ('ksdma', 'Open the hazard maps and find the flood and landslide maps for Kozhikode district', '15 minutes'),
        ('mit-re', 'Optional: read the first lecture note on real estate markets (space and asset markets)', '30 minutes'),
    ],
    steps=[
        'Talk to three people about the local property market (a relative who bought recently, a shopkeeper, a broker). Ask the five questions: who buys, what, how long listings stay, price cuts, what is changing nearby.',
        'Find one infrastructure project or plan near you (a road widening, a bypass, a college, a hospital) and note its stage (announced, land acquisition, construction, complete).',
        'Check the KSDMA flood and landslide hazard maps for your panchayat and note whether parts of your area are marked.',
        'Write a one-page market snapshot: main demand drivers, cycle stage (your best guess), property types in demand, and risks.',
    ],
    proof='Notes from three conversations, one infrastructure note, a hazard-map note and your one-page market snapshot.',
    templates=[('Local market snapshot', """LOCAL MARKET SNAPSHOT                    Area: ______  Date: ______
Who is buying: NRIs __ local salaried __ investors __ migrants/tenants __
What sells fastest: ______   What sells slowest: ______
Typical listing time (from conversations): ______
Price trend (rising / flat / falling / frozen): ______  Evidence: ______
Demand drivers here: remittances / roads / colleges / hospitals / tourism / other ______
Infrastructure nearby (stage): ______
Hazards (KSDMA maps, 2018/2019 flood history): ______
My guess at the cycle stage: recovery / expansion / peak / slowdown. Why: ______
Opportunities for a low-capital service business: ______""")],
    mistakes=[
        ('Believing "land prices never fall".', 'Real prices can stagnate or fall for years, especially for interior and flood-prone land.'),
        ('Taking asking prices as market prices.', 'Asking prices are often far above what deals close at. Track listings and ask about actual deals.'),
        ('Buying on infrastructure announcements.', 'Projects get delayed or re-routed. Check the stage before treating it as value.'),
    ],
    fraud="""
**"New road coming" land sales.** Sellers sometimes claim a highway or bypass will pass next to a plot to justify a high price. Ask for the official alignment or notification, check the stage, and remember that land acquired for the road itself may be acquired at notified compensation, not market hopes.
""",
    quiz=[
        Q('Which has historically been a major driver of land and house demand in Malabar?', 'Remittances from Kerala workers abroad, especially in the Gulf', 'Large manufacturing industries', 'Mining', 'Government land auctions', why='NRI money has long funded house building and land purchases.'),
        Q('What is a sign that a market is in a slowdown?', 'Listings stay up longer and sellers quietly cut prices', 'New projects launch every month', 'Buyers compete for every plot', 'Banks raise loan limits', why='Longer listing times and price cuts signal weaker demand.'),
        Q('Why track actual listings and deals rather than what people say?', 'Asking prices and talk often differ from real closing prices', 'Talk is always lies', 'Listings never change', 'Banks require it', why='Real data protects your clients and your reputation.'),
        Q('How did the 2018 and 2019 floods affect the Kerala market?', 'Buyers now ask about flood history, and flood-prone plots can sell more slowly', 'They had no effect', 'Flood-prone land became more expensive', 'All prices doubled', why='Hazard history now affects demand and value.'),
    ],
    study='read the lesson and look at the KSDMA hazard maps for your district',
    action='talk to three people, note an infrastructure project and write a one-page market snapshot',
)

LESSONS = [L1, L2]

MODULE = module(
    1,
    overview=f"""
How real estate works in Kerala: property types (land, residential, commercial, agricultural, plantation), the people in a deal and what each does, market cycles, and the drivers of demand here (NRI money, migration, infrastructure, tourism, disasters, law). You map your local players and write a market snapshot.

Before learning laws and documents, you need a picture of the market you will work in. This module is mostly field work: a road survey, conversations and a one-page snapshot that you will update throughout the course.

Remember the course rule from **Start here**: this is education, not legal, tax or investment advice. You will learn when to call an advocate, a surveyor, a CA or a document writer, and never to do their licensed work yourself.
""",
    outcomes=[
        'Classify properties by type and by legal land type.',
        'Name the players in a deal and what each is responsible for.',
        'Describe market cycles and Kerala\'s demand drivers.',
        'Write a one-page snapshot of your local market.',
    ],
    lessons=LESSONS,
    project='a local market snapshot and players map',
    project_steps=[
        'Complete the road survey and players map (RE-M01-L01).',
        'Complete the market snapshot (RE-M01-L02).',
        'Share the snapshot with one experienced person (a broker or a relative who has bought land) and note what they disagree with.',
        'Save both in your toolkit folder; you will update the snapshot at the end of Part B and in the capstone.',
    ],
    project_proof='Your players map, road survey count, market snapshot and the feedback note.',
    rubric=[
        ('Property types', 'Confuses legal and physical type', 'Knows main types', 'Classifies by physical and legal type with examples'),
        ('Players', 'Few named', 'Most roles named', 'All roles named with local offices and contacts'),
        ('Market drivers', 'Generic list', 'Some local evidence', 'Local evidence from conversations, infrastructure and hazard maps'),
        ('Honesty', 'Repeats "prices only go up"', 'Some caveats', 'Separates asking prices from real deals and names risks'),
    ],
    short=[
        'Do the road survey on one short stretch (5 properties).',
        'Write a half-page snapshot from one conversation.',
    ],
    flashcards=[
        ('Purayidam', 'Garden or dry land in revenue records; generally buildable.'),
        ('Nilam', 'Paddy or wet land; protected by law.'),
        ('Who registers deeds?', 'The Sub-Registrar Office.'),
        ('Who drafts deeds?', 'A licensed document writer or an advocate.'),
        ('Who gives a title opinion?', 'An advocate.'),
        ('Four cycle stages', 'Recovery, expansion, peak/oversupply, slowdown.'),
        ('Main Malabar demand driver', 'NRI remittances.'),
    ],
    mistakes=[
        ('Skipping field work.', 'Your local knowledge is your main asset as a beginner.'),
        ('Treating rumours as data.', 'Write down sources and dates.'),
        ('Overlooking rentals.', 'Rentals are often the fastest low-capital start.'),
    ],
    tools=[
        'The local players map and property-type count (RE-M01-L01).',
        'The local market snapshot (RE-M01-L02).',
    ],
    toolkit=[
        'Local players map (offices, document writers, advocates, surveyors, banks, brokers).',
        'Local market snapshot, version 1.',
    ],
)
