"""Course-level sections for Mind, Body and People: start here, schedule,
week 0 setup, baseline tests, the daily system track, the toolkit, the five
part pages, the final retest and checklist, what next, glossary and the
sources page."""
from common import (R, STATUS, VDATE, CHECK, GROUP_ORDER, EVIDENCE_KEY, FOLDERS, WEEKS, PROJECT_WEEK,
                    LAST_WEEK, LOAD, PLAYBOOK, link, rules, xref, fence, bullets, numbered, table, fmt_hours, code_of)
import plan
import tests
import tools

FULL_TIME_WEEK = 0.4     # one course week = 0.4 calendar weeks at full-time pace (about 15 hours a week)
FINAL = LAST_WEEK


def wk(m, l):
    return WEEKS[(m, l)][0]


# Daily-practice checkpoints on the system track: (id, text, week, evidence)
def challenges():
    out = []
    b = wk(3, 3)
    out += [('pd-sys-bias-w1', 'Bias journal: week 1 done (21 entries)', b + 1, 'your bias journal note, with the bias you caught most in yourself'),
            ('pd-sys-bias-w2', 'Bias journal: week 2 done, and a 3-line summary of your top traps', b + 2, 'the journal and the summary in 03 Thinking traps')]
    e = wk(8, 4)
    out += [('pd-sys-exp-w1', 'Personal experiment: baseline week logged (7 days of study minutes)', e + 1, 'the experiment log'),
            ('pd-sys-exp-w2', 'Personal experiment: change week logged and result written', e + 2, 'the completed experiment log with averages and your decision')]
    t = wk(11, 2)
    out += [('pd-sys-tr-w1', 'Thought records: week 1 (at least 3 records)', t + 1, 'photos or notes of the records in 11 Stress and resilience'),
            ('pd-sys-tr-w2', 'Thought records: week 2, plus re-rated feelings compared', t + 2, 'the records and a note on which distortions came up most')]
    for name, (m, l), log in (('Meditation', (12, 1), 'Medito history screenshot or your Loop habit graph'),
                              ('Journaling', (12, 2), 'photos of your journal pages or the Joplin notes'),
                              ('Rejection', (14, 3), 'your 30-day rejection log'),
                              ('Fitness', (17, 3), 'your workout log and a retest of push-ups and plank on day 30')):
        s = wk(m, l)
        key = name.lower()
        out += [(f'pd-sys-{key}-d10', f'{name} challenge: day 10 of 30', s + 1, log),
                (f'pd-sys-{key}-d20', f'{name} challenge: day 20 of 30', s + 3, log),
                (f'pd-sys-{key}-d30', f'{name} challenge: day 30 of 30, with a short review', s + 4, log + ', plus 3 lines on what changed')]
    c = wk(25, 2)
    out += [('pd-sys-conv-w1', 'Conversation challenges: 7 days logged', c + 1, 'your conversation log'),
            ('pd-sys-conv-w2', 'Conversation challenges: 14 days logged, names remembered counted', c + 2, 'your conversation log with the totals')]
    for letter, title, a, z in plan.PARTS:
        end = max(PROJECT_WEEK[m] for m in range(a, z + 1))
        if letter != 'E':
            out.append((f'pd-sys-part-{letter.lower()}', f'Part {letter} review: what changed, what to keep', end,
                        f'a half-page review in your Playbook notebook: your Part {letter} projects, rubric scores and the three habits or ideas you are keeping'))
    return sorted(out, key=lambda x: x[2])


MODULE_MAP = [
    (1, 'System 1 and System 2, heuristics, emotion and reason', 'A "think slower" checklist'),
    (2, 'Experiments, correlations, sample size, replication crisis, pop psychology', 'A claim-checker card'),
    (3, 'Seven biases, CBT distortions, debiasing, the bias journal', 'Two weeks of bias journal'),
    (4, 'Uncertainty, base rates, pre-mortems, choice overload, regret', 'A decision sheet for a real choice'),
    (5, 'Values, life wheel, Big Five, VIA strengths, limits of MBTI', 'Your self-awareness profile'),
    (6, 'Self-determination theory, intrinsic and extrinsic motivation, goal-setting, progress principle', 'A motivation redesign of one goal'),
    (7, 'Vision, 12-month plan, weekly planning and review', 'Your 12-month plan, version 1'),
    (8, 'Present bias, commitment devices, environment design, habit loop, if-then plans, tiny habits, identity, procrastination', 'A two-week personal experiment with data'),
    (9, 'Growth mindset (honest evidence), limiting beliefs, self-compassion', 'A self-talk rewrite'),
    (10, 'Emotions, negativity bias, labelling, reappraisal, empathy', 'An emotion log and reappraisal practice'),
    (11, 'Stress response, when to get help, thought records, Stoic practices, failure', 'Two weeks of thought records'),
    (12, 'Meditation, breathwork, journaling, gratitude', '30-day meditation and journaling challenges'),
    (13, 'Self-efficacy, spotlight effect, impostor feelings, fear ladders', 'Your personal fear ladder'),
    (14, 'Rejection therapy: psychology, rules, 30-step ladder, 30-day challenge, comfort-zone challenges', '30-day rejection challenge'),
    (15, 'Hedonic adaptation, social comparison, money, meaning, flow', 'A happiness experiment'),
    (16, 'Attention economy, phone plan, digital-detox day', 'A phone plan and a detox day'),
    (17, 'Safety, warm-ups, bodyweight strength, cardio, mobility', '30-day fitness challenge'),
    (18, 'The Common Yoga Protocol', 'A safe 20-minute yoga routine'),
    (19, 'Sleep science and your sleep plan', 'A 2-week sleep plan with a log'),
    (20, 'The ICMR plate in Kerala meals, protein on a budget, food myths', 'A week of balanced plates'),
    (21, 'Phone and laptop ergonomics, eye care', 'Your study-space fix'),
    (22, 'Check-ups, hydration, tobacco and alcohol', 'A personal prevention plan'),
    (23, 'Hygiene, grooming, dressing well on a budget', 'A grooming routine and a budget wardrobe'),
    (24, 'First impressions, warmth and competence, halo, attribution error, stereotypes', 'Field notes on first impressions'),
    (25, 'Similarity, familiarity, conversation, listening, names, praise', '14 days of conversation challenges'),
    (26, 'Storytelling, assertiveness, saying no, NVC, feedback, difficult conversations', 'One real piece of feedback given'),
    (27, 'Talk structure, voice, body language, nerves, etiquette, English and Malayalam', 'A 5-minute talk to a real audience'),
    (28, 'Seven principles of influence, framing, ethics', 'The persuasion lab'),
    (29, 'Interests, BATNA, anchoring, win-win', 'A real small negotiation'),
    (30, 'Conformity, obedience, groupthink, loafing, bystander effect, trust, leading', 'Field notes and a led group task'),
    (31, 'Friendships, family, conflict, lasting relationships, networking', 'A relationship map and 5 outreach messages'),
    (32, 'High-pressure sales, MLM, scams, dark patterns, gaslighting, emotional blackmail', 'A manipulation-spotting file'),
    (33, 'Sales and marketing psychology, interviews, exam nerves', 'A mock PSC interview, recorded'),
    (34, 'Integrity, responsibility, humility, humour', 'A character audit'),
    (35, 'Meaning, volunteering, giving back', 'A contribution project'),
    (36, 'Behaviour-change project, social-skills project, personal operating system', 'Your one-page Personal Playbook'),
]


def total_hours():
    return sum(LOAD.values())


def week_plan():
    """Return {week: (items, hours)} at part-time pace."""
    plan_ = {0: (['Week 0: setup and baseline tests'], LOAD[0])}

    def add(w, item, hrs):
        items, h = plan_.get(w, ([], 0))
        if item and item not in items:
            items.append(item)
        plan_[w] = (items, h + hrs)

    for m, (title, lessons, ph) in enumerate(plan.MODULES, 1):
        for l, (lt, h) in enumerate(lessons, 1):
            a, b = WEEKS[(m, l)]
            label = code_of(m, l) + ('' if a == b else f' (weeks {a}–{b})')
            for w in range(a, b + 1):
                add(w, label, h / (b - a + 1))
        add(PROJECT_WEEK[m], f'M{m:02d} project', ph)
    for w in range(1, FINAL + 1):
        add(w, '', plan.REVIEW_H)
    add(FINAL, 'final retest and checklist', 1.5)
    return plan_


def daily_load(w):
    """Daily practice minutes on top of study, for the schedule table."""
    mins, what = 10, ['tracker and journal lines']
    spans = [((12, 1), 10, 'meditation'), ((14, 3), 10, 'rejection request'), ((17, 3), 25, 'workout')]
    for (m, l), mn, name in spans:
        s = wk(m, l)
        if s <= w:
            mins += mn
            what.append(name)
    if wk(3, 3) <= w < wk(3, 3) + 2:
        mins += 5
        what.append('bias journal')
    if wk(11, 2) <= w < wk(11, 2) + 2:
        mins += 5
        what.append('thought records')
    return mins, what


def schedule_rows():
    rows = []
    wp = week_plan()
    for w in range(0, FINAL + 1):
        items, h = wp.get(w, ([], 0))
        part = ''
        for letter, title, a, z in plan.PARTS:
            if wk(a, 1) == w:
                part = f'**Part {letter} starts.** '
        mins, _ = daily_load(w) if w else (0, [])
        rows.append((str(w), part + (', '.join(items) or 'catch-up week'), f'{h:.1f}', f'{mins}' if w else '—'))
    return rows


def full_time_rows():
    rows = []
    notes = {
        1: 'Week 0 setup and the baseline (the sleep log and resting heart rate need 7 days; start them on day 1 and keep going while you study Part A).',
        3: 'Bias journal (2 weeks) and the personal experiment (2 weeks) run in real days alongside the modules.',
        4: 'The 30-day meditation and journaling challenges start; they run in real days to about calendar week 8.',
        5: 'The 30-day rejection challenge starts (real days, to about week 9). Part C starts: the 30-day fitness challenge begins.',
        8: 'Part D: do the conversation challenges for 14 real days; give the 5-minute talk when an audience is available.',
        10: 'Start the 30-day capstone as soon as you finish M36-L01. It needs a real month.',
    }
    names = {m: plan.MODULES[m - 1][0] for m in range(1, 37)}
    c = 1
    while True:
        lo = int((c - 1) / FULL_TIME_WEEK + 0.999) if c > 1 else 0
        hi = min(int(c / FULL_TIME_WEEK - 0.001), FINAL)
        mods = []
        for m in range(1, 37):
            ws = [WEEKS[(m, l)] for l in range(1, len(plan.MODULES[m - 1][1]) + 1)]
            s, e = min(x[0] for x in ws), max(max(x[1] for x in ws), PROJECT_WEEK[m])
            if s <= hi and e >= lo:
                mods.append(f'M{m:02d}')
        rows.append((str(c), f'{lo}–{hi}', ', '.join(mods) or '—', notes.get(c, '')))
        if hi >= FINAL:
            break
        c += 1
    return rows


SAFETY = f"""
**This course is not therapy and not medical care.** It teaches everyday psychology and healthy habits. It cannot diagnose or treat anything. Talk to a doctor or a mental health professional if, for two weeks or more, low mood, worry, sleep problems or loss of interest are stopping you from studying, working or enjoying things; if you have thoughts of harming yourself; or if you use alcohol, tobacco or other substances to cope. In India you can call **Tele-MANAS on 14416 or 1-800-89-14416** (toll-free, 24 hours, in the language you choose; {link('telemanas', 'checked ' + VDATE)}). In an emergency, call 112 or go to the nearest hospital.

**Before the fitness modules,** see a doctor first if you have heart, lung, joint or blood-pressure problems, diabetes, a recent injury or surgery, are pregnant, or get chest pain, dizziness or unusual breathlessness when active.
"""


def start_section():
    total = total_hours()
    n_lessons = sum(len(x[1]) for x in plan.MODULES)
    part_rows = []
    for letter, title, a, z in plan.PARTS:
        hrs = sum(sum(h for _, h in plan.MODULES[m - 1][1]) + plan.MODULES[m - 1][2] for m in range(a, z + 1))
        weeks_ = f'{wk(a, 1)}–{max(PROJECT_WEEK[m] for m in range(a, z + 1))}'
        part_rows.append((f'**{letter}: {title}**', f'Modules {a}–{z}', weeks_, f'about {round(hrs)} h'))
    content = f"""
## What this course is

A practical, evidence-based course in everyday psychology, self-mastery, health and people skills, built for one learner: a 30-year-old near Kuttiady, Kozhikode, preparing for Kerala PSC exams, with an Android phone, an old laptop, no gym and a budget of ₹0. Every lesson ends with something you **do** in real life, and a piece of **proof** you keep: a log entry, a recording, a tracker screenshot. Over {FINAL} weeks you build a **personal operating system**: morning and evening routines, a weekly review, a 12-month growth plan and a one-page **Personal Playbook**.

## What you will be able to do

- Explain how your mind really works (fast and slow thinking, shortcuts, emotions) and catch your own thinking traps.
- Read a psychology claim and judge it: experiment or correlation, sample size, replicated or not.
- Run daily habits that stick: a habit tracker, a weekly reflection, a meditation and journaling practice, a home workout and a sleep routine.
- Handle stress, failure and strong emotions with tested tools (thought records, reappraisal, self-compassion, Stoic exercises), and know when to get professional help.
- Act with more courage: a fear ladder, 30 days of rejection therapy, speaking up, a 5-minute talk to a real audience in English or Malayalam.
- Connect with people: listen, ask follow-up questions, remember names, give real praise and honest feedback, say no, negotiate and lead a small group.
- Influence people **honestly**, and recognise and resist manipulation: high-pressure sales, scams, MLM, gaslighting, emotional blackmail and dark patterns.
- Measure yourself: the same baseline tests at the start and the end show what changed.

## Duration

- **{len(plan.MODULES)} modules, {n_lessons} lessons**, in five parts. Lessons take 10 to 25 minutes to read plus a real-world task.
- **Part-time:** {FINAL} weeks at about 5 to 6 study hours a week (about {round(total)} hours in all), alongside PSC preparation. Daily practices add 10 to 40 minutes a day on top, but they replace things you would do anyway (exercise, winding down) and they are the point of the course.
- **Full-time:** about {len(full_time_rows())} calendar weeks at about 15 hours a week. The 30-day challenges still take 30 real days each; the **Weekly schedule** page shows how they overlap.

## The five parts

Each part works on its own: its part page tells you the minimum setup and baseline tests you need if you start there.

{table(['Part', 'Modules', 'Part-time weeks', 'Study time'], part_rows)}

## How every lesson works

Psychology lessons follow one flow: **the principle in one line → the science (the key study, explained honestly) → how strong the evidence is → an everyday Kerala example → how to use it on yourself or with others → an action task with proof**. Health and skills lessons follow the same shape. Each lesson also has free resources (with exactly what to study and how long), a copy-ready template, common mistakes, a 3 to 5 question quiz with answers, and a progress checklist. Each module has a project, a self-assessment rubric, a "short on time" version, revision flashcards and lines to add to your Personal Playbook.

## How strong is the evidence?

Every principle gets a rating. {EVIDENCE_KEY}

Psychology has had a **replication crisis** (PD-M02-L02): many famous findings shrank or vanished when other labs repeated them. This course tells you which ones. You will see, for example, that **power posing** does not change hormones, that **strong ego-depletion claims** failed large replications, that **learning styles** have no support, that habits do not form in "21 days" (a median of about 66 days, with a wide range, in the best-known study), and that **MBTI-style type tests** are unreliable.

## Ethics: influence yes, manipulation no

Part D teaches influence and persuasion only for honest, mutually beneficial use: the request must be true, good for the other person too, and easy to refuse. Manipulation and "dark psychology" tactics are covered only so you can **recognise and resist** them (Module 32). Rejection therapy has strict safety and respect rules (PD-M14-L02).

## Safety

{SAFETY.strip()}

## Key assumptions made for this course

- No Personal Development or Practical Psychology course existed in the app, so this is a new course. Its lesson IDs (PD-M01-L01 and so on) will not change.
- Rejection therapy has its own module (Module 14) after Confidence and courage, so the 35 topics in the brief become 36 modules, with the capstone as Module 36.
- Topics already taught in depth in other courses in this app are cross-referenced instead of repeated: procrastination, focus and exam anxiety in {xref('lrn', 'lrn-m06', 'Practical Learning Capabilities')}; money psychology and scams in {xref('fin', 'fin-m15', 'Practical Personal Finance')}; selling in {xref('ent', 'ent-m07', 'Practical Entrepreneurship')}.
- Notes and proof are kept in **Joplin** (free and open source) in a notebook called **Playbook**, with one sub-notebook per module. Any notes app or a paper notebook works too.
- All examples and characters (Anu, Ashiq, Sreeja, Joseph sir and others) are fictional.

## The course map

{table(['Module', 'What it covers', 'What you build'], [(f'M{m:02d}', what, build) for m, what, build in MODULE_MAP])}

## Start here

1. Read the **Weekly schedule** page.
2. Do **Week 0: setup** (about 1 hour) and the **Baseline tests** (spread over 7 days: the sleep log and heart rate need a week).
3. Start Module 1 in week 1, and the **daily system track** (habit tracker and Sunday reflection) at the same time.
"""
    return {
        'id': 'pd-start',
        'title': 'Start here: Mind, Body and People',
        'kind': 'intro',
        'summary': f'What the course covers, how it works, how strong the evidence is, the safety rules and the course map. {len(plan.MODULES)} modules, {n_lessons} lessons, {FINAL} weeks part-time.',
        'content': content.strip(),
    }


def schedule_section():
    content = f"""
The app's **This week** view follows the part-time schedule. If you study full-time, switch the pace to **Full-time** on the course page: one course week then becomes about {round(FULL_TIME_WEEK * 7, 1)} days.

## Part-time schedule (about 5 to 6 study hours a week)

"Daily minutes" is the time for daily practices (tracker, journal, meditation, the rejection request, workouts), added gradually so no week is a shock. Catch-up weeks fall where a new part starts; use them to finish projects or rest.

{table(['Week', 'Lessons and projects', 'Study hours', 'Daily minutes'], schedule_rows())}

## A typical part-time week

- **Weekdays:** one lesson on two or three evenings (25 minutes of reading, then the task over the next days), after PSC study.
- **Every day:** the habit tracker, plus whichever daily practice is running.
- **Saturday:** the module project or a real-world task (a conversation, a negotiation, a talk).
- **Sunday:** the 20-minute **weekly reflection**, with a 1 to 2 minute recording (English and Malayalam on alternate weeks).

## Full-time schedule (about 15 hours a week)

{table(['Calendar week', 'Course weeks', 'Modules', 'Notes'], full_time_rows())}

## If you fall behind

Skip nothing that builds a habit; shrink it instead (the "short on time" box in every module). Missing a week is normal: do the weekly reflection, pick up where you stopped, and never try to do two weeks of daily practices in one day.
"""
    return {
        'id': 'pd-schedule',
        'title': 'Weekly schedule: part-time and full-time',
        'kind': 'reference',
        'summary': f'Week-by-week plan: {FINAL} weeks part-time at about 5 to 6 hours, or about {len(full_time_rows())} weeks full-time, with daily practice minutes shown.',
        'content': content.strip(),
    }


def setup_section():
    folders = ', '.join(FOLDERS[:4]) + ' … ' + FOLDERS[-1]
    content = f"""
About one hour. Everything is free; open-source apps are preferred.

## The free tool stack

{table(['Tool', 'What it is for', 'Cost and licence', 'Status'], [
    (link('loop', 'Loop Habit Tracker'), 'The daily habit tracker for the whole course', 'Free, open source (GPLv3)', STATUS['v3']),
    (link('medito', 'Medito'), 'Guided meditation for the 30-day challenge', 'Free, from a non-profit; open source', STATUS['v']),
    (link('joplin', 'Joplin'), 'Your Playbook notebook: notes, logs, photos of proof', 'Free, open source', STATUS['v3']),
    (link('wellbeing', 'Android Digital Wellbeing'), 'Screen-time numbers for the baseline and Module 16', 'Built into most Android phones', STATUS['vr']),
    ('Your phone\'s voice recorder and camera', 'Weekly speaking recordings, proof photos', 'Already on your phone', '—'),
    ('A notebook and pen', 'Journal, thought records, paper backup of everything', 'About ₹30, or one you have', '—'),
])}

## Steps

1. **Install Loop Habit Tracker.** Add the five starter habits from the **Daily system track** page, each with a reminder time.
2. **Install Joplin** (phone, and laptop if it runs). Create a notebook called **Playbook** with sub-notebooks: {folders}. Make a note called **Personal Playbook** inside it (it grows module by module) and a note called **Proof index** (one line per piece of proof: date, task code, where it is).
3. **Install Medito** now or in Module 12.
4. **Open Digital Wellbeing** (Settings > Digital Wellbeing and parental controls) and check that it is recording screen time. Names and steps vary by phone.
5. **Make a recordings folder** on your phone (for example, Recordings/Playbook). Name files like `2026-11-15 week01 EN.m4a`.
6. **Pick your time slots:** the 20-minute Sunday reflection, two or three lesson evenings, and a 10-minute evening slot for the tracker and journal.
7. **Tell one person** (a friend, sibling or study partner) what you are doing and ask them to ask you about it every Sunday. Social commitment helps (PD-M08-L01).

**Low-spec laptop?** You do not need the laptop at all. Everything works on the phone; Joplin can sync to a free account or just stay on the phone (back it up monthly with Joplin's export).
"""
    tasks = [
        ('pd-setup-loop', 'Loop Habit Tracker installed with five starter habits and reminders'),
        ('pd-setup-joplin', 'Joplin Playbook notebook made, with the Personal Playbook and Proof index notes'),
        ('pd-setup-recorder', 'Recordings folder made and a 30-second test recording saved'),
        ('pd-setup-slots', 'Weekly time slots written down, and one person told'),
    ]
    return {
        'id': 'pd-setup',
        'title': 'Week 0: free tool setup',
        'kind': 'setup',
        'weeks': [0, 0],
        'hours': 1.0,
        'summary': 'Install Loop, Joplin and (later) Medito, make your Playbook notebook and recordings folder, and choose your weekly time slots. About one hour.',
        'content': content.strip(),
        'tasks': [{'id': i, 'text': t, 'kind': 'task', 'week': 0} for i, t in tasks],
    }


def ratings_table():
    rows = []
    for scale, items in tests.SELF_RATINGS.items():
        for i, s in enumerate(items, 1):
            rows.append((scale if i == 1 else '', s, '', ''))
    return table(['Scale', 'Statement (rate 1 = not at all like me, 5 = very like me)', 'Start', 'End'], rows)


def record_table(form):
    col = 'Start' if form == 'A' else 'End'
    rows = [(a, f'1–10') for a, _ in tests.LIFE_AREAS]
    out = [f'### Life wheel ({col})', table(['Area', 'What it includes', 'Score 1–10'], [(a, d, '') for a, d in tests.LIFE_AREAS])]
    return '\n\n'.join(out)


def tests_text(form):
    qs, key = tests.mcq(tests.QUIZ_A if form == 'A' else tests.QUIZ_B, form)
    when = 'now, in week 0' if form == 'A' else f'now, in week {FINAL}'
    fit = table(['Test', 'How to do it safely', 'Unit', 'Result'], [(n, how, unit, '') for n, how, unit in tests.FITNESS_TESTS])
    return f"""
Take every test {when}, on a normal week, and write the results in a note called **Baseline {form}** in your Playbook notebook ({FOLDERS[0]}). Be honest; nobody else sees these numbers. The point is to measure change, not to score high.

## 1. Life wheel (5 minutes)

Score each area of your life from 1 (very unhappy with it) to 10 (couldn't be better). Draw it as a wheel with eight spokes if you like; low spokes show where the wheel is "flat".

{table(['Area', 'What it includes', 'Score 1–10'], [(a, d, '') for a, d in tests.LIFE_AREAS])}

## 2. Big Five personality (10 minutes)

Take the free {link('ipip-bffm', 'IPIP Big Five Factor Markers test')} (50 statements, 3 to 8 minutes; educational use only). Write down your five percentile scores: Extraversion, Agreeableness, Conscientiousness, Emotional stability, Openness (Intellect/Imagination). Traits change slowly; at the end of the course expect small shifts at most, mainly in conscientiousness and emotional stability. Lesson PD-M05-L02 explains what the scores mean and don't mean.

## 3. VIA character strengths (15 minutes)

Take the free {link('via', 'VIA character strengths survey')} (about 12 minutes). Write down your top five strengths in order. (The site offers paid reports; you don't need them.)

## 4. Fitness tests (30 minutes, plus heart rate on 3 mornings)

Read the safety box on **Start here** first. Warm up for 5 minutes (march on the spot, arm circles, gentle squats). Rest 3 to 5 minutes between tests. Stop if anything hurts sharply.

{fit}

## 5. One-week sleep log (1 minute each morning for 7 days)

Use this log every morning for 7 days. Write the averages at the bottom.

{fence(tools.SLEEP_LOG)}

## 6. Screen time (2 minutes, after 7 days)

In Digital Wellbeing, write down your **daily average screen time** for the last 7 days, the **number of unlocks** per day, and your **top 3 apps** by time.

## 7. Self-ratings (5 minutes)

Rate each statement 1 to 5. Add up each scale (5 to 25).

{ratings_table()}

## 8. Thinking-traps quiz, form {form} (10 minutes)

Answer quickly, the way you normally would; don't look anything up. Score 1 per correct answer, out of 10. The answers are under the questions: cover them first.

{qs}

### Answers, form {form}

{key}
"""


def baseline_section():
    content = tests_text('A')
    tasks = [
        ('pd-base-wheel', 'Baseline: life wheel scored'),
        ('pd-base-big5', 'Baseline: Big Five percentiles recorded'),
        ('pd-base-via', 'Baseline: VIA top five recorded'),
        ('pd-base-fitness', 'Baseline: five fitness tests done and recorded'),
        ('pd-base-sleep', 'Baseline: 7-day sleep log done, averages written'),
        ('pd-base-screen', 'Baseline: screen time, unlocks and top 3 apps recorded'),
        ('pd-base-ratings', 'Baseline: three self-rating scales totalled'),
        ('pd-base-quiz', 'Baseline: thinking-traps quiz form A scored'),
    ]
    return {
        'id': 'pd-baseline',
        'title': 'Baseline tests: measure where you start',
        'kind': 'setup',
        'weeks': [0, 1],
        'hours': 2.0,
        'summary': 'Life wheel, Big Five, VIA strengths, five fitness tests, a 7-day sleep log, screen time, self-ratings for confidence, social confidence and listening, and a 10-question thinking-traps quiz. You repeat all of them at the end.',
        'content': content.strip(),
        'tasks': [{'id': i, 'text': t, 'kind': 'task', 'week': 0} for i, t in tasks],
    }


def system_section():
    ch = challenges()
    rows = [(str(w), text, ev) for _, text, w, ev in ch]
    habits = table(['Habit', 'Starts'], tools.HABITS)
    content = f"""
Two things run underneath the whole course: a **daily habit tracker** and a **weekly reflection** with a short recording. On top of them, a series of 2-week and 30-day challenges switch on module by module. **This week** on the course page shows each checkpoint when it is due.

## 1. The daily habit tracker (every day, from week 0)

Track in Loop Habit Tracker (or on paper). Start with the first five habits only; the others switch on when their module arrives, and some switch off after their challenge ends.

{habits}

{fence(tools.HABIT_TRACKER)}

## 2. The weekly reflection (every Sunday, from week 1)

Twenty minutes, same time every week. It includes a **1 to 2 minute speaking recording**: English one week, Malayalam the next. That is your weekly speaking practice for the whole course; from Module 27 you also count filler words and pace.

{fence(tools.WEEKLY_REFLECTION)}

## 3. The challenges

{table(['From week', 'Challenge', 'Length', 'Where it is taught'], [
    (str(wk(3, 3)), 'Bias journal: 3 biases a day (yourself, the news, an ad)', '2 weeks', 'PD-M03-L03'),
    (str(wk(8, 4)), 'Personal experiment on your study time', '2 weeks', 'PD-M08-L04'),
    (str(wk(11, 2)), 'Thought records whenever a feeling is strong', '2 weeks', 'PD-M11-L02'),
    (str(wk(12, 1)), 'Meditation, 5 to 10 minutes a day', '30 days, then keep', 'PD-M12-L01'),
    (str(wk(12, 2)), 'Journaling with gratitude, 5 minutes a day', '30 days, then keep', 'PD-M12-L02'),
    (str(wk(14, 3)), 'Rejection therapy, one request a day', '30 days', 'PD-M14-L03'),
    (str(wk(17, 3)), 'Fitness, 20 to 30 minutes on 5 days a week', '30 days, then keep', 'PD-M17-L03'),
    (str(wk(25, 2)), 'Conversation challenges: listening first, names, follow-up questions', '14 days', 'PD-M25-L02'),
    (str(wk(36, 2)), 'Capstone: 30-day behaviour-change project and social-skills project', '30 days', 'PD-M36-L02'),
])}

**Peak load:** weeks {wk(17, 3)} to {wk(17, 3) + 2} can have meditation, the end of the rejection challenge and the start of the fitness challenge at once (about 45 minutes a day). If that is too much, start the fitness challenge the day after the rejection challenge ends; the app will simply show those checkpoints as overdue for a week.

## Checkpoints

{table(['Due by week', 'Checkpoint', 'Evidence'], rows)}

The weekly reflection is a checkpoint every week as well (not listed above).

## When you miss a day

Never miss twice. A missed day is data: write in the tracker's note why it happened (no cue, too big, bad day) and fix that one thing. Count challenge days, not calendar days: if you miss one, the 30 days end a day later.
"""
    tasks = [{'id': f'pd-reflect-w{w:02d}', 'text': f'Weekly reflection and recording, week {w}', 'kind': 'project', 'week': w,
              'detail': '**Evidence:** your written reflection and the recording file name in the Proof index. Language this week: ' + ('English' if w % 2 else 'Malayalam') + '.'}
             for w in range(1, FINAL + 1)]
    tasks += [{'id': i, 'text': t, 'kind': 'project', 'week': w, 'detail': f'**Evidence:** {ev}.'} for i, t, w, ev in ch]
    tasks.sort(key=lambda t: (t['week'], t['id']))
    return {
        'id': 'pd-system',
        'title': 'Daily system track: habit tracker, weekly reflection and 30-day challenges',
        'kind': 'track',
        'weeks': [1, FINAL],
        'summary': 'The daily habit tracker, a 20-minute Sunday reflection with a short recording, and the bias, experiment, thought-record, meditation, journaling, rejection, fitness and conversation challenges, with checkpoints.',
        'content': content.strip(),
        'tasks': tasks,
    }


def toolkit_section():
    parts = ["""
Every copy-ready tool in the course, in one place. Copy them into Joplin, a notebook or a spreadsheet. The lesson named under each tool explains how to use it well.
"""]
    for name, body, where in tools.TOOLKIT:
        parts.append(f'## {name}\n\nFrom {where}.\n\n' + fence(body))
    return {
        'id': 'pd-toolkit',
        'title': 'Toolkit: every copy-ready template in one place',
        'kind': 'reference',
        'summary': 'Habit tracker, weekly reflection, bias journal, decision sheet, experiment log, thought record, rejection log, workout and sleep logs, conversation log, feedback script, speaking log, persuasion lab, negotiation prep, field notes, manipulation check, routines and the Personal Playbook.',
        'content': '\n\n'.join(p.strip() for p in parts),
    }


PART_INFO = {
    'A': ('How your mind takes shortcuts, how to read research, your thinking traps, and better decisions.',
          ['Thinking-traps quiz (form A)', 'Life wheel'],
          ['Joplin Playbook notebook'],
          'You will notice your own mental shortcuts as they happen, read any psychology headline with healthy doubt, and have a decision sheet for big choices.'),
    'B': ('Values, strengths, motivation, goals, habits, mindset, emotions, stress, mindfulness, confidence, rejection therapy, happiness and attention.',
          ['Life wheel', 'Big Five', 'VIA', 'Confidence and social-confidence ratings', 'Screen time'],
          ['Loop Habit Tracker', 'Joplin Playbook notebook', 'Medito (Module 12)'],
          'You will have a values list, a 12-month plan, habits that run on cues, two weeks of thought records, 30 days of meditation, journaling and rejection requests, and a phone that works for you.'),
    'C': ('A safe no-equipment fitness programme, yoga, sleep, a Kerala diet, posture and eye care, prevention and grooming.',
          ['Five fitness tests', '7-day sleep log', 'Life wheel (health area)'],
          ['Loop Habit Tracker', 'A mat or folded bedsheet', 'A timer'],
          'You will be training 3 to 5 days a week with a log, sleeping on a regular schedule, eating balanced plates, and have a check-up plan.'),
    'D': ('How people see each other, rapport, communication, public speaking, honest influence, negotiation, groups, relationships, manipulation defence and psychology at work.',
          ['Social-confidence and listening ratings', 'Thinking-traps quiz (questions 2, 3 and 10)'],
          ['Joplin Playbook notebook', 'Phone voice recorder', 'Loop Habit Tracker'],
          'You will have had dozens of better conversations, given real feedback, negotiated a purchase, spoken for 5 minutes to an audience, and built a file of manipulation red flags.'),
    'E': ('Character, purpose and contribution, and the capstone that pulls everything into your personal operating system.',
          ['Every baseline test (you will retest them all at the end)'],
          ['Everything from earlier parts'],
          'You will have run a 30-day behaviour-change project and a social-skills project with data, and written your one-page Personal Playbook.'),
}


def part_section(letter):
    _, title, a, z = [p for p in plan.PARTS if p[0] == letter][0]
    what, base, tools_, result = PART_INFO[letter]
    start = wk(a, 1)
    end = max(PROJECT_WEEK[m] for m in range(a, z + 1))
    mods = [(f'Module {m}', plan.MODULES[m - 1][0], f'{len(plan.MODULES[m - 1][1])}') for m in range(a, z + 1)]
    hrs = sum(sum(h for _, h in plan.MODULES[m - 1][1]) + plan.MODULES[m - 1][2] for m in range(a, z + 1))
    content = f"""
## What this part covers

{what}

{table(['Module', 'Title', 'Lessons'], mods)}

Part-time: weeks {start}–{end}, about {round(hrs)} study hours. Full-time: about {max(1, round((end - start + 1) * FULL_TIME_WEEK))} calendar weeks.

## Taking this part on its own

If you start the course here, do this first (about 45 minutes, plus any 7-day logs):

1. Read **Start here**, especially the evidence key and the **safety** box.
2. Do the parts of **Week 0: setup** you need: {', '.join(tools_)}.
3. Take these baseline tests from the **Baseline tests** page: {', '.join(base)}. Retake them at the end of the part to see what changed.
4. Start the **daily habit tracker** and the **Sunday reflection** from the Daily system track. They make any part stick.
5. Lessons sometimes point to earlier lessons by code (for example PD-M08-L03). Each one is short; read it when it comes up rather than going back to the start.

## What you will have at the end

{result}

The part review on the Daily system track (due week {end}) asks you to write half a page on what changed and what you are keeping.
"""
    return {
        'id': f'pd-part-{letter.lower()}',
        'title': f'Part {letter}: {title}',
        'kind': 'gate',
        'weeks': [start, start],
        'summary': f'Part {letter} overview: Modules {a}–{z}, weeks {start}–{end}. How to take this part on its own, which baseline tests to take, and what you will have at the end.',
        'content': content.strip(),
        'tasks': [{'id': f'pd-part-{letter.lower()}-start', 'text': f'Part {letter}: read the overview; if starting here, standalone setup and baseline done', 'kind': 'task', 'week': start}],
    }


def front():
    return [start_section(), schedule_section(), setup_section(), baseline_section(), system_section(), toolkit_section()]


# ---------------------------------------------------------------- back matter

SYSTEM_ITEMS = [
    ('pd-final-tracker', 'Habit tracker in use for the whole course, with at least 5 habits above 80% in the last month', 'Week 0 onwards'),
    ('pd-final-reflections', 'At least 20 weekly reflections and recordings', 'Daily system track'),
    ('pd-final-bias', 'Two weeks of bias journal, and your top three traps named', 'PD-M03-L03'),
    ('pd-final-decision', 'A decision sheet used for a real decision', 'PD-M04-L02'),
    ('pd-final-plan', 'A 12-month plan and a weekly planning routine', 'Module 7'),
    ('pd-final-experiment', 'A two-week personal experiment with data and a decision', 'PD-M08-L04'),
    ('pd-final-thought', 'Two weeks of thought records', 'PD-M11-L02'),
    ('pd-final-challenges', 'The 30-day meditation, journaling, rejection and fitness challenges completed (or restarted and completed)', 'Modules 12, 14 and 17'),
    ('pd-final-body', 'A training plan, a sleep window and a plate you actually follow', 'Part C'),
    ('pd-final-conv', '14 days of conversation challenges logged', 'PD-M25-L02'),
    ('pd-final-feedback', 'One real piece of constructive feedback given with the script', 'PD-M26-L03'),
    ('pd-final-talk', 'A 5-minute talk given to a real audience, recorded', 'Module 27'),
    ('pd-final-lab', 'The persuasion lab and a real negotiation, with results', 'Modules 28 and 29'),
    ('pd-final-manip', 'A manipulation-spotting file with at least 10 real examples analysed', 'Module 32'),
    ('pd-final-capstone', 'Capstone: 30-day behaviour-change project and social-skills project, with data', 'Module 36'),
    ('pd-final-playbook', 'Your one-page Personal Playbook, morning and evening routines, and 12-month growth plan', 'PD-M36-L03'),
]


def final_section():
    fit = table(['Test', 'Start', 'End', 'Change'], [(n, '', '', '') for n, _, _ in tests.FITNESS_TESTS])
    compare = table(['Measure', 'Start', 'End', 'Change'], [
        ('Life wheel: total of 8 areas (out of 80)', '', '', ''),
        ('Life wheel: lowest area', '', '', ''),
        ('Big Five: conscientiousness / emotional stability percentiles', '', '', ''),
        ('VIA top five (same or different?)', '', '', ''),
        ('Average sleep (hours) and quality (1–5)', '', '', ''),
        ('Screen time per day and unlocks', '', '', ''),
        ('Confidence scale (5–25)', '', '', ''),
        ('Social-confidence scale (5–25)', '', '', ''),
        ('Listening scale (5–25)', '', '', ''),
        ('Thinking-traps quiz (out of 10; A at start, B at end)', '', '', ''),
    ])
    content = f"""
Take every test again, the same way as in week 0, then compare. Use **form B** of the thinking-traps quiz (form A's answers would be remembered). Use the same push-up version, route and time of day as at the start.

## How to read your results honestly

- **Small changes are real changes.** One or two points on a 25-point scale, or a few more push-ups, matter when they come from habits you will keep.
- **Personality barely moves in months.** If your Big Five scores hardly changed, that is normal. Habits and skills change faster than traits.
- **Some numbers get worse for good reasons.** Your screen time may rise in an exam month; your rejection fears may feel bigger because you finally notice them. Write the reason next to the number.
- **The quiz is not an IQ test.** It measures whether you now slow down on trap questions. Knowing the traps helps less than you would hope (PD-M03-L03): the habit of checking is what counts.

{tests_text('B').strip()}

## Compare start and end

{compare}

### Fitness

{fit}

## Final checklist: your personal operating system

Tick each item under **Your tasks**. Each line shows where it was built.

{table(['Item', 'Built in'], [(t, w) for _, t, w in SYSTEM_ITEMS])}

## Your final reflection (one page)

1. The three biggest changes, with the numbers that show them.
2. The three habits you will keep for the next 12 months, with their cues.
3. One thing that did not work for you, and why.
4. Who helped, and how you will thank them.
5. Read your Personal Playbook aloud and record it (2 to 3 minutes). Listen to it on the 1st of each month.
"""
    tasks = [{'id': f'pd-final-{k}', 'text': t, 'kind': 'task', 'week': FINAL} for k, t in [
        ('wheel', 'Final: life wheel scored and compared'),
        ('big5', 'Final: Big Five retaken and compared'),
        ('via', 'Final: VIA retaken and compared'),
        ('fitness', 'Final: five fitness tests done and compared'),
        ('sleep', 'Final: 7-day sleep log done and compared'),
        ('screen', 'Final: screen time and unlocks compared'),
        ('ratings', 'Final: three self-rating scales totalled and compared'),
        ('quiz', 'Final: thinking-traps quiz form B scored'),
    ]]
    tasks += [{'id': i, 'text': t, 'kind': 'task', 'week': FINAL} for i, t, _ in SYSTEM_ITEMS]
    tasks.append({'id': 'pd-final-reflection', 'text': 'Final reflection written and the Playbook recording saved', 'kind': 'exit', 'week': FINAL})
    return {
        'id': 'pd-final',
        'title': 'Final retest and checklist',
        'kind': 'capstone',
        'weeks': [FINAL, FINAL],
        'hours': 1.5,
        'summary': 'Repeat every baseline test (form B of the quiz), compare start and end, tick the final checklist of your personal operating system and write a one-page reflection.',
        'content': content.strip(),
        'tasks': tasks,
    }


def next_section():
    content = f"""
## The next 12 months

{table(['When', 'Focus', 'How'], [
    ('Every day', 'Keep the 3 to 6 habits that earned a place in your Playbook', 'Loop Habit Tracker; never miss twice'),
    ('Every Sunday', 'Weekly reflection and recording', 'The same template; it is your steering wheel'),
    ('1st of each month', 'Re-read your Personal Playbook and pick one monthly focus', 'One module\'s project, repeated at a harder level'),
    ('Every 3 months', 'Retest fitness and the three self-rating scales', 'The baseline page; write the change in your Playbook'),
    ('Every 6 months', 'Life wheel and 12-month plan review', 'PD-M07-L01 and PD-M07-L02'),
    ('Once a year', 'A new 30-day challenge (rejection, speaking, fitness or a new one)', 'The challenge templates on the Toolkit page'),
])}

## Go deeper (all free)

- **Psychology:** read {link('os-psych', 'OpenStax Psychology 2e')} chapters 2, 7, 10, 12 and 14 in full (about 2 hours each), then work through the {link('mit-psych', 'MIT OCW Introduction to Psychology')} lectures (about 1 hour each) and the {link('noba', 'Noba modules')} on topics you liked.
- **Wellbeing:** audit {link('yale-wb', 'The Science of Well-Being')} (about 13 hours over 6 weeks) and try one new {link('ggia', 'Greater Good in Action')} practice a month.
- **Stoicism and character:** one letter of {link('seneca', 'Seneca')} a week, and a book of {link('meditations', 'Meditations')} a month.
- **Speaking:** visit {link('tm-calicut', 'Calicut Toastmasters')} as a guest (check meeting details and any fees with the club first), or start a speaking circle with friends using the PD-M27 practice plan.
- **Other courses in this app:** {xref('lrn', 'lrn-start', 'Practical Learning Capabilities')} for study skills and PSC exam mastery; {xref('fin', 'fin-m01', 'Practical Personal Finance')} for money habits; {xref('ent', 'ent-m03', 'Practical Entrepreneurship')} to turn people skills into customer conversations and sales.

## Signs you need more than a course

If a problem keeps returning despite your best effort for several weeks (sleep, mood, anxiety, anger, a habit you cannot control), that is a reason to see a professional, not a personal failure. Tele-MANAS (**14416**) is free and confidential to call; a doctor at your local Family Health Centre can refer you.
"""
    return {
        'id': 'pd-next',
        'title': 'What next: your 12-month roadmap',
        'kind': 'reference',
        'summary': 'How to keep the system running for a year, free resources to go deeper, other courses in the app, and when to get professional help.',
        'content': content.strip(),
    }


GLOSSARY = [
    ('System 1 / System 2', 'വേഗ ചിന്ത / മന്ദ ചിന്ത', 'Fast, automatic thinking versus slow, effortful thinking'),
    ('Heuristic', 'ചിന്താ കുറുക്കുവഴി', 'A mental shortcut that is usually good enough but sometimes wrong'),
    ('Cognitive bias', 'ചിന്താ പക്ഷപാതം', 'A predictable error in thinking'),
    ('Confirmation bias', 'സ്ഥിരീകരണ പക്ഷപാതം', 'Looking only for evidence that agrees with what you already believe'),
    ('Sunk cost', 'മുടക്കിപ്പോയ ചെലവ്', 'Money or time already spent that cannot be recovered'),
    ('Overconfidence', 'അമിത ആത്മവിശ്വാസം', 'Being more sure than your accuracy justifies'),
    ('Planning fallacy', 'ആസൂത്രണ പിഴവ്', 'Underestimating how long tasks will take'),
    ('Loss aversion', 'നഷ്ടഭയം', 'Losses feel bigger than equal gains'),
    ('Anchoring', 'നങ്കൂരമിടൽ (ആദ്യ സംഖ്യയുടെ സ്വാധീനം)', 'The first number you hear pulls your judgement'),
    ('Availability heuristic', 'ഓർമ്മയിൽ എളുപ്പം വരുന്നതിനെ ആശ്രയിക്കൽ', 'Judging how common something is by how easily examples come to mind'),
    ('Base rate', 'അടിസ്ഥാന നിരക്ക്', 'How common something is in general, before details'),
    ('Correlation', 'പരസ്പര ബന്ധം', 'Two things that tend to go together, without proof that one causes the other'),
    ('Causation', 'കാര്യകാരണ ബന്ധം', 'One thing actually making another happen'),
    ('Experiment', 'പരീക്ഷണം', 'A study where researchers change one thing and compare groups'),
    ('Sample size', 'സാമ്പിൾ വലിപ്പം', 'How many people a study included'),
    ('Replication', 'ആവർത്തന പഠനം', 'Repeating a study to see if the result holds'),
    ('Replication crisis', 'ആവർത്തന പ്രതിസന്ധി', 'The discovery that many famous findings did not repeat'),
    ('Effect size', 'ഫലത്തിന്റെ വലിപ്പം', 'How big a difference is, not just whether it exists'),
    ('Cognitive distortion', 'ചിന്താ വൈകല്യം', 'An unhelpful thinking pattern named in CBT'),
    ('CBT (cognitive behavioural therapy)', 'കോഗ്നിറ്റീവ് ബിഹേവിയറൽ തെറാപ്പി', 'A well-tested therapy that works on thoughts and actions'),
    ('Pre-mortem', 'മുൻകൂർ പരാജയ വിശകലനം', 'Imagining a plan has failed in order to find its weak points'),
    ('Choice overload', 'തിരഞ്ഞെടുപ്പ് ബാഹുല്യം', 'Feeling stuck when there are too many options'),
    ('Values', 'മൂല്യങ്ങൾ', 'What matters most to you, guiding how you want to act'),
    ('Big Five', 'അഞ്ച് പ്രധാന വ്യക്തിത്വ ഗുണങ്ങൾ', 'Five broad personality traits measured on a scale'),
    ('Character strengths', 'സ്വഭാവ ശക്തികൾ', 'Positive traits such as kindness, curiosity and honesty'),
    ('Intrinsic motivation', 'ആന്തരിക പ്രചോദനം', 'Doing something because it is interesting or meaningful in itself'),
    ('Extrinsic motivation', 'ബാഹ്യ പ്രചോദനം', 'Doing something for a reward or to avoid punishment'),
    ('Autonomy', 'സ്വയംഭരണം', 'Feeling that your actions are your own choice'),
    ('Present bias', 'വർത്തമാന പക്ഷപാതം', 'Valuing rewards now far more than bigger rewards later'),
    ('Commitment device', 'പ്രതിജ്ഞാ ഉപാധി', 'An arrangement that makes it harder to break a promise to yourself'),
    ('Temptation bundling', 'ഇഷ്ടവും കടമയും ചേർക്കൽ', 'Allowing a treat only while doing a task you avoid'),
    ('Habit loop (cue, routine, reward)', 'ശീല ചക്രം (സൂചന, പ്രവൃത്തി, പ്രതിഫലം)', 'The trigger, the action and the payoff that build a habit'),
    ('Implementation intention (if-then plan)', 'എങ്കിൽ-അപ്പോൾ പദ്ധതി', 'A plan of the form "If X happens, then I will do Y"'),
    ('Procrastination', 'നീട്ടിവയ്ക്കൽ', 'Delaying a task even though delay will make things worse'),
    ('Growth mindset', 'വളർച്ചാ മനോഭാവം', 'The belief that abilities can be developed with effort and good strategies'),
    ('Self-compassion', 'സ്വയം കരുണ', 'Treating yourself with the kindness you would show a friend'),
    ('Emotional intelligence', 'വൈകാരിക ബുദ്ധി', 'Noticing, understanding and managing emotions in yourself and others'),
    ('Affect labelling', 'വികാരത്തിന് പേര് നൽകൽ', 'Putting a feeling into words, which can calm it'),
    ('Reappraisal', 'പുനർ വിലയിരുത്തൽ', 'Changing how you interpret a situation to change how you feel'),
    ('Empathy', 'സഹാനുഭൂതി', 'Understanding and sharing another person\'s feelings'),
    ('Negativity bias', 'നിഷേധാത്മക പക്ഷപാതം', 'Bad events weigh more in the mind than good ones'),
    ('Stress response', 'സമ്മർദ്ദ പ്രതികരണം', 'The body\'s fight-or-flight reaction to a demand or threat'),
    ('Resilience', 'അതിജീവന ശേഷി', 'Bouncing back from difficulty'),
    ('Thought record', 'ചിന്താ രേഖ', 'A CBT worksheet for examining an upsetting thought'),
    ('Stoicism', 'സ്റ്റോയിക് ചിന്ത', 'An ancient philosophy of focusing on what you can control'),
    ('Mindfulness', 'സൂക്ഷ്മ ബോധം', 'Paying attention to the present moment without judging it'),
    ('Self-efficacy', 'സ്വയം കാര്യക്ഷമതാ വിശ്വാസം', 'Belief in your ability to do a specific task'),
    ('Spotlight effect', 'ശ്രദ്ധാകേന്ദ്ര മിഥ്യ', 'Overestimating how much others notice you'),
    ('Impostor feelings', 'കപടനാണെന്ന തോന്നൽ', 'Feeling like a fraud despite evidence of ability'),
    ('Exposure (fear ladder)', 'ഭയ ഗോവണി', 'Facing fears step by step, from easy to hard, until they shrink'),
    ('Rejection therapy', 'നിരസന ചികിത്സ (നിരസനം ശീലിക്കൽ)', 'Seeking small, safe "no"s on purpose to lose the fear of rejection'),
    ('Hedonic adaptation', 'സുഖാനുകൂലനം', 'Getting used to good and bad changes so they stop affecting mood'),
    ('Social comparison', 'സാമൂഹിക താരതമ്യം', 'Judging yourself against others'),
    ('Flow', 'ലയാവസ്ഥ', 'Being fully absorbed in a challenging task'),
    ('Dark pattern', 'വഞ്ചനാത്മക ഡിസൈൻ', 'An app or website design that tricks you into choices'),
    ('Warm-up', 'ശരീരം ചൂടാക്കൽ', 'Light movement that prepares the body for exercise'),
    ('Progressive overload', 'ക്രമാനുഗത ഭാരവർധന', 'Making exercise slightly harder over time'),
    ('Resting heart rate', 'വിശ്രമ ഹൃദയമിടിപ്പ്', 'Heartbeats per minute when sitting still'),
    ('Asana / pranayama', 'ആസനം / പ്രാണായാമം', 'Yoga postures / yoga breathing practices'),
    ('Circadian rhythm', 'ശരീര ഘടികാരം', 'The body\'s roughly 24-hour clock'),
    ('Protein', 'മാംസ്യം (പ്രോട്ടീൻ)', 'The nutrient the body uses to build and repair'),
    ('Ergonomics', 'ശരീരസൗഹൃദ ക്രമീകരണം', 'Arranging your space to fit your body'),
    ('Halo effect', 'പ്രഭാവലയ പ്രഭാവം', 'One good trait making us rate everything about a person higher'),
    ('Fundamental attribution error', 'അടിസ്ഥാന ആരോപണ പിഴവ്', 'Blaming people\'s character and ignoring their situation'),
    ('Stereotype', 'മുൻധാരണ', 'A fixed, oversimplified idea about a group'),
    ('Rapport', 'ആത്മബന്ധം', 'A feeling of connection and understanding between people'),
    ('Active listening', 'സജീവ ശ്രവണം', 'Listening to understand, and showing it'),
    ('Assertiveness', 'ദൃഢനിശ്ചയത്തോടെയുള്ള ആശയവിനിമയം', 'Saying what you need clearly and respectfully'),
    ('Non-violent communication', 'അക്രമരഹിത ആശയവിനിമയം', 'Observations, feelings, needs and requests instead of blame'),
    ('Face-saving', 'മാനം കാക്കൽ', 'Letting someone keep their dignity in a disagreement'),
    ('Reciprocity', 'പ്രത്യുപകാരം', 'The urge to return favours'),
    ('Social proof', 'സാമൂഹിക തെളിവ്', 'Doing what others like us are doing'),
    ('Scarcity', 'ദൗർലഭ്യം', 'Things seem more valuable when they are rare or running out'),
    ('Framing', 'അവതരണ രീതി', 'How the same facts are presented changes choices'),
    ('BATNA', 'ഒത്തുതീർപ്പിലെത്തിയില്ലെങ്കിലുള്ള മികച്ച ബദൽ', 'Your best option if the negotiation fails'),
    ('Conformity', 'അനുരൂപപ്പെടൽ', 'Changing behaviour to match a group'),
    ('Obedience', 'അനുസരണ', 'Following orders from an authority'),
    ('Groupthink', 'സംഘ ചിന്ത', 'A group agreeing too quickly and ignoring doubts'),
    ('Social loafing', 'കൂട്ടത്തിലെ ഉഴപ്പ്', 'Putting in less effort when working in a group'),
    ('Bystander effect', 'കാഴ്ചക്കാരന്റെ നിഷ്ക്രിയത്വം', 'Being less likely to help when others are present'),
    ('Gaslighting', 'ഗ്യാസ്‌ലൈറ്റിംഗ് (ഓർമ്മയെ സംശയിപ്പിക്കൽ)', 'Making someone doubt their own memory or sanity'),
    ('Emotional blackmail', 'വൈകാരിക ഭീഷണി', 'Using fear, obligation or guilt to control someone'),
    ('MLM (multi-level marketing)', 'ബഹുതല വിപണനം', 'Selling schemes where income depends on recruiting others'),
    ('Integrity', 'സത്യസന്ധത / ധർമ്മനിഷ്ഠ', 'Acting by your values even when no one is watching'),
    ('Humility', 'വിനയം', 'An accurate, modest view of yourself and openness to learning'),
    ('Personal operating system', 'വ്യക്തിഗത ജീവിതക്രമം', 'Your routines, reviews and rules working together'),
]


def glossary_section():
    rows = [(f'**{en}**', ml, meaning) for en, ml, meaning in GLOSSARY]
    content = f"""
Key words from the course, roughly in the order you meet them. Some English terms (CBT, BATNA, MLM) are used as they are in Malayalam conversation; the Malayalam is a plain-language rendering so you can explain the idea to family and friends. Malayalam psychology terms vary between textbooks; if your PSC material uses a different word, use that one.

{table(['English', 'മലയാളം (Malayalam)', 'Simple meaning'], rows)}
"""
    return {
        'id': 'pd-glossary',
        'title': 'Glossary with Malayalam meanings',
        'kind': 'reference',
        'summary': f'{len(GLOSSARY)} key terms in English and Malayalam, with simple meanings.',
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
Every link in this course is listed here with the date it was checked. Links were opened and read for this course (most on {VDATE}, some on 2026-11-03); nothing was copied from memory. If a link stops working, search for its title on the same website.

- **verified [date]:** the page was opened on that date and its content matched what the course says.
- **verified; check current rules:** as above, but it describes something that changes (an app, a price, free access, a meeting time, a law). Check before you rely on it.
- **headline figures checked; secondary summary:** the numbers were checked on a summary page, not the original paper. Treat them as approximate.
- **found in a web search; page not opened:** the address came from a search result but the page itself could not be opened for checking. Marked unverified.
- **unverified:** the site blocks automated checks. The address is the official one; type it yourself and check that it is the real site.

Open-licensed and official sources are preferred: OpenStax and Noba (CC BY-NC-SA 4.0), MIT OpenCourseWare, public-domain classics on Project Gutenberg and Standard Ebooks, government and health bodies (WHO, NHS, ICMR-NIN, the Ministry of Ayush), university centres (Greater Good, Harvard), and open-source apps (Loop, Medito, Joplin). Wikipedia is used for the history and criticism of classic experiments, because its articles on them cite the replication studies.

**Studies named without a link** (for example "Iyengar and Lepper, 2000") are well-known published papers described through the linked review or summary in the same lesson. The course gives numbers only where they were checked against a linked source.
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
    unverified = [k for k in used_in if R[k]['s'] in ('u', 's')]
    rules_keys = [k for k in used_in if R[k]['s'] == 'vr']
    headline = [k for k in used_in if R[k]['s'] == 'vt']
    parts.append('## Marked "unverified"\n\n' + (bullets([f"[{R[k]['title']}]({R[k]['url']})" for k in unverified]) or 'None.'))
    if headline:
        parts.append('## Secondary summaries\n\n' + bullets([f"[{R[k]['title']}]({R[k]['url']})" for k in headline]))
    parts.append('## Marked "check current rules"\n\n' + (bullets([f"[{R[k]['title']}]({R[k]['url']})" for k in rules_keys]) or 'None.'))
    sections.append({
        'id': 'pd-sources',
        'title': 'Sources and verification log',
        'kind': 'reference',
        'summary': f'Every link in the course, where it is used and when it was checked.',
        'content': '\n\n'.join(p.strip() for p in parts),
    })
