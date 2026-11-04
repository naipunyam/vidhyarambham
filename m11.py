from common import lesson, module, link, rules, xref, table, fence, Q, RULE, ASOF, CHECK
import tools

INTERVIEW = """BROKER / PROFESSIONAL INTERVIEW GUIDE (20-30 minutes; ask permission to take notes)
Name (private) ______  Role: broker / document writer / advocate  Area ______  Years ______
ABOUT THE MARKET
1 What sells fastest here, and at what price per cent? What doesn't sell?
2 What is the usual gap between asking and final price?
3 Who are the buyers now: local families, NRIs, investors? What changed since 2018-2020?
HOW DEALS WORK
4 How do you find owners and buyers? Which sources work best?
5 What commission do you charge for sales and rentals? Who pays?
6 What goes wrong most often in deals? (title, heirs, nilam, roads, cash)
7 How do token advances and agreements usually work here?
FOR DOCUMENT WRITERS / ADVOCATES
8 What papers do you need for a sale deed? Fees? How long?
9 What problems do you see most often in title chains?
10 When should a broker call you?
CLOSE
11 What would you advise someone starting out honestly?
12 Can I contact you again, or refer clients to you?  Y/N
MY NOTES: three things I learned ______ ; one thing I'll do differently ______"""

L1 = lesson(
    11, 1,
    outcome='You can build a local and NRI network for sourcing properties and clients, and learn the market through interviews with 3 brokers and 1 document writer or advocate.',
    split='15 minutes reading, 60 minutes on interviews (spread over two weeks)',
    core=f"""
**Where deals come from in Kerala.** Most property in villages and small towns changes hands through **people**: relatives, neighbours, shopkeepers, auto and taxi drivers, temple, mosque and church committees, cooperative bank staff, document writers, contractors and Gulf returnees. Online listings are growing, but personal trust still decides most deals around Kuttiady.

**Local network (sources of owners and buyers):**
- Family and friends: tell people clearly what you do ("I help people buy, sell and rent property honestly, with proper papers").
- Shops and auto stands near junctions: owners often mention plots for sale.
- Document writers and advocates: they see deals and may refer clients who need help with marketing or rentals (never pay them for client documents or information).
- Contractors, engineers and building designers: they meet owners who are building and families who want to sell old houses.
- Cooperative banks and local institutions: they know who is moving or needs to sell.
- Residents' associations and Kudumbashree units: good for rental leads.

**NRI network.** A large share of Kerala's property owners and buyers live abroad (the Gulf in particular). They need someone trustworthy to: show and manage property, collect rent, pay taxes and handle papers. Reach them through:
- Relatives in the Gulf and returnees in your area.
- WhatsApp groups of your village's diaspora (join only with an introduction; post rarely and usefully).
- Facebook groups of Kerala NRIs and Gulf associations (follow group rules).
- Referrals from satisfied clients.

**Learning from brokers.** Experienced local brokers know prices, people and problems. Interview **3 brokers** and **1 document writer or advocate** using the guide below. Be respectful: you are a learner, not a competitor stealing clients. Offer something in return (for example good photos and listing copy for one of their properties).

**Privacy.** Collect only the contact details people give you for this purpose, ask before adding anyone to a list or group, and never share owners' or clients' details without consent. India's Digital Personal Data Protection Act, 2023 sets rules for handling personal data (unverified in this course how its rules apply to small brokers; {CHECK}).
""",
    example="""
Sachin's first two weeks:
- He tells 30 people in person and in his family WhatsApp group what he does (one clear message, no spam).
- He interviews three brokers: one in Kuttiady town (20 years, mostly land), one in Kakkattil (rentals and houses) and one younger broker who uses Instagram and NoBroker. He interviews a document writer near the SRO.
- Key lessons: plots on wide roads near town sell in weeks, interior land can take a year; heirs' disputes are the most common problem; most rentals go through word of mouth; the young broker gets NRI buyers through short walkthrough videos.
- One broker agrees to co-broke: Sachin brings a buyer, the broker has the mandate, and they split the commission in writing.
""",
    resources=[
        ('krera', 'Look up whether the brokers you meet are K-RERA registered (agent search)', '10 minutes'),
        ('nobroker', 'See how an online platform competes with local brokers, and think about what you offer that it can\'t', '10 minutes'),
    ],
    steps=[
        'Write your one-line introduction and tell 20+ people in person or by direct message (not spam).',
        'Interview 3 local brokers and 1 document writer or advocate using the guide, with permission to take notes.',
        'List your network in a "Network" tab: role, area, how you met, what they can help with, last contact (only details they gave you).',
        'Join one NRI or village diaspora group through an introduction, and read its rules before posting anything.',
    ],
    proof='Your introduction message, 4 interview notes, the Network tab (private) and the group you joined.',
    templates=[('Interview guide', INTERVIEW), ('Network tab', """NETWORK (tab "Network")  only details people gave you; keep private
Name | Role (broker/writer/advocate/engineer/contractor/NRI/owner/other) | Area | How we met | Can help with | Phone (with consent) | Last contact | Next contact | Notes
Rule: follow up every 30-60 days with something useful (a market update, a listing they asked for), not spam.""")],
    mistakes=[
        ('Spamming groups with listings.', 'Share rarely and usefully; follow group rules.'),
        ('Treating other brokers as enemies.', 'Learn from them and co-broke openly.'),
        ('Collecting phone numbers without consent.', 'Ask first; keep data private.'),
    ],
    fraud="""
**"Inside information" for a fee.** Some people offer lists of owners, NRIs or loan defaulters for money. Buying or using such data is unethical and may be illegal. Build your network through real relationships.
""",
    quiz=[
        Q('How do most village property deals around Kuttiady start?', 'Through personal networks and trust', 'Only through portals', 'Through newspapers only', 'Through banks only', why='Online is growing, but people decide.'),
        Q('Why interview local brokers?', 'To learn prices, practice and common problems', 'To steal their clients', 'To get their passwords', 'It is required by law', why='Be a respectful learner.'),
        Q('What do NRI owners most need from a local person?', 'Trustworthy help showing, managing and handling papers for their property', 'Cheap loans', 'Free holidays', 'Nothing', why='Trust is the product.'),
        Q('What should you do before adding someone to a WhatsApp list?', 'Ask for their consent', 'Nothing', 'Add everyone', 'Share their number with others', why='Respect privacy.'),
    ],
    study='read the lesson and the interview guide',
    action='interview 3 brokers and 1 document writer or advocate and set up your network',
)

LEAD_Q = [
    ('Hot', 'Clear need, budget and timeline within 3 months; loan pre-approved or cash ready', 'Visit within a week'),
    ('Warm', 'Clear need, budget unclear or timeline 3 to 12 months', 'Follow up monthly with matching properties'),
    ('Cold', 'Just looking, no budget or timeline', 'Add to your occasional updates, with consent'),
    ('Not a fit', 'Wants cash deals, undervaluation, or properties you don\'t handle', 'Politely decline or refer'),
]

L2 = lesson(
    11, 2,
    outcome='You can source properties and buyers from builders and online channels, qualify leads as hot, warm or cold, and track them.',
    split='15 minutes reading, 45 minutes on sourcing and lead qualification',
    core=f"""
**Builders and developers.** Small builders in Kozhikode and nearby towns need sales help for flats, villas and plotted layouts. Before working with any project:
- Check its **K-RERA registration** if it is above the threshold ({link('krera', 'K-RERA')}) and your own registration (RE-M10-L01).
- Read the approvals and the builder's track record (completed projects, complaints).
- Get a written agreement for commission, payment timing and what you may advertise.
- Never promise buyers what the builder hasn't put in writing.

**Online sources:**
- **Portals:** MagicBricks, 99acres, Housing.com and NoBroker for both listings and buyer enquiries; owners can list free on NoBroker ({link('nobroker', 'NoBroker')}). Watch the portals for "for sale by owner" listings and contact owners politely to offer help (accept a "no").
- **OLX and Facebook Marketplace and groups:** many local rentals and plots; verify every detail.
- **Instagram and YouTube:** good for walkthrough videos that attract NRI buyers (Module 12).
- **Google Business Profile:** people searching "real estate agent near Kuttiady" (Module 12).

**Lead quality.** A lead is anyone who might buy, sell, rent or let. Qualify every lead with the client intake form (RE-M13-L01) and grade it:
{table(['Grade', 'Signs', 'Action'], LEAD_Q)}

**Responding to a new lead.** Reply the same day if you can; speed matters more than polish. A simple first reply: "Thank you for contacting me about the 10-cent plot in Kakkattil. I'm Sachin, a local property agent. The owner has asked me to handle enquiries. Could you tell me what you're looking for, your budget range and when you plan to buy? I can share the location and photos, and arrange a visit with the owner's permission." Then fill in the intake form. Don't send the owner's phone number, the full address or document copies at this stage.

**Following up without pestering.** Hot leads: every few days until a visit. Warm leads: once a month with genuinely matching properties. Cold leads: occasional market updates only if they agreed. Stop when someone says no, and remove their number if asked.

Track every lead in your **CRM** (Leads tab; RE-M19-L01) from the first contact, with the source, so you learn which sources bring deals, not just enquiries.
""",
    example="""
After a month Sachin has 26 leads:
- Sources: family network 9, NoBroker 6, Facebook groups 5, brokers (co-broke) 3, builder 3.
- Grades: hot 3, warm 9, cold 12, not a fit 2 (one wanted a cash deal with an undervalued deed; one wanted "any land, cheapest possible, no papers").
- His CRM shows that family network leads became 2 site visits and Facebook leads became 0. He spends more time on referrals and less on Facebook posts.
""",
    resources=[
        ('nobroker', 'See owner listings in Kozhikode', '10 minutes'),
        ('magicbricks', 'See builder and owner listings', '10 minutes'),
        ('krera', 'Check registration of one local project', '10 minutes'),
    ],
    steps=[
        'Find 3 local builders or projects; check K-RERA status and note who handles sales.',
        'Find 5 "for sale by owner" or "for rent by owner" listings and politely offer your service to 2 owners (accept any "no").',
        'Grade all current leads with the table and enter them in your CRM with the source.',
        'After two weeks, count leads and site visits by source.',
    ],
    proof='Builder notes, owner contact notes, the CRM with grades and sources, and the source count.',
    templates=[('Lead grading and source count', """LEAD GRADING (add column "Grade" to the Leads tab)
Hot  = need + budget + timeline < 3 months + finance ready
Warm = need + budget unclear or timeline 3-12 months
Cold = browsing
Not a fit = asks for cash/undervaluation/no papers -> decline politely
SOURCE COUNT (Dashboard tab)
Leads by source:   =COUNTIF(Leads!E:E,"NoBroker")
Visits by source:  =COUNTIFS(Leads!E:E,"NoBroker",Leads!J:J,"visited")
Closed by source:  =COUNTIFS(Leads!E:E,"NoBroker",Leads!J:J,"closed")""")],
    mistakes=[
        ('Chasing every lead equally.', 'Grade leads and focus on hot ones.'),
        ('Promoting unregistered projects.', 'Check K-RERA first.'),
        ('Not recording the source.', 'You can\'t improve what you don\'t measure.'),
    ],
    fraud="""
**Fake buyers.** Some "buyers" want copies of owners' documents, or ask for the owner's details to bypass you, or are scammers looking for property papers to misuse. Share documents only with serious buyers after a site visit, and only the summary until the advocate stage.
""",
    quiz=[
        Q('What should you check before selling a builder\'s project?', 'Its K-RERA registration and your own registration', 'Only the brochure', 'The builder\'s car', 'Nothing', why='RERA rules apply.'),
        Q('A lead has a clear need, budget and a loan pre-approved for next month. Grade?', 'Hot', 'Cold', 'Not a fit', 'Warm', why='Visit within a week.'),
        Q('A lead wants an undervalued deed and part payment in cash. What do you do?', 'Politely decline', 'Agree', 'Ignore the law', 'Ask for more cash', why='Not a fit.'),
        Q('Why record the source of each lead?', 'To see which sources bring real deals', 'For tax', 'It is not useful', 'To share with others', why='Measure and improve.'),
    ],
    study='read the lesson and the lead grading table',
    action='source from builders and owner listings, grade your leads and count them by source',
)

LESSONS = [L1, L2]

MODULE = module(
    11,
    overview=f"""
Sourcing properties and buyers: local and NRI networks, learning from brokers and professionals, builders, online sources, and qualifying and tracking leads.

The practical heart of this module is the interviews: 3 local brokers and 1 document writer or advocate. They will teach you more about the Kuttiady and Kozhikode market than any website. Everything is {RULE}.
""",
    outcomes=[
        'Build a local and NRI network with consent.',
        'Interview brokers and professionals and learn the local market.',
        'Source from builders and online channels.',
        'Grade and track leads by source.',
    ],
    lessons=LESSONS,
    project='a network and lead pipeline',
    project_steps=[
        'Complete 4 interviews and write a one-page summary of what you learned.',
        'Set up the Network tab with at least 20 contacts (with consent).',
        'Have at least 10 graded leads in your CRM with sources.',
        'Agree one co-broking or referral arrangement in writing, if possible.',
    ],
    project_proof='The interview summary, Network tab, CRM and any written arrangement (private details hidden).',
    rubric=[
        ('Interviews', 'None', '1 to 3 done', '4 done with a written summary'),
        ('Network', 'Under 10 contacts', '10 to 19', '20+ with roles and follow-up dates'),
        ('Leads', 'Not tracked', 'Tracked without grades', 'Graded, with source counts'),
        ('Ethics', 'Spam or no consent', 'Some care', 'Consent, privacy and honest co-broking'),
    ],
    short=[
        'Interview 2 brokers.',
        'Enter 5 leads in the CRM with grades.',
    ],
    flashcards=[
        ('Main source of village deals', 'Personal networks and trust.'),
        ('NRI owners need', 'A trustworthy local person.'),
        ('Co-broking', 'Two brokers share a deal and commission openly.'),
        ('Hot lead', 'Need + budget + timeline + finance ready.'),
        ('Not a fit', 'Wants cash, undervaluation or no papers.'),
        ('Builder check', 'K-RERA registration first.'),
    ],
    mistakes=[
        ('Relying only on portals.', 'Build personal networks too.'),
        ('Not following up.', 'Set next contact dates.'),
        ('Overpromising to builders or owners.', 'Promise effort and honesty, not results.'),
    ],
    tools=[
        'Interview guide (RE-M11-L01).',
        'Network tab (RE-M11-L01).',
        'Lead grading and source count (RE-M11-L02).',
    ],
    toolkit=[
        'Interview guide and 4 interview notes.',
        'Network tab.',
        'Lead grading in the CRM.',
    ],
)
