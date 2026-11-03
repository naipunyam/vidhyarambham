"""Module 8: Deep understanding."""
from common import lesson, module, link, fence, table
import tools

M = 8

L1 = lesson(
    M, 1,
    outcome='Explain a PSC topic aloud in simple words without notes, record it, find the gaps, and record an improved version: the first of your five Feynman explanations.',
    split='20 minutes reading, 30 minutes resources, 40 minutes action',
    core=f"""
### Self-explanation

**Self-explanation** means explaining to yourself, while you study, why each statement is true or why each step follows. Studying a solved maths problem, you ask: "Why do we divide by 100 here? Why add the rates?" Reading the Constitution, you ask: "Why would the makers put this in Part III and not Part IV?" Dunlosky and colleagues rated self-explanation **moderate utility**: it helps across many topics, although it takes time ({link('dunlosky-aft', 'Dunlosky, 2013')}).

### The Feynman technique

The **Feynman technique** is named after the physicist Richard Feynman, famous for explaining hard ideas in plain words. It turns self-explanation into a routine:

1. **Choose a topic** you have studied.
2. **Explain it simply, aloud, without notes,** as if to a 12-year-old or to someone at home. Record it on your phone.
3. **Listen back and find the gaps:** where you stopped, said "basically" or "something like", used a word you couldn't explain, or said something wrong.
4. **Go back to the source** and fix each gap.
5. **Simplify:** find an analogy or example from Kerala life.
6. **Explain it again** and record a second version. Compare.

Honesty about the evidence: Feynman didn't publish this as a method, and there are no studies of "the Feynman technique" under that name. Its parts are well supported. Explaining from memory is retrieval practice. Self-explanation is rated moderate utility. Research on learning by teaching finds that explaining to others helps learning, most of all when you explain **without notes**, which makes it a retrieval activity ({link('fiorella', 'Fiorella, Learning by Teaching')}).

### Why record it?

While you talk, you can't hear your own gaps. Playback shows them clearly: the long pause before a date, the vague "and then they made some changes". The recording is also your proof, and five of them become this module's project.

### What suits the technique

Use it for things that have reasons and connections: processes, causes and effects, how an institution works, a maths method, a science concept. For pure lists of facts (award winners, article numbers), cards and mnemonics work better (Modules 4 and 11).

### Simple is not careless

A simple explanation still has to be **correct**. Use the right terms, but explain each one the first time you use it. If you can't explain a term, that is a gap to fix, not a word to hide behind.
""",
    example="""
**Ashiq** chose Article 32 and the writs for his first Feynman explanation. He explained it to his imaginary listener, his 12-year-old niece, and recorded 2 minutes 40 seconds.

When he listened back, the gaps were obvious. He said "the court can issue some orders called writs", then named only three of the five. He couldn't say clearly how mandamus differs from prohibition, and he called Article 32 "a fundamental right to go to court" without saying which court.

He went back to his textbook. The five writs are habeas corpus, mandamus, prohibition, certiorari and quo warranto; Article 32 lets you go directly to the Supreme Court when a Fundamental Right is violated, and Article 226 gives High Courts their writ powers. For an analogy he used a school: habeas corpus is like asking "show me the student you are keeping in the staffroom"; mandamus is ordering a teacher to do a duty they are refusing to do.

His second recording was 2 minutes 15 seconds, named all five writs and had no long pauses. He scored v1 at 6 out of 12 and v2 at 11, and made three cards from the gaps.
""",
    evidence=[
        ('Self-explanation', 'moderate', 'Rated moderate utility by Dunlosky and others (2013): helps across topics, though it takes time.'),
        ('Explaining to others without notes', 'moderate', 'Fiorella (2023): explaining helps more than only preparing to teach, especially as a retrieval activity.'),
        ('"The Feynman technique" as a named method', 'limited', 'No direct studies; it packages self-explanation, retrieval and explaining, which are supported.'),
    ],
    resources=[
        ('dunlosky-aft', 'Read the section on self-explanation', '10 minutes'),
        ('fiorella', 'Read the parts on explaining to others and on teaching as retrieval', '25 minutes'),
    ],
    steps=[
        'Choose a PSC topic you have studied that has reasons or steps in it (a Constitution provision, a history cause, a geography process or a maths method).',
        'Without notes, explain it aloud for 2 to 3 minutes to an imaginary 12-year-old and record it (v1).',
        'Listen back and fill in step 2 of the Feynman template: every pause, vague phrase, unexplained term and error.',
        'Fix each gap from your textbook, and find one analogy or example from Kerala life.',
        'Record a second version without notes (v2). Score both versions on the template.',
        'Turn the gaps into 2 or 3 flashcards in AnkiDroid.',
    ],
    proof='Your v1 and v2 recordings, the filled-in Feynman template with both scores, and the new cards. This is Feynman explanation 1 of 5.',
    templates=[
        ('Feynman explanation (core tool)', tools.FEYNMAN, ''),
        ('self-explanation prompts (for worked examples and dense text)', """
For each step or sentence, ask and answer in a few words:
- Why is this step done? Why this operation and not another?
- What does this term mean, in my words?
- How does this connect to the line before it?
- What would change if this number or condition were different?
- Can I say this step without looking?
""", ''),
    ],
    mistakes=[
        ('Glancing at notes while "explaining".', 'Notes turn it into reading aloud. Explain from memory, then check.'),
        ('Explaining a list of facts.', 'Use the technique for reasons and processes; use cards for lists.'),
        ('Skipping the listen-back.', 'The playback is where the gaps show. Listen with the template in hand.'),
        ('Ten-minute recordings.', 'Two or three minutes per topic keeps it focused and easy to review.'),
        ('Hiding behind jargon.', 'If you use a term, explain it. If you can\'t, it is a gap.'),
    ],
    quiz=[
        {'q': 'What is self-explanation?', 'o': ['Explaining to yourself why each statement or step is true while you study', 'Reading your notes aloud', 'Writing a summary at the end of the week', 'Asking a friend for the answer'], 'a': 'A', 'why': 'It is rated moderate utility by Dunlosky and others.'},
        {'q': 'What is the honest evidence position on the Feynman technique?', 'o': ['No studies test it by name, but its parts (self-explanation, retrieval, explaining) are supported', 'It has been proven in hundreds of studies', 'It has been shown not to work', 'Feynman tested it himself'], 'a': 'A', 'why': 'It is a popular package of well-supported principles.'},
        {'q': 'Why record your explanation?', 'o': ['Playback reveals gaps you can\'t hear while talking, and it is your proof', 'Because PSC exams are oral', 'To post it online', 'Recording makes you remember automatically'], 'a': 'A', 'why': 'You can\'t listen critically while you are explaining.'},
        {'q': 'Which topic suits the Feynman technique best?', 'o': ['How Article 32 protects Fundamental Rights through writs', 'The list of Jnanpith winners', 'Kerala\'s 14 district names', 'Telephone codes of districts'], 'a': 'A', 'why': 'It has reasons and connections to explain; lists suit cards and mnemonics.'},
    ],
    study='Dunlosky\'s section on self-explanation and Fiorella on explaining and teaching',
    action='Record, review and improve your first Feynman explanation of a PSC topic',
)

L2 = lesson(
    M, 2,
    outcome='Turn any PSC text into deep questions with question stems, write exam-style statement questions, and ask for help in a way that gets useful answers.',
    split='20 minutes reading, 20 minutes resources, 45 minutes action over two days',
    core=f"""
Understanding grows from questions. Most students ask only "what" questions (what is it, when was it, who did it). Those matter for PSC, but deeper questions build the connections that hold the facts (Module 3) and help with the trickier question types in modern papers.

### Six kinds of question

{table(['Kind', 'Question stems', 'PSC example'], [
    ('Fact', 'What? When? Who? Where?', 'When was the 73rd Amendment passed?'),
    ('Reason', 'Why? What caused...?', 'Why was a constitutional amendment needed for panchayats?'),
    ('Process', 'How does... work? What are the steps?', 'How does a money bill pass Parliament?'),
    ('Comparison', 'How is X different from Y? What do they share?', 'How is a writ of mandamus different from prohibition?'),
    ('Application', 'What is an example of...? How would this apply to...?', 'Which Fundamental Right applies when a child is denied school admission?'),
    ('What if', 'What would happen if...? What would change if...?', 'What would happen if the Rajya Sabha did not return a money bill in 14 days?'),
])}

Write questions of every kind, then **answer them from memory a day later**. Writing questions is useful; answering them is retrieval practice, which is where most of the benefit comes from.

### Think like the examiner

Kerala PSC papers include more than simple recall. Common forms include:

- **Statement questions:** "Consider the following statements. Which is/are correct?"
- **Match the following**
- **Chronological order:** arrange events in the order they happened
- **Odd one out**

Writing your own questions in these forms trains you to notice the details examiners test: the exact year, the difference between similar bodies, the word "not". For example: *"Consider the statements: (1) The 73rd Amendment added Part IX to the Constitution. (2) It deals with municipalities. Which is correct?"* (Only 1: municipalities are in Part IXA, added by the 74th Amendment.)

### Asking for help well

When you are stuck, a good question gets a good answer from a teacher, a study partner or an AI tutor (Module 17). A good help question has three parts:

1. **What I am trying to understand:** "how the writ of certiorari works"
2. **What I already know or tried:** "I know it is issued by a higher court to a lower court"
3. **Exactly where I am stuck:** "I don't see how it differs from prohibition"

"Explain the writs" gets a lecture. The three-part question gets the one explanation you need.
""",
    example="""
**Joseph sir**'s study group took the chapter on Panchayati Raj. Each member wrote twelve questions using at least six different stems, two of each kind, and three statement questions in PSC style.

Vinod's best question was a "what if": "What would happen to local planning if panchayats had no fixed term?" Answering it, the group worked out for themselves why the 73rd Amendment fixed a five-year term and required elections, which made the facts easier to remember. Sreeja's statement question caught the whole group: two of five members wrongly said the 73rd Amendment covered municipalities.

The next day, each member answered their own questions without the book, then swapped sheets. Joseph sir asked everyone to write one three-part help question about what was still unclear. Three members were stuck on the same point, the Eleventh Schedule, and he explained it once for all of them.
""",
    evidence=[
        ('Asking and answering why-questions (elaborative interrogation)', 'moderate', 'Rated moderate utility by Dunlosky and others (2013).'),
        ('Writing your own questions', 'limited', 'Studied less than retrieval; the benefit grows when you also answer them from memory later.'),
        ('Answering your own questions from memory', 'strong', 'This is retrieval practice, rated high utility.'),
    ],
    resources=[
        ('ls-elaboration', 'Use the elaboration bookmark prompts as extra question stems', '10 minutes'),
        ('os-cs-5', 'Read 5.2 Effective Reading Strategies, noting where questions come in', '15 minutes'),
    ],
    steps=[
        'Take one chapter or section of your PSC material.',
        'Write 12 questions on it using at least six different kinds from the table (two of each), and mark each question\'s kind.',
        'Write 3 PSC-style statement questions with their answers and the reason each statement is right or wrong.',
        'The next day, answer all 15 from memory, then check against the source and correct in another colour.',
        'Write two three-part help questions about what is still unclear, and ask one of them to your study partner, teacher or an AI tutor.',
    ],
    proof='Your question sheet with kinds marked, the three statement questions, your next-day answers with corrections, and the help questions with the answer you got.',
    templates=[
        ('question stems card', """
FACT         What...? When...? Who...? Where...?
REASON       Why...? What caused...? Why was it needed?
PROCESS      How does... work? What are the steps of...?
COMPARISON   How is ___ different from ___? What do ___ and ___ share?
APPLICATION  What is an example of...? Which rule applies when...?
WHAT IF      What would happen if...? What would change if...?
Rule: write them today, answer from memory tomorrow, then check.
""", ''),
        ('PSC-style statement question builder', """
Topic: ______________
Consider the following statements:
1. ______________________________________ (true / false: ____________)
2. ______________________________________ (true / false: ____________)
Which of the statements given above is/are correct?
(A) 1 only  (B) 2 only  (C) Both 1 and 2  (D) Neither 1 nor 2
Answer: ___   Why each statement is right or wrong: ______________________
Source: ______________ page ___
""", ''),
        ('three-part help question', """
I am trying to understand: ___________________________________________
What I already know or tried: _________________________________________
Exactly where I am stuck: ____________________________________________
""", ''),
    ],
    mistakes=[
        ('Writing only "what" questions.', 'Use all six kinds; reason and comparison questions build understanding.'),
        ('Writing questions and never answering them.', 'Answer them from memory the next day. That is where the benefit is.'),
        ('Making statement questions you can\'t check.', 'Every statement needs a source, so the answer is certain.'),
        ('Asking vague help questions.', 'Use the three-part form: goal, what you know, where you are stuck.'),
    ],
    quiz=[
        {'q': 'Which is a comparison question?', 'o': ['How is a writ of mandamus different from prohibition?', 'When was the 73rd Amendment passed?', 'Who was the first Speaker of the Lok Sabha?', 'Where is the Supreme Court?'], 'a': 'A', 'why': 'It asks how two similar things differ.'},
        {'q': 'Consider: (1) The 73rd Amendment added Part IX to the Constitution. (2) It deals with municipalities. Which is correct?', 'o': ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 'a': 'A', 'why': 'Municipalities are in Part IXA, added by the 74th Amendment.'},
        {'q': 'Where does most of the benefit of writing your own questions come from?', 'o': ['Answering them from memory later', 'Writing them neatly', 'Sharing them online', 'Copying them into a notebook'], 'a': 'A', 'why': 'Answering from memory is retrieval practice.'},
        {'q': 'Which is the best help question?', 'o': ['"I\'m trying to understand certiorari. I know a higher court issues it to a lower court. I don\'t see how it differs from prohibition."', '"Explain the writs."', '"I don\'t understand anything."', '"Is this important?"'], 'a': 'A', 'why': 'It states the goal, what you know and exactly where you are stuck.'},
    ],
    study='The elaboration bookmark prompts and College Success 5.2',
    action='Write and answer 12 deep questions and 3 statement questions, and ask a three-part help question',
)

L3 = lesson(
    M, 3,
    outcome='Draw concept maps of connected PSC ideas from memory, check and correct them, and use them as retrieval practice rather than decoration.',
    split='15 minutes reading, 15 minutes resources, 45 minutes action plus a 15-minute redraw two days later',
    core=f"""
### What a concept map is

A **concept map** shows ideas (concepts) in boxes, joined by **labelled arrows** that say how they are related. Each box-arrow-box reads as a sentence: "Lok Sabha → elected directly by → the people"; "Vice-President → is the chairman of → Rajya Sabha". The labels are the point: they force you to say exactly how ideas connect.

It differs from a mind map (Module 9), which branches out from one central topic, usually without labelled links.

### What the research found, honestly

In a well-known study, Karpicke and Blunt compared students who studied a science text by making concept maps with the text available against students who practised retrieval (reading, then recalling on paper). Retrieval practice produced much better long-term retention, and students had predicted the opposite ({link('karpicke-blunt', 'Purdue University, 2011')}).

So concept mapping **with the book open** is not the best use of your time. But you don't have to choose. Draw the map **from memory**, then check it against the source. That makes the map a form of retrieval practice, and it adds what retrieval alone doesn't show: whether you understand how the ideas fit together.

### How to draw one from memory

1. **List 10 to 15 key concepts** from the topic, from memory.
2. **Place the most general one at the top** (for example "Parliament") and more specific ones below.
3. **Join them with arrows and write a short label** on each: "consists of", "elected by", "appoints", "can delay", "causes", "is part of".
4. **Add cross-links** between distant parts of the map; these show deep understanding.
5. **Check against the source** and fix wrong or missing links in another colour.
6. **Redraw it from memory** two days later and count the correct links.

### Topics that suit concept maps

Topics with many connected parts: the structure of Parliament, the Indian monsoon, the Kerala renaissance (leaders, organisations, movements and places), inflation and the RBI, the structure of local government. Simple lists don't need maps.
""",
    example="""
**Anu** drew a concept map of Parliament from memory, with 12 concepts: President, Parliament, Lok Sabha, Rajya Sabha, Speaker, Vice-President, money bill, ordinary bill, members, people, state legislatures, joint sitting.

She drew arrows such as "Parliament → consists of → President, Lok Sabha and Rajya Sabha", "Vice-President → is the chairman of → Rajya Sabha", "Rajya Sabha members → elected by → elected members of state legislative assemblies", and "money bill → can be introduced only in → Lok Sabha".

When she checked with her textbook, she found two wrong links: she had drawn the President presiding over joint sittings (it is the Speaker of the Lok Sabha), and she had forgotten that the Rajya Sabha must return a money bill within 14 days. She fixed both in red. Two days later she redrew the map from memory with 17 of 18 links right. The joint-sitting fact became a contrast card.
""",
    evidence=[
        ('Concept mapping with the text open', 'limited', 'Karpicke and Blunt (2011): less effective for long-term retention than retrieval practice.'),
        ('Drawing concept maps from memory, then checking', 'moderate', 'It turns mapping into retrieval with feedback, and shows how well you understand the connections.'),
        ('Labelled links between concepts', 'limited', 'A practical feature of concept maps that forces precise thinking; little direct research on labels alone.'),
    ],
    resources=[
        ('karpicke-blunt', 'Reread the press release: what concept mapping was compared with', '5 minutes'),
        ('ls-dual', 'Revisit the dual coding poster: maps and diagrams as a second route to memory', '5 minutes'),
        ('ls-retrieval', 'Revisit the retrieval practice poster: drawing from memory counts', '5 minutes'),
    ],
    steps=[
        'Choose a PSC topic with many connected ideas that you have already studied.',
        'Without the book, list 10 to 15 key concepts, then draw the map with labelled arrows and at least two cross-links (about 15 minutes).',
        'Open the source. Add missing concepts and links, and fix wrong ones, in another colour. Count your correct links.',
        'Turn every wrong link into a contrast card or a margin question.',
        'Two days later, redraw the map from memory without looking, and count the correct links again.',
    ],
    proof='Your first map with corrections and link count, and the two-day redraw with its link count.',
    templates=[
        ('concept map from memory', """
CONCEPT MAP FROM MEMORY     Topic: ______________  Date: ______
1. Concepts I can recall (10-15): ____________________________________________
2. Most general concept (top): ______________
3. Draw boxes and LABELLED arrows. Each arrow must read as a sentence.
4. Cross-links (at least 2): __________________ ; __________________
5. Checked against: ______________ page ___
   Correct links ___ / total ___   Wrong links fixed ___   Missing links added ___
6. Two-day redraw: correct links ___ / ___
""", ''),
        ('linking words', """
consists of | is part of | is elected by | is appointed by | is the head of
presides over | can delay | must approve | causes | leads to | prevents
depends on | is an example of | is different from | replaced | was founded by
""", ''),
    ],
    mistakes=[
        ('Lines without labels.', 'Every arrow needs a label; otherwise you can\'t tell if the link is right.'),
        ('Copying a map from the book.', 'Draw from memory first, then check. Copying is not retrieval.'),
        ('Thirty concepts on one page.', 'Ten to fifteen is enough. Split big topics into two maps.'),
        ('Using maps instead of recall practice.', 'A map drawn from memory is recall practice; one drawn with the book open mostly isn\'t.'),
    ],
    quiz=[
        {'q': 'What did Karpicke and Blunt find about concept mapping with the text available?', 'o': ['It gave worse long-term retention than retrieval practice', 'It beat every other method', 'It was the same as rereading', 'It was never tested'], 'a': 'A', 'why': 'Retrieval practice produced much better long-term retention.'},
        {'q': 'How do you turn a concept map into retrieval practice?', 'o': ['Draw it from memory, then check against the source', 'Copy it neatly from the book', 'Colour it carefully', 'Print one from the internet'], 'a': 'A', 'why': 'Producing it from memory is retrieval; checking gives feedback.'},
        {'q': 'Which is a properly labelled link?', 'o': ['"Vice-President → is the chairman of → Rajya Sabha"', '"Vice-President — Rajya Sabha"', '"Vice-President, Rajya Sabha, Lok Sabha"', '"Vice-President → ?"'], 'a': 'A', 'why': 'The label turns the link into a checkable sentence.'},
        {'q': 'Who presides over a joint sitting of the two houses of Parliament?', 'o': ['The Speaker of the Lok Sabha', 'The President', 'The Prime Minister', 'The Chief Justice of India'], 'a': 'A', 'why': 'This was one of the errors Anu found and fixed by checking her map.'},
    ],
    study='The Karpicke and Blunt press release, revisited with the dual coding and retrieval posters',
    action='Draw a concept map from memory, check it, and redraw it two days later',
)

L4 = lesson(
    M, 4,
    outcome='Rebuild formulas and rules from a few basic truths so you can work them out instead of memorising them, starting with PSC arithmetic.',
    split='15 minutes reading, 20 minutes resources, 50 minutes action',
    core=f"""
### What first principles are

**First principles** are the basic truths from which other things follow. A student who knows only the shortcut formula is stuck when a question is phrased differently. A student who knows **why** the formula works can rebuild it, check it and adapt it under pressure.

### Six PSC examples

1. **Per cent means "per hundred".** So x% of y = x × y ÷ 100, and percentage change = (new − old) ÷ old × 100. A classic trap: a price rises 20% and then falls 20%. From first principles, the price becomes 1.2 × 0.8 = 0.96 of the original: a **4% fall**, not "no change".
2. **Profit and loss** are percentages of the **cost price**. Selling price = cost price × (1 + profit% ÷ 100).
3. **Speed:** distance = speed × time. Two people moving towards each other close the gap at the **sum** of their speeds; moving the same way, at the **difference**. Every "relative speed" formula follows.
4. **Time and work:** if A finishes a job in 10 days, A does 1/10 of it each day. Rates add. A (1/10 a day) and B (1/15 a day) together do 1/10 + 1/15 = 1/6 a day, so they finish in **6 days**.
5. **Simple interest:** R% of the principal P each year for T years gives P × R × T ÷ 100. Compound interest applies the same R% to a growing amount each year.
6. **Calendars:** a 365-day year is 52 weeks and **1 extra day**, so the same date moves one weekday later the next year (two if a 29 February comes between). "Odd days" questions are all built on this.

### The method

1. **Ask: what must be true for this rule to work?**
2. **Go down to the definition:** per cent, rate, distance, a week.
3. **Rebuild the rule** step by step in your own words.
4. **Test it with small, easy numbers:** a price of ₹100, a job of 1, a distance of 60 km.
5. **Keep the principle,** and make a card only for the principle plus one example.

Then practise until applying the principle is fast. In the exam you won't have time to derive slowly; first principles make the method reliable, and practice makes it quick (Module 14).

### Beyond maths

The same habit helps in GK when there is a reason behind a rule: why the Rajya Sabha is permanent (continuity), why Directive Principles can't be enforced in court (they depend on resources and policy), why the monsoon rains on the windward side of the Ghats (Module 3). **Dates, names and article numbers have no first principles.** Learn those with cards and mnemonics (Modules 4 and 11).
""",
    example="""
**Ashiq**'s maths guide had a page of 42 shortcut formulas, and he had tried to learn them all. In mocks he kept using the wrong one, especially for successive percentage changes and time-and-work questions.

He picked five formulas and rebuilt each from its definition, testing with small numbers. For successive changes he wrote: "Each change multiplies: 1.1 × 1.1 = 1.21, so two 10% rises make 21%." For time and work: "Turn days into a daily rate, add the rates, turn back into days." For pipes and cisterns he noticed it was the same principle with one rate negative, which removed four formulas from his list.

He solved two previous-year questions for each principle without the shortcut page. All ten were right, and for the first time he could explain why. His list of 42 shortcuts became 6 principles and a few cards.
""",
    evidence=[
        ('Understanding why a method works (self-explanation of worked examples)', 'moderate', 'Self-explanation is rated moderate utility by Dunlosky and others (2013); worked examples help beginners (CESE review).'),
        ('Rebuilding rules from first principles', 'limited', 'A practical approach consistent with research on self-explanation and schemas; little direct research by this name.'),
        ('Memorising many shortcut formulas without understanding', 'limited', 'Little direct research; shortcuts are fragile when a question is phrased differently. Keep principles, practise speed.'),
    ],
    resources=[
        ('os-prealg-6-1', 'Read the definition of percent and do the first exercises, rebuilding each conversion from the definition', '20 minutes'),
        ('os-prealg', 'Look at the table of contents and note the chapters that match your PSC maths syllabus', '10 minutes'),
        ('cese-clt', 'Reread the part on worked examples and expertise reversal', '10 minutes'),
    ],
    steps=[
        'Pick five formulas or shortcuts from your PSC maths or reasoning guide that you often confuse.',
        'For each, fill in the first-principles sheet: the basic truth, the rule rebuilt step by step, and a test with small numbers.',
        'Solve two previous-year questions for each principle without looking at the shortcut page.',
        'Pick one non-maths rule (for example why the Rajya Sabha is permanent) and explain its reason from first principles in five lines; check it in your textbook.',
        'Make one AnkiDroid card per principle: the principle on the back, with one worked example.',
    ],
    proof='Five first-principles sheets with tests and PYQ solutions, your five-line non-maths explanation, and a screenshot of the new cards.',
    templates=[
        ('first-principles sheet', """
FIRST PRINCIPLES      Formula or rule: ______________________________
The basic truth (definition): ________________________________________
Rebuilt step by step:
1. ______________________________________________________________
2. ______________________________________________________________
3. ______________________________________________________________
Small-number test (e.g. ₹100, a job of 1, 60 km): ___________________ works? Y / N
PYQ 1: ______ solved with the principle: right? Y / N
PYQ 2: ______ solved with the principle: right? Y / N
Card: front "____________ (principle)?"  back "____________ + one example"
""", ''),
        ('principle or memorise?', """
Has a reason or a definition behind it?  -> rebuild it from first principles
  (percentages, rates, interest, speed, calendars, why a rule exists)
Pure fact with no reason to derive?       -> card or mnemonic
  (dates, names, article numbers, places, awards)
""", ''),
    ],
    mistakes=[
        ('Memorising pages of shortcuts.', 'Keep the few principles they come from, and practise applying them.'),
        ('Deriving slowly in the exam.', 'Understand first, then practise until the method is fast.'),
        ('Trying to "derive" dates and names.', 'Facts have no first principles. Use cards and mnemonics.'),
        ('Skipping the small-number test.', 'Testing with ₹100 or a job of 1 catches mistakes in your rebuilt rule.'),
    ],
    quiz=[
        {'q': 'A price rises by 20% and then falls by 20%. What is the overall change?', 'o': ['A 4% fall', 'No change', 'A 4% rise', 'A 40% fall'], 'a': 'A', 'why': '1.2 × 0.8 = 0.96 of the original price.'},
        {'q': 'A can finish a job in 10 days and B in 15 days. How long do they take together?', 'o': ['6 days', '12.5 days', '25 days', '5 days'], 'a': 'A', 'why': '1/10 + 1/15 = 1/6 of the job per day.'},
        {'q': 'Why does a date move one weekday later in the next ordinary year?', 'o': ['365 days is 52 weeks and 1 extra day', 'Because of leap seconds', 'Because the calendar was changed', 'It moves two weekdays every year'], 'a': 'A', 'why': 'The one odd day shifts the weekday; a 29 February makes it two.'},
        {'q': 'Which of these should you learn with cards rather than first principles?', 'o': ['The year the Vaikom Satyagraha began', 'Successive percentage change', 'Relative speed', 'Simple interest'], 'a': 'A', 'why': 'Dates have no principle to derive; the others follow from definitions.'},
    ],
    study='OpenStax Prealgebra 6.1 on percent, and the CESE review on worked examples',
    action='Rebuild five PSC formulas from first principles and solve two PYQs with each',
)

LESSONS = [L1, L2, L3, L4]

MODULE = module(
    M,
    overview="""
Go beyond memorising: explain topics simply with the Feynman technique, ask deep questions, draw concept maps from memory and rebuild rules from first principles. Record five Feynman explanations of PSC topics and improve each one.

Memorised facts answer simple questions; understanding answers the harder ones, such as statement questions, unfamiliar maths problems and "which of these is not" questions. This module gives you four ways to build understanding, each honest about its evidence and each combined with recall so it works for the exam too.

The module project is five recorded Feynman explanations, each with a first and an improved version. Listening to your own explanations is one of the fastest ways to find out what you really understand.
""",
    outcomes=[
        'Use self-explanation and the Feynman technique, and record and improve explanations',
        'Ask six kinds of questions and write PSC-style statement questions',
        'Ask for help with a clear three-part question',
        'Draw and check concept maps from memory',
        'Rebuild arithmetic rules from first principles and test them',
    ],
    lessons=LESSONS,
    tools=[
        'The **Feynman template** (one of the six core tools) and **self-explanation prompts**',
        'The **question stems card**, **statement-question builder** and **three-part help question**',
        'The **concept map from memory** sheet and **linking words**',
        'The **first-principles sheet**',
    ],
    project='Five Feynman explanations',
    project_steps=[
        'Choose five PSC topics, including at least one maths or reasoning method and at least one Constitution topic. Your explanation from LRN-M08-L01 counts as the first.',
        'For each, record v1 without notes, listen back with the Feynman template, fix the gaps from the source, and record v2.',
        'Score every version (accuracy, clarity, completeness, without notes; out of 12) and work out your average for v1 and v2.',
        'Turn the gaps from all five into flashcards (at least 10 in total).',
        'Play one v2 to your study partner or a family member and ask: "What was unclear?" Note their answer.',
    ],
    project_proof='Ten recordings (v1 and v2 for five topics), five filled-in Feynman templates with scores and averages, the new cards, and your listener\'s feedback.',
    rubric=[
        ('Recordings', 'Fewer than five topics', 'Five topics, some without v2', 'Five topics, each with v1 and v2'),
        ('Gap finding', 'Listened without noting gaps', 'Some gaps noted', 'Every pause, vague phrase and error noted and fixed from the source'),
        ('Improvement', 'No change from v1 to v2', 'Small improvement', 'Clear improvement in scores and clarity'),
        ('Follow-up', 'No cards', 'A few cards', 'At least 10 cards from the gaps and one listener\'s feedback'),
    ],
    short=[
        'Do three Feynman explanations instead of five, each with v1 and v2.',
        'Skip the concept map lesson\'s redraw; keep the first-principles sheets for maths.',
    ],
    flashcards=[
        ('Self-explanation', 'Explaining to yourself why each statement or step is true while studying; moderate utility.'),
        ('The six Feynman steps', 'Choose, explain simply without notes and record, find gaps, fix from source, simplify, record again.'),
        ('Evidence position on the Feynman technique', 'Not tested by name; its parts (self-explanation, retrieval, explaining) are supported.'),
        ('Six kinds of question', 'Fact, reason, process, comparison, application, what if.'),
        ('Three-part help question', 'What I am trying to understand, what I know or tried, exactly where I am stuck.'),
        ('Concept map versus retrieval (Karpicke and Blunt)', 'Mapping with the text open lost to retrieval practice; draw maps from memory instead.'),
        ('A 20% rise then a 20% fall', 'A 4% fall overall (1.2 × 0.8 = 0.96).'),
        ('Facts with no first principles', 'Dates, names and article numbers: use cards and mnemonics.'),
    ],
    mistakes=[
        ('Feeling that you understand because the explanation made sense in class.', 'Explain it yourself, without notes, and record it.'),
        ('Spending hours on beautiful maps or notes.', 'Understanding shows in what you can explain and answer from memory.'),
    ],
)
