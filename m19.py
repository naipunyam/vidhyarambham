from common import lesson, module, link, xref, table, fence, Q
import tools

L1 = lesson(
    19, 1,
    outcome='You can explain sleep stages, the body clock and sleep pressure, how much sleep adults need, and what harms sleep, with honest evidence.',
    split='20 minutes reading, 20 minutes of tasks',
    principle='Two systems run your sleep, a body clock set by light and a sleep pressure built by being awake; adults need at least 7 hours, and regular timing, light and caffeine habits matter most.',
    science=f"""
**How sleep works.** Sleep cycles through stages about every 90 minutes: light sleep (N1, N2), deep slow-wave sleep (N3) and REM sleep (rapid eye movement, when most vivid dreams happen). Deep sleep is concentrated early in the night and REM later, so cutting sleep short in the morning cuts REM disproportionately ({link('os-4-3', 'OpenStax 4.3 Stages of Sleep')}).

**Two systems** (Alexander Borbély's two-process model):
1. **The body clock (circadian rhythm):** a roughly 24-hour clock in the brain, set mainly by **light**. Morning daylight anchors it; bright light at night (including screens and room lights) pushes it later. The hormone **melatonin** rises in the evening darkness.
2. **Sleep pressure:** a chemical called **adenosine** builds up the longer you are awake, making you sleepy. **Caffeine** works by blocking adenosine receptors. Caffeine's half-life is roughly 5 hours on average (varying a lot between people), so an evening tea or coffee can still affect sleep at bedtime.

**How much?** The American Academy of Sleep Medicine and Sleep Research Society consensus recommends that adults sleep **7 or more hours** a night regularly ({link('aasm', 'AASM consensus')}). Regularly sleeping less is linked to weight gain, high blood pressure, diabetes, heart disease, depression, poorer attention and more accidents. Short-term sleep loss clearly harms attention, memory and mood in experiments. People who sleep 6 hours a night for two weeks perform about as badly on attention tests as people kept awake all night, yet they rate themselves as only slightly sleepy (a study by Hans Van Dongen and colleagues, 2003).

**Sleep and learning.** Sleep helps consolidate memories learned during the day; all-nighters before exams usually backfire. The {xref('lrn', 'lrn-m19', 'Learning Capabilities brain-health module')} covers sleep for study.

**What harms sleep:** irregular timing (late nights and long lie-ins, "social jet lag"), caffeine after early afternoon, alcohol (it helps you fall asleep but fragments sleep later in the night), heavy late meals, screens and bright light late at night, long or late naps, worry, noise, heat (an issue in Kerala summers) and mosquitoes. Napping: short naps of 10 to 20 minutes in the early afternoon refresh most people; long or late naps can make night sleep worse.

**Popular claims to treat carefully:** "blue light from phones is the main problem" (the content and timing of use, and lost sleep time, probably matter more than blue light itself; night modes help a little at most); "everyone needs exactly 8 hours" (needs vary; 7 to 9 suits most adults); "you can catch up fully at weekends" (partial recovery only).
""",
    evidence=[
        ('Adults need 7 or more hours regularly', 'strong', 'Expert consensus based on large reviews.'),
        ('Short sleep is linked to health problems', 'strong', 'Large observational studies plus experiments on short-term effects.'),
        ('Chronic short sleep impairs attention while people feel fine', 'strong', 'Controlled lab studies (e.g. Van Dongen et al., 2003).'),
        ('Caffeine late in the day disturbs sleep', 'strong', 'Experimental and observational studies.'),
        ('Blue light from screens is the main cause of poor sleep', 'mixed', 'Effects of blue light alone are small; timing, content and lost time matter more.'),
        ('Short early-afternoon naps refresh', 'moderate', 'Supported by several studies.'),
    ],
    example="""
Ashiq's 7-day sleep log from the baseline: lights out between 12:30 and 1:30 am, up at 6 or 9 depending on the day, average 6 hours 10 minutes, quality 2/5. He drinks tea at 4 pm and 8 pm, watches YouTube in bed, and naps for 90 minutes after lunch on some days.

He looks at the two systems. **Body clock:** his wake time swings by three hours, so his clock never settles (social jet lag). **Sleep pressure:** the long afternoon naps and the 8 pm tea both reduce it at bedtime. **Light and arousal:** an hour of exciting videos in bed. He notices that on the days he walked in the morning sun he fell asleep faster.

He doesn't change everything yet. He writes three targets for the sleep plan in PD-M19-L02: a fixed 6:00 wake time, no tea after 2 pm, and naps of 20 minutes at most.
""",
    apply="""
**Understand your own sleep (from your log):**
1. Average total sleep: below 7 hours?
2. Timing: how much do lights-out and wake time vary? (More than an hour is a problem.)
3. Sleep pressure: late caffeine? long or late naps?
4. Light: morning daylight? bright screens in bed?
5. Environment: heat, noise, mosquitoes, light in the room?

**Three facts to remember:** fixed wake time sets the clock; caffeine lasts for hours; screens in bed cost sleep mostly by keeping you up and alert.

**With others:** family sleep habits affect yours (late TV, early noise). Talk about a "quiet after 10:30" rule. Don't shame anyone's sleep; shift work and caring duties are real constraints.
""",
    resources=[
        ('os-4-3', 'Read the stages of sleep', '15 minutes'),
        ('aasm', 'Read the summary of the recommendation for adults', '5 minutes'),
        ('noba', 'Search for the module "States of Consciousness" and read the sleep sections', '20 minutes'),
    ],
    steps=[
        'Look at your 7-day sleep log from the Baseline page (or keep one now for 7 days).',
        'Answer the five "understand your own sleep" questions.',
        'Write your total caffeine (cups of tea and coffee) and their times for three days.',
        'Write your top three sleep problems and the system each affects (body clock, sleep pressure, light, environment).',
    ],
    proof='Your 7-day sleep log with averages, answers to the five questions, three days of caffeine times and your top three problems.',
    templates=[('7-day sleep log', tools.SLEEP_LOG, '')],
    mistakes=[
        ('Judging your sleep by how you feel.', 'Chronic short sleep feels normal while attention drops. Use the log.'),
        ('Catching up with long lie-ins.', 'They shift your body clock. Keep the wake time fixed.'),
        ('Thinking alcohol helps sleep.', 'It fragments sleep in the second half of the night.'),
        ('Blaming only blue light.', 'Timing, content and lost sleep time matter more.'),
    ],
    quiz=[
        Q('What sets the body clock most strongly?', 'Light, especially morning daylight', 'Food', 'Music', 'Room colour', why='Light is the main signal for the circadian rhythm.'),
        Q('How does caffeine keep you awake?', 'It blocks adenosine, the chemical that builds sleep pressure', 'It adds energy calories', 'It cools the brain', 'It raises melatonin', why='Caffeine blocks adenosine receptors.'),
        Q('How much sleep does the AASM consensus recommend for adults?', '7 or more hours a night, regularly', '5 hours', 'Exactly 8 hours for everyone', '10 hours', why='The expert consensus recommendation.'),
        Q('What did Van Dongen\'s study find about people sleeping 6 hours for two weeks?', 'Their attention fell sharply while they felt only slightly sleepy', 'They adapted fully', 'They performed better', 'They slept longer later', why='Chronic sleep restriction impairs performance without people noticing.'),
    ],
    study='read the lesson and OpenStax 4.3',
    action='analyse your 7-day sleep log, caffeine times and top three sleep problems',
)

L2 = lesson(
    19, 2,
    outcome='You can design and follow a two-week sleep plan using fixed wake time, a wind-down routine and CBT-I principles, and measure the change.',
    split='15 minutes reading, a few minutes a day for two weeks',
    principle='A fixed wake time, morning light, a caffeine cut-off, a calm wind-down and using the bed only for sleep improve sleep for most people; persistent insomnia has an effective non-drug treatment, CBT-I.',
    science="""
**Sleep hygiene versus CBT-I.** "Sleep hygiene" (good habits like regular timing, a dark quiet room, avoiding late caffeine) is sensible but, on its own, has only modest effects for people with real insomnia. **Cognitive behavioural therapy for insomnia (CBT-I)** is recommended by major medical bodies (including the American College of Physicians) as the **first-line treatment for chronic insomnia**, ahead of sleeping pills, with lasting benefits shown in many trials. Its core parts can be used as habits:

1. **Fixed wake time** every day, including weekends.
2. **Stimulus control:** use the bed only for sleep (no studying, scrolling or worrying in bed); if you can't sleep after about 20 minutes, get up, do something calm in dim light, and return when sleepy.
3. **Sleep restriction** (in therapy): temporarily limiting time in bed to your actual sleep time to build sleep pressure. **Do this only with professional guidance**; it causes short-term sleepiness and is not suitable for some people (for example, those with bipolar disorder, epilepsy, or jobs where sleepiness is dangerous).
4. **Cognitive work:** challenging worry about sleep ("If I don't sleep 8 hours, I'll fail tomorrow"), using thought records (PD-M11-L02) or a "worry time" earlier in the evening.
5. **Relaxation:** slow breathing, a body scan, or Shavasana.

**Light.** Getting outdoor light in the morning (even 10 to 30 minutes; cloudy daylight is still much brighter than indoor light) helps set the clock earlier; dimming lights in the evening helps melatonin rise.

**When to see a doctor.** If you have trouble sleeping at least three nights a week for three months, loud snoring with gasping or pauses in breathing (possible sleep apnoea), severe daytime sleepiness, leg discomfort that stops you sleeping, or sleep problems with low mood, see a doctor. Don't take sleeping pills or antihistamines for sleep without medical advice.
""",
    evidence=[
        ('CBT-I is effective first-line treatment for chronic insomnia', 'strong', 'Many trials; recommended by major medical bodies.'),
        ('Fixed wake time and stimulus control', 'strong', 'Core, well-tested components of CBT-I.'),
        ('Sleep hygiene alone for insomnia', 'mixed', 'Sensible, but modest effects on its own.'),
        ('Morning light helps set the body clock', 'strong', 'Well established in circadian research.'),
        ('Self-directed sleep restriction', 'tool', 'Effective in therapy; do it only with professional guidance.'),
    ],
    example=f"""
Ashiq's two-week sleep plan:
- **Wake 6:00** every day, alarm across the room. Walk outside by 6:15 for morning light.
- **Tea by 2 pm** at the latest; ginger water or lime juice after that.
- **Naps:** 20 minutes maximum, before 3 pm.
- **Wind-down 10:15:** phone charging in the hall; lights dimmed; journal (three good things); 10 pages of a paper book.
- **Lights out 10:45** if sleepy. If awake after about 20 minutes, sit in the hall with a dim light and read until sleepy.
- **Bedroom:** fan on, mosquito net, curtain fixed to block the street light.

Week 1 is hard: he is sleepy at 4 pm. By week 2 he falls asleep in about 20 minutes, sleeps 7 hours 5 minutes on average (from 6:10), and his quality rises to 3.5/5. His morning study block is more focused. He keeps the plan, allowing a later night for weddings but never moving the wake time by more than an hour.
""",
    apply=f"""
**Your two-week sleep plan:**
1. **Wake time** (same every day): ______. Alarm across the room.
2. **Morning light:** outdoors within 30 minutes of waking, for 10 to 30 minutes.
3. **Caffeine cut-off:** no tea or coffee after ______ (try 2 pm).
4. **Naps:** none, or 20 minutes before 3 pm.
5. **Wind-down (30 to 45 minutes):** phone out of the bedroom, dim lights, a calm routine (journal, reading, slow breathing).
6. **Bed for sleep only;** up after about 20 minutes awake, back when sleepy.
7. **Bedroom:** dark, quiet, cool as possible (fan, net, curtain).
8. **Worry time:** 10 minutes earlier in the evening to write worries and next steps.

{fence(tools.EVENING_ROUTINE)}

**Measure:** keep the sleep log for the two weeks and compare averages with your baseline.

**With others:** agree household quiet hours; if you share a room, discuss lights and phone use; offer the same plan to a family member who sleeps badly.
""",
    resources=[
        ('aasm', 'Re-read the recommendation: 7 or more hours, regularly', '5 minutes'),
        ('wellbeing', 'Set Bedtime mode to start at your wind-down time', '5 minutes'),
        ('os-4-3', 'From this page, go to the next section, 4.4 Sleep Problems and Disorders (insomnia, sleep apnoea), and read it', '15 minutes'),
    ],
    steps=[
        'Write your two-week sleep plan with all eight parts.',
        'Follow it for 14 days and keep the sleep log every morning.',
        'Compare average total sleep, time to fall asleep and quality with your baseline.',
        'Decide what to keep, and write your sleep window in your Playbook. Note any signs that you should see a doctor.',
    ],
    proof='Your written plan, a 14-day sleep log and a before-and-after comparison.',
    templates=[('Two-week sleep plan', """TWO-WEEK SLEEP PLAN            Start ______
Wake time (every day): ______   Morning light by ______
Caffeine cut-off: ______        Naps: none / 20 min before 3 pm
Wind-down from ______: phone out, dim lights, ______, ______
Lights out (when sleepy): ______  Awake ~20 min -> get up, dim light, return when sleepy
Bedroom fixes: ______  Worry time at ______
RESULTS            Baseline     Week 2
Total sleep        ___ h        ___ h
Time to fall asleep ___ min     ___ min
Quality (1-5)      ___          ___
See a doctor if: 3+ nights/week for 3 months, loud snoring with gasps,
severe daytime sleepiness, restless legs, or sleep problems with low mood.""", '')],
    mistakes=[
        ('Changing the wake time at weekends.', 'Keep it within an hour; that is what sets the clock.'),
        ('Lying in bed awake for hours.', 'Get up after about 20 minutes and return when sleepy.'),
        ('Trying strict sleep restriction alone.', 'Do it only with professional guidance.'),
        ('Taking sleeping pills or antihistamines without advice.', 'See a doctor; CBT-I is the first-line treatment.'),
    ],
    quiz=[
        Q('What is the first-line treatment for chronic insomnia recommended by major medical bodies?', 'CBT-I (cognitive behavioural therapy for insomnia)', 'Sleeping pills', 'Alcohol before bed', 'Longer naps', why='CBT-I has strong, lasting evidence.'),
        Q('What should you do if you can\'t sleep after about 20 minutes in bed?', 'Get up, do something calm in dim light, and return when sleepy', 'Scroll your phone in bed', 'Stay in bed and try harder', 'Drink coffee', why='Stimulus control keeps the bed linked with sleep.'),
        Q('Which single habit best sets your body clock?', 'A fixed wake time with morning light', 'A fixed dinner menu', 'A late nap', 'Sleeping in at weekends', why='Wake time and light anchor the circadian rhythm.'),
        Q('Which is a sign to see a doctor about sleep?', 'Loud snoring with gasping or pauses in breathing', 'One bad night before an exam', 'Dreaming', 'Waking briefly to drink water', why='These can be signs of sleep apnoea.'),
    ],
    study='read the lesson and set Bedtime mode',
    action='follow a two-week sleep plan with a daily log and compare with your baseline',
)

LESSONS = [L1, L2]

MODULE = module(
    19,
    overview=f"""
Sleep science and a practical sleep plan: sleep stages, the body clock and sleep pressure, how much adults need, caffeine, light, naps and alcohol, then a two-week plan built on CBT-I principles (fixed wake time, stimulus control, wind-down) with a log.

Sleep is the most underrated performance tool in this course. Short sleep quietly lowers attention, memory, mood and self-control, and you won't feel how much. The good news: a few habits, especially a fixed wake time and morning light, help most people within two weeks.

If you have persistent insomnia, loud snoring with gasping, or severe daytime sleepiness, see a doctor. CBT-I is the first-line treatment for chronic insomnia; avoid sleeping pills without medical advice.
""",
    outcomes=[
        'Explain sleep stages, the body clock and sleep pressure.',
        'Know the adult sleep recommendation and what harms sleep.',
        'Design and follow a sleep plan using CBT-I principles.',
        'Measure the change with a sleep log and know when to see a doctor.',
    ],
    lessons=LESSONS,
    project='a two-week sleep plan with a log',
    project_steps=[
        'Analyse your baseline sleep log (PD-M19-L01).',
        'Follow the two-week sleep plan (PD-M19-L02) with a daily log.',
        'Compare averages and write a half-page review.',
        'Write your sleep window and wind-down into your evening routine in the Playbook.',
    ],
    project_proof='Baseline and 14-day sleep logs, your plan and the half-page review.',
    rubric=[
        ('Understanding', 'Cannot explain the two systems', 'Explains one', 'Explains body clock, sleep pressure and caffeine'),
        ('Plan', 'No plan', 'A few changes', 'All eight parts written and followed'),
        ('Data', 'No log', 'Partial log', 'Baseline and 14-day logs with averages'),
        ('Safety', 'Ignores warning signs', 'Knows some signs', 'Knows when to see a doctor and avoids self-medicating'),
    ],
    short=[
        'Fix your wake time and get morning light for two weeks.',
        'Move your tea cut-off to 2 pm.',
    ],
    flashcards=[
        ('Two systems of sleep', 'Body clock (light) and sleep pressure (adenosine).'),
        ('Caffeine half-life', 'Roughly 5 hours on average, varying between people.'),
        ('Adult sleep recommendation', '7 or more hours a night, regularly.'),
        ('Best clock-setter', 'Fixed wake time plus morning daylight.'),
        ('Stimulus control', 'Bed for sleep only; up after about 20 minutes awake.'),
        ('First-line treatment for chronic insomnia', 'CBT-I.'),
        ('Alcohol and sleep', 'Helps you fall asleep, fragments sleep later.'),
        ('Good nap', '10–20 minutes, early afternoon.'),
    ],
    mistakes=[
        ('Cutting sleep to study more.', 'You lose more in attention and memory than you gain in hours.'),
        ('Perfectionism about sleep.', 'Worrying about sleep worsens it. Follow the plan; some bad nights are normal.'),
        ('Ignoring snoring with gasping.', 'Possible sleep apnoea: see a doctor.'),
    ],
    tools=[
        'The 7-day sleep log (PD-M19-L01).',
        'The two-week sleep plan and evening routine (PD-M19-L02).',
    ],
    playbook=[
        'My sleep window: lights out ______, wake ______ every day; morning light; tea by 2 pm.',
        'Bed is for sleep. Awake ~20 minutes → get up, dim light, return when sleepy.',
    ],
)
