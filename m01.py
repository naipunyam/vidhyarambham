from common import lesson, module, link, xref, table, Q

L1 = lesson(
    1, 1,
    outcome='You can explain fast and slow thinking, spot when you are answering on autopilot, and use a three-question pause before decisions that matter.',
    split='15 minutes reading, 30 minutes of tasks over three days',
    principle='Most of what you think and do runs on a fast, automatic system; a slower, effortful system can check it, but it is lazy and switches on only when you make it.',
    science=f"""
Psychologists have long noticed that some thinking happens by itself (you read a shop sign without trying, you know a friend is upset from one look) and some takes effort (multiplying 17 by 24, filling in a PSC application without mistakes). Daniel Kahneman made this popular in his 2011 book *Thinking, Fast and Slow*, using the labels **System 1** and **System 2** from earlier researchers.

- **System 1** is fast, automatic, effortless and always on. It recognises faces, reads emotions, completes "bread and…", and jumps to answers. It is usually right, which is why we trust it.
- **System 2** is slow, effortful and limited. It does calculations, follows rules, compares options and checks System 1's answers. It tires quickly and is easily disturbed (try multiplying in your head while crossing a busy road).

The classic demonstration is a puzzle you met in the baseline quiz: *a pen and a notebook cost Rs 110 together; the notebook costs Rs 100 more than the pen; how much is the pen?* "Rs 10" pops up instantly. That is System 1. If you check (Rs 10 + Rs 110 = Rs 120), you see it is wrong; the pen is Rs 5. Problems like this, from Shane Frederick's Cognitive Reflection Test, show that many educated people give the quick answer, because nothing tells System 2 to wake up. The answer *feels* right.

**Be careful with the metaphor.** System 1 and System 2 are not two places in the brain; they are a handy way of describing two modes of thinking that blend into each other. And not everything in Kahneman's book has held up. His chapter on **priming** (the claim that, for example, reading words about old age makes people walk more slowly) relied on small studies that later failed to replicate. Kahneman himself wrote, "I placed too much faith in underpowered studies." The core idea, that quick intuitive answers often go unchecked, is solid; some of the colourful examples are not. You will learn why that happens in PD-M02-L02.

**When is fast thinking good?** In areas where you have had lots of practice with quick, honest feedback: an experienced driver braking, a nurse sensing a patient is getting worse, you recognising your mother's voice on the phone. It is unreliable where feedback is slow or noisy: predicting exam results, judging a stranger's honesty, choosing investments, or guessing how long a task will take.
""",
    evidence=[
        ('Fast intuitive answers often go unchecked (trick problems such as the pen-and-notebook puzzle)', 'strong', 'Replicated many times in many countries; many people give the intuitive wrong answer.'),
        ('"Two systems" as a model of the mind', 'moderate', 'Useful description; psychologists debate whether there are really two separate systems or a continuum.'),
        ('Behavioural priming (e.g. old-age words making people walk slowly)', 'failed', 'Famous examples failed to replicate; Kahneman admitted relying on underpowered studies.'),
        ('Expert intuition is reliable when practice and feedback are good', 'moderate', 'Supported in fields such as chess and firefighting; poor in fields with slow or noisy feedback.'),
    ],
    example=f"""
Ashiq, from Kuttiady, gets a WhatsApp message from a cousin: "Kerala PSC has announced a new exam pattern from next month: forward to all aspirants!" It has a logo and urgent red text. His fast system reacts first: worry, then the urge to forward it to his study group. Last year he did exactly that and later found the message was false.

This time he uses the pause. *What would I need to believe this?* An official notice. *Where would that be?* On the Kerala PSC website. *What is the cost of waiting ten minutes?* Nothing. He checks, finds no such notice, and posts in the group: "Couldn't find this on the PSC site; let's wait for the official notification." Two people thank him. The whole check took four minutes; the old habit had cost him embarrassment and an hour of anxious messages.

The same pattern shows up in ordinary moments: agreeing to a cousin's "small loan" on the spot, buying a phone because the first price you saw made the second look cheap, or snapping back at your father before hearing his full sentence. None of these needs deep thought. Each one needs a short pause in which System 2 gets a chance to look.
""",
    apply=f"""
**On yourself: build a "slow down" trigger.** You cannot run System 2 all day; it would exhaust you. Instead, decide in advance which situations deserve a check:

1. **Money:** any payment, loan, purchase over ₹500 or "offer" with a deadline.
2. **Forwards and news:** anything that makes you angry, scared or excited and asks you to share it.
3. **People judgements:** "he is lazy", "she doesn't like me", "they are cheating".
4. **Plans:** any estimate of time ("I'll finish this topic by Friday").

In those four situations, ask the **three-question pause**: *What exactly is the claim or choice? What would I need to see to believe it? What does waiting a little cost me?* If waiting costs little, wait and check.

**With others: make it easy for their System 2.** When you ask someone for something important, give them time and the key facts in writing; do not ambush them. People who are rushed decide with System 1, and they often regret it (and resent you). Part D builds on this: honest influence gives people room to think; manipulation takes it away (Module 32).
""",
    resources=[
        ('os-7-3', 'Read the section on heuristics and biases ("Pitfalls to Problem Solving" and the table of biases)', '15 minutes'),
        ('wp-tfas', 'Read the summary of the two systems and the "Replication crisis" criticism section', '10 minutes'),
        ('crashcourse', 'Watch episode #24 "Brains vs. Bias" (search the episode list on the page)', '10 minutes'),
    ],
    steps=[
        'Write your four "slow down" situations (money, forwards, people judgements, plans) on a card or as the first note in your Playbook notebook, adding one situation of your own.',
        'For three days, every time one of those situations comes up, do the three-question pause and write one line: what happened, what your first impulse was, and what you did after the pause.',
        'Count how many times your first impulse was right and how many times the pause changed your action.',
        'Tell one person the pen-and-notebook puzzle. Notice whether they give the fast answer, and explain why it happens without making them feel foolish.',
    ],
    proof='A note with at least five pause entries over three days (situation, first impulse, action after the pause) and your count of impulses that changed.',
    templates=[('The three-question pause card', """THREE-QUESTION PAUSE (use for money, forwards, people judgements, plans)
1. What exactly is the claim or the choice?
   ______________________________________________
2. What would I need to see to believe it / choose it?
   ______________________________________________
3. What does waiting (10 minutes, a day, a week) cost me?
   ______________________________________________
If waiting costs little: WAIT and CHECK.
Log: Date | Situation | First impulse | After the pause | Impulse right? (Y/N)""", '')],
    mistakes=[
        ('Treating System 1 as "bad".', 'Fast thinking runs most of life well. The goal is to catch it in a few high-stakes situations, not to distrust every instinct.'),
        ('Thinking you are immune once you know.', 'Knowing about the pen-and-notebook trap does not protect you from the next one in a new form. Rely on triggers and checklists, not on feeling clever.'),
        ('Quoting priming studies as facts.', 'Many popular "subtle cue changes behaviour" findings failed to replicate. Say "a famous study claimed…, but it did not hold up".'),
        ('Using "System 2" as an excuse to overthink small choices.', 'Which tea to order does not need a pause. Save the pause for choices that are costly or hard to undo.'),
    ],
    quiz=[
        Q('Which task is mainly System 1?', 'Recognising that a friend is angry from their face', 'Calculating 17 × 24 in your head', 'Comparing two loan offers line by line', 'Filling in an OMR sheet carefully', why='Reading facial emotion is fast and automatic: System 1. The others need effortful attention.'),
        Q('Why do many people answer "Rs 10" to the pen-and-notebook puzzle?', 'The quick answer feels right, so they never check it', 'They are bad at arithmetic', 'The puzzle has no correct answer', 'They are tired of quizzes', why='The problem is easy to solve once checked; the trap is that nothing prompts the check.'),
        Q('What happened to the behavioural priming studies in Thinking, Fast and Slow?', 'Many failed to replicate, and Kahneman said he had trusted underpowered studies', 'They were all confirmed by large studies', 'They were never published', 'They were proved to be fraud by Kahneman', why='They were weak (small samples) rather than fraudulent, and later replications failed.'),
        Q('When is gut intuition most trustworthy?', 'In areas where you have had lots of practice with quick, honest feedback', 'When you feel very sure', 'When the decision is about strangers', 'When there is no time to think', why='Intuition is learned pattern-matching; it is good only where the patterns were learned with feedback.'),
    ],
    study='read the lesson and the OpenStax section on heuristics',
    action='use the three-question pause for three days and log at least five cases',
)

L2 = lesson(
    1, 2,
    outcome='You can name the main mental shortcuts (representativeness, availability, anchoring, affect), explain how emotion and reason work together, and catch a shortcut misleading you.',
    split='15 minutes reading, 30 minutes of tasks',
    principle='Heuristics are mental shortcuts that save effort and usually work, but in predictable situations they lead to errors; emotion is not the enemy of reason but its guide, and it can also mislead.',
    science=f"""
In the 1970s, Amos Tversky and Daniel Kahneman described three shortcuts people use when judging likelihoods. Their work is among the most replicated in psychology.

- **Representativeness:** judging how likely something is by how much it *looks like* a typical case. In the baseline quiz, "Ravi is quiet and loves books: farmer or librarian?" The description fits a librarian, but there are far more people in farming than librarians, so a random quiet book-lover is more likely to farm. Ignoring how common things are (the **base rate**) is the classic error. A related trap is the **conjunction fallacy**: in Tversky and Kahneman's "Linda problem", most people rated "Linda is a bank teller and active in the feminist movement" as more likely than "Linda is a bank teller", which is logically impossible. A story with more details feels more probable while being less so.
- **Availability:** judging how common something is by how easily examples come to mind. Dramatic, recent or personal events (a plane crash, a friend's hacked phone) feel more frequent than they are.
- **Anchoring:** the first number you see pulls your estimate towards it, even when it is irrelevant. In the original study, a spinning wheel's random number changed people's estimates of African countries in the UN. Anchoring is one of the findings that replicated well in the large Many Labs project (PD-M02-L02).

The **gambler's fallacy** (after five heads, tails feels "due") is a cousin: we expect short runs to look like the long-run average.

**Emotion and reason.** The old picture of cold reason fighting hot emotion is wrong. Emotions are fast evaluations: fear says "danger", disgust says "avoid", interest says "explore". Paul Slovic called the use of feelings to judge risks and benefits the **affect heuristic**: if you like something (a new phone, a friendly salesman), you judge its risks as low and its benefits as high, and the reverse. The neurologist Antonio Damasio described patients with damage to emotion-related brain areas who could reason about choices but struggled to make sensible decisions in daily life; his "somatic marker" explanation is debated, but the broad point, that feelings help us choose, is widely accepted (OpenStax 10.4 covers theories of emotion).

So the aim is not to remove emotion. It is to **notice which emotion is driving a judgement** and ask whether it fits the facts. Fear before a job interview fits; fear of a forwarded message designed to scare you does not.
""",
    evidence=[
        ('Anchoring on irrelevant numbers', 'strong', 'Replicated in large multi-lab projects; the size varies with how much you already know.'),
        ('Base-rate neglect and the conjunction fallacy', 'strong', 'Replicated widely; people do better when problems are given as counts ("10 out of 100") instead of percentages.'),
        ('Availability heuristic', 'moderate', 'Well supported in lab studies and in risk perception; effects vary by task.'),
        ('Affect heuristic: liking something lowers its perceived risk', 'moderate', 'Supported by many studies on risk perception.'),
        ('Emotion is the opposite of good reasoning', 'failed', 'Evidence from neuroscience and psychology shows emotions are part of good decision-making.'),
    ],
    example=f"""
Sreeja, from Nadapuram, is deciding whether to join a ₹12,000 PSC coaching batch. The coaching centre's poster shows ten smiling toppers. That is **availability** and **representativeness** at work: the toppers come to mind easily and "look like" success. What she does not see is the base rate: how many students joined and how many got a rank list place? When she asks, the centre will not say.

At the counter, the manager says the course "normally costs ₹25,000", so ₹12,000 feels like a bargain (**anchoring**). He is warm and funny, so the course *feels* safe (**affect**). Sreeja notices her excitement, uses the three-question pause from PD-M01-L01, and asks two former students from her village. Both say the classes were good but the material was the same as the free SCERT textbooks. She joins a cheaper weekend test series instead, and keeps studying from free material.
""",
    apply=f"""
**Turn each shortcut into a question you ask before an important judgement:**

| Shortcut | The question that checks it |
| --- | --- |
| Representativeness | "How common is this in general, before I look at the details?" |
| Conjunction | "Does each extra detail make the story more convincing but less likely?" |
| Availability | "Am I judging by vivid examples, or by real numbers over time?" |
| Anchoring | "Where did the first number come from, and what would I guess without it?" |
| Affect | "Which emotion am I feeling, and does it fit the facts?" |
| Gambler's fallacy | "Are these events really connected, or independent?" |

**With others:** when you present information, give numbers as counts ("3 out of 10 students cleared it") rather than percentages; people understand them better. And do not exploit anchors or emotions to push someone into a choice; Module 28 shows how to persuade with truth instead.
""",
    resources=[
        ('os-7-3', 'Re-read the table of biases and heuristics (anchoring, confirmation, hindsight, representative, availability)', '10 minutes'),
        ('os-10', 'Read 10.4 Emotion: the theories of emotion section', '20 minutes'),
        ('decisionlab', 'Look up anchoring and the availability heuristic in the bias index; read one entry fully', '10 minutes'),
    ],
    steps=[
        'Find three real examples this week, one each of anchoring (a price, a "was" price, a salary figure), availability (a news story or WhatsApp forward), and representativeness (a judgement about a person from how they look or talk). They can be your own judgements or someone else\'s.',
        'For each, write the shortcut, the checking question from the table, and what the answer to that question showed.',
        'Once this week, before a purchase over ₹500, write down your own price estimate before looking at any price tag or website. Then compare it with the first price you see.',
        'Notice one strong emotion during the week and write: the emotion, what it was telling you, and whether it fitted the facts.',
    ],
    proof='A note with three shortcut examples (each with its checking question and answer), your pre-purchase estimate versus the first price seen, and one emotion check.',
    templates=[('Shortcut spotting note', """SHORTCUT SPOTTING
Date | Situation | Shortcut (representativeness / availability / anchoring / affect / gambler's) | Checking question | What the check showed
Pre-purchase anchor test: item ______ my estimate Rs ____ first price seen Rs ____ final price paid Rs ____
Emotion check: emotion ______ what it said ______ fits the facts? Y / N / partly""", '')],
    mistakes=[
        ('Calling every mistake a bias.', 'Sometimes a judgement is wrong because you lacked information. A bias is a predictable pattern; name it only when it fits.'),
        ('Thinking shortcuts are stupid.', 'They save effort and are usually good enough. They fail in predictable conditions: unfamiliar problems, rare events, emotional pressure and numbers chosen by someone else.'),
        ('Using "you are just being emotional" to dismiss people.', 'Emotions carry information. Ask what the feeling is about before deciding whether it fits.'),
    ],
    quiz=[
        Q('"Most quiet, bookish people are librarians, so Ravi is probably a librarian." What is missing from this reasoning?', 'The base rate: how many librarians there are compared with other jobs', 'Ravi\'s age', 'His favourite books', 'Nothing; it is correct', why='Ignoring how common each category is leads to base-rate neglect.'),
        Q('A seller says "MRP Rs 4,999, today Rs 1,999". Which shortcut is the seller using?', 'Anchoring', 'Availability', 'The gambler\'s fallacy', 'Representativeness', why='The high first number anchors your sense of value.'),
        Q('Why do plane crashes feel more common than they are?', 'Vivid, widely reported events come to mind easily (availability)', 'Planes crash every day', 'People are bad at maths', 'Because of anchoring', why='Ease of recall is mistaken for frequency.'),
        Q('Which statement about emotion and reasoning fits the research?', 'Emotions are fast evaluations that help decisions but can mislead when they don\'t fit the facts', 'Good decisions need emotions switched off', 'Emotions only matter in relationships', 'Reason and emotion use the same brain cells', why='Emotion guides choice; the skill is checking whether it fits the situation.'),
    ],
    study='read the lesson, the OpenStax emotion theories section and one Decision Lab entry',
    action='find and check three real shortcut examples, do one pre-purchase anchor test and one emotion check',
)

LESSONS = [L1, L2]

MODULE = module(
    1,
    overview=f"""
How your mind actually makes judgements: the fast automatic system and the slow checking one, the main mental shortcuts, and how emotion and reason work together. You build a "think slower" checklist for the moments that matter.

Everything in this course rests on one idea: your mind is not a calm calculator, it is a fast pattern-matcher with a slow, lazy checker. Once you see that, most of the later modules make sense: biases (Module 3), habits (Module 8), emotions (Module 10), first impressions (Module 24) and manipulation (Module 32) all exploit or work with the fast system.

This module is deliberately short and practical. You will not memorise theories; you will catch your own mind taking shortcuts, in real situations, for a week. If you have done the Learning Capabilities course, its {xref('lrn', 'lrn-m16', 'thinking skills module')} adds reasoning practice for PSC; here the focus is on everyday judgement.
""",
    outcomes=[
        'Describe System 1 and System 2, and say where intuition can and cannot be trusted.',
        'Name representativeness, the conjunction fallacy, availability, anchoring, the affect heuristic and the gambler\'s fallacy, with an example of each.',
        'Use the three-question pause in your four "slow down" situations.',
        'Explain honestly which famous findings in this area held up and which did not (priming).',
    ],
    lessons=LESSONS,
    project='a "think slower" checklist tested for a week',
    project_steps=[
        'Combine the three-question pause card and the shortcut-checking questions into one checklist of no more than 10 lines that fits on a phone screen or a card.',
        'Use it for seven days. Keep the pause log from PD-M01-L01 going.',
        'At the end, write five lines: how many pauses you did, how many changed your action, which shortcut caught you most often, which situation you will add or remove, and one line for your Playbook.',
    ],
    project_proof='Your checklist, the seven-day pause log and the five-line review.',
    rubric=[
        ('Understanding', 'Cannot explain System 1 and 2 without notes', 'Explains them, but mixes up the shortcuts', 'Explains both systems and four shortcuts with own examples'),
        ('Practice', 'Fewer than five logged pauses', 'Five to nine pauses, mostly the same kind of situation', 'Ten or more pauses across at least three kinds of situation'),
        ('Honesty about evidence', 'Repeats priming claims as fact', 'Knows some findings failed but not which', 'Can say which findings are strong and which failed'),
        ('Usefulness', 'Checklist not used', 'Used sometimes', 'Used daily and edited after the week'),
    ],
    short=[
        'Read PD-M01-L01 only and do the three-question pause for three days.',
        'Put the six shortcut-checking questions on your phone lock screen or a card in your wallet.',
    ],
    flashcards=[
        ('System 1', 'Fast, automatic, effortless thinking: reading faces, gut reactions, quick answers.'),
        ('System 2', 'Slow, effortful, limited thinking that can check System 1, but only when prompted.'),
        ('Pen and notebook cost Rs 110; notebook is Rs 100 more. Pen?', 'Rs 5. The fast answer, Rs 10, fails the check.'),
        ('Representativeness heuristic', 'Judging likelihood by resemblance to a typical case, ignoring base rates.'),
        ('Availability heuristic', 'Judging frequency by how easily examples come to mind.'),
        ('Anchoring', 'The first number seen pulls later estimates towards it. Replicates strongly.'),
        ('Affect heuristic', 'Liking something makes its risks seem low and benefits high.'),
        ('Behavioural priming status', 'Famous examples failed to replicate; Kahneman admitted relying on underpowered studies.'),
        ('When is intuition trustworthy?', 'When it was learned with lots of practice and quick, honest feedback.'),
    ],
    mistakes=[
        ('Trying to think slowly about everything.', 'You will burn out. Pick a few trigger situations and pause only there.'),
        ('Learning the names and stopping.', 'Naming a bias does little. The pause, the checklist and the log change behaviour.'),
        ('Using these ideas to win arguments.', '"That\'s just your availability bias" makes people defensive. Use the questions on yourself first, and ask them gently with others.'),
    ],
    tools=[
        'The three-question pause card (PD-M01-L01).',
        'The shortcut-spotting note and pre-purchase anchor test (PD-M01-L02).',
    ],
    playbook=[
        'My "slow down" situations: money, forwards, people judgements, plans, and ______.',
        'Before those decisions I ask: What exactly is the claim? What would I need to see? What does waiting cost?',
    ],
)
