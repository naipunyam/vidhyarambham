"""Module 12: Exam mastery for Kerala PSC."""
from common import lesson, module, link, rules, fence, table
import tools

M = 12

L1 = lesson(
    M, 1,
    outcome='Turn your exam\'s official syllabus into a Syllabus tab of topics with weights, previous-paper counts and confidence ratings, and pick your top priorities with a simple formula.',
    split='15 minutes reading, 30 minutes resources, 45 minutes building the tab',
    core=f"""
### The syllabus is the contract

Everything in your exam comes from the official syllabus, and everything outside it is optional. Many aspirants study from a coaching centre's list or a guide's chapters and never read the official syllabus closely. Kerala PSC publishes a syllabus for each post ({rules('psc-syllabus', 'post-wise syllabus page')}). You downloaded yours in week 0; now you turn it into a working tool.

Notices often state the total marks and the duration. For example, the 2022 notice for the Degree Level Common Preliminary Examination gave 100 marks and 1 hour 15 minutes, with questions in English and in Malayalam, Tamil or Kannada ({rules('psc-cpe-2022', 'Kerala PSC notice, 2022')}). Many syllabuses also list marks for each part, such as general knowledge, current affairs, simple arithmetic and mental ability, English and Malayalam. Check exactly what yours says; schemes differ between exams and change over time.

### Building the Syllabus tab

1. **List every part** of the syllabus with its marks, if given.
2. **Break each part into topics** small enough to study in one to three sessions: not "History" but "Kerala renaissance: reformers and organisations", "Freedom struggle: 1885–1919" and so on. Aim for 10 to 40 topics per part.
3. **Add the marks share** of each part (if given) and, after LRN-M12-L02, the **number of previous-year questions** on each topic.
4. **Rate your confidence** from 1 to 5 using a delayed recall test, not a feeling (Module 7).
5. **Add status, source and next review** for each topic.

### Choosing priorities

A simple priority score combines how often a topic is asked with how weak you are in it:

{fence('Priority = (PYQ count + 1) × (6 − confidence)')}

A topic asked 6 times with confidence 2 scores 7 × 4 = 28. A topic asked twice with confidence 4 scores 3 × 2 = 6. Sort by priority and you have your study order. The "+ 1" keeps topics that haven't been asked yet from scoring zero; they can still appear.

Use the score as a guide, not a law. A low-priority topic that takes 20 minutes to learn may be worth doing early, and topics that support others (basic arithmetic, the structure of the Constitution) come first whatever their score.
""",
    example="""
**Anu** mapped the syllabus for the Degree Level preliminary she was preparing for. Her syllabus PDF listed its parts with marks; she broke them into 64 topics, from "Kerala renaissance" to "Ratio and proportion" to "Malayalam: synonyms (പര്യായപദങ്ങൾ)".

She rated confidence with two-minute recall tests over three evenings (Module 7) instead of guessing. Twelve topics she had thought were strong got a 2 or 3. After counting previous-year questions in LRN-M12-L02, she filled in the priority formula and sorted.

Her top ten surprised her: three were in mental ability, which she had been avoiding, and two in English grammar, which she had assumed was easy. Kerala history, which she had studied most, ranked eleventh. She printed the top ten and taped it inside her notebook cover.
""",
    evidence=[
        ('Studying from the official syllabus', 'limited', 'Common sense rather than research: the exam is set from it. It prevents wasted time.'),
        ('Prioritising by question frequency and weakness', 'limited', 'A practical planning rule; past patterns guide but do not guarantee future papers.'),
        ('Rating confidence with delayed recall instead of feeling', 'moderate', 'Feelings of knowing are often wrong (Module 7); recall tests are more accurate.'),
    ],
    resources=[
        ('psc-syllabus', 'Download the syllabus for your post again if needed, and read it line by line', '15 minutes'),
        ('psc-cpe-2022', 'See how a notice states marks, duration and the language of questions', '5 minutes'),
        ('os-cs-3', 'Read 3.5 on prioritisation', '10 minutes'),
    ],
    steps=[
        'Add a Syllabus tab to your Learning Workbook with the headings below, plus a "Priority" column.',
        'Enter every part of your exam\'s official syllabus, broken into topics of one to three sessions each.',
        'Enter the marks for each part, if your syllabus gives them.',
        'Rate your confidence in each topic from 1 to 5 using a two-minute recall test (spread over several days if needed).',
        'Add the priority formula, sort by priority, and write your top ten topics. (You will add the PYQ counts in the next lesson and re-sort.)',
    ],
    proof='A screenshot of your Syllabus tab with every topic, and your top-ten priority list.',
    templates=[
        ('Syllabus tab headings', tools.SYLLABUS + ',Priority', 'csv'),
        ('priority formula', """
With PYQ count in D2 and confidence (1-5) in E2, in the Priority column (I2):
=(D2+1)*(6-E2)
Copy down. Then sort the tab by Priority, largest first (Data -> Sort range).
""", ''),
        ('syllabus breakdown sheet', """
EXAM: ______________________  Syllabus file: ______________  Date: ______
Part (as in the syllabus)       Marks   Topics (1-3 sessions each)
1. ___________________________  ___     ______________________________________
2. ___________________________  ___     ______________________________________
3. ___________________________  ___     ______________________________________
...
Total topics: ___   Topics rated by recall test: ___
""", ''),
    ],
    mistakes=[
        ('Using a coaching centre\'s list instead of the official syllabus.', 'Start from the official PDF; use guides only as sources for each topic.'),
        ('Topics that are too big.', '"History" can\'t be scheduled. Break it into topics of one to three sessions.'),
        ('Rating confidence by feeling.', 'Use a two-minute recall test; feelings of knowing mislead.'),
        ('Never updating the tab.', 'Update confidence after every review and re-sort every four weeks.'),
    ],
    quiz=[
        {'q': 'Topic A was asked 6 times and your confidence is 2. Topic B was asked twice and your confidence is 4. Which has the higher priority score?', 'o': ['A (28 against 6)', 'B (6 against 28)', 'They are equal', 'Neither has a score'], 'a': 'A', 'why': '(6 + 1) × (6 − 2) = 28; (2 + 1) × (6 − 4) = 6.'},
        {'q': 'Where should your list of topics come from?', 'o': ['The official syllabus for your post on the Kerala PSC website', 'A coaching centre\'s advertisement', 'A WhatsApp forward', 'The chapters of any guide'], 'a': 'A', 'why': 'The exam is set from the official syllabus.'},
        {'q': 'What did the 2022 Degree Level preliminary notice state?', 'o': ['100 marks and 1 hour 15 minutes', '200 marks and 3 hours', '50 marks and 30 minutes', 'No time limit'], 'a': 'A', 'why': 'Check your own exam\'s notice; schemes differ.'},
        {'q': 'Why add 1 to the PYQ count in the priority formula?', 'o': ['So topics not yet asked don\'t score zero', 'To make the numbers bigger', 'Because PSC adds one mark', 'It is a mistake'], 'a': 'A', 'why': 'Unasked syllabus topics can still appear.'},
    ],
    study='Your exam\'s official syllabus, the 2022 preliminary notice and College Success 3.5',
    action='Build your Syllabus tab with confidence ratings and a priority list',
)

L2 = lesson(
    M, 2,
    outcome='Tag at least 200 previous-year questions by subject and topic, count the patterns into your Syllabus tab, and turn your misses into cards.',
    split='15 minutes reading, 30 minutes resources, 75 minutes tagging (it can be split over several days)',
    core=f"""
### Why previous-year questions matter

Previous-year questions (PYQs) are the best free study material you have. They show:

- **What is asked:** which topics, and which details within them
- **How deeply:** a name, a reason, a calculation, a statement to judge
- **In what form:** direct questions, statement questions, match the following, odd one out
- **What repeats:** facts and topics asked again and again across years

Kerala PSC publishes previous question papers by year, post, paper code and test date ({link('psc-pyq', 'previous question papers')}), and answer keys for OMR exams ({rules('psc-keys', 'answer keys')}). Use the **final** answer key, not the provisional one, when you check answers.

### Choosing papers

Pick papers for **your post or the same level** (for example, all degree-level preliminaries, or several LDC papers) from the last three to five years. Two or three papers of 100 questions give you a solid first picture.

### Tagging

Add a **PYQ** tab and give each question one row: the paper, question number, subject, topic (copied **exactly** from your Syllabus tab, so formulas can count it), subtopic, type (fact, concept, calculation, statement), whether it repeats an earlier question, whether it was in your study material, and whether you got it right when you first tried it.

Then count. In your Syllabus tab, a formula counts how many PYQs match each topic:

{fence('''In the Syllabus tab, PYQ count for the topic in B2 (D2):
=COUNTIF(PYQ!D:D,B2)
LibreOffice may need: =COUNTIF($PYQ.D:D;B2)''')}

A pivot table (Insert → Pivot table in Google Sheets; Data → Pivot Table in LibreOffice) shows counts by subject and by type in seconds.

### What to look for

1. **Which topics are asked most** for your exam
2. **Repeated facts:** the same fact asked in different years. These are among the highest-value facts you can learn.
3. **Question types:** if a third of the questions are statement questions, practise them (LRN-M08-L02).
4. **Gaps:** questions on things that weren't in your material at all. Find a source for them.

### Two cautions

- **Patterns guide, they don't guarantee.** Syllabuses change, and examiners ask new things. Don't drop syllabus topics that haven't been asked yet; just give them lower priority.
- **Tagging is not studying.** Its value comes from what you do next: every question you got wrong, guessed or didn't know becomes a card, a note or a Revision-tab entry.
""",
    example="""
**Ashiq** downloaded three degree-level preliminary papers from the last three years and their final answer keys. Tagging 300 questions took him four evenings of about an hour each.

His counts showed things he hadn't seen while simply solving papers. In his three papers, mental ability and arithmetic together made up a large and steady share. In GK, the Constitution and Kerala history were asked every year, while some topics in his guide had never appeared. He found 14 facts asked in two or more of the three papers; they became a special AnkiDroid sub-deck called "Repeated".

He also counted how many questions came from facts he had never seen in his material: 23 of 300. Most were current affairs or recent government schemes, which sent him back to the routine in LRN-M10-L04. He turned his 61 wrong or unknown questions into cards over the next week, within his daily budget.
""",
    evidence=[
        ('Practising with previous-year questions', 'strong', 'Practice testing is rated high utility; PYQs are the closest practice to the real exam.'),
        ('Using question frequency to set priorities', 'limited', 'Sensible, but patterns can change between years and exams.'),
        ('Turning missed questions into cards and notes', 'strong', 'Retrieval with feedback, targeted at your real gaps.'),
    ],
    resources=[
        ('psc-pyq', 'Download two or three papers for your post or level from recent years', '20 minutes'),
        ('psc-keys', 'Find the final answer keys for the same papers', '10 minutes'),
    ],
    steps=[
        'Add a PYQ tab to your Learning Workbook with the headings below.',
        'Choose two or three recent papers for your post or level (at least 200 questions) with their final answer keys.',
        'Answer each question first (options covered, confidence marked, as in Module 7), then check, and tag it in the PYQ tab. Copy topic names exactly from the Syllabus tab.',
        'Add the COUNTIF formula to the Syllabus tab, re-sort by priority, and write your top 15 topics.',
        'List the repeated facts and make them cards. Then, over the next week, turn every wrong, guessed or unknown question into cards or Revision-tab entries within your daily budget.',
    ],
    proof='Your PYQ tab with at least 200 tagged rows, the Syllabus tab with PYQ counts and the new top 15, and your list of repeated facts.',
    templates=[
        ('PYQ tab headings', tools.PYQ, 'csv'),
        ('PYQ pattern summary', """
PYQ PATTERN SUMMARY     Papers: ___________________________  Questions: ___
Most-asked topics (top 5): 1. ______ 2. ______ 3. ______ 4. ______ 5. ______
Question types: fact ___%  concept ___%  calculation ___%  statement ___%
Repeated facts (asked 2+ times): ___  -> "Repeated" sub-deck made [ ]
Questions on things not in my material: ___  -> new source needed for: ______
Right at first try: ___%   Wrong or unknown -> cards / Revision tab: ___
""", ''),
    ],
    mistakes=[
        ('Solving PYQs without tagging them.', 'Tagging shows patterns that solving alone hides.'),
        ('Topic names that don\'t match the Syllabus tab.', 'Copy them exactly, or COUNTIF won\'t count them.'),
        ('Treating patterns as guarantees.', 'Lower the priority of unasked topics; don\'t delete them.'),
        ('Checking with the provisional key.', 'Use the final answer key; provisional keys can change after complaints.'),
    ],
    quiz=[
        {'q': 'Which answer key should you use to check previous papers?', 'o': ['The final answer key', 'The provisional key only', 'A coaching centre\'s key', 'Your own guess'], 'a': 'A', 'why': 'Provisional keys can be revised after complaints.'},
        {'q': 'Why must topic names in the PYQ tab match the Syllabus tab exactly?', 'o': ['So the COUNTIF formula can count them', 'Because PSC requires it', 'To make the sheet look neat', 'It doesn\'t matter'], 'a': 'A', 'why': 'COUNTIF matches text exactly.'},
        {'q': 'What are "repeated facts"?', 'o': ['Facts asked in two or more different years\' papers', 'Facts you studied twice', 'Facts that appear in two textbooks', 'Facts you got wrong twice'], 'a': 'A', 'why': 'They are among the highest-value facts to learn.'},
        {'q': 'A syllabus topic hasn\'t appeared in your three papers. What should you do?', 'o': ['Give it lower priority but keep it on the plan', 'Delete it from your plan', 'Study it first', 'Complain to PSC'], 'a': 'A', 'why': 'Patterns guide but don\'t guarantee; it can still be asked.'},
    ],
    study='Two or three previous papers and their final answer keys from the Kerala PSC website',
    action='Tag at least 200 PYQs, count them into your Syllabus tab and turn the misses into cards',
)

L3 = lesson(
    M, 3,
    outcome='Take a full mock test under real conditions, record every wrong or guessed answer in the Errors tab, and fix each error by its type.',
    split='10 minutes reading, 20 minutes resources, a full mock (about 75 minutes) plus 60 minutes of analysis',
    core=f"""
### A mock is a rehearsal

A **mock test** is a full paper taken under exam conditions: the same number of questions, the same time limit, an answer sheet like the real one, no phone, no breaks, and ideally at the same time of day as your exam. The best free mocks are **previous papers you haven't seen yet**. Keep a few unseen papers aside for this.

A mock does three jobs: it is retrieval practice on the whole syllabus, it trains your timing, and it makes the exam hall feel familiar.

### Answer sheets and marking

Kerala PSC's instructions for OMR exams say that each correct answer gets 1 mark and each wrong answer loses one-third of a mark, and that marking more than one answer, or altering an answer, also counts against you ({rules('psc-omr', 'OMR instructions')}). Practise on an OMR-style sheet (print one, or draw rows of four bubbles) so that shading carefully becomes a habit.

Score your mock the same way:

{fence('Score = correct answers − (wrong answers ÷ 3)        unanswered = 0\nExample: 60 correct, 15 wrong, 25 unanswered -> 60 − 5 = 55')}

### The analysis is where you learn

The mock takes 75 minutes; the analysis should take about as long. Go through **every question you got wrong, and every one you got right by guessing** (your S, U and G marks from Module 7 show these). Add each to the **Errors** tab with its error type:

{table(['Code', 'Error type', 'Fix'], [(c, m, f) for (c, m), f in zip(tools.ERROR_TYPES, ['1 to 3 cards, or add the topic to the Revision tab', '1 to 3 cards; check the topic\'s review dates', 'One card contrasting the two facts side by side', 'Underline NOT, EXCEPT, FIRST, LARGEST in every question for a week', 'Slow down on the last step; check the bubble number', 'Guess only after ruling out at least one option (LRN-M12-L04)', 'Use the two-pass method and time checkpoints (LRN-M12-L04)'])])}

### Retest your errors

Seven days later, answer each logged question again from memory. Clear an error only when you get it right **twice** in separate retests. Errors that keep coming back go to your weekly review.

### How often?

Start with a mock every two weeks while you are still learning topics. In the last weeks before the exam, one a week (LRN-M12-L05). More mocks without analysis teach little; fewer mocks with careful analysis teach a lot.
""",
    example="""
**Sreeja** took her first full mock with a 2021 paper she had kept unseen. She set a 75-minute timer at the dining table at 10 a.m., the usual start time of her exam, used a hand-drawn OMR sheet, and marked S, U or G beside each answer.

Her result: 52 correct, 20 wrong, 28 unanswered: 52 − 20 ÷ 3 = 45.33. The analysis took an hour. Of her 20 wrong answers and 7 guessed-right ones, she logged 8 as K (didn't know), 6 as F (forgot), 4 as I (mixed up two facts), 5 as M (misread) and 4 as C (careless). Five misreadings shocked her: three questions had "NOT" in them.

Her fixes: 14 new cards, 4 contrast cards, a week of underlining NOT and EXCEPT in every question she practised, and a rule to recheck the bubble number every tenth question. A week later her retest cleared 19 of the 27 errors on the first try.
""",
    evidence=[
        ('Full practice tests', 'strong', 'Practice testing is rated high utility; full mocks also train timing.'),
        ('Reviewing errors with the correct answers (feedback)', 'strong', 'Feedback after testing corrects errors so they don\'t repeat.'),
        ('Sorting errors by type', 'limited', 'A practical way to choose the right fix; little direct research on the categories.'),
    ],
    resources=[
        ('psc-omr', 'Read the instructions for OMR exams, especially marking and shading rules', '10 minutes'),
        ('os-cs-6-3', 'Read the parts on test day and after the test', '15 minutes'),
        ('psc-pyq', 'Choose an unseen recent paper for your post or level as your mock', '5 minutes'),
    ],
    steps=[
        'Take a full mock: an unseen previous paper, the real time limit, an OMR-style sheet, no phone, ideally at your exam\'s time of day. Mark S, U or G beside each answer.',
        'Score it: correct − wrong ÷ 3. Record the score in your Weekly tab.',
        'Add an Errors tab with the headings below. Log every wrong answer and every guessed-right answer, with its type, why it happened and the fix.',
        'Apply the fixes: cards, contrast cards, notes and reading rules.',
        'Put a retest date seven days later in the Errors tab, and do the retest.',
    ],
    proof='A photo of your answer sheet, your score calculation, your Errors tab with types and fixes, and the retest results.',
    templates=[
        ('Errors tab headings', tools.ERROR_LOG, 'csv'),
        ('error log rules (core tool)', tools.ERROR_LOG_TEXT, ''),
        ('mock test conditions', """
MOCK TEST     Paper: ______________ (unseen [ ])   Date: ______   Start: ____
[ ] Real time limit: ___ minutes    [ ] Real number of questions: ___
[ ] OMR-style sheet (printed or drawn)  [ ] Blue or black ball-point pen
[ ] Phone in another room           [ ] No breaks, no notes
[ ] S / U / G marked beside every answer
Score: correct ___ − wrong ___ ÷ 3 = ___   Unanswered: ___
Analysis done (all wrong + guessed-right logged): [ ]   Time spent: ___ min
""", ''),
    ],
    mistakes=[
        ('Taking mocks without analysing them.', 'The analysis is where the learning happens. Spend as long on it as on the mock.'),
        ('Logging only wrong answers.', 'Guessed-right answers are also gaps. Log them.'),
        ('Vague reasons ("silly mistake").', 'Use the error types; each type has a different fix.'),
        ('Never retesting errors.', 'Retest after seven days; clear an error only when it is right twice.'),
    ],
    quiz=[
        {'q': 'Under Kerala PSC\'s OMR marking, what is the score for 60 correct, 15 wrong and 25 unanswered?', 'o': ['55', '60', '45', '50'], 'a': 'A', 'why': '60 − 15 ÷ 3 = 55; unanswered questions score 0.'},
        {'q': 'Which questions go into the Errors tab after a mock?', 'o': ['Every wrong answer and every guessed-right answer', 'Only wrong answers', 'Only questions you skipped', 'Only maths questions'], 'a': 'A', 'why': 'A lucky guess hides a real gap.'},
        {'q': 'You answered a question wrongly because you missed the word NOT. Which error type is it?', 'o': ['M: misread', 'K: didn\'t know', 'C: careless calculation', 'T: time'], 'a': 'A', 'why': 'The fix is to underline NOT and EXCEPT in every question for a while.'},
        {'q': 'When can you clear an error from the log?', 'o': ['When you get it right in two separate retests', 'As soon as you read the right answer', 'After one week whatever happens', 'Never'], 'a': 'A', 'why': 'Two correct retests show the fix has stuck.'},
    ],
    study='Kerala PSC\'s OMR instructions and College Success 6.3 on test day',
    action='Take a full mock under real conditions, log and fix every error, and retest after a week',
)

L4 = lesson(
    M, 4,
    outcome='Plan your time in the exam hall with a two-pass method and checkpoints, and decide when to guess using the arithmetic of negative marking and your own calibration data.',
    split='20 minutes reading, 15 minutes resources, 30 minutes calculation plus your next mock',
    core=f"""
### The arithmetic of negative marking

Kerala PSC's OMR instructions give **+1 for a correct answer and −1/3 for a wrong one**; unanswered questions score 0 ({rules('psc-omr', 'OMR instructions')}). With four options, the **expected value** of answering depends on your chance of being right, p:

{fence('''Expected marks from answering = p × 1 − (1 − p) × 1/3

Blind guess among 4 options (p = 1/4):   1/4 − 3/4 × 1/3 = 0        (no gain on average)
One option ruled out (p = 1/3):          1/3 − 2/3 × 1/3 = 1/9      (about +0.11)
Two options ruled out (p = 1/2):         1/2 − 1/2 × 1/3 = 1/3      (about +0.33)
"Unsure" answers that are right 60%:     0.6 − 0.4 × 1/3 ≈ 0.47

Break-even: p − (1 − p)/3 = 0  ->  p = 1/4''')}

So, under this scheme, **answering pays on average whenever your chance of being right is above 1 in 4**. A blind guess gains nothing on average and only adds risk. But as soon as you can rule out even one option, answering is worth it on average.

Your calibration table from Module 7 tells you your real chances. If your "unsure" answers are right 55% of the time, you should almost always answer them. If your guesses after ruling out two options are right about half the time, answer those too.

This is arithmetic, not a guarantee: on a single question you can still lose a third of a mark. Over a whole paper, following the rule raises your expected score. Check the marking scheme in your own exam's instructions; if it differs, redo the calculation.

### Time: the two-pass method

Work out your time per question first. In the 2022 Degree Level preliminary (100 marks at one mark a question, in 1 hour 15 minutes), that is 45 seconds a question ({rules('psc-cpe-2022', '2022 notice')}).

1. **Pass 1 (about 60% of the time):** go through every question. Answer the ones you know (S) immediately and shade them. Mark the doubtful ones (U, G) in the way your exam allows, and skip long calculations.
2. **Pass 2 (about 30%):** return to the marked questions. Rule out options, use the break-even rule, and do the skipped calculations.
3. **Last 10% of the time:** check that every shaded bubble matches its question number. Don't change answers without a clear reason.

OpenStax *College Success* gives the same core advice: answer the questions you are confident about first, skip very difficult ones and return, and keep time at the end to review ({link('os-cs-6-3', 'College Success 6.3')}).

### Time checkpoints

Before the exam, write your checkpoints: for 100 questions in 75 minutes, you want to be at about question 25 by minute 12, question 50 by minute 23 and question 100 by minute 45 in pass 1. Practise them in every mock and record where you actually were.
""",
    example="""
**Ashiq** used to skip every question he wasn't sure of, about 25 per mock, because he feared negative marks. His calibration table from Module 7 said his guesses after ruling out two options were right about half the time.

He did the arithmetic: at p = 1/2, each such answer is worth +1/3 of a mark on average. In his next mock he used the two-pass method and answered the doubtful questions where he could rule out at least one option. He answered 12 more questions than usual; 6 were right and 6 wrong, which gave him 6 − 2 = +4 marks compared with skipping them.

His timing checkpoints showed something else: he reached question 50 at minute 31, eight minutes behind plan, because he solved every calculation in pass 1. In the following mock he skipped long calculations in pass 1 and finished pass 1 at minute 46, with time to check every bubble.
""",
    evidence=[
        ('The expected value of answering under +1 and −1/3 marking', 'strong', 'This is arithmetic, not research: it holds whenever the scheme is +1 and −1/3 with four options.'),
        ('Using your own calibration data to decide when to answer', 'limited', 'A practical use of Module 7\'s data; your calibration can change, so update it after each mock.'),
        ('The two-pass method and time checkpoints', 'limited', 'Standard test-taking advice (College Success 6.3); judge it by your mock timing and scores.'),
    ],
    resources=[
        ('psc-omr', 'Read the marking rules in the OMR instructions', '10 minutes'),
        ('psc-cpe-2022', 'Note the marks and duration in the 2022 notice as an example', '5 minutes'),
        ('os-cs-6-3', 'Reread the multiple-choice advice', '10 minutes'),
    ],
    steps=[
        'Read your own exam\'s marking instructions and write down the scheme. If it isn\'t +1 and −1/3 with four options, redo the break-even calculation.',
        'Fill in the guessing calculator below with your calibration data from Module 7 and your latest mock.',
        'Work out your time per question and your three pass-1 checkpoints.',
        'In your next mock, use the two-pass method, the checkpoints and the break-even rule. Note where you were at each checkpoint.',
        'Compare with your previous mock: questions answered, accuracy, net score and time left at the end.',
    ],
    proof='Your filled-in guessing calculator, your timing plan, the next mock\'s checkpoint times and the comparison with your previous mock.',
    templates=[
        ('guessing calculator', """
MARKING SCHEME (from my exam's instructions): +___ correct, −___ wrong, options ___
Break-even chance: p where p × (right mark) = (1 − p) × (wrong mark) -> p = ___
My data (from calibration and mocks):
  "Unsure" answers right: ___%   -> answer them?  yes / no
  Guesses after ruling out 1 option right: ___%   -> answer?  yes / no
  Guesses after ruling out 2 options right: ___%  -> answer?  yes / no
  Blind guesses right: ___%  (expected value about 0: skip unless I want the risk)
My rule: I answer when ______________________________________________
""", ''),
        ('two-pass time plan', """
Questions ___   Minutes ___   Seconds per question = minutes × 60 ÷ questions = ___
PASS 1 (about 60% of time = ___ min): answer S, mark U and G, skip long calculations
  Checkpoints: Q25 by min ___   Q50 by min ___   Q100 by min ___
PASS 2 (about 30% = ___ min): marked questions, rule out options, calculations
CHECK (last 10% = ___ min): every bubble matches its question number
Actual in this mock: Q25 at ___  Q50 at ___  end of pass 1 at ___  time left ___
""", ''),
    ],
    mistakes=[
        ('Blind guessing on every question.', 'A blind guess gains nothing on average and adds risk. Rule out options first.'),
        ('Skipping everything you are unsure of.', 'If your unsure answers are right more than 1 time in 4, answering pays on average.'),
        ('Spending minutes on one hard question in pass 1.', 'Mark it and move on; come back in pass 2.'),
        ('Not checking the bubbles.', 'One shifted row can cost many marks. Keep the last minutes for checking.'),
        ('Assuming the marking scheme.', 'Read your own exam\'s instructions; schemes can differ.'),
    ],
    quiz=[
        {'q': 'Under +1 and −1/3 marking with four options, what is the expected value of a blind guess?', 'o': ['0', '+1/4', '−1/3', '+1/2'], 'a': 'A', 'why': '1/4 × 1 − 3/4 × 1/3 = 0.'},
        {'q': 'You can rule out two of the four options. What is the expected value of answering?', 'o': ['+1/3', '0', '−1/6', '+1'], 'a': 'A', 'why': '1/2 − 1/2 × 1/3 = 1/3.'},
        {'q': 'Above what chance of being right does answering pay on average under this scheme?', 'o': ['1 in 4', '1 in 2', '3 in 4', '1 in 10'], 'a': 'A', 'why': 'Break-even: p − (1 − p)/3 = 0 gives p = 1/4.'},
        {'q': 'An exam has 100 questions in 75 minutes. How many seconds per question is that?', 'o': ['45', '75', '60', '30'], 'a': 'A', 'why': '75 × 60 ÷ 100 = 45 seconds.'},
        {'q': 'What happens in pass 1 of the two-pass method?', 'o': ['Answer the questions you know, mark doubtful ones and skip long calculations', 'Solve every question in order, however long it takes', 'Check all the bubbles', 'Guess every question'], 'a': 'A', 'why': 'Secure the sure marks first; return to the rest in pass 2.'},
    ],
    study='The marking rules in the OMR instructions, the 2022 notice and College Success 6.3',
    action='Calculate your guessing rule from your own data and use the two-pass method in your next mock',
)

L5 = lesson(
    M, 5,
    outcome='Build a complete 12-week PSC study and revision plan from your syllabus map, PYQ analysis and real weekly hours, with revision cycles and mocks built in.',
    split='15 minutes reading, 15 minutes resources, 90 minutes building the plan',
    core=f"""
### What goes into the plan

A good plan starts from facts, not hopes:

- **The exam date,** or a target date 12 weeks away if your exam date isn't announced yet. Kerala PSC lists exam programmes under its exam schedule ({rules('psc-home', 'Kerala PSC website')}).
- **Your real weekly hours** for PSC study, from your Study Log, not the hours you wish you had.
- **Your priorities** from the Syllabus tab (LRN-M12-L01) and PYQ analysis (LRN-M12-L02).
- **Your current mock score** (LRN-M12-L03), so you can track progress.
- **Your daily routines:** AnkiDroid, Revision-tab reviews and the Sunday weekly review.

### A default 12-week structure

{table(['Weeks', 'Phase', 'How the time splits (a sensible default)', 'Mocks'], [
    ('1–8', 'Learn and revise', 'About 60% new topics in priority order, 25% spaced reviews (Revision tab and AnkiDroid), 15% mixed practice and PYQs', 'One every two weeks (weeks 2, 4, 6, 8)'),
    ('9–11', 'Revision cycles and mocks', 'A full revision cycle through every topic by recall, weak-topic sprints, few new topics', 'One a week, with full analysis'),
    ('12', 'Taper', 'Short reviews, error-log retests, sleep, logistics; nothing new in the last three days', 'One early in the week'),
])}

The percentages are a starting point, not research. Adjust them in your weekly reviews.

### Revision cycles

A **revision cycle** goes through every topic once, by recall, in priority order. Cycle 1 runs through weeks 9 and 10; cycle 2 through week 11, faster, focusing on ambers and reds from your traffic-light check; a light cycle 3 in week 12 uses only cue questions, cards and the error log. Every review starts with recall, never with rereading (Module 3).

### The capacity check

Multiply your weekly hours by the weeks for each phase and compare with the number of topics. If the topics don't fit, don't pretend: cut or shorten the lowest-priority topics, or plan them for a lighter depth (key facts on cards only). A realistic plan you follow beats an ideal plan you abandon in week 3.

### Each week

Every week of the plan becomes a filled-in **weekly study planner** (LRN-M05-L02), written on Sunday in your weekly review, with if-then plans for your three priorities (Module 6). Each day has the same skeleton: AnkiDroid reviews, DUE Revision-tab reviews, one or two new-topic blocks and a mixed-practice block.

### Keep it alive

- **Every 4 weeks:** re-sort the Syllabus tab, compare mock scores, and adjust the remaining weeks.
- **If the exam date moves:** stretch the learning phase and keep the last four weeks as they are.
- **After the exam:** start the next 12-week cycle for your next exam, with what you learned from this one.
""",
    example="""
**Anu**'s LDC exam was about 12 weeks away when she reached this lesson. Her Study Log showed about 18 hours of PSC study a week, on top of 6 hours for this course; she tutors on weekday evenings.

Her capacity check: weeks 1 to 8 gave her about 144 hours, of which 60%, about 86 hours, could go to new topics. Her Syllabus tab had 64 topics, of which 41 were amber or red. At about 2 hours per topic, 41 topics needed about 82 hours: just enough, with the 23 green topics left to reviews and cards.

She wrote the 12-week plan with mocks in weeks 2, 4, 6 and 8, then weekly. Each Sunday she fills in the week's planner from the plan. Week 1 included three priority topics from mental ability, two from English grammar and her daily routines. She put all mock dates and the taper week into her calendar, and showed the plan to her study partner, who promised to ask every Sunday whether she had followed it.
""",
    evidence=[
        ('Spaced reviews, retrieval and practice tests built into the plan', 'strong', 'The plan schedules the two high-utility techniques every week.'),
        ('Written if-then plans for each week\'s priorities', 'strong', 'Implementation intentions have a medium-to-large effect on reaching goals.'),
        ('This exact 12-week structure and time split', 'limited', 'A practical design, not tested research. Adjust it with your weekly review data.'),
    ],
    resources=[
        ('psc-home', 'Check the exam schedule for your exam\'s date, if announced', '5 minutes'),
        ('os-cs-3', 'Reread 3.4 How to Manage Time', '10 minutes'),
    ],
    steps=[
        'Write down your exam date (or a target date 12 weeks away), your real weekly PSC hours from the Study Log, and your latest mock score.',
        'Do the capacity check below for weeks 1 to 8 against your amber and red topics.',
        'Fill in the 12-week plan template: topics for each week in priority order, mock weeks, the revision cycles in weeks 9 to 11 and the taper week.',
        'Fill in the weekly study planner for week 1 from the plan, with if-then plans for its three priorities.',
        'Put all mock dates and the taper week in your calendar. Show the plan to your study partner or a family member and agree on a Sunday check-in.',
    ],
    proof='Your complete 12-week plan, the capacity check, the week-1 planner and a screenshot of the mock dates in your calendar.',
    templates=[
        ('12-week PSC plan', """
12-WEEK PLAN     Exam: ______________  Date: ______ (or target)  Start: ______
Weekly PSC hours (real, from the Study Log): ___   Course hours: ___
Starting mock score: ___   Target score: ___
Week | Phase        | New topics (priority order)        | Mock?  | Notes
1    | Learn+revise | __________________________________ | -      | ______
2    | Learn+revise | __________________________________ | Mock 1 | ______
3    | Learn+revise | __________________________________ | -      | ______
4    | Learn+revise | __________________________________ | Mock 2 | ______
5    | Learn+revise | __________________________________ | -      | ______
6    | Learn+revise | __________________________________ | Mock 3 | ______
7    | Learn+revise | __________________________________ | -      | ______
8    | Learn+revise | __________________________________ | Mock 4 | re-sort Syllabus tab
9    | Cycle 1      | all topics by recall (part 1)      | Mock 5 | ______
10   | Cycle 1      | all topics by recall (part 2)      | Mock 6 | ______
11   | Cycle 2      | ambers and reds, error log         | Mock 7 | ______
12   | Taper        | cards, cue questions, error retests | Mock 8 early | nothing new in last 3 days
Daily skeleton: AnkiDroid ___ min | DUE reviews | new-topic block(s) | mixed practice | sleep by ____
""", ''),
        ('capacity check', """
Hours in weeks 1-8 = weekly PSC hours ___ × 8 = ___
Hours for new topics (about 60%) = ___
Amber and red topics: ___ × about ___ hours each = ___ hours needed
Fits?  yes / no.  If no: cut or shorten these lowest-priority topics: ___________
""", ''),
        ('weekly study planner (core tool)', tools.STUDY_PLANNER, ''),
    ],
    mistakes=[
        ('Twelve weeks of new topics and no revision.', 'Weeks 9 to 12 are for revision cycles and mocks; plan them now.'),
        ('Leaving all mocks to the end.', 'A mock every two weeks from week 2 shows progress and gaps early.'),
        ('Planning with the hours you wish you had.', 'Use your Study Log hours, and cut topics if they don\'t fit.'),
        ('No buffer.', 'Keep one empty block a week (Module 5) for illness, functions and power cuts.'),
        ('Never revisiting the plan.', 'Re-sort the Syllabus tab and adjust every four weeks.'),
    ],
    quiz=[
        {'q': 'In the default plan, what happens in weeks 9 to 11?', 'o': ['Revision cycles through all topics by recall, and a mock every week', 'Only new topics', 'No study at all', 'Only current affairs'], 'a': 'A', 'why': 'The final weeks consolidate everything and train exam conditions.'},
        {'q': 'Your capacity check shows the topics don\'t fit. What should you do?', 'o': ['Cut or shorten the lowest-priority topics', 'Plan to sleep less', 'Ignore it and hope', 'Drop all reviews'], 'a': 'A', 'why': 'A realistic plan you follow beats an ideal plan you abandon.'},
        {'q': 'Where do your weekly hours for the plan come from?', 'o': ['Your Study Log: the hours you really studied', 'The hours you hope to study', 'A topper\'s timetable', 'Your coaching centre'], 'a': 'A', 'why': 'Plans built on real hours survive.'},
        {'q': 'What should the last three days before the exam contain?', 'o': ['Short reviews, error-log retests and sleep, but no new topics', 'Several new chapters', 'All-night study', 'Three full mocks a day'], 'a': 'A', 'why': 'New topics at the end add stress and little marks; sleep consolidates.'},
    ],
    study='The Kerala PSC exam schedule for your exam and College Success 3.4',
    action='Build your complete 12-week PSC study and revision plan and fill in week 1',
)

L6 = lesson(
    M, 6,
    outcome='Manage exam anxiety with techniques that have evidence behind them, prepare an exam-day checklist, and know what to do after the exam and when anxiety needs more help.',
    split='15 minutes reading, 30 minutes resources, 30 minutes action plus your next mock',
    core=f"""
### Some nerves are normal

Feeling nervous before a PSC exam is normal; it shows the exam matters to you. Strong anxiety is different: worry thoughts take up working memory (Module 1), so there is less room for thinking. The goal is not zero nerves, but nerves that don't take over.

### Techniques, with honest evidence

1. **Prepare well, and practise under exam conditions.** OpenStax *College Success* puts preparation first among ways to manage test anxiety: it is the part you control ({link('os-cs-6-3', 'College Success 6.3')}). Mocks (LRN-M12-L03) make the hall, the timing and the answer sheet familiar.
2. **Write about your worries for 10 minutes just before the exam.** In studies published in *Science* in 2011, students who wrote about their worries for 10 minutes right before an exam did better than those who didn't; anxious ninth-grade students who wrote averaged a B+ on their final, against a B− for anxious students who didn't ({link('rb-writing', 'University of Chicago on Ramirez and Beilock')}). One well-known paper with two studies: promising, not settled.
3. **Slow breathing and relaxation.** College Success recommends controlled breathing, visualisation and positive self-talk. Research support in exam settings is limited, but slow breathing is free and calming for many people.
4. **Keep perspective.** One exam is not your whole future; Kerala PSC holds many exams every year, and the system you are building works for all of them.

### In the hall: the reset

If panic rises during the exam: put the pen down, take three slow breaths, and go to a question you know. Getting one right brings the thinking part of your mind back.

### Exam-day checklist

Kerala PSC's OMR instructions include being in your seat 30 minutes before the exam and using a blue or black ball-point pen ({rules('psc-omr', 'OMR instructions')}). Your admission ticket gives the rules for your exam, including what identity proof to carry. Read it the day you download it, not on exam morning.

### After the exam

Kerala PSC publishes **provisional** answer keys for OMR exams, then **final** keys. If you find an error in a provisional key, complaints are made online through your One Time Registration profile within five days ({rules('psc-keys', 'answer keys page')}). Check your answers calmly against the provisional key, file a complaint only with a solid source, then start your next cycle.

### When it is more than exam nerves

If anxiety stays high for weeks, affects your sleep or eating, or comes with panic attacks or hopeless thoughts, it is more than exam nerves. Talk to someone you trust and to a doctor. **Tele-MANAS** is a free government mental health helpline, open 24 hours, in your language of choice: call **14416** or **1-800-891-4416** ({link('telemanas', 'Tele-MANAS')}).
""",
    example="""
**Sreeja** always felt her mind go blank in the first ten minutes of an exam. In her last real exam she had left several easy questions unanswered, and only remembered the answers on the bus home.

Before her next mock she tried the 10-minute worry writing. At the dining table, with the timer set, she wrote everything she was afraid of: her children, the cost of another year without a job, what relatives would say. She rated her anxiety 8 out of 10 before writing and 5 after. Then she took three slow breaths and started.

She did the same before the next two mocks and her first ten minutes went smoothly each time; her scores rose too, though her practice was also improving, so she can't be sure how much was the writing. She wrote her exam-day checklist and her in-hall reset on one card, and saved the Tele-MANAS number in her phone, "just in case, for me or for someone else".
""",
    evidence=[
        ('Expressive writing about worries just before an exam', 'moderate', 'Ramirez and Beilock (2011), in Science: two studies, with gains for anxious students. Promising, not settled.'),
        ('Preparation and practice under exam conditions', 'limited', 'Standard advice (College Success 6.3) and very plausible; little direct research on anxiety itself.'),
        ('Slow breathing and relaxation', 'limited', 'Recommended by College Success; research in exam settings is limited, but it is free and harmless.'),
    ],
    resources=[
        ('rb-writing', 'Read the news article on the expressive-writing studies', '10 minutes'),
        ('os-cs-6-3', 'Read the sections on test anxiety and test day', '15 minutes'),
        ('psc-omr', 'Read the rules for candidates on exam day', '10 minutes'),
        ('psc-keys', 'Read how provisional and final keys and complaints work', '5 minutes'),
        ('telemanas', 'Save the helpline number in your phone', '2 minutes'),
    ],
    steps=[
        'Write your exam-day checklist with the template below, using your own admission ticket and exam instructions.',
        'Before your next mock, rate your anxiety from 1 to 10, do the 10-minute worry writing, and rate it again. Keep the writing private; you can tear it up afterwards.',
        'Take the mock and note your score and how the first ten minutes felt.',
        'Write your in-hall reset on the same card as your checklist.',
        'Save the Tele-MANAS number in your phone.',
    ],
    proof='Your exam-day checklist and in-hall reset card, and your before-and-after anxiety ratings with the mock score (not the private writing itself).',
    templates=[
        ('exam-day checklist', """
THE WEEK BEFORE
[ ] Admission ticket downloaded and read: date ____ time ____ centre ____________
[ ] ID proof required: ______________   Other items allowed / not allowed: ________
[ ] Route to the centre checked; travel time ___ (visit it if possible)
THE DAY BEFORE
[ ] Light review only: cue questions, cards, error-log retests. Nothing new.
[ ] Pens (blue or black ball-point, two), ticket, ID, water, watch if allowed
[ ] Sleep by ____
EXAM DAY
[ ] Leave by ____ to be seated 30 minutes before the start
[ ] 10-minute worry writing while waiting, then three slow breaths
[ ] Two-pass plan and checkpoints (LRN-M12-L04)
AFTER
[ ] Check against the provisional key; complaint within the deadline only with a solid source
""", ''),
        ('10-minute worry writing and the in-hall reset', """
WORRY WRITING (10 minutes, just before the exam or mock)
Anxiety before (1-10): ___
Write freely about what you are worried about in this exam. Nobody will read it.
Anxiety after (1-10): ___

IN-HALL RESET (if panic rises)
1. Pen down.  2. Three slow breaths, longer out than in.
3. Go to a question you know and answer it.  4. Continue the two-pass plan.
""", ''),
    ],
    mistakes=[
        ('Cramming new topics the night before.', 'Review lightly and sleep; consolidation needs the night.'),
        ('Reading the admission ticket on exam morning.', 'Read it the day you download it, so there are no surprises.'),
        ('Reading "expected questions" forums on exam morning.', 'They raise anxiety and add nothing. Use your checklist instead.'),
        ('Ignoring anxiety that lasts for weeks.', 'Talk to someone you trust and a doctor; Tele-MANAS is free at 14416.'),
    ],
    quiz=[
        {'q': 'What did Ramirez and Beilock (2011) test?', 'o': ['Writing about worries for 10 minutes just before an exam', 'Studying for 10 hours the night before', 'Listening to music during the exam', 'Skipping breakfast'], 'a': 'A', 'why': 'Anxious students who wrote did better; promising evidence from two studies.'},
        {'q': 'According to Kerala PSC\'s OMR instructions, when should you be in your seat?', 'o': ['30 minutes before the exam', 'At the exact start time', '5 minutes after the start', 'Two hours before'], 'a': 'A', 'why': 'Check your admission ticket for your exam\'s exact rules.'},
        {'q': 'You find an error in a provisional answer key. What can you do?', 'o': ['Complain online through your One Time Registration profile within five days, with a solid source', 'Nothing at all', 'Phone the exam centre', 'Wait for the final key and complain then'], 'a': 'A', 'why': 'Complaints are made through the OTR profile within the deadline.'},
        {'q': 'What is Tele-MANAS?', 'o': ['A free 24-hour government mental health helpline: 14416', 'A PSC coaching app', 'An exam scheduling site', 'A paid counselling service only'], 'a': 'A', 'why': 'It offers support in your language of choice, free of charge.'},
    ],
    study='The expressive-writing studies, College Success 6.3 on test anxiety, and the PSC rules for exam day and answer keys',
    action='Write your exam-day checklist and reset, and try the 10-minute worry writing before a mock',
)

LESSONS = [L1, L2, L3, L4, L5, L6]

MODULE = module(
    M,
    overview="""
Master the Kerala PSC exam itself: map the official syllabus, analyse previous-year questions, take mock tests and keep an error log, use the arithmetic of negative marking, build a complete 12-week study and revision plan, and manage exam anxiety and exam day.

Everything so far has made you a better learner. This module points that learning at the exam. It uses only official sources for the rules (the syllabus, previous papers, answer keys and OMR instructions on the Kerala PSC website) and marks every rule with "check current rules", because schemes can change.

By the end you have an exam system: a Syllabus tab with priorities, a PYQ analysis, an Errors tab, a guessing rule based on your own data, a 12-week plan and an exam-day checklist.
""",
    outcomes=[
        'Turn the official syllabus into a prioritised Syllabus tab',
        'Analyse 200 or more previous-year questions and act on the patterns',
        'Take mocks under real conditions and fix every error by type',
        'Decide when to answer using expected value and your own calibration',
        'Build and run a 12-week study and revision plan',
        'Manage exam anxiety and prepare for exam day',
    ],
    lessons=LESSONS,
    tools=[
        'The **error log** (one of the six core tools) and the **Errors** tab',
        'The **study planner** (core tool) used inside the **12-week plan**',
        'The **Syllabus** and **PYQ** tabs with the priority and COUNTIF formulas',
        'The **guessing calculator**, **two-pass time plan** and **mock test conditions** checklist',
        'The **exam-day checklist** and **in-hall reset**',
    ],
    project='My exam system',
    project_steps=[
        'Make sure your Syllabus tab is complete, with PYQ counts and priorities from at least 200 tagged questions.',
        'Take a second full mock, log every error and compare both mocks: score, error types, timing.',
        'Finalise your 12-week plan with the results of both mocks.',
        'Put your guessing rule, two-pass plan and exam-day checklist on one card.',
        'Write a one-page summary: your three biggest gaps, your plan for them, and your target score.',
    ],
    project_proof='Screenshots of your Syllabus, PYQ and Errors tabs, both mock scores with the comparison, your 12-week plan, your exam card and the one-page summary.',
    rubric=[
        ('Syllabus map', 'No map', 'Topics listed without priorities', 'All topics with confidence, PYQ counts and priorities'),
        ('PYQ analysis', 'Fewer than 100 questions', '100 to 199 tagged', '200 or more tagged, patterns written, misses turned into cards'),
        ('Mocks and errors', 'No mock', 'One mock, errors noted loosely', 'Two mocks, every error typed, fixed and retested'),
        ('Exam strategy', 'Guessing by feeling', 'Rule known but not tested', 'Guessing rule from my data and two-pass plan used in a mock'),
        ('12-week plan', 'None', 'A plan without mocks or revision cycles', 'Complete plan with capacity check, mocks, cycles and taper'),
    ],
    short=[
        'Do LRN-M12-L02 with one paper of 100 questions, and LRN-M12-L03 with one mock.',
        'Write a simple 12-week plan: weeks 1-8 learn and revise, 9-11 cycles and weekly mocks, 12 taper.',
    ],
    flashcards=[
        ('Kerala PSC OMR marking', '+1 for a correct answer, −1/3 for a wrong one, 0 for unanswered (check your exam\'s instructions).'),
        ('Break-even chance for answering under −1/3 marking', '1 in 4; answer when your chance is higher.'),
        ('Expected value with two options ruled out', '+1/3 of a mark.'),
        ('Mock score formula', 'Correct − wrong ÷ 3.'),
        ('The seven error types', 'K didn\'t know, F forgot, I interference, M misread, C careless, G bad guess, T time.'),
        ('Priority score', '(PYQ count + 1) × (6 − confidence).'),
        ('The 12-week structure', 'Weeks 1-8 learn and revise, 9-11 revision cycles and weekly mocks, 12 taper.'),
        ('Expressive writing before exams', '10 minutes writing about worries just before; helped anxious students (Ramirez and Beilock, 2011).'),
        ('Free mental health helpline', 'Tele-MANAS: 14416 or 1-800-891-4416.'),
    ],
    mistakes=[
        ('Studying hard without looking at the exam itself.', 'The syllabus, PYQs and mocks tell you where your hours earn marks.'),
        ('Trusting forwarded rules about marking or dates.', 'Check the official instructions, notification and admission ticket.'),
    ],
)
