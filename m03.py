"""Module 3: The six evidence-based strategies."""
from common import lesson, module, link, fence, table
import tools

M = 3

L1 = lesson(
    M, 1,
    outcome='Use several forms of retrieval practice on PSC material, and make recall the first and last step of every study session.',
    split='20 minutes reading, 25 minutes resources, 45 minutes action over three sessions',
    core=f"""
Retrieval practice means **learning by pulling information out of your memory**, not by putting it in again. In Module 1 you saw it beat rereading on your own facts. Of the ten techniques Dunlosky and colleagues reviewed, practice testing was one of only two rated **high utility**: it works for many kinds of material, for learners of different ages and abilities, and in real classrooms ({link('dunlosky-aft', 'Dunlosky, 2013')}).

### Ten ways to retrieve

You don't need a formal test. Anything that makes you produce the answer from memory counts:

1. **Blank-page recall:** close the book and write everything you remember about the topic.
2. **Answer previous-year questions** (PYQs) on the topic.
3. **Cover the options:** read an MCQ's question, cover the four options with your thumb, answer in your head, then uncover and choose.
4. **Flashcards** with spaced repetition (Module 4).
5. **Explain it aloud** without notes, as if teaching (Module 8).
6. **Fill a blank map, timeline or table** from memory: draw Kerala's districts, the order of the Five-Year Plans, the three lists of the Seventh Schedule.
7. **Answer your own margin questions** with the text covered.
8. **The two-minute warm-up:** before a new topic, recall yesterday's.
9. **Quiz a partner,** and let them quiz you (Module 20).
10. **The weekly brain dump:** on Sunday, list everything you studied this week from memory (your weekly review).

### Rules that make retrieval work

- **Retrieve before you reread.** The book opens after you have tried.
- **Always check.** Compare with the source and fix errors straight away, so you don't strengthen a wrong answer.
- **Make it effortful, not impossible.** If you can't recall anything, the material was never learned: study it again first, then retrieve.
- **Keep it low-stakes.** These are practice tests, not judgements of you. Mistakes now are cheap.
- **Recall at the start and end of every session:** the "retrieval sandwich". Start with yesterday's topic; end with today's.

### Why cover the options?

Kerala PSC exams are multiple choice. When you see the options first, you often recognise the answer without being able to recall it, and recognition feels like knowing. Covering the options makes you recall first, then confirms with the options. It turns every MCQ in your guide into harder, more useful retrieval. It is a simple practical tweak; you will check it against your own scores.
""",
    example="""
**Sreeja** had a guide with 1,000 MCQs on the Indian Constitution. She used to read each question with its options, tick the one that looked right and move on. She scored about 70% in practice and 45% in a mock exam with new questions.

She changed one thing: she covered the options with a strip of card. For each question she said her answer aloud, then uncovered. If her answer was among the options and correct, she ticked it; if she had recognised the answer only after seeing the options, she marked it with an R.

On the first day, 40% of her "correct" answers were R's: things she recognised but couldn't recall. Those became her review list and, later, her flashcards. She also began every afternoon slot with a three-minute blank-page recall of the morning's topic. After two weeks, the R's were down to 15%, and her next mock rose to 58%.
""",
    evidence=[
        ('Retrieval practice (practice testing)', 'strong', 'Rated high utility by Dunlosky and others (2013): works across materials, ages and real classrooms.'),
        ('Checking answers after retrieval (feedback)', 'strong', 'Feedback corrects errors so they are not strengthened; recommended in the reviews behind this lesson.'),
        ('Covering the options before answering MCQs', 'limited', 'A practical tweak that turns recognition into recall. Retrieval in any format helps; judge this one by your own scores.'),
    ],
    resources=[
        ('ls-retrieval', 'Watch the video and download the poster and bookmark', '15 minutes'),
        ('retrievalpractice', 'Browse the free guides and read one on retrieval practice strategies', '20 minutes'),
        ('dunlosky-aft', 'Read the section on practice testing', '10 minutes'),
    ],
    steps=[
        'For your next three PSC study sessions, use the retrieval sandwich below.',
        'Start each session with a 3-minute blank-page recall of the previous session\'s topic. Check and fix in another colour.',
        'Study today\'s topic in two chunks. After each chunk, close the book and recall for 3 minutes, then check.',
        'End with 10 MCQs on today\'s topic from a previous paper or your guide, using cover-the-options. Mark answers you only recognised with an R.',
        'Log each session in your Study Log: Method = retrieval, and what you recalled.',
    ],
    proof='Three retrieval sandwich sheets with your recalls, corrections and MCQ scores (with R marks), and the three Study Log rows.',
    templates=[
        ('retrieval sandwich (one study session)', """
RETRIEVAL SANDWICH      Date: ______  Today's topic: ______________

START (3 min): blank-page recall of last session's topic: ______________
   Recalled ___ points; fixed ___ errors; gaps for tomorrow: ___________

MIDDLE: today's topic in two chunks
   Chunk 1: read ___ min -> recall 3 min -> check   [ ]
   Chunk 2: read ___ min -> recall 3 min -> check   [ ]

END: 10 MCQs, options covered first
   Correct ___/10   of which recognised only (R) ___
   Wrong or R questions go to: review list / flashcards / Revision tab
""", ''),
        ('cover-the-options method', """
1. Cover the four options with a strip of card or your thumb.
2. Read the question. Say or write your answer.
3. Uncover. If your answer is there and right: tick.
   If you only knew it once you saw the options: tick and mark R.
   If wrong: mark X and write the right answer with its source.
4. R and X questions are your review list for the next session.
""", ''),
    ],
    mistakes=[
        ('Peeking at the answer after a few seconds.', 'Give yourself a real try, 20 to 30 seconds for a fact, before checking.'),
        ('Practising only with MCQs and options visible.', 'Recognition is easier than recall. Cover the options and mix in blank-page recall.'),
        ('Testing only topics you already know well.', 'Retrieve your weak topics too. That is where the gains are.'),
        ('Never checking answers.', 'Unchecked errors get stronger. Check every time.'),
    ],
    quiz=[
        {'q': 'Which is a form of retrieval practice?', 'o': ['Drawing Kerala\'s districts on a blank map from memory', 'Reading the map again', 'Highlighting district names', 'Copying the map neatly'], 'a': 'A', 'why': 'Producing it from memory is retrieval; the others are re-exposure.'},
        {'q': 'What is the "retrieval sandwich"?', 'o': ['Recall at the start of a session (previous topic) and at the end (today\'s topic)', 'Studying between two meals', 'Reading a topic twice with a break', 'A type of flashcard'], 'a': 'A', 'why': 'Recall begins and ends every session.'},
        {'q': 'Why cover the options of an MCQ?', 'o': ['Recognising an answer is easier than recalling it, so covering forces recall', 'It makes the question shorter', 'PSC questions have no options', 'It saves paper'], 'a': 'A', 'why': 'It turns recognition into recall and shows you what you only recognise.'},
        {'q': 'You recall nothing at all about a topic. What should you do?', 'o': ['Study it again first, then retrieve', 'Keep trying for an hour', 'Skip the topic for good', 'Mark it as done'], 'a': 'A', 'why': 'Retrieval should be effortful but possible. If nothing comes, the material needs learning first.'},
    ],
    study='The Learning Scientists\' retrieval practice materials and the practice testing section of Dunlosky\'s review',
    action='Run three retrieval sandwich sessions on your PSC topics',
)

L2 = lesson(
    M, 2,
    outcome='Build a Revision tab that schedules spaced reviews of your PSC topics automatically, and follow it for a week.',
    split='15 minutes reading, 20 minutes resources, 40 minutes action plus 10 minutes a day for a week',
    core=f"""
### The spacing effect

The same amount of study, spread over several days, is remembered much longer than the same amount crammed into one session. This is the **spacing effect**, and distributed practice is the second technique Dunlosky and colleagues rated **high utility** ({link('dunlosky-aft', 'Dunlosky, 2013')}).

Cramming does work, for tomorrow. If your test is the next morning, a long session tonight can help. But a PSC exam covers months of material, and the questions come weeks or months after you studied. Cramming loses that race; spacing wins it.

Spacing works together with retrieval. Each time you come back after a gap and recall, you are doing **spaced retrieval practice**: the forgetting curve flattens a little more with every successful recall (Module 1).

### How far apart?

A sensible default for whole topics is **expanding gaps**: review 1 day after first learning, then 3 days, 7 days, 21 days and about 60 days. Each review starts with recall, then a check.

Don't worry about exact numbers. Research shows clearly that spacing beats cramming; it is less clear that one gap pattern is best for everyone. What matters is that you come back, more than once, with gaps that grow.

For single facts (names, dates, article numbers), spacing by hand is too much work. AnkiDroid does it for you in Module 4, adjusting each card's gaps to how well you know it. The revision schedule in this lesson is for **whole topics and skills**: a chapter, a type of maths problem, a grammar rule.

### Making it automatic

Your Learning Workbook gets a **Revision** tab. You type the topic and the date you first studied it; formulas fill in the review dates, show the next one, and mark DUE on the right days. Each day you open the tab, do the DUE reviews first, and log your score.

A daily PSC plan then has two parts: **reviews due today** (do them first, usually 15 to 30 minutes) and **new learning**. If you have to drop something on a bad day, drop new learning, not reviews.

### When you miss a review

Do it as soon as you can and continue the schedule; don't restart. If your score in a review is low (under about 60%), relearn the gaps and restart that topic from the 1-day review.
""",
    example="""
**Anu** studies three PSC subjects in rotation: Kerala history, the Indian Constitution and geography. Before this lesson she "revised" everything in a panic during the last two weeks before an exam.

She made the Revision tab on her phone and entered the twelve topics she had studied in the previous fortnight, using approximate dates. The formulas immediately showed four topics DUE that day, which surprised her: she had forgotten she had studied two of them.

Her new routine starts at 6 a.m. with the DUE topics: for each one, a five-minute blank-page recall, a check against her notes, and a score out of 10 in the "Last score" column. Then she moves to new learning. After a week she had done 19 reviews and her average score had risen from 5.5 to 7. The Kerala renaissance, which she had always found slippery, was at 8 out of 10 on its 7-day review.
""",
    evidence=[
        ('Spaced (distributed) practice', 'strong', 'Rated high utility by Dunlosky and others (2013), across many kinds of material.'),
        ('Spacing combined with retrieval', 'strong', 'Each spaced review that starts with recall strengthens memory more than rereading.'),
        ('Cramming for an exam weeks away', 'none', 'It can help a test the next day, but the material fades quickly.'),
        ('One best pattern of gaps (such as 1-3-7-21-60)', 'limited', 'Any spacing beats cramming; expanding gaps are a sensible default, not a proven optimum.'),
    ],
    resources=[
        ('ls-spacing', 'Watch the video and download the spaced practice poster', '15 minutes'),
        ('ncase', 'Revisit the part of the comic that explains why gaps should grow', '10 minutes'),
        ('dunlosky-aft', 'Read the section on distributed practice', '10 minutes'),
    ],
    steps=[
        'Add a Revision tab to your Learning Workbook with the headings and formulas below. Check that the dates appear when you type a first-studied date.',
        'Enter every PSC topic you studied in the last two weeks, with approximate first-studied dates, plus today\'s topic. Aim for at least 8 rows.',
        'For the next 7 days, open the tab first thing in your study time and do every DUE review: blank-page recall for 5 minutes, check, score out of 10 (as a %) in "Last score %".',
        'Add each new topic you study this week on the day you study it.',
        'On day 7, count the reviews you did and work out your average score. Write two lines on what you noticed.',
    ],
    proof='A screenshot of your Revision tab with at least 8 topics and 7 days of review scores, and your two lines.',
    templates=[
        ('Revision tab headings', tools.REVISION, 'csv'),
        ('Revision tab formulas', tools.REVISION_FORMULAS, ''),
        ('revision schedule (core tool)', tools.REVISION_SCHEDULE, ''),
    ],
    mistakes=[
        ('Reviewing by rereading.', 'Every review starts with recall, then a check. Rereading alone wastes the spacing.'),
        ('Skipping a review because "I remember it".', 'Prove it with a 5-minute recall. If you do, the review is quick.'),
        ('Putting 40 topics in on day one.', 'Start with your last two weeks. Add new topics daily, and the tab grows at a pace you can manage.'),
        ('Dropping reviews on busy days.', 'Drop new learning instead. Reviews protect everything you already studied.'),
    ],
    quiz=[
        {'q': 'Why does cramming fail for a PSC exam that is weeks away?', 'o': ['Crammed material fades quickly, while spaced study lasts', 'Cramming is against the rules', 'It only works for maths', 'It takes more time than spacing'], 'a': 'A', 'why': 'Cramming can help tomorrow\'s test but not one weeks later.'},
        {'q': 'What should every spaced review start with?', 'o': ['A recall from memory, then a check', 'Rereading the chapter', 'Highlighting the key points', 'Watching a video on the topic'], 'a': 'A', 'why': 'Spaced retrieval is stronger than spaced rereading.'},
        {'q': 'On a very busy day, what should you drop first?', 'o': ['New learning', 'Reviews that are due', 'Sleep', 'AnkiDroid reviews'], 'a': 'A', 'why': 'Reviews protect what you have already learned; new topics can wait a day.'},
        {'q': 'What is the course\'s default pattern of review gaps for whole topics?', 'o': ['1, 3, 7, 21 and about 60 days', 'Every day for a year', 'Only once, the day before the exam', '30, 60 and 90 days'], 'a': 'A', 'why': 'Expanding gaps are a sensible default; any spacing beats cramming.'},
    ],
    study='The spaced practice materials and the distributed practice section of Dunlosky\'s review',
    action='Build your Revision tab and follow it for 7 days',
)

L3 = lesson(
    M, 3,
    outcome='Build mixed practice sets for PSC maths and reasoning, and learn to name the problem type before you solve it.',
    split='15 minutes reading, 20 minutes resources, 50 minutes action over two days',
    core=f"""
### Blocked versus interleaved practice

Most maths books teach in **blocks**: a chapter on percentages followed by 30 percentage questions, then a chapter on ratios followed by 30 ratio questions. In blocked practice you always know which method to use before you read the question, because it is the chapter's method.

The exam is different. Question 63 might be a ratio problem, question 64 a time-and-work problem and question 65 a calendar problem. The hardest part is often **choosing the method**, and blocked practice never trains that.

**Interleaving** means mixing different types of problems in one practice session: a percentage question, then a ratio question, then an average question, in no fixed order. You have to identify the type each time.

### What the research says

Dunlosky and colleagues rated interleaved practice **moderate utility**: promising, with the strongest evidence in mathematics and in learning to tell categories apart, and less evidence for other material ({link('dunlosky-aft', 'Dunlosky, 2013')}). The Learning Scientists include it among their six strategies ({link('ls-interleaving', 'interleaving materials')}).

Interleaving has a cost you should expect: practice feels harder and slower, and your score during practice may drop. The benefit shows up later, in tests with mixed questions, which is exactly what a PSC paper is.

### How to interleave

1. **Learn each type first.** Use worked examples and a few blocked questions when a type is new (Module 1). Interleave once you know two or more types.
2. **Mix related types that are easy to confuse:** percentage and profit-and-loss, ratio and partnership, speed and time-and-work, simple and compound interest.
3. **Name the type before solving.** Write "ratio: compare parts" or "time and work: add the rates" before you calculate. This is the skill you are training.
4. **Mix old and new.** Include types from earlier weeks; that also gives you spacing.
5. **Interleave subjects in a day:** a block of GK, then a block of maths, then English, instead of a whole day on one subject.

The idea also helps outside maths when topics are easy to confuse: Fundamental Rights, Directive Principles and Fundamental Duties; the rivers of Kerala and those of Karnataka; similar-sounding award names. Mixed questions force you to tell them apart.
""",
    example="""
**Ashiq** is good at maths. He practised by chapter: 30 percentage questions in 25 minutes, 30 ratio questions in 20. In his first full mock, the mental ability section went badly. He knew every method, but he lost time staring at mixed questions, unsure which method each one needed, and he used the percentage method on a profit-and-loss question with a twist.

He built mixed sets of 12 questions from four chapters he had studied: percentages, profit and loss, ratio and proportion, and averages. He wrote each question number on a slip of paper, shuffled the slips, and solved in that order. Before solving, he wrote the type and the method in a few words.

His first mixed set took 22 minutes, and he named the type correctly for 9 of 12. By the fourth set, a week later, he took 15 minutes and named all 12. In his next mock he finished the mental ability section with five minutes to spare.
""",
    evidence=[
        ('Interleaved practice for maths and problem types', 'moderate', 'Rated moderate utility by Dunlosky and others (2013); strongest evidence in mathematics and category learning.'),
        ('Interleaving easily confused topics in GK', 'limited', 'Less research outside maths and categories; useful in practice for telling similar facts apart.'),
        ('Practice scores drop at first', 'moderate', 'Interleaving feels harder during practice; its benefit shows in later mixed tests.'),
    ],
    resources=[
        ('ls-interleaving', 'Watch the video and download the interleaving poster', '15 minutes'),
        ('os-prealg-6-1', 'Do 6 mixed exercises from the end of the section, using the name-the-type method', '25 minutes'),
        ('dunlosky-aft', 'Read the section on interleaved practice', '10 minutes'),
    ],
    steps=[
        'Choose four maths or reasoning question types you have already studied, from your PSC syllabus (for example percentages, profit and loss, ratio, averages; or series, coding, directions, blood relations).',
        'Pick three questions of each type from your guide or previous papers: 12 in all. Write their numbers on slips of paper and shuffle them.',
        'Solve in the shuffled order. Before each one, write the type and the method in a few words. Time the whole set.',
        'Mark each question twice: type named correctly? answer correct?',
        'The next day, build a second mixed set of 12 from the same four types (new questions) and repeat. Compare time, types named and answers correct.',
    ],
    proof='Your two mixed sets with type labels, workings, both marks and the times.',
    templates=[
        ('mixed practice set builder', """
MIXED SET #___     Date: ______   Types in this set: A ______ B ______ C ______ D ______
Shuffled order: ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___

Q  | Type I named      | Method in a few words         | Type right? | Answer right?
1  | _________________ | _____________________________ | Y / N       | Y / N
2  | _________________ | _____________________________ | Y / N       | Y / N
...
12 | _________________ | _____________________________ | Y / N       | Y / N
Time: ___ min   Types named right ___/12   Answers right ___/12
Confused pairs (e.g. percentage vs profit-and-loss): _______________________
""", ''),
        ('easily confused pairs to mix (PSC)', table(['Maths and reasoning', 'GK and language'], [
            ('Percentage and profit and loss', 'Fundamental Rights, Directive Principles and Fundamental Duties'),
            ('Ratio and partnership', 'Lok Sabha and Rajya Sabha'),
            ('Speed-distance and time and work', 'Kerala rivers and their districts'),
            ('Simple and compound interest', 'Similar award names and their fields'),
            ('Number series and letter series', 'Synonyms and antonyms'),
        ]), ''),
    ],
    mistakes=[
        ('Interleaving a type you have not learned yet.', 'Learn each type with worked examples first; mix once you know two or more.'),
        ('Giving up because it feels slow.', 'Slower practice is the price of better exam performance. Compare scores after a week.'),
        ('Solving before naming the type.', 'Naming the type is the skill. Write it first, every time.'),
        ('Mixing only unrelated topics.', 'Mix types that are easy to confuse; that is where interleaving helps most.'),
    ],
    quiz=[
        {'q': 'What skill does interleaving train that blocked practice does not?', 'o': ['Choosing the right method for each question', 'Writing faster', 'Remembering formulas', 'Reading questions aloud'], 'a': 'A', 'why': 'In blocked practice the chapter tells you the method; in exams you must choose.'},
        {'q': 'How did Dunlosky and colleagues rate interleaved practice?', 'o': ['Moderate utility, strongest in maths and category learning', 'High utility for everything', 'Low utility', 'Not reviewed'], 'a': 'A', 'why': 'It is promising, with most evidence in maths and telling categories apart.'},
        {'q': 'When should you start interleaving a new maths type?', 'o': ['After learning it with worked examples and a few practice questions', 'Before seeing any example', 'Only on exam day', 'Never'], 'a': 'A', 'why': 'Learn each type first, then mix.'},
        {'q': 'Your practice score drops when you start interleaving. What does that most likely mean?', 'o': ['It is the expected cost; the benefit shows in later mixed tests', 'Interleaving does not work for you', 'You should go back to blocked practice for good', 'The questions are wrong'], 'a': 'A', 'why': 'Interleaving feels harder at first; judge it by mixed tests a week later.'},
    ],
    study='The interleaving materials and the interleaved practice section of Dunlosky\'s review',
    action='Solve two shuffled mixed sets of PSC maths or reasoning questions, naming each type first',
)

L4 = lesson(
    M, 4,
    outcome='Turn PSC facts into connected knowledge with how-and-why questions, and make abstract ideas memorable with accurate examples from Kerala life.',
    split='15 minutes reading, 25 minutes resources, 40 minutes action plus a 10-minute check two days later',
    core=f"""
### Elaboration: ask how and why

**Elaboration** means explaining and connecting ideas: asking how and why something is true, and how it relates to what you already know. Dunlosky and colleagues rated two forms of it, **elaborative interrogation** (asking "why?") and **self-explanation**, as **moderate utility**: promising, with good evidence for factual learning ({link('dunlosky-aft', 'Dunlosky, 2013')}).

It works because a fact connected to other facts has more ways to be found again (Module 1). Compare:

- "Kerala state was formed on 1 November 1956." One isolated fact.
- "**Why** then? Because the States Reorganisation Act of 1956 redrew states on language lines, and Malayalam-speaking Travancore-Cochin and Malabar were joined." Now the date hangs on a reason, a law and a map.

Good elaboration questions for PSC topics:

- **Why** did this happen? **Why** is this true?
- **How** does it work? **How** did it change things?
- **How is X different from Y?** (Fundamental Rights and Directive Principles: the first can be enforced in court, the second cannot.)
- **What would happen if** it were not so?
- **How does this connect to** something I already know?

Always **check your answers against the source**. Elaboration with a wrong explanation can make a wrong idea stick.

### Concrete examples: make it real

Abstract ideas (federalism, inflation, secularism, a fundamental duty, GDP) are hard to remember as definitions. A **concrete example** is a specific case that shows the idea. The Learning Scientists list concrete examples as one of their six strategies ({link('ls-concrete', 'concrete examples materials')}). Three tips:

1. **Use more than one example,** and make them different. Then ask what they have in common: that common thread is the idea.
2. **Use examples from your own life in Kerala.** Inflation: the price of a meal at your local hotel this year compared with five years ago. The Concurrent List: education, where both Parliament and the state legislature can make laws.
3. **Check that your example is accurate.** A wrong example teaches a wrong idea. Confirm it in your textbook.

### Using both together

Read a paragraph, ask a why-question, answer it from memory in your own words, give an example, then check. This is slower than reading, and it is supposed to be: you are building connections that will hold the facts for months.
""",
    example="""
**Joseph sir**'s study group uses "why chains" for geography. One evening the topic was the monsoon. Instead of memorising "the south-west monsoon reaches Kerala first", they asked a chain of questions and answered each from memory before checking the SCERT textbook:

- Why does the monsoon reach Kerala first? Because Kerala is at the south-western tip of the peninsula, the first land the moist south-west winds meet.
- Why does it rain so much on our side? Because the Western Ghats force the moist winds to rise and cool.
- So how is the other side of the Ghats different? It gets far less rain; it is in the rain shadow.

Then each member gave a concrete example from their own experience: Vinod described the heavy rain at Kuttiady compared with what his cousin sees across the Ghats in Karnataka. One member's answer about where the winds come from turned out to be wrong when they checked, and they corrected it together. Two days later, all five answered the group's five monsoon questions without notes.
""",
    evidence=[
        ('Elaborative interrogation (asking why)', 'moderate', 'Rated moderate utility by Dunlosky and others (2013), with good evidence for learning facts.'),
        ('Self-explanation', 'moderate', 'Rated moderate utility; explored further in Module 8.'),
        ('Concrete examples, especially several different ones', 'moderate', 'One of the Learning Scientists\' six strategies; works best with varied examples and the common idea made explicit.'),
    ],
    resources=[
        ('ls-elaboration', 'Watch the video and download the elaboration poster', '15 minutes'),
        ('ls-concrete', 'Watch the video and download the concrete examples poster', '15 minutes'),
        ('dunlosky-aft', 'Read the sections on elaborative interrogation and self-explanation', '10 minutes'),
    ],
    steps=[
        'Choose a PSC topic with causes, processes or comparisons: a period of Kerala history, a geography process or a part of the Constitution.',
        'Write 10 how-or-why questions about it. Answer each from memory in one or two sentences, then check the textbook and correct in another colour.',
        'Write 3 "how is X different from Y?" questions on things in the topic that are easy to confuse, and answer them the same way.',
        'Pick 3 abstract terms from your syllabus (for example federalism, inflation, secularism, a fundamental duty, GDP). Write two different concrete examples for each, from Kerala life where you can, and check each against your textbook.',
        'Two days later, answer 5 of your why-questions from memory, without looking. Score them.',
    ],
    proof='Your why-question sheet with corrections, the 3 comparisons, the 6 examples and your two-day score.',
    templates=[
        ('why-chain sheet', """
WHY-CHAIN SHEET      Topic: ______________  Source: ______________ page ___
Q1  Why ______________________________?  My answer: _________________ Checked [ ] Fixed: ____
Q2  How ______________________________?  My answer: _________________ Checked [ ] Fixed: ____
...
Q10 _________________________________?  My answer: _________________ Checked [ ] Fixed: ____

COMPARE
How is ______ different from ______? _________________________________________
How is ______ different from ______? _________________________________________
How is ______ different from ______? _________________________________________

Two-day check (no looking): ___/5
""", ''),
        ('concrete example card', """
ABSTRACT IDEA: ______________   Definition in my words: _______________________
Example 1 (from Kerala life): ____________________________________________
Example 2 (different kind): _____________________________________________
What both examples have in common (the idea): _____________________________
Checked in: ______________ page ___
""", ''),
    ],
    mistakes=[
        ('Accepting your own explanation without checking.', 'A confident wrong answer sticks too. Check every answer against the source.'),
        ('Vague examples ("like in daily life").', 'Name a specific case: a place, a price, a law, a person.'),
        ('Using only one example.', 'Two different examples show what the idea really is; one example can mislead.'),
        ('Asking only "what" questions.', '"What" checks the fact; "why" and "how" build the connections that hold it.'),
    ],
    quiz=[
        {'q': 'Which question is an elaborative why-question?', 'o': ['Why did the 1956 reorganisation create Kerala on language lines?', 'When was Kerala formed?', 'Who was the first Chief Minister of Kerala?', 'How many districts does Kerala have?'], 'a': 'A', 'why': 'It asks for a reason and connects the date to a law and an idea.'},
        {'q': 'What is the main risk of elaboration?', 'o': ['Building on a wrong explanation if you don\'t check it', 'It takes no effort', 'It works only for maths', 'It replaces all other study'], 'a': 'A', 'why': 'Always check your answers against the source.'},
        {'q': 'What makes concrete examples most useful?', 'o': ['Several different examples, with the common idea made clear', 'One vivid example repeated often', 'Examples from another country only', 'Examples without checking them'], 'a': 'A', 'why': 'Varied examples show what the idea is, not just one case of it.'},
        {'q': 'How did Dunlosky and colleagues rate elaborative interrogation?', 'o': ['Moderate utility', 'High utility', 'Low utility', 'Harmful'], 'a': 'A', 'why': 'It is promising, with good evidence for factual learning.'},
    ],
    study='The elaboration and concrete examples materials and Dunlosky\'s sections on elaborative interrogation and self-explanation',
    action='Write and answer 10 why-questions, 3 comparisons and 6 checked examples on a PSC topic',
)

L5 = lesson(
    M, 5,
    outcome='Combine words with maps, timelines and diagrams, and run a complete 60-minute study session that uses all six strategies on one PSC topic.',
    split='20 minutes reading, 25 minutes resources, 60-minute study session plus a 15-minute check two days later',
    core=f"""
### Dual coding: words plus pictures

**Dual coding** means combining words with visuals: a map, a timeline, a flowchart, a table or a diagram. You then have two connected ways to find the memory, a verbal one and a visual one. The Learning Scientists list it among their six strategies ({link('ls-dual', 'dual coding materials')}).

Dual coding is **not** about learning styles (Module 2). A map helps everyone learn where places are. A timeline helps everyone learn the order of events.

Choose the visual by the content:

{table(['PSC content', 'Visual', 'Example'], [
    ('Places', 'Map', 'Kerala\'s 14 districts from north to south; national parks'),
    ('Order of events', 'Timeline', 'The Kerala renaissance: 1888, 1903, 1924, 1936'),
    ('Processes', 'Flowchart', 'How a bill becomes law; how a PSC rank list is made'),
    ('Comparisons', 'Table', 'Lok Sabha and Rajya Sabha; rights and duties'),
    ('Parts of a whole', 'Labelled diagram', 'Parts of the heart; layers of the atmosphere'),
    ('Hierarchies', 'Tree', 'The court system; local government tiers'),
])}

Three rules make dual coding work:

1. **The picture must carry meaning.** A decorative photo of a temple doesn't help you remember the Temple Entry Proclamation; a timeline that places it after the Vaikom and Guruvayur satyagrahas does.
2. **Draw it from memory, then check.** Drawing a timeline from memory is dual coding and retrieval at once. Copying a diagram neatly is mostly copying.
3. **Keep it simple.** Boxes, arrows, a few words. You are not making art, and an overloaded diagram adds cognitive load (Module 1).

Be careful with one related idea: Dunlosky and colleagues rated **imagining pictures while reading text** as low utility ({link('dunlosky-aft', 'Dunlosky, 2013')}). Real, meaningful visuals that you look at and draw are a different thing.

### One session, six strategies

Each strategy is good alone; together they make a study session that is hard to beat. Here is a 60-minute plan for one PSC topic:

{table(['Minutes', 'What you do', 'Strategies'], [
    ('0–5', 'Blank-page recall of the last session\'s topic; check', 'Retrieval, spacing'),
    ('5–25', 'Learn the new topic in chunks; ask why and how; give your own example for each idea', 'Elaboration, concrete examples'),
    ('25–35', 'Close the book; draw a map, timeline or diagram of it from memory; check and fix', 'Dual coding, retrieval'),
    ('35–50', 'Mixed practice: 10 questions from this topic and two older ones, options covered', 'Interleaving, retrieval'),
    ('50–55', 'Check answers; note errors; add the topic to the Revision tab', 'Spacing'),
    ('55–60', 'Write three margin questions for tomorrow\'s warm-up', 'Retrieval (planned)'),
])}

The same structure works in 30 minutes: halve every part.
""",
    example="""
**Anu** chose the Kerala renaissance for her six-strategy session. She began with a five-minute recall of yesterday's topic, the Travancore kings, and fixed two errors.

Then she studied four events with why-questions: why Sree Narayana Guru's consecration of a Shiva idol at Aruvippuram in 1888 was revolutionary; why the SNDP Yogam was founded in 1903; what the Vaikom Satyagraha of 1924 demanded; and what the Temple Entry Proclamation of 1936 changed. For each she wrote one line in her own words and one example of what the change meant for an ordinary person.

She closed the book and drew a timeline from memory with the four dates and the causes between them. She had placed two events in the wrong order; she fixed them in red. Next came ten mixed MCQs from the renaissance, the Travancore kings and the freedom struggle, with options covered. She scored 7, noted the three errors and added the topic to her Revision tab.

Two days later she redrew the timeline from memory, this time with no errors, and scored 9 out of 10 on new questions.
""",
    evidence=[
        ('Meaningful visuals combined with words (dual coding)', 'moderate', 'One of the Learning Scientists\' six strategies; the visual must carry the meaning, not decorate.'),
        ('Imagining pictures while reading text', 'limited', 'Rated low utility by Dunlosky and others (2013). Draw real visuals instead.'),
        ('Combining the six strategies in one session', 'limited', 'Little research on this exact package; each part has its own evidence, and the strongest parts are retrieval and spacing.'),
    ],
    resources=[
        ('ls-dual', 'Watch the video and download the dual coding poster', '15 minutes'),
        ('ls-materials', 'Download the six-strategy bookmarks (or posters) and keep them where you study', '10 minutes'),
        ('os-cs-6', 'Read 6.2 Studying, and compare its advice with the six strategies', '20 minutes'),
    ],
    steps=[
        'Choose a new PSC topic for one 60-minute session.',
        'Run the six-strategy session plan below, ticking each part as you finish it.',
        'Make your visual (map, timeline, flowchart, table or diagram) from memory in the 25–35 minute part, then check and fix it.',
        'Add the topic to your Revision tab.',
        'Two days later, redraw the visual from memory without looking, and answer 5 new questions on the topic. Score both.',
    ],
    proof='Your session plan with all six parts ticked, both versions of your visual drawn from memory, and the two-day scores.',
    templates=[
        ('six-strategy study session (60 minutes)', """
SIX-STRATEGY SESSION     Date: ______  Topic: ______________
[ ] 0-5    Warm-up recall of last topic (__________): recalled ___ points, fixed ___
[ ] 5-25   Learn in chunks: why/how question + my own example for each idea
           1. ______________________  2. ______________________  3. ____________
[ ] 25-35  Visual from memory: map / timeline / flowchart / table / diagram
           Errors found when checking: ___
[ ] 35-50  Mixed practice: 10 questions (this topic + __________ + __________)
           Correct ___/10, recognised only (R) ___
[ ] 50-55  Errors noted; topic added to the Revision tab
[ ] 55-60  Three margin questions for tomorrow:
           1. _____________________ 2. _____________________ 3. _____________________
Two-day check: visual redrawn with ___ errors; new questions ___/5
""", ''),
        ('choose your visual', """
Is it about WHERE?         -> map
Is it about WHEN or ORDER? -> timeline
Is it about HOW (steps)?   -> flowchart
Is it about COMPARING?     -> two- or three-column table
Is it about PARTS?         -> labelled diagram
Is it about LEVELS?        -> tree
Rule: draw it from memory first, then check, then fix in another colour.
""", ''),
    ],
    mistakes=[
        ('Decorating notes with pictures that carry no meaning.', 'Every visual should show where, when, how, what differs, or what the parts are.'),
        ('Copying a diagram instead of drawing it from memory.', 'Look, close the book, draw, check. Copying feels productive and teaches little.'),
        ('Cramming too much onto one visual.', 'One visual, one idea. Make two simple ones rather than one crowded one.'),
        ('Skipping the mixed practice part to save time.', 'It is where retrieval and interleaving happen. Shorten the other parts instead.'),
    ],
    quiz=[
        {'q': 'Which visual best suits the order of events in the Kerala renaissance?', 'o': ['A timeline', 'A pie chart', 'A photo of a temple', 'A labelled diagram of a building'], 'a': 'A', 'why': 'A timeline shows order and the gaps between events.'},
        {'q': 'Is dual coding the same as matching a "visual learning style"?', 'o': ['No: meaningful visuals help everyone learn content such as places and sequences', 'Yes, it only helps visual learners', 'Yes, and it harms auditory learners', 'No, it only helps auditory learners'], 'a': 'A', 'why': 'The content decides the visual, not a learning style.'},
        {'q': 'What did Dunlosky and colleagues rate as low utility?', 'o': ['Imagining pictures while reading text', 'Practice testing', 'Distributed practice', 'Interleaved practice in maths'], 'a': 'A', 'why': 'Imagery for text learning was rated low; real, meaningful visuals are different.'},
        {'q': 'In the 60-minute six-strategy session, what happens in minutes 35–50?', 'o': ['Mixed practice questions from this topic and older ones', 'Rereading the chapter', 'Drawing decorative pictures', 'A break'], 'a': 'A', 'why': 'Mixed questions combine interleaving and retrieval, with spacing for the older topics.'},
    ],
    study='The dual coding materials, the six-strategy bookmarks and College Success 6.2 Studying',
    action='Run one 60-minute six-strategy session with a visual drawn from memory, and check it two days later',
)

LESSONS = [L1, L2, L3, L4, L5]

MODULE = module(
    M,
    overview="""
Master the six strategies with the best research behind them: retrieval practice, spaced practice, interleaving, elaboration, concrete examples and dual coding. Use each on your PSC subjects, then combine all six in one study session.

These six strategies are promoted by The Learning Scientists, a group of cognitive psychologists who turn research into free materials for students and teachers. Two of them, retrieval and spacing, were the only techniques rated high utility in Dunlosky and colleagues\' major review; the others are rated moderate or promising. This module is the heart of the course: everything later builds on it.

Each lesson gives you a tool for your learning system, and the last lesson joins them into one session plan you can use every day of your PSC preparation.
""",
    outcomes=[
        'Use at least five forms of retrieval practice, and start and end every session with recall',
        'Run a Revision tab that schedules spaced reviews of your topics',
        'Build interleaved practice sets and name problem types before solving',
        'Ask and check how-and-why questions, and make accurate concrete examples',
        'Draw meaningful visuals from memory and run a 60-minute six-strategy session',
    ],
    lessons=LESSONS,
    tools=[
        'The **revision schedule** (one of the six core tools) and the **Revision** tab with formulas',
        'The **retrieval sandwich** and **cover-the-options** method',
        'The **mixed practice set builder**',
        'The **why-chain sheet** and **concrete example card**',
        'The **six-strategy session plan** for daily study',
    ],
    project='My six-strategy week',
    project_steps=[
        'Over one week, run at least four six-strategy sessions (60 or 30 minutes) on your PSC subjects.',
        'Keep the Revision tab running all week, doing DUE reviews first each day.',
        'Keep all session sheets and log each session in the Study Log.',
        'At the end of the week, write half a page: which strategy felt hardest, which gave the best two-day scores, and what you will keep doing.',
    ],
    project_proof='Four session sheets, a screenshot of your Revision tab with the week\'s scores, and your half-page reflection.',
    rubric=[
        ('Retrieval', 'Sessions start with reading', 'Recall used sometimes', 'Every session starts and ends with recall'),
        ('Spacing', 'No Revision tab', 'Tab made but not followed', 'DUE reviews done first every study day'),
        ('Interleaving', 'Only chapter-by-chapter practice', 'Some mixed questions', 'Mixed sets with types named first'),
        ('Elaboration and examples', 'Only "what" questions', 'Why-questions without checking', 'Checked why-questions and accurate examples'),
        ('Dual coding', 'No visuals, or copied ones', 'Visuals sometimes drawn from memory', 'A meaningful visual drawn from memory in each session'),
    ],
    short=[
        'Do only LRN-M03-L01 and LRN-M03-L02: the retrieval sandwich and the Revision tab.',
        'Run one 30-minute six-strategy session in the week.',
    ],
    flashcards=[
        ('The six strategies', 'Retrieval practice, spaced practice, interleaving, elaboration, concrete examples, dual coding.'),
        ('The two techniques rated high utility by Dunlosky and others', 'Practice testing and distributed (spaced) practice.'),
        ('The retrieval sandwich', 'Recall at the start of a session (last topic) and at the end (today\'s topic).'),
        ('Default review gaps for whole topics', '1, 3, 7, 21 and about 60 days, each starting with recall.'),
        ('What interleaving trains', 'Choosing the right method; name the type before solving.'),
        ('Best elaboration questions', 'Why? How? How is X different from Y? Then check the answer.'),
        ('Two tips for concrete examples', 'Use several different examples; check each is accurate.'),
        ('Rule for dual coding', 'Use meaningful visuals and draw them from memory, then check.'),
    ],
    mistakes=[
        ('Using one strategy and ignoring the rest.', 'Retrieval and spacing are the base; add the others where they fit the content.'),
        ('Judging strategies by how easy they feel.', 'The strongest strategies feel harder. Judge by scores two days or a week later.'),
    ],
)
