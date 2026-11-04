from common import lesson, module, link, xref, table, Q
import tools

L1 = lesson(
    11, 1,
    outcome='You can explain the stress response, tell helpful from harmful stress, use three fast calming tools, and recognise the signs that mean it is time to get professional help.',
    split='20 minutes reading, 25 minutes of tasks',
    principle='Stress is the body preparing to meet a demand; short bursts can help you perform, but long, uncontrollable stress harms health, and some signs mean you should get professional help rather than cope alone.',
    science=f"""
**The stress response.** When you face a threat or demand (an interview, an exam, a family argument), the brain triggers two systems. The fast **sympathetic nervous system** releases adrenaline: heart rate and breathing rise, muscles tense, digestion slows ("fight or flight", described by Walter Cannon). A slower hormonal chain, the **HPA axis** (hypothalamus, pituitary, adrenal glands), releases **cortisol**, which mobilises energy. Hans Selye described the pattern of alarm, resistance and exhaustion under prolonged stress. When the demand ends, the **parasympathetic** system calms the body ("rest and digest"). OpenStax Psychology 2e chapter 14 covers this in detail.

**Helpful and harmful stress.** Moderate, short stress can sharpen performance (the old Yerkes-Dodson idea that performance rises with arousal up to a point, then falls, is a rough description, not a precise law). Harm comes from **chronic** stress: weeks or months of pressure with little control or recovery. It is linked to poorer sleep, raised blood pressure, weaker immune response, low mood and anxiety.

**What makes stress worse or better:** lack of control, unpredictability, isolation and rumination make it worse; a sense of control, social support, physical activity, sleep and problem-solving make it better. Research on **"stress mindset"** by Alia Crum and others suggests that seeing stress as a challenge that can help you can improve how people respond; the evidence is promising but still developing.

**Fast calming tools with evidence:**
1. **Slow breathing:** breathing at about six breaths a minute (for example, in for 4 seconds, out for 6) increases heart-rate variability and activates calming systems; small studies show reduced anxiety. A 2023 Stanford study by Balban and colleagues found five minutes a day of "cyclic sighing" (a double inhale through the nose, long exhale through the mouth) improved mood more than mindfulness meditation over a month, in a small trial.
2. **Movement:** a brisk 10-minute walk burns off stress hormones and lifts mood (Module 17).
3. **Talking to someone you trust:** social support is one of the strongest buffers against stress.
4. **Writing it down:** expressive writing about worries before an exam helped anxious students (PD-M08-L04).

**When to get help: this course is not therapy.** See a doctor or mental-health professional if, for **two weeks or more**:
- you feel low, hopeless or empty most of the day, or have lost interest in things you used to enjoy;
- worry or panic is hard to control and stops you studying, working or sleeping;
- sleep or appetite has changed a lot;
- you are using alcohol, tobacco or other substances to cope;
- you feel you can't manage daily tasks.

**Get help immediately** if you have thoughts of harming yourself or ending your life, or if someone else is in danger. In India, **Tele-MANAS** is a toll-free, 24x7 national mental health helpline: **14416** or **1-800-89-14416**, in the language you choose ({link('telemanas', 'verified ' + '2026-11-04')}). In an emergency call **112** or go to the nearest hospital. Your local Family Health Centre (Primary Health Centre) doctor can also advise and refer you. Asking for help is a sign of good judgement, not weakness.
""",
    evidence=[
        ('Stress response: sympathetic system and HPA axis', 'strong', 'Well established in physiology and psychology.'),
        ('Chronic stress harms sleep, mood and health', 'strong', 'Large body of evidence, including long-term studies.'),
        ('Social support buffers stress', 'strong', 'Consistent across many studies and countries.'),
        ('Slow breathing reduces anxiety', 'moderate', 'Several small trials; effects are real but modest.'),
        ('Yerkes-Dodson curve as a precise law', 'mixed', 'A rough description; the original study was about mice and the exact shape is debated.'),
        ('Stress-is-helpful mindset', 'mixed', 'Promising studies; still being tested.'),
    ],
    example="""
Two weeks before the Degree Level prelims, Anu feels her heart racing at night, her jaw is tight and she can't fall asleep. She has been studying 10 hours a day and has stopped seeing friends.

She recognises the stress response and uses three tools: **slow breathing** (in for 4, out for 6) for five minutes before bed; a **20-minute walk** every evening with her cousin, which also brings back some **social support**; and **writing her worries** on paper for 10 minutes before sitting down to study. She also cuts her day to 8 hours with proper breaks; her mock scores don't drop.

Her friend Shamna, by contrast, has felt hopeless and empty for over a month, barely eats and says she "doesn't see the point". Anu recognises these are signs to get help, not to cope alone. She sits with Shamna while she calls Tele-MANAS (14416), and goes with her to the Family Health Centre the next week. Shamna is now seeing a counsellor and is doing better.
""",
    apply="""
**Your stress plan (fill it in once, keep it in your Playbook):**

1. **My early warning signs** (body, thoughts, behaviour): for example, tight jaw, skipping meals, scrolling at 1 am, snapping at family.
2. **Fast tools** (5 minutes): slow breathing (4 in, 6 out) or two cyclic sighs; a walk; cold water on the face; calling one person.
3. **Daily buffers:** sleep window, movement, one real conversation, a break every 60–90 minutes of study.
4. **Problem step:** what part of this stress can I act on today? (one step)
5. **Help line:** the signs above, and Tele-MANAS 14416, in your phone contacts now.

**With others:** if a friend shows the warning signs, listen without judging, say you're concerned, and help them contact a doctor or Tele-MANAS. If someone mentions suicide or self-harm, take it seriously, stay with them and get help immediately. You don't need the perfect words; staying with them and getting help matters most.
""",
    resources=[
        ('os-14-4', 'Read 14.4 Regulation of Stress (coping, control, social support, relaxation)', '25 minutes'),
        ('telemanas', 'Read what Tele-MANAS offers and save 14416 in your contacts', '5 minutes'),
        ('noba', 'Search for the module "The Healthy Life" and read the section on stress', '15 minutes'),
    ],
    steps=[
        'Write your stress plan (the five parts above) in your Playbook notebook.',
        'Save Tele-MANAS (14416) in your phone contacts.',
        'Practise slow breathing (in 4, out 6) for five minutes on five days this week. Rate your tension 0–10 before and after.',
        'On one stressful day, use at least two tools from your plan and write what helped.',
    ],
    proof='Your written stress plan, a screenshot of the saved Tele-MANAS contact (name and number only), and five days of before-and-after tension ratings.',
    templates=[('Personal stress plan', """MY STRESS PLAN
Early warning signs:  Body ______  Thoughts ______  Behaviour ______
Fast tools (5 min):   [ ] slow breathing 4 in / 6 out  [ ] 2 cyclic sighs
                      [ ] 10-minute walk  [ ] cold water  [ ] call ______
Daily buffers:        sleep by ______ ; move ______ ; talk to ______ ;
                      break every ___ minutes of study
Problem step today:   ______________________________
GET HELP if 2+ weeks of: low mood / lost interest / uncontrollable worry /
  big sleep or appetite change / using substances to cope / can't manage.
GET HELP NOW if: thoughts of self-harm or someone in danger.
  Tele-MANAS 14416 or 1-800-89-14416 (toll-free, 24x7) | Emergency 112
Breathing log: Date | Tension before (0-10) | after (0-10)""", '')],
    mistakes=[
        ('Treating all stress as bad.', 'Short stress before an exam is normal and can help. The problem is chronic stress with no recovery.'),
        ('Coping alone for too long.', 'If warning signs last two weeks or more, talk to a professional. Earlier help works better.'),
        ('Using this course as therapy.', 'These are everyday skills, not treatment. They work alongside professional help, not instead of it.'),
        ('Dismissing a friend\'s distress.', 'Listen, take it seriously and help them get help.'),
    ],
    quiz=[
        Q('Which system releases cortisol during stress?', 'The HPA axis (hypothalamus, pituitary, adrenal glands)', 'The digestive system', 'The parasympathetic system', 'The immune system only', why='The HPA axis is the slower hormonal stress pathway.'),
        Q('What kind of stress is most linked to health harm?', 'Chronic stress with little control or recovery', 'Short stress before an exam', 'Any stress at all', 'Stress from exercise', why='Prolonged, uncontrollable stress is the main concern.'),
        Q('A friend has felt hopeless for a month and has lost interest in everything. What should you do?', 'Listen, say you\'re concerned and help them contact a doctor or Tele-MANAS', 'Tell them to think positively', 'Wait for it to pass', 'Avoid them', why='These are signs that professional help is needed.'),
        Q('What is the Tele-MANAS short code?', '14416', '112', '1930', '108', why='Tele-MANAS: 14416 or 1-800-89-14416, toll-free, 24x7.'),
    ],
    study='read the lesson and OpenStax 14.4',
    action='write your stress plan, save Tele-MANAS and practise slow breathing on five days',
)

L2 = lesson(
    11, 2,
    outcome='You can fill in a full CBT thought record and use it for two weeks to examine upsetting thoughts.',
    split='15 minutes reading, 5 to 10 minutes per record for two weeks',
    principle='Writing out the situation, feelings, hot thought, evidence and a balanced alternative weakens upsetting thoughts more than arguing with them in your head.',
    science="""
The **thought record** is one of the core tools of cognitive therapy, developed from Aaron Beck's work and popularised in self-help by Christine Padesky and Dennis Greenberger (*Mind Over Mood*) and David Burns. It builds on catch-name-check-replace from PD-M03-L02 but goes further: it separates **facts** from **interpretations**, rates how strongly you **believe** a thought, and asks for **evidence on both sides**.

**Why writing helps.** Thoughts in your head loop and blur together; on paper they become specific claims you can examine. Rating belief and feelings before and after shows you, in numbers, whether the reframe helped. Over time, people often notice the same "hot thoughts" and distortions repeating, which points to underlying beliefs (PD-M09-L02).

**Evidence.** Thought records are one component of CBT, which has strong evidence as a whole. Studies that isolate the cognitive part suggest it contributes but is not the only active ingredient: behavioural activation (doing more valued activities) and exposure (facing fears) also matter a lot. So thought records work best combined with action: the last step of the record is always one small thing you can do.

**When not to use it.** For grief, real danger or a problem that needs action (an unpaid fee, an unsafe situation), the issue is not distorted thinking. Use problem-solving or get support instead. And if thought records stir up very painful memories, stop and talk to a professional.
""",
    evidence=[
        ('CBT, including cognitive restructuring', 'strong', 'Strong evidence for anxiety and depression as a full therapy.'),
        ('Thought records as a self-help tool', 'moderate', 'Widely used in guided self-help with positive results; benefit varies.'),
        ('The cognitive part alone explains CBT\'s effect', 'mixed', 'Behavioural parts (activation, exposure) also contribute strongly.'),
    ],
    example="""
Ashiq's record on a Tuesday night:

1. **Situation:** In the study group, I gave a wrong answer about the Directive Principles. Two people laughed.
2. **Feelings:** embarrassed 80, anxious 60, angry 40.
3. **Hot thought:** "Everyone thinks I'm stupid and I don't belong in this group." Belief: 85%.
4. **Distortions:** mind reading, labelling, overgeneralising.
5. **Evidence for:** two people laughed; I got it wrong.
   **Evidence against:** they laugh at everyone's mistakes, including their own; Rahul asked me for help with geography last week; I got 7 of 10 right in the quiz that day.
6. **Balanced thought:** "I made one mistake, and the laughter was the group's usual joking. I'm a useful member, strong in geography, weaker in Polity." Belief: 70%.
7. **Re-rate:** embarrassed 35, anxious 25, angry 15.
8. **Action:** revise Directive Principles for 20 minutes tomorrow and make three flashcards.

After two weeks he has nine records. The same hot thought ("I don't belong") appears four times, which shows him a belief worth testing with a behavioural experiment.
""",
    apply=f"""
**How to fill in a thought record (5 to 10 minutes):**

1. **Situation:** facts only: what a camera would have recorded.
2. **Feelings:** name and rate 0–100.
3. **Hot thought:** the thought that drives the strongest feeling, word for word. Rate how much you believe it.
4. **Distortion:** which trap? (list in the template)
5. **Evidence for and against:** facts, not feelings, on both sides.
6. **Balanced thought:** true, fair, kind; rate belief.
7. **Re-rate feelings.**
8. **One action.**

**Two-week practice:** fill in a record whenever a feeling is 60 or more, or at least three times a week. On the Daily system track, the thought-record checkpoints are at the end of each week.

**Patterns:** after two weeks, list your hot thoughts. Repeating ones point to a deeper belief to test.
""",
    resources=[
        ('os-14-4', 'Re-read the part on cognitive coping strategies', '10 minutes'),
        ('noba', 'Search for the module "Therapeutic Orientations" and re-read the CBT section, focusing on cognitive restructuring', '15 minutes'),
        ('enchiridion', 'Read section 5 (people are disturbed not by things themselves but by their views about them) and compare it with CBT', '5 minutes'),
    ],
    steps=[
        'Print or copy the thought-record template (paper works well).',
        'For two weeks, fill in a thought record whenever a feeling is 60 or more, and at least three times a week.',
        'At the end of each week, list the distortions that appeared and your average feeling drop.',
        'At the end of two weeks, list repeating hot thoughts and choose one to test with a behavioural experiment (PD-M09-L02).',
    ],
    proof='At least six complete thought records over two weeks, two weekly summaries and your list of repeating hot thoughts.',
    templates=[('Thought record', tools.THOUGHT_RECORD, '')],
    mistakes=[
        ('Writing interpretations in the situation box.', '"He insulted me" is an interpretation; "He said my answer was wrong in front of others" is a fact.'),
        ('Skipping the evidence for the thought.', 'Taking the thought seriously first makes the balanced thought more believable.'),
        ('Expecting feelings to drop to zero.', 'A drop from 80 to 40 is a big success.'),
        ('Using thought records for real problems that need action.', 'If the problem is real, use problem-solving or get support.'),
    ],
    quiz=[
        Q('What goes in the "situation" box of a thought record?', 'Facts only, as a camera would record them', 'Your interpretation', 'How you feel', 'What you should have done', why='Separating facts from interpretations is the first step.'),
        Q('What is a "hot thought"?', 'The thought driving the strongest feeling', 'Any thought about anger', 'A positive thought', 'A thought about the weather', why='The hot thought is the main target for examination.'),
        Q('What is the honest status of thought records?', 'A useful part of a well-supported therapy; works best with action', 'Proven to cure depression alone', 'Useless', 'Only for children', why='CBT is strong; the cognitive part is one of several active ingredients.'),
        Q('A balanced thought should be:', 'True, fair and kind', 'As positive as possible', 'The exact opposite of the hot thought', 'Short and funny', why='Believable balanced thoughts change feelings; forced positivity does not.'),
    ],
    study='read the lesson and copy the thought-record template',
    action='fill in at least six thought records over two weeks and find your repeating hot thoughts',
)

L3 = lesson(
    11, 3,
    outcome='You can use four Stoic practices (the dichotomy of control, negative visualisation, the view from above and the evening review) and a failure-review routine.',
    split='20 minutes reading, 30 minutes of practice and reading',
    principle='Focus your effort on what is in your control, prepare calmly for setbacks, and treat failure as information to review, not a verdict on your worth.',
    science=f"""
**Stoicism** is a Greek and Roman philosophy (about 300 BCE to 200 CE). Its best-known writers, all free in the public domain, are **Epictetus** (a former slave who taught in Greece; his *Enchiridion* or "Handbook"), **Seneca** (a Roman statesman; *Moral Letters to Lucilius*) and **Marcus Aurelius** (a Roman emperor; *Meditations*, his private notes to himself). Aaron Beck and Albert Ellis both credited Stoic ideas as an influence on CBT: Epictetus's line that people are disturbed not by things but by their judgements about things is close to the core idea of cognitive therapy.

**Four practices:**
1. **The dichotomy of control** (Epictetus, *Enchiridion* 1): some things are up to us (our judgements, effort, choices, actions) and some are not (other people, results, the past, the body's luck, reputation). Put your energy into the first.
2. **Negative visualisation** (Seneca, Epictetus): briefly imagine losing something or a plan going wrong, to prepare calmly and to appreciate what you have. (Compare the pre-mortem, PD-M04-L02.)
3. **The view from above** (Marcus Aurelius): picture your problem from high above (your house, Kuttiady, Kerala, the earth) to see it in proportion.
4. **The evening review** (Seneca, *On Anger*, describing his own nightly habit): each night, review the day: what did I do well, what badly, what will I do better tomorrow? Without self-punishment.

**Evidence.** There is little direct research on Stoicism itself. An online "Stoic Week" run by the Modern Stoicism project reported improved wellbeing in participants' self-reports, but without control groups. The individual practices overlap with tested methods: cognitive restructuring (CBT), problem-focused coping, savouring and gratitude, and reflection. So the evidence is mainly **indirect**.

**Handling failure.** Research on learning from failure suggests people often avoid looking at their failures because it hurts, and so learn less (studies by Lauren Eskreis-Winkler and Ayelet Fishbach found people learned less from failure feedback than from success feedback, mainly because failure feels threatening). A structured, kind review makes failure easier to look at: separate what you controlled from what you didn't, find one lesson, and take one step. Many successful people describe repeated failures before success; this is survivorship bias if used as proof, but it is true that most skills grow through many failed attempts.
""",
    evidence=[
        ('Stoic ideas influenced CBT', 'strong', 'Beck and Ellis acknowledged the influence; the overlap is clear.'),
        ('Stoic practices improve wellbeing', 'mixed', 'Mostly uncontrolled self-report studies; indirect support from CBT and coping research.'),
        ('Focusing on controllable actions (problem-focused coping)', 'moderate', 'Linked to better outcomes when the problem is controllable.'),
        ('People learn less from failure because it feels threatening', 'moderate', 'Several experiments by Eskreis-Winkler and Fishbach.'),
        ('Evening review as a habit', 'tool', 'Practical reflection habit, consistent with reflection research.'),
    ],
    example="""
Sreeja didn't make the rank list for a post she had prepared for over a year. She spends one evening on a Stoic failure review.

**Control:** In her control were study hours, methods, mock tests, sleep and exam-day choices. Not in her control: the cut-off, the number of vacancies, other candidates and two ambiguous questions. **Lesson:** her error log showed most lost marks were in current affairs, which she had revised only in the last month. **Step:** a weekly current-affairs routine from the newspaper, starting Monday.

Then the **view from above**: she pictures her room, her village, the district, Kerala, and the thousands of others who also missed this list, many of whom will succeed next time. The disappointment doesn't vanish, but it shrinks to its real size. She reads Seneca's letter on travel ("you need a change of soul rather than a change of climate") and writes one line in her evening review: "I did my part; I'll improve one thing."
""",
    apply=f"""
**Daily (5 minutes before sleep): the evening review.**
1. What did I do well today?
2. What did I do badly, or not do?
3. What will I do better tomorrow?
Write one line for each. Be your own fair coach, not your judge.

**When something goes wrong: the control split.** Draw two columns: **in my control** and **not in my control**. Put your energy only into the first.

**Weekly (2 minutes): negative visualisation.** Imagine briefly that a plan fails or that you lose something you value (your health, a friend). Ask: How would I cope? What can I appreciate today?

**When a problem feels huge: the view from above.**

**After a real failure: the failure review.** Control split → one lesson → one step → one kind sentence to yourself.

**With others:** the control split is a gentle way to help a friend after a setback: "What part of this was in your hands?"
""",
    resources=[
        ('enchiridion', 'Read sections 1 to 10 of the Handbook', '20 minutes'),
        ('seneca', 'Read Letter 1 ("On Saving Time") and Letter 28 ("On Travel as a Cure for Discontent")', '20 minutes'),
        ('meditations', 'Read the first ten paragraphs of the second book (Marcus Aurelius\'s notes to himself)', '15 minutes'),
    ],
    steps=[
        'Do the evening review for seven nights (three lines each).',
        'Use the control split on one current worry or recent failure and write the lesson and one step.',
        'Do one negative visualisation and one view from above, and write two lines on each.',
        'Copy one Stoic quotation that means something to you into your Playbook, with a line on how you will use it.',
    ],
    proof='Seven evening reviews, one control split with lesson and step, notes on one negative visualisation and one view from above, and your chosen quotation.',
    templates=[('Stoic practices and failure review', """EVENING REVIEW (each night, 3 lines)
Did well: ______  Did badly or skipped: ______  Better tomorrow: ______

CONTROL SPLIT                 Situation: ______________________
IN MY CONTROL                       NOT IN MY CONTROL
______________________________      ______________________________
______________________________      ______________________________

FAILURE REVIEW
What happened (facts): ______________________________
What was in my control? ______________________________
One lesson: ______________________________
One step this week: ______________________________
One kind sentence to myself: ______________________________""", '')],
    mistakes=[
        ('Using "not in my control" to avoid responsibility.', 'Effort, preparation and choices are in your control. Be honest in the left column.'),
        ('Turning negative visualisation into worry.', 'It is brief and ends with appreciation or a plan. If it makes you anxious, skip it.'),
        ('Treating Stoicism as suppressing all emotion.', 'The Stoics aimed at good judgement, not emotional numbness. Feel the feeling; choose the response.'),
        ('Using famous failure stories as proof.', 'For every famous person who failed and then succeeded, many failed and stopped. Learn the process, not the legend.'),
    ],
    quiz=[
        Q('According to the dichotomy of control, which is up to you?', 'Your effort and choices', 'The exam cut-off', 'Other candidates\' scores', 'Your reputation', why='Epictetus: our judgements and actions are up to us; results and others are not.'),
        Q('Which Stoic idea is closest to the core of CBT?', 'People are disturbed not by things but by their judgements about them', 'Always suppress emotions', 'Never plan for the future', 'Wealth brings happiness', why='Beck and Ellis cited this Stoic idea as an influence.'),
        Q('What is the honest evidence status of Stoic practices?', 'Mainly indirect: overlap with tested methods, plus uncontrolled self-report studies', 'Proven by many controlled trials', 'Shown to be harmful', 'No connection to psychology', why='Few controlled trials exist; support is largely indirect.'),
        Q('Why do people often learn less from failure?', 'Failure feels threatening, so they avoid looking at it', 'Failure has no information', 'They are lazy', 'Success teaches nothing', why='Eskreis-Winkler and Fishbach found ego threat reduces learning from failure.'),
    ],
    study='read the lesson and Enchiridion sections 1 to 10',
    action='do seven evening reviews, a control split with one step, and one negative visualisation and view from above',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    11,
    overview=f"""
Stress and resilience: how the stress response works, fast calming tools, the signs that mean you should get professional help (with Tele-MANAS), two weeks of CBT thought records, and Stoic practices for handling failure.

Kerala PSC preparation can run for years, with uncertain results, family pressure and money worries. That is a recipe for chronic stress. This module gives you a stress plan, a tested way to examine upsetting thoughts, and a calm way to look at failure.

It also says clearly what this course cannot do. Everyday tools help everyday stress; they are not treatment. If the warning signs in PD-M11-L01 last two weeks or more, talk to a professional. The exam-specific side of anxiety is covered in {xref('lrn', 'lrn-m12', 'the Learning Capabilities exam module')} and in PD-M33-L02.
""",
    outcomes=[
        'Explain the stress response and the difference between short and chronic stress.',
        'Use slow breathing, movement, talking and writing to calm stress.',
        'Recognise the signs that mean it is time to get professional help, and know how to contact Tele-MANAS.',
        'Fill in full CBT thought records and find repeating hot thoughts.',
        'Use the dichotomy of control, the evening review and a failure review.',
    ],
    lessons=LESSONS,
    project='two weeks of thought records and a resilience plan',
    project_steps=[
        'Complete at least six thought records over two weeks (PD-M11-L02).',
        'Keep the evening review on at least ten of those nights (PD-M11-L03).',
        'Write a one-page resilience plan: early warning signs, fast tools, daily buffers, your repeating hot thought and its balanced version, your control-split habit, and when to get help.',
        'Share the help part of the plan with one trusted person.',
    ],
    project_proof='Six thought records, ten evening reviews and your one-page resilience plan.',
    rubric=[
        ('Stress knowledge', 'Cannot describe the stress response', 'Describes it partly', 'Explains both systems and short versus chronic stress'),
        ('Thought records', 'Fewer than three', 'Three to five, some incomplete', 'Six or more complete records with ratings'),
        ('Stoic practice', 'Not tried', 'A few reviews', 'Ten evening reviews and a failure review'),
        ('Safety', 'No help plan', 'Knows Tele-MANAS', 'A written plan with warning signs, Tele-MANAS saved and shared with someone'),
    ],
    short=[
        'Save Tele-MANAS (14416) and read the warning signs.',
        'Do one thought record a week and a three-line evening review on most nights.',
    ],
    flashcards=[
        ('Two stress systems', 'Sympathetic (adrenaline, fast) and HPA axis (cortisol, slower).'),
        ('Most harmful kind of stress', 'Chronic, uncontrollable, with little recovery.'),
        ('Slow breathing rhythm', 'About 6 breaths a minute, e.g. in 4 seconds, out 6.'),
        ('When to get professional help', 'Two weeks or more of low mood, lost interest, uncontrollable worry, big sleep/appetite change, substance use to cope; now if any thoughts of self-harm.'),
        ('Tele-MANAS', '14416 or 1-800-89-14416, toll-free, 24x7.'),
        ('Thought record steps', 'Situation, feelings, hot thought, distortion, evidence for and against, balanced thought, re-rate, action.'),
        ('Dichotomy of control', 'Focus on what is up to you: judgements, effort, choices.'),
        ('Evening review', 'Did well, did badly, better tomorrow.'),
    ],
    mistakes=[
        ('Waiting until a crisis to make a plan.', 'Write the stress plan while you are calm.'),
        ('Hiding distress to look strong.', 'Social support is one of the strongest stress buffers. Use it.'),
        ('Treating these tools as a replacement for care.', 'If warning signs persist, see a professional.'),
    ],
    tools=[
        'The personal stress plan with warning signs and Tele-MANAS (PD-M11-L01).',
        'The full CBT thought record (PD-M11-L02).',
        'The evening review, control split and failure review (PD-M11-L03).',
    ],
    playbook=[
        'My early warning signs: ______. My fast tools: slow breathing, a walk, calling ______.',
        'I get help if warning signs last two weeks, and at once if I think of harming myself: Tele-MANAS 14416.',
        'After a failure: control split, one lesson, one step, one kind sentence.',
    ],
)
