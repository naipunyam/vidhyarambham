from common import lesson, module, link, xref, table, Q

L1 = lesson(
    6, 1,
    outcome='You can explain self-determination theory, tell intrinsic from extrinsic motivation, and redesign one task so it meets your needs for autonomy, competence and relatedness.',
    split='20 minutes reading, 30 minutes of tasks',
    principle='People are most motivated, and stay motivated longest, when they feel choice (autonomy), growing skill (competence) and connection (relatedness); rewards help some tasks but can crowd out interest in others.',
    science=f"""
**Self-determination theory (SDT)** was developed by Edward Deci and Richard Ryan from the 1970s onwards and is one of the most researched theories of motivation ({link('sdt', 'Center for Self-Determination Theory')}). It says people have three basic psychological needs:

- **Autonomy:** feeling that what you do is your own choice, in line with your values (not necessarily doing it alone).
- **Competence:** feeling effective and able to grow.
- **Relatedness:** feeling connected to and cared for by others.

When these needs are supported, people show more lasting motivation, better performance on complex tasks and better wellbeing. When they are thwarted (constant control, repeated failure without help, isolation), motivation drops or becomes grudging.

**Intrinsic and extrinsic motivation.** Intrinsic motivation means doing something because it is interesting or enjoyable in itself. Extrinsic motivation means doing it for an outcome outside the activity: money, marks, praise, avoiding punishment. SDT adds an important idea: extrinsic motivation comes in **degrees**. At one end is doing something only because you are forced or to avoid guilt (controlled). At the other end is doing something because you have made its purpose your own: you may not enjoy revising Indian history, but you value the job it can lead to and the family security it brings (identified or integrated). This "owned" extrinsic motivation works almost as well as intrinsic motivation for persistence.

**Can rewards backfire?** In Deci's early experiments, people paid to solve interesting puzzles later spent less free time on them than unpaid people. A large 1999 review by Deci, Koestner and Ryan concluded that expected, tangible rewards for an interesting task tend to reduce intrinsic motivation. Other researchers (Cameron and Pierce) argued the effect is smaller and limited to specific conditions. A balanced reading: rewards work well for dull tasks and for getting started; for tasks you already enjoy, heavy controlling rewards can make them feel like work. Positive, informative feedback ("your answers on Polity improved") tends to increase motivation.

**Motivation in India and Kerala.** SDT research has been done in many cultures, including collectivist ones. Autonomy does not mean ignoring family: you can feel autonomous when you willingly accept a family goal because you share its value. Feeling *forced* into a goal is what drains motivation.
""",
    evidence=[
        ('Supporting autonomy, competence and relatedness increases lasting motivation', 'strong', 'Many studies in schools, workplaces, health and sport, in many countries.'),
        ('"Owned" (identified) extrinsic motivation predicts persistence', 'strong', 'Consistent across SDT studies.'),
        ('Expected tangible rewards reduce intrinsic motivation for interesting tasks', 'moderate', 'Supported by a large review; debated in size and conditions.'),
        ('Informative positive feedback increases motivation', 'moderate', 'Supported in many studies.'),
    ],
    example=f"""
Anu finds PSC study a grind. She does it because her mother keeps asking about it and because she feels guilty when cousins get jobs. Using SDT, she redesigns her week:

- **Autonomy:** instead of following a coaching centre's timetable, she chooses her own order of topics within the syllabus and writes down *her* reason: "A government job gives me independence and lets me support Amma." The study did not change; the ownership did.
- **Competence:** she starts each session with five questions she can answer and ends with a quick score. Seeing her Polity score rise from 11/20 to 15/20 in three weeks makes her want to continue.
- **Relatedness:** she joins two friends on a Sunday call where each explains one topic.

She also stops promising herself a new dress for every mock above 60%, since the rewards were making the mocks feel like bribed work, and keeps a simple progress graph instead.
""",
    apply=f"""
**The SDT redesign (for any task you avoid):**

| Need | Ask | Changes to try |
| --- | --- | --- |
| Autonomy | "Where do I have choice? What is my own reason?" | Choose the order, time or method; write your own "why" in one line. |
| Competence | "Can I see myself improving?" | Start with a win; track a simple score; make tasks the right difficulty. |
| Relatedness | "Who is in this with me?" | A study partner, a weekly call, telling someone your progress. |

**On rewards:** use small rewards to start dull tasks (tea after the first 25 minutes), but for things you want to love, rely on progress and meaning instead of bribes.

**With others:** if you lead, teach or parent, support others' needs: give choices ("Would you rather start with maths or GK?"), give informative feedback rather than only praise or criticism, and show you care about the person, not just the result. Controlling pressure ("You must, or else") works short-term and backfires long-term.
""",
    resources=[
        ('sdt', 'Read the overview of the theory: the three needs and the types of motivation', '15 minutes'),
        ('os-10', 'Read 10.1 Motivation (intrinsic and extrinsic motivation, theories of motivation)', '20 minutes'),
        ('noba', 'Search for the module "Motives and Goals" and read the introduction', '15 minutes'),
    ],
    steps=[
        'Pick the one task you most avoid (a PSC subject, exercise, a household duty).',
        'Rate it 1–5 on autonomy, competence and relatedness right now.',
        'Write one change for each need, using the table, and do all three this week.',
        'At the end of the week, rate the three needs again and write how many times you did the task compared with the week before.',
    ],
    proof='Before and after ratings for the three needs, your three changes, and the task count for both weeks.',
    templates=[('SDT redesign sheet', """SDT REDESIGN                Task I avoid: ________________________
                   Before (1-5)   Change I'll make                    After (1-5)
Autonomy           ___            ______________________________      ___
Competence         ___            ______________________________      ___
Relatedness        ___            ______________________________      ___
My own reason for doing this (one line): ______________________________
Times I did the task: last week ___  this week ___""", '')],
    mistakes=[
        ('Waiting to "feel motivated".', 'Motivation often follows action and visible progress. Start small and let competence grow.'),
        ('Thinking autonomy means doing everything alone.', 'You can choose to accept help or a family goal; what matters is that it is your choice.'),
        ('Bribing yourself for everything.', 'Use rewards to start dull tasks; use progress and meaning for lasting interest.'),
    ],
    quiz=[
        Q('What are the three basic needs in self-determination theory?', 'Autonomy, competence and relatedness', 'Food, money and status', 'Discipline, rewards and punishment', 'Intelligence, effort and luck', why='Deci and Ryan\'s three basic psychological needs.'),
        Q('You study history because you value the job it leads to, though you don\'t enjoy it. What kind of motivation is this?', 'Owned (identified) extrinsic motivation', 'Pure intrinsic motivation', 'Controlled motivation', 'No motivation', why='The outcome is external, but you have made its purpose your own.'),
        Q('According to the 1999 review, when can rewards reduce motivation?', 'When expected, tangible rewards are given for an already interesting task', 'Always', 'Never', 'Only for children', why='Rewards can crowd out interest in tasks people already enjoy; the size is debated.'),
        Q('Which is the most motivating feedback?', '"Your Polity score went from 11 to 15; your errors are now mostly about dates"', '"Good job"', '"You must do better"', '"Others are doing better than you"', why='Informative feedback supports competence.'),
    ],
    study='read the lesson and the SDT overview',
    action='redesign your most-avoided task for autonomy, competence and relatedness and compare one week before and after',
)

L2 = lesson(
    6, 2,
    outcome='You can set specific, challenging goals with feedback, break them into progress steps, and use a daily progress note.',
    split='20 minutes reading, 30 minutes of tasks',
    principle='Specific, challenging goals with feedback beat "do your best"; and on ordinary days, seeing small progress in meaningful work is one of the strongest boosts to motivation.',
    science=f"""
**Goal-setting theory.** Edwin Locke and Gary Latham summarised about 35 years of research (more than 400 studies) in 2002: **specific, difficult goals** lead to better performance than easy goals or vague "do your best" goals, as long as the person is committed, has the ability and gets **feedback** on progress. Goals work by directing attention, increasing effort, increasing persistence and prompting people to find strategies.

Important limits from the same research:
- For **complex tasks you are still learning**, a performance goal ("score 80") can backfire; a **learning goal** ("find and practise three strategies for percentage problems") works better at first.
- Very hard goals with no feedback, or goals imposed without commitment, can cause stress, cheating or giving up.
- Too many goals compete for attention.

**SMART goals** (Specific, Measurable, Achievable, Relevant, Time-bound) is a popular management acronym that roughly matches this research, but it was not itself tested as a package. "Achievable" also undersells the finding that *challenging* goals work best.

**The progress principle.** Teresa Amabile and Steven Kramer studied nearly 12,000 daily diary entries from 238 professionals in seven companies. On days when people felt most positive and motivated, the most common event was **making progress in meaningful work**, even small progress. Setbacks had an even bigger negative effect than progress had a positive one (a sign of negativity bias, PD-M10-L01). Their study is observational (diaries), so it shows a strong link rather than proof of cause, but it fits much other research on feedback and competence.

**Putting it together:** a good goal system has one or two challenging, specific outcome goals, broken into learning or process goals you control, with frequent feedback and a way to see daily progress.
""",
    evidence=[
        ('Specific, challenging goals with feedback improve performance', 'strong', 'Hundreds of studies summarised by Locke and Latham.'),
        ('Learning goals beat performance goals for new, complex tasks', 'moderate', 'Supported in several studies; matters most early in learning.'),
        ('SMART as a tested package', 'tool', 'A popular acronym consistent with parts of the research, not tested as a whole.'),
        ('Progress in meaningful work drives daily motivation', 'moderate', 'Large diary study; observational, but consistent with feedback research.'),
    ],
    example=f"""
Vinod's goal was "prepare well for LDC". It changed nothing. He rewrites it.

**Outcome goal (challenging, specific):** "Score 70 or more out of 100 on a full PSC-pattern mock by 15 March." His current mock average is 52.

**Learning goals (for weak areas):** "Learn and practise three methods for percentage and ratio questions by 31 January."

**Process goals (fully in his control):** "Five study sessions a week of 90 minutes; one mock every Sunday; every error logged."

**Feedback:** a graph of Sunday mock scores on his shop wall.

**Progress:** every night, a one-line note: "Today's progress: finished 20 ratio questions; 16 right." On bad days he writes even tiny progress ("read one page of the Constitution"). After a month his mocks are at 58, below plan but rising, and he adjusts his plan instead of giving up.
""",
    apply=f"""
**Write goals in three layers:**

1. **One or two outcome goals** for the next three months: specific number, date, and challenging (a stretch, not a fantasy).
2. **Learning goals** for skills you don't yet have: "Find and practise…".
3. **Process goals** you control completely: how many sessions, when, how long.

Then add **feedback** (a weekly number you can see) and a **daily progress note** (one line each evening: "Today's progress: ______").

**When you miss a goal:** check commitment (do I still want it?), ability (do I need a learning goal first?) and feedback (did I see the problem early enough?). Adjust the plan, not your self-worth.

**With others:** when you help others set goals, ask them to set their own, make them specific, and agree on how they will see progress. Celebrate small progress you notice; it matters more than big speeches.
""",
    resources=[
        ('os-10', 'Re-read the part of 10.1 on theories of motivation and goals', '10 minutes'),
        ('ggsc', 'Search the site for "progress principle" or "small wins" and read one article', '10 minutes'),
        ('franklin', 'Read the part of Franklin\'s Autobiography about his plan for "moral perfection" and his weekly chart of 13 virtues (search the text for "thirteen")', '20 minutes'),
    ],
    steps=[
        'Write one outcome goal for the next three months with a number and a date.',
        'Break it into one learning goal and two or three process goals.',
        'Choose the feedback number you will check every Sunday and put it somewhere visible.',
        'Write a one-line daily progress note every evening for seven days.',
    ],
    proof='Your three-layer goal sheet, the feedback number and seven daily progress notes.',
    templates=[('Three-layer goal sheet', """THREE-LAYER GOAL SHEET                         Written: ______
OUTCOME GOAL (specific, challenging, dated):
  ______________________________________ by ______  (now: ______)
LEARNING GOAL(S) (skills I need first):
  Find and practise ______________________ by ______
PROCESS GOALS (fully in my control):
  ___ sessions a week, ___ minutes, at ______ ; ______________________
FEEDBACK I check every Sunday: ______________  Where it's visible: ______
DAILY PROGRESS NOTE (one line each evening):
  Date | Today's progress (however small) | Setback?""", '')],
    mistakes=[
        ('Setting ten goals.', 'One or two outcome goals at a time; the rest is distraction.'),
        ('Only outcome goals.', 'You cannot fully control results. Process goals are where daily effort goes.'),
        ('Using a performance goal for a skill you have not learned.', 'Start with a learning goal; set the score target once you know the methods.'),
        ('Ignoring small progress.', 'Write it down. It is what keeps motivation alive on ordinary days.'),
    ],
    quiz=[
        Q('Which kind of goal led to the best performance in Locke and Latham\'s research?', 'Specific and challenging, with feedback', 'Easy and vague', '"Do your best"', 'Secret goals with no feedback', why='Specific, difficult goals with commitment and feedback outperform the others.'),
        Q('For a complex skill you are still learning, which goal tends to work better at first?', 'A learning goal, such as "find and practise three methods"', 'A high score target', 'No goal', 'Many goals at once', why='Performance pressure before you know the methods can hurt.'),
        Q('What did Amabile and Kramer find in about 12,000 diary entries?', 'Progress in meaningful work was the most common feature of the best days', 'Pay rises made the best days', 'Long holidays drove motivation', 'Criticism improved motivation', why='Small wins in meaningful work were strongly linked with good inner work days.'),
        Q('What is the main limit of the progress-principle study?', 'It is observational, so it shows a strong link rather than proof of cause', 'It had only ten people', 'It was done on animals', 'It was never published', why='Diary data show association; other research supports the causal story.'),
    ],
    study='read the lesson and Franklin\'s virtues chart passage',
    action='write a three-layer goal sheet and keep a daily progress note for seven days',
)

LESSONS = [L1, L2]

MODULE = module(
    6,
    overview=f"""
What really drives lasting motivation: self-determination theory (autonomy, competence, relatedness), intrinsic and "owned" extrinsic motivation, goal-setting theory, and the progress principle. You redesign one goal so motivation comes from the design, not from willpower.

Motivation is not a feeling you wait for; it is something you can design. This module gives you the two best-supported ideas: meet your three basic needs, and set specific, challenging goals with visible progress. Together they explain why some study plans keep you going for months and others die in a week.

If procrastination is your main problem, Module 8 and the {xref('lrn', 'lrn-m06', 'Learning Capabilities procrastination module')} go deeper. Here the focus is on the *engine* of motivation.
""",
    outcomes=[
        'Explain SDT and the difference between controlled and owned motivation.',
        'Redesign a task to support autonomy, competence and relatedness.',
        'Use rewards wisely (to start dull tasks, not to bribe interest).',
        'Write three-layer goals with feedback, and keep a daily progress note.',
    ],
    lessons=LESSONS,
    project='a motivation redesign of one real goal',
    project_steps=[
        'Pick your most important goal for the next three months.',
        'Write it as a three-layer goal sheet (PD-M06-L02).',
        'Run the SDT redesign (PD-M06-L01) on its hardest daily task.',
        'Track for two weeks: process-goal completion, your weekly feedback number and daily progress notes. Write a five-line review.',
    ],
    project_proof='The goal sheet, the SDT redesign, two weeks of tracking and the five-line review.',
    rubric=[
        ('Goal quality', 'Vague goal', 'Specific outcome goal only', 'Outcome, learning and process layers with feedback'),
        ('Needs support', 'No changes made', 'One need addressed', 'All three needs addressed with real changes'),
        ('Tracking', 'No tracking', 'Some days tracked', 'Two weeks of daily progress notes and weekly feedback'),
        ('Reflection', 'No review', 'Review describes what happened', 'Review adjusts the plan based on data'),
    ],
    short=[
        'Write one outcome goal with a number and date, and one process goal.',
        'Keep a one-line daily progress note for a week.',
    ],
    flashcards=[
        ('Three SDT needs', 'Autonomy, competence, relatedness.'),
        ('Owned (identified) motivation', 'Doing something for an outside goal you have made your own; nearly as strong as intrinsic.'),
        ('When can rewards backfire?', 'Expected tangible rewards for already-interesting tasks can reduce interest.'),
        ('Goal-setting theory', 'Specific, challenging goals with commitment and feedback beat "do your best".'),
        ('Learning goal', '"Find and practise methods for X": better than a score target for new complex skills.'),
        ('Process goal', 'A goal fully in your control: sessions, times, actions.'),
        ('Progress principle', 'Small progress in meaningful work is the top feature of good workdays (diary study).'),
    ],
    mistakes=[
        ('Relying on motivational videos.', 'They lift mood briefly; design (needs, goals, feedback) lasts.'),
        ('Setting goals others chose for you without making them yours.', 'Write your own reason, or negotiate the goal.'),
        ('Changing goals every week.', 'Commit for at least a month before judging.'),
    ],
    tools=[
        'The SDT redesign sheet (PD-M06-L01).',
        'The three-layer goal sheet with daily progress note (PD-M06-L02).',
    ],
    playbook=[
        'When I lose motivation I check: Do I have choice? Can I see progress? Who is in this with me?',
        'My goals have three layers: outcome, learning, process; I check one feedback number every Sunday.',
    ],
)
