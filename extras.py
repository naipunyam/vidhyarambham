"""Course-level sections: start here, schedule, week 0, baseline tests, the
learning system track, the toolkit, the final retest, what next, glossary
and the sources page."""
from common import (R, STATUS, VDATE, CHECK, GROUP_ORDER, EVIDENCE_KEY, FOLDERS, WEEKS, PROJECT_WEEK,
                    ANKI_START, LAST_WEEK, LOAD, link, rules, fence, bullets, numbered, table, fmt_hours)
import plan
import tests
import tools

FULL_TIME_WEEK = 0.375   # one course week = 0.375 calendar weeks at full-time pace
FINAL = LAST_WEEK

MODULE_MAP = [
    (1, 'How the brain works for study: attention, working memory, encoding, sleep, retrieval, forgetting', 'A one-page model of how you learn, and your first study log'),
    (2, 'Learning styles, rereading, highlighting, multitasking, speed-reading claims', 'Your "stop doing" list'),
    (3, 'Retrieval, spacing, interleaving, elaboration, concrete examples, dual coding', 'Revision tab and a six-strategy study session'),
    (4, 'AnkiDroid from zero: good cards, cloze, image occlusion, daily reviews, workload', 'A 100+ card PSC deck reviewed for 30 days'),
    (5, 'Attention span, Pomodoro, time-blocking, Android distraction control', 'Focus tab, a quiet phone and a time-blocked week'),
    (6, 'Why we procrastinate, if-then plans, tiny habits, rewards, restarting', 'If-then plans and habits tracked in Loop'),
    (7, 'Illusions of knowing, self-testing, confidence ratings, weekly reviews', 'Your weekly learning review routine'),
    (8, 'Feynman technique, self-explanation, good questions, concept maps, first principles', 'Five recorded Feynman explanations'),
    (9, 'Cornell notes, outlines, mind maps, sketchnotes, notes into questions and cards', 'Notes that turn into recall practice'),
    (10, 'SQ3R, skimming and scanning, speed versus comprehension, newspapers', 'Reading routine and current-affairs system'),
    (11, 'Chunking, acronyms, stories, memory palace, pegs, the major system', 'A memory palace for a real PSC topic'),
    (12, 'Syllabus map, PYQ analysis, mocks, error log, negative marking, 12-week plan, anxiety', 'Syllabus map, PYQ analysis, error log and 12-week plan'),
    (13, 'Deliberate practice, feedback loops, self-directed learning projects', 'A practice loop and a learning project plan'),
    (14, 'Mental maths, PSC arithmetic, reasoning practice', 'Maths and reasoning practice system'),
    (15, 'English for PSC, input, shadowing, vocabulary with AnkiDroid, PSC Malayalam, any new language', 'Language routine and vocabulary deck'),
    (16, 'Critical thinking, logical reasoning, mental models, problem solving, cognitive biases', 'Thinking checklist and reasoning practice'),
    (17, 'AI as a Socratic tutor, quizzes, checking AI answers, avoiding over-reliance', 'Tutor prompts and a fact-check routine'),
    (18, 'Linked notes, Joplin or Logseq, a PSC knowledge base', 'Your knowledge base'),
    (19, 'Sleep, exercise, food, breaks, stress', 'Sleep, movement and stress plan'),
    (20, 'Learning by teaching, study groups', 'A taught lesson and study-group rules'),
    (21, 'A 30-day learning sprint with before and after tests', 'Sprint report and your learning system for life'),
]

BRIEF = [
    ('How the brain learns: attention, working memory, encoding, consolidation, retrieval, forgetting curve, cognitive load, neuroplasticity', 1),
    ('Myths to drop: learning styles, rereading and highlighting, multitasking, speed-reading claims', 2),
    ('The six strategies: retrieval, spacing, interleaving, elaboration, concrete examples, dual coding', 3),
    ('Spaced repetition from zero: AnkiDroid, good cards, cloze, image occlusion, daily reviews, workload', 4),
    ('Focus and deep work: Pomodoro, time-blocking, Android distractions, attention span', 5),
    ('Motivation and procrastination: causes, implementation intentions, tiny habits, rewards', 6),
    ('Metacognition: self-testing, judging what you know, weekly learning reviews', 7),
    ('Deep understanding: Feynman technique, self-explanation, concept maps, first principles, good questions', 8),
    ('Note-making: Cornell, outlines, mind maps, sketchnotes, notes into questions and cards', 9),
    ('Reading: SQ3R, skimming and scanning, speed versus comprehension, textbooks, newspapers', 10),
    ('Memory techniques: memory palace, pegs, major system, chunking, acronyms, stories', 11),
    ('Exam mastery: syllabus mapping, plans and revision cycles, PYQs, mocks, error logs, time, negative marking, anxiety', 12),
    ('Deliberate practice and skill acquisition: feedback loops, self-directed projects', 13),
    ('Numerical ability, reasoning practice, mental maths', 14),
    ('Language learning: English, input, shadowing, vocabulary with spaced repetition, any language', 15),
    ('Thinking skills: critical thinking, logic, mental models, problem solving, biases', 16),
    ('Learning with AI: Socratic tutor, quizzes, explanations, checking answers, over-reliance', 17),
    ('Personal knowledge management: linked notes, open-source tools', 18),
    ('Brain health: sleep, exercise, nutrition, breaks, stress', 19),
    ('Teaching others and study groups', 20),
    ('Capstone: a 30-day sprint with before and after tests', 21),
]

REVIEW_WEEKS = [1, 4, 8, 12, 16, 20, 24]
ANKI_DAYS = [(7, ANKI_START + 1), (14, ANKI_START + 2), (21, ANKI_START + 3), (30, ANKI_START + 4)]


def total_hours():
    return sum(LOAD.values())


def week_plan():
    """Return {week: (items, hours)} at part-time pace."""
    plan_ = {0: (['Week 0: Learning Folder, Learning Workbook, PSC material and baseline tests'], 4.0)}

    def add(w, item, hrs):
        items, h = plan_.get(w, ([], 0))
        if item and item not in items:
            items.append(item)
        plan_[w] = (items, h + hrs)

    for m, (title, lessons, ph) in enumerate(plan.MODULES, 1):
        for l, (lt, h) in enumerate(lessons, 1):
            a, b = WEEKS[(m, l)]
            label = f'LRN-M{m:02d}-L{l:02d}' + ('' if a == b else f' (weeks {a}–{b})')
            for w in range(a, b + 1):
                add(w, label, h / (b - a + 1))
        add(PROJECT_WEEK[m], f'Module {m} project', ph)
    for w in range(1, FINAL + 1):
        add(w, 'weekly review', plan.REVIEW_H)
        if ANKI_START <= w < ANKI_START + 5:
            add(w, 'daily AnkiDroid reviews', plan.ANKI_H if w < ANKI_START + 4 else plan.ANKI_H / 3)
    add(FINAL, 'final retests and checklist', 1.5)
    return plan_


def full_time_rows():
    rows = []
    notes = {
        1: 'Week 0 and the baseline tests (the 24-hour recall needs a second short session the next day). Then Modules 1–2.',
        2: 'AnkiDroid starts (Module 4). The 30-day review runs in real days, to about calendar week 6, alongside the next modules.',
        6: 'Module 12 ends: make your 12-week PSC plan. Read LRN-M21-L01 now and start the 30-day capstone sprint at the end of this week.',
        7: 'Sprint days 1–7, with Modules 13–14 alongside (about 45–60 minutes of sprint a day, plus lessons).',
        8: 'Sprint continues; Modules 15–17 alongside.',
        9: 'Sprint continues; Modules 18–20 alongside. The app shows LRN-M21-L01 now: you have already done it.',
        10: 'Finish the sprint days. Keep AnkiDroid and the weekly review going.',
        11: 'Sprint after-tests and reflection, the final retests, and your learning system document.',
    }
    names = {m: plan.MODULES[m - 1][0] for m in range(1, 22)}
    c = 1
    while True:
        lo = int((c - 1) / FULL_TIME_WEEK + 0.999) if c > 1 else 0
        hi = min(int(c / FULL_TIME_WEEK - 0.001), FINAL)
        mods = []
        for m in range(1, 22):
            ws = [WEEKS[(m, l)] for l in range(1, len(plan.MODULES[m - 1][1]) + 1)]
            s, e = min(x[0] for x in ws), max(max(x[1] for x in ws), PROJECT_WEEK[m])
            if s <= hi and e >= lo:
                mods.append(f'M{m:02d}')
        rows.append((str(c), f'{lo}–{hi}', ', '.join(mods) or '—', notes.get(c, '')))
        if hi >= FINAL:
            break
        c += 1
    return rows


def start_section():
    total = total_hours()
    map_rows = []
    for m, does, output in MODULE_MAP:
        ws = [WEEKS[(m, l)] for l in range(1, len(plan.MODULES[m - 1][1]) + 1)]
        a, b = min(x[0] for x in ws), max(max(x[1] for x in ws), PROJECT_WEEK[m])
        wl = f'{a}' if a == b else f'{a}–{b}'
        map_rows.append((f'{m}. {plan.MODULES[m - 1][0]}', wl, does, output))
    brief_rows = [(t, f'Module {m}') for t, m in BRIEF]
    ft_weeks = len(full_time_rows())
    content = f"""
## What this course is

A free, practical "learn how to learn" course that you do on your own study material. Every lesson teaches one evidence-based method, says honestly how strong the research behind it is, and ends with an action task on your real Kerala PSC subjects: GK, current affairs, the Constitution, Kerala, maths and reasoning, English and Malayalam. Lesson by lesson, the tasks build one **personal learning system** that you keep using for PSC and for everything you learn after it: AI skills, business, languages.

It is written for a PSC aspirant near Kuttiady in Kozhikode district with an Android phone, an old laptop and ₹0 to spend. It works for anyone preparing for a competitive exam.

## By the end you will have

- **Measured results:** four baseline tests in week 0 (list recall after 10 minutes and 24 hours, reading speed with comprehension, focus duration, digit span), repeated with fresh versions in week {FINAL}
- **An AnkiDroid deck** of 100 or more well-made cards on one PSC topic, reviewed every day for 30 days, and a daily review habit
- **A memory palace** that holds a real PSC topic
- **Five recorded Feynman explanations** of PSC topics, each improved after listening back
- **A previous-year question analysis and an error log** for your target exam
- **A complete 12-week PSC study and revision plan**
- **A lesson you taught** to a family member or study partner
- **A 30-day learning sprint** with before and after tests and a reflection report
- **The Learning Workbook and Learning Folder** that hold the whole system: planner, revision schedule, card checklist, error log, Feynman template and weekly review

## How long it takes

{table(['Pace', 'Calendar time', 'Hours a week', 'Total work'], [
    ('Part-time (the default)', f'Week 0, then {FINAL} weeks: about 6.5 months', 'About 6 (5 to 7)', f'About {total:.0f} hours'),
    ('Full-time', f'About {ft_weeks} weeks', 'About 15', f'About {total:.0f} hours'),
])}

Pick your pace and start date on the course page; the app then shows your week and what is due. Two things take real days at any pace: the 30-day AnkiDroid review and the 30-day capstone sprint. Much of the action-task time is also PSC study, because you do it on your own syllabus.

## Honest expectations

- **Your list recall will improve the most,** because techniques such as chunking and the memory palace work quickly. The list test shows it.
- **Your digit span will change little.** Working memory capacity is fairly stable. A large review of "brain training" found gains on trained tasks but no convincing improvement in reading, arithmetic or intelligence ({link('wm-training', 'Melby-Lervåg and others, 2016')}). A gain of one digit usually comes from a better strategy, such as chunking.
- **Reading speed will rise a little; comprehension can rise more.** No method lets you read several times faster with full understanding ({link('aps-speed', 'APS, 2016')}). The test reports your **effective reading rate**: speed multiplied by comprehension.
- **Focus depends mostly on habits and your phone.** It usually improves a lot once the phone is out of reach.
- **What matters most is your exam score.** Retrieval practice and spaced practice have the strongest evidence of any study methods ({link('dunlosky-aft', 'Dunlosky, 2013')}). The capstone measures the change on a real PSC subject.
- **Some weeks will go badly.** The weekly review is where you notice and adjust, without guilt.

## How strong is the evidence?

Every lesson has a short evidence table. The ratings mean:

{EVIDENCE_KEY}

When research is thin, the lesson says so. Some popular methods in this course (the Feynman technique, Pomodoro, SQ3R, mind maps) have little direct research. They are included because they put well-supported principles into practice, and you will test them on your own results.

## How each lesson works

1. **ID, title, outcome and time** at the top, such as LRN-M01-L01
2. **Core lesson:** the idea, explained simply
3. **Local example:** the idea used by PSC aspirants in Kozhikode district
4. **How strong is the evidence?** an honest rating
5. **Free resources:** exactly what to study, how long it takes, and when the link was checked
6. **Action task:** real work on your PSC material, and the **proof to record**
7. **Template:** copy-ready tools for your Learning Workbook or notebook
8. **Common mistakes** and how to avoid them
9. **Quiz:** 3 to 5 questions, with answers at the very bottom
10. **Progress checklist:** the ticks under **Your tasks**

Each module starts with an overview page: outcomes, time, the tools it adds, the module project, a self-assessment rubric, a "short on time?" version and revision flashcards.

## Where each topic is taught

The modules are ordered so your system starts working early: the six strategies and AnkiDroid in the first month, focus, habits and self-testing in the second, and exam mastery by week {PROJECT_WEEK[12]}, so your 12-week PSC plan runs during the rest of the course.

{table(['Topic', 'Module'], brief_rows)}

## Module map

{table(['Module', 'Part-time weeks', 'What you learn', 'What you add to your system'], map_rows)}

## PSC exam soon? Take the fast path

- **Exam within 8 weeks:** do Week 0, then Module 3 (the six strategies), Module 4 (AnkiDroid), LRN-M05-L03 (phone), Module 12 (exam mastery) and LRN-M19-L01 (sleep). Return to the rest after the exam.
- **Exam within 12 to 16 weeks:** follow the normal order to the end of Module 4, then do Module 12 and start your 12-week plan. Continue with Modules 5 onwards alongside the plan.
- **No exam date yet:** follow the normal order.

On the course page, mark the lessons you skip as done later, or move your start date; your ticks are kept either way.

## Key assumptions

These decisions were made when the course was written. Change them if your situation is different.

1. **Pace:** part-time, about 6 hours a week (5 to 7) for {FINAL} weeks after week 0. The full-time pace does the same work in about {ft_weeks} weeks at about 15 hours a week.
2. **Your PSC study continues.** The course changes **how** you study, not **what**. Action tasks use your syllabus, books and question papers, so they count as PSC study too.
3. **Target exam:** you choose one Kerala PSC exam (for example LDC, LGS, a Degree Level or Plus Two Level preliminary, or a department test) and download its syllabus in week 0. Examples use topics common to most general exams.
4. **Devices:** the Android phone does nearly everything (AnkiDroid, Google Sheets, voice recorder, timer). The laptop helps with long typing and PDFs, and can run Anki for computers if it has Windows 10 or later or a recent Linux.
5. **Money:** ₹0. Every tool and resource is free. No paid coaching, apps or AI plans are needed.
6. **Language:** simple English. Key terms have Malayalam meanings in the glossary.
7. **Facts in examples** (articles of the Constitution, rivers, awards) were checked on {VDATE}. PSC answer keys follow official textbooks, so check your own book when they differ.
8. **Health:** the brain-health module gives general guidance, not medical advice. See a doctor for sleep, mood or health problems.
9. **Privacy:** your recordings, notes and scores stay in your own Learning Folder. Your progress in this app is saved on your phone only.

## The running examples (all made up)

- **Anu**, 27, from Kakkattil: preparing for LDC and the Degree Level preliminary while tutoring students in the evenings (you may know her from the Personal Finance course)
- **Sreeja**, 34, from Nadapuram: a homemaker with two children, studying for LGS in two 45-minute slots a day
- **Ashiq**, 22, from Kuttiady: a new BCom graduate, good at maths, fighting a strong phone habit
- **Joseph sir**, 61, from Thottilpalam: a retired Malayalam teacher who runs a small study group at the panchayat library

## Other courses in this app

This course links to the others instead of repeating them:

- **Free AI Generalist Course:** how AI models work and why they make things up (Level 0), and prompting (Level 1). Module 17 here uses AI for studying; that course teaches AI as a skill.
- **Practical Entrepreneurship**, **Practical Social Media Marketing** and **Practical Personal Finance:** good next courses once your learning system runs (see **What next**). The methods you learn here apply to every one of them.
"""
    return {
        'id': 'lrn-start',
        'title': 'Start here: how this course works',
        'kind': 'intro',
        'summary': 'What you will build and measure, how long it takes, how evidence is rated, where each topic is taught, the PSC fast path and the assumptions behind the course.',
        'content': content.strip(),
    }


def schedule_section():
    wp = week_plan()
    rows = [(str(w), '; '.join(items), f'{h:.1f}'.rstrip('0').rstrip('.')) for w, (items, h) in sorted(wp.items())]
    ft = full_time_rows()
    content = f"""
## Part-time: about 6 hours a week

One course week is one calendar week. This is the default pace on the course page. From week {ANKI_START}, the **30-day AnkiDroid review** adds about 15 minutes a day; the **weekly learning review** takes about 20 minutes every Sunday.

{table(['Week', 'What you do', 'Hours'], rows)}

## Full-time: about 15 hours a week

Choose **Full-time** on the course page. The app then moves through about 2.7 course weeks every calendar week (one course week is {FULL_TIME_WEEK} of a calendar week). Real-day tasks don't speed up, so the full-time plan starts the 30-day sprint earlier and runs the later modules alongside it:

{table(['Calendar week', 'Course weeks', 'Modules', 'Notes'], ft)}

## A weekly rhythm that fits around PSC study

- **Every morning, 15 minutes:** AnkiDroid reviews (from week {ANKI_START}), before you open WhatsApp or YouTube.
- **Your main PSC study block:** use the method from the latest lesson on that day's PSC topic. This is where the course pays off.
- **Weekday evenings, 30–40 minutes:** read one lesson and do its quiz.
- **Saturday, 60–90 minutes:** the action task. Most need your books, question papers and a quiet hour.
- **Sunday, 20 minutes:** the weekly learning review and next week's plan.

## When you fall behind

- **This week** on the course page shows earlier open tasks as overdue. Do the action tasks first; readings can wait.
- More than two weeks behind? Set a new start date on the course page so the weeks match your real progress. Your ticks are kept.
- Use each module's "short on time?" version when you need it.
- Never skip the daily AnkiDroid reviews to catch up on lessons: missed reviews pile up (LRN-M04-L04).

## Exam mode

In the last four weeks before a PSC exam, pause new lessons. Keep AnkiDroid, the weekly review and your 12-week plan's final phase (LRN-M12-L05), and reread LRN-M12-L04 and LRN-M12-L06. Move your start date later by the same number of weeks. The course waits for you.
"""
    return {
        'id': 'lrn-schedule',
        'title': 'Weekly schedule: part-time and full-time',
        'kind': 'reference',
        'summary': 'What to do each week at both paces, how the 30-day tracks fit the full-time pace, and a weekly rhythm around PSC study.',
        'content': content.strip(),
    }


TUTOR_PROMPT = """
You are my study tutor for the Kerala PSC exam. I am a beginner at learning
techniques, and I study in English with Malayalam as my first language.
Today's topic: [topic]. My goal for this session: [goal].
1. Ask me 2-3 questions first to find out what I already know.
2. Do not give me long answers. Teach one small idea at a time, then ask me a
   question that makes me recall or explain it.
3. If I am wrong, give a hint before giving the answer.
4. At the end, quiz me with 5 questions in PSC style, then list what I should
   review.
5. If you are not sure a fact is correct, say so, and tell me which official
   source or textbook to check.
"""


def setup_section():
    folder_list = ', '.join(FOLDERS)
    tab_rows = [(name, when, f'`{hdr}`' if ',' in hdr else hdr) for name, when, hdr in tools.TABS]
    content = f"""
Week 0 takes about 4 hours, including the baseline tests on the next page. You set up the places where your learning system will live, collect your PSC material, and measure where you start.

## 1. A Learning Folder

Make a folder called **Learning Folder** in Google Drive (or on your phone, if you prefer to keep it offline) with these subfolders: {folder_list}. Every proof goes into one of them: photos of handwritten work, screenshots, voice recordings and filled-in templates.

Keep it **private**. Your recordings and scores are for you; share only what you choose.

## 2. The Learning Workbook

Make one spreadsheet called **Learning Workbook** in Google Sheets (phone or laptop). LibreOffice Calc on the laptop opens the same file if you prefer working offline. Start with three tabs; later modules add the rest:

{table(['Tab', 'Added in', 'Row 1 headings'], tab_rows)}

- **On the laptop:** paste a heading line into cell A1, then use **Data → Split text to columns** (Google Sheets) or **Data → Text to Columns** (LibreOffice).
- **On the phone:** type the headings into row 1, one per cell.
- **Formulas** in this course work in Google Sheets and LibreOffice Calc. If LibreOffice shows an error, change the commas between the parts of a formula to semicolons (its setting is under Tools → Options → LibreOffice Calc → Formula).

## 3. Your PSC material

Every action task uses your real material, so collect it now:

1. **Choose your target exam.** If you have several, choose the next big one.
2. **Download its syllabus** from the {rules('psc-syllabus', 'Kerala PSC post-wise syllabus page')} and save it in **12 Exam**.
3. **Download at least three previous question papers** for the same or a similar post from {link('psc-pyq', 'Kerala PSC previous question papers')}, and their final answer keys from {link('psc-keys', 'the answer key page')}.
4. **List your main sources** for each subject: SCERT school textbooks ({link('scert', 'SCERT Kerala')}), any guide or rank file you already own, your notes, and one current-affairs source (Module 10 builds this).

## 4. Your phone and laptop

- Nothing new to install yet. You need the **Clock app** (stopwatch and timer) and a **voice recorder** (most phones have one; a voice note to yourself also works).
- Later modules install free, open-source apps: AnkiDroid (Module 4), Loop Habit Tracker (Module 6) and Joplin or Logseq (Module 18).
- Turn off notifications for games and shopping apps today. Module 5 goes much further.

## 5. Your weekly slots

Block about 6 hours a week in your calendar, outside your best PSC study hours: for example 35 minutes on five weekday evenings, 90 minutes on Saturday and 20 minutes on Sunday for the weekly review.

## 6. A helper and a study partner

Ask a family member or friend to help for 10 minutes with the digit-span test on the next page, and again in week {FINAL}. Ask a friend or classmate who also studies for PSC whether they'd be your study partner for Module 20; it helps from the start to have someone to quiz.

## 7. An AI tutor (optional)

The free plans of common AI chat tools can quiz you and explain ideas. Save this prompt and paste it at the start of a study chat:

{fence(TUTOR_PROMPT)}

AI tools can be confidently wrong about PSC facts. Check facts against your textbook or an official source, and let the AI question you rather than do the thinking for you (Module 17).

## 8. Start two habits today

- **The study log:** after every study session, add one row to the **Study Log** tab: what you studied, for how long, which method, and one thing you can now recall without looking. It takes one minute and builds the data for your weekly reviews.
- **The weekly review:** every Sunday, answer three questions in a notebook or the **Weekly** tab: What did I learn (from memory)? What worked? What will I change? The full version arrives in LRN-M07-L03.

Every link on this page was checked on {VDATE}. The **Sources and verification log** at the end of the course lists each one with its status.
"""
    tasks = [
        ('lrn-w0-folder', 'Learning Folder made, private, with its 22 subfolders'),
        ('lrn-w0-workbook', 'Learning Workbook made with the Baseline, Study Log and Weekly tabs'),
        ('lrn-w0-psc', 'Target exam chosen; syllabus and at least three previous papers with answer keys saved in 12 Exam'),
        ('lrn-w0-slots', 'Weekly course slots blocked; a helper for the digit-span test found'),
        ('lrn-w0-log', 'Study log started: at least three rows'),
    ]
    return {
        'id': 'lrn-w0',
        'title': 'Week 0: Learning Folder, Learning Workbook and your PSC material',
        'kind': 'setup',
        'weeks': [0, 0],
        'hours': 2.5,
        'summary': 'One private folder, one workbook, your PSC syllabus and question papers, weekly slots, and two habits that start today.',
        'content': content.strip(),
        'tasks': [{'id': i, 'text': t, 'kind': 'task', 'week': 0} for i, t in tasks],
    }


def _digit_block(form):
    fwd, bwd = tests.digit_sets(form)
    f = '\n'.join(f'{n} digits: {s}' for n, s in fwd)
    b = '\n'.join(f'{n} digits: {s}' for n, s in bwd)
    return f'FORWARD (say them back in the same order)\n{f}\n\nBACKWARD (say them back in reverse order)\n{b}'


def _record_table():
    return table(['Test', 'Start (week 0)', f'End (week {FINAL})', 'Change'], [
        ('List recall after 10 minutes (out of 20)', '', '', ''),
        ('List recall after 24 hours (out of 20)', '', '', ''),
        ('Reading speed (words per minute)', '', '', ''),
        ('Comprehension (out of 8, and %)', '', '', ''),
        ('Effective reading rate (wpm × comprehension %)', '', '', ''),
        ('Minutes to first distraction (average of 2 days)', '', '', ''),
        ('Distractions in 45 minutes (average of 2 days)', '', '', ''),
        ('Digit span forward', '', '', ''),
        ('Digit span backward', '', '', ''),
        ('Learning habits total (out of 75)', '', '', ''),
    ])


def _tests_text(form):
    words = tests.LIST_A if form == 'A' else tests.LIST_B
    title = tests.PASSAGE_A_TITLE if form == 'A' else tests.PASSAGE_B_TITLE
    passage = tests.PASSAGE_A if form == 'A' else tests.PASSAGE_B
    n_words = tests.WORDS_A if form == 'A' else tests.WORDS_B
    qs, key = tests.mcq(tests.QUESTIONS_A if form == 'A' else tests.QUESTIONS_B, form)
    word_rows = '\n'.join(f'{i:>2}. {w}' for i, w in enumerate(words, 1))
    return f"""
## Test 1: the 20-item list (about 20 minutes, plus 3 minutes tomorrow)

1. Have a pen, paper and a timer ready. Set the timer for **2 minutes**.
2. Start the timer and study the list below in any way you like. Stop when the timer rings.
3. Cover the list. For the next **10 minutes**, do something that keeps your mind busy, such as arithmetic questions from your PSC book. Don't rehearse the list.
4. Write down every word you remember, in any order, in **3 minutes**. Count the correct words (spelling doesn't matter). That is your **10-minute score**.
5. **Don't look at the list again.** Exactly 24 hours later, write the words again in 3 minutes, without looking. That is your **24-hour score**.

{fence(f'LIST {form} (study for 2 minutes)' + chr(10) + word_rows)}

## Test 2: reading speed and comprehension (about 15 minutes)

1. Read the passage below **once**, at your normal pace for understanding: not skimming, not studying. Time yourself with the stopwatch from the first word to the last.
2. Without looking back, answer the 8 questions below it.
3. Work out your scores:
    - **Reading speed (wpm)** = {n_words} words ÷ your minutes. Example: 3 minutes 20 seconds is 3.33 minutes, so {n_words} ÷ 3.33 = {n_words / 3.333:.0f} wpm.
    - **Comprehension %** = correct answers ÷ 8 × 100
    - **Effective reading rate** = wpm × comprehension % ÷ 100

### Passage {form}: {title} ({n_words} words)

{passage.strip()}

### Questions on passage {form}

{qs}

## Test 3: focus duration (45 minutes, on two different days)

1. Choose a normal PSC study task: reading a new chapter and making notes works well.
2. Set up the way you **usually** study. Don't change anything for the test.
3. Start the stopwatch. Study for 45 minutes. Keep a paper beside you: every time you notice your attention left the task (you checked the phone, got up, started daydreaming), make a tally mark. Write down the time of the **first** one.
4. Record: **minutes to first distraction**, **number of tally marks**, and a focus rating from 1 to 10.
5. Repeat on another day this week, and use the average of the two.

## Test 4: digit span (10 minutes, with a helper if possible)

**With a helper (best):** the helper reads each line aloud at about one digit per second, in a flat voice. You repeat the digits (forward: same order; backward: reverse order). Start at the shortest lines. Stop a section when you fail **both** lines of the same length.

**Alone:** cover the list with a paper and slide it down to show one line for as many seconds as there are digits, cover it again, and write the digits down. Use the same method again in week {FINAL}, so the scores compare fairly.

**Your span** in each section is the longest length where you got at least one of the two lines exactly right.

{fence(f'DIGIT SPAN, FORM {form}' + chr(10) + _digit_block(form))}

## Part 5: your learning habits (5 minutes)

Rate each statement: **1** never, **2** rarely, **3** sometimes, **4** usually, **5** almost always. Add them up (out of 75).

{table(['No', 'Statement', 'Start', 'End'], [(str(i), s, '', '') for i, s in enumerate(tests.HABITS, 1)])}

## Answer key for passage {form}

Check only after you have answered all 8 questions: **{key}**.
"""


def baseline_section():
    content = f"""
Before you learn anything new, measure where you start. These four short tests and a habits rating take about 1.5 hours, spread over two days, because two of them need a second session. In week {FINAL} you repeat them with fresh versions (form B, on the final page), so you can see what changed. Don't practise for them, and don't look at form B.

Copy this table into the **Baseline** tab of your Learning Workbook and fill in the **Start** column as you go:

{_record_table()}
{_tests_text('A')}
## What your scores mean

There are no good or bad scores here; they are your starting line. Short-term memory holds roughly seven items, give or take two ({link('os-psych-8-1', 'OpenStax Psychology 2e, 8.1')}), so a 20-word list is meant to be too long to hold without a method. What matters is the change by week {FINAL}, and the methods you used to get it. Save a photo of your answer sheets and a screenshot of the Baseline tab in **00 Baseline**.
"""
    return {
        'id': 'lrn-baseline',
        'title': 'Baseline tests: memory, reading, focus and digit span',
        'kind': 'setup',
        'weeks': [0, 0],
        'hours': 1.5,
        'summary': f'Four short tests and a habits rating to measure where you start: list recall after 10 minutes and 24 hours, reading speed with comprehension, focus duration and digit span. You repeat them in week {FINAL}.',
        'content': content.strip(),
        'tasks': [
            {'id': 'lrn-baseline-list10', 'text': 'Baseline: list A recalled after 10 minutes, score recorded', 'kind': 'task', 'week': 0},
            {'id': 'lrn-baseline-list24', 'text': 'Baseline: list A recalled after 24 hours, score recorded', 'kind': 'task', 'week': 0},
            {'id': 'lrn-baseline-reading', 'text': 'Baseline: passage A read and quiz done; wpm, comprehension and effective rate recorded', 'kind': 'task', 'week': 0},
            {'id': 'lrn-baseline-focus', 'text': 'Baseline: focus test done on two days, averages recorded', 'kind': 'task', 'week': 0},
            {'id': 'lrn-baseline-digits', 'text': 'Baseline: digit span forward and backward recorded', 'kind': 'task', 'week': 0},
            {'id': 'lrn-baseline-habits', 'text': 'Baseline: 15 learning habits rated, total recorded', 'kind': 'task', 'week': 0},
        ],
    }


def system_section():
    rows = [(str(w), f'Weekly learning review (week {w})', 'Weekly tab row and your written review') for w in REVIEW_WEEKS]
    rows += [(str(w), f'AnkiDroid: day {d} of 30 reviewed', 'Screenshot of the AnkiDroid statistics calendar') for d, w in ANKI_DAYS]
    rows.sort(key=lambda r: int(r[0]))
    content = f"""
Two habits run underneath the whole course. They turn lessons into a system. **This week** on the course page shows the checkpoints when they are due.

## Habit 1: the weekly learning review (every Sunday, from week 1)

Twenty minutes, at the same time every week. Until you reach LRN-M07-L03, use the short version:

1. **Recall:** without notes, write the three most important things you learned this week.
2. **Numbers:** hours studied, days of AnkiDroid done (from week {ANKI_START}), and any test score.
3. **Adjust:** what worked, what didn't, and one change for next week.

From week {WEEKS[(7, 3)][0]}, use the full **weekly review** template (it is also on the **Toolkit** page) and copy its numbers into the **Weekly** tab.

## Habit 2: the 30-day AnkiDroid review (from week {ANKI_START})

In Module 4 you build a deck of 100 or more cards on one PSC topic. The course asks you to review it **every day for 30 days**. That proves the habit, and it is long enough to see spaced repetition work.

- **Review every day,** even on bad days: 5 minutes is better than none. Do the reviews before you add new cards.
- **Count review days, not calendar days.** If you miss a day, the 30 days end a day later.
- **Add new cards gradually:** about 10 to 20 new cards a day until the deck has 100 or more (LRN-M04-L04 explains the workload).
- **Proof:** a screenshot of the AnkiDroid statistics screen with its calendar, and your true retention (the share of mature reviews you passed).

## Checkpoints

{table(['Due by week', 'Checkpoint', 'Evidence'], rows)}

## When a checkpoint is missed

Missing one is information, not failure. Ask why: no fixed time, too many new cards, exam pressure, a bad week? Fix that one thing. Never try to "catch up" weeks of reviews in one sitting; do today's, and the backlog clears in a few days (LRN-M04-L04).
"""
    tasks = [{'id': f'lrn-review-w{w:02d}', 'text': f'Weekly learning review, week {w}', 'kind': 'project', 'week': w,
              'detail': '**Evidence:** your written review and a row in the Weekly tab. Save a photo or screenshot in 07 Metacognition.'}
             for w in REVIEW_WEEKS]
    tasks += [{'id': f'lrn-anki-day{d:02d}', 'text': f'AnkiDroid: day {d} of 30 reviewed', 'kind': 'project', 'week': w,
               'detail': '**Evidence:** a screenshot of the AnkiDroid statistics calendar, saved in 04 Anki.'}
              for d, w in ANKI_DAYS]
    tasks.sort(key=lambda t: t['week'])
    return {
        'id': 'lrn-system',
        'title': 'Learning system track: weekly reviews and the 30-day AnkiDroid review',
        'kind': 'track',
        'weeks': [1, REVIEW_WEEKS[-1]],
        'summary': f'A 20-minute review every Sunday from week 1, and daily AnkiDroid reviews for 30 days from week {ANKI_START}. Eleven checkpoints keep you on track.',
        'content': content.strip(),
        'tasks': tasks,
    }


def toolkit_section():
    parts = ["""
These are the six core tools of your learning system, in one place, ready to copy into your notebook, Joplin or the Learning Workbook. Each was introduced in a lesson; the lesson explains how to use it well.
"""]
    for name, var, where in tools.SIX_TOOLS:
        parts.append(f'## {name}\n\nFrom {where}.\n\n' + fence(getattr(tools, var)))
    parts.append('## Revision tab formulas\n\n' + fence(tools.REVISION_FORMULAS))
    parts.append('## Error types\n\n' + table(['Code', 'Meaning'], tools.ERROR_TYPES))
    rows = [(name, when, f'`{hdr}`' if ',' in hdr else hdr) for name, when, hdr in tools.TABS]
    parts.append('## Learning Workbook tabs\n\n' + table(['Tab', 'Added in', 'Row 1 headings'], rows))
    return {
        'id': 'lrn-toolkit',
        'title': 'Toolkit: every copy-ready template in one place',
        'kind': 'reference',
        'summary': 'The study planner, revision schedule, card-writing checklist, error log, Feynman template and weekly review, plus the Learning Workbook tab headings and formulas.',
        'content': '\n\n'.join(p.strip() for p in parts),
    }


def front():
    return [start_section(), schedule_section(), setup_section(), baseline_section(), system_section(), toolkit_section()]


# ---------------------------------------------------------------- back matter

SYSTEM_ITEMS = [
    ('lrn-final-workbook', 'Learning Workbook with every tab in use and up to date', 'Week 0 onwards'),
    ('lrn-final-deck', 'AnkiDroid deck of 100+ cards with 30 review days done, and a daily review habit', 'Module 4'),
    ('lrn-final-revision', 'Revision tab with your current PSC topics scheduled', 'LRN-M03-L02'),
    ('lrn-final-focus', 'A quiet phone setup and a time-blocked weekly planner', 'Module 5'),
    ('lrn-final-habits', 'If-then plans and study habits tracked in Loop', 'Module 6'),
    ('lrn-final-reviews', 'At least eight weekly reviews written', 'Module 7 and the system track'),
    ('lrn-final-feynman', 'Five Feynman recordings, each with a second version', 'Module 8'),
    ('lrn-final-palace', 'A memory palace for a PSC topic, recalled after a week', 'LRN-M11-L02'),
    ('lrn-final-exam', 'Syllabus map, PYQ analysis and error log for your target exam', 'Module 12'),
    ('lrn-final-plan', 'A 12-week PSC study and revision plan', 'LRN-M12-L05'),
    ('lrn-final-kb', 'A knowledge base in Joplin or Logseq', 'Module 18'),
    ('lrn-final-teach', 'A taught lesson with feedback, and study-group rules', 'Module 20'),
    ('lrn-final-sprint', '30-day sprint report with before and after scores', 'Module 21'),
]


def final_section():
    rows = [(t, where) for _, t, where in SYSTEM_ITEMS]
    content = f"""
Two things finish the course: retake the four tests with fresh versions, and check that every part of your learning system exists and runs.

## 1. Retake the tests (form B)

Use exactly the same steps, timing and conditions as in week 0, but with the form B materials below. This time, **use any technique you learned**: that is the point. Fill in the **End** column of the Baseline tab, then the **Change** column.

When you compare, be fair to yourself:

- **Some improvement comes from practice:** you have done these tests before. The big gains (often in list recall) come from technique.
- **Digit span may not move.** That's normal (see **Start here**). If it did, write down the strategy you used.
- **Write three lines:** your biggest gain, the method behind it, and one score you want to improve next.
{_tests_text('B')}
## 2. Check your learning system

Each item should be a tab, a file, an app or a habit you could show someone tomorrow. If something is missing, the module listed has its template.

{table(['System item', 'Where it was built'], rows)}

## Before you call the course done

- Save a backup of your progress from **Backup and courses** in this app, and keep it in your Learning Folder.
- Download a copy of your Learning Workbook (File → Download) and export your AnkiDroid collection as a backup.
- Put your next weekly review, your next 12-week plan review and a "retest" date six months from now in your calendar. The course ends; your learning system doesn't.
"""
    tasks = [
        {'id': 'lrn-final-list10', 'text': 'Final: list B recalled after 10 minutes, score recorded', 'kind': 'task', 'week': FINAL},
        {'id': 'lrn-final-list24', 'text': 'Final: list B recalled after 24 hours, score recorded', 'kind': 'task', 'week': FINAL},
        {'id': 'lrn-final-reading', 'text': 'Final: passage B read and quiz done; effective reading rate recorded', 'kind': 'task', 'week': FINAL},
        {'id': 'lrn-final-focusdur', 'text': 'Final: focus test on two days, averages recorded', 'kind': 'task', 'week': FINAL},
        {'id': 'lrn-final-digits', 'text': 'Final: digit span forward and backward recorded', 'kind': 'task', 'week': FINAL},
        {'id': 'lrn-final-habitsrating', 'text': 'Final: learning habits rated; Change column filled in', 'kind': 'task', 'week': FINAL},
        {'id': 'lrn-final-compare', 'text': 'Final: three lines written on your biggest gain, its method and your next target', 'kind': 'exit', 'week': FINAL},
    ] + [{'id': i, 'text': t, 'kind': 'task', 'week': FINAL} for i, t, _ in SYSTEM_ITEMS]
    return {
        'id': 'lrn-final',
        'title': 'Final retests and learning system checklist',
        'kind': 'capstone',
        'weeks': [FINAL, FINAL],
        'hours': 1.5,
        'summary': 'Retake the four tests with fresh versions, compare with week 0, and check that every part of your learning system exists and runs.',
        'content': content.strip(),
        'tasks': tasks,
    }


def next_section():
    content = f"""
Finishing the course is the start of running your own learning system. Here is how to keep it going, for PSC and after it.

## Every day (20–60 minutes)

- AnkiDroid reviews first, then new cards only if the reviews are done.
- One retrieval session on your main PSC topic: blank-page recall or practice questions, before any rereading.
- Phone out of reach during study blocks.

## Every week (20 minutes)

- The weekly learning review. One change at a time.
- Update the Revision tab and clear the Errors tab's retests.

## Every 12 weeks (one evening)

- Review your 12-week PSC plan (LRN-M12-L05): what is solid, what is weak, and the next cycle's priorities.
- Take one full mock test under exam conditions, and analyse it with the error log.
- Repeat one of the baseline tests (form A works again by now), to keep measuring.

## After PSC: the same system, new subjects

{table(['What you want to learn', 'Where to start', 'Methods to use'], [
    ('AI skills', 'The Free AI Generalist Course in this app', 'A learning project plan (LRN-M13-L02), Feynman explanations of each new idea, AnkiDroid for terms'),
    ('Starting a business', 'Practical Entrepreneurship in this app', 'Deliberate practice with real customers, feedback loops, a weekly review'),
    ('Marketing and freelancing', 'Practical Social Media Marketing in this app', 'Interleaved practice on real posts, an error log of what failed'),
    ('Money management', 'Practical Personal Finance in this app', 'Concrete examples with your own numbers, spaced review of key rules'),
    ('A new language (Hindi, Arabic, German...)', link('langtransfer', 'Language Transfer') + ' (free audio courses) and the LRN-M15-L04 plan', 'Daily input, shadowing, a vocabulary deck in AnkiDroid'),
    ('Better English', link('learnenglish', 'British Council LearnEnglish'), 'Reading and listening every day, a phrase deck, speaking practice with a partner'),
    ('How learning works, in more depth', link('lhtl', 'Learning How to Learn') + ' on Coursera (free to enrol)', 'Take notes as questions; make cards for key ideas'),
])}

## Keep learning about learning, free

- {link('ls-materials', 'The Learning Scientists')}: posters, slides and a blog on the six strategies
- {link('retrievalpractice', 'RetrievalPractice.org')}: guides and research summaries
- {link('ncase', 'How To Remember Anything Forever-ish')}: the best 20-minute refresher on spaced repetition
- {link('os-psych', 'OpenStax Psychology 2e')}, chapters 7 and 8 on thinking and memory

## A warning about "learning hacks"

You will meet videos and apps that promise photographic memory, 1,000 words a minute, or "brain training" that raises intelligence. Check them against what you learned in Module 2 and the evidence tables in this course. The methods that work are less exciting: recall, spacing, mixing, explaining, sleep, and doing it every week.

Every link on this page was checked on {VDATE}; see the **Sources and verification log** for each one's status.
"""
    return {
        'id': 'lrn-next',
        'title': 'What next: keep your learning system running',
        'kind': 'reference',
        'summary': 'Daily, weekly and 12-weekly routines after the course, and how to use the same system for AI skills, business, money and new languages.',
        'content': content.strip(),
    }


GLOSSARY = [
    ('Learning', 'പഠനം', 'A lasting change in what you know or can do'),
    ('Attention', 'ശ്രദ്ധ', 'Choosing what your mind works on right now'),
    ('Working memory', 'പ്രവർത്തന ഓർമ്മ (താൽക്കാലിക ഓർമ്മ)', 'The small mental "desk" that holds a few items for seconds while you use them'),
    ('Long-term memory', 'ദീർഘകാല ഓർമ്മ', 'Your large, lasting store of knowledge and skills'),
    ('Cognitive load', 'ബൗദ്ധിക ഭാരം', 'How much a task demands from working memory'),
    ('Schema', 'അറിവിന്റെ ചട്ടക്കൂട്', 'An organised pattern of knowledge in long-term memory'),
    ('Encoding', 'ഓർമ്മയിൽ പതിപ്പിക്കൽ', 'Turning what you experience into a memory'),
    ('Consolidation', 'ഓർമ്മ ഉറപ്പിക്കൽ', 'The brain stabilising new memories over hours and during sleep'),
    ('Retrieval', 'ഓർത്തെടുക്കൽ', 'Bringing a memory back to mind'),
    ('Forgetting curve', 'മറവിയുടെ വക്രരേഖ', 'Memory loss that is fast at first and slower later'),
    ('Neuroplasticity', 'ന്യൂറോപ്ലാസ്റ്റിസിറ്റി (തലച്ചോറിന് മാറാനുള്ള കഴിവ്)', 'The brain changing its connections with learning and experience'),
    ('Chunk', 'കൂട്ടം (ചങ്ക്)', 'Several items grouped and remembered as one unit'),
    ('Neuromyth', 'തലച്ചോറിനെക്കുറിച്ചുള്ള മിഥ്യാധാരണ', 'A popular but false belief about the brain'),
    ('Learning styles', 'പഠന ശൈലികൾ', 'The unsupported idea that teaching should match "visual" or "auditory" learners'),
    ('Illusion of knowing', 'അറിവിന്റെ മിഥ്യാബോധം', 'Feeling that you know something because it looks familiar'),
    ('Retrieval practice', 'ഓർത്തെടുക്കൽ പരിശീലനം', 'Learning by recalling without looking'),
    ('Spaced practice', 'ഇടവിട്ടുള്ള പഠനം', 'Spreading study over days and weeks instead of cramming'),
    ('Interleaving', 'ഇടകലർത്തിയുള്ള പരിശീലനം', 'Mixing different types of problems in one practice session'),
    ('Elaboration', 'വിശദീകരിച്ചുള്ള പഠനം', 'Asking how and why, and linking new ideas to what you know'),
    ('Concrete example', 'മൂർത്തമായ ഉദാഹരണം', 'A specific case that shows an abstract idea'),
    ('Dual coding', 'ഇരട്ട കോഡിങ് (വാക്കും ചിത്രവും)', 'Combining words with pictures, maps, timelines or diagrams'),
    ('Spaced repetition', 'ഇടവേള ആവർത്തനം', 'Reviewing at growing intervals, timed by software'),
    ('Flashcard', 'ഓർമ്മക്കാർഡ് (ഫ്ലാഷ്കാർഡ്)', 'A card with a question on one side and the answer on the other'),
    ('Cloze deletion', 'വിട്ടഭാഗം പൂരിപ്പിക്കൽ', 'A card that hides one word or phrase in a sentence'),
    ('Image occlusion', 'ചിത്രഭാഗം മറയ്ക്കൽ', 'A card that hides part of a map or diagram'),
    ('Deck', 'കാർഡ് ശേഖരം (ഡെക്ക്)', 'A collection of flashcards'),
    ('Retention', 'ഓർമ്മ നിലനിർത്തൽ നിരക്ക്', 'The share of reviews you answer correctly'),
    ('Leech', 'ആവർത്തിച്ച് തെറ്റുന്ന കാർഡ് (ലീച്ച്)', 'A card you keep failing; rewrite or split it'),
    ('Focus', 'ഏകാഗ്രത', 'Keeping attention on one task'),
    ('Distraction', 'ശ്രദ്ധ തെറ്റൽ', 'Anything that pulls your attention away'),
    ('Multitasking', 'ഒരേസമയം പല ജോലികൾ', 'Switching quickly between tasks; it costs accuracy and time'),
    ('Deep work', 'ആഴത്തിലുള്ള ജോലി', 'Long, undistracted work on a demanding task'),
    ('Time-blocking', 'സമയം മുൻകൂട്ടി വിഭജിക്കൽ', 'Giving each task a fixed slot in your day'),
    ('Procrastination', 'നീട്ടിവയ്ക്കൽ', 'Delaying a task you intend to do, even though delay will cost you'),
    ('Implementation intention', 'എങ്കിൽ-അപ്പോൾ പദ്ധതി', 'A plan in the form "If X happens, then I will do Y"'),
    ('Habit', 'ശീലം', 'An action done almost automatically in a familiar situation'),
    ('Motivation', 'പ്രചോദനം', 'The reasons and energy that move you to act'),
    ('Metacognition', 'മെറ്റാകോഗ്നിഷൻ (സ്വന്തം പഠനത്തെക്കുറിച്ചുള്ള ബോധം)', 'Knowing, checking and managing your own learning'),
    ('Calibration', 'ആത്മവിലയിരുത്തലിന്റെ കൃത്യത', 'How well your confidence matches your real accuracy'),
    ('Self-explanation', 'സ്വയം വിശദീകരണം', 'Explaining each step or idea to yourself as you study'),
    ('Feynman technique', 'ഫെയ്ൻമാൻ രീതി', 'Explaining a topic simply, aloud, to find and fix the gaps'),
    ('Concept map', 'ആശയ ഭൂപടം', 'Ideas in boxes joined by labelled arrows'),
    ('First principles', 'അടിസ്ഥാന തത്ത്വങ്ങൾ', 'The basic truths from which you can rebuild an idea'),
    ('Cornell notes', 'കോർണൽ കുറിപ്പ് രീതി', 'A page with notes, a question column and a summary'),
    ('Mind map', 'മനോഭൂപടം (മൈൻഡ് മാപ്പ്)', 'A central topic with branches of related ideas'),
    ('Skimming', 'ഓടിച്ചു വായിക്കൽ', 'Reading fast for the main idea'),
    ('Scanning', 'തിരഞ്ഞു വായിക്കൽ', 'Searching a text quickly for one specific fact'),
    ('Comprehension', 'ഗ്രഹണശേഷി', 'Understanding what you read'),
    ('Mnemonic', 'ഓർമ്മസൂത്രം', 'A trick that makes something easier to remember'),
    ('Memory palace (method of loci)', 'ഓർമ്മക്കൊട്ടാരം (സ്ഥാനരീതി)', 'Placing vivid images along a familiar route to remember a list'),
    ('Peg system', 'കൊളുത്ത് രീതി (പെഗ് സിസ്റ്റം)', 'Hanging items on a memorised list of number-images'),
    ('Major system', 'മേജർ സിസ്റ്റം (അക്കം-വ്യഞ്ജനം രീതി)', 'Turning digits into consonant sounds, then into words'),
    ('Syllabus', 'പാഠ്യപദ്ധതി (സിലബസ്)', 'The official list of topics for an exam'),
    ('Previous-year questions (PYQ)', 'മുൻവർഷ ചോദ്യങ്ങൾ', 'Questions from past papers of the same or similar exams'),
    ('Mock test', 'മാതൃകാ പരീക്ഷ', 'A practice exam under real exam conditions'),
    ('Error log', 'തെറ്റുകളുടെ രേഖ', 'A record of your mistakes, their causes and fixes'),
    ('Negative marking', 'നെഗറ്റീവ് മാർക്ക്', 'Marks deducted for wrong answers'),
    ('Revision', 'പുനരവലോകനം (റിവിഷൻ)', 'Going back over what you learned, best done by recall'),
    ('Deliberate practice', 'ബോധപൂർവമായ പരിശീലനം', 'Focused practice on weak points, with feedback'),
    ('Feedback', 'പ്രതികരണം (ഫീഡ്ബാക്ക്)', 'Information on how you did and what to fix'),
    ('Critical thinking', 'വിമർശനാത്മക ചിന്ത', 'Judging claims by their evidence and reasoning'),
    ('Argument', 'വാദം', 'Reasons (premises) offered in support of a conclusion'),
    ('Fallacy', 'തെറ്റായ വാദരീതി', 'A flawed argument that can still sound convincing'),
    ('Cognitive bias', 'ചിന്താ പക്ഷപാതം', 'A systematic error in thinking'),
    ('Mental model', 'മാനസിക മാതൃക', 'A simple idea that helps explain how something works'),
    ('Comprehensible input', 'മനസ്സിലാകുന്ന ഭാഷാ ഇൻപുട്ട്', 'Listening or reading that you can mostly understand'),
    ('Shadowing', 'ഷാഡോയിങ് (കേട്ട് ഒപ്പം പറയൽ)', 'Repeating audio aloud right after the speaker'),
    ('Vocabulary', 'പദസമ്പത്ത്', 'The words you know and can use'),
    ('Hallucination (AI)', 'എഐയുടെ സാങ്കൽപ്പിക ഉത്തരം', 'An AI tool stating something false as if it were true'),
    ('Socratic questioning', 'സോക്രട്ടീസിയൻ ചോദ്യരീതി', 'Teaching by asking questions that make you think'),
    ('Knowledge base', 'വിജ്ഞാന ശേഖരം', 'Your linked collection of notes'),
    ('Stress', 'മാനസിക സമ്മർദ്ദം', 'The body\'s response to demands or threats'),
    ('Exam anxiety', 'പരീക്ഷാ ഉത്കണ്ഠ', 'Worry and tension about exams that can lower performance'),
    ('Learning sprint', 'തീവ്ര പഠന കാലയളവ് (സ്പ്രിന്റ്)', 'A short, focused period of study with a clear goal and a measured result'),
]


def glossary_section():
    rows = [(f'**{en}**', ml, meaning) for en, ml, meaning in GLOSSARY]
    content = f"""
Key words from the course, roughly in the order you meet them. Many English terms, such as AnkiDroid, mock test and PYQ, are used as they are in Malayalam conversation; the Malayalam is given so you can explain them to family and study partners.

{table(['English', 'മലയാളം (Malayalam)', 'Simple meaning'], rows)}
"""
    return {
        'id': 'lrn-glossary',
        'title': 'Glossary with Malayalam meanings',
        'kind': 'reference',
        'summary': f'{len(GLOSSARY)} key learning terms in English and Malayalam, with simple meanings.',
        'content': content.strip(),
    }


def back():
    return [final_section(), next_section(), glossary_section()]


def finish(course):
    """Add the sources page, built from every link the course actually uses."""
    sections = course['sections']
    used_in = {}
    for s in sections:
        texts = [s.get('content', ''), s.get('summary', '')] + [t.get('detail', '') for t in s.get('tasks', [])]
        blob = '\n'.join(texts)
        code = s['title'].split(':')[0]
        for key, r in R.items():
            if f"]({r['url']})" in blob:
                used_in.setdefault(key, [])
                if code not in used_in[key]:
                    used_in[key].append(code)
    groups = {}
    for key in used_in:
        groups.setdefault(R[key]['group'], []).append(key)
    parts = [f"""
Every link in this course is listed here with the date it was checked. Links were opened and read on {VDATE}; nothing here was copied from memory. If a link stops working, search for its title on the same website.

- **verified {VDATE}:** the page was opened on that date and its content matched what the course says.
- **verified {VDATE}; check current rules:** as above, but it describes something that changes: an app feature, an exam rule or a syllabus. Open the source before you rely on it.
- **unverified:** the site blocks automated checks, so the page could not be opened for this course. The address is the official one; type it yourself and check that it is the real site.

Official and open-licensed sources are preferred: OpenStax books (CC BY-NC-SA 4.0), the public-domain comic by Nicky Case, open-access papers, and open-source apps (AnkiDroid, Joplin, Logseq, Loop). This course only links to them. Where a paper is behind a paywall, the course links to a free summary by the university or society that published it, and says so in the title. Wikipedia is used only to check facts used in examples.
"""]
    for g in GROUP_ORDER:
        if g not in groups:
            continue
        rows = []
        for key in groups[g]:
            r = R[key]
            where = ', '.join(used_in[key][:6]) + (' and more' if len(used_in[key]) > 6 else '')
            rows.append((f"[{r['title']}]({r['url']})", where, STATUS[r['s']]))
        parts.append(f'## {g}\n\n' + table(['Resource', 'Used in', 'Status'], rows))
    unverified = [k for k in used_in if R[k]['s'] == 'u']
    rules_keys = [k for k in used_in if R[k]['s'] == 'vr']
    headline = [k for k in used_in if R[k]['s'] == 'vt']
    parts.append('## Marked "unverified"\n\n' + (bullets([f"[{R[k]['title']}]({R[k]['url']})" for k in unverified]) or 'None.'))
    if headline:
        parts.append('## Headline checked only\n\n' + bullets([f"[{R[k]['title']}]({R[k]['url']})" for k in headline]))
    parts.append('## Marked "check current rules"\n\n' + (bullets([f"[{R[k]['title']}]({R[k]['url']})" for k in rules_keys]) or 'None.'))
    sections.append({
        'id': 'lrn-sources',
        'title': 'Sources and verification log',
        'kind': 'reference',
        'summary': f'Every link in the course, where it is used and when it was checked ({VDATE}).',
        'content': '\n\n'.join(p.strip() for p in parts),
    })
