"""Module 9: Note-making that leads to recall."""
from common import lesson, module, link, fence, table

M = 9

L1 = lesson(
    M, 1,
    outcome='Make Cornell notes and outlines from PSC sources in your own words, and use the cue column as a recall test.',
    split='20 minutes reading, 30 minutes resources, 40 minutes action plus a 10-minute check the next day',
    core=f"""
### Note-taking versus note-making

**Note-taking** often means copying: lines from the textbook, everything the teacher says, whole paragraphs from a PDF. It feels productive and keeps you busy, but copying needs little thinking. **Note-making** means processing: choosing what matters, putting it in your own words, and preparing it for recall later.

The test of good notes is simple: **can you use them to recall and answer questions?** Not: are they long, neat or colourful?

### The Cornell method

The Cornell method was developed by Walter Pauk, an education professor at Cornell University, and described in his book *How to Study in College* ({link('cornell-lsc', 'Cornell Learning Strategies Center')}). OpenStax's *College Success* explains it in its note-taking section ({link('os-cs-5', 'chapter 5')}). Divide each page into three parts:

{fence('''+-----------+-------------------------------------+
| CUE       | NOTES                               |
| column    | (about two-thirds of the width)     |
| (about    |                                     |
| 6 cm)     | Key points in your own words,       |
| questions | short phrases, abbreviations,       |
| and       | small diagrams                      |
| keywords  |                                     |
+-----------+-------------------------------------+
| SUMMARY (bottom 5 cm): 2-3 sentences in your    |
| own words, written after the notes              |
+-------------------------------------------------+''')}

The method is often summarised in five steps:

1. **Record:** while reading or listening, write key points in the notes column, in your own words.
2. **Reduce:** soon after, write questions or keywords in the cue column for each key point.
3. **Recite:** cover the notes column and answer the cue questions from memory. This is the step that matters most: it is retrieval practice.
4. **Reflect:** write the summary at the bottom and link the page to what you already know.
5. **Review:** come back to the cue column on your revision days (Module 3).

### Outlines

An **outline** arranges notes as headings and sub-points, like the structure of a textbook. It suits subjects with a clear hierarchy, such as the Constitution (Parts, Articles, clauses) or a geography chapter (physical features, climate, soils, forests). Write outline headings as questions where you can, so the outline doubles as a recall test.

### Paper or phone?

The famous claim that handwritten notes beat typed ones did not hold up when the study was repeated; what you write matters more than how ({link('ls-laptop', 'The Learning Scientists, 2019')}). Use paper for Cornell pages and diagrams if you prefer, or Joplin on the phone or laptop (Module 18). Either way: your own words, few words, and questions you will answer later.

### Notes from video classes

Pause the video every 5 to 10 minutes and write the key points from memory, then rewind to check. Never try to write everything the teacher says.
""",
    example="""
**Sreeja** used to copy her guide's page on Fundamental Duties into a notebook, word for word: two pages, neat handwriting, nothing remembered a week later.

This time she made one Cornell page. In the notes column she wrote short phrases in her own words: "Article 51A, Part IVA. Added by 42nd Amendment, 1976, on the Swaran Singh Committee's recommendation. 10 duties at first; 11th added by 86th Amendment, 2002: parents or guardians to give children aged 6 to 14 opportunities for education. Not enforceable in court." In the cue column she wrote questions: "Which article? Which amendment added them? Which committee? How many at first? What did the 86th add?"

The next morning she covered the notes column and answered the cue questions aloud: 6 out of 7. At the bottom she had written her summary: "Duties were added in 1976 and expanded in 2002; they guide citizens but can't be enforced like rights." The page took 25 minutes instead of 50.
""",
    evidence=[
        ('Answering cue-column questions with the notes covered', 'strong', 'This is retrieval practice, rated high utility by Dunlosky and others (2013).'),
        ('The Cornell layout itself', 'limited', 'Widely taught, with little direct research; its value comes mostly from the questions and the recall step.'),
        ('Handwritten notes always beat typed notes', 'limited', 'The well-known result did not replicate (Learning Scientists, 2019). Content matters more than the tool.'),
    ],
    resources=[
        ('os-cs-5', 'Read 5.3 on taking notes, including the Cornell method', '25 minutes'),
        ('cornell-lsc', 'Look at the Cornell Learning Strategies Center page on the method (it claims handwriting is better; see the next link)', '5 minutes'),
        ('ls-laptop', 'Reread why the handwriting-versus-laptop claim is doubtful', '5 minutes'),
    ],
    steps=[
        'Choose one PSC chapter or section you haven\'t made notes on yet.',
        'Make 2 or 3 Cornell pages on it: key points in your own words in the notes column (no copying of whole sentences).',
        'Within the same day, write a question or keyword in the cue column for every key point, and write a 2 to 3 sentence summary at the bottom of each page.',
        'The next day, cover the notes column and answer every cue question aloud from memory. Score yourself and mark misses.',
        'Make a short outline of a different section, with headings written as questions, and compare which format suited that content better.',
    ],
    proof='Photos of your Cornell pages and outline, and your next-day cue-column score.',
    templates=[
        ('Cornell page checklist', """
[ ] Line drawn: cue column about 6 cm on the left; summary space 5 cm at the bottom
[ ] Notes column: key points in MY words, short phrases, small diagrams
[ ] Cue column: one question or keyword per key point (written the same day)
[ ] Summary: 2-3 sentences, written without looking at the source
[ ] Next day: notes covered, cue questions answered aloud. Score ___/___
[ ] Misses added to: AnkiDroid / Revision tab / margin questions
""", ''),
        ('outline with question headings', """
TOPIC: ________________________ (source ______ page ___)
1. What is ______________?
   a. ______________________
   b. ______________________
2. Why / how ______________?
   a. ______________________
3. How is ______ different from ______?
   a. ______________________
Recall test: cover everything except the headings and answer them.
""", ''),
    ],
    mistakes=[
        ('Copying the textbook into a notebook.', 'Write key points in your own words, in short phrases.'),
        ('An empty cue column.', 'The questions are the point. Write them the same day.'),
        ('Never covering the notes to recall.', 'Without the recall step, Cornell notes are just tidy copying.'),
        ('Spending time on colours and neatness.', 'Judge notes by what you can recall from them, not by how they look.'),
    ],
    quiz=[
        {'q': 'Which step of the Cornell method matters most for memory?', 'o': ['Covering the notes and answering the cue questions from memory', 'Drawing the lines neatly', 'Using three colours', 'Copying the textbook exactly'], 'a': 'A', 'why': 'Reciting from the cues is retrieval practice.'},
        {'q': 'What goes in the cue column?', 'o': ['Questions or keywords for each key point', 'The full text of the chapter', 'The page numbers only', 'Nothing; it stays empty'], 'a': 'A', 'why': 'They turn the page into a recall test.'},
        {'q': 'What happened when the handwriting-beats-laptop study was repeated?', 'o': ['The advantage did not hold up; content matters more', 'Handwriting won by more', 'Laptops won clearly', 'It was never repeated'], 'a': 'A', 'why': 'Morehead, Dunlosky and Rawson (2019) did not find a reliable advantage.'},
        {'q': 'How should you take notes from a video class?', 'o': ['Pause every 5 to 10 minutes, write key points from memory, then check', 'Write everything the teacher says', 'Take no notes at all', 'Watch at double speed and note the slides'], 'a': 'A', 'why': 'Recalling at pauses turns watching into retrieval.'},
    ],
    study='College Success 5.3 on the Cornell method and the Learning Scientists post on handwriting and laptops',
    action='Make Cornell notes on a PSC chapter, test yourself from the cue column the next day, and try an outline',
)

L2 = lesson(
    M, 2,
    outcome='Make mind maps and simple sketchnotes for PSC topics where structure and pictures help, drawing them from memory and checking them.',
    split='15 minutes reading, 20 minutes resources, 50 minutes action plus a 10-minute redraw the next day',
    core=f"""
### Mind maps

A **mind map** puts the main topic in the centre of a page, with branches for its subtopics and smaller branches for details: keywords, not sentences, and small pictures where they help. It shows the **shape of a whole chapter** on one page.

Mind maps and concept maps look similar but do different jobs. A mind map is a tree that branches out from one centre; a concept map (LRN-M08-L03) is a network with labelled links between any ideas. Use mind maps for overview and revision; use concept maps when the relationships themselves are what you must understand.

Good uses for PSC:

- **A one-page overview of a chapter** before you study it in detail, and again before the exam
- **Revision:** one mind map per chapter, drawn from memory, is a fast way to check what you remember
- **Linking subtopics:** seeing that rivers, soils and crops all depend on the same three regions of Kerala

### Sketchnotes

**Sketchnotes** mix words with simple drawings: boxes, arrows, icons and small figures. They apply dual coding (Module 3) to your own notes. You don't need drawing skills. A stick figure, a box, an arrow and a dozen simple icons are enough. Build a small "visual vocabulary" of icons you reuse: a person, a building, a rupee sign, a scale for law, a calendar, a map pin, a factory, a book, a water drop, a flag.

### What the evidence says

Mind maps and sketchnotes have **little direct research**, and the claims made for them online are often exaggerated. They rest on two principles that are well supported: combining words with meaningful pictures (dual coding) and, when you draw them from memory, retrieval. So the rule from Module 8 applies again: **draw from memory, then check**. A beautiful mind map copied from a book is decoration.

### When not to use them

- **Detailed facts** (articles, dates, award winners): cards and mnemonics are better.
- **Maths and reasoning:** practise problems instead.
- **When drawing takes longer than learning.** If you spend 40 minutes colouring, switch to Cornell notes.
""",
    example="""
**Ashiq** drew a mind map of Kerala geography from memory, with "Kerala" in the centre and six branches: physical divisions, rivers, climate, soils, forests and wildlife, and minerals. Under physical divisions he drew the three regions taught in his SCERT textbook: highland, midland and lowland, each with a tiny icon (a mountain, gentle hills, waves).

When he checked against the textbook, he had left out an entire branch for agriculture and put two facts under the wrong region. He fixed them in red. The next morning he redrew the map from memory in 8 minutes, with all seven branches and no misplaced facts.

He also tried a sketchnote of a 25-minute video class on the Indian economy: boxes for sectors, a rupee icon for income, arrows for flows. Watching his own sketchnote the next day brought back the class better than his old line-by-line notes, but it took him longer to make, so he uses sketchnotes only for classes with lots of processes.
""",
    evidence=[
        ('Mind maps and sketchnotes as such', 'limited', 'Little direct research, and online claims are often exaggerated.'),
        ('Meaningful pictures combined with words (dual coding)', 'moderate', 'One of the six strategies in Module 3.'),
        ('Drawing a map from memory, then checking', 'moderate', 'It turns the map into retrieval with feedback.'),
    ],
    resources=[
        ('ls-dual', 'Read the dual coding blog post and keep the poster beside your notebook', '15 minutes'),
        ('karpicke-blunt', 'Reminder: maps made with the book open lost to retrieval practice', '5 minutes'),
    ],
    steps=[
        'Choose a whole PSC chapter you have studied. Draw a one-page mind map of it from memory, with the topic in the centre and keywords on the branches (15 minutes).',
        'Check against the source. Add missing branches and fix misplaced facts in another colour.',
        'Draw your visual vocabulary: 10 simple icons you will reuse in notes.',
        'Make a sketchnote of one PSC class, video or chapter section (20 to 30 minutes of material), using at least five of your icons.',
        'The next day, redraw the mind map from memory and compare with your corrected version.',
    ],
    proof='Your corrected mind map, the next-day redraw, your 10-icon visual vocabulary and the sketchnote.',
    templates=[
        ('mind map from memory, steps', """
1. Centre: the chapter's topic, with a small picture.
2. Main branches: the chapter's 4-7 subtopics, from memory.
3. Smaller branches: keywords only (no sentences), small icons where they help.
4. Check against the source; fix and add in another colour.
5. Next day: redraw from memory. Branches right ___/___  details right ___/___
""", ''),
        ('visual vocabulary (draw your own version of each)', """
person (stick figure)   building (institution)   rupee sign (money, economy)
scale (law, courts)     calendar (date, year)    map pin (place)
factory (industry)      book (literature)        water drop (rivers, rain)
flag (nation, state)    arrow (cause, flow)      box (group, category)
""", ''),
    ],
    mistakes=[
        ('Spending more time on art than on content.', 'Simple icons, few colours. If it takes longer than learning, switch methods.'),
        ('Copying a mind map from a book or the internet.', 'Draw from memory, then check; copying is decoration.'),
        ('Sentences on branches.', 'Keywords only. Sentences turn a map into crowded notes.'),
        ('Using mind maps for lists of dates and articles.', 'Use cards and mnemonics for detailed facts.'),
    ],
    quiz=[
        {'q': 'How does a mind map differ from a concept map?', 'o': ['A mind map branches out from one centre; a concept map links ideas with labelled arrows', 'They are exactly the same', 'A mind map has no keywords', 'A concept map has no boxes'], 'a': 'A', 'why': 'Use mind maps for overview and concept maps for relationships.'},
        {'q': 'What is the honest evidence position on mind maps?', 'o': ['Little direct research; they work through dual coding and retrieval when drawn from memory', 'Proven to double memory', 'Proven harmful', 'Only for visual learners'], 'a': 'A', 'why': 'The principles behind them are supported; the method itself is less tested.'},
        {'q': 'Which PSC content is least suited to a mind map?', 'o': ['A list of article numbers and their exact contents', 'An overview of a geography chapter', 'Revision of a history chapter\'s main themes', 'Linking subtopics of a chapter'], 'a': 'A', 'why': 'Detailed facts suit cards and mnemonics.'},
        {'q': 'What is a visual vocabulary?', 'o': ['A small set of simple icons you reuse in your notes', 'A dictionary of English words', 'A collection of photos', 'A list of colours'], 'a': 'A', 'why': 'Reusable icons make sketchnotes fast without drawing skills.'},
    ],
    study='The Learning Scientists\' dual coding post, with the Karpicke and Blunt reminder',
    action='Draw a chapter mind map from memory, make a sketchnote, and redraw the map the next day',
)

L3 = lesson(
    M, 3,
    outcome='Turn every page of notes into questions, flashcards and Revision-tab entries within 24 hours, so your notes become recall practice.',
    split='15 minutes reading, 15 minutes resources, 15 minutes a day for 5 days plus a 20-minute test on day 6',
    core=f"""
Notes are a means, not the product. A notebook full of good notes that you never test yourself on is a slow way to forget. This lesson connects your notes to the rest of your system.

### The 24-hour rule

Process today's notes **within 24 hours**, before the forgetting curve (Module 1) takes most of them. Processing takes about 15 minutes a day:

1. **Mark the key points** on today's pages.
2. **Write a question** for each in the cue column or margin.
3. **Facts become AnkiDroid cards,** following the card-writing checklist (Module 4).
4. **Reasons and processes become why-questions** or go on your Feynman list (Module 8).
5. **The topic goes into the Revision tab** with today's date (Module 3).
6. **Mistakes go into the error log** (Module 12).

### What becomes what

{table(['In your notes', 'Becomes', 'Where'], [
    ('A single fact (date, name, article, place)', 'A Basic or cloze card', 'AnkiDroid'),
    ('A list (rivers, awards, duties)', 'One cloze per item, or a memory palace', 'AnkiDroid or Module 11'),
    ('A map or diagram', 'An image occlusion note', 'AnkiDroid'),
    ('A cause, reason or process', 'A why or how question; a Feynman topic', 'Cue column; Feynman list'),
    ('Two similar things', 'A comparison table and a contrast card', 'Notes and AnkiDroid'),
    ('A whole topic', 'A row with review dates', 'Revision tab'),
    ('A maths method', 'A worked example plus a first-principles card', 'Notes and AnkiDroid'),
])}

### Don't drown in cards

Only facts that are on your syllabus or in previous papers become cards, and new cards stay within your daily budget (LRN-M04-L04). If processing produces 40 new cards a day, you are carding too much: keep the facts that matter and let the rest live in your notes and the Revision tab.

### Notes in your knowledge base later

From Module 18, processed notes can live in Joplin or Logseq, linked to each other. The processing routine stays the same.
""",
    example="""
**Anu** attends a PSC coaching class two evenings a week and studies her guide on the other days. She used to fill a notebook and look at it again only before exams.

For five days she processed each day's notes before her morning AnkiDroid reviews, using the 24-hour rule. A typical day: three pages of notes became 9 new cards (within her budget of 12), 6 margin questions, 1 Revision-tab entry and 1 topic for her Feynman list. It took 12 to 18 minutes.

On day 6 she tested herself with 20 questions drawn from all five days, without looking: 16 right. On an older, unprocessed set of notes from the previous month, the same kind of test gave 7. She now writes "P" at the top of each page once it is processed, and a page without a P is her first job the next morning.
""",
    evidence=[
        ('Turning notes into questions and cards you answer later', 'strong', 'It turns notes into retrieval practice, rated high utility.'),
        ('Processing notes within 24 hours', 'limited', 'A practical rule consistent with the forgetting curve; no direct study of the 24-hour cut-off.'),
        ('Keeping new cards within a daily budget', 'moderate', 'The Anki manual\'s workload rule: new cards drive future reviews.'),
    ],
    resources=[
        ('anki-edit', 'Refresh the cloze and image occlusion steps you will use when processing', '10 minutes'),
        ('sm-20rules', 'Reread rules 4, 9 and 10 (minimum information, avoid sets, avoid enumerations)', '10 minutes'),
        ('os-cs-6', 'Read 6.2 Studying, with an eye to how notes are used after class', '10 minutes'),
    ],
    steps=[
        'For the next five study days, process each day\'s notes within 24 hours using the six steps, in about 15 minutes.',
        'Each day, log what the processing produced: cards, questions, Revision-tab entries, Feynman topics.',
        'Keep new cards within your daily budget; let extra facts stay in your notes.',
        'Mark each processed page with a P at the top.',
        'On day 6, test yourself with 20 questions drawn from all five days, without looking. Score it.',
    ],
    proof='Photos of two processed note pages, your five-day processing log, your AnkiDroid card count before and after, and the day-6 score.',
    templates=[
        ('daily note-processing routine (15 minutes)', """
NOTE PROCESSING      Date: ______   Pages: ___
[ ] 1. Key points marked
[ ] 2. A question for each key point (cue column or margin)
[ ] 3. Facts -> cards (checklist!)      new cards today: ___ (budget ___)
[ ] 4. Reasons and processes -> why-questions / Feynman list: _____________
[ ] 5. Topic -> Revision tab (first-studied date = today)
[ ] 6. Mistakes -> error log
[ ] Page marked P
""", ''),
        ('five-day processing log', """
Day | Pages | Cards | Questions | Revision entries | Feynman topics | Minutes
1   | ___   | ___   | ___       | ___              | ___            | ___
2   | ___   | ___   | ___       | ___              | ___            | ___
3   | ___   | ___   | ___       | ___              | ___            | ___
4   | ___   | ___   | ___       | ___              | ___            | ___
5   | ___   | ___   | ___       | ___              | ___            | ___
Day-6 test (20 questions from all five days): ___/20
""", ''),
    ],
    mistakes=[
        ('Processing notes weeks later.', 'By then most of it is forgotten. Process within 24 hours.'),
        ('Making a card of every line.', 'Card only syllabus facts, within your budget; the rest stays in notes.'),
        ('Writing questions without answers in your notes.', 'Every question must be answerable from your notes or source, so you can check.'),
        ('Never reopening processed pages.', 'The Revision tab brings each topic back; follow it.'),
    ],
    quiz=[
        {'q': 'What is the 24-hour rule?', 'o': ['Process today\'s notes into questions, cards and revision entries within a day', 'Study for 24 hours before an exam', 'Wait 24 hours before taking notes', 'Rewrite notes every 24 hours'], 'a': 'A', 'why': 'Processing before most is forgotten turns notes into recall practice.'},
        {'q': 'Your notes contain a list of Kerala\'s east-flowing rivers. What should it become?', 'o': ['One cloze per river, or a memory palace', 'One card asking for the whole list', 'A long paragraph', 'Nothing'], 'a': 'A', 'why': 'Lists are split so each item is recalled on its own.'},
        {'q': 'Processing produces 40 new cards a day. What should you do?', 'o': ['Card only syllabus facts within your budget and leave the rest in notes', 'Add all 40 every day', 'Stop using AnkiDroid', 'Double the budget'], 'a': 'A', 'why': 'New cards drive future reviews; too many leads to backlog.'},
        {'q': 'A cause-and-effect explanation in your notes should become...', 'o': ['A why-question or a Feynman topic', 'A single fact card', 'An image occlusion note', 'A highlight'], 'a': 'A', 'why': 'Reasons are best tested by explaining them.'},
    ],
    study='The Anki cloze refresher, Wozniak\'s rules on lists and College Success 6.2',
    action='Process five days of notes within 24 hours each and test yourself on day 6',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    M,
    overview="""
Make notes that lead to recall: Cornell notes and outlines, mind maps and sketchnotes, and a daily routine that turns every note page into questions, flashcards and revision entries within 24 hours.

Most PSC aspirants have notebooks full of copied text. This module changes notes from a record into a tool: short, in your own words, with questions you answer later. It is honest that the famous formats (Cornell, mind maps, sketchnotes) have little direct research; they work when they lead to retrieval, and the lessons make sure they do.

The result is a note-to-recall pipeline: what you write today becomes tomorrow's practice.
""",
    outcomes=[
        'Make Cornell notes and outlines in your own words, with cue questions',
        'Draw mind maps and sketchnotes from memory and check them',
        'Choose a note format that suits the content',
        'Process each day\'s notes into cards, questions and Revision-tab entries within 24 hours',
        'Measure your notes by what you can recall from them',
    ],
    lessons=LESSONS,
    tools=[
        'The **Cornell page checklist** and **outline with question headings**',
        'The **mind map from memory** steps and your **visual vocabulary**',
        'The **daily note-processing routine** and the **what becomes what** table',
    ],
    project='My note-to-recall pipeline',
    project_steps=[
        'For one week, make all your PSC notes as Cornell pages or question outlines.',
        'Process each day\'s notes within 24 hours, logging what each day produced.',
        'Draw one chapter mind map from memory and check it.',
        'At the end of the week, take a 20-question test on the week\'s notes without looking, and compare with a similar test on old, unprocessed notes.',
    ],
    project_proof='Photos of a week of processed notes, the processing log, your mind map and both test scores.',
    rubric=[
        ('Own words', 'Mostly copied', 'Mixed', 'Short phrases in my own words throughout'),
        ('Questions', 'No cue questions', 'Some pages with questions', 'Every key point has a question, answered the next day'),
        ('Processing', 'Notes left as they are', 'Processed sometimes', 'Processed within 24 hours every day, cards within budget'),
        ('Measured result', 'No test', 'Tested once', 'Tested and compared with unprocessed notes'),
    ],
    short=[
        'Use only the cue column: add questions to your existing notes and answer them the next day.',
        'Process notes on three days of the week instead of every day.',
    ],
    flashcards=[
        ('Note-taking versus note-making', 'Copying versus processing: choosing, own words, questions for recall.'),
        ('The three parts of a Cornell page', 'Notes column, cue column (questions), summary at the bottom.'),
        ('The step of Cornell notes that matters most', 'Covering the notes and answering the cue questions from memory.'),
        ('Mind map versus concept map', 'Mind map: branches from one centre. Concept map: labelled links between ideas.'),
        ('Rule for mind maps and sketchnotes', 'Draw from memory, then check.'),
        ('The 24-hour rule', 'Process today\'s notes into cards, questions and revision entries within a day.'),
        ('What a list in your notes becomes', 'One cloze per item, or a memory palace.'),
    ],
    mistakes=[
        ('Judging notes by length or neatness.', 'Judge them by what you can recall a week later.'),
        ('Keeping notes and cards in separate worlds.', 'The processing routine connects them every day.'),
    ],
)
