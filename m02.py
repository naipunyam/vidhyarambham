"""Module 2: Myths to drop."""
from common import lesson, module, link, table

M = 2

L1 = lesson(
    M, 1,
    outcome='Recognise the learning-styles myth and other brain myths, check any learning claim with three questions, and choose methods by the content instead of by "your style".',
    split='20 minutes reading, 25 minutes resources, 30 minutes action',
    core=f"""
### The learning-styles idea

You have probably heard it from a teacher, a coaching centre or a YouTube channel: everyone has a **learning style**, usually visual, auditory or kinesthetic (learning by doing), and you learn best when lessons match your style. Many people have taken a quiz that told them their type.

The idea sounds respectful and personal. The problem is that it doesn't hold up when it is tested.

### What the research found

In 2008 four psychologists, Pashler, McDaniel, Rohrer and Bjork, reviewed the evidence for the core claim: that matching teaching to a person's style improves learning. They explained what a fair test needs: people with different styles are taught with different methods, then all are tested in the same way. If the theory is right, "visual" learners should learn more from the visual lesson and "auditory" learners from the spoken one.

Very few studies used this design, and those that did mostly contradicted the theory. Their conclusion: there is no adequate evidence base to justify using learning-styles assessments in general education ({link('pashler', 'Pashler and others, 2008')}).

Two things are true and often confused with learning styles:

- **People have preferences.** You may enjoy videos more than books. Enjoyment matters for getting started, but it is not the same as learning more.
- **The content decides the best method, for everyone.** Everyone learns Kerala's districts better with a map, the order of events better with a timeline, and English pronunciation better by listening. A map helps a "verbal" learner as much as a "visual" one.

### Other brain myths

In a survey of 242 teachers in the United Kingdom and the Netherlands, Dekker and others (2012) found that 93% and 96% believed that people learn better in their preferred learning style. Around 46% to 48% believed that we use only 10% of our brain, and 86% to 91% believed that differences between left-brained and right-brained learners explain how people learn. The researchers treat all three as **neuromyths**: popular beliefs that brain science doesn't support. Surprisingly, teachers who knew more general facts about the brain believed more myths, probably because they had read more popular material ({link('dekker', 'Dekker and others, Frontiers in Psychology')}).

### Why myths matter for a PSC aspirant

Myths cost time. An "auditory learner" may spend months listening to PSC audio classes and never practise recall. A "right-brained" person may avoid maths. A believer in the 10% myth may buy an app that promises to "unlock the other 90%".

### Three questions for any learning claim

When a video, coaching centre, app or WhatsApp forward makes a claim about learning, ask:

1. **What is the evidence?** A real study compares two methods and tests learning days later, not right after.
2. **Who says so, and are they selling something?** A course, an app or a "secret method"?
3. **Does it match what reviews say?** Check it against Dunlosky's review (Module 3) and the evidence tables in this course.
""",
    example="""
**Joseph sir**, the retired Malayalam teacher who runs a study group at the Thottilpalam panchayat library, noticed that one member, Vinod, spent every evening listening to PSC audio classes on his phone while driving his autorickshaw. "I'm an auditory learner," Vinod said. "Books don't work for me."

Joseph sir suggested a fair test. For one week, Vinod learned half of a Kerala geography topic his usual way, by listening twice. The other half he learned from a map in the SCERT textbook: he looked, then drew the rivers and districts from memory and checked. Both halves got the same 40 minutes.

Two days later the group quizzed him with ten questions on each half. He scored 4 on the listened half and 8 on the map half. Vinod still listens in the autorickshaw, because it keeps him in touch with the subject, but he now follows each audio class with ten minutes of recall from a map or a blank page at home.
""",
    evidence=[
        ('Matching teaching to your learning style improves learning', 'none', 'Pashler and others (2008): the few properly designed studies mostly contradicted it.'),
        ('Choosing the method by the content (maps for places, timelines for events)', 'moderate', 'Supported by research on dual coding and concrete examples (Module 3). It helps everyone, whatever their preference.'),
        ('"We only use 10% of our brain"', 'none', 'Listed as a neuromyth by Dekker and others (2012).'),
        ('Left-brained and right-brained learners', 'none', 'Listed as a neuromyth by Dekker and others (2012).'),
    ],
    resources=[
        ('pashler', 'Read the abstract: what a fair test of learning styles needs, and what was found', '10 minutes'),
        ('dekker', 'Read the abstract and the introduction\'s description of neuromyths', '15 minutes'),
        ('ls-dual', 'Look at the dual coding poster: a method that helps everyone, not one style', '5 minutes'),
    ],
    steps=[
        'Write down what you have believed about your own learning: a style, a "type", or a subject you think you can\'t learn.',
        'Choose one PSC topic that you usually learn in your preferred way (for example, listening to classes, or only reading).',
        'Split it into two halves of similar size. Learn one half your usual way and the other half with a method that suits the content (a map for places, a timeline for history, a worked example for maths, recall practice for facts). Give each half the same time.',
        'Two days later, test both halves with 5 to 10 questions each, without looking. Score them.',
        'Find one learning claim online or on WhatsApp (an app, a "secret method", a speed-memory course) and check it with the three questions. Write your verdict in three lines.',
    ],
    proof='Your two-half test with both scores, and your three-question check of one learning claim.',
    templates=[
        ('match the method to the content', table(['Content in your PSC syllabus', 'A method that helps everyone'], [
            ('Places: districts, rivers, national parks, borders', 'A map: look, draw from memory, check'),
            ('Events and dates: renaissance, freedom struggle', 'A timeline: draw it from memory, add causes'),
            ('Processes: how a bill becomes law, the water cycle', 'A flow diagram explained aloud'),
            ('Comparisons: Lok Sabha and Rajya Sabha, rights and duties', 'A two-column table filled in from memory'),
            ('Maths and reasoning', 'Worked examples, then mixed practice'),
            ('Pronunciation and spoken English', 'Listening and shadowing'),
            ('Lists of facts: articles, awards, firsts', 'Flashcards with spaced repetition, mnemonics'),
        ]), ''),
        ('three-question claim check', """
CLAIM CHECK        Date: ______
The claim: _________________________________________________
Where I saw it: ____________________________________________
1. Evidence: is there a study that compared methods and tested days later?  yes / no / not shown
   Details: ________________________________________________
2. Who says so, and are they selling something? ______________
3. Does it agree with Dunlosky's review and this course's evidence tables? yes / no
My verdict: believe / doubt / reject.   Why: ________________
""", ''),
    ],
    mistakes=[
        ('Labelling yourself as one type of learner.', 'Your preferences are real, but they shouldn\'t limit how you study. Choose methods by the content.'),
        ('Avoiding reading because you are "visual" or "auditory".', 'PSC exams are written. Reading with recall is a skill you can build (Module 10).'),
        ('Believing a confident coach or a popular video.', 'Ask the three questions. Confidence and views are not evidence.'),
        ('Testing a method right after studying.', 'Fair tests are done days later, because short-term performance misleads.'),
    ],
    quiz=[
        {'q': 'What did Pashler and others (2008) conclude about learning styles?', 'o': ['There is no adequate evidence base for using learning-styles assessments in education', 'Visual learners learn twice as fast from pictures', 'Learning styles work only for adults', 'Everyone has exactly one learning style'], 'a': 'A', 'why': 'The few properly designed studies mostly contradicted the matching idea.'},
        {'q': 'You are learning Kerala\'s rivers. Which method helps best, whatever your preference?', 'o': ['A map that you draw from memory and check', 'Only listening to a lecture', 'Copying the list ten times', 'Highlighting the list'], 'a': 'A', 'why': 'The content (places) suits a map, and drawing from memory adds retrieval.'},
        {'q': 'In Dekker and others\' survey, who believed more neuromyths?', 'o': ['Teachers with more general knowledge about the brain', 'Teachers who knew nothing about the brain', 'Only new teachers', 'Nobody believed them'], 'a': 'A', 'why': 'General brain knowledge predicted more myth belief, probably from popular sources.'},
        {'q': 'Which is the strongest evidence for a learning method?', 'o': ['A study comparing two methods with a test days later', 'A video with a million views', 'A coaching centre\'s advertisement', 'A friend\'s recommendation'], 'a': 'A', 'why': 'Fair comparisons with delayed tests show real learning, not short-term performance.'},
    ],
    study='The abstracts of Pashler and others (2008) and Dekker and others (2012)',
    action='Test your "learning style" on a split PSC topic and check one learning claim',
)

L2 = lesson(
    M, 2,
    outcome='Drop four popular habits that waste study time (rereading, highlighting, multitasking and speed-reading tricks), and replace each with a better use of the same minutes.',
    split='20 minutes reading, 30 minutes resources, 40 minutes action across three sessions',
    core=f"""
In 2013, John Dunlosky and four colleagues reviewed the research on ten common study techniques and rated each one for how useful it is to students ({link('dunlosky-aft', 'Dunlosky, American Educator')}). Two came out on top: practice testing and spaced practice. Several of the most popular ones came out near the bottom. This lesson covers the habits to drop; Module 3 covers what to do instead.

### 1. Rereading

Rereading is the most common study method, and it was rated **low utility**. The second reading feels smooth and familiar, so you feel you know the material; that feeling is not memory. In Roediger and Karpicke's experiment (LRN-M01-L03), rereaders were the most confident and remembered the least after a week.

**Instead:** read once carefully, close the book, recall, then reread only the parts you missed.

### 2. Highlighting and underlining

Highlighting was also rated **low utility**. It is quick and looks productive, but deciding what to colour is not the same as learning it, and many students highlight half the page.

**Instead:** write a question in the margin for each important point ("Which article abolished untouchability?"). Later, cover the text and answer your own questions. If you like colours, use them after a recall, to mark what you missed.

### 3. Summarising

Writing summaries was rated low utility too, mainly because most students do it badly: they copy sentences instead of putting ideas in their own words. A summary written **from memory**, then checked, is retrieval practice and is worth doing.

### 4. Multitasking

Studying with WhatsApp, YouTube or the TV running is multitasking: your attention switches back and forth. In a Stanford study, people who multitasked heavily with media were worse at ignoring irrelevant information, at keeping items in memory organised, and at switching between tasks ({link('ophir', 'Ophir, Nass and Wagner, reported by ScienceDaily')}). Every switch costs time and accuracy, and the study session feels long while little is learned.

**Instead:** single-task blocks of 25 to 50 minutes with the phone out of the room (Module 5).

### 5. Speed-reading promises

Courses and apps promise reading at 1,000 words a minute with full understanding, "photo-reading" or flashing words one by one. A major review led by the reading scientist Keith Rayner found that there is a trade-off between speed and accuracy: when you read much faster, you understand less. Eye movements are not the bottleneck; understanding the language is. Skimming has its uses, but it loses detail. The best way to read faster is to become a better reader, through practice and vocabulary ({link('aps-speed', 'APS summary of Rayner and others, 2016')}).

**Instead:** read at a comfortable pace for study, skim only when you need the gist or a single fact (Module 10), and build vocabulary (Module 15).

### 6. A myth about notes

You may have heard that handwritten notes always beat typed notes. The famous 2014 study behind that claim was repeated with more students and the advantage did not hold up; what you write matters more than the tool ({link('ls-laptop', 'The Learning Scientists, 2019')}). Use paper or phone, whichever helps you write questions and recall.
""",
    example="""
**Ashiq** counted his Sunday as a good study day: three hours. He played a PSC class on YouTube at 1.5x speed, kept WhatsApp open on the laptop, and highlighted the class PDF as he went. On Monday a friend asked him five questions from the class. He got one.

He did the time audit from this lesson for three sessions. Over about 4 hours, he spent 52% of the time watching or rereading, 21% highlighting, 18% on the phone, and 9% answering questions. Almost nothing was recall.

For the next two sessions, on topics of the same size, he changed only the method: watch at normal speed once, pause every 10 minutes and write what he remembered, write two margin questions per page, phone in the kitchen. Each session took about the same time. The next day his friend's five-question test gave him 4 and 5 out of 5. He wrote his stop-doing list on a card and kept it inside his notebook cover.
""",
    evidence=[
        ('Rereading as your main method', 'limited', 'Rated low utility by Dunlosky and others (2013): small benefits compared with recall.'),
        ('Highlighting and underlining', 'limited', 'Rated low utility: it rarely improves test performance beyond reading alone.'),
        ('Studying while multitasking costs nothing', 'none', 'Heavy media multitaskers did worse at filtering distractions, organising memory and switching (Ophir and others, 2009).'),
        ('Speed reading several times faster with full comprehension', 'none', 'Rayner and others (2016): a trade-off between speed and understanding; eye movements are not the bottleneck.'),
        ('Handwritten notes always beat typed notes', 'limited', 'The 2014 result did not replicate (Learning Scientists, 2019). Content matters more than the tool.'),
    ],
    resources=[
        ('dunlosky-aft', 'Read the introduction and the parts on rereading, highlighting and summarisation', '20 minutes'),
        ('ophir', 'Read the whole news report on media multitasking', '5 minutes'),
        ('aps-speed', 'Read the whole news release on speed reading', '10 minutes'),
        ('ls-laptop', 'Read the blog post on laptop versus longhand notes', '10 minutes'),
    ],
    steps=[
        'For your next three normal study sessions, keep a time audit: every 10 minutes, write what you were mostly doing (reading, rereading, highlighting, watching, recalling, answering questions, explaining, or on the phone).',
        'Add up the percentages of passive time (reading again, highlighting, watching, phone) and active time (recalling, answering, explaining).',
        'Do two more sessions on topics of similar size, with the same time, but only active methods: read once, recall on a blank page, write margin questions and answer them, phone out of the room.',
        'The next day, answer 5 questions on one old-style topic and 5 on one new-style topic, without looking. Compare.',
        'Write your stop-doing list (four habits) with a do-instead for each, and keep it where you study.',
    ],
    proof='Your three-session time audit with percentages, the two next-day scores, and your stop-doing list.',
    templates=[
        ('study time audit (one line every 10 minutes)', """
Session date: ______  Topic: ______________  Total minutes: ___
Time   | Mostly doing (read / reread / highlight / watch / recall / answer / explain / phone)
0-10   | ______
10-20  | ______
20-30  | ______
30-40  | ______
40-50  | ______
50-60  | ______
Passive minutes ___ (___%)   Active minutes ___ (___%)
""", ''),
        ('stop doing, do instead', """
STOP DOING                         DO INSTEAD
1. Rereading to feel ready         Read once, close the book, recall, reread only the gaps
2. Highlighting whole pages        One margin question per key point, answered later from memory
3. Studying with WhatsApp open     25-50 minute blocks, phone in another room
4. Speed-watching or speed-reading Normal speed, pause every 10 minutes to recall
My own extra: ____________________ ____________________________________________
""", ''),
    ],
    mistakes=[
        ('Counting hours instead of recall.', 'Three hours of rereading can teach less than one hour of recall. Track what you can recall, not how long you sat.'),
        ('Watching classes at 2x speed and calling it study.', 'Speed hides how little sticks. Watch at normal speed and stop often to recall.'),
        ('Keeping the phone nearby "just for the dictionary".', 'Use a paper slip for unknown words and look them up after the block.'),
        ('Paying for speed-reading or memory "secrets".', 'No method gives several times the speed with full understanding. Spend the money on nothing; the methods in this course are free.'),
    ],
    quiz=[
        {'q': 'Which two techniques did Dunlosky and others rate most useful?', 'o': ['Practice testing and spaced practice', 'Rereading and highlighting', 'Summarising and highlighting', 'Speed reading and mind maps'], 'a': 'A', 'why': 'Practice testing and distributed practice were the only two rated high utility.'},
        {'q': 'What is a better use of time than highlighting a page?', 'o': ['Writing margin questions and answering them later from memory', 'Highlighting in two colours', 'Copying the page', 'Reading it aloud three times'], 'a': 'A', 'why': 'Questions turn the page into retrieval practice.'},
        {'q': 'What did the Stanford study find about heavy media multitaskers?', 'o': ['They were worse at ignoring irrelevant information and switching tasks', 'They were better at everything', 'They had better memories', 'They read faster'], 'a': 'A', 'why': 'Ophir, Nass and Wagner (2009) found worse filtering, memory organisation and switching.'},
        {'q': 'According to Rayner and others, what limits reading speed?', 'o': ['Understanding the language, not eye movements', 'Eye movements only', 'The size of the font', 'Whether you move your lips'], 'a': 'A', 'why': 'There is a trade-off between speed and accuracy; better readers are faster because they understand faster.'},
        {'q': 'What happened when the famous laptop-versus-longhand study was repeated?', 'o': ['The handwriting advantage did not hold up', 'Handwriting won by even more', 'Laptops won clearly', 'Nobody repeated it'], 'a': 'A', 'why': 'The replication by Morehead, Dunlosky and Rawson found no reliable advantage; what you write matters more.'},
    ],
    study='Dunlosky\'s review on rereading, highlighting and summarising, and the reports on multitasking and speed reading',
    action='Audit three study sessions, test active methods, and write your stop-doing list',
)

LESSONS = [L1, L2]

MODULE = module(
    M,
    overview="""
Drop the beliefs and habits that waste the most study time: learning styles, brain myths, rereading, highlighting, multitasking and speed-reading promises. Test them on your own PSC study and keep a stop-doing list.

Dropping a bad habit frees time for good ones. Many PSC aspirants study for long hours and get little back, not because they lack ability, but because their methods feel productive while teaching little. This short module shows what the research says about the most popular beliefs and habits, and asks you to test them yourself.

The result is a stop-doing list and one study session done entirely with active methods, the bridge to Module 3.
""",
    outcomes=[
        'Explain why the learning-styles idea is not supported and choose methods by content',
        'Name common neuromyths and check any learning claim with three questions',
        'Explain why rereading and highlighting feel useful but teach little',
        'Explain the costs of multitasking and the limits of speed reading',
        'Keep a stop-doing list with a better habit for each item',
    ],
    lessons=LESSONS,
    tools=[
        'The **three-question claim check** for any learning claim you meet',
        'The **match the method to the content** table',
        'The **study time audit** to see where your minutes go',
        'Your **stop-doing list**',
    ],
    project='My stop-doing list and one myth-free study session',
    project_steps=[
        'Finalise your stop-doing list from LRN-M02-L02, with a do-instead for each habit.',
        'Plan one 50-minute study session on your next PSC topic using only active methods: read once, recall, margin questions, phone out of the room.',
        'Run it, and at the end write how many of your margin questions you could answer from memory.',
        'Show the list and your result to a study partner or family member and explain one habit you dropped.',
    ],
    project_proof='Your stop-doing list and the notes from your myth-free session with its recall score.',
    rubric=[
        ('Myths', 'Still believe a style or myth without checking', 'Know the myths but not the evidence', 'Can explain the evidence and checked one claim'),
        ('Habits', 'No change', 'One habit changed', 'Stop-doing list in use, with do-instead habits'),
        ('Session', 'Not run', 'Run with some passive time', 'Run with only active methods and a recall score'),
    ],
    short=[
        'Read the APS speed-reading summary and the parts of Dunlosky\'s review on rereading and highlighting.',
        'Write your stop-doing list with four items and keep it where you study.',
    ],
    flashcards=[
        ('The learning-styles claim and the verdict', 'Matching teaching to your style improves learning: no adequate evidence (Pashler and others, 2008).'),
        ('Two neuromyths besides learning styles', '"We use only 10% of our brain" and left-brained versus right-brained learners.'),
        ('Dunlosky\'s rating of rereading and highlighting', 'Low utility.'),
        ('A better use of highlighting time', 'Margin questions answered later from memory.'),
        ('Effect of heavy media multitasking (Ophir and others)', 'Worse at ignoring distractions, organising memory and switching tasks.'),
        ('The speed-reading verdict', 'A trade-off between speed and understanding; get faster by becoming a better reader.'),
        ('Three questions for a learning claim', 'What is the evidence? Who says so and are they selling? Does it agree with reviews?'),
    ],
    mistakes=[
        ('Feeling guilty about past habits.', 'Most students study this way. Notice, replace, move on.'),
        ('Dropping a habit without a replacement.', 'Every stop needs a do-instead, or the old habit returns.'),
    ],
)
