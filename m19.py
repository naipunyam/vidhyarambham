"""Module 19: Brain health."""
from common import lesson, module, link, rules, fence, table

M = 19

L1 = lesson(
    M, 1,
    outcome='Protect the sleep that consolidates learning: track your sleep for two weeks, set a consistent schedule and fix the habits that cut it short.',
    split='15 minutes reading, 25 minutes resources, 20 minutes setup plus a two-week log',
    core=f"""
### Sleep is part of studying

In Module 1 you saw that new memories are stabilised over the following hours, with sleep playing a part: stage 2 sleep spindles and REM sleep have been linked to learning and memory ({link('os-psych-4-3', 'OpenStax Psychology 2e, 4.3')}). Sleep also restores attention, mood and self-control, which every study method in this course depends on.

The American Academy of Sleep Medicine and the Sleep Research Society recommend that **adults sleep 7 or more hours a night on a regular basis**. Sleeping less regularly is linked with impaired performance, more errors and a higher risk of accidents ({link('aasm', 'AASM and SRS consensus statement')}).

For a PSC aspirant, cutting sleep to "study more" is usually a bad trade: you get extra hours with worse attention, and you lose part of the consolidation of what you studied.

### Habits that protect sleep

- **A consistent schedule:** the same bedtime and wake time every day, including weekends, as far as your life allows.
- **The phone outside the bedroom,** or at least in Bedtime mode with greyscale and Do Not Disturb (Module 5; {rules('wellbeing', 'Android Digital Wellbeing')}).
- **A wind-down routine:** the last 30 minutes before bed without new study topics or screens. A short recall of the day's topic (Module 1) fits well here.
- **Tea and coffee:** if they affect your sleep, keep them to the earlier part of the day. Test it with your sleep log.
- **Light and noise:** a dark, quiet, cool room as far as you can manage.

### Exam season

The nights before mocks and exams matter most. Stop new topics the evening before, do a light review, and sleep at your usual time. An all-nighter before an exam usually costs more marks than it gains.

### When to see a doctor

See a doctor if you have trouble sleeping for weeks despite good habits, if you are very sleepy during the day even after enough hours in bed, or if someone notices loud snoring with pauses or gasping in your sleep. These can be signs of conditions that need treatment.

This lesson is general guidance, not medical advice.
""",
    example="""
**Ashiq** started his sleep log without changing anything. The first five nights averaged 6 hours 10 minutes, with bedtimes between 11:40 p.m. and 2:15 a.m., and he scrolled Reels in bed most nights.

He set three rules: phone on the charger in the kitchen at 10:45 p.m., in bed by 11, up at 6:30 every day including Sunday. He moved his evening tea before 6 p.m. and did a 5-minute recall of the day's topic as his wind-down.

Over the second week his average rose to 7 hours 15 minutes. He also noticed in his log that his morning AnkiDroid percentage was lower after short nights, on average, which convinced him more than any article. Sunday was the hardest day to keep, so he wrote an if-then plan: "If my friends ask me out late on Saturday, then I will come home by 10:30."
""",
    evidence=[
        ('Adults sleeping 7 or more hours regularly', 'strong', 'AASM and SRS consensus: less is linked with impaired performance, more errors and accidents.'),
        ('Sleep helps consolidate new memories', 'moderate', 'Sleep stages have been linked to learning and memory (OpenStax 4.3); the details are still being studied.'),
        ('Specific habits (phone out of the bedroom, consistent times, no late tea)', 'limited', 'Common, sensible advice; test each with your own sleep log.'),
    ],
    resources=[
        ('aasm', 'Read the recommendation and the effects of short sleep', '5 minutes'),
        ('os-psych-4-3', 'Reread the stages of sleep and their links to memory', '15 minutes'),
        ('wellbeing', 'Set up or check Bedtime mode on your phone', '5 minutes'),
    ],
    steps=[
        'Keep a 14-night sleep log: time in bed, time up, hours slept, how rested you feel, and your morning AnkiDroid percentage correct.',
        'After the first five nights, set your three sleep rules: a bedtime, a wake time (every day) and where the phone stays at night.',
        'Set Bedtime mode on your phone for your new bedtime, and write a 30-minute wind-down routine.',
        'At the end of 14 nights, work out your average hours for the first five and the last five nights, and compare your morning AnkiDroid percentages on short and long nights.',
        'Write an if-then plan for the night you are most likely to break your rules.',
    ],
    proof='Your 14-night sleep log with both averages and the AnkiDroid comparison, your three sleep rules and your if-then plan.',
    templates=[
        ('14-night sleep log', """
Night | In bed | Up    | Hours | Rested (1-5) | AnkiDroid % next morning | Phone in bedroom?
1     | ______ | _____ | _____ | ___          | ___%                     | Y / N
2     | ______ | _____ | _____ | ___          | ___%                     | Y / N
...
14    | ______ | _____ | _____ | ___          | ___%                     | Y / N
Average hours: nights 1-5 ___   nights 10-14 ___
AnkiDroid % after nights under 7 hours ___  after 7 hours or more ___
""", ''),
        ('my sleep rules', """
MY SLEEP RULES
1. In bed by ______, every day.
2. Up at ______, every day, including Sunday.
3. Phone charges in ______________ (or Bedtime mode from ______).
Wind-down (last 30 minutes): no new topics, no screens; 5-minute recall of today's topic.
Night before a mock or exam: light review only; usual bedtime.
If-then: If ______________________, then I will ______________________.
""", ''),
    ],
    mistakes=[
        ('Trading sleep for study hours.', 'Seven hours or more makes the hours you do study count.'),
        ('Sleeping late on Sunday to "catch up".', 'Keep wake times steady; large swings disturb the next week.'),
        ('Scrolling in bed.', 'Charge the phone outside the bedroom or use Bedtime mode.'),
        ('Ignoring long-lasting sleep problems.', 'See a doctor if problems last for weeks despite good habits.'),
    ],
    quiz=[
        {'q': 'How much sleep do the AASM and the Sleep Research Society recommend for adults?', 'o': ['7 or more hours a night, regularly', '5 hours on study days', '4 hours plus a nap', 'As little as possible during exams'], 'a': 'A', 'why': 'Less is linked with impaired performance, errors and accidents.'},
        {'q': 'What should the night before a mock or exam look like?', 'o': ['A light review and your usual bedtime', 'An all-nighter on new topics', 'Three mocks in a row', 'No sleep at all'], 'a': 'A', 'why': 'Sleep supports attention and consolidation; new topics add little.'},
        {'q': 'Which habit best protects sleep from your phone?', 'o': ['Charging it outside the bedroom, or using Bedtime mode', 'Keeping it under the pillow', 'Turning up the brightness', 'Watching Reels until you feel sleepy'], 'a': 'A', 'why': 'Distance and Bedtime mode reduce late scrolling.'},
        {'q': 'When should you see a doctor about sleep?', 'o': ['When problems last for weeks despite good habits, or with loud snoring and gasping', 'After one bad night', 'Never', 'Only before exams'], 'a': 'A', 'why': 'These can be signs of conditions that need treatment.'},
    ],
    study='The AASM sleep recommendation and OpenStax 4.3 on sleep stages',
    action='Keep a 14-night sleep log, set three sleep rules and compare your averages',
)

L2 = lesson(
    M, 2,
    outcome='Add regular physical activity and real breaks to your study week, and make simple food choices that follow official Indian guidance.',
    split='15 minutes reading, 25 minutes resources, 20 minutes planning plus two weeks of logging',
    core=f"""
### Movement

The World Health Organization recommends that adults do **at least 150 minutes of moderate-intensity physical activity a week**, such as brisk walking, cycling or active housework, and says physical activity improves brain health, thinking and sleep, and reduces symptoms of depression and anxiety ({link('who-pa', 'WHO physical activity fact sheet, 2024')}).

For a PSC aspirant, 150 minutes is 30 minutes on five days: a brisk walk to the library, an evening walk with family, cycling to the market, a yoga routine. It doesn't need a gym or money.

Be honest about what to expect: the evidence that activity is good for health, mood and sleep is strong; the evidence that a walk will directly raise your exam score is limited. Think of it as protecting the brain you study with.

### Breaks

Long stretches of sitting drain attention. In the study of Pomodoro-style breaks (Module 5), students who took short planned breaks reported less fatigue and more concentration than those who chose their own breaks ({link('biwer', 'Biwer and others, 2023')}). Use breaks to **move**: stand, stretch, walk to the verandah, drink water. Don't spend them scrolling.

### Food

The Indian Council of Medical Research's National Institute of Nutrition released updated **Dietary Guidelines for Indians** in 2024. Its main messages, as reported by All India Radio News, include being physically active, limiting salt, sugar and fats, cutting down on ultra-processed foods and preventing obesity ({link('icmr-diet', 'All India Radio News, May 2024')}).

For study days, that suggests simple habits:

- **Regular meals:** long gaps followed by a heavy meal tend to bring tiredness. Notice what happens to your focus after different meals in your Focus log.
- **Fewer fried and packaged snacks** during study: swap some for fruit, nuts or home-made snacks.
- **Water:** keep a bottle where you study, especially in Kerala's heat.

This course found no good evidence for special "brain foods" or supplements that improve exam performance; be wary of products that promise it. If you have a health condition, follow your doctor's advice.
""",
    example="""
**Sreeja** spent most of her day either working at home or sitting with her books. Her weekly activity, when she counted it honestly, was about 40 minutes.

She planned 30-minute brisk walks with her children on five evenings, on the road to the temple and back, and a short stretching routine in every study break. In her two-week activity log she reached 160 minutes in week 1 and 175 in week 2. She also noticed in her Focus log that her worst blocks came after a large lunch with fried snacks, so she moved to a lighter lunch with a fruit at 4 p.m.

She can't prove that the walks raised her mock score. But she sleeps better, feels less heavy in her evening study slot, and her children now remind her when it is time to walk.
""",
    evidence=[
        ('Regular physical activity for health, mood and sleep', 'strong', 'WHO recommends at least 150 minutes of moderate activity a week for adults, citing benefits for brain health, sleep and mood.'),
        ('Exercise directly raising exam scores', 'limited', 'Plausible, but direct evidence for exam results is limited.'),
        ('Planned short breaks reduce fatigue', 'limited', 'One study of 87 students (Biwer and others, 2023).'),
        ('Special "brain foods" or supplements for exams', 'limited', 'This course found no good evidence; official guidance stresses a balanced diet with less salt, sugar, fat and ultra-processed food.'),
    ],
    resources=[
        ('who-pa', 'Read the recommendations for adults and the listed benefits', '15 minutes'),
        ('icmr-diet', 'Read the news report on the 2024 Dietary Guidelines for Indians', '5 minutes'),
        ('biwer', 'Reread the abstract on breaks and fatigue', '5 minutes'),
    ],
    steps=[
        'Count your physical activity for one normal week honestly (minutes of moderate activity).',
        'Plan how you will reach at least 150 minutes a week, in sessions that fit your day (for example five 30-minute walks), and add them to your study planner.',
        'Write a break menu of movements for study breaks, and use it in every break for two weeks.',
        'Choose one food change for study days (a lighter lunch, fewer fried snacks, a water bottle at your desk) and keep it for two weeks.',
        'Keep a two-week activity log with your minutes, and note your focus rating after meals in your Focus tab.',
    ],
    proof='Your two-week activity log with weekly totals, your break menu, and a note on your food change and what you noticed.',
    templates=[
        ('weekly activity log', """
WEEKLY ACTIVITY      Week of ______   Target: 150 minutes of moderate activity
Day | Activity (brisk walk, cycling, yoga, active housework) | Minutes
Mon | __________________________________________________ | ___
Tue | __________________________________________________ | ___
...
Sun | __________________________________________________ | ___
Total ___ minutes   Target met? Y / N   Sleep this week (average) ___ h
""", ''),
        ('break menu (5 minutes, no phone)', """
[ ] Stand and stretch: arms, neck, back
[ ] Walk to the verandah or courtyard and back, twice
[ ] Drink a glass of water
[ ] Look at something far away for a minute (rest the eyes)
[ ] Ten slow breaths
""", ''),
    ],
    mistakes=[
        ('An all-or-nothing gym plan.', 'Walking 30 minutes on five days is enough to meet the WHO target.'),
        ('Breaks spent scrolling.', 'Move in your breaks; keep the phone for later.'),
        ('Buying "brain" supplements.', 'No good evidence was found for exam benefits; spend nothing.'),
        ('Long gaps without food, then a heavy meal before study.', 'Regular, lighter meals keep energy steadier; check your Focus log.'),
    ],
    quiz=[
        {'q': 'How much moderate physical activity does WHO recommend for adults each week?', 'o': ['At least 150 minutes', 'At least 15 minutes', 'Exactly 10 hours', 'None if you study'], 'a': 'A', 'why': 'For example, 30 minutes of brisk walking on five days.'},
        {'q': 'Which is a key message of the 2024 Dietary Guidelines for Indians, as reported?', 'o': ['Limit salt, sugar and fats, and cut down on ultra-processed foods', 'Eat as many sweets as you like before exams', 'Skip breakfast to focus', 'Take daily brain supplements'], 'a': 'A', 'why': 'The guidelines also stress being physically active.'},
        {'q': 'What is the honest evidence on exercise and exam scores?', 'o': ['Strong for health, mood and sleep; limited for exam scores directly', 'Proven to add 20 marks', 'Proven harmful for studying', 'There is no evidence for any benefit'], 'a': 'A', 'why': 'Treat activity as protecting the brain you study with.'},
        {'q': 'What is the best use of a 5-minute study break?', 'o': ['Stand, stretch, walk and drink water', 'Check Instagram', 'Start another topic', 'Lie in bed with the phone'], 'a': 'A', 'why': 'Movement rests attention; scrolling pulls it away.'},
    ],
    study='The WHO physical activity fact sheet and the report on the 2024 Dietary Guidelines for Indians',
    action='Reach 150 minutes of activity a week for two weeks, use a movement break menu and make one food change',
)

L3 = lesson(
    M, 3,
    outcome='Recognise how stress affects learning, practise simple ways to manage it, and know when and where to get help.',
    split='15 minutes reading, 25 minutes resources, 20 minutes planning plus two weeks of practice',
    core=f"""
### Stress and learning

Some stress is useful: a deadline sharpens focus. Long-lasting stress is different. It disturbs sleep, makes concentration harder, crowds working memory with worry and wears down motivation, so the same hours of study produce less.

PSC preparation has its own stresses: years of effort, uncertain notifications and results, family expectations, money worries, and constant comparison with "toppers" on social media.

### Ways to regulate stress

OpenStax *Psychology 2e* describes several ways people regulate stress, including **exercise**, **relaxation** methods such as the relaxation response, **biofeedback** and **social support** ({link('os-psych-14-4', 'OpenStax Psychology 2e, 14.4')}). In practice:

1. **Move every day** (LRN-M19-L02). WHO lists reduced symptoms of depression and anxiety among the benefits of physical activity ({link('who-pa', 'WHO')}).
2. **Slow breathing or relaxation,** 5 to 10 minutes a day: breathe in gently, breathe out more slowly, and let your shoulders drop.
3. **Talk to people.** Share how you feel with a family member, a friend or your study group. Social support is one of the most reliable buffers against stress.
4. **Control what you can:** your plan, your routines and today's blocks. Let go of what you can't: the date of a notification, other people's results.
5. **Limit comparison:** mute accounts that make you feel behind; compare yourself only with your own past (your Weekly tab).
6. **Put worries on paper:** a short daily "worry time" in a notebook, or the 10-minute writing before exams (LRN-M12-L06).
7. **Keep a life outside study:** one rest block a week, a hobby, time with people you love. A long preparation needs rest to last.

### When stress is more than stress

Talk to someone you trust and see a doctor if, for two weeks or more, you feel low or hopeless most of the time, lose interest in things you used to enjoy, sleep or eat very differently, have panic attacks, or have any thoughts of harming yourself.

**Tele-MANAS** is a free government mental health helpline, open 24 hours a day, in your language of choice: call **14416** or **1-800-891-4416** ({link('telemanas', 'Tele-MANAS')}). In an emergency, call **112**.

Asking for help is a strength, and it is part of looking after the learner, which is the point of this module. This lesson is general guidance, not medical advice.
""",
    example="""
**Joseph sir** noticed that Vinod had stopped coming to the study group after his name was missing from a rank list he had hoped for. When Joseph sir called him, Vinod said he couldn't sleep and felt there was no point.

Joseph sir listened, then shared what he had read in this module. Vinod agreed to two small things: a 30-minute walk each evening with a friend from the group, and coming back to the group on Saturday, without any study target. He also wrote down what he could control (his next 12-week plan, his routines) and what he couldn't (the rank list).

Joseph sir gave him the Tele-MANAS number and said there was no shame in calling, and that a doctor could help if the low mood stayed. Vinod called once. Two weeks later he was back at the group, sleeping better, and working on a new plan for the next notification.
""",
    evidence=[
        ('Exercise, relaxation and social support for stress', 'moderate', 'Described in OpenStax Psychology 2e as ways to regulate stress; WHO lists reduced symptoms of depression and anxiety among the benefits of activity. Results vary between people.'),
        ('Writing about worries', 'moderate', 'Expressive writing before exams helped anxious students in two studies (Ramirez and Beilock, 2011).'),
        ('Limiting social comparison and keeping rest time', 'limited', 'Sensible advice with little direct research checked for this course.'),
    ],
    resources=[
        ('os-psych-14-4', 'Read the section on regulating stress', '20 minutes'),
        ('who-pa', 'Reread the benefits of activity for mental health', '5 minutes'),
        ('telemanas', 'Save the helpline numbers in your phone', '2 minutes'),
    ],
    steps=[
        'Fill in the stress inventory: your main sources of stress, how stress shows up in you (sleep, focus, mood, body), and what you can and can\'t control.',
        'Choose three stress tools from this lesson and plan when you will use each.',
        'Practise them for two weeks and keep a short daily log: stress level from 1 to 10 and which tools you used.',
        'Write a support plan: two people you can talk to, when you will talk to them, and the Tele-MANAS and emergency numbers.',
        'Put one rest block a week into your study planner.',
    ],
    proof='Your stress inventory, the two-week tool log and your support plan (keep anything private to yourself; only the plan and log are needed as proof).',
    templates=[
        ('stress inventory', """
STRESS INVENTORY      Date: ______
Main sources of stress: 1. __________ 2. __________ 3. __________
How stress shows up in me: sleep ____ focus ____ mood ____ body ____
I CAN control: _______________________________________________
I CAN'T control: _____________________________________________
My three tools: 1. ______________ when: ______
                2. ______________ when: ______
                3. ______________ when: ______
""", ''),
        ('support plan', """
SUPPORT PLAN
People I can talk to: 1. ______________  2. ______________
When I will talk to them: ____________________________________
Rest block each week: ______________ (day and time)
If low mood, hopelessness, panic or thoughts of self-harm last or worsen:
talk to someone I trust and see a doctor.
Tele-MANAS (free, 24 hours): 14416 or 1-800-891-4416
Emergency: 112
""", ''),
    ],
    mistakes=[
        ('Hiding stress until it becomes a crisis.', 'Talk to someone early; small support now prevents bigger problems.'),
        ('Comparing yourself with "toppers" every day.', 'Mute what makes you feel behind; compare with your own past.'),
        ('No rest at all for months.', 'Plan one rest block a week; long preparations need rest to last.'),
        ('Thinking help is only for "serious" cases.', 'Tele-MANAS is free and open 24 hours; asking early is wise.'),
    ],
    quiz=[
        {'q': 'Which ways of regulating stress does OpenStax Psychology 2e describe?', 'o': ['Exercise, relaxation, biofeedback and social support', 'Studying through the night', 'Avoiding all people', 'Energy drinks'], 'a': 'A', 'why': 'Section 14.4 describes these methods.'},
        {'q': 'What is Tele-MANAS?', 'o': ['A free 24-hour government mental health helpline: 14416', 'A paid counselling app', 'A PSC helpline for results', 'A coaching centre'], 'a': 'A', 'why': 'It offers support in your language of choice.'},
        {'q': 'Which is something you can control during PSC preparation?', 'o': ['Your plan, routines and today\'s study blocks', 'The date of the next notification', 'Other candidates\' results', 'The cut-off marks'], 'a': 'A', 'why': 'Focusing on what you control reduces helpless worry.'},
        {'q': 'When should you seek help from a doctor or helpline?', 'o': ['If low mood, hopelessness, panic or thoughts of self-harm last or worsen', 'Only after an exam', 'Never; push through alone', 'Only if your family insists'], 'a': 'A', 'why': 'These signs need support, and asking early is a strength.'},
    ],
    study='OpenStax Psychology 2e 14.4 on regulating stress',
    action='Fill in a stress inventory, practise three stress tools for two weeks and write your support plan',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    M,
    overview="""
Look after the brain you study with: protect your sleep, move every day, take real breaks, eat simply following official guidance, and manage stress, with clear signs for when to get help.

All the techniques in this course work better in a rested, active, calm brain, and worse in a tired, stressed one. This module uses official and open sources (the AASM sleep recommendation, WHO's activity guidance, the Indian Dietary Guidelines and OpenStax Psychology) and is honest about what is strongly supported (enough sleep, regular activity) and what is not (brain foods, supplements).

It is general guidance, not medical advice. If you have a health condition, follow your doctor.
""",
    outcomes=[
        'Explain how sleep supports learning and keep a consistent sleep schedule',
        'Reach at least 150 minutes of moderate activity a week',
        'Use movement breaks and simple food habits from official guidance',
        'Recognise stress and use exercise, relaxation, support and planning to manage it',
        'Know the signs that need help, and the Tele-MANAS and emergency numbers',
    ],
    lessons=LESSONS,
    tools=[
        'The **14-night sleep log** and **my sleep rules**',
        'The **weekly activity log** and **break menu**',
        'The **stress inventory** and **support plan**',
    ],
    project='My brain-health plan',
    project_steps=[
        'Put your sleep rules, activity plan, break menu, food change, stress tools and support plan on one page.',
        'Show two weeks of the sleep log and the activity log with your averages and totals.',
        'Write what changed in your Focus tab and AnkiDroid percentages over the same weeks, honestly, including if nothing did.',
        'Add the plan\'s weekly items (walks, rest block) to your study planner for the next month.',
    ],
    project_proof='Your one-page brain-health plan, two weeks of sleep and activity logs, and your honest note on what changed.',
    rubric=[
        ('Sleep', 'Not tracked', 'Tracked without rules', 'Two weeks tracked, rules set and kept most nights'),
        ('Activity and breaks', 'Under 60 minutes a week', 'Some weeks at target', '150 minutes or more in both weeks, with movement breaks'),
        ('Stress', 'No plan', 'Tools chosen, not practised', 'Three tools practised and a support plan written'),
        ('Honesty', 'Claims miracles', 'Some reflection', 'Honest note on what changed and what didn\'t'),
    ],
    short=[
        'Keep three sleep rules and walk 30 minutes on five days a week.',
        'Save the Tele-MANAS number and name two people you can talk to.',
    ],
    flashcards=[
        ('Recommended sleep for adults (AASM and SRS)', '7 or more hours a night, regularly.'),
        ('The night before an exam', 'Light review only, usual bedtime.'),
        ('WHO activity target for adults', 'At least 150 minutes of moderate activity a week.'),
        ('Key messages of the 2024 Dietary Guidelines for Indians', 'Be active; limit salt, sugar and fats; cut down on ultra-processed foods.'),
        ('Evidence for "brain foods" and supplements for exams', 'This course found no good evidence.'),
        ('Four ways to regulate stress (OpenStax 14.4)', 'Exercise, relaxation, biofeedback, social support.'),
        ('Free mental health helpline', 'Tele-MANAS: 14416 or 1-800-891-4416, 24 hours.'),
    ],
    mistakes=[
        ('Treating health as separate from study.', 'Sleep, movement and calm are what make the study methods work.'),
        ('Waiting for a crisis before asking for help.', 'Talk to someone early; use Tele-MANAS if needed.'),
    ],
)
