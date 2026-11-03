"""Module 10: Reading."""
from common import lesson, module, link, rules, fence, table

M = 10

L1 = lesson(
    M, 1,
    outcome='Read a PSC textbook chapter with SQ3R (survey, question, read, recite, review), and compare the result with ordinary reading.',
    split='15 minutes reading, 30 minutes resources, 45 minutes action plus a 10-minute test the next day',
    core=f"""
### Reading to learn is different

Reading a story and reading a textbook chapter for an exam are different jobs. For a story, you read once, front to back. For a chapter you must remember, reading once and closing the book loses most of it within days (Module 1). **Active reading** means doing something with the text while you read, so that you remember it.

### SQ3R

**SQ3R** is a classic active-reading method, popular since the 1940s and explained in OpenStax *College Success* ({link('os-cs-5', 'chapter 5, section 5.2')}). The name stands for five steps:

1. **Survey (2 to 3 minutes):** before reading, look over the chapter: title, headings, pictures, maps, tables, the summary and the questions at the end. You are building a frame for what is coming.
2. **Question:** turn each heading into a question. "Climate of India" becomes "What controls India's climate, and how does it vary?"
3. **Read:** read **one section** at a time, looking for the answer to its question. Slow down for dense paragraphs.
4. **Recite:** close the book and answer the question aloud or on paper, in your own words. Then check.
5. **Review:** at the end of the chapter, recall all the questions without looking; then again on your revision days (Module 3).

### Why it works, honestly

SQ3R as a whole package has been studied less than you might expect, and the research on it is limited. But two of its steps are exactly the strongest methods in this course: **Recite** is retrieval practice and **Review** is spaced retrieval. The Survey and Question steps help you read with a purpose. If you only have time for one step, keep Recite.

### Reading SCERT textbooks for PSC

Many Kerala PSC aspirants build their GK on school textbooks from **SCERT Kerala**, because they are official, written for Kerala, and cover history, geography, economics, the Constitution and science step by step ({link('scert', 'SCERT Kerala')}). NCERT textbooks are another free official source ({link('ncert', 'NCERT')}). Read them with SQ3R, one chapter per session, and add margin questions instead of highlights (Module 2).

### Reading speed for textbooks

Dense textbook pages should be read slowly. Going back to reread a sentence you didn't understand is normal and useful. Fast reading belongs to skimming and scanning (next lesson), not to learning.
""",
    example="""
**Sreeja** wanted to compare SQ3R with her usual reading. She took two SCERT social science chapters of similar length.

The first she read her usual way: start to finish, with a pencil, in 35 minutes. The second she read with SQ3R: a 3-minute survey of headings, maps and the end-of-chapter questions; six headings turned into questions on a sheet; then one section at a time, closing the book after each section to answer its question aloud before checking. It took 45 minutes.

The next day she answered ten questions on each chapter without looking. Ordinary reading: 4 out of 10. SQ3R: 8 out of 10. She noticed that the recite step was the uncomfortable part, and that it was also the step that showed her, section by section, what she hadn't understood.
""",
    evidence=[
        ('SQ3R as a complete method', 'limited', 'Widely taught since the 1940s, with limited rigorous research on the whole package.'),
        ('The Recite and Review steps', 'strong', 'These are retrieval practice and spaced retrieval, both rated high utility.'),
        ('Surveying a chapter and turning headings into questions', 'limited', 'Sensible preparation that gives reading a purpose; little direct evidence on its own.'),
    ],
    resources=[
        ('os-cs-5', 'Read 5.2 Effective Reading Strategies, including SQ3R', '20 minutes'),
        ('scert', 'Find the textbook chapter you need for your PSC syllabus and download it', '10 minutes'),
        ('ncert', 'Optional: NCERT textbooks as a second official source', 'As needed'),
    ],
    steps=[
        'Choose two textbook chapters of similar length and difficulty from your PSC syllabus (SCERT or NCERT).',
        'Read the first in your usual way, and note the time taken.',
        'Read the second with SQ3R, using the sheet below: survey, questions from headings, one section at a time, recite after each section, review at the end.',
        'The next day, answer ten questions on each chapter without looking (from the end-of-chapter questions, previous papers or your own). Score both.',
        'Add the SQ3R chapter to your Revision tab and its key facts to AnkiDroid.',
    ],
    proof='Your SQ3R sheet, the times for both chapters and the two next-day scores.',
    templates=[
        ('SQ3R sheet', """
SQ3R     Chapter: ______________________  Source: ______  Date: ______
SURVEY (2-3 min): headings ___ | maps/tables ___ | summary read [ ] | end questions read [ ]
Section | Heading -> my question                       | Recite: my answer (book closed)   | Checked
1       | ____________________________________________ | _________________________________ | [ ]
2       | ____________________________________________ | _________________________________ | [ ]
3       | ____________________________________________ | _________________________________ | [ ]
4       | ____________________________________________ | _________________________________ | [ ]
5       | ____________________________________________ | _________________________________ | [ ]
REVIEW (end of chapter): questions answered from memory ___/___
Added to: Revision tab [ ]  AnkiDroid ___ cards
""", ''),
        ('heading to question patterns', """
"Climate of India"           -> What controls India's climate, and how does it vary?
"Causes of the revolt"       -> What caused the revolt, and which cause mattered most?
"Powers of the Governor"     -> What can the Governor do, and what can't they do?
"Types of soil"              -> Which soils are found where, and why there?
Pattern: WHAT + WHY/HOW + a comparison or limit
""", ''),
    ],
    mistakes=[
        ('Skipping the Recite step.', 'It is the step with the strongest evidence. Close the book after each section.'),
        ('Turning the survey into full reading.', 'Two to three minutes: headings, pictures, summary, end questions. Then stop.'),
        ('Reading several sections before reciting.', 'One section, one recite. Long stretches overload working memory.'),
        ('Highlighting instead of questioning.', 'Write a margin question; it becomes tomorrow\'s recall.'),
    ],
    quiz=[
        {'q': 'What does SQ3R stand for?', 'o': ['Survey, Question, Read, Recite, Review', 'Study, Quiz, Read, Repeat, Rest', 'Skim, Question, Reread, Recall, Rewrite', 'Survey, Quote, Read, Rewrite, Remember'], 'a': 'A', 'why': 'Five steps that make reading active.'},
        {'q': 'Which steps of SQ3R have the strongest research support?', 'o': ['Recite and Review, because they are retrieval and spaced retrieval', 'Survey and Question', 'Read only', 'None of them'], 'a': 'A', 'why': 'The package has limited research, but retrieval and spacing are rated high utility.'},
        {'q': 'How should you turn the heading "Powers of the Governor" into a question?', 'o': ['"What can the Governor do, and what can\'t they do?"', '"Governor?"', '"Read about the Governor"', '"Highlight the powers"'], 'a': 'A', 'why': 'A real question gives you something to answer while reading and reciting.'},
        {'q': 'When should you recite?', 'o': ['After each section, with the book closed', 'Only once at the end of the book', 'While reading, with the book open', 'Never; reading is enough'], 'a': 'A', 'why': 'One section, then recall, keeps the load small and shows gaps early.'},
    ],
    study='College Success 5.2 on reading strategies and SQ3R',
    action='Read one textbook chapter with SQ3R, one the usual way, and compare next-day scores',
)

L2 = lesson(
    M, 2,
    outcome='Choose between close reading, skimming and scanning, and use skimming and scanning to find PSC information fast in long sources.',
    split='15 minutes reading, 30 minutes resources, 35 minutes action',
    core=f"""
### Three reading gears

Good readers change gear depending on the job:

{table(['Gear', 'What you do', 'Use it for'], [
    ('Close reading', 'Read every sentence, slow down, recite (SQ3R)', 'Learning a chapter for the exam'),
    ('Skimming', 'Read headings, first sentences of paragraphs, summaries, bold words and pictures', 'Getting the gist; deciding what to read closely; previewing'),
    ('Scanning', 'Search for one item (a date, name, number or keyword) without reading the rest', 'Finding a specific fact: checking an answer, reading a notification'),
])}

OpenStax *College Success* describes these different kinds of reading ({link('os-cs-5', 'chapter 5, section 5.1')}).

### Skimming, honestly

Skimming is fast because it skips most of the text, so it **loses detail**. The reading research reviewed by Rayner and others found exactly this: skimming can give you the gist, but understanding drops ({link('aps-speed', 'APS, 2016')}). Use skimming to decide what to read and to preview, never as a way of learning a chapter.

### Scanning: find it fast

When you scan, you hold the target in mind (a year, a name, a keyword) and let your eyes run down the page looking for its shape. On a phone or laptop, **use the search function** in your PDF reader: it is scanning done by the computer. Search for the rarest word in your question: "Vaikom" finds more than "satyagraha".

### PSC uses for each gear

- **Checking PYQ answers:** scan your textbook or guide for the keyword, then close-read the paragraph you find.
- **Previewing a chapter:** skim it for 3 minutes before SQ3R.
- **Current affairs:** skim headlines, then close-read only the PSC-relevant items (LRN-M10-L04).
- **Reading a Kerala PSC notification:** scan for the details that matter to you (below). Getting one of them wrong can cost you an exam, so close-read those lines once you find them.

### Scanning a PSC notification

Kerala PSC notifications are long, but you need a few details. Scan for: the **post name and category number**, **qualifications**, **age limit**, **last date** to apply, the **mode of selection** (for example an OMR test), and the link to the **syllabus**. The official website lists notifications and syllabuses ({rules('psc-home', 'Kerala PSC')}). Always check details on the official notification, not in a forwarded message.
""",
    example="""
**Ashiq** had 30 previous-year questions he had answered wrongly, and he wanted to find each answer in his 300-page guide PDF and in his SCERT textbooks. The first time he tried it, he paged through looking for each one, and it took nearly two hours.

This time he scanned. For each question he picked the rarest keyword ("Aruvippuram", "quo warranto", "Eravikulam") and used the PDF reader's search on his phone. When the search found the word, he close-read the paragraph around it and wrote the answer with the page number. All 30 took 40 minutes.

He also skimmed a new economics chapter for three minutes before reading it with SQ3R, writing down the five main points he expected. After reading closely, four of his five were right, and the skim had shown him that the chapter's hardest part was a table on sectors, so he gave it extra time.
""",
    evidence=[
        ('Skimming loses detail and understanding', 'strong', 'A clear finding of the reading research reviewed by Rayner and others (2016).'),
        ('Scanning and search for specific facts', 'limited', 'A practical skill with little formal research; it saves time when you know exactly what you need.'),
        ('Choosing the reading gear to fit the purpose', 'limited', 'Standard advice in study-skills books such as College Success; judge it by time saved and scores kept.'),
    ],
    resources=[
        ('os-cs-5', 'Read 5.1 on the nature and types of reading', '15 minutes'),
        ('aps-speed', 'Reread the part on skimming', '5 minutes'),
        ('psc-home', 'Open a current notification relevant to you and practise scanning it', '10 minutes'),
    ],
    steps=[
        'Skim a new chapter for 3 minutes and write the 5 main points you expect. Then read it closely (SQ3R) and mark how many of your 5 were right.',
        'Take 10 previous-year questions whose answers you need to check. For each, scan your textbook or guide (use PDF search) with the rarest keyword, then close-read the paragraph. Time the whole job.',
        'Scan one current Kerala PSC notification for a post you might apply for, and fill in the notification checklist below.',
        'Write two lines on which gear you overuse and which you will use more.',
    ],
    proof='Your skim prediction compared with the close reading, the timed scan log for 10 questions, and the completed notification checklist.',
    templates=[
        ('which gear?', """
I need to LEARN this for the exam             -> close reading (SQ3R)
I need the GIST, or to decide what to read   -> skim: headings, first lines, summary, pictures
I need ONE FACT (date, name, number)         -> scan: rarest keyword, PDF search, then close-read that paragraph
""", ''),
        ('PSC notification scan checklist', """
Post name: ______________________   Category number: ______
Department: _____________________
Qualifications: _______________________________________________
Age limit (and relaxations that apply to me): __________________
Last date to apply: ______   Mode of selection: ______________
Syllabus link found: [ ]   Saved in 12 Exam: [ ]
I close-read each of these lines on the official notification: [ ]
""", ''),
    ],
    mistakes=[
        ('Skimming a chapter and calling it studied.', 'Skimming gives the gist only. Learn with close reading and recall.'),
        ('Scanning without a clear target.', 'Choose the rarest keyword first, then search.'),
        ('Reading every line of every source closely.', 'Switch gears: preview by skimming, find facts by scanning.'),
        ('Trusting notification details from a forward.', 'Check the official notification on the Kerala PSC website.'),
    ],
    quiz=[
        {'q': 'You need to check one date in a 300-page guide. Which gear?', 'o': ['Scanning, with the PDF search and the rarest keyword', 'Close reading of the whole guide', 'Skimming the whole guide', 'Reading the guide twice'], 'a': 'A', 'why': 'Scanning finds one specific item fast.'},
        {'q': 'What does research say about skimming?', 'o': ['It gives the gist but loses detail and understanding', 'It is the best way to learn', 'It improves comprehension', 'It doubles memory'], 'a': 'A', 'why': 'Rayner and others (2016) found understanding drops with skimming.'},
        {'q': 'Which keyword should you search to find a question about the Aruvippuram consecration?', 'o': ['"Aruvippuram"', '"temple"', '"Kerala"', '"reform"'], 'a': 'A', 'why': 'The rarest word finds the right page fastest.'},
        {'q': 'Where should you confirm the last date to apply for a PSC post?', 'o': ['On the official notification on the Kerala PSC website', 'In a WhatsApp forward', 'From a friend', 'On any coaching website'], 'a': 'A', 'why': 'Only the official notification is authoritative.'},
    ],
    study='College Success 5.1 on types of reading and the APS summary on skimming',
    action='Skim and predict a chapter, scan for 10 PYQ answers, and scan a PSC notification',
)

L3 = lesson(
    M, 3,
    outcome='Measure your reading rate and comprehension honestly, understand what limits reading speed, and start the practice that makes you a faster reader without losing understanding.',
    split='20 minutes reading, 25 minutes resources, 30 minutes action plus 15 minutes a day for four weeks',
    core=f"""
### The honest truth about speed reading

You will see apps and courses that promise reading at 1,000 words a minute or more with full understanding. A major review of reading research, led by Keith Rayner and published by the Association for Psychological Science, examined such claims ({link('aps-speed', 'APS, 2016')}). Its main findings:

- **There is a trade-off between speed and accuracy.** When you read much faster than normal, you understand and remember less.
- **Eye movements are not the bottleneck.** The limit is how fast your mind can recognise words and build meaning, not how fast your eyes move.
- **Skimming loses detail** (LRN-M10-L02).
- **The best way to read faster is to become a better reader:** read a lot, and grow your vocabulary.

So no trick will let you read a SCERT chapter in two minutes and remember it. But you **can** become a faster, better reader over months.

### What actually makes reading faster

1. **Vocabulary.** Each unknown word slows you down and breaks understanding. A vocabulary deck in AnkiDroid (Module 15) is one of the best investments for PSC English and Malayalam.
2. **Background knowledge.** The more you know about a topic, the faster you read about it, because familiar ideas take little working memory (Module 1). Your GK study makes your GK reading faster.
3. **Lots of reading practice,** in both English and Malayalam, on varied texts slightly above your comfort level.
4. **Familiarity with question language.** Reading many PSC questions makes you faster at reading new ones.

### Measure effective reading, not just speed

In week 0 you measured your **effective reading rate**: words per minute multiplied by comprehension. That number matters more than speed alone, because reading fast and understanding half gets you nothing in an exam.

{fence('''Reading speed (wpm)     = words in the passage ÷ minutes taken
Comprehension (%)       = correct answers ÷ questions × 100
Effective reading rate  = wpm × comprehension % ÷ 100
Example: 540 words in 2.5 minutes = 216 wpm; 6 of 8 right = 75%; effective rate = 162''')}

### A four-week reading practice

Fifteen minutes a day: alternate English and Malayalam. For English, the British Council's free LearnEnglish site has graded reading texts with tasks from beginner to advanced levels ({link('learnenglish', 'LearnEnglish')}). For Malayalam, read a newspaper editorial or a chapter of a Malayalam book. Once a week, time yourself on a new text and answer its questions, and log your effective reading rate.
""",
    example="""
**Anu** had once paid for a "speed reading" video course from an advertisement. After a week of flashing words on the screen, she could "read" a page in a minute and remember almost nothing, so she stopped.

In week 0 her baseline was 190 words a minute with 6 of 8 questions right: an effective rate of about 143. She started this lesson's practice: 15 minutes a day, English texts from LearnEnglish at her level on odd days and Malayalam editorials on even days, plus five new English words a day in her vocabulary deck.

After four weeks, her timed reading on a new LearnEnglish text was about 215 words a minute with 7 of 8 right: an effective rate of about 188. Her speed rose modestly; her comprehension rose more, and the combination rose by almost a third. She stopped looking for tricks.
""",
    evidence=[
        ('Speed reading several times faster with full comprehension', 'none', 'Rayner and others (2016): a speed-accuracy trade-off; eye movements are not the bottleneck.'),
        ('Vocabulary and wide reading make you a better, faster reader', 'moderate', 'The route recommended by the same review; improvement is gradual.'),
        ('Tracking effective reading rate (speed × comprehension)', 'limited', 'A practical measure for your own progress, not a research standard.'),
    ],
    resources=[
        ('aps-speed', 'Read the whole news release on the speed-reading review', '10 minutes'),
        ('learnenglish', 'Open the reading section, choose your level, and do one text with its tasks', '20 minutes'),
    ],
    steps=[
        'Choose a new reading text with questions: a LearnEnglish text at your level is ideal. Count its words (or count the words in five lines, divide by five, and multiply by the number of lines).',
        'Time yourself reading it once at normal study pace, then answer its questions without looking back. Work out wpm, comprehension and effective reading rate.',
        'Plan four weeks of 15-minute daily reading practice, alternating English and Malayalam, and write it into your study planner.',
        'Start a vocabulary list: five new words a day from your reading, added to AnkiDroid (Module 15 builds this into a full deck).',
        'Once a week, time yourself on a new text and log the results in the reading log.',
    ],
    proof='Your first timed reading with all three numbers, your four-week plan, and the reading log after the first week.',
    templates=[
        ('reading log', """
READING LOG
Date   | Text (title, language, level) | Words | Minutes | wpm | Questions right | Comprehension % | Effective rate
______ | _____________________________ | ____  | ____    | ___ | ___/___         | ___%            | ___
______ | _____________________________ | ____  | ____    | ___ | ___/___         | ___%            | ___
Week 0 baseline effective rate: ___   Target in 4 weeks: ___
""", ''),
        ('counting words quickly', """
1. Count the words in 5 full lines.
2. Divide by 5 = average words per line.
3. Count the lines in the passage.
4. Words ≈ average words per line × number of lines.
Example: 5 lines = 60 words -> 12 per line; 42 lines -> about 504 words.
""", ''),
    ],
    mistakes=[
        ('Paying for speed-reading courses or apps.', 'The research finds a speed-accuracy trade-off. Read more and build vocabulary instead.'),
        ('Measuring speed without comprehension.', 'Always answer questions and use the effective reading rate.'),
        ('Reading only easy texts.', 'Practise slightly above your comfort level, where new words appear.'),
        ('Never measuring.', 'Time yourself once a week; small gains are invisible without numbers.'),
    ],
    quiz=[
        {'q': 'According to Rayner and others (2016), what limits reading speed?', 'o': ['How fast the mind recognises words and builds meaning, not eye movements', 'How fast the eyes move', 'The size of the font', 'The colour of the paper'], 'a': 'A', 'why': 'Eye movements are not the bottleneck; understanding is.'},
        {'q': 'You read 600 words in 3 minutes and answer 6 of 8 questions correctly. What is your effective reading rate?', 'o': ['150', '200', '75', '600'], 'a': 'A', 'why': '600 ÷ 3 = 200 wpm; 6 of 8 = 75%; 200 × 0.75 = 150.'},
        {'q': 'Which is the best route to faster reading, according to the review?', 'o': ['Reading a lot and growing vocabulary', 'Flashing one word at a time', 'Moving your eyes faster', 'Reading only headings'], 'a': 'A', 'why': 'Becoming a better reader is the reliable path.'},
        {'q': 'Why does GK study make GK reading faster?', 'o': ['Background knowledge makes familiar ideas take less working memory', 'It trains eye muscles', 'It doesn\'t; reading speed is fixed', 'Because GK texts are shorter'], 'a': 'A', 'why': 'What you already know frees working memory for new information.'},
    ],
    study='The APS release on the speed-reading review and one LearnEnglish reading text',
    action='Measure your effective reading rate and start a four-week reading practice with a vocabulary list',
)

L4 = lesson(
    M, 4,
    outcome='Build a 20-minute daily current-affairs routine from free, reliable sources, and turn the news into dated notes, cards and monthly self-tests.',
    split='15 minutes reading, 30 minutes resources, 20 minutes a day for a week plus a 30-minute review',
    core=f"""
Current affairs questions appear in most Kerala PSC general papers: national and Kerala news, appointments, awards, sports, science, government schemes and international events. The trap is spending two hours a day on news and remembering little. This lesson builds a short, reliable routine.

### Reliable free sources

{table(['Source', 'What it gives you', 'Language'], [
    (link('pib', 'Press Information Bureau (PIB)'), 'Official press releases of central government ministries: schemes, appointments, events', 'English and Hindi, with regional offices'),
    (link('newsonair', 'All India Radio News'), 'National and regional news bulletins, including audio bulletins you can listen to', 'English, Hindi and others'),
    (link('prd', 'Kerala I&PRD'), 'Kerala government press releases, and the monthly e-magazines Janapadham and Kerala Calling', 'Malayalam (and some English)'),
    ('A daily newspaper', 'Wider coverage; read the family copy, the library copy, or a free e-paper where one is offered', 'English or Malayalam'),
])}

Official sources are slower and drier than YouTube channels, but they are correct. "Current affairs PDFs" and forwards are often full of errors; if you use them, check every fact against an official or reliable source.

### Find your time window

How far back do current affairs questions go in your exam? Check your saved previous papers: find the current affairs questions and see how old the events were at the time of the exam. Plan your coverage from that, not from a coaching centre's guess.

### The 20-minute daily routine

1. **Scan headlines (5 minutes):** PIB, PRD Kerala and your newspaper. Pick 2 or 3 items that PSC could ask about.
2. **Read closely (10 minutes):** only those items. Find who, what, where, when, and why it matters.
3. **Write (5 minutes):** 3 to 5 one-line facts in your current-affairs note for the month, each with the **date and source**.

### Link news to the syllabus

Each news item connects to a static topic: a new national park links to geography; a constitutional amendment to the Constitution; an award to your awards list. Write the link next to the fact ("links to: Part IX, panchayats"). This is elaboration (Module 3), and it makes both the news and the static topic easier to remember.

### Monthly review

On the last Sunday of each month: reread the month's note once, then cover it and answer 20 questions you write from it. Make cards for what you missed (within your AnkiDroid budget), and add the month to your Revision tab.
""",
    example="""
**Anu** used to watch PSC current-affairs videos for an hour every night and still struggle with current-affairs questions in mocks.

She started the 20-minute routine at 7:30 each evening. She scanned PIB's releases and the PRD Kerala press releases, picked two or three items, and wrote facts in a note called "CA 2026-11" with the date and source for each. Next to each fact she wrote its static link, such as "links to: Kerala rivers" or "links to: awards (literature)".

At the end of the first week she covered her notes and answered 15 questions she had written from them: 11 right. The four misses became cards. When she checked two recent PSC papers, she counted their current-affairs questions and found the events they asked about mostly from the previous year, so she planned her monthly reviews to cover the last 12 months.
""",
    evidence=[
        ('Monthly self-tests and spaced cards for current affairs', 'strong', 'Retrieval and spacing, rated high utility, applied to news facts.'),
        ('Linking news to static syllabus topics', 'moderate', 'A form of elaboration: connected facts are easier to remember.'),
        ('A short daily routine instead of long news sessions', 'limited', 'A practical design; judge it by your monthly self-test scores.'),
    ],
    resources=[
        ('pib', 'Explore the latest releases and find two that PSC could ask about', '10 minutes'),
        ('newsonair', 'Listen to one news bulletin and note three facts', '10 minutes'),
        ('prd', 'Find the latest Kerala press releases and the Kerala Calling e-magazine', '10 minutes'),
        ('psc-pyq', 'Count the current-affairs questions in two recent papers and note how old the events were', '15 minutes'),
    ],
    steps=[
        'Start a current-affairs note for this month (paper notebook or phone) using the template below.',
        'For 7 days, do the 20-minute routine: scan, read 2 or 3 items closely, write 3 to 5 facts with date, source and static link.',
        'On day 7, cover your notes and answer 15 questions you write from them. Make cards for the misses.',
        'Check two recent PSC papers: count the current-affairs questions and estimate their time window.',
        'Put the monthly review (last Sunday of the month) into your calendar and Loop.',
    ],
    proof='Seven days of current-affairs notes with dates, sources and links, your day-7 self-test score, and your PYQ count with the time window.',
    templates=[
        ('daily current-affairs note', """
CURRENT AFFAIRS     Month: ______
Date   | Fact (one line: who / what / where / when)            | Source        | Links to (syllabus)
______ | _____________________________________________________ | PIB / PRD / __ | __________________
______ | _____________________________________________________ | ____________  | __________________
______ | _____________________________________________________ | ____________  | __________________
""", ''),
        ('monthly current-affairs review', """
MONTHLY REVIEW     Month: ______   Date: ______ (last Sunday)
1. Reread the month's note once (10 min).
2. Cover it. Answer 20 questions written from it. Score ___/20
3. Misses -> cards (within budget): ___ cards
4. Month added to the Revision tab [ ]
5. Time window check: my exam asks about roughly the last ___ months
""", ''),
    ],
    mistakes=[
        ('Two hours of news a day.', 'Twenty focused minutes with notes and monthly tests beat hours of watching.'),
        ('Notes without dates and sources.', 'Every fact needs its date and source, so you can check it later.'),
        ('Collecting PDFs you never read.', 'A thin note you test yourself on beats a folder of unread PDFs.'),
        ('Ignoring Kerala news.', 'PRD Kerala covers state schemes and events that PSC asks about.'),
        ('Trusting forwards.', 'Check every fact against an official or reliable source.'),
    ],
    quiz=[
        {'q': 'Which source gives official press releases of central government ministries?', 'o': ['The Press Information Bureau (PIB)', 'A WhatsApp group', 'A random YouTube channel', 'A coaching centre poster'], 'a': 'A', 'why': 'PIB publishes the ministries\' releases.'},
        {'q': 'Where can you find Kerala government press releases and the Kerala Calling e-magazine?', 'o': ['The Information and Public Relations Department (PRD) website', 'The PIB website only', 'Only in paid magazines', 'Nowhere online'], 'a': 'A', 'why': 'PRD Kerala publishes state releases and e-magazines.'},
        {'q': 'How should you decide how far back to study current affairs?', 'o': ['Check how old the events were in your exam\'s previous papers', 'Study only today\'s news', 'Study ten years of news', 'Follow any coaching centre\'s guess'], 'a': 'A', 'why': 'Your own exam\'s papers show the real window.'},
        {'q': 'Why write the "links to" syllabus topic next to each fact?', 'o': ['Linking it to a static topic is elaboration, making both easier to remember', 'It looks neat', 'PSC requires it', 'It replaces revision'], 'a': 'A', 'why': 'Connected facts have more routes back in memory.'},
    ],
    study='PIB, All India Radio News, PRD Kerala and two recent PSC papers',
    action='Run the 20-minute current-affairs routine for 7 days and test yourself on day 7',
)

LESSONS = [L1, L2, L3, L4]

MODULE = module(
    M,
    overview="""
Read for learning, not just for covering pages: active reading with SQ3R, skimming and scanning when they fit, the honest truth about speed and comprehension, and a short, reliable current-affairs routine from official free sources.

Reading is where most PSC study time goes, and where most of it leaks away. This module gives you three reading gears and the judgement to choose between them, measures your effective reading rate (speed multiplied by understanding), and replaces hours of news watching with 20 minutes that you can test yourself on.

The result is a reading system: textbooks with SQ3R, facts found by scanning, a four-week reading practice and a dated current-affairs note with monthly reviews.
""",
    outcomes=[
        'Read a textbook chapter with SQ3R and recite after every section',
        'Choose close reading, skimming or scanning to fit the job',
        'Explain why speed reading doesn\'t work and measure your effective reading rate',
        'Use vocabulary and practice to read better over time',
        'Run a daily current-affairs routine from official sources with monthly self-tests',
    ],
    lessons=LESSONS,
    tools=[
        'The **SQ3R sheet** and **heading-to-question patterns**',
        'The **which gear?** guide and the **PSC notification scan checklist**',
        'The **reading log** with effective reading rate',
        'The **daily current-affairs note** and **monthly current-affairs review**',
    ],
    project='My reading system',
    project_steps=[
        'Read one more full chapter with SQ3R and test yourself on it the next day.',
        'Keep the reading log for two weeks, with at least two timed readings and their effective rates.',
        'Keep 14 days of current-affairs notes with dates, sources and links, and do a 20-question self-test on them.',
        'Write your reading rules on one card: which gear for which job, your daily reading practice, and your current-affairs routine.',
    ],
    project_proof='The SQ3R sheet and score, two weeks of the reading log, 14 days of current-affairs notes with the self-test, and your reading rules card.',
    rubric=[
        ('Active reading', 'Read and close the book', 'SQ3R with some steps skipped', 'SQ3R with recite after every section, tested next day'),
        ('Gears', 'Everything read the same way', 'Skimming or scanning used sometimes', 'Gear chosen for each job; scanning with PDF search'),
        ('Speed and comprehension', 'Not measured', 'Speed measured only', 'Effective reading rate logged and practice running'),
        ('Current affairs', 'Hours of videos, no notes', 'Notes without sources', 'Dated, sourced notes with links and a self-test'),
    ],
    short=[
        'Use only the Recite step: close the book after each section and answer from memory.',
        'Do the current-affairs routine on three days a week, with the monthly review.',
    ],
    flashcards=[
        ('SQ3R', 'Survey, Question, Read, Recite, Review.'),
        ('The strongest steps of SQ3R', 'Recite and Review: retrieval and spaced retrieval.'),
        ('Three reading gears', 'Close reading to learn, skimming for gist, scanning for one fact.'),
        ('Speed-reading verdict (Rayner and others, 2016)', 'A speed-accuracy trade-off; eye movements are not the bottleneck.'),
        ('Effective reading rate', 'Words per minute × comprehension % ÷ 100.'),
        ('Official current-affairs sources', 'PIB, All India Radio News, PRD Kerala.'),
        ('The 20-minute current-affairs routine', 'Scan headlines 5, read 2-3 items closely 10, write dated, sourced facts 5.'),
    ],
    mistakes=[
        ('Measuring reading by pages covered.', 'Measure by what you can recall and answer the next day.'),
        ('Chasing speed tricks.', 'Build vocabulary and background knowledge; speed follows slowly.'),
    ],
)
