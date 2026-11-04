"""Shared helpers and the resource registry for the Kerala Real Estate
Business course. Every link lives in R with the status found when it was
checked; lessons refer to links by key so the sources page lists exactly the
links used."""

import collections
import hashlib
import random

import plan

VDATE = '2026-11-04'
ASOF = 'as of November 2026'
CHECK = 'check current rules'
RULE = f'{ASOF}; {CHECK}'
APP = 'https://naipunyam.github.io/vidhyarambham/#/course/'

STATUS = {
    'v': f'verified {VDATE}',
    'vr': f'verified {VDATE}; check current rules',
    'vt': f'verified {VDATE} through a secondary source; check current rules',
    's': f'found in a web search {VDATE}; page not opened, so unverified',
    'u': 'unverified: the site blocks automated checks; type the address yourself',
}

G_OFF = 'Official Kerala and Government of India portals'
G_LAW = 'Laws, rules and court decisions'
G_SEC = 'Secondary guides used to check rates and procedures'
G_TEXT = 'Free courses and textbooks'
G_TOOLS = 'Free tools'
G_MKT = 'Property portals and marketing platforms'
GROUP_ORDER = [G_OFF, G_LAW, G_SEC, G_TEXT, G_TOOLS, G_MKT]


def _r(title, url, s='v', group='Other'):
    assert ' ' not in url and ')' not in url and '(' not in url, url
    return {'title': title, 'url': url, 's': s, 'group': group}


R = {
    # ---- Official portals
    'krera': _r('Kerala Real Estate Regulatory Authority (K-RERA): agent and project registration, complaints, project search', 'https://rera.kerala.gov.in/', 'vr', G_OFF),
    'kreg': _r('Kerala Registration Department (fair value, EC, e-stamp, document services)', 'https://keralaregistration.gov.in/', 'u', G_OFF),
    'pearl': _r('Kerala Registration PEARL portal: EC applications and status', 'https://pearl.registration.kerala.gov.in/', 'u', G_OFF),
    'igr-fv': _r('Kerala IGR fair value search', 'https://igr.kerala.gov.in/', 'u', G_OFF),
    'revenue': _r('Kerala Revenue Department (ReLIS): land tax and revenue e-services', 'http://www.revenue.kerala.gov.in/', 'u', G_OFF),
    'wayanad-tax': _r('Wayanad district (official NIC site): pay land tax online through ReLIS', 'https://wayanad.gov.in/en/service/pay-land-tax-online/', 'v', G_OFF),
    'entebhoomi': _r('Ente Bhoomi: Kerala integrated land information portal', 'https://entebhoomi.kerala.gov.in/', 'u', G_OFF),
    'entebhoomi-nic': _r('NIC Informatics (January 2025): Ente Bhoomi Integrated Land Information Management System', 'https://informatics.nic.in/files/websites/january-2025/ente-bhoomi.php', 'v', G_OFF),
    'erekha': _r('e-Rekha (Kerala Land Information Mission): buy digital survey records and maps', 'https://erekha.kerala.gov.in/', 'vr', G_OFF),
    'sanketham': _r('LSGD Sanketham building-permit portal (notice on the move to K-SMART)', 'https://buildingpermit.lsgkerala.gov.in/default.aspx', 'v', G_OFF),
    'kpbr': _r('Kerala Panchayat Building Rules, 2019 (LSGD PDF)', 'https://dop.lsgkerala.gov.in/system/files/file_page/kerala-panchayat-building-rules-2019_1.pdf', 's', G_OFF),
    'ksdma': _r('Kerala State Disaster Management Authority: hazard maps (flood, landslide)', 'https://sdma.kerala.gov.in/hazard-maps/', 'v', G_OFF),
    'it-tds': _r('Income Tax Department: TDS on the sum paid to buy an immovable property', 'https://incometaxindia.gov.in/w/tds-from-sum-paid-to-buy-an-immovable-property', 'vr', G_OFF),
    'ecourts': _r('eCourts Services (eCommittee, Supreme Court of India): case status by party name, CNR number, court orders, caveats', 'https://services.ecourts.gov.in/', 'v', G_OFF),
    'kp-1930': _r('Kerala Police notice: National Cyber Crime Reporting Helpline 1930 and the portal cybercrime.gov.in', 'https://ps.keralapolice.gov.in/ernakulamruralcyber-ps/notifications/National-Cyber-Crime-Reporting-Helpline-No-1930-3338', 'v', G_OFF),
    'gbp': _r('Google Business Profile Help: guidelines for service-area businesses', 'https://support.google.com/business/answer/10514137?hl=en', 'v', G_OFF),

    # ---- Laws and court decisions
    'tpa-54': _r('Indian Kanoon: Section 54, Transfer of Property Act, 1882 (sale defined)', 'https://future.indiankanoon.org/doc/613871', 'v', G_LAW),
    'rent-act': _r('India Code: Kerala Buildings (Lease and Rent Control) Act, 1965 (PDF)', 'https://www.indiacode.nic.in/bitstream/123456789/20372/1/kerala_buildings_lease_and_rent_ctrl_act_1965.pdf', 'v', G_LAW),
    'klr-act': _r('India Code: Kerala Land Reforms Act, 1963 (PDF)', 'https://www.indiacode.nic.in/bitstream/123456789/15605/1/the_kerala_land_reforms_act%2C_1963_%28no.1_of_1964%29.pdf', 'v', G_LAW),
    'sc-paddy': _r('LiveLaw (February 2025): Supreme Court on Paddy Land Act conversion fee above 25 cents (State of Kerala v. Moushmi Ann Jacob)', 'https://www.livelaw.in/amp/supreme-court/kerala-paddy-land-act-no-exemption-from-conversion-fee-if-land-exceeds-25-cents-supreme-court-284584', 'v', G_LAW),
    'wp-rera': _r('Wikipedia: Real Estate (Regulation and Development) Act, 2016', 'https://en.wikipedia.org/wiki/Real_Estate_%28Regulation_and_Development%29_Act,_2016', 'v', G_LAW),
    'wp-landreform': _r('Wikipedia: Land reform in Kerala', 'https://en.wikipedia.org/wiki/Land_reform_in_Kerala', 'v', G_LAW),
    'tg-gpa': _r('TaxGuru (15 October 2011): Supreme Court in Suraj Lamp & Industries v. State of Haryana, GPA sales do not transfer title', 'https://taxguru.in/corporate-law/general-power-attorney-legal-sanctity-immovable-property-sold-transferred-registered-deeds-sc.html', 'v', G_LAW),
    'reg-act': _r('iPleaders: compulsory registration under Section 17 of the Registration Act, 1908, and the effect of non-registration', 'https://blog.ipleaders.in/registration-of-documents-and-consequences-of-non-registration-under-section-17-of-the-registration-act-l908/', 'v', G_LAW),

    # ---- Secondary guides
    'sy-stamp': _r('Square Yards (updated July 2026): stamp duty and registration charges in Kerala', 'https://www.squareyards.com/blog/stamp-duty-and-registration-charges-in-kerala', 'vt', G_SEC),
    'hc-fv': _r('Housing.com: how to check the fair value of land in Kerala', 'https://housing.com/news/how-to-check-the-fair-value-of-land-in-kerala', 'vt', G_SEC),
    'hc-ec': _r('Housing.com (April 2025): how to get an encumbrance certificate in Kerala', 'https://housing.com/news/steps-to-get-an-encumbrance-certificate-in-kerala/amp', 'vt', G_SEC),
    'hc-online': _r('Housing.com: Kerala\'s online property-related services', 'https://housing.com/news/all-about-keralas-online-property-related-services', 'vt', G_SEC),
    'om-fv2023': _r('Onmanorama (28 March 2023): 20% increase in land fair value from 1 April 2023', 'https://www.onmanorama.com/news/kerala/2023/03/28/kerala-increases-land-fair-value.html', 'v', G_SEC),
    'om-flat7': _r('Onmanorama (3 February 2023): Kerala Budget, stamp duty for flats sold within six months raised to 7%', 'https://www.onmanorama.com/news/business/2023/02/03/kerala-budget-flat-apartment-stamp-duy-land-fair-price.amp.html', 'v', G_SEC),
    'om-rera': _r('Onmanorama (January 2020): RERA norms in Kerala, registration thresholds and fees', 'https://www.onmanorama.com/news/kerala/2020/01/01/rera-real-estate-regulatory-authority-norms.html', 'vt', G_SEC),
    'tg-krera': _r('TaxGuru: Kerala RERA Rules, registration fees', 'https://taxguru.in/corporate-law/kerala-rera-rules-registration.html', 'vt', G_SEC),
    'sy-krera': _r('Square Yards (updated 22 November 2024): RERA Kerala agent registration, Form G and documents', 'https://www.squareyards.com/blog/rera-kerala-rerat', 'vt', G_SEC),
    'om-czmp': _r('Onmanorama (24 September 2024): Centre approves Kerala\'s revised Coastal Zone Management Plan', 'https://www.onmanorama.com/news/kerala/2024/09/24/coastal-zone-management-plan-centre-approves-proposal-of-kerala.html', 'v', G_SEC),
    'air-esa': _r('All India Radio News (3 August 2024): fresh Western Ghats ESA draft notification', 'https://newsonair.gov.in/centre-issues-fresh-esa-draft-notification-for-western-ghats-across-six-states', 'v', G_SEC),
    'week-ksmart': _r('The Week (10 April 2025): K-SMART services rolled out across Kerala\'s panchayats', 'https://www.theweek.in/wire-updates/national/2025/04/10/mes7-kl-k-smart-panchayats.html', 'v', G_SEC),
    'bb-benami': _r('BankBazaar: the Benami Property Transactions Act explained', 'https://www.bankbazaar.com/home-loan/benami-property-act.html', 'vt', G_SEC),
    'hc-ltcg': _r('Housing.com: LTCG on property, 12.5% without indexation or 20% with indexation', 'https://housing.com/news/fm-gives-choice-to-property-owners-20-ltcg-with-indexation-or-12-5-without-indexation', 'vt', G_SEC),
    'tg-tds2025': _r('TaxGuru: TDS on immovable property purchases under the Income-tax Act, 2025', 'https://taxguru.in/income-tax/tds-immovable-property-purchases-compliance-income-tax-act-2025.html', 'vt', G_SEC),
    'pa-cg': _r('Patron Accounting (updated 6 April 2026): capital gains exemptions, old sections 54, 54F and 54EC', 'https://www.patronaccounting.com/blog/capital-gains-exemption-section-54-54ec-54f', 'vt', G_SEC),
    'ts-86': _r('Taxscan (17 December 2025): section 54F becomes section 86 of the Income-tax Act, 2025', 'https://www.taxscan.in/top-stories/capital-gains-for-home-buyers-section-54f-vs-section-86-explained-old-vs-new-tax-act-series-article-1-1440142', 'vt', G_SEC),
    'bt-hp': _r('Business Today (14 August 2025): new Income-tax Bill keeps the 30% standard deduction on house property after municipal taxes', 'https://www.businesstoday.in/personal-finance/tax/story/new-income-tax-bill-clarifies-key-deductions-on-house-property-income-489507-2025-08-14', 'vt', G_SEC),
    'bf-gst': _r('Bajaj Finserv (July 2026): GST rates on housing', 'https://www.bajajfinserv.in/reduction-in-gst-rate-on-housing', 'vt', G_SEC),
    'rp-gst': _r('Razorpay: GST on brokerage and commission', 'https://razorpay.com/learn/gst-on-brokerage-and-commission/', 'vt', G_SEC),
    'bs-ltv': _r('Business Standard (8 October 2015): RBI loan-to-value limits for home loans', 'https://www.business-standard.com/amp/article/pf/home-buyers-can-now-get-more-loan-for-property-up-to-rs-30-lakh-115100801016_1.html', 'vt', G_SEC),
    'week-reit': _r('The Week (30 June 2021): SEBI cuts minimum application amount for REITs', 'https://www.theweek.in/news/biz-tech/2021/06/30/sebi-reduces-minimum-application-amount-for-reits-should-you-invest-now.html', 'vt', G_SEC),
    'taxscan-sft': _r('Taxscan: property transactions and income tax rules for FY 2026-27 (SFT threshold)', 'https://www.taxscan.in/top-stories/property-transactions-and-income-tax-rules-in-india-compliance-essentials-for-fy-2026-27-1446927', 'vt', G_SEC),

    # ---- Courses and textbooks
    'os-fin': _r('OpenStax, Principles of Finance (free, CC BY-NC-SA)', 'https://openstax.org/books/principles-finance/pages/preface', 'v', G_TEXT),
    'lt-fin': _r('Principles of Finance (OpenStax) on LibreTexts: chapter list including time value of money (chapters 7-9)', 'https://biz.libretexts.org/Bookshelves/Finance/Principles_of_Finance_%28OpenStax%29', 'v', G_TEXT),
    'mit-re': _r('MIT OpenCourseWare 11.431J Real Estate Finance and Investment (Geltner and McGrath, CC BY-NC-SA)', 'https://ocw.mit.edu/courses/11-431j-real-estate-finance-and-investment-fall-2006', 'v', G_TEXT),

    # ---- Tools
    'gsheets': _r('Google Sheets (free with a Google account; works on phones and offline)', 'https://workspace.google.com/products/sheets/', 'v', G_TOOLS),
    'libreoffice': _r('LibreOffice (free and open source; Calc spreadsheet works on an old laptop)', 'https://www.libreoffice.org/', 'v', G_TOOLS),
    'canva': _r('Canva (free plan for listing graphics; site blocks automated checks)', 'https://www.canva.com/', 'u', G_TOOLS),
    'qgis': _r('QGIS: free and open-source GIS (GPL)', 'https://qgis.org/', 'v', G_TOOLS),
    'gearth': _r('Google Earth versions (web, mobile, Pro desktop)', 'https://www.google.com/earth/about/versions/', 'vr', G_TOOLS),

    # ---- Portals
    'nobroker': _r('NoBroker: list your property for rent or sale (free for owners)', 'https://www.nobroker.in/list-your-property-for-rent-sale', 'vr', G_MKT),
    'magicbricks': _r('MagicBricks (property portal)', 'https://www.magicbricks.com/', 'u', G_MKT),
    '99acres': _r('99acres (property portal)', 'https://www.99acres.com/', 's', G_MKT),
    'housing': _r('Housing.com (property portal)', 'https://housing.com/', 's', G_MKT),
}

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
    return f"{link(key, text)} ({RULE})"


OTHER = {
    'ent': ('entrepreneurship', 'Practical Entrepreneurship'),
    'smm': ('social-media-marketing', 'Practical Social Media Marketing'),
    'fin': ('personal-finance', 'Practical Personal Finance for India'),
    'pd': ('mind-body-people', 'Mind, Body and People'),
    'lrn': ('learning-capabilities', 'Practical Learning Capabilities'),
    'ai': ('ai-generalist', 'Free AI Generalist Course'),
}


def xref(course, section, text):
    cid, name = OTHER[course]
    return f'[{text}]({APP}{cid}/{section}) (in the {name} course)'


def res_table(rows):
    out = ['| Resource | What to study | Time | Status |', '| --- | --- | --- | --- |']
    for key, what, time in rows:
        r = use(key)
        for cell in (what, time):
            assert '|' not in cell, cell
        out.append(f"| [{r['title']}]({r['url']}) | {what} | {time} | {STATUS[r['s']]} |")
    return '\n'.join(out)


def table(header, rows):
    out = ['| ' + ' | '.join(header) + ' |', '| ' + ' | '.join('---' for _ in header) + ' |']
    for row in rows:
        assert len(row) == len(header), row
        for c in row:
            assert '|' not in c, c
        out.append('| ' + ' | '.join(row) + ' |')
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


QUIZ_LETTERS = collections.Counter()


def quiz_blocks(quiz):
    qs, ans = [], []
    for i, q in enumerate(quiz, 1):
        rng = random.Random(int(hashlib.md5(q['q'].encode('utf-8')).hexdigest(), 16))
        order = list(range(len(q['o'])))
        rng.shuffle(order)
        options = [q['o'][k] for k in order]
        letter = 'ABCD'[order.index(0)]
        QUIZ_LETTERS[letter] += 1
        opts = '\n'.join(f'    - {chr(65 + j)}) {o}' for j, o in enumerate(options))
        qs.append(f"{i}. {q['q']}\n{opts}")
        ans.append(f"{i}. **{letter}.** {q['why']}")
    return '\n'.join(qs), '\n'.join(ans)


def Q(q, right, *wrong, why):
    return {'q': q, 'o': [right, *wrong], 'why': why}


CAPSTONE = plan.CAPSTONE
WEEKS, PROJECT_WEEK, LAST_WEEK, LOAD = plan.assign()
FOLDERS = ['00 Setup'] + [f'{m:02d} {t}' for m, (t, _, _) in enumerate(plan.MODULES, 1)]
TOOLKIT_ITEMS = []   # (module, item) collected from modules


def fmt_hours(h):
    if h == int(h):
        return f'{int(h)} hour' + ('' if h == 1 else 's')
    whole = int(h)
    mins = round((h - whole) * 60)
    if whole == 0:
        return f'{mins} minutes'
    return f'{whole} hour' + ('' if whole == 1 else 's') + f' {mins} minutes'


def code_of(m, l=None):
    return f'RE-M{m:02d}' + (f'-L{l:02d}' if l else '')


def lesson(m, l, *, outcome, split, core, example, resources, steps, proof, templates, mistakes,
           fraud, quiz, study, action, calc=None, rules_rows=None, pro=None, fulltime=None, extra_tasks=None):
    title = plan.MODULES[m - 1][1][l - 1][0]
    hours = plan.MODULES[m - 1][1][l - 1][1]
    code = code_of(m, l)
    sid = code.lower()
    a, b = WEEKS[(m, l)]
    q_text, a_text = quiz_blocks(quiz)
    assert 3 <= len(quiz) <= 5, code
    assert templates, code
    assert len(mistakes) >= 2, code
    assert fraud, code
    parts = ['## Core lesson', core.strip(), '## Local example', example.strip()]
    if calc:
        parts += ['## Worked calculation', calc.strip()]
    if rules_rows:
        parts += [f'## Key rules ({ASOF})',
                  f'Laws, rates and portals change. Each rule below was checked against the source shown on {VDATE}; **{CHECK}** before you rely on it.',
                  table(['Rule', 'What it means in practice', 'Source'], rules_rows)]
    if pro:
        parts += ['## When you need a licensed professional', pro.strip()]
    parts += ['## Free resources', res_table(resources), '## Action task (in your local market)', numbered(steps),
              f'**Proof to record:** {proof}']
    if fulltime:
        parts.append(f'**Full-time track:** {fulltime.strip()}')
    for t_title, t_body in templates:
        parts += [f'## Template: {t_title}', fence(t_body)]
    parts += ['## Common mistakes', mistakes_list(mistakes),
              '## Local fraud warning', fraud.strip(),
              '## Quiz', 'Answer from memory first. The answers are at the bottom of this page.', q_text,
              '## Progress checklist', 'Tick these under **Your tasks** at the top of this page:',
              bullets([f'**Study:** {study}',
                       f'**Action:** {action}. It is done when your proof is saved: {proof[0].lower() + proof[1:]}',
                       f'**Quiz:** at least {len(quiz) - 1} right, or re-read the lesson and try again tomorrow.']),
              '## Answers', a_text]
    folder = FOLDERS[m]
    tasks = [
        {'id': f'{sid}-study', 'text': f'Study: {study}', 'kind': 'task', 'week': a},
        {'id': f'{sid}-action', 'text': f'Action: {action}', 'kind': 'project', 'week': b,
         'detail': f'**Proof to record:** {proof} Save it in your Real Estate Toolkit folder ({folder}) and note where it is.'},
        {'id': f'{sid}-quiz', 'text': f'Quiz: at least {len(quiz) - 1} right', 'kind': 'task', 'week': b},
    ]
    for tid, text, wk, detail in (extra_tasks or []):
        t = {'id': f'{sid}-{tid}', 'text': text, 'kind': 'project', 'week': wk if wk is not None else b}
        if detail:
            t['detail'] = detail
        tasks.append(t)
    return {
        'id': sid, 'title': f'{code}: {title}', 'kind': 'capstone' if m == CAPSTONE else 'level',
        'weeks': [a, b], 'hours': hours,
        'summary': f'**Outcome:** {outcome} **Time:** about {fmt_hours(hours)} ({split}).',
        'content': '\n\n'.join(parts), 'tasks': tasks,
    }


def module(m, *, overview, outcomes, lessons, project, project_steps, project_proof, rubric,
           short, flashcards, mistakes, tools, toolkit, fulltime=None):
    title = plan.MODULES[m - 1][0]
    sid = f're-m{m:02d}'
    ws = [WEEKS[(m, l)] for l in range(1, len(lessons) + 1)]
    a = min(x[0] for x in ws)
    pw = PROJECT_WEEK[m]
    b = max(pw, max(x[1] for x in ws))
    hours = sum(s['hours'] for s in lessons) + plan.MODULES[m - 1][2]
    assert len(lessons) == len(plan.MODULES[m - 1][1])
    rub = ['| Criterion | 1: Not yet | 2: Getting there | 3: Ready |', '| --- | --- | --- | --- |']
    for row in rubric:
        assert len(row) == 4 and all('|' not in c for c in row)
        rub.append('| ' + ' | '.join(row) + ' |')
    assert 5 <= len(flashcards) <= 10
    cards = ['| Front (say the answer aloud) | Back |', '| --- | --- |']
    for front, back in flashcards:
        assert '|' not in front and '|' not in back
        cards.append(f'| {front} | {back} |')
    for item in toolkit:
        TOOLKIT_ITEMS.append((m, item))
    lesson_hours = sum(s['hours'] for s in lessons)
    paras = overview.strip().split('\n\n')
    assert len(paras) >= 2
    when = f'weeks {a}–{b}' if a != b else f'week {a}'
    letter, ptitle, _, _ = plan.part_of(m)
    parts = [
        f'*Part {letter}: {ptitle}.*', '## Overview', '\n\n'.join(paras[1:]),
        '## Outcomes', 'By the end of this module you can:', bullets(outcomes),
        '## Time', f'About {fmt_hours(hours)} in total: {fmt_hours(lesson_hours)} of lessons and {fmt_hours(hours - lesson_hours)} for the module project. Part-time: {when}, with the module project due in week {pw}.',
    ]
    if fulltime:
        parts.append(f'**Full-time track:** {fulltime.strip()}')
    parts += [
        '## Lessons', numbered([f"{s['title']} (about {fmt_hours(s['hours'])})" for s in lessons]),
        '## Copy-ready tools in this module', bullets(tools),
        f'## Module project: {project}', numbered(project_steps), f'**Proof to record:** {project_proof}',
        '## Add to your Real Estate Toolkit', 'Save these in your toolkit folder and Google Sheets workbook (set up in Week 0). By the capstone they form your complete business toolkit.',
        bullets(toolkit),
        '## Self-assessment rubric', 'Score yourself honestly after the project. Move on when no row is a 1 and at least half the rows are 3.', '\n'.join(rub),
        '## Short on time?', 'The minimum version, for weeks when PSC study or work leaves little time:', bullets(short),
        '## Revision flashcards', 'Cover the right-hand column, say the answer aloud, then check.', '\n'.join(cards),
        '## Top mistakes in this module', mistakes_list(mistakes),
    ]
    return {
        'id': sid, 'title': f'Module {m}: {title}', 'kind': 'capstone' if m == CAPSTONE else 'level',
        'weeks': [a, b], 'hours': hours, 'summary': paras[0], 'content': '\n\n'.join(parts),
        'tasks': [
            {'id': f'{sid}-project', 'text': f'Module project: {project}', 'kind': 'project', 'week': pw,
             'detail': f'**Proof to record:** {project_proof} Save it in your toolkit folder ({FOLDERS[m]}).'},
            {'id': f'{sid}-toolkit', 'text': 'Toolkit: this module\'s tools saved and adapted to your area', 'kind': 'task', 'week': pw},
            {'id': f'{sid}-rubric', 'text': 'Self-assessment: rubric scored, no row at 1', 'kind': 'exit', 'week': pw},
        ],
    }
