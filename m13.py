from common import lesson, module, link, rules, xref, table, fence, Q, RULE, ASOF, CHECK
import tools

NEEDS = [
    ('Purpose', 'Live in, rent out, build later, invest, business use?'),
    ('Must-haves', 'Road access, water, school or work nearby, bedrooms, plot size'),
    ('Deal-breakers', 'Flood risk, steep slope, narrow road, near a quarry'),
    ('Budget', 'Total budget including stamp duty and costs; loan or own money; pre-approved?'),
    ('Timeline', 'When must they buy or move? What happens if they don\'t?'),
    ('Decision makers', 'Spouse, parents, siblings abroad? Who must see it?'),
]

L1 = lesson(
    13, 1,
    outcome='You can understand a buyer\'s or tenant\'s real needs with an intake conversation, shortlist properties honestly and run (or shadow) a professional site visit.',
    split='15 minutes reading, 45 minutes on intake and a site visit',
    core=f"""
**Start with needs, not properties.** Most wasted visits happen because the broker showed what was available, not what the client needed. Use the intake form and ask open questions:
{table(['Area', 'Questions'], NEEDS)}

**Listen for the real reason.** "We want 10 cents near town" may really mean "our children need a school within 2 km and my mother can't climb steps". Repeat back what you heard: "So the most important things are…".

**Shortlist honestly.** Choose 2 to 4 properties that fit. Tell the client the weak points before the visit (narrow road, slope, missing OC). Check affordability first (RE-M08-L01).

**Running a site visit:**
- **Before:** owner's permission and a time; route; documents summary; the site-visit checklist; water, umbrella, a tape and a charged phone. Tell the client the visit is a look, not a commitment.
- **On site:** introduce the owner and client politely; walk the boundaries and road; let the client look without pressure; point out both good and bad; answer honestly ("I don't know; I'll find out" is fine); don't discuss the owner's minimum price.
- **After:** ask for feedback (1 to 5) and questions; send a short written summary the same day; update the CRM with the next step.
- **Safety:** tell someone where you are going; visit unknown places in daylight; for women clients or owners, offer to bring a family member or meet in public first.

If you have no client yet, **shadow** a visit with one of the brokers you interviewed (with their and the client's permission) and fill in the checklist yourself.
""",
    example="""
A Gulf-based nurse and her husband want "a house near Kuttiady for ₹40 lakh". The intake call (on WhatsApp video) reveals: they'll return in 3 years; her parents will live there now; her father uses a walking stick (no steps, level plot); they need a bus stop within 1 km; they have ₹15 lakh saved and will take a loan; her brother in Kakkattil will see houses for them.

Sachin shortlists 3 single-storey houses on level plots near bus routes. Before the visit he tells the brother: "House B has a missing occupancy certificate; we'll need an advocate's view if you like it." He sends a video of each visit to the couple with honest notes, and updates the CRM.
""",
    resources=[
        ('ksdma', 'Check flood and landslide maps before each visit', '5 minutes'),
        ('gearth', 'Plan the route and view the surroundings', '10 minutes'),
    ],
    steps=[
        'Do one full intake conversation with a real buyer or tenant (or a friend role-playing one) using the intake form.',
        'Shortlist 2 to 4 suitable properties from your inventory or co-broke partners, with honest notes.',
        'Conduct a real site visit (with the owner\'s permission) or shadow a broker\'s visit, completing the site-visit checklist.',
        'Send the client a written visit summary and update the CRM.',
    ],
    proof='The intake form (private), the shortlist, the completed site-visit checklist and the summary message.',
    templates=[('Client intake form', tools.INTAKE), ('Site-visit checklist', tools.SITE_VISIT)],
    mistakes=[
        ('Showing many unsuitable properties.', 'Do intake first and shortlist 2 to 4.'),
        ('Hiding weak points until the visit.', 'Tell the client before.'),
        ('Revealing the owner\'s minimum price.', 'That is the owner\'s confidential information.'),
    ],
    fraud="""
**Visit scams.** Fraudsters ask for a "visit fee" or "booking amount" before showing a property, or show a property they don't control. Never charge clients to visit, and never pay anyone before verifying who owns the property.
""",
    quiz=[
        Q('What should come before showing properties?', 'An intake conversation about needs, budget and timeline', 'A token advance', 'A sale agreement', 'A building permit', why='Needs first.'),
        Q('A shortlisted house has no OC. When do you tell the client?', 'Before the visit', 'After registration', 'Never', 'Only if asked', why='Honesty saves time and trust.'),
        Q('During a visit, the client asks the owner\'s lowest price. You:', 'Say the owner decides and you\'ll take any offer to them', 'Tell them the minimum', 'Make up a number', 'End the visit', why='Keep the owner\'s confidence.'),
        Q('If you have no client yet, how can you practise?', 'Shadow a broker\'s visit with permission', 'Visit properties without permission', 'Skip it', 'Pretend to be a buyer', why='Learn by watching.'),
    ],
    study='read the lesson and the intake form',
    action='do an intake conversation and conduct or shadow a real site visit',
)

OBJ = [
    ('"The price is too high."', 'Show comparables (your Comps sheet) and the price per cent; ask what price they think is fair and why; take a written offer to the owner'),
    ('"I need to think / ask my family."', 'Agree; ask what they need to decide; offer a video or second visit for family members; set a follow-up date'),
    ('"Is the title clear?"', 'Explain what you checked, and that an advocate\'s opinion comes before any large payment'),
    ('"The road is narrow."', 'Acknowledge it; show the price reflects it; check whether widening is planned'),
    ('"Another broker showed it cheaper."', 'Check whether it is the same property and mandate; never undercut dishonestly; co-broke if appropriate'),
    ('"Can we pay part in cash and show a lower price?"', 'Refuse clearly: illegal, risky for both sides, and against your money rules'),
]

L2 = lesson(
    13, 2,
    outcome='You can handle common objections, negotiate fairly between buyer and seller, close a deal and handle a token advance legally and safely.',
    split='20 minutes reading, 55 minutes on role-plays and your token receipt',
    core=f"""
**Objections are questions.** Most objections mean "help me feel safe". Answer with facts, not pressure:
{table(['Objection', 'Honest response'], OBJ)}

**Negotiating as the middle person.** You usually work for the owner (who pays the commission), but you must deal honestly with the buyer too.
- Take **every offer** to the owner, in writing (WhatsApp is fine), with the buyer's conditions.
- Use evidence: comparables, condition, legal issues, time on market.
- Don't reveal either side's limit without permission.
- Look for terms other than price: payment timing, who pays which costs, repairs before handover, including furniture.
- When the gap is small, suggest meeting halfway; when it is large, give both sides time.
For general negotiation and closing skills, see the {xref('ent', 'ent-m07-l03', 'Entrepreneurship lesson on objections, closing and follow-up')}.

**Closing.** When both agree: write the agreed terms in a short message to both (price, token amount, agreement date, registration target, conditions such as the advocate's clearance and loan sanction). Ask for confirmation.

**Token advance (അഡ്വാൻസ്).** A token is a small payment to show serious intent and reserve the property for a short period while documents are checked.
- **Keep it small** (an amount the buyer can afford to lose if things go wrong) and **conditional**: refundable if the advocate finds title problems.
- **Pay by bank transfer or UPI**, never in cash (cash advances of ₹20,000 or more for property are prohibited; RE-M04-L05).
- **Written token receipt** signed by the owner (all co-owners if possible) with: property details, price agreed, token amount, payment reference, period of reservation, the date for the agreement for sale, and conditions for refund.
- The token is **not** ownership; the agreement for sale and then the registered deed follow (RE-M14).
- Pay the token to the **owner's** account, never to the broker's.
""",
    example="""
Asking price ₹38 lakh. The buyer offers ₹34 lakh; the owner says ₹37 lakh. Sachin shows both the comparables (median adjusted ₹2.35 lakh per cent for similar houses ≈ ₹35.3 lakh) and the honest issues (slope, painting). He asks the owner whether he would pay for painting if the buyer met him at ₹36 lakh; the owner agrees to ₹35.5 lakh with no painting. The buyer agrees.

**Token:** ₹50,000 by UPI from the buyer to the owner's bank account, with a written receipt: price ₹35.5 lakh; property reserved for 21 days; agreement for sale to be signed by day 21 after the advocate's clearance; token fully refundable if the advocate finds title problems; otherwise adjusted against the price.
""",
    resources=[
        ('tpa-54', 'Remember: a token and agreement don\'t transfer ownership', '5 minutes'),
        ('krera', 'For project units, check the builder\'s booking terms are as per RERA', '10 minutes'),
    ],
    steps=[
        'Role-play the six objections with a friend or family member, twice each.',
        'Write a token receipt template and have an advocate or document writer check it (or note that you will before using it).',
        'Practise writing an offer message and a closing summary for a sample deal.',
        'If you have a live deal, take a real offer to the owner in writing and record it in the CRM.',
    ],
    proof='Notes from the role-plays, your token receipt template, sample offer and closing messages, and any real offer record.',
    templates=[('Token receipt template', """TOKEN ADVANCE RECEIPT (have an advocate check your template)
Date ______  Place ______
I/We ______ (owner/s) of ______ received ₹ ______ (in words ______) as token advance from
______ (buyer) by bank transfer / UPI, reference ______, on ______,
towards the sale of: survey/resurvey no. ______, ______ village, ______ taluk, area ______ cents,
building ______ sq ft, as per deed no. ______ of ______ SRO.
Agreed price: ₹ ______.
The property is reserved for the buyer until ______ (date).
An agreement for sale will be signed by ______ after the buyer's advocate reviews the documents.
If the advocate finds a defect in title that the owner cannot cure by ______, the token will be
refunded in full within ___ days by bank transfer. If the buyer withdraws for other reasons, ______.
The token will be adjusted against the price.
Owner(s) signature ______  Buyer signature ______  Witnesses 1 ______ 2 ______"""), ('Offer and closing messages', """OFFER MESSAGE (to owner)
"Offer for your property at ______: ₹______ from ______ (buyer). Conditions: advocate's title check, loan sanction from ______ by ______, registration by ______. Token ₹______ by bank transfer once you accept. Please let me know your response in writing."
CLOSING SUMMARY (to both)
"Agreed: price ₹______; token ₹______ by bank transfer to the owner's account by ______; agreement for sale by ______ after advocate's clearance; registration target ______; [other terms]. Please reply 'Confirmed'."
""")],
    mistakes=[
        ('Pushing a buyer to pay a big token on the first visit.', 'Small, conditional tokens after basic checks.'),
        ('Collecting the token in your own account.', 'Pay the owner\'s account directly.'),
        ('Verbal agreements on terms.', 'Write the terms and get confirmation.'),
    ],
    fraud="""
**Token traps.** Some sellers take tokens from several buyers, or take a token and then raise the price. Written, conditional receipts, payment by bank transfer and a fresh EC before the agreement protect the buyer.
""",
    quiz=[
        Q('How should a token advance be paid?', 'By bank transfer or UPI to the owner\'s account with a written receipt', 'In cash to the broker', 'In cash to the owner', 'By a promise', why='Cash limits and safety.'),
        Q('Does a token make the buyer the owner?', 'No; the registered sale deed does', 'Yes', 'Yes, after 21 days', 'Yes, if notarised', why='TPA s.54.'),
        Q('What should you do with every offer?', 'Take it to the owner in writing', 'Ignore low offers', 'Decide yourself', 'Tell the buyer the owner\'s minimum', why='The owner decides.'),
        Q('A buyer asks to show a lower price and pay cash. You:', 'Refuse clearly and explain why', 'Agree', 'Ask the owner to decide', 'Say nothing', why='Illegal and risky.'),
    ],
    study='read the lesson and the objections table',
    action='role-play objections and prepare token receipt, offer and closing templates',
)

LESSONS = [L1, L2]

MODULE = module(
    13,
    overview=f"""
Sales and negotiation: understanding clients, honest shortlists, site visits, objections, fair negotiation, closing and legal, safe token advances.

The practical milestone is a **real site visit**, conducted or shadowed. Selling here means helping people make a good decision with full information, not pushing. Everything is {RULE}.
""",
    outcomes=[
        'Run an intake conversation and shortlist honestly.',
        'Conduct a professional, safe site visit.',
        'Handle objections and negotiate fairly.',
        'Close and handle a token advance legally.',
    ],
    lessons=LESSONS,
    project='a site visit and a negotiation pack',
    project_steps=[
        'Conduct or shadow a real site visit with the checklist.',
        'Prepare token receipt, offer and closing templates.',
        'Complete the objection role-plays.',
        'If you have a live deal, run it through offer and token with the templates.',
    ],
    project_proof='The checklist, templates and role-play notes (and live deal records if any, private).',
    rubric=[
        ('Needs', 'No intake', 'Basic questions', 'Full intake with real reasons understood'),
        ('Visit', 'Unplanned', 'Planned', 'Checklist, honesty, safety and same-day summary'),
        ('Negotiation', 'Pressure or secrets', 'Takes offers', 'Written offers, evidence and fair options'),
        ('Token', 'Cash or no receipt', 'Bank transfer', 'Conditional written receipt to owner\'s account'),
    ],
    short=[
        'Do one intake conversation.',
        'Write a token receipt template.',
    ],
    flashcards=[
        ('First step with a client', 'Intake: needs, budget, timeline, decision makers.'),
        ('Shortlist size', '2 to 4 suitable properties.'),
        ('Owner\'s minimum price', 'Confidential.'),
        ('Every offer', 'To the owner, in writing.'),
        ('Token', 'Small, conditional, by bank transfer, with a receipt.'),
        ('Cash advance limit', 'Under ₹20,000; larger cash advances are prohibited.'),
    ],
    mistakes=[
        ('Talking more than listening.', 'Ask and repeat back.'),
        ('Rushing the close.', 'Let families decide.'),
        ('Skipping written terms.', 'Confirm everything in writing.'),
    ],
    tools=[
        'Client intake form and site-visit checklist (RE-M13-L01).',
        'Token receipt template (RE-M13-L02).',
        'Offer and closing messages (RE-M13-L02).',
    ],
    toolkit=[
        'Client intake form.',
        'Token receipt template.',
        'Offer and closing message templates.',
    ],
)
