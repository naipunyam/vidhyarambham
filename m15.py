from common import lesson, module, link, rules, xref, table, fence, Q, RULE, ASOF, CHECK
import tools

SCREEN = [
    ('Identity', 'Government photo ID of each adult occupant (keep only what is needed; mask numbers in copies you share)'),
    ('Work or study', 'Employer or college letter, or business details; recent payslips or bank statement showing income'),
    ('Previous landlord', 'Name and phone; ask about rent payment, care of property and why they left'),
    ('References', 'One or two local references'),
    ('Fit', 'Number of occupants, pets, vehicles, intended use (residential only?)'),
    ('Affordability', 'Rent is usually comfortable if it is no more than about a third of take-home income (a rule of thumb)'),
]

L1 = lesson(
    15, 1,
    outcome='You can screen tenants fairly, prepare and execute a rental agreement correctly, and complete verification steps.',
    split='20 minutes reading, 40 minutes on screening and agreement templates',
    core=f"""
Rentals are the fastest low-capital start: many deals, small commissions (often about one month's rent; RE-M10-L02), repeat clients and a path into property management.

**Before marketing a rental:** owner's mandate; ownership proof (deed or building tax receipt); rent, deposit and terms agreed with the owner; photos with consent.

**Fair tenant screening:**
{table(['Check', 'How'], SCREEN)}
Screen everyone the same way. Don't refuse tenants because of religion, caste, community, marital status or similar personal characteristics: it is unfair, it harms people and it may be unlawful. Decide on facts (income, references, fit with the owner's reasonable rules).

**Rental agreement.** Use your advocate-reviewed template and the rental agreement checklist (RE-M05-L03):
- Term (commonly 11 months), rent, due date, payment by bank or UPI, increase on renewal.
- Deposit: the Kerala Rent Control Act allows an advance of up to one month's rent ({link('rent-act', 'Act, section 8')}); larger deposits are common, so make the terms clear and take an advocate's advice.
- Maintenance, utilities, use, notice, inventory, entry.
- Proper stamp paper; registration if longer than one year ({CHECK}).

**Verification.** Many landlords ask tenants for police verification or inform the local police station. Ask your local police station what they require for tenants in your area (the procedure is unverified in this course; {CHECK}). Keep copies of ID and the agreement safely; share them only with those who need them.

**Move-in:** inventory with photos and meter readings, signed by both; keys; welcome note with rent payment details and the maintenance contact.
""",
    example="""
A 2-bedroom house in Kakkattil, rent ₹9,000. Three enquiries:
- A: bank clerk couple, take-home ₹42,000, previous landlord confirms on-time rent. Rent is 21% of income. ✓
- B: four young men starting a business, no previous landlord, income unclear. The owner wants a family or working couple (a reasonable rule he has set in writing for all applicants); Sachin explains this politely.
- C: a teacher, take-home ₹26,000, two children; rent would be 35% of income. Sachin tells her honestly that it may be tight and shows a cheaper option.
The owner chooses A. The agreement is signed on proper stamp paper; deposit by bank transfer; inventory and meter photos at move-in. Sachin's commission: ₹9,000 from the owner as agreed (the tenant pays nothing).
""",
    pro="""
- **Advocate:** your rental template, unusual terms, disputes and evictions (only through the Rent Control Court).
""",
    resources=[
        ('rent-act', 'Re-read sections 5, 8 and 11', '15 minutes'),
        ('nobroker', 'Look at how rentals are listed and what tenants search for', '10 minutes'),
    ],
    steps=[
        'Write your tenant screening form and the same rules for every applicant.',
        'Ask your local police station what tenant verification they require, and note the answer with the date.',
        'Prepare (or update) your rental agreement template and have an advocate review it.',
        'If you have a rental mandate, screen at least two applicants with the form and record results privately.',
    ],
    proof='The screening form, police station notes, the reviewed template and any screening records (private).',
    templates=[('Tenant screening form', """TENANT SCREENING FORM      Property ______  Date ______
Applicant(s) ______  Occupants: adults ___ children ___  Pets ___  Vehicles ___
ID seen (type only; mask numbers) ______
Work/study: ______  Take-home income ₹ ______  Rent as % of income: =rent/income ______
Previous landlord: ______ (called on ______): rent on time? Y/N  care of property? Y/N  reason for leaving ______
References: 1 ______ 2 ______
Owner's written rules (same for all): ______
Decision: recommend / not recommend   Reason (facts only): ______
Consent to store these details: Y/N   Delete if not selected by ______"""), ('Rental agreement checklist', tools.RENTAL_AGREEMENT)],
    mistakes=[
        ('Unfair or discriminatory screening.', 'Use the same factual checks for everyone.'),
        ('Skipping the inventory.', 'Photos and readings at move-in prevent disputes.'),
        ('Keeping ID copies carelessly.', 'Store safely and delete when no longer needed.'),
    ],
    fraud="""
**Rental scams.** Fake landlords collect deposits for houses they don't own; fake tenants use stolen IDs. Verify ownership, meet in person, call previous landlords and take payments only by bank transfer after signing.
""",
    quiz=[
        Q('How should you screen tenants?', 'With the same factual checks for everyone', 'By religion or caste', 'By appearance', 'Not at all', why='Fair and lawful.'),
        Q('What advance does the Kerala Rent Control Act allow?', 'Up to one month\'s rent', 'Any amount', 'Ten months', 'None', why='Large deposits are common but legally risky.'),
        Q('What should be recorded at move-in?', 'Inventory with photos and meter readings', 'Nothing', 'Only the rent', 'The tenant\'s salary', why='Evidence for the deposit.'),
        Q('Who should you ask about tenant verification requirements?', 'Your local police station', 'A WhatsApp group', 'The neighbour', 'Nobody', why='Procedures vary; check locally.'),
    ],
    study='read the lesson and the screening table',
    action='prepare a screening form and agreement template and find out local verification requirements',
)

L2 = lesson(
    15, 2,
    outcome='You can design and price a rent collection, maintenance and NRI property care service with clear written terms and monthly reports.',
    split='15 minutes reading, 45 minutes designing your service',
    core=f"""
**Property management** turns one-off rentals into monthly income. **NRI property care** is especially valuable in Kozhikode district, where many owners work in the Gulf and houses stand empty or are let.

**Services you can offer** (toolkit service menu below):
- **Rent collection:** the tenant pays directly into the owner's bank account; you track payments and follow up late rent politely. Avoid handling the owner's money yourself; if you must, use a separate account and give receipts.
- **Maintenance:** regular checks, minor repairs through trusted plumbers, electricians and painters, monsoon preparation (gutters, roof leaks, drains), pest and termite control, garden clearing.
- **Empty-house care:** monthly visits, photos and video, airing the house, checking locks, leaks, electricity and encroachment, keeping the compound clean, paying bills with the owner's money.
- **Paperwork:** paying land and building tax online, getting ECs and certificates with the owner's written authority.
- **Tenant changes:** finding new tenants, move-out inspection and deposit settlement.

**Rules that protect you and the owner:**
- A **written service agreement** listing services, fees, payment, reporting and limits.
- **No legal acts** (selling, signing agreements, representing in court) without a registered power of attorney and specific written instructions; refer legal work to an advocate.
- A **monthly report** on the same date: photos, issues, payments, next actions.
- Get quotes before repairs above an agreed limit, and share bills.

**Pricing:** monthly fee per property for care; a percentage of rent (practice varies, for example 5% to 10%) for full management; per-task fees for one-off work. Price to cover your time and travel and to be fair; check what others charge locally.

For running this as a business, see RE-M20 and the {xref('ent', 'ent-m05-l03', 'Entrepreneurship lesson on pricing')}.
""",
    example="""
**Sachin's NRI care service for 3 houses near Kuttiady** (illustrative prices):
- Basic care ₹1,500 a month: monthly visit, 20 photos and a 1-minute video, check for leaks, locks and encroachment.
- Standard ₹2,500: basic plus paying taxes and bills from the owner's money (receipts shared), compound cleaning every two months (cost passed on).
- Monthly report on the 5th via WhatsApp and a Google Drive folder.
Before the monsoon he finds a blocked gutter and a roof leak in one house, sends photos and two quotes; the owner approves ₹6,500 for repairs, paid directly to the worker by the owner.
Income: about ₹5,500 to ₹7,500 a month from 3 owners, growing by referral.
""",
    resources=[
        ('wayanad-tax', 'How to pay land tax online for an owner (with authority)', '5 minutes'),
        ('hc-online', 'Online building tax and other services', '10 minutes'),
    ],
    steps=[
        'Write your service menu with prices for basic care, standard care, full management and one-off tasks.',
        'Write a service agreement outline (services, fees, reporting, limits, termination) and have an advocate review it.',
        'Create a monthly report template.',
        'Offer the service to 3 NRI owners or their families in your network; record responses in the CRM.',
    ],
    proof='The service menu, agreement outline, report template and the CRM record of your offers.',
    templates=[('NRI property care service menu', tools.NRI_CARE), ('Monthly property report', """MONTHLY PROPERTY REPORT     Owner ______  Property ______  Month ______  Visit date ______
1 Photos and video link ______
2 Condition: roof ___ walls ___ doors/locks ___ plumbing ___ electrical ___ compound ___ boundary ___
3 Issues found and action: ______ (quote ₹ ______; owner approval needed? Y/N)
4 Payments made with owner's money: land tax ₹ ___ building tax ₹ ___ electricity ₹ ___ water ₹ ___ (receipts attached)
5 Tenant (if let): rent received ₹ ___ on ___ ; issues ______
6 Neighbourhood: encroachment? road work? other ______
7 Next visit ______   Fee for this month ₹ ______ (invoice no. ______)""")],
    mistakes=[
        ('Mixing owners\' money with your own.', 'Tenants pay owners directly; separate account if unavoidable.'),
        ('Doing legal acts without a POA.', 'Only with a registered POA and written instructions; refer legal work.'),
        ('Irregular reports.', 'Same date every month.'),
    ],
    fraud="""
**Caretaker fraud.** Some caretakers secretly let NRI houses, cut trees, or help encroachers or fake sellers. Your monthly photo reports, transparency and written limits are your selling point: make them strong.
""",
    quiz=[
        Q('How should rent be paid in a managed property?', 'Directly into the owner\'s bank account', 'In cash to the manager', 'To the manager\'s personal account', 'By barter', why='Avoid handling owners\' money.'),
        Q('Can a property manager sign a sale agreement for an NRI owner?', 'Only with a registered POA and specific written instructions, and legal work goes to an advocate', 'Yes, always', 'Yes, verbally', 'Yes, if the tenant agrees', why='Know your limits.'),
        Q('What makes an NRI care service trustworthy?', 'Regular photo reports, receipts and written limits', 'Low price only', 'No reports', 'Secret repairs', why='Transparency.'),
        Q('A roof leak is found. What do you do?', 'Send photos and quotes to the owner for approval', 'Ignore it', 'Repair it at any cost without telling', 'Wait for the monsoon', why='Approval above agreed limits.'),
    ],
    study='read the lesson and the service menu',
    action='design and price your property care service and offer it to 3 owners',
)

LESSONS = [L1, L2]

MODULE = module(
    15,
    overview=f"""
Rentals and property management: fair tenant screening, rental agreements and verification, rent collection, maintenance and NRI property care as a service.

Rentals and NRI care are the most realistic low-capital start around Kuttiady: steady demand, small amounts at risk and repeat clients. Everything is {RULE}.
""",
    outcomes=[
        'Screen tenants fairly and execute agreements correctly.',
        'Handle verification and move-in properly.',
        'Design, price and report on a property management service.',
        'Protect owners\' money and stay within legal limits.',
    ],
    lessons=LESSONS,
    project='a rental and property care service pack',
    project_steps=[
        'Screening form, reviewed rental template and move-in inventory.',
        'Service menu, agreement outline and monthly report template.',
        'Offers to at least 3 owners, tracked in the CRM.',
        'If possible, complete one real rental or one month of property care.',
    ],
    project_proof='The pack, CRM records and any real deal or report (private details masked).',
    rubric=[
        ('Screening', 'Informal or unfair', 'Some checks', 'Same factual checks for all, recorded'),
        ('Agreement', 'Verbal', 'Template', 'Reviewed template, stamped, inventory signed'),
        ('Service design', 'Vague', 'Menu without terms', 'Menu, agreement, report and limits'),
        ('Real work', 'None', 'Offers made', 'A real rental or month of care done'),
    ],
    short=[
        'Write a screening form.',
        'Write your service menu.',
    ],
    flashcards=[
        ('Rental commission (common)', 'About one month\'s rent.'),
        ('Rent Act advance', 'Up to one month\'s rent.'),
        ('Fair screening', 'Same factual checks for everyone.'),
        ('Rent payment', 'Directly to the owner\'s account.'),
        ('Legal acts for owners', 'Only with a registered POA; refer to an advocate.'),
        ('Monthly report', 'Photos, condition, payments, issues, next visit.'),
    ],
    mistakes=[
        ('Overpromising availability.', 'Promise what you can do every month.'),
        ('Underpricing.', 'Cover your time and travel.'),
        ('No written agreement.', 'Always in writing.'),
    ],
    tools=[
        'Tenant screening form and rental agreement checklist (RE-M15-L01).',
        'NRI care service menu and monthly report (RE-M15-L02).',
    ],
    toolkit=[
        'Tenant screening form.',
        'NRI care service menu.',
        'Monthly property report.',
    ],
)
