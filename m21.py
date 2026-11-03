"""Module 21: Capstone: a 30-day learning sprint."""
from common import lesson, module, link, fence, table, WEEKS
import tools

M = 21

SPRINT_START = WEEKS[(M, 2)][0]

L1 = lesson(
    M, 1,
    outcome='Choose a sprint subject (a PSC subject or a new skill), set a measurable goal, design a 30-day plan that uses your whole learning system, and take the before test.',
    split='15 minutes reading, 30 minutes building the tests, 45 minutes for the before test, 30 minutes planning',
    core=f"""
### What the sprint is

The capstone is a **30-day learning sprint**: 30 consecutive days, at least 45 minutes a day (about 22 hours in all), on **one** subject, using everything you have built in this course. You measure where you start with a **before test**, log every day, check progress every week, and measure again with an **after test** at the end. Then you write a reflection report on what worked, with your own data as evidence.

It is the proof that your learning system works, and practice for running it alone after the course.

### Choose the subject

- **A PSC subject** where you are weak and which carries marks: look at the top of your Syllabus tab's priority list (Module 12). Good sprint subjects are big enough to matter and small enough for 30 days: "the Indian Constitution", "arithmetic", "English grammar", "Kerala geography".
- **Or a new skill** for after PSC, planned with the learning project canvas (LRN-M13-L02), if your exam is far away or already over.

### Set a measurable goal

Write the goal as a number you can test: "raise my score on a 40-question Constitution test from 17 to 30", "solve 25 mixed arithmetic problems in 25 minutes with at least 22 right", "give a 3-minute self-introduction in Arabic with no more than three pauses".

### Build two matched tests

You need a **before test** now and an **after test** at the end. Don't use the same questions twice, or you will measure memory of the test, not of the subject.

1. Collect a pool of at least 80 previous-year questions on the subject (Module 12).
2. Sort them by subtopic, then split each subtopic's questions evenly into **form 1** and **form 2**, so both forms cover the same subtopics at similar difficulty.
3. Take **form 1 now**, under exam conditions, with S, U and G confidence marks (Module 7). Keep form 2 sealed until the end.

For a skill, the before test is a recorded or timed attempt at your goal.

### Plan the 30 days

{table(['Days', 'Focus'], [
    ('1–20', 'Work through the subtopics in priority order, about one or two per session, each with the six-strategy session (LRN-M03-L05) or a practice loop (Module 13)'),
    ('7, 14, 21', 'Checkpoints: a 10-question mini-test from new questions, and your weekly review'),
    ('21–28', 'Revision cycle: every subtopic by recall, mixed sets, error-log retests'),
    ('29–30', 'Light review and rest, ready for the after test on day 31'),
])}

A daily session of 45 minutes: a 5-minute warm-up recall, 25 minutes of learning or practice with the method that suits the content, 10 minutes of mixed questions, and 5 minutes to log the session in the **Sprint** tab and make cards. On bad days, do the **minimum version**: 15 minutes of recall and cards. Never miss twice (Module 6).

**Full-time track:** make sessions 60 to 90 minutes, start the sprint when you finish Module 12, and do Modules 13 to 20 alongside it (see the weekly schedule).
""",
    example="""
**Sreeja** chose the Indian Constitution: it was at the top of her priority list, and her mocks kept losing marks there. Her goal: "from 17 to 30 out of 40 on a matched test".

She collected 84 previous-year Constitution questions from her saved papers, sorted them into 12 subtopics (Preamble, citizenship, Fundamental Rights, Directive Principles, duties, Parliament, the President, the judiciary, federalism, amendments, local government, emergency provisions), and split each subtopic evenly into form 1 and form 2. Form 1 under exam conditions gave her 17 out of 40, with 9 "sure" answers wrong, mostly mix-ups.

Her 30-day plan put the subtopics with most errors first, with a memory palace for the Fundamental Rights she already had, Feynman explanations for federalism and emergency provisions, and contrast cards for her mix-ups. She set the Sprint tab up, put the checkpoints and the day-31 after test in her calendar, and told her study group so they would ask her about it every Saturday.
""",
    evidence=[
        ('The methods the sprint uses (retrieval, spacing, interleaving, explanation)', 'strong', 'The sprint is built on the best-supported techniques in this course.'),
        ('Before and after tests with matched forms', 'limited', 'A measuring tool, not research; matched forms make the comparison fairer, but some gain will come from practice and from the forms differing.'),
        ('A fixed daily minimum and "never miss twice"', 'limited', 'Practical habit rules (Module 6).'),
    ],
    resources=[
        ('psc-pyq', 'Collect at least 80 previous-year questions on your sprint subject', '30 minutes'),
        ('psc-syllabus', 'Check the subject\'s subtopics against the official syllabus', '10 minutes'),
        ('dunlosky-aps', 'Skim the technique ratings again to choose your sprint methods', '10 minutes'),
    ],
    steps=[
        'Choose your sprint subject from your Syllabus tab priorities (or a new skill with a learning project canvas), and write a measurable goal.',
        'Build two matched tests from a pool of at least 80 questions, split evenly by subtopic. Seal form 2 (in an envelope or a hidden file).',
        'Take form 1 under exam conditions with confidence marks. Record the score and your confident errors.',
        'Write your 30-day plan: subtopics by day, methods for each, checkpoint days, the revision cycle and the after-test date (day 31).',
        'Add a Sprint tab to your Learning Workbook with the headings below, and put the start date, checkpoints and after test in your calendar.',
    ],
    proof='Your goal, both test forms (form 2 still unseen), your form 1 score with confident errors, your 30-day plan and a screenshot of the Sprint tab.',
    templates=[
        ('30-day sprint plan', """
SPRINT PLAN     Subject: ______________________   Start: day 1 = ______
Goal (a number): ____________________________________________________
Before test (form 1): ___/___ on ______   After test (form 2): day 31 = ______
Daily session (45 min): warm-up recall 5 | learn or practise 25 | mixed questions 10 | log and cards 5
Minimum version (bad days, 15 min): recall + cards. Never miss twice.
Day  | Subtopic                     | Method (six-strategy, loop, Feynman, palace, cards)
1    | __________________________   | ______________________________
2    | __________________________   | ______________________________
...
7    | CHECKPOINT: 10-question mini-test + weekly review
14   | CHECKPOINT
21   | CHECKPOINT; revision cycle starts
22-28| every subtopic by recall, mixed sets, error retests
29-30| light review, rest
31   | AFTER TEST (form 2), then reflection report
""", ''),
        ('matched test builder', """
POOL: ___ questions on ______________ from papers: ____________________
Subtopic           Questions in pool   Form 1   Form 2
______________     ___                 ___      ___
______________     ___                 ___      ___
...
Totals:            ___                 ___      ___   (forms equal by subtopic [ ])
Form 2 sealed until day 31 [ ]
""", ''),
        ('Sprint tab headings', tools.SPRINT, 'csv'),
    ],
    mistakes=[
        ('A subject far too big for 30 days.', 'Choose one subject, such as the Constitution or arithmetic, not "all of GK".'),
        ('A vague goal ("get better").', 'Write a number you will test on day 31.'),
        ('Using the same questions before and after.', 'Use matched forms, or you measure memory of the test.'),
        ('No minimum version for bad days.', 'Decide it now: 15 minutes of recall and cards.'),
    ],
    quiz=[
        {'q': 'Why use two matched test forms instead of one test twice?', 'o': ['So the after test measures the subject, not memory of the test questions', 'Because PSC requires it', 'To make the test longer', 'It doesn\'t matter'], 'a': 'A', 'why': 'Repeating the same questions inflates the after score.'},
        {'q': 'Which is a measurable sprint goal?', 'o': ['"From 17 to 30 out of 40 on a matched Constitution test"', '"Learn the Constitution well"', '"Study hard for a month"', '"Feel more confident"'], 'a': 'A', 'why': 'A number can be tested on day 31.'},
        {'q': 'What happens on days 21 to 28 of the sprint plan?', 'o': ['A revision cycle: every subtopic by recall, mixed sets and error retests', 'Only new subtopics', 'Rest', 'The after test'], 'a': 'A', 'why': 'The last week consolidates everything before the after test.'},
        {'q': 'What is the minimum version for bad days?', 'o': ['15 minutes of recall and cards', 'Skip the day and the next', 'Three hours to catch up', 'Restart the sprint'], 'a': 'A', 'why': 'A small session keeps the chain; never miss twice.'},
    ],
    study='Your sprint subject\'s previous-year questions and official syllabus, and the technique ratings',
    action='Choose your sprint, build two matched tests, take the before test and write your 30-day plan',
)

L2 = lesson(
    M, 2,
    outcome='Run your 30-day sprint with a daily log, weekly checkpoint tests and adjustments, using your whole learning system every day.',
    split='45 minutes a day for 30 days, plus three weekly checkpoints',
    core=f"""
### Every day

Each session follows the same shape, so starting needs no decisions:

1. **Warm-up (5 minutes):** blank-page recall of yesterday's subtopic, then check.
2. **Learn or practise (25 minutes):** the method that suits today's subtopic. Use the six-strategy session for content (LRN-M03-L05), a practice loop for skills (LRN-M13-L01), a Feynman explanation for anything with reasons (LRN-M08-L01), a memory palace or mnemonic for lists (Module 11), or image occlusion for maps and diagrams (Module 4).
3. **Mixed questions (10 minutes):** today's subtopic mixed with earlier ones, options covered, answers checked immediately.
4. **Log and cards (5 minutes):** one row in the Sprint tab and your new cards, within your AnkiDroid budget.

Your daily AnkiDroid reviews and Revision-tab reviews continue as usual; they are what keep days 1 to 20 alive by day 31.

### Every week: checkpoints

On days 7, 14 and 21:

- **A 10-question mini-test** from questions that are in neither test form, under timed conditions, with confidence marks
- **Your weekly review** (LRN-M07-L03) with sprint data: Sprint tab minutes, retrieval scores, mini-test score, error types
- **One change** for next week: more time on a slipping subtopic, a different method, more mixed practice

### The mid-sprint slump

Around days 10 to 20 most people feel the sprint has lost its excitement. That is normal. Use the minimum version on hard days, keep the never-miss-twice rule, and look at your Sprint tab: the rows are progress you can see. If you miss two days, use the restart protocol (LRN-M06-L03) and carry on; extend the sprint by the days you missed so you still get 30 days.

### The last week

From day 21, stop new subtopics and run a **revision cycle**: every subtopic by recall, mixed sets that cover the whole subject, and retests of every error in your Errors tab. Days 29 and 30 are light: cards, cue questions and good sleep before the after test on day 31.

### Keep the evidence

Everything you log becomes evidence in your reflection report (LRN-M21-L03): which methods you used on which days, and which subtopics improved most. Don't skip the log, even on minimum days.
""",
    example="""
**Sreeja** started her Constitution sprint on a Monday. Week 1 went well: six full sessions and one minimum day when her son was ill. Her day-7 mini-test: 6 out of 10.

Week 2 was the slump. Two relatives' visits and a power cut gave her three minimum days in a row, and she felt the sprint slipping. Her Sprint tab still showed 14 rows, and her study group asked about it on Saturday. Her weekly review's one change: move the sprint session to her morning slot, before the household woke up. Day-14 mini-test: 7 out of 10.

In week 3 her error log showed that her remaining mistakes were mostly mix-ups between similar provisions, so she spent two sessions on contrast cards and a comparison table of Parliament and the state legislature. Day-21 mini-test: 9 out of 10. She ran the revision cycle from day 22, retested all 31 errors in her Errors tab, and slept at her usual time before day 31.
""",
    evidence=[
        ('Daily spaced retrieval and mixed practice', 'strong', 'Retrieval, spacing and interleaving are the core of the sprint.'),
        ('Weekly checkpoint tests with feedback', 'strong', 'Practice testing with feedback; it also shows whether the plan needs to change.'),
        ('Adjusting the plan with the weekly review', 'limited', 'A practical self-regulation routine; judge it by your checkpoint scores.'),
    ],
    resources=[
        ('psc-pyq', 'Choose checkpoint questions that are in neither test form', '10 minutes each week'),
        ('ls-materials', 'Keep the six-strategy bookmark beside you during sprint sessions', '2 minutes'),
    ],
    steps=[
        'Run the sprint for 30 days, with the daily session shape and a Sprint tab row every day (minimum days included).',
        'On days 7, 14 and 21, take a 10-question mini-test from questions outside both test forms, and do your weekly review with one change.',
        'From day 21, stop new subtopics and run the revision cycle, including retests of every error in your Errors tab.',
        'If you miss two days, use the restart protocol and extend the sprint so you still get 30 days.',
        'Keep days 29 and 30 light, and sleep at your usual time before the after test.',
    ],
    proof='Your Sprint tab with 30 rows, the three checkpoint scores, and the three weekly reviews with their changes.',
    extra_tasks=[
        ('day07', 'Sprint day 7: checkpoint mini-test and weekly review', SPRINT_START, '**Evidence:** the mini-test score and your weekly review with one change, saved in 21 Capstone.'),
        ('day14', 'Sprint day 14: checkpoint mini-test and weekly review', SPRINT_START + 1, '**Evidence:** the mini-test score and your weekly review with one change, saved in 21 Capstone.'),
        ('day21', 'Sprint day 21: checkpoint mini-test, weekly review and start of the revision cycle', SPRINT_START + 2, '**Evidence:** the mini-test score and your revision-cycle plan, saved in 21 Capstone.'),
        ('day28', 'Sprint day 28: revision cycle done and error-log retests cleared', SPRINT_START + 3, '**Evidence:** your Errors tab with retest results, saved in 21 Capstone.'),
    ],
    templates=[
        ('daily sprint session (45 minutes)', """
SPRINT DAY ___   Date: ______   Subtopic: ______________
[ ] Warm-up recall of yesterday (5 min): ___ points, fixed ___
[ ] Learn or practise (25 min). Method: six-strategy / loop / Feynman / palace / image occlusion
[ ] Mixed questions (10 min): ___/___ right; recognised only (R) ___
[ ] Log in the Sprint tab + cards made: ___ (within budget)
Minimum day? [ ] (15 min: recall + cards)
""", ''),
        ('checkpoint sheet', """
CHECKPOINT DAY ___   Date: ______
Mini-test (10 new questions, timed, S/U/G marked): ___/10
Confident errors: ____________________________________________
Sprint tab this week: minutes ___  sessions ___  minimum days ___
Subtopic slipping: ______________   Subtopic improving: ______________
Most common error type this week: ___
One change for next week: ____________________________________
""", ''),
    ],
    mistakes=[
        ('Skipping the log on minimum days.', 'Log every day; the rows are your evidence and your motivation.'),
        ('Only reading during sessions.', 'Every session includes recall and mixed questions.'),
        ('Changing the subject halfway.', 'Finish the 30 days; start a new sprint afterwards.'),
        ('Giving up after missing a day.', 'Never miss twice; if you do, restart and extend.'),
        ('Using test-form questions for checkpoints.', 'Keep both forms untouched; use other questions.'),
    ],
    quiz=[
        {'q': 'What are the four parts of a daily sprint session?', 'o': ['Warm-up recall, learn or practise, mixed questions, log and cards', 'Reading, highlighting, rereading, sleep', 'Video, notes, video, notes', 'Mock, mock, mock, rest'], 'a': 'A', 'why': 'The same shape every day removes decisions and keeps retrieval central.'},
        {'q': 'Which questions should you use for checkpoint mini-tests?', 'o': ['Questions that are in neither test form', 'Questions from form 2', 'Questions from form 1 only', 'No questions; just reread'], 'a': 'A', 'why': 'The forms must stay unseen to keep the after test fair.'},
        {'q': 'You miss two days in week 2. What do you do?', 'o': ['Use the restart protocol and extend the sprint so you still get 30 days', 'Start the whole sprint again from day 1', 'Stop the sprint', 'Do six hours the next day'], 'a': 'A', 'why': 'Restart quickly and keep the 30 days.'},
        {'q': 'What happens from day 21?', 'o': ['No new subtopics; a revision cycle and error retests', 'Twice as many new subtopics', 'Rest until day 31', 'The after test'], 'a': 'A', 'why': 'Consolidation before the after test.'},
    ],
    study='Your sprint plan, the six-strategy bookmark and the checkpoint routine',
    action='Run the 30-day sprint with a daily log and three checkpoints',
)

L3 = lesson(
    M, 3,
    outcome='Take the after test, compare it honestly with the before test, write your reflection report, and write the one-page learning system you will keep using after the course.',
    split='45 minutes for the after test, 45 minutes for the report, 30 minutes for the system document',
    core=f"""
### The after test

On day 31, open the sealed **form 2** and take it under exactly the same conditions as form 1: same time limit, same place if possible, confidence marks, no help. Score it. Then repeat the blank-page recalls of five subtopics you did at the start, if you did them.

### Reading your result honestly

Compare the two scores, but read them fairly:

- **Some gain comes from practice and familiarity** with the question style, not only from learning.
- **The two forms are matched, not identical;** one may be slightly easier.
- **One sprint is not a scientific study,** but it is real evidence about you, collected carefully.

What makes the result convincing is the pattern: before and after scores, the three checkpoint scores rising, fewer confident errors, and subtopics that moved from red to green in your traffic-light check.

### The reflection report

Write one or two pages. Use your Sprint tab, checkpoints and Errors tab as evidence:

1. **Goal and result:** what you aimed for, and the before and after scores.
2. **What you did:** total minutes, sessions, minimum days, methods used.
3. **What worked best,** with evidence from your data (for example, "the subtopics where I used contrast cards had the fewest errors").
4. **What didn't work,** and why you think so.
5. **Surprises:** what you learned about yourself as a learner.
6. **How your ranking compares with the research:** did the methods with the strongest evidence also work best for you? Where not, why might that be?
7. **What you will keep,** and what your next sprint will be.

### Your learning system for life

The course ends; your system shouldn't. Write it on one page, so you can follow it without this app:

- **Daily:** AnkiDroid first; one retrieval session; phone out of the room in study blocks; sleep rules.
- **Weekly:** the seven-part review; next week's planner with if-then plans.
- **Monthly:** current-affairs review; knowledge base check and backup; four-week look-back.
- **Every 12 weeks:** a new 12-week plan or a sprint; a mock or a test; one baseline test repeated.
- **For anything new:** the learning project canvas, a baseline, a practice loop, and the methods with the strongest evidence.
- **Your rules:** AI, phone, sleep, and checking sources.

Put the next review dates in your calendar before you close this page.

### And then

On the **Final retests** page you repeat the four baseline tests with fresh versions. With your sprint report, they show how much you have changed, as a learner and in your PSC subject.
""",
    example="""
**Sreeja** opened form 2 on day 31 at 10 a.m., at the same dining table, with the same 40-minute limit. Her score: 31 out of 40, against 17 on form 1, with 2 confident errors instead of 9. Her checkpoints had been 6, 7 and 9 out of 10.

Her reflection report was two pages. She wrote that some of the gain was probably familiarity with the question style, but the checkpoint pattern and the fall in confident errors convinced her the learning was real. Her best methods, from her data: contrast cards for look-alike provisions, the memory palace for the Fundamental Rights, and the daily warm-up recall. Her worst: reading the guide's long chapter summaries, which she dropped in week 2. Her ranking matched the research closely, except that Feynman explanations helped her more than she had expected.

Her one-page learning system went on the inside cover of her notebook and into her knowledge base. Her next sprint: arithmetic, starting the following Monday.
""",
    evidence=[
        ('Comparing matched before and after tests', 'limited', 'A fair personal measure, but not a controlled study: practice effects and form differences remain.'),
        ('Reflecting on which methods worked, with your own data', 'limited', 'A practical self-regulation step; it makes your system better each cycle.'),
        ('Continuing the high-utility methods after the course', 'strong', 'Retrieval and spacing keep working for whatever you learn next.'),
    ],
    resources=[
        ('dunlosky-aps', 'Compare your own ranking of methods with the research ratings', '10 minutes'),
        ('retrievalpractice', 'Keep this free site for ideas after the course', '5 minutes'),
        ('ls-materials', 'Keep the six-strategy posters as reminders for future learning', '5 minutes'),
    ],
    steps=[
        'On day 31, take form 2 under the same conditions as form 1, with confidence marks. Score it and count confident errors.',
        'Fill in the results table in the reflection report outline: before, checkpoints, after, and confident errors.',
        'Write your reflection report (one or two pages) using your Sprint tab, checkpoints and Errors tab as evidence.',
        'Write your one-page learning system for life with the template below, and put the next review dates in your calendar.',
        'Share the report and your system page with your study partner or group, and ask one question: "What would you add?"',
    ],
    proof='Your form 2 score next to form 1, your reflection report, your one-page learning system and the review dates in your calendar.',
    templates=[
        ('reflection report outline', """
SPRINT REFLECTION REPORT      Subject: ______________   Dates: ______ to ______
1. Goal: ________________   Before (form 1) ___/___   After (form 2) ___/___
   Checkpoints: day 7 ___/10  day 14 ___/10  day 21 ___/10
   Confident errors: before ___  after ___
2. What I did: ___ minutes, ___ sessions, ___ minimum days. Methods: _______________
3. What worked best (with evidence from my data): _________________________________
4. What didn't work, and why I think so: _________________________________________
5. Surprises about myself as a learner: __________________________________________
6. My ranking compared with the research: ________________________________________
7. What I will keep: ___________________   My next sprint: _______________________
Honest limits: some gain is from practice and familiarity; the forms are matched, not identical.
""", ''),
        ('my learning system for life (one page)', """
MY LEARNING SYSTEM                         Written: ______   Review: ______
DAILY     AnkiDroid first (___ min) | one retrieval session | phone out of the room | sleep by ____
WEEKLY    seven-part review on ______ | planner with if-then plans | one change
MONTHLY   current-affairs review | knowledge base check + backup | four-week look-back
12-WEEKLY new 12-week plan or sprint | a mock or test | repeat one baseline test
NEW SKILL learning project canvas -> baseline -> practice loop -> retrieval + spacing
MY RULES  AI: ______________ | phone: ______________ | sleep: ______________ | sources: check first
Next dates in my calendar: weekly review ______  12-week review ______  baseline retest ______
""", ''),
    ],
    mistakes=[
        ('Skipping the reflection because the score was good (or bad).', 'The report is what makes your next cycle better.'),
        ('Claiming too much from one sprint.', 'Note the honest limits; trust the pattern of results.'),
        ('A learning system too complicated to follow.', 'One page, with a few daily and weekly habits.'),
        ('No next review date.', 'Put the dates in your calendar before you finish.'),
    ],
    quiz=[
        {'q': 'Why can\'t a before-and-after comparison prove that a method caused your improvement?', 'o': ['Practice and familiarity also raise scores, and the forms may differ slightly', 'Because tests are never accurate', 'Because PSC changes every year', 'It can prove it completely'], 'a': 'A', 'why': 'It is strong personal evidence, not a controlled study.'},
        {'q': 'What makes your sprint result more convincing?', 'o': ['A consistent pattern: rising checkpoints, fewer confident errors and a higher after score', 'One lucky question', 'How tired you felt', 'The number of hours alone'], 'a': 'A', 'why': 'Several measures pointing the same way are stronger than one.'},
        {'q': 'What belongs in your one-page learning system?', 'o': ['Daily, weekly, monthly and 12-weekly routines, a plan for new skills, and your rules', 'Every note from the course', 'Only your exam date', 'A list of apps to buy'], 'a': 'A', 'why': 'It is the system you will follow without this app.'},
        {'q': 'What should you do before closing the capstone?', 'o': ['Put the next review dates in your calendar', 'Delete your AnkiDroid decks', 'Stop all reviews', 'Start three sprints at once'], 'a': 'A', 'why': 'Dates in the calendar keep the system running.'},
    ],
    study='The technique ratings, compared with your own sprint data',
    action='Take the after test, write your reflection report and write your one-page learning system for life',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    M,
    overview="""
Prove your learning system on a real subject: a 30-day learning sprint on a PSC subject (or a new skill), with a before test, daily logging, weekly checkpoints, an after test, a reflection report and a one-page learning system for life.

The capstone brings every module together. You choose the subject from your own data, design matched tests, use the methods that suit each subtopic, adjust from weekly checkpoints, and finish with honest evidence of what changed and why.

The capstone ends in the same week as the final retests of your four baseline tests, so you finish the course with two kinds of measured improvement: in your PSC subject, and in your learning abilities.
""",
    outcomes=[
        'Choose a sprint subject from your own data and set a measurable goal',
        'Build matched before and after tests from previous-year questions',
        'Run 30 days of daily sessions with a log, checkpoints and adjustments',
        'Interpret before-and-after results honestly',
        'Write a reflection report and a one-page learning system for life',
    ],
    lessons=LESSONS,
    tools=[
        'The **30-day sprint plan**, **matched test builder** and **Sprint** tab',
        'The **daily sprint session** and **checkpoint sheet**',
        'The **reflection report outline** and **my learning system for life**',
    ],
    project='My complete learning system',
    project_steps=[
        'Put your reflection report and your one-page learning system in your Learning Folder (21 Capstone) and your knowledge base.',
        'Complete the Final retests page: the four baseline tests with fresh versions, and the learning system checklist.',
        'Write five lines comparing your week 0 baseline with your final results and your sprint result.',
        'Choose your next 12-week plan or sprint, with a start date in your calendar.',
    ],
    project_proof='Your reflection report, your learning system page, your final retest results with the five-line comparison, and the start date of your next plan or sprint.',
    rubric=[
        ('Design', 'Vague goal, one test', 'Goal with a number, same test twice', 'Measurable goal with matched forms and a day-by-day plan'),
        ('Running', 'Fewer than 20 days', '20 to 29 days or few logs', '30 days logged, three checkpoints with changes'),
        ('Evidence', 'Score only', 'Scores with a short comment', 'Scores, checkpoints and errors interpreted honestly'),
        ('Reflection', 'None', 'A list of feelings', 'A report using data, compared with the research'),
        ('System for life', 'None', 'Ideas in my head', 'One-page system with review dates in the calendar'),
    ],
    short=[
        'Run a 14-day sprint instead of 30, with forms of 20 questions and one checkpoint on day 7.',
        'Write the one-page learning system even if the sprint is short.',
    ],
    flashcards=[
        ('The capstone sprint', '30 consecutive days, at least 45 minutes a day, one subject, before and after tests.'),
        ('Why two matched test forms', 'So the after test measures the subject, not memory of the questions.'),
        ('Daily sprint session', 'Warm-up recall 5, learn or practise 25, mixed questions 10, log and cards 5.'),
        ('Checkpoint days', 'Days 7, 14 and 21: a 10-question mini-test and the weekly review.'),
        ('Days 21 to 28', 'Revision cycle: every subtopic by recall, mixed sets, error retests.'),
        ('Honest limits of a before-and-after comparison', 'Practice effects and form differences; trust the pattern of results.'),
        ('Your learning system for life', 'Daily, weekly, monthly and 12-weekly routines, a new-skill plan and your rules, on one page.'),
    ],
    mistakes=[
        ('Treating the sprint as the end.', 'It is the first cycle of a system you keep running.'),
        ('Skipping the honest interpretation.', 'Knowing what your evidence shows, and what it doesn\'t, is part of learning how to learn.'),
    ],
)
