from common import lesson, module, link, xref, table, Q

L1 = lesson(
    2, 1,
    outcome='You can tell an experiment from a correlation, judge whether a sample is big and fair enough, and explain regression to the mean.',
    split='20 minutes reading, 25 minutes of tasks',
    principle='Only a fair comparison, ideally with people assigned at random, can show that one thing causes another; a pattern in survey data can come from many other causes.',
    science=f"""
Psychology uses a few kinds of study. Knowing which one you are looking at tells you how much to trust a headline. OpenStax Psychology 2e chapter 2 covers this well; here is the short version.

**1. Case studies and stories.** One person or one event, studied in depth. Rich, but you cannot generalise: the one uncle who smoked and lived to 95 tells you nothing about smoking.

**2. Surveys and correlational studies.** Researchers measure two things in many people and see whether they go together. A **correlation** runs from -1 (perfectly opposite) through 0 (no relation) to +1 (perfectly together). Correlations are useful, but three things can create them without one causing the other:
- **A third factor:** people who visit tea shops daily have more friends. Maybe sociable people both visit tea shops and make friends.
- **Reverse direction:** people who exercise are happier. Exercise may lift mood, but happy people may also exercise more.
- **Chance:** test enough pairs of variables and some will correlate by luck.

**3. Experiments.** Researchers **change one thing** (the independent variable) and measure the effect (the dependent variable), comparing an experimental group with a **control group**. The key ingredient is **random assignment**: a coin toss, not the person, decides who gets what. Randomness spreads all other differences (motivation, money, age) evenly between groups, so a difference in the result can be put down to the change. Good experiments also use **blinding** (participants, and ideally researchers, do not know who got what) to avoid expectation effects such as the **placebo effect**.

**Sample size and sample type.** A study of 20 students can easily find a big "effect" by luck. Larger samples give more stable answers. Ask also *who* was studied: much psychology has used Western university students (researchers call such samples "WEIRD": Western, educated, industrialised, rich, democratic). A finding from 60 American undergraduates may or may not apply in Kuttiady.

**Effect size.** "Significant" in a paper means "unlikely to be pure chance" (usually p < 0.05), not "big" or "important". A study can be statistically significant with a tiny effect. Look for the size: a difference in average scores, a percentage, or a standardised number like *d* (roughly: 0.2 is small, 0.5 medium, 0.8 large).

**Regression to the mean.** Extreme results are usually partly luck, so the next measurement tends to be closer to average whatever you do. A student's best-ever mock is usually followed by a lower one; a cricket team's worst match is usually followed by a better one. Many "treatments" seem to work because people start them when things are at their worst, and things would have improved anyway. That is why experiments need control groups.
""",
    evidence=[
        ('Random assignment is needed to show cause and effect', 'strong', 'A basic principle of research design, accepted across science and medicine.'),
        ('Small samples produce unstable, often exaggerated effects', 'strong', 'Shown repeatedly; one main cause of the replication crisis (PD-M02-L02).'),
        ('Regression to the mean misleads people about what works', 'strong', 'A statistical certainty whenever measurements include luck.'),
        ('Findings from Western student samples apply everywhere', 'mixed', 'Many hold broadly; others (some social and cultural effects) vary between countries.'),
    ],
    example=f"""
A YouTube channel claims: "Students who wake up at 4 am score 30% more in PSC exams!" Joseph sir, a retired teacher in Thottilpalam who now helps local aspirants, asks his group three questions.

*Is it an experiment or a correlation?* The video surveyed toppers. Nobody was randomly told to wake at 4 am, so it is a correlation. *What could cause it besides waking time?* Toppers may be more disciplined in everything, or have fewer household duties, or be full-time aspirants. *Who was in the sample, and how many?* Twelve toppers who agreed to be interviewed: tiny, and only successes (nobody asked the 4 am risers who failed).

He then suggests a fair test the group can do themselves: each person picks a study start time at random (by drawing a chit) for two weeks and logs their study minutes and mock scores. It will not be a perfect experiment, but it will tell them more than the video. You will run a similar personal experiment in PD-M08-L04.
""",
    apply=f"""
**The five-question claim check.** Use it on any psychology or health claim, in a video, a newspaper, a WhatsApp forward or a coaching class:

1. **What kind of study?** Story, survey (correlation) or experiment with random assignment?
2. **How many people, and who?** Dozens or thousands? Students, patients, Indians, Americans?
3. **How big is the effect?** A number, not just "significantly better".
4. **Compared with what?** Was there a control group, and was it fair?
5. **Has anyone else found the same?** One study or many (PD-M02-L02)?

**With others:** ask these questions with curiosity, not scorn. "Interesting! Do you know how many people they studied?" keeps the conversation friendly and makes people think.
""",
    resources=[
        ('os-2', 'Read 2.2 Approaches to Research and 2.3 Analyzing Findings (correlation, causation, experiments)', '35 minutes'),
        ('noba', 'Search for the module "Research Designs" and read the parts on experiments and correlational designs', '20 minutes'),
        ('mit-psych', 'Optional: watch the first lecture session to see how a psychology course frames research', '50 minutes'),
    ],
    steps=[
        'Collect three psychology or health claims from your own life this week: a news item, a video or forward, and something a relative or coaching centre says.',
        'Run the five-question claim check on each. Write the answers you can find and mark "unknown" where the source does not say.',
        'Rate each claim: "trust it", "maybe" or "don\'t trust it yet", and say why in one line.',
        'Find one example of regression to the mean in your life (a score, a cricket match, a "cure" that worked after a bad spell) and explain it in two lines.',
    ],
    proof='A note with three five-question claim checks, a rating for each, and one regression-to-the-mean example.',
    templates=[('Five-question claim check', """CLAIM CHECK          Date ______  Source ______________
Claim (exact words): "_____________________________________________"
1. Kind of study:  story / survey or correlation / experiment (random?) / unknown
2. How many people, and who? ______________________________
3. How big is the effect (a number)? ______________________
4. Compared with what (control group)? ______________________
5. Repeated by others? one study / several / reviews / unknown
Could a third factor or reverse direction explain it? ________________
My rating: trust it / maybe / don't trust it yet. Why: ______________""", '')],
    mistakes=[
        ('Rejecting every correlation.', 'Correlations are real information. They just cannot prove cause on their own. Smoking and cancer were first linked by correlations, then confirmed by many kinds of evidence.'),
        ('Treating "significant" as "large".', 'Ask for the size of the effect. A significant but tiny effect may not be worth changing your life for.'),
        ('Believing a study because it agrees with you.', 'Run the check hardest on claims you like. That is the confirmation-bias trap (PD-M03-L01).'),
        ('Forgetting regression to the mean when judging your own changes.', 'If you start a new habit in your worst week, some improvement would have come anyway. Compare with a baseline.'),
    ],
    quiz=[
        Q('What makes an experiment able to show cause and effect?', 'Random assignment to groups, with one thing changed', 'A very large survey', 'Famous researchers', 'Interviews with successful people', why='Randomisation spreads other differences evenly, so the change explains the result.'),
        Q('A study finds that people who own more books have children with higher marks. What is the best conclusion?', 'Book ownership and marks go together; other factors such as family income or parents\' education may explain both', 'Buying books raises children\'s marks', 'Marks cause book buying', 'The study is useless', why='It is a correlation with obvious possible third factors.'),
        Q('Your best-ever mock score (after months of average scores) is followed by a lower score. What is the most likely explanation?', 'Regression to the mean: the best score included some luck', 'You forgot everything', 'The second test was unfair', 'Mocks are useless', why='Extreme results tend to be followed by ones closer to average.'),
        Q('"Statistically significant" in a study means:', 'The result is unlikely to be due to chance alone', 'The effect is large and important', 'The study is famous', 'The researchers are sure it is true', why='Significance is about chance, not size.'),
    ],
    study='read the lesson and OpenStax 2.2 and 2.3',
    action='run the five-question claim check on three real claims and explain one case of regression to the mean',
)

L2 = lesson(
    2, 2,
    outcome='You can explain the replication crisis and its causes, name famous findings that failed, and use a pop-psychology red-flag list.',
    split='20 minutes reading, 25 minutes of tasks',
    principle='A single exciting study is a hypothesis, not a fact; believe findings that have been repeated by independent teams with large samples, and be wary of simple, dramatic claims.',
    science=f"""
In 2015 the **Open Science Collaboration**, a team of 270 researchers, repeated 100 studies published in three top psychology journals. Of 97 original studies with significant results, only **36%** gave a significant result again, and the average effect was about **half** the original size. Later, the **Many Labs** projects tested famous effects across dozens of labs at once; in one, about half of 28 findings failed to replicate. This is the **replication crisis**. It hit social psychology hardest but also affected medicine, economics and other fields.

**Why did it happen?** Not mainly fraud (though there were some fraud cases). The usual causes were ordinary:
- **Small samples:** many studies had too few people to detect real effects reliably, so the ones that "worked" were often lucky flukes.
- **Publication bias:** journals published exciting positive results; failed studies stayed in drawers.
- **Flexible analysis ("p-hacking"):** trying several ways of analysing data and reporting the one that crosses p < 0.05. With enough flexibility, false positives become very likely.
- **Surprising, media-friendly claims** got attention and citations, so there was little reward for checking them.

**What psychology did about it:** larger samples, **pre-registration** (writing down the hypothesis and analysis plan before collecting data), sharing data openly, and multi-lab replications. Findings that survive these tests are much more trustworthy. That is good news: psychology corrected itself, and you now know which findings are solid.

**Famous findings that failed or shrank** (you will meet each one in its own lesson):
- **Power posing:** standing in a "power pose" for two minutes was claimed to raise testosterone, lower cortisol and increase risk-taking (2010, 42 people). A larger replication in 2015 found no hormonal or behavioural effects; the original first author later said she does not believe the effects are real. A small effect on *feeling* powerful may exist (PD-M13-L01).
- **Ego depletion:** the idea that willpower is a fuel tank that empties with use. Pre-registered replications across 23 labs (2016, about 2,100 people) and 36 labs (2021, about 3,500 people) found effects near zero (PD-M08-L01).
- **Behavioural priming:** subtle word cues changing walking speed and similar effects (PD-M01-L01).
- **The marshmallow test as destiny:** a larger 2018 study found the link between a child's waiting time and later success about half as strong as claimed, and smaller still after accounting for family background (PD-M08-L01).
- **Learning styles:** teaching to "visual" or "auditory" learners. Reviews found no good evidence that matching teaching to a style improves learning ({link('pashler', 'Pashler et al., 2008')}).
- **"21 days to form a habit":** not from research. In the best-known study, habits took a median of about 66 days to become automatic, ranging from 18 to 254 days ({link('lally', 'Lally')}).

**Telling science from pop psychology.** Pop psychology often takes a small, early finding and sells it as a life-changing rule. Real findings tend to be modest, conditional ("works for some people, in some situations") and boring to describe.
""",
    evidence=[
        ('Many published psychology findings fail to replicate', 'strong', 'Shown by large, coordinated projects (Open Science Collaboration 2015, Many Labs).'),
        ('Small samples, publication bias and flexible analysis cause false positives', 'strong', 'Well documented in statistics and in replication data.'),
        ('Power posing changes hormones', 'failed', 'Not supported by larger replications; the original first author withdrew her support.'),
        ('Strong ego depletion', 'failed', 'Large pre-registered multi-lab replications found effects near zero.'),
        ('Learning styles matching', 'failed', 'No good evidence that matching teaching to a style helps.'),
        ('Findings that replicated in multi-lab projects (e.g. anchoring)', 'strong', 'Some classic effects held up well, and you can rely on them more.'),
    ],
    example=f"""
Anu, from Kakkattil, follows an Instagram "psychology facts" page. One post says: "Psychology says people who touch their nose while talking are lying." Another: "Hold a pen in your teeth to force a smile and you'll feel happier: proven by science." A third: "Your birth order decides your personality."

She runs the red-flag list. The nose-touching claim has no study named at all and promises mind-reading (two flags); research on lie detection from body language shows people are only slightly better than chance. The pen-in-teeth "facial feedback" study is real but its famous version failed a 17-lab replication in 2016; later work suggests a small effect in some conditions, so "proven" is wrong. Birth-order effects on personality in large studies are very small or absent. She unfollows the page and follows Greater Good and the Noba Project instead.
""",
    apply=f"""
**Pop-psychology red flags.** Be sceptical when a claim:

1. Promises a big change from a tiny trick ("one pose", "one word", "one hack").
2. Names no study, or one small old study, and no replications.
3. Says "science proves" or "psychology says" (real scientists rarely talk like that).
4. Claims to read minds: lie detection from gestures, personality from handwriting or birth order.
5. Is sold with a course, supplement or "secret" attached.
6. Sounds too neat: always, never, everyone.

**Trust signals:** several independent studies; large samples; pre-registration; a review or meta-analysis (a study of studies); a careful source that admits limits (OpenStax, Noba, university sites, Wikipedia's articles on replication, which cite their sources).

**With others:** when someone shares a dramatic "psychology fact", try "I read that one was tested again with bigger groups. Shall we look it up?" You are teaching them a skill, not winning a point.
""",
    resources=[
        ('wp-replication', 'Read the introduction and the sections on psychology and on causes', '20 minutes'),
        ('wp-power', 'Read the replication section: a case study of how a famous finding fell', '10 minutes'),
        ('os-2', 'Read 2.4 Ethics (how research with people is supposed to be done)', '15 minutes'),
    ],
    steps=[
        'Find five "psychology facts" on social media, YouTube or in forwards.',
        'Score each against the six red flags. Write the number of flags.',
        'For the two with the fewest flags, search for the original study and any replication. Write what you found in two lines each.',
        'Write one "pop-psychology to science" translation: rewrite one of the claims in honest words (for example, "One small study in 2010 found…, but larger studies did not").',
    ],
    proof='A table of five claims with red-flag counts, two short search notes, and one honest rewrite.',
    templates=[('Pop-psychology red-flag scorecard', """RED-FLAG SCORECARD (1 point per flag)
Claim | Source | Tiny trick, big change? | No study / no replication? | "Science proves"? | Mind-reading? | Selling something? | Always/never/everyone? | Total
Honest rewrite of one claim:
"One/several studies (year, how many people) found ______ ; later studies ______ ;
so the fair conclusion is ______." """, '')],
    mistakes=[
        ('Concluding that psychology is useless.', 'The crisis showed which findings are weak. Many are strong (anchoring, the benefits of exercise for mood, CBT for anxiety and depression, implementation intentions). The course rates each one.'),
        ('Trusting a finding because a famous person said it.', 'Even Nobel winners relied on weak studies. Ask about replications, not reputations.'),
        ('Throwing away a useful practice because one claim failed.', 'Power posing may not change hormones, but standing tall before a talk does no harm. Separate "is this proven?" from "is this worth trying, cheaply and safely?"'),
    ],
    quiz=[
        Q('In the 2015 Open Science Collaboration project, about what share of significant findings gave significant results again?', 'About 36%', 'About 90%', 'About 5%', 'All of them', why='36% of 97 significant originals replicated, with effects about half as large.'),
        Q('Which was NOT a main cause of the replication crisis?', 'Most psychologists inventing data', 'Small samples', 'Journals preferring positive results', 'Flexible analysis (p-hacking)', why='Fraud happened but was rare; the main causes were ordinary research practices.'),
        Q('What happened to power posing when it was tested with larger samples?', 'No effect on hormones or behaviour; at most a small effect on feeling powerful', 'It was confirmed', 'It was found to lower confidence', 'It was never retested', why='Ranehill et al. (2015) and later work did not find the hormonal or behavioural effects.'),
        Q('What is pre-registration?', 'Writing down the hypothesis and analysis plan before collecting data', 'Registering for a psychology course', 'Paying to publish a paper', 'Getting ethics approval after a study', why='It stops researchers from choosing the analysis after seeing the data.'),
        Q('How long did habits take to become automatic in the best-known habit study?', 'A median of about 66 days, ranging from 18 to 254', 'Exactly 21 days', 'One week', 'One year for everyone', why='The "21 days" claim is not from research.'),
    ],
    study='read the lesson and the Wikipedia replication crisis article',
    action='score five real "psychology facts" with the red-flag list, check two, and write one honest rewrite',
)

LESSONS = [L1, L2]

MODULE = module(
    2,
    overview=f"""
How to read psychology research like a sceptical scientist: experiments versus correlations, samples and effect sizes, the replication crisis, and how to tell science from pop psychology. You build a claim-checker card you will use for the rest of the course and your life.

Personal development is full of confident claims: "21 days to a habit", "power poses build confidence", "your personality type decides your career". Some are well supported; many are not. This module gives you the tools to tell the difference yourself, so you never have to take this course (or any course) on trust.

Every lesson in this course rates its claims as strong, moderate, mixed or weak, failed, or a practical tool. After this module you will understand what those ratings mean and how they were decided.
""",
    outcomes=[
        'Tell an experiment from a correlation and name three reasons a correlation can mislead.',
        'Judge sample size and effect size, and explain regression to the mean.',
        'Explain the replication crisis, its causes and the reforms that followed.',
        'Name at least five famous findings that failed or shrank.',
        'Use a five-question claim check and a six-point red-flag list.',
    ],
    lessons=LESSONS,
    project='a claim-checker card and a ten-claim audit',
    project_steps=[
        'Combine the five-question claim check and the six red flags into one card or phone note (no more than 12 lines).',
        'Audit ten claims you meet in two weeks: at least three from social media, two from news, two from people you know and one from this course.',
        'For each, write the verdict (trust, maybe, not yet) and one line of reasoning.',
        'Pick the one claim you most wanted to be true and write two lines on whether that made you check it less carefully.',
    ],
    project_proof='Your claim-checker card and a ten-claim audit table with verdicts.',
    rubric=[
        ('Study types', 'Confuses correlations and experiments', 'Knows the difference but misses third factors', 'Spots study type and alternative explanations every time'),
        ('Replication knowledge', 'Cannot name failed findings', 'Names two or three', 'Names five and explains why they failed'),
        ('Audit', 'Fewer than five claims checked', 'Five to nine claims checked', 'Ten claims checked, from varied sources'),
        ('Fairness', 'Checks only claims you dislike', 'Checks some favourite claims', 'Checks favourite claims as hard as others'),
    ],
    short=[
        'Learn the five-question claim check and use it on two claims.',
        'Memorise three failed findings: power posing (hormones), ego depletion, learning styles.',
    ],
    flashcards=[
        ('Correlation', 'Two things go together; does not by itself show that one causes the other.'),
        ('Three reasons a correlation can mislead', 'A third factor, reverse direction, chance.'),
        ('Random assignment', 'Chance decides who gets the treatment, so other differences spread evenly.'),
        ('Regression to the mean', 'Extreme results tend to be followed by more average ones, because extremes include luck.'),
        ('Open Science Collaboration 2015', '100 studies repeated; 36% of significant ones replicated; effects about half the size.'),
        ('p-hacking', 'Trying analyses until one gives p < 0.05; inflates false positives.'),
        ('Pre-registration', 'Recording hypothesis and analysis plan before collecting data.'),
        ('Five failed or shrunken findings', 'Power posing (hormones), ego depletion, behavioural priming, learning styles, marshmallow test as destiny.'),
    ],
    mistakes=[
        ('Becoming cynical about all research.', 'The goal is calibrated trust: more for replicated findings, less for single small studies.'),
        ('Judging claims by how they make you feel.', 'Exciting, hopeful claims deserve the most checking.'),
        ('Never acting until something is "proven".', 'For cheap, safe practices (a gratitude note, a walk), trying them and tracking your own data is reasonable.'),
    ],
    tools=[
        'The five-question claim check (PD-M02-L01).',
        'The pop-psychology red-flag scorecard (PD-M02-L02).',
    ],
    playbook=[
        'One study is a hypothesis. I trust findings that independent teams have repeated with large samples.',
        'Before I believe or share a claim: study type, sample, effect size, comparison, replication.',
    ],
)
