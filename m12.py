from common import lesson, module, link, xref, table, Q

L1 = lesson(
    12, 1,
    outcome='You can do a basic breath-focused meditation and two breathing exercises, explain what meditation research really shows, and start a 30-day meditation challenge.',
    split='15 minutes reading, 10 minutes a day for 30 days',
    principle='Mindfulness meditation trains attention and acceptance; it helps anxiety, depression and pain moderately, about as much as other active treatments, not more, and it works through regular short practice.',
    science=f"""
**What mindfulness is.** Jon Kabat-Zinn, who created the **Mindfulness-Based Stress Reduction (MBSR)** programme in 1979, defined mindfulness as paying attention on purpose, in the present moment, without judging. It draws on Buddhist and other contemplative traditions; India has its own long traditions of meditation and dhyana (you will meet dhyana in the Common Yoga Protocol, Module 18). Modern programmes are secular.

**The basic practice.** Sit comfortably, attend to the breath (at the nostrils or belly). The mind will wander, often within seconds. Notice that it has wandered, then gently bring attention back. **The returning is the exercise**, like a repetition in the gym. You are not trying to empty the mind or feel blissful.

**What the research shows.** The best-known review, by Madhav Goyal and colleagues in *JAMA Internal Medicine* (2014), pooled 47 randomised trials with 3,515 people. Mindfulness programmes showed **moderate evidence** of improving **anxiety** (effect size about 0.38 at 8 weeks), **depression** (about 0.30) and **pain** (about 0.33), and low evidence for stress and quality of life. There was insufficient or low evidence for effects on attention, sleep, mood and weight, and **no evidence that meditation was better than other active treatments** such as exercise or therapy ({link('goyal', 'Goyal et al., 2014')}). **Mindfulness-Based Cognitive Therapy (MBCT)** has good evidence for reducing relapse in people with recurrent depression.

**Honest cautions.** Many studies are small, use waiting-list controls and rely on self-report; brain-change findings are often over-hyped in the media. A minority of people report unpleasant experiences (anxiety, distressing memories) during intensive meditation; if that happens, shorten sessions, open your eyes, try walking meditation or stop and seek advice. Ten minutes a day is not dangerous for most people.

**Breathwork.** Slow breathing (about six breaths a minute, PD-M11-L01) and the **physiological sigh** (two inhales through the nose, a long exhale through the mouth) are quick ways to calm the body. Pranayama practices such as **Nadi Shodhana** (alternate-nostril breathing) and **Bhramari** (humming bee breath) are taught in the Common Yoga Protocol (Module 18). Avoid forceful breath-holding or hyperventilation techniques promoted online.

**Apps.** {link('medito', 'Medito')} is free, from a non-profit foundation, open source and works on Android, with guided sessions from 5 minutes.
""",
    evidence=[
        ('Mindfulness programmes reduce anxiety, depression and pain', 'moderate', 'Meta-analysis of 47 trials: small-to-moderate effects; not better than other active treatments.'),
        ('MBCT reduces depression relapse in recurrent depression', 'strong', 'Several trials and reviews.'),
        ('Meditation improves attention, sleep or weight', 'mixed', 'Low or insufficient evidence in the main review.'),
        ('Slow breathing calms the body', 'moderate', 'Several small trials.'),
        ('Dramatic "meditation rewires your brain" headlines', 'mixed', 'Brain findings come from small studies and are often overstated.'),
    ],
    example="""
Ashiq starts the 30-day challenge with Medito's 5-minute sessions after his morning tea, sitting on the veranda. Day 1: his mind wanders "about 40 times" and he feels he is failing. On day 4 he reads that noticing and returning is the exercise, and stops judging. By day 12 he does 10 minutes and notices a small change: when his uncle criticises him at lunch, he catches the anger rising in his chest a second earlier and takes one slow breath before replying.

He misses days 15 and 16 (a wedding) and does a 2-minute version on day 17 rather than quitting. On day 30 he writes: "Not calm all the time. I notice my mind faster. Sleep about the same. Keep 10 minutes, 5 days a week." That honest result matches the research: modest, real, practice-dependent.
""",
    apply="""
**Basic breath meditation (5 to 10 minutes):**
1. Sit upright but relaxed, on a chair or the floor. Set a timer. Eyes closed or looking down.
2. Feel three slow breaths.
3. Rest attention on the natural breath at the nostrils or belly.
4. When the mind wanders (it will), notice "thinking", and gently return. No scolding.
5. At the end, notice how you feel; open your eyes slowly.

**Two breathing tools for daily life:**
- **Slow breathing:** in for 4, out for 6, for 2 to 5 minutes (before study, in the exam hall, before a hard conversation).
- **Physiological sigh:** two inhales through the nose, one long exhale through the mouth; repeat two or three times.

**The 30-day meditation challenge:** same time and place each day (anchor it: "After my morning tea, I sit for 5 minutes"); start at 5 minutes, grow to 10; tick it in Loop; never miss twice; on day 30 write an honest review.

**With others:** do a 5-minute sit with a friend or family member; don't preach meditation or promise it will fix their problems.
""",
    resources=[
        ('medito', 'Install the app and do a 5-minute beginner session', '10 minutes'),
        ('goyal', 'Read the abstract: what meditation helps and what it does not', '5 minutes'),
        ('nhs-yoga', 'Optional: try one short relaxation or yoga video if you prefer moving meditation', '10 minutes'),
    ],
    steps=[
        'Install Medito (or use a simple timer) and add "Meditation (5 to 10 minutes)" to Loop with a reminder at your anchor time.',
        'Meditate every day for 30 days, starting with 5 minutes. Note the minutes and one word about the session.',
        'Use slow breathing or the physiological sigh at least once in a real stressful moment and note what happened.',
        'On day 30, write a five-line review: days done, average minutes, what changed, what didn\'t, whether you will continue.',
    ],
    proof='A Loop or Medito screenshot showing the 30 days, your session notes, one real-moment breathing note and the five-line review.',
    templates=[('30-day meditation log', """30-DAY MEDITATION CHALLENGE      Anchor: After ______, I sit for ___ minutes.
Day | Date | Minutes | One word (restless / calm / sleepy / focused...) | Mind wandered (few / many)
1 | ____ | __ | ______ | ______
...
Real-moment breathing: Date ____ Situation ______ Tool (slow / sigh) ______ Result ______
DAY-30 REVIEW
Days done ___/30  Average minutes ___
What changed: ______  What didn't: ______  Continue? ___ min, ___ days a week""", '')],
    mistakes=[
        ('Thinking a wandering mind means failure.', 'Noticing and returning is the practice.'),
        ('Expecting dramatic results.', 'Research shows modest benefits with regular practice. Judge by your 30-day review, not by one session.'),
        ('Long sessions too soon.', 'Start with 5 minutes. Consistency beats length.'),
        ('Ignoring distress during practice.', 'If meditation brings up strong distress, shorten it, try walking meditation or stop and get advice.'),
    ],
    quiz=[
        Q('In a mindfulness session, what is the core exercise?', 'Noticing the mind has wandered and gently returning to the breath', 'Emptying the mind of all thoughts', 'Feeling blissful', 'Breathing as fast as possible', why='Returning attention is the repetition that trains it.'),
        Q('What did the 2014 review of 47 trials find?', 'Moderate evidence for anxiety, depression and pain; not better than other active treatments', 'Meditation cures all mental illness', 'No benefits at all', 'Big improvements in weight and sleep', why='Goyal et al. found small-to-moderate effects and no superiority over active treatments.'),
        Q('What is the physiological sigh?', 'Two inhales through the nose and one long exhale through the mouth', 'Holding the breath for a minute', 'Breathing only through the mouth', 'A loud yawn', why='A quick calming breath pattern.'),
        Q('What should you do if you miss two days of the challenge?', 'Do a short version the next day and continue', 'Restart from day 1 with longer sessions', 'Give up', 'Do three sessions at once', why='Never miss twice; restart with a tiny version.'),
    ],
    study='read the lesson and the Goyal abstract, and do a first 5-minute session',
    action='complete the 30-day meditation challenge and write the day-30 review',
)

L2 = lesson(
    12, 2,
    outcome='You can use three journaling methods (three good things, expressive writing and a daily log) and run a 30-day journaling challenge with honest expectations.',
    split='15 minutes reading, 5 minutes a day for 30 days',
    principle='Writing a few lines a day about what went well and what you learned helps many people modestly; writing about difficult experiences can help too, but gratitude is not a cure and forcing it can backfire.',
    science=f"""
**Gratitude practices.** In a study by Robert Emmons and Michael McCullough (2003), people who wrote weekly lists of things they were grateful for reported feeling better about their lives than people who listed hassles or neutral events. Martin Seligman and colleagues (2005) tested the **Three Good Things** exercise (each night, write three things that went well and why) and found improvements in happiness and depressive symptoms that lasted months in some participants ({link('ggia-3gt', 'Greater Good in Action: Three Good Things')}). A 2016 meta-analysis by Davis and colleagues found that gratitude interventions had **small** effects on wellbeing compared with neutral activities, and smaller still compared with other positive activities. Sonja Lyubomirsky found in one study that counting blessings once a week worked better than three times a week, perhaps because daily practice became routine. So: helpful for many, modest in size, and best kept fresh.

**Expressive writing.** James Pennebaker's research from the 1980s found that writing about stressful or traumatic experiences for 15 to 20 minutes on three or four days led to fewer doctor visits and better mood weeks later in many studies. Meta-analyses find **small** average benefits, with large variation between studies. People often feel worse immediately after writing and better later. This is different from rumination: the writing makes sense of the experience rather than replaying it. If writing about a trauma overwhelms you, stop and seek professional support.

**Daily logs and reflection.** Short daily notes (what I did, what I learned, one win) support memory, progress awareness (the progress principle, PD-M06-L02) and the weekly review. The evening review in PD-M11-L03 is one version.

**Kerala note.** Many people already practise gratitude through prayer or thanking elders. Journaling adds two things: **specific** details ("my mother made pathiri even though she was tired") and **why** it happened, which seems to be part of what makes the exercise work.
""",
    evidence=[
        ('Gratitude interventions improve wellbeing', 'moderate', 'Many trials, but a meta-analysis found small effects versus neutral activities.'),
        ('Three Good Things', 'moderate', 'Positive results in trials, including follow-ups of months; effects modest.'),
        ('Expressive writing about stressful events', 'moderate', 'Small average benefits across many studies, with wide variation.'),
        ('Daily practice always beats weekly practice', 'mixed', 'One study found weekly gratitude worked better; findings vary.'),
    ],
    example="""
Sreeja keeps a small notebook by her bed for the 30-day challenge. Each night she writes:

**Three good things (and why):** "1. Solved 8/10 percentage questions: because I practised the method daily. 2. Amma laughed at my imitation of the bus conductor: because I made time to talk with her after dinner. 3. Rain stopped just as I walked home: luck!"

**One line of the day:** "Studied 3 h; walk done; argued with my brother, then apologised."

On day 9, after a bad mock, she does **expressive writing** instead: 15 minutes about her fear of failing again and what her family expects. She feels worse that night and better the next morning, with a clearer plan. By day 20 the three good things feel repetitive, so she varies them: one day "three people I'm grateful for", another "three small pleasures". Her day-30 review: "Small lift in mood, more noticing of good moments, best for my sleep routine. Keep it, but four nights a week."
""",
    apply="""
**Three methods (choose one or rotate):**

1. **Three good things (3–5 minutes, at night):** write three things that went well today and, for each, why it happened. Be specific. Include small things.
2. **Expressive writing (15 minutes, when something is weighing on you):** write your deepest thoughts and feelings about it, without worrying about grammar. Do it for 3–4 days. Stop if it overwhelms you.
3. **Daily log (2 minutes):** one line on what you did, one on what you learned, one win.

**The 30-day journaling challenge:** 5 minutes a night, anchored to your evening routine (after brushing teeth, in bed). Rotate prompts when it gets stale. Never miss twice. Day-30 honest review.

**With others:** a **gratitude letter** or message to someone who helped you (a teacher, a relative) is one of the stronger short-term mood boosters in studies, for you and for them. Make it specific: what they did, how it affected you.
""",
    resources=[
        ('ggia-3gt', 'Read the practice: how to do it, why it works and the evidence', '10 minutes'),
        ('ggia', 'Search for "Gratitude Letter" and read the practice', '10 minutes'),
        ('ggsc', 'Take the free Gratitude quiz (under Quizzes) now and again on day 30', '10 minutes'),
    ],
    steps=[
        'Choose your journal (a small notebook or a Joplin note) and add "Journal (5 minutes)" to Loop.',
        'Write every night for 30 days, mainly Three Good Things with why, plus a one-line log.',
        'Do one expressive-writing session (15 minutes on 3 days) if something is weighing on you during the 30 days.',
        'Send one specific gratitude message or letter to someone who helped you.',
        'On day 30, retake the Gratitude quiz and write a five-line review.',
    ],
    proof='Photos or screenshots of journal entries across the 30 days, your gratitude message (or a note of it), quiz scores at start and day 30, and your review.',
    templates=[('Journal prompts', """NIGHTLY JOURNAL (5 minutes)
Three good things today, and why:
1. ______________________ because ______________________
2. ______________________ because ______________________
3. ______________________ because ______________________
Log: Did ______  Learned ______  Win ______
ROTATING PROMPTS (when it gets stale)
- Three people I'm grateful for, and one thing each did
- Three small pleasures today (food, weather, music)
- One thing I'm looking forward to tomorrow
- One mistake and what it taught me
- One thing about my body I'm thankful for
EXPRESSIVE WRITING (15 minutes, 3-4 days): my deepest thoughts and feelings about ______""", '')],
    mistakes=[
        ('Writing the same three things every night.', 'Vary prompts and be specific; routine dulls the effect.'),
        ('Forcing gratitude to cover real problems.', 'Gratitude is not denial. Write about problems too (expressive writing) and act on them.'),
        ('Expecting a big transformation.', 'Effects are modest. Judge by your day-30 review.'),
        ('Continuing expressive writing that overwhelms you.', 'Stop, and talk to a professional if a past event keeps causing distress.'),
    ],
    quiz=[
        Q('What does the Three Good Things exercise ask you to write?', 'Three things that went well today and why each happened', 'Three goals for tomorrow', 'Three problems to solve', 'Three people who annoyed you', why='Specific good events plus their causes.'),
        Q('What did a 2016 meta-analysis find about gratitude interventions?', 'Small effects on wellbeing compared with neutral activities', 'Huge effects for everyone', 'They make people worse', 'No studies existed', why='Davis et al. found modest effects.'),
        Q('How do people often feel right after expressive writing about a stressful event?', 'Worse at first, and often better later', 'Immediately cured', 'Nothing at all', 'Always better at once', why='Short-term distress, later benefit, in many studies.'),
        Q('Which is a strong short-term mood booster in studies?', 'A specific gratitude letter to someone who helped you', 'Complaining to friends', 'Scrolling social media', 'Writing a to-do list', why='Gratitude letters and visits showed strong short-term effects.'),
    ],
    study='read the lesson and the Three Good Things practice',
    action='complete the 30-day journaling challenge, send one gratitude message and write the day-30 review',
)

LESSONS = [L1, L2]

MODULE = module(
    12,
    overview=f"""
Mindfulness, breathwork, journaling and gratitude, with honest evidence: modest, real benefits from regular short practice. You run two 30-day challenges side by side: 5 to 10 minutes of meditation in the morning and 5 minutes of journaling at night.

These are the "maintenance" habits of the mind. None of them is magic, and the research says so: meditation helps anxiety, depression and pain about as much as other active approaches; gratitude has small effects. But they are free, take minutes, and combine well with everything else in the course.

The two challenges start together and are tracked on the Daily system track (days 10, 20 and 30). If 15 minutes a day is too much right now, do meditation first and add journaling when the first habit is steady.
""",
    outcomes=[
        'Do a basic breath meditation, slow breathing and the physiological sigh.',
        'Explain what meditation research shows and what it does not.',
        'Use Three Good Things, expressive writing and a daily log.',
        'Complete 30-day meditation and journaling challenges with honest reviews.',
    ],
    lessons=LESSONS,
    project='30-day meditation and journaling challenges',
    project_steps=[
        'Run both 30-day challenges (PD-M12-L01 and PD-M12-L02), tracked in Loop.',
        'At days 10, 20 and 30, tick the checkpoints on the Daily system track.',
        'On day 30, write a combined half-page review: days done, changes noticed, what you will keep and at what dose.',
        'Add your keeper routine to your morning and evening routines in the Playbook.',
    ],
    project_proof='Loop screenshots for both challenges, your day-30 reviews and the updated routines.',
    rubric=[
        ('Meditation', 'Fewer than 15 days', '15 to 24 days', '25 or more days with notes'),
        ('Journaling', 'Fewer than 15 nights', '15 to 24 nights', '25 or more nights, with varied prompts'),
        ('Honesty', 'Claims dramatic results without data', 'General impressions', 'A review with numbers and both changes and non-changes'),
        ('Integration', 'Nothing kept', 'Vague plan to continue', 'A specific keeper routine in the Playbook'),
    ],
    short=[
        'Meditate 3 minutes a day and write one good thing a night.',
        'Use the physiological sigh in stressful moments.',
    ],
    flashcards=[
        ('Mindfulness (Kabat-Zinn)', 'Paying attention on purpose, in the present, without judging.'),
        ('Core meditation exercise', 'Notice the mind wandered; gently return.'),
        ('Meditation evidence (47 trials)', 'Moderate for anxiety, depression, pain; not better than other active treatments.'),
        ('Physiological sigh', 'Two nasal inhales, one long mouth exhale.'),
        ('Three Good Things', 'Three things that went well and why, each night.'),
        ('Gratitude effect size', 'Small, compared with neutral activities.'),
        ('Expressive writing', '15–20 minutes about a stressful event, 3–4 days; small average benefits.'),
    ],
    mistakes=[
        ('Doing both challenges perfectly or not at all.', 'Short versions on bad days keep the habit alive.'),
        ('Using mindfulness to push away problems.', 'It is about seeing clearly, then acting.'),
        ('Overselling these practices to others.', 'Share honestly: "It helps me a bit; research says modest benefits."'),
    ],
    tools=[
        'The 30-day meditation log (PD-M12-L01).',
        'Nightly journal prompts with rotations and expressive writing (PD-M12-L02).',
    ],
    playbook=[
        'Morning: ___ minutes of meditation after ______. Stressful moment: slow breathing or two sighs.',
        'Night: three good things and why, ___ nights a week.',
    ],
)
