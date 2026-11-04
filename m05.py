from common import lesson, module, link, rules, xref, table, fence, Q, RULE, ASOF, CHECK
import tools

SAFE = f'You are learning to **read** these documents and spot problems, not to draft them. Deeds are drafted by licensed document writers or advocates. Rates and rules are {RULE}.'

DEED_PARTS = [
    ('Heading and date', 'Type of deed (sale deed, ആധാരം), date and place of execution', 'Wrong deed type for the deal'),
    ('Parties', 'Seller(s) and buyer(s) with names, parents\' names, ages, addresses, ID details', 'A co-owner or heir missing; names differ from the prior deed'),
    ('Recitals (history of title)', 'How the seller got the property: prior deed number, year and SRO, inheritance, partition', 'Gaps in the chain; prior deed not mentioned'),
    ('Consideration', 'The price and how it was paid (bank transfer details)', 'Price far below market; "paid in cash"'),
    ('Operative clause', 'The words that transfer the property ("hereby sell, convey and transfer")', 'Missing or conditional wording'),
    ('Schedule of property', 'District, taluk, village, desam, survey/resurvey numbers, area, boundaries on four sides', 'Area or numbers that don\'t match the tax receipt and sketch'),
    ('Covenants', 'Seller\'s promises: clear title, no encumbrances, will indemnify the buyer', 'No promise of clear title'),
    ('Signatures, witnesses, photos', 'Parties sign before two witnesses; photos and thumb impressions at the SRO', 'Signatures that differ from earlier deeds'),
    ('SRO endorsements', 'Document number, book, year, stamp duty paid, registration fee', 'No registration number: not a registered deed'),
]

L1 = lesson(
    5, 1,
    outcome='You can read an agreement for sale and a sale deed, name each part and spot the common red flags.',
    split='20 minutes reading, 40 minutes annotating a sample deed',
    core=f"""
{SAFE}

**Agreement for sale (വില്പന കരാർ, karar).** Signed after the token advance, before the sale deed. It sets the price, the advance paid, the balance and when it is due, the date by which the sale deed must be registered, who pays stamp duty and fees, the seller's duty to give documents, and what happens if either side backs out (usually: the buyer loses the advance if the buyer backs out; the seller returns double, or the advance plus damages, if the seller backs out; terms vary).
- It **does not transfer ownership** (TPA s.54, RE-M04-L01).
- If the buyer takes possession under it and wants to rely on part-performance (TPA s.53A), it must be registered (Registration Act s.17, as amended in 2001).
- It is stamped as an agreement; an advocate or document writer should draft it.

**Sale deed (വിലയാധാരം / ആധാരം).** The registered document that transfers ownership. Its standard parts:

{table(['Part', 'What it contains', 'Red flags'], DEED_PARTS)}

**The deed chain.** Each deed recites how the seller got the property. Reading back through the prior deeds (and partition deeds or wills) gives the **title chain**, usually checked for at least 30 years (RE-M06-L01).

**Language.** Most older Kerala deeds are in Malayalam; newer ones may be in Malayalam or English. You should be able to find the parties, schedule, consideration and registration details in either language. Ask a document writer to explain unfamiliar terms.
""",
    example="""
Sachin reads a sample sale deed (a real deed of his family's, with permission, names masked):
- Heading: sale deed, registered at Kuttiady SRO, document 1234/2009.
- Parties: two sellers (brother and sister, heirs of their father).
- Recitals: the father got the land by a 1982 partition deed, document 567/1982, Kuttiady SRO.
- Consideration: ₹3,60,000 (2009).
- Schedule: Velom village, resurvey 344, 4.86 ares (12 cents), boundaries: east, road; west, Kunhammed's property; north, a canal; south, Ammini's property.
- Endorsements: stamp duty and fee paid, registered.
His notes: all heirs signed ✓; recitals give a prior deed to check ✓; schedule matches the tax receipt ✓. The question to ask an advocate: whether the 1982 partition included all heirs at that time.
""",
    rules_rows=[
        ('Agreement for sale', 'Creates no interest in the property; register it if relied on for part-performance', 'TPA s.54 (Indian Kanoon); Registration Act s.17 (iPleaders)'),
        ('Sale deed', 'Must be registered to transfer ownership', 'TPA s.54'),
    ],
    pro="""
- **Document writer or advocate:** drafts the agreement and deed.
- **Advocate:** gives a title opinion based on the deed chain and EC (the bank's advocate also does this for loans).
""",
    resources=[
        ('tpa-54', 'Re-read section 54 with the agreement and deed in mind', '5 minutes'),
        ('reg-act', 'Re-read the part on documents that must be registered', '10 minutes'),
    ],
    steps=[
        'Get a real sale deed you are allowed to read (your family\'s) or ask a document writer to show you a sample with names hidden.',
        'Using the table above, annotate each part on a copy (paper or PDF).',
        'List every prior document mentioned in the recitals (number, year, SRO).',
        'Write three questions you would ask an advocate about this deed.',
    ],
    proof='An annotated copy (names and numbers masked if shared), the list of prior documents and your three questions.',
    templates=[('Deed reading sheet', """DEED READING SHEET     Deed no. ______ / year ______ / SRO ______
Type: sale / gift / partition / settlement / release / other ______
Parties: seller(s) ______  buyer(s) ______  all co-owners/heirs signed? Y/N
Recitals: prior document(s) ______ (no./year/SRO) ; inheritance? ______
Consideration: ₹ ______ ; payment mode ______
Schedule: village ______ survey/resurvey ______ area ______ ; boundaries E__ W__ N__ S__
Matches tax receipt and sketch?  Y/N
Covenants: clear title promised? Y/N
Registered (number and endorsements)? Y/N
Questions for advocate: 1 ______ 2 ______ 3 ______""")],
    mistakes=[
        ('Reading only the latest deed.', 'Follow the recitals back through the chain.'),
        ('Skipping the schedule.', 'Match numbers, area and boundaries to the land.'),
        ('Drafting agreements for clients.', 'Leave drafting to a document writer or advocate.'),
    ],
    fraud="""
**Forged or altered deeds.** Fake certified copies, altered schedules or forged signatures exist. Compare signatures with earlier deeds, get certified copies from the SRO yourself and check the document number in the EC (RE-M06-L01).
""",
    quiz=[
        Q('Does an agreement for sale make the buyer the owner?', 'No, only the registered sale deed transfers ownership', 'Yes, once the advance is paid', 'Yes, if notarised', 'Yes, after one month', why='TPA s.54.'),
        Q('Which part of a sale deed describes the land\'s village, survey number, area and boundaries?', 'The schedule of property', 'The recitals', 'The covenants', 'The heading', why='Match it to the tax receipt and sketch.'),
        Q('What do the recitals tell you?', 'How the seller got the property', 'The buyer\'s income', 'The rent', 'The building plan', why='They lead you back through the title chain.'),
        Q('Who should draft a sale deed?', 'A licensed document writer or advocate', 'The broker', 'The buyer', 'Anyone with a template', why='Brokers must not draft deeds.'),
    ],
    study='read the lesson and the deed parts table',
    action='annotate a real or sample sale deed and list its prior documents',
)

L2 = lesson(
    5, 2,
    outcome='You can explain gift, partition, settlement and release deeds and powers of attorney, and the risks of each in a deal.',
    split='25 minutes reading, 30 minutes on the action task',
    core=f"""
{SAFE}

Much Kerala property passes within families, so you will see these documents in nearly every title chain.

**Gift deed (ദാനാധാരം).** A transfer without payment. Under the TPA it must be registered, signed by the donor and accepted by the donee during the donor's lifetime. Stamp duty on gifts to close family members is reported as lower (around 2%) than on sales; gifts to others are charged like sales ({link('sy-stamp', 'Square Yards')}; {CHECK}).

**Settlement deed (ധനനിശ്ചയാധാരം).** Common in Kerala: a parent settles property on a child or relative, sometimes keeping a **life interest** (the right to live on or use the property for life). A settlement may have conditions; read them carefully. A buyer from the settlee needs to know whether the life interest has ended (the settlor has died) or has been released.

**Partition deed (ഭാഗപത്രം).** Divides jointly held family property among co-owners or heirs. Problems arise if an heir was left out, a minor's share was not protected or the shares don't add up.

**Release deed (ഒഴിമുറി).** One co-owner gives up their share in favour of others. Common when siblings release shares to one sibling.

**Will (ഒസ്യത്ത്).** Takes effect only after death; registration is optional, so unregistered wills appear. A will can be challenged. A buyer from someone who inherited under a will should get an advocate's view; probate rules depend on the situation.

**Power of attorney (POA, മുക്ത്യാർ).** Lets an agent act for the owner, for example an NRI who cannot attend registration.
- A POA to sell immovable property should be **registered**, and the agent must act within its powers. The stamp duty for a GPA for sale was reported as a fixed ₹1,000 ({link('sy-stamp', 'Square Yards')}).
- A POA **does not transfer ownership**. The Supreme Court in *Suraj Lamp & Industries v. State of Haryana* (2011) held that "GPA sales" (sale agreement + GPA + will) do not convey title; only a registered sale deed does ({link('tg-gpa', 'TaxGuru summary')}).
- A POA ends if the owner dies or cancels it. Always check that the owner is alive and the POA has not been cancelled, and if possible speak to the owner by video call.
- A POA signed abroad must be executed before the Indian embassy or consulate (or notarised and apostilled) and then adjudicated (stamped) in Kerala within the time limit; {CHECK} with an advocate.
""",
    example="""
A 20-cent property near Thottilpalam is offered by "Rajan, power of attorney holder for his brother in Dubai". Sachin asks for:
1. The POA: registered at which SRO and when? Does it give power to sell and receive money?
2. Proof the owner (the brother) is alive and has not cancelled the POA: a recent video call arranged by the buyer's advocate.
3. The title chain: the brother got the land by a 1995 partition deed. Were all heirs included?
4. The sale price paid into the **owner's** bank account, not Rajan's.
The buyer's advocate also checks the EC for any cancellation of the POA registered at the SRO.
""",
    rules_rows=[
        ('GPA sales', 'Sale agreement + GPA + will does not transfer title; only a registered conveyance does', 'TaxGuru summary of Suraj Lamp (2011)'),
        ('Family gift or settlement duty', 'Reported around 2% (lower than a sale)', 'Square Yards'),
        ('GPA for sale', 'Reported ₹1,000 stamp duty', 'Square Yards'),
    ],
    pro="""
- **Advocate:** every title chain with a will, settlement with life interest, partition where an heir may be missing, or a POA sale.
""",
    resources=[
        ('tg-gpa', 'Read the summary of the Suraj Lamp decision', '10 minutes'),
        ('sy-stamp', 'Find the rates for gift, settlement, partition and POA', '10 minutes'),
    ],
    steps=[
        'Ask a family elder (or a document writer) how land in your family passed down: partition, settlement, gift, will. Draw the chain as a family tree with document types.',
        'For one link in the chain, find the document (with permission) and note its type, number, year and SRO.',
        'List two risks you would check for that type of document.',
        'Write a POA checklist for NRI sellers (5 points).',
    ],
    proof='The family title-chain diagram (private), notes on one document and your POA checklist.',
    templates=[('Family-transfer and POA checklist', """FAMILY TRANSFER CHECK
Gift: registered? accepted by donee? donor alive at acceptance?  Y/N
Settlement: life interest? ended (death certificate) or released?  Y/N; conditions? ______
Partition: all heirs included (legal heir certificate)? minors' shares? shares add up?  Y/N
Release: registered? releasing person's share clear?  Y/N
Will: registered? probate needed? challenged?  -> advocate
POA CHECK (seller acting through an attorney)
1 Registered POA (SRO ______ no. ______) with power to sell and receive money?
2 Owner alive and POA not cancelled (video call; EC search for cancellation)?
3 Foreign POA executed at embassy/notarised + apostilled, and adjudicated in Kerala?
4 Sale money paid to the OWNER's account?
5 Buyer's advocate has seen the original POA?""")],
    mistakes=[
        ('Treating a POA holder as the owner.', 'The owner is the owner; the attorney only acts for them.'),
        ('Ignoring a life interest in a settlement.', 'Check whether it has ended.'),
        ('Assuming all heirs agreed.', 'Ask for a legal heir certificate and check signatures.'),
    ],
    fraud="""
**Forged or cancelled POAs.** A classic Kerala fraud uses a forged POA from an NRI owner, or a POA that was cancelled or whose owner has died. Always verify with the owner directly and pay the owner's own account.
""",
    quiz=[
        Q('Does a general power of attorney transfer ownership?', 'No; only a registered sale deed does', 'Yes, if registered', 'Yes, after a year', 'Yes, with a will', why='Suraj Lamp (2011).'),
        Q('What is a common risk in a settlement deed?', 'A life interest that may not have ended', 'It is always invalid', 'It needs no registration', 'It cannot be sold', why='Check the settlor\'s status and conditions.'),
        Q('What document gives up one co-owner\'s share in favour of others?', 'A release deed (ഒഴിമുറി)', 'A sale agreement', 'A rental agreement', 'An EC', why='Common between siblings.'),
        Q('When does a POA end?', 'When the owner dies or cancels it', 'Never', 'After the sale agreement', 'After 30 days always', why='Check both before any deal.'),
    ],
    study='read the lesson and the Suraj Lamp summary',
    action='draw your family\'s title chain and write a POA checklist',
)

L3 = lesson(
    5, 3,
    outcome='You can read a rental or lease agreement, check its key clauses and stamp and registration needs, and use a rental agreement checklist.',
    split='20 minutes reading, 40 minutes annotating a sample agreement',
    core=f"""
{SAFE}

**Rental agreement (വാടകച്ചീട്ട് / വാടക കരാർ)** and **lease (പാട്ടം)**: for houses, flats, shops and offices.

**Key clauses** (an advocate should prepare your standard template):
1. Parties, with ID details, and the property description.
2. **Period** (commonly 11 months for houses), start date, renewal terms and rent increase (for example 5% to 10% on renewal).
3. **Rent**, due date, mode (bank transfer or UPI) and late-payment terms.
4. **Security deposit:** amount, how it is held and when and how it is returned (after deducting only agreed items). The Kerala Rent Control Act allows an advance of up to one month's rent (RE-M04-L05); larger deposits are common, so make the terms clear and get advice.
5. **Use:** residential or commercial; no subletting without consent.
6. **Maintenance:** who pays for what (minor repairs, major repairs, painting, electricity, water, building tax).
7. **Notice period** for either side (often one to three months).
8. **Inventory** of fittings and furniture, with photos and meter readings at handover.
9. **Entry:** when the owner can inspect, with notice.
10. **Disputes:** how they will be resolved.

**Stamp duty and registration.** Leases for more than one year must be registered (Registration Act s.17). Stamp duty on a lease up to one year was reported as 1% of the rent for the period ({link('sy-stamp', 'Square Yards')}); longer leases are charged differently. Even an 11-month agreement must be on stamp paper of the right value; {CHECK}.

The full rental agreement checklist is in the template below and in your toolkit.
""",
    example="""
A teacher couple want to rent a 2-bedroom house in Kakkattil from an owner in Qatar for ₹9,000 a month. The owner's sister manages it. Sachin uses the advocate-reviewed template:
- 11 months from 1 December, rent ₹9,000 by UPI by the 5th of each month, 7% increase on renewal.
- Deposit: the owner wants ₹50,000; Sachin tells the owner about the Act's one-month limit and suggests getting the advocate to set the terms; they agree a smaller deposit by bank transfer with written return terms.
- Inventory: 4 fans, 2 cots, water tank and pump, meter readings photographed.
- Notice: 2 months either side.
- Stamp paper: as advised by the document writer for an 11-month agreement.
The sister signs with a written authorisation from the owner (or a POA, if needed).
""",
    rules_rows=[
        ('Leases over one year', 'Must be registered', 'Registration Act s.17 (iPleaders)'),
        ('Lease up to one year', 'Stamp duty reported as 1% of rent', 'Square Yards'),
        ('Advance', 'Up to one month\'s rent under the Rent Act', 'India Code PDF'),
    ],
    pro="""
- **Advocate:** prepares your standard rental template, and handles any disputes or evictions.
""",
    resources=[
        ('rent-act', 'Re-read sections 5, 8 and 11', '15 minutes'),
        ('sy-stamp', 'Find the lease stamp duty rates', '5 minutes'),
        ('nobroker', 'See how online platforms describe rental agreements and what they include (don\'t copy their template)', '10 minutes'),
    ],
    steps=[
        'Get a sample rental agreement (your own, a relative\'s with permission, or one a broker shows you with names hidden).',
        'Check it against the rental agreement checklist and mark missing clauses.',
        'Ask a document writer or advocate what stamp paper value they use for an 11-month house agreement in your area and what they charge.',
        'Write the clause list you would want in your own template (an advocate will draft it).',
    ],
    proof='The annotated sample (masked), the missing clauses list and stamp-paper notes.',
    templates=[('Rental agreement checklist', tools.RENTAL_AGREEMENT)],
    mistakes=[
        ('Using a free template from the internet unchanged.', 'Use an advocate-reviewed template for Kerala.'),
        ('Skipping the inventory and meter readings.', 'Photos at handover prevent deposit disputes.'),
        ('Taking the deposit in cash.', 'Use bank transfer with a receipt.'),
    ],
    fraud="""
**Fake landlords.** Scammers advertise houses they don\'t own, collect deposits and disappear. Always confirm ownership (deed or building tax receipt in the owner's name) and pay only after the agreement is signed.
""",
    quiz=[
        Q('Which rental agreements must be registered?', 'Leases for more than one year', 'All agreements', 'None', 'Only shops', why='Registration Act s.17.'),
        Q('Why record an inventory with photos at handover?', 'To prevent disputes over damage and the deposit', 'For marketing', 'For tax', 'It is not useful', why='It is the evidence for both sides.'),
        Q('What should the agreement say about the deposit?', 'Amount, mode of payment and how and when it is returned', 'Nothing', 'Only the amount', 'That it is never returned', why='Clear terms avoid disputes.'),
        Q('What is a sign of a fake landlord?', 'They can\'t show ownership papers and want the deposit before signing', 'They have a building tax receipt', 'They use an advocate\'s template', 'They want UPI payment', why='Confirm ownership first.'),
    ],
    study='read the lesson and the rental agreement checklist',
    action='check a sample rental agreement against the checklist',
)

L4 = lesson(
    5, 4,
    outcome='You can check building permits, occupancy certificates, building tax receipts and NOCs for a house or flat, and know what is missing when they are not there.',
    split='20 minutes reading, 35 minutes on the action task',
    core=f"""
{SAFE}

**Building documents to ask for:**
- **Building permit** from the panchayat or municipality, with the approved plan (now through K-SMART; RE-M04-L04).
- **Occupancy certificate (OC)** or completion approval: issued when the building is completed as per the permit. Without it, the building may be irregular.
- **Building number and property (building) tax receipts:** the local body gives a building number after the OC and assesses property tax. Tax receipts in the owner's name, paid up to date, are important.
- **Ownership certificate** from the local body (for the building; RE-M03-L02).
- **Regularisation:** some buildings built without permits or with deviations are later regularised by paying a fee; ask for the order.
- **NOCs (no-objection certificates)** that may apply: fire (for larger buildings), pollution control (for some commercial uses), the Airports Authority (near airports such as Calicut), the railway (near railway land), the PWD or NHAI (near highways), and the Archaeological Survey (near protected monuments).
- **Utilities:** electricity (KSEB) consumer number and bills, water (KWA) connection, in the owner's name.
- **For flats:** RERA registration, the builder's agreement, the association's no-dues letter, the share of land and common areas.

**What to do when something is missing:** note it, ask the seller why, and get an advocate's and an engineer's view. A missing OC or a building larger than the permit is a common Kerala problem, especially with Gulf-funded houses built in stages.

**Matching documents to the building:** compare the plinth area in the permit with what you see; count floors and rooms; check the building number on the tax receipt matches the house.
""",
    example="""
A 1,800 sq ft two-storey house in Kuttiady grama panchayat (so the permit comes from the panchayat). The owner shows:
- Permit (2014) for a single-storey house of 1,100 sq ft.
- Building tax receipt for 1,100 sq ft.
- The first floor (700 sq ft) was added in 2019 without a new permit.
Sachin's notes: the first floor may be unauthorised; ask whether it was regularised; the buyer's bank may refuse to lend on the unauthorised area; the price should reflect this. He refers the buyer to an engineer and an advocate before any advance.
""",
    rules_rows=[
        ('Permit system', 'K-SMART for new permits in all local bodies from April 2025', 'The Week; Sanketham notice'),
        ('Building rules', 'KPBR / KMBR 2019, as amended', 'LSGD PDF'),
    ],
    pro="""
- **Licensed engineer:** compares the building with the approved plan.
- **Advocate:** advises on missing OCs, regularisation and the effect on the sale and loan.
""",
    resources=[
        ('week-ksmart', 'Re-read about K-SMART services', '5 minutes'),
        ('hc-online', 'Read about online property tax and building services', '10 minutes'),
        ('kpbr', 'Search the PDF for "occupancy" to see the relevant rule', '10 minutes'),
    ],
    steps=[
        'With permission, check one house\'s papers (your own family\'s): permit, plan, OC, building number, latest tax receipt.',
        'Compare the permit area with the actual building (approximate measurement).',
        'Ask at the panchayat or municipality front office how a buyer can verify a building permit and building number, and note the answer.',
        'Build a building-document checklist (use the toolkit\'s document checklist as a start).',
    ],
    proof='The comparison for one building (private), the verification procedure and your checklist.',
    templates=[('Document checklist by deal type', tools.DOC_CHECKLIST)],
    mistakes=[
        ('Ignoring a missing OC.', 'Find out why; it affects loans and value.'),
        ('Not comparing the permit with the building.', 'Extra floors and extensions are common.'),
        ('Forgetting NOCs near airports, railways and highways.', 'Check location-specific NOCs.'),
    ],
    fraud="""
**Fake permits and tax receipts.** Edited permit copies and fake tax receipts are used to sell irregular buildings. Verify the permit number and building number with the local body directly.
""",
    quiz=[
        Q('What does an occupancy certificate show?', 'The building was completed as per the permit', 'The owner has no loans', 'The land type', 'The fair value', why='Without it, the building may be irregular.'),
        Q('Who issues building permits in a grama panchayat?', 'The panchayat (now through K-SMART)', 'The SRO', 'K-RERA', 'The village office', why='Permits come from the local body.'),
        Q('A house has a first floor added without a permit. What should you do?', 'Note it and refer the buyer to an engineer and advocate before any advance', 'Ignore it', 'Tell the buyer it\'s normal and fine', 'Hide it from the buyer', why='It affects loans, value and legality.'),
        Q('Which NOC may matter near Calicut airport?', 'Airports Authority of India height clearance', 'Pollution control only', 'None', 'RERA', why='Location-specific NOCs apply.'),
    ],
    study='read the lesson and the document checklist',
    action='check one building\'s papers against the building and the checklist',
)

LESSONS = [L1, L2, L3, L4]

MODULE = module(
    5,
    overview=f"""
The documents of Kerala real estate: agreements for sale and sale deeds; gift, settlement, partition and release deeds, wills and powers of attorney; rental agreements and leases; building permits, occupancy certificates, tax receipts and NOCs.

You will read and annotate real or sample documents. Use your own family's papers with permission, or samples shown by a document writer with names hidden. Never share other people's documents. Everything is {RULE}.
""",
    outcomes=[
        'Read an agreement for sale and a sale deed and spot red flags.',
        'Explain family transfers and powers of attorney and their risks.',
        'Check a rental agreement against a checklist.',
        'Check building permits, OCs, tax receipts and NOCs.',
    ],
    lessons=LESSONS,
    project='an annotated document pack: sale deed, EC (from RE-M06) and rental agreement',
    project_steps=[
        'Annotate one sale deed with the deed reading sheet (RE-M05-L01).',
        'Draw the title chain with document types (RE-M05-L02).',
        'Annotate one rental agreement with the checklist (RE-M05-L03).',
        'Check one building\'s papers (RE-M05-L04).',
        'Add the EC annotation after RE-M06-L01.',
    ],
    project_proof='The annotated pack with names and numbers masked if shared.',
    rubric=[
        ('Sale deed', 'Can\'t find the parts', 'Finds most parts', 'Annotates every part and lists questions'),
        ('Family transfers', 'Not understood', 'Knows types', 'Draws a chain and names the risk in each link'),
        ('Rental agreement', 'No checklist', 'Some clauses checked', 'Full checklist with gaps marked'),
        ('Building papers', 'Not checked', 'Some checked', 'Permit, OC, tax and NOCs checked against the building'),
    ],
    short=[
        'Annotate one sale deed.',
        'Learn why a POA doesn\'t transfer ownership.',
    ],
    flashcards=[
        ('Agreement for sale (കരാർ)', 'Sets terms; doesn\'t transfer ownership.'),
        ('Sale deed (ആധാരം)', 'Registered document that transfers ownership.'),
        ('Recitals', 'How the seller got the property.'),
        ('Schedule', 'Village, survey numbers, area and boundaries.'),
        ('Settlement deed', 'Family transfer, may keep a life interest.'),
        ('Release deed (ഒഴിമുറി)', 'Co-owner gives up a share.'),
        ('Suraj Lamp (2011)', 'GPA sales don\'t transfer title.'),
        ('OC', 'Occupancy certificate: building done as per permit.'),
    ],
    mistakes=[
        ('Practising on strangers\' documents.', 'Use your own or masked samples.'),
        ('Drafting documents yourself.', 'Leave it to document writers and advocates.'),
        ('Skipping building papers for houses.', 'Missing OCs are common.'),
    ],
    tools=[
        'Deed reading sheet (RE-M05-L01).',
        'Family-transfer and POA checklist (RE-M05-L02).',
        'Rental agreement checklist (RE-M05-L03).',
        'Document checklist by deal type (RE-M05-L04).',
    ],
    toolkit=[
        'Deed reading sheet.',
        'Family-transfer and POA checklist.',
        'Rental agreement checklist and document checklist.',
    ],
)
