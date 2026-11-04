from common import lesson, module, link, rules, xref, table, fence, Q, RULE, ASOF, CHECK
import tools

L1 = lesson(
    10, 1,
    outcome='You can explain when you need K-RERA agent registration, how to apply, what it costs and the rules a registered agent must follow.',
    split='20 minutes reading, 30 minutes on the K-RERA site and your registration plan',
    core=f"""
**Do you need to register?** Under the RERA Act, anyone who acts as an agent for the sale of plots, apartments or buildings in a **RERA-registered project** must register with the state authority before doing so (RE-M04-L02). Resale of individual properties between owners and rentals are generally outside RERA, but registering early:
- lets you work with builders and project sales;
- shows clients you are accountable;
- puts your registration number on your cards, listings and agreements.

**How to apply in Kerala** (from K-RERA and secondary guides; {CHECK} on the {link('krera', 'K-RERA site')} before applying):
- Application in **Form G** under the Kerala RERA rules ({link('tg-krera', 'TaxGuru')}).
- Reported documents: PAN, address proof, two passport photos, business address proof, registration certificate (for a firm or company) and **income tax returns for the previous three years** ({link('sy-krera', 'Square Yards, November 2024')}). If you haven't filed returns, ask K-RERA what they accept and start filing now.
- Fee: **₹25,000** for an individual; ₹2 lakh to ₹2.5 lakh for others (sources differ) ({link('tg-krera', 'TaxGuru')}; {link('om-rera', 'Onmanorama')}).
- The procedure was reported as offline (by post) in late 2024; check whether an online option exists now.
- Registration is valid for a fixed period and must be renewed (renewal Form J); check the current period and fee.

**Rules registered agents must follow** (RERA Act, as summarised by {link('wp-rera', 'Wikipedia')}):
- Don\'t facilitate sales in unregistered projects that must be registered.
- Quote your registration number in every advert and deal.
- Keep books of account, records and documents.
- Don\'t make false statements about a project or property, and don\'t use unfair trade practices.
- Help buyers get the information and documents they are entitled to.
- Penalties for agents who don\'t register: reported **₹10,000 a day** ({link('om-rera', 'Onmanorama')}).

**When to register:** the ₹25,000 fee is significant on a small budget. A sensible path: start with rentals, resale and NRI property care (no RERA registration needed), file your tax returns, then register before you handle any project sales.
""",
    example="""
Sachin's plan:
- Months 1 to 6: rentals and resale only; no project sales. File his income tax return for the year, even if income is low.
- Month 6: a builder in Kuttiady offers him 1.5% commission to sell flats in a 24-flat registered project. He tells the builder he will apply for K-RERA registration first and will not advertise the project until he has his number.
- He prepares Form G, documents and the ₹25,000 fee (from his first commissions), and adds a line to his cards: "K-RERA agent registration no. ______".
""",
    rules_rows=[
        ('Agent registration form', 'Form G under the Kerala RERA rules', 'TaxGuru; Square Yards'),
        ('Agent fee', 'Individual ₹25,000; others ₹2 lakh to ₹2.5 lakh (sources differ)', 'TaxGuru; Onmanorama'),
        ('Documents (reported)', 'PAN, address proof, photos, business address, ITRs for 3 years', 'Square Yards, November 2024'),
        ('Penalty for not registering', 'Reported ₹10,000 per day', 'Onmanorama'),
    ],
    pro="""
- **Advocate or CA:** if you form a firm or company for the agency, or need help with the application.
""",
    resources=[
        ('krera', 'Find the agent registration page, forms and the list of registered agents', '20 minutes'),
        ('sy-krera', 'Read the documents list and steps', '10 minutes'),
        ('tg-krera', 'Read the fee table', '5 minutes'),
    ],
    steps=[
        'On the K-RERA site, find the current agent registration process and forms, and note the date you checked.',
        'List the documents you have and those you still need (ITRs, address proof).',
        'Count the registered agents in Kozhikode district and look at two of their public profiles.',
        'Write your registration plan: when you will register, how you will pay the fee and what you will do before then.',
    ],
    proof='Notes on the current process with the date, your documents list and your registration plan.',
    templates=[('K-RERA agent registration plan', """K-RERA AGENT REGISTRATION PLAN      checked on ______ at rera.kerala.gov.in
Process: offline / online ______   Form: G   Renewal form: J
Fee (individual): ₹ ______ (reported ₹25,000)   Validity: ______ years
Documents:  PAN [ ]  address proof [ ]  2 photos [ ]  business address proof [ ]
            ITR year 1 [ ] year 2 [ ] year 3 [ ]  (firm: registration certificate [ ])
Before registering I will only do: rentals / resale / NRI care / marketing services
I will register by: ______ (before any project sale)
After registering: number on cards, listings, mandates, website [ ]""")],
    mistakes=[
        ('Selling project units before registering.', 'Register first; penalties are heavy.'),
        ('Not filing income tax returns.', 'Returns are needed for registration and loans.'),
        ('Assuming registration means you can draft documents.', 'It doesn\'t; drafting is for document writers and advocates.'),
    ],
    fraud="""
**Fake RERA agents.** Some people print made-up K-RERA numbers on cards. Clients can search the agent list; make sure your own number is real and visible, and check other agents' numbers before working with them.
""",
    quiz=[
        Q('When must an agent register with K-RERA?', 'Before facilitating sales in RERA-registered projects', 'Only after 10 deals', 'Never', 'Only for rentals', why='Resale and rentals are generally outside RERA.'),
        Q('What is the reported K-RERA fee for an individual agent?', '₹25,000', '₹500', '₹2,50,000', 'Free', why='Firms pay more.'),
        Q('Which document is reported as required that many beginners lack?', 'Income tax returns for the previous three years', 'A passport', 'A degree certificate', 'A car licence', why='Start filing returns now.'),
        Q('What must a registered agent show in adverts?', 'Their K-RERA registration number', 'Their bank balance', 'Their home address', 'Nothing', why='It\'s required.'),
    ],
    study='read the lesson and the K-RERA agent pages',
    action='check the current K-RERA process and write your registration plan',
)

COMM = [
    ('Land or house sale', 'Commonly 1% to 2% of the price from the seller, sometimes also from the buyer', 'Must be agreed in writing; disclose if you take from both'),
    ('House or shop rental', 'Commonly one month\'s rent (or half from each side)', 'Agree who pays before showing'),
    ('Project flats (builder)', 'Percentage paid by the builder (needs K-RERA registration)', 'Builder agreement; TDS may be deducted'),
    ('NRI property care', 'Monthly fee per property', 'Written service agreement (RE-M15-L02)'),
]

L2 = lesson(
    10, 2,
    outcome='You can get a written owner mandate, agree commission clearly and build an inventory of properties with complete, verified information.',
    split='20 minutes reading, 55 minutes on mandates and inventory',
    core=f"""
**Why a written mandate.** A mandate (authorisation) from the owner proves you have permission to market the property, sets the commission and avoids disputes ("I never asked you to sell"). Without one, you risk misrepresenting a property you don't control, working for nothing or falling out with the owner. The rule is simple: **act only with the owner's consent, in writing.**

**What a mandate covers** (toolkit template below; have an advocate review your version):
- Property details as in the deed.
- Sale or rent; exclusive or not; period (for example 90 days).
- Asking price and who decides the final price (the owner).
- Commission: amount, when it is due (on registration or on signing the rental agreement) and payment by bank transfer.
- Owner's confirmation that they have the right to sell and that the information is true.
- Your duties: honest marketing, sharing all offers in writing, privacy, no money collected without written approval.
- Where photos and videos may be published.

**Commission norms in Kerala** (practice varies; confirm in your broker interviews):
{table(['Deal', 'Common practice', 'How to handle'], COMM)}
Write the commission in the mandate and in a short note to the buyer or tenant if they also pay. Never hide commission from either side.

**Building an inventory.** Your inventory is your stock of properties you are allowed to market. For each property: owner's mandate, verified documents summary, photos, price, key facts and status. Keep it in an "Inventory" tab (columns similar to the Comps sheet, plus mandate date, expiry and status). Quality beats quantity: 10 properties with verified papers and mandates are worth more than 50 rumours.
""",
    example="""
An owner in Thottilpalam wants to sell 15 cents with a house. Sachin meets him, reads the deed and tax receipt, and explains his service. They agree:
- Non-exclusive mandate for 90 days; asking ₹38 lakh; the owner decides the final price.
- Commission 2% of the final price on registration, by bank transfer.
- Photos and video can go on NoBroker, Facebook and Sachin's WhatsApp channel; no house number or owner\'s phone number in public.
- The owner signs; Sachin keeps a copy and adds the property to his Inventory tab with the mandate expiry date.
If a buyer is found at ₹36 lakh, commission is 36,00,000 × 0.02 = **₹72,000**, invoiced after registration.
""",
    pro="""
- **Advocate:** reviews your standard mandate template once, and any unusual terms.
""",
    resources=[
        ('krera', 'Check whether K-RERA publishes any agent code of conduct or forms you should follow', '10 minutes'),
        ('nobroker', 'See how owner listings describe properties (for inventory fields)', '10 minutes'),
    ],
    steps=[
        'Adapt the mandate template with your details and have it reviewed by an advocate (or note that you will before first use).',
        'Ask your interviewed brokers what commission they charge for sales and rentals, and note the range.',
        'Approach 2 to 3 owners you know (family, neighbours) who want to sell or let; with consent, sign a mandate with at least one.',
        'Set up the Inventory tab and add each mandated property with full details.',
    ],
    proof='Your mandate template, commission notes from brokers, at least one signed mandate (private) and the Inventory tab.',
    templates=[('Owner mandate template', tools.MANDATE), ('Inventory tab', """INVENTORY (tab "Inventory")
ID | Owner (private) | Mandate date | Mandate expiry | Exclusive? | Type | Locality | Cents | Sq ft | Asking ₹ | Docs checked (Y/partial/N) | Photos (Y/N) | Listed where | Status (active/under offer/sold/let/withdrawn) | Notes
Expiry alert: =IF(D2-TODAY()<=14,"RENEW OR CLOSE","")
Rule: no listing goes public without a signed mandate and owner-approved text and photos.""")],
    mistakes=[
        ('Marketing on a verbal "OK".', 'Get it in writing, even a signed short mandate.'),
        ('Unclear commission.', 'Write the amount, timing and payment mode.'),
        ('Collecting big inventories of unverified properties.', 'Fewer, verified, mandated properties.'),
    ],
    fraud="""
**Listing without consent.** Some brokers copy listings from portals or WhatsApp groups and advertise them as their own. It misleads buyers, angers owners and breaks trust. Only market properties you hold a mandate for, or co-broke openly with the broker who does.
""",
    quiz=[
        Q('Why get a written owner mandate?', 'It proves consent, sets commission and prevents disputes', 'It transfers ownership', 'It replaces the sale deed', 'It is only for NRIs', why='Act only with written consent.'),
        Q('Who decides the final sale price?', 'The owner', 'The broker', 'The buyer alone', 'The neighbour', why='The broker advises; the owner decides.'),
        Q('What is commonly charged for a house rental in Kerala?', 'About one month\'s rent', '10% of property value', 'Nothing', 'One year\'s rent', why='Practice varies; confirm locally.'),
        Q('If you take commission from both buyer and seller, what must you do?', 'Disclose it to both in writing', 'Hide it', 'Charge double secretly', 'Nothing', why='Transparency avoids conflicts.'),
    ],
    study='read the lesson and the mandate template',
    action='adapt the mandate, sign at least one with an owner and set up your inventory',
)

LESSONS = [L1, L2]

MODULE = module(
    10,
    overview=f"""
Becoming a registered agent: when and how to register with K-RERA, the rules agents must follow, written owner mandates, commission norms and building a verified inventory.

Part C is about running a legal real estate service business. It starts with doing things properly: registration when needed, written consent from owners and clear commission. Everything is {RULE}.
""",
    outcomes=[
        'Explain when K-RERA registration is needed and how to apply.',
        'Follow the rules for registered agents.',
        'Use a written owner mandate with clear commission.',
        'Build a verified inventory.',
    ],
    lessons=LESSONS,
    project='your agent starter pack',
    project_steps=[
        'Registration plan with current K-RERA process notes.',
        'Advocate-reviewed (or ready to review) mandate template.',
        'At least one signed mandate and the Inventory tab.',
        'A one-paragraph "how I work" statement (consent, honesty, no cash, privacy) for owners and clients.',
    ],
    project_proof='The four items (owner details private).',
    rubric=[
        ('Registration', 'Not considered', 'Knows the rules', 'Dated plan with documents and timing'),
        ('Mandates', 'Verbal only', 'Template ready', 'Signed mandate in use'),
        ('Commission', 'Unclear', 'Range known', 'Written, disclosed and paid by bank transfer'),
        ('Inventory', 'None', 'Unverified list', 'Verified, mandated properties with expiry alerts'),
    ],
    short=[
        'Read the K-RERA agent rules.',
        'Sign one mandate.',
    ],
    flashcards=[
        ('K-RERA agent form', 'Form G.'),
        ('Agent fee (individual)', '₹25,000 (reported).'),
        ('Registration needed for', 'Sales in RERA-registered projects.'),
        ('Mandate', 'Owner\'s written authorisation to market.'),
        ('Who sets the final price?', 'The owner.'),
        ('Sale commission (common)', '1% to 2%; agree in writing.'),
        ('Rental commission (common)', 'About one month\'s rent.'),
    ],
    mistakes=[
        ('Skipping paperwork to move fast.', 'Paperwork protects you.'),
        ('Promising owners unrealistic prices to win mandates.', 'Use your comparables.'),
        ('Ignoring mandate expiry.', 'Renew or close.'),
    ],
    tools=[
        'K-RERA registration plan (RE-M10-L01).',
        'Owner mandate template (RE-M10-L02).',
        'Inventory tab (RE-M10-L02).',
    ],
    toolkit=[
        'Owner mandate template.',
        'Inventory tab with expiry alerts.',
        'Registration plan.',
    ],
)
