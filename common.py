"""Shared helpers and the resource registry for Mind, Body and People.

Every link used in the course lives in R, with the status found when it was
checked. Lessons refer to links by key, so the sources page is generated from
exactly the links the course uses. Lesson titles, hours and part-time weeks
come from plan.py, so the schedule is balanced in one place.
"""

import collections
import hashlib
import random

import plan

VDATE = '2026-11-04'
ASOF = 'as of November 2026'
CHECK = 'check current rules'
APP = 'https://naipunyam.github.io/vidhyarambham/#/course/'

STATUS = {
    'v': f'verified {VDATE}',
    'v3': 'verified 2026-11-03',
    'vr': f'verified {VDATE}; check current rules',
    'vt': f'verified {VDATE} (headline figures checked; secondary summary)',
    's': f'found in a web search {VDATE}; page not opened, so unverified',
    'u': 'unverified',
}

G_TEXT = 'Free textbooks and courses'
G_SCI = 'Studies and reviews behind the claims'
G_WIKI = 'Wikipedia background articles (classic experiments and replication)'
G_PRACT = 'Free practices, surveys and tests'
G_CLASSIC = 'Public-domain classics'
G_TALK = 'Free talks and clubs'
G_TOOLS = 'Free and open-source tools'
G_BODY = 'Fitness, yoga, sleep and nutrition'
G_HELP = 'Helplines and official safety sources'

GROUP_ORDER = [G_TEXT, G_SCI, G_WIKI, G_PRACT, G_CLASSIC, G_TALK, G_TOOLS, G_BODY, G_HELP]


def _r(title, url, s='v', group='Other'):
    assert ' ' not in url and ')' not in url and '(' not in url, url
    return {'title': title, 'url': url, 's': s, 'group': group}


OS = 'https://openstax.org/books/psychology-2e/pages/'
WP = 'https://en.wikipedia.org/wiki/'
GG = 'https://ggia.berkeley.edu/practice/'
DL = 'https://thedecisionlab.com/biases/'
NHS = 'https://www.nhs.uk/live-well/exercise/'

R = {
    # ---- Free textbooks and courses
    'os-psych': _r('OpenStax, Psychology 2e (free, CC BY-NC-SA 4.0)', OS + 'preface', 'v3', G_TEXT),
    'os-2': _r('OpenStax Psychology 2e, chapter 2: Psychological Research (2.1 to 2.4)', OS + '2-introduction', 'v', G_TEXT),
    'os-7-3': _r('OpenStax Psychology 2e, 7.3 Problem Solving (heuristics and biases)', OS + '7-3-problem-solving', 'v3', G_TEXT),
    'os-10': _r('OpenStax Psychology 2e, chapter 10: Motivation and Emotion (10.1 and 10.4)', OS + '10-introduction', 'v', G_TEXT),
    'os-12': _r('OpenStax Psychology 2e, chapter 12: Social Psychology (12.1 to 12.7)', OS + '12-introduction', 'v', G_TEXT),
    'os-14-4': _r('OpenStax Psychology 2e, 14.4 Regulation of Stress', OS + '14-4-regulation-of-stress', 'v3', G_TEXT),
    'os-4-3': _r('OpenStax Psychology 2e, 4.3 Stages of Sleep', OS + '4-3-stages-of-sleep', 'v3', G_TEXT),
    'noba': _r('Noba Project: free psychology modules and textbooks (CC BY-NC-SA 4.0)', 'https://nobaproject.com/', 'v', G_TEXT),
    'mit-psych': _r('MIT OpenCourseWare 9.00SC Introduction to Psychology, John Gabrieli (CC BY-NC-SA 4.0)', 'https://ocw.mit.edu/courses/9-00sc-introduction-to-psychology-fall-2011/', 'v', G_TEXT),
    'yale-wb': _r('Yale, "The Science of Well-Being" with Laurie Santos (Coursera; free to enrol, some features or the certificate may cost money)', 'https://www.coursera.org/learn/the-science-of-well-being', 'vr', G_TEXT),
    'crashcourse': _r('Crash Course Psychology with Hank Green (40 episodes)', 'https://thecrashcourse.com/topic/psychology/', 'v', G_TEXT),
    'ggsc': _r('Greater Good Science Center, UC Berkeley: free articles, quizzes and podcasts', 'https://greatergood.berkeley.edu/', 'v', G_TEXT),

    # ---- Studies and reviews
    'sisk': _r('Sisk, Burgoyne et al. (2018), "To What Extent and Under Which Circumstances Are Growth Mind-Sets Important to Academic Achievement?" (PDF)', 'https://englelab.gatech.edu/articles/2018/Sisk,%20Burgoyne%20et%20al.%20%282018%29%20-%20Mindset%20and%20Academic%20Achievement.pdf', 'v', G_SCI),
    'goyal': _r('Goyal et al. (2014), "Meditation programs for psychological stress and well-being", JAMA Internal Medicine (PubMed abstract)', 'https://pubmed.ncbi.nlm.nih.gov/24395196/', 'v', G_SCI),
    'scheibehenne': _r('Scheibehenne, Greifeneder and Todd (2010), "Can There Ever Be Too Many Options?" choice-overload meta-analysis (PDF)', 'https://abcwest.cogs.indiana.edu/pmwiki/pdf/scheibehenne.options.2010.pdf', 'v', G_SCI),
    'killingsworth': _r('ScienceDaily (6 March 2023): money and happiness, the Killingsworth, Kahneman and Mellers adversarial collaboration', 'https://sciencedaily.com/releases/2023/03/230306163006.htm', 'v', G_SCI),
    'klein': _r('Gary Klein (2007), "Performing a Project Premortem", Harvard Business Review (PDF copy)', 'https://comprobo24.github.io/assignments/performing_a_project_premortem.pdf', 'v', G_SCI),
    'spotlight-sum': _r('Atticus Li, "The Barry Manilow T-shirt": a summary of the spotlight-effect studies', 'https://atticusli.com/replication-crisis/spotlight-effect/', 'vt', G_SCI),
    'lally': _r('University of Surrey (21 January 2026): does it really take 66 days to form a habit? (Dr Pippa Lally)', 'https://www.surrey.ac.uk/news/does-it-really-take-66-days-form-habit-we-asked-expert-dr-pippa-lally', 'v3', G_SCI),
    'gollwitzer': _r('Gollwitzer and Sheeran (2006), implementation intentions meta-analysis (free PDF)', 'https://kops.uni-konstanz.de/entities/publication/2e749bfb-8533-437c-8203-7e788c910c5f', 'v3', G_SCI),
    'sirois': _r('Sirois and Pychyl (2013), "Procrastination and the Priority of Short-Term Mood Regulation" (free author copy)', 'https://eprints.whiterose.ac.uk/id/eprint/91793/', 'v3', G_SCI),
    'wohl': _r('BPS Research Digest (4 May 2010): to cure procrastination, forgive yourself (Wohl, Pychyl and Bennett)', 'https://bps.org.uk/research-digest/cure-procrastination-forgive-yourself', 'v3', G_SCI),
    'rb-writing': _r('University of Chicago (2011): writing about worries eases anxiety and improves test performance (Ramirez and Beilock)', 'https://news.uchicago.edu/story/writing-about-worries-eases-anxiety-and-improves-test-performance', 'v3', G_SCI),
    'sdt': _r('Center for Self-Determination Theory: the theory (autonomy, competence, relatedness)', 'https://selfdeterminationtheory.org/theory/', 'v', G_SCI),
    'pon-batna': _r('Harvard Program on Negotiation: what is BATNA and how to find it', 'https://www.pon.harvard.edu/daily/batna/translate-your-batna-to-the-current-deal/', 'v', G_SCI),
    'hsad': _r('Harvard Study of Adult Development (director: Robert Waldinger)', 'https://www.adultdevelopmentstudy.org/', 'v', G_SCI),

    # ---- Wikipedia
    'wp-biases': _r('Wikipedia: List of cognitive biases', WP + 'List_of_cognitive_biases', 's', G_WIKI),
    'wp-replication': _r('Wikipedia: Replication crisis', WP + 'Replication_crisis', 'v', G_WIKI),
    'wp-power': _r('Wikipedia: Power posing', WP + 'Power_posing', 'v', G_WIKI),
    'wp-ego': _r('Wikipedia: Ego depletion', WP + 'Ego_depletion', 'v', G_WIKI),
    'wp-rejection': _r('Wikipedia: Rejection therapy', WP + 'Rejection_therapy', 'v', G_WIKI),
    'wp-spe': _r('Wikipedia: Stanford prison experiment', WP + 'Stanford_prison_experiment', 'v', G_WIKI),
    'wp-milgram': _r('Wikipedia: Milgram experiment', WP + 'Milgram_experiment', 'v', G_WIKI),
    'wp-asch': _r('Wikipedia: Asch conformity experiments', WP + 'Asch_conformity_experiments', 'v', G_WIKI),
    'wp-bystander': _r('Wikipedia: Bystander effect', WP + 'Bystander_effect', 'v', G_WIKI),
    'wp-marshmallow': _r('Wikipedia: Stanford marshmallow experiment', WP + 'Stanford_marshmallow_experiment', 'v', G_WIKI),
    'wp-mbti': _r('Wikipedia: Myers–Briggs Type Indicator (criticism section)', WP + 'Myers%E2%80%93Briggs_Type_Indicator', 'v', G_WIKI),
    'wp-cialdini': _r('Wikipedia: Robert Cialdini (the principles of influence)', WP + 'Robert_Cialdini', 'v', G_WIKI),
    'wp-gottman': _r('Wikipedia: John Gottman (including criticism of divorce-prediction claims)', WP + 'John_Gottman', 'v', G_WIKI),
    'wp-tfas': _r('Wikipedia: Thinking, Fast and Slow (including the priming replication problem)', WP + 'Thinking,_Fast_and_Slow', 'v', G_WIKI),
    'wp-loss': _r('Wikipedia: Loss aversion', WP + 'Loss_aversion', 'v', G_WIKI),
    'wp-overchoice': _r('Wikipedia: Overchoice (choice overload)', WP + 'Overchoice', 'v', G_WIKI),
    'wp-spotlight': _r('Wikipedia: Spotlight effect', WP + 'Spotlight_effect', 'v', G_WIKI),

    # ---- Practices, surveys and tests
    'ggia': _r('Greater Good in Action (UC Berkeley): free, research-based practices', 'https://ggia.berkeley.edu/', 'v', G_PRACT),
    'ggia-3gt': _r('Greater Good in Action: Three Good Things', GG + 'three-good-things', 'v', G_PRACT),
    'ggia-silver': _r('Greater Good in Action: Finding Silver Linings', GG + 'finding_silver_linings', 'v', G_PRACT),
    'decisionlab': _r('The Decision Lab: free index of cognitive biases', DL, 'v', G_PRACT),
    'dl-confirm': _r('The Decision Lab: confirmation bias', DL + 'confirmation-bias', 's', G_PRACT),
    'implicit': _r('Project Implicit (Harvard): Implicit Association Tests', 'https://implicit.harvard.edu/implicit/', 'v', G_PRACT),
    'via': _r('VIA Institute on Character: free character strengths survey (24 strengths, about 12 minutes)', 'https://www.viacharacter.org/', 'v', G_PRACT),
    'ipip-bffm': _r('Open-Source Psychometrics: IPIP Big Five Factor Markers test (50 items, educational use)', 'https://openpsychometrics.org/tests/IPIP-BFFM/', 'v', G_PRACT),
    'ipip': _r('International Personality Item Pool (public-domain personality items)', 'https://ipip.ori.org/', 'v', G_PRACT),
    'selfcomp': _r('Kristin Neff, self-compassion.org: free practices (How would you treat a friend?, Self-Compassion Break)', 'https://self-compassion.org/self-compassion-practices/', 'v', G_PRACT),

    # ---- Public-domain classics
    'meditations': _r('Marcus Aurelius, Meditations (Project Gutenberg, public domain in the USA)', 'https://www.gutenberg.org/ebooks/2680', 'v', G_CLASSIC),
    'enchiridion': _r('Epictetus, The Enchiridion, Higginson translation (Project Gutenberg)', 'https://www.gutenberg.org/ebooks/45109', 'v', G_CLASSIC),
    'seneca': _r('Seneca, Moral Letters to Lucilius, Gummere translation (Standard Ebooks; free in the USA, check your local law)', 'https://standardebooks.org/ebooks/seneca/moral-letters-to-lucilius/richard-m-gummere', 'v', G_CLASSIC),
    'franklin': _r('Benjamin Franklin, Autobiography (Project Gutenberg)', 'https://www.gutenberg.org/ebooks/20203', 'v', G_CLASSIC),
    'smiles': _r('Samuel Smiles, Self-Help (Project Gutenberg)', 'https://www.gutenberg.org/ebooks/935', 'v', G_CLASSIC),
    'allen': _r('James Allen, As a Man Thinketh (Project Gutenberg)', 'https://www.gutenberg.org/ebooks/4507', 'v', G_CLASSIC),
    'james-talks': _r('William James, Talks to Teachers on Psychology; and to Students on Some of Life\'s Ideals (Project Gutenberg)', 'https://www.gutenberg.org/ebooks/16287', 'v', G_CLASSIC),

    # ---- Talks and clubs
    'ted-jiang': _r('TED: Jia Jiang, "What I learned from 100 days of rejection" (about 15 minutes)', 'https://www.ted.com/talks/jia_jiang_what_i_learned_from_100_days_of_rejection', 'v', G_TALK),
    'ted-waldinger': _r('TED: Robert Waldinger, "What makes a good life? Lessons from the longest study on happiness" (about 13 minutes)', 'https://www.ted.com/talks/robert_waldinger_what_makes_a_good_life_lessons_from_the_longest_study_on_happiness', 'v', G_TALK),
    'tm-find': _r('Toastmasters International: Find a Club', 'https://www.toastmasters.org/find-a-club', 'v', G_TALK),
    'tm-calicut': _r('Toastmasters: Calicut Toastmasters (Kozhikode; Sundays 3 to 5 pm, online attendance allowed)', 'https://www.toastmasters.org/Find-a-Club/03984104-calicut-toastmasters', 'vr', G_TALK),
    'tm-malabar': _r('Toastmasters: Malabar Toastmasters Club', 'https://www.toastmasters.org/Find-a-Club/28676179-malabar-toastmasters-club', 's', G_TALK),

    # ---- Tools
    'loop': _r('Loop Habit Tracker (free, open source, GPLv3)', 'https://loophabits.org/', 'v3', G_TOOLS),
    'medito': _r('Medito: free meditation app from a non-profit foundation (open source)', 'https://meditofoundation.org/', 'v', G_TOOLS),
    'joplin': _r('Joplin: free, open-source notes for Android, Windows and Linux', 'https://joplinapp.org/', 'v3', G_TOOLS),
    'wellbeing': _r('Android Help: manage how you spend time with Digital Wellbeing', 'https://support.google.com/android/answer/9346420?hl=en', 'vr', G_TOOLS),

    # ---- Body
    'who-pa': _r('World Health Organization: physical activity fact sheet', 'https://www.who.int/news-room/fact-sheets/detail/physical-activity', 'v3', G_BODY),
    'nhs-guide': _r('NHS: physical activity guidelines for adults aged 19 to 64', NHS + 'physical-activity-guidelines-for-adults-aged-19-to-64/', 'v', G_BODY),
    'nhs-strength': _r('NHS: strength exercises', NHS + 'strength-exercises/', 'v', G_BODY),
    'nhs-flex': _r('NHS: flexibility exercises', NHS + 'flexibility-exercises/', 'v', G_BODY),
    'nhs-strvid': _r('NHS Fitness Studio: strength and resistance exercise videos', NHS + 'strength-and-resistance/', 'v', G_BODY),
    'nhs-aero': _r('NHS Fitness Studio: aerobic exercise videos', NHS + 'aerobic-exercises/', 'v', G_BODY),
    'nhs-yoga': _r('NHS Fitness Studio: Pilates and yoga videos', NHS + 'pilates-and-yoga/', 'v', G_BODY),
    'c25k': _r('NHS Couch to 5K: free 9-week running plan (app, website and PDF)', 'https://www.nhs.uk/better-health/get-active/get-running-with-couch-to-5k/', 'v', G_BODY),
    'cyp': _r('Ministry of AYUSH and MDNIY, Common Yoga Protocol, 4th revised edition, 2019 (PDF, MEA copy)', 'https://www.mea.gov.in/images/pdf/common-yoga-protocol-english.pdf', 'v', G_BODY),
    'cyp-2022': _r('Ministry of Ayush, Common Yoga Protocol, 5th revised edition, 2022 (PDF)', 'https://www.sanskrit.nic.in/uploads/CYP_2022/English.pdf', 'v', G_BODY),
    'aasm': _r('AASM and Sleep Research Society (2015): recommended sleep for adults (PDF)', 'https://www.aasm.org/resources/pdf/adultsleepdurationconsensus.pdf', 'v3', G_BODY),
    'nin-dgi': _r('ICMR-NIN, Dietary Guidelines for Indians, 2024 (PDF)', 'https://www.nin.res.in/dietaryguidelines/pdfjs/locale/DGI24thJune2024fin.pdf', 's', G_BODY),
    'icmr-sf': _r('South First (May 2024): ICMR releases Dietary Guidelines for Indians after 13 years', 'https://thesouthfirst.com/health/icmr-releases-dietary-guidelines-for-indians-after-13-years-says-no-to-protein-supplements/', 'v', G_BODY),
    'icmr-air': _r('All India Radio News (May 2024): ICMR releases updated Dietary Guidelines for Indians', 'https://newsonair.gov.in/icmr-releases-updated-dietary-guidelines-for-indians-in-2024', 'v', G_BODY),
    'aao-screen': _r('American Academy of Ophthalmology: computers, digital devices and eye strain', 'https://www.aao.org/eye-health/tips-prevention/computer-usage', 'v', G_BODY),

    # ---- Help and safety
    'telemanas': _r('Tele-MANAS: toll-free 24x7 national mental health helpline, 14416 or 1-800-89-14416', 'https://ehrc.iiitb.ac.in/project/tele-manas', 'v', G_HELP),
    'quitline': _r('National Tobacco Quitline Services: 1800-11-2356 (toll-free)', 'https://ntqls.in/', 'vr', G_HELP),
    'pib-cyber': _r('PIB (12 March 2025): steps against digital arrest scams; the 1930 helpline and cybercrime.gov.in', 'https://pib.gov.in/PressReleasePage.aspx?PRID=2110809', 'v', G_HELP),
    'cybercrime': _r('National Cyber Crime Reporting Portal', 'https://cybercrime.gov.in/', 'u', G_HELP),
    'darkpatterns': _r('Deloitte India summary: CCPA Guidelines for Prevention and Regulation of Dark Patterns, 2023 (13 patterns, PDF)', 'https://www2.deloitte.com/content/dam/Deloitte/in/Documents/tax/in-tax-gbt-the-guidelines-for-prevention-and-regulation-of-dark-patterns-noexp.pdf', 'vr', G_HELP),
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
    """A link to an official source, marked check current rules."""
    return f"{link(key, text)} ({CHECK})"


OTHER = {
    'lrn': ('learning-capabilities', 'Practical Learning Capabilities'),
    'fin': ('personal-finance', 'Practical Personal Finance for India'),
    'ent': ('entrepreneurship', 'Practical Entrepreneurship'),
    'smm': ('social-media-marketing', 'Practical Social Media Marketing'),
}

XREFS = []


def xref(course, section, text):
    """A link to a section of another course in this app."""
    cid, name = OTHER[course]
    XREFS.append((cid, section))
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


EVIDENCE = {
    'strong': 'Strong',
    'moderate': 'Moderate',
    'mixed': 'Mixed or weak',
    'failed': 'Failed to replicate or myth',
    'tool': 'Practical tool',
}

EVIDENCE_KEY = ('**Strong:** many studies, including large or real-world ones, agree. **Moderate:** good studies, but fewer, '
                'smaller effects or some mixed results. **Mixed or weak:** small, indirect or conflicting studies; treat it as a '
                'hypothesis. **Failed to replicate or myth:** tested properly and not supported, or never tested at all. '
                '**Practical tool:** a sensible method with little direct research of its own; judge it by your own data.')


def evidence_table(rows):
    out = ['| Principle or claim | Evidence | What the research says |', '| --- | --- | --- |']
    for name, level, note in rows:
        assert level in EVIDENCE, level
        assert '|' not in name and '|' not in note
        out.append(f'| {name} | **{EVIDENCE[level]}** | {note} |')
    return '\n'.join(out)


QUIZ_LETTERS = collections.Counter()


def quiz_blocks(quiz):
    """Render questions and answers. Options are shuffled with a seed taken
    from the question text, so the order is stable between builds but the
    correct letter isn't always the same one. Write the correct option as 'A'."""
    qs, ans = [], []
    for i, q in enumerate(quiz, 1):
        assert q['a'] in 'ABCD'[: len(q['o'])], q
        rng = random.Random(int(hashlib.md5(q['q'].encode('utf-8')).hexdigest(), 16))
        order = list(range(len(q['o'])))
        rng.shuffle(order)
        options = [q['o'][k] for k in order]
        letter = 'ABCD'[order.index('ABCD'.index(q['a']))]
        QUIZ_LETTERS[letter] += 1
        opts = '\n'.join(f'    - {chr(65 + j)}) {o}' for j, o in enumerate(options))
        qs.append(f"{i}. {q['q']}\n{opts}")
        ans.append(f"{i}. **{letter}.** {q['why']}")
    return '\n'.join(qs), '\n'.join(ans)


def Q(q, right, *wrong, why):
    """Quiz question helper: the right answer first, then the distractors."""
    return {'q': q, 'o': [right, *wrong], 'a': 'A', 'why': why}


CAPSTONE = plan.CAPSTONE
WEEKS, PROJECT_WEEK, LAST_WEEK, LOAD = plan.assign()
FOLDERS = ['00 Baseline'] + [f'{m:02d} {t}' for m, (t, _, _) in enumerate(plan.MODULES, 1)]

PLAYBOOK = []   # (module, line) collected from every module, shown on the final page


def fmt_hours(h):
    if h == int(h):
        return f'{int(h)} hour' + ('' if h == 1 else 's')
    whole = int(h)
    mins = round((h - whole) * 60)
    if whole == 0:
        return f'{mins} minutes'
    return f'{whole} hour' + ('' if whole == 1 else 's') + f' {mins} minutes'


def code_of(m, l=None):
    return f'PD-M{m:02d}' + (f'-L{l:02d}' if l else '')


def lesson(m, l, *, outcome, split, principle, science, evidence, example, apply, resources, steps, proof,
           templates, mistakes, quiz, study, action, fulltime=None, extra_tasks=None):
    title = plan.MODULES[m - 1][1][l - 1][0]
    hours = plan.MODULES[m - 1][1][l - 1][1]
    code = code_of(m, l)
    sid = code.lower()
    a, b = WEEKS[(m, l)]
    q_text, a_text = quiz_blocks(quiz)
    assert 3 <= len(quiz) <= 5, code
    assert templates, f'{code} needs at least one template'
    assert len(mistakes) >= 3, f'{code} needs common mistakes'
    assert evidence, f'{code} needs an evidence check'
    parts = [
        '## The principle in one line',
        principle.strip(),
        '## The science',
        science.strip(),
        '## How strong is the evidence?',
        evidence_table(evidence),
        '## Everyday Kerala example',
        example.strip(),
        '## How to use it',
        apply.strip(),
        '## Free resources',
        res_table(resources),
        '## Action task',
        numbered(steps),
        f'**Proof to record:** {proof}',
    ]
    if fulltime:
        parts.append(f'**Full-time track:** {fulltime.strip()}')
    for t_title, t_body, t_lang in templates:
        parts += [f'## Template: {t_title}', fence(t_body, t_lang)]
    parts += [
        '## Common mistakes and misuses',
        mistakes_list(mistakes),
        '## Quiz',
        'Answer from memory first; that is retrieval practice. The answers are at the bottom of this page.',
        q_text,
        '## Progress checklist',
        'Tick these under **Your tasks** at the top of this page:',
        bullets([
            f'**Study:** {study}',
            f'**Action:** {action}. It is done when your proof is saved: {proof[0].lower() + proof[1:]}',
            f'**Quiz:** at least {len(quiz) - 1} right, or re-read the lesson and try again tomorrow.',
        ]),
        '## Answers',
        a_text,
    ]
    content = '\n\n'.join(parts)
    folder = FOLDERS[m]
    tasks = [
        {'id': f'{sid}-study', 'text': f'Study: {study}', 'kind': 'task', 'week': a},
        {'id': f'{sid}-action', 'text': f'Action: {action}', 'kind': 'project', 'week': b,
         'detail': f'**Proof to record:** {proof} Save it in your Playbook notebook ({folder}) and write in this task\'s note where it is.'},
        {'id': f'{sid}-quiz', 'text': f'Quiz: at least {len(quiz) - 1} right', 'kind': 'task', 'week': b},
    ]
    for tid, text, wk, detail in (extra_tasks or []):
        t = {'id': f'{sid}-{tid}', 'text': text, 'kind': 'project', 'week': wk if wk is not None else b}
        if detail:
            t['detail'] = detail
        tasks.append(t)
    return {
        'id': sid,
        'title': f'{code}: {title}',
        'kind': 'capstone' if m == CAPSTONE else 'level',
        'weeks': [a, b],
        'hours': hours,
        'summary': f'**Outcome:** {outcome} **Time:** about {fmt_hours(hours)} ({split}).',
        'content': content,
        'tasks': tasks,
    }


def module(m, *, overview, outcomes, lessons, project, project_steps, project_proof, rubric,
           short, flashcards, mistakes, tools, playbook, fulltime=None):
    title = plan.MODULES[m - 1][0]
    sid = f'pd-m{m:02d}'
    ws = [WEEKS[(m, l)] for l in range(1, len(lessons) + 1)]
    a = min(x[0] for x in ws)
    pw = PROJECT_WEEK[m]
    b = max(pw, max(x[1] for x in ws))
    hours = sum(s['hours'] for s in lessons) + plan.MODULES[m - 1][2]
    assert len(lessons) == len(plan.MODULES[m - 1][1]), f'module {m}: lesson count differs from plan'
    lesson_lines = [f"{s['title']} (about {fmt_hours(s['hours'])})" for s in lessons]
    rub = ['| Criterion | 1: Not yet | 2: Getting there | 3: Ready |', '| --- | --- | --- | --- |']
    for row in rubric:
        assert len(row) == 4 and all('|' not in c for c in row)
        rub.append('| ' + ' | '.join(row) + ' |')
    assert 5 <= len(flashcards) <= 10, f'module {m}: 5-10 flashcards'
    cards = ['| Front (say the answer aloud) | Back |', '| --- | --- |']
    for front, back in flashcards:
        assert '|' not in front and '|' not in back
        cards.append(f'| {front} | {back} |')
    assert playbook, f'module {m} needs Playbook lines'
    for line in playbook:
        PLAYBOOK.append((m, line))
    lesson_hours = sum(s['hours'] for s in lessons)
    paras = overview.strip().split('\n\n')
    assert len(paras) >= 2, 'the first paragraph becomes the summary; the rest is the overview'
    when = f'weeks {a}–{b}' if a != b else f'week {a}'
    letter, ptitle, _, _ = plan.part_of(m)
    parts = [
        f'*Part {letter}: {ptitle}.*',
        '## Overview',
        '\n\n'.join(paras[1:]),
        '## Outcomes',
        'By the end of this module you can:',
        bullets(outcomes),
        '## Time',
        f'About {fmt_hours(hours)} in total: {fmt_hours(lesson_hours)} of lessons and {fmt_hours(hours - lesson_hours)} for the module project. Part-time: {when}, with the module project due in week {pw}.',
    ]
    if fulltime:
        parts.append(f'**Full-time track:** {fulltime.strip()}')
    parts += [
        '## Lessons',
        numbered(lesson_lines),
        '## Copy-ready tools in this module',
        bullets(tools),
        f'## Module project: {project}',
        numbered(project_steps),
        f'**Proof to record:** {project_proof}',
        '## Add to your Personal Playbook',
        'Copy these lines into the Playbook note in Joplin (set up in Week 0). By the end of the course they become your one-page Personal Playbook.',
        bullets(playbook),
        '## Self-assessment rubric',
        'Score yourself honestly after the project. Move on when no row is a 1 and at least half the rows are 3. If a row is a 1, redo that part first.',
        '\n'.join(rub),
        '## Short on time?',
        'The minimum version, for weeks when PSC study, work or family leaves little time:',
        bullets(short),
        '## Revision flashcards',
        'Cover the right-hand column, read the front, say the answer aloud, then check. Put the ones you miss on your phone\'s flashcard app (AnkiDroid, if you did the Learning Capabilities course).',
        '\n'.join(cards),
        '## Top mistakes and misuses in this module',
        mistakes_list(mistakes),
    ]
    return {
        'id': sid,
        'title': f'Module {m}: {title}',
        'kind': 'capstone' if m == CAPSTONE else 'level',
        'weeks': [a, b],
        'hours': hours,
        'summary': paras[0],
        'content': '\n\n'.join(parts),
        'tasks': [
            {'id': f'{sid}-project', 'text': f'Module project: {project}', 'kind': 'project', 'week': pw,
             'detail': f'**Proof to record:** {project_proof} Save it in your Playbook notebook ({FOLDERS[m]}).'},
            {'id': f'{sid}-playbook', 'text': 'Personal Playbook: this module\'s lines added and edited in your own words', 'kind': 'task', 'week': pw},
            {'id': f'{sid}-rubric', 'text': 'Self-assessment: rubric scored, no row at 1', 'kind': 'exit', 'week': pw},
        ],
    }
