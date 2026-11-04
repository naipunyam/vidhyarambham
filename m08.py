from common import lesson, module, link, xref, table, Q
import tools

L1 = lesson(
    8, 1,
    outcome='You can explain present bias, set up a commitment device, use temptation bundling, and describe honestly what happened to the "willpower as fuel" and marshmallow-test ideas.',
    split='20 minutes reading, 30 minutes of tasks',
    principle='We overvalue rewards now compared with later, so self-control works best when you arrange things in advance (commitments, bundles, removed temptations) rather than relying on in-the-moment willpower.',
    science=f"""
**Present bias.** Offered ₹1,000 today or ₹1,100 in a week, many people take ₹1,000. Offered ₹1,000 in 52 weeks or ₹1,100 in 53 weeks, most choose to wait the extra week. The same one-week delay feels much bigger when it starts now. Economists call this **present bias** (or hyperbolic discounting). It explains why "I'll start tomorrow" feels reasonable every single day.

**Commitment devices.** If your future self will be tempted, your present self can tie its hands, like Ulysses asking to be tied to the mast so he could hear the Sirens without steering onto the rocks. In a well-known field study in the Philippines, Nava Ashraf, Dean Karlan and Wesley Yin offered savings accounts that locked money until a goal date or amount; people offered them saved more on average after a year. Other commitments: paying for a weekly class in advance, promising a friend you will show up at 6 am, giving your phone to a family member during study blocks. Commitments work best when they are **small, specific and easy to set up**, and many people do not take them up when offered, so they are a tool, not a cure.

**Temptation bundling.** Katherine Milkman and colleagues gave gym members iPods loaded with audiobooks they wanted, usable only at the gym. In the 2014 study, gym visits rose noticeably at first, and the effect faded after a few weeks (and over holiday breaks). A much larger 2021 replication with members of a big US gym chain found a **smaller** but real effect. Honest summary: bundling a treat you want (a podcast, a favourite song list, the good tea) with a task you avoid helps a little, especially early on.

**Is willpower a fuel tank?** Roy Baumeister's "ego depletion" research (from 1998) claimed that self-control uses up a limited resource: resisting cookies made people give up sooner on a puzzle afterwards. It became hugely popular. But a pre-registered replication across 23 labs with about 2,100 people (2016) found no evidence of the effect, and another across 36 labs with about 3,500 people (2021) found an effect close to zero ({link('wp-ego', 'summary')}). People do get tired and lose motivation after long effort, but the strong "fuel tank" model is not supported. Studies by Veronika Job and colleagues even suggest people who *believe* willpower is limited show more depletion-like effects.

**The marshmallow test.** Walter Mischel's studies (from the late 1960s) let children wait for two treats instead of eating one now. Follow-ups linked longer waiting to better teenage outcomes. But a larger 2018 replication by Tyler Watts, Greg Duncan and Haonan Quan found the link was about **half** as strong, and shrank further after accounting for family background. Celeste Kidd's 2013 study showed children wait much longer when the adult has been reliable, so waiting partly reflects whether waiting is likely to pay off ({link('wp-marshmallow', 'summary')}). The useful lessons are the original ones: children waited longer when treats were out of sight, and when they distracted themselves. **Self-control is easier when temptation is out of sight.**
""",
    evidence=[
        ('Present bias (preferring now over later)', 'strong', 'Found in many lab and field studies across countries.'),
        ('Commitment devices', 'moderate', 'Field studies show benefits for those who use them; many people do not take them up.'),
        ('Temptation bundling', 'moderate', 'Original effect faded; a large replication found a smaller but real effect.'),
        ('Ego depletion (willpower as a limited fuel)', 'failed', 'Large pre-registered multi-lab replications found effects near zero.'),
        ('Marshmallow test predicts life success', 'mixed', 'Link about half as strong in a larger study and smaller after family background.'),
        ('Keeping temptation out of sight helps self-control', 'strong', 'Shown in the original delay studies and in many later environment studies.'),
    ],
    example="""
Anu loses her evening study block to Instagram reels nearly every day. Each night she plans "only 10 minutes", which becomes an hour (present bias: the reel's reward is now, the exam's is months away).

She sets up three things. **Commitment device:** she pays ₹200 a week in advance for a Saturday test series at a library study centre; skipping wastes the money and she has told the organiser she will be there. **Out of sight:** during the 7–8:30 pm block her phone charges in her mother's room, not hers. **Temptation bundle:** she saves her favourite film-song playlist for her evening walk only.

She stops telling herself she has "run out of willpower" by evening. Instead, she notices that she is bored and tired, and starts the block with an easy 10-minute task. Over three weeks, her evening study days go from 2 to 5 a week. The test series is the device she uses least; the phone in another room does the most.
""",
    apply="""
**Design self-control in advance:**

1. **Name the conflict:** "When ______, I choose ______ now instead of ______ later."
2. **Choose one device:**
   - **Remove or hide the temptation** (strongest and simplest).
   - **Commit:** pay in advance, promise a specific person, set a deadline someone else checks.
   - **Bundle:** allow a treat only during the task you avoid.
3. **Make the good choice easy now:** start with a small first step.
4. **Change the story:** say "I'm tired or bored; what would make this easier?" instead of "I'm out of willpower."

**Ethics with others:** commitment devices are for yourself. Do not trap other people into commitments they would not choose (hidden auto-renewing subscriptions are exactly this, and Module 32 shows how to spot them).
""",
    resources=[
        ('wp-ego', 'Read the sections on the replication attempts', '10 minutes'),
        ('wp-marshmallow', 'Read the follow-up and replication sections', '10 minutes'),
        ('os-10', 'Re-read 10.1 for the basic ideas about drives, incentives and self-regulation', '10 minutes'),
    ],
    steps=[
        'Write your biggest present-bias conflict in one sentence.',
        'Set up one device of each kind: a hidden or removed temptation, a commitment (money, a person or a deadline) and a temptation bundle.',
        'Use them for seven days and tick each day the good choice won.',
        'Write which device helped most and which you will keep.',
    ],
    proof='Your conflict sentence, a photo or note of each of the three devices, and seven days of ticks with your verdict.',
    templates=[('Self-control design sheet', """SELF-CONTROL DESIGN                  Week of ______
Conflict: When ______________, I choose ______ now instead of ______ later.
1. Hide or remove the temptation: ______________________________
2. Commitment (money / person / deadline): ______________________
3. Temptation bundle: I only ______ (treat) while ______ (task).
4. Easy first step: ______________________________
Day:            M  T  W  T  F  S  S
Good choice won [ ][ ][ ][ ][ ][ ][ ]
Most helpful device: ______  Keep? ______""", '')],
    mistakes=[
        ('Relying on "more willpower".', 'Change the situation. Hiding temptation beats resisting it.'),
        ('Commitments that are too big.', '"₹5,000 to a friend if I miss one session" leads to quitting the device. Start small.'),
        ('Telling people "willpower runs out like fuel".', 'The strong version failed replication. Say "effort tires us, and environment matters more".'),
        ('Believing a child\'s marshmallow wait decides their future.', 'Larger studies show a modest link, partly explained by family background.'),
    ],
    quiz=[
        Q('Why does "I\'ll start tomorrow" feel reasonable every day?', 'Present bias makes rewards now feel much bigger than the same rewards later', 'Because tomorrow you will have more willpower fuel', 'Because plans never work', 'Because of anchoring', why='The delay that starts now always feels largest.'),
        Q('What did large multi-lab replications find about ego depletion?', 'Effects close to zero', 'Large effects', 'That willpower increases with use', 'That glucose drinks double willpower', why='Studies in 2016 (23 labs) and 2021 (36 labs) found little or no effect.'),
        Q('What did the 2018 marshmallow replication find?', 'The link with later achievement was about half as strong and shrank after family background', 'The original results were confirmed exactly', 'Waiting predicts nothing at all, ever', 'Children cannot wait', why='Watts, Duncan and Quan found a weaker, partly background-driven link.'),
        Q('Which self-control method has the strongest, simplest support?', 'Keeping the temptation out of sight or out of reach', 'Thinking about the temptation more', 'Promising yourself silently', 'Watching motivational videos', why='Out of sight is easier than resisting in the moment.'),
    ],
    study='read the lesson and the Wikipedia replication sections on ego depletion and the marshmallow test',
    action='set up a hidden temptation, a commitment and a temptation bundle and track seven days',
)

L2 = lesson(
    8, 2,
    outcome='You can map a habit as cue, routine and reward, redesign your environment to make good habits easy and bad ones hard, and measure the difference.',
    split='20 minutes reading, 30 minutes of tasks',
    principle='Habits are actions triggered automatically by cues in a stable context; change the cues and the effort required, and behaviour follows with far less willpower.',
    science=f"""
**What a habit is.** In psychology, a habit is a behaviour triggered **automatically by a cue** in a familiar context, because it has been repeated and rewarded there many times. Wendy Wood's research suggests that a large share of daily actions (in diary studies, roughly 40%) are done in the same place almost every day, often while thinking about something else.

**Cue, routine, reward.** Charles Duhigg popularised the "habit loop" (cue → routine → reward) in *The Power of Habit*. It is a useful simplification of learning research: a **cue** (a time, a place, a feeling, a person, a preceding action) triggers a **routine**, which is followed by a **reward** that makes the link stronger. Over time the cue alone starts the routine, even when the reward no longer matters much. That is why you reach for your phone the moment you sit down, even when you don't want to.

**How long does it take?** In Phillippa Lally's 2009 study, 96 people chose a new daily behaviour (such as drinking water with lunch or doing sit-ups after morning coffee). It took a **median of about 66 days** to reach their peak automaticity, with a range from **18 to 254 days**, and missing a single day did not significantly derail the process ({link('lally', 'Lally')}). Simple behaviours became automatic faster than complex ones. The "21 days" claim is not from research.

**Friction.** Small changes in effort have big effects. Making a healthy option slightly easier (placing it first, closer, at eye level) or an unhealthy one slightly harder (further away, needing an extra step) changes behaviour in many studies of food choice, saving and screen use. Wood calls this **friction**: add it to bad habits, remove it from good ones.

**Context change is an opportunity.** Habits are tied to context. When context changes (moving house, a new job, a new term), old cues disappear and people are more open to new habits: a "habit discontinuity". This fits with the "fresh start effect" found by Hengchen Dai, Katherine Milkman and Jason Riis: people are more likely to start goals at temporal landmarks such as Mondays, birthdays and new months.
""",
    evidence=[
        ('Habits are cue-triggered and context-dependent', 'strong', 'Supported by many lab and field studies (Wood, Neal and others).'),
        ('Habit formation takes weeks to months, varying widely', 'moderate', 'Lally (2009): median about 66 days, range 18–254; one key study plus later work.'),
        ('Missing one day does not ruin habit formation', 'moderate', 'Found in Lally\'s study; consistent with later work.'),
        ('Friction (small changes in effort) changes behaviour', 'strong', 'Many studies on food placement, defaults and access.'),
        ('Fresh-start effect at temporal landmarks', 'moderate', 'Found in several large datasets and studies.'),
        ('"21 days to form a habit"', 'failed', 'Not from research; real times vary widely.'),
    ],
    example="""
Ashiq maps two habits.

**Bad habit:** *cue* sitting on the bed after dinner → *routine* opening YouTube → *reward* relief from tiredness and something new. **Redesign:** the phone charges on the shelf by the door (friction: he has to get up); the Kerala PSC book is on his pillow; the YouTube app is logged out and moved off the home screen.

**Good habit he wants:** a morning walk. *Cue* the alarm at 5:50 → *routine* walk → *reward* tea with his cousin at the junction tea shop. **Redesign:** walking clothes laid out on the chair the night before; shoes by the door; a fixed meeting time with his cousin.

He measures it: before the change, YouTube after dinner took about 70 minutes on average (Digital Wellbeing); in week two, about 25. Walks went from 1 to 4 a week. He also notices that his best start was on a Monday, the first of the month: a fresh start.
""",
    apply="""
**Habit redesign in four moves:**

1. **Map the loop:** for one habit you want and one you want to drop, write cue, routine and reward.
2. **For a good habit: make it obvious and easy.** Put the cue where you cannot miss it (the book on the pillow, shoes by the door). Remove steps. Keep the reward immediate (the tea, the tick in Loop).
3. **For a bad habit: make it invisible and hard.** Remove the cue (phone out of the bedroom) and add friction (log out, delete the app, keep snacks out of the house).
4. **Use fresh starts:** begin on a Monday, the 1st of the month, or after a context change.

**Expect weeks, not days:** keep going for at least two months. If you miss a day, don't miss twice.

**With others:** you can help family and friends by changing shared environments (fruit on the table, the TV off at study time) instead of nagging. Change the situation, not the person.
""",
    resources=[
        ('lally', 'Read the whole interview: the 66 days, the range and what helps', '10 minutes'),
        ('loop', 'Set up the habit with a reminder at the cue time; turn on the habit score graph', '10 minutes'),
        ('wellbeing', 'Check your daily average for your top app before and after the redesign', '5 minutes'),
    ],
    steps=[
        'Map one habit you want and one you want to drop (cue, routine, reward).',
        'Make at least three environment changes: one cue added, one cue removed, one friction change. Photograph them.',
        'Record a before number (minutes, count or days) for each habit from the last week.',
        'Run the redesign for 14 days and record the after number.',
    ],
    proof='Two habit maps, photos of three environment changes, and before-and-after numbers over 14 days.',
    templates=[('Habit loop map and redesign', """HABIT LOOP MAP
Habit I want: ______________   Habit I want to drop: ______________
Cue:     ______________                ______________
Routine: ______________                ______________
Reward:  ______________                ______________
REDESIGN
Make it obvious (cue added): ____________  Make it invisible (cue removed): ____________
Make it easy (steps removed): ___________  Make it hard (friction added): ____________
Keep it rewarding: ____________
Numbers:  before ______  after 14 days ______
Start date (a fresh start?): ______""", '')],
    mistakes=[
        ('Relying on motivation instead of cues.', 'A habit needs a reliable trigger. "Sometime in the evening" is not a cue; "after dinner, at the desk" is.'),
        ('Expecting automaticity in 21 days.', 'Plan for two months or more, especially for complex habits.'),
        ('Changing everything at once.', 'Redesign one or two habits at a time.'),
        ('Leaving the old cue in place.', 'If the phone stays by the bed, the old habit wins most nights.'),
    ],
    quiz=[
        Q('In Lally\'s study, how long did habits take to reach peak automaticity?', 'A median of about 66 days, ranging from 18 to 254', 'Exactly 21 days', 'One week', 'One year for everyone', why='The median was about 66 days with a very wide range.'),
        Q('What is "friction" in habit design?', 'The effort a behaviour takes; add it to bad habits, remove it from good ones', 'Arguments with family', 'Rubbing your hands before studying', 'A type of reward', why='Small changes in effort strongly change behaviour.'),
        Q('Which is the best cue for a study habit?', '"After dinner, at my desk, with the book already open"', '"When I feel like it"', '"Sometime in the evening"', '"When I have free time"', why='Specific time and place cues trigger habits.'),
        Q('What does the fresh-start effect suggest?', 'People are more likely to start goals at landmarks such as Mondays and new months', 'Habits only start in January', 'Never start on a Monday', 'Fresh food builds habits', why='Temporal landmarks make new beginnings feel natural.'),
    ],
    study='read the lesson and the Lally interview',
    action='map two habit loops, make three environment changes and compare 14 days before and after',
)

L3 = lesson(
    8, 3,
    outcome='You can write if-then plans, start tiny habits anchored to existing routines, and use identity statements without fooling yourself.',
    split='20 minutes reading, 25 minutes of tasks',
    principle='Deciding exactly when, where and how you will act ("If X, then I will Y") roughly doubles follow-through; tiny starting versions and identity-based framing help the habit grow.',
    science=f"""
**Implementation intentions (if-then plans).** Peter Gollwitzer showed that people who form a plan of the form "If situation X arises, then I will do Y" are much more likely to act than people with the same goal and no plan. A meta-analysis of 94 tests by Gollwitzer and Paschal Sheeran found a **medium-to-large average effect (d = 0.65)** ({link('gollwitzer', 'Gollwitzer and Sheeran, 2006')}). If-then plans work because the situation becomes a cue that triggers the action automatically, so you don't need to decide in the moment. They also work for **obstacles**: "If I feel like skipping, then I will do just five minutes." They are one of the best-supported tools in this whole course.

**Tiny habits.** B. J. Fogg, a Stanford researcher, teaches starting with a behaviour so small it takes under 30 seconds (two push-ups, opening the book, one line in the journal), anchored right after an existing routine ("After I brush my teeth, I will…"), and celebrated immediately to create a good feeling. His method is popular and fits habit research (a strong cue, low friction, an immediate reward), but it has mostly been tested in his own programmes rather than in independent trials. Treat it as a practical tool.

**Habit stacking** is the same anchoring idea: "After [current habit], I will [new habit]." James Clear's *Atomic Habits* popularised it, along with the idea of **identity-based habits**: instead of "I want to run", think "I am becoming someone who moves every day". There is supporting research on identity and behaviour: in studies by Christopher Bryan and colleagues, asking people about "being a voter" rather than "voting" increased turnout in some studies (later replications were mixed), and people tend to act consistently with how they see themselves (self-perception, commitment and consistency, PD-M28-L01). Identity framing is a moderate-evidence idea; it works best when backed by small actions that give you real evidence about who you are.

**Never miss twice.** Missing once has little effect (Lally's study); what breaks habits is the slide from one miss to many. A simple rule: "If I miss a day, the next day I do at least the tiny version."
""",
    evidence=[
        ('If-then plans (implementation intentions)', 'strong', 'Meta-analysis of 94 tests: medium-to-large average effect (d = 0.65).'),
        ('If-then plans for obstacles', 'moderate', 'Supported in many studies; effects vary by task.'),
        ('Tiny habits with anchors and celebration', 'tool', 'Consistent with habit research; mostly tested in its creator\'s programmes.'),
        ('Identity-based framing ("be a voter")', 'mixed', 'Some studies found effects; replications were mixed.'),
        ('"Never miss twice" rule', 'tool', 'Practical rule consistent with Lally\'s finding that single misses do little harm.'),
    ],
    example="""
Sreeja wants three new habits. She writes them as if-then plans and starts tiny:

- "**After** I finish my morning tea, **I will** do 2 push-ups (from the knees) and say 'done!'" Within three weeks, she does 10 most days.
- "**If** it is 7 pm on a weekday, **then I will** sit at my desk with the phone in Amma's room and open the Polity book." Some evenings she only reads one page. That still counts.
- "**After** I switch off the light, **I will** think of one good thing from today."

For obstacles: "If I feel like skipping study, then I will do five minutes and decide after that." She writes an identity line in her Playbook: "I'm becoming someone who shows up every day, even for five minutes." Each tick in Loop is a small piece of evidence for that identity.

When her cousin's wedding takes three days, she misses the push-ups twice. On day four she does the tiny version: two push-ups. The chain restarts.
""",
    apply="""
**Write three if-then plans:**

1. **Action plan:** "If/When [time + place or after current routine], then I will [specific action]."
2. **Obstacle plan:** "If [likely obstacle], then I will [response]."
3. **Restart plan:** "If I miss a day, then the next day I will do [tiny version]."

**Start tiny:** shrink each new habit to a version that takes under two minutes. Do the tiny version every day for two weeks before growing it. Celebrate immediately (a word, a tick, a small fist pump).

**Identity:** write one line: "I'm becoming someone who ______." Count each completion as a vote for it.

**With others:** if-then plans work in pairs and families too: "If Amma calls during my study block, I'll call back at 8:30." Agree on them together in advance.
""",
    resources=[
        ('gollwitzer', 'Read the abstract and the summary of effect sizes', '10 minutes'),
        ('loop', 'Add each new habit with a reminder at its cue time', '10 minutes'),
        ('franklin', 'Read how Franklin focused on one virtue a week (search the text for "a week\'s strict attention")', '10 minutes'),
    ],
    steps=[
        'Write one action plan, one obstacle plan and one restart plan for a habit that matters to you.',
        'Choose two tiny habits anchored to existing routines and add them to Loop.',
        'Do them for 14 days. Celebrate each one. Note any misses and whether you missed twice.',
        'Write your identity line and three pieces of evidence for it from the 14 days.',
    ],
    proof='Your three if-then plans, a 14-day Loop screenshot for two tiny habits, and your identity line with three pieces of evidence.',
    templates=[('If-then plan card', """IF-THEN PLANS
Action:   When ______________________ (time/place or after ______),
          then I will ______________________.
Obstacle: If ______________________, then I will ______________________.
Restart:  If I miss a day, then the next day I will ______ (tiny version).
TINY HABITS (under 2 minutes)
After I ______________, I will ______________. Celebrate: "______!"
After I ______________, I will ______________. Celebrate: "______!"
Identity: I'm becoming someone who ______________________.
Evidence this fortnight: 1 ______ 2 ______ 3 ______""", '')],
    mistakes=[
        ('Vague plans.', '"I\'ll study in the evening" is not an if-then plan. Name the time, place and first action.'),
        ('Starting big.', 'Thirty push-ups a day collapses in week one; two push-ups grows.'),
        ('Identity statements without action.', 'Saying "I am a fit person" while never moving is self-deception. Identity grows from small, repeated evidence.'),
        ('Too many if-then plans at once.', 'Three to five are plenty. More and they stop being memorable.'),
    ],
    quiz=[
        Q('What was the average effect of if-then plans in the 94-test meta-analysis?', 'Medium to large (d = 0.65)', 'Zero', 'Tiny (d = 0.05)', 'Negative', why='Implementation intentions are among the best-supported behaviour-change tools.'),
        Q('Which is a good tiny habit?', '"After I brush my teeth, I will do 2 push-ups"', '"I will exercise more"', '"I will do 50 push-ups every morning from tomorrow"', '"I will be healthier this year"', why='Small, anchored to an existing routine, and specific.'),
        Q('What does "never miss twice" mean?', 'A single miss is fine; restart with the tiny version the next day', 'Never miss a day ever', 'Do double the next day', 'Stop the habit if you miss twice', why='Single misses do little harm; slides do.'),
        Q('How strong is the evidence for identity-based framing?', 'Mixed: some studies found effects and replications were mixed', 'Strong and universal', 'No research at all', 'Proved harmful', why='The voter-identity studies had mixed replications.'),
    ],
    study='read the lesson and the Gollwitzer and Sheeran abstract',
    action='write three if-then plans, run two tiny habits for 14 days and write your identity line with evidence',
)

L4 = lesson(
    8, 4,
    outcome='You can explain procrastination as mood repair, use three anti-procrastination tools, and run a two-week personal experiment on your study time with real data.',
    split='20 minutes reading, 10 minutes a day for two weeks',
    principle='Procrastination is less about laziness or poor time management and more about avoiding bad feelings; the fix is to make starting feel less bad, and to test your fixes with your own data.',
    science=f"""
**Why we procrastinate.** Fuschia Sirois and Timothy Pychyl argue that procrastination is mainly **short-term mood repair**: a task makes us feel anxious, bored, confused or inadequate, and delaying it brings instant relief, at the cost of our future self ({link('sirois', 'Sirois and Pychyl, 2013')}). That is why procrastination is common on tasks that are boring, unclear, difficult or tied to our self-worth (exam preparation is all four). It links with present bias (PD-M08-L01).

**What helps:**
1. **Make the first step tiny and clear:** "Open the book to page 112 and read one paragraph" is easier to start than "study Polity".
2. **Time-box it:** commit to 10 or 25 minutes, then decide whether to continue. Starting is the hard part.
3. **Self-forgiveness:** in a study by Michael Wohl, Pychyl and Shannon Bennett, students who forgave themselves for procrastinating on the first exam procrastinated less before the next one ({link('wohl', 'BPS summary')}). Harsh self-criticism makes the task feel worse, which feeds more avoidance.
4. **Expressive writing before high-stakes tasks:** writing about worries for 10 minutes before an exam improved scores for anxious students in Ramirez and Beilock's study ({link('rb-writing', 'University of Chicago summary')}).

The Learning Capabilities course has a full module on this: {xref('lrn', 'lrn-m06', 'Motivation, procrastination and habits')}. Here you add the most powerful tool for your whole life: **testing your own changes**.

**Personal experiments (n-of-1).** In medicine, "n-of-1 trials" test treatments on one person by switching between conditions and measuring. You can do a simple version: keep everything the same except **one change** and compare a **baseline week** with a **change week**, using one number (study minutes from a timer). It will not be perfect science: weeks differ, you know which week is which (no blinding), and two weeks is short. But it beats guessing, and it protects you from regression to the mean (PD-M02-L01) and from the confirmation bias of "I'm sure it helped". Repeating the switch (A-B-A-B) makes it stronger.
""",
    evidence=[
        ('Procrastination as short-term mood repair', 'moderate', 'Supported by several studies; a leading explanation, not the only one.'),
        ('Self-forgiveness reduces later procrastination', 'mixed', 'One well-known study with students; consistent with self-compassion research.'),
        ('Expressive writing about worries before exams', 'moderate', 'Lab and classroom studies found benefits for anxious students; later replications varied.'),
        ('Time-boxed starts (e.g. 10 or 25 minutes)', 'tool', 'Widely used and consistent with mood-repair theory; little direct testing.'),
        ('Personal A-B experiments', 'tool', 'A sound way to test changes on yourself, with clear limits (short, unblinded).'),
    ],
    example=f"""
Vinod suspects his study time is low because his books are in a cupboard in the shop's back room and his phone is always on the counter. He runs a two-week experiment.

**Question:** Does keeping a "study corner" set up (book open on the table, phone in a drawer, a timer ready) increase his study minutes?
**Week 1 (baseline):** normal routine. Study minutes measured with a phone timer each day: 35, 0, 50, 20, 45, 30, 60 → average about 34.
**Week 2 (change):** study corner set up every evening before he leaves the shop: 55, 40, 70, 60, 0 (a family function), 65, 75 → average about 52.

He writes honestly: "Week 2 had one function day; week 1 had a slow Tuesday at the shop. Both weeks were normal otherwise. The change seems to help by about 15–20 minutes a day." He keeps the study corner and plans a second experiment: does an earlier dinner help? He also notes that the timer itself may have made him study more in both weeks (people often change when they are measured), which is fine: measurement is part of the system.
""",
    apply="""
**The two-week personal experiment:**

1. **One question, one change:** "Does ______ increase my daily study minutes?" Good changes to test: phone in another room, a fixed start time, a study corner, studying before breakfast, a Pomodoro timer, a study partner call.
2. **One number:** study minutes, measured with a timer every day.
3. **Week 1 = baseline,** with no change. **Week 2 = the change** every day. Keep everything else as similar as possible.
4. **Log unusual events** (guests, illness, festivals, power cuts).
5. **Compare averages** and write an honest note about other differences.
6. **Decide:** keep, modify or drop, and plan the next experiment.

**For procrastination moments during the experiment:** tiny first step, a 10-minute time box, and forgiveness if you slip.
""",
    resources=[
        ('sirois', 'Read the abstract and the introduction on mood repair', '10 minutes'),
        ('wohl', 'Read the short summary of the self-forgiveness study', '5 minutes'),
        ('rb-writing', 'Read the summary of the expressive-writing study', '5 minutes'),
    ],
    steps=[
        'Write your experiment question, the one change and how you will measure study minutes.',
        'Week 1: record daily study minutes with a timer, with no change.',
        'Week 2: make the change every day and keep recording.',
        'Write averages, unusual events, an honest note about other differences, and your decision.',
    ],
    proof='The completed experiment log with 14 daily numbers, both averages, notes on unusual events and your decision.',
    templates=[('Personal experiment log', tools.EXPERIMENT_LOG, '')],
    mistakes=[
        ('Changing two things at once.', 'Then you cannot tell which one worked. One change per experiment.'),
        ('Estimating minutes from memory.', 'Use a timer. Memory overestimates good days.'),
        ('Declaring victory after a few good days.', 'Wait for the full week and compare averages, noting unusual days.'),
        ('Beating yourself up for procrastinating during the experiment.', 'Self-criticism feeds avoidance. Note it, forgive it, restart with the tiny step.'),
    ],
    quiz=[
        Q('According to Sirois and Pychyl, procrastination is mainly:', 'Short-term mood repair: avoiding the bad feelings a task brings', 'Laziness', 'Poor time-management skills only', 'Low intelligence', why='Delay brings instant relief from negative feelings.'),
        Q('In the Wohl, Pychyl and Bennett study, what reduced later procrastination?', 'Forgiving yourself for earlier procrastination', 'Punishing yourself', 'Studying all night', 'Ignoring the exam', why='Self-forgiveness lowered procrastination before the next exam.'),
        Q('What is the most important rule of a personal experiment?', 'Change one thing at a time and measure one number', 'Change everything to get quick results', 'Trust your feeling about whether it worked', 'Only do it for one day', why='One change and one measure make the comparison meaningful.'),
        Q('Why compare with a baseline week?', 'Without it, natural ups and downs (and regression to the mean) can look like effects', 'Because baselines are traditional', 'To make the experiment longer', 'It is not necessary', why='The baseline shows what would have happened anyway.'),
    ],
    study='read the lesson and the three study summaries',
    action='run the two-week personal experiment on your study time and write the result',
)

LESSONS = [L1, L2, L3, L4]

MODULE = module(
    8,
    overview=f"""
The core self-control and habits toolkit: present bias, commitment devices, temptation bundling, environment design, the habit loop, if-then plans, tiny habits, identity, procrastination, and a two-week personal experiment with data. Honest notes on what failed (ego depletion, "21 days").

This is the most practical module in Part B. It replaces "try harder" with design: make good behaviour easy, bad behaviour hard, and plans automatic. The best-supported tools here (if-then plans, friction, keeping temptation out of sight) work for almost everyone.

It ends with a skill you will use for life: testing a change on yourself with real numbers. The {xref('lrn', 'lrn-m06', 'Learning Capabilities procrastination module')} covers study-specific procrastination in more depth.
""",
    outcomes=[
        'Explain present bias and design commitment devices and temptation bundles.',
        'Explain what happened to ego depletion and the marshmallow test.',
        'Map habit loops and redesign your environment (cues and friction).',
        'Write action, obstacle and restart if-then plans and grow tiny habits.',
        'Explain procrastination as mood repair and run a two-week personal experiment.',
    ],
    lessons=LESSONS,
    project='a two-week personal experiment with data (and the habit redesign behind it)',
    project_steps=[
        'Complete the habit redesign from PD-M08-L02 and the if-then plans from PD-M08-L03.',
        'Run the two-week experiment from PD-M08-L04 on one change.',
        'Write a one-page report: question, method, numbers, other differences, decision.',
        'Add the change you are keeping, and your best if-then plan, to your Personal Playbook.',
    ],
    project_proof='The experiment log, the one-page report and the updated Playbook lines.',
    rubric=[
        ('Design', 'No environment changes', 'One or two changes', 'Cues and friction changed for a good and a bad habit'),
        ('Planning', 'No if-then plans', 'Vague plans', 'Specific action, obstacle and restart plans in use'),
        ('Experiment', 'Not done', 'Done without a baseline or a timer', 'Baseline and change weeks with timer data'),
        ('Honesty', 'Overclaims the result', 'Some caveats', 'Clear note on other differences and a reasoned decision'),
    ],
    short=[
        'Move one temptation out of sight and write one if-then plan.',
        'Do a one-week mini experiment: three days without the change, three days with it.',
    ],
    flashcards=[
        ('Present bias', 'Rewards now feel much bigger than the same rewards later.'),
        ('Commitment device', 'Arranging things now so your future self can\'t easily give in.'),
        ('Temptation bundling: honest status', 'Helps a little; the large replication found a smaller effect.'),
        ('Ego depletion status', 'Failed large pre-registered replications (23 and 36 labs).'),
        ('Habit loop', 'Cue → routine → reward; the cue alone eventually triggers the routine.'),
        ('Habit formation time (Lally)', 'Median about 66 days; range 18–254.'),
        ('If-then plan effect', 'Medium to large (d = 0.65) across 94 tests.'),
        ('Procrastination is mainly…', 'Short-term mood repair.'),
        ('Personal experiment rules', 'One change, one number, a baseline week, an honest note.'),
    ],
    mistakes=[
        ('Collecting tools without testing them.', 'Pick two, use them for two weeks, measure.'),
        ('Blaming your character.', 'Most failures are design failures: a missing cue, too much friction, too big a start.'),
        ('Stopping a working habit once it feels easy.', 'Easy means it is becoming automatic: that is the goal. Keep the cue.'),
    ],
    tools=[
        'The self-control design sheet (PD-M08-L01).',
        'The habit loop map and redesign (PD-M08-L02).',
        'The if-then plan card with tiny habits and identity line (PD-M08-L03).',
        'The personal experiment log (PD-M08-L04).',
    ],
    playbook=[
        'I design, I don\'t rely on willpower: temptation out of sight, cues in sight, tiny starts.',
        'My keystone if-then plan: If ______, then I will ______. If I miss a day, I do the tiny version.',
        'I test changes on myself: one change, one number, two weeks.',
    ],
)
