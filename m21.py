from common import lesson, module, link, rules, xref, table, fence, Q, RULE, ASOF, CHECK

FRAUDS = [
    ('Fake or forged title', 'Forged deeds or certified copies; fake ECs; "lost original" stories', 'Certified copies and EC from the SRO/PEARL yourself; 30-year chain; advocate'),
    ('Double sale', 'Same land agreed or sold to two buyers', 'Fresh EC before agreement and before registration; registered agreement where advised'),
    ('Forged or cancelled POA', 'Attorney sells an NRI\'s or elderly owner\'s land without real authority', 'Verify the owner directly (video call via advocate); check POA registration and cancellation; pay the owner\'s account'),
    ('Impersonation', 'Someone poses as the owner with fake ID', 'Meet the owner early; compare photos and signatures with earlier deeds; neighbours confirm'),
    ('Heirs left out', 'One heir sells family land without others', 'Legal heir certificate; partition deed; all heirs sign'),
    ('Encroachment', 'Seller includes a neighbour\'s strip or puramboke; or land is occupied by others', 'Surveyor measures; sketch and FMB; neighbours; site visits'),
    ('Wrong land type', 'Nilam or data bank land sold as building land', 'Tax receipt land type; data bank check; advocate'),
    ('Unapproved layouts', 'Plots without approval, no proper road, no RERA', 'Layout approval, K-RERA check, road ownership'),
    ('Undervaluation and black money', 'Deed shows a low price; rest paid in cash', 'Refuse; bank payments only; deed shows the true price'),
    ('Advance and deposit scams', 'Fake landlords or sellers take tokens and vanish', 'Verify ownership first; pay the owner\'s account after written agreement'),
    ('Cyber fraud', 'Fake portals, phishing "EC" links, fake payment screenshots', 'Official .gov.in sites; confirm payments in the bank app, not screenshots'),
]

L1 = lesson(
    21, 1,
    outcome='You can recognise the common real estate frauds in Kerala, name the check that catches each, and know what to do and where to report if you suspect one.',
    split='20 minutes reading, 40 minutes on the fraud checklist and case review',
    core=f"""
Fraud is the biggest risk for small buyers and sellers, and for your reputation. Almost every fraud is caught by **official records checked by you, an advocate's opinion and patience**.

{table(['Fraud', 'How it works', 'The check that catches it'], FRAUDS)}

**Red flags in behaviour:** pressure to pay today; insistence on cash; refusing an advocate's check; only photocopies; owner "abroad" and unreachable; price far below comparables; changes to documents or people at the last minute; payment to someone other than the owner.

**If you suspect fraud:**
1. **Stop** the deal and any payment. Tell your client calmly and in writing.
2. Send the documents to the client's **advocate**.
3. Keep copies of everything (messages, documents, payment records).
4. For cheating or forgery, the victim can file a complaint with the **police**; for online payment fraud, call **1930** quickly and report on the national portal (cybercrime.gov.in) ({link('kp-1930', 'Kerala Police notice')}).
5. For project issues (builders), complain to **K-RERA** ({link('krera', 'K-RERA')}).
Never confront suspected fraudsters alone or try to investigate people yourself beyond checking records; leave that to the police and advocates.
""",
    example="""
A man offers 20 cents near Kuttiady at ₹1.4 lakh per cent (comparables: ₹2 lakh). He says the owner, his uncle in Saudi Arabia, has given him a POA; the original deed is "with the bank"; he wants ₹2 lakh token in cash "today because another buyer is waiting".

Red flags: price 30% below comparables, cash, urgency, absent owner, no original deed. Sachin tells his buyer to pay nothing. The buyer's advocate checks: the POA was registered in 2015, but the EC shows a **cancellation of the POA registered in 2022**. The uncle, reached by video call through the advocate, confirms he had cancelled it and is not selling. The buyer is saved ₹2 lakh, and the uncle is warned that someone is trying to sell his land.
""",
    pro="""
- **Advocate:** any suspected fraud, before any further step.
- **Police:** cheating, forgery, impersonation.
- **Licensed surveyor:** encroachment and boundary questions.
""",
    resources=[
        ('kp-1930', 'Read about the 1930 helpline and the national portal', '5 minutes'),
        ('hc-ec', 'EC steps (your main fraud check)', '5 minutes'),
        ('tg-gpa', 'Why POA sales don\'t transfer title', '5 minutes'),
    ],
    steps=[
        'Ask two brokers and your document writer or advocate about real fraud cases they have seen in your area (no names), and how each was or could have been caught.',
        'Match each case to a row in the fraud table.',
        'Build your fraud red-flag checklist and add it to your due-diligence file.',
        'Save the 1930 helpline and the police station number in your phone and on your toolkit.',
    ],
    proof='Notes on at least three local fraud cases (anonymised), your red-flag checklist and saved contacts.',
    templates=[('Fraud red-flag checklist', """FRAUD RED-FLAG CHECKLIST (any YES -> stop and call the advocate)
[ ] Price far below comparables (>20%)        [ ] Pressure to pay today
[ ] Cash demanded or "part in cash"           [ ] Only photocopies; original "lost" or "with someone"
[ ] Owner absent and unreachable; POA seller  [ ] Payment to someone other than the owner
[ ] Names/areas/survey numbers don't match     [ ] Heirs or co-owners missing
[ ] Land type nilam / data bank / puramboke    [ ] No layout approval or RERA number (projects)
[ ] Documents or people change at the last minute  [ ] Seller refuses advocate's check or fresh EC
IF FRAUD SUSPECTED: stop payments -> tell client in writing -> advocate -> keep records -> police / 1930 (online payment fraud) / K-RERA (projects)""")],
    mistakes=[
        ('Ignoring red flags because the deal looks good.', 'Below-market prices are the most common bait.'),
        ('Investigating suspects yourself.', 'Check records; leave investigation to police and advocates.'),
        ('Delaying reports of payment fraud.', 'Call 1930 quickly.'),
    ],
    fraud="""
**Fraud against the broker.** Fraudsters also use brokers to look legitimate. Protect yourself: verify every owner before listing, never collect money for owners, and keep written records of what you checked and told clients.
""",
    quiz=[
        Q('What catches most double sales?', 'A fresh EC before the agreement and before registration', 'A nice brochure', 'A cash token', 'Trusting the seller', why='It shows registered transactions.'),
        Q('A seller with a POA wants a cash token today. You:', 'Advise the client to pay nothing until the advocate verifies the owner and POA', 'Pay quickly', 'Pay half', 'Ignore the POA', why='Several red flags.'),
        Q('Where do you report online payment fraud quickly?', 'Helpline 1930 and the national cybercrime portal', 'A WhatsApp group', 'The seller', 'Nowhere', why='Speed helps recovery.'),
        Q('How do you avoid buying nilam sold as building land?', 'Check the land type in revenue records and the data bank', 'Look at the soil', 'Ask the seller', 'Trust the broker', why='Records, not appearances.'),
    ],
    study='read the lesson and the fraud table',
    action='collect three anonymised local fraud cases and build your red-flag checklist',
)

ETHICS = [
    ('Consent', 'Market only with the owner\'s written mandate; share details only with consent'),
    ('Truth', 'Never misrepresent a property, its papers, its risks or your own role'),
    ('Money', 'No cash beyond legal limits, no undervaluation, no black money, no benami'),
    ('Loyalty and fairness', 'Act for your client; deal honestly with the other side; disclose if you are paid by both'),
    ('Conflicts', 'Disclose any personal interest (your family\'s property, your own purchase, referral fees)'),
    ('Limits', 'Never do work that needs a licence you don\'t have (drafting, title opinions, surveying, tax advice, valuation certificates)'),
    ('Privacy', 'Protect documents and personal data; delete what you no longer need'),
    ('Compliance', 'Follow K-RERA rules, register when required, keep records'),
]

L2 = lesson(
    21, 2,
    outcome='You can apply a clear code of ethics, handle conflicts of interest and protect clients, and explain why honest dealing is also good business.',
    split='15 minutes reading, 45 minutes on your code and case responses',
    core=f"""
**Your code of ethics:**
{table(['Principle', 'In practice'], ETHICS)}

**Conflicts of interest.** A conflict exists when your interest could pull against your client's.
- **Buying for yourself** a property you were asked to sell: tell the owner in writing, suggest they get an independent opinion on price, or step back.
- **Selling your family's property** to your client: disclose it.
- **Taking commission from both sides:** disclose it to both in writing (RE-M10-L02).
- **Referral fees** from advocates, banks or contractors: disclose them, or better, don't take them (RE-M20-L02).
- **Pushing a property because the commission is higher:** don't; show what fits the client.

**Protecting clients:**
- Encourage every buyer to use their own advocate and, where needed, a surveyor.
- Keep tokens small and conditional; payments to the owner's account by bank transfer.
- Put important information in writing (WhatsApp or email): issues found, advice to get an advocate, offers.
- Tell clients the honest risks: illiquidity, legal disputes, market downturns and low yields (Module 18).
- Know when to walk away and say so.

**Why ethics is good business.** In a small market like Kuttiady, reputation travels fast. One dishonest deal can end a career; ten honest deals bring a stream of referrals. NRI clients, in particular, choose agents they can trust from thousands of kilometres away.

**Honest risk talk (a script):** "Property can be a good home and sometimes a good investment, but it's hard to sell quickly, legal problems can take years to solve, prices don't always rise, and after costs many small purchases earn less than a fixed deposit. Let's check the numbers and get an advocate's opinion before you decide."
""",
    example="""
**Three situations and Sachin's responses:**
1. An owner asks him to advertise a plot as "10 cents" when the deed says 8.6: he refuses and lists 8.6 cents, explaining that misrepresentation will kill the deal at the advocate stage anyway.
2. A buyer from Dubai asks him to "manage everything, including signing for me": he explains he can coordinate, but legal acts need a registered POA in favour of someone the buyer trusts, and the buyer's own advocate.
3. He finds a plot he wants to buy himself, listed with him by an elderly owner: he tells the owner in writing, recommends she get a second broker's or valuer's view on price, and offers the comparables price, not a lower one. She agrees, and both sides use their own advocates.
""",
    pro="""
- **Advocate:** for any conflict you are unsure about, and for clients who need legal acts done.
""",
    resources=[
        ('krera', 'Look for any code of conduct or obligations for agents on the K-RERA site', '10 minutes'),
        ('wp-rera', 'Re-read the agents\' obligations under RERA', '10 minutes'),
    ],
    steps=[
        'Write your own code of ethics (8 principles, one line each) and your honest risk script.',
        'Write how you would respond to five difficult situations (the three above plus two from your interviews).',
        'Add your code to your website or GBP description, visiting card and mandate (short version).',
        'Ask one mentor, broker or advocate to read your code and suggest one improvement.',
    ],
    proof='Your code, risk script, five written responses and the feedback.',
    templates=[('Code of ethics and conflict disclosure', """MY CODE OF ETHICS (short version for cards and profiles)
I act only with owners' written consent. I never misrepresent a property. All payments go by bank transfer
to the right person; no cash deals, no undervaluation. I disclose any personal interest or fee.
I don't do work that needs a licence I don't hold; I bring in advocates, surveyors and CAs.
I protect your documents and privacy.
CONFLICT DISCLOSURE (to client, in writing)
"I want to tell you that ______ (my relative owns this property / I am also paid by the other side / I would like to buy this myself / I receive a referral fee from ______). You may want an independent opinion. Please confirm you are happy for me to continue." Date ______ Client's reply ______""")],
    mistakes=[
        ('Hiding a personal interest.', 'Disclose in writing.'),
        ('Doing licensed work to save the client money.', 'Refer to professionals.'),
        ('Avoiding uncomfortable truths.', 'Use your honest risk script.'),
    ],
    fraud="""
**"Everyone does it."** Undervaluation, cash and hidden commissions are common, which makes them feel normal. They are still illegal or dishonest, and they expose you to penalties and lost trust. Your clean record is your competitive advantage.
""",
    quiz=[
        Q('You want to buy a property an owner asked you to sell. What do you do?', 'Disclose in writing and suggest an independent price opinion', 'Buy it secretly at a low price', 'Tell nobody', 'Raise your commission', why='Conflict of interest.'),
        Q('A client asks you to sign documents for them. You:', 'Explain that legal acts need a registered POA and their own advocate', 'Sign anyway', 'Forge their signature', 'Ask a friend to sign', why='Know your limits.'),
        Q('Why is ethics good business in a small market?', 'Reputation travels fast and referrals depend on trust', 'It isn\'t', 'Only for NRIs', 'Because of taxes', why='Trust is the product.'),
        Q('Which work needs a licence you don\'t have?', 'Drafting deeds, title opinions, surveying, tax advice and valuation certificates', 'Taking photos', 'Writing listings', 'Running site visits', why='Refer to professionals.'),
    ],
    study='read the lesson and the ethics table',
    action='write your code of ethics, risk script and responses to five difficult situations',
)

LESSONS = [L1, L2]

MODULE = module(
    21,
    overview=f"""
Fraud, risk and ethics: the common real estate frauds in Kerala and the checks that catch them, what to do and where to report, a personal code of ethics, conflicts of interest and protecting clients.

Read this module early if you can, and keep the red-flag checklist with every deal. Everything is {RULE}.
""",
    outcomes=[
        'Recognise common frauds and the check for each.',
        'Know what to do and where to report.',
        'Apply a code of ethics and handle conflicts.',
        'Explain risks honestly to clients.',
    ],
    lessons=LESSONS,
    project='a fraud and ethics pack',
    project_steps=[
        'Red-flag checklist and three anonymised local cases.',
        'Code of ethics, risk script and conflict disclosure template.',
        'Five written responses to difficult situations.',
        'Code shown on your card, GBP and mandate.',
    ],
    project_proof='The pack and screenshots.',
    rubric=[
        ('Fraud awareness', 'Generic', 'Knows the types', 'Matches local cases to checks'),
        ('Response', 'Unclear', 'Knows to stop', 'Clear steps and reporting routes'),
        ('Ethics', 'None written', 'Some rules', 'Written code used in cards, mandates and practice'),
        ('Conflicts', 'Ignored', 'Recognised', 'Disclosure template and examples'),
    ],
    short=[
        'Memorise the red flags.',
        'Write your code of ethics.',
    ],
    flashcards=[
        ('Main fraud check', 'Your own EC and certified copies, plus an advocate.'),
        ('POA fraud check', 'Verify owner directly; check cancellation; pay the owner.'),
        ('Price 30% below market', 'Red flag.'),
        ('Online payment fraud', 'Call 1930; report on the national portal.'),
        ('Conflict of interest', 'Disclose in writing.'),
        ('Licensed work', 'Drafting, title opinions, surveying, tax advice, valuation certificates.'),
    ],
    mistakes=[
        ('Thinking "it won\'t happen to my client".', 'Use the checklist every time.'),
        ('Silence about problems.', 'Write them down for the client.'),
        ('Compromising once.', 'One bad deal can end your reputation.'),
    ],
    tools=[
        'Fraud red-flag checklist (RE-M21-L01).',
        'Code of ethics and conflict disclosure (RE-M21-L02).',
    ],
    toolkit=[
        'Fraud red-flag checklist.',
        'Code of ethics and conflict disclosure template.',
    ],
)
