from common import lesson, module, link, rules, xref, here, table, fence, Q, RULE, ASOF, CHECK, WEEKS
import tools

A2 = WEEKS[(22, 2)][0]

OPTIONS = [
    ('A. First real deal', 'Close a real rental or sale legally, with a signed mandate, proper written agreements, bank payments and the full checklists', 'You have at least one mandated property or a serious client, and an advocate or document writer you can work with'),
    ('B. Investment analysis + business plan', 'A complete analysis of a real property (due diligence on public and permitted information, valuation, full costs, returns, risks) plus a 12-month business plan, with everything ready for a first deal', 'No deal is ready yet, or you are short on time'),
]

L1 = lesson(
    22, 1,
    outcome='You can choose the right capstone (a first real deal, or a complete investment analysis plus business plan), set a realistic five-week plan and prepare every document and tool you will need.',
    split='20 minutes reading, 55 minutes planning',
    core=f"""
The capstone brings the whole course together. Choose **one** option:
{table(['Option', 'What you do', 'Choose it if'], OPTIONS)}

Both options require the **full toolkit** (RE-M22-L03) and the same legal and ethical standards: owner's written consent, honest marketing, advocates for title opinions, licensed professionals for licensed work, bank payments only and no black money.

**Option A: first real deal.** A rental is the most realistic first deal (smaller amounts, faster, fewer legal steps). A sale is fine if you already have a mandate and a serious buyer. Your deal file must include: mandate; listing with approval; CRM records; intake and site-visit checklists; due-diligence checklist (for a sale) or tenant screening (for a rental); token receipt or deposit record (bank transfer); agreement (prepared or reviewed by an advocate or document writer); for a sale, the transaction timeline to registration and handover; invoice and payment record.
**If the deal doesn't close in five weeks** (common: deals take time), submit everything up to the furthest stage reached, plus Option B's business plan. That still counts.

**Option B: investment analysis + business plan.** Choose a real property you can analyse with permission or from public information (or the course's sample case for the legal part): comparables valuation, fair value check, full cost of purchase, rental yield and returns with a downside case, due-diligence checklist with the issues you'd send to an advocate, and a recommendation **framework** (not a recommendation to buy). Add a 12-month business plan: services, rate card, sourcing, marketing, monthly targets, compliance (K-RERA, GST, books) and risks.

**Planning:** list every step, who is involved, what document is needed and a target week. Book time with professionals early. Your weekly schedule stays at 5 to 7 hours (10 hours of capstone work spread over five weeks).
""",
    example="""
Sachin chooses **Option A (rental)**: a 2-bedroom house in Kakkattil whose owner (an NRI in Muscat) has signed a mandate. His five-week plan:
- Week 1: photos, video, bilingual listing approved by the owner; posted on two portals, WhatsApp Business and Facebook Marketplace.
- Week 2: enquiries into the CRM; intake calls; three site visits.
- Week 3: screening of two applicants; the owner chooses; police station guidance followed.
- Week 4: advocate-reviewed agreement; stamp paper; deposit and first rent by bank transfer to the owner; inventory and meter photos.
- Week 5: handover; invoice for one month's rent to the owner; review and testimonial request.
Backup: if it doesn't close, he completes Option B on a 10-cent plot in his market study.
""",
    resources=[
        ('krera', 'Check whether your deal needs K-RERA registration (project units do)', '5 minutes'),
        ('rent-act', 'Rental rules if you choose a rental', '10 minutes'),
        ('sy-stamp', 'Current stamp duty for the deal type', '5 minutes'),
    ],
    steps=[
        'Choose Option A or B and write why in three lines.',
        'Write a five-week plan with steps, people, documents and target weeks.',
        'List the professionals you\'ll need and contact them now.',
        'Prepare your deal file folders from the transaction file template.',
    ],
    proof='Your choice, the five-week plan, the professionals list and the empty (ready) deal file.',
    templates=[('Capstone plan', """CAPSTONE PLAN          Option: A (first deal: rental / sale) / B (analysis + business plan)
Why this option: ______
Week | Steps | People involved | Documents needed | Done
1 | ______ | ______ | ______ | [ ]
2 | ______ | ______ | ______ | [ ]
3 | ______ | ______ | ______ | [ ]
4 | ______ | ______ | ______ | [ ]
5 | ______ | ______ | ______ | [ ]
Professionals: advocate ______ document writer ______ surveyor (if needed) ______ CA (if needed) ______
Legal and ethics check: mandate [ ] honest listing [ ] bank payments only [ ] advocate for title [ ] no licensed work by me [ ]
Backup if the deal stalls: ______""")],
    mistakes=[
        ('Choosing a big sale as the first deal.', 'A rental is the realistic first deal.'),
        ('No backup plan.', 'Option B is the fallback.'),
        ('Booking professionals late.', 'Contact them in week 1.'),
    ],
    fraud="""
**Rushing to finish the course.** Don't let a deadline make you cut corners: no cash, no skipped checks, no listing without consent. A capstone that stops at an honest "the title had a problem" is a pass.
""",
    quiz=[
        Q('Which first deal is usually most realistic?', 'A rental', 'A large plotting project', 'A flip with a loan', 'A builder\'s whole project', why='Smaller and faster.'),
        Q('What if the deal doesn\'t close in five weeks?', 'Submit everything up to the furthest stage plus the business plan', 'Fail the course', 'Close it with cash', 'Skip the checks', why='Honest progress counts.'),
        Q('What does Option B NOT include?', 'A recommendation to buy a specific property', 'Valuation', 'Full costs and returns', 'A business plan', why='No investment recommendations.'),
        Q('When should you contact professionals for the capstone?', 'In week 1', 'On the last day', 'Never', 'After registration', why='They need time.'),
    ],
    study='read the lesson and the two options',
    action='choose your capstone and write a five-week plan',
)

L2 = lesson(
    22, 2,
    outcome='You can carry out your capstone over five weeks, keeping every document, payment and decision legal, written and recorded.',
    split='10 hours over five weeks (about 2 hours a week, inside your 5 to 7 hour schedule)',
    core=f"""
**Weekly rhythm (about 2 hours of capstone work):**
1. Monday: review the plan; update the CRM and deal file.
2. During the week: do the steps (visits, calls, documents).
3. Sunday: weekly log, write what happened, what's blocked and next week's three actions.

**Option A checklist (first deal):**
- [ ] Signed mandate (RE-M10-L02) and owner-approved photos and listing (RE-M12).
- [ ] Listing live on free portals and social channels; every enquiry in the CRM (RE-M19-L01).
- [ ] Intake and site-visit checklists for each visit (RE-M13-L01).
- [ ] **Rental:** tenant screening (RE-M15-L01), advocate-reviewed agreement, correct stamp paper, deposit and rent by bank transfer to the owner, inventory and meter readings, verification as required locally.
- [ ] **Sale:** due-diligence checklist and the buyer's advocate's opinion (RE-M06), conditional token by bank transfer (RE-M13-L02), agreement for sale by an advocate or document writer, cost calculation with current rates, TDS if applicable, registration, mutation and handover (RE-M14).
- [ ] Invoice and commission by bank transfer; Income tab updated (RE-M09-L02).
- [ ] A short deal review: what went well, what you'd change, the client's feedback.

**Option B checklist (analysis + business plan):**
- [ ] Property chosen with permission or from public information; sample case for the legal checks if needed.
- [ ] Comparables (from your 20+ listings) and fair value check (RE-M07).
- [ ] Full cost of purchase with current dated rates (RE-M08-L02).
- [ ] Yield, cash-on-cash and 5-year IRR with a downside case (RE-M08-L02, RE-M18-L01).
- [ ] Due-diligence checklist with issues for an advocate (RE-M06-L03).
- [ ] Risk section: liquidity, legal and market (RE-M18).
- [ ] 12-month business plan: services, rate card, sourcing, marketing, monthly targets, compliance and risks (RE-M20).
- [ ] Ready-for-first-deal pack: mandate, listing, intake, site-visit, token and rental templates printed or saved.

**When something goes wrong** (it often does): a missing heir, a refusing bank, a tenant who backs out. Stop, write it down, get the right professional's advice and decide with the client. Record it in the deal review: handling problems properly is the real skill.
""",
    example="""
Sachin's rental capstone, week by week (summary from his log):
- Week 1: listing live (NoBroker, Facebook Marketplace, WhatsApp Business); 7 enquiries.
- Week 2: 4 intake calls, 3 visits; one couple very interested.
- Week 3: screening done; the owner (by video call) chooses the couple; Sachin asks the local police station about verification and follows its advice.
- Week 4: advocate-reviewed agreement on the right stamp paper; deposit and first month's rent paid by bank transfer to the owner; inventory and meter photos signed.
- Week 5: keys handed over; ₹9,000 invoice to the owner, paid by bank transfer; review on his Google Business Profile.
Deal review: the slowest step was getting the owner's signature from abroad (solved by a scanned signed copy followed by the original by courier, as the advocate advised). Next time: arrange signing logistics in week 1.
""",
    resources=[
        ('krera', 'Project rules if relevant', '5 minutes'),
        ('it-tds', 'TDS if a sale is ₹50 lakh or more', '5 minutes'),
        ('entebhoomi', 'Mutation check after a sale', '5 minutes'),
    ],
    steps=[
        'Follow your five-week plan, with a weekly log entry every Sunday.',
        'Keep every document, message and payment record in the deal file.',
        'Tick the checklist for your option as you go.',
        'At the end, write a one-page deal (or analysis) review.',
    ],
    proof='The complete deal file (or analysis and business plan), five weekly log entries and the one-page review (private details masked in anything shared).',
    templates=[('Capstone weekly log and review', """CAPSTONE WEEKLY LOG   Week ___ of 5
Done this week: ______
Blocked / problems: ______ ; professional consulted: ______
Documents added to the file: ______
Next week's three actions: 1 ______ 2 ______ 3 ______
FINAL REVIEW (one page)
Option and outcome: ______
What went well: ______   What went wrong and how I handled it: ______
Legal and ethics check passed? mandate | consent | written agreements | bank payments | professionals used  Y/N each
Client feedback: ______
What I will do differently in my next deal: ______""")],
    mistakes=[
        ('Missing weekly logs.', 'Write every Sunday; it is your evidence.'),
        ('Doing a professional\'s job to save time.', 'Use the right professional every time.'),
        ('Hiding problems in the review.', 'Problems handled well are the best evidence of skill.'),
    ],
    fraud="""
**Late surprises.** Even in a small rental, a "landlord" may turn out not to be the owner, or a tenant may give fake ID. Your checks protect your first deal as much as your hundredth.
""",
    quiz=[
        Q('How much capstone work is planned each week?', 'About 2 hours inside your 5 to 7 hour schedule', '20 hours', 'None', '10 hours a day', why='10 hours over five weeks.'),
        Q('A rental deposit should be paid:', 'By bank transfer to the owner, with the agreement signed', 'In cash to you', 'In cash to the owner', 'Before the visit', why='Your money rules.'),
        Q('Something goes wrong in week 3. What do you do?', 'Stop, record it, get the right professional\'s advice and decide with the client', 'Hide it', 'Cut corners', 'Abandon the client', why='Handling problems is the skill.'),
        Q('What is the proof for the capstone?', 'The deal file or analysis and plan, five weekly logs and a review', 'A screenshot of the course', 'Nothing', 'A friend\'s opinion', why='Evidence of real work.'),
    ],
    study='read the lesson and your option\'s checklist',
    action='run your capstone for five weeks with weekly logs and a final review',
    extra_tasks=[
        ('week1', 'Capstone week 1: plan steps done and weekly log written', A2, None),
        ('week2', 'Capstone week 2: plan steps done and weekly log written', A2 + 1, None),
        ('week3', 'Capstone week 3: plan steps done and weekly log written', A2 + 2, None),
        ('week4', 'Capstone week 4: plan steps done and weekly log written', A2 + 3, None),
        ('week5', 'Capstone week 5: deal file or analysis complete; one-page review written', A2 + 4, None),
    ],
)

TK_ROWS = [(name, where) for name, _, where in tools.TOOLKIT]

L3 = lesson(
    22, 3,
    outcome='You can assemble your complete Real Estate Toolkit, retake the knowledge quiz to measure progress and set your plan for the next 12 months.',
    split='15 minutes reading, 75 minutes assembling the toolkit and planning (the final retest is on its own page)',
    core=f"""
**1. Assemble your toolkit.** Gather every template and calculator into one folder (and a printed set for site visits). The core items are listed below; the full text of each is on the {here('re-toolkit', 'Toolkit page')}:
{table(['Tool', 'Where you learned it'], TK_ROWS)}
Also include what you built in the modules: the land records comparison, portal guide, legal red-flag checklist, deed reading sheet, title chain and EC sheet, valuation sheets, loan calculator, tax questions, mandate and inventory, interview guide, network tab, photo checklist, token receipt, transaction file, screening form, service menu and monthly report, plotting and construction sheets, strategy and REIT sheets, AI rules, set-up checklist, rate card, fraud red flags and code of ethics.
Check every formula works in both Google Sheets and LibreOffice. Date-stamp every rate (stamp duty, fees, thresholds) and add a "check current rules" note.

**2. Retake the quiz.** Go to the {here('re-final', 'Final retest page')}: take knowledge quiz form B, compare with your baseline, and re-rate your skills.

**3. Plan the next 12 months.** Use the {here('re-next', 'What next page')}. A realistic path:
- **Months 1 to 3:** 2 to 4 rentals, 2 NRI care clients, keep your market study current.
- **Months 4 to 6:** first sale (co-broke if needed); file your return; decide on K-RERA registration.
- **Months 7 to 12:** specialise (for example NRI property care or houses for returning families); build reviews and referrals; consider an assistant.
- **Every quarter:** re-check rates and rules on official sources (stamp duty, fair value, K-RERA, GST, tax) and update your toolkit.
- **Investing:** only after steady service income, an emergency fund and a full analysis (Module 18).

**4. Keep learning:** the Entrepreneurship, Social Media Marketing and Personal Finance courses in this app; the {link('mit-re', 'MIT real estate finance course')} for deeper finance; and the people you met: brokers, document writers and advocates are your best teachers.
""",
    example="""
Sachin's toolkit folder: 15 core templates plus 22 module tools, all dated "rates as of November 2026; check current rules". His retest: knowledge score from 4/12 to 11/12; skills self-rating from 14/50 to 38/50. His 12-month plan targets 30 rentals, 3 sales and 8 NRI care clients, K-RERA registration in month 6, and a quarterly rules check on the first Sunday of January, April, July and October.
""",
    resources=[
        ('gsheets', 'Check every formula in Sheets', '15 minutes'),
        ('libreoffice', 'Check every formula in Calc', '15 minutes'),
        ('krera', 'Re-check agent registration before your plan', '5 minutes'),
    ],
    steps=[
        'Assemble the full toolkit folder and test every formula in Sheets and LibreOffice.',
        'Date-stamp every rate and add "check current rules".',
        'Take the final retest and compare with your baseline.',
        'Write your 12-month plan with quarterly rules checks.',
    ],
    proof='The toolkit folder index, the tested formulas, your retest comparison and your 12-month plan.',
    templates=[('Toolkit index and 12-month plan', """TOOLKIT INDEX    rates as of ______; check current rules
Core: Comps | Cost | ROI | EMI | Due diligence | Document checklist | Mandate | Intake | Site visit | Listing | CRM | Timeline | Rental agreement | NRI care | Weekly log
Module tools: ______ (list)
Formula test: Sheets [ ] LibreOffice [ ]
12-MONTH PLAN
Quarter | Rentals | Sales | NRI clients | Learning | Compliance (K-RERA / ITR / GST / rules check) | Income target
Q1 | ___ | ___ | ___ | ______ | rules check on ______ | ₹ ___
Q2 | ...
Q3 | ...
Q4 | ...""")],
    mistakes=[
        ('Letting the toolkit go stale.', 'Quarterly rules check.'),
        ('Skipping the retest.', 'It shows your progress and gaps.'),
        ('A plan without numbers.', 'Set targets you can track in the CRM.'),
    ],
    fraud="""
**Outdated rules as a risk.** Stamp duty, fair values, tax sections, thresholds and portals change. Using an old rate can cost a client money or break the law. Your quarterly check is part of protecting clients.
""",
    quiz=[
        Q('How often should you re-check rates and rules?', 'Every quarter, and before every deal', 'Never', 'Every 10 years', 'Only when a client complains', why='Rules change.'),
        Q('What should every rate in your toolkit carry?', 'A date and a "check current rules" note', 'Nothing', 'A guarantee', 'The broker\'s signature', why='Shows when it was verified.'),
        Q('When should you consider investing in property yourself?', 'After steady service income, an emergency fund and a full analysis', 'Right now', 'With borrowed money first', 'Never think about it', why='Services first.'),
        Q('Where do you take the final knowledge retest?', 'The Final retest page', 'Nowhere', 'The glossary', 'The start page', why='Form B compares with the baseline.'),
    ],
    study='read the lesson and gather your module tools',
    action='assemble and test the full toolkit, take the retest and write your 12-month plan',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    22,
    overview=f"""
The capstone: close a first real deal legally (a rental or a sale) with proper written agreements, **or** complete a full investment analysis and a business plan, together with your complete Real Estate Toolkit. Then retake the quiz and plan the next 12 months.

Both options use the same standards: written consent, honest marketing, professionals for licensed work, bank payments only and no black money. A deal that stops honestly at a problem is still a pass. Everything is {RULE}.
""",
    outcomes=[
        'Plan and run a five-week capstone.',
        'Close a first deal legally, or produce a full analysis and business plan.',
        'Assemble and test the complete toolkit.',
        'Measure progress and plan the next 12 months.',
    ],
    lessons=LESSONS,
    project='your capstone: first deal or analysis + business plan, plus the full toolkit',
    project_steps=[
        'Choose and plan (RE-M22-L01).',
        'Run it for five weeks with logs (RE-M22-L02).',
        'Assemble the toolkit, retest and plan (RE-M22-L03).',
        'Optional: show your deal file or plan to a broker or advocate you interviewed and note their feedback.',
    ],
    project_proof='The deal file or analysis and plan, five logs, the review, the toolkit index and the retest comparison.',
    rubric=[
        ('Legal and ethical', 'Cash, no consent or licensed work done by you', 'Mostly compliant', 'Written consent, agreements, bank payments, professionals at every step'),
        ('Completeness', 'Missing key documents', 'Most documents', 'Every checklist and record in the file'),
        ('Numbers', 'Guesses', 'Some calculations', 'Dated rates, full costs and returns with a downside case'),
        ('Reflection', 'None', 'Brief', 'Honest review with problems, fixes and next steps'),
        ('Toolkit', 'Scattered', 'Mostly gathered', 'Complete, tested in Sheets and LibreOffice, dated'),
    ],
    short=[
        'Do Option B on one property and a one-page plan.',
        'Assemble the core 15 tools.',
    ],
    flashcards=[
        ('Capstone options', 'A: first real deal; B: analysis + business plan.'),
        ('Most realistic first deal', 'A rental.'),
        ('If the deal stalls', 'Submit up to the furthest stage plus a plan.'),
        ('Capstone time', '10 hours over five weeks.'),
        ('Toolkit rule', 'Every rate dated; "check current rules".'),
        ('Quarterly habit', 'Re-check rules on official sources.'),
    ],
    mistakes=[
        ('Cutting corners to finish.', 'Standards over speed.'),
        ('No records.', 'The file is your proof.'),
        ('Stopping after the course.', 'Follow your 12-month plan.'),
    ],
    tools=[
        'Capstone plan (RE-M22-L01).',
        'Capstone weekly log and review (RE-M22-L02).',
        'Toolkit index and 12-month plan (RE-M22-L03).',
    ],
    toolkit=[
        'The complete toolkit folder with index.',
        'Your deal file or analysis and business plan.',
    ],
)
