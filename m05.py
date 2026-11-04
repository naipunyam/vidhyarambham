from common import lesson, module, link, xref, table, Q

L1 = lesson(
    5, 1,
    outcome='You can name your top five values in your own words, score your life wheel, and pick one value-based action for your lowest area.',
    split='15 minutes reading, 40 minutes of exercises',
    principle='Knowing what matters to you gives direction when motivation is low; values are chosen directions, not goals you finish, and they are best seen in what you do, not what you say.',
    science=f"""
**What values are.** Psychologists describe values as broad, lasting beliefs about what is important: family, honesty, freedom, security, achievement, helping others, tradition. Shalom Schwartz's research across more than 80 countries found a similar set of basic human values everywhere, arranged in a circle where some sit naturally together (achievement and power) and some pull against each other (tradition versus stimulation, self-interest versus caring for others). Cultures and people differ mainly in how they **rank** these values, not in having different ones.

**Values versus goals.** In **Acceptance and Commitment Therapy (ACT)**, a form of CBT with good evidence for anxiety, depression and chronic pain, values are described as directions, like "west", while goals are places on the way, like "Kozhikode". You never finish "being a caring son"; you can complete "take my father to his eye check-up on Saturday". Values help when goals fail: if you miss a rank list, the value of "learning" or "serving people" is still there to act on.

**Does writing about values help?** Short "values affirmation" exercises, in which people write about a value that matters to them, were found in early studies to reduce stress and improve the performance of students under threat. Later, larger replications found smaller and less consistent effects. So treat values writing as a useful reflection tool, not a magic intervention.

**The life wheel.** The life wheel (or wheel of life) is a coaching tool, not a psychological test. You rate satisfaction in about eight areas of life from 1 to 10. Its value is practical: it shows imbalance at a glance (a "flat" spoke) and gives a baseline to compare later. Your baseline scores from week 0 are on your Baseline A note.

**A Kerala note.** In family-centred cultures, people sometimes list values they were taught (duty, respect for elders, religion) without asking whether they also hold them personally. Both can be true: many people deeply hold inherited values. The exercise is to *choose* consciously, not to reject tradition.
""",
    evidence=[
        ('A common set of basic values across cultures (Schwartz)', 'strong', 'Supported by surveys in more than 80 countries.'),
        ('Values-based action as part of ACT', 'moderate', 'ACT has good trial evidence; the specific contribution of values work is harder to isolate.'),
        ('Brief values-affirmation writing improves performance', 'mixed', 'Early studies were promising; large replications found small or inconsistent effects.'),
        ('Life wheel', 'tool', 'A coaching tool for reflection and tracking; not a validated test.'),
    ],
    example=f"""
Ashiq lists his values quickly: "success, family, money". When he does the exercise properly, he finds that the stories he is proudest of are teaching his nephew maths, standing by a friend in a dispute, and organising flood relief in 2018. His top five, in his own words: "helping people learn", "loyalty to friends and family", "being fair", "financial independence", "steady improvement".

His life wheel shows Health 3, Friends 4, Learning 7, Money 4, Family 6, Fun 2, Purpose 5, Mind 4. His lowest areas are Fun and Health. He picks a value-based action for Health that also fits "loyalty to friends": a 6 am walk with his cousin three times a week. It is small, but it serves two values at once.
""",
    apply=f"""
**Find your values in four steps (about 30 minutes):**

1. **Peak moments:** write three times you felt proud, alive or "this is me". What values were you living?
2. **Anger and envy:** what makes you angry (injustice? laziness? cruelty?) and whom do you envy? Both point to values being blocked or wanted.
3. **The funeral or retirement speech:** what would you like people to say about you at 70? (Not your job title: how you treated people, what you stood for.)
4. **Choose five,** in your own words, and rank them. For each, write one sentence: "This means I ______."

**Use them weekly:** in the Sunday reflection, ask "Which value did I act on this week? Which did I neglect?"

**With others:** values explain many family arguments. Your father may rank **security** highly and you may rank **freedom**: you are not enemies, you weigh things differently. Naming this ("I think you want me to be safe; I also want to try this") lowers the heat.
""",
    resources=[
        ('ggsc', 'Search the site for "values" and read one article about living by your values', '10 minutes'),
        ('ggia', 'Search for a values-affirmation or "Best Possible Self" practice and read it', '10 minutes'),
        ('noba', 'Search for the module "Self and Identity" and read the introduction and the part on the self-concept', '20 minutes'),
    ],
    steps=[
        'Do the four-step values exercise in your Playbook notebook.',
        'Write your top five values, ranked, each with a "This means I…" sentence.',
        'Look at your Baseline A life wheel. Choose the lowest area and write one action for the next week that serves one of your values.',
        'Do the action and write two lines about how it went.',
    ],
    proof='Your ranked top five values with meanings, your life-wheel scores, one value-based action for your lowest area, and two lines on doing it.',
    templates=[('Values worksheet', """VALUES WORKSHEET                         Date ______
Peak moments (3): what was I doing, what value was I living?
1. ______________________ -> ______________
2. ______________________ -> ______________
3. ______________________ -> ______________
What makes me angry? ____________  Whom do I envy, and for what? ____________
At 70, I want people to say I was: ____________________________________
MY TOP FIVE (ranked, in my words)     This means I...
1. ________________                   ______________________________
2. ________________                   ______________________________
3. ________________                   ______________________________
4. ________________                   ______________________________
5. ________________                   ______________________________
Lowest life-wheel area: ________  Value-based action this week: ______________""", '')],
    mistakes=[
        ('Listing what sounds good.', 'Check each value against your behaviour. If you never act on it, it is a wish, not a value (or a value you want to grow into: say so).'),
        ('Treating values as goals.', 'Values are directions. Turn them into weekly actions.'),
        ('Trying to raise every life-wheel area at once.', 'Pick one low area at a time.'),
    ],
    quiz=[
        Q('What is the difference between a value and a goal, in ACT terms?', 'A value is a direction you never finish; a goal is a point you can complete', 'They are the same thing', 'Goals matter and values do not', 'Values are only religious', why='Values are like "west"; goals are destinations on the way.'),
        Q('What did large replications find about brief values-affirmation writing?', 'Smaller and less consistent effects than early studies', 'Large effects for everyone', 'That it harms students', 'That it was never studied', why='The early promise did not fully hold up in larger studies.'),
        Q('What kind of tool is the life wheel?', 'A coaching tool for reflection and tracking, not a validated test', 'A diagnostic test', 'A personality test', 'A medical scale', why='It is useful for seeing balance, not for measuring traits.'),
        Q('Your father values security and you value freedom. What is the most helpful view?', 'You weigh shared values differently; naming this can reduce conflict', 'One of you is wrong', 'Values cannot be discussed', 'You should drop your values', why='Most value conflicts are about ranking, not having opposite values.'),
    ],
    study='read the lesson and one Greater Good article on values',
    action='find your top five values, act on one in your lowest life-wheel area, and write about it',
)

L2 = lesson(
    5, 2,
    outcome='You can interpret your Big Five and VIA results sensibly, explain why MBTI-style type tests are unreliable, and use your strengths deliberately.',
    split='25 minutes reading, 30 minutes of tasks',
    principle='Personality is best described as five broad traits on a scale, not as types; traits are fairly stable but can change, and knowing your strengths is useful only if you use them.',
    science=f"""
**The Big Five.** Decades of research, starting from the words people in many languages use to describe each other, converged on five broad traits (OpenStax Psychology 2e chapter 11 and Noba cover them):

- **Openness to experience:** curiosity, imagination, liking new ideas.
- **Conscientiousness:** organisation, self-discipline, reliability.
- **Extraversion:** sociability, energy, seeking stimulation.
- **Agreeableness:** warmth, cooperation, trust.
- **Neuroticism** (or its opposite, **emotional stability**): tendency to feel anxiety, worry and low mood.

Each trait is a **continuum**; most people score near the middle. The Big Five predicts real outcomes modestly but reliably: conscientiousness predicts job and academic performance and even health and longevity; neuroticism predicts risk of anxiety and depression. Effects are real but moderate; your traits do not decide your life.

**Do traits change?** Traits are fairly stable in adulthood, but they shift slowly, with most people becoming more conscientious, agreeable and emotionally stable from their twenties to middle age (the "maturity principle"). Some studies suggest people who want to change a trait and act differently for weeks can shift a little, though results vary. Expect small changes over this course, if any.

**Your test.** The {link('ipip-bffm', 'IPIP Big Five Factor Markers')} test you took uses public-domain items from the {link('ipip', 'International Personality Item Pool')}. It is a good research-style measure for self-understanding, but it is not a clinical or hiring test.

**Why not MBTI?** The Myers–Briggs Type Indicator sorts people into 16 types using four either/or choices (for example, introvert or extravert). Its problems, documented in the research ({link('wp-mbti', 'summary on Wikipedia')}):
- **Unreliable:** between 39% and 76% of people get a different type when they retake it after only five weeks.
- **False either/or:** scores on each scale cluster in the middle (like height), not in two groups, so people with nearly identical scores get opposite labels.
- **Weak prediction:** its own manual advises against using it to predict job success.
- **Overlap:** its scales roughly match four of the Big Five, minus neuroticism.

Free online "type" quizzes (including ones based on the Enneagram, colours or animals) are entertainment at best.

**Character strengths (VIA).** Christopher Peterson and Martin Seligman catalogued 24 character strengths (such as kindness, curiosity, perseverance, humour, fairness), grouped under six virtues, and the free {link('via', 'VIA survey')} ranks yours. Studies of "use your top strengths in a new way each day" exercises found small boosts in wellbeing in some trials; evidence is moderate and effects are modest. The useful idea: build on what you are already good at, rather than only fixing weaknesses.
""",
    evidence=[
        ('Big Five traits describe personality across cultures', 'strong', 'Found in many languages and countries, though some traits appear less clearly in some cultures.'),
        ('Conscientiousness predicts work, study and health outcomes', 'strong', 'Consistent, moderate effects in large studies and reviews.'),
        ('Traits change slowly with age (maturity principle)', 'strong', 'Large long-term studies show average increases in conscientiousness, agreeableness and stability.'),
        ('Deliberately changing a trait in weeks', 'mixed', 'Some studies find small changes; others do not.'),
        ('MBTI types are reliable and predictive', 'failed', 'Poor retest reliability and weak prediction; scores are not two separate groups.'),
        ('Using top strengths in new ways boosts wellbeing', 'moderate', 'Small positive effects in several trials.'),
    ],
    example=f"""
Sreeja's results: Openness 82nd percentile, Conscientiousness 35th, Extraversion 28th, Agreeableness 70th, Emotional stability 30th. Her VIA top five: love of learning, kindness, fairness, curiosity, appreciation of beauty.

She first reads them as a verdict ("I'm lazy and anxious"). Then she reframes. Low-ish conscientiousness means she will rely more on **systems** than on discipline (environment design and if-then plans in Module 8). Lower emotional stability means stress tools matter for her (Module 11), and that her worry is a trait, not a personal failure. High openness and love of learning are strengths she can use: she turns dull topics into curiosity questions ("Why did this river become the boundary?"). Her friend took a free "16 personalities" quiz and was told he is "an introvert who should avoid sales". She shows him the retest numbers and suggests he judge himself by what he has actually done.
""",
    apply=f"""
**Using your Big Five:**

- **Not a label, a map.** Write: "Because I score ______ on ______, I will rely on ______ (a system or support)." For example: "Because my conscientiousness is low, I will set fixed study times and keep my phone out of the room."
- **Know your traps:** high agreeableness may make saying no hard (PD-M26-L02); low extraversion may make networking tiring (plan shorter events and recovery time, PD-M31-L03); high openness may scatter your focus across too many interests.
- **Remember the middle:** if you are near the 50th percentile, the trait barely describes you either way.

**Using your strengths (one week):** each day, use one of your top five strengths in a new way: "kindness" by helping a younger aspirant with a doubt, "curiosity" by asking a shopkeeper how their business started, "perseverance" by doing one extra past paper.

**With others:** never judge people by a type. Ask about what they enjoy and how they work best instead.
""",
    resources=[
        ('ipip-bffm', 'If you skipped the baseline, take the 50-item test now; read the explanation of each trait on the results page', '15 minutes'),
        ('via', 'Read the descriptions of your top five strengths on the site', '10 minutes'),
        ('wp-mbti', 'Read the criticism section (reliability, dichotomies, validity)', '10 minutes'),
        ('noba', 'Search for the module "Personality Traits" and read the Big Five section', '20 minutes'),
    ],
    steps=[
        'Write your five Big Five percentiles and your VIA top five in your Playbook notebook.',
        'For each Big Five trait, write one "Because I score…, I will rely on…" sentence.',
        'For seven days, use one top strength in a new way each day and log it in one line.',
        'Ask one person who knows you well which three strengths they see in you. Compare with your VIA results.',
    ],
    proof='Your trait sentences, a seven-day strengths log and the other person\'s three strengths compared with your VIA top five.',
    templates=[('Self-awareness profile', """SELF-AWARENESS PROFILE                 Date ______
Big Five (percentiles):  O ___  C ___  E ___  A ___  Emotional stability ___
Because I score ______ on ______, I will rely on ______.
Because I score ______ on ______, I will watch out for ______.
VIA top five: 1 ______ 2 ______ 3 ______ 4 ______ 5 ______
Strengths others see in me (ask 1-2 people): ______ ______ ______
Strengths-in-a-new-way log (7 days):
Day | Strength | New way I used it | How it felt (1-5)""", '')],
    mistakes=[
        ('Treating scores as fixed destiny.', 'Traits shift slowly and do not decide outcomes. Use them to design systems, not excuses.'),
        ('Comparing your percentiles with friends as "better" or "worse".', 'Each trait has advantages and costs. High agreeableness helps teamwork but can make you easy to pressure.'),
        ('Taking type quizzes seriously.', 'Retest reliability is poor. Prefer the Big Five, and judge people by behaviour.'),
        ('Ignoring strengths and only fixing weaknesses.', 'Use your strengths to work around weaknesses.'),
    ],
    quiz=[
        Q('Which Big Five trait most consistently predicts work and study performance?', 'Conscientiousness', 'Extraversion', 'Openness', 'Agreeableness', why='Conscientiousness shows consistent, moderate links with performance.'),
        Q('What is the main reliability problem with MBTI?', 'Many people get a different type when retested after a few weeks', 'It has too many questions', 'It is too expensive', 'It measures only intelligence', why='Between 39% and 76% got a different type after five weeks in studies.'),
        Q('Scores on personality scales usually:', 'Cluster around the middle, like height', 'Split into two clear groups', 'Are all extreme', 'Change every day', why='Traits are continuous, so either/or types mislabel many people.'),
        Q('How should you use a low conscientiousness score?', 'Rely more on systems such as fixed times and environment design', 'Accept you can never be disciplined', 'Ignore it', 'Retake the test until it is higher', why='Traits guide which supports you need; they are not destiny.'),
    ],
    study='read the lesson, your trait descriptions and the MBTI criticism section',
    action='write a trait sentence for each Big Five trait and use a top strength in a new way for seven days',
)

LESSONS = [L1, L2]

MODULE = module(
    5,
    overview=f"""
Self-awareness that is useful: your values, your life wheel, your Big Five personality and your VIA character strengths, and why MBTI-style type tests mislead. You build a one-page self-awareness profile that guides the rest of Part B.

Part B, Master yourself, starts with knowing yourself. Not in a vague "find yourself" way, but with tested tools: a values exercise, a life wheel, a research-grade personality measure and a strengths survey. Each gives you a specific design decision: which goals fit you (Module 7), which habits need support (Module 8), where stress hits hardest (Module 11).

You already have your baseline scores from week 0. This module teaches you to read them sensibly and to avoid both over-trusting and dismissing them.
""",
    outcomes=[
        'Name, rank and explain your top five values.',
        'Read your life wheel and pick one area to improve.',
        'Interpret your Big Five scores and turn each into a design sentence.',
        'Explain three reasons MBTI-style type tests are unreliable.',
        'Use your VIA top strengths deliberately.',
    ],
    lessons=LESSONS,
    project='your one-page self-awareness profile',
    project_steps=[
        'Combine your values, life-wheel scores, Big Five design sentences and strengths into one page.',
        'Add one line: "The area I most want to change in the next six months is ______, because it serves my value ______."',
        'Show the page to one trusted person and ask: "What did I miss?" Add their answer.',
        'Copy the key lines into your Personal Playbook.',
    ],
    project_proof='Your one-page profile with the trusted person\'s comment.',
    rubric=[
        ('Values', 'Generic list', 'Five values with some meaning', 'Five ranked values, each with a behaviour sentence'),
        ('Personality', 'Scores only', 'Scores with some interpretation', 'A design sentence for each trait'),
        ('Strengths', 'VIA list only', 'Strengths used on some days', 'Seven-day log and outside view compared'),
        ('Honesty about tests', 'Treats type tests as truth', 'Knows they are weak', 'Explains reliability and dichotomy problems'),
    ],
    short=[
        'Write your top three values and your lowest life-wheel area.',
        'Write one "Because I score…, I will rely on…" sentence for conscientiousness.',
    ],
    flashcards=[
        ('Values versus goals', 'Values are directions; goals are completable points on the way.'),
        ('The Big Five', 'Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism (emotional stability).'),
        ('Best Big Five predictor of performance', 'Conscientiousness.'),
        ('Maturity principle', 'Most adults slowly become more conscientious, agreeable and emotionally stable.'),
        ('MBTI retest problem', '39–76% got a different type after five weeks.'),
        ('Why types mislead', 'Trait scores cluster in the middle; either/or cut-offs split near-identical people.'),
        ('VIA survey', 'Free survey ranking 24 character strengths.'),
        ('Life wheel status', 'Coaching tool for reflection, not a validated test.'),
    ],
    mistakes=[
        ('Doing the tests but not the design sentences.', 'Self-knowledge matters only when it changes how you set up your days.'),
        ('Copying values from parents or posters without checking.', 'Keep inherited values you truly hold; check each against your behaviour.'),
        ('Labelling others by type.', 'Ask what people enjoy and how they work best instead.'),
    ],
    tools=[
        'The values worksheet (PD-M05-L01).',
        'The self-awareness profile with trait sentences and a strengths log (PD-M05-L02).',
    ],
    playbook=[
        'My top five values: ______. I check one value-based action every Sunday.',
        'My VIA top strengths: ______. Because I score ______ on ______, I rely on ______.',
    ],
)
