"""Module 18: Personal knowledge management."""
from common import lesson, module, link, rules, fence, table

M = 18

L1 = lesson(
    M, 1,
    outcome='Explain how a linked-notes system works (atomic notes, links, backlinks, index notes and tags), and turn ten notes on a PSC topic into a small linked network.',
    split='20 minutes reading, 15 minutes resources, 50 minutes action',
    core=f"""
### What personal knowledge management is

**Personal knowledge management (PKM)** is a system for capturing, organising, connecting and finding what you learn, so that it builds up over years instead of being scattered across notebooks, WhatsApp messages and PDFs. People sometimes call it a "second brain". For you it means one place where your PSC notes live now, and where your notes on AI, business or a new language will live later.

### Folders versus links

Folders put each note in **one** place: "Kerala history". Real knowledge doesn't fit in one place. The Vaikom Satyagraha belongs to Kerala history, but it also connects to Gandhi's visits to Kerala, to the Temple Entry Proclamation, to Article 17 of the Constitution and to the reformers involved. **Links** let one note connect to many others, across subjects. Following those links is elaboration (Module 3): it builds the connections that make facts easier to remember and understand.

### Five building blocks

1. **Atomic notes:** one idea per note, in your own words, with a clear title, often a statement or a question ("Why the Vaikom Satyagraha mattered").
2. **Links:** in Logseq and Obsidian you link to another note by typing its title in double square brackets, like `[[Temple Entry Proclamation]]`. Other apps, including Joplin, have their own way to link notes.
3. **Backlinks:** apps such as Logseq and Obsidian show, on each note, which other notes link to it. You discover connections you didn't plan.
4. **Index notes:** one note per subject that lists and links its key notes, like a table of contents you write yourself.
5. **Tags:** for status and purpose, not for topics: `#to-review`, `#pyq`, `#weak`, `#confirmed`.

### An old idea

A famous example of linked notes on paper is the slip-box (Zettelkasten) of the German sociologist Niklas Luhmann, thousands of numbered index cards that referred to each other. You can do the same with paper index cards today; apps simply make links and search faster.

### Honest expectations

No research shows that a PKM app raises exam scores by itself. Its value is practical: everything in one place, connections you can see, and notes you can find in seconds. A beautiful note collection you never test yourself on is still forgetting with extra steps. Every important note should feed your retrieval system: cue questions, AnkiDroid cards and Revision-tab entries (Module 9).
""",
    example="""
**Anu** had notes on the Kerala renaissance in three notebooks, a PDF and her phone's gallery. For this lesson she made ten atomic notes on paper index cards, one idea per card: one card each for four reformers, three organisations, two events (the Vaikom Satyagraha and the Temple Entry Proclamation) and one for Article 17.

On each card she wrote, at the bottom, "links to:" and the titles of at least two other cards: the reformer cards linked to their organisations and events; the Temple Entry Proclamation linked to the Vaikom and Guruvayur satyagrahas and to Article 17. She made an index card, "Kerala renaissance: start here", listing all ten.

When she drew the network on one page, she saw a connection she had never noticed: three of her ten notes linked to the struggle against untouchability, which tied the history topic to the Constitution topic. She now asks one cross-subject question in every weekly review: "What does this connect to in another subject?"
""",
    evidence=[
        ('Linking new ideas to what you know (elaboration)', 'moderate', 'Elaborative interrogation and self-explanation are rated moderate utility by Dunlosky and others (2013).'),
        ('PKM apps improving exam results', 'limited', 'No research was found or checked for this course; their value is organisation and finding things.'),
        ('Collecting notes without testing yourself', 'none', 'Collecting is not learning; memory needs retrieval and spacing (Modules 3 and 4).'),
    ],
    resources=[
        ('logseq', 'Read the home page: what Logseq is for', '5 minutes'),
        ('joplin-help', 'Skim the Joplin features: notebooks, tags, search, sync', '10 minutes'),
        ('obsidian', 'Optional: if you already use Obsidian, check its current free and paid features', '5 minutes'),
    ],
    steps=[
        'Choose one PSC topic you have studied, with at least ten connected ideas.',
        'Write ten atomic notes on it (on index cards or in any notes app): one idea each, your own words, a clear title, and the source.',
        'Give every note at least two links to other notes, and at least one link to a note in a different subject.',
        'Write one index note that lists and links all ten.',
        'Draw the network of your ten notes on one page, and write the most surprising connection you found.',
    ],
    proof='Photos or screenshots of your ten linked notes and the index note, and your network drawing with the connection you found.',
    templates=[
        ('atomic note', """
TITLE: ________________________________ (one idea, as a statement or question)
In my own words (3-6 lines):
____________________________________________________________________
Key facts (-> cards): ________________________________________________
Why it matters / how it connects: _____________________________________
Links to: [[__________]]  [[__________]]  [[__________ (other subject)]]
Source: ______________ page ___     Tags: #to-review #pyq
""", ''),
        ('index note', """
INDEX: ______________ (subject or topic) - start here
Core ideas:      [[_______]]  [[_______]]  [[_______]]
People:          [[_______]]  [[_______]]
Events / dates:  [[_______]]  [[_______]]
Links to other subjects: [[_______]]  [[_______]]
Open questions: ____________________________________________
""", ''),
    ],
    mistakes=[
        ('Giant notes that hold a whole chapter.', 'One idea per note; link them together.'),
        ('Relying only on folders.', 'Add links, especially across subjects.'),
        ('Copying text into notes.', 'Write in your own words; copied notes are hard to link and hard to remember.'),
        ('Collecting without reviewing.', 'Every important note feeds cards, questions or the Revision tab.'),
    ],
    quiz=[
        {'q': 'What is an atomic note?', 'o': ['A note with one idea, in your own words, with a clear title', 'A note with a whole chapter', 'A copied paragraph', 'A note without a title'], 'a': 'A', 'why': 'Small notes can be linked and reused in many places.'},
        {'q': 'Why are links more powerful than folders?', 'o': ['One note can connect to many others, across subjects', 'Folders are not allowed', 'Links are faster to type', 'Links delete old notes'], 'a': 'A', 'why': 'Real knowledge connects across subjects; folders hold each note in one place.'},
        {'q': 'What is the honest evidence on PKM apps and exam scores?', 'o': ['No research shows they raise scores by themselves; notes still need retrieval', 'They are proven to double scores', 'They harm memory', 'They replace AnkiDroid'], 'a': 'A', 'why': 'Their value is organisation; memory still comes from retrieval and spacing.'},
        {'q': 'How do you link to a note called Temple Entry Proclamation in Logseq or Obsidian?', 'o': ['Type [[Temple Entry Proclamation]]', 'Type #Temple', 'Underline the title', 'Put it in a folder'], 'a': 'A', 'why': 'Double square brackets create a link to that note.'},
    ],
    study='The Logseq home page and the Joplin features list',
    action='Write ten atomic, linked notes on a PSC topic with an index note, and map the network',
)

L2 = lesson(
    M, 2,
    outcome='Set up a free knowledge base on your phone in Joplin or Logseq (or Obsidian if you already use it), organise it for PSC and later learning, and connect it to your review system.',
    split='15 minutes reading, 25 minutes resources, 50 minutes setup and moving notes',
    core=f"""
### Choosing a tool

All the options below are free; the first two are open source.

{table(['Tool', 'Best for', 'What you should know'], [
    ('Joplin', 'Notebooks and tags, like a tidy filing cabinet', 'Open source; Android, Windows and Linux; notes in Markdown; full-text search; sync through Dropbox, OneDrive, Nextcloud or Joplin Cloud; end-to-end encryption; works offline'),
    ('Logseq', 'Linking ideas, with a daily journal page', 'Open source (AGPL); built around [[links]] and backlinks; on Android through F-Droid'),
    ('Obsidian', 'Linking ideas, if you already use it', 'Free without limits; optional paid sync; your data stays on your device; not open source'),
    ('Paper index cards', 'No phone at all', 'Number the cards and write links as card numbers'),
])}

Sources: {link('joplin', 'Joplin')} and {link('joplin-help', 'its help pages')}; {link('logseq', 'Logseq')} and {link('logseq-fdroid', 'Logseq on F-Droid')}; {rules('obsidian', 'Obsidian pricing')}.

**If you already use one of these, keep it.** The structure and workflow below matter more than the app. If you are starting fresh, choose Joplin if you prefer notebooks, Logseq if you want links first.

### A structure for PSC and after

{fence('''Inbox            new notes waiting to be processed (24-hour rule)
Index            one index note per subject (start here)
Constitution     Kerala history     Indian history     Geography
Economics        Science            Current affairs (one note per month)
English          Malayalam          Maths and reasoning
Exam             syllabus map, 12-week plan, mock analyses
Learning system  your templates: planner, revision, card checklist, error log, Feynman, weekly review
Later            AI skills, business, a new language (one notebook or page each)''')}

Each topic note follows the atomic note template (LRN-M18-L01): your own summary, key facts, why it matters, links, source and tags.

### The workflow

1. **Capture:** anything new goes into the Inbox: class notes, a fact from the news, a question.
2. **Process within 24 hours** (Module 9): turn it into an atomic note in the right place, with links.
3. **Connect:** add at least two links, and update the subject's index note.
4. **Feed your review system:** key facts become AnkiDroid cards, the topic goes into the Revision tab, why-questions go into the note.
5. **Use it:** before a Feynman explanation, a teaching session or a mock analysis, open the topic's index note.

### Keep it safe and simple

- **Back up** once a month with the app's export option or by copying its folder to your Learning Folder, even if you also sync.
- **Don't build for weeks.** Twenty minutes of setup, then move notes in as you study. The system serves your learning, not the other way round.
- **Sources on every note,** so you can check facts later (Module 16).
""",
    example="""
**Ashiq** installed Logseq from F-Droid, because he wanted links first. He created the pages from this lesson's structure and an Inbox. His daily study notes went into Logseq's journal page for the day, then each evening he moved them into atomic topic pages with links: "[[Article 32]]" linked to "[[Writs]]", "[[Supreme Court]]" and "[[Fundamental Rights - start here]]".

In the first week he moved in 20 notes from his Cornell pages (Module 9) and his current-affairs note for the month. He added a "Learning system" page holding his six core templates, so he could copy them on his phone.

On the first Sunday of each month, Loop reminds him to back up: he exports the Logseq folder to his Learning Folder. The surprise for him was search: when a previous-year question mentioned "quo warranto", he found his own note and its links in five seconds.
""",
    evidence=[
        ('Connecting notes to cards and the Revision tab', 'strong', 'This is what turns notes into retrieval and spaced practice.'),
        ('A single, searchable place for all notes', 'limited', 'Practical value (finding and linking), not tested learning research.'),
        ('Any particular app being best', 'limited', 'No evidence favours one app; the workflow matters more.'),
    ],
    resources=[
        ('joplin', 'If you choose Joplin: install it and create the notebooks', '10 minutes'),
        ('joplin-help', 'Read about sync and encryption if you want to sync', '10 minutes'),
        ('logseq-fdroid', 'If you choose Logseq: install it from F-Droid', '10 minutes'),
        ('obsidian', 'If you already use Obsidian: check what is free and what is paid', '5 minutes'),
    ],
    steps=[
        'Choose your tool (or keep the one you already use) and install it.',
        'Create the structure: Inbox, Index, your PSC subjects, Exam, Learning system and Later.',
        'Move or process at least 20 notes into it: from your Cornell pages, your memory palace plan, your current-affairs notes and your Syllabus tab priorities. Give each note at least two links and a source.',
        'Put your six core templates (from the Toolkit page) into the Learning system notebook or page.',
        'Set a monthly backup reminder in Loop or your calendar, and do the first backup to your Learning Folder.',
    ],
    proof='Screenshots of your knowledge base structure, a topic note with its links and source, the Learning system page, and your first backup file in the Learning Folder.',
    templates=[
        ('topic note template', """
# [Topic title]
Summary (my words): ______________________________________________
Key facts -> cards: ______________________________________________
Why / how: _______________________________________________________
Links: [[______]] [[______]] [[______]]
PYQs on this topic: paper ______ Q ___ ; paper ______ Q ___
Source: ______________ page ___   Last reviewed: ______   Tags: #to-review
""", ''),
        ('monthly knowledge base check', """
MONTHLY CHECK      Month: ______
[ ] Inbox empty (everything processed or deleted)
[ ] Index notes updated for subjects studied this month
[ ] Notes without links: ___ -> linked
[ ] Notes without sources: ___ -> sources added
[ ] Backup exported to the Learning Folder
""", ''),
    ],
    mistakes=[
        ('Spending days designing the perfect system.', 'Twenty minutes of setup, then move notes in as you study.'),
        ('Notes without sources.', 'Every note gets a source, so facts can be checked.'),
        ('No backup.', 'Export once a month to your Learning Folder, even if you sync.'),
        ('Switching apps every month.', 'Choose one, use it for three months, then decide.'),
    ],
    quiz=[
        {'q': 'Which of these tools is open source?', 'o': ['Joplin and Logseq', 'Only Obsidian', 'None of them', 'Only paper cards'], 'a': 'A', 'why': 'Joplin and Logseq are open source; Obsidian is free but not open source.'},
        {'q': 'Where do new notes go first in the workflow?', 'o': ['The Inbox, to be processed within 24 hours', 'Straight into AnkiDroid', 'Nowhere; keep them in your head', 'The Exam notebook'], 'a': 'A', 'why': 'Capture first, then process, connect and feed the review system.'},
        {'q': 'How often should you back up your knowledge base?', 'o': ['At least once a month, to your Learning Folder', 'Never, if it syncs', 'Once a year', 'Only when the phone breaks'], 'a': 'A', 'why': 'Sync is not a backup; a monthly export protects your notes.'},
        {'q': 'You already use Obsidian. What does the lesson suggest?', 'o': ['Keep it; the structure and workflow matter more than the app', 'Delete it and switch at once', 'Use three apps at the same time', 'Stop taking notes'], 'a': 'A', 'why': 'No app is proven best; consistency matters.'},
    ],
    study='The help pages of the tool you choose (Joplin, Logseq or Obsidian)',
    action='Set up your PSC knowledge base, move in 20 linked notes and make your first backup',
)

LESSONS = [L1, L2]

MODULE = module(
    M,
    overview="""
Build a personal knowledge base that grows with you: atomic notes, links across subjects, index notes and a simple workflow, in a free app on your phone (Joplin or Logseq, both open source, or Obsidian if you already use it), connected to your review system.

Your PSC preparation produces hundreds of notes. Without a system they end up scattered and unused. With one, every note has a home, connects to related ideas, and feeds your cards and revision schedule. The same knowledge base then carries everything you learn after PSC.

This module is honest that apps don't raise scores by themselves. The point is a single searchable place where notes are connected and turned into retrieval practice.
""",
    outcomes=[
        'Explain atomic notes, links, backlinks, index notes and tags',
        'Write linked notes across subjects and find connections',
        'Choose and set up a free knowledge-base app on your phone',
        'Run the capture, process, connect, review, use workflow',
        'Keep the knowledge base backed up and tidy with a monthly check',
    ],
    lessons=LESSONS,
    tools=[
        'The **atomic note** and **index note** templates',
        'The **topic note template** and your **knowledge base structure**',
        'The **monthly knowledge base check**',
    ],
    project='My knowledge base',
    project_steps=[
        'Grow your knowledge base to at least 30 notes, each with a source and at least two links.',
        'Write an index note for every subject you have studied so far.',
        'Use the knowledge base in one real task: preparing a Feynman explanation, a teaching session (Module 20) or a mock analysis.',
        'Do the monthly check and a backup.',
    ],
    project_proof='Screenshots showing 30 or more linked notes, your index notes, notes from the real task, and the monthly check with the backup file.',
    rubric=[
        ('Notes', 'Long copied notes', 'Some atomic notes', '30 or more atomic notes in my own words, with sources'),
        ('Links', 'Folders only', 'Some links within a subject', 'At least two links per note, including across subjects'),
        ('Workflow', 'Notes added and forgotten', 'Processed sometimes', 'Inbox processed within 24 hours; facts feed cards and the Revision tab'),
        ('Safety', 'No backup', 'Synced only', 'Monthly export to the Learning Folder'),
    ],
    short=[
        'Use paper index cards with numbers and "links to" lines.',
        'Keep one index note per subject and process your inbox once a week.',
    ],
    flashcards=[
        ('Personal knowledge management', 'A system for capturing, organising, connecting and finding what you learn.'),
        ('Atomic note', 'One idea, your own words, a clear title, a source.'),
        ('Backlinks', 'A list, on each note, of other notes that link to it.'),
        ('Index note', 'One note per subject that lists and links its key notes.'),
        ('Open-source knowledge base apps in this course', 'Joplin and Logseq.'),
        ('The workflow', 'Capture, process (24 hours), connect, feed the review system, use.'),
        ('Why back up even if you sync', 'Sync copies mistakes too; a monthly export protects your notes.'),
    ],
    mistakes=[
        ('Treating the knowledge base as the goal.', 'It serves your learning; retrieval still does the remembering.'),
        ('Building a perfect system before using it.', 'Start small and improve it in your monthly check.'),
    ],
)
