from common import lesson, module, link, xref, table, fence, Q

L1 = lesson(
    34, 1,
    outcome='You can define integrity and responsibility in practical terms, run a character audit against your values, and use three habits that make honest behaviour easier.',
    split='20 minutes reading, 30 minutes of tasks',
    principle='Integrity means acting by your values and keeping your word when it costs something; most people are honest most of the time but bend in small ways under pressure, so design your life to make honesty easy.',
    science=f"""
**What character means.** Psychologists use "character" for morally valued traits: honesty, fairness, responsibility, kindness, humility, courage. The VIA classification you took (PD-M05-L02) lists 24 character strengths. **Integrity** usually means consistency between values and actions, and **keeping commitments**; **responsibility** means owning your actions and their effects, including mistakes.

**How honest are people?** Dan Ariely and colleagues reported many experiments in which people cheated "a little" (over-reporting puzzle scores slightly) but rarely a lot, suggesting most people want to see themselves as honest while taking small advantages. **Caution:** one famous study in this line (on signing an honesty pledge at the top of a form) was **retracted in 2021** after evidence of fabricated data, and related findings failed to replicate. So be careful with specific claims from this research. A large 2019 field study by Alain Cohn and colleagues, which "lost" over 17,000 wallets in 40 countries, found that people were **more likely to return wallets that contained more money**, contrary to what most experts predicted, suggesting honesty is more common than people assume. (Rates differed by country; India was included.)

**Situations matter.** People behave less honestly when they are tired, rushed, anonymous, when others around them cheat (social norms), when rules are unclear, and when they can tell themselves a story ("everyone does it", "it's only a small thing"). They behave more honestly with clear rules, reminders of their values, being seen, and fair treatment.

**Responsibility and blame.** Taking responsibility is different from self-blame. Research on **attribution** (PD-M24-L02) and self-compassion (PD-M09-L02) suggests the healthy combination is: "I did this; it had these effects; here is what I'll do to fix it and prevent it," without harsh self-condemnation. People who apologise and repair are usually trusted more afterwards (PD-M31-L02).

**Public service and integrity.** For anyone aiming at a government job, integrity is central: honest use of public money, no bribes, fair treatment of every citizen regardless of caste, religion or status, and keeping records truthfully. The Stoic emperor Marcus Aurelius wrote extensively about doing one's duty honestly; Benjamin Franklin listed "Sincerity" and "Justice" among his 13 virtues and tracked them daily.

**Small things compound.** Character shows in small acts: returning extra change, keeping a minor promise, not copying in a mock test, giving credit, admitting a mistake at work. These small acts build both your reputation and your identity (PD-M08-L03).
""",
    evidence=[
        ('People cheat a little but rarely a lot, to keep an honest self-image', 'mixed', 'Influential studies; one key study retracted for fabricated data; some findings failed replication.'),
        ('People return lost wallets more often when they contain more money', 'moderate', 'Large field study across 40 countries (Cohn et al., 2019).'),
        ('Situations (fatigue, anonymity, norms) affect honesty', 'moderate', 'Supported by many studies, though effect sizes vary.'),
        ('Apology and repair rebuild trust', 'moderate', 'Supported by apology and trust research.'),
        ('Tracking virtues daily (Franklin\'s method)', 'tool', 'A practical self-monitoring method; consistent with monitoring research.'),
    ],
    example="""
Vinod runs his character audit for one week against his top values (honesty, fairness, family). He finds:
- He told a customer a repair would cost ₹800, then charged ₹950 "for parts" without asking first. (**Integrity gap**.)
- He promised his nephew a cricket bat "next week" three times.
- He took credit in his study group for a summary another member wrote half of.
- He returned ₹200 extra change at the vegetable shop. (**Good**.)

His fixes: a written quote with a "parts may change; I'll call you first" line for every repair; a rule that he only promises things with a date he puts in his phone; and a message to his study group: "Divya wrote the first half of the Polity summary, sorry I didn't mention it." He buys the cricket bat that Saturday.

His Franklin-style tracker for two weeks has three columns: "kept my word", "told the full truth", "gave credit". He ticks most days and notices that the written quote made honesty *easier*: no awkward conversations later.
""",
    apply=f"""
**The character audit (one week):**
1. Write your top five values (PD-M05-L01).
2. Each evening, note one moment you **lived** a value and one moment of a **gap** (a small lie, a broken promise, a missed chance to be fair or kind).
3. For each gap: what made it easy (rushed, tired, everyone does it, a story you told yourself)?
4. Choose one **design fix** that makes the honest choice easier next time.

**Three habits that make honesty easy:**
1. **Promise less, with dates:** only commit to what you can schedule; put it in your calendar.
2. **Write it down:** quotes, agreements, who did what. Clarity reduces "grey" situations.
3. **Fix fast:** when you slip, admit it quickly, apologise specifically and repair.

**Franklin-style virtue tracker (two weeks):** choose three practices (e.g. kept my word, told the full truth, gave credit) and tick them each day.

{fence('''VIRTUE TRACKER (two weeks)
Practice              M T W T F S S | M T W T F S S
Kept my word          [ ][ ][ ][ ][ ][ ][ ] [ ][ ][ ][ ][ ][ ][ ]
Told the full truth   [ ][ ][ ][ ][ ][ ][ ] [ ][ ][ ][ ][ ][ ][ ]
Gave credit / owned   [ ][ ][ ][ ][ ][ ][ ] [ ][ ][ ][ ][ ][ ][ ]
my mistakes''')}

**With others:** don't police others' small lapses publicly. Model honesty and make it easy for others (clear agreements, fair processes, thanks when people admit mistakes).
""",
    resources=[
        ('franklin', 'Read Franklin\'s list of 13 virtues and his description of his little book for tracking them', '20 minutes'),
        ('meditations', 'Read the opening of the third book, on doing your duty and acting justly', '15 minutes'),
        ('via', 'Re-read the descriptions of honesty, fairness and perseverance in the strengths list', '10 minutes'),
    ],
    steps=[
        'Do the one-week character audit: one value lived and one gap each evening.',
        'For each gap, write what made it easy and one design fix.',
        'Repair at least one gap (keep a promise, correct credit, return something, apologise).',
        'Keep the virtue tracker for two weeks with three practices.',
    ],
    proof='Your seven-day character audit, the design fixes, a note on one repaired gap and the two-week virtue tracker.',
    templates=[('Character audit', """CHARACTER AUDIT (one week)          My top values: ______
Day | Value lived (what I did) | Gap (what I did or didn't do) | What made the gap easy | Design fix
Mon | ______ | ______ | rushed / tired / "everyone does it" / unclear rule / ______ | ______
...
Gap repaired: ______ (how: kept promise / corrected credit / returned / apologised)""", '')],
    mistakes=[
        ('Thinking integrity is only about big moral choices.', 'It is built and shown in small daily acts.'),
        ('Self-condemnation after a slip.', 'Own it, fix it, design a better situation.'),
        ('Quoting the retracted honesty-pledge study.', 'Be careful: some famous findings in this area were retracted or failed replication.'),
        ('Promising more than you can keep.', 'Promise less, with dates.'),
    ],
    quiz=[
        Q('What did the 2019 lost-wallet study across 40 countries find?', 'People returned wallets more often when they contained more money', 'Nobody returned wallets', 'Only empty wallets were returned', 'Honesty was the same everywhere', why='Cohn and colleagues\' surprising result.'),
        Q('What happened to a famous study on signing an honesty pledge at the top of a form?', 'It was retracted in 2021 after evidence of fabricated data', 'It was confirmed by many studies', 'It won a prize', 'It was never published', why='A warning to treat this research carefully.'),
        Q('Which is a design fix for honesty?', 'Giving written quotes and only making promises with dates', 'Trying to remember to be honest', 'Avoiding all customers', 'Never apologising', why='Clarity makes the honest choice easier.'),
        Q('What is healthy responsibility?', 'Owning your actions and effects, fixing them, without harsh self-condemnation', 'Blaming yourself for everything', 'Blaming the situation for everything', 'Hiding mistakes', why='Responsibility plus self-compassion.'),
    ],
    study='read the lesson and Franklin\'s 13 virtues',
    action='do a one-week character audit, repair one gap and keep a two-week virtue tracker',
)

L2 = lesson(
    34, 2,
    outcome='You can explain what research says about intellectual humility and humour, practise both, and use humour in ways that connect rather than hurt.',
    split='20 minutes reading, 25 minutes of tasks',
    principle='Humility means seeing yourself accurately and staying open to learning; humour that is kind and shared builds connection and resilience, while humour that mocks people damages trust.',
    science="""
**Humility.** Researchers distinguish **intellectual humility** (recognising the limits of your knowledge and being open to being wrong) from general humility (an accurate, modest view of yourself and an orientation towards others). Studies by Mark Leary and colleagues found that people higher in intellectual humility were better at judging the strength of arguments, more open to opposing views and less likely to dismiss people who disagree. Humble leaders have been linked to more engaged and learning-oriented teams in several studies (for example, by Bradley Owens and David Hekman), though research is still developing. Humility is **not** low self-esteem or false modesty: it means accurate self-assessment plus interest in others.

**Humility in practice:** saying "I don't know" and "I was wrong"; asking for feedback (PD-M26-L03); giving credit (PD-M25-L03); treating everyone (the cleaner, the peon, the officer) with the same respect; and noticing when your confidence outruns your accuracy (overconfidence, PD-M03-L01).

**Humour.** Rod Martin's research distinguished four humour styles:
- **Affiliative:** jokes and fun that bring people together.
- **Self-enhancing:** finding the funny side of life and your own troubles; a healthy coping style.
- **Aggressive:** sarcasm, teasing and mockery that put others down.
- **Self-defeating:** putting yourself down excessively to gain approval.
In his studies, affiliative and self-enhancing humour were linked to better wellbeing and relationships; aggressive and self-defeating humour to worse. Laughter shared with others is linked to bonding (Robin Dunbar's research suggests shared laughter may raise pain tolerance, a sign of endorphin release, in small studies). Claims that "laughter is the best medicine" or that laughter therapy cures illness are overstated; humour helps coping and connection, not as a treatment.

**Kerala context.** Malayalam culture has a rich humour tradition: from Kunchan Nambiar's thullal satire to mimicry and cinema comedy. Much of it is affiliative and self-enhancing; some relies on mocking appearance, caste, gender, region or disability. The research suggests that mocking humour may get laughs but costs trust and hurts people.

**Humour at work and in talks:** light, kind humour (often about yourself or the shared situation) makes speakers more likeable; offensive or forced jokes backfire. When unsure, leave it out (PD-M27-L02).
""",
    evidence=[
        ('Intellectual humility improves openness and judgement of arguments', 'moderate', 'Several studies by Leary and colleagues.'),
        ('Humble leadership is linked to team learning', 'mixed', 'Promising studies; research still developing.'),
        ('Affiliative and self-enhancing humour linked to wellbeing', 'moderate', 'Martin\'s studies and later research.'),
        ('Aggressive humour harms relationships', 'moderate', 'Linked to worse relationships and trust.'),
        ('"Laughter is the best medicine"', 'failed', 'Overstated; humour supports coping and connection, not treatment.'),
    ],
    example="""
In his study group, Ashiq has a reputation as "the funny one". Looking at Martin's humour styles, he realises much of his humour is **aggressive**: mimicking a member's accent from Wayanad, calling another "Professor" sarcastically when she answers correctly. People laugh, but the Wayanad member has gone quiet in sessions.

He changes two things. **Humour:** he keeps the jokes about shared struggles ("Polity articles are like our bus timetable: everyone memorises them and nobody understands them") and about himself ("My mock score went up by 2 marks; at this rate I'll be ready by retirement"), and drops jokes about people. He apologises privately to the member he mimicked. **Humility:** when he gets a GK question wrong and someone corrects him, he says, "You're right, I had that mixed up; thanks," instead of arguing.

Two weeks later, the quiet member starts speaking again in sessions, and the group asks Ashiq to open the next session with a funny current-affairs headline of the week.
""",
    apply="""
**Humility practice (one week):**
1. Say "I don't know" or "I was wrong" at least once a day when it is true.
2. Ask one person a week for feedback on something you think you do well.
3. Treat every person the same: notice how you speak to people with less status (a waiter, a cleaner, a younger student).
4. Before arguing, ask: "What would change my mind?" (PD-M03-L01).

**Humour audit (one week):** note jokes you make and classify them: affiliative, self-enhancing, aggressive or self-defeating. Keep the first two; drop aggressive jokes about people's appearance, caste, religion, gender, region or disability; reduce self-defeating ones.

**Humour that connects:** shared situations, gentle self-deprecation (not self-hatred), playful exaggeration of everyday frustrations, stories of your own mistakes. Test: "Would the person the joke is about laugh too?"

**With others:** when someone makes a hurtful joke, you don't need a lecture; a flat "Not funny, man" or changing the subject often works. Be the "one ally" (PD-M30-L01) for the target.
""",
    resources=[
        ('ggsc', 'Take the free Intellectual Humility quiz if available, or search the site for "intellectual humility" and read one article', '15 minutes'),
        ('enchiridion', 'Read section 46 on not calling yourself a philosopher and acting rather than talking', '5 minutes'),
        ('franklin', 'Read the passage where Franklin added "Humility" to his list after a friend told him he was proud (search for "Humility")', '10 minutes'),
    ],
    steps=[
        'Do the one-week humility practice and log each "I don\'t know / I was wrong" moment.',
        'Do the one-week humour audit, classifying your jokes by style.',
        'Drop or apologise for one hurtful joke pattern, and try one affiliative or self-enhancing joke in a group.',
        'Ask one person for feedback on something you think you do well, and note the answer.',
    ],
    proof='Your humility log, your humour audit with styles counted, a note on the dropped pattern or apology, and the feedback received.',
    templates=[('Humility and humour log', """HUMILITY LOG
Date | "I don't know" / "I was wrong" moment | How it felt | How others responded
Feedback asked: from ______ on ______ ; answer ______
HUMOUR AUDIT
Date | Joke (short) | Style: affiliative / self-enhancing / aggressive / self-defeating | Would the target laugh too?
Count: affiliative __ self-enhancing __ aggressive __ self-defeating __
Pattern I'm dropping: ______  Apology given? ______""", '')],
    mistakes=[
        ('Confusing humility with putting yourself down.', 'Humility is accurate self-assessment plus interest in others.'),
        ('False modesty.', '"Oh, I\'m terrible" when you aren\'t is not humility.'),
        ('Defending a hurtful joke as "just a joke".', 'If the target isn\'t laughing, it isn\'t working.'),
        ('Forcing humour into serious moments.', 'Read the room; leave it out when unsure.'),
    ],
    quiz=[
        Q('What is intellectual humility?', 'Recognising the limits of your knowledge and being open to being wrong', 'Having low self-esteem', 'Never sharing opinions', 'Agreeing with everyone', why='Leary and colleagues\' definition.'),
        Q('Which humour style is linked to better relationships?', 'Affiliative: humour that brings people together', 'Aggressive: mockery and sarcasm', 'Self-defeating: putting yourself down a lot', 'None', why='Martin\'s research on humour styles.'),
        Q('What is a good test for a joke about someone?', '"Would the person the joke is about laugh too?"', '"Will most people laugh?"', '"Is it clever?"', '"Has it gone viral?"', why='Humour that hurts the target damages trust.'),
        Q('What is the honest status of "laughter is the best medicine"?', 'Overstated: humour helps coping and connection, not as a treatment', 'Proven by many trials', 'Laughter is harmful', 'Only true for children', why='Benefits are real but modest.'),
    ],
    study='read the lesson and Franklin\'s passage on humility',
    action='do one week of humility practice and a humour audit, drop one hurtful pattern and ask for feedback',
)

LESSONS = [L1, L2]

MODULE = module(
    34,
    overview=f"""
Character: integrity and responsibility in daily life (with honest notes on the honesty research, including a retracted study), a character audit and virtue tracker in Franklin's style, intellectual humility, and humour that connects rather than hurts.

Part E, Character and purpose, turns from skills to the kind of person who uses them. Every influence, negotiation and leadership skill in Part D becomes either trust-building or manipulative depending on character. Integrity is what makes people trust your persuasion; humility is what keeps you learning.

These are practical exercises, not sermons: audits, trackers and small repairs. Your top values from Module 5 are the measuring stick.
""",
    outcomes=[
        'Define integrity and responsibility in practical, behavioural terms.',
        'Run a character audit and design situations that make honesty easier.',
        'Explain what the research on honesty shows, including its retractions.',
        'Practise intellectual humility.',
        'Use affiliative and self-enhancing humour and avoid hurtful humour.',
    ],
    lessons=LESSONS,
    project='a character audit with a two-week virtue tracker',
    project_steps=[
        'Do the one-week character audit and repair one gap (PD-M34-L01).',
        'Keep a two-week virtue tracker with three practices.',
        'Do the humility practice and humour audit (PD-M34-L02).',
        'Write a half-page character statement: the person you want to be in five years, with three daily practices, and add it to the Playbook.',
    ],
    project_proof='The character audit, the virtue tracker, the humility and humour logs and your character statement.',
    rubric=[
        ('Self-honesty', 'No gaps found', 'Gaps found but not analysed', 'Gaps analysed with design fixes'),
        ('Repair', 'No repair', 'Repair planned', 'At least one gap repaired'),
        ('Tracking', 'No tracker', 'Partial tracker', 'Two weeks of virtue tracking'),
        ('Humour and humility', 'No audit', 'Audit only', 'Audit plus a dropped hurtful pattern and feedback sought'),
    ],
    short=[
        'Make only promises with dates for two weeks.',
        'Say "I was wrong" once this week when it is true.',
    ],
    flashcards=[
        ('Integrity (practical)', 'Acting by your values and keeping your word, especially when it costs something.'),
        ('Lost-wallet study finding', 'More money in the wallet → more often returned (40 countries).'),
        ('Retracted honesty-pledge study', 'Retracted in 2021 for fabricated data; treat this field carefully.'),
        ('Three honesty habits', 'Promise less with dates; write it down; fix fast.'),
        ('Intellectual humility', 'Knowing the limits of your knowledge; open to being wrong.'),
        ('Four humour styles', 'Affiliative, self-enhancing, aggressive, self-defeating.'),
        ('Joke test', '"Would the target laugh too?"'),
    ],
    mistakes=[
        ('Measuring character by intentions.', 'Measure by actions, in an audit.'),
        ('Moralising at others.', 'Start with yourself and model it.'),
        ('Treating humility as weakness.', 'It is linked to better judgement and learning.'),
    ],
    tools=[
        'The character audit and virtue tracker (PD-M34-L01).',
        'The humility and humour log (PD-M34-L02).',
    ],
    playbook=[
        'Integrity: I promise less, with dates; I write agreements down; I fix mistakes fast.',
        'Humility: "I don\'t know", "I was wrong", "What would change my mind?"',
        'Humour: together, not at people. Would the target laugh too?',
    ],
)
