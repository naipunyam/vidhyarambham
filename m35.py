from common import lesson, module, link, xref, table, fence, Q

L1 = lesson(
    35, 1,
    outcome='You can explain what research says about meaning and giving, find a contribution that fits your values and time, and complete a small contribution project.',
    split='20 minutes reading, 40 minutes of planning plus the project',
    principle='Giving time, skills or money to others is linked to greater meaning and wellbeing, especially when you choose it freely, can see its impact and do it with others; it doesn\'t have to be big.',
    science=f"""
**Purpose.** Psychologists William Damon and colleagues define purpose as a stable intention to accomplish something that is **meaningful to you** and **of consequence beyond yourself**. Large observational studies link a stronger sense of purpose with better health and longer life, though cause and effect are hard to separate (PD-M15-L02). The free Greater Good "Purpose in Life" quiz you may have taken in Module 15 gives a quick check.

**Giving and wellbeing.** Research finds:
- **Prosocial spending:** in studies by Elizabeth Dunn, Lara Aknin and Michael Norton, people who spent money on others reported more happiness than those who spent the same on themselves, including in studies across many countries; some later replications found smaller effects.
- **Volunteering:** large surveys link volunteering with better wellbeing and lower mortality, especially in older adults; a 2013 review by Caroline Jenkinson and colleagues found the trial evidence was **weaker and mixed**, so part of the link may be that healthier, happier people volunteer more.
- **What makes giving feel good** (Aknin, Dunn and others): **choice** (it was your decision), **connection** (you meet or work with the people you help or with other volunteers) and **seeing the impact** (you know what difference it made). Forced or guilt-driven giving feels less good (self-determination theory, Module 6).
- **Helper burnout:** giving too much, without rest or boundaries, harms carers (compassion versus empathic distress, PD-M10-L02). Sustainable giving fits your time and energy.

**Kerala's tradition of contribution.** Kerala has strong community networks: the community palliative-care movement that began in the Kozhikode–Malappuram region in the 1990s and spread across the state; blood-donation groups; library and reading-room councils; Kudumbashree; NSS and NCC; and the volunteer response to the 2018 floods, when fishermen and young people rescued thousands. Many of these welcome volunteers with small amounts of time.

**Contribution and your goals.** Contribution is not a distraction from PSC preparation: teaching a younger student strengthens your own learning (learning by teaching, {xref('lrn', 'lrn-m20', 'Learning Capabilities Module 20')}), volunteering builds your network (Module 31) and skills, and service experience gives you true stories for interviews (PD-M33-L02).

**The classics.** William James's essay "What Makes a Life Significant" argues that ordinary people doing their work with courage and ideals lead significant lives; Samuel Smiles's *Self-Help* (1859) celebrates individual effort, but read it critically: it underplays luck, privilege and social support, which modern research shows matter a great deal.
""",
    evidence=[
        ('Purpose linked to better health and longevity', 'moderate', 'Large observational studies; causality unclear.'),
        ('Spending on others increases happiness', 'moderate', 'Studies in many countries; some replications smaller.'),
        ('Volunteering linked to wellbeing and lower mortality', 'moderate', 'Strong observational links; trial evidence weaker and mixed.'),
        ('Choice, connection and visible impact make giving feel good', 'moderate', 'Supported by several experiments.'),
        ('Over-giving without boundaries leads to burnout', 'moderate', 'Supported by carer and empathy research.'),
    ],
    example="""
Anu wants to contribute but has only about two hours a week alongside PSC study. She lists her values (learning, family, fairness) and skills (English, explaining maths, patience) and three options: weekend English sessions for children in her ward; volunteering with the local palliative-care unit on home visits; or donating blood regularly.

She chooses the English sessions (fits her values and skills; she can see the impact) and adds blood donation every few months (low time, high impact). She asks the reading room for a space on Saturday mornings and starts with four children aged 10 to 12, one hour a week, using story books from the library.

After six weeks: six children attend; two can now read a short English story aloud; one mother brings her tea every Saturday. Anu notices she looks forward to Saturday all week. Her own spoken English has improved (learning by teaching), and she has a true story for her interview about "a time you helped your community".
""",
    apply=f"""
**Find your contribution (30 minutes):**
1. **Values:** which of your top values could giving express? (PD-M05-L01)
2. **Skills and strengths:** what can you offer? (teaching, cooking, organising, physical help, design, phones and apps, listening)
3. **Time:** realistic hours a week or month.
4. **Options:** list three local opportunities (ask at the panchayat, library, palliative-care unit, school, religious or cultural organisation, Kudumbashree, blood bank).
5. **Choose:** one regular contribution, plus one occasional one if you like.

{fence('''CONTRIBUTION PROJECT PLAN                 Start ______
Values it serves: ______  Skills I bring: ______
What: ______________________  Where/with whom: ______
Time: ___ hours a week / month, on ______
Who benefits, and how I'll see the impact: ______
Who I'll do it with (connection): ______
Boundaries (what I won't do, max time): ______
Six-week review: sessions ___ ; impact seen ______ ; how I feel ______ ; continue? ______''')}

**Make giving feel good and last:** choose it freely; do it with others; find a way to see the impact; set boundaries.

**Small acts count:** a weekly call to a lonely elderly neighbour, helping a junior with PSC preparation, picking up litter on your walk, sharing free resources in your study group.

**With others:** invite a friend to join you; contribution done together builds friendships too.
""",
    resources=[
        ('james-talks', 'Read the essay "What Makes a Life Significant"', '30 minutes'),
        ('ggsc', 'Take the Purpose in Life quiz (or retake it) and read one article on purpose', '15 minutes'),
        ('ggia', 'Search for a practice on kindness or purpose (for example "Random Acts of Kindness" or "Magic of Purpose") and read it', '10 minutes'),
    ],
    steps=[
        'Fill in the contribution project plan.',
        'Contact the organisation or people involved and agree on a start.',
        'Do the contribution at least four times over about six weeks (or, if it is occasional, complete it once and add small weekly acts of kindness).',
        'Write the six-week review: sessions, impact, how you felt, and whether you will continue.',
    ],
    proof='Your contribution plan, evidence of at least four sessions (a log, photos with permission, or a note from the organiser), and your six-week review.',
    templates=[('Contribution log', """CONTRIBUTION LOG
Date | What I did | Time | Who benefited | Impact I saw | How I felt (1-10)
Small acts of kindness this week: 1 ______ 2 ______ 3 ______""", '')],
    mistakes=[
        ('Waiting for a big cause.', 'Small, regular contributions are where most good happens.'),
        ('Giving out of guilt.', 'Choose freely; guilt-driven giving burns out.'),
        ('Over-giving.', 'Set a maximum time and protect your exam preparation and rest.'),
        ('Posting your good deeds for praise.', 'Share to invite others, not to impress; respect the privacy of people you help.'),
    ],
    quiz=[
        Q('What three features make giving feel best, according to research?', 'Choice, connection and seeing the impact', 'Large amounts, public praise and tax benefits', 'Guilt, obligation and pressure', 'Secrecy, speed and size', why='Aknin, Dunn and colleagues\' findings.'),
        Q('What is the honest status of research linking volunteering and longer life?', 'Strong observational links, but trial evidence is weaker and mixed', 'Proven by many trials', 'No link at all', 'Volunteering shortens life', why='Healthier people may volunteer more.'),
        Q('How can contribution help your own PSC preparation?', 'Teaching others strengthens your own learning and gives you real interview stories', 'It always takes time away with no benefit', 'It replaces studying', 'It doesn\'t', why='Learning by teaching and true service stories.'),
        Q('What protects helpers from burnout?', 'Boundaries, rest and compassion rather than taking on all the distress', 'Giving more hours', 'Never saying no', 'Working alone', why='Sustainable giving fits your time and energy.'),
    ],
    study='read the lesson and William James\'s "What Makes a Life Significant"',
    action='plan and complete a six-week contribution project and write the review',
)

LESSONS = [L1]

MODULE = module(
    35,
    overview=f"""
Purpose and contribution: what research says about meaning, giving and volunteering (with honest caveats), how to find a contribution that fits your values, skills and time, and a six-week contribution project, connected to Kerala's strong tradition of community service.

You have spent this course building yourself: your mind, habits, body and skills with people. This module points those strengths outward. Research suggests that freely chosen giving, done with others and with visible impact, adds meaning and wellbeing to life, and it often brings unexpected benefits: friendships, skills, stories and perspective.

It doesn't have to be big. One hour a week matters.
""",
    outcomes=[
        'Explain what research says about purpose, prosocial spending and volunteering.',
        'Find a contribution that fits your values, skills and time.',
        'Make giving sustainable with choice, connection, visible impact and boundaries.',
        'Complete a six-week contribution project.',
    ],
    lessons=LESSONS,
    project='a six-week contribution project',
    project_steps=[
        'Plan the project with the contribution plan (PD-M35-L01).',
        'Do it at least four times over about six weeks, logging each session.',
        'Write the six-week review and decide whether to continue.',
        'Write your purpose statement (one sentence) and add it to the Playbook.',
    ],
    project_proof='The plan, the contribution log, the review and your purpose statement.',
    rubric=[
        ('Fit', 'Random choice', 'Fits some values', 'Fits values, skills and time'),
        ('Consistency', 'One session', 'Two or three sessions', 'Four or more sessions logged'),
        ('Impact', 'Unknown', 'Described vaguely', 'Concrete impact observed and recorded'),
        ('Sustainability', 'No boundaries', 'Some limits', 'Clear time limits and a plan to continue or hand over'),
    ],
    short=[
        'Do one small act of kindness a week and log it.',
        'Donate blood once if you are eligible.',
    ],
    flashcards=[
        ('Purpose (Damon)', 'A stable intention meaningful to you and of consequence beyond yourself.'),
        ('Prosocial spending', 'Spending on others is linked to more happiness than spending on yourself.'),
        ('Volunteering evidence', 'Strong observational links; weaker, mixed trial evidence.'),
        ('What makes giving feel good', 'Choice, connection, seeing the impact.'),
        ('Avoiding helper burnout', 'Boundaries, rest, compassion over distress.'),
    ],
    mistakes=[
        ('Thinking you must wait until you have a job or money.', 'Time and skills are valuable now.'),
        ('Taking on too much.', 'One regular commitment is enough.'),
        ('Ignoring what the people you help actually need.', 'Ask them; listen first.'),
    ],
    tools=[
        'The contribution project plan and contribution log (PD-M35-L01).',
    ],
    playbook=[
        'My purpose in one sentence: ______.',
        'My contribution: ______, ___ hours a week, with ______; I review it every six weeks.',
    ],
)
