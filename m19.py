from common import lesson, module, link, rules, xref, table, fence, Q, RULE, ASOF, CHECK
import tools

L1 = lesson(
    19, 1,
    outcome='You can build and use a free CRM in Google Sheets (or LibreOffice) that tracks every lead, property and follow-up, with formulas for overdue actions and conversion.',
    split='15 minutes reading, 45 minutes building and using the CRM',
    core=f"""
**Why a CRM.** Deals in real estate take weeks or months, and leads go cold if you forget them. A simple **CRM (customer relationship management) sheet** is enough for a beginner and works on your phone ({link('gsheets', 'Google Sheets')}) and old laptop ({link('libreoffice', 'LibreOffice Calc')}).

**Your workbook tabs (built through the course):** Comps, Cost, ROI, Loan, Inventory, **Leads**, Network, Income, Log. The Leads tab is your CRM; its header row and formulas are in the templates below.

**Making it work:**
- **Data validation** (drop-down lists) for Stage, Source and Type so the counts work.
- **Conditional formatting:** colour overdue follow-ups red, hot leads green.
- **Filter views:** "today's follow-ups", "hot leads", "properties under offer".
- **Link leads to properties:** use your Inventory IDs in "Properties shown".
- **Daily habit (10 minutes):** check overdue actions, update stages after every call or visit, set a next action date for every open lead.
- **Weekly (in your log):** count leads, visits and deals by source (RE-M11-L02).

**Privacy and security:** keep the sheet private (not "anyone with the link"); use a strong password and two-step verification on your Google account; record consent; delete details of people who ask, and of leads that are closed or lost after a reasonable time; never share client data with others without consent.
""",
    example="""
After two months Sachin's Leads tab has 48 rows. His Dashboard tab shows: new 9, contacted 14, visit booked 4, visited 11, offer 2, agreement 1, closed 4, lost 3. Overdue follow-ups: 6 (red). Conversion: 4 ÷ 48 ≈ **8%**. By source: referrals 15 leads → 3 closed; NoBroker 12 → 1 closed; Facebook 11 → 0 closed.
He changes his week: more time with referral partners, fewer Facebook posts, and a rule that every visited lead gets a follow-up within 48 hours.
""",
    resources=[
        ('gsheets', 'Set up the workbook and install the phone app', '10 minutes'),
        ('libreoffice', 'Optional: install Calc on the laptop for offline work', '15 minutes'),
    ],
    steps=[
        'Create the Leads tab with the header row, drop-down lists for Stage, Source and Type, and the overdue formula.',
        'Enter every current lead (with consent) and set a next action date for each open one.',
        'Build a Dashboard tab with counts by stage and source, and the conversion rate.',
        'Use the CRM daily for two weeks and note how many follow-ups you completed on time.',
    ],
    proof='A CRM screenshot with personal details blurred, the dashboard and your two-week follow-up count.',
    templates=[('CRM sheet', tools.CRM_HEADER + '\n\n' + tools.CRM_FORMULAS), ('Dashboard formulas', """DASHBOARD (tab "Dashboard")
Leads total:         =COUNTA(Leads!A2:A)
By stage (A2 list of stages, B2): =COUNTIF(Leads!J:J,A2)
By source (D2 list of sources, E2): =COUNTIF(Leads!E:E,D2)   closed: =COUNTIFS(Leads!E:E,D2,Leads!J:J,"closed")
Overdue follow-ups:  =COUNTIF(Leads!P:P,"OVERDUE")
Conversion:          =COUNTIF(Leads!J:J,"closed")/COUNTA(Leads!A2:A)
Commission this year: =SUM(Income!E:E)""")],
    mistakes=[
        ('Free-text stages.', 'Use drop-down lists so counts work.'),
        ('Leads without next action dates.', 'Every open lead gets a date.'),
        ('Sharing the sheet publicly.', 'Keep it private and secure.'),
    ],
    fraud="""
**Data theft.** Client lists are valuable to scammers. Don't share login details, don't install unknown "CRM" apps that ask for full access to your contacts, and turn on two-step verification.
""",
    quiz=[
        Q('Why use drop-down lists in the CRM?', 'So stages and sources are spelled the same and counts work', 'For colour', 'It is required by law', 'To slow you down', why='Clean data.'),
        Q('What must every open lead have?', 'A next action date', 'A token advance', 'A photo', 'Nothing', why='Prevents forgotten leads.'),
        Q('Which formula flags overdue follow-ups?', '=IF(AND(L2<>"", L2<TODAY(), J2<>"closed", J2<>"lost"),"OVERDUE","")', '=SUM(L2)', '=MEDIAN(L2)', '=PMT(L2)', why='Compares the date with today.'),
        Q('How should the CRM sheet be shared?', 'Privately, with two-step verification on the account', 'Anyone with the link', 'Posted in groups', 'Printed and left at the office', why='Protect client data.'),
    ],
    study='read the lesson and the CRM formulas',
    action='build the CRM and dashboard and use them daily for two weeks',
)

AI_RULES = [
    ('Facts', 'AI tools can invent laws, rates and section numbers. Check every legal or numeric claim against official sources'),
    ('Privacy', 'Don\'t paste clients\' names, phone numbers, ID numbers or documents into AI tools'),
    ('Honesty', 'AI-written listings must still be true; edit out hype and anything you can\'t verify'),
    ('Disclosure', 'Don\'t use AI to fake reviews, testimonials or photos (no AI-generated "photos" of a real property)'),
    ('Advice', 'AI is not an advocate, surveyor, CA or valuer'),
]

L2 = lesson(
    19, 2,
    outcome='You can use Google Earth, QGIS and AI tools for property research, listings, analysis and communication, safely and honestly.',
    split='15 minutes reading, 45 minutes of practice',
    core=f"""
**Google Earth** ({link('gearth', 'versions')}): web and mobile apps let you view plots, measure distances and areas roughly, see surroundings (rivers, slopes, quarries) and historical imagery (in Earth Pro). Google has said the Earth Pro desktop download will end on 25 June 2027; check what remains available ({CHECK}). Use it to: draw a plot boundary for a virtual tour, measure distance to the road and town, and check flood-prone low land near rivers.

**QGIS** ({link('qgis', 'QGIS')}): free, open-source GIS (GPL). It can run on an older laptop for small projects. Uses for you: overlay your listings (from the Comps sheet as a CSV with coordinates) on a map, add the KSDMA hazard map layers if available ({link('ksdma', 'KSDMA')}), and make a simple price map by locality. Start small: load a CSV of 20 listings with latitude and longitude and colour them by price per cent.

**AI tools** (free tiers of general assistants) can help with:
- **Listings:** turning your notes into clear English and Malayalam drafts (then you edit for accuracy).
- **Analysis:** explaining formulas, checking your spreadsheet logic, summarising your market notes.
- **Communication:** polite follow-up messages, explaining a process to an NRI client in simple words, translating.
- **Learning:** quizzing yourself on this course.

**Rules for AI use:**
{table(['Area', 'Rule'], AI_RULES)}

The {xref('ent', 'ent-m11-l01', 'Entrepreneurship lesson on AI for research and marketing')} and the {xref('smm', 'smm-m13-l01', 'Social Media Marketing lesson on AI for content')} cover more uses.
""",
    example="""
Sachin types his notes for a plot into an AI assistant (no names or numbers): "10 cents, 4 m panchayat road, 2 km Kuttiady, level, well, part slopes at back, price 2.2 lakh per cent". He asks for a 4-line English listing and a Malayalam version. The draft says "prime investment opportunity with excellent appreciation": he deletes it, because he can't promise that, and adds "back 2 cents slope". He then asks the AI to explain how to colour points by value in QGIS, and checks the steps against the QGIS documentation.

In QGIS he loads his 24 listings (CSV with coordinates from Google Maps pins) and colours them by price per cent: the map shows prices dropping sharply beyond 3 km from Kuttiady town, which matches what brokers told him.
""",
    resources=[
        ('qgis', 'Download QGIS (long-term release) and load a CSV of points', '30 minutes'),
        ('gearth', 'Measure a plot and draw its boundary', '15 minutes'),
        ('ksdma', 'Hazard maps to compare with your listings', '10 minutes'),
    ],
    steps=[
        'Add latitude and longitude to 20 listings in your Comps sheet (from map pins you are allowed to use) and export them as CSV.',
        'Load them in QGIS (or Google Earth/My Maps if your laptop can\'t run QGIS) and colour by price per cent.',
        'Use an AI assistant to draft one listing and one client message from your notes (no personal data), then edit and fact-check.',
        'Write your own AI use rules (5 lines) for your business.',
    ],
    proof='The price map screenshot, the AI draft and your edited version side by side, and your AI rules.',
    templates=[('AI prompt starters and rules', """AI PROMPT STARTERS (never include names, phone numbers, ID or document numbers)
Listing: "Turn these facts into a 4-line honest listing in English and simple Malayalam. Do not add claims I didn't give. Facts: ..."
Message: "Write a polite WhatsApp follow-up to a buyer who visited a plot 3 days ago. Ask if they have questions. 3 lines."
Explain: "Explain to an NRI client in simple English what an encumbrance certificate shows and doesn't show."
Check: "Find errors in this formula: ..."
MY AI RULES
1 Check every law, rate and number against official sources.  2 No personal data in AI tools.
3 Edit out hype and unverifiable claims.  4 No fake photos, reviews or testimonials.
5 AI is not my advocate, surveyor, CA or valuer.""")],
    mistakes=[
        ('Trusting AI for legal facts.', 'Verify with official sources.'),
        ('Pasting client documents into AI tools.', 'Never share personal data.'),
        ('Using AI-generated images of properties.', 'Only real photos.'),
    ],
    fraud="""
**AI-faked documents and photos.** AI makes it easier to fake deeds, ECs, certificates and photos. Always get documents from official sources yourself, and visit properties in person.
""",
    quiz=[
        Q('What should you never paste into an AI tool?', 'Clients\' names, phone numbers, IDs or documents', 'Plot size', 'Road width', 'A formula', why='Privacy.'),
        Q('An AI draft says "guaranteed appreciation". You:', 'Delete it; you can\'t promise that', 'Keep it', 'Make it bigger', 'Add more hype', why='Honest listings.'),
        Q('What is QGIS?', 'Free, open-source GIS software', 'A property portal', 'A government office', 'A bank', why='GPL licensed.'),
        Q('Why check AI answers on laws and rates?', 'AI can invent laws, rates and section numbers', 'It is always right', 'Only for fun', 'It is not necessary', why='Verify with official sources.'),
    ],
    study='read the lesson and the AI rules',
    action='make a price map of 20 listings and use AI safely for one listing and one message',
)

LESSONS = [L1, L2]

MODULE = module(
    19,
    overview=f"""
Tech and AI in real estate: a free CRM in Google Sheets or LibreOffice, maps with Google Earth and QGIS, and AI tools for listings, analysis and communication, used safely and honestly.

Everything here works on an Android phone and an old laptop with free tools. The practical milestone is a CRM in daily use with every lead tracked. Everything is {RULE}.
""",
    outcomes=[
        'Build and use a CRM with formulas and a dashboard.',
        'Map listings with Google Earth or QGIS.',
        'Use AI tools for drafts and analysis with clear rules.',
        'Protect client data.',
    ],
    lessons=LESSONS,
    project='your digital toolkit in use',
    project_steps=[
        'CRM with all leads and next actions, used daily for two weeks.',
        'Dashboard with conversion by source.',
        'Price map of 20+ listings.',
        'Your AI rules and two edited AI drafts.',
    ],
    project_proof='Screenshots (personal details blurred), the map and your AI rules.',
    rubric=[
        ('CRM', 'Not used', 'Set up', 'Used daily with next actions and dashboard'),
        ('Maps', 'None', 'Google Earth views', 'Price map of 20+ listings'),
        ('AI', 'Unchecked drafts', 'Edited drafts', 'Edited, fact-checked drafts and written rules'),
        ('Privacy', 'Public sheet or shared data', 'Private sheet', 'Private, 2-step verified, consent recorded'),
    ],
    short=[
        'Build the Leads tab with the overdue formula.',
        'Write your AI rules.',
    ],
    flashcards=[
        ('CRM', 'Track every lead, stage and next action.'),
        ('Overdue flag', 'Next action date before today and not closed or lost.'),
        ('Conversion rate', 'Closed ÷ total leads.'),
        ('QGIS', 'Free, open-source GIS.'),
        ('Google Earth Pro desktop download', 'Ending 25 June 2027 (announced).'),
        ('AI rule 1', 'Verify every law, rate and number.'),
    ],
    mistakes=[
        ('Buying software too early.', 'Free sheets are enough to start.'),
        ('Not updating the CRM.', 'Daily 10-minute habit.'),
        ('Letting AI write unchecked content.', 'You are responsible for every word.'),
    ],
    tools=[
        'CRM sheet and dashboard formulas (RE-M19-L01).',
        'AI prompt starters and rules (RE-M19-L02).',
    ],
    toolkit=[
        'CRM (Leads tab) and Dashboard.',
        'Price map.',
        'AI prompt starters and rules.',
    ],
)
