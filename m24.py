from common import lesson, module, link, xref, table, fence, Q
import tools

L1 = lesson(
    24, 1,
    outcome='You can explain how first impressions form, the warmth and competence dimensions, and the halo effect, and use them honestly to make a better first impression and to judge others more fairly.',
    split='20 minutes reading, 25 minutes of tasks',
    principle='We judge people quickly on two main dimensions, warmth (are they friendly and trustworthy?) and competence (are they capable?), and one good or bad trait colours everything else (the halo effect); first impressions stick, but they are often wrong.',
    science=f"""
**Fast impressions.** In studies by Janine Willis and Alexander Todorov (2006), people's judgements of a face's trustworthiness after a tenth of a second were similar to their judgements with unlimited time. Nalini Ambady and Robert Rosenthal's "thin slices" research found that ratings of teachers from short silent video clips correlated with end-of-term student ratings. These findings show impressions form fast; they do **not** show that impressions are accurate. Face-based judgements of character are often wrong, and confident first impressions resist change, partly through confirmation bias (PD-M03-L01).

**Warmth and competence.** Susan Fiske, Amy Cuddy and Peter Glick's **stereotype content model** proposes that we judge people and groups on two broad dimensions: **warmth** (friendly, sincere, trustworthy: "Do they mean well?") and **competence** (capable, skilled, confident: "Can they act on it?"). Warmth is usually judged first and weighs more. This model has broad support across many countries, though how the dimensions are measured is debated.

**The halo effect.** Psychologist Edward Thorndike noticed in 1920 that army officers rating soldiers gave consistently similar scores across unrelated traits: a soldier rated handsome was also rated intelligent and loyal. Richard Nisbett and Timothy Wilson (1977) showed students a video of a lecturer behaving warmly or coldly; students who saw the warm version rated his appearance, accent and mannerisms as more attractive, and did not realise the warmth had influenced them. Halo effects appear in job interviews, exam marking, elections and online reviews. The reverse, a "horns effect", also happens: one bad trait spreads too.

**Primacy.** Solomon Asch found that the order of traits matters: "intelligent, industrious, impulsive, critical, stubborn, envious" produced a more positive impression than the same list in reverse. Early information shapes how later information is read.

**What this means for you:** you can make a fair, good first impression (warmth first: a smile, a greeting, attention; then competence: preparation, clarity) without pretending. And you can **delay your own judgements** of others.
""",
    evidence=[
        ('First impressions form very fast', 'strong', 'Replicated in many studies.'),
        ('Fast impressions are accurate', 'mixed', 'Some thin-slice judgements predict outcomes; character judgements from faces are often wrong.'),
        ('Warmth and competence as the two main dimensions', 'strong', 'Supported across many countries; measurement debated.'),
        ('Halo effect', 'strong', 'Found across ratings, interviews, marking and reviews.'),
        ('Primacy effect in impressions', 'moderate', 'Classic findings; size depends on the situation.'),
    ],
    example="""
Sreeja attends a free career seminar at a Kozhikode college. In the first minute, she meets two people. One, Rafeeq, smiles, says her name back to her and asks what she is preparing for: **warmth**. Later he explains a tricky point about the Kerala Administrative Service exam clearly: **competence**. She remembers him as "very sharp", although she later realises he only answered one question; the warmth gave him a **halo**.

The other, an older woman, looks stern and doesn't smile. Sreeja judges her as "unfriendly" (**horns effect**) until the woman stays after the seminar to give her a list of free mock-test sources and her phone number. Sreeja writes in her bias journal: "First impression wrong. She was tired, not cold. Wait for a second piece of evidence before judging."

For her own first impressions, Sreeja practises: a greeting with eye contact and a smile, using people's names, one good question about them (warmth), and a 20-second clear answer to "What are you preparing for?" (competence).
""",
    apply=f"""
**Making a good, honest first impression:**
1. **Warmth first:** greet, smile naturally, make eye contact (culturally appropriate), use their name, show interest with one question about them.
2. **Then competence:** be prepared, speak clearly, keep it short, follow through on what you say.
3. **Appearance basics:** clean and appropriate (Module 23).
4. **Be on time:** lateness is an early negative signal.
5. **End warmly:** thank them; a short follow-up message later.

**Judging others fairly:**
1. **Delay:** "That's my first impression; I'll wait for two more pieces of evidence."
2. **Separate traits:** "Is she a good speaker *and* a good teacher, or am I assuming one from the other?"
3. **Use structure** when you have to evaluate people (in hiring, judging a competition): the same questions for everyone, scored separately, before discussing.

**Ethics:** using warmth to fake friendliness for a sale or a favour slides into manipulation (Module 32). Be genuinely interested; it works better anyway.
""",
    resources=[
        ('os-12', 'Read 12.1 What Is Social Psychology? (situational and dispositional explanations) and 12.2 Self-presentation', '25 minutes'),
        ('decisionlab', 'Read the halo effect entry', '5 minutes'),
        ('noba', 'Search for the module "Social Cognition and Attitudes" and read the impressions section', '15 minutes'),
    ],
    steps=[
        'For three days, note your first impression of every new person you meet (at least five), on warmth and competence (1–5 each).',
        'A week later, if you have met them again, re-rate. Note any halo or horns effect.',
        'Practise the five-step first impression with at least two new people and note how the conversation went.',
        'Write a 20-second answer to "What do you do?" that is warm and clear, and say it aloud until it feels natural.',
    ],
    proof='Your first-impression notes (five or more people, with re-ratings where possible), two practice notes and your 20-second answer.',
    templates=[('Field notes on first impressions', """FIRST-IMPRESSION FIELD NOTES
Date | Person (first name or role) | Where | Warmth 1-5 | Competence 1-5 | Based on (look / voice / words / action) | Re-rating later | Halo or horns?
MY 20-SECOND ANSWER: "I'm ______ from ______. I'm preparing for ______ and
I'm especially interested in ______. What about you?"
First-impression checklist: greet, smile, name, one question, clear answer, thank""", '')],
    mistakes=[
        ('Trusting your gut about people\'s character.', 'Fast impressions often mislead. Wait for evidence.'),
        ('Leading with competence and forgetting warmth.', 'People decide first whether you mean well.'),
        ('Faking warmth.', 'People often sense it, and it is manipulation if used to exploit.'),
        ('Letting one trait colour everything.', 'Rate traits separately.'),
    ],
    quiz=[
        Q('What are the two main dimensions of social judgement in the stereotype content model?', 'Warmth and competence', 'Height and weight', 'Wealth and age', 'Intelligence and humour', why='Fiske, Cuddy and Glick\'s model.'),
        Q('What is the halo effect?', 'One positive trait making us rate a person higher on unrelated traits', 'A religious experience', 'Remembering only the last impression', 'Preferring tall people only', why='Thorndike and later Nisbett and Wilson showed this.'),
        Q('What is the best way to judge people fairly in an interview panel?', 'Ask everyone the same questions and score answers separately before discussing', 'Go with your first feeling', 'Choose the most confident person', 'Let the most senior member decide', why='Structure reduces halo and first-impression effects.'),
        Q('Which is usually judged first and weighs more?', 'Warmth', 'Competence', 'Clothing brand', 'Accent', why='People first ask whether others mean well.'),
    ],
    study='read the lesson and OpenStax 12.1 and 12.2',
    action='keep first-impression field notes on five or more people, practise the five-step first impression twice and write your 20-second answer',
)

L2 = lesson(
    24, 2,
    outcome='You can explain the fundamental attribution error, stereotypes and implicit bias (including the limits of the IAT), and use three habits to judge people more fairly.',
    split='20 minutes reading, 30 minutes of tasks',
    principle='We explain other people\'s behaviour by their character and our own by the situation; stereotypes and biases shape our judgements, but noticing them and checking the situation reduces unfairness.',
    science=f"""
**The fundamental attribution error (FAE).** Lee Ross (1977) named the tendency to explain others' behaviour by their **character** ("he's rude") while underestimating the **situation** ("he just got bad news"). In a classic 1967 study by Edward Jones and Victor Harris, people read essays for or against Fidel Castro and were told the writers had been **assigned** their side; they still believed the essays showed the writers' true views. We are kinder to ourselves: when *we* are late it's the traffic; when *they* are late they're careless (the actor-observer difference). Research suggests the error is weaker in some collectivist cultures that pay more attention to context, but it still appears.

**Stereotypes.** Stereotypes are generalisations about groups: by caste, religion, region, gender, age, class, skin colour, accent or occupation. They are mental shortcuts (Module 1), sometimes containing a grain of truth about averages, but they are often exaggerated or false, and applying them to **individuals** is unfair and frequently wrong. They become prejudice (a negative attitude) and discrimination (unfair treatment) when acted on. OpenStax 12.5 covers prejudice and discrimination.

**Implicit bias and the IAT.** The **Implicit Association Test** (from Anthony Greenwald, Mahzarin Banaji and colleagues; free at {link('implicit', 'Project Implicit')}) measures how quickly people pair concepts (for example, faces of different groups with "good" and "bad" words). Many people show associations they don't consciously endorse. **Be careful with the results:** the IAT's test-retest reliability is modest (your score can change a lot between sessions), and meta-analyses (for example, Frederick Oswald and colleagues, 2013; Patrick Forscher and colleagues, 2019) found that IAT scores predict real discriminatory **behaviour** only weakly, and that changing IAT scores did not reliably change behaviour. The IAT is a useful **learning tool** about how associations work, not a diagnosis of whether you are prejudiced.

**Stereotype threat**, the idea that being reminded of a negative stereotype about your group lowers performance, was influential but has had **mixed replications** (several large studies found small or no effects).

**What helps reduce bias in judgements:** slowing down for important decisions (Module 1), structured evaluations (same criteria for everyone), **contact** with people from other groups as equals in shared goals (Gordon Allport's contact hypothesis has good support from meta-analyses, though effects vary), and **perspective-taking** combined with asking.
""",
    evidence=[
        ('Fundamental attribution error', 'strong', 'Replicated widely; weaker in some cultures.'),
        ('Stereotypes affect judgements of individuals', 'strong', 'Many studies across countries and groups.'),
        ('IAT reveals associations people don\'t endorse', 'moderate', 'Robust at group level; modest reliability for individuals.'),
        ('IAT scores predict discriminatory behaviour', 'mixed', 'Weak prediction in meta-analyses; changing scores didn\'t reliably change behaviour.'),
        ('Stereotype threat lowers performance', 'mixed', 'Influential but with mixed replications.'),
        ('Intergroup contact reduces prejudice', 'moderate', 'Supported by large meta-analyses; conditions matter.'),
    ],
    example="""
A bus conductor on the Kuttiady–Kozhikode route snaps at Ashiq when he gives a ₹500 note for a ₹28 ticket. Ashiq's first thought: "These conductors are always rude" (a **stereotype**, and the **fundamental attribution error**). Then he remembers the lesson and checks the situation: it's 8:30 am, the bus is packed, the conductor has given change to 60 people in 40 minutes and has no small notes left. Ashiq apologises, finds a ₹50 note, and the conductor smiles tiredly.

At home, Ashiq takes an IAT on the Project Implicit site. His result suggests a "moderate automatic preference" for one group over another. He feels defensive, then remembers its limits: modest reliability, weak prediction of behaviour. He uses it as a prompt rather than a verdict: "I'll notice when I make quick assumptions about people from that group, and judge by what they actually do."

In his study group, he suggests that when they rate each other's mock interview answers, they use the same five criteria for everyone and score before discussing.
""",
    apply="""
**Three habits for fairer judgements:**
1. **The situation check:** when someone behaves badly, ask "What situation might make a reasonable person act like this?" before judging their character. Find at least one plausible situational reason.
2. **The individual check:** when you catch a group stereotype ("people from X are…"), ask "What do I know about *this* person from what they have actually done?"
3. **The structure habit:** when you evaluate people (choosing a study partner, rating answers, hiring for a small job), use the same criteria for everyone and score before discussing.

**On yourself:** apply the FAE in reverse sometimes. When you fail, the situation mattered (good for self-compassion), but also ask what *you* could change.

**With others:** challenge stereotypes gently: "I know a few who aren't like that" or "Do you think that's true of everyone?" works better than accusing someone of prejudice. Speak up when a joke or comment targets a group; silence can look like agreement (Module 30 on bystanders).
""",
    resources=[
        ('os-12', 'Read 12.5 Prejudice and Discrimination', '20 minutes'),
        ('implicit', 'Optional: take one IAT for learning purposes and read the site\'s explanation of what the results mean and don\'t mean', '15 minutes'),
        ('decisionlab', 'Read the fundamental attribution error entry', '5 minutes'),
    ],
    steps=[
        'For one week, use the situation check at least five times when someone annoys you. Write their behaviour, your first explanation and at least one situational explanation.',
        'Catch one stereotype in your own thinking and one in media or conversation; apply the individual check to each.',
        'Use the structure habit for one real evaluation (rating study-group answers, choosing between two shops or helpers).',
        'If you take an IAT, write two lines on what it can and cannot tell you.',
    ],
    proof='Five situation checks, two stereotype checks, one structured evaluation, and (optional) two lines on the IAT.',
    templates=[('Fair-judgement log', """FAIR-JUDGEMENT LOG
SITUATION CHECKS
Date | Who | What they did | My first explanation (character) | Situational explanation(s)
STEREOTYPE CHECKS
Date | Stereotype noticed (me / media / conversation) | What I know about this individual
STRUCTURED EVALUATION
What I evaluated: ______ Criteria (same for all): 1 ___ 2 ___ 3 ___
Scores before discussion: ______  Did structure change my view? ______""", '')],
    mistakes=[
        ('Treating an IAT score as proof of prejudice.', 'It measures associations with modest reliability and weakly predicts behaviour.'),
        ('Excusing all bad behaviour as "the situation".', 'Situations explain a lot, not everything. People are still responsible for their choices.'),
        ('Thinking you have no biases.', 'Everyone has associations. The goal is fair actions, not a pure mind.'),
        ('Shaming people for stereotypes.', 'Gentle questions and examples change minds better.'),
    ],
    quiz=[
        Q('What is the fundamental attribution error?', 'Explaining others\' behaviour by their character while underestimating the situation', 'Blaming the weather', 'Always blaming yourself', 'Forgetting names', why='Ross named this tendency in 1977.'),
        Q('What do meta-analyses say about IAT scores and behaviour?', 'They predict discriminatory behaviour only weakly', 'They predict behaviour perfectly', 'They have no link to anything', 'They are a medical diagnosis', why='Oswald (2013) and Forscher (2019) found weak prediction.'),
        Q('Which approach reduces bias in evaluating people?', 'Using the same criteria for everyone and scoring before discussing', 'Trusting first impressions', 'Letting the loudest person decide', 'Judging by appearance', why='Structure reduces halo and stereotype effects.'),
        Q('What is the honest status of stereotype threat research?', 'Influential but with mixed replications', 'Proven in every study', 'Never studied', 'Shown to be fraud', why='Several large studies found small or no effects.'),
    ],
    study='read the lesson and OpenStax 12.5',
    action='do five situation checks, two stereotype checks and one structured evaluation',
)

LESSONS = [L1, L2]

MODULE = module(
    24,
    overview=f"""
How people see each other: fast first impressions, warmth and competence, the halo effect, the fundamental attribution error, stereotypes and implicit bias (with honest limits of the IAT). You keep field notes and practise judging people more fairly, and making a better first impression yourself.

Part D, Win with people (ethically), starts with perception, because every relationship starts with an impression, and most conflicts involve a misjudgement. The aim is twofold: show people the real you clearly (warmth first, then competence), and judge others more fairly than your fast mind wants to.

Everything in Part D follows one ethical rule: influence only for honest, mutually beneficial purposes. Manipulation is covered only so you can recognise and resist it (Module 32).
""",
    outcomes=[
        'Explain fast impressions, warmth and competence, the halo effect and primacy.',
        'Make an honest, good first impression.',
        'Explain the fundamental attribution error, stereotypes, implicit bias and the IAT\'s limits.',
        'Use the situation check, the individual check and structured evaluation.',
    ],
    lessons=LESSONS,
    project='field notes on first impressions and fair judgements',
    project_steps=[
        'Keep first-impression field notes for two weeks (PD-M24-L01), re-rating people you meet again.',
        'Keep the fair-judgement log for the same two weeks (PD-M24-L02).',
        'Write a half-page summary: how often your first impressions changed, your most common halo or horns trigger, and the habit you will keep.',
        'Add your first-impression checklist and situation check to the Playbook.',
    ],
    project_proof='Two weeks of field notes and fair-judgement entries, and your half-page summary.',
    rubric=[
        ('Observation', 'Fewer than five people noted', 'Five to nine', 'Ten or more with re-ratings'),
        ('Fairness habits', 'Not used', 'Used occasionally', 'Situation and individual checks used regularly'),
        ('Honesty about evidence', 'Treats IAT or first impressions as truth', 'Some caveats', 'Explains limits clearly'),
        ('Own impression', 'No practice', 'Practised once', 'Practised and refined the 20-second answer'),
    ],
    short=[
        'Use the situation check once a day for a week.',
        'Practise warmth first with one new person.',
    ],
    flashcards=[
        ('Two dimensions of social judgement', 'Warmth (do they mean well?) and competence (can they act on it?).'),
        ('Which is judged first?', 'Warmth.'),
        ('Halo effect', 'One good trait colours judgement of unrelated traits.'),
        ('Fundamental attribution error', 'Character explanations for others; situation for ourselves.'),
        ('Situation check', '"What situation might make a reasonable person act like this?"'),
        ('IAT limits', 'Modest reliability; weak prediction of behaviour; a learning tool, not a diagnosis.'),
        ('Contact hypothesis', 'Equal-status contact with shared goals reduces prejudice (meta-analyses).'),
    ],
    mistakes=[
        ('Using perception tricks to manipulate.', 'Be genuinely warm and competent; don\'t fake it to exploit.'),
        ('Labelling people as biased.', 'Everyone has associations; focus on fair actions.'),
        ('Never revising first impressions.', 'Write them down and re-rate.'),
    ],
    tools=[
        'First-impression field notes and the 20-second answer (PD-M24-L01).',
        'The fair-judgement log (PD-M24-L02).',
    ],
    playbook=[
        'First impressions: warmth first (greet, smile, name, a question), then competence (prepared, clear, brief).',
        'Before judging someone: situation check, individual check, wait for two more pieces of evidence.',
    ],
)
