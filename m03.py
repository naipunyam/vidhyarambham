from common import lesson, module, link, rules, xref, table, fence, Q, RULE, ASOF, CHECK

UNITS = [
    ('1 cent', '435.6 sq ft', '40.47 sq m', '0.405 are'),
    ('1 are', '1,076.4 sq ft', '100 sq m', '2.471 cents'),
    ('1 acre', '43,560 sq ft', '4,046.9 sq m', '100 cents = 40.47 ares'),
    ('1 hectare', '1,07,639 sq ft', '10,000 sq m', '100 ares = 247.1 cents = 2.471 acres'),
    ('1 sq m', '10.764 sq ft', '1 sq m', '0.0247 cent'),
]

L1 = lesson(
    3, 1,
    outcome='You can convert between cents, ares, acres, hectares, square feet and square metres, estimate a plot\'s area from its measurements, and explain carpet, built-up and super built-up area.',
    split='15 minutes reading, 40 minutes of practice and a field measurement',
    core=f"""
**Kerala land units.** In everyday Kerala deals, land is priced **per cent**. Official records after the resurvey use **ares** and **hectares** (metric), and older deeds may use cents and acres. Buildings are measured in **square feet** (sq ft) in the market and **square metres** in building rules and permits.

{table(['Unit', 'Square feet', 'Square metres', 'Other'], UNITS)}

**Quick memory rules:** 1 cent ≈ 436 sq ft ≈ 40.5 sq m. 1 are ≈ 2.47 cents. 10 cents ≈ 4,356 sq ft ≈ 4.05 ares. 1 acre = 100 cents.

**Estimating area from measurements.** For a roughly rectangular plot, area = length × width. For irregular plots, split the shape into rectangles and triangles (area of a triangle = ½ × base × height) and add them. On the ground, measure with a tape (or count paces only as a rough check). For any boundary question or legal measurement, a **licensed surveyor** must measure; your estimate is only for your own understanding.

**Building areas** (important when comparing houses and flats):
- **Carpet area:** the usable floor area inside the walls (rooms, kitchen, toilets). Under RERA, builders must quote prices on carpet area for registered projects.
- **Built-up area:** carpet area plus the thickness of walls and, often, balconies.
- **Super built-up area:** built-up area plus a share of common areas (lobbies, stairs, lifts). Flats in Kerala cities were often sold on super built-up area before RERA; super built-up can be 20% to 35% more than carpet area, which makes the price per sq ft look lower than it is.
- **Plinth area:** the covered area at the floor level, used in some building-rule and tax contexts.

Always ask: **which area** is this price per sq ft based on?
""",
    example="""
A listing in Kayakkody says "8.25 cents, ₹2.2 lakh per cent". The deed shows **3.34 ares**. Check: 3.34 × 2.471 = 8.25 cents. ✓ Price: 8.25 × ₹2,20,000 = **₹18,15,000**.

A house nearby is advertised as "1,450 sq ft, ₹48 lakh". The owner's building permit shows 118 sq m plinth area: 118 × 10.764 = 1,270 sq ft. The extra 180 sq ft in the advert is a sit-out and a sunshade counted generously. The real price per sq ft of the house on the permit area is ₹48,00,000 ÷ 1,270 ≈ **₹3,780**, not ₹3,310 as the advert implies (and that price also includes the land).
""",
    calc="""
**Irregular plot:** a plot is 30 m along the road, 45 m deep on the left side and 38 m deep on the right side (a trapezium).
- Area ≈ (45 + 38) ÷ 2 × 30 = 41.5 × 30 = **1,245 sq m**
- In ares: 1,245 ÷ 100 = **12.45 ares**
- In cents: 1,245 ÷ 40.47 ≈ **30.8 cents**
- In Google Sheets: cents from sq m `=A1/40.4686`; cents from ares `=A1*2.47105`; sq ft from cents `=A1*435.6`.
This is an estimate only. A licensed surveyor's measurement and the official sketch decide the legal area.
""",
    resources=[
        ('erekha', 'Look at the list of record types and prices (maps, FMB, area list) to see how areas are recorded', '10 minutes'),
        ('wp-rera', 'Read the part on carpet area', '5 minutes'),
        ('gearth', 'Open Google Earth (web or mobile) and try the measure tool on your own house or a public ground', '15 minutes'),
    ],
    steps=[
        'Make a conversion sheet in your workbook with the formulas above and test it on five numbers (10 cents, 4 ares, 1 acre, 1,000 sq m, 2,000 sq ft).',
        'With permission, measure your own house plot (or a family plot) with a tape; estimate its area in sq m, ares and cents. Compare with the area in the deed if you have it.',
        'Use Google Earth\'s measure tool on the same plot and compare the three numbers (tape, Google Earth, deed).',
        'Find two house listings and work out whether the price per sq ft uses carpet, built-up or super built-up area.',
    ],
    proof='Your conversion sheet, the three-way area comparison for one plot and notes on two listings\' area basis.',
    templates=[('Area conversion sheet', """AREA CONVERSIONS (tab "Units")
A2 value | B2 unit | results:
Cents from sq ft:     =A2/435.6
Cents from sq m:      =A2/40.4686
Cents from ares:      =A2*2.47105
Ares from cents:      =A2/2.47105
Sq ft from cents:     =A2*435.6
Sq m from sq ft:      =A2/10.7639
Rectangle (sq m):     =length*width
Trapezium (sq m):     =(side1+side2)/2*width
Triangle (sq m):      =0.5*base*height
PLOT CHECK: tape ___ cents | Google Earth ___ cents | deed ___ cents | difference ___%""")],
    mistakes=[
        ('Mixing up ares and cents.', 'An are is about 2.47 cents. Confusing them misprices land by more than double.'),
        ('Comparing prices per sq ft on different area bases.', 'Ask whether it is carpet, built-up or super built-up.'),
        ('Trusting your own tape measure for legal boundaries.', 'Only a licensed surveyor\'s measurement and official records decide.'),
    ],
    fraud="""
**Inflated area.** Sellers sometimes quote "about 10 cents" when the deed says 8.4, or include a neighbour's strip, a puramboke edge or a road margin. Always take the area from the deed and the official sketch, and have a surveyor measure if anything doesn't match (RE-M06-L02).
""",
    quiz=[
        Q('About how many square feet are in 10 cents?', '4,356 sq ft', '1,000 sq ft', '43,560 sq ft', '435 sq ft', why='10 × 435.6.'),
        Q('A deed says 8.1 ares. About how many cents is that?', 'About 20 cents', 'About 8 cents', 'About 3.3 cents', 'About 81 cents', why='8.1 × 2.471 ≈ 20.0.'),
        Q('What does super built-up area include?', 'Built-up area plus a share of common areas such as stairs and lobbies', 'Only the rooms', 'Only the land', 'Only balconies', why='It makes price per sq ft look lower than carpet-area price.'),
        Q('Who decides a plot\'s legal measurement in a dispute?', 'A licensed surveyor\'s measurement and the official survey records', 'The broker', 'Google Earth', 'The buyer', why='Your estimate is only a check.'),
    ],
    study='read the lesson and practise the conversion table',
    action='build a conversion sheet and compare tape, Google Earth and deed areas for one plot',
)

L2 = lesson(
    3, 2,
    outcome='You can explain survey and resurvey numbers, thandaper, land tax receipts, sketches and village office certificates, and what each proves and does not prove.',
    split='20 minutes reading, 40 minutes including an office visit or a document review',
    core=f"""
**Survey numbers.** Every parcel of land in Kerala is identified in survey records by a **survey number** and often a **sub-division** (for example Sy. No. 112/3B). Old surveys date from the colonial and princely-state periods. Kerala has been carrying out a **resurvey** (and since about 2022 a **digital resurvey** using satellite positioning and drones, under the Ente Bhoomi programme) that assigns new **block** and **resurvey numbers**. A **correlation statement** links old survey numbers to new resurvey numbers ({link('erekha', 'e-Rekha')} sells copies). Deeds may use either system, so checking both is essential.

**Village records and the thandaper.** The **village office** keeps the land records for its village. Each landholder has a **thandaper** (account) number in the village records, linked to the land tax paid. The **land tax (karam) receipt** shows the thandaper, survey number, area, land type and the name in which tax is paid. Under Ente Bhoomi, records are being linked to a **Unique Thandaper** and integrated with the Registration and Survey departments ({link('entebhoomi-nic', 'NIC description of Ente Bhoomi')}).

**Sketches and maps.** A **location sketch** or survey sketch shows the parcel's shape and neighbours; the **FMB** (field measurement book) sketch from the resurvey shows measured boundaries. These are available from the village or taluk office, the survey office and, for digital records, e-Rekha.

**Certificates from the village office** (issued through the village office or online through e-District / Akshaya centres; {CHECK}):
- **Possession certificate:** states that a person is in possession of the land. It supports, but does not prove, ownership.
- **Location certificate:** states where the property is located.
- **Other certificates** for loans and permits, such as a non-attachment or land-type certificate, may also be needed.
The **ownership certificate** for a building comes from the **local body** (panchayat or municipality), linked to building tax ({link('hc-online', 'Housing.com list of online services')}).

**What these do and do not prove.** Revenue records (thandaper, tax receipts, possession certificate) show who pays tax and who is in possession. **Title** (ownership) comes from registered deeds; revenue entries can lag behind or be wrong. A seller who has a tax receipt but no clear deed chain is a red flag; so is a deed in one name and tax receipts in another.
""",
    example="""
Sachin helps his uncle collect papers for a 12-cent plot in Velom village. The deed (from 1998) describes the land as old survey number 214/2 with an area of 12 cents. The land tax receipt shows resurvey block 18, resurvey number 344, area **4.86 ares** (12.0 cents), purayidam, thandaper number 2117, in his uncle's name. ✓

The correlation statement confirms that old 214/2 corresponds to resurvey 344 in block 18. The village office issues a possession certificate in his uncle's name. The FMB sketch shows the shape matches the boundaries on the ground. All the papers agree. If any of them disagreed (a different area, a different name, land type shown as nilam), that would be a question for an advocate and a surveyor before any sale.
""",
    rules_rows=[
        ('Resurvey and digital resurvey', 'New block and resurvey numbers replace old survey numbers; correlation statements link them', 'NIC Ente Bhoomi; e-Rekha'),
        ('Ente Bhoomi', 'Integrates Revenue (ReLIS), Registration (PEARL) and Survey; thandaper, sketches and EC online; auto-mutation', 'NIC Informatics, January 2025'),
        ('e-Rekha fees (per page, including tax)', 'FMB resurvey ₹750; maps ₹1,000; land/settlement register ₹1,400; correlation statement ₹1,000; area list ₹550', 'e-Rekha'),
    ],
    pro="""
- **Licensed surveyor:** if the sketch, the deed area and the ground don't match, or boundaries are disputed.
- **Advocate:** if the names, land type or survey numbers differ between the deed, the tax receipt and the certificates.
""",
    resources=[
        ('entebhoomi-nic', 'Read the description of Ente Bhoomi services and the digital resurvey', '15 minutes'),
        ('erekha', 'Read the list of record types and what each contains', '10 minutes'),
        ('wayanad-tax', 'See how land tax is paid online through ReLIS (the same system applies statewide)', '5 minutes'),
    ],
    steps=[
        'With permission, look at your own family\'s or a relative\'s land papers: deed, latest land tax receipt and any sketch. Note the survey or resurvey number, area, land type, thandaper and names on each (keep this private).',
        'Check whether the area and survey numbers agree across the papers, converting ares and cents.',
        'Visit the village office (or ask an Akshaya centre) to learn how to get a possession certificate and a location sketch: what to bring, fees and time. Don\'t apply unless the owner wants it.',
        'Write which items agree, which disagree, and what you would ask an advocate.',
    ],
    proof='A private comparison table of one property\'s papers (numbers and names masked in anything you share), and notes from the village office or Akshaya visit.',
    templates=[('Land records comparison', """LAND RECORDS COMPARISON          Property ______ (keep private)
Item                 Deed        Tax receipt   Certificate   Sketch/FMB   Match?
Old survey no.       ______      ______        ______        ______       __
Resurvey block/no.   ______      ______        ______        ______       __
Area (ares/cents)    ______      ______        ______        ______       __
Land type            ______      ______        ______        ______       __
Name(s)              ______      ______        ______        ______       __
Thandaper no.        —           ______        ______        —            __
Village office visit: certificate procedure ______ ; fees ______ ; time ______
Questions for an advocate / surveyor: ______""")],
    mistakes=[
        ('Treating a tax receipt as proof of ownership.', 'Revenue records show tax and possession; title comes from registered deeds.'),
        ('Ignoring old versus new survey numbers.', 'Use the correlation statement to match them.'),
        ('Sharing people\'s land papers publicly.', 'Keep them private and mask names and numbers.'),
    ],
    fraud="""
**Mismatched numbers.** A common trick is to show papers for a neighbouring or larger parcel, or a deed with an old survey number that doesn\'t match the land being shown. Always match the survey/resurvey number, area and boundaries on the papers with the land on the ground.
""",
    quiz=[
        Q('What links old survey numbers to new resurvey numbers?', 'The correlation statement', 'The building permit', 'The sale agreement', 'The EC', why='e-Rekha and survey offices provide it.'),
        Q('What is a thandaper?', 'The landholder\'s account number in the village revenue records', 'A building number', 'A loan account', 'A stamp paper', why='It links the holder to land-tax records.'),
        Q('What does a possession certificate show?', 'That a person is in possession of land; it supports but does not prove ownership', 'Absolute ownership', 'That the land has no loans', 'That the building has a permit', why='Title comes from registered deeds.'),
        Q('Which body issues an ownership certificate for a building?', 'The local body (panchayat or municipality)', 'The village office', 'The SRO', 'K-RERA', why='Buildings are linked to local-body building tax.'),
    ],
    study='read the lesson and the Ente Bhoomi description',
    action='compare one property\'s papers and find out the certificate procedure at your village office or an Akshaya centre',
)

L3 = lesson(
    3, 3,
    outcome='You can use the main Kerala online land-record portals (fair value search, EC application, land tax, Ente Bhoomi, e-Rekha) safely and know what each gives you.',
    split='15 minutes reading, 40 minutes on the portals',
    core=f"""
Kerala has moved many land services online. Official sites sometimes change addresses and some block automated checks, so always confirm you are on a **.gov.in** site and {CHECK}.

| Portal | What it is for | Notes |
| --- | --- | --- |
| Kerala Registration Department ({link('kreg', 'keralaregistration.gov.in')}) | Fair value, EC, e-stamp, registration services | Address checked {ASOF} through secondary guides; the site blocks automated checks |
| PEARL ({link('pearl', 'pearl.registration.kerala.gov.in')}) | Apply for and download ECs; application status | Fees reported in April 2025: application ₹15; first 5 years ₹105; 6 to 30 years ₹265; more years ₹30 each ({link('hc-ec', 'Housing.com')}) |
| IGR fair value search ({link('igr-fv', 'igr.kerala.gov.in')}) | Government fair value of land by district, RDO, taluk, village, desam, survey number | Fair value was raised by 20% from 1 April 2023 ({link('om-fv2023', 'Onmanorama')}); how to search: {link('hc-fv', 'Housing.com guide')} |
| Revenue / ReLIS ({link('revenue', 'revenue.kerala.gov.in')}) | Pay land tax online; revenue e-services | Linked from district sites ({link('wayanad-tax', 'example')}) |
| Ente Bhoomi ({link('entebhoomi', 'entebhoomi.kerala.gov.in')}) | Integrated land information: thandaper, sketches, EC, auto-mutation | Rolling out with the digital resurvey ({link('entebhoomi-nic', 'NIC')}) |
| e-Rekha ({link('erekha', 'erekha.kerala.gov.in')}) | Buy digital survey records: FMB, maps, registers, correlation statements | Paid per page |

**Safe use:**
- Use official sites only; many look-alike sites and paid "agents" offer land records. Akshaya centres are official service points if you need help.
- Never share OTPs, and only apply for records of property you own or have the owner's permission to check.
- Save every PDF with a file name like `2026-11-10 EC Velom 344 1995-2026.pdf`.
- Online records can have errors; when they don't match the deed, ask the office and an advocate.
""",
    example="""
For his uncle's 12-cent plot (RE-M03-L02), Sachin, with his uncle's permission:
1. Searches the fair value for Velom village using district Kozhikode, the RDO, taluk Vadakara, village Velom, and the resurvey block and number. The fair value shown is, for example, ₹1.6 lakh per are (about ₹65,000 per cent: the course's illustrative number).
2. Applies for an EC on PEARL for 1995 to 2026 (31 years), paying about ₹15 + ₹265 + ₹30 = ₹310 (fees as reported; check the current amount on the portal).
3. Checks the latest land-tax payment through ReLIS.
4. Notes that the market asking price around Velom is ₹1.8 to ₹2.4 lakh per cent, far above the fair value: common in Kerala, where fair values often lag market prices.
""",
    rules_rows=[
        ('Fair value increase', '20% increase from 1 April 2023 (G.O.(P) No.45/2023/TAXES)', 'Onmanorama; Housing.com'),
        ('EC fees (reported April 2025)', 'Application ₹15; 5 years ₹105; 6–30 years ₹265; extra years ₹30 each', 'Housing.com'),
        ('e-stamping', 'Stamp duty paid through e-stamps bought online or from licensed vendors', 'Housing.com online services guide'),
    ],
    resources=[
        ('hc-fv', 'Read the step-by-step fair value search guide', '10 minutes'),
        ('hc-ec', 'Read the EC application steps and fees', '10 minutes'),
        ('hc-online', 'Read the overview of Kerala registration online services', '10 minutes'),
    ],
    steps=[
        'Search the fair value for three locations in your area (your own village, a town location and an interior location), noting the inputs and the value per are.',
        'Convert each to a value per cent and compare with asking prices you have seen.',
        'With an owner\'s permission (your family\'s property is fine), apply for or at least walk through the EC application on PEARL up to the payment step, and note the fee shown.',
        'Write a one-page "portal guide" for your toolkit with the addresses, what each is for and your notes.',
    ],
    proof='Three fair-value screenshots or notes with dates, a fair value versus asking price comparison, notes from the EC walk-through and your portal guide.',
    templates=[('Portal guide and fair value log', """PORTAL GUIDE (checked on ______)
Fair value: igr.kerala.gov.in -> inputs: district, RDO, taluk, village, desam, survey/resurvey no.
EC: pearl.registration.kerala.gov.in -> Certificates -> EC application (OTP to mobile)
Land tax: revenue.kerala.gov.in (ReLIS)
Ente Bhoomi: entebhoomi.kerala.gov.in    Survey records: erekha.kerala.gov.in
FAIR VALUE LOG
Date | Village | Survey/resurvey | Fair value per are | per cent (=x/2.47105) | Typical asking per cent | Gap %""")],
    mistakes=[
        ('Using unofficial sites or paying "agents".', 'Use .gov.in sites or Akshaya centres.'),
        ('Assuming fair value equals market value.', 'In Kerala fair value usually lags market prices; it sets the minimum for stamp duty.'),
        ('Searching records without permission.', 'Check only your own or permitted properties.'),
    ],
    fraud="""
**Fake portals and fake "online EC".** Scammers create look-alike sites, or send PDFs that look like ECs or certificates. Download records yourself from official portals, check the transaction ID, and confirm suspicious documents at the office.
""",
    quiz=[
        Q('Which portal do you use to apply for an EC in Kerala?', 'PEARL (Kerala Registration)', 'K-RERA', 'Sanketham', 'NoBroker', why='ECs come from the Registration Department.'),
        Q('What does the fair value search give you?', 'The government-notified minimum land value used for stamp duty', 'The market price', 'The owner\'s name', 'The building permit', why='Duty is on the higher of price or fair value.'),
        Q('By how much was fair value increased from 1 April 2023?', '20%', '2%', '50%', 'It was not changed', why='Per the 2023 government order.'),
        Q('What is the safest way to get records if you need help?', 'An Akshaya centre or the office itself', 'A WhatsApp agent', 'Any website that ranks first in search', 'A stranger at the bus stand', why='Akshaya centres are official service points.'),
    ],
    study='read the lesson and the three guides',
    action='search fair value for three locations, walk through an EC application and write your portal guide',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    3,
    overview=f"""
Land measurement and records in Kerala: cents, ares and square feet; carpet and built-up area; survey and resurvey numbers; thandaper and land tax; possession, location and ownership certificates; sketches; and the online portals (fair value, EC, ReLIS, Ente Bhoomi, e-Rekha).

Part B, the knowledge base, starts with the records that every deal depends on. A good broker reads land papers quickly and spots mismatches; that one skill prevents most bad deals.

Practise on your own family's papers (with permission) or the sample case in RE-M06-L03. Never ask strangers for their documents for practice.
""",
    outcomes=[
        'Convert land and building units and explain area types.',
        'Read survey and resurvey numbers, thandaper, tax receipts, sketches and certificates.',
        'Explain what revenue records prove and what they don\'t.',
        'Use the official land-record portals safely.',
    ],
    lessons=LESSONS,
    project='a land-records walk-through for one plot',
    project_steps=[
        'Choose one plot you can legally check (your family\'s, with permission).',
        'Complete the area comparison (RE-M03-L01), the records comparison (RE-M03-L02) and the fair value search and EC walk-through (RE-M03-L03).',
        'Write a one-page summary: what matches, what doesn\'t, what you\'d ask an advocate or surveyor.',
        'Save your conversion sheet and portal guide in the toolkit.',
    ],
    project_proof='The three comparisons, the summary and your portal guide (personal details masked).',
    rubric=[
        ('Units', 'Errors in conversion', 'Mostly right', 'Fast, accurate conversions with formulas'),
        ('Records', 'Can\'t read papers', 'Reads most items', 'Reads and cross-checks every item'),
        ('Portals', 'Not used', 'Some used', 'Fair value, EC and land tax portals used with notes'),
        ('Judgement', 'Treats tax receipts as title', 'Knows the limits', 'Explains what each record proves and when to call a professional'),
    ],
    short=[
        'Learn the five unit conversions.',
        'Search one fair value on the official portal.',
    ],
    flashcards=[
        ('1 cent', '435.6 sq ft = 40.47 sq m.'),
        ('1 are', '100 sq m = 2.471 cents.'),
        ('Carpet vs super built-up', 'Usable inside area vs built-up plus a share of common areas.'),
        ('Correlation statement', 'Links old survey numbers to resurvey numbers.'),
        ('Thandaper', 'Landholder\'s account in village revenue records.'),
        ('Possession certificate', 'Supports possession; does not prove title.'),
        ('EC portal', 'PEARL (Kerala Registration).'),
        ('Fair value', 'Government minimum value for stamp duty; often below market.'),
    ],
    mistakes=[
        ('Skipping the paperwork practice.', 'Reading papers is the core skill.'),
        ('Assuming online records are always right.', 'Cross-check with deeds and offices.'),
        ('Doing a surveyor\'s or advocate\'s job.', 'Know your limits.'),
    ],
    tools=[
        'The area conversion sheet (RE-M03-L01).',
        'The land records comparison (RE-M03-L02).',
        'The portal guide and fair value log (RE-M03-L03).',
    ],
    toolkit=[
        'Units tab with conversion formulas.',
        'Land records comparison template.',
        'Portal guide with official addresses and fair value log.',
    ],
)
