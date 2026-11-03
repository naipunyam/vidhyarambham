"""Shared helpers and the resource registry for the learning capabilities course.

Every link used in the course lives in R, with the status found when it was
checked on VDATE. Lessons refer to links by key, so the sources page is
generated from exactly the links the course uses. Lesson titles, hours and
part-time weeks come from plan.py, so the schedule is balanced in one place.
"""

import collections
import hashlib
import random

import plan

VDATE = '2026-11-03'
ASOF = 'as of November 2026'
CHECK = 'check current rules'

STATUS = {
    'v': f'verified {VDATE}',
    'vr': f'verified {VDATE}; check current rules',
    'vt': f'verified {VDATE} (headline checked)',
    'u': 'unverified: the site blocks automated checks',
}

G_SCI = 'Learning science: reviews and studies'
G_BOOK = 'Free books, courses and guides'
G_TOOLS = 'Free and open-source tools'
G_PSC = 'Kerala PSC and official study material'
G_NEWS = 'Current affairs sources'
G_HEALTH = 'Health and wellbeing'
G_AI = 'AI study tools and research'
G_LANG = 'Language learning'
G_FACT = 'Facts used in examples'

GROUP_ORDER = [G_SCI, G_BOOK, G_TOOLS, G_PSC, G_NEWS, G_LANG, G_AI, G_HEALTH, G_FACT]


def _r(title, url, s='v', group='Other'):
    assert ' ' not in url and ')' not in url and '(' not in url, url
    return {'title': title, 'url': url, 's': s, 'group': group}


CS = 'https://socialsci.libretexts.org/Bookshelves/Counseling_and_Guidance/College_Success_%28OpenStax%29'

R = {
    # ---- Learning science: reviews and studies
    'dunlosky-aft': _r('Dunlosky (2013), "Strengthening the Student Toolbox", American Educator', 'https://www.aft.org/ae/fall2013/dunlosky', 'v', G_SCI),
    'dunlosky-aps': _r('Dunlosky et al. (2013), "Improving Students\' Learning With Effective Learning Techniques", APS summary with the full paper', 'https://www.psychologicalscience.org/publications/journals/pspi/learning-techniques.html', 'v', G_SCI),
    'roediger': _r('Roediger and Karpicke (2006), "Test-Enhanced Learning" (PDF)', 'https://psychology.ecu.edu/wp-content/pv-uploads/sites/216/2019/03/Roediger-Karpicke-2006.pdf', 'v', G_SCI),
    'karpicke-blunt': _r('Purdue University (20 January 2011): retrieval practice beats concept mapping (Karpicke and Blunt, Science)', 'https://www.purdue.edu/newsroom/research/2011/110120KarpickeScience.html', 'v', G_SCI),
    'murre': _r('Murre and Dros (2015), "Replication and Analysis of Ebbinghaus\' Forgetting Curve", PLOS ONE', 'https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0120644', 'v', G_SCI),
    'pashler': _r('Pashler, McDaniel, Rohrer and Bjork (2008), "Learning Styles: Concepts and Evidence"', 'https://digitalcommons.usf.edu/psy_facpub/1765/', 'v', G_SCI),
    'dekker': _r('Dekker et al. (2012), "Neuromyths in Education", Frontiers in Psychology', 'https://www.frontiersin.org/articles/10.3389/fpsyg.2012.00429/full', 'v', G_SCI),
    'aps-speed': _r('APS (14 January 2016): speed-reading promises are too good to be true (Rayner et al.)', 'https://www.psychologicalscience.org/news/releases/speed-reading-promises-are-too-good-to-be-true-scientists-find.html', 'v', G_SCI),
    'ophir': _r('ScienceDaily (26 August 2009): heavy media multitaskers pay a mental price (Ophir, Nass and Wagner, PNAS)', 'https://www.sciencedaily.com/releases/2009/08/090825113133.htm', 'v', G_SCI),
    'ls-laptop': _r('The Learning Scientists blog (21 February 2019): laptop versus longhand notes, a failed replication', 'https://www.learningscientists.org/blog/2019/2/21-1', 'v', G_SCI),
    'wm-training': _r('Melby-Lervåg, Redick and Hulme (2016): working memory training does not improve far transfer', 'https://ora.ox.ac.uk/objects/uuid:daa9a729-f17b-4e45-97c0-cff5075ea404', 'v', G_SCI),
    'dresler': _r('Dresler et al. (2017), "Mnemonic Training Reshapes Brain Networks to Support Superior Memory", Neuron', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5439266/', 'v', G_SCI),
    'gollwitzer': _r('Gollwitzer and Sheeran (2006), implementation intentions meta-analysis (free PDF)', 'https://kops.uni-konstanz.de/entities/publication/2e749bfb-8533-437c-8203-7e788c910c5f', 'v', G_SCI),
    'lally': _r('University of Surrey (21 January 2026): does it really take 66 days to form a habit? (Dr Pippa Lally)', 'https://www.surrey.ac.uk/news/does-it-really-take-66-days-form-habit-we-asked-expert-dr-pippa-lally', 'v', G_SCI),
    'sirois': _r('Sirois and Pychyl (2013), "Procrastination and the Priority of Short-Term Mood Regulation" (free author copy)', 'https://eprints.whiterose.ac.uk/id/eprint/91793/', 'v', G_SCI),
    'wohl': _r('BPS Research Digest (4 May 2010): to cure procrastination, forgive yourself (Wohl, Pychyl and Bennett)', 'https://bps.org.uk/research-digest/cure-procrastination-forgive-yourself', 'v', G_SCI),
    'biwer': _r('Biwer et al. (2023), "Understanding effort regulation: Comparing Pomodoro breaks and self-regulated breaks"', 'https://cris.maastrichtuniversity.nl/en/publications/understanding-effort-regulation-comparing-pomodoro-breaks-and-sel', 'v', G_SCI),
    'macnamara': _r('APS (2 July 2014): becoming an expert takes more than practice (Macnamara, Hambrick and Oswald)', 'https://www.psychologicalscience.org/news/releases/becoming-an-expert-takes-more-than-practice.html', 'v', G_SCI),
    'fiorella': _r('Fiorella (2023), "Learning by Teaching", in an APA Division 2 e-book (PDF)', 'https://www.unh.edu/teaching-learning-resource-hub/sites/default/files/media/2023-06/itow-learning-by-teaching-fiorella.pdf', 'v', G_SCI),
    'rb-writing': _r('University of Chicago (2011): writing about worries eases anxiety and improves test performance (Ramirez and Beilock, Science)', 'https://news.uchicago.edu/story/writing-about-worries-eases-anxiety-and-improves-test-performance', 'v', G_SCI),
    'cese-clt': _r('NSW Centre for Education Statistics and Evaluation (2017), "Cognitive load theory: Research that teachers really need to understand" (PDF)', 'https://education.nsw.gov.au/content/dam/main-education/about-us/educational-data/cese/2017-cognitive-load-theory.pdf', 'v', G_SCI),

    # ---- Free books, courses and guides
    'ls-materials': _r('The Learning Scientists: free posters, slides and bookmarks for the six strategies', 'https://www.learningscientists.org/downloadable-materials', 'v', G_BOOK),
    'ls-retrieval': _r('The Learning Scientists: retrieval practice materials', 'https://www.learningscientists.org/retrieval-practice', 'v', G_BOOK),
    'ls-spacing': _r('The Learning Scientists: spaced practice materials', 'https://www.learningscientists.org/spaced-practice', 'v', G_BOOK),
    'ls-interleaving': _r('The Learning Scientists: interleaving materials', 'https://www.learningscientists.org/interleaving', 'v', G_BOOK),
    'ls-elaboration': _r('The Learning Scientists: elaboration materials', 'https://www.learningscientists.org/elaboration', 'v', G_BOOK),
    'ls-concrete': _r('The Learning Scientists: concrete examples materials', 'https://www.learningscientists.org/concrete-examples', 'v', G_BOOK),
    'ls-dual': _r('The Learning Scientists: dual coding materials', 'https://www.learningscientists.org/dual-coding', 'v', G_BOOK),
    'retrievalpractice': _r('RetrievalPractice.org (Pooja Agarwal): free guides and research', 'https://www.retrievalpractice.org/', 'v', G_BOOK),
    'ncase': _r('Nicky Case, "How To Remember Anything Forever-ish" (interactive comic, public domain)', 'https://ncase.me/remember/', 'v', G_BOOK),
    'lhtl': _r('"Learning How to Learn" by Barbara Oakley and Terrence Sejnowski (Coursera, free to enrol; certificate paid)', 'https://www.coursera.org/learn/learning-how-to-learn', 'vr', G_BOOK),
    'os-psych': _r('OpenStax, Psychology 2e (free, CC BY-NC-SA 4.0)', 'https://openstax.org/books/psychology-2e/pages/preface', 'v', G_BOOK),
    'os-psych-8-1': _r('OpenStax Psychology 2e, 8.1 How Memory Functions', 'https://openstax.org/books/psychology-2e/pages/8-1-how-memory-functions', 'v', G_BOOK),
    'os-psych-4-3': _r('OpenStax Psychology 2e, 4.3 Stages of Sleep', 'https://openstax.org/books/psychology-2e/pages/4-3-stages-of-sleep', 'v', G_BOOK),
    'os-psych-7-3': _r('OpenStax Psychology 2e, 7.3 Problem Solving', 'https://openstax.org/books/psychology-2e/pages/7-3-problem-solving', 'v', G_BOOK),
    'os-psych-3-4': _r('OpenStax Psychology 2e, 3.4 The Brain and Spinal Cord', 'https://openstax.org/books/psychology-2e/pages/3-4-the-brain-and-spinal-cord', 'v', G_BOOK),
    'os-psych-14-4': _r('OpenStax Psychology 2e, 14.4 Regulation of Stress', 'https://openstax.org/books/psychology-2e/pages/14-4-regulation-of-stress', 'v', G_BOOK),
    'os-cs': _r('OpenStax, College Success (free, CC BY-NC-SA 4.0)', 'https://openstax.org/books/college-success/pages/preface', 'v', G_BOOK),
    'os-cs-lt': _r('College Success (OpenStax) on LibreTexts: all 12 chapters', CS, 'v', G_BOOK),
    'os-cs-3': _r('College Success, chapter 3: Managing Your Time and Priorities (procrastination, time management, goals)', CS + '/03%3A_Managing_Your_Time_and_Priorities', 'v', G_BOOK),
    'os-cs-5': _r('College Success, chapter 5: Reading and Notetaking (SQ3R, Cornell method)', CS + '/05%3A_Reading_and_Notetaking', 'v', G_BOOK),
    'os-cs-6': _r('College Success, chapter 6: Studying, Memory, and Test Taking', CS + '/06%3A_Studying_Memory_and_Test_Taking', 'v', G_BOOK),
    'os-cs-6-3': _r('College Success, 6.3 Test Taking (including test anxiety)', CS + '/06%3A_Studying_Memory_and_Test_Taking/6.03%3A_Test_Taking', 'v', G_BOOK),
    'os-prealg': _r('OpenStax, Prealgebra 2e (free, CC BY-NC-SA 4.0)', 'https://openstax.org/books/prealgebra-2e/pages/preface', 'v', G_BOOK),
    'os-prealg-6-1': _r('OpenStax Prealgebra 2e, 6.1 Understand Percent', 'https://openstax.org/books/prealgebra-2e/pages/6-1-understand-percent', 'v', G_BOOK),
    'os-phil-2': _r('OpenStax Introduction to Philosophy, chapter 2: Critical Thinking, Research, Reading, and Writing', 'https://openstax.org/books/introduction-philosophy/pages/2-introduction', 'v', G_BOOK),
    'os-phil-5': _r('OpenStax Introduction to Philosophy, chapter 5: Logic and Reasoning', 'https://openstax.org/books/introduction-philosophy/pages/5-introduction', 'v', G_BOOK),
    'sm-20rules': _r('Piotr Wozniak, "Effective learning: Twenty rules of formulating knowledge" (SuperMemo, 1999)', 'https://www.supermemo.com/en/blog/twenty-rules-of-formulating-knowledge', 'v', G_BOOK),
    'cornell-lsc': _r('Cornell University Learning Strategies Center: the Cornell note-taking system', 'https://lsc.cornell.edu/how-to-study/taking-notes/cornell-note-taking-system/', 'v', G_BOOK),

    # ---- Free and open-source tools
    'ankidroid-play': _r('AnkiDroid Flashcards on Google Play (free, open source)', 'https://play.google.com/store/apps/details?id=com.ichi2.anki', 'v', G_TOOLS),
    'ankidroid-gh': _r('AnkiDroid source code and other download options (GitHub, GPL-3.0)', 'https://github.com/ankidroid/Anki-Android', 'v', G_TOOLS),
    'ankidroid-manual': _r('AnkiDroid manual', 'https://docs.ankidroid.org/', 'v', G_TOOLS),
    'anki-apps': _r('Anki for computers (free) and AnkiWeb sync', 'https://apps.ankiweb.net/', 'v', G_TOOLS),
    'anki-start': _r('Anki manual: Getting Started (cards, decks, notes, note types)', 'https://docs.ankiweb.net/getting-started.html', 'v', G_TOOLS),
    'anki-study': _r('Anki manual: Studying (the four answer buttons)', 'https://docs.ankiweb.net/studying.html', 'v', G_TOOLS),
    'anki-edit': _r('Anki manual: Editing (cloze deletion and image occlusion)', 'https://docs.ankiweb.net/editing.html', 'v', G_TOOLS),
    'anki-deck': _r('Anki manual: Deck Options (daily limits, FSRS, desired retention)', 'https://docs.ankiweb.net/deck-options.html', 'v', G_TOOLS),
    'anki-io-forum': _r('Anki forums (April 2024): image occlusion in AnkiDroid 2.17', 'https://forums.ankiweb.net/t/image-occlusion-ankidroid-v2-17/43841', 'v', G_TOOLS),
    'joplin': _r('Joplin: free, open-source notes for Android, Windows and Linux', 'https://joplinapp.org/', 'v', G_TOOLS),
    'joplin-help': _r('Joplin help: features, sync options, encryption and apps', 'https://joplinapp.org/help/', 'v', G_TOOLS),
    'obsidian': _r('Obsidian pricing: free without limits; optional paid sync (not open source)', 'https://obsidian.md/pricing', 'vr', G_TOOLS),
    'logseq': _r('Logseq: privacy-first, open-source knowledge management', 'https://logseq.com/', 'v', G_TOOLS),
    'logseq-fdroid': _r('Logseq for Android on F-Droid (AGPL-3.0)', 'https://f-droid.org/en/packages/com.logseq.app/', 'v', G_TOOLS),
    'loop': _r('Loop Habit Tracker (free, open source, GPLv3)', 'https://loophabits.org/', 'v', G_TOOLS),
    'wellbeing': _r('Android Help: manage how you spend time with Digital Wellbeing', 'https://support.google.com/android/answer/9346420?hl=en', 'vr', G_TOOLS),

    # ---- Kerala PSC and official study material
    'psc-home': _r('Kerala Public Service Commission (official website)', 'https://www.keralapsc.gov.in/', 'v', G_PSC),
    'psc-syllabus': _r('Kerala PSC: post-wise syllabus', 'https://www.keralapsc.gov.in/syllabus1', 'vr', G_PSC),
    'psc-pyq': _r('Kerala PSC: previous question papers', 'https://www.keralapsc.gov.in/previous-question-papers', 'v', G_PSC),
    'psc-keys': _r('Kerala PSC: answer keys for OMR exams', 'https://www.keralapsc.gov.in/answerkey_omrexams', 'vr', G_PSC),
    'psc-omr': _r('Kerala PSC: instructions to candidates for OMR examinations (PDF)', 'https://keralapsc.gov.in/sites/default/files/inline-files/new-omr-instructionsENGLISH.pdf', 'vr', G_PSC),
    'psc-cpe-2022': _r('Kerala PSC: Degree Level Common Preliminary Examination notice, 2022 (PDF)', 'https://keralapsc.gov.in/sites/default/files/2022-07/degree_level_cpe__for_confirmation_.pdf', 'vr', G_PSC),
    'scert': _r('SCERT Kerala: school textbooks', 'https://scert.kerala.gov.in/', 'v', G_PSC),
    'ncert': _r('NCERT: free textbooks (PDF)', 'https://ncert.nic.in/textbook.php', 'u', G_PSC),

    # ---- Current affairs sources
    'pib': _r('Press Information Bureau (PIB), Government of India', 'https://www.pib.gov.in/', 'v', G_NEWS),
    'newsonair': _r('All India Radio News (News Services Division)', 'https://newsonair.gov.in/', 'v', G_NEWS),
    'prd': _r('Information and Public Relations Department, Government of Kerala', 'https://www.prd.kerala.gov.in/', 'v', G_NEWS),

    # ---- Language learning
    'learnenglish': _r('British Council LearnEnglish (free)', 'https://learnenglish.britishcouncil.org/', 'v', G_LANG),
    'langtransfer': _r('Language Transfer: free audio courses', 'https://www.languagetransfer.org/', 'v', G_LANG),

    # ---- AI
    'oai-study': _r('OpenAI (29 July 2025): Introducing study mode in ChatGPT', 'https://openai.com/index/chatgpt-study-mode/', 'vr', G_AI),
    'gemini-guided': _r('Google (6 August 2025): Guided Learning in Gemini', 'https://blog.google/outreach-initiatives/education/guided-learning/', 'vr', G_AI),
    'wharton-ai': _r('Knowledge at Wharton (27 August 2024): without guardrails, generative AI can harm education (Bastani et al.)', 'https://knowledge.wharton.upenn.edu/article/without-guardrails-generative-ai-can-harm-education', 'v', G_AI),

    # ---- Health
    'aasm': _r('AASM and Sleep Research Society (2015): recommended sleep for adults (PDF)', 'https://www.aasm.org/resources/pdf/adultsleepdurationconsensus.pdf', 'v', G_HEALTH),
    'who-pa': _r('World Health Organization: physical activity fact sheet (26 June 2024)', 'https://www.who.int/news-room/fact-sheets/detail/physical-activity', 'v', G_HEALTH),
    'icmr-diet': _r('All India Radio News (9 May 2024): ICMR releases updated Dietary Guidelines for Indians', 'https://newsonair.gov.in/icmr-releases-updated-dietary-guidelines-for-indians-in-2024', 'v', G_HEALTH),
    'telemanas': _r('Tele-MANAS: free 24x7 mental health helpline, 14416 or 1-800-891-4416', 'https://ehrc.iiitb.ac.in/project/tele-manas', 'v', G_HEALTH),

    # ---- Facts used in examples
    'jnanpith': _r('Wikipedia: Jnanpith Award (list of recipients)', 'https://en.wikipedia.org/wiki/Jnanpith_Award', 'v', G_FACT),
    'kl-rivers': _r('Wikipedia: List of rivers of Kerala', 'https://en.wikipedia.org/wiki/List_of_rivers_of_Kerala', 'v', G_FACT),
    'major-system': _r('Wikipedia: Mnemonic major system', 'https://en.wikipedia.org/wiki/Mnemonic_major_system', 'v', G_FACT),
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
    'limited': 'Limited',
    'none': 'No good evidence',
}

EVIDENCE_KEY = ('**Strong:** many studies, in labs and real classrooms, agree. **Moderate:** good studies, '
                'but fewer, narrower or with mixed results. **Limited:** small or indirect studies; use it as a '
                'practical tool and judge it by your own results. **No good evidence:** tested and not supported.')


def evidence_table(rows):
    out = ['| Technique or claim | Evidence | What the research says |', '| --- | --- | --- |']
    for name, level, note in rows:
        assert level in EVIDENCE, level
        assert '|' not in name and '|' not in note
        out.append(f'| {name} | **{EVIDENCE[level]}** | {note} |')
    return '\n'.join(out)


QUIZ_LETTERS = collections.Counter()


def quiz_blocks(quiz):
    """Render questions and answers. Options are shuffled with a seed taken
    from the question text, so the order is stable between builds but the
    correct letter isn't always the same one."""
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


CAPSTONE = plan.CAPSTONE
WEEKS, PROJECT_WEEK, ANKI_START, LAST_WEEK, LOAD = plan.assign()

FOLDERS = ['00 Baseline', '01 Brain', '02 Myths', '03 Strategies', '04 Anki', '05 Focus', '06 Habits',
           '07 Metacognition', '08 Understanding', '09 Notes', '10 Reading', '11 Memory', '12 Exam',
           '13 Practice', '14 Maths', '15 Language', '16 Thinking', '17 AI', '18 Knowledge base',
           '19 Health', '20 Teaching', '21 Capstone']


def fmt_hours(h):
    if h == int(h):
        return f'{int(h)} hour' + ('' if h == 1 else 's')
    whole = int(h)
    mins = round((h - whole) * 60)
    if whole == 0:
        return f'{mins} minutes'
    return f'{whole} hour' + ('' if whole == 1 else 's') + f' {mins} minutes'


def code_of(m, l=None):
    return f'LRN-M{m:02d}' + (f'-L{l:02d}' if l else '')


def lesson(m, l, *, outcome, split, core, example, evidence, resources, steps, proof,
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
        '## Core lesson',
        core.strip(),
        '## Local example',
        example.strip(),
        '## How strong is the evidence?',
        evidence_table(evidence),
        '## Free resources',
        res_table(resources),
        '## Action task (on your PSC material)',
        numbered(steps),
        f'**Proof to record:** {proof}',
    ]
    if fulltime:
        parts.append(f'**Full-time track:** {fulltime.strip()}')
    for t_title, t_body, t_lang in templates:
        parts += [f'## Template: {t_title}', fence(t_body, t_lang)]
    parts += [
        '## Common mistakes',
        mistakes_list(mistakes),
        '## Quiz',
        'Answer from memory first: that is retrieval practice. The answers are at the bottom of this page.',
        q_text,
        '## Progress checklist',
        'Tick these under **Your tasks** at the top of this page:',
        bullets([
            f'**Study:** {study}',
            f'**Action:** {action}. It is done when your proof is saved: {proof[0].lower() + proof[1:]}',
            f'**Quiz:** at least {len(quiz) - 1} right, or re-read the core lesson and try again tomorrow.',
        ]),
        '## Answers',
        a_text,
    ]
    content = '\n\n'.join(parts)
    folder = FOLDERS[m]
    tasks = [
        {'id': f'{sid}-study', 'text': f'Study: {study}', 'kind': 'task', 'week': a},
        {'id': f'{sid}-action', 'text': f'Action: {action}', 'kind': 'project', 'week': b,
         'detail': f'**Proof to record:** {proof} Save it in your Learning Folder ({folder}) and write in this task\'s note where it is.'},
        {'id': f'{sid}-quiz', 'text': f'Quiz: at least {len(quiz) - 1} right', 'kind': 'task', 'week': b},
    ]
    for tid, text, wk, detail in (extra_tasks or []):
        t = {'id': f'{sid}-{tid}', 'text': text, 'kind': 'project', 'week': wk}
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
           short, flashcards, mistakes, tools, fulltime=None):
    title = plan.MODULES[m - 1][0]
    sid = f'lrn-m{m:02d}'
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
    lesson_hours = sum(s['hours'] for s in lessons)
    paras = overview.strip().split('\n\n')
    assert len(paras) >= 2, 'the first paragraph becomes the summary; the rest is the overview'
    when = f'weeks {a}–{b}' if a != b else f'week {a}'
    parts = [
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
        '## Tools this module adds to your learning system',
        bullets(tools),
        f'## Module project: {project}',
        numbered(project_steps),
        f'**Proof to record:** {project_proof}',
        '## Self-assessment rubric',
        'Score yourself honestly after the project. Move on when no row is a 1 and at least half the rows are 3. If a row is a 1, redo that part first.',
        '\n'.join(rub),
        '## Short on time?',
        'The minimum version, for weeks when PSC study, work or family leaves little time:',
        bullets(short),
        '## Revision flashcards',
        'Cover the right-hand column, read the front, say the answer aloud, then check. Add the ones you miss to AnkiDroid (from Module 4 on).',
        '\n'.join(cards),
        '## Top mistakes in this module',
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
             'detail': f'**Proof to record:** {project_proof} Save it in your Learning Folder ({FOLDERS[m]}).'},
            {'id': f'{sid}-rubric', 'text': 'Self-assessment: rubric scored, no row at 1', 'kind': 'exit', 'week': pw},
        ],
    }
