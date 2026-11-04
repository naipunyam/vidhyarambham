from common import lesson, module, link, rules, xref, table, fence, Q, RULE, ASOF, CHECK
import tools

SAFE = f'Due diligence by a broker is a **first check** to protect clients and avoid bad deals. It never replaces an **advocate\'s written title opinion** or a **licensed surveyor\'s measurement**. Rules and fees are {RULE}.'

EC_ROWS = [
    ('Sale deed in 2009 from A to B', 'B is the current owner, if no later transfer appears', 'Matches the deed you were shown?'),
    ('Mortgage (equitable mortgage memorandum) in 2016 to a bank', 'B borrowed against the property', 'Is there a release or loan-closure entry later? If not, ask for the bank\'s closure letter'),
    ('Agreement for sale in 2023 from B to C (registered)', 'B agreed to sell to someone else', 'Serious red flag: ask what happened; advocate'),
    ('Release deed in 2012 from B\'s sister to B', 'The sister gave up her share', 'Good: confirms B\'s full ownership'),
    ('No entries for 30 years', 'Either no transactions or the wrong survey number or SRO was searched', 'Check the survey number, the old and new numbers, and the right SRO'),
]

L1 = lesson(
    6, 1,
    outcome='You can trace a title chain for 30 years, read an encumbrance certificate (EC), and check for loans, prior sales and litigation.',
    split='25 minutes reading, 40 minutes on the action task',
    core=f"""
{SAFE}

**Title chain.** Starting from the seller's deed, follow each prior document back (sale, partition, gift, settlement, release, will, Land Tribunal purchase certificate) for **at least 30 years** where possible. At each link, ask: did the person transferring actually own it? Did all co-owners and heirs sign? Was the document registered? Do the survey numbers and areas match?

**Encumbrance certificate (EC, ബാധ്യതാ സർട്ടിഫിക്കറ്റ്).** An EC from the Registration Department lists the **registered** transactions on a survey number at an SRO for a chosen period: sales, mortgages, gifts, partitions, agreements, releases and attachments that were registered. Apply online through PEARL (RE-M03-L03). Reported fees: application ₹15; first 5 years ₹105; 6 to 30 years ₹265; ₹30 for each extra year ({link('hc-ec', 'Housing.com, April 2025')}; {CHECK}).

**Reading an EC:**
{table(['EC entry', 'What it means', 'What to check'], EC_ROWS)}

**What an EC does not show:** unregistered agreements, court cases (unless an attachment was registered), tenancy claims, revenue recovery that was not registered, government acquisition plans, or a fraud registered at a different SRO under a different survey number. That's why you also check the following.

**Why banks need an EC.** For a home loan or LAP, the bank's advocate checks the deed chain and a 13 to 30 year EC and registers the bank's mortgage. A recent EC is also needed at sale time to confirm no new transaction since the last one.

**Litigation checks.**
- Ask the seller in writing whether there is any case, dispute or claim.
- Search **eCourts** by party name for the seller and previous owners in the district courts ({link('ecourts', 'eCourts Services')}); an advocate can do a fuller search, including the High Court.
- Ask neighbours and the village office informally about disputes.
- Look for **lis pendens** (a pending suit about the property) noted in the EC or court records.
""",
    example="""
For a 15-cent plot in Kayakkody, Sachin (with the owner's permission, for a buyer) applies for an EC for 1995 to 2026 (32 years: about ₹15 + ₹265 + ₹60). The EC shows:
- 2004: partition deed, family of the seller.
- 2011: sale deed from the brother to the seller (consistent with what was shown).
- 2018: mortgage to a cooperative bank.
- No release of the mortgage.
He asks the seller: "Is the 2018 loan closed?" The seller produces a closure letter from the bank, but the release isn't registered. The buyer's advocate advises that the bank must register the release (or issue documents to cancel the mortgage) before or at the sale. An eCourts search by the seller's name shows no cases in Kozhikode district courts.
""",
    rules_rows=[
        ('EC fees', 'Application ₹15; 5 years ₹105; 6–30 years ₹265; ₹30 per extra year', 'Housing.com, April 2025'),
        ('Title period', 'Commonly 30 years checked by advocates and banks (practice, not a single statutory rule)', 'Local practice; ask your advocate'),
    ],
    pro="""
- **Advocate:** writes the title opinion, does a fuller litigation search and advises on mortgages, attachments or prior agreements.
""",
    resources=[
        ('hc-ec', 'Read the EC application steps', '10 minutes'),
        ('ecourts', 'Try a case status search (use a public name such as a company, or your own)', '15 minutes'),
        ('pearl', 'Open the PEARL portal and find the EC section', '10 minutes'),
    ],
    steps=[
        'With an owner\'s permission (your family\'s property), apply for or download a 30-year EC. If you can\'t, ask a document writer to show you a sample EC with names hidden.',
        'List each entry and what it means, using the table above.',
        'Draw the title chain from the deeds and the EC together and mark any gaps.',
        'Try an eCourts party-name search for a public name to learn how it works.',
    ],
    proof='The EC (private) or sample with your entry-by-entry notes, the title chain and a screenshot of the eCourts search page.',
    templates=[('Title chain and EC sheet', """TITLE CHAIN AND EC SHEET   Survey/resurvey ______ Village ______ SRO ______
TITLE CHAIN (newest first)
Year | Document type | Doc no./SRO | From -> To | Area | All heirs signed? | Notes
____ | ____________ | ___________ | __________ | ____ | ___ | ______
EC: period ______ to ______ ; applied on ______ ; fee ₹ ______
Entry | Year | Type | Parties | Open issue?
Mortgages without release: ______ -> closure letter + registered release?
Prior agreements to others: ______ -> advocate
Litigation: seller's written declaration Y/N ; eCourts search by names ______ (date) ; result ______
Questions for advocate: ______""")],
    mistakes=[
        ('Checking only a 13-year EC.', 'Check 30 years where possible.'),
        ('Thinking an EC shows everything.', 'It shows only registered documents; do litigation checks too.'),
        ('Searching the wrong survey number or SRO.', 'Use both old and new numbers and the correct SRO.'),
    ],
    fraud="""
**Double sales.** A seller signs a registered agreement with one buyer and sells to another, or sells the same land twice. A fresh EC just before registration catches many of these.
""",
    quiz=[
        Q('What does an EC list?', 'Registered transactions on a property for a period', 'All court cases', 'The market price', 'The building plan', why='It doesn\'t show unregistered matters.'),
        Q('An EC shows a 2018 mortgage with no release. What do you ask for?', 'The bank\'s closure letter and a registered release', 'Nothing', 'A new building permit', 'The buyer\'s salary', why='The mortgage must be cleared.'),
        Q('Where can you search district court cases by party name?', 'eCourts Services', 'K-RERA', 'PEARL', 'e-Rekha', why='An advocate can search further.'),
        Q('How far back is a title chain usually checked?', 'At least 30 years where possible', '1 year', '5 years', 'Only the latest deed', why='Common practice of advocates and banks.'),
    ],
    study='read the lesson and the EC table',
    action='read a 30-year EC (or a sample) and draw the title chain',
)

L2 = lesson(
    6, 2,
    outcome='You can carry out a physical verification of a property: boundaries, access road, flood and slope risks, utilities and neighbours.',
    split='15 minutes reading, 50 minutes on a site visit',
    core=f"""
{SAFE}

Papers can be perfect and the land still a problem. Physical verification checks that the land on the ground is the land in the papers and is usable.

**Boundaries.** Walk the boundaries with the owner. Compare with the sketch and the deed's four boundaries (east, west, north, south neighbours). Look for boundary stones, walls, fences and trees. Ask neighbours (politely) whether they agree with the boundaries. Watch for **encroachment** (the seller using a neighbour's or government strip, or a neighbour using part of the plot).

**Access road.**
- Is it a **public road** (panchayat, PWD) or a **private path**? A private path needs a **registered right of way** (easement) in the deed or a separate document.
- Width: affects building permits and vehicle access (RE-M04-L04).
- Is there **road widening** planned (for example a highway or bypass)? Ask the panchayat or PWD.

**Water and flood risk.** Check the **KSDMA hazard maps** ({link('ksdma', 'KSDMA')}), ask neighbours about the 2018 and 2019 floods, look for water marks on walls and water-logging in the monsoon. Visit during rain if you can.

**Slope and soil.** Steep slopes, cut hillsides and loose soil raise landslide risk, especially in the hilly parts of Kozhikode district. Check the landslide map too.

**Utilities.** Well (depth and summer water level), Kerala Water Authority connection, electricity (single or three-phase), drainage, mobile signal.

**Surroundings.** Quarries, high-tension power lines, streams and canals, factories, garbage sites, and important amenities (school, hospital, bus stop).

**Take photos** of everything (with permission) and record GPS coordinates. Use your **site-visit checklist** from the toolkit.
""",
    example="""
Sachin visits a 10-cent plot near Kuttiady river with the owner. The deed's boundaries: east, a panchayat road; west, a canal; north and south, private land. On site:
- The "panchayat road" is a 2.5 m mud path that becomes a stream in the monsoon. The concrete road is 80 m away, across a neighbour's land. Is there a registered right of way? The deed doesn't mention one.
- The canal side is low; a neighbour says water came up to knee height in 2018.
- The KSDMA flood map marks the area as flood-prone.
- The south boundary wall seems to include 1.5 m of the neighbour's land, according to the neighbour.
Sachin records all this, tells the buyer honestly and recommends a licensed surveyor and an advocate before any advance.
""",
    pro="""
- **Licensed surveyor:** measures the plot and fixes boundaries when anything is unclear or disputed.
- **Advocate:** easements, encroachment and road issues.
- **Engineer:** soil, slope and building suitability.
""",
    resources=[
        ('ksdma', 'Check the flood and landslide maps for the plot\'s area', '10 minutes'),
        ('gearth', 'Use Google Earth to view the plot and surroundings and measure distances', '15 minutes'),
    ],
    steps=[
        'With the owner\'s permission, visit one plot or house (your family\'s or a listing whose owner agrees).',
        'Complete the site-visit checklist from the toolkit, with photos.',
        'Check the hazard maps and Google Earth for the plot.',
        'Write a one-page verification note: what matches the papers, what doesn\'t, risks and which professional to call.',
    ],
    proof='The completed checklist with photos, map screenshots and your verification note.',
    templates=[('Site-visit checklist', tools.SITE_VISIT)],
    mistakes=[
        ('Visiting only in dry weather.', 'Ask about the monsoon or visit during rain.'),
        ('Assuming a path is a public road.', 'Check ownership and any registered right of way.'),
        ('Fixing boundaries yourself.', 'A licensed surveyor does that.'),
    ],
    fraud="""
**Showing the wrong plot.** Some sellers show a better plot next door. Always match the sketch, boundaries and neighbours, and use GPS and Google Earth.
""",
    quiz=[
        Q('What is needed if the only access is a private path?', 'A registered right of way (easement)', 'Nothing', 'A building permit', 'An EC', why='Without it, access can be blocked.'),
        Q('Where can you check flood and landslide zones in Kerala?', 'KSDMA hazard maps', 'PEARL', 'K-RERA', 'NoBroker', why='Also ask neighbours about 2018 and 2019.'),
        Q('A neighbour says the boundary wall includes part of their land. What do you do?', 'Record it and recommend a licensed surveyor and advocate', 'Ignore it', 'Move the wall', 'Tell the buyer it\'s fine', why='Encroachment disputes are serious.'),
        Q('Why record GPS coordinates and photos?', 'To match the land to the papers and keep evidence', 'For fun', 'For tax', 'They are not useful', why='Prevents wrong-plot confusion.'),
    ],
    study='read the lesson and the site-visit checklist',
    action='verify one property on site with the checklist and write a verification note',
)

CASE = """
**Sample case (fictional, for practice).** "Plot at Kayakkody":
- Seller: Mr. A (55), says he owns 15 cents; asking ₹2.4 lakh per cent (₹36 lakh).
- Deed: sale deed 2011 (Kuttiady SRO) from his brother; recitals: partition 2004 among four siblings.
- Tax receipt: 6.07 ares (15.0 cents), land type purayidam, in Mr. A's name, paid for 2025-26.
- EC 1995–2026: partition 2004; sale 2011; mortgage 2018 to a cooperative bank; no release.
- Sketch: matches the shape; east boundary "panchayat road".
- Site visit: road is a 3 m tarred panchayat road ✓; part of the north side is low and gets water-logged; KSDMA map: not in a mapped flood zone.
- Neighbour: says one of the four siblings (a sister in Bengaluru) "never agreed" to the 2004 partition.
- Seller wants ₹5 lakh token "in cash, to keep it simple".
"""

L3 = lesson(
    6, 3,
    outcome='You can run a full due-diligence checklist on a property, record the evidence and decide when to bring in an advocate or surveyor.',
    split='15 minutes reading, 55 minutes running the checklist',
    core=f"""
{SAFE}

**The full due-diligence checklist** brings together everything in Part B: title and EC (RE-M06-L01), land records (RE-M03), land type and legal limits (RE-M04), building papers (RE-M05-L04) and physical verification (RE-M06-L02). The full checklist is in the templates below and in your toolkit.

**How to run it:**
1. Get the owner's written permission and a copy of all documents.
2. Go section by section; for each item, record the evidence (file name or photo) or "missing".
3. Mark each issue as **minor** (fixable by the seller before sale), **major** (needs an advocate or surveyor) or **deal-breaker** (walk away or advise the client to).
4. Hand the file to the buyer's advocate for the title opinion. Your work saves the advocate time and the client money.

**When to bring in an advocate (always for a sale):** any break in the title chain, missing heirs, POA sales, wills, settlements with life interest, mortgages, agreements with others, cases, nilam land or conversion, assigned land, CRZ or ESA questions, and for drafting.

**When to bring in a licensed surveyor:** area mismatch, unclear or disputed boundaries, no sketch, resurvey errors, or encroachment.

**Never** tell a client a title is "clear" yourself. Say: "My checks found no problems in these items; the advocate's opinion is needed before you pay more than a token."
""",
    example=CASE + """
**Sachin's findings:**
- **Deal-breaker until resolved:** the sister's possible non-consent to the 2004 partition (if she did not sign, she may still have a share). Advocate needed.
- **Major:** the 2018 mortgage without a registered release. Bank closure and release needed before sale.
- **Minor:** water-logging on the north side; reflect in price and design.
- **Refuse:** the cash token; ₹5 lakh in cash breaks the cash limit. Token by bank transfer only, after the advocate's first review.
Decision: "Proceed only with conditions": the advocate checks the partition; the seller clears the mortgage; token by bank transfer with a written receipt that refers to these conditions.
""",
    pro="""
- **Advocate:** always, for the title opinion on any sale.
- **Licensed surveyor:** whenever area or boundaries are unclear.
""",
    resources=[
        ('hc-ec', 'Re-check the EC process for your checklist', '5 minutes'),
        ('ksdma', 'Re-check hazard maps for the property', '5 minutes'),
        ('ecourts', 'Party-name search for litigation', '10 minutes'),
    ],
    steps=[
        'Choose a real property where the owner gives written permission (best: your family\'s), or use the sample case above.',
        'Run the full checklist, recording evidence for each item.',
        'Classify every issue as minor, major or deal-breaker, and name the professional for each.',
        'Write a one-page due-diligence summary for the client, with a clear decision and conditions.',
    ],
    proof='The completed checklist with evidence (private), the issue classification and the one-page summary.',
    templates=[('Due-diligence checklist', tools.DUE_DILIGENCE), ('Due-diligence summary', """DUE-DILIGENCE SUMMARY        Property ______  For client ______  Date ______
Prepared by ______ (broker; this is not a legal opinion)
Checks completed: title chain __ EC __ land records __ land type __ building __ site __ litigation __
DEAL-BREAKERS: ______
MAJOR (advocate / surveyor needed): ______
MINOR (seller to fix): ______
RECOMMENDATION: proceed / proceed with conditions / do not proceed
Conditions: ______
Next step: advocate's written title opinion by ______ ; token only by bank transfer with conditions""")],
    mistakes=[
        ('Telling a client the title is clear.', 'Only an advocate gives a title opinion.'),
        ('Skipping evidence.', 'Record a file or photo for every item.'),
        ('Letting a client pay a big token before checks.', 'Keep the token small and conditional.'),
    ],
    fraud="""
**Pressure to skip checks.** "Another buyer is ready; pay today" is a classic pressure tactic. A genuine seller with clean papers can wait a few days for an advocate's check.
""",
    quiz=[
        Q('Who gives the title opinion?', 'An advocate', 'The broker', 'The seller', 'The neighbour', why='Your checklist supports the advocate\'s work.'),
        Q('In the sample case, what is the biggest issue?', 'A sibling who may not have agreed to the partition', 'Water-logging', 'The price per cent', 'The road width', why='She may still have a share.'),
        Q('When should a licensed surveyor be called?', 'When area or boundaries are unclear or disputed', 'Never', 'Only for flats', 'Only after registration', why='Surveyors measure and fix boundaries.'),
        Q('How should the token be paid in the sample case?', 'By bank transfer with a written receipt and conditions', 'In cash', 'By a promise', 'In gold', why='Cash limits and safety.'),
    ],
    study='read the lesson and the full checklist',
    action='run the full due-diligence checklist on a real (permitted) property or the sample case',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    6,
    overview=f"""
Due diligence: the title chain and EC, litigation checks, physical verification of boundaries, roads, flood and slope risks, and a full checklist with clear decisions about when to bring in an advocate or surveyor.

This is the skill that protects your clients and your reputation. Most property frauds and bad deals in Kerala would be caught by a careful checklist plus an advocate's opinion. Everything is {RULE}.
""",
    outcomes=[
        'Trace a 30-year title chain and read an EC.',
        'Check for litigation using official sources.',
        'Verify a property on site.',
        'Run the full checklist and classify issues.',
    ],
    lessons=LESSONS,
    project='a full due-diligence file on one property',
    project_steps=[
        'Choose a permitted real property or the sample case in RE-M06-L03.',
        'Complete the title chain and EC sheet, site-visit checklist and full checklist.',
        'Write the one-page summary with a decision.',
        'If possible, ask an advocate to review your summary briefly (part of your interview in RE-M11-L01).',
    ],
    project_proof='The full file (private) and the summary.',
    rubric=[
        ('Title and EC', 'Not checked', 'Latest deed and short EC', '30-year chain and EC with every entry explained'),
        ('Site', 'No visit', 'Visit without checklist', 'Full checklist with photos and maps'),
        ('Judgement', 'Says "title clear"', 'Lists issues', 'Classifies issues and names the professional for each'),
        ('Ethics', 'Accepts cash or pressure', 'Some caution', 'Conditions, bank transfer and advocate before money'),
    ],
    short=[
        'Read one EC and draw the chain.',
        'Run the checklist on the sample case.',
    ],
    flashcards=[
        ('EC', 'Lists registered transactions on a property for a period.'),
        ('What an EC doesn\'t show', 'Court cases, unregistered deals, some claims.'),
        ('Title chain', 'Prior documents for at least 30 years.'),
        ('eCourts', 'Search cases by party name.'),
        ('Right of way', 'Registered easement for a private access path.'),
        ('Deal-breaker', 'An issue that stops the deal until resolved.'),
        ('Who gives a title opinion?', 'An advocate.'),
    ],
    mistakes=[
        ('Doing checks after the advance.', 'Check before money moves beyond a small conditional token.'),
        ('Trusting copies from the seller only.', 'Get certified copies and ECs yourself.'),
        ('Overstepping.', 'You check; the advocate and surveyor decide.'),
    ],
    tools=[
        'Title chain and EC sheet (RE-M06-L01).',
        'Site-visit checklist (RE-M06-L02).',
        'Due-diligence checklist and summary (RE-M06-L03).',
    ],
    toolkit=[
        'Due-diligence checklist (full).',
        'Due-diligence summary template.',
        'Site-visit checklist.',
    ],
)
