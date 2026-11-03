"""Module 15: Language learning."""
from common import lesson, module, link, fence, table

M = 15

L1 = lesson(
    M, 1,
    outcome='Explain the roles of input, output and vocabulary in learning a language, and start an AnkiDroid vocabulary deck with card formats that build real use, not just recognition.',
    split='20 minutes reading, 25 minutes resources, 40 minutes action',
    core=f"""
Whether it is English for PSC, Malayalam grammar, or Hindi or Arabic for a future job, every language is learned through the same three things.

### 1. Input: lots of understandable listening and reading

You learn a language mostly by understanding it: hearing and reading a lot of it, at a level where you understand most of what you meet. Language researchers broadly agree that large amounts of such input are essential. The stronger claim, that input alone is enough and practice in speaking adds nothing, is disputed. (No single source was checked for this course on this point; treat it as the general picture.) For you, input means daily reading (Module 10) and listening (LRN-M15-L03).

### 2. Output: speaking and writing

When you try to say or write something, you notice what you can't yet say: a missing word, a tense you're unsure of. That gap is where learning happens, if you get feedback. Output includes your Feynman explanations in English (Module 8), writing answers, and speaking with a partner (Module 20).

### 3. Vocabulary: the words that carry meaning

Without enough words, input is incomprehensible and output is impossible. Vocabulary is also tested directly in PSC: synonyms, antonyms, one-word substitutes, idioms, spelling. And vocabulary is exactly where spaced repetition shines: thousands of small items, each needing retrieval at growing gaps (Module 4).

### Learn phrases, not lonely words

Words live in company. "Decision" is used with "make" (make a decision), "exam" with "take" or "write" (take an exam), "interested" with "in". Learning these chunks (collocations and phrases) helps both understanding and correct use. So every vocabulary card should include an **example sentence**, ideally one from your reading.

### Four card formats for vocabulary

{table(['Format', 'Front', 'Back', 'What it trains'], [
    ('Meaning', 'diligent (word, with an example sentence)', 'hard-working, careful; Malayalam: ഉത്സാഹമുള്ള', 'Understanding'),
    ('Production', 'hard-working and careful (one word): "a ___ student"', 'diligent', 'Using the word: harder and more useful'),
    ('Cloze sentence', 'She was {{c1::diligent}} about her daily reviews.', 'diligent', 'The word in context'),
    ('Phrase', 'to stop working for the day (idiom)', 'to call it a day', 'Idioms and set phrases'),
])}

Use **production** and **cloze** cards for words you want to use; **meaning** cards for words you only need to recognise. Avoid the keyword mnemonic as your main method: Dunlosky and colleagues rated it low utility, partly because its benefits for vocabulary may not last ({link('dunlosky-aft', 'Dunlosky, 2013')}).

### Which words first?

Common words first: the words you meet again and again in your reading, in previous papers and in the news. A word from three PSC papers is worth more than a rare word from a vocabulary list.
""",
    example="""
**Sreeja** had a notebook of English words copied from a "1,000 words for competitive exams" list, but she couldn't use them and kept forgetting them.

She started a deck called `Lang::English::Vocabulary` and filled it only with words and phrases she had met: in the English sections of previous papers, in LearnEnglish texts and in the newspaper. For each she wrote an example sentence from where she had found it. She used production cards for words she wanted to use ("hard-working and careful (one word)") and meaning cards for rarer ones, with a Malayalam gloss.

She added 8 new cards a day. After four weeks she had about 220 cards and noticed the difference in two places: English passages in mocks were easier to follow, and she got synonym and antonym questions right that she would once have guessed.
""",
    evidence=[
        ('Spaced retrieval for vocabulary', 'strong', 'Practice testing and spacing (both high utility) suit vocabulary well.'),
        ('Large amounts of understandable input', 'moderate', 'Widely accepted in language research; the claim that input alone is enough is disputed.'),
        ('Learning words with example sentences and phrases', 'limited', 'Sensible and widely recommended; no specific source was checked for this course.'),
        ('The keyword mnemonic for vocabulary', 'limited', 'Rated low utility by Dunlosky and others (2013).'),
    ],
    resources=[
        ('learnenglish', 'Open the vocabulary section and do one exercise at your level', '20 minutes'),
        ('anki-edit', 'Refresh cloze syntax for sentence cards', '5 minutes'),
        ('dunlosky-aft', 'Reread the keyword mnemonic section on vocabulary', '5 minutes'),
    ],
    steps=[
        'Create a deck named Lang::English::Vocabulary (or a Malayalam or other language deck if English is not your priority).',
        'Collect 30 words and phrases you have actually met: from the English sections of your previous papers, your reading log (Module 10) and the news.',
        'Make cards in at least three of the four formats, each with an example sentence and a Malayalam gloss where it helps.',
        'Set the deck to 5 to 10 new cards a day, within your total AnkiDroid budget.',
        'Keep a word-capture list on your phone or in your notebook, and add to it during reading and listening.',
    ],
    proof='A screenshot of your vocabulary deck with at least 30 notes, and one example of each card format you used.',
    templates=[
        ('vocabulary card formats', """
MEANING      Front: diligent  ("She was diligent about her reviews.")
             Back:  hard-working and careful | ഉത്സാഹമുള്ള
PRODUCTION   Front: hard-working and careful (one word): "a ___ student"
             Back:  diligent
CLOZE        She was {{c1::diligent}} about her daily reviews.
PHRASE       Front: to stop working for the day (idiom)
             Back:  to call it a day  ("It was late, so we called it a day.")
""", ''),
        ('word-capture list', """
WORD CAPTURE     (add during reading and listening; make cards within 24 hours)
Date   | Word or phrase | Sentence where I met it                 | Source        | Card made?
______ | ______________ | _______________________________________ | ____________ | [ ]
______ | ______________ | _______________________________________ | ____________ | [ ]
""", ''),
    ],
    mistakes=[
        ('Learning lonely words from long lists.', 'Learn words you meet, with the sentence you met them in.'),
        ('Only meaning cards.', 'Add production and cloze cards for words you want to use.'),
        ('Fifty new words a day.', 'Five to ten a day, within your AnkiDroid budget, lasts.'),
        ('Rare words first.', 'Common words from your papers and reading first.'),
    ],
    quiz=[
        {'q': 'Which card trains you to use a word, not just recognise it?', 'o': ['"Hard-working and careful (one word)" → diligent', '"Diligent" → hard-working and careful', 'A list of 50 words', 'A highlighted word in a book'], 'a': 'A', 'why': 'Production cards make you recall the word itself.'},
        {'q': 'Why include an example sentence on vocabulary cards?', 'o': ['Words are used in phrases and contexts; the sentence shows how', 'It makes cards longer', 'AnkiDroid requires it', 'It isn\'t useful'], 'a': 'A', 'why': 'Context and collocations help understanding and correct use.'},
        {'q': 'Which words should you learn first?', 'o': ['Common words you meet in your reading and previous papers', 'The rarest words you can find', 'Words starting with A', 'Words from a random list'], 'a': 'A', 'why': 'Frequent words pay off most in understanding and in exams.'},
        {'q': 'What is the honest position on "input alone is enough to learn a language"?', 'o': ['Input is essential, but the claim that it alone is enough is disputed', 'Proven true', 'Proven false: input doesn\'t matter', 'Only children need input'], 'a': 'A', 'why': 'Most agree input is essential; output and feedback also help.'},
    ],
    study='The LearnEnglish vocabulary section and the Anki cloze refresher',
    action='Start a vocabulary deck with 30 words and phrases you have met, in at least three card formats',
)

L2 = lesson(
    M, 2,
    outcome='Map the English part of your PSC syllabus, find your weakest areas from previous papers, and fix them with rule cards and practice loops.',
    split='15 minutes reading, 30 minutes resources, 50 minutes action',
    core=f"""
### What PSC English usually tests

English sections in general Kerala PSC papers commonly cover areas like these. **Check your own syllabus**, because the exact list differs between exams:

{table(['Area', 'Examples'], [
    ('Grammar', 'Articles, prepositions, tenses, subject-verb agreement, active and passive voice, direct and indirect speech, question tags, degrees of comparison'),
    ('Vocabulary', 'Synonyms, antonyms, one-word substitution, idioms and phrases, phrasal verbs, foreign words and phrases'),
    ('Spelling and correction', 'Correctly spelt words, spotting the error in a sentence'),
    ('Comprehension', 'Short passages with questions, in some exams'),
])}

### Find your weak areas from data

Tag the English questions from your saved previous papers by area in your PYQ tab (Module 12). Your errors will cluster in two or three areas. Those are your practice-loop targets (Module 13), not the whole grammar book.

### Rule cards with your own mistakes

For each weak area, learn the rule with examples (the LearnEnglish grammar pages explain each area simply, by level: {link('learnenglish', 'LearnEnglish')}), then make **rule cards** that include a sentence you got wrong and its correction:

{table(['Area', 'Rule card front', 'Back'], [
    ('Question tags', 'He is a doctor, ___ ? (tag)', 'isn\'t he? A positive statement takes a negative tag.'),
    ('Subject-verb agreement', 'Each of the students ___ (have / has) a book.', 'has: "each" takes a singular verb.'),
    ('Articles', '___ honest man (a / an)', 'an: the choice follows the sound, and "honest" starts with a vowel sound.'),
    ('Articles', '___ university (a / an)', 'a: "university" starts with a "yoo" sound.'),
    ('Prepositions', 'good ___, interested ___, afraid ___', 'good at, interested in, afraid of'),
    ('Reported speech', 'He said, "I am tired." (indirect)', 'He said that he was tired.'),
    ('Passive voice', 'The PSC conducts the exam. (passive)', 'The exam is conducted by the PSC.'),
    ('One-word substitution', 'Fear of heights (one word)', 'acrophobia'),
    ('Idioms', 'a piece of cake', 'something very easy'),
])}

### Practice loops for grammar

For a weak area, take 10 sentences at a time from previous papers or LearnEnglish exercises. Do one, check it immediately, and if it is wrong, say which rule you broke and make or update a rule card. Then do two more of the same kind. Track accuracy over three sessions (Module 13).

### Spelling

Spelling questions often use the same troublesome words: accommodation, committee, necessary, separate, occurrence, embarrass. Put misspellings you meet into cloze cards, with the tricky letters as the gap ("acco{{c1::mm}}odation").

### A daily English habit

Ten minutes of English reading (Module 10), five new words or phrases (LRN-M15-L01), and one grammar loop a week is enough to move steadily, alongside the rest of your PSC study.
""",
    example="""
**Ashiq** believed his English was "fine" because he read English news easily. Tagging 50 English questions from three previous papers told a different story: 9 of his 14 errors were in prepositions and question tags.

He made 20 rule cards, each with a sentence he had got wrong and its correction, for example "afraid ___ the dark: afraid of" and "You haven't finished, ___? : have you?". Then he ran three practice loops of 10 sentences each on prepositions and question tags, checking each sentence as he went.

His accuracy on those two areas rose from 45% to 70% to 90% across the three sessions. In a mixed set of 20 English questions a week later he scored 18, and the two misses were spelling, which became his next loop.
""",
    evidence=[
        ('Practice on weak grammar areas with immediate feedback', 'moderate', 'Consistent with research on practice testing and feedback (Modules 3 and 13).'),
        ('Rule cards built from your own mistakes', 'limited', 'A practical method combining feedback and spaced retrieval; no direct study of this format.'),
        ('Spaced retrieval of rules, idioms and spellings', 'strong', 'Practice testing and spacing, rated high utility.'),
    ],
    resources=[
        ('learnenglish', 'Open the grammar section and study your two weakest areas at your level, with their exercises', '30 minutes'),
        ('psc-pyq', 'Collect the English questions from your saved papers for tagging', '15 minutes'),
        ('scert', 'Optional: the grammar sections of SCERT English textbooks for your level', 'As needed'),
    ],
    steps=[
        'List the English areas in your exam\'s syllabus.',
        'Tag at least 50 English questions from previous papers by area in your PYQ tab, and mark which you got wrong.',
        'Choose your two weakest areas. Learn each rule with examples, and make at least 20 rule cards that include your own wrong sentences, corrected.',
        'Run three practice loops of 10 sentences on each weak area, checking each sentence immediately. Record accuracy.',
        'A week later, do a mixed set of 20 English questions and score it.',
    ],
    proof='Your tagged English questions with the weak areas marked, your rule cards, the practice-loop sheets with accuracy, and the mixed-set score.',
    templates=[
        ('English syllabus map', """
ENGLISH MAP     Exam: ______________
Area                 In my syllabus?   PYQs tagged   My errors   Priority
Articles             Y / N             ___           ___         ___
Prepositions         Y / N             ___           ___         ___
Tenses               Y / N             ___           ___         ___
Agreement            Y / N             ___           ___         ___
Voice                Y / N             ___           ___         ___
Reported speech      Y / N             ___           ___         ___
Question tags        Y / N             ___           ___         ___
Synonyms/antonyms    Y / N             ___           ___         ___
One-word substitutes Y / N             ___           ___         ___
Idioms and phrases   Y / N             ___           ___         ___
Spelling/correction  Y / N             ___           ___         ___
""", ''),
        ('rule card format', """
FRONT: [area]: [your wrong sentence with a gap or choice]
BACK:  [correct form] + the rule in one line + one more example
Example:
FRONT: Question tags: You haven't finished, ___ ?
BACK:  have you? A negative statement takes a positive tag. ("She can't swim, can she?")
""", ''),
    ],
    mistakes=[
        ('Learning grammar terms without practising.', 'Rules stick through practice loops with immediate checking.'),
        ('Studying the whole grammar book.', 'Your errors show the two or three areas that matter; start there.'),
        ('Idioms without example sentences.', 'Put each idiom in a sentence on its card.'),
        ('Ignoring spelling.', 'Spelling questions repeat the same tricky words; card them.'),
    ],
    quiz=[
        {'q': 'Choose the correct tag: "He is a doctor, ___?"', 'o': ['isn\'t he', 'is he', 'doesn\'t he', 'wasn\'t he'], 'a': 'A', 'why': 'A positive statement takes a negative tag with the same auxiliary.'},
        {'q': 'Choose the correct verb: "Each of the students ___ a book."', 'o': ['has', 'have', 'are having', 'were having'], 'a': 'A', 'why': '"Each" takes a singular verb.'},
        {'q': 'Which is correct?', 'o': ['an honest man', 'a honest man', 'the honest a man', 'honest an man'], 'a': 'A', 'why': 'The article follows the sound; "honest" starts with a vowel sound.'},
        {'q': 'What is one word for "fear of heights"?', 'o': ['acrophobia', 'claustrophobia', 'hydrophobia', 'xenophobia'], 'a': 'A', 'why': 'Claustrophobia is fear of closed spaces; hydrophobia, of water; xenophobia, of foreigners.'},
        {'q': 'Change to indirect speech: He said, "I am tired."', 'o': ['He said that he was tired.', 'He said that I am tired.', 'He says he is tired.', 'He said that he is being tired.'], 'a': 'A', 'why': 'The pronoun changes and the present tense moves back to the past.'},
    ],
    study='The LearnEnglish grammar pages for your two weakest areas, and the English questions in your saved papers',
    action='Tag 50 English PYQs, make rule cards for your two weakest areas and run three practice loops on each',
)

L3 = lesson(
    M, 3,
    outcome='Improve listening and pronunciation with daily input and shadowing, and practise speaking every week with a simple routine, even without a partner.',
    split='15 minutes reading, 30 minutes resources, 15 minutes a day for two weeks',
    core=f"""
### Listening every day

Listening is input (LRN-M15-L01), and it helps reading, speaking and comprehension questions. Ten to fifteen minutes a day is enough to make progress, if the audio is at the right level: you should understand most of it.

Two free sources do double duty:

- **All India Radio News** in English: national and regional bulletins with audio ({link('newsonair', 'newsonair.gov.in')}). Listening to a bulletin is English practice and current affairs at the same time (Module 10).
- **British Council LearnEnglish:** listening practice at levels from beginner to advanced, with tasks and transcripts, and a speaking section ({link('learnenglish', 'LearnEnglish')}).

### Shadowing

**Shadowing** means speaking along with a recording, a fraction of a second behind the speaker, copying their words, rhythm and intonation, like a shadow. It trains pronunciation, rhythm and listening together.

1. **Choose a clip** of 30 to 60 seconds with a transcript (LearnEnglish has many).
2. **Listen twice** without speaking.
3. **Read the transcript** and check any words you didn't catch.
4. **Shadow with the transcript:** speak along with the audio, three times.
5. **Shadow without the transcript,** three times.
6. **Record yourself** once and compare it with the original.

Honest evidence: shadowing has been studied mostly in small studies, many with learners of English in Japan, with promising results for listening and pronunciation. It is not proven, but it is free, quick and easy to measure with recordings.

### Speaking without a partner

You can practise speaking alone:

- **Talk to yourself** in English while walking or cooking: describe what you are doing.
- **One-minute talks:** pick a PSC topic, speak about it for one minute without notes, and record it. This is also retrieval practice; your Feynman explanations (Module 8) can be in English.
- **Read aloud** a paragraph from your reading practice each day.

With a partner or study group (Module 20), add a weekly 15-minute English conversation on a PSC topic. For posts that include an interview, speaking practice also helps you feel at ease.

### Measure it

Record a one-minute talk and a shadowed clip on day 1. Record the same clip and a new talk on day 14. Listen to both: is your speech smoother, are there fewer long pauses, are hard words clearer?
""",
    example="""
**Anu** could read English well but froze when she had to speak, and she found fast English news hard to follow. She started 15 minutes a day: on most days a 10-minute English bulletin from All India Radio News while she prepared tea, then 5 minutes of shadowing a 45-second LearnEnglish clip.

On day 1 she recorded herself shadowing the clip and giving a one-minute talk on the Kerala renaissance in English. Listening back was uncomfortable: long pauses, and "renaissance" pronounced three different ways.

She kept going for two weeks, with three one-minute talks a week on PSC topics. On day 14 she recorded the same clip and a new talk. Her shadowing kept up with the speaker almost all the way, and her talk had two pauses instead of nine. The news bulletins were easier to follow too, and she started noting their facts for current affairs.
""",
    evidence=[
        ('Daily listening at an understandable level', 'moderate', 'Input is widely accepted as essential for language learning.'),
        ('Shadowing for pronunciation and listening', 'limited', 'Small studies, many with Japanese learners of English; promising, not proven.'),
        ('Recording yourself and comparing over time', 'limited', 'A practical feedback tool; it makes progress audible.'),
    ],
    resources=[
        ('newsonair', 'Listen to one English news bulletin and note three facts', '10 minutes'),
        ('learnenglish', 'Open the listening and speaking sections; choose a clip at your level with a transcript', '20 minutes'),
    ],
    steps=[
        'Choose a 30 to 60 second clip with a transcript at your level. On day 1, record yourself shadowing it and giving a one-minute talk on a PSC topic.',
        'For 14 days, listen for 10 minutes a day (a news bulletin or a LearnEnglish track) and shadow your clip for 5 minutes on at least five days a week.',
        'Give and record three one-minute talks a week on PSC topics, without notes.',
        'Log each day in the listening and speaking log.',
        'On day 14, record the same clip and a new talk. Compare with day 1 and write three lines on what changed.',
    ],
    proof='Your day-1 and day-14 recordings, the two-week log, and your three lines of comparison.',
    templates=[
        ('shadowing steps', """
SHADOWING      Clip: ______________ (30-60 s, with transcript)
[ ] Listen twice, no speaking
[ ] Read the transcript; check words I didn't catch: ____________________
[ ] Shadow with the transcript x3
[ ] Shadow without the transcript x3
[ ] Record once; compare with the original. Hardest words: ______________
""", ''),
        ('listening and speaking log', """
Day | Listened (source, minutes) | Shadowed? | One-minute talk (topic) | Note
1   | ________________________   | Y / N     | ______________________  | recorded [ ]
2   | ________________________   | Y / N     | ______________________  | ______
...
14  | ________________________   | Y / N     | ______________________  | recorded [ ]
""", ''),
    ],
    mistakes=[
        ('Listening to audio far above your level.', 'You should understand most of it; otherwise choose an easier level.'),
        ('Shadowing without ever checking the transcript.', 'Check the words you didn\'t catch, or you will copy mistakes.'),
        ('Never recording yourself.', 'Day-1 and day-14 recordings show progress you can\'t feel.'),
        ('Waiting for a partner before speaking.', 'Self-talk, one-minute talks and reading aloud work alone.'),
    ],
    quiz=[
        {'q': 'What is shadowing?', 'o': ['Speaking along with a recording just behind the speaker, copying rhythm and intonation', 'Reading silently in a dark room', 'Writing a summary of a podcast', 'Translating every word'], 'a': 'A', 'why': 'It trains pronunciation, rhythm and listening together.'},
        {'q': 'What is the honest evidence position on shadowing?', 'o': ['Small studies with promising results; not proven', 'Proven in hundreds of large trials', 'Shown to harm pronunciation', 'Never studied'], 'a': 'A', 'why': 'Many studies are small, often with learners in Japan.'},
        {'q': 'Which free source gives English practice and current affairs at once?', 'o': ['All India Radio News English bulletins', 'A random music channel', 'A paid language app', 'None'], 'a': 'A', 'why': 'News bulletins are listening practice and PSC current affairs together.'},
        {'q': 'How can you practise speaking without a partner?', 'o': ['One-minute recorded talks on PSC topics, self-talk and reading aloud', 'You can\'t', 'Only by listening', 'Only by writing'], 'a': 'A', 'why': 'Speaking alone still gives output practice, and recordings give feedback.'},
    ],
    study='One All India Radio English bulletin and the LearnEnglish listening and speaking sections',
    action='Listen daily, shadow a clip and record one-minute talks for two weeks, comparing day 1 with day 14',
)

L4 = lesson(
    M, 4,
    outcome='Apply the course\'s methods to the Malayalam part of your PSC syllabus, and write a plan for learning a new language with free resources.',
    split='15 minutes reading, 30 minutes resources, 45 minutes action',
    core=f"""
### Part A: PSC Malayalam

Many aspirants neglect Malayalam because it is their own language, then lose easy marks to grammar and vocabulary questions. Malayalam sections in general PSC papers commonly include areas like these; **check your own syllabus**:

{table(['Area', 'Examples (Malayalam terms)'], [
    ('Vocabulary', 'പര്യായപദങ്ങൾ (synonyms), വിപരീതപദങ്ങൾ (antonyms), ഒറ്റപ്പദം (one-word substitution)'),
    ('Grammar', 'സന്ധി (sandhi), സമാസം (samasam), ശരിയായ പ്രയോഗം and വാക്യശുദ്ധി (correct usage, sentence correction)'),
    ('Idioms and proverbs', 'ശൈലികൾ, പഴഞ്ചൊല്ലുകൾ'),
    ('Literature', 'Authors, works, pen names, awards'),
    ('Translation', 'English sentences or phrases into Malayalam'),
])}

The same tools work here:

- **Vocabulary deck:** synonyms and antonyms are perfect for cards, for example the synonyms of സൂര്യൻ (sun) such as ആദിത്യൻ, ഭാനു, രവി and ദിവാകരൻ. Use one card per word, or a cloze per synonym, rather than a list on one card (Module 4).
- **Grammar rule cards** with examples and your own mistakes, plus practice loops (LRN-M15-L02 and Module 13).
- **Literature facts:** cards, acrostics and memory palaces (Module 11). For example, the Malayalam Jnanpith winners in order: G. Sankara Kurup (1965, the first Jnanpith of all), S. K. Pottekkatt (1980), Thakazhi Sivasankara Pillai (1984), M. T. Vasudevan Nair (1995), O. N. V. Kurup (2007) and Akkitham Achuthan Namboothiri (2019) ({link('jnanpith', 'Jnanpith Award list')}).
- **Translation:** practise with previous-year questions and check against the answer keys.

Use your SCERT Malayalam textbooks and previous papers as the main sources ({link('scert', 'SCERT Kerala')}; {link('psc-pyq', 'previous papers')}).

### Part B: any new language

After PSC, you may want Hindi for central government work, Arabic for a job in the Gulf, or German, French or Spanish for interest or study. The system is the same:

1. **A functional goal:** "introduce myself and talk about my work for five minutes", "read a simple notice", not "learn Arabic".
2. **A main free course:** Language Transfer offers free audio courses with no fees, adverts or sign-up, in languages including Arabic, Spanish, French, German, Italian, Greek, Turkish and Swahili ({link('langtransfer', 'Language Transfer')}).
3. **Daily input:** a little listening and reading you mostly understand.
4. **A vocabulary deck** in AnkiDroid with the formats from LRN-M15-L01.
5. **Output:** self-talk, one-minute talks, and later a conversation partner.
6. **Shadowing** short clips for pronunciation (LRN-M15-L03).
7. **A baseline and monthly checks:** a recorded self-introduction now, and every month.

If your PSC exam is near, write the plan now and start after the exam.
""",
    example="""
**Joseph sir** was surprised when his study group's previous-paper analysis showed that several members, all native Malayalam speakers, were losing marks in the Malayalam section. Synonyms, sandhi and pen names were the main problems.

The group built a shared list of Malayalam vocabulary from previous papers and SCERT textbooks; each member made their own cards from it, one synonym per card. Joseph sir taught one sandhi rule each week with examples, and members ran practice loops on it. For literature, Sreeja made a memory palace of the six Malayalam Jnanpith winners in order along the road from her house to the bus stop.

Vinod, who drives an autorickshaw and hopes to work in the Gulf, wrote a new-language plan for Arabic: a goal of a five-minute self-introduction and talk about driving work, Language Transfer's free Arabic course for 20 minutes a day after his PSC exam, and an AnkiDroid deck for words from the course. He recorded his baseline self-introduction: "Marhaba." That was all, and that was fine.
""",
    evidence=[
        ('Spaced retrieval for Malayalam vocabulary and literature facts', 'strong', 'Practice testing and spacing, rated high utility, suit these facts well.'),
        ('Practice loops with rule cards for grammar', 'moderate', 'Immediate feedback on specific weaknesses (Module 13).'),
        ('Free audio courses such as Language Transfer', 'limited', 'No research on this particular course was checked for this course; judge it by your monthly recordings.'),
    ],
    resources=[
        ('psc-pyq', 'Collect the Malayalam questions from your saved papers', '15 minutes'),
        ('scert', 'Find the Malayalam textbook for your level for grammar and vocabulary', '10 minutes'),
        ('jnanpith', 'Check the Malayalam Jnanpith winners and years before making cards', '5 minutes'),
        ('langtransfer', 'Look through the free courses and choose one if you plan a new language', '15 minutes'),
    ],
    steps=[
        'List the Malayalam areas in your exam\'s syllabus, and tag at least 30 Malayalam questions from previous papers by area. Find your two weakest areas.',
        'Make at least 30 Malayalam cards from your weak areas (synonyms, antonyms, idioms, grammar rules or literature facts), checked against your textbook.',
        'Run one practice loop of 10 items on your weakest grammar area, checking each immediately.',
        'Write a new-language plan for one language you want after PSC, using the template.',
        'If your exam is not close, do the first lesson of your chosen free course and record a baseline self-introduction.',
    ],
    proof='Your tagged Malayalam questions, the 30 cards, the practice-loop sheet, and your new-language plan (with a baseline recording if you started).',
    templates=[
        ('PSC Malayalam map', """
MALAYALAM MAP     Exam: ______________
Area                                  In syllabus?   PYQs   My errors   Plan
പര്യായപദങ്ങൾ (synonyms)                Y / N          ___    ___         cards
വിപരീതപദങ്ങൾ (antonyms)                Y / N          ___    ___         cards
ഒറ്റപ്പദം (one-word substitution)        Y / N          ___    ___         cards
സന്ധി / സമാസം (sandhi / samasam)        Y / N          ___    ___         rule cards + loops
ശരിയായ പ്രയോഗം (correct usage)          Y / N          ___    ___         rule cards + loops
ശൈലികൾ / പഴഞ്ചൊല്ലുകൾ (idioms/proverbs) Y / N          ___    ___         cards with examples
Literature (authors, works, awards)    Y / N          ___    ___         cards / palace
Translation                            Y / N          ___    ___         PYQ practice
""", ''),
        ('new-language plan', """
NEW LANGUAGE PLAN      Language: __________   Start date: ______
Goal (what I will be able to DO): ___________________________________
Main free course: ______________________   Minutes a day: ___
Daily input (listening/reading): ______________________________
Vocabulary deck: Lang::__________::Vocabulary   new cards a day: ___
Output: self-talk [ ]  one-minute talks [ ]  partner (later): ______
Shadowing clips from: ______________________
Baseline (recorded self-introduction) on ______; monthly checks on ______
""", ''),
    ],
    mistakes=[
        ('Ignoring Malayalam because it is your own language.', 'PSC Malayalam tests grammar and vocabulary you may not use every day. Check your error data.'),
        ('Literature lists without hooks.', 'Use cards, acrostics or a memory palace, after checking the facts.'),
        ('Putting all synonyms of a word on one card.', 'One card or one cloze per synonym.'),
        ('Starting a new language just before the exam.', 'Write the plan now; start when the exam is over.'),
    ],
    quiz=[
        {'q': 'Which is a synonym (പര്യായം) of സൂര്യൻ?', 'o': ['ആദിത്യൻ', 'ചന്ദ്രൻ', 'സമുദ്രം', 'പർവതം'], 'a': 'A', 'why': 'ആദിത്യൻ, ഭാനു, രവി and ദിവാകരൻ are synonyms of സൂര്യൻ.'},
        {'q': 'Who received the first Jnanpith Award, in 1965?', 'o': ['G. Sankara Kurup', 'Thakazhi Sivasankara Pillai', 'O. N. V. Kurup', 'M. T. Vasudevan Nair'], 'a': 'A', 'why': 'He was the first recipient of the award in any language.'},
        {'q': 'Which is a well-written goal for a new language?', 'o': ['"Introduce myself and talk about my work for five minutes"', '"Learn Arabic"', '"Be fluent soon"', '"Watch Arabic films"'], 'a': 'A', 'why': 'A functional goal can be tested and measured.'},
        {'q': 'What does Language Transfer offer?', 'o': ['Free audio language courses, run on donations', 'Paid coaching only', 'Malayalam grammar notes', 'PSC mock tests'], 'a': 'A', 'why': 'Its courses have no fees, adverts or sign-up.'},
    ],
    study='The Malayalam questions in your saved papers, your SCERT Malayalam textbook and (optionally) Language Transfer',
    action='Map PSC Malayalam, make 30 cards from your weak areas, run one loop and write a new-language plan',
)

LESSONS = [L1, L2, L3, L4]

MODULE = module(
    M,
    overview="""
Learn languages the way the research suggests: lots of understandable input, regular output with feedback, and vocabulary with spaced repetition. Apply it to PSC English and Malayalam, improve listening and pronunciation with shadowing, and plan any new language for after PSC.

Language questions are some of the most learnable marks in a PSC paper, and English and Malayalam skills keep paying off long after the exam. This module uses the tools you already have (AnkiDroid, practice loops, previous-paper analysis and recordings) and adds the two habits that matter most for language: daily input and daily vocabulary.

The result is a language routine: a vocabulary deck, rule cards from your own mistakes, a listening and shadowing habit, and a plan for your next language.
""",
    outcomes=[
        'Explain the roles of input, output and vocabulary',
        'Build a vocabulary deck with meaning, production, cloze and phrase cards',
        'Find and fix your weakest PSC English areas with rule cards and practice loops',
        'Improve listening and pronunciation with daily input and shadowing, measured by recordings',
        'Apply the same methods to PSC Malayalam and plan a new language',
    ],
    lessons=LESSONS,
    tools=[
        'The **vocabulary card formats** and **word-capture list**',
        'The **English syllabus map** and **rule card format**',
        'The **shadowing steps** and **listening and speaking log**',
        'The **PSC Malayalam map** and **new-language plan**',
    ],
    project='My language routine',
    project_steps=[
        'Grow your English (or Malayalam) vocabulary deck to at least 100 notes, all from words you have met.',
        'Show the accuracy trend from your English grammar practice loops and one Malayalam loop.',
        'Keep your day-1 and day-14 listening and speaking recordings with your comparison.',
        'Write your daily and weekly language routine on one card, and your new-language plan for after PSC.',
    ],
    project_proof='A screenshot of your vocabulary deck with 100 or more notes, your practice-loop sheets, the two recordings with comparison, and your routine card and plan.',
    rubric=[
        ('Vocabulary', 'Word lists only', 'A deck with meaning cards only', '100 or more notes from real reading, with production and cloze cards'),
        ('Grammar', 'Studying the whole grammar book', 'Weak areas known', 'Weak areas fixed with rule cards and loops, accuracy rising'),
        ('Listening and speaking', 'None', 'Some listening', 'Daily listening, shadowing and recorded talks compared over two weeks'),
        ('Malayalam and new language', 'Malayalam ignored', 'Malayalam cards made', 'Malayalam loops and cards, and a new-language plan written'),
    ],
    short=[
        'Add five words a day from your reading to a vocabulary deck.',
        'Run one practice loop a week on your weakest English or Malayalam area.',
    ],
    flashcards=[
        ('The three things every language is learned through', 'Input, output and vocabulary.'),
        ('Production card', 'Meaning on the front, the word on the back: it trains using the word.'),
        ('Why example sentences on vocabulary cards', 'Words live in phrases; the sentence shows how they are used.'),
        ('Question tag for a positive statement', 'A negative tag: "He is a doctor, isn\'t he?"'),
        ('Shadowing', 'Speaking along with a recording, just behind the speaker.'),
        ('Evidence for shadowing', 'Small studies with promising results; not proven.'),
        ('First Jnanpith Award', 'G. Sankara Kurup, in 1965.'),
        ('A free source of audio language courses', 'Language Transfer.'),
    ],
    mistakes=[
        ('Collecting word lists instead of meeting words in reading.', 'Learn words from your reading and papers, with their sentences.'),
        ('Practising only the language skills you enjoy.', 'Your error data chooses your next practice loop.'),
    ],
)
