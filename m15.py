from common import lesson, module, link, xref, table, Q

L1 = lesson(
    15, 1,
    outcome='You can explain hedonic adaptation, the costs of social comparison and what research says about money and happiness, and use three counter-strategies.',
    split='20 minutes reading, 25 minutes of tasks',
    principle='We get used to most good and bad changes, we judge ourselves by comparison with others, and money helps happiness more than once claimed but far less than we expect from any single purchase.',
    science=f"""
**Hedonic adaptation.** People adapt to changes in their lives: the joy of a new phone, a salary rise or a new house fades within weeks or months, and many bad events hurt less over time than people predict. Philip Brickman and colleagues' famous 1978 study compared lottery winners and people paralysed in accidents and found smaller long-term differences in happiness than expected. The study was small and is often over-quoted: later large studies found that adaptation is **incomplete** for some events (long-term unemployment, disability, the death of a spouse), and that people differ. But the core finding holds: **we overestimate how long good and bad changes will affect us** (Daniel Gilbert and Timothy Wilson called this the **impact bias**).

**What slows adaptation:** variety, surprise, sharing, savouring and spending on experiences rather than things. Studies by Thomas Gilovich and Leaf Van Boven found people often get more lasting happiness from experiences (a trip, a class, a meal with friends) than from material goods, partly because experiences are shared, become part of who we are and are harder to compare. Later work found the effect depends on the person and the purchase.

**Social comparison.** Leon Festinger (1954) proposed that we evaluate ourselves by comparing with others. **Upward comparison** (with people doing better) can inspire but often lowers mood; **downward comparison** can comfort but can also breed complacency. Social media makes upward comparison constant: we compare our ordinary days with others' highlights. Studies on social media and wellbeing find small average negative links, stronger for passive scrolling than for active contact with friends (Module 16).

**Money and happiness.** Daniel Kahneman and Angus Deaton's 2010 US study suggested that day-to-day emotional wellbeing rose with income only up to about $75,000 a year, then levelled off. Matthew Killingsworth's later data suggested no plateau. In 2023 the two sides ran an **adversarial collaboration** (Killingsworth, Kahneman and Barbara Mellers): on average, happiness rises with income without a plateau; but for the **least happy** people, it rises up to about $100,000 and then levels off ({link('killingsworth', 'ScienceDaily summary')}). As Killingsworth put it, if you're rich and miserable, more money won't help. Note: these are US income figures, and the effect is roughly logarithmic (each doubling of income adds about the same amount), so money matters most when you have little. Other robust findings: **spending on others** (Elizabeth Dunn, Lara Aknin and Michael Norton) and **buying time** (paying to avoid hated chores) are linked to more happiness than spending on yourself; financial security and lower debt reduce stress a great deal.
""",
    evidence=[
        ('Hedonic adaptation to many life changes', 'strong', 'Found in many studies; incomplete for some major events.'),
        ('Impact bias: overestimating how long feelings last', 'strong', 'Replicated across many kinds of events.'),
        ('Experiences beat things for lasting happiness', 'moderate', 'Supported in several studies; depends on person and purchase.'),
        ('Upward social comparison often lowers mood', 'moderate', 'Supported by many studies; effects vary.'),
        ('Happiness rises with income on average (no plateau for most)', 'moderate', 'Adversarial collaboration (2023) on US data; plateau for the least happy.'),
        ('Spending on others raises happiness', 'moderate', 'Several studies across countries; some replications show smaller effects.'),
    ],
    example="""
Vinod saves for eight months and buys a ₹24,000 phone. For two weeks he loves it. By week six it is just his phone (**hedonic adaptation**). Then a friend posts a picture of a newer model, and Vinod's phone suddenly feels old (**upward comparison**).

He decides to test two ideas from the lesson. With the ₹2,000 he would have spent on a phone case and earbuds, he takes his mother and sister for a day trip to Thusharagiri waterfalls (an **experience**, shared). Months later, they still talk about the monkey that stole his sister's banana. And he spends ₹500 on a PSC book for a younger neighbour who can't afford it (**spending on others**). He writes in his journal: "The trip and the book still make me smile. The phone doesn't."

He also mutes three accounts that mostly show expensive gadgets and holidays, and notices less "my life is behind" feeling.
""",
    apply=f"""
**Three counter-strategies:**

1. **Slow adaptation:** vary good things (new routes for your walk, new recipes), savour them (pause and notice for 20 seconds), share them, and occasionally take a break from a pleasure to enjoy it again.
2. **Manage comparison:** compare with your **own past** (your baseline scores) rather than others' highlights; mute or unfollow accounts that consistently make you feel worse; when you envy someone, ask "What exactly do I want here, and what is one step towards it?"
3. **Spend for happiness:** prefer experiences, spending on others, and buying time; build financial security first (an emergency fund lowers stress more than gadgets; see {xref('fin', 'fin-m05', 'the Personal Finance emergency fund module')}).

**Before a big purchase, predict:** "How happy will this make me in 3 months?" Then check later. You will usually find you overestimated (impact bias).

**With others:** stop comparing others too: "Look at your cousin" hurts relationships and rarely motivates.
""",
    resources=[
        ('killingsworth', 'Read the summary of the 2023 money-and-happiness study', '10 minutes'),
        ('yale-wb', 'Audit week 2 or 3 (misconceptions about happiness, why our expectations are so bad); check what is free', '60 minutes'),
        ('ggsc', 'Search the site for "savoring" and read one article', '10 minutes'),
    ],
    steps=[
        'Write three past purchases or events: how happy you predicted they would make you, and how you feel about them now.',
        'Do one savouring practice this week: pause for 20 seconds to fully notice something good, three times.',
        'Spend a small amount (₹100–500) on an experience or on someone else, and write how you felt then and three days later.',
        'Audit social media: list five accounts that make you feel worse and mute or unfollow at least three.',
    ],
    proof='Your three prediction-versus-reality notes, three savouring notes, a note on the experience or gift spending, and a list of accounts muted.',
    templates=[('Happiness experiment sheet', """IMPACT-BIAS CHECK
Purchase or event | Predicted happiness boost (0-10) and how long | Actual feeling now (0-10)
SAVOURING (20 seconds each): Date | What I noticed | How it felt
SPENDING TEST: Rs ___ on (experience / someone else): ______
  Feeling that day (0-10) ___  three days later ___
COMPARISON AUDIT: accounts that make me feel worse: ______ ______ ______
  Muted / unfollowed: ______
Before my next big purchase: predicted happiness in 3 months ___ -> check on ______""", '')],
    mistakes=[
        ('Saying "money doesn\'t buy happiness".', 'More income helps on average, especially when you have little. It just helps less than expected per purchase and doesn\'t fix unhappiness on its own.'),
        ('Quoting the lottery study as proof that nothing matters.', 'It was small; adaptation is incomplete for some events.'),
        ('Comparing yourself with highlights.', 'Compare with your own past.'),
        ('Ignoring financial security.', 'Savings and low debt reduce stress more than most purchases.'),
    ],
    quiz=[
        Q('What is hedonic adaptation?', 'Getting used to good and bad changes so their effect on mood fades', 'Always feeling happy', 'A type of diet', 'Becoming addicted to pleasure', why='We adapt to most changes, though not completely to all.'),
        Q('What did the 2023 adversarial collaboration find about income and happiness?', 'On average happiness keeps rising with income; for the least happy it levels off around $100,000', 'Happiness stops rising at $75,000 for everyone', 'Money has no link to happiness', 'Richer people are always less happy', why='Killingsworth, Kahneman and Mellers resolved their disagreement this way.'),
        Q('Which spending is most linked to lasting happiness?', 'Shared experiences and spending on others', 'Expensive gadgets', 'Brand-name clothes', 'Lottery tickets', why='Experiences and prosocial spending tend to give more lasting happiness.'),
        Q('What is the impact bias?', 'Overestimating how strongly and how long events will affect our feelings', 'Being hit by bad luck', 'Remembering only bad events', 'Underestimating others', why='Gilbert and Wilson\'s term for this forecasting error.'),
    ],
    study='read the lesson and the money-and-happiness summary',
    action='check three past predictions, savour three times, do a small spending test and audit your social media',
)

L2 = lesson(
    15, 2,
    outcome='You can describe the conditions for flow, find more meaning in daily life, and design one happiness experiment for yourself.',
    split='20 minutes reading, 25 minutes of tasks',
    principle='Lasting wellbeing comes less from pleasure than from meaning (doing what matters to you), absorbing challenge (flow) and good relationships; pleasure matters too, but it adapts fastest.',
    science=f"""
**Two kinds of wellbeing.** Researchers distinguish **hedonic** wellbeing (pleasure, positive feelings, life satisfaction) and **eudaimonic** wellbeing (meaning, growth, purpose, living by your values). Both matter, and they overlap. Martin Seligman's **PERMA** model lists five building blocks: Positive emotion, Engagement, Relationships, Meaning and Accomplishment. It is a useful map, though researchers debate how distinct the five really are.

**Flow.** Mihaly Csikszentmihalyi studied people deeply absorbed in activities: surgeons, rock climbers, chess players, factory workers. Using the "experience sampling method" (beeping people at random times to ask what they were doing and feeling), he found that people reported their best moments when **challenge and skill were both high and balanced**, goals were clear and feedback was immediate. Time seems to fly and self-consciousness fades. Too much challenge for your skill → anxiety; too little → boredom. Flow can happen in work, study, sport, music, cooking or conversation. Evidence is mainly from experience sampling and surveys (moderate), showing flow is linked to positive experience and to performance.

**Meaning.** Roy Baumeister and colleagues found that **happiness** and **meaningfulness** overlap but differ: happiness is linked more to having needs met and feeling good now; meaning is linked more to linking past, present and future, giving to others and expressing yourself, and sometimes involves stress and worry (raising children, caring for parents). Viktor Frankl, a psychiatrist who survived Nazi concentration camps, argued in *Man's Search for Meaning* that meaning can be found through work or a cause, through love, and through the attitude we take to unavoidable suffering. His book is a powerful account, not a research study. Research suggests a sense of purpose is linked to better health and longer life in large observational studies, though cause and effect are hard to separate.

**Relationships matter most.** In many studies, the strongest everyday predictor of happiness is the quality of close relationships. The Harvard Study of Adult Development, directed by Robert Waldinger, has followed participants since the late 1930s and emphasises the primacy of relationships for wellbeing and health ({link('ted-waldinger', 'Waldinger\'s TED talk')}). You will build on this in Module 31.
""",
    evidence=[
        ('Flow occurs when challenge and skill are high and balanced', 'moderate', 'Experience-sampling and survey studies across many activities.'),
        ('Meaning and happiness overlap but differ', 'moderate', 'Large surveys (Baumeister and colleagues).'),
        ('Sense of purpose linked to better health and longevity', 'moderate', 'Large observational studies; causality unclear.'),
        ('Close relationships predict wellbeing', 'strong', 'Consistent across many studies and countries.'),
        ('PERMA as five separate building blocks', 'mixed', 'A useful map; the parts overlap statistically.'),
    ],
    example="""
Anu keeps a "flow and meaning" log for a week, rating each main activity 1–5 for enjoyment, absorption and meaning.

Her highest absorption: teaching her neighbour's daughter English on Saturday (challenge matched to skill, clear goal, instant feedback when the girl got it). Her highest meaning: taking her grandmother to the hospital (stressful, low enjoyment, high meaning). Her lowest on all three: two hours of scrolling at night. PSC study was mixed: easy revision was boring (too little challenge); a mock test was anxious (too much); timed sets of 20 questions just above her level gave real flow.

She makes three changes: timed 20-question sets in place of passive rereading; scrolling cut to 30 minutes; and the Saturday class kept as a fixed weekly commitment, because it is both absorbing and meaningful.
""",
    apply="""
**Find more flow:**
- Make tasks **slightly harder than comfortable** (timed sets, a harder level, teaching it to someone).
- Set a **clear goal** for each session and get **fast feedback** (check answers immediately).
- **Remove interruptions** (phone in another room) for at least 25 minutes.
- If anxious, lower the challenge or build skill; if bored, raise the challenge.

**Find more meaning:**
- Connect daily tasks to your values (PD-M05-L01): "This revision serves my value of independence."
- Do one thing for others each week (Module 35).
- Tell your story: how your past, present and future connect.

**Design one happiness experiment (2 weeks):** choose one change (more flow in study, a weekly act for others, less scrolling, a weekly experience with family), rate daily mood 1–10 for one baseline week and one change week, and compare, like your PD-M08-L04 experiment.

**With others:** shared flow (playing music, sport, cooking together, solving problems) builds relationships. Invite people into absorbing activities rather than only passive ones.
""",
    resources=[
        ('ted-waldinger', 'Watch the talk; note the three lessons about relationships', '13 minutes'),
        ('ggsc', 'Take the free Purpose in Life quiz and read the feedback', '10 minutes'),
        ('james-talks', 'Read the essay "What Makes a Life Significant" (in the second half of the book)', '30 minutes'),
    ],
    steps=[
        'Keep a one-week flow and meaning log: each main activity rated 1–5 for enjoyment, absorption and meaning.',
        'Find your top flow activity, your top meaning activity and your biggest low-value activity.',
        'Design and run a two-week happiness experiment with one change and daily mood ratings.',
        'Write the result and one change you will keep.',
    ],
    proof='Your one-week log, your three findings, the two-week experiment numbers and your decision.',
    templates=[('Flow and meaning log', """FLOW AND MEANING LOG (one week)
Day | Activity | Minutes | Enjoyment (1-5) | Absorption/flow (1-5) | Meaning (1-5) | Challenge vs skill (too easy / balanced / too hard)
Top flow activity: ______  Top meaning activity: ______  Biggest low-value activity: ______
HAPPINESS EXPERIMENT (2 weeks)
Change: ______________________
Week 1 (baseline) daily mood 1-10: __ __ __ __ __ __ __  average ___
Week 2 (change)   daily mood 1-10: __ __ __ __ __ __ __  average ___
Other differences: ______  Decision: keep / modify / drop""", '')],
    mistakes=[
        ('Chasing pleasure only.', 'Pleasure adapts fastest. Balance it with meaning, flow and relationships.'),
        ('Expecting to feel happy all the time.', 'Meaningful activities often include stress. Wellbeing is not constant cheerfulness.'),
        ('Treating Frankl or PERMA as lab-proven.', 'They are valuable frameworks; the research behind them is partial.'),
        ('Making tasks too hard in the name of flow.', 'Flow needs balance; too hard creates anxiety.'),
    ],
    quiz=[
        Q('When is flow most likely?', 'When challenge and skill are both high and balanced, with clear goals and quick feedback', 'When a task is very easy', 'When you multitask', 'When you are tired', why='Csikszentmihalyi\'s experience-sampling findings.'),
        Q('How do happiness and meaning differ, according to Baumeister\'s surveys?', 'Happiness is more about feeling good now; meaning links past, present and future and giving to others', 'They are the same', 'Meaning is about money', 'Happiness requires suffering', why='They overlap but have different correlates.'),
        Q('What is the strongest everyday predictor of happiness in many studies?', 'Quality of close relationships', 'Phone model', 'Height', 'Number of followers', why='Relationships consistently predict wellbeing.'),
        Q('If a study task makes you anxious, what does flow research suggest?', 'Lower the challenge a little or build skill first', 'Make it harder', 'Stop studying', 'Add music and videos', why='Anxiety means challenge exceeds skill.'),
    ],
    study='read the lesson and watch Waldinger\'s talk',
    action='keep a one-week flow and meaning log and run a two-week happiness experiment',
)

LESSONS = [L1, L2]

MODULE = module(
    15,
    overview=f"""
Happiness science without the fluff: hedonic adaptation and the impact bias, social comparison, what the 2023 money-and-happiness collaboration found, experiences and spending on others, flow, meaning and relationships. You test one happiness change on yourself with data.

Most people chase happiness through the things that adapt fastest: purchases, status and comparison wins. Research points elsewhere: absorbing challenge, meaning, relationships, and enough money to be secure. This module gives you the evidence and lets you check it against your own life.

Yale's free course {link('yale-wb', 'The Science of Well-Being')} covers these topics in more depth if you want to go further.
""",
    outcomes=[
        'Explain hedonic adaptation, the impact bias and social comparison.',
        'Summarise the current evidence on money and happiness honestly.',
        'Use savouring, experiences and spending on others.',
        'Describe the conditions for flow and design tasks for it.',
        'Run a two-week happiness experiment.',
    ],
    lessons=LESSONS,
    project='a two-week happiness experiment',
    project_steps=[
        'Use your flow and meaning log (PD-M15-L02) to choose one change.',
        'Run the experiment: one baseline week and one change week with daily mood ratings.',
        'Add one savouring practice and one act of spending on others during the change week.',
        'Write a half-page report and add your keeper change to the Playbook.',
    ],
    project_proof='The flow and meaning log, two weeks of mood ratings and your half-page report.',
    rubric=[
        ('Understanding', 'Repeats "money can\'t buy happiness"', 'Knows some findings', 'Explains adaptation, comparison and the 2023 income finding accurately'),
        ('Self-data', 'No log', 'Partial log', 'Full one-week log with ratings'),
        ('Experiment', 'Not done', 'Done without a baseline', 'Baseline and change weeks compared'),
        ('Application', 'No change kept', 'Vague plan', 'A specific change kept and added to the Playbook'),
    ],
    short=[
        'Savour one good moment a day for a week.',
        'Mute three accounts that make you feel worse.',
    ],
    flashcards=[
        ('Hedonic adaptation', 'We get used to most good and bad changes; incomplete for some.'),
        ('Impact bias', 'Overestimating how strongly and how long events will affect us.'),
        ('Money and happiness (2023)', 'Rises with income on average; plateau only for the least happy (US data).'),
        ('Happiest spending', 'Experiences, spending on others, buying time.'),
        ('Upward comparison', 'Comparing with people doing better: often lowers mood.'),
        ('Flow conditions', 'High, balanced challenge and skill; clear goals; quick feedback.'),
        ('PERMA', 'Positive emotion, Engagement, Relationships, Meaning, Accomplishment.'),
        ('Strongest everyday happiness predictor', 'Quality of close relationships.'),
    ],
    mistakes=[
        ('Expecting one purchase or event to change your life.', 'Impact bias. Predict, then check.'),
        ('Using happiness research to judge others\' choices.', 'Apply it to your own life.'),
        ('Ignoring the boring basics.', 'Sleep, exercise, relationships and financial security do much of the work.'),
    ],
    tools=[
        'The happiness experiment sheet: impact-bias check, savouring, spending test, comparison audit (PD-M15-L01).',
        'The flow and meaning log with a two-week experiment (PD-M15-L02).',
    ],
    playbook=[
        'Before big purchases: "How happy will this make me in 3 months?" I prefer experiences and giving.',
        'I compare with my own past, not others\' highlights.',
        'My best flow activity: ______. My most meaningful weekly act: ______.',
    ],
)
