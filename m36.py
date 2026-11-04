from common import lesson, module, link, xref, table, fence, Q, PLAYBOOK, WEEKS, FOLDERS
import plan
import tools

a2, b2 = WEEKS[(36, 2)]

PROJECT_PLAN = """CAPSTONE PROJECT PLAN                         Start ______  End (day 30) ______
PROJECT 1: 30-DAY BEHAVIOUR CHANGE
Behaviour (specific): ______________________
Why it matters (value): ______  Identity: "I'm becoming someone who ______"
Metric (one number, measured daily): ______  Baseline (7 days before): ______
Design (from Module 8): cue ______ ; tiny start ______ ; friction removed ______ ;
  temptation hidden ______ ; commitment ______ ; reward ______
If-then plans: action ______ ; obstacle ______ ; restart ______
Target by day 30: ______
PROJECT 2: SOCIAL SKILLS - 10 NEW GENUINE CONNECTIONS
Definition of a "genuine connection" (choose): at least two real conversations,
  names remembered, one follow-up, and a reason to meet again.
Where I'll meet people: ______ ______ ______
Skills I'll use: listening first, follow-ups, names, genuine praise, asking for advice
Weekly target: 2-3 new people; follow up with last week's
PROJECT 3: PERSONAL OPERATING SYSTEM (built during the 30 days)
Morning routine draft: ______  Evening routine draft: ______
Weekly review day/time: ______  12-month plan update by: day 30"""

CONNECTIONS = """CONNECTIONS TRACKER (target: 10 genuine connections)
# | Name | Where met | Conversation 1 (date, what I learned) | Conversation 2 | Name remembered? | Follow-up done? | Reason to meet again
1 | ______ | ______ | ______ | ______ | __ | __ | ______
...
Counts: people met ___ ; second conversations ___ ; follow-ups ___ ; genuine connections ___ /10"""

DAILY = """30-DAY DAILY LOG (both projects; 2 minutes each evening)
Day | Date | Behaviour done? (Y/N or amount) | Metric | Obstacle? | New person met (name) | Follow-up done | Energy (1-5) | Note
1 | ____ | ___ | ___ | ___ | ______ | ___ | _ | ______
...
Weekly summary (Sundays): metric average ___ vs baseline ___ ; connections so far ___ ; one fix ______"""

L1 = lesson(
    36, 1,
    outcome='You can design the three capstone projects (a 30-day behaviour change with tracked data, 10 new genuine connections, and your personal operating system) using the tools from the whole course.',
    split='30 minutes reading, 60 minutes of planning',
    principle='Lasting change comes from applying a few well-supported methods to one behaviour and one social goal at a time, measuring honestly, and building routines that keep running after the course ends.',
    science=f"""
**Why a capstone?** Learning research shows that applying knowledge in a real, integrated task builds skill and transfer far better than reading alone. The capstone pulls together the most strongly supported tools from the course:
- **Goals and feedback** (Module 6): specific, challenging, measured.
- **Design over willpower** (Module 8): cues, friction, hidden temptations, commitment devices, tiny starts.
- **If-then plans** (PD-M08-L03): the best-supported behaviour-change tool in the course.
- **Self-monitoring** (PD-M07-L02): recording progress roughly doubles its effect when it is written or shared.
- **Personal experiments** (PD-M08-L04): baseline first, one change, honest comparison.
- **Exposure and self-efficacy** (Modules 13 and 14): for the social project, many small conversations build confidence.
- **Listening, names, praise and follow-up** (Module 25) and **networking** (PD-M31-L03).
- **Weekly review** (PD-M07-L02) and **self-compassion** after slips (PD-M09-L02).

**Choosing the behaviour.** Pick one behaviour that (a) serves a top value or a 12-month goal, (b) you can do or measure **daily**, (c) is specific ("study 90 minutes before 9 am", "walk 30 minutes", "no phone after 10 pm", "meditate 10 minutes", "speak English for 10 minutes a day"), and (d) has a baseline you can measure for 7 days before you start. Avoid behaviours involving extreme diets or anything unsafe. Thirty days won't make most habits fully automatic (a median of about 66 days, Lally), so the project is the **first stage**; you'll continue after.

**The social-skills project.** "Ten new genuine connections" means ten people with whom you have had at least two real conversations, whose names you remember, whom you followed up with and have a reason to meet again. It is about quality, not collecting contacts. Places: the library, a club, a class, a volunteer group (Module 35), a sports ground, Toastmasters, events, work.

**The personal operating system.** By day 30 you will have tested morning and evening routines, a weekly review rhythm, an updated 12-month plan and a one-page Personal Playbook. "Operating system" just means: the routines and rules that run your days without needing a decision each time.
""",
    evidence=[
        ('Applying knowledge in integrated real tasks improves transfer', 'moderate', 'Supported by learning research on application and projects.'),
        ('If-then plans and self-monitoring for behaviour change', 'strong', 'Large meta-analyses.'),
        ('Environment design (cues and friction)', 'strong', 'Many studies.'),
        ('Repeated conversations build social confidence', 'moderate', 'Supported by exposure and social-skills research.'),
        ('30 days makes a habit automatic', 'mixed', 'Times vary widely (median about 66 days); 30 days is a first stage.'),
    ],
    example="""
Ashiq plans his capstone:

**Project 1 (behaviour):** "Study 90 minutes before 9 am, six days a week." **Value:** independence and steady improvement. **Metric:** minutes studied before 9 am (timer). **Baseline:** 7-day average 34 minutes. **Design:** alarm across the room at 5:50; books open on the desk the night before; phone charging in the hall; tea flask ready (reward); a commitment with his cousin to message "done" by 9 am. **If-then plans:** "If I wake late, I'll still do 30 minutes"; "If guests come, I'll study 6:00–7:00 before they wake." **Target:** average 75 minutes by day 30.

**Project 2 (social):** 10 genuine connections, through the library, Toastmasters (as a guest), a Sunday volunteer group and his cousin's cricket club. He'll use listening first, names (ARLR) and follow-ups.

**Project 3 (operating system):** a morning routine draft (wake, walk, study block), an evening routine (tracker, journal, phone out), Sunday review at 7 pm.

He writes his feared prediction for Project 2 ("People will think I'm strange for following up") and plans to test it.
""",
    apply=f"""
**Plan all three projects (60 minutes):**
{fence(PROJECT_PLAN)}

**Before day 1:**
1. Measure your behaviour **baseline** for 7 days (or use a recent week's data).
2. Set up the environment changes and the commitment.
3. Add the behaviour and "one new conversation" to Loop.
4. Tell one person about both projects and ask them to check in weekly.
5. Run a quick **pre-mortem** (PD-M04-L02): "It's day 30 and both projects failed; why?" Fix the top three risks.

**Choosing well:** if your 12-month plan (Module 7) has a health goal, the behaviour might be exercise or sleep; if it has a PSC goal, the study block; if it has a people goal, consider making the behaviour "one listening-first conversation a day" and pairing it with the connections project.
""",
    resources=[
        ('gollwitzer', 'Re-read the abstract before writing your if-then plans', '5 minutes'),
        ('lally', 'Re-read the interview: what 30 days can and cannot do', '5 minutes'),
        ('klein', 'Use the premortem steps on your capstone plan', '10 minutes'),
    ],
    steps=[
        'Choose your behaviour and write the full Project 1 plan with a 7-day baseline.',
        'Write the Project 2 plan: places, skills and weekly targets.',
        'Draft morning and evening routines and your weekly review time (Project 3).',
        'Run a pre-mortem on all three and fix the top three risks. Tell one person about the projects.',
    ],
    proof='The completed capstone project plan with baseline data, your pre-mortem with fixes and the name of the person you told.',
    templates=[('Capstone project plan', PROJECT_PLAN, '')],
    mistakes=[
        ('Choosing several behaviours.', 'One behaviour for 30 days. Others can come later.'),
        ('No baseline.', 'Without a baseline you can\'t see change honestly.'),
        ('Vague social goals.', 'Define "genuine connection" in advance.'),
        ('Skipping the pre-mortem.', 'Ten minutes now prevents the most common failures.'),
    ],
    quiz=[
        Q('Which behaviour is best for the 30-day project?', '"Study 90 minutes before 9 am, six days a week", measured with a timer', '"Be more productive"', '"Change my whole life"', '"Lose 10 kg in a month"', why='Specific, daily, measurable and safe.'),
        Q('Why measure a 7-day baseline first?', 'To compare honestly and avoid mistaking normal ups and downs for change', 'Because it is traditional', 'To delay starting', 'It is not needed', why='Baseline versus change, as in the personal experiment.'),
        Q('What counts as a "genuine connection" in the social project?', 'At least two real conversations, name remembered, a follow-up and a reason to meet again', 'Any phone number collected', 'A social-media follow', 'One handshake', why='Quality, not collecting contacts.'),
        Q('What does a 30-day project achieve for most habits?', 'A strong first stage; full automaticity often takes longer', 'A permanent habit', 'Nothing', 'Exactly 21 days of benefit', why='Habit formation times vary widely.'),
    ],
    study='read the lesson and re-read your Playbook so far',
    action='plan all three capstone projects with a baseline, a pre-mortem and one person told',
)

L2 = lesson(
    36, 2,
    outcome='You can run both capstone projects for 30 days with a daily log and weekly reviews, adjust when things go wrong, and finish with honest data.',
    split='10 minutes reading, then about 25 to 35 minutes a day for 30 days (the behaviour itself plus logging), and a 20-minute weekly review',
    principle='Thirty days of small daily actions, measured honestly and reviewed weekly, change more than any amount of planning; slips are expected, and the response to a slip decides the result.',
    science=f"""
**What predicts success in 30-day projects.** Across behaviour-change research, the strongest predictors are: **doing it at a consistent time and place** (context stability, PD-M08-L02), **monitoring** (recording every day), **if-then plans for obstacles**, **social support** (someone checking in), and **how you respond to lapses**. Lapses are normal: in Lally's habit study, missing a single day didn't significantly affect habit formation. The danger is the "what-the-hell effect" (described by Janet Polivy and Peter Herman in dieting research): after one slip, people abandon the whole plan. Self-compassion after a slip (PD-M09-L02) and a **restart rule** prevent this.

**Weekly reviews.** Each Sunday (your weekly reflection), compare the week's metric average with your baseline and target, count connections, and make **one change** to the design (not ten). This is the feedback loop that makes the project a learning process rather than a test of willpower.

**Plateaus and dips.** Many people improve quickly in week 1 (novelty), dip in week 2 or 3 (the novelty wears off, life intervenes), and stabilise in week 4. Expect the dip and plan for it; don't read it as failure.

**Social project rhythm.** Meeting 2 or 3 new people a week and following up with the previous week's gives about 10 genuine connections in 30 days. Remember the liking gap (PD-M25-L01): people usually enjoy your follow-up more than you expect. Record the feared predictions you test.

**Measurement honesty.** Use a timer or count, not memory. Record bad days too. At the end, compare averages, not best days, and note other things that changed (exams, illness, festivals). This honesty is what turns your project into real evidence about what works for you.
""",
    evidence=[
        ('Self-monitoring improves behaviour change', 'strong', 'Meta-analysis of 138 studies.'),
        ('Context stability helps habits form', 'moderate', 'Habit research (Wood, Lally).'),
        ('Single lapses don\'t ruin habit formation', 'moderate', 'Lally\'s study.'),
        ('"What-the-hell" abandonment after a slip', 'moderate', 'Dieting research; consistent with self-compassion findings.'),
        ('Week-2 to week-3 dip', 'tool', 'A common pattern in practice; plan for it.'),
    ],
    example="""
Ashiq's 30 days, summarised from his log:

- **Week 1:** study-before-9 average 68 minutes (baseline 34). Met three new people: Divya and Rafeeq at the library, an older man named Mohanan at the Toastmasters guest visit.
- **Week 2:** dip to 52 minutes: two late nights at a cousin's wedding, a cold. He uses his restart rule (30 minutes minimum) and never misses twice. Follows up with Divya and Rafeeq; meets two volunteers at the river clean-up. **One change:** he moves the alarm 15 minutes earlier and goes to bed by 10:30.
- **Week 3:** 74 minutes. Second conversations with four people; Mohanan offers to review his interview answers. Feared prediction "People will think it's strange that I follow up" tested five times: wrong every time.
- **Week 4 (days 22–30):** 81 minutes. Total: 9 genuine connections by his definition, plus three acquaintances.

**Day-30 result:** behaviour average over the 30 days 69 minutes (baseline 34; target 75: close). Connections: 9 of 10. He writes honestly: "Week 2 dip came from late nights; the bedtime change fixed it. Connections came mostly from places I visited regularly."
""",
    apply=f"""
**Every evening (2 minutes):** fill in the daily log.
{fence(DAILY)}

**Every Sunday (part of the weekly reflection, 20 minutes):**
1. Metric average this week versus baseline and target.
2. Connections tracker: new people, second conversations, follow-ups.
3. What got in the way? Which if-then plan worked?
4. **One change** to the design for next week.
5. Update your morning and evening routine drafts based on what actually worked.

{fence(CONNECTIONS)}

**After a slip:** self-compassion break, the restart rule (tiny version tomorrow), and one design fix if the same obstacle repeats. Never miss twice.

**Halfway check (day 15):** if you are far below target, shrink the target rather than quitting; if far above, keep the target and focus on consistency.
""",
    resources=[
        ('loop', 'Use the habit-score and history graphs at each weekly review', '5 minutes'),
        ('selfcomp', 'Re-read the Self-Compassion Break for use after slips', '5 minutes'),
        ('ggia-3gt', 'Optional: add Three Good Things about the project to your journal on hard days', '5 minutes'),
    ],
    steps=[
        'Run both projects for 30 days, filling in the daily log every evening.',
        'Do four weekly reviews (Sundays), each with one design change.',
        'Keep the connections tracker up to date and follow up with every new person within a week.',
        'On day 30, calculate your metric average (compared with baseline and target) and count your genuine connections.',
    ],
    proof='The 30-day daily log, four weekly reviews with design changes, the connections tracker and your day-30 numbers.',
    templates=[('Connections tracker', CONNECTIONS, '')],
    mistakes=[
        ('Abandoning the plan after a bad day.', 'Expect slips; use the restart rule and never miss twice.'),
        ('Changing many things at once in a weekly review.', 'One change a week, so you can see what helps.'),
        ('Counting contacts instead of connections.', 'Second conversations and follow-ups are what count.'),
        ('Reporting only your best days.', 'Averages and honest notes make the data useful.'),
    ],
    quiz=[
        Q('What is the "what-the-hell effect"?', 'Abandoning a whole plan after one slip', 'Feeling excited at the start', 'A type of reward', 'Doing too much in week 1', why='Polivy and Herman\'s observation; prevented by self-compassion and restart rules.'),
        Q('How many design changes should you make at each weekly review?', 'One', 'Ten', 'None ever', 'Change everything', why='One change at a time shows what works.'),
        Q('What should you do if you are far below target at day 15?', 'Shrink the target and keep going', 'Quit', 'Double the effort for one day', 'Restart from day 1', why='Consistency matters more than the original target.'),
        Q('What makes your day-30 result trustworthy?', 'Daily measured data, averages compared with baseline, and honest notes about other changes', 'Remembering your best days', 'How you feel on day 30', 'What friends think', why='Honest measurement turns the project into evidence.'),
    ],
    study='read the lesson and set up the daily log and connections tracker',
    action='run both capstone projects for 30 days with daily logs and four weekly reviews',
    extra_tasks=[
        ('week1', 'Capstone week 1: daily log complete, weekly review with one change', a2, None),
        ('week2', 'Capstone week 2: daily log complete, weekly review with one change', a2 + 1, None),
        ('week3', 'Capstone week 3: daily log complete, weekly review with one change; day-15 halfway check', a2 + 2, None),
        ('week4', 'Capstone week 4: daily log complete, weekly review with one change', a2 + 3, None),
    ],
)

pb_rows = []
for m, line in PLAYBOOK:
    pb_rows.append(f'- **M{m:02d}:** {line}')
PB_LIST = '\n'.join(pb_rows)

L3 = lesson(
    36, 3,
    outcome='You can finish your personal operating system: morning and evening routines, a weekly review, a 12-month growth plan and a one-page Personal Playbook, and you know how to keep them running.',
    split='20 minutes reading, 90 minutes of writing and review (plus the final retest on its own page)',
    principle='A personal operating system is a small set of routines and rules you actually follow, written on one page and reviewed regularly; it keeps the course\'s gains alive long after the course ends.',
    science=f"""
**Why routines and a one-page summary?** Two findings from the course explain the design:
1. **Decisions are costly; routines are cheap.** Behaviours tied to stable cues and contexts become automatic and need little effort (habit research, Module 8). Morning and evening routines anchor your most important habits to fixed points in the day.
2. **What you review, you keep.** Monitoring and regular review improve goal attainment (PD-M07-L02). A one-page Playbook you read on the 1st of every month keeps your best rules in mind; a 50-page notebook you never open does not.

**The final retest.** Repeat every baseline test on the **Final retest and checklist** page (form B of the thinking-traps quiz). Compare start and end honestly, including things that didn't change. Remember regression to the mean and other life changes (PD-M02-L01): your numbers are evidence about your life, not a controlled experiment.

**Your Personal Playbook.** Over 35 modules you added lines to your Playbook note. They are listed below, collected from every module. Your job now is to **edit them into one page**: keep the 15 to 25 rules and routines you actually use, write them in your own words, and organise them under the template's headings. Delete what you don't use; a shorter Playbook you follow beats a long one you don't.

**The 12-month growth plan.** Update the plan from Module 7 using what you learned about yourself: your capacity (planned versus actual hours), your best habits and your values. Keep it to three goals with quarterly milestones and a "not this year" list.

**All the Playbook lines you added during the course:**

{PB_LIST}
""",
    evidence=[
        ('Routines tied to stable cues become automatic', 'strong', 'Habit research.'),
        ('Regular review and monitoring improve goal attainment', 'strong', 'Meta-analysis of 138 studies.'),
        ('A one-page Playbook', 'tool', 'A practical summary tool; judge it by whether you use it.'),
    ],
    example="""
Sreeja's one-page Playbook, after editing 80 lines down to 22:

- **Who I am:** values: learning, fairness, family, independence, kindness. Strengths: love of learning, kindness, fairness. "I'm becoming someone who shows up every day, even for five minutes."
- **How I think:** top traps: mind reading, planning fallacy, catastrophising. Counter-moves: "I don't know what they think until I ask"; plan from my last three weeks; "most likely, not worst".
- **My day:** morning (5:45 wake, walk, 10-minute meditation, 90-minute study block); evening (tracker, three good things, phone in the hall by 10, lights out 10:30).
- **Hard moments:** slow breathing; thought record if over 60; Tele-MANAS 14416 if two weeks low.
- **Body:** strength A/B three times a week; walk daily; half-plate vegetables; protein at every meal.
- **People:** listen first, two follow-ups, names, specific praise; my no-script; SBI for feedback; influence code (true, mutual, easy no).
- **Red flags:** urgency, secrecy, fake authority, too good to be true. Money: never the same day; 1930.
- **Where I'm going:** PSC mock average 72 by June; 10 genuine connections a year; teach weekend English.

She reads it aloud on the 1st of each month and records it on her phone.
""",
    apply=f"""
**Finish your personal operating system (90 minutes):**
1. **Morning routine:** write the version you actually followed during the capstone, with times.
2. **Evening routine:** the same.
3. **Weekly review:** day, time and the template you will use (the weekly reflection plus plan).
4. **12-month growth plan:** three goals with quarterly milestones, from your updated Module 7 plan.
5. **Personal Playbook:** edit all your Playbook lines (listed above) into one page using the template.

{fence(tools.MORNING_ROUTINE)}

{fence(tools.EVENING_ROUTINE)}

{fence(tools.PLAYBOOK_TEMPLATE)}

**Keep it running:** read the Playbook on the 1st of every month; review the 12-month plan every 3 months; retest fitness and self-ratings every 3 months; do one new 30-day challenge a year (see **What next**).
""",
    resources=[
        ('franklin', 'Re-read Franklin\'s daily "scheme of employment", an 18th-century operating system, and compare it with yours', '10 minutes'),
        ('meditations', 'Read a few paragraphs from any book of Meditations: Marcus Aurelius\'s own playbook, written to himself', '15 minutes'),
        ('loop', 'Export or screenshot your habit history for the whole course', '5 minutes'),
    ],
    steps=[
        'Complete the final retest on the Final retest and checklist page and compare start and end.',
        'Write your final morning and evening routines and weekly review time.',
        'Update your 12-month growth plan.',
        'Edit your Playbook lines into a one-page Personal Playbook using the template, then read it aloud and record it.',
    ],
    proof='Your final retest comparison, routines, weekly review time, updated 12-month plan, one-page Personal Playbook and its recording file name.',
    templates=[('Personal Playbook (one page)', tools.PLAYBOOK_TEMPLATE, '')],
    mistakes=[
        ('Keeping every line.', 'Edit hard. One page you follow beats ten pages you don\'t.'),
        ('Writing routines you have never actually done.', 'Write what worked during the capstone, then improve.'),
        ('Treating the end of the course as the end.', 'Monthly Playbook reading and quarterly retests keep it alive.'),
        ('Judging yourself only by the retest numbers.', 'Habits, relationships and skills you now have matter more than any single score.'),
    ],
    quiz=[
        Q('Why keep the Personal Playbook to one page?', 'A short page you review monthly is more likely to be used than a long notebook', 'Because paper is expensive', 'Because longer is always worse', 'It must fit in a wallet by law', why='What you review, you keep.'),
        Q('Which routine should you write for your operating system?', 'The version you actually followed during the capstone, then improve it', 'An ideal routine from social media', 'A routine with no times', 'Someone else\'s routine', why='Start from what works for you.'),
        Q('How often should you read your Playbook?', 'Monthly, for example on the 1st of each month', 'Once, at the end of the course', 'Every hour', 'Never again', why='Regular review keeps it in mind.'),
        Q('How should you interpret your final retest?', 'As honest evidence about your life, noting other changes and regression to the mean', 'As proof the course caused every change', 'As meaningless', 'Only by the best score', why='Measure honestly, interpret carefully.'),
    ],
    study='read the lesson and all your Playbook lines',
    action='complete the final retest, write your routines and 12-month plan, and edit your one-page Personal Playbook',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    36,
    overview=f"""
The capstone: a 30-day behaviour-change project with tracked data, a social-skills project (10 new genuine connections), and your personal operating system: morning and evening routines, a weekly review, a 12-month growth plan and a one-page Personal Playbook. Finish with the final retest.

This is where the course comes together. You choose one behaviour and one social goal, apply the best-supported tools from all five parts, measure honestly for 30 days, and turn what worked into routines and a one-page Playbook you will keep using.

The 30 days need real calendar days, at either pace. Plan them for a month without a major exam or family event if you can; if that's impossible, shrink the targets, don't skip the project.
""",
    outcomes=[
        'Design a 30-day behaviour-change project with a baseline, design, if-then plans and a metric.',
        'Build 10 new genuine connections using the Part D skills.',
        'Run both projects with daily logs and weekly reviews, and handle slips well.',
        'Write morning and evening routines, a weekly review rhythm and a 12-month growth plan.',
        'Edit your Playbook into one page and complete the final retest.',
    ],
    lessons=LESSONS,
    project='your personal operating system and one-page Personal Playbook',
    project_steps=[
        'Plan the capstone projects (PD-M36-L01).',
        'Run them for 30 days with logs and weekly reviews (PD-M36-L02).',
        'Write a one-page capstone report: behaviour baseline, average and target; connections made; what worked; what didn\'t; what you will keep.',
        'Finish your operating system and one-page Personal Playbook (PD-M36-L03), and complete the final retest.',
    ],
    project_proof='The capstone report, the 30-day logs, the connections tracker, your routines, 12-month plan and one-page Personal Playbook.',
    rubric=[
        ('Behaviour project', 'No baseline or data', 'Data for part of the month', '30 days of data with baseline comparison and honest notes'),
        ('Social project', 'Fewer than four connections', 'Four to seven', 'Eight to ten genuine connections with follow-ups'),
        ('Operating system', 'Not written', 'Routines only', 'Routines, weekly review, 12-month plan and one-page Playbook'),
        ('Reflection', 'Only results', 'Results with some lessons', 'Clear lessons about what works for you and a plan to keep it'),
    ],
    short=[
        'Do a 14-day version of the behaviour project and aim for five genuine connections.',
        'Write a half-page Playbook with your ten most-used rules.',
    ],
    flashcards=[
        ('Three capstone projects', '30-day behaviour change; 10 genuine connections; personal operating system.'),
        ('Genuine connection (course definition)', 'Two real conversations, name remembered, a follow-up, a reason to meet again.'),
        ('Before day 1', 'Baseline, environment changes, commitment, tell someone, pre-mortem.'),
        ('After a slip', 'Self-compassion break, restart with the tiny version, never miss twice.'),
        ('Weekly review rule', 'One design change a week.'),
        ('Personal operating system', 'Routines and rules that run your days without fresh decisions.'),
        ('Playbook review', 'Read it on the 1st of every month.'),
    ],
    mistakes=[
        ('Starting the capstone in a festival or exam month without adjusting.', 'Shrink targets or shift dates; don\'t skip it.'),
        ('Doing the projects without the daily log.', 'The log is the project\'s evidence and feedback.'),
        ('A Playbook full of other people\'s quotes.', 'Your own rules, in your own words, from your own data.'),
    ],
    tools=[
        'The capstone project plan (PD-M36-L01).',
        'The 30-day daily log and connections tracker (PD-M36-L02).',
        'Morning and evening routines and the one-page Personal Playbook template (PD-M36-L03).',
    ],
    playbook=[
        'My operating system: morning routine ______, evening routine ______, Sunday review at ______, Playbook on the 1st of each month.',
    ],
)
