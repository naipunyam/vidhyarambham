from common import lesson, module, link, rules, xref, table, fence, Q, RULE, ASOF, CHECK
import tools

ROLES = [
    ('Broker (you)', 'Coordinates the timeline, collects documents, keeps both sides informed, books appointments', 'Drafting deeds, title opinions, measuring boundaries, tax advice'),
    ('Advocate', 'Title opinion; drafts or reviews the agreement; advises on problems', '—'),
    ('Licensed document writer', 'Drafts the sale deed and other documents for registration; calculates duty', '—'),
    ('Licensed surveyor', 'Measures and fixes boundaries; prepares sketches', '—'),
    ('Bank (if loan)', 'Sanctions the loan; its advocate and valuer check the property; pays the seller', '—'),
    ('Chartered accountant', 'Capital gains, TDS (especially NRI sellers), tax planning', '—'),
    ('Sub-Registrar Office (SRO)', 'Registers the document after checking duty, identities and signatures', '—'),
]

L1 = lesson(
    14, 1,
    outcome='You can manage a sale from token advance to a signed agreement for sale, coordinating due diligence and the professionals involved.',
    split='15 minutes reading, 45 minutes building a transaction file',
    core=f"""
**The transaction timeline** (toolkit) takes a sale from offer to handover. Your job is to keep it moving, keep both sides informed and make sure nothing is skipped.

{fence(tools.TIMELINE)}

**Week 1 after the token:**
1. Open a **transaction file** (a folder per deal): mandate, token receipt, owner's documents, buyer's details, timeline.
2. Collect copies of all documents (deed and prior deeds, tax receipt, certificates, sketch, building papers) and apply for a fresh EC.
3. Help the buyer choose an **advocate** (the buyer pays and the advocate works for the buyer; you don't pick someone who works for you). Share the documents and your due-diligence summary.
4. If there's a loan, the buyer applies to the bank now with the documents.

**Weeks 2 to 3: due diligence and agreement.**
- The advocate gives a written title opinion; the seller fixes minor issues (mortgage release, tax arrears, missing certificates).
- The **agreement for sale** is drafted by the advocate or a document writer: price, advance (the token plus any further advance), balance and date, registration deadline, who pays which costs, conditions (loan sanction, title clearance), what happens on default, and possession date.
- Further advances also by bank transfer, with receipts.

**Roles:**
{table(['Who', 'Does', 'Must not do (if broker)'], ROLES)}
""",
    example="""
Thottilpalam deal (₹35.5 lakh): token ₹50,000 on day 0. Sachin opens the file and the buyer engages an advocate in Vadakara. By day 6 the fresh EC shows the 2018 mortgage closure letter but no registered release. The advocate asks for the release; the seller's bank registers it by day 18. The advocate's opinion (day 20): title acceptable subject to the release (now done). Agreement for sale signed on day 21: advance ₹3.5 lakh more by bank transfer; balance ₹31.5 lakh on registration within 60 days; loan sanction of ₹22 lakh as a condition; refund of advances if the loan is refused for a reason not caused by the buyer.
""",
    pro="""
- **Advocate:** title opinion and agreement.
- **Document writer:** drafting for registration.
""",
    resources=[
        ('tpa-54', 'Re-read: an agreement creates no interest in the property', '5 minutes'),
        ('reg-act', 'Re-read: registration of agreements relied on for part-performance', '10 minutes'),
        ('hc-ec', 'EC application for the fresh EC', '5 minutes'),
    ],
    steps=[
        'Create a transaction file template (folder structure and a cover sheet) in your toolkit.',
        'Fill in the timeline with target dates for a sample deal (or your live deal).',
        'List the advocates and document writers you know (from your interviews) with fees and turnaround times.',
        'Write the checklist of points an agreement for sale must cover, to discuss with the advocate.',
    ],
    proof='The transaction file template, a filled timeline, your professionals list and the agreement checklist.',
    templates=[('Transaction timeline', tools.TIMELINE), ('Transaction file cover sheet', """TRANSACTION FILE      Deal ID ______  Property ______  Price ₹ ______
Seller(s) ______  Buyer(s) ______  Advocate ______  Writer ______  Bank ______
Folders: 01 Mandate | 02 Token | 03 Seller documents | 04 EC | 05 Advocate opinion | 06 Agreement | 07 Loan | 08 Registration | 09 Mutation and handover | 10 Commission
AGREEMENT FOR SALE MUST COVER: price | advances paid (bank refs) | balance and due date | registration deadline |
costs (who pays duty, fees, EC) | conditions (title, loan, release of mortgage) | default terms | possession date | documents to be handed over
Status today ______ ; next step ______ by ______""")],
    mistakes=[
        ('Choosing the buyer\'s advocate for them.', 'Suggest options; the buyer decides and pays.'),
        ('Skipping a fresh EC.', 'Always get one after the token.'),
        ('Loose agreement terms.', 'Use the checklist with the advocate.'),
    ],
    fraud="""
**Last-minute substitutions.** Some sellers bring different documents or a "new" co-owner on agreement day. Check every document against the file, and pause if anything changes.
""",
    quiz=[
        Q('What should you apply for right after the token?', 'A fresh EC', 'A new building permit', 'A K-RERA licence', 'Nothing', why='It catches new transactions.'),
        Q('Who should the buyer\'s advocate work for?', 'The buyer', 'The broker', 'The seller', 'The bank only', why='Independence protects the buyer.'),
        Q('Who drafts the agreement for sale?', 'An advocate or licensed document writer', 'The broker', 'The buyer alone', 'The neighbour', why='Brokers coordinate, not draft.'),
        Q('What is a common condition in the agreement?', 'Loan sanction and title clearance', 'The broker\'s birthday', 'The weather', 'None', why='Protects both sides.'),
    ],
    study='read the lesson and the timeline',
    action='build a transaction file template and fill a timeline for a sample or live deal',
)

L2 = lesson(
    14, 2,
    outcome='You can coordinate the loan, calculate and arrange stamp duty and fees, handle TDS, and prepare both sides for registration at the Sub-Registrar Office.',
    split='20 minutes reading, 50 minutes on the full cost and an SRO visit',
    core=f"""
**Loan stage.** The bank's advocate checks the title (and EC), the valuer checks the property, and the bank issues a sanction and then pays the seller directly on registration (often by demand draft or transfer). Share the documents promptly and keep the timeline realistic: loans often take 3 to 6 weeks.

**Stamp duty and fee.** Calculate on the higher of price or fair value (RE-M04-L01): 8% stamp duty and 2% registration fee for a sale deed ({link('sy-stamp', 'Square Yards')}; {CHECK}). Use the **full cost calculator** (below) with current rates, dated. Stamp duty is paid by **e-stamp**; the document writer will guide.

**TDS.** If the value is ₹50 lakh or more, the buyer deducts 1% and files the required form (Form 141 under the 2025 Act, earlier 26QB) before or at payment ({link('it-tds', 'Income Tax Department')}; RE-M09-L01). Keep the challan with the file.

**Preparing for registration:**
- Draft deed read and approved by both sides (and the bank, if any), well before the day.
- Book the SRO appointment through the document writer.
- **Seller(s):** original title deed, prior deeds, ID, PAN, photos; all co-owners present (or a registered POA).
- **Buyer(s):** ID, PAN, photos; balance by bank transfer or demand draft; TDS challan if applicable.
- **Two witnesses** with ID.
- At the SRO, parties are photographed and give fingerprints; the Sub-Registrar checks identities, duty and signatures, then registers the document. The original is returned after registration (sometimes the same day, sometimes later).

**Payment on the day.** Balance by bank transfer or bank's DD, confirmed before signatures. No cash. The seller gives a written acknowledgement (often in the deed itself).
""",
    example="""
**Full cost for the Thottilpalam buyer (illustrative rates; check current rules):**
- Price ₹35,50,000; fair value ₹14,00,000 (land) + building value; the duty base is the price.
- Stamp duty 8%: ₹2,84,000. Registration fee 2%: ₹71,000.
- Document writer ₹6,000 (quote); EC and copies ₹1,000.
- Brokerage: paid by the seller under the mandate; the buyer pays nothing to Sachin.
- Loan processing and legal/valuation charges: ₹9,500 (bank quote).
- Total extra: about **₹3,71,500 (10.5%)**. Total cost ≈ **₹39.2 lakh**.
- TDS: not applicable (below ₹50 lakh).
""",
    calc="""
In the Cost tab: B1 `3550000`, B2 fair value; B3 `=MAX(B1,B2)`; B6 `=B3*0.08` → 2,84,000; B7 `=B3*0.02` → 71,000; B8 6,000; B9 1,000; B13 9,500; B15 `=SUM(B6:B9,B11:B14)` → 3,71,500; B17 `=B15/B1` → 10.5%.
""",
    rules_rows=[
        ('Stamp duty and fee', '8% + 2% on the higher of price or fair value', 'Square Yards, July 2026'),
        ('TDS', '1% at ₹50 lakh or more; buyer deducts', 'Income Tax Department'),
        ('Presentation for registration', 'Within 4 months of execution', 'Registration Act s.23 (iPleaders)'),
    ],
    pro="""
- **Document writer:** drafting, e-stamp, SRO appointment.
- **CA:** TDS for NRI sellers or values near ₹50 lakh.
""",
    resources=[
        ('sy-stamp', 'Check current duty and fees for the cost tab', '5 minutes'),
        ('it-tds', 'TDS steps', '10 minutes'),
        ('hc-online', 'Read about e-stamping and online registration services', '10 minutes'),
    ],
    steps=[
        'Calculate the full cost of one purchase using current official rates (date-stamped) and real quotes.',
        'Visit your local SRO (or talk to a document writer there) and note: working hours, how appointments work, what parties bring and how long registration takes.',
        'Write a "registration day checklist" for sellers and buyers.',
        'If you have a live deal, prepare both sides with the checklist one week before.',
    ],
    proof='The dated Cost tab, your SRO notes and the registration day checklist.',
    templates=[('Full cost of a purchase', tools.COST_CALC), ('Registration day checklist', """REGISTRATION DAY CHECKLIST     SRO ______  Date ______  Time ______
SELLER(S): original deed [ ] prior deeds [ ] ID + PAN [ ] photos [ ] all co-owners or registered POA [ ]
           latest tax receipt [ ] building tax receipt [ ] keys (if handover today) [ ]
BUYER(S):  ID + PAN [ ] photos [ ] balance by transfer/DD (confirmed) [ ] TDS challan if ₹50 lakh+ [ ]
           e-stamp and fee receipts [ ] bank officer (if loan) [ ]
WITNESSES: two adults with ID [ ]
DRAFT DEED approved by both (and bank) on ______ [ ]
AFTER: deed number ______ ; original collected on ______ ; copies to buyer/bank [ ]""")],
    mistakes=[
        ('Calculating duty on the wrong value.', 'Use the higher of price or fair value.'),
        ('Missing a co-owner on the day.', 'Confirm attendance or a registered POA days before.'),
        ('Cash on registration day.', 'Bank transfer or DD only.'),
    ],
    fraud="""
**Impostor sellers at the SRO.** Fraudsters impersonate owners (especially NRIs or elderly owners) with fake IDs. Meet the real owner early, compare photos and signatures with earlier deeds, and make sure the money goes to the owner\'s account.
""",
    quiz=[
        Q('Who usually pays the seller in a loan-funded purchase?', 'The bank, directly on registration', 'The broker', 'The SRO', 'Nobody', why='The bank pays the seller.'),
        Q('What do parties give at the SRO besides signatures?', 'Photographs and fingerprints', 'Their salary slips', 'Their passwords', 'Nothing', why='Identity checks.'),
        Q('Total extra costs in the example were about:', '10.5% of the price', '1%', '50%', '0%', why='Duty, fee and other costs.'),
        Q('How should the balance be paid on registration day?', 'Bank transfer or demand draft, confirmed before signing', 'Cash', 'Gold', 'A post-dated cheque only', why='No cash.'),
    ],
    study='read the lesson and the registration day checklist',
    action='calculate a full purchase cost with current rates and visit or ask about your local SRO',
)

L3 = lesson(
    14, 3,
    outcome='You can complete a deal after registration: mutation, tax and utility transfers, handover and commission, and work smoothly with document writers, advocates and banks.',
    split='15 minutes reading, 40 minutes on the action task',
    core=f"""
**Mutation (പോക്കുവരവ്, pokkuvaravu).** After registration, the revenue records (thandaper, land tax) must be changed to the buyer's name. Under **Ente Bhoomi**, integration of Registration and Revenue supports **auto-mutation** in covered villages ({link('entebhoomi-nic', 'NIC')}); elsewhere, the buyer applies at the village office (or online) with the deed copy. Check that mutation is done and pay the next land tax in the buyer's name; {CHECK}.

**Building tax and ownership.** Apply to the panchayat or municipality (through K-SMART) to change the building's owner in the tax records. Get the new ownership certificate later if needed.

**Utilities.** Transfer the KSEB electricity connection and the KWA water connection to the buyer (each has its own process and documents). Read meters at handover.

**Handover.** Walk through the property with both sides; hand over keys, the original deed (if not with the bank), prior deeds, tax receipts and building papers; sign a short handover note with meter readings and an inventory.

**Your commission.** Invoice the party who pays (as per the mandate) after registration; payment by bank transfer; GST if you are registered. Record it in your Income tab.

**After the deal:** thank both sides, ask for an honest review, and keep the file for future reference (and for your tax records). A follow-up call a month later often brings referrals.

**Working with professionals.** Build good relationships with a few advocates, document writers and bank officers: send complete files, respect their time and fees, don't ask them to cut corners, and never take secret referral payments that the client doesn't know about.
""",
    example="""
Thottilpalam deal, after registration on day 52:
- Day 52: deed registered; the bank keeps the original (mortgage); the buyer gets a certified copy.
- Day 60: Sachin helps the buyer check mutation; the village is covered by Ente Bhoomi and the record shows the buyer\'s name. The buyer pays land tax online.
- Day 65: building tax owner change applied through K-SMART; KSEB and KWA transfer applications submitted.
- Handover note signed with meter readings; keys given.
- Commission: 2% of ₹35.5 lakh = ₹71,000, invoiced to the seller, paid by bank transfer, recorded. (Sachin is not GST-registered, so no GST.)
- One month later, the buyer refers his cousin, who wants a rental.
""",
    resources=[
        ('entebhoomi-nic', 'Read about auto-mutation under Ente Bhoomi', '5 minutes'),
        ('entebhoomi', 'Open the Ente Bhoomi portal to see services for your village', '10 minutes'),
        ('wayanad-tax', 'Land tax payment through ReLIS', '5 minutes'),
    ],
    steps=[
        'Find out how mutation works in your village: auto-mutation under Ente Bhoomi, or an application at the village office.',
        'Find the process for changing building tax ownership in your panchayat (K-SMART) and for KSEB and KWA transfers.',
        'Write a handover note template and a commission invoice template.',
        'Complete the post-registration section of your timeline for a sample or live deal.',
    ],
    proof='Notes on mutation and transfers in your area, the handover note and invoice templates, and the completed timeline.',
    templates=[('Handover note and invoice', """HANDOVER NOTE        Date ______  Property ______
Keys handed over: ___ sets  Meter readings: electricity ______ water ______
Documents handed over: original deed / certified copy [ ] prior deeds [ ] tax receipts [ ] permit/OC [ ] other ______
Inventory items: ______
Mutation status: done / applied on ______   Building tax transfer applied ______   KSEB ______  KWA ______
Seller ______  Buyer ______  Agent ______
COMMISSION INVOICE    No. ______ Date ______
To: ______ (as per mandate dated ______)
For: brokerage services, sale of ______, registered as deed no. ______ / ______ SRO
Amount: ₹ ______ (__% of ₹ ______)  GST: not registered / ______
Pay by bank transfer to: ______ (account in my name)""")],
    mistakes=[
        ('Forgetting mutation.', 'Check revenue records and pay the next land tax in the buyer\'s name.'),
        ('Collecting commission before registration.', 'Invoice after the deal completes, per the mandate.'),
        ('Losing touch after the deal.', 'Follow up for reviews and referrals.'),
    ],
    fraud="""
**Delayed mutation risk.** If mutation is not done, the old owner (or someone impersonating them) can appear in revenue records for longer, which some fraudsters exploit. Complete mutation promptly and keep proof.
""",
    quiz=[
        Q('What is mutation (pokkuvaravu)?', 'Changing revenue records to the buyer\'s name', 'A building permit', 'A loan', 'A rental agreement', why='Follows registration.'),
        Q('What does Ente Bhoomi support in covered villages?', 'Auto-mutation', 'Free land', 'Cash payments', 'RERA registration', why='Integration of registration and revenue.'),
        Q('When should a broker invoice commission on a sale?', 'After registration, as per the mandate', 'Before the first visit', 'On the token day only', 'Never', why='Payment follows completion.'),
        Q('What should a handover note record?', 'Keys, meter readings, documents and inventory', 'Only the price', 'The broker\'s hobbies', 'Nothing', why='Prevents disputes.'),
    ],
    study='read the lesson and the post-registration steps',
    action='find out how mutation and transfers work locally and prepare handover and invoice templates',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    14,
    overview=f"""
Managing a transaction: token, fresh EC, advocate, agreement for sale, loan, stamp duty, TDS, SRO registration, mutation, tax and utility transfers, handover and commission, with clear roles for document writers, advocates and banks.

This module ties Parts B and C together into a step-by-step deal. If you have a live deal, use it; otherwise use the Thottilpalam example as your sample file. Everything is {RULE}.
""",
    outcomes=[
        'Run a deal from token to agreement with due diligence.',
        'Coordinate loan, duty, TDS and SRO registration.',
        'Complete mutation, transfers, handover and commission.',
        'Work well and ethically with professionals.',
    ],
    lessons=LESSONS,
    project='a complete transaction file',
    project_steps=[
        'Use a live deal or the sample case to fill a transaction file from token to handover.',
        'Include the timeline, cost calculation, checklists and templates.',
        'Note who did what (you vs professionals).',
        'Review the file with an advocate or document writer, if they agree.',
    ],
    project_proof='The transaction file (private details masked).',
    rubric=[
        ('Timeline', 'Missing steps', 'Most steps', 'Every step with dates and owners'),
        ('Money', 'Cash or unclear', 'Bank transfers', 'All payments documented with references and TDS if needed'),
        ('Professionals', 'Broker does everything', 'Some professionals', 'Clear roles; broker coordinates only'),
        ('Completion', 'Stops at registration', 'Mutation noted', 'Mutation, transfers, handover and invoice done'),
    ],
    short=[
        'Fill the timeline for the sample deal.',
        'Calculate one full purchase cost.',
    ],
    flashcards=[
        ('After token', 'Fresh EC and buyer\'s advocate.'),
        ('Agreement for sale covers', 'Price, advances, balance date, conditions, default, possession.'),
        ('Loans take', 'Often 3 to 6 weeks.'),
        ('SRO checks', 'Identity, duty, signatures; photos and fingerprints.'),
        ('Pokkuvaravu', 'Mutation of revenue records.'),
        ('Commission timing', 'After registration, per the mandate.'),
    ],
    mistakes=[
        ('Rushing to registration without the advocate\'s opinion.', 'Opinion first.'),
        ('Doing professionals\' work.', 'Coordinate, don\'t draft or certify.'),
        ('Leaving post-registration steps.', 'Finish mutation and transfers.'),
    ],
    tools=[
        'Transaction timeline and file cover sheet (RE-M14-L01).',
        'Full cost calculator and registration day checklist (RE-M14-L02).',
        'Handover note and commission invoice (RE-M14-L03).',
    ],
    toolkit=[
        'Transaction timeline.',
        'Transaction file cover sheet.',
        'Registration day checklist.',
        'Handover note and invoice.',
    ],
)
