"""Shared helpers and the resource registry for the entrepreneurship course.

Every link used in the course lives in R, with the status found when it was
checked. Lessons refer to links by key, so the sources page is generated from
exactly the links the course uses.
"""

VDATE = '2026-10-24'

STATUS = {
    'v': f'verified {VDATE}',
    'vr': f'verified {VDATE}; check current rules',
    'u': 'unverified: the site blocks automated checks',
}


def _r(title, url, s='v', group='Other'):
    return {'title': title, 'url': url, 's': s, 'group': group}


R = {
    # Y Combinator
    'yc-ss': _r('Y Combinator Startup School (free course)', 'https://www.startupschool.org/', 'v', 'Courses and talks'),
    'yc-playlist': ('YC Startup School videos (YouTube playlist)', 'https://www.youtube.com/playlist?list=PLQ-uHSnFig5M9fW16o2l35jrfdsxGknNB'),
    'yc-should': _r('YC: "Should You Start A Startup?" (Harj Taggar)', 'https://www.youtube.com/watch?v=BUE-icVYRFU', 'v', 'Courses and talks'),
    'yc-ideas': _r('YC: "How to Get and Evaluate Startup Ideas" (Jared Friedman)', 'https://www.youtube.com/watch?v=Th8JoIan4dg', 'v', 'Courses and talks'),
    'yc-users': _r('YC: "How To Talk To Users" (Gustaf Alströmer)', 'https://www.youtube.com/watch?v=z1iF1c8w5Lg', 'v', 'Courses and talks'),
    'yc-mvp': _r('YC: "How to Build An MVP" (Michael Seibel)', 'https://www.youtube.com/watch?v=QRZ_l7cVzzU', 'v', 'Courses and talks'),
    'yc-pricing': _r('YC: "Startup Business Models and Pricing" (Aaron Epstein)', 'https://www.youtube.com/watch?v=oWZbWzAyHAE', 'v', 'Courses and talks'),
    'yc-first': _r('YC: "How to Get Your First Customers" (Gustaf Alströmer)', 'https://www.youtube.com/watch?v=hyYCn_kAngI', 'v', 'Courses and talks'),
    'yc-launch': _r('YC: "The Best Way To Launch Your Startup" (Kat Mañalac)', 'https://www.youtube.com/watch?v=u36A-YTxiOw', 'v', 'Courses and talks'),
    'yc-fund': _r('YC: "How Startup Fundraising Works" (Brad Flora)', 'https://www.youtube.com/watch?v=zBUhQPPS9AY', 'v', 'Courses and talks'),
    'yc-cofound': _r('YC: "Keys To Successful Co-Founder Relationships"', 'https://www.youtube.com/watch?v=A4SLDQDXdp0', 'v', 'Courses and talks'),
    'yc-seed': _r('YC Startup Library: "A guide to seed fundraising"', 'https://www.ycombinator.com/library/4A-a-guide-to-seed-fundraising', 'v', 'Courses and talks'),
    # Steve Blank, MIT, Lean
    'blank-udacity': _r('Steve Blank: "How to Build a Startup" (free Udacity course)', 'https://www.udacity.com/course/how-to-build-a-startup--ep245', 'v', 'Courses and talks'),
    'blank-tools': _r('Steve Blank: Startup Tools page', 'https://steveblank.com/tools-and-blogs-for-entrepreneurs/', 'v', 'Courses and talks'),
    'mit-390': _r('MIT OpenCourseWare 15.390 New Enterprises (2013): video tutorials', 'https://ocw.mit.edu/courses/15-390-new-enterprises-spring-2013/video_galleries/video-tutorials/', 'v', 'Courses and talks'),
    'mit-s21': _r('MIT OpenCourseWare 15.S21 Nuts and Bolts of Business Plans (2014)', 'https://ocw.mit.edu/courses/15-s21-nuts-and-bolts-of-business-plans-january-iap-2014/', 'v', 'Courses and talks'),
    'lean-principles': _r('The Lean Startup: the five principles', 'https://theleanstartup.com/principles', 'v', 'Frameworks and articles'),
    'jtbd': _r('Christensen Institute: Jobs to Be Done', 'https://www.christenseninstitute.org/theory/jobs-to-be-done/', 'v', 'Frameworks and articles'),
    'bmc': _r('Strategyzer: The Business Model Canvas (free PDF)', 'https://www.strategyzer.com/library/the-business-model-canvas', 'v', 'Frameworks and articles'),
    'vpc': _r('Strategyzer: The Value Proposition Canvas (free PDF)', 'https://www.strategyzer.com/library/the-value-proposition-canvas', 'v', 'Frameworks and articles'),
    'strategyzer-use': _r('Strategyzer: how you may use its canvases', 'https://strategyzer.com/legal/usage-of-our-tools', 'v', 'Frameworks and articles'),
    'leancanvas': _r('LEANSpark: Lean Canvas (free tool, sign-up needed)', 'https://leanspark.ai/leancanvas', 'v', 'Frameworks and articles'),
    'a16z': _r('a16z: "16 Startup Metrics"', 'https://a16z.com/16-startup-metrics/', 'v', 'Frameworks and articles'),
    'altman': _r('Sam Altman: Startup Playbook', 'https://playbook.samaltman.com/', 'v', 'Frameworks and articles'),
    # Paul Graham
    'pg-ideas': _r('Paul Graham: "How to Get Startup Ideas"', 'https://paulgraham.com/startupideas.html', 'v', 'Frameworks and articles'),
    'pg-ds': _r('Paul Graham: "Do Things That Don\'t Scale"', 'https://paulgraham.com/ds.html', 'v', 'Frameworks and articles'),
    'pg-growth': _r('Paul Graham: "Startup = Growth"', 'https://paulgraham.com/growth.html', 'v', 'Frameworks and articles'),
    'pg-notnot': _r('Paul Graham: "Why to Not Not Start a Startup"', 'https://paulgraham.com/notnot.html', 'v', 'Frameworks and articles'),
    'pg-schlep': _r('Paul Graham: "Schlep Blindness"', 'https://paulgraham.com/schlep.html', 'v', 'Frameworks and articles'),
    'pg-aord': _r('Paul Graham: "Default Alive or Default Dead?"', 'https://paulgraham.com/aord.html', 'v', 'Frameworks and articles'),
    'pg-ramen': _r('Paul Graham: "Ramen Profitable"', 'https://paulgraham.com/ramenprofitable.html', 'v', 'Frameworks and articles'),
    'pg-13': _r('Paul Graham: "Startups in 13 Sentences"', 'https://paulgraham.com/13sentences.html', 'v', 'Frameworks and articles'),
    # Free tools
    'gsheets': _r('Google Sheets help: How to use Google Sheets', 'https://support.google.com/docs/answer/6000292', 'v', 'Free tools'),
    'gforms': _r('Google Forms help: How to use Google Forms', 'https://support.google.com/docs/answer/6281888', 'v', 'Free tools'),
    'gsites': _r('Google Sites help: create and publish a site', 'https://support.google.com/sites/answer/6372878', 'v', 'Free tools'),
    'appsscript': _r('Google Apps Script', 'https://developers.google.com/apps-script', 'v', 'Free tools'),
    'gtrends': _r('Google Trends', 'https://trends.google.com/trends/', 'v', 'Free tools'),
    'gbp-free': _r('Google Business Profile help: a free Business Profile', 'https://support.google.com/business/answer/7039811', 'v', 'Free tools'),
    'gbp-rank': _r('Google Business Profile help: improve your local ranking', 'https://support.google.com/business/answer/7091?hl=en', 'v', 'Free tools'),
    'skillshop': _r('Google Skillshop (free training)', 'https://skillshop.withgoogle.com/', 'v', 'Free tools'),
    'wa-business': _r('WhatsApp Business app (Google Play listing)', 'https://play.google.com/store/apps/details?id=com.whatsapp.w4b', 'v', 'Free tools'),
    'ig-pro': _r('Instagram help: set up a professional account', 'https://help.instagram.com/502981923235522', 'v', 'Free tools'),
    'yt-creators': _r('YouTube Creators (free guides)', 'https://www.youtube.com/creators/', 'v', 'Free tools'),
    'hubspot-content': _r('HubSpot Academy: Content Marketing (free course)', 'https://academy.hubspot.com/courses/content-marketing', 'v', 'Courses and talks'),
    'hubspot-sales': _r('HubSpot: Inbound Sales training (free)', 'https://www.hubspot.com/sales/sales-training', 'v', 'Courses and talks'),
    'canva-license': _r('Canva Free Media License', 'https://www.canva.com/policies/free-media', 'v', 'Free tools'),
    'libreoffice': _r('LibreOffice (free, open-source office suite)', 'https://www.libreoffice.org/', 'v', 'Free tools'),
    'gnucash': _r('GnuCash (free, open-source accounting)', 'https://www.gnucash.org/', 'v', 'Free tools'),
    'gnucash-docs': _r('GnuCash documentation', 'https://www.gnucash.org/docs.phtml', 'v', 'Free tools'),
    'razorpay': _r('Razorpay pricing', 'https://razorpay.com/pricing/', 'vr', 'Free tools'),
    'indiapost': _r('India Post', 'https://www.indiapost.gov.in/', 'v', 'Free tools'),
    'gemini-plans': _r('Google Gemini plans (has a free plan)', 'https://gemini.google/subscriptions/', 'vr', 'AI tools'),
    'claude-plans': _r('Claude plans (has a free plan)', 'https://claude.com/pricing', 'vr', 'AI tools'),
    'chatgpt-plans': _r('ChatGPT plans (has a free plan)', 'https://chatgpt.com/pricing', 'vr', 'AI tools'),
    'gemini-notebook': _r('Gemini Notebook (formerly NotebookLM)', 'https://notebook.google/', 'v', 'AI tools'),
    'gemini-api-terms': _r('Gemini API terms: how free-tier data is used', 'https://ai.google.dev/gemini-api/terms', 'v', 'AI tools'),
    'elements-ai': _r('Elements of AI (free course, University of Helsinki and MinnaLearn)', 'https://www.elementsofai.com/', 'v', 'AI tools'),
    'ncfe': _r('NCFE: National Centre for Financial Education (free e-learning)', 'https://ncfe.org.in/', 'v', 'Money'),
    # India: tax, registration, schemes
    'udyam': _r('Udyam Registration portal (free)', 'https://udyamregistration.gov.in/', 'vr', 'Government of India'),
    'gst': _r('GST portal', 'https://www.gst.gov.in/', 'vr', 'Government of India'),
    'gst-council-32': _r('GST Council, 32nd meeting: thresholds and composition scheme (PDF)', 'https://gstcouncil.gov.in/sites/default/files/2024-10/32nd_gst_press_information_bureau.pdf', 'vr', 'Government of India'),
    'gst-notif-10': _r('Notification 10/2019-Central Tax: ₹40 lakh threshold for goods (PDF)', 'https://www.gstcouncil.gov.in/sites/default/files/2024-05/notfctn-10-central-tax-english-2019.pdf', 'vr', 'Government of India'),
    'it-58': _r('Income Tax Department: Section 58, Income-tax Act 2025 (presumptive taxation)', 'https://www.incometaxindia.gov.in/w/section-58-138', 'vr', 'Government of India'),
    'it-faq': _r('Income Tax Department: FAQs on presumptive taxation (PDF)', 'https://www.incometaxindia.gov.in/documents/d/guest/faqs-on-tax-on-presumptive-taxation-scheme', 'vr', 'Government of India'),
    'mudra': _r('MUDRA: Pradhan Mantri Mudra Yojana', 'https://www.mudra.org.in/', 'vr', 'Government of India'),
    'pib-tarun': _r('PIB: Mudra loan limit raised, Tarun Plus category (PDF)', 'https://static.pib.gov.in/WriteReadData/specificdocs/documents/2024/oct/doc20241029426401.pdf', 'vr', 'Government of India'),
    'pmegp-sbi': _r('SBI: PMEGP scheme details', 'https://sbi.bank.in/web/business/sme/sme-government-schemes/pmegp', 'vr', 'Government of India'),
    'pmegp-portal': _r('PMEGP e-portal (KVIC)', 'https://www.kviconline.gov.in/pmegpeportal/pmegphome/index.jsp', 'u', 'Government of India'),
    'cgtmse': _r('CGTMSE: credit guarantees for collateral-free loans', 'https://www.cgtmse.in/', 'vr', 'Government of India'),
    'standup': _r('Stand-Up India', 'https://www.standupmitra.in/', 'vr', 'Government of India'),
    'startupindia': _r('Startup India (DPIIT recognition, Seed Fund)', 'https://www.startupindia.gov.in/', 'vr', 'Government of India'),
    'startupindia-kerala': _r('Startup India: Kerala state startup policy', 'https://www.startupindia.gov.in/content/sih/en/startup-scheme/state-startup-policies/Kerala-state-policy.html', 'vr', 'Government of India'),
    'startupindia-recognition': _r('Startup India: who is eligible for DPIIT startup recognition', 'https://www.startupindia.gov.in/content/sih/en/startupgov/startup_recognition_page.html', 'vr', 'Government of India'),
    'partnership-act': _r('Indian Partnership Act, 1932 (India Code, PDF)', 'https://www.indiacode.nic.in/bitstream/123456789/12849/1/the_indian_partnership_act_1932.pdf', 'vr', 'Government of India'),
    'mca': _r('Ministry of Corporate Affairs (MCA): LLPs and companies', 'https://www.mca.gov.in/', 'vr', 'Government of India'),
    'ipindia': _r('IP India: trademarks', 'https://ipindia.gov.in/', 'vr', 'Government of India'),
    'tm-search': _r('IP India: search existing trademarks', 'https://ipindia.gov.in/trade-marks-before-you-apply-search-existing-trademarks', 'v', 'Government of India'),
    'tm-fees': _r('IP India: trademark forms and official fees', 'https://ipindia.gov.in/pages/trade-marks/learn/forms-and-official-fees', 'vr', 'Government of India'),
    'fssai-doc': _r('FSSAI: which food businesses need registration or a licence (PDF)', 'https://mail.fssai.gov.in/upload/uploadfiles/files/Eligibility_Kind_Business_04_05_2020.pdf', 'vr', 'Government of India'),
    'foscos': _r('FSSAI FoSCoS portal (apply online)', 'https://foscos.fssai.gov.in/', 'u', 'Government of India'),
    'cpa-2019': _r('Consumer Protection Act, 2019 (India Code, PDF)', 'https://www.indiacode.nic.in/bitstream/123456789/18964/1/cpa.pdf', 'vr', 'Government of India'),
    'doca-online': _r('Department of Consumer Affairs: protection in online transactions (PDF)', 'https://consumeraffairs.nic.in/sites/default/files/Consumer%20Protection%20Act%2C%202019%20protects%20consumers%20involved%20in%20online%20transactions%20English.pdf', 'vr', 'Government of India'),
    'legal-metrology': _r('Department of Consumer Affairs: label rules for packaged goods (PDF)', 'https://consumeraffairs.nic.in/sites/default/files/02-Aug-2024.pdf', 'vr', 'Government of India'),
    'nch': _r('National Consumer Helpline, 1915', 'https://consumerhelpline.gov.in/', 'v', 'Help and safety'),
    'direct-selling': _r('Consumer Protection (Direct Selling) Rules, 2021 (UNEP LEAP law database)', 'https://leap.unep.org/en/countries/in/national-legislation/consumer-protection-direct-selling-rules-2021', 'vr', 'Help and safety'),
    'asci': _r('ASCI: influencer advertising FAQs', 'https://www.ascionline.in/social/faqs/', 'vr', 'Government of India'),
    'dpdp': _r('PIB: Digital Personal Data Protection Rules, 2025 explained (PDF)', 'https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf', 'vr', 'Government of India'),
    'epfo': _r('EPFO (Employees\' Provident Fund)', 'https://www.epfindia.gov.in/', 'vr', 'Government of India'),
    'sachet': _r('RBI Sachet: check entities, report illegal deposit schemes', 'https://sachet.rbi.org.in/', 'v', 'Help and safety'),
    'rbi-beaware': _r('RBI press release: BE(A)WARE booklet on financial frauds', 'https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=53372', 'v', 'Help and safety'),
    'kp-1930': _r('Kerala Police: 1930 cyber crime helpline', 'https://ps.keralapolice.gov.in/ernakulamruralcyber-ps/notifications/National-Cyber-Crime-Reporting-Helpline-No-1930-3338', 'v', 'Help and safety'),
    'cybercrime': _r('National Cyber Crime Reporting Portal', 'https://cybercrime.gov.in/', 'u', 'Help and safety'),
    'telemanas': _r('Tele-MANAS mental health helpline, 14416 (IIIT Bangalore page)', 'https://ehrc.iiitb.ac.in/project/tele-manas', 'v', 'Help and safety'),
    # Kerala
    'ksum': _r('Kerala Startup Mission (KSUM)', 'https://startupmission.kerala.gov.in/', 'vr', 'Kerala'),
    'ksum-grants': _r('KSUM innovation grant portal (login page)', 'https://grants.startupmission.in/', 'vr', 'Kerala'),
    'kied': _r('KIED: Kerala Institute for Entrepreneurship Development', 'https://kied.info/', 'v', 'Kerala'),
    'kerala-industries': _r('Kerala Department of Industries & Commerce: schemes', 'https://industry.kerala.gov.in/', 'vr', 'Kerala'),
    'kerala-ess': _r('Kerala: Entrepreneur Support Scheme (manufacturing units)', 'https://industry.kerala.gov.in/index.php/schemes-mainmenu/entrepreneur-support-scheme-schemes', 'vr', 'Kerala'),
    'kerala-nano': _r('Kerala: Margin Money Grant to Nano Units', 'https://industry.kerala.gov.in/index.php/schemes-mainmenu/margin-money-grand-to-nano-units-schemes', 'vr', 'Kerala'),
    'kerala-olop': _r('Kerala: One Local Body One Product (OLOP)', 'https://industry.kerala.gov.in/index.php/schemes-mainmenu/one-local-body-one-product-olop', 'vr', 'Kerala'),
    'kerala-dic': _r('Kerala: District Industries Centres', 'https://industry.kerala.gov.in/index.php/district-industries-centre', 'v', 'Kerala'),
    'kerala-clinic': _r('Kerala: MSME Clinic (experts at every DIC)', 'https://industry.kerala.gov.in/index.php/pages/facilitation-and-support/msme-clinic1', 'v', 'Kerala'),
    'kswift': _r('K-SWIFT: Kerala single window clearance', 'https://kswift.kerala.gov.in/', 'vr', 'Kerala'),
    'kerala-msme-act': _r('Kerala MSME Facilitation Act, 2019 (India Code, PDF)', 'https://www.indiacode.nic.in/bitstream/123456789/21022/1/act16_of_2019_engfinal.pdf', 'vr', 'Kerala'),
    'sc-msme': _r('Verdictum: Supreme Court says the Kerala MSME Act overrides the Panchayat Raj Act (2023)', 'https://www.verdictum.in/court-updates/supreme-court/kerala-msme-act-has-overriding-effect-on-kerala-panchayat-raj-act-1471771', 'v', 'Kerala'),
    'ksmart': _r('K-SMART: local body services online', 'https://ksmart.lsgkerala.gov.in/', 'vr', 'Kerala'),
    'ksmart-ikm': _r('IKM: what K-SMART covers', 'https://ikm.gov.in/en/node/1103', 'v', 'Kerala'),
    'ksmart-panchayat': _r('Edavaka Grama Panchayat: services now only through K-SMART', 'https://edavakapanchayat.lsgkerala.gov.in/en/node/182', 'v', 'Kerala'),
    'kudumbashree': _r('Kudumbashree', 'https://www.kudumbashree.org/', 'v', 'Kerala'),
    'kerala-labour': _r('Kerala Labour Commissionerate', 'https://lc.kerala.gov.in/', 'vr', 'Kerala'),
    'kerala-registration': _r('Kerala Registration Department (registration of firms)', 'https://keralaregistration.gov.in/', 'u', 'Kerala'),
    # Statistics
    'bls': _r('US Bureau of Labor Statistics: survival of new establishments, Table 7', 'https://www.bls.gov/bdm/us_age_naics_00_table7.txt', 'v', 'Statistics'),
}

# One entry above was written as a tuple by mistake-proofing: normalise it.
for _k, _v in list(R.items()):
    if isinstance(_v, tuple):
        R[_k] = _r(_v[0], _v[1], 'v', 'Courses and talks')

OPENSTAX_BOOK = 'https://openstax.org/details/books/entrepreneurship'
for _n in range(1, 16):
    R[f'os{_n}'] = _r(
        f'OpenStax Entrepreneurship, Chapter {_n}',
        f'https://openstax.org/books/entrepreneurship/pages/{_n}-introduction',
        'v',
        'OpenStax Entrepreneurship (CC BY-NC-SA 4.0)',
    )
R['os-book'] = _r('OpenStax Entrepreneurship (free textbook, CC BY-NC-SA 4.0)', OPENSTAX_BOOK, 'v', 'OpenStax Entrepreneurship (CC BY-NC-SA 4.0)')

USED = []


def use(key):
    if key not in R:
        raise KeyError(f'unknown resource {key}')
    if key not in USED:
        USED.append(key)
    return R[key]


def link(key, text=None):
    r = use(key)
    return f"[{text or r['title']}]({r['url']})"


def rules(key, text=None):
    """A link to an official source, marked check current rules."""
    return f"{link(key, text)} (check current rules)"


def res_table(rows):
    out = ['| Resource | What to study | Time | Status |', '| --- | --- | --- | --- |']
    for key, what, time in rows:
        r = use(key)
        for cell in (what, time):
            assert '|' not in cell, cell
        out.append(f"| [{r['title']}]({r['url']}) | {what} | {time} | {STATUS[r['s']]} |")
    return '\n'.join(out)


def numbered(items):
    return '\n'.join(f'{i}. {t}' for i, t in enumerate(items, 1))


def bullets(items):
    return '\n'.join(f'- {t}' for t in items)


def mistakes_list(items):
    return '\n'.join(f'- **{m}** {fix}' for m, fix in items)


def fence(text, lang=''):
    text = text.strip('\n')
    assert '```' not in text
    return f'```{lang}\n{text}\n```'


def quiz_blocks(quiz):
    qs, ans = [], []
    for i, q in enumerate(quiz, 1):
        opts = '\n'.join(f'    - {chr(65 + j)}) {o}' for j, o in enumerate(q['o']))
        qs.append(f"{i}. {q['q']}\n{opts}")
        letter = q['a']
        assert letter in 'ABCD'[: len(q['o'])], q
        ans.append(f"{i}. **{letter}.** {q['why']}")
    return '\n'.join(qs), '\n'.join(ans)


def lesson(m, l, *, title, weeks, hours, outcome, split, core, example, resources,
           steps, proof, templates, mistakes, quiz, study, action):
    code = f'ENT-M{m:02d}-L{l:02d}'
    sid = code.lower()
    a, b = weeks
    q_text, a_text = quiz_blocks(quiz)
    assert 3 <= len(quiz) <= 5
    parts = [
        '## Core lesson',
        core.strip(),
        '## Local example',
        example.strip(),
        '## Free resources',
        res_table(resources),
        '## Action task',
        numbered(steps),
        f'**Proof to record:** {proof}',
    ]
    for t_title, t_body, t_lang in templates:
        parts += [f'## Template: {t_title}', fence(t_body, t_lang)]
    parts += [
        '## Common mistakes',
        mistakes_list(mistakes),
        '## Quiz',
        'Answer without looking back. The answers are at the bottom of this page.',
        q_text,
        '## Progress checklist',
        'Tick these under **Your tasks** at the top of this page:',
        bullets([
            f'**Study:** {study}',
            f'**Action:** {action}. It is done when your proof is saved: {proof[0].lower() + proof[1:]}',
            '**Quiz:** at least 4 right, or re-read the core lesson and try again.',
        ]),
        '## Answers',
        a_text,
    ]
    content = '\n\n'.join(parts)
    return {
        'id': sid,
        'title': f'{code}: {title}',
        'kind': 'capstone' if m == 14 else 'level',
        'weeks': [a, b],
        'hours': hours,
        'summary': f'**Outcome:** {outcome} **Time:** about {hours} hours ({split}).',
        'content': content,
        'tasks': [
            {'id': f'{sid}-study', 'text': f'Study: {study}', 'kind': 'task', 'week': a},
            {'id': f'{sid}-action', 'text': f'Action: {action}', 'kind': 'project', 'week': b,
             'detail': f'**Proof to record:** {proof} Paste the link to your proof (a Google Drive file, sheet or photo) in this task\'s note.'},
            {'id': f'{sid}-quiz', 'text': 'Quiz: at least 4 right', 'kind': 'task', 'week': b},
        ],
    }


def module(m, *, title, weeks, hours, overview, outcomes, lessons, project, project_steps,
           project_proof, rubric, short, mistakes):
    sid = f'ent-m{m:02d}'
    a, b = weeks
    lesson_lines = [f"{s['title']} (about {s['hours']} hours)" for s in lessons]
    rub = ['| Criterion | 1: Not yet | 2: Getting there | 3: Ready |', '| --- | --- | --- | --- |']
    for row in rubric:
        assert len(row) == 4 and all('|' not in c for c in row)
        rub.append('| ' + ' | '.join(row) + ' |')
    lesson_hours = sum(s['hours'] for s in lessons)
    parts = [
        '## Overview',
        overview.strip(),
        '## Outcomes',
        'By the end of this module you can:',
        bullets(outcomes),
        '## Time',
        f'About {hours} hours in total: {lesson_hours} hours of lessons and {hours - lesson_hours} hours for the module project. Part-time: weeks {a}–{b}.' if a != b else
        f'About {hours} hours in total: {lesson_hours} hours of lessons and {hours - lesson_hours} hours for the module project. Part-time: week {a}.',
        '## Lessons',
        numbered(lesson_lines),
        f'## Module project: {project}',
        numbered(project_steps),
        f'**Proof to record:** {project_proof}',
        '## Self-assessment rubric',
        'Score yourself honestly after the project. Move on when no row is a 1 and at least half the rows are 3. If a row is a 1, redo that part first.',
        '\n'.join(rub),
        '## Short on time?',
        'The minimum version, when PSC prep or work leaves little time:',
        bullets(short),
        '## Top mistakes in this module',
        mistakes_list(mistakes),
    ]
    return {
        'id': sid,
        'title': f'Module {m}: {title}',
        'kind': 'capstone' if m == 14 else 'level',
        'weeks': [a, b],
        'hours': hours,
        'summary': overview.strip().split('\n\n')[0],
        'content': '\n\n'.join(parts),
        'tasks': [
            {'id': f'{sid}-project', 'text': f'Module project: {project}', 'kind': 'project', 'week': b,
             'detail': f'**Proof to record:** {project_proof}'},
            {'id': f'{sid}-rubric', 'text': 'Self-assessment: rubric scored, no row at 1', 'kind': 'exit', 'week': b},
        ],
    }
