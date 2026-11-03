"""Module 4: Spaced repetition from zero with AnkiDroid."""
from common import lesson, module, link, fence, table
import tools

M = 4

L1 = lesson(
    M, 1,
    outcome='Explain how spaced repetition decides when you see each card, set up AnkiDroid for one PSC topic, take a 20-question pre-test, and make your first 15 cards.',
    split='20 minutes reading, 30 minutes resources, 40 minutes setup and cards',
    core=f"""
### What spaced repetition does

In Module 3 you scheduled whole topics by hand. For single facts (who, when, which article, which river) there are far too many to schedule by hand. **Spaced repetition software** does it for you. Each fact is a flashcard. When you review a card, you say how well you recalled it, and the software decides when to show it next: soon if you struggled, much later if it was easy. Each card comes back just as you are about to forget it, which is when a successful recall strengthens memory most (Module 1).

The idea is older than smartphones. Nicky Case's comic shows the **Leitner box**: cards move forward through boxes that are reviewed less and less often, and back to box 1 when you forget them ({link('ncase', 'How To Remember Anything Forever-ish')}). Software does the same with exact dates.

### AnkiDroid

**AnkiDroid** is the free, open-source Android version of Anki, one of the most widely used spaced repetition programs ({link('ankidroid-play', 'Google Play')}; {link('ankidroid-gh', 'source code and other downloads')}). Anki for computers is also free, and a free AnkiWeb account can sync your phone and laptop ({link('anki-apps', 'Anki downloads')}).

A few words from the Anki manual ({link('anki-start', 'Getting Started')}):

- A **note** is the information you type in. A **card** is one question-and-answer that Anki shows you. One note can make several cards.
- A **deck** is a group of cards. Use `::` for sub-decks, such as `PSC::Constitution::Fundamental Rights`.
- **Note types** decide which cards a note makes. You will use four: **Basic** (one card), **Basic (and reversed card)** (two cards, both directions), **Cloze** (hides words in a sentence) and **Image Occlusion** (hides parts of a picture).
- A card is **young** until its gap reaches 21 days, then **mature**.

### The four answer buttons

After you try to recall, you reveal the answer and press one button ({link('anki-study', 'Anki manual: Studying')}):

- **Again:** you forgot or got it wrong. The card comes back soon.
- **Hard:** you got it, with real difficulty.
- **Good:** you got it with some effort. Use this for most correct answers.
- **Easy:** it was too easy. The gap grows a lot.

If you can't recall the answer in about 10 seconds, reveal it and press Again. Be honest: pressing Good when you were wrong only fools the schedule.

### Choose your 100-card topic

The course asks you to build one deck of 100 or more well-made cards on **one PSC topic** and review it every day for 30 days. Choose a topic that:

- **Appears in your syllabus and in previous papers** (look at the three papers you saved in week 0)
- **Is rich in facts:** the Constitution (Fundamental Rights, Directive Principles, amendments, schedules), the Kerala renaissance, Kerala geography, awards and firsts, English idioms, Malayalam synonyms and antonyms
- **You actually need,** not one you already know well

Before you make any cards, take a **20-question pre-test** on the topic from previous papers or your guide, without looking anything up. You'll take a similar test on day 30, and the difference will show what the deck did.
""",
    example="""
**Ashiq** chose the Fundamental Rights (Articles 12 to 35) for his deck: they appear in almost every general PSC paper, and he kept mixing up the article numbers.

He picked 20 questions on the topic from previous papers and his guide and took the pre-test cold: 9 out of 20. Then he installed AnkiDroid from Google Play, made a deck called `PSC::Constitution::Fundamental Rights`, and set **New cards/day** to 15 in the deck options.

His first 15 cards were Basic cards, one fact each, such as "Constitution: which article abolishes untouchability?" with "Article 17" on the back and the textbook page in brackets. He studied them once that evening. The next morning, at the bus stop on his way to the library, AnkiDroid showed him the cards that were due. He set a daily alarm for 7:15 a.m. as his review time: day 1 of his 30 days had begun.
""",
    evidence=[
        ('Spaced repetition (spacing plus retrieval in one tool)', 'strong', 'It combines the two techniques rated high utility by Dunlosky and others (2013).'),
        ('The Leitner box on paper', 'strong', 'The same principles without software: spaced, effortful recall with feedback.'),
        ('Newer schedulers (FSRS) versus the older one', 'limited', 'The Anki manual says FSRS estimates forgetting more accurately; either scheduler works if you review daily.'),
    ],
    resources=[
        ('ncase', 'Read the comic if you have not, or reread the Leitner box part', '25 minutes'),
        ('anki-start', 'Read Getting Started: cards, decks, notes, fields, note types', '15 minutes'),
        ('anki-study', 'Read the parts on the answer buttons and what to do when you can\'t recall', '10 minutes'),
        ('ankidroid-play', 'Install AnkiDroid (free; open source)', '5 minutes'),
        ('ankidroid-manual', 'Keep it open for anything you can\'t find in the app', 'As needed'),
    ],
    steps=[
        'Choose your 100-card topic with the checklist below, using your saved previous papers.',
        'Take a 20-question pre-test on the topic from previous papers or your guide, without looking anything up. Record the score in your Study Log.',
        'Install AnkiDroid. Create a deck named PSC::<subject>::<topic>, and set New cards/day to 15 in its options.',
        'Make 15 Basic cards from your notes or textbook: one fact per card, a short context word at the start of each question, and the source (book and page, or paper and question number) in brackets on the back.',
        'Study the 15 new cards today. Choose a fixed daily review time and set an alarm. Tomorrow is day 2 of your 30 days.',
        'Optional: make a free AnkiWeb account and sync, so your deck is backed up.',
    ],
    proof='A screenshot of your deck with its card count and of the deck options showing New cards/day, plus your pre-test score.',
    templates=[
        ('choose your 100-card topic', """
CHOOSE MY DECK TOPIC
Candidate topics: 1. ______________ 2. ______________ 3. ______________
For each, tick:
[ ] In my exam's syllabus
[ ] Appears in at least 2 of my saved previous papers (count: ___)
[ ] Rich in facts (enough for 100 cards)
[ ] I don't know it well yet (pre-test likely under 70%)
Chosen topic: ______________   Deck name: PSC::__________::__________
Pre-test (20 questions, no help): ___/20   Date: ______   Day-30 retest date: ______
""", ''),
        ('AnkiDroid setup checklist', """
[ ] AnkiDroid installed from Google Play (or F-Droid)
[ ] Deck created: PSC::<subject>::<topic>
[ ] Deck options: New cards/day = 15
[ ] First 15 Basic cards made (context word + one fact + source)
[ ] Studied once today
[ ] Daily review time chosen: ______  Alarm set [ ]
[ ] Optional: AnkiWeb account made and synced (backup)
""", ''),
    ],
    mistakes=[
        ('Making cards before you understand the topic.', 'The first of Wozniak\'s rules: do not learn what you do not understand. Read and make sense of it first.'),
        ('Creating ten decks on the first day.', 'Start with one deck for one topic. Add subjects one at a time, later.'),
        ('Setting 50 new cards a day.', 'New cards create future reviews. Start with 15; LRN-M04-L04 shows the maths.'),
        ('Pressing Good when you were wrong.', 'Honest answers keep the schedule right. Wrong means Again.'),
    ],
    quiz=[
        {'q': 'What is the difference between a note and a card in Anki?', 'o': ['A note is what you type in; a card is one question-answer that Anki shows, and one note can make several cards', 'They are the same thing', 'A card is a deck of notes', 'A note is a deck'], 'a': 'A', 'why': 'For example, a Basic (and reversed) note makes two cards.'},
        {'q': 'You can\'t recall the answer after about 10 seconds. What should you do?', 'o': ['Reveal it and press Again', 'Keep thinking for five minutes', 'Press Easy and move on', 'Delete the card'], 'a': 'A', 'why': 'The Anki manual suggests revealing after about 10 seconds; forgetting means Again.'},
        {'q': 'Which button should you use for most correct answers?', 'o': ['Good', 'Easy', 'Hard', 'Again'], 'a': 'A', 'why': 'Good is for answers recalled with some effort, which is most of them.'},
        {'q': 'Why take a 20-question pre-test before making the deck?', 'o': ['To measure how much the deck helps when you retest on day 30', 'Because AnkiDroid requires it', 'To choose a deck name', 'To find the answers to copy'], 'a': 'A', 'why': 'A before-and-after test turns your 30 days into measured improvement.'},
    ],
    study='Nicky Case\'s comic and the Anki manual\'s Getting Started and Studying pages',
    action='Choose your deck topic, take the 20-question pre-test, set up AnkiDroid and make your first 15 cards',
)

L2 = lesson(
    M, 2,
    outcome='Write clear one-fact PSC cards with the card-writing checklist, rewrite bad cards, and grow your deck to 45 or more.',
    split='20 minutes reading, 30 minutes resources, 50 minutes writing cards',
    core=f"""
A deck is only as good as its cards. Bad cards are slow to review, easy to fail and hard to remember. Most rules for good cards come from Piotr Wozniak's classic "Twenty rules of formulating knowledge", written in 1999 by the creator of SuperMemo, the first spaced repetition program ({link('sm-20rules', 'SuperMemo')}). The most important ones for PSC:

### 1. Understand first, then memorise

"Do not learn if you do not understand" and "learn before you memorise" are rules 1 and 2. A card should capture something you already understand. If you don't understand Article 32, read and explain it first (Module 8), then make cards.

### 2. One fact per card: the minimum information principle

Compare:

{table(['Bad card', 'Why it is bad', 'Good card(s)'], [
    ('Fundamental Rights? → Articles 12–35: equality, freedom, against exploitation, religion, cultural and educational, constitutional remedies, with article ranges', 'A whole list on one card: you will fail it even when you know most of it', 'Constitution: right to constitutional remedies is in which article? → Article 32 (and one card per right)'),
    ('Periyar → longest river, 244 km, ends in the Arabian Sea, ...', 'Many facts, no clear question', 'Kerala rivers: the longest river? → Periyar (244 km)'),
    ('Important features of the Preamble?', 'No single correct answer', 'Preamble: which words were added by the 42nd Amendment? → Socialist, secular, integrity'),
])}

Short questions with short answers are fast to review and easy to grade honestly.

### 3. Avoid sets and lists

"Name the six Malayalam Jnanpith winners" is one card you will keep failing. Instead, make one card per winner ("Jnanpith: the first ever award, in 1965, went to which Malayalam poet? → G. Sankara Kurup"), use one cloze per item (next lesson), or put the list in a memory palace (Module 11).

### 4. Fight interference

Similar facts get mixed up: "longest river" and "second longest river"; Article 14 and Article 15. Make the difference obvious in the question: "Kerala rivers: the **second** longest? → Bharathapuzha (209 km)". When two facts keep colliding, make one card that contrasts them side by side.

### 5. Context cues, wording and sources

- Start each question with a short context word: "Constitution:", "Kerala rivers:", "Jnanpith:". It tells your brain where to search, and it keeps cards clear when your deck grows.
- Write the shortest question that has **one** correct answer.
- Add the source in brackets on the back (book and page, or paper and question number). When a card and an answer key disagree, you know where to check.

### 6. Both directions only when PSC asks both ways

**Basic (and reversed card)** makes two cards: "Article 17 is about...?" and "Abolition of untouchability is in which article?" That doubles the reviews, so use it only for pairs that exam questions really ask both ways: article and content, author and book, award and field.

### 7. Turn mistakes into cards

Every previous-year question you get wrong, or answer by recognition only, can become one to three cards. These are the most valuable cards in your deck, because they target exactly what you didn't know.
""",
    example="""
**Sreeja** made her first 20 cards on the Kerala renaissance in a hurry, copying lines from her guide. Seven of them were lists, such as "Reformers from Travancore and their organisations". After a week she was pressing Again on those seven almost every time, and AnkiDroid felt like punishment.

She went through her cards with the card-writing checklist. The seven list cards became 19 one-fact cards, each starting with "Kerala renaissance:" and ending with the guide's page number. Two pairs she had mixed up for weeks got a contrast card each. She added Basic (and reversed) only for reformer and organisation pairs, because previous papers asked those both ways.

Her daily reviews now take her about 10 minutes, and she presses Again far less often. She also made 6 cards from her mistakes in a previous paper, and two of those exact facts came up in the next mock.
""",
    evidence=[
        ('Flashcards used for retrieval with spacing', 'strong', 'Practice testing and distributed practice, the two high-utility techniques, in one tool.'),
        ('One fact per card (minimum information principle) and avoiding lists', 'limited', 'Practical rules from Wozniak\'s long experience, consistent with research on retrieval; not each tested separately.'),
        ('Understanding before memorising', 'moderate', 'Meaningful encoding lasts longer (Module 1); cards for things you don\'t understand are fragile.'),
    ],
    resources=[
        ('sm-20rules', 'Read rules 1 to 5, 9 to 12, 16 and 18 (understand first, minimum information, cloze, imagery, avoid sets and enumerations, interference, wording, context cues, sources)', '35 minutes'),
        ('anki-start', 'Reread the part on note types, especially Basic (and reversed card)', '5 minutes'),
    ],
    steps=[
        'Check your 15 cards from LRN-M04-L01 against the card-writing checklist. Rewrite every card that fails a line, and note what was wrong.',
        'Write at least 30 new cards on your topic, so the deck has 45 or more. Follow the checklist for every card.',
        'Use Basic (and reversed card) only for pairs that previous papers ask both ways; aim for at least 5 such pairs.',
        'Make at least 5 cards from questions you got wrong in your pre-test or in a previous paper.',
        'Ask a study partner or family member to read 10 random cards aloud. For each, ask: is the question clear, with only one correct answer? Fix any they find unclear.',
        'Keep up your daily reviews: reviews first, then new cards.',
    ],
    proof='Screenshots of 5 cards before and after rewriting, and of the deck showing 45 or more cards.',
    templates=[
        ('card-writing checklist (core tool)', tools.CARD_CHECKLIST, ''),
        ('bad card to good card rewrite sheet', """
REWRITE SHEET
Old card (front -> back): ___________________________________________
Problem (tick): [ ] list or set  [ ] more than one fact  [ ] vague question
                [ ] no context cue  [ ] look-alike fact  [ ] no source  [ ] not understood
New card(s):
1. _______________: ________________ ? -> ________________ (source ______)
2. _______________: ________________ ? -> ________________ (source ______)
3. _______________: ________________ ? -> ________________ (source ______)
""", ''),
    ],
    mistakes=[
        ('Putting a list on one card.', 'Split it: one card per item, one cloze per item, or a memory palace.'),
        ('Copying whole textbook sentences as answers.', 'Shorten to the one fact you need: a word, number or name.'),
        ('Making cards for facts outside your syllabus.', 'Check the syllabus and previous papers. Every card costs review time for months.'),
        ('Reversing every card.', 'It doubles the work. Reverse only pairs that PSC asks both ways.'),
        ('Leaving out the source.', 'When an answer key disagrees, the source tells you where to check.'),
    ],
    quiz=[
        {'q': 'Which card follows the minimum information principle?', 'o': ['Kerala rivers: the longest river? → Periyar (244 km)', 'Kerala rivers? → all 44 rivers with lengths', 'Periyar → everything about it', 'Rivers and dams of Kerala? → a full table'], 'a': 'A', 'why': 'One short question with one short answer.'},
        {'q': 'What is the best way to learn the six Malayalam Jnanpith winners?', 'o': ['One card or cloze per winner, or a memory palace for the list', 'One card asking for all six', 'Reading the list daily', 'A reversed card with the whole list'], 'a': 'A', 'why': 'Sets and lists on one card are hard to recall and grade.'},
        {'q': 'Why start questions with a context word such as "Constitution:"?', 'o': ['It tells your memory where to search and keeps cards clear as the deck grows', 'AnkiDroid requires it', 'It makes cards longer', 'It is only for decoration'], 'a': 'A', 'why': 'Context cues are one of Wozniak\'s rules and make short questions unambiguous.'},
        {'q': 'When should you use Basic (and reversed card)?', 'o': ['Only for pairs that exam questions ask both ways', 'For every card', 'Never', 'Only for maths'], 'a': 'A', 'why': 'Reversed cards double reviews, so use them only where both directions matter.'},
        {'q': 'Which cards are often the most valuable in your deck?', 'o': ['Cards made from questions you got wrong or only recognised', 'Cards on facts you already know well', 'Cards copied from a friend\'s deck', 'Cards on topics outside the syllabus'], 'a': 'A', 'why': 'They target exactly the gaps that previous papers exposed.'},
    ],
    study='Wozniak\'s twenty rules (the rules listed in the resources) and the Anki note types',
    action='Rewrite your first cards with the checklist and grow your deck to 45 or more good cards',
)

L3 = lesson(
    M, 3,
    outcome='Make cloze cards from key sentences and image occlusion cards from maps and diagrams, and grow your deck to 70 or more cards.',
    split='15 minutes reading, 25 minutes resources, 50 minutes making cards',
    core=f"""
### Cloze deletion: hide part of a sentence

A **cloze** card shows a sentence with a gap, and you recall what is missing. In Anki you choose the **Cloze** note type and wrap the hidden part in double braces ({link('anki-edit', 'Anki manual: Editing')}):

{fence('''The Temple Entry Proclamation was issued in {{c1::1936}} in {{c2::Travancore}}.
Article {{c1::21A}} makes education a Fundamental Right for children aged {{c2::6 to 14}} years.
Kerala's longest river is the {{c1::Periyar::river}} ({{c2::244}} km).''')}

- Each number (c1, c2, ...) makes **its own card**. The first line above makes two cards: one hides the year, the other hides the place.
- Text after a double colon inside a cloze, such as `::river`, is a **hint** shown in the gap.
- Giving two gaps the **same number** hides both on one card. Use that rarely; one gap per card is easier to grade.

Cloze is a quick way to make cards from good sentences in your textbook or notes. Wozniak calls it "easy and effective" (rule 5), with a warning: keep each sentence short and clear, and don't hide trivial words.

**Cloze works well for lists too**, because each card hides one item and shows the rest as context:

{fence("Kerala's three east-flowing rivers are {{c1::Kabani}}, {{c2::Bhavani}} and {{c3::Pambar}}.")}

### Image occlusion: hide part of a picture

**Image occlusion** works like cloze, but on a picture: you draw boxes over parts of a map or diagram, and each box becomes a card. It arrived in Anki 23.10 and is part of AnkiDroid from version 2.17 ({link('anki-io-forum', 'Anki forums')}). Wozniak's rule 8 says graphic deletion is as good as cloze deletion.

To make one: add a note, choose the **Image Occlusion** note type, pick a photo or screenshot, draw boxes (or other shapes) over the labels you want to learn, and save. Each box makes a card. Two modes:

- **Hide all, guess one:** all boxes are hidden; one is marked as the question. Best for maps, where neighbouring labels would give the answer away.
- **Hide one, guess one:** only the asked box is hidden; the others are visible. Fine for diagrams where the other labels don't give clues.

If you delete a box later, its card stays until you run Tools → Empty Cards (in Anki for computers).

Good PSC uses: a map of Kerala's districts, national parks or rivers; a map of India's states; a diagram of the heart, the eye or the atmosphere; a chart of the Constitution's Parts; a timeline photo.

**If image occlusion doesn't work on your phone,** make these notes in Anki for computers on the laptop (if it runs Windows 10 or later or a recent Linux) and sync through AnkiWeb, or use a numbered hand-drawn map with Basic cards ("Kerala map: district number 4 from the north? → Kozhikode").

Take map photos from your SCERT textbook or draw your own. Check the map is correct and up to date; an old map can show old boundaries or names.
""",
    example="""
**Anu** chose Kerala geography as her deck topic. Lists of districts and rivers were her weak spot.

She photographed the district map in her SCERT textbook, added an **Image Occlusion** note in AnkiDroid, drew a box over each of the 14 district names and chose **hide all, guess one**, so neighbouring names couldn't give the answer away. That one note made 14 cards.

For rivers she used cloze sentences from her notes, one fact per gap, with hints where two answers were possible: "Kerala's second longest river is the {{c1::Bharathapuzha}} ({{c2::209}} km)". In one evening her deck went from 46 to 78 cards. A week later she could fill a blank district map without errors, which she had never managed by reading.
""",
    evidence=[
        ('Cloze cards and image occlusion as retrieval practice', 'strong', 'Both make you produce the answer from memory, then check: retrieval with feedback.'),
        ('Cloze or graphic deletion versus Basic cards', 'limited', 'Wozniak calls them easy and effective; there is little research comparing card formats. Choose by the content.'),
        ('Pictures that carry meaning (maps, diagrams)', 'moderate', 'Dual coding (Module 3): the visual adds a second route to the memory.'),
    ],
    resources=[
        ('anki-edit', 'Read the sections on cloze deletion and image occlusion', '20 minutes'),
        ('anki-io-forum', 'Read the thread on image occlusion in AnkiDroid 2.17', '5 minutes'),
        ('sm-20rules', 'Read rules 5 (cloze deletion) and 8 (graphic deletion)', '10 minutes'),
    ],
    steps=[
        'Find 25 key sentences in your topic (from the textbook, your notes or answer explanations). Shorten each to one clear sentence.',
        'Make 25 cloze cards: one key fact per gap, a hint where two answers could fit, and the source at the end.',
        'Make at least one image occlusion note from a map, diagram, chart or timeline related to your topic, with 8 to 15 boxes. Choose hide all, guess one for maps.',
        'If image occlusion doesn\'t work on your phone, make it on the laptop and sync, or use a numbered hand-drawn map with Basic cards.',
        'Check that your deck now has 70 or more cards, and keep up the daily reviews.',
    ],
    proof='Screenshots of three cloze notes in the editor, the image occlusion screen with your boxes, and the deck count.',
    templates=[
        ('cloze patterns for PSC facts', """
FACT IN A SENTENCE   The {{c1::Vaikom Satyagraha}} began in {{c2::1924}}.
DEFINITION           {{c1::Federalism}} means power is divided between the centre and the states.
NUMBER WITH HINT     Kerala has {{c1::14::number}} districts.
LIST, ONE PER CARD   The three lists in the Seventh Schedule are the {{c1::Union}}, {{c2::State}} and {{c3::Concurrent}} lists.
CAUSE AND EFFECT     Rain is heavy on Kerala's side of the Western Ghats because {{c1::the moist winds rise and cool}}.
Rules: one key fact per gap; never hide small words (the, of, in); keep the sentence short; add the source.
""", ''),
        ('image occlusion steps', """
1. Photo or screenshot: a clear map or diagram, cropped to what you need.
2. AnkiDroid: add a note -> note type "Image Occlusion" -> choose the image.
3. Draw a box over each label to learn (8 to 15 per image).
4. Choose: hide all, guess one (maps) or hide one, guess one (diagrams).
5. Add a header such as "Kerala districts" and the source.
6. Save, then study one card to check the masks look right.
""", ''),
    ],
    mistakes=[
        ('Hiding several facts in one gap.', 'One key fact per cloze. Long gaps are hard to grade.'),
        ('Clozing small words.', 'Hide the fact that matters (a name, a number, a term), not "the" or "of".'),
        ('Forty boxes on one image.', 'Split big maps into regions; 8 to 15 boxes per image is easier to review.'),
        ('Using hide one, guess one on a map.', 'The neighbours give the answer away. Use hide all, guess one.'),
        ('Trusting an old or wrong map.', 'Check the map against your current textbook before making cards.'),
    ],
    quiz=[
        {'q': 'How many cards does this cloze note make: "The {{c1::SNDP Yogam}} was founded in {{c2::1903}}"?', 'o': ['Two', 'One', 'Three', 'None'], 'a': 'A', 'why': 'Each cloze number makes its own card.'},
        {'q': 'Which image occlusion mode suits a map of Kerala\'s districts?', 'o': ['Hide all, guess one', 'Hide one, guess one', 'Show all, guess none', 'No masks'], 'a': 'A', 'why': 'On a map, visible neighbouring labels would give the answer away.'},
        {'q': 'What does the text after a double colon inside a cloze do, as in {{c1::Periyar::river}}?', 'o': ['It shows a hint in the gap', 'It makes a second card', 'It hides the whole sentence', 'It adds a picture'], 'a': 'A', 'why': 'The hint appears in the gap while you recall.'},
        {'q': 'Image occlusion doesn\'t work on your phone. What is a good alternative?', 'o': ['Make the note in Anki on the laptop and sync, or use a numbered hand-drawn map with Basic cards', 'Skip maps entirely', 'Copy the map ten times', 'Buy a paid app'], 'a': 'A', 'why': 'Both keep the map as a retrieval cue at no cost.'},
    ],
    study='The Anki manual\'s sections on cloze deletion and image occlusion, and Wozniak\'s rules 5 and 8',
    action='Make 25 cloze cards and one image occlusion note, and bring your deck to 70 or more cards',
)

L4 = lesson(
    M, 4,
    outcome='Keep your daily AnkiDroid habit sustainable by budgeting new cards, rescuing a backlog and fixing cards you keep failing, and finish your deck at 100 or more cards.',
    split='20 minutes reading, 25 minutes resources, 30 minutes action plus finishing the deck',
    core=f"""
### New cards decide tomorrow's work

Every new card you add today will come back for reviews for weeks and months. So the number of **new cards a day** controls your future daily workload. The Anki manual gives a rule of thumb: if you consistently learn 20 new cards a day, you can expect roughly 200 reviews a day ({link('anki-deck', 'Anki manual: Deck Options')}).

Scale that down to plan your own budget. Ten new cards a day leads, over time, to roughly 100 reviews a day. If a review takes you about 8 seconds (time yourself; it varies), 100 reviews take about 13 minutes. A sensible PSC budget is **10 to 15 new cards a day** and 15 to 25 minutes of reviews. When exam pressure rises, cut new cards first, never reviews.

### The daily routine

1. **Same time, same place, every day:** for example with your morning tea. Module 6 shows how to anchor a habit to something you already do.
2. **Reviews first, then new cards.** If time runs out, the new cards wait.
3. **Answer honestly and quickly.** Recall, reveal, judge, press. Don't think for minutes about one card.

### Desired retention

Newer versions of Anki can use a scheduler called **FSRS**, with a setting called **desired retention**: the share of cards you want to remember when they come up. The default is 90%. A higher number gives shorter gaps and more reviews, and the workload rises sharply as you approach 100%; the manual advises staying below 97%. If your AnkiDroid shows these options, the default is a good place to start; if not, the older scheduler works fine too.

### When you fall behind

Missed a few days? The reviews pile up, and the pile looks frightening. Don't delete the deck and don't try to do 500 reviews in one sitting.

1. Set **New cards/day to 0** until you are back on track.
2. Do a fixed amount every day, for example 150 reviews or 25 minutes.
3. When the daily due count is back to normal, turn new cards back on.

When you are behind, Anki shows the cards that have waited longest first ({link('anki-study', 'Anki manual: Studying')}), so the most forgotten cards get attention first.

### Leeches: cards you keep failing

Some cards you fail again and again. Anki calls them **leeches** and can tag them automatically. Repeating a bad card doesn't fix it; rewriting does:

- **Split it** if it holds more than one fact.
- **Add context or a contrast** if you confuse it with a similar fact (LRN-M04-L02).
- **Add a hook:** an example, a picture or a mnemonic (Module 11).
- **Check you understand it;** if not, relearn the idea first.
- **Suspend or delete it** if it is not worth the time.

### After the 30 days

Your 30 days prove the habit. Keep going: add decks for other PSC subjects one at a time, and keep the total review time within your budget. Export or sync your collection regularly as a backup.
""",
    example="""
**Sreeja** was excited in her first week and set New cards/day to 30. By day 9 AnkiDroid showed 180 reviews due, she had a sick child and a busy week, and she didn't open the app for three days. When she did, it showed 400 due. She nearly gave up.

Her study partner showed her the backlog plan. She set new cards to 0 and did 25 minutes of reviews every day after dropping her children at school. After four days the due count was back below 80. She then set New cards/day to 12, which her timing showed would settle at about 15 minutes of reviews a day.

She also found four cards she had failed at least five times. Two were lists, which she split; one confused the Vaikom and Guruvayur satyagrahas, which got a contrast card; one she suspended because it was not in her syllabus. Her deck reached 112 cards on day 14, and she finished her 30 days without missing another day.
""",
    evidence=[
        ('Daily spaced reviews (consistency)', 'strong', 'Spacing works only if reviews happen near their due dates; daily review keeps the schedule intact.'),
        ('New cards drive future workload (about ten reviews a day per daily new card)', 'moderate', 'A rule of thumb from the Anki manual, based on how the scheduler works; your own timing gives your numbers.'),
        ('Rewriting leeches instead of repeating them', 'limited', 'Practical advice from Anki and Wozniak, consistent with research on interference and meaningful encoding.'),
    ],
    resources=[
        ('anki-deck', 'Read the parts on daily limits, FSRS and desired retention', '20 minutes'),
        ('anki-study', 'Read what happens when you fall behind', '5 minutes'),
        ('ankidroid-manual', 'Find the statistics screen and the deck options in AnkiDroid', '10 minutes'),
    ],
    steps=[
        'Time 20 of your reviews to find your seconds per review. Fill in the workload calculator below and set New cards/day to match your daily minutes.',
        'Finish your deck at 100 or more cards, adding cards from questions you got wrong in previous papers where you can.',
        'Find three cards you have failed three or more times. Rewrite, split or suspend each, and note what was wrong.',
        'Take a screenshot of the statistics screen showing your review days and the percentage of answers you got right.',
        'Write your daily review rule in one line: when, where, and what comes just before it (for example: "After morning tea, at the kitchen table, before I open WhatsApp").',
    ],
    proof='A screenshot of your deck with 100 or more cards, your filled-in workload calculator, the three leech fixes, a statistics screenshot and your daily review rule.',
    templates=[
        ('AnkiDroid workload calculator', """
My seconds per review (timed over 20 reviews): ___ s
Minutes I can give to AnkiDroid each day: ___ min
Reviews that fit: minutes x 60 / seconds = ___ reviews a day
Long-run reviews are about 10 x new cards a day, so:
New cards a day = reviews that fit / 10 = ___   (cap at 15 while preparing for PSC)
Example: 8 s per review, 15 min a day -> 15 x 60 / 8 = 112 reviews -> about 11 new cards a day
""", ''),
        ('backlog rescue plan', """
BACKLOG RESCUE      Start date: ______   Due count today: ___
1. New cards/day -> 0
2. Daily target: ___ reviews or ___ minutes (same time every day)
3. Track: day 1 ___ due | day 2 ___ | day 3 ___ | day 4 ___ | day 5 ___
4. When the due count is back near my normal (___), set new cards back to ___
Cause of the backlog: __________   My fix so it doesn't happen again: __________
""", ''),
    ],
    mistakes=[
        ('Adding more new cards on good days.', 'Today\'s extra cards are next month\'s extra reviews. Keep new cards steady.'),
        ('Skipping reviews to "catch up" on lessons.', 'Missed reviews pile up. Five minutes of reviews beats none.'),
        ('Trying to clear a huge backlog in one sitting.', 'Set new cards to 0 and do a fixed amount daily; it clears in days.'),
        ('Repeating a leech forever.', 'Rewrite, split, add a hook or suspend it.'),
        ('Never backing up.', 'Sync to AnkiWeb or export your collection to your Learning Folder.'),
    ],
    quiz=[
        {'q': 'According to the Anki manual, learning 20 new cards a day leads to roughly how many reviews a day?', 'o': ['About 200', 'About 20', 'About 2,000', 'None after a week'], 'a': 'A', 'why': 'New cards keep coming back, so daily reviews grow to about ten times the daily new cards.'},
        {'q': 'You missed five days and have 400 reviews due. What should you do?', 'o': ['Set new cards to 0 and do a fixed amount of reviews daily until the count is normal', 'Delete the deck and start again', 'Do all 400 tonight', 'Add more new cards to make up'], 'a': 'A', 'why': 'A steady daily amount clears the backlog without burning you out.'},
        {'q': 'What happens to your workload if you raise desired retention from 90% to 97%?', 'o': ['Reviews increase, sharply as you near 100%', 'Reviews decrease', 'Nothing changes', 'Cards are deleted'], 'a': 'A', 'why': 'Higher retention means shorter gaps and more reviews.'},
        {'q': 'What is the best fix for a card you have failed six times?', 'o': ['Rewrite, split it, add a hook or contrast, or suspend it', 'Keep pressing Again until it sticks', 'Press Easy to get rid of it', 'Make five copies of it'], 'a': 'A', 'why': 'Leeches usually have a problem in the card itself.'},
        {'q': 'Exam pressure rises and time is short. What do you cut first?', 'o': ['New cards', 'Reviews', 'Sleep', 'The weekly review'], 'a': 'A', 'why': 'Reviews protect what you already learned; new cards can pause.'},
    ],
    study='The Anki manual\'s Deck Options and the part of Studying on falling behind',
    action='Set a workload budget, fix three leeches and finish your deck at 100 or more cards',
)

LESSONS = [L1, L2, L3, L4]

MODULE = module(
    M,
    overview="""
Learn spaced repetition from zero with AnkiDroid: set it up, write good cards, use cloze and image occlusion, and keep the daily habit sustainable. Build a deck of 100 or more cards on one PSC topic and review it every day for 30 days, with a test before and after.

AnkiDroid is free and open source, and it does the hard part of spacing for you: it shows each card just before you would forget it. Used well, 15 to 25 minutes a day can hold thousands of PSC facts. Used badly, with list-cards and too many new cards, it becomes a chore people abandon in a fortnight. This module teaches the good way.

Your deck starts this week, and so does your 30-day review on the **Learning system track**. On day 30 you retake a 20-question test on your topic to measure the difference.
""",
    outcomes=[
        'Explain how spaced repetition schedules reviews and use the four answer buttons honestly',
        'Write one-fact cards with context cues and sources, using the card-writing checklist',
        'Make cloze cards and image occlusion cards from maps and diagrams',
        'Budget new cards, rescue a backlog and fix leeches',
        'Build a 100-card PSC deck and review it daily for 30 days',
    ],
    lessons=LESSONS,
    tools=[
        'The **card-writing checklist** (one of the six core tools)',
        'Your **AnkiDroid deck** and the daily review habit',
        'The **workload calculator** and **backlog rescue plan**',
        '**Cloze patterns** and **image occlusion steps**',
    ],
    project='My 100-card PSC deck',
    project_steps=[
        'Make sure your deck has 100 or more cards on one PSC topic, with a mix of Basic, Basic (and reversed) where PSC asks both ways, cloze and at least one image occlusion note.',
        'Pick 20 cards at random and check each against the card-writing checklist. Fix any that fail.',
        'Back up the deck: sync to AnkiWeb or export it to your Learning Folder (04 Anki).',
        'Keep reviewing daily to day 30 on the Learning system track, then retake a 20-question test on the topic (new questions where possible) and compare with your pre-test.',
    ],
    project_proof='A screenshot of the deck with its card count, your 20-card checklist audit, and your pre-test score (the day-30 retest goes on the Learning system track).',
    rubric=[
        ('Size and mix', 'Under 100 cards', '100 cards, one card type', '100 or more, with Basic, cloze and image occlusion used where they fit'),
        ('Card quality', 'Lists and vague questions', 'Mostly one fact, some unclear', '20-card audit passed: one fact, context cue, source'),
        ('Habit', 'Missed several days', 'Reviews most days', 'Reviews every day at a fixed time, reviews before new cards'),
        ('Workload', 'Backlog out of control', 'Workable but uneven', 'Budget set from timing; backlog plan known'),
    ],
    short=[
        'Make 100 Basic and cloze cards on one topic at 10 a day; skip image occlusion.',
        'Never skip the daily reviews: on a bad day, 5 minutes.',
    ],
    flashcards=[
        ('Note versus card', 'A note is what you type in; a card is one question Anki shows. One note can make several cards.'),
        ('The four answer buttons', 'Again (forgot), Hard, Good (most correct answers), Easy (too easy).'),
        ('Young versus mature card', 'Young: gap under 21 days. Mature: 21 days or more.'),
        ('The minimum information principle', 'One fact per card, short question, short answer.'),
        ('What each cloze number does', 'Makes its own card; c1 and c2 make two cards.'),
        ('Image occlusion mode for maps', 'Hide all, guess one.'),
        ('Anki\'s workload rule of thumb', '20 new cards a day leads to roughly 200 reviews a day.'),
        ('Backlog rescue', 'New cards to 0; a fixed amount of reviews daily until the count is normal.'),
        ('Leech fixes', 'Split, add context or contrast, add a hook, relearn, or suspend.'),
    ],
    mistakes=[
        ('Building a big deck fast, then quitting.', 'Slow and daily beats big and abandoned. Ten good cards a day is plenty.'),
        ('Copying someone else\'s ready-made deck instead of making your own.', 'Making cards is part of learning, and other people\'s cards often don\'t match your syllabus or understanding.'),
    ],
)
