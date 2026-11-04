from common import lesson, module, link, xref, table, Q

L1 = lesson(
    16, 1,
    outcome='You can explain how apps are designed to capture attention, what research says (and doesn\'t) about phones and wellbeing, and spot attention traps on your own phone.',
    split='20 minutes reading, 25 minutes of tasks',
    principle='Many apps are built to maximise your time on them using rewards that arrive unpredictably; the honest research shows small average harms, bigger for some people and some uses, so the aim is control, not panic.',
    science=f"""
**How attention is captured.** Most free apps earn money from advertising, so they are designed to keep you using them. Common design features:
- **Variable rewards:** you don't know what the next reel, notification or message will bring. B. F. Skinner's experiments showed that rewards on an unpredictable schedule produce the most persistent behaviour; slot machines use the same principle. Pull-to-refresh and endless feeds work similarly.
- **Infinite scroll and autoplay:** no natural stopping point.
- **Notifications and badges:** red dots and sounds that pull you back.
- **Social rewards:** likes, views and comments that tap into our need for approval.
- **Streaks:** fear of losing a streak keeps you returning (loss aversion, PD-M03-L01).

Some of these become **dark patterns** when they trick you into choices against your interest; India's consumer authority issued guidelines against 13 such patterns in 2023 (you will analyse them in PD-M32-L02).

**What research says about phones and wellbeing.** This is debated. Large studies by Amy Orben and Andrew Przybylski (2019), using data from hundreds of thousands of adolescents, found that the average link between digital technology use and wellbeing was **negative but very small**, comparable in size to the link with eating potatoes. Jonathan Haidt and others argue that heavy social-media use, especially among teenage girls, is a major cause of rising anxiety and depression; critics say the evidence is mostly correlational and mixed. Experiments where adults reduce or quit social media for one to four weeks have shown mixed but often small improvements in wellbeing. Points most researchers agree on:
- **How** you use it matters more than total hours: active use (messaging friends, learning) is less harmful than passive scrolling and comparison.
- **Displacement** matters: screen time that replaces sleep, exercise, study or face-to-face time causes real costs.
- Phones in the bedroom harm sleep for many people (Module 19).
- Some people are much more affected than others.

**Attention and phones.** In one study by Adrian Ward and colleagues (2017), students did worse on memory and attention tasks when their phone was on the desk, even face down and silent, than when it was in another room. A later replication by other researchers found **smaller or no effects**, so the "mere presence" effect is uncertain. But interruptions clearly hurt focused work: switching tasks has costs, and getting back into deep study after a notification takes time. The {xref('lrn', 'lrn-m05', 'Learning Capabilities focus module')} covers phone control for study in detail.
""",
    evidence=[
        ('Apps use variable rewards and endless feeds to increase use', 'strong', 'Documented design practice; matches classic learning research.'),
        ('Average link between screen use and wellbeing is small and negative', 'moderate', 'Large datasets; size and causality debated.'),
        ('Social media is the main cause of rising youth mental-health problems', 'mixed', 'Strongly argued but contested; evidence largely correlational.'),
        ('Passive scrolling is worse than active social use', 'moderate', 'Supported by several studies.'),
        ('Mere presence of a phone reduces attention', 'mixed', 'Original study striking; replication found small or no effects.'),
        ('Interruptions harm focused work', 'strong', 'Task-switching costs are well established.'),
    ],
    example="""
Sreeja checks Digital Wellbeing: 5 hours 40 minutes a day of screen time, 112 unlocks, top apps Instagram (2 h 10 min), YouTube (1 h 30 min), WhatsApp (1 h). She expected "about two hours".

She spots the traps: reels autoplay into the next one (no stopping point); she opens Instagram "just to check one message" and ends up in the feed (variable reward); a learning app's streak makes her open it daily for one minute, then she drifts to other apps; WhatsApp group notifications buzz 200 times a day.

She sorts her use into **active** (calls with her sister, a PSC group that shares PYQs, one good YouTube lecture) and **passive** (reels, random videos, scrolling status updates). About 70% is passive, much of it late at night, when it cuts into sleep. She decides not to quit her phone, but to take control (PD-M16-L02).
""",
    apply="""
**Audit your attention (20 minutes):**
1. Open Digital Wellbeing: write daily screen time, unlocks and your top five apps.
2. For each top app, list its traps: autoplay, infinite scroll, notifications, streaks, likes.
3. Label each app's use as mostly **active** (connecting, creating, learning with a goal) or **passive** (scrolling, watching without choosing).
4. Note **what it displaces**: sleep, study, exercise, family time?
5. Note **triggers**: when do you reach for the phone (boredom, a hard task, loneliness, waiting)?

**One quick change today:** turn off all non-human notifications (only calls and messages from real people) and turn off autoplay in YouTube and Instagram settings where available.

**With others:** don't lecture friends or family about screen time. Share what you're doing and invite them to join (a phone-free dinner, for example).
""",
    resources=[
        ('wellbeing', 'Open Digital Wellbeing and look at the dashboard, app timers and Focus mode', '10 minutes'),
        ('darkpatterns', 'Read the list of 13 dark patterns; note any you have met', '10 minutes'),
        ('crashcourse', 'Watch an episode on operant conditioning (#11, "How to Train a Brain") to understand variable rewards', '10 minutes'),
    ],
    steps=[
        'Do the attention audit and write the results.',
        'Turn off non-human notifications and autoplay where possible.',
        'For two days, each time you unlock without a plan, write the trigger in one word (bored, avoiding, lonely, waiting…).',
        'Write your three biggest attention traps and what they displace.',
    ],
    proof='Your audit (screen time, unlocks, top five apps with traps, active versus passive), a screenshot of changed notification settings, two days of trigger words, and your top three traps.',
    templates=[('Attention audit', """ATTENTION AUDIT                       Date ______
Daily screen time ___ h ___ min   Unlocks ___ /day
App | Time/day | Traps (autoplay / scroll / notifications / streak / likes) | Active or passive | Displaces (sleep / study / exercise / people)
1. ______ | ___ | ______ | ______ | ______
...
Unplanned unlock triggers (2 days): bored __ avoiding __ lonely __ waiting __ habit __
Top three traps: 1 ______ 2 ______ 3 ______""", '')],
    mistakes=[
        ('Panic about "phone addiction".', 'The average harm is small; focus on what your use displaces and how it makes you feel.'),
        ('Counting all screen time as bad.', 'Calling family, learning and creating are different from passive scrolling.'),
        ('Blaming yourself.', 'Apps are designed by experts to hold attention. Change the design of your phone, not your character.'),
        ('Believing every scary headline.', 'Check study type and size (Module 2).'),
    ],
    quiz=[
        Q('Why are endless feeds and pull-to-refresh so hard to stop?', 'They give unpredictable (variable) rewards, which produce persistent behaviour', 'They are boring', 'They tire the eyes', 'They are paid apps', why='Variable rewards are the most habit-forming schedule.'),
        Q('What did large studies by Orben and Przybylski find?', 'A negative but very small average link between technology use and wellbeing', 'Huge harm for everyone', 'Phones improve wellbeing a lot', 'No studies existed', why='The average association was very small.'),
        Q('Which use is generally less harmful?', 'Active use, such as messaging friends or learning with a goal', 'Passive scrolling late at night', 'Autoplay videos for hours', 'Checking likes every few minutes', why='How you use it matters more than total time.'),
        Q('What happened when researchers tried to replicate the "phone on the desk" attention study?', 'They found smaller or no effects', 'They found much bigger effects', 'They never tried', 'Phones improved attention', why='The mere-presence effect is uncertain.'),
    ],
    study='read the lesson and look through Digital Wellbeing',
    action='do the attention audit, change notifications and autoplay, and log unlock triggers for two days',
)

L2 = lesson(
    16, 2,
    outcome='You can set up a personal phone plan (home screen, notifications, timers, phone-free zones) and complete a digital-detox day.',
    split='15 minutes reading, 30 minutes of setup, plus one detox day',
    principle='Small changes in friction and cues (where the phone lives, what is on the home screen, which notifications reach you) change behaviour more than willpower; a planned detox day shows you what the phone has been replacing.',
    science="""
**Design beats willpower here too.** Everything from Module 8 applies to phones: **remove cues** (notifications, icons on the home screen), **add friction** (log out, use the browser instead of the app, grey-scale mode), **use place** (phone-free bedroom and study desk), and **if-then plans** ("If I sit down to study, then the phone goes to the shelf by the door").

**What helps, from studies:**
- **Turning off notifications:** in a field study by Kostadin Kushlev and colleagues (2016), people who kept notifications off for a week reported less inattention and hyperactivity than when notifications were on; batching notifications a few times a day also improved wellbeing in another study.
- **Phone out of the bedroom:** linked to better sleep in several studies (screens and light delay sleep; night-time checking interrupts it).
- **Time limits:** app timers help some people; others simply override them, so combine timers with friction.
- **Grey-scale mode:** small studies found it reduced screen time slightly; evidence is limited.
- **Short breaks from social media:** studies of one-week to one-month breaks found small improvements in wellbeing for some, with large individual differences.

**Digital-detox days.** There is little research on single detox days, so treat it as a **personal experiment**: what do you do instead, how do you feel, what did you miss and not miss? People commonly report feeling anxious for the first hours (a sign of habit), then calmer, with more time for people and activities. Some report feeling cut off; that is useful information too.

**Be realistic.** You need your phone for family, PSC notifications (OTR updates, admit cards), banking and study groups. The aim is not to quit but to decide **when, where and why** you use it. Make sure essential calls can still reach you during a detox day.
""",
    evidence=[
        ('Turning off or batching notifications improves attention and wellbeing', 'moderate', 'Several field experiments; effects modest.'),
        ('Phones out of the bedroom improve sleep', 'moderate', 'Supported by sleep research and several studies.'),
        ('App timers reduce use', 'mixed', 'Helpful for some; many override them.'),
        ('Grey-scale mode reduces use', 'mixed', 'A few small studies.'),
        ('Single digital-detox days', 'tool', 'Little direct research; run it as a personal experiment.'),
    ],
    example="""
Ashiq's phone plan:

- **Home screen:** only Phone, Messages, Camera, Maps, Loop, Medito and the Kerala PSC app. Instagram and YouTube moved to a folder on the last screen; Instagram used in the browser only.
- **Notifications:** only calls, SMS and WhatsApp from family and two groups; all others off. PSC group muted, checked at 8 pm.
- **Places:** phone charges in the hall at night (an old alarm clock in the bedroom); during study blocks it stays on the shelf by the door.
- **Timer:** YouTube 45 minutes a day in Digital Wellbeing; Bedtime mode from 10 pm.
- **If-then:** "If I unlock without a reason, I put it face down and take three breaths."

On Sunday he does a **digital-detox day**: he tells his family and two friends in advance, gives his mother the number of a neighbour for emergencies, and keeps calls on. The first two hours he reaches for his pocket "every five minutes". By afternoon he has helped his father in the garden, read 60 pages, walked to a friend's house and slept an hour. In the evening he checks: he missed nothing important. Screen time the following week drops from 4 h 50 min to 3 h 10 min a day.
""",
    apply="""
**Your phone plan (30 minutes):**
1. **Home screen:** keep only tools; move entertainment apps off the first screen or into a folder.
2. **Notifications:** allow only real people and essentials; mute groups and check them at set times.
3. **Places:** phone-free bedroom (use an alarm clock) and phone-free study desk.
4. **Limits:** app timers for your top two passive apps; Bedtime or Focus mode at night.
5. **One if-then plan** for unplanned unlocks.
6. **Weekly check:** screen time and unlocks in your Sunday reflection.

**The digital-detox day:**
- Choose a day (Sunday works for many); tell family and friends; make sure emergency calls can still reach you.
- Phone off or in a drawer except for calls; no social media, no video.
- Plan the day: a walk, a visit, reading, a hobby, helping at home.
- In the evening write: what I did, how I felt at three points of the day, what I missed, what I didn't.

**With others:** suggest a phone-free family dinner or a phone-free study-group hour. Lead by example.
""",
    resources=[
        ('wellbeing', 'Set app timers, Bedtime mode and Focus mode (steps vary by phone)', '15 minutes'),
        ('loop', 'Add "Phone out of the room for the first study block" if you haven\'t already', '5 minutes'),
        ('seneca', 'Read Letter 2 ("On Discursiveness in Reading"): Seneca on scattered attention', '10 minutes'),
    ],
    steps=[
        'Set up your phone plan (all six parts) and take before-and-after home-screen screenshots.',
        'Run the plan for one week; record daily screen time and unlocks.',
        'Do a digital-detox day and write the evening reflection.',
        'Compare the week before (from your PD-M16-L01 audit) with the week after, and keep or adjust each part of the plan.',
    ],
    proof='Before-and-after home-screen screenshots, a week of screen-time and unlock numbers, and your detox-day reflection.',
    templates=[('Phone plan and detox day', """MY PHONE PLAN
Home screen keeps only: ______________________
Notifications allowed: calls, ______; groups muted, checked at ______
Phone-free places: bedroom (alarm clock instead), study desk, ______
Timers: ______ ___ min/day, ______ ___ min/day; Bedtime mode from ______
If I unlock without a reason, then I ______________________.
Weekly numbers: screen time ___ (before ___); unlocks ___ (before ___)

DIGITAL-DETOX DAY          Date ______  Told: ______  Emergency contact: ______
Plan: morning ______ afternoon ______ evening ______
Feeling (0-10): 10 am ___  2 pm ___  8 pm ___
What I did instead: ______  Missed: ______  Didn't miss: ______""", '')],
    mistakes=[
        ('Going cold turkey without a plan.', 'Empty time pulls you back to the phone. Plan what you will do instead.'),
        ('Cutting off essential contact.', 'Keep calls on and tell family. Safety first.'),
        ('Relying only on timers.', 'Timers are easy to override. Combine them with friction and place.'),
        ('Judging the detox by the first hours.', 'Restlessness early is normal. Judge by the evening reflection.'),
    ],
    quiz=[
        Q('Which phone change has the best support for improving attention?', 'Turning off or batching non-essential notifications', 'Buying a new phone', 'Using dark mode', 'Changing the wallpaper', why='Field experiments found reduced inattention.'),
        Q('Why keep the phone out of the bedroom?', 'It is linked to better sleep: less light and night-time checking', 'Phones explode at night', 'To save battery', 'It makes no difference', why='Screens and checking delay and interrupt sleep.'),
        Q('What is the honest status of a single digital-detox day?', 'Little direct research; treat it as a personal experiment', 'Proven to cure anxiety', 'Proven harmful', 'Required by law', why='Run it and record what you learn.'),
        Q('What is the best first step before a detox day?', 'Tell family, keep calls on for emergencies and plan activities', 'Delete all apps permanently', 'Throw the phone away', 'Do it without telling anyone', why='Safety and a plan make it work.'),
    ],
    study='read the lesson and set up Digital Wellbeing tools',
    action='set up your phone plan, track a week, and do a digital-detox day with a reflection',
)

LESSONS = [L1, L2]

MODULE = module(
    16,
    overview=f"""
Digital wellbeing and attention: how apps capture attention (variable rewards, infinite scroll, streaks), what the research honestly says about phones and wellbeing, and a personal phone plan plus a digital-detox day.

Part B ends with the device you touch more than anything else. The aim is not to fear your phone but to decide when, where and why you use it, using the same design tools as Module 8: remove cues, add friction, use places, write if-then plans.

The detox day here is also one of the comfort-zone challenges from Module 14. For study-focused phone control, see {xref('lrn', 'lrn-m05', 'the Learning Capabilities focus module')}.
""",
    outcomes=[
        'Explain how apps capture attention and name common traps.',
        'Summarise what research says (and doesn\'t) about screens and wellbeing.',
        'Audit your own use: time, unlocks, traps, active versus passive, triggers.',
        'Set up a phone plan and complete a digital-detox day.',
    ],
    lessons=LESSONS,
    project='a phone plan with before-and-after numbers and a detox day',
    project_steps=[
        'Do the attention audit (PD-M16-L01).',
        'Set up the phone plan and run it for two weeks (PD-M16-L02).',
        'Do one digital-detox day.',
        'Compare screen time, unlocks and your mood and sleep ratings before and after; write a half-page review.',
    ],
    project_proof='The audit, the phone plan, two weeks of numbers, the detox reflection and the half-page review.',
    rubric=[
        ('Understanding', 'Thinks all screen time is equally harmful', 'Knows some traps', 'Explains traps and the honest evidence'),
        ('Audit', 'No numbers', 'Screen time only', 'Time, unlocks, apps, traps, triggers and displacement'),
        ('Plan', 'No changes', 'One or two changes', 'All six parts set up and used for two weeks'),
        ('Detox', 'Not done', 'Done without reflection', 'Done with a planned day and evening reflection'),
    ],
    short=[
        'Turn off non-human notifications and keep the phone out of the bedroom.',
        'Do a half-day detox instead of a full day.',
    ],
    flashcards=[
        ('Variable rewards', 'Unpredictable rewards: the most habit-forming schedule (feeds, refresh).'),
        ('Average screen–wellbeing link', 'Negative but very small in large studies; debated.'),
        ('Active versus passive use', 'Active (connecting, learning) is less harmful than passive scrolling.'),
        ('Displacement', 'The real cost: screens replacing sleep, study, exercise, people.'),
        ('Phone on the desk (mere presence)', 'Original effect uncertain after replication.'),
        ('Best-supported phone change', 'Turn off or batch non-essential notifications.'),
        ('Detox day rules', 'Tell people, keep calls on, plan activities, reflect in the evening.'),
    ],
    mistakes=[
        ('All-or-nothing thinking about phones.', 'Aim for control, not perfection.'),
        ('Forgetting essential notifications.', 'PSC updates, bank alerts and family calls must still reach you.'),
        ('Letting the plan drift.', 'Check numbers every Sunday.'),
    ],
    tools=[
        'The attention audit (PD-M16-L01).',
        'The phone plan and digital-detox day sheet (PD-M16-L02).',
    ],
    playbook=[
        'My phone plan: tools on the home screen, only people notify me, no phone in the bedroom or at the study desk.',
        'One digital-detox day every month.',
    ],
)
