from common import lesson, module, link, xref, table, Q

L1 = lesson(
    13, 1,
    outcome='You can explain where confidence comes from (self-efficacy), use the spotlight effect to worry less about being judged, and handle impostor feelings, without relying on power poses.',
    split='20 minutes reading, 25 minutes of tasks',
    principle='Confidence grows mainly from doing things successfully, step by step; other people notice us far less than we think; and feeling like a fraud is common and says little about your real ability.',
    science=f"""
**Self-efficacy.** Albert Bandura (1977) defined **self-efficacy** as your belief that you can carry out a specific task, such as giving a talk, solving percentage problems or asking for a discount. It is specific, not general: you can have high self-efficacy for cooking and low for public speaking. Bandura identified four sources, in order of strength:
1. **Mastery experiences:** succeeding at the task, especially after effort. The strongest source.
2. **Vicarious experiences:** seeing someone similar to you succeed ("If Anu from my village can, so can I").
3. **Verbal persuasion:** encouragement from people you trust (weaker on its own; it works when followed by success).
4. **Physical and emotional states:** how you read your racing heart (as fear, or as readiness).

Self-efficacy is one of the best-supported ideas in psychology: it predicts effort, persistence and performance across education, health and work. The practical lesson: **build confidence by designing small successes**, not by waiting to feel confident first.

**The spotlight effect.** In a study by Thomas Gilovich, Victoria Husted Medvec and Kenneth Savitsky (2000), students were asked to wear an embarrassing T-shirt (with a picture of the singer Barry Manilow) into a room of peers. Wearers estimated that about **half** the room would notice; in fact, about **a quarter** did, roughly half as many as they expected ({link('spotlight-sum', 'summary of the figures')}; {link('wp-spotlight', 'background')}). Later studies found the same direction for bad hair days, mistakes in a group discussion and even for good performances. Most people are too busy thinking about themselves to watch you closely.

**Impostor feelings.** Pauline Clance and Suzanne Imes (1978) described the "impostor phenomenon": capable people who feel like frauds and fear being found out. It is **not a mental illness** or a formal diagnosis. A 2020 review by Dena Bravata and colleagues found it reported very widely, though estimates vary enormously depending on how it is measured. It often comes with perfectionism and with being the first in a family to enter a field (common for first-generation government employees or graduates). Useful responses: talk about it (you will find others feel it too), keep a record of evidence of competence, and redefine mistakes as part of learning.

**What about power posing?** As you saw in PD-M02-L02, the claim that two minutes of a "power pose" changes hormones and risk-taking failed larger replications. A small effect on *feeling* powerful may exist, and the authors still disagree about it. Standing upright and breathing slowly before a talk does no harm; just don't expect it to transform you. Mastery experiences do the real work.
""",
    evidence=[
        ('Self-efficacy predicts effort and performance', 'strong', 'Decades of research across education, health and work.'),
        ('Mastery experiences are the strongest source of self-efficacy', 'strong', 'Consistent with many studies and meta-analyses.'),
        ('Spotlight effect: people overestimate how much they are noticed', 'moderate', 'The direction replicates across studies; the size varies.'),
        ('Impostor feelings are common, especially among high achievers and newcomers to a field', 'moderate', 'Widely reported; prevalence estimates vary greatly with measurement.'),
        ('Power posing changes hormones or behaviour', 'failed', 'Not supported by larger replications.'),
    ],
    example="""
Ashiq has been asked to explain the new bus timetable at the residents' association meeting. He feels sure everyone will notice his shaking hands and his "village English" mixed with Malayalam.

He uses **mastery experiences** in small steps: he explains the timetable to his mother, then to two neighbours, then records himself on his phone. Each success raises his rating of "I can explain this clearly" from 3/10 to 7/10. He watches a video of a friend from his school speaking at a panchayat meeting (**vicarious experience**). On the day, his heart races; he tells himself "my body is getting ready" (**physical state**). He speaks for four minutes, mostly in Malayalam with some English terms.

Afterwards he asks two people, "Did you notice I was nervous?" Both say no; one only remembers that the 7:40 bus had moved to 7:55 (**spotlight effect**). When his brother calls him "the new president", Ashiq feels like an impostor. He writes down three pieces of evidence that he explained the timetable well, and smiles.
""",
    apply="""
**Build self-efficacy deliberately:**
1. Pick one skill you want confidence in (speaking, maths, talking to strangers).
2. Rate your confidence 0–10 for a specific task: "explain the timetable for 3 minutes".
3. Design three small mastery steps, from easy to harder. Do them.
4. Find a similar person who has done it (a video, a friend) and watch them.
5. Re-rate after each step.

**Use the spotlight effect:** before something embarrassing, say "Most people will notice half as much as I fear, and forget it sooner." Afterwards, check by asking one person.

**Impostor feelings:** keep an **evidence file**: a note with every compliment, good result and solved problem. Read it when you feel like a fraud. Say the feeling aloud to a friend; you will often hear "Me too".

**With others:** give **specific** encouragement *after* a success ("You explained that clearly; the example helped"), and share your own nervous moments. That builds others' self-efficacy far more than "You'll be fine!"
""",
    resources=[
        ('os-10', 'Re-read the section on self-efficacy in 10.1', '10 minutes'),
        ('wp-spotlight', 'Read the article', '10 minutes'),
        ('wp-power', 'Re-read the replication section so you can explain it to others', '5 minutes'),
    ],
    steps=[
        'Choose one confidence skill and one specific task. Rate your confidence 0–10.',
        'Design and do three mastery steps this week, re-rating after each.',
        'After one mildly embarrassing moment, ask one person whether they noticed. Write what they said.',
        'Start an evidence file with at least five entries.',
    ],
    proof='Your confidence ratings before and after three mastery steps, one spotlight check, and an evidence file with five entries.',
    templates=[('Confidence builder', """SELF-EFFICACY BUILDER          Skill: ______________________
Task: ______________________   Confidence now (0-10): ___
Mastery steps (easy -> harder):          Done   Confidence after
1. ______________________________        [ ]    ___
2. ______________________________        [ ]    ___
3. ______________________________        [ ]    ___
Someone like me who has done it: ______________
SPOTLIGHT CHECK: I feared ___% would notice ______. I asked ______; they said ______.
EVIDENCE FILE (add whenever it happens)
Date | Evidence of competence (result, compliment, problem solved)""", '')],
    mistakes=[
        ('Waiting to feel confident before acting.', 'Confidence follows successful action. Start with a step small enough to succeed.'),
        ('Steps that are too big.', 'If a step fails badly, make the next one smaller.'),
        ('Relying on power poses or affirmations.', 'They do little on their own. Mastery experiences do the work.'),
        ('Telling impostor feelings to go away.', 'Name them, check the evidence file, carry on. They usually fade with experience.'),
    ],
    quiz=[
        Q('According to Bandura, what is the strongest source of self-efficacy?', 'Mastery experiences: succeeding at the task', 'Encouragement from others', 'Watching motivational videos', 'Power poses', why='Doing it successfully builds belief most strongly.'),
        Q('In the T-shirt study, how many people noticed compared with what wearers predicted?', 'Roughly half as many', 'Exactly as many', 'Twice as many', 'Nobody noticed at all', why='About a quarter noticed versus about half predicted.'),
        Q('Which statement about impostor feelings is accurate?', 'They are common, not a diagnosis, and often fade with experience and evidence', 'They mean you really are a fraud', 'They are a mental illness', 'Only beginners feel them', why='Common among capable people and newcomers to a field.'),
        Q('What is the honest status of power posing?', 'Hormone and behaviour effects failed replication; a small effect on feeling powerful is debated', 'Proven to raise testosterone', 'Proven harmful', 'Never studied', why='Larger studies did not support the original claims.'),
    ],
    study='read the lesson and the spotlight-effect article',
    action='do three mastery steps for one skill with ratings, one spotlight check and start an evidence file',
)

L2 = lesson(
    13, 2,
    outcome='You can build a personal fear ladder of 10 steps and climb the first steps using exposure principles, without safety behaviours.',
    split='20 minutes reading, 30 minutes of planning plus practice',
    principle='Fears shrink when you face them step by step, staying with the discomfort long enough to learn that the feared outcome doesn\'t happen or is bearable; avoidance keeps fears alive.',
    science="""
**Exposure.** Exposure therapy is one of the best-supported treatments in psychology, especially for phobias, social anxiety, panic and obsessive-compulsive disorder. The idea is simple: avoiding what you fear brings short-term relief but teaches your brain that the situation is dangerous and that you couldn't have coped. **Facing it, gradually and repeatedly,** teaches the opposite.

**How it works.** Two explanations are used:
- **Habituation:** the fear response weakens with repeated, prolonged contact (like getting used to cold water).
- **Inhibitory learning:** Michelle Craske and colleagues argue that exposure works mainly by creating **new learning** ("I spoke and nobody laughed"; "I felt anxious and it passed") that competes with the old fear memory. On this view, what matters most is **testing your feared prediction**, not just waiting until the fear goes down.

**The fear ladder (exposure hierarchy).** You list feared situations from easiest to hardest and rate each with **SUDS** (Subjective Units of Distress, 0–100). Start with a step that causes some anxiety (around 30–40), repeat it until it feels manageable, then move up.

**Safety behaviours.** These are small things people do to feel safer that secretly keep the fear alive: avoiding eye contact, rehearsing every word, holding a phone as a shield, speaking very fast to finish, always taking a friend. Research by Paul Salkovskis and David Clark on social anxiety found that dropping safety behaviours during exposure made it work better. Some researchers find that limited, early use of safety aids does little harm, but the general advice is to reduce them.

**Kerala-friendly ladders** can cover speaking (in class, at a function, in English), social situations (talking to strangers, going alone to a hotel), assertiveness (refusing a relative, returning a product) and performance (singing at a family event). **This module is for everyday fears.** If fear is severe (panic attacks, avoiding leaving home, avoiding all social contact) or linked to trauma, work with a professional; Tele-MANAS (14416) can guide you.
""",
    evidence=[
        ('Exposure therapy for phobias, social anxiety and panic', 'strong', 'Many trials and reviews; a core part of CBT for anxiety.'),
        ('Inhibitory learning (testing predictions) as a mechanism', 'moderate', 'Supported by lab and clinical research; still being refined.'),
        ('Dropping safety behaviours improves exposure', 'moderate', 'Supported in social anxiety studies; some debate about limited early use.'),
        ('Self-directed graded exposure for everyday fears', 'moderate', 'Guided self-help shows benefits; severe fears need professional support.'),
    ],
    example="""
Anu fears speaking English in front of others. She builds a fear ladder:

| Step | Situation | SUDS |
| --- | --- | --- |
| 1 | Record a 1-minute English voice note for myself | 20 |
| 2 | Send a 1-minute English voice note to a friend | 35 |
| 3 | Ask a question in English at the bank counter | 40 |
| 4 | Speak 2 minutes in English in my study group | 50 |
| 5 | Order food in English at a restaurant in Kozhikode city | 55 |
| 6 | Make an English phone call to a company helpline | 60 |
| 7 | Introduce myself in English to a stranger at a library event | 70 |
| 8 | Record and post a 1-minute English video on my status | 75 |
| 9 | Give a 3-minute English talk at a Toastmasters guest visit | 85 |
| 10 | Give a 5-minute English talk to a real audience | 95 |

She starts at step 2, repeats it three times in a week until it drops to 15, then moves to step 3. Her safety behaviour is writing out every sentence first; she drops it from step 4. Her prediction before step 4: "I'll freeze and people will look away." Result: she paused twice, one person nodded, nobody looked away. She writes: "Pauses feel long to me, not to them."
""",
    apply="""
**Build your fear ladder (30 minutes):**
1. Choose one fear area (speaking, strangers, saying no, being seen).
2. List 10 situations from easy (SUDS 10–20) to very hard (SUDS 90–100). Make them specific and realistic in your life.
3. Name your safety behaviours for this fear.

**Climb it:**
1. Before each step, write your **feared prediction** ("I will…", "They will…") and rate SUDS.
2. Do the step **without safety behaviours**, and stay in the situation until you've tested the prediction (don't escape early).
3. Afterwards, write what actually happened and rate SUDS again.
4. Repeat a step until SUDS drops by about half or it feels manageable, then move up.
5. Two or three steps a week is a good pace. A setback means: go back one step, not to zero.

**Connection to the next module:** rejection therapy (Module 14) is a fear ladder for the fear of hearing "no".

**With others:** you can support a friend's ladder by being there, but don't do the step for them and don't reassure them over and over (reassurance can become a safety behaviour). Ask, "What did you predict, and what happened?"
""",
    resources=[
        ('os-14-4', 'Re-read the section on coping and control (why avoidance maintains stress)', '10 minutes'),
        ('noba', 'Search for the module "Anxiety and Related Disorders" and read the treatment section on exposure', '20 minutes'),
        ('seneca', 'Read Letter 13 ("On Groundless Fears"): "we suffer more often in imagination than in reality"', '15 minutes'),
    ],
    steps=[
        'Write a 10-step fear ladder for one fear area, with SUDS ratings and your safety behaviours.',
        'Do the first two or three steps this week, each with a written prediction, the result and SUDS before and after.',
        'Repeat at least one step until its SUDS drops by about half.',
        'Write one sentence about what you learned that your fear did not tell you.',
    ],
    proof='Your 10-step ladder with SUDS and safety behaviours, at least three exposure records (prediction, result, SUDS before and after) and your learning sentence.',
    templates=[('Fear ladder and exposure record', """FEAR LADDER                  Fear area: ______________________
Step | Situation (specific) | SUDS (0-100) | Done (dates)
1  | ______________________________ | __ | ______
...
10 | ______________________________ | __ | ______
My safety behaviours (drop them): ______  ______  ______
EXPOSURE RECORD
Date | Step | Feared prediction | SUDS before | What actually happened | SUDS after | Learned""", '')],
    mistakes=[
        ('Starting too high.', 'Begin with a step around SUDS 30–40. Too hard too soon leads to escape and stronger fear.'),
        ('Escaping as soon as anxiety rises.', 'Stay long enough to test the prediction.'),
        ('Keeping hidden safety behaviours.', 'Scripts, avoiding eye contact, rushing: drop them step by step.'),
        ('Treating severe fears alone.', 'Panic attacks, trauma-related fear or avoiding daily life need professional support.'),
    ],
    quiz=[
        Q('Why does avoiding a feared situation keep the fear alive?', 'Relief teaches the brain the situation is dangerous and you couldn\'t have coped', 'Avoidance cures fear', 'Fear has nothing to do with avoidance', 'Because you forget the situation', why='Avoidance blocks the new learning that exposure provides.'),
        Q('According to the inhibitory-learning view, what matters most in exposure?', 'Testing your feared prediction and learning it doesn\'t happen or is bearable', 'Feeling no anxiety at all', 'Doing the hardest step first', 'Reassurance from others', why='New learning competes with the old fear memory.'),
        Q('Which is a safety behaviour in public speaking?', 'Reading a fully written script so you never look up', 'Practising beforehand', 'Breathing slowly', 'Making eye contact', why='It feels safer but stops you learning you can cope without it.'),
        Q('When should you move up the ladder?', 'When the current step\'s distress has dropped by about half or feels manageable', 'Immediately after the first try', 'Only when you feel no fear at all', 'After a month on each step', why='Repeat until manageable, then climb.'),
    ],
    study='read the lesson and Seneca\'s Letter 13',
    action='build a 10-step fear ladder and climb the first steps with prediction records',
)

LESSONS = [L1, L2]

MODULE = module(
    13,
    overview=f"""
Confidence and courage built the way research says it grows: self-efficacy through mastery experiences, the spotlight effect, honest handling of impostor feelings (and why power posing doesn't do the job), and a fear ladder climbed with exposure principles.

Confidence is not a personality trait you have or lack. It is a set of task-specific beliefs that grow when you succeed at slightly harder steps. This module gives you the method; Module 14 applies it to the fear of rejection, and Module 27 applies it to public speaking.

If you have severe anxiety (panic attacks, avoiding normal life), use these ideas only with a professional's guidance.
""",
    outcomes=[
        'Explain Bandura\'s four sources of self-efficacy and design mastery steps.',
        'Use the spotlight effect to reduce fear of being judged.',
        'Handle impostor feelings with an evidence file.',
        'Explain why power posing is not a confidence tool.',
        'Build and climb a fear ladder without safety behaviours.',
    ],
    lessons=LESSONS,
    project='your personal fear ladder, climbed halfway',
    project_steps=[
        'Build a 10-step fear ladder for the fear that holds you back most (PD-M13-L02).',
        'Over two to three weeks, climb at least the first five steps, with an exposure record for each attempt.',
        'Keep your evidence file going (PD-M13-L01).',
        'Write a half-page review: SUDS changes, predictions that were wrong, safety behaviours dropped, next three steps.',
    ],
    project_proof='Your ladder, at least five exposure records and the half-page review.',
    rubric=[
        ('Ladder quality', 'Vague or too few steps', 'Ten steps but uneven', 'Ten specific, realistic steps with SUDS'),
        ('Practice', 'Fewer than three attempts', 'Three or four attempts', 'Five or more attempts with repeats'),
        ('Learning', 'No predictions recorded', 'Predictions without results', 'Predictions, results and lessons for each step'),
        ('Safety behaviours', 'Not identified', 'Identified, still used', 'Identified and dropped step by step'),
    ],
    short=[
        'Write a five-step ladder and do step 1 twice.',
        'Add one item to your evidence file each week.',
    ],
    flashcards=[
        ('Self-efficacy', 'Belief you can do a specific task (Bandura).'),
        ('Four sources of self-efficacy', 'Mastery, vicarious experience, verbal persuasion, physical/emotional states.'),
        ('Spotlight effect', 'People notice us about half as much as we think (T-shirt study).'),
        ('Impostor phenomenon', 'Capable people feeling like frauds; common, not a diagnosis.'),
        ('Power posing status', 'Hormone and behaviour claims failed replication.'),
        ('SUDS', 'Subjective Units of Distress, 0–100.'),
        ('Safety behaviour', 'Something done to feel safe that keeps fear alive (scripts, avoiding eye contact).'),
        ('Inhibitory learning', 'Exposure works by testing predictions and creating new learning.'),
    ],
    mistakes=[
        ('Collecting confidence quotes instead of doing steps.', 'Small successful actions build confidence; quotes don\'t.'),
        ('Comparing your step 2 with someone else\'s step 10.', 'Compare with your own last attempt.'),
        ('Pushing someone else up their ladder.', 'Exposure must be chosen, not forced.'),
    ],
    tools=[
        'The self-efficacy builder, spotlight check and evidence file (PD-M13-L01).',
        'The fear ladder and exposure record (PD-M13-L02).',
    ],
    playbook=[
        'Confidence comes after action: I design small mastery steps.',
        'When I fear being judged: "People notice about half as much as I think."',
        'My fear ladder: next step is ______. I drop the safety behaviour ______.',
    ],
)
