from common import lesson, module, link, xref, table, Q
import tools

L1 = lesson(
    7, 1,
    outcome='You can write a short life vision from your values and turn it into a 12-month plan with no more than three goals and quarterly milestones.',
    split='20 minutes reading, 40 minutes of planning',
    principle='A vision says where you are heading and why; a 12-month plan turns it into a few concrete goals with milestones, so daily choices line up with what you care about.',
    science=f"""
**Why imagine the future at all?** Two lines of research matter here.

1. **"Best possible self" writing.** Laura King and later researchers asked people to write for about 15 to 20 minutes, on several days, about their life in the future if everything went as well as it reasonably could. Studies and a 2019 meta-analysis of positive-psychology interventions found small to moderate increases in optimism and wellbeing. It is one of the better-supported positive-psychology exercises, though effects are modest and short-lived without follow-up.

2. **Mental contrasting.** Gabriele Oettingen's research found that just fantasising about a positive future can *reduce* effort, because the mind enjoys the fantasy as if it were achieved. What works better is **mental contrasting**: imagine the desired future, then imagine the main obstacle inside you or your situation, then plan for it. Combined with if-then plans (PD-M08-L03), this method is called **WOOP**: Wish, Outcome, Obstacle, Plan. Several trials found WOOP improved behaviours such as exercise, healthy eating and study effort, with small to moderate effects.

**Life design.** Stanford designers Bill Burnett and Dave Evans adapted design thinking to life choices in their course and book *Designing Your Life*: try small **prototypes** (a conversation with someone in a career, a one-week trial) before big commitments. The approach is practical rather than scientifically tested as a package, but it fits decision research: reversible small tests teach you more, more cheaply, than imagining (PD-M04-L01).

**Why only three goals?** Attention and time are limited. Goal research (PD-M06-L02) shows that competing goals reduce progress on each. For someone preparing for PSC exams, one major goal (the exam) plus one health goal plus one relationship or skill goal is plenty.
""",
    evidence=[
        ('Best-possible-self writing raises optimism and wellbeing', 'moderate', 'Supported by several trials and meta-analyses; effects are small to moderate and fade without practice.'),
        ('Positive fantasy alone can reduce effort', 'moderate', 'Found in several studies by Oettingen and colleagues.'),
        ('Mental contrasting with implementation intentions (WOOP)', 'moderate', 'Trials show small to moderate improvements in health and study behaviours.'),
        ('Life-design prototyping', 'tool', 'A practical method consistent with decision research; not tested as a package.'),
    ],
    example=f"""
Sreeja writes her best possible self, one year from now: "I am on the LGS rank list or at least on a short list, studying calmly with a routine. I walk every morning and sleep by 10:30. I have two close friends I meet each week, and I am teaching my neighbour's daughter English on Saturdays. I feel steady, not frantic."

Then she does WOOP for the biggest wish (rank list). **Obstacle:** "When I get anxious after a bad mock, I stop studying for days." **Plan:** "If I score badly in a mock, then the same evening I will log three errors and study one of them for 20 minutes."

Her 12-month plan has three goals: (1) PSC: a mock average of 70 by June; (2) health: walk five days a week and sleep by 10:30; (3) people: one weekly friend meeting and the Saturday class. Each gets four quarterly milestones. Ideas she cut for this year: learning guitar, starting a YouTube channel. She writes them on a "not this year" list so they stop nagging her.
""",
    apply=f"""
**Build your vision and 12-month plan (about 40 minutes):**

1. **Best possible self (15 minutes):** write freely about a realistic best version of your life in 12 months, across your life-wheel areas. Use your values from PD-M05-L01.
2. **Pick three goals:** the three that matter most and fit together. One of them will usually be PSC or work.
3. **WOOP each one:** Wish, best Outcome, main inner Obstacle, if-then Plan.
4. **Quarterly milestones:** for each goal, what will be true at 3, 6, 9 and 12 months?
5. **"Not this year" list:** write the good ideas you are deliberately postponing.
6. **First prototype:** for any big uncertain goal (a career change, a business), plan one small test this month: a conversation, a one-week trial, a small paid job.

**With others:** share your three goals with one person who cares about you. Ask for support with one obstacle, not for advice on everything.
""",
    resources=[
        ('ggia', 'Search for the "Best Possible Self" practice and follow its instructions', '20 minutes'),
        ('smiles', 'Read chapter 1, "Self-Help: National and Individual" (a public-domain classic on effort and character; notice what is timeless and what is dated)', '25 minutes'),
        ('allen', 'Read the short opening chapter "Thought and Character"; compare its claims with what you know about evidence', '10 minutes'),
    ],
    steps=[
        'Write your best-possible-self text (15 minutes).',
        'Choose three goals and write WOOP for each.',
        'Write quarterly milestones for each goal and a "not this year" list.',
        'Plan one prototype (a test) for your most uncertain goal and put it in your calendar this month.',
        'Share the three goals with one person and note their response.',
    ],
    proof='Your best-possible-self text, three WOOPs, the 12-month plan with milestones, the "not this year" list and the prototype date.',
    templates=[('12-month plan with WOOP', """12-MONTH PLAN               From ______ to ______
Vision (3 lines, from my best-possible-self writing):
____________________________________________________________
GOAL 1: ______________________  Value it serves: ______
  WOOP: Wish ______ | Outcome ______ | Obstacle (inner) ______
        Plan: If ______, then I will ______.
  Milestones: 3 mo ______ 6 mo ______ 9 mo ______ 12 mo ______
GOAL 2: (same)
GOAL 3: (same)
NOT THIS YEAR: ______ ______ ______
PROTOTYPE this month: ______________________ on ______
Shared with: ______  Their support for one obstacle: ______""", '')],
    mistakes=[
        ('Writing a fantasy and stopping.', 'Positive fantasy alone can lower effort. Always add the obstacle and a plan (WOOP).'),
        ('More than three goals.', 'Put the rest on the "not this year" list.'),
        ('Picking obstacles outside you.', 'Name the inner obstacle you can plan for ("I scroll when anxious"), not just "not enough time".'),
        ('Treating old self-help classics as science.', 'Books like As a Man Thinketh inspire, but claims such as "thought alone shapes circumstance" overstate what research supports.'),
    ],
    quiz=[
        Q('What did Oettingen\'s research find about positive fantasies alone?', 'They can reduce effort, because the mind enjoys the fantasy', 'They always increase effort', 'They have no effect on anything', 'They work only for athletes', why='Contrasting the wish with an obstacle works better than fantasy alone.'),
        Q('What does WOOP stand for?', 'Wish, Outcome, Obstacle, Plan', 'Work, Order, Organise, Practise', 'Will, Optimism, Opportunity, Progress', 'Want, Obtain, Own, Profit', why='Mental contrasting plus an if-then plan.'),
        Q('Why limit your 12-month plan to about three goals?', 'Competing goals split limited time and attention', 'Three is a lucky number', 'Research proves exactly three is best', 'More goals are always better', why='Goal research shows competing goals reduce progress on each.'),
        Q('What is a life-design "prototype"?', 'A small, cheap test of an option before a big commitment', 'A detailed five-year plan', 'A personality test', 'A vision board', why='Small reversible tests teach you about an option quickly.'),
    ],
    study='read the lesson and do the Best Possible Self practice',
    action='write your vision, three WOOPs and a 12-month plan with milestones, and schedule one prototype',
)

L2 = lesson(
    7, 2,
    outcome='You can plan a week from your 12-month goals and run a 20-minute weekly review that keeps your plan alive.',
    split='15 minutes reading, 40 minutes of planning and review',
    principle='Plans die without a regular review; a short weekly plan and review connect your big goals to next week\'s calendar and let you adjust before small slips become big failures.',
    science=f"""
**Why weekly?** A year is too long to steer by, and a day is too short to see patterns. A week contains a full cycle of work, rest and family life, so it is the natural unit for planning and review.

**What the research supports:**

- **Monitoring progress helps.** A 2016 meta-analysis by Benjamin Harkin and colleagues of 138 studies found that prompting people to monitor their progress towards goals increased goal attainment, and more so when progress was recorded physically or reported to others.
- **Planning when and where** (implementation intentions) roughly doubles follow-through in many studies; the {link('gollwitzer', 'Gollwitzer and Sheeran meta-analysis')} found a medium-to-large average effect (d = 0.65) across 94 tests. You will use these in PD-M08-L03; your weekly plan is where you write them.
- **Reflection improves learning from experience.** Studies of workers who spent a few minutes at the end of the day reflecting on what they learned (Di Stefano, Gino, Pisano and Staats) found better performance than those who simply worked longer. The evidence is promising but limited.

**Time blocking and the "big rocks" idea.** Putting your most important tasks in the calendar first, before smaller ones, is a practical rule from time-management writers (often illustrated with rocks, pebbles and sand in a jar). There is little direct research on it, but it follows from implementation intentions and the planning fallacy: if the important thing has no time slot, it usually loses to urgent small things.

**Your weekly reflection** (the template on the Daily system track) is already a review. This lesson adds the **planning** half and connects both to your 12-month plan.
""",
    evidence=[
        ('Monitoring and recording progress improves goal attainment', 'strong', 'Meta-analysis of 138 studies; stronger when progress is recorded or shared.'),
        ('Planning when and where (implementation intentions)', 'strong', 'Medium-to-large average effects across many studies.'),
        ('Brief reflection on lessons learned improves performance', 'mixed', 'A few promising studies; not yet widely replicated.'),
        ('Time-blocking the most important tasks first', 'tool', 'A practical rule consistent with planning research.'),
    ],
    example=f"""
Every Sunday at 7 pm, after dinner, Ashiq spends 20 minutes on his weekly reflection and plan.

**Review (10 minutes):** habit tracker 71%; PSC study 9 hours (plan was 12); walks 3 of 5; one great conversation with his cousin about her nursing job. What went badly: Wednesday and Thursday he lost both evening blocks to helping at his uncle's shop. Lesson: weekday evenings are fragile.

**Plan (10 minutes):** he looks at his 12-month plan, then puts the big rocks in his phone calendar first: three morning study blocks of 90 minutes (6:30–8:00), Saturday mock at 10, walks at 6 am, the Sunday reflection. Only then does he add the shop help, a cousin's engagement and two errands. He writes one if-then plan for the fragile evenings: "If I'm asked to help at the shop on a study evening, then I'll offer Saturday afternoon instead."
""",
    apply=f"""
**The 20-minute weekly review and plan (Sunday, same time each week):**

**Review (10 minutes):** fill in the Weekly reflection template (on the Daily system track page). Add one line: "Am I on track for this quarter's milestones? Yes / behind / ahead."

**Plan (10 minutes):**
1. Look at your 12-month plan and this quarter's milestones.
2. Choose **three priorities** for the week, one per goal if possible.
3. **Block the big rocks first** in your calendar: study blocks, workouts, the people goal.
4. Add fixed commitments and errands around them.
5. Write **one if-then plan** for the biggest risk to the week.
6. Check the total: is it realistic? Use your past weeks' numbers (the outside view).

**Monthly (first Sunday):** reread your 12-month plan and Personal Playbook; adjust milestones if life has changed.

**With others:** share your week's plan with family if their help or understanding matters ("Mornings 6:30 to 8 are my study time this week").
""",
    resources=[
        ('gollwitzer', 'Read the abstract: how big the effect of if-then planning is', '5 minutes'),
        ('franklin', 'Read the passage on Franklin\'s daily "Scheme of Employment" (search the text for "scheme of employment") and compare it with your plan', '10 minutes'),
        ('wellbeing', 'Optional: set a weekly reminder in your phone or Loop for the Sunday review', '5 minutes'),
    ],
    steps=[
        'Choose a fixed time each Sunday for the 20-minute review and plan, and set a reminder.',
        'Do the review and plan this Sunday using both halves of the routine.',
        'Put your three priorities and big rocks into your phone calendar (or a paper week planner) before anything else.',
        'Next Sunday, compare planned and actual hours and write one change.',
    ],
    proof='Two consecutive weekly reviews and plans, with a calendar screenshot showing the big rocks, and your planned-versus-actual numbers.',
    templates=[('Weekly plan (with the weekly reflection)', tools.WEEKLY_REFLECTION + """

WEEKLY PLAN (after the reflection)
Quarter milestones: Goal 1 ______ Goal 2 ______ Goal 3 ______  On track? Y / behind / ahead
Three priorities this week: 1 ______ 2 ______ 3 ______
Big rocks blocked first (day, time): ______________________________
Biggest risk this week: ______ -> If ______, then I will ______.
Planned study hours ___ (last 3 weeks' average ___). Realistic? Y/N""", '')],
    mistakes=[
        ('Skipping the review when the week went badly.', 'Bad weeks are when the review matters most. Do the short version: numbers, one lesson, three priorities.'),
        ('Planning more hours than you have ever done.', 'Use your average of the last three weeks plus a little.'),
        ('Filling the calendar with small tasks first.', 'Big rocks first; errands fit around them.'),
        ('Making the review a punishment.', 'Write it as you would for a friend: honest, kind, focused on the next step.'),
    ],
    quiz=[
        Q('What did a meta-analysis of 138 studies find about monitoring goal progress?', 'It increased goal attainment, especially when recorded or shared', 'It had no effect', 'It reduced motivation', 'It only works for weight loss', why='Harkin et al. (2016) found monitoring helps, more so when made physical or public.'),
        Q('What does "big rocks first" mean in weekly planning?', 'Put the most important tasks in the calendar before smaller ones', 'Do the hardest physical work first', 'Plan only big projects', 'Ignore small tasks', why='If important tasks have no slot, urgent small things take over.'),
        Q('How should you set this week\'s planned study hours?', 'Start from your recent actual average and add a little', 'Plan the maximum possible', 'Double last week', 'Do not plan hours', why='The outside view protects against the planning fallacy.'),
        Q('Why is a week a good unit for review?', 'It contains a full cycle of work, rest and family life, so patterns show', 'Because research proves seven days is magic', 'Because months are too short', 'It is not a good unit', why='Days are too short and years too long to steer by.'),
    ],
    study='read the lesson and set your review time',
    action='do two consecutive Sunday reviews and plans, with big rocks blocked first in your calendar',
)

LESSONS = [L1, L2]

MODULE = module(
    7,
    overview=f"""
Turn values into direction: a short life vision, a 12-month plan with no more than three goals, WOOP for obstacles, small life-design prototypes, and a 20-minute weekly review and plan. This becomes the spine of your personal operating system.

Modules 5 and 6 gave you values, strengths and a working understanding of motivation. This module turns them into a plan you will actually follow: a one-page 12-month plan that you revisit monthly, and a weekly rhythm that connects it to your calendar.

If you did the Learning Capabilities course, its {xref('lrn', 'lrn-m07', 'weekly learning review')} covers study-specific reviews; here the review covers your whole life, and you can merge the two into one Sunday session.
""",
    outcomes=[
        'Write a best-possible-self vision grounded in your values.',
        'Use WOOP (mental contrasting with an if-then plan) on each goal.',
        'Write a 12-month plan with three goals, quarterly milestones and a "not this year" list.',
        'Run a 20-minute weekly review and plan, blocking big rocks first.',
    ],
    lessons=LESSONS,
    project='your 12-month plan (version 1) and four weekly reviews',
    project_steps=[
        'Finish your 12-month plan with WOOPs and milestones (PD-M07-L01).',
        'Run the weekly review and plan for four consecutive Sundays (PD-M07-L02); this continues the Daily system track.',
        'After four weeks, compare planned and actual hours each week and write what you learned about your realistic capacity.',
        'Update the plan (version 2) if needed.',
    ],
    project_proof='The 12-month plan, four weekly plans with planned-versus-actual numbers, and your capacity note.',
    rubric=[
        ('Vision', 'No vision written', 'Vision written but vague', 'Vision rooted in values, across life areas'),
        ('Goals', 'More than three or vague', 'Three goals without milestones', 'Three goals with WOOP and quarterly milestones'),
        ('Weekly rhythm', 'Fewer than two reviews', 'Two or three reviews', 'Four consecutive reviews with plans'),
        ('Realism', 'Plans far above actual', 'Some adjustment', 'Plans match actual capacity within about 20%'),
    ],
    short=[
        'Write three goals with one WOOP each.',
        'Do a 10-minute version of the weekly review: numbers, one lesson, three priorities.',
    ],
    flashcards=[
        ('Best possible self', 'Writing about a realistic best future; small to moderate wellbeing and optimism gains.'),
        ('Positive fantasy alone', 'Can reduce effort; add obstacles and plans.'),
        ('WOOP', 'Wish, Outcome, Obstacle, Plan (if-then).'),
        ('Why only three goals?', 'Competing goals split attention and reduce progress.'),
        ('Life-design prototype', 'A small test (conversation, short trial) before a big commitment.'),
        ('Monitoring progress', 'Meta-analysis: improves goal attainment, more when recorded or shared.'),
        ('Big rocks first', 'Block the most important tasks in the calendar before small ones.'),
    ],
    mistakes=[
        ('A beautiful plan never looked at again.', 'The weekly review is what keeps it alive.'),
        ('Rigid plans that ignore family life in Kerala.', 'Weddings, festivals and hospital visits happen. Plan buffer time and adjust weekly.'),
        ('Comparing your plan with other people\'s.', 'Your plan serves your values and capacity.'),
    ],
    tools=[
        'The 12-month plan with WOOP and "not this year" list (PD-M07-L01).',
        'The weekly plan added to the weekly reflection (PD-M07-L02).',
    ],
    playbook=[
        'My three goals for this year: ______ (with WOOP plans).',
        'Every Sunday at ______: 10-minute review, 10-minute plan, big rocks first.',
    ],
)
