"""Module 6: Motivation, procrastination and habits."""
from common import lesson, module, link, fence, table

M = 6

L1 = lesson(
    M, 1,
    outcome='Explain procrastination as short-term mood repair, find your own triggers with a procrastination log, and use the five-minute start on a task you have been avoiding.',
    split='20 minutes reading, 30 minutes resources, 30 minutes action plus a 5-day log',
    core=f"""
### Procrastination is not laziness

**Procrastination** means delaying something you intended to do, even though you expect the delay to cost you. Almost everyone does it, and PSC preparation, with its long syllabus and distant exam dates, invites it.

Researchers Fuschia Sirois and Timothy Pychyl describe procrastination as a problem of **short-term mood repair**. When a task feels unpleasant (boring, confusing, frightening), avoiding it makes you feel better right now. The bill goes to your **future self**, who has less time and more stress ({link('sirois', 'Sirois and Pychyl, 2013')}). That is why "just be disciplined" rarely works: the problem is a feeling, so the fix has to deal with the feeling.

### What makes a PSC task feel bad

Notice which of these describe the tasks you put off:

- **Boring:** long lists of static GK facts
- **Hard or unclear:** a maths topic where you don't know the method
- **Big or vague:** "finish the Constitution", "start current affairs"
- **Frightening:** a full mock test that might show a low score
- **No reward now:** the exam is months away; Reels are right here
- **Unsure where to start:** a new subject with no plan

### Five ways to make starting easier

1. **Shrink the task.** Not "do maths" but "open the guide at page 34 and do five percentage questions". A small, specific task feels less threatening.
2. **The five-minute start.** Promise yourself only five minutes. Once started, most people continue; if you don't, you still did five minutes.
3. **Remove friction the night before.** Book open at the right page, phone charging in another room, pen on the table.
4. **Name the feeling.** "I feel bored" or "I'm afraid of this mock". Naming it makes it smaller, and you can start anyway.
5. **Talk to your future self.** Write one line from "exam-day me" to "today me": what you will be glad you did.

### Forgive yourself

One study followed 134 first-year university students through two sets of exams. Students who forgave themselves for procrastinating before the first exams felt less negative afterwards and procrastinated less before the second exams ({link('wohl', 'BPS Research Digest on Wohl, Pychyl and Bennett, 2010')}). Harsh self-criticism makes the next task feel even worse, which feeds the cycle. Forgiving yourself is not excusing the delay; it is clearing the way to start again.
""",
    example="""
**Anu** kept postponing the mental ability section of her syllabus. Every evening she planned to start "time and work" and every evening she reorganised her notes, tidied her desk, or did another round of GK instead.

Her five-day procrastination log made the pattern clear. Every delay was on maths, the feeling was always the same ("I'll get them wrong and feel stupid"), and her escape was always a task that felt productive. The trigger was fear, not laziness.

She shrank the task to "two worked examples of time and work from the guide, then one problem of my own", and used the five-minute start. On the first evening she stopped after the five minutes. On the second she did 20 minutes. By the fourth she finished the chapter's first exercise. She also wrote a short note forgiving herself for the three weeks of delay, and kept it in the back of her maths notebook. "It was the feeling of failing I was avoiding," she wrote, "not the maths."
""",
    evidence=[
        ('Procrastination as short-term mood repair', 'moderate', 'A well-supported view in procrastination research, set out by Sirois and Pychyl (2013).'),
        ('Self-forgiveness reduces later procrastination', 'limited', 'One study of 134 students (Wohl, Pychyl and Bennett, 2010); encouraging but not yet strong.'),
        ('Shrinking tasks and the five-minute start', 'limited', 'Practical methods consistent with research on task aversion and if-then plans (LRN-M06-L02).'),
    ],
    resources=[
        ('sirois', 'Read the abstract and introduction: why procrastination is about mood', '20 minutes'),
        ('wohl', 'Read the summary of the self-forgiveness study', '5 minutes'),
        ('os-cs-3', 'Read 3.3 Procrastination: The Enemy Within', '20 minutes'),
        ('lhtl', 'Optional, later: Module 3 (Procrastination and Memory) of Learning How to Learn', 'About 3 hours'),
    ],
    steps=[
        'For five days, keep a procrastination log: each time you delay a planned study block, note the task, the feeling, the trigger type, what you did instead, and for how long.',
        'Pick the study task you avoided most. Shrink it to a first step of five minutes or less, written down exactly (book, page, number of questions).',
        'Do the five-minute start three times on that task. After each, note whether you stopped at five minutes or kept going, and for how long.',
        'The night before each start, remove friction: book open, pen out, phone charging in another room.',
        'Write a short self-forgiveness note for one past delay, ending with what you will do next time.',
    ],
    proof='Your 5-day procrastination log, notes from your three five-minute starts, and your self-forgiveness note.',
    templates=[
        ('procrastination log', """
PROCRASTINATION LOG
Day | Task I delayed        | Feeling (bored / confused / afraid / tired / other) | Trigger type | What I did instead | How long
1   | ____________________ | ____________________ | ____________ | __________________ | ____
2   | ____________________ | ____________________ | ____________ | __________________ | ____
3   | ____________________ | ____________________ | ____________ | __________________ | ____
4   | ____________________ | ____________________ | ____________ | __________________ | ____
5   | ____________________ | ____________________ | ____________ | __________________ | ____
Trigger types: boring, hard or unclear, big or vague, frightening, no reward now, unsure where to start
Pattern I see: ____________________________________________________________
""", ''),
        ('task shrinker', """
BIG TASK: ______________________________________ (e.g. "start time and work")
First step of 5 minutes or less (book, page, exact action):
______________________________________________________________________
Friction removed the night before: [ ] book open  [ ] pen out  [ ] phone away
Five-minute starts:  1. date ___ kept going for ___ min
                     2. date ___ kept going for ___ min
                     3. date ___ kept going for ___ min
""", ''),
    ],
    mistakes=[
        ('Calling yourself lazy.', 'Procrastination is usually avoiding a feeling. Find the feeling and shrink the task.'),
        ('Waiting until you feel motivated.', 'Motivation often comes after starting. Start for five minutes.'),
        ('Planning giant, vague tasks.', 'Write the first step so exactly that you could start without thinking.'),
        ('Punishing yourself after a delay.', 'Forgive yourself and restart; harshness makes the next start harder.'),
    ],
    quiz=[
        {'q': 'According to Sirois and Pychyl, what drives much procrastination?', 'o': ['Short-term mood repair: avoiding a task to feel better now', 'A lack of intelligence', 'Too much sleep', 'Knowing the subject too well'], 'a': 'A', 'why': 'Avoiding an unpleasant task improves mood now, while the cost falls on the future self.'},
        {'q': 'Which first step is best for a task you keep avoiding?', 'o': ['"Open the guide at page 34 and do five percentage questions"', '"Master mental ability"', '"Study maths properly this week"', '"Be more disciplined"'], 'a': 'A', 'why': 'A small, specific step makes the task less threatening and easier to start.'},
        {'q': 'What did the self-forgiveness study find?', 'o': ['Students who forgave themselves for procrastinating procrastinated less before their next exams', 'Self-forgiveness made students lazier', 'It had no effect on mood', 'Only harsh self-criticism helped'], 'a': 'A', 'why': 'Wohl, Pychyl and Bennett (2010) followed 134 students through two sets of exams.'},
        {'q': 'What is the five-minute start?', 'o': ['Promising yourself only five minutes on the task, then deciding whether to continue', 'Studying for exactly five minutes a day', 'Taking a five-minute break before every task', 'Reading for five hours'], 'a': 'A', 'why': 'Starting is the hardest part; most people continue once they begin.'},
    ],
    study='Sirois and Pychyl\'s paper (abstract and introduction) and College Success 3.3 on procrastination',
    action='Keep a 5-day procrastination log and use the five-minute start on your most avoided task',
)

L2 = lesson(
    M, 2,
    outcome='Write if-then plans for your key study habits and obstacles, shrink each habit to a tiny starter anchored to an existing routine, and track them in Loop Habit Tracker.',
    split='20 minutes reading, 30 minutes resources, 25 minutes action plus 14 days of tracking',
    core=f"""
### Goals are not enough

"I will study more this month" is a **goal intention**. It names what you want, but not when, where or how. Most such goals fade within days.

An **implementation intention** is an if-then plan: **"If [situation], then I will [action]."** For example:

- "If it is 6 a.m. and I have poured my tea, then I will open AnkiDroid at the kitchen table."
- "If I sit down at the library after lunch, then I will start with a mixed set of 12 maths questions."

A meta-analysis of 94 independent tests found that forming implementation intentions had a medium-to-large effect on reaching goals ({link('gollwitzer', 'Gollwitzer and Sheeran, 2006')}). That is one of the strongest findings in habit and motivation research, and it costs one sentence.

### If-then plans for obstacles

The same trick handles what usually derails you:

- "If a WhatsApp message arrives during a study block, then I will leave it until the break."
- "If there is a power cut at night, then I will switch to AnkiDroid and a paper recall of today's topic."
- "If I wake up late, then I will still do the 15-minute AnkiDroid review before anything else."

### Habits take time

A **habit** is an action that happens almost automatically in a familiar situation. Habits form by repeating the same action in the same context. Popular claims say a habit takes 21 days. In Dr Pippa Lally's research, forming a daily habit took **66 days on average**, with a very wide range, from 18 to 254 days ({link('lally', 'University of Surrey, 2026')}). Expect weeks to months, and don't judge yourself at day 10.

### Tiny habits and anchors

Two ideas make new habits easier:

- **Make it tiny.** Start with a version so small it is hard to refuse: "open AnkiDroid and do 10 cards", "write three lines of recall", "solve one maths question". The tiny version builds the routine; on most days you will do more. This idea is popularised by B. J. Fogg's "Tiny Habits" method.
- **Anchor it to something you already do every day.** "After I pour my morning tea, I will open AnkiDroid." "After I return from the bus stop, I will do a five-minute recall." The existing routine becomes the "if".

### Track it with Loop

**Loop Habit Tracker** is a free, open-source Android app with reminders, charts and statistics ({link('loop', 'Loop Habit Tracker')}). Add only two or three habits at first: for example daily AnkiDroid, the morning study block, and the Sunday weekly review. Tick each day you do them. The chart makes progress visible and shows which days of the week are weak.
""",
    example="""
**Sreeja** had tried to "study every day" many times. This time she wrote five if-then plans:

- If the children's school bus leaves, then I will sit at the dining table and open my Revision tab.
- If I have poured my evening tea, then I will do my AnkiDroid reviews before switching on the TV.
- If it is Sunday after lunch, then I will do my weekly review.
- If relatives visit during my morning slot, then I will do my reviews after they leave, before cooking.
- If I feel too tired at night, then I will do just 10 cards and sleep.

She installed Loop and added three habits with reminders. Her tiny versions were 10 cards, one Revision-tab review and three lines of weekly review. After 14 days Loop showed 13 out of 14 ticks for AnkiDroid, 11 for the morning slot and both Sunday reviews. The chart showed one weak day, Saturday, when her husband's family visits. She added an if-then plan for Saturdays.
""",
    evidence=[
        ('If-then plans (implementation intentions)', 'strong', 'Gollwitzer and Sheeran (2006): a medium-to-large effect on goal attainment across 94 independent tests.'),
        ('Habits take weeks to months to form', 'moderate', 'Lally\'s research: an average of 66 days for a daily habit, ranging from 18 to 254. Based mainly on one well-known study.'),
        ('Tiny habits anchored to existing routines', 'limited', 'A popular method consistent with research on context cues and if-then plans; little direct testing.'),
    ],
    resources=[
        ('gollwitzer', 'Read the abstract and the summary of results', '15 minutes'),
        ('lally', 'Read the whole article on how long habits take', '10 minutes'),
        ('loop', 'Install Loop Habit Tracker and add your first habit', '10 minutes'),
        ('os-cs-3', 'Read 3.6 Goal Setting and Motivation', '15 minutes'),
    ],
    steps=[
        'Write three if-then plans for study habits, each with a time or cue, a place and an action.',
        'Write two if-then plans for the obstacles that most often derail you (use your procrastination log).',
        'For each of the three habits, write its tiny version (two minutes or less) and the existing routine it follows.',
        'Install Loop Habit Tracker, add the three habits with reminders at the right times, and tick them each day.',
        'Track for 14 days (and keep going). On day 14, look at the chart, find your weakest day, and add an if-then plan for it.',
    ],
    proof='Your five if-then plans with tiny versions and anchors, and a Loop screenshot after 14 days.',
    templates=[
        ('if-then planner', """
IF-THEN PLANS (implementation intentions)
Habits
1. If ________________________________ (time / cue), then I will ________________ at ____________ (place).
   Tiny version: ________________   Anchor (after I ...): ________________
2. If ________________________________, then I will ________________ at ____________.
   Tiny version: ________________   Anchor: ________________
3. If ________________________________, then I will ________________ at ____________.
   Tiny version: ________________   Anchor: ________________
Obstacles
4. If ________________________________ (obstacle), then I will ________________.
5. If ________________________________ (obstacle), then I will ________________.
""", ''),
        ('Loop setup', """
[ ] Loop Habit Tracker installed
[ ] Habit 1: ______________  reminder at ____  days: every day
[ ] Habit 2: ______________  reminder at ____  days: ______
[ ] Habit 3: ______________  reminder at ____  days: Sunday
[ ] Ticked daily for 14 days
Day-14 check: weakest day ______  new if-then plan for it: _______________________
""", ''),
    ],
    mistakes=[
        ('Vague plans ("study in the morning").', 'Name the cue, place and action: "after tea, at the kitchen table, AnkiDroid".'),
        ('Starting ten habits at once.', 'Two or three habits first. Add more when these feel automatic.'),
        ('Expecting a habit in 21 days.', 'The average in Lally\'s research was 66 days. Keep going past the first month.'),
        ('Only planning for good days.', 'Write if-then plans for your usual obstacles too.'),
    ],
    quiz=[
        {'q': 'Which is an implementation intention?', 'o': ['"If I have poured my morning tea, then I will open AnkiDroid at the kitchen table"', '"I will study harder this month"', '"I want to pass the PSC exam"', '"I should use AnkiDroid more"'], 'a': 'A', 'why': 'It names the situation, the place and the action.'},
        {'q': 'What did Gollwitzer and Sheeran\'s meta-analysis find?', 'o': ['If-then plans had a medium-to-large effect on reaching goals across 94 tests', 'If-then plans had no effect', 'They work only for exercise', 'They harm motivation'], 'a': 'A', 'why': 'The reported effect size was d = 0.65.'},
        {'q': 'In Lally\'s research, how long did forming a daily habit take on average?', 'o': ['About 66 days, ranging from 18 to 254', 'Exactly 21 days', 'One week', 'One year for everyone'], 'a': 'A', 'why': 'Habits take weeks to months, and people vary widely.'},
        {'q': 'What is a good tiny version of "do AnkiDroid reviews every day"?', 'o': ['Open AnkiDroid and do 10 cards after morning tea', 'Do 500 cards every morning', 'Review only on Sundays', 'Make 50 new cards a day'], 'a': 'A', 'why': 'A tiny version anchored to a routine is easy to start every day.'},
    ],
    study='Gollwitzer and Sheeran\'s abstract, the Surrey article on habits and College Success 3.6',
    action='Write five if-then plans, set up three tiny habits in Loop and track them for 14 days',
)

L3 = lesson(
    M, 3,
    outcome='Use small rewards and streaks without letting them control you, connect daily study to your reasons, and restart quickly after a bad day or week.',
    split='15 minutes reading, 20 minutes resources, 25 minutes action plus a week of rewards',
    core=f"""
### Motivation often follows action

Many people wait to feel motivated before they study. Often it works the other way round: you start, you make a little progress, and the progress makes you want to continue. The five-minute start (LRN-M06-L01) and tiny habits (LRN-M06-L02) use this. Motivation is helpful, but your system should work on days when you don't feel it.

### Rewards that help

The exam is months away; Reels are right here. A small, immediate reward after a study block gives your brain something now:

- A cup of tea or coffee, a short walk, a favourite song, a call with a friend, a sweet on Sundays
- **Pairing:** keep something you enjoy only for study-related moments, such as a favourite podcast only on the walk to the library

Two rules: the reward comes **after** the block, and it must not undo the work. An hour of Reels as a "reward" for a 25-minute block is a trap.

### Streaks: useful, with one rule

Loop and AnkiDroid show your streaks and calendars. A growing chain of ticks is motivating. The danger is **all-or-nothing thinking**: one missed day breaks the chain, you feel the streak is "ruined", and you stop for a week.

Use one rule: **never miss twice.** Missing one day is normal life. Missing two in a row starts a new habit: not studying. If you miss a day, the next day's tiny version is non-negotiable.

### Your reasons, and your process

Write down **why** you are doing this: a government job, security for your family, independence, pride, the subjects you enjoy. Read it on hard days. But don't rely only on the big outcome; it is far away and uncertain. Also take pride in the **process**: today's blocks done, this week's reviews done, this month's rising mock scores. Your Weekly tab and AnkiDroid statistics make the process visible.

### The restart protocol

Bad weeks will happen: illness, a wedding, exam stress, a family problem. What matters is how fast you restart.

1. **No guilt.** Forgive yourself (LRN-M06-L01); it makes restarting easier.
2. **Do the tiny version today,** not tomorrow and not "from Monday".
3. **Find what broke:** sleep, health, a family event, an unrealistic plan, stress.
4. **Adjust the plan:** fewer blocks, new cards to 0 in AnkiDroid until the backlog clears (LRN-M04-L04), one subject instead of three.
5. **Tell your study partner** or a family member, and agree on the next check-in.

If a bad week turns into weeks of low mood, exhaustion or dread, that is not a motivation problem; talk to someone you trust and see Module 19.
""",
    example="""
**Ashiq** had a 23-day AnkiDroid streak when his cousin's wedding took over his family's life for five days. He didn't open the app once, and when he did, it showed 350 cards due. His first thought was, "The streak is gone, what's the point?"

His study partner Anu sent him the restart protocol from this lesson. He forgave himself (a wedding is a good reason), did the tiny version that same evening (10 cards), set new cards to 0, and did 20 minutes of reviews a day. He saw what had broken: no plan for family events. He added an if-then plan: "If there is a family function, then I will do 10 cards before leaving the house."

Within four days the backlog was gone. He started a new streak and wrote on the first page of his notebook: "Never miss twice." His reason card, taped inside the cover, says: "A permanent job, so Umma can stop working at the shop."
""",
    evidence=[
        ('Small immediate rewards after study', 'limited', 'Consistent with basic research on reinforcement; little direct research with exam learners.'),
        ('Forgiving yourself after a lapse', 'limited', 'One study of 134 students (Wohl and others, 2010) found less later procrastination.'),
        ('"Never miss twice" and restart protocols', 'limited', 'Practical rules, consistent with Lally\'s finding that habit strength builds over many repetitions.'),
    ],
    resources=[
        ('wohl', 'Reread the self-forgiveness study summary', '5 minutes'),
        ('os-cs-3', 'Reread 3.6 Goal Setting and Motivation, focusing on motivation', '15 minutes'),
        ('loop', 'Look at your Loop charts and statistics for the last two weeks', '5 minutes'),
    ],
    steps=[
        'Write your reason card: three lines on why you are preparing and learning. Keep it inside your notebook cover or as your phone\'s lock-screen note.',
        'Write a reward menu of five small rewards that don\'t undo your work.',
        'For one week, take one reward from the menu after each completed study block, and tick it.',
        'Write your restart protocol (use the template) and keep it in your notebook.',
        'Look at your Loop and AnkiDroid records. Find the day of the week you are most likely to miss, and write an if-then plan for it.',
    ],
    proof='Your reason card, your reward menu with a week of ticks, your restart protocol and your weak-day if-then plan.',
    templates=[
        ('reward menu', """
REWARD MENU (small, immediate, after the block, never undoing the work)
1. ____________________ (e.g. tea on the verandah)
2. ____________________ (e.g. a 10-minute walk)
3. ____________________ (e.g. one favourite song)
4. ____________________ (e.g. a call with a friend)
5. ____________________ (e.g. Sunday sweet after the weekly review)
Pairing: I only ____________________ when I ____________________.
Week: Mon [ ] Tue [ ] Wed [ ] Thu [ ] Fri [ ] Sat [ ] Sun [ ]
""", ''),
        ('restart protocol', """
RESTART PROTOCOL (after a bad day or week)
1. Forgive: "I missed ____ because ____. That is human."
2. Tiny version TODAY: ______________________ (not "from Monday")
3. What broke? sleep / health / family event / unrealistic plan / stress / other: ____
4. Adjust: blocks ___ -> ___ ; AnkiDroid new cards -> 0 until due count < ___ ; subjects: ____
5. Tell: ______________ (study partner or family). Next check-in: ______
Rule: never miss twice.
""", ''),
    ],
    mistakes=[
        ('Rewards that undo the work.', 'An hour of scrolling after 25 minutes of study is a trap. Keep rewards small and short.'),
        ('Treating a broken streak as failure.', 'Never miss twice. One missed day is normal.'),
        ('Restarting "from Monday".', 'Do the tiny version today.'),
        ('Relying only on the big goal for motivation.', 'Track and celebrate the process: blocks, reviews, rising scores.'),
    ],
    quiz=[
        {'q': 'What does the "never miss twice" rule mean?', 'o': ['Missing one day is normal; the next day\'s tiny version is non-negotiable', 'You must never miss a single day', 'Miss two days, then restart on Monday', 'Study twice as much after missing a day'], 'a': 'A', 'why': 'It keeps one lapse from becoming a new habit of not studying.'},
        {'q': 'Which is a good reward after a 25-minute study block?', 'o': ['A cup of tea and a short walk', 'An hour of Reels', 'Skipping the next block', 'Buying an expensive gadget'], 'a': 'A', 'why': 'Small and immediate, and it doesn\'t undo the work.'},
        {'q': 'After a bad week, what is the first step of the restart protocol?', 'o': ['Forgive yourself', 'Plan a 12-hour study day', 'Delete your decks and start fresh', 'Wait for Monday'], 'a': 'A', 'why': 'Guilt makes restarting harder; forgiveness clears the way.'},
        {'q': 'Why track the process (blocks, reviews, scores) and not only the exam goal?', 'o': ['The goal is far away and uncertain; visible daily progress keeps you going', 'The exam goal doesn\'t matter', 'Process tracking replaces studying', 'Goals reduce motivation'], 'a': 'A', 'why': 'Seeing progress now supports motivation between now and the exam.'},
    ],
    study='The self-forgiveness summary, College Success 3.6 and your own Loop charts',
    action='Write your reason card, reward menu and restart protocol, and use rewards for a week',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    M,
    overview="""
Understand why you procrastinate, and build habits that run on days when motivation is low: if-then plans, tiny habits anchored to your routines, small rewards, and a restart protocol for bad weeks.

PSC preparation is a long race, and most aspirants don't fail because of ability; they fail because study becomes irregular. This module treats procrastination as a feeling to manage, not a character flaw, and gives you the tool with some of the strongest evidence in behaviour research: the if-then plan.

The result is a small habit system, tracked in the free Loop app, with your reasons, rewards and a plan for restarting.
""",
    outcomes=[
        'Explain procrastination as short-term mood repair and find your own triggers',
        'Use the five-minute start and shrink tasks you avoid',
        'Write if-then plans for habits and obstacles, and anchor tiny habits to routines',
        'Track habits in Loop and use rewards and streaks wisely',
        'Restart quickly after a bad week with a written protocol',
    ],
    lessons=LESSONS,
    tools=[
        'The **procrastination log** and **task shrinker**',
        'The **if-then planner** and **Loop Habit Tracker** with three habits',
        'Your **reason card**, **reward menu** and **restart protocol**',
    ],
    project='My habit system',
    project_steps=[
        'Show at least 14 days of Loop records for your three habits.',
        'Review your if-then plans: keep those that worked, rewrite those that didn\'t, and add one for your weakest day.',
        'Put your reason card, reward menu and restart protocol together on one page in your notebook.',
        'Explain your habit system to your study partner or a family member, and ask them to check in with you once a week for the next month.',
    ],
    project_proof='A Loop screenshot with 14 or more days, your updated if-then plans and your one-page habit system.',
    rubric=[
        ('Understanding procrastination', 'Still "I\'m lazy"', 'Know the triggers in general', 'Found my own triggers in a log and acted on them'),
        ('If-then plans', 'None', 'Vague plans', 'Specific plans for habits and obstacles, revised after 14 days'),
        ('Tracking', 'Not tracked', 'Tracked a few days', '14 or more days in Loop'),
        ('Restarting', 'No plan', 'A plan in my head', 'A written protocol, used at least once if needed'),
    ],
    short=[
        'Write three if-then plans and add one habit (daily AnkiDroid) to Loop.',
        'Keep the restart protocol in your notebook.',
    ],
    flashcards=[
        ('Procrastination in one line (Sirois and Pychyl)', 'Short-term mood repair: avoiding an unpleasant task to feel better now.'),
        ('The five-minute start', 'Promise only five minutes; most people keep going.'),
        ('Implementation intention', '"If [situation], then I will [action]."'),
        ('Effect of if-then plans (Gollwitzer and Sheeran)', 'Medium to large (d = 0.65) across 94 tests.'),
        ('Average time to form a daily habit (Lally)', 'About 66 days, from 18 to 254.'),
        ('Tiny habit with an anchor', '"After I pour my morning tea, I will open AnkiDroid and do 10 cards."'),
        ('Streak rule', 'Never miss twice.'),
        ('First step after a bad week', 'Forgive yourself, then do the tiny version today.'),
    ],
    mistakes=[
        ('Reading about habits without writing any if-then plans.', 'The plan is one sentence. Write it now.'),
        ('Building a perfect system and abandoning it after one bad week.', 'The restart protocol is part of the system.'),
    ],
)
