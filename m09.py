from common import lesson, module

L1 = lesson(
    9, 1,
    title='Choose a business structure',
    weeks=(22, 22), hours=3,
    outcome='Compare the five common business structures in India and choose the right one for now, with a written agreement if you have a partner.',
    split='1 hour 20 minutes study (plus 35 minutes if you have a co-founder), 1 hour 40 minutes action',
    core="""
A business structure decides who owns the business, who is responsible for its debts, how it is taxed and how much paperwork it needs. For a new micro-business, simpler is usually better, and you can change structure later when there is a reason.

| | Sole proprietorship | Partnership firm | LLP | One Person Company (OPC) | Private limited company |
| --- | --- | --- | --- | --- | --- |
| Owners | One person | 2 or more partners | 2 or more partners, at least 2 of them designated partners | One person, with a nominee | 2 or more shareholders and directors |
| Main law | No special law: it is you, trading | Indian Partnership Act, 1932 | LLP Act, 2008 | Companies Act, 2013 | Companies Act, 2013 |
| Registration | None as such; you use Udyam, GST and licences as needed | A partnership deed; registering with the Registrar of Firms is optional but useful | With the Ministry of Corporate Affairs (MCA) | With the MCA | With the MCA |
| Liability | Unlimited: your personal property is at risk | Unlimited, and shared | Limited to your contribution (not for your own fraud) | Limited | Limited |
| Paperwork | Lowest | Low | Medium: yearly filings | High: company compliance | Highest |
| Raising equity | Not possible | Hard | Possible, but investors prefer companies | Limited | Easiest; most investors need it |
| Good for | Starting small and testing | Two or more people starting small together | Partners who want limited liability with less paperwork than a company | A single founder who needs a company | Startups planning to raise investment or grow fast |

Points to know (check current rules):

- **Partnership firms:** under section 69 of the Partnership Act, an unregistered firm generally can't sue a third party to enforce a contract. Registering with the Registrar of Firms (in Kerala, under the Registration Department) avoids this problem.
- **Startup India recognition** (by DPIIT) is for private limited companies, registered partnership firms, LLPs and cooperative societies. A sole proprietorship can't be recognised as a startup.
- **Tax** differs between structures. Ask a CA before you choose anything other than a sole proprietorship.
- **Costs:** an LLP or a company needs digital signatures, government fees, professional help and yearly filings. Don't take that on until you need limited liability, investors, or a bigger client who insists on it.

### Protect the business from big losses

A structure limits some kinds of liability, but most risks for a micro-business are practical:

- **Insurance:** fire and theft cover for stock and equipment, and health insurance for yourself, so that one bad event doesn't end the business. Kerala's MSME Insurance Scheme reimburses Udyam-registered MSMEs 50% of the annual premium, up to ₹2,500, for certain policies from public sector insurers, through the DIC (check current rules).
- **Backups:** keep your Founder Workbook, customer list and designs in Google Drive with two-step verification, and download a copy every month.
- **Written agreements** with customers, partners and helpers (ENT-M09-L03).
- **Spread the risk:** avoid depending on one big customer or a single supplier.

OpenStax's section 13.7 on mitigating and managing risks covers the wider picture.

### If you have a co-founder or partner

Write your agreement down before you start, even with a friend or relative. Cover:

1. **Roles:** who does what
2. **Money:** who puts in how much, and whether it is a loan or ownership
3. **Ownership split**, and **vesting**: ownership earned over time, so someone who leaves early doesn't keep a big share
4. **Decisions:** how they are made, and how a tie is broken
5. **Pay:** when and how partners take money out
6. **Assets:** who owns the brand, the content and the customer list
7. **Leaving:** what happens if someone leaves or wants to sell
8. **Disputes:** how they will be resolved

Y Combinator's talk on co-founder relationships covers choosing a co-founder and keeping the relationship healthy.
""",
    example="""
Arun works with his friend Fazil, who photographs stock for some shops. They thought about a partnership but kept ShopAssist as **Arun's sole proprietorship** for now, paying Fazil ₹300 per shop as a freelancer, agreed in writing. If they later share ownership, they will write a partnership deed with vesting and register the firm, or form an LLP if clients or risks grow.

Nisha runs Nisha's Oven as a **sole proprietorship**: she is the only owner, her risks are small and the paperwork is the lowest.

Fathima and her cousin want to turn PSC Sprint into an app and apply to KSUM. They plan to form a **private limited company** once their weekly test channel proves demand, because startup recognition needs a registered entity and investors would expect a company.
""",
    resources=[
        ('os13', 'Sections 13.1, 13.3–13.5 and 13.7 on structures and risk. The book uses US law, so read it for the ideas only', '55 min'),
        ('kerala-insurance', 'Read who is eligible for the premium support and how to claim it (check current rules)', '10 min'),
        ('mca', 'Browse the portal to see where LLPs and companies are registered (check current rules)', '10 min'),
        ('partnership-act', 'Optional: section 69, on what happens when a firm is not registered', '5 min'),
        ('startupindia-recognition', 'Read the eligibility criteria for startup recognition', '5 min'),
        ('yc-cofound', 'Only if you have, or want, a co-founder', 'about 35 min'),
    ],
    steps=[
        'Fill in the structure decision sheet for your business.',
        'Write down what would make you change structure later (hiring staff, a large contract, raising money, a partner joining), and your two biggest risks with how you will protect against them: insurance, backups or agreements.',
        'If you have a partner or co-founder, draft your one-page agreement covering the 8 points, and sign it together.',
        'Ask one CA, lawyer or experienced business owner one question about your choice, and note the answer.',
        'Save the decision in Founder Toolkit/09 Legal.',
    ],
    proof='Your structure decision sheet, your triggers for changing structure, your two biggest risks with their protections, the partner agreement (if you have a partner) and the expert\'s answer.',
    templates=[
        ('structure decision', """
STRUCTURE DECISION     Date: ____
Owners: ____ (how many, and who)
Could customers or suppliers hold me liable for large
amounts? Y / N  ____________
Do I plan to raise equity from investors? Y / N
Do I need Startup India or KSUM recognition? Y / N
Paperwork I can handle: low / medium / high

Choice for now: sole proprietorship / partnership /
LLP / OPC / private limited company
Why (3 reasons): ____________
I will review this when:
[ ] I hire staff  [ ] turnover passes ₹____
[ ] a partner joins  [ ] I raise money
[ ] a client insists
Question asked to (CA / lawyer / owner): ____
Answer: ____________
""", ''),
        ('co-founder or partner agreement', """
PARTNER AGREEMENT (one page, signed by everyone)
1. Roles: ____ does ____; ____ does ____
2. Money in: ____ (a loan, or ownership?)
3. Ownership split: ____ / ____
   Vesting: earned over ____ years, ____ each year
4. Decisions: ____; ties broken by ____
5. Taking money out: ____
6. The brand, content and customer list belong to ____
7. If someone leaves: ____
8. Disputes: talk first, then ____
   (mediation or arbitration)
Signed: ____  ____    Date: ____
""", ''),
    ],
    mistakes=[
        ('Registering a company too early.', 'A company brings yearly filings and professional fees. Start as a sole proprietor unless you have a clear reason not to.'),
        ('No written agreement with a partner.', 'Friends and relatives fall out over money and roles. Write it down while you still agree.'),
        ('A 50/50 split with no vesting.', 'If one partner leaves after two months and keeps half, the business is stuck. Use vesting.'),
        ('Following a US article.', 'OpenStax explains the ideas using US law. Check Indian rules on official sites or with a professional.'),
    ],
    quiz=[
        {'q': 'Which structure has the least paperwork?',
         'o': ['Private limited company', 'Sole proprietorship', 'LLP', 'One Person Company'],
         'a': 'B', 'why': 'There is no separate registration law; you trade as yourself.'},
        {'q': 'What is the main risk of a sole proprietorship?',
         'o': ['It needs seven directors', 'Unlimited liability: your personal property is at risk', 'It can\'t open a bank account', 'It can\'t sell online'],
         'a': 'B', 'why': 'You and the business are legally the same, so its debts are your debts.'},
        {'q': 'What can an unregistered partnership firm generally not do, under section 69?',
         'o': ['Sell goods', 'Sue a third party to enforce a contract', 'Hire staff', 'Open a shop'],
         'a': 'B', 'why': 'Registration with the Registrar of Firms removes this limit.'},
        {'q': 'Which kinds of entity can get DPIIT startup recognition?',
         'o': ['Only sole proprietorships', 'Private limited companies, registered partnership firms, LLPs and cooperative societies', 'Any individual', 'Only government companies'],
         'a': 'B', 'why': 'That is the list on Startup India\'s recognition page.'},
        {'q': 'Why use vesting in a co-founder agreement?',
         'o': ['To pay less tax', 'So ownership is earned over time, and someone who leaves early doesn\'t keep a big share', 'Every business must', 'To raise prices'],
         'a': 'B', 'why': 'Vesting protects the people who stay and keep building.'},
    ],
    study='OpenStax chapter 13 (for the ideas), the MCA portal and Startup India\'s eligibility page (about 1 hour)',
    action='choose your structure with reasons, set review triggers, write a partner agreement if needed and ask an expert',
)

L2 = lesson(
    9, 2,
    title='Registrations and licences in Kerala',
    weeks=(22, 22), hours=3,
    outcome='List the registrations and licences your business needs in Kerala, do the free and simple ones yourself, and avoid agents who charge for free services.',
    split='1 hour 15 minutes study, 1 hour 45 minutes action',
    core="""
Which registrations you need depends on what you do, where you do it and how big you are. These are the common ones for a small business in Kerala. Check each one against the official source for your exact activity (check current rules).

### The basics

- **PAN, Aadhaar and a bank account** for the business.
- **Udyam registration (MSME):** free, online, paperless and based on self-declaration, using your Aadhaar, with PAN and GST details linked where required. The portal warns against fake websites and says no private agency is authorised to do MSME registration. Udyam opens the door to MSME schemes and priority-sector loans. Under the limits shown on the portal, a micro enterprise has investment up to ₹2.5 crore and turnover up to ₹10 crore.
- **GST registration:** only if your turnover crosses the threshold or a compulsory case applies (ENT-M08-L03).

### The local body licence

Most trades and businesses need a licence from the local body: the **grama panchayat** in villages, or the **municipality or corporation** in towns. Kerala's **K-SMART** system runs local body services online. It started in municipalities and corporations in January 2024, and grama panchayats have been moving their services onto it; one panchayat's website now says it accepts applications only through K-SMART, either directly or through Akshaya centres. Ask your panchayat's front office which licence your activity needs, the fee, and whether a home-based activity is covered.

### The Kerala MSME Facilitation Act and K-SWIFT

Under the **Kerala Micro, Small and Medium Enterprises Facilitation Act, 2019**, an MSME that is not in the Pollution Control Board's "red" category can file a self-certification and receive a **Certificate of in-principle approval**. It is valid for **three years and six months**: you must obtain the required approvals within that time, and during it no authority may inspect you for the purpose of those approvals. **K-SWIFT** is Kerala's online single-window system for clearances. In 2023, the Supreme Court held that once such a certificate was obtained, a separate permission under the Kerala Panchayat Raj Act was not needed during its validity. Ask your DIC or Taluk Industries Office whether this route suits your unit.

### Food businesses: FSSAI

Every food business needs **FSSAI registration or a licence**. Small food businesses, including home-based ones, with turnover up to ₹12 lakh a year need only **basic registration**, at ₹100 a year; above that, a state licence is required (check current rules). Applications go through FSSAI's FoSCoS portal. Packed products also need proper labels under the FSSAI and legal metrology rules: the maker's name and address, net quantity, MRP, date of manufacture, best-before date and consumer care details.

### When you hire or open premises

- **Kerala Shops and Commercial Establishments Act:** if you open a shop or office, or employ workers, check with the Labour Department whether you must register.
- **EPF and ESI:** these apply once you employ a certain number of people. Check the current rules with EPFO and ESIC.
- **Professional tax:** collected by local bodies from people in trades and professions above certain income levels.
- **Pollution Control Board consent:** needed for some manufacturing activities.

### Don't pay agents for free services

Udyam registration is free. MUDRA says it has no agents. Many official services can be done online yourself, or at an Akshaya centre for its usual service charge. Be wary of websites that look official but charge "registration fees", and of messages saying your registration will be "cancelled" unless you pay.
""",
    example="""
**Nisha's checklist:** Udyam registration (free; she did it herself online in about 15 minutes); FSSAI basic registration, since her turnover is under ₹12 lakh (₹100 a year); a call to her grama panchayat's front office to ask whether her home bakery needs a licence, with the answer and date written down; labels for her packed plum cakes showing her name and address, net weight, price, date of manufacture, best-before date and phone number. No GST registration yet.

**Arun's checklist:** Udyam registration (free); no FSSAI, as he sells no food; no GST yet. The panchayat told him that his home-based service didn't need a licence, but that an office would; he noted the answer, the officer's role and the date.

**Fathima's checklist:** Udyam is optional for now. Her main legal care is copyright: every question in her packs is her own (next lesson).
""",
    resources=[
        ('udyam', 'Read the home page: free registration, documents and the warning about fake sites (check current rules)', '15 min'),
        ('fssai-doc', 'Only for food businesses: find your category and fee (check current rules)', '15 min'),
        ('foscos', 'Only for food businesses: the application portal; type the address yourself and check it is the FSSAI site', '5 min'),
        ('ksmart-ikm', 'Read what K-SMART covers', '5 min'),
        ('ksmart-panchayat', 'See how one grama panchayat now takes applications only through K-SMART', '5 min'),
        ('kerala-msme-act', 'Optional: sections 5 and 6, on self-certification and the in-principle approval certificate (check current rules)', '15 min'),
        ('kswift', 'Browse the single-window system', '5 min'),
        ('kerala-clinic', 'Find the MSME Clinic expert list for Kozhikode', '5 min'),
        ('legal-metrology', 'Only if you sell packed goods: the label declarations', '5 min'),
    ],
    steps=[
        'Fill in the compliance checklist below for your business: for each item, whether it is needed, how to get it, the cost, the official link, the status and the renewal date.',
        'If you are already selling, do your Udyam registration yourself on the official portal. It is free.',
        'Call or visit your grama panchayat or municipality front office and ask which licence your activity needs, the fee and the process. Note the answer, the officer\'s role and the date.',
        'If you sell food, start your FSSAI registration or licence.',
        'Put every renewal date in your calendar, and save a copy of every certificate in Founder Toolkit/09 Legal.',
    ],
    proof='Your filled Compliance tab, your Udyam certificate (if you are selling), notes from the local body with the date, and any applications you started.',
    templates=[
        ('compliance checklist (Compliance tab)', """
Item,Needed? (Y / N / check),How to get it,Cost,Official link,Status,Renewal date,Notes
PAN,,,,,,,
Business bank account,,,,,,,
Udyam registration,,Online (free),0,udyamregistration.gov.in,,,
GST registration,,Only above the threshold or in a compulsory case,,gst.gov.in,,,
Local body licence (panchayat or municipality),,K-SMART or the front office,,,,,
FSSAI registration or licence (food only),,FoSCoS,,,,,
Labels for packed goods,,,,,,,
Shops and Establishments registration,,Labour Department,,,,,
EPF and ESI (when hiring),,,,,,,
Professional tax,,Local body,,,,,
Trademark (optional),,IP India e-filing,,,,,
Kerala MSME in-principle approval (optional),,K-SWIFT or DIC,,,,,
Insurance for stock and equipment (optional),,Insurer; Kerala premium support via DIC,,,,,
""", 'csv'),
    ],
    mistakes=[
        ('Paying agents for free registrations.', 'Udyam registration is free on the official portal, which says no agency is authorised to do it for you.'),
        ('Assuming a home business needs nothing.', 'Food businesses need FSSAI registration even at home, and some activities need a local licence. Ask, and write down the answer.'),
        ('Missing renewals.', 'Licences expire. Put every renewal date in your calendar.'),
        ('Using someone else\'s licence or GST number.', 'It is illegal and puts both of you at risk. Get your own.'),
        ('Trusting one website.', 'Rules vary by activity and place. Confirm with the office concerned, and note the date.'),
    ],
    quiz=[
        {'q': 'How much does Udyam registration cost on the official portal?',
         'o': ['₹2,999', 'Nothing: it is free', '₹500 a year', '₹100'],
         'a': 'B', 'why': 'The portal says registration is totally free.'},
        {'q': 'What does a home baker with ₹4 lakh annual turnover need from FSSAI? (Check current rules.)',
         'o': ['Nothing', 'Basic FSSAI registration', 'A central FSSAI licence', 'Only GST'],
         'a': 'B', 'why': 'Basic registration covers food businesses with turnover up to ₹12 lakh.'},
        {'q': 'How long is Kerala\'s Certificate of in-principle approval valid?',
         'o': ['6 months', '1 year', '3 years and 6 months', 'Forever'],
         'a': 'C', 'why': 'Section 6 of the Kerala MSME Facilitation Act sets three years and six months.'},
        {'q': 'Which system now handles Kerala local body services, including trade licences, online?',
         'o': ['K-SMART', 'Udyam', 'The GST portal', 'The MCA portal'],
         'a': 'A', 'why': 'K-SMART covers business licences, building permits, certificates and more.'},
        {'q': 'A website says: "Your Udyam certificate will be cancelled. Pay a ₹2,500 renewal fee today." What is it likely to be?',
         'o': ['A real government notice', 'A scam: Udyam registration is free', 'A tax refund', 'A loan offer'],
         'a': 'B', 'why': 'Official Udyam registration has no fee; scammers copy official-looking pages.'},
    ],
    study='the Udyam, K-SMART and K-SWIFT pages, plus the FSSAI and legal metrology pages if you sell food or packed goods (about 1 hour 15 minutes)',
    action='fill in your compliance checklist, register on Udyam if selling, and confirm your local licence with the panchayat or municipality',
)

L3 = lesson(
    9, 3,
    title='Contracts, IP, consumer and digital law basics',
    weeks=(23, 23), hours=4,
    outcome='Use a simple written agreement or terms of sale, protect your name and content, follow consumer and advertising rules, and handle customer data safely.',
    split='1 hour 20 minutes study, 2 hours 40 minutes action',
    core="""
### Contracts: put it in writing

Under the Indian Contract Act, 1872, an agreement is an enforceable contract when there is an offer and an acceptance, something of value exchanged, free consent, parties able to contract and a lawful purpose. A spoken agreement can be a contract, but a written one is much easier to prove and prevents "I thought it included…" arguments. WhatsApp messages can be evidence, but a clear one-page agreement is better for anything above a small amount.

A simple service agreement covers:

1. Who the parties are
2. The scope: what is included, and what is not
3. Price, payment terms and the advance
4. The timeline, and what the customer must provide (photos, access, information)
5. Changes and revisions, and what extra work costs
6. Cancellation and refunds
7. Who owns the work and its content
8. Confidentiality, where needed
9. Limits on your liability, for things outside your control
10. How disputes will be handled

Some agreements need stamp paper under the Kerala Stamp Act. For large or long contracts, ask a lawyer.

### Intellectual property

- **Trademark:** protects your brand name and logo. Search first on IP India's public search; you can file online yourself. The official online filing fee is ₹4,500 per class for individuals, startups and small enterprises, and ₹9,000 for others (check current rules). You may use ™ with a mark you claim, but use ® only after registration.
- **Copyright:** your original writing, photos, designs and videos are protected automatically from the moment you create them; registration is optional. Other people's work is protected in the same way, so don't copy questions from paid guides, photos from Google or music from films. When you use open content, follow its licence. OpenStax's CC BY-NC-SA licence, for example, allows sharing with credit but not commercial use, so you can't sell a copy of an OpenStax book.
- **Designs and patents** protect product shapes and inventions; you are unlikely to need them early on.

### Consumer law

The **Consumer Protection Act, 2019** gives consumers six rights, including protection against hazardous goods and services, the right to information about quality, quantity, purity, standard and price, and the right to seek redress against unfair trade practices. It covers online buying too. In practice:

- Show prices clearly, with what is included.
- Give a receipt for every sale.
- Have a fair refund or replacement policy for defects. "No refunds ever" is not fair if what you sold was faulty.
- Never make false or misleading claims. The Central Consumer Protection Authority can order a misleading advertisement stopped and fine a manufacturer or endorser up to ₹10 lakh, or up to ₹50 lakh for repeat offences. Endorsements must reflect genuine, current experience.
- If you sell online, the **Consumer Protection (E-Commerce) Rules, 2020** apply: show clearly who you are, how to contact you, and your return and refund policy (check current rules).
- Customers can complain to the National Consumer Helpline on 1915. Handle complaints well before they get that far.

### Advertising and influencers

ASCI's guidelines require a clear label, such as #ad or #collaboration, on any post where there is a material connection between the advertiser and the person posting: payment, free products, discounts, gifts, or a family or work relationship.

### Customer data: the DPDP Act

The **Digital Personal Data Protection Act, 2023** and the **DPDP Rules, 2025** (notified on 14 November 2025, with 18 months for phased compliance) set rules for anyone handling people's personal data, such as names and phone numbers. The duties include a clear notice saying why you collect data, consent that can be withdrawn, reasonable security, telling people about data breaches, and acting on requests to access, correct or erase data within 90 days. Penalties under the Act can be very large: up to ₹250 crore for failing to protect data. For a micro-business, the good habits are simple:

- Collect only what you need, such as a name, phone number and delivery address.
- Tell people why, in a line or two on your form or first message.
- Don't add people to groups or broadcast lists without their consent.
- Keep customer lists in your own Google account with two-factor login, and never share or sell them.
- Delete data you no longer need, and whenever someone asks you to.

The Act and Rules are new and being phased in, so check current rules.
""",
    example="""
**Arun's one-page agreement** with each shop says: the setup covers the profile, a catalogue of up to 30 items, 5 quick replies, labels, an away message, the Google profile and 30 minutes of training; it doesn't cover paid ads, photos of more than 30 items or a website. The price is ₹1,800, with ₹900 in advance. Setup is done within 7 days of receiving the product list. One round of changes is free, then ₹300 an hour. The shop gets a full refund within 14 days if it isn't satisfied. The shop owns its catalogue, photos and customer chats. Arun keeps customer data confidential and deletes his copy after setup, and he isn't responsible for changes to WhatsApp's or Google's policies. Both sign, and each keeps a photo.

**Fathima's copyright rule:** every question in PSC Sprint is written by her or her team, from public facts and official syllabuses. She never copies questions from coaching-centre guides or paid apps, and she credits any open-licensed source she quotes.

**Nisha's terms of sale:** prices include delivery within 5 km; custom cakes need a 50% advance; cancellations more than 48 hours ahead get a full refund, later ones lose the advance; a damaged or wrong cake is replaced or refunded in full.
""",
    resources=[
        ('cpa-2019', 'Read section 2(9) on consumer rights and section 2(28) on misleading advertisements (check current rules)', '20 min'),
        ('doca-online', 'Read the summary of protection in online transactions', '10 min'),
        ('tm-fees', 'Check the current trademark filing fee for your category', '5 min'),
        ('dpdp', 'Read the summary of duties and penalties (check current rules)', '15 min'),
        ('os3', 'Section 3.1 Ethical and Legal Issues in Entrepreneurship', '30 min'),
    ],
    steps=[
        'Write your one-page service agreement or terms of sale with the templates below, including a fair refund policy.',
        'Use it with your next customer, or send your terms with your next order confirmation.',
        'Run a trademark public search for your business name in your class, and save a screenshot.',
        'Write a short privacy notice for your order or enquiry form, and add it.',
        'Review your last 10 posts and your product photos. Is everything yours or properly licensed, and is every paid or gifted promotion labelled? Fix anything that isn\'t.',
    ],
    proof='Your agreement or terms (used with a customer), the trademark search screenshot, your privacy notice in place and your notes from the content review.',
    templates=[
        ('one-page service agreement', """
SERVICE AGREEMENT (one page)
Between: [your name / business], [contact]
and: [customer name / business], [contact]
Date: ____

1. Work: ____ (list what is included)
   Not included: ____
2. Price: ₹____  Advance: ₹____ on signing
   Balance: ₹____ on ____
3. Timeline: done within ____ days of receiving ____
4. Changes: ____ free; extra work at ₹____ an hour
5. Cancellation and refund: ____
6. Ownership: the customer owns ____. I may show the
   work as a sample: [ ] yes  [ ] no
7. Confidentiality: I keep the customer's data private
   and delete my copy when the work ends.
8. Liability: I am not responsible for ____ (for
   example, platform rule changes or internet outages).
9. Disputes: we talk first; if unresolved, ____.
Signed: ____ (me)    ____ (customer)
""", ''),
        ('terms of sale and privacy notice', """
TERMS OF SALE (for products)
Prices include: ____ (for example, delivery within 5 km)
Advance: ____% for custom orders
Cancellation: full refund if cancelled more than ____
hours ahead; after that, ____
Damaged or wrong item: tell us within ____ hours with
a photo, and we replace it or refund in full.
Contact: [number], [hours]

PRIVACY NOTICE (on your form or in your first message)
We collect your name, phone number and address only to
take and deliver your order. We never share or sell
them. Ask us any time to see, correct or delete your
details: [number].
""", ''),
    ],
    mistakes=[
        ('No written scope.', 'Most disputes start with different ideas of what was included. Write it down.'),
        ('Copying content.', 'Copied questions, photos or music can lead to takedowns or legal notices, and they destroy trust. Create your own, or follow the licence.'),
        ('Fake testimonials.', 'Invented reviews and endorsements are misleading and can break consumer law. Use real ones, with permission.'),
        ('Collecting more data than you need.', 'Every extra detail is a risk you must protect. Ask only for what you use.'),
        ('"No refunds" on faulty goods.', 'A fair replacement or refund for defects is both what the law expects and good business.'),
    ],
    quiz=[
        {'q': 'Which of these is NOT normally needed for a valid contract?',
         'o': ['An offer and an acceptance', 'Free consent', 'A lawyer\'s signature', 'A lawful purpose'],
         'a': 'C', 'why': 'Lawyers help with complex contracts, but their signature is not a requirement.'},
        {'q': 'When does copyright in your own original writing begin?',
         'o': ['Only after registration', 'Automatically, when you create it', 'After 10 years', 'Only for printed books'],
         'a': 'B', 'why': 'Registration is optional; protection is automatic.'},
        {'q': 'What is the official online fee for a trademark application by an individual or small enterprise, per class? (Check current rules.)',
         'o': ['₹500', '₹4,500', '₹9,000', '₹45,000'],
         'a': 'B', 'why': 'Others pay ₹9,000 per class.'},
        {'q': 'Under the DPDP Rules, how quickly must a business act on a request to access, correct or erase personal data?',
         'o': ['Within 7 days', 'Within 30 days', 'Within 90 days', 'Within a year'],
         'a': 'C', 'why': 'The PIB summary of the Rules gives 90 days.'},
        {'q': 'You give a local YouTuber a free cake to review. What does their post need?',
         'o': ['Nothing', 'A clear disclosure label, such as #ad or #collaboration', 'Your bank details', 'A discount code'],
         'a': 'B', 'why': 'A free product is a material connection under ASCI\'s guidelines.'},
    ],
    study='the Consumer Protection Act sections, the DoCA online summary, the trademark fee page, the DPDP summary and OpenStax 3.1 (about 1 hour 20 minutes)',
    action='write and use an agreement or terms of sale, run a trademark search, add a privacy notice and review your content',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    9,
    title='Legal and compliance',
    weeks=(22, 23), hours=12,
    overview="""
Legal work sounds frightening, but for a micro-business most of it is simple: choose the right structure, register what your activity needs, put agreements in writing, protect your name and treat customers and their data fairly. This module walks through each, using official sources, and ends with a compliance checklist for your own business.

This is general information, not legal advice. Rules differ by activity and change often, so every rule here is marked **check current rules**. Confirm anything important with a lawyer, a CA or the office concerned.
""",
    outcomes=[
        'Compare sole proprietorship, partnership, LLP, OPC and private limited company, and choose one for now',
        'List the registrations and licences your business needs in Kerala, and do the free, simple ones yourself',
        'Use a simple written agreement or terms of sale with a fair refund policy',
        'Protect your name and content, and follow consumer, advertising and data protection basics',
    ],
    lessons=LESSONS,
    project='Compliance checklist and legal pack',
    project_steps=[
        'Your structure decision, with reasons (L01).',
        'Your compliance checklist: every registration and licence, whether it is needed, status, renewal date and official link (L02).',
        'Your one-page agreement or terms of sale, with a refund policy (L03).',
        'The privacy notice on your order or enquiry form (L03).',
        'Your trademark search result for your business name (L03).',
        'Show the checklist to someone who knows the rules (a DIC officer, a CA or an experienced business owner) and note any corrections.',
    ],
    project_proof='The Founder Toolkit/09 Legal folder with these documents, and your filled Compliance tab.',
    rubric=[
        ('Structure', 'Not considered', 'Chosen without comparing', 'Compared, with reasons, and a partner agreement if needed'),
        ('Registrations', 'Unknown', 'Listed, but not checked with official sources', 'Checked with official sources; free ones done; renewal dates set'),
        ('Agreements', 'Nothing in writing', 'WhatsApp messages only', 'A one-page agreement or terms, with a refund policy'),
        ('Name and content', 'Not checked', 'Checked on Google only', 'Trademark search done; only own or licensed content'),
        ('Customer data', 'Collected freely', 'Some care taken', 'Minimum data, a privacy notice, consent and safe storage'),
    ],
    short=[
        'L01: read the comparison table and stay a sole proprietor unless you have a partner or an investor.',
        'L02: do Udyam (if you are selling) and confirm your local licence.',
        'L03: write a five-line refund policy and a three-line privacy notice.',
    ],
    mistakes=[
        ('Registering a company too early.', 'Compliance costs add up; start simple and change when there is a reason.'),
        ('Paying agents for free registrations.', 'Udyam registration is free on the official portal.'),
        ('Borrowing someone else\'s licence or GST number.', 'Never. Get your own registrations.'),
    ],
)
