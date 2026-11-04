from common import lesson, module, link, rules, xref, table, fence, Q, RULE, ASOF, CHECK

STRUCT = [
    ('Sole proprietorship', 'You alone; simplest; no separate registration of the business itself', 'Unlimited personal liability; good to start'),
    ('Partnership firm', 'Two or more partners with a written (preferably registered) partnership deed', 'Shared liability; disputes common without a clear deed'),
    ('LLP', 'Limited liability partnership registered with the Ministry of Corporate Affairs', 'Limited liability; annual filings and costs'),
    ('Private limited company', 'Separate company; directors and shareholders', 'Most compliance; for larger agencies or development'),
]

REGS = [
    ('PAN and bank account', 'A separate bank account (savings at first, current account later) for business income and expenses', 'From day 1'),
    ('Income tax returns', 'File every year, even with small income; needed for K-RERA registration and loans', 'From year 1'),
    ('K-RERA agent registration', 'Before handling sales in registered projects (RE-M10-L01)', 'When you start project sales'),
    ('Udyam registration', 'Free online MSME registration; useful for some schemes and bank relationships', 'Optional, early'),
    ('Local body trade licence / Shops and Establishments registration', 'If you open an office or shop; requirements vary', 'When you have premises; ask your panchayat'),
    ('GST registration', 'Required above ₹20 lakh service turnover, or voluntarily (RE-M09-L02)', 'When turnover approaches the limit'),
]

L1 = lesson(
    20, 1,
    outcome='You can choose a business structure, list the registrations you need and when, and keep simple, accurate books for a real estate service business.',
    split='20 minutes reading, 40 minutes on your set-up checklist and books',
    core=f"""
**Choosing a structure:**
{table(['Structure', 'What it is', 'Notes'], STRUCT)}
For a beginner working alone, a **sole proprietorship** is usually enough. Move to a partnership or LLP when you work with partners, and only with an advocate-drafted agreement. The {xref('ent', 'ent-m09-l01', 'Entrepreneurship lesson on business structures')} goes into detail.

**Registrations and when you need them** ({CHECK} with your panchayat, a CA and the {xref('ent', 'ent-m09-l02', 'Entrepreneurship lesson on registrations in Kerala')}):
{table(['Item', 'What it is', 'When'], REGS)}

**Bookkeeping (simple and accurate):**
- One **Income** tab (RE-M09-L02) and one **Expenses** tab; every entry with date, client or vendor, amount, mode and receipt or invoice number.
- Number your invoices (RE-2026-001, RE-2026-002…).
- Keep receipts as photos in a folder by month.
- Reconcile with the bank statement monthly.
- Never mix owners' or clients' money with yours; if you hold any client money, use a separate account and record it separately.
- Monthly profit: income − expenses. Set aside money for tax.
See the {xref('ent', 'ent-m08-l01', 'Entrepreneurship lesson on bookkeeping and cash flow')}.

**Insurance and safety:** consider personal accident cover and phone and data backups. Keep copies of every mandate and agreement.

**Your business name and identity:** a clear name, a professional email (free), a WhatsApp Business profile, a Google Business Profile and simple visiting cards that show your K-RERA number once registered, and your money rules (RE-M04-L05).
""",
    example="""
Sachin's set-up (month 1):
- Sole proprietor; trade name "Sachin Property Services, Kuttiady".
- PAN (has one); a separate savings account for business; files his income tax return for the year.
- Udyam registration (free) done online.
- No office yet, so no trade licence needed (he checked with the panchayat; he works from home and meets clients on site).
- Books: Income and Expenses tabs, invoice numbering RE-2026-001, receipts folder by month; monthly reconciliation on the 1st.
- GST: not needed (turnover far below ₹20 lakh); he notes the threshold in his calendar to review every quarter.
""",
    pro="""
- **CA:** structure choice, tax returns and GST.
- **Advocate:** partnership deeds and business agreements.
""",
    resources=[
        ('krera', 'Agent registration requirements, to plan your documents', '10 minutes'),
        ('rp-gst', 'GST thresholds for services', '10 minutes'),
        ('gsheets', 'Set up the Income and Expenses tabs', '10 minutes'),
    ],
    steps=[
        'Choose your structure and write why in three lines.',
        'Make your set-up checklist with each registration, whether you need it now, and the date you checked (ask your panchayat about trade licences).',
        'Open (or designate) a separate bank account for business and set up Income and Expenses tabs with invoice numbering.',
        'Enter all income and expenses so far and do your first monthly reconciliation.',
    ],
    proof='Your structure choice, the dated set-up checklist, and screenshots of the Income and Expenses tabs (amounts can be blurred).',
    templates=[('Business set-up checklist', """BUSINESS SET-UP CHECKLIST    checked on ______
Structure: sole proprietor / partnership / LLP / company   Reason: ______
PAN [ ]  Separate bank account [ ]  ITR filed for FY ______ [ ]
Udyam registration [ ] (optional)   Trade licence / Shops and Establishments: needed? Y/N (asked ______ on ______)
K-RERA agent registration: planned by ______ (RE-M10-L01)
GST: turnover this year ₹ ______ ; review on ______ ; register when near ₹20 lakh (CA advice)
Books: Income tab [ ] Expenses tab [ ] invoice numbering [ ] receipts folder [ ] monthly reconciliation date ___
Identity: name ______ email ______ WhatsApp Business [ ] GBP [ ] cards with K-RERA no. and money rules [ ]""")],
    mistakes=[
        ('Starting a company too early.', 'Start simple; add structure when needed.'),
        ('Not filing returns.', 'File every year; you\'ll need them.'),
        ('Mixing personal and business money.', 'Separate account and books.'),
    ],
    fraud="""
**Fake registration agents.** Some agents charge for "mandatory" registrations that are free (such as Udyam) or not required. Use official portals, ask your CA and check the panchayat's own requirements.
""",
    quiz=[
        Q('Which structure is usually enough for a beginner working alone?', 'Sole proprietorship', 'Private limited company', 'LLP', 'Trust', why='Simplest to start.'),
        Q('Why file income tax returns from year 1?', 'They are needed for K-RERA registration and loans, and build a record', 'They are optional forever', 'They cost nothing to skip', 'Only for NRIs', why='Plan ahead.'),
        Q('When is GST registration required for services?', 'When turnover exceeds ₹20 lakh a year (or voluntarily)', 'From the first rupee', 'Never', 'Only for rentals', why='Check current rules.'),
        Q('What should you do with clients\' money?', 'Keep it separate from yours and record it separately', 'Use it for expenses', 'Mix it in your account', 'Spend it and repay later', why='Trust and law.'),
    ],
    study='read the lesson and the registrations table',
    action='choose your structure, make a dated set-up checklist and set up your books',
)

PRICES = [
    ('Sale brokerage', '1% to 2% of price (local practice varies)', 'Written in the mandate; due on registration'),
    ('Rental brokerage', 'About one month\'s rent (sometimes split)', 'Due on signing'),
    ('NRI property care', 'Monthly fee per property', 'Service agreement; monthly invoice'),
    ('Full rental management', 'Percentage of rent (for example 5% to 10%)', 'Service agreement'),
    ('Listing and marketing package (for owners or other brokers)', 'Fixed fee per property (photos, video, copy, posting)', 'Paid in advance or on delivery'),
    ('Document collection', 'Fixed fee per task (EC, certificates, tax payment) with written authority', 'Plus government fees at cost'),
]

L2 = lesson(
    20, 2,
    outcome='You can price your services, set up fair partnerships and co-broking, and plan how to grow from a solo broker into a small agency.',
    split='20 minutes reading, 40 minutes on pricing and a 12-month plan',
    core=f"""
**Pricing your services.** Check local practice in your broker interviews, then price to cover your time, travel and risk:
{table(['Service', 'Common basis', 'How to agree'], PRICES)}
Write prices on a simple one-page rate card. Be consistent: discounting heavily for one client undermines trust with others. For pricing method, see the {xref('ent', 'ent-m05-l03', 'Entrepreneurship lesson on setting your price')}.

**Partnerships and co-broking:**
- **Co-broking with other brokers:** agree in writing who has the mandate, who brings the client, and the split (often 50:50). Tell clients if more than one broker is involved.
- **Referral relationships** with document writers, advocates, engineers, banks and contractors: refer clients to good professionals because they're good. **Don't take or pay secret referral commissions** that clients don't know about; if any referral fee exists, disclose it in writing and make sure it doesn't affect your advice.
- **Partners in your business:** a written agreement (advocate-drafted) covering roles, money, decisions, exit and disputes.

**Growing into an agency:**
1. **Solo (year 1):** rentals, resale, NRI care; build reputation, systems and savings.
2. **Specialise (year 2):** become known for one thing (for example NRI property care in Kuttiady–Nadapuram, or houses for returning Gulf families).
3. **First help:** a part-time assistant for photos and site visits, paid fairly, trained on your checklists and ethics.
4. **Systems:** CRM, checklists, templates, a website or GBP with reviews; written procedures so others can follow them.
5. **Agency:** K-RERA registration for the firm if needed, an office, a few agents, a clear commission split and strict compliance.
Grow only when your systems work and cash flow is steady. See the {xref('ent', 'ent-m12-l03', 'Entrepreneurship lesson on hiring, delegating and scaling')}.

**Simple projections.** Estimate deals per month by type × average commission; subtract expenses; compare with your time. Real estate income is uneven: keep 3 to 6 months of expenses as a buffer.
""",
    example="""
**Sachin's rate card and a 12-month plan (illustrative):**
- Rentals: one month's rent from the owner. Sales: 2% from the seller. NRI care: ₹1,500 basic, ₹2,500 standard. Listing package for other brokers: ₹1,500 per property.
- Year 1 target: 2 rentals a month (₹18,000), one sale every two months (avg ₹40,000 → ₹20,000 a month), 5 NRI care clients (₹10,000) = about ₹48,000 a month by month 12, from about ₹8,000 in month 3.
- Expenses: about ₹5,000 a month (phone, travel, portal upgrades).
- Co-broking agreement with the Kakkattil broker: 50:50 split, written.
- Month 9: hire a part-time college student for photo shoots at ₹300 per property.
These are targets, not promises; he reviews them monthly against the CRM.
""",
    resources=[
        ('gbp', 'Use reviews and service areas to support growth', '10 minutes'),
        ('krera', 'Requirements for registering a firm as an agent', '10 minutes'),
    ],
    steps=[
        'Write your one-page rate card using local practice from your interviews.',
        'Draft a co-broking agreement outline and a referral policy (no secret commissions).',
        'Build a 12-month plan with monthly targets, expenses and growth steps.',
        'Share the rate card with one broker or mentor and note their feedback.',
    ],
    proof='The rate card, co-broking outline and referral policy, the 12-month plan and the feedback.',
    templates=[('Rate card and 12-month plan', """RATE CARD   (name, area, K-RERA no. if registered, money rules)
Sale brokerage ___% (seller) | Rental ___ month's rent | NRI care basic ₹___ standard ₹___ | Full management ___% of rent
Listing package ₹___ | Document collection ₹___ per task + government fees
All payments by bank transfer/UPI with invoice. No cash deals, no undervaluation.
CO-BROKING (written): mandate holder ______ | client introducer ______ | split ___:___ | disclosed to clients Y/N
REFERRAL POLICY: I refer to professionals for quality only; any referral fee is disclosed in writing.
12-MONTH PLAN
Month | Rentals | Sales | NRI clients | Income ₹ | Expenses ₹ | Net ₹ | Growth step
Buffer target: ___ months of expenses""")],
    mistakes=[
        ('Undercharging to win clients.', 'Price fairly and consistently.'),
        ('Secret referral commissions.', 'Disclose any referral fee in writing.'),
        ('Hiring before systems work.', 'Systems and cash flow first.'),
    ],
    fraud="""
**Franchise and "agency in a box" offers.** Some companies sell expensive franchises or leads packages to new brokers with promises of guaranteed deals. Check reviews, ask existing franchisees, and never pay large fees for promises.
""",
    quiz=[
        Q('What should a co-broking arrangement include?', 'Who holds the mandate, who brings the client, and the split, in writing', 'Nothing', 'A verbal promise', 'The client\'s salary', why='Avoids disputes.'),
        Q('Is it acceptable to take a secret commission from an advocate you refer clients to?', 'No; any referral fee must be disclosed and must not affect advice', 'Yes', 'Yes, if small', 'Only on Sundays', why='Conflicts of interest.'),
        Q('When should you hire help?', 'When systems work and cash flow is steady', 'On day 1', 'Never', 'Before your first deal', why='Grow carefully.'),
        Q('Why keep a buffer of 3 to 6 months of expenses?', 'Real estate income is uneven', 'It is required by law', 'Banks demand it', 'It is not needed', why='Deals come irregularly.'),
    ],
    study='read the lesson and the pricing table',
    action='write your rate card, partnership policies and a 12-month plan',
)

LESSONS = [L1, L2]

MODULE = module(
    20,
    overview=f"""
Setting up your business: structure, registrations, GST, bookkeeping, pricing, partnerships, co-broking and growing from a solo broker into a small agency.

This module turns your skills into a legal, organised business. It builds on the Entrepreneurship course rather than repeating it. Everything is {RULE}.
""",
    outcomes=[
        'Choose a structure and plan registrations.',
        'Keep simple, accurate books.',
        'Price services and set fair partnerships.',
        'Plan 12 months of growth.',
    ],
    lessons=LESSONS,
    project='your business set-up and 12-month plan',
    project_steps=[
        'Set-up checklist with dates.',
        'Income and Expenses tabs in use.',
        'Rate card, co-broking outline and referral policy.',
        '12-month plan with targets and growth steps.',
    ],
    project_proof='The four items.',
    rubric=[
        ('Set-up', 'Not started', 'Some items', 'Dated checklist with each item decided'),
        ('Books', 'None', 'Partial', 'Income, expenses, invoices and monthly reconciliation'),
        ('Pricing', 'Unclear', 'Rates known', 'Rate card based on local evidence'),
        ('Growth', 'No plan', 'Targets only', 'Monthly targets, expenses, buffer and growth steps'),
    ],
    short=[
        'Choose a structure and open a separate account.',
        'Write your rate card.',
    ],
    flashcards=[
        ('Beginner structure', 'Sole proprietorship.'),
        ('Separate account', 'Business money apart from personal and client money.'),
        ('Invoice numbering', 'RE-2026-001, 002, ...'),
        ('Co-broking', 'Written split, disclosed to clients.'),
        ('Referral fees', 'Disclosed in writing; never affect advice.'),
        ('Buffer', '3 to 6 months of expenses.'),
    ],
    mistakes=[
        ('Ignoring the paperwork side of the business.', 'Set it up early.'),
        ('Growth before quality.', 'Reputation first.'),
        ('No review of targets.', 'Review monthly against the CRM.'),
    ],
    tools=[
        'Business set-up checklist (RE-M20-L01).',
        'Rate card and 12-month plan (RE-M20-L02).',
    ],
    toolkit=[
        'Business set-up checklist.',
        'Rate card.',
        '12-month plan.',
    ],
)
