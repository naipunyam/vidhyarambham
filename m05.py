"""Module 5: Focus and deep work."""
from common import lesson, module, link, rules, fence, table
import tools

M = 5

L1 = lesson(
    M, 1,
    outcome='Explain why focus breaks, measure your own focus with a Focus log, and start a focus ladder that lengthens your study blocks step by step.',
    split='20 minutes reading, 15 minutes resources, 40 minutes action plus a week of logging',
    core=f"""
### Why focus breaks

Attention is the doorway to working memory (Module 1), and it is easily pulled away. Three things break it most often for PSC aspirants:

1. **Interruptions from outside:** notifications, calls, people, noise. Each one pulls attention away, and getting back into a hard topic takes time.
2. **Switching by choice:** "just checking" WhatsApp, a quick look at YouTube. In the Stanford multitasking study, heavy media multitaskers were worse at ignoring irrelevant information and at switching tasks ({link('ophir', 'Ophir and others, 2009')}). That study shows a link, not proof that multitasking caused the problems, but the cost of switching is easy to feel.
3. **Mind-wandering from inside:** thoughts about family, money, the exam, food. This is normal for every human brain. The skill is not to stop it but to **notice it and come back**.

The phrase **deep work** comes from a popular book by the computer scientist Cal Newport. It means long, undistracted work on a demanding task. For you, a deep-work block is 25 to 50 minutes on one PSC topic, with nothing else competing for attention.

### Can you "train" your attention span?

Honestly: there is no proven quick training that enlarges attention in general. "Brain training" games make you better at those games, not at studying (Module 1; {link('wm-training', 'Melby-Lervåg and others, 2016')}). What reliably helps is practical:

- **Remove what pulls attention:** the phone out of reach, notifications off (LRN-M05-L03), a quiet place.
- **Practise focusing on real study,** in blocks that grow slowly, like building stamina for running. This is the **focus ladder** below.
- **Rest properly:** sleep (Module 19) and real breaks (LRN-M05-L02).
- **Handle urges:** when you feel the pull to check the phone, write the urge on a "distraction pad" and return to the task. The urge usually fades in a minute or two.

### The focus ladder

1. Take your baseline "minutes to first distraction" from week 0.
2. Set your study block **5 minutes longer** than that, with a minimum of 15 minutes.
3. A block **counts** when you stayed on the task the whole time, with any stray thoughts written on the pad instead of acted on.
4. After **five counted blocks** at one length, add 5 minutes.
5. Stop climbing at 45 to 50 minutes. Longer blocks rarely help; regular blocks do.

### The Focus log

Each block gets one row in a new **Focus** tab: task, planned minutes, minutes to first distraction, tally of distractions, where the phone was, and a focus rating. After two weeks, the log shows what helps your focus and what hurts it, which matters more than any general advice.
""",
    example="""
**Ashiq** scored 9 minutes to first distraction in his week 0 focus test, with 11 tally marks in 45 minutes, nearly all of them phone checks. He did not believe he could ever sit for 45 minutes.

He started his focus ladder at 15-minute blocks, with the phone charging in the kitchen and a small notebook as his distraction pad. In the first week, the pad filled with lines like "reply to Faisal", "check the cricket score", "look up the meaning of 'concurrent'". He dealt with them in his breaks.

He logged every block in the Focus tab. By the end of week two he had moved to 25-minute blocks; by week four, 35. The log taught him two things he wouldn't have guessed: his worst blocks were straight after lunch, and blocks with earphones playing music had twice as many distractions as silent ones. He moved his maths practice to 7 a.m. and stopped the music.
""",
    evidence=[
        ('Heavy media multitasking goes with weaker attention control', 'moderate', 'Ophir and others (2009) found the link; the study cannot show that multitasking caused it.'),
        ('Brain-training games to build general attention', 'none', 'Training improves the trained task, with no convincing transfer (Melby-Lervåg and others, 2016).'),
        ('Removing the phone and notifications during study', 'limited', 'Plausible and widely used; studies of phones and attention have mixed results. Your Focus log shows whether it works for you.'),
        ('A focus ladder of slowly longer blocks', 'limited', 'A practical method with no direct research. Judge it by your log and your retest.'),
    ],
    resources=[
        ('ophir', 'Reread the report on media multitaskers, noting the three findings', '5 minutes'),
        ('wm-training', 'Reread the abstract: why games don\'t build general attention', '5 minutes'),
        ('os-cs-3', 'Read 3.4 How to Manage Time, for ideas on where and when to study', '15 minutes'),
    ],
    steps=[
        'Add a Focus tab to your Learning Workbook with the headings below.',
        'Look up your week 0 "minutes to first distraction". Set your first focus-ladder block length: 5 minutes more, and at least 15 minutes.',
        'Keep a distraction pad (a small notebook or slip of paper) beside you in every study block. Write urges and stray thoughts on it instead of acting on them.',
        'For one week, log every study block in the Focus tab, including where the phone was.',
        'At the end of the week, write three lines: your most common distraction, the time of day you focus best, and one change for next week. Move up the ladder if you have five counted blocks.',
    ],
    proof='A screenshot of your Focus tab with a week of blocks, a photo of one page of your distraction pad, and your three lines.',
    templates=[
        ('Focus tab headings', tools.FOCUS_LOG, 'csv'),
        ('focus ladder', """
FOCUS LADDER     Baseline minutes to first distraction: ___
Rung  Block length   Counted blocks (5 to climb)    Dates
1     ___ min        [ ] [ ] [ ] [ ] [ ]            ______
2     ___ min        [ ] [ ] [ ] [ ] [ ]            ______
3     ___ min        [ ] [ ] [ ] [ ] [ ]            ______
4     ___ min        [ ] [ ] [ ] [ ] [ ]            ______
5     45-50 min      [ ] [ ] [ ] [ ] [ ]            ______
A block counts when I stayed on the task the whole time and wrote urges on the pad.
""", ''),
        ('distraction pad', """
DISTRACTION PAD      Date: ______
Time   Urge or thought                          Deal with it when?
_____  ______________________________________   break / evening / never
_____  ______________________________________   break / evening / never
_____  ______________________________________   break / evening / never
""", ''),
    ],
    mistakes=[
        ('Starting with 60-minute blocks.', 'Start just above your baseline and climb 5 minutes at a time.'),
        ('Fighting every stray thought.', 'Write it on the pad and return. Noticing and returning is the skill.'),
        ('Blaming yourself for poor focus.', 'Most poor focus comes from the setup. Change the setup first, then judge.'),
        ('Not logging.', 'Without the Focus log you are guessing. Two weeks of rows show what really helps.'),
    ],
    quiz=[
        {'q': 'What did the Stanford study find about heavy media multitaskers?', 'o': ['They were worse at ignoring irrelevant information and switching tasks, though the study shows a link, not cause', 'They were better at focusing', 'They had longer attention spans', 'Nothing at all'], 'a': 'A', 'why': 'Ophir and others (2009) found weaker attention control in heavy multitaskers.'},
        {'q': 'Your baseline minutes to first distraction is 12. What block length does the focus ladder start with?', 'o': ['17 minutes', '60 minutes', '5 minutes', '45 minutes'], 'a': 'A', 'why': 'Start 5 minutes above your baseline, with a minimum of 15.'},
        {'q': 'An urge to check WhatsApp arrives mid-block. What does this lesson suggest?', 'o': ['Write it on the distraction pad and return to the task', 'Check quickly and come back', 'Stop the block and start again tomorrow', 'Keep the phone in your hand to resist it'], 'a': 'A', 'why': 'The pad takes the urge out of your head; it usually fades in a minute or two.'},
        {'q': 'What does research say about brain games for building attention?', 'o': ['They improve the trained games, with no convincing transfer to studying', 'They double attention span', 'They work only for children', 'They replace sleep'], 'a': 'A', 'why': 'Gains stay narrow; practical changes to your setup help more.'},
    ],
    study='The media multitasking report and College Success 3.4 How to Manage Time',
    action='Start the Focus tab, the focus ladder and a distraction pad, and log a week of blocks',
)

L2 = lesson(
    M, 2,
    outcome='Plan a realistic week of focused study blocks around PSC, work and family, with Pomodoro-style breaks and the weekly study planner.',
    split='15 minutes reading, 15 minutes resources, 40 minutes planning plus a week of blocks',
    core=f"""
### The Pomodoro technique

The **Pomodoro technique**, created by Francesco Cirillo, is simple: work on one task for 25 minutes, take a 5-minute break, and after four rounds take a longer break of 15 to 30 minutes. It is named after a tomato-shaped kitchen timer.

How strong is the evidence? There is little direct research. One careful study with 87 university students compared fixed, Pomodoro-style breaks (24 minutes of study and 6 of rest, or 12 and 3) with breaks the students chose themselves. With fixed breaks, students reported less fatigue and distraction and more concentration and motivation, and they got as much work done in less time; students who chose their own breaks studied in longer stretches and took longer breaks ({link('biwer', 'Biwer and others, 2023')}). One small study is a start, not proof. Treat Pomodoro as a useful tool, and judge it by your Focus log.

Useful adjustments:

- **25 and 5 is a starting point.** As your focus ladder climbs, 40 and 10 or 50 and 10 may suit you better.
- **A break is a real break:** stand up, drink water, look outside, stretch. Scrolling the phone is not a break; it tends to stretch to 20 minutes and drags your mind elsewhere.
- **One Pomodoro, one task, one method:** for example, "Kerala renaissance: two chunks with recall, then 10 MCQs".

### Time-blocking

**Time-blocking** means giving each study task a fixed slot in your week, written down in advance, instead of studying "whenever I get time". It turns vague intentions into appointments with yourself, and it links to the strongest habit research in Module 6 (if-then plans).

1. **Find your fixed commitments first:** work, family duties, travel, prayer times, meals.
2. **Protect your best hours** for your hardest PSC work. Many people focus best early in the morning; your Focus log tells you your own best time.
3. **Give every block a task and a method,** not just a subject. "Maths" is vague; "mixed set of 12: percentages, ratio, averages, time and work" is a block.
4. **Plan for real life in Kerala:** power cuts (keep offline PDFs and paper ready), monsoon days, functions and festivals, visitors. Leave one empty buffer block a week to catch up.
5. **Plan the week on Sunday** during your weekly review, and tick blocks as you finish them.

The **weekly study planner** below is one of the six core tools of your learning system. In Module 12 it becomes part of your 12-week PSC plan.
""",
    example="""
**Sreeja** has two study windows a day: 10:00 to 10:45, after the children leave for school, and 21:30 to 22:15, after they sleep. She used to "study when the work is done", which often meant not at all.

On Sunday she filled in the weekly planner. Each morning window became one 25-minute Pomodoro of new learning and one 15-minute block of Revision-tab reviews, with a 5-minute break between them. Each evening window became AnkiDroid reviews and one 25-minute block of mixed MCQs. Saturday afternoon, when her husband takes the children to his mother's house, became her 90-minute block for the course's action task. Wednesday evening stayed empty as a buffer.

She ticked 11 of her 13 planned blocks in the first week. The two she missed were on the day of a family function, and the buffer block caught one of them. For the first time she could see exactly what she had studied in a week.
""",
    evidence=[
        ('Planned, fixed breaks (Pomodoro-style)', 'limited', 'One study of 87 students (Biwer and others, 2023): less fatigue and distraction, more concentration, same work done in less time. Promising, not proven.'),
        ('Time-blocking a week in advance', 'limited', 'Little direct research; it applies if-then planning, which has strong evidence (Module 6).'),
        ('Breaks spent scrolling the phone', 'limited', 'Little research either way; the practical risk is that breaks stretch and attention leaves the topic.'),
    ],
    resources=[
        ('biwer', 'Read the abstract of the Pomodoro-breaks study', '5 minutes'),
        ('os-cs-3', 'Read 3.5 on prioritising and 3.7 on strategies for time and task management', '20 minutes'),
    ],
    steps=[
        'List your fixed commitments for next week: work, family, travel, meals, prayer, and your best focus time from your Focus log.',
        'Fill in the weekly study planner below for next week. Every block gets a subject, a topic and a method. Include daily AnkiDroid reviews, your Revision-tab reviews, one Saturday action-task block and one empty buffer block.',
        'Use Pomodoro-style blocks (25 and 5, or your focus-ladder length) for every block, and log each one in the Focus tab.',
        'Take real breaks, away from the phone.',
        'At the end of the week, count planned versus done blocks, and note what got in the way. Plan the following week in your weekly review.',
    ],
    proof='Your filled-in weekly planner with ticks, and a week of rows in the Focus tab.',
    templates=[
        ('weekly study planner (core tool)', tools.STUDY_PLANNER, ''),
        ('one Pomodoro block card', """
BLOCK      Time: ______  Length: ___ min (break ___ min)
Task: ____________________________________________ (one task only)
Method: retrieval / mixed practice / Feynman / cards / reading + recall
Done when: _______________________________________ (e.g. 2 chunks + 10 MCQs)
Phone: in another room [ ]   Distraction pad ready [ ]
After: Focus log row added [ ]   Result: _____________________________
""", ''),
    ],
    mistakes=[
        ('Planning ten hours a day.', 'Plan what you really did last week plus a little. A plan you keep beats a plan you admire.'),
        ('Blocks without a task ("study GK").', 'Write the topic and method, so the block starts without decisions.'),
        ('Spending breaks on the phone.', 'Stand up, drink water, look outside. Keep the phone for the long break or the evening.'),
        ('No buffer.', 'Real life in Kerala includes power cuts, guests and functions. Keep one empty block a week.'),
    ],
    quiz=[
        {'q': 'What did Biwer and others (2023) find with fixed Pomodoro-style breaks?', 'o': ['Less fatigue and distraction and more concentration, with the same work done in less time', 'Students learned twice as much', 'No difference in anything', 'Students felt more tired'], 'a': 'A', 'why': 'One study with 87 students; promising, not proof.'},
        {'q': 'Which is a well-planned study block?', 'o': ['"Kerala renaissance: two chunks with recall, then 10 MCQs, 25 minutes"', '"Study GK"', '"Read for a while"', '"Revise everything"'], 'a': 'A', 'why': 'It names a topic, a method and when it is done.'},
        {'q': 'What is a good use of a 5-minute break?', 'o': ['Stand up, drink water and look outside', 'Scroll Instagram', 'Start a new topic', 'Reply to every WhatsApp group'], 'a': 'A', 'why': 'A real break rests attention; phone breaks tend to stretch and pull you away.'},
        {'q': 'Why keep one empty buffer block a week?', 'o': ['To catch up after power cuts, guests or functions', 'Because the brain needs one empty block', 'Because PSC exams are on that day', 'It is not needed'], 'a': 'A', 'why': 'Real life interrupts plans; a buffer keeps one bad day from ruining the week.'},
    ],
    study='The Pomodoro-breaks study and College Success sections 3.5 and 3.7',
    action='Plan next week in the weekly study planner and run it with Pomodoro-style blocks',
)

L3 = lesson(
    M, 3,
    outcome='Set up your Android phone to support study instead of interrupting it, using Digital Wellbeing, notification control and a few physical rules, and measure the change in screen time.',
    split='15 minutes reading, 15 minutes resources, 40 minutes setup plus a check a week later',
    core=f"""
For most PSC aspirants, the phone is both the best study tool (PDFs, AnkiDroid, previous papers, classes) and the biggest distraction (WhatsApp groups, Reels, YouTube, games). This lesson keeps the first and tames the second.

### Step 1: see the truth

Android's **Digital Wellbeing** shows a dashboard of how long you used each app today and in the past days, how many notifications you got, and how many times you unlocked the phone ({rules('wellbeing', 'Android Help: Digital Wellbeing')}). Most people underestimate their screen time. Take a screenshot before you change anything; that is your baseline.

Menus differ by phone brand and Android version. Samsung, Xiaomi, Realme and others may call these settings something slightly different; search your Settings for "Digital Wellbeing", "Focus mode" or "screen time".

### Step 2: silence the noise

- **Turn off notifications** for every app that isn't urgent: games, shopping, news, social media. Keep calls, SMS, your bank and the few people you must reach.
- **Mute WhatsApp groups** (open the group, tap its name, choose mute, then always). Read them once a day at a time you choose.
- **Turn off autoplay** in YouTube, so one PSC class doesn't become an hour of recommendations.

### Step 3: use the built-in tools

- **Focus mode** pauses the apps you choose (for example YouTube, Instagram, games) and can run on a schedule. Set it for your study blocks, and leave AnkiDroid and your PDF reader unpaused.
- **App timers** set a daily limit for an app; the limit resets at midnight. Try 30 minutes a day for your biggest time-taker.
- **Bedtime mode** can turn the screen grey and silence the phone at night. Greyscale makes scrolling much less attractive.

### Step 4: physical rules beat willpower

- **Out of reach during study blocks:** in another room, or in a drawer. Use a cheap timer or the clock app on a family member's phone if you need one.
- **Social apps off the home screen.** One extra tap to reach them is often enough to stop the automatic reach.
- **Charge the phone outside the bedroom** at night (Module 19).
- **Study offline when you can:** download PDFs and previous papers, then turn on airplane mode while reading them.

### Honest expectations

Research on phones and attention is mixed: some studies find that a nearby phone hurts focus, others don't. Nobody needs a study to know that a notification interrupts. Treat this lesson as an experiment: compare your Digital Wellbeing numbers and your Focus log before and after, and keep what works for you.
""",
    example="""
**Ashiq** took his first Digital Wellbeing screenshot and was shocked: 6 hours 40 minutes of screen time on the day, more than 3 hours of it on Instagram and YouTube, and 92 unlocks.

He spent 40 minutes on setup. Notifications went off for all but calls, SMS, his bank and his family group. He muted 14 WhatsApp groups and decided to read them once at 8 p.m. Focus mode paused Instagram, YouTube and two games from 6 to 8 a.m. and 7 to 9 p.m., his study blocks. He set a 30-minute app timer on Instagram, turned on greyscale at 10:30 p.m., and moved every social app into a folder on the last screen.

A week later his screen time was 3 hours 50 minutes a day, with 41 unlocks. In his Focus log, minutes to first distraction rose from about 15 to 22. He had to switch Focus mode off twice for a class link sent on WhatsApp; he now asks for class links by SMS.
""",
    evidence=[
        ('Notifications interrupt focus', 'moderate', 'An interruption pulls attention away by definition; how long recovery takes varies by person and task.'),
        ('Focus modes, app timers and greyscale reduce phone use', 'limited', 'Little strong research; easy to test with your own Digital Wellbeing numbers.'),
        ('A phone nearby (even silent) hurts focus', 'limited', 'Studies have mixed results. Keeping it out of reach costs nothing, so test it with your Focus log.'),
    ],
    resources=[
        ('wellbeing', 'Read the parts on the dashboard, app timers, Focus mode and Bedtime mode, and find them on your phone', '15 minutes'),
        ('ophir', 'Optional: reread why switching between media is costly', '5 minutes'),
    ],
    steps=[
        'Take a screenshot of your Digital Wellbeing dashboard (screen time per app, notifications and unlocks) before changing anything.',
        'Do a notification audit with the template below: turn off every notification you don\'t need, and mute all WhatsApp groups except one or two.',
        'Set Focus mode on a schedule for your study blocks, pausing your most distracting apps but not AnkiDroid or your PDF reader.',
        'Set an app timer on your biggest time-taker, and turn on Bedtime mode with greyscale for your sleep time.',
        'Move social apps off the home screen, and decide where the phone will be during study blocks and at night.',
        'After 7 days, take a second dashboard screenshot and compare screen time, unlocks and your Focus log.',
    ],
    proof='Your before and after dashboard screenshots, screenshots of Focus mode, the app timer and Bedtime settings, and your completed notification audit.',
    templates=[
        ('notification audit', """
NOTIFICATION AUDIT      Date: ______
App                 Keep notifications?   Why
Calls / SMS         yes                   family, emergencies
Bank app            yes                   fraud alerts
WhatsApp (chats)    yes / no              ______________
WhatsApp groups     muted (always)        read once a day at ____
YouTube             no                    ______________
Instagram / Reels   no                    ______________
Games               no                    ______________
Shopping            no                    ______________
Other: ________     yes / no              ______________
""", ''),
        ('phone setup checklist', """
[ ] Baseline dashboard screenshot taken (screen time ___ h ___ min, unlocks ___)
[ ] Notifications off for everything not urgent
[ ] WhatsApp groups muted; reading time set: ____
[ ] YouTube autoplay off
[ ] Focus mode scheduled: ____ to ____ and ____ to ____ (AnkiDroid not paused)
[ ] App timer: __________ at ___ min a day
[ ] Bedtime mode with greyscale from ____
[ ] Social apps off the home screen
[ ] Study blocks: phone in ______________   Night: phone charges in ______________
[ ] After 7 days: screen time ___ h ___ min, unlocks ___
""", ''),
    ],
    mistakes=[
        ('Deleting every app in a burst of resolve.', 'All-or-nothing rarely lasts. Silence and limit them; keep the ones you need.'),
        ('Relying on willpower with the phone on the desk.', 'Distance works better than willpower. Put it in another room.'),
        ('Pausing your study apps in Focus mode.', 'Leave AnkiDroid and your PDF reader free; pause only the distractions.'),
        ('Never checking the numbers again.', 'Look at the dashboard in your weekly review. Habits drift back.'),
    ],
    quiz=[
        {'q': 'What does an Android app timer do?', 'o': ['Sets a daily limit for an app, which resets at midnight', 'Deletes the app after a week', 'Speeds up the app', 'Blocks calls'], 'a': 'A', 'why': 'Digital Wellbeing app timers limit daily use and reset at midnight.'},
        {'q': 'How should you set up Focus mode for study?', 'o': ['Schedule it for study blocks, pausing distracting apps but not AnkiDroid or your PDF reader', 'Pause every app including AnkiDroid', 'Use it only at night', 'Turn it on once a month'], 'a': 'A', 'why': 'Keep the study tools; pause the distractions.'},
        {'q': 'What is the honest summary of research on phones and attention?', 'o': ['Mixed results, so test changes with your own screen time and Focus log', 'Phones have no effect at all', 'Phones permanently damage attention', 'A silent phone on the desk always halves focus'], 'a': 'A', 'why': 'Studies disagree; your own before-and-after numbers decide.'},
        {'q': 'Which physical rule tends to work better than willpower?', 'o': ['Keeping the phone in another room during study blocks', 'Keeping it face-down on the desk', 'Holding it in your pocket', 'Keeping it on silent beside the book'], 'a': 'A', 'why': 'Distance removes the automatic reach.'},
    ],
    study='The Android Help page on Digital Wellbeing, with each setting found on your own phone',
    action='Audit notifications, set up Focus mode, an app timer and Bedtime mode, and compare screen time after a week',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    M,
    overview="""
Protect your attention: understand why focus breaks, rebuild your study stamina with a focus ladder, plan your week in time blocks with Pomodoro-style breaks, and set up your Android phone so it helps instead of interrupting.

Every method in this course needs attention first. A PSC aspirant who studies three focused hours learns more than one who sits for six with the phone buzzing. This module is practical: you measure your focus, change your setup, and measure again.

At the end you retake the week 0 focus test, so you can see how much your setup and practice have already changed.
""",
    outcomes=[
        'Explain why focus breaks and what can and cannot "train" attention',
        'Run a focus ladder and keep a Focus log',
        'Plan a realistic week with the weekly study planner and Pomodoro-style blocks',
        'Set up Digital Wellbeing, notifications and physical rules on your phone',
        'Measure the change with your screen time and a repeat focus test',
    ],
    lessons=LESSONS,
    tools=[
        'The **weekly study planner** (one of the six core tools)',
        'The **Focus** tab, the **focus ladder** and the **distraction pad**',
        'The **notification audit** and **phone setup checklist**',
    ],
    project='My focus system and a repeat focus test',
    project_steps=[
        'Make sure your Focus tab has at least 10 logged blocks and your phone setup checklist is complete.',
        'Repeat the week 0 focus test (45 minutes, normal PSC study, tally marks), this time with your new setup.',
        'Compare minutes to first distraction and tally marks with your week 0 average, and write two lines on what made the difference.',
        'Write your three focus rules for the rest of the course (for example: phone in the kitchen, 35-minute blocks, maths at 7 a.m.).',
    ],
    project_proof='Your Focus tab, the repeat focus test result next to your week 0 result, and your three focus rules.',
    rubric=[
        ('Measurement', 'No Focus log', 'A few blocks logged', '10 or more blocks logged and a repeat focus test'),
        ('Phone', 'Unchanged', 'Some settings changed', 'Full setup done and screen time compared after a week'),
        ('Planning', 'Studying "when I get time"', 'A plan made but not followed', 'A weekly planner followed, with planned and done counted'),
        ('Rules', 'None', 'General ideas', 'Three specific focus rules based on your own log'),
    ],
    short=[
        'Do LRN-M05-L03 (phone setup) first: it gives the biggest change for the least time.',
        'Use one 25-minute Pomodoro a day with the phone in another room, and log it.',
    ],
    flashcards=[
        ('Three things that break focus', 'Outside interruptions, switching by choice, and mind-wandering.'),
        ('The skill with mind-wandering', 'Notice it and come back; write urges on a distraction pad.'),
        ('Focus ladder rule', 'Start 5 minutes above your baseline; add 5 minutes after five counted blocks; stop at 45 to 50.'),
        ('The Pomodoro technique', '25 minutes on one task, a 5-minute break; a longer break after four rounds.'),
        ('Biwer and others (2023) in one line', 'Fixed breaks gave less fatigue and more concentration, with the same work done in less time.'),
        ('Digital Wellbeing tools', 'Dashboard, app timers, Focus mode and Bedtime mode.'),
        ('Best physical rule for the phone', 'Out of reach (another room) during study blocks.'),
    ],
    mistakes=[
        ('Changing everything at once and keeping nothing.', 'Make the phone changes this week and add one new habit at a time.'),
        ('Judging focus by how you feel.', 'Use the numbers: minutes to first distraction, tallies and screen time.'),
    ],
)
