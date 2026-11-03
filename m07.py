"""Module 7: Metacognition: knowing what you really know."""
from common import lesson, module, link, fence, table
import tools

M = 7

L1 = lesson(
    M, 1,
    outcome='Recognise the main illusions of knowing, and judge what you really know with a delayed recall test and a traffic-light topic check.',
    split='20 minutes reading, 25 minutes resources, 45 minutes action',
    core=f"""
**Metacognition** means thinking about your own thinking: planning how to learn, checking how well it is going, and adjusting. Its most important part for an exam is simple to say and hard to do: **knowing what you really know**.

### Five illusions of knowing

1. **The fluency illusion.** A page you have read twice reads smoothly, so it feels learned. In Roediger and Karpicke's study, students who reread were more confident than those who tested themselves, yet remembered less a week later ({link('roediger', 'Roediger and Karpicke, 2006')}).
2. **Recognition passing for recall.** You see the four options, one looks familiar, and you feel you knew it. In the exam, with different options and no time, you don't.
3. **Hindsight from the answer key.** You check an answer and think "of course, I knew that". Knowing it after seeing it is not knowing it.
4. **The effort illusion.** Methods that feel hard (recall, mixed practice) feel less effective than easy ones. When Karpicke and Blunt compared retrieval practice with concept mapping, students predicted that concept mapping would work best; retrieval practice produced much better long-term retention ({link('karpicke-blunt', 'Purdue University, 2011')}).
5. **The understanding illusion.** Following an explanation in a class or video is not the same as being able to recall it or use it on a new question.

There is also the **hours illusion**: time spent studying feels like progress, whatever happened in that time (Module 2).

### How to judge what you know

All five illusions have the same cure: **test yourself after a delay, without help**, and judge by the result, not the feeling.

- **Cover and recall:** close the book and write or say what you know about the topic. Two minutes is enough.
- **Apply it to a new question:** a PYQ or a question you haven't seen, with the options covered.
- **Wait first:** judge a topic a day or more after studying it, not right after. Right after reading, everything feels known.
- **Explain it** to someone, or aloud to yourself, without notes (Module 8).

### The traffic-light check

Use three colours for every topic you think you have "done":

- **Green:** after a gap, you can recall the main points and answer a new question.
- **Amber:** you recall part of it, or you only recognise answers when you see options.
- **Red:** you can't recall it or answer questions on it.

Most students find their list has far fewer greens than they expected. That isn't bad news; it is the most useful news you can get, because it tells you exactly where to spend your next hours.
""",
    example="""
**Anu** had a list of 30 GK topics she had "finished": she had read each at least twice, and most were highlighted. Before the check, she rated her confidence for each from 1 to 5; she gave 22 topics a 4 or 5.

She did the traffic-light check over two evenings: for each topic, a two-minute recall on a blank page and one previous-year question with the options covered. The result: 12 green, 10 amber, 8 red. Six of the topics she had rated 5 came out amber or red; four were in the Kerala renaissance, where she knew the names but kept mixing up who did what.

She moved the 8 reds to the top of her Revision tab as "relearn", brought the ambers' next reviews forward to the next two days, and turned the renaissance mix-ups into contrast cards in AnkiDroid. "I had been revising the greens," she said, "because they felt good."
""",
    evidence=[
        ('Rereading creates false confidence (the fluency illusion)', 'strong', 'Roediger and Karpicke (2006): rereaders were more confident and remembered less after a week.'),
        ('Students misjudge which study methods work', 'moderate', 'Students predicted concept mapping would beat retrieval practice; it didn\'t (Karpicke and Blunt, 2011).'),
        ('Judging by delayed recall instead of feeling', 'moderate', 'Follows from the findings above: judgements based on an actual recall attempt, after a gap, reflect real memory.'),
    ],
    resources=[
        ('karpicke-blunt', 'Read the press release, including what students predicted', '10 minutes'),
        ('roediger', 'Reread the part of the results on students\' confidence', '10 minutes'),
        ('lhtl', 'Optional: the videos on illusions of competence in Module 2 of Learning How to Learn', 'About 30 minutes'),
    ],
    steps=[
        'List 20 PSC topics you consider "done". Next to each, rate your confidence from 1 to 5 before testing anything.',
        'At least a day after you last studied them, test each topic: a two-minute blank-page recall, then one previous-year or new question with the options covered.',
        'Mark each topic green, amber or red using the rules in this lesson.',
        'Compare the colours with your confidence ratings. Count the topics you rated 4 or 5 that came out amber or red.',
        'Update your Revision tab: reds become "relearn" at the top; ambers get their next review within two days. Turn any mix-ups into contrast cards.',
    ],
    proof='Your 20-topic traffic-light sheet with confidence ratings and results, and a screenshot of the updated Revision tab.',
    templates=[
        ('traffic-light topic check', """
TRAFFIC-LIGHT CHECK      Date: ______   (test at least a day after studying)
Topic                 Confidence (1-5)  2-min recall (points)  New question right?  Colour
1. _________________  ___               ___                    Y / N                G / A / R
2. _________________  ___               ___                    Y / N                G / A / R
...
20. ________________  ___               ___                    Y / N                G / A / R
Greens ___  Ambers ___  Reds ___
Rated 4-5 but amber or red: ___ topics: ______________________________________
Green: recall the main points AND answer a new question.
Amber: partial recall, or recognition only.  Red: can't recall or answer.
""", ''),
        ('five illusions checklist', """
Before I tick a topic as "done", I check:
[ ] Fluency: did I test myself, or did it just read smoothly?
[ ] Recognition: could I answer with the options covered?
[ ] Hindsight: did I know it before I saw the answer key?
[ ] Effort: am I choosing an easy method because it feels better?
[ ] Understanding: can I recall and use it, not just follow it?
""", ''),
    ],
    mistakes=[
        ('Judging a topic right after reading it.', 'Everything feels known then. Test at least a day later.'),
        ('Using the answer key to "confirm" you knew it.', 'Answer first, with the options covered, then check.'),
        ('Revising the topics that feel good.', 'Spend your time on ambers and reds; greens need only short reviews.'),
        ('Taking a red as a sign you\'re bad at the subject.', 'A red is a map, not a verdict. It shows where the next hour goes.'),
    ],
    quiz=[
        {'q': 'Which is an example of the fluency illusion?', 'o': ['A chapter feels learned because it reads smoothly the second time', 'You fail a recall test and feel worried', 'You draw a map from memory', 'You answer a PYQ with the options covered'], 'a': 'A', 'why': 'Smooth reading feels like knowing, but memory is tested by recall.'},
        {'q': 'What did students predict in Karpicke and Blunt\'s study?', 'o': ['That concept mapping would work best, although retrieval practice did better', 'That retrieval practice would work best, and it did', 'That rereading would beat everything', 'That nothing would work'], 'a': 'A', 'why': 'Students misjudged which method would help them remember.'},
        {'q': 'When is the best time to judge whether you know a topic?', 'o': ['At least a day after studying, by trying to recall it', 'Immediately after reading it', 'While the book is open', 'Never; trust your feeling'], 'a': 'A', 'why': 'A delayed recall attempt shows what has really stayed.'},
        {'q': 'A topic is "amber" when...', 'o': ['you recall part of it, or only recognise answers when you see options', 'you can recall it and answer new questions', 'you have never studied it', 'you have highlighted it'], 'a': 'A', 'why': 'Green needs recall plus answering a new question; red means neither.'},
    ],
    study='The Karpicke and Blunt press release and the confidence results of Roediger and Karpicke',
    action='Run a traffic-light check on 20 "done" topics and update your Revision tab',
)

L2 = lesson(
    M, 2,
    outcome='Rate your confidence before checking each answer, work out your calibration, and fix your confident errors first.',
    split='15 minutes reading, 20 minutes resources, 55 minutes action',
    core=f"""
### Calibration

**Calibration** is how well your confidence matches your accuracy. A well-calibrated student who feels "sure" is right almost every time, and one who feels "unsure" is right about half the time. Most of us are not well calibrated, and in an exam with negative marking, that costs marks in two ways:

- **Overconfidence:** you mark answers you are "sure" of, and some are wrong. Each wrong answer loses marks.
- **Underconfidence:** you skip questions you could have answered, because you feel unsure.

You can't fix what you don't measure. Confidence ratings measure it.

### How to rate confidence

While answering practice questions, write one letter beside each answer **before** you check it:

- **S (sure):** I would bet on this.
- **U (unsure):** I think so, but I could be wrong.
- **G (guess):** I am choosing between options without real knowledge.

After checking, count how many were right in each group:

{table(['Group', 'What good calibration looks like', 'What it means if it is not'], [
    ('Sure', 'Nearly all right (about 9 out of 10 or better)', 'Sure but wrong = confident errors: your most dangerous mistakes'),
    ('Unsure', 'Roughly half right, or a bit more', 'If most are right, you know more than you think'),
    ('Guess', 'Near chance (1 in 4 with four options) or a bit above', 'If well above chance, your partial knowledge is useful'),
])}

### What to do with the results

1. **Fix confident errors first.** A "sure" answer that was wrong is usually a mix-up of two similar facts, or a fact learned wrongly. Make a contrast card or correct the note at its source (Module 4). These are worth more than any new topic.
2. **Turn unsure-right into sure-right** with a few spaced reviews.
3. **Use your guess data for exam strategy.** If your guesses after ruling out one or two options are right well above chance, careful guessing can pay even with negative marking. Module 12 does the arithmetic for Kerala PSC's marking scheme.

### Self-testing at three time scales

- **Daily:** AnkiDroid reviews and the retrieval sandwich (Modules 3 and 4)
- **Weekly:** five cold questions in your weekly review (LRN-M07-L03)
- **Monthly:** a mock test with confidence marks (Module 12)

Each one is retrieval practice and a measurement at the same time.
""",
    example="""
**Ashiq** took 50 questions from two previous papers and marked each S, U or G before checking. His calibration table: 30 sure, of which 24 right (80%); 12 unsure, of which 6 right (50%); 8 guesses, of which 3 right (38%).

His six confident errors told a clear story: four were mix-ups between similar facts (two Constitutional amendments, and two national parks), one was a fact he had learned from a wrong WhatsApp forward, and one was misreading "NOT" in a question. He made four contrast cards, fixed the wrong note, and started underlining NOT, EXCEPT and FIRST in every question.

His guesses were right more often than chance (38% against 25%), mostly where he had ruled out two options first. He saved that number for Module 12, where he would work out whether such guesses pay under negative marking.
""",
    evidence=[
        ('Self-testing with practice questions', 'strong', 'Practice testing is rated high utility by Dunlosky and others (2013).'),
        ('Confidence ratings to measure calibration', 'limited', 'A simple measuring tool; no single source was checked for this course. Your own table decides what to change.'),
        ('Fixing confident errors first', 'limited', 'A practical priority rule: confident errors are both likely to repeat and costly under negative marking.'),
    ],
    resources=[
        ('dunlosky-aps', 'Skim the summary of the ten techniques and their ratings', '10 minutes'),
        ('os-cs-6-3', 'Read the part on multiple-choice questions and preparing for tests', '15 minutes'),
    ],
    steps=[
        'Take 50 previous-year questions on mixed topics from the papers you saved in week 0.',
        'Answer them with the options covered first (Module 3). Before checking each, write S, U or G beside it.',
        'Check all 50 against the answer key. Fill in the calibration table below.',
        'List every sure-but-wrong question. For each, write the cause (mix-up, wrong source, misreading, other) and the fix: a contrast card, a corrected note or a reading rule.',
        'Write two lines on what your unsure and guess rows suggest, and keep the numbers for Module 12.',
    ],
    proof='Your 50-question sheet with S, U and G marks, the completed calibration table and your list of confident errors with fixes.',
    templates=[
        ('calibration table', """
CALIBRATION TABLE      Date: ______  Source: __________________  Questions: ___
Group    Answered   Right   % right   Target
Sure     ___        ___     ___%      90% or more
Unsure   ___        ___     ___%      about 50-70%
Guess    ___        ___     ___%      about 25% (4 options)
Confident errors (sure but wrong):
Q no   Cause (mix-up / wrong source / misread / other)   Fix (contrast card / note / rule)
____   ______________________________________________   ________________________________
____   ______________________________________________   ________________________________
""", ''),
        ('confidence marks, quick key', """
Write BEFORE checking:
S = sure: I would bet on it
U = unsure: I think so
G = guess: no real knowledge, choosing between options
After checking, circle: sure-wrong (fix first), unsure-right (review more), guess-right (note how many options you ruled out)
""", ''),
    ],
    mistakes=[
        ('Marking confidence after seeing the answer.', 'It must be written before you check, or it measures nothing.'),
        ('Ignoring confident errors because the score was good.', 'Sure-wrong answers repeat in exams. Fix them first.'),
        ('Marking everything "sure" to feel better.', 'Honest marks are the point. Nobody else sees them.'),
        ('Treating calibration as a judgement of intelligence.', 'It is a skill that improves with practice and feedback.'),
    ],
    quiz=[
        {'q': 'What is calibration?', 'o': ['How well your confidence matches your actual accuracy', 'How fast you answer questions', 'How many hours you study', 'How neat your notes are'], 'a': 'A', 'why': 'Good calibration means "sure" answers are nearly always right.'},
        {'q': 'Which mistakes should you fix first?', 'o': ['Answers you were sure of that turned out wrong', 'Guesses that were wrong', 'Questions you skipped', 'Questions you got right'], 'a': 'A', 'why': 'Confident errors repeat and cost marks under negative marking.'},
        {'q': 'When must you write your S, U or G mark?', 'o': ['Before checking the answer', 'After checking the answer', 'At the end of the week', 'Only for wrong answers'], 'a': 'A', 'why': 'After seeing the answer, hindsight changes your feeling of confidence.'},
        {'q': 'Your "unsure" answers are right 80% of the time. What does that suggest?', 'o': ['You know more than you think, and may be skipping questions you could answer', 'You should stop studying', 'Your calibration is perfect', 'You should guess everything'], 'a': 'A', 'why': 'Underconfidence can cost marks; a few reviews turn unsure into sure.'},
    ],
    study='The summary of Dunlosky and others\' ratings and College Success 6.3 on test taking',
    action='Answer 50 PYQs with confidence marks, build your calibration table and fix your confident errors',
)

L3 = lesson(
    M, 3,
    outcome='Run the full weekly learning review: recall, numbers, a cold self-test, calibration, errors and next week\'s if-then plans, and record it in the Weekly tab.',
    split='15 minutes reading, 10 minutes resources, 35 minutes for your first full review',
    core=f"""
You have done the short weekly review since week 1. Now it becomes the centre of your learning system: once a week, for 20 minutes, you **plan, check and adjust**, which is metacognition in practice.

### The seven parts

1. **Recall from memory.** Before looking at anything, write the three most important things you learned this week. If you can't, that itself is information.
2. **Numbers.** Copy this week's numbers from your tools: study hours (Study Log), AnkiDroid days and percentage correct (AnkiDroid statistics), Revision-tab scores, focus blocks (Focus tab), and any test or mock score.
3. **Cold self-test.** Five questions from this week's topics, answered without notes. Make them in the moment, or keep five margin questions from the week for this.
4. **Calibration.** What did you feel sure about but get wrong this week? Those go to the top of next week.
5. **Error pattern.** What kind of mistake happened most? From Module 12 on, your Errors tab answers this in seconds.
6. **What worked, what didn't.** One line each, based on the numbers, not on mood.
7. **Next week.** Three priorities, each with a day and time (if-then plans from Module 6), and **one change** to your system.

### One change at a time

Change one thing a week: a new block time, fewer new cards, a different place to study. If you change five things together, you won't know which one helped. Keep a short "changes" list at the back of your notebook with the date, the change and what happened.

### Every fourth week: look back

Every fourth review, put the last four weeks' numbers side by side in the **Weekly** tab. Trends tell you more than single weeks: Is the AnkiDroid percentage steady? Are mock scores rising? Are focus blocks growing? Which subject keeps slipping?

### Make it a ritual

Same day, same time, same place: for example Sunday after lunch at the dining table. Anchor it to something you already do (Module 6). The review is also where you fill in next week's study planner (Module 5), so the week starts on Monday with no decisions left to make.
""",
    example="""
**Sreeja** does her review on Sunday after lunch, while the children watch a film. This week her recall came easily for the Kerala renaissance and not at all for the Lok Sabha topic she had studied on Thursday. Her numbers: 6 hours 10 minutes of study, AnkiDroid 7 out of 7 days at 88% correct, two focus blocks cut short by visitors, and 3 out of 5 on her cold test.

Calibration: she had been sure that the Rajya Sabha is dissolved like the Lok Sabha, and it is not (it is a permanent house). That became a contrast card. Her error pattern: both wrong questions in her mixed set were misreadings. What worked: morning reviews. What didn't: maths at night, when she was tired.

Her one change for next week: maths moves to the morning slot on Monday, Wednesday and Friday. She wrote three if-then plans, filled in next week's planner, and copied the numbers into the Weekly tab. It took 22 minutes.
""",
    evidence=[
        ('A weekly cold self-test', 'strong', 'It is spaced retrieval practice of the week\'s material (Dunlosky and others, 2013).'),
        ('If-then plans for the coming week', 'strong', 'Implementation intentions have a medium-to-large effect on reaching goals (Gollwitzer and Sheeran, 2006).'),
        ('A regular weekly review routine', 'limited', 'Planning, checking and adjusting is the core of self-regulated learning; this exact routine is a practical design, not a tested package.'),
    ],
    resources=[
        ('gollwitzer', 'Reread the abstract: why the "next week" part uses if-then plans', '5 minutes'),
        ('os-cs-3', 'Reread 3.7 on strategies for time and task management', '10 minutes'),
    ],
    steps=[
        'Choose your fixed review time and anchor (for example, Sunday after lunch at the dining table) and add it to Loop as a weekly habit if it isn\'t there yet.',
        'This Sunday, do the full seven-part review using the template below.',
        'Copy the numbers into a new row of the Weekly tab.',
        'Fill in next week\'s study planner, with your three priorities as if-then plans.',
        'Start a "changes" list at the back of your notebook with this week\'s one change.',
    ],
    proof='Your completed seven-part review, the new Weekly tab row, next week\'s planner and the first line of your changes list.',
    templates=[
        ('weekly learning review (core tool)', tools.WEEKLY_REVIEW, ''),
        ('Weekly tab headings', tools.WEEKLY, 'csv'),
        ('every fourth week: look back', """
FOUR-WEEK LOOK-BACK      Weeks ___ to ___
                     Wk __   Wk __   Wk __   Wk __   Trend
Study hours          ____    ____    ____    ____    up / flat / down
AnkiDroid % correct  ____    ____    ____    ____    ______
Self-test %          ____    ____    ____    ____    ______
Mock / PYQ score     ____    ____    ____    ____    ______
Focus blocks         ____    ____    ____    ____    ______
Subject that keeps slipping: ______________  Plan for it: ______________________
Changes that worked (from my changes list): ___________________________________
""", ''),
    ],
    mistakes=[
        ('Listing hours and skipping the recall and self-test.', 'Hours measure effort, not learning. Recall and test first.'),
        ('Changing five things at once.', 'One change a week, written down, so you can see what helped.'),
        ('Ending the review without next week\'s plan.', 'The review finishes when the planner is filled in.'),
        ('Reviewing only the good news.', 'The confident errors and slipping subjects are the reason to review.'),
    ],
    quiz=[
        {'q': 'What is the first part of the weekly review?', 'o': ['Recalling the week\'s three most important things from memory', 'Copying hours from the Study Log', 'Planning next week', 'Reading all the week\'s notes again'], 'a': 'A', 'why': 'Recall comes first, before any notes, because it shows what really stayed.'},
        {'q': 'Why make only one change to your system each week?', 'o': ['So you can tell which change helped', 'Because more changes are not allowed', 'Because systems should never change', 'To save paper'], 'a': 'A', 'why': 'Several changes at once hide which one worked.'},
        {'q': 'What do you do every fourth weekly review?', 'o': ['Compare the last four weeks\' numbers to see trends', 'Skip the review', 'Start a new deck', 'Take a full mock test'], 'a': 'A', 'why': 'Trends over four weeks are more reliable than one week\'s numbers.'},
        {'q': 'How should next week\'s priorities be written?', 'o': ['As if-then plans with a day and time', 'As a long wish list', 'As "study more"', 'They don\'t need writing'], 'a': 'A', 'why': 'If-then plans are among the best-supported ways to follow through.'},
    ],
    study='Gollwitzer and Sheeran\'s abstract and College Success 3.7, with the seven-part review template',
    action='Do your first full seven-part weekly review and record it in the Weekly tab',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    M,
    overview="""
Learn to judge what you really know: spot the illusions of knowing, test yourself after a delay, measure your calibration with confidence ratings, and run a full weekly learning review that turns your data into decisions.

Metacognition is often called the skill behind all other learning skills. Students waste the most time not by studying too little but by studying the wrong things: the topics that feel good instead of the ones they don't know. This module gives you three simple instruments (the traffic-light check, the calibration table and the weekly review) and the habit of trusting them over your feelings.

The weekly review you build here runs every Sunday for the rest of the course and after it.
""",
    outcomes=[
        'Name five illusions of knowing and test topics after a delay',
        'Sort topics into green, amber and red and act on the result',
        'Rate confidence before checking answers and build a calibration table',
        'Fix confident errors first',
        'Run the full seven-part weekly review and track trends every four weeks',
    ],
    lessons=LESSONS,
    tools=[
        'The **weekly review** (one of the six core tools) and the **Weekly** tab',
        'The **traffic-light topic check** and **five illusions checklist**',
        'The **calibration table** with S, U and G marks',
        'The **four-week look-back** and your **changes list**',
    ],
    project='My metacognition dashboard',
    project_steps=[
        'Extend your traffic-light check to at least 30 topics from your syllabus.',
        'Keep your 50-question calibration table and your list of confident errors with fixes.',
        'Complete two full weekly reviews, each recorded in the Weekly tab.',
        'Write three decisions you made because of this data (for example: "relearn the 8 red topics before new ones", "underline NOT in every question", "maths in the morning").',
    ],
    project_proof='Your 30-topic traffic-light sheet, the calibration table, two Weekly tab rows and your three data-based decisions.',
    rubric=[
        ('Judging knowledge', 'By feeling', 'Some recall tests, done right after study', 'Delayed recall tests for 30 topics, colours assigned honestly'),
        ('Calibration', 'Not measured', 'Measured but not acted on', 'Calibration table with confident errors fixed'),
        ('Weekly review', 'Skipped', 'Short version only', 'Full seven-part review, twice, with Weekly tab rows'),
        ('Decisions', 'None', 'Vague intentions', 'Three specific decisions based on the data'),
    ],
    short=[
        'Do the traffic-light check on 10 topics.',
        'Do the full weekly review once, even if some numbers are missing.',
    ],
    flashcards=[
        ('Metacognition', 'Planning, checking and adjusting your own learning; knowing what you really know.'),
        ('The fluency illusion', 'Smooth rereading feels like knowing, but recall shows the truth.'),
        ('Best time to judge a topic', 'At least a day later, by recalling without help.'),
        ('Green, amber, red', 'Green: recall plus a new question right. Amber: partial or recognition only. Red: neither.'),
        ('Calibration', 'How well confidence matches accuracy.'),
        ('S, U and G marks', 'Sure, unsure and guess, written before checking.'),
        ('Fix first', 'Confident errors: sure but wrong.'),
        ('The seven parts of the weekly review', 'Recall, numbers, cold self-test, calibration, error pattern, what worked, next week (with one change).'),
    ],
    mistakes=[
        ('Trusting the feeling of knowing.', 'Test it. The feeling is often wrong in both directions.'),
        ('Collecting data and never acting on it.', 'Every check ends with a change to your Revision tab, cards or plan.'),
    ],
)
