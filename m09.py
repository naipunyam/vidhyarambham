from common import lesson, module, link, xref, table, Q

L1 = lesson(
    9, 1,
    outcome='You can explain growth mindset and what the large studies really found, and use the useful part (effort plus strategy plus help) without the hype.',
    split='20 minutes reading, 25 minutes of tasks',
    principle='Believing abilities can grow is mildly helpful, mostly for struggling learners; what matters more is what you do with the belief: change strategies, seek feedback and keep practising.',
    science=f"""
**The idea.** Carol Dweck's research, from the 1990s, contrasted a **fixed mindset** (abilities are set; failure shows you lack them) with a **growth mindset** (abilities develop with effort, good strategies and help). Early studies found that students praised for being "smart" chose easier tasks and gave up sooner after failure than students praised for effort, and that growth-mindset students did better through difficult school transitions. *Mindset* (2006) became a bestseller, and schools worldwide ran mindset programmes.

**What the big studies found.** In 2018, Victoria Sisk, Alexander Burgoyne and colleagues ran two meta-analyses ({link('sisk', 'Sisk et al., 2018')}):
- Across 273 samples (about 366,000 students), the link between holding a growth mindset and academic achievement was **weak (r = .10)**.
- Across 43 intervention studies (about 57,000 students), teaching growth mindset improved achievement by a **very small average amount (d = 0.08)**.
- Effects were larger for **students from low-income families (d = 0.34)** and somewhat larger for academically at-risk students.

A large, carefully pre-registered US national study led by David Yeager (2019) found that a short online mindset programme raised grades slightly for lower-achieving students, with bigger effects in schools whose culture supported the message. So the honest picture: **growth mindset is real but small on average**, helps most those who are struggling, and works only when the environment supports it. It is not a cure-all, and it was oversold.

**"False growth mindset."** Dweck herself warned against reducing it to "just praise effort" or "anything is possible". Effort that keeps using a failing strategy is not growth; neither is pretending. The useful version is **effort + better strategies + help-seeking + learning from mistakes**.

**Ability is not unlimited.** People differ in aptitude, and some limits are real. A growth mindset does not mean you can become anything. It means your current level is not your final level, and that the best way to find your limits is to practise well.
""",
    evidence=[
        ('Growth mindset correlates with achievement', 'mixed', 'Weak average link (r = .10) across 273 samples.'),
        ('Growth mindset interventions raise achievement on average', 'mixed', 'Very small average effect (d = 0.08) across 43 studies.'),
        ('Benefits for low-income or struggling students', 'moderate', 'Larger effects in these groups in meta-analyses and a national study.'),
        ('Praising effort and strategy rather than "being smart"', 'moderate', 'Supported by experiments; effects depend on honesty and context.'),
    ],
    example="""
Ashiq failed the arithmetic part of his last mock badly and said, "I'm just not a maths person." His friend replied, "Have a growth mindset!" That didn't help; it felt like being told to cheer up.

What helped was the practical version. He looked at his errors and found 14 of 20 wrong answers were percentage and ratio questions. **Strategy:** he learned one method for each type from a free video and practised 10 questions a day. **Help:** he asked Joseph sir to watch him solve three problems aloud and point out where he went wrong (he was converting fractions slowly). **Effort tracked:** after three weeks, his percentage questions went from 3/10 to 7/10. His belief changed *after* the evidence did: "I'm not a maths person yet" became "I'm getting better at percentages."

He also accepted a limit: he may never be the fastest in reasoning, so he plans to collect marks in GK and language and aim for "good enough" in maths.
""",
    apply="""
**Use the strong part, skip the hype:**

1. **When you fail at something, ask three questions:** What strategy did I use? What could I try instead? Who could show me?
2. **Track skill, not just effort:** a score on the same type of problem over weeks shows real growth and builds belief.
3. **Use "yet":** "I can't do this yet" is a small but honest reframe.
4. **Accept real limits:** choose where to invest effort; you don't have to be equally good at everything.

**With others (children, students, colleagues):**
- Praise **specific strategies and progress** ("You checked each step; that's why you caught the error"), not intelligence ("You're so smart") and not empty effort ("Good try!" when the method was wrong).
- Show your own mistakes and how you fixed them.
- Change the environment: a teacher or parent who punishes every mistake undermines any mindset talk.
""",
    resources=[
        ('sisk', 'Read the abstract and the discussion section: where effects were found and where not', '20 minutes'),
        ('os-10', 'Re-read the self-efficacy part of 10.1 (it connects to Module 13)', '10 minutes'),
        ('james-talks', 'Read the chapter "The Laws of Habits" (in Talks to Teachers): James on how practice shapes ability, written in 1899', '25 minutes'),
    ],
    steps=[
        'Pick one skill where you say "I\'m not a ______ person".',
        'Write your current level with a number (a score on 10 questions, a time, a count).',
        'Choose one new strategy and one person or resource to learn from. Practise for 10 to 20 minutes on at least five days.',
        'Measure the same way again and write the change, plus one honest limit you accept.',
    ],
    proof='Your before and after numbers for one skill, the strategy and help used, and one accepted limit.',
    templates=[('Strategy, not slogans', """SKILL GROWTH CARD                  Skill: ______________________
"I'm not a ______ person" -> "I'm not good at ______ YET."
Before: ______ (score / time / count) on ______ (date)
What strategy was I using? ____________________________
New strategy to try: ____________________________
Who or what can show me? ____________________________
Practice log: Day | Minutes | Score
After: ______ on ______ (date)   Change: ______
A limit I accept, and where I'll invest instead: ______________""", '')],
    mistakes=[
        ('Treating growth mindset as positive thinking.', 'It is about strategy, practice and help, not feeling good.'),
        ('Praising effort when the method is wrong.', 'Praise effective strategies and progress; help change ineffective ones.'),
        ('Believing mindset is the main cause of success.', 'Average effects are small; ability, teaching, resources and practice matter more.'),
        ('Blaming people for a "fixed mindset".', 'Context matters. Change the environment and offer better strategies first.'),
    ],
    quiz=[
        Q('What did the 2018 meta-analysis find about growth-mindset interventions on average?', 'A very small effect (d = 0.08)', 'A huge effect', 'No studies existed', 'They made students worse', why='Sisk et al. found small average effects, larger for low-income students.'),
        Q('For whom did growth-mindset interventions seem to help most?', 'Students from low-income families and struggling students', 'Top students', 'Only adults', 'Nobody', why='Effects were larger for low-SES (d = 0.34) and at-risk students.'),
        Q('What is the most useful response when you fail at a skill?', 'Ask what strategy you used, what to try instead and who could show you', 'Tell yourself to have a growth mindset', 'Give up on that skill forever', 'Work harder with the same method', why='Effort plus better strategy plus help is the real "growth" recipe.'),
        Q('Which praise fits the research best?', '"You checked each step, which is why you caught the error"', '"You\'re so smart"', '"Good try" when the method was wrong', '"You\'re a natural"', why='Specific praise of strategies and progress supports learning.'),
    ],
    study='read the lesson and the Sisk et al. abstract and discussion',
    action='measure one "I\'m not a ___ person" skill, practise a new strategy with help for five days, and measure again',
)

L2 = lesson(
    9, 2,
    outcome='You can find and test a limiting belief, and use self-compassion practices to handle mistakes without beating yourself up or letting yourself off the hook.',
    split='20 minutes reading, 25 minutes of practice',
    principle='Beliefs like "people like me can\'t…" are predictions you can test; and treating yourself with the kindness you would show a friend helps you recover and improve, not go soft.',
    science=f"""
**Limiting beliefs.** A limiting belief is a general rule about yourself or the world that stops you trying: "People from villages can't speak good English", "I'm too old to start exercising at 30", "Rich people are all cheats, so I'll never earn well". In CBT terms (PD-M03-L02), these are often **core beliefs** or **rules** built from early experiences. CBT's main way of changing them is the **behavioural experiment**: turn the belief into a prediction, test it in real life, and see what happens. This is better supported than repeating positive affirmations. In one study by Joanne Wood and colleagues (2009), people with low self-esteem who repeated "I am a lovable person" felt *worse*, apparently because the statement clashed with what they believed.

**Self-compassion.** Kristin Neff defines self-compassion as three parts:
1. **Self-kindness** instead of harsh self-judgement.
2. **Common humanity:** seeing your struggles as part of being human ("many people fail interviews"), not proof that you are uniquely broken.
3. **Mindfulness:** noticing painful feelings clearly, without exaggerating or suppressing them.

Research finds self-compassion is linked to lower anxiety and depression and greater resilience, and meta-analyses of self-compassion training (such as Mindful Self-Compassion programmes) report moderate improvements. Many studies are correlational or small, so effects may be smaller than claimed.

**Does it make you lazy?** The common fear is that being kind to yourself removes the drive to improve. Juliana Breines and Serena Chen (2012) found the opposite in several experiments: people who wrote self-compassionately about a failure or weakness were **more** motivated to improve, studied longer for a retest and were more willing to make amends for a wrong. Self-compassion is not self-pity or excuses; it is honest about the mistake and kind about the person. The self-forgiveness and procrastination study (PD-M08-L04) fits the same pattern.

**Kerala context.** Many of us grew up with harsh correction ("Why only 92? Who got 98?"). Harsh self-talk can feel normal, even virtuous. It is worth knowing that the research favours being firm about standards and kind about the person.
""",
    evidence=[
        ('Behavioural experiments for changing beliefs (CBT)', 'moderate', 'Core CBT method with good support as part of therapy; fewer studies of it alone.'),
        ('Positive self-statements can backfire for low self-esteem', 'mixed', 'One well-known study; replications are limited.'),
        ('Self-compassion is linked to lower anxiety and depression', 'moderate', 'Many studies, largely correlational; training trials show moderate gains.'),
        ('Self-compassion increases motivation to improve after failure', 'moderate', 'Several experiments (Breines and Chen, 2012); consistent with later work.'),
    ],
    example="""
Anu believes, "People from Malayalam-medium schools can't speak English confidently in front of others." It stops her from speaking up in her study group's English sessions.

She turns it into a **behavioural experiment**. *Prediction:* "If I speak for two minutes in English in the group, people will laugh, and I'll freeze." *Test:* she prepares two minutes on a current-affairs topic and speaks on Sunday. *Result:* she stumbled twice; nobody laughed; one friend said her points were clear; she did not freeze. *New belief:* "I can speak English in a friendly group. My grammar slips when I'm nervous, and I can practise that."

That night she notices harsh self-talk about the stumbles: "You sounded stupid." She uses the **self-compassion break**: "This is a moment of embarrassment (mindfulness). Lots of people feel this when speaking a second language (common humanity). May I be patient with myself while I learn (kindness)." Then she writes one specific improvement: "Practise past-tense verbs with shadowing for 10 minutes a day."
""",
    apply="""
**Test a limiting belief (behavioural experiment):**

1. Write the belief: "People like me can't ______."
2. Turn it into a prediction about a specific situation: "If I ______, then ______ will happen."
3. Design a small, safe test and do it.
4. Record what actually happened, compared with the prediction.
5. Write a new, more accurate belief.

**Self-compassion break (1 minute, when you're upset with yourself):**
- "This is hard / painful right now." (mindfulness)
- "Others go through this too." (common humanity)
- "May I be kind to myself and learn from this." (kindness; use words that feel natural, in Malayalam if you prefer)
- Then: "What would help now?" (one concrete step)

**"How would I treat a friend?" (5 minutes):** write how you'd respond to a friend in your situation; compare it with how you talk to yourself; write a response to yourself in the friend version.

**With others:** offer common humanity rather than comparisons ("Lots of people struggle with this") and avoid "At least…" responses that dismiss feelings.
""",
    resources=[
        ('selfcomp', 'Do Exercise 1 ("How would you treat a friend?") and Exercise 2 ("Self-Compassion Break")', '20 minutes'),
        ('ggia', 'Search for "Self-Compassionate Letter" and read the practice', '10 minutes'),
        ('enchiridion', 'Read sections 1 to 5 (what is and isn\'t in our control; it is not things but our judgements about them that disturb us)', '15 minutes'),
    ],
    steps=[
        'Write one limiting belief and turn it into a testable prediction.',
        'Design and carry out a small, safe test this week.',
        'Record the result versus the prediction and write a new belief.',
        'Use the self-compassion break at least three times this week, and do the "treat a friend" exercise once. Note what you did next each time.',
    ],
    proof='Your behavioural experiment (belief, prediction, test, result, new belief) and notes on three self-compassion breaks plus one friend exercise.',
    templates=[('Behavioural experiment and self-compassion break', """BEHAVIOURAL EXPERIMENT                    Date ______
Belief: "People like me can't ________________________."
How much I believe it (0-100%): ___
Prediction: If I ________________, then ________________ will happen.
Test (small and safe): ________________ on ______
What actually happened: ________________________________
New belief: ____________________________  Belief in old one now: ___%

SELF-COMPASSION BREAK (1 minute)
1. "This is hard right now."
2. "Others go through this too."
3. "May I be kind to myself and learn from this."
4. One concrete step now: ______________""", '')],
    mistakes=[
        ('Repeating affirmations you don\'t believe.', 'They can backfire. Test beliefs with experiments instead.'),
        ('Confusing self-compassion with excuses.', 'Be honest about the mistake and kind about the person; then take a concrete step.'),
        ('Designing tests that are too big.', 'A test should be small and safe enough to actually do this week.'),
        ('Expecting one experiment to erase a belief.', 'Beliefs weaken with repeated evidence. Run several small tests.'),
    ],
    quiz=[
        Q('What is the main CBT way of changing a limiting belief?', 'A behavioural experiment: test the belief as a prediction in real life', 'Repeating positive affirmations', 'Ignoring it', 'Arguing with others about it', why='Real evidence changes beliefs better than slogans.'),
        Q('What are Neff\'s three parts of self-compassion?', 'Self-kindness, common humanity and mindfulness', 'Self-esteem, confidence and pride', 'Forgiveness, forgetting and moving on', 'Positive thinking, optimism and hope', why='Neff\'s model has these three components.'),
        Q('What did Breines and Chen find about self-compassion after failure?', 'It increased motivation to improve', 'It made people lazy', 'It had no effect', 'It increased self-pity', why='Self-compassionate people studied longer and were more willing to make amends.'),
        Q('Why might "I am a lovable person" backfire for some people?', 'It can clash with what people with low self-esteem believe and make them feel worse', 'It is too short', 'It is not in Malayalam', 'It never backfires', why='Wood and colleagues found it made low self-esteem participants feel worse.'),
    ],
    study='read the lesson and do Neff\'s two exercises',
    action='run one behavioural experiment on a limiting belief and use the self-compassion break three times',
)

LESSONS = [L1, L2]

MODULE = module(
    9,
    overview=f"""
Mindset and self-talk with honest evidence: what growth mindset really does (a small effect, mostly for struggling learners), how to test limiting beliefs with behavioural experiments, and how self-compassion helps you improve rather than go soft.

The way you talk to yourself after a failure shapes what you do next. This module avoids the hype ("Change your mindset, change your life!") and keeps the useful core: treat your current level as temporary, change strategies, test your beliefs against reality, and be firm about standards and kind about the person.

These skills prepare you for the harder emotional work of Modules 10 and 11, and for the confidence and rejection work in Modules 13 and 14.
""",
    outcomes=[
        'Explain growth mindset and the honest size of its effects.',
        'Use effort plus strategy plus help to grow a real skill, with numbers.',
        'Run a behavioural experiment on a limiting belief.',
        'Use self-compassion practices and explain why they don\'t make you lazy.',
    ],
    lessons=LESSONS,
    project='a self-talk rewrite backed by evidence',
    project_steps=[
        'For one week, collect five examples of your self-talk after mistakes, word for word.',
        'For each, write a rewrite that is honest about the mistake, kind about the person and names one next step.',
        'Run one behavioural experiment on the belief behind your harshest self-talk.',
        'Write your new "default sentence" for mistakes and put it in your Playbook.',
    ],
    project_proof='Five self-talk examples with rewrites, one behavioural experiment and your default sentence.',
    rubric=[
        ('Honesty about mindset evidence', 'Repeats hype', 'Knows effects are mixed', 'Explains the small average effect and who benefits more'),
        ('Skill growth', 'No measurement', 'Before or after only', 'Before and after numbers with a new strategy'),
        ('Belief testing', 'No experiment', 'Experiment planned', 'Experiment done with a new belief written'),
        ('Self-compassion', 'Not practised', 'Practised once', 'Practised several times with concrete next steps'),
    ],
    short=[
        'Use "yet" and the three questions (strategy, alternative, help) after one failure.',
        'Use the one-minute self-compassion break twice this week.',
    ],
    flashcards=[
        ('Growth mindset intervention effect (meta-analysis)', 'Very small on average (d = 0.08); larger for low-income and struggling students.'),
        ('Mindset–achievement link', 'Weak (r = .10) across 273 samples.'),
        ('The useful version of growth mindset', 'Effort + better strategies + help-seeking + learning from mistakes.'),
        ('Behavioural experiment', 'Turn a belief into a prediction, test it, compare, update.'),
        ('Self-compassion: three parts', 'Self-kindness, common humanity, mindfulness.'),
        ('Does self-compassion reduce motivation?', 'No: experiments found more motivation to improve.'),
        ('Why affirmations can backfire', 'They clash with existing beliefs and can make people feel worse.'),
    ],
    mistakes=[
        ('Using mindset language to blame people.', 'Struggles have many causes; offer strategies and support.'),
        ('Harshness as motivation.', 'It increases avoidance. Be firm about standards, kind about the person.'),
        ('Skipping the measurement.', 'Numbers turn a slogan into real evidence of growth.'),
    ],
    tools=[
        'The skill growth card (PD-M09-L01).',
        'The behavioural experiment and self-compassion break (PD-M09-L02).',
    ],
    playbook=[
        'After a mistake I say: "______" (honest, kind, with one next step).',
        'When I think "people like me can\'t…", I test it with a small experiment.',
    ],
)
