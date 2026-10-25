from common import lesson, module, link, ASOF

L1 = lesson(
    15, 1,
    title='Service packages and pricing',
    weeks=(37, 37), hours=2.5,
    outcome='Turn your skills into clear packages with fixed scope and price, work out a fair price from your time, costs and the value to the client, and make a one-page price sheet.',
    split='40 minutes study, 1 hour 50 minutes action',
    core="""
### Sell packages, not hours

Shop owners don't want to buy "10 hours of social media". They want to know **what they get, what it costs and what it will do for them.** A **package** has a fixed scope, a fixed price and a clear result to aim for. Packages are easier to sell, easier to deliver and easier to repeat.

A simple structure for local clients:

| Type | What it is | Example |
| --- | --- | --- |
| **One-time setup** | Fix the foundations once | Google Business Profile, WhatsApp Business with catalogue and quick replies, Instagram profile optimised, 3 templates, a 1-hour training |
| **Monthly retainer** | Ongoing work for a monthly fee | 8–12 posts including Reels, Status ideas, replies support, Google updates, a monthly report |
| **Add-ons** | Extras priced separately | Managing ads (ad spend paid by the client), a photo or video shoot visit, extra Reels, influencer coordination |

Offer **two or three tiers** (Starter, Growth, Pro) so clients can choose; most choose the middle one.

### Three ways to set a price

1. **Cost-based:** your hours × your hourly target + any costs (travel, data, tools). Work out your hourly target first: the monthly income you need ÷ the hours you can really bill (not all your working hours; some go to admin and learning).
2. **Value-based:** what the result is worth to the client. If a retainer brings a gym 4 extra members a month at ₹1,500 each, the result is worth ₹6,000 a month or more over time.
3. **Market check:** what similar services cost in your area. Ask businesses what they've paid before, look at real local job and freelance listings, and ask other freelancers. Don't trust anyone's "standard rate" without checking.

Set your price between your cost floor and the value to the client, and check it against the market. OpenStax's chapter on pricing explains the role and psychology of pricing; the Entrepreneurship course covers pricing in detail in ENT-M05-L03.

### Rules that protect you

- **Ad spend is separate** from your fee, and paid by the client directly to the platform.
- **Say what's not included** (shoots, printing, ad spend, extra revisions).
- **Payment in advance** for monthly work, and 50% upfront for setups.
- **A minimum term** for retainers (often three months), because results take time.
- **Taxes:** prices may be "plus GST if applicable" once you are registered; ENT-M08-L03 explains GST basics (check current rules).
- **Review prices every three months** as your results and skills grow.

### Don't underprice

Very low prices attract clients who don't value the work, and leave you no time to do it well. Start with a fair introductory price for your first one or two clients, linked to your pilot results, and raise it as your case studies grow.
""",
    example="""
Arun's ShopAssist (from the Entrepreneurship course) built three packages for shops around Vatakara (made-up prices to show the method; check your own local rates):

| | **Setup** (one-time) | **Starter** (monthly) | **Growth** (monthly) |
| --- | --- | --- | --- |
| What's included | Google profile, WhatsApp Business with catalogue and quick replies, Instagram profile, 3 Canva templates, 1-hour training | 8 posts (4 Reels), daily Status ideas, Google updates weekly, monthly report | 12 posts (6 Reels), Status, Google updates, replies support 6 days a week, ads management, monthly meeting |
| Price | ₹4,000 | ₹6,000 a month | ₹12,000 a month (ad spend extra) |
| Terms | 50% upfront | 3-month minimum, paid in advance | 3-month minimum, paid in advance |

How he checked the Starter price: about 14 hours a month at his target of ₹400 an hour is ₹5,600, plus ₹400 for travel and data. He also asked four shop owners what they had paid before for similar help.
""",
    resources=[
        ('os-12-1', 'Read the role and psychology of pricing', '30 min'),
        ('li-pages', 'Optional: note how LinkedIn presents services, for your profile later', '5 min'),
    ],
    steps=[
        'Study the resource (about 30 minutes).',
        'Work out your hourly target: the monthly income you need ÷ your realistic billable hours.',
        'Time your pilot work: how many hours a month did each task take? Use it to cost your packages.',
        'Design a one-time setup package, two monthly tiers and two add-ons, with exactly what is and isn\'t included.',
        'Check your prices three ways (cost, value, market) and make a one-page price sheet in Canva.',
    ],
    proof='Your hourly target calculation, your package designs with the three price checks, and your one-page price sheet.',
    templates=[
        ('package designer', """
PACKAGE: ________ (setup / monthly / add-on)
FOR: ________ (kind of business)
INCLUDED: 1. ____ 2. ____ 3. ____ 4. ____
NOT INCLUDED: shoots / printing / ad spend / ________
HOURS A MONTH (from pilot timing): ____
COST CHECK: hours ____ x Rs ____ + costs Rs ____ = Rs ____
VALUE CHECK: result ____ worth about Rs ____ to the client
MARKET CHECK: similar offers seen: Rs ____ to Rs ____
PRICE: Rs ____ (+ GST if applicable)
TERMS: advance ____; minimum ____ months; revisions ____
""", ''),
        ('price sheet (one page)', """
[YOUR NAME] - SOCIAL MEDIA FOR LOCAL BUSINESSES
I help [kind of business] in [area] get [result].
Proof: [one line from a case study]

SETUP (one-time)          Rs ____   [what's included]
STARTER (monthly)         Rs ____   [what's included]
GROWTH (monthly)          Rs ____   [what's included]
ADD-ONS: ads management Rs ____ / shoot visit Rs ____ /
         extra Reel Rs ____
Ad spend is paid by you directly to the platform.
Monthly packages: 3-month minimum, paid in advance.
Prices + GST if applicable. Valid until ____.
WhatsApp: ____  Portfolio: ____
""", ''),
    ],
    mistakes=[
        ('Charging by the post.', 'It turns you into a post factory. Price the outcome and the service.'),
        ('Hiding ad spend inside your fee.', 'Keep it separate and paid directly by the client.'),
        ('No "not included" list.', 'Scope creep eats your time. Write down what\'s extra.'),
        ('Pricing too low to look attractive.', 'It attracts the wrong clients and burns you out.'),
    ],
    quiz=[
        {'q': 'Why sell packages instead of hours?',
         'o': ['Hours are illegal', 'Clients understand what they get and what it costs, and you can repeat the work', 'Packages need no work', 'Platforms require it'],
         'a': 'B', 'why': 'Clear scope and price make selling and delivering easier.'},
        {'q': 'How do you work out your hourly target?',
         'o': ['Copy a friend\'s rate', 'Monthly income needed ÷ realistic billable hours', 'Followers × 10', 'A random number'],
         'a': 'B', 'why': 'Not all working hours are billable; plan for that.'},
        {'q': 'Who should pay the ad spend in a package?',
         'o': ['You, hidden in your fee', 'The client, directly to the platform, separate from your fee', 'Nobody', 'The platform'],
         'a': 'B', 'why': 'It keeps money clear and protects you.'},
        {'q': 'Which three checks set a fair price?',
         'o': ['Colour, font and logo', 'Cost, value to the client and the local market', 'Followers, likes and shares', 'Guess, hope and luck'],
         'a': 'B', 'why': 'Price between your cost floor and the client\'s value, checked against the market.'},
    ],
    study='OpenStax 12.1 on pricing (about 30 minutes)',
    action='design setup, monthly and add-on packages, check the prices three ways and make a price sheet',
)

L2 = lesson(
    15, 2,
    title='Finding local clients and writing proposals',
    weeks=(38, 38), hours=2.5,
    outcome='Find local clients through warm contacts, referrals and honest outreach, run a discovery conversation, and write a short proposal that wins work without promising what you can\'t deliver.',
    split='35 minutes study, 1 hour 55 minutes action',
    core="""
### Where local clients come from

In order of how well they usually work:

1. **People who know you:** the pilot client, the businesses you audited, family and friends' businesses.
2. **Referrals:** ask every happy client, "Who else should I talk to?"
3. **Your practice page:** shops you featured have already seen your work.
4. **Local networks:** traders' associations, Kudumbashree units, college and alumni groups, business events.
5. **LinkedIn:** for bigger businesses, institutions and agencies.
6. **Walk-in visits with a free check:** "I help shops get found on Google and Instagram. Can I show you two quick fixes for your profile?"
7. **Researched outreach:** businesses with weak profiles you found on Google Maps or Instagram, contacted personally.

**Be careful with cold WhatsApp messages** to strangers: they often get blocked or reported, and WhatsApp has been testing limits on messages that get no reply. A personal visit, a phone call or a message after an introduction works better.

### Keep a pipeline

Use the **Leads and Clients** tab: every business moves through **Lead → Contacted → Meeting → Proposal sent → Won / Lost**, with a next step and a date. Follow up politely twice; most deals happen after the second or third conversation. The Entrepreneurship course covers sales conversations and objections in Module 7, and HubSpot's free Inbound Sales course is a good next step.

### The discovery conversation

Before you propose anything, listen. Ask:

- "What would you like more of: calls, WhatsApp orders, visits, bookings?"
- "Who are your best customers, and how do they find you now?"
- "What have you tried online? What worked, what didn't?"
- "Who decides, and what budget do you have in mind for marketing each month?"
- "What would make the next three months a success for you?"

Take notes in their words; they go straight into your proposal.

### A proposal that wins

Keep it to **one or two pages**, in plain language (and Malayalam if the owner prefers):

1. **Your goal** (in their words)
2. **What I found** (3 points from a mini-audit, with screenshots)
3. **The plan** for the first three months
4. **The package and price**, with what's included and not included
5. **What I need from you** (photos, approvals, access as manager)
6. **How we'll measure** (enquiries, calls, orders) and report
7. **Terms** (advance payment, minimum term) and **the next step** ("Reply YES and we'll start on Monday")

**Never guarantee sales or follower numbers.** Promise the work, the measurement and honest reporting. Your case studies show what's possible.
""",
    example="""
After his pilot results spread by word of mouth, Arun met the owner of **Peak Fitness**. In the discovery talk she said: "We need more women joining the morning batch; most come from referrals now."

His one-page proposal (made-up example):

- **Your goal:** 10 new women members in the morning batch over 3 months.
- **What I found:** no women trainers shown on Instagram; the Google profile has no hours; the WhatsApp number in the bio is wrong.
- **Plan:** fix the profiles in week 1; two Reels a week featuring the women's batch (with members' consent); a "bring a friend" offer; a small Click-to-WhatsApp ad test in month 2.
- **Package:** Growth, ₹12,000 a month, 3 months, ad spend separate (suggested ₹2,000 a month).
- **Measure:** WhatsApp enquiries labelled "women's batch", trial sessions, joins; monthly report.
- **Next step:** "Reply YES and I'll send the agreement today."

She replied YES the next day.
""",
    resources=[
        ('os-15-1', 'Read about personal selling and relationship selling', '25 min'),
        ('hubspot-sales', 'Optional: note the free Inbound Sales Certification for later', '5 min'),
        ('tc-wa-unreplied', 'Re-read why cold WhatsApp messages are risky', '5 min'),
    ],
    steps=[
        'Study the resources (about 35 minutes).',
        'List 30 possible clients in your Leads and Clients tab, from the seven sources above, with one line on why each might need help.',
        'Contact at least 10 of them personally (visit, call, or a message after an introduction), offering a free 15-minute check.',
        'Hold at least 2 discovery conversations using the questions, and take notes in their words.',
        'Write one proposal from a real conversation, using the template.',
    ],
    proof='Your Leads and Clients tab with 30 leads and 10 contacted, your discovery notes from 2 conversations and one proposal.',
    templates=[
        ('discovery questions (English and Malayalam)', """
1. What would you like more of: calls, orders, visits?
   കൂടുതൽ വേണ്ടത് എന്താണ്: കോളുകൾ, ഓർഡറുകൾ, സന്ദർശകർ?
2. Who are your best customers, and how do they find you?
   നിങ്ങളുടെ മികച്ച ഉപഭോക്താക്കൾ ആരാണ്, അവർ നിങ്ങളെ എങ്ങനെ അറിയുന്നു?
3. What have you tried online? What worked?
   ഓൺലൈനിൽ എന്തൊക്കെ ശ്രമിച്ചു? എന്താണ് ഫലിച്ചത്?
4. Who decides, and what monthly budget is comfortable?
   തീരുമാനിക്കുന്നത് ആരാണ്, മാസം എത്ര ചെലവാക്കാൻ സൗകര്യമുണ്ട്?
5. What would make the next 3 months a success?
   അടുത്ത 3 മാസം വിജയമായി എന്ന് എപ്പോൾ തോന്നും?
""", ''),
        ('proposal (one or two pages)', """
PROPOSAL FOR [BUSINESS] - [DATE]
1. YOUR GOAL: "________" (their words)
2. WHAT I FOUND: 1. ____ 2. ____ 3. ____ (screenshots)
3. THE PLAN (3 months): month 1 ____ / 2 ____ / 3 ____
4. PACKAGE: ________ Rs ____ a month (+ GST if applicable)
   Included: ____  Not included: ____  Ad spend: ____
5. WHAT I NEED FROM YOU: photos ____ / approvals within
   24 h / manager access (never passwords)
6. HOW WE'LL MEASURE: ________; monthly report
7. TERMS: paid in advance; 3-month minimum; either side
   can end with ___ days' notice after that
NEXT STEP: Reply YES and I'll send the agreement.
(No guarantees of sales or followers: I promise the work,
honest measurement and clear reports.)
""", ''),
        ('walk-in and follow-up scripts', """
WALK-IN: "Hi, I'm ____, I help shops around ____ get found
on Google and Instagram. I noticed two quick fixes for
your profile. Can I show you in 2 minutes?"
FOLLOW-UP 1 (3 days): "Hi ____, thanks for your time on
____. Here's the profile check I mentioned: [link]. Happy
to help with it if useful."
FOLLOW-UP 2 (1 week): "Hi ____, just checking if you had
a chance to look. No pressure; I'm around if you need me."
""", ''),
    ],
    mistakes=[
        ('Mass cold messages.', 'They annoy people and can get your number restricted. Be personal.'),
        ('Pitching before listening.', 'Discovery first; the proposal uses their words.'),
        ('Guaranteeing results.', 'Promise work, measurement and honesty, not sales.'),
        ('No follow-up.', 'Follow up twice, politely, with something useful.'),
        ('Ten-page proposals.', 'One or two pages, plain language.'),
    ],
    quiz=[
        {'q': 'Which source usually brings a beginner\'s first clients?',
         'o': ['Mass cold WhatsApp messages', 'People who know you, the pilot and audited businesses, and referrals', 'Paid lead lists', 'Random comments'],
         'a': 'B', 'why': 'Warm contacts trust you faster.'},
        {'q': 'What should a proposal promise?',
         'o': ['Guaranteed sales', '10,000 followers', 'The work, honest measurement and clear reports', 'Going viral'],
         'a': 'C', 'why': 'Outcomes depend on many things; promise what you control.'},
        {'q': 'What comes before writing a proposal?',
         'o': ['Sending your price list to everyone', 'A discovery conversation about the client\'s goals', 'An invoice', 'An ad campaign'],
         'a': 'B', 'why': 'Listening first lets you propose what they actually need.'},
    ],
    study='OpenStax 15.1 on personal selling, HubSpot\'s sales training and WhatsApp\'s messaging limits (about 35 minutes)',
    action='build a 30-lead pipeline, contact 10, hold 2 discovery talks and write one proposal',
)

L3 = lesson(
    15, 3,
    title='Contracts, onboarding and monthly reports',
    weeks=(39, 39), hours=2,
    outcome='Put every paid client on a simple written agreement, onboard them in the first week with roles instead of passwords, and run a monthly reporting rhythm that keeps clients for years.',
    split='30 minutes study, 1 hour 30 minutes action',
    core="""
### A simple service agreement

A written agreement protects you and the client and prevents most arguments. It doesn't need legal jargon; it needs clarity. The Entrepreneurship course covers contract basics in ENT-M09-L03. This course isn't legal advice; for large or unusual contracts, ask a lawyer.

Cover these points:

| Point | What to write |
| --- | --- |
| **Parties** | Names, business names, addresses |
| **Scope** | Exactly what you'll deliver each month (from the package) |
| **Not included** | Shoots, printing, ad spend, extra revisions, emergencies outside hours |
| **Term** | Start date, minimum term (for example 3 months), then month to month |
| **Fees and payment** | Amount, GST if applicable, paid in advance by a date, how |
| **Ad spend** | Paid by the client directly to the platform |
| **Approvals** | The client approves posts within 24 hours; what happens if they don't |
| **Access** | Roles, never passwords; the client owns the accounts |
| **Content ownership** | The client owns the final content once paid; you may show it in your portfolio unless they say no |
| **Compliance** | Honest claims, disclosure, consent for photos; the client confirms facts and offers |
| **Data** | You keep customers' details private and use them only for the agreed work |
| **No guarantees** | You don't guarantee specific sales or follower numbers |
| **Ending** | Either side can end with a set notice after the minimum term; you hand over files and remove your access |

### Invoices and tax

Send an invoice for every payment: your name, the client's, the date, what it's for, the amount and GST if you're registered. Some business clients may deduct tax (TDS) before paying; ENT-M08-L03 explains the basics, and a tax professional can advise you (check current rules).

### Onboarding in the first week

A smooth start tells the client they chose well:

1. **Welcome message** with the plan for week 1.
2. **Kick-off meeting** (30–45 minutes): goals, customers, offers, do's and don'ts, approval process, contact hours.
3. **Access by roles:** manager on Google Business Profile; people or partners added in Meta Business Suite; never passwords.
4. **Materials:** logo, colours, photos, price list, FAQs.
5. **Baseline numbers** for the KPIs.
6. **First calendar** shared for approval.
7. **Tracking** set up: keyword, labels, "how did you hear about us?".

### The monthly rhythm

- **Weekly:** a short WhatsApp update (SMM-M08-L03).
- **Monthly:** the one-page report and a 20-minute meeting: results, what you learned, next month's plan, what you need.
- **Every three months:** review the goal, the package and the price.

Clients rarely leave a marketer who reports honestly, explains clearly and keeps improving the results.
""",
    example="""
Arun's onboarding of Peak Fitness (made-up example):

- **Day 1:** agreement signed (Growth package, 3 months, ₹12,000 a month paid in advance on the 1st, ad spend separate, approvals within 24 hours, 15 days' notice after 3 months). Invoice sent and paid by UPI.
- **Day 2:** 40-minute kick-off. The owner's rules: no "before and after" body photos, no weight-loss promises, women members filmed only with written consent.
- **Day 3:** manager access to the Google profile; added to the business portfolio in Meta Business Suite; baseline: 6 WhatsApp enquiries a week.
- **Day 5:** first month's calendar sent for approval; review card and "how did you hear" question at the front desk.

At the end of month 1 he sent the one-page report (11 enquiries a week by week 4, 3 joins from the women's batch) and agreed month 2's plan in a 20-minute meeting.
""",
    resources=[
        ('dpdp', 'Re-read consent and data duties, for the data clause', '10 min'),
        ('mbs-app', 'Re-read what Meta Business Suite manages, for access by roles', '3 min'),
        ('gbp-start', 'Re-read Google Business Profile basics, for manager access', '3 min'),
    ],
    steps=[
        'Study the resources (about 15 minutes) and read ENT-M09-L03 on contracts if you haven\'t.',
        'Write your service agreement template from the table, in plain English (and a Malayalam summary).',
        'Make an invoice template.',
        'Write your onboarding checklist and welcome message.',
        'Turn your monthly report from SMM-M08-L03 into a client version with your branding.',
    ],
    proof='Your service agreement template, invoice template, onboarding checklist with welcome message, and client report template.',
    templates=[
        ('service agreement (template)', """
SOCIAL MEDIA SERVICE AGREEMENT
Between [your name, address] and [client, business, address]
1. SCOPE each month: ________________ (from the package)
2. NOT INCLUDED: shoots, printing, ad spend, extra revisions,
   work outside [hours]
3. TERM: from ____; minimum 3 months; then month to month
4. FEES: Rs ____ a month (+ GST if applicable), paid in
   advance by the ___ of each month, by UPI/bank transfer
5. AD SPEND: paid by the client directly to the platform
6. APPROVALS: the client replies within 24 hours; if not,
   the post moves to the next slot
7. ACCESS: by roles only; the client owns all accounts
8. CONTENT: the client owns final content once paid; I may
   show it in my portfolio unless the client says no
9. COMPLIANCE: honest claims; disclosure of paid or gifted
   posts; consent for people filmed; the client confirms
   facts, prices and offers
10. DATA: customers' details kept private, used only for
    this work
11. NO GUARANTEES of specific sales or follower numbers
12. ENDING: after the minimum term, ___ days' notice by
    either side; I hand over files and remove my access
Signed: ________ (client)  ________ (me)  Date: ____
""", ''),
        ('onboarding checklist and welcome message', """
WELCOME: "Hi ____, welcome aboard! This week: kick-off
meeting (____), access set-up, and your first month's
calendar for approval by ____."
[ ] Agreement signed; first invoice paid
[ ] Kick-off: goals, customers, offers, do's and don'ts,
    approvals, contact hours
[ ] Access: Google profile manager; Meta Business Suite
    roles; WhatsApp plan agreed (never passwords)
[ ] Materials: logo, colours, photos, price list, FAQs
[ ] Baseline KPI numbers recorded
[ ] Tracking: keyword, labels, "how did you hear" question
[ ] First calendar sent for approval
[ ] Weekly update day and monthly meeting date agreed
""", ''),
        ('invoice', """
INVOICE No. ____  Date: ____
From: [your name, address, phone, GSTIN if registered]
To: [client name, business, address]
Description                         Amount (Rs)
[Package] for [month]               ________
GST (if applicable)                 ________
TOTAL                               ________
Pay by: UPI ____ / bank ____  Due: ____
""", ''),
    ],
    mistakes=[
        ('Starting without a written agreement.', 'Even a one-page agreement prevents most disputes.'),
        ('Taking passwords.', 'Use roles; the client owns the accounts.'),
        ('Unclear approvals.', 'Agree a time limit and what happens when it passes.'),
        ('Reports only when things go well.', 'Report every month, good or bad, with a plan.'),
    ],
    quiz=[
        {'q': 'Who should own the client\'s social media accounts?',
         'o': ['The marketer', 'The client; the marketer gets access by roles', 'Whoever made them', 'The platform'],
         'a': 'B', 'why': 'It protects the client and keeps your role clean.'},
        {'q': 'What should the agreement say about results?',
         'o': ['Guaranteed sales', 'No guarantee of specific sales or follower numbers', 'Double followers in a month', 'Nothing'],
         'a': 'B', 'why': 'You promise the work and honest reporting, not outcomes you don\'t control.'},
        {'q': 'What is the purpose of the kick-off meeting?',
         'o': ['To collect payment only', 'To agree goals, customers, offers, rules, approvals and contact hours', 'To post the first Reel', 'To set up ads'],
         'a': 'B', 'why': 'A clear start prevents misunderstandings later.'},
    ],
    study='Data and access rules for client work, plus ENT-M09-L03 on contracts (about 15 minutes)',
    action='write your service agreement, invoice, onboarding checklist and client report templates',
)

L4 = lesson(
    15, 4,
    title='Growing into an agency',
    weeks=(39, 39), hours=1,
    outcome='Recognise when you are ready to grow from freelancer to a small agency, and plan the first steps (niche, systems, first helper, margins) without risking quality or your health.',
    split='20 minutes study, 40 minutes action',
    core="""
### Freelancer or agency?

Many marketers stay happily solo with four to six good clients. An **agency** makes sense when you have more demand than time, systems that others could follow, and the wish to manage people. It is a choice, not the only definition of success.

### Signs you're ready

- You've had a steady 4–6 clients for several months, and still get enquiries.
- Your work follows repeatable steps (the templates and checklists from this course).
- Clients pay on time, and you know your cost per client.
- You're turning work down, or your quality is starting to slip.

### The first steps

1. **Niche down:** become the go-to for one kind of business (bakeries and cafés, gyms and clinics, homestays) in your area. A niche makes templates, case studies and referrals stronger.
2. **Write SOPs:** turn your checklists into step-by-step instructions someone else could follow (the Entrepreneurship course covers SOPs in Module 10).
3. **First helper:** usually a part-time freelance video editor or designer, paid per piece, before any full-time hire. ENT-M12-L03 covers hiring and delegating. Give them a short written agreement covering the work, payment, confidentiality and that the client owns the final content.
4. **Check your margins:** price so that you still earn a healthy profit after paying helpers.
5. **Quality control:** you approve everything before it reaches a client, at least at first.
6. **Formalise:** registrations, GST and a business bank account as you grow (ENT-M08 and ENT-M09; check current rules).

### Risks to watch

- **One big client** making up most of your income
- **Cash flow:** paying helpers before clients pay you
- **Saying yes to everything** and missing deadlines
- **Burnout:** growth on top of exhaustion fails. YouTube's advice to creators applies here too: get help with the tasks that take your time and energy (Module 16).
""",
    example="""
Arun's ShopAssist after a year (made-up example):

- **Niche:** small shops in Vatakara and Kuttiady: textiles, mobiles, bakeries.
- **Clients:** 7 on monthly packages, none more than 20% of income.
- **Helpers:** one part-time video editor (₹300 per Reel edit) and one college student for Status design, both on short written agreements.
- **SOPs:** onboarding, monthly calendar, Reel production, monthly report, offboarding.
- **Margin check:** a Growth client brings ₹12,000; helpers cost about ₹3,000; travel and tools ₹800; Arun's margin is about ₹8,200 for roughly 9 hours of his own time.
- **Next step:** a second editor before taking client number 9, so quality doesn't drop.
""",
    resources=[
        ('yt-burnout', 'Re-read the tip on getting help for tasks that drain your time', '5 min'),
        ('hubspot-sales', 'Optional: look at the Sales Enablement course for later', '5 min'),
    ],
    steps=[
        'Study the resources (about 10 minutes), and skim ENT-M12-L03 on hiring and delegating.',
        'Score yourself on the four "ready" signs, honestly.',
        'Choose a niche you could own in your area, and write why.',
        'List the three tasks you would hand to a first helper, and write one SOP for one of them.',
        'Do a margin check for one package with a helper\'s cost included.',
    ],
    proof='Your readiness score, niche choice, one SOP and a margin calculation.',
    templates=[
        ('agency readiness and margin check', """
READY? (Y/N)
[ ] Steady 4-6 clients for several months
[ ] Repeatable steps written down
[ ] Clients pay on time; I know my cost per client
[ ] Turning work down or quality slipping
NICHE I COULD OWN: ________ in ________ because ________
FIRST HELPER TASKS: 1. ____ 2. ____ 3. ____
MARGIN (one client, per month)
  Fee                      Rs ____
  Helper costs           - Rs ____
  Travel, data, tools    - Rs ____
  My margin                Rs ____ for ___ of my hours
""", ''),
    ],
    mistakes=[
        ('Hiring before systems exist.', 'Write SOPs first, then delegate.'),
        ('Dropping prices to win volume.', 'Agency margins need fair prices.'),
        ('Relying on one big client.', 'Keep any single client under about a fifth of income where you can.'),
    ],
    quiz=[
        {'q': 'What is usually the best first hire for a small social media business?',
         'o': ['A full-time manager', 'A part-time freelance editor or designer paid per piece', 'An accountant on salary', 'Nobody, ever'],
         'a': 'B', 'why': 'It adds capacity with low risk.'},
        {'q': 'Why niche down when growing?',
         'o': ['It\'s required by law', 'Templates, case studies and referrals get stronger in one kind of business', 'To have fewer clients', 'To avoid reporting'],
         'a': 'B', 'why': 'Specialists win trust and work faster.'},
        {'q': 'Which is a sign you are ready to grow?',
         'o': ['One client and lots of free time', 'Steady clients, written systems and more demand than time', 'Wanting a bigger title', 'Getting bored'],
         'a': 'B', 'why': 'Growth works when demand and systems are already there.'},
    ],
    study='YouTube\'s delegation tip and the Entrepreneurship course\'s hiring lesson (about 10 minutes)',
    action='score your readiness, choose a niche, write one SOP and check one package\'s margin',
)

LESSONS = [L1, L2, L3, L4]

MODULE = module(
    15,
    title='Earning with social media marketing',
    weeks=(37, 39), hours=9,
    overview="""
Turn your skills into income: clear packages and prices, local clients found honestly, proposals that win, written agreements, smooth onboarding, monthly reports that keep clients, and a path to a small agency if you want one.

This module turns your pilot and case studies into a business. In three weeks you'll design packages and a price sheet, build a pipeline of local leads, run discovery conversations, write proposals, and set up the agreement, invoice, onboarding and reporting templates that make you look and work like a professional.

The module project is your sales kit and your first ten real pitches.
""",
    outcomes=[
        'Design setup, monthly and add-on packages with clear scope',
        'Price fairly using cost, value and market checks',
        'Find local clients and run discovery conversations',
        'Write proposals and simple service agreements',
        'Onboard clients with roles instead of passwords and report monthly',
    ],
    lessons=LESSONS,
    project='Your sales kit and 10 real pitches',
    project_week=39,
    project_steps=[
        'Put your sales kit in 15 Sales: price sheet, package designs, proposal template, service agreement, invoice, onboarding checklist and client report template.',
        'Add your packages and price sheet to the Services page of your portfolio site.',
        'Pitch 10 real businesses (visits, calls, or messages after an introduction), including your pilot client for a paid package.',
        'Track every pitch in the Leads and Clients tab with a next step and date.',
    ],
    project_proof='Your sales kit folder, the updated Services page and the Leads and Clients tab showing 10 pitches.',
    rubric=[
        ('Packages and pricing', 'Prices per post, no scope', 'Packages without checks', 'Clear packages priced by cost, value and market, with terms'),
        ('Finding clients', 'Waits for enquiries', 'Some outreach', 'A 30-lead pipeline from warm sources, 10 personal pitches'),
        ('Proposals', 'Price list only', 'Long or vague', 'One or two pages in the client\'s words, no guarantees, clear next step'),
        ('Agreements and onboarding', 'Verbal only', 'Agreement without onboarding', 'Written agreement, invoice and first-week onboarding with roles'),
        ('Reporting', 'Irregular', 'Monthly numbers only', 'Weekly updates and a one-page monthly report with a plan'),
    ],
    short=[
        'Design one setup package and one monthly package.',
        'List 15 leads and pitch 5.',
        'Write a one-page proposal from the template.',
        'Use the agreement template as it is for your first client.',
    ],
    flashcards=[
        ('Three package types?', 'One-time setup, monthly retainer, add-ons.'),
        ('Hourly target formula?', 'Monthly income needed ÷ realistic billable hours.'),
        ('Three price checks?', 'Cost, value to the client, local market.'),
        ('Who pays ad spend?', 'The client, directly to the platform, separate from your fee.'),
        ('Pipeline stages?', 'Lead, contacted, meeting, proposal sent, won or lost.'),
        ('What does a proposal never promise?', 'Guaranteed sales or follower numbers.'),
        ('How do you get access to client accounts?', 'By roles (manager, partner), never passwords.'),
        ('Who owns the final content?', 'The client, once paid (you may show it in your portfolio unless they say no).'),
    ],
    mistakes=[
        ('Free work forever.', 'One pilot is enough; then charge fairly.'),
        ('No written terms.', 'Agreements protect friendships as well as business.'),
        ('Selling what you can\'t deliver.', 'Promise a scope you can do well alongside everything else.'),
    ],
)
