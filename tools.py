"""The copy-ready tools of the personal learning system. Lessons and the
toolkit page use these same strings, so every copy stays identical."""

# ---- Learning Workbook tab headers (Google Sheets or LibreOffice Calc)
STUDY_LOG = 'Date,Subject,Topic,Minutes,Method,Focus (1-5),What I can now recall,Next step'
REVISION = 'Topic,First studied,Review 1 (+1 day),Review 2 (+3 days),Review 3 (+7 days),Review 4 (+21 days),Review 5 (+60 days),Next review,Due today?,Last score %'
REVISION_FORMULAS = """In row 2, with the first study date in B2 (type it as a date, e.g. 2026-11-09):
C2: =B2+1
D2: =B2+3
E2: =B2+7
F2: =B2+21
G2: =B2+60
H2: =IF(C2>=TODAY(),C2,IF(D2>=TODAY(),D2,IF(E2>=TODAY(),E2,IF(F2>=TODAY(),F2,IF(G2>=TODAY(),G2,"done")))))
I2: =IF(OR(C2=TODAY(),D2=TODAY(),E2=TODAY(),F2=TODAY(),G2=TODAY()),"DUE","")
Format C2:H2 as dates. Copy row 2 down for every new topic. Sort or filter by column H to see what is coming."""
ERROR_LOG = 'Date,Source (mock / PYQ / practice),Question no,Subject,Topic,My answer,Correct answer,Error type,Why it happened,Fix (card / note / rule),Retest date,Retest result'
ERROR_TYPES = [
    ('K', "Didn't know: never learned it, or not on my cards"),
    ('F', 'Forgot: learned it once, could not recall it in time'),
    ('I', 'Interference: mixed it up with a similar fact'),
    ('M', 'Misread: missed a word such as NOT, first, largest, except'),
    ('C', 'Careless: a slip in calculation or in marking the OMR bubble'),
    ('G', 'Bad guess: guessed when I could not rule anything out'),
    ('T', 'Time: rushed, or never reached the question'),
]
PYQ = 'Paper (post and year),Question no,Subject,Topic,Subtopic,Type (fact / concept / calculation / statement),Repeated? (Y/N),Seen in my material? (Y/N),Right at first try? (Y/N),Notes'
SYLLABUS = 'Subject,Topic (from the official syllabus),Marks or share,PYQ count,Confidence (1-5),Status (not started / learning / revising / solid),Source I use,Next review'
WEEKLY = 'Week,Dates,Study hours,AnkiDroid days (of 7),AnkiDroid % correct,Self-test score %,Mock or PYQ score,Focus blocks done,Top error type,One change for next week'
FOCUS_LOG = 'Date,Task,Planned minutes,Minutes to first distraction,Distractions (tally),Phone where?,Focus (1-10),Note'
SPRINT = 'Day,Date,Minutes,What I studied,Methods used,Retrieval score (e.g. 7/10),Cards added,Energy (1-5),Note'

# ---- The six core tools named in the course brief
STUDY_PLANNER = """WEEKLY STUDY PLANNER          Week of: ________
Exam: __________________ on ________   Weeks left: ___
Hours this week: course ___ + PSC study ___ = ___

DAY   BLOCK (time)   SUBJECT : TOPIC            METHOD                    DONE
Mon   ____–____      ________ : __________      ______________________    [ ]
Tue   ____–____      ________ : __________      ______________________    [ ]
Wed   ____–____      ________ : __________      ______________________    [ ]
Thu   ____–____      ________ : __________      ______________________    [ ]
Fri   ____–____      ________ : __________      ______________________    [ ]
Sat   ____–____      ________ : __________      ______________________    [ ]
Sun   20 minutes     Weekly learning review + plan next week               [ ]

METHOD words: retrieval (blank-page recall, practice questions), spaced review
(from the Revision tab), mixed practice (interleaving), Feynman, cards, mock test.

Every day:  [ ] AnkiDroid reviews (___ min)  [ ] one retrieval session
            [ ] phone in another room during blocks  [ ] sleep by ____
If-then plans: If ____________________, then I will ____________________."""

REVISION_SCHEDULE = """REVISION SCHEDULE (expanding gaps)
Day 0   Learn it: read, understand, make notes and questions
Day 1   Review 1: blank-page recall, then check and fix
Day 3   Review 2: answer your questions from memory
Day 7   Review 3: mixed practice questions with other topics
Day 21  Review 4: PYQs or a short timed test on this topic
Day 60  Review 5: quick recall; anything you miss goes to AnkiDroid
Every review starts with RECALL, not rereading. Score yourself, and log the
score in the Revision tab. A score under 60% means: re-learn the gaps and
restart the schedule from Day 1 for that topic.
Facts (names, dates, articles, numbers) live in AnkiDroid, which spaces them
for you. This schedule is for whole topics and skills."""

CARD_CHECKLIST = """CARD-WRITING CHECKLIST (tick before you add a card)
[ ] I understand it: I could explain it in my own words
[ ] One fact per card (the minimum information principle)
[ ] The question has exactly one correct answer
[ ] The answer is short: a word, a number, a name or a phrase
[ ] Lists are split: one cloze per item, or a memory palace instead
[ ] A context cue starts the question when needed ("Constitution:", "Kerala rivers:")
[ ] Look-alike facts are made clearly different ("longest" vs "largest")
[ ] A picture, map or diagram is used where it helps (image occlusion)
[ ] The source is in the Source field (book and page, or PYQ paper and number)
[ ] It is worth knowing: it is on the syllabus or has appeared in PYQs"""

ERROR_LOG_TEXT = """ERROR LOG (one row per wrong or guessed question; Errors tab)
Date | Source | Q no | Subject | Topic | My answer | Correct | Type | Why | Fix | Retest date | Retest result
Error types:
K = didn't know      F = forgot         I = interference (mixed up two facts)
M = misread          C = careless slip  G = bad guess      T = ran out of time
Fix rules:
K or F -> make 1-3 cards, or add the topic to the Revision tab
I      -> one card that contrasts the two facts side by side
M      -> underline NOT / EXCEPT / FIRST / LARGEST in every question for a week
C      -> slow down on the last step; check the OMR bubble number
G      -> guess only after ruling out at least one option
T      -> two-pass method in the next mock
Retest every error 7 days later, from memory. Clear it only when it is right twice."""

FEYNMAN = """FEYNMAN EXPLANATION       Topic: ______________   Date: ________
Recording: v1 file ________  v2 file ________
1. Explain it aloud, without notes, to an imaginary 12-year-old (2-3 minutes).
   Record it on your phone (v1).
2. Listen back. Mark every gap: where I stopped, said "basically" or "something
   like", used a word I can't define, or got a fact wrong:
   ___________________________________________________________________
3. Go back to the source (book ______ page ___). Fix each gap:
   ___________________________________________________________________
4. Simplify: one analogy or example from Kerala life: ____________________
5. Record again without notes (v2). What is clearer now? __________________
6. Turn the gaps into 2-3 flashcards and 1 question for my Revision tab.
Score each 1-3:  Accuracy __  Clarity __  Complete __  Without notes __  Total __/12"""

WEEKLY_REVIEW = """WEEKLY LEARNING REVIEW        Week ___ (dates ________)   20 minutes, Sunday
Numbers: study hours ___ | AnkiDroid days ___/7, % correct ___%
         self-test ___% | mock or PYQ score ___ | focus blocks ___
1. From memory, no notes: the three most important things I learned this week
   ______________________________________________________________________
2. Cold self-test: 5 questions from this week's topics. Score ___/5
3. Calibration: what did I feel sure about but get wrong? ________________
4. Error log: my most common error type this week ___ ; the fix ___________
5. What worked? ______________________  What didn't? ______________________
6. Next week's three priorities, each with a day and time (if-then plans)
   1. ________________ 2. ________________ 3. ________________
7. One change to my system: ______________________________________________
Copy the numbers into the Weekly tab of the Learning Workbook."""

SIX_TOOLS = [
    ('Study planner', 'STUDY_PLANNER', 'LRN-M05-L02 (time-blocking) and LRN-M12-L05 (the 12-week plan)'),
    ('Revision schedule', 'REVISION_SCHEDULE', 'LRN-M03-L02 (spaced practice)'),
    ('Card-writing checklist', 'CARD_CHECKLIST', 'LRN-M04-L02 (writing good cards)'),
    ('Error log', 'ERROR_LOG_TEXT', 'LRN-M12-L03 (mock tests and the error log)'),
    ('Feynman template', 'FEYNMAN', 'LRN-M08-L01 (self-explanation and the Feynman technique)'),
    ('Weekly review', 'WEEKLY_REVIEW', 'LRN-M07-L03 (the weekly learning review)'),
]

TABS = [
    ('Baseline', 'Week 0', 'Your four baseline test scores and habit ratings, start and end'),
    ('Study Log', 'Week 0', STUDY_LOG),
    ('Weekly', 'Week 0', WEEKLY),
    ('Revision', 'Module 3', REVISION),
    ('Focus', 'Module 5', FOCUS_LOG),
    ('Syllabus', 'Module 12', SYLLABUS),
    ('PYQ', 'Module 12', PYQ),
    ('Errors', 'Module 12', ERROR_LOG),
    ('Sprint', 'Module 21', SPRINT),
]
