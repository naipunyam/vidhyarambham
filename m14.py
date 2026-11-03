"""Module 14: Numerical ability and reasoning."""
from common import lesson, module, link, fence, table

M = 14

L1 = lesson(
    M, 1,
    outcome='Use a dozen reliable mental-maths tricks for PSC arithmetic, check answers in seconds, and practise until the basics are automatic.',
    split='20 minutes reading, 25 minutes resources, 45 minutes action plus a 10-minute daily warm-up for a week',
    core=f"""
### Why mental maths matters

In a PSC paper you may have about 45 seconds a question (LRN-M12-L04). If "17 × 6" or "15% of 640" takes you 30 seconds, you have no time left to think about the problem itself. When basic calculations are **automatic**, they take almost no working memory, and the reasoning gets the space it needs. The CESE review of cognitive load theory describes exactly this: extensive practice makes knowledge automatic, which frees working memory for new problems ({link('cese-clt', 'CESE, 2017')}).

### A dozen tricks that always work

These are arithmetic facts, so they are always correct; the only question is practice.

{table(['Trick', 'How', 'Example'], [
    ('× 5', '× 10, then halve', '48 × 5 = 480 ÷ 2 = 240'),
    ('× 25', '× 100, then divide by 4', '36 × 25 = 3,600 ÷ 4 = 900'),
    ('× 9', '× 10, then subtract the number', '47 × 9 = 470 − 47 = 423'),
    ('× 11 (two digits)', 'Write the two digits apart and put their sum between (carry if 10 or more)', '53 × 11 = 583; 78 × 11 = 858'),
    ('Squares ending in 5', 'First digit × (first digit + 1), then write 25', '65² = (6 × 7) then 25 = 4,225'),
    ('Near a round number', '(a − b)(a + b) = a² − b²', '47 × 53 = 50² − 3² = 2,500 − 9 = 2,491'),
    ('Percentages', '10% is a decimal shift; 5% is half of that; build the rest', '15% of 640 = 64 + 32 = 96'),
    ('Swap a percentage', 'x% of y = y% of x', '8% of 25 = 25% of 8 = 2'),
    ('Successive changes', 'Net % = a + b + (a × b) ÷ 100', '+20% then −20%: 20 − 20 − 4 = −4%'),
    ('Averages with a base', 'Pick a base, average the differences', '46, 48, 52, 54: base 50, differences sum to 0, average 50'),
    ('BODMAS', 'Brackets, Of, Division, Multiplication, Addition, Subtraction', '8 + 4 × 3 = 20, not 36'),
    ('Last-digit check', 'The last digit of a product is the last digit of the product of last digits', '47 × 23 must end in 1 (7 × 3 = 21); it is 1,081'),
])}

### Facts worth making automatic

Put these in AnkiDroid (Module 4) and they will become instant within weeks:

- **Fractions and percentages:** 1/2 = 50%, 1/3 = 33.33%, 1/4 = 25%, 1/5 = 20%, 1/6 = 16.67%, 1/8 = 12.5%, 1/9 = 11.11%, 1/10 = 10%, 1/12 = 8.33%, 1/16 = 6.25%, 1/20 = 5%
- **Squares from 11 to 30** and **cubes from 1 to 15**
- **Multiplication tables to 20,** if you don't know them already
- **Divisibility rules:** by 3 or 9, the sum of the digits is divisible by 3 or 9; by 4, the last two digits; by 8, the last three; by 11, the difference between the sums of alternate digits is 0 or a multiple of 11

### Checking in seconds

With four options, a quick check often picks the answer without full working: the last digit, a rough estimate (is it about 400 or about 4,000?), or divisibility. Always check before marking the bubble.

### How speed really comes

Tricks help only after practice. Ten minutes of mixed mental arithmetic a day, timed, with immediate checking (the practice loop from Module 13), builds speed far better than learning fifty tricks once.
""",
    example="""
**Sreeja** lost a lot of time in the arithmetic section, mainly on the calculations rather than the problems. She learned six tricks from this lesson (× 5, × 25, × 11, squares ending in 5, percentages and successive changes) and made AnkiDroid cards for the fraction-percentage table and squares from 11 to 30.

Each morning, before her first study block, she did a 20-problem mental maths warm-up from a sheet she wrote by mixing problems from her guide, timed on the phone's stopwatch and checked straight away. Day 1 took 9 minutes with 14 right. By day 7 it took 6 minutes with 18 right, and after three weeks under 5 minutes with 19 or 20 right.

In her next mock she finished the arithmetic questions with time to spare, and for the first time she used the last-digit check to choose between two options that looked close.
""",
    evidence=[
        ('Automatic basic facts free working memory for problem solving', 'strong', 'The CESE review describes automation through extensive practice; it follows from working-memory limits (Module 1).'),
        ('The mental-maths tricks in this lesson', 'strong', 'They are arithmetic identities, always correct. What varies is how well you have practised them.'),
        ('Short daily timed practice with immediate checking', 'moderate', 'It combines spacing, retrieval and feedback; speed grows with practice.'),
    ],
    resources=[
        ('cese-clt', 'Reread the part on automation and long-term memory', '5 minutes'),
        ('os-prealg', 'Do a few exercises from the chapters on whole numbers, fractions, decimals and percents, using the tricks', '30 minutes'),
        ('os-prealg-6-1', 'Practise converting between fractions, decimals and percents', '15 minutes'),
    ],
    steps=[
        'Learn six of the tricks in the table, one at a time: for each, do five examples from your guide and check them.',
        'Make AnkiDroid cards for the fraction-percentage table and for squares from 11 to 30.',
        'Write a sheet of 20 mixed mental-maths problems (or use one from your guide). Each day for 7 days, do a fresh 20 under a stopwatch and check each answer straight away.',
        'Log time and accuracy each day.',
        'In your next practice set, use the last-digit check or an estimate on at least five questions before marking an answer.',
    ],
    proof='Your 7-day warm-up log with times and scores, and a screenshot of your new cards.',
    templates=[
        ('mental maths warm-up log', """
WARM-UP LOG (20 mixed problems, timed, checked straight away)
Day | Date   | Time (min:sec) | Right /20 | Trick I used most | Error I made
1   | ______ | ____           | ___       | ____________      | ____________
2   | ______ | ____           | ___       | ____________      | ____________
...
7   | ______ | ____           | ___       | ____________      | ____________
""", ''),
        ('checking an answer in seconds', """
1. Last digit: does the option's last digit match?
2. Estimate: round the numbers; is the option about the right size?
3. Divisibility: should the answer be even, a multiple of 3, 5, 9 or 11?
4. Reverse: put the answer back into the question.
5. Units: rupees, km/h or m/s, days, percent?
""", ''),
    ],
    mistakes=[
        ('Learning fifty tricks and practising none.', 'Six tricks, practised daily, beat fifty read once.'),
        ('Speed without checking.', 'A fast wrong answer loses a third of a mark. Check before you mark.'),
        ('Ignoring BODMAS.', 'Many PSC simplification questions test the order of operations.'),
        ('Doing calculations on paper that tricks could do mentally.', 'Use the warm-up to make the basics automatic.'),
    ],
    quiz=[
        {'q': 'What is 36 × 25?', 'o': ['900', '960', '850', '1,000'], 'a': 'A', 'why': '36 × 100 = 3,600, and 3,600 ÷ 4 = 900.'},
        {'q': 'What is 65²?', 'o': ['4,225', '4,025', '3,625', '4,125'], 'a': 'A', 'why': '6 × 7 = 42, then 25: 4,225.'},
        {'q': 'What is 15% of 640?', 'o': ['96', '64', '106', '90'], 'a': 'A', 'why': '10% is 64 and 5% is 32; 64 + 32 = 96.'},
        {'q': 'A price rises 10% and then another 10%. What is the total rise?', 'o': ['21%', '20%', '11%', '19%'], 'a': 'A', 'why': '10 + 10 + (10 × 10) ÷ 100 = 21%.'},
        {'q': 'What is 47 × 53?', 'o': ['2,491', '2,500', '2,481', '2,509'], 'a': 'A', 'why': '50² − 3² = 2,500 − 9.'},
    ],
    study='The CESE review on automation and OpenStax Prealgebra exercises on whole numbers, fractions, decimals and percents',
    action='Learn six tricks, make cards for the key facts and do a timed mental-maths warm-up for 7 days',
)

L2 = lesson(
    M, 2,
    outcome='Solve the core PSC arithmetic topics (percentages, profit and loss, ratio, averages, interest, time and work, speed and distance) from a few principles, and check every answer.',
    split='15 minutes reading, 25 minutes resources, 50 minutes action',
    core=f"""
Most PSC arithmetic questions come from a small set of topics, and each topic rests on one or two principles (LRN-M08-L04). Learn the principle, see one worked example, then practise with previous papers.

### The core topics

{table(['Topic', 'Principle', 'Worked example'], [
    ('Percentages', 'Change ÷ original × 100', 'Salary rises from ₹20,000 to ₹23,000: 3,000 ÷ 20,000 × 100 = 15%'),
    ('Profit and loss', 'Profit % is on the cost price', 'Bought for ₹800, sold for ₹1,000: profit 200 ÷ 800 × 100 = 25%'),
    ('Discount', 'Discount is on the marked price', 'Marked ₹1,200, 15% discount: 1,200 × 0.85 = ₹1,020'),
    ('Ratio and proportion', 'Add the parts, find one part, multiply', '₹1,800 in the ratio 2:3:4: 9 parts of ₹200, so ₹400, ₹600, ₹800'),
    ('Averages', 'Total = average × count', 'Average of 5 numbers is 42; without one of them, the average of 4 is 40: removed = 210 − 160 = 50'),
    ('Simple interest', 'SI = P × R × T ÷ 100', '₹5,000 at 8% for 3 years: 5,000 × 8 × 3 ÷ 100 = ₹1,200'),
    ('Compound interest', 'Amount = P × (1 + R/100)^T', '₹10,000 at 10% for 2 years: 10,000 × 1.1 × 1.1 = ₹12,100, so CI = ₹2,100'),
    ('Time and work', 'Daily rates add: rate = 1 ÷ days', 'A in 12 days, B in 18: 1/12 + 1/18 = 5/36 a day, so 36/5 = 7.2 days together'),
    ('Speed and distance', 'Distance = speed × time; km/h × 5/18 = m/s', 'A 200 m train at 72 km/h (20 m/s) passes a pole in 10 s and a 300 m platform in 500 ÷ 20 = 25 s'),
    ('Relative speed', 'Towards each other: add speeds; same direction: subtract', 'Trains 180 km apart at 50 and 40 km/h towards each other meet in 180 ÷ 90 = 2 hours'),
])}

A useful extra: for two years, the difference between compound and simple interest is P × (R/100)². For ₹10,000 at 10%, that is ₹100 (CI ₹2,100 against SI ₹2,000).

### A five-step method for every question

1. **Name the type** (Module 3): "this is time and work".
2. **Write the principle** in a few words: "rates add".
3. **Set up** the numbers with units.
4. **Calculate,** using mental tricks where they fit (LRN-M14-L01).
5. **Check:** estimate, last digit, units, or put the answer back into the question.

### Common traps

- **Profit on selling price** instead of cost price
- **Mixing units:** km/h with metres, months with years in interest
- **Averaging speeds:** going at 40 km/h and returning at 60 km/h does **not** average 50 km/h; work it out from total distance ÷ total time
- **Percentage of what?** "A is 25% more than B" is not the same as "B is 25% less than A"
- **Forgetting the train's own length** when it crosses a platform or bridge

### Practise from previous papers

Your PYQ tab (Module 12) shows which topics your exam asks most. Collect three previous-year questions per topic, solve them with the five steps, then mix them into timed sets (Module 3).
""",
    example="""
**Anu** knew most formulas but kept losing marks to traps. She went through ten topics with this lesson's table: for each, she wrote the principle on a card in her own words, studied the worked example, and then solved three previous-year questions with the five-step method.

Her Errors tab told her which traps she fell into: profit calculated on the selling price twice, and the "average speed" trap once. She made a contrast card for each ("Profit % is on COST price"; "Average speed = total distance ÷ total time, not the average of the speeds").

Then she built a mixed set of 20 (two per topic), shuffled, timed. First attempt: 14 right in 22 minutes. A week later, a new mixed set: 18 right in 16 minutes. The five steps felt slow at first; by the second week, naming the type and the principle took her a few seconds.
""",
    evidence=[
        ('Worked examples first, then practice', 'strong', 'The worked example effect (CESE review): beginners learn more from studied solutions before solving alone.'),
        ('Mixed sets of different arithmetic types', 'moderate', 'Interleaving is rated moderate utility, with its strongest evidence in maths (Dunlosky and others, 2013).'),
        ('Solving from principles instead of many formulas', 'limited', 'A practical approach consistent with research on self-explanation (Module 8).'),
    ],
    resources=[
        ('os-prealg-6-1', 'Review percent conversions and do the end-of-section practice', '20 minutes'),
        ('os-prealg', 'Do a few exercises from the chapters on fractions and decimals, using the five steps', '25 minutes'),
        ('psc-pyq', 'Collect three previous-year arithmetic questions for each core topic', '20 minutes'),
    ],
    steps=[
        'For each of the ten topics in the table, write the principle on an AnkiDroid card in your own words, with the worked example on the back.',
        'Solve three previous-year questions per topic (or as many as you can find) using the five-step method, writing the type and principle first.',
        'Log every error in your Errors tab, and make a contrast card for any trap you fall into.',
        'Build a mixed, shuffled set of 20 (two per topic) and solve it timed. Record time and score.',
        'A week later, solve a new mixed set of 20 and compare.',
    ],
    proof='Your ten principle cards, your worked PYQ solutions with types and principles written, and both mixed-set scores and times.',
    templates=[
        ('topic principle card', """
FRONT: Time and work: the principle?
BACK:  Daily rates add. Rate = 1 / days.
       Example: A 12 days, B 18 days -> 1/12 + 1/18 = 5/36 a day -> 36/5 = 7.2 days.
(Make one card like this for each topic.)
""", ''),
        ('five-step solving sheet', """
Q ___  Type: ______________  Principle: ____________________________
Set up (with units): ______________________________________________
Calculate: ________________________________________________________
Check (estimate / last digit / units / reverse): ____________________
Answer: ___   Right? Y / N   If wrong, error type (K F I M C G T): ___
""", ''),
    ],
    mistakes=[
        ('Hunting for a formula for each question.', 'Name the type and use its principle; most topics need one or two.'),
        ('Mixing units.', 'Write units at every step; convert km/h to m/s with × 5/18.'),
        ('Averaging two speeds directly.', 'Use total distance ÷ total time.'),
        ('Not checking when options are close.', 'Use the last digit, an estimate or reverse substitution.'),
    ],
    quiz=[
        {'q': 'An item is bought for ₹800 and sold for ₹1,000. What is the profit percentage?', 'o': ['25%', '20%', '200%', '12.5%'], 'a': 'A', 'why': 'Profit 200 ÷ cost 800 × 100 = 25%.'},
        {'q': 'What is 72 km/h in metres per second?', 'o': ['20', '72', '25', '18'], 'a': 'A', 'why': '72 × 5/18 = 20.'},
        {'q': 'A can finish a job in 12 days and B in 18 days. How long together?', 'o': ['7.2 days', '15 days', '6 days', '30 days'], 'a': 'A', 'why': '1/12 + 1/18 = 5/36 a day, so 36/5 = 7.2 days.'},
        {'q': 'What is the compound interest on ₹10,000 at 10% a year for 2 years?', 'o': ['₹2,100', '₹2,000', '₹1,100', '₹12,100'], 'a': 'A', 'why': 'Amount is ₹12,100, so the interest is ₹2,100.'},
        {'q': 'Divide ₹1,800 in the ratio 2:3:4. What is the largest share?', 'o': ['₹800', '₹600', '₹900', '₹720'], 'a': 'A', 'why': '9 parts of ₹200; the largest is 4 parts.'},
    ],
    study='OpenStax Prealgebra on percent, fractions and decimals, and three PYQs per topic',
    action='Write principle cards for ten arithmetic topics, solve PYQs with the five steps and compare two mixed sets',
)

L3 = lesson(
    M, 3,
    outcome='Solve the common PSC reasoning types (series, coding, analogies, odd one out, blood relations, directions, clocks and calendars) with a method for each, and run a weekly maths and reasoning practice system.',
    split='15 minutes reading, 20 minutes resources, 55 minutes action plus the first week of the system',
    core=f"""
Mental ability questions look varied, but each type has a reliable method. Learn the method, practise it with previous papers, then mix the types (Module 3).

### Reasoning types and their methods

{table(['Type', 'Method', 'Example'], [
    ('Number series', 'Check differences, then ratios, then squares or cubes, then alternate terms', '2, 6, 12, 20, 30, ?: differences 4, 6, 8, 10, so the next is 30 + 12 = 42'),
    ('Coding', 'Write letter positions (A = 1 ... Z = 26) and find the shift', 'If CAT is written DBU (each letter + 1), DOG is EPH'),
    ('Analogy', 'State the relationship in a sentence first', 'Doctor : hospital :: teacher : school (where each works)'),
    ('Odd one out', 'Find the rule that three share', '9, 25, 49, 50: the first three are squares of odd numbers, so 50'),
    ('Blood relations', 'Draw a family tree: generations in rows, + male, − female, = married', '"He is the son of my father\'s only brother": he is my cousin'),
    ('Directions', 'Draw it, with north at the top', '5 km north, right 3 km, right 5 km: you are 3 km east of the start, facing south'),
    ('Clocks', 'Angle between the hands = the difference between 30 × hours and 5.5 × minutes (ignore the sign)', 'At 3:20: 30 × 3 = 90 and 5.5 × 20 = 110, so 20°'),
    ('Calendars', 'Count odd days: an ordinary year adds 1 weekday, a leap year adds 2', '1 January 2025 was a Wednesday, so 1 January 2026 is a Thursday'),
])}

### Draw it

Blood relations, directions and seating arrangements are hard to hold in working memory (Module 1). **Draw them** on paper: a family tree, a compass sketch, a row of seats. It takes a few seconds and prevents most errors. This is dual coding (Module 3) used as a thinking tool.

### Check against every term

In series questions, a rule that fits two terms may not fit the third. Check your rule against **every** term before choosing an answer.

### A weekly maths and reasoning system

Combine everything in this module into a routine:

{table(['When', 'What', 'Time'], [
    ('Every day', 'Mental-maths warm-up (LRN-M14-L01)', '10 minutes'),
    ('Every day', 'AnkiDroid: principle cards, squares, fraction-percentages, formulas', 'Part of your reviews'),
    ('Three days a week', 'Mixed set of 15 (arithmetic and reasoning), timed, each answer checked straight away', '20 to 25 minutes'),
    ('One day a week', 'The mental-ability section of a previous paper under exam timing', '20 to 30 minutes'),
    ('Every week', 'Errors tab updated; next week\'s weakest type chosen for a practice loop (Module 13)', '10 minutes'),
    ('Every month', 'Retest on a fresh mixed set; compare with last month', '30 minutes'),
])}
""",
    example="""
**Ashiq** was strong in arithmetic but lost marks in reasoning, especially blood relations and directions, which he tried to solve in his head. He started drawing every one: a family tree with + and − signs, a compass sketch for directions. His accuracy on those two types went from about half to almost all within a week.

He then set up the weekly system. Every morning: the 10-minute warm-up. Monday, Wednesday and Friday: a shuffled set of 15 mixed questions, checked one by one. Saturday: the mental-ability section of an unseen previous paper, under the real time limit. Sunday: the Errors tab, and the weakest type chosen for next week's practice loop.

His first month's retest showed his accuracy on mixed sets rising from 70% to 87%, and his time per question falling. Calendar questions became his favourite after he made one card for the odd-days rule and checked it against a calendar.
""",
    evidence=[
        ('Drawing diagrams for relations, directions and arrangements', 'moderate', 'Dual coding (Module 3) and lower working-memory load (Module 1); widely recommended for reasoning.'),
        ('Mixed sets of reasoning and arithmetic types', 'moderate', 'Interleaving: moderate utility, strongest in maths and category learning.'),
        ('A weekly practice system with timed sections', 'limited', 'A practical combination of spacing, retrieval, interleaving and feedback; judge it by your monthly retests.'),
    ],
    resources=[
        ('psc-pyq', 'Collect two previous-year questions for each reasoning type from the mental-ability sections', '20 minutes'),
        ('ls-interleaving', 'Revisit the interleaving poster before building mixed sets', '5 minutes'),
        ('os-phil-5', 'Optional: read 5.4 Types of Inferences for the logic behind patterns', '15 minutes'),
    ],
    steps=[
        'For each of the eight reasoning types, write the method on an AnkiDroid card with one example.',
        'Solve two previous-year questions per type with the method, drawing a diagram for blood relations and directions.',
        'Set up the weekly maths and reasoning system in your study planner for next week.',
        'Run the first week: daily warm-ups, three mixed sets, one timed previous-paper section, and the Sunday Errors-tab review.',
        'Choose your weakest reasoning type for a practice loop next week.',
    ],
    proof='Your eight method cards, the solved PYQs with diagrams, and your first week\'s system log with scores.',
    templates=[
        ('reasoning methods card set', """
SERIES      differences -> ratios -> squares/cubes -> alternate terms; check EVERY term
CODING      A=1 ... Z=26; find the shift or pattern; apply it to the new word
ANALOGY     say the relationship in a sentence first
ODD ONE OUT find the rule three items share
RELATIONS   family tree: rows = generations, + male, - female, = married
DIRECTIONS  sketch with north at the top; track turns (right = clockwise)
CLOCKS      angle = difference between 30H and 5.5M (ignore the sign)
CALENDARS   ordinary year +1 weekday, leap year +2; count odd days
""", ''),
        ('weekly maths and reasoning system log', """
WEEK ___
Mon  warm-up ___/20 in ___ | mixed set ___/15 in ___ min
Tue  warm-up ___/20 in ___
Wed  warm-up ___/20 in ___ | mixed set ___/15 in ___ min
Thu  warm-up ___/20 in ___
Fri  warm-up ___/20 in ___ | mixed set ___/15 in ___ min
Sat  previous-paper mental ability section: ___/___ in ___ min
Sun  Errors tab updated [ ]  weakest type for next week: ______________
""", ''),
    ],
    mistakes=[
        ('Solving relations and directions in your head.', 'Draw them. A few seconds of sketching prevents most errors.'),
        ('Accepting a series rule that fits only two terms.', 'Check the rule against every term.'),
        ('Practising each reasoning type only in blocks.', 'Mix types in timed sets, as the exam does.'),
        ('Skipping clock and calendar rules because they seem hard.', 'Each is one formula or one rule, and questions on them are often quick marks.'),
    ],
    quiz=[
        {'q': 'What is the next number in 2, 6, 12, 20, 30, ...?', 'o': ['42', '40', '36', '44'], 'a': 'A', 'why': 'The differences are 4, 6, 8, 10, so the next difference is 12.'},
        {'q': 'What is the angle between the clock hands at 3:20?', 'o': ['20°', '30°', '0°', '40°'], 'a': 'A', 'why': '30 × 3 = 90 and 5.5 × 20 = 110; they differ by 20°.'},
        {'q': 'You walk 5 km north, turn right and walk 3 km, then turn right and walk 5 km. Where are you?', 'o': ['3 km east of the start', '3 km west of the start', 'Back at the start', '10 km south of the start'], 'a': 'A', 'why': 'North, then east, then south: you end 3 km east, facing south.'},
        {'q': 'If CAT is written DBU, how is DOG written?', 'o': ['EPH', 'CNF', 'EPG', 'DPH'], 'a': 'A', 'why': 'Each letter moves forward by one.'},
        {'q': '1 January 2025 was a Wednesday. What day is 1 January 2026?', 'o': ['Thursday', 'Friday', 'Wednesday', 'Tuesday'], 'a': 'A', 'why': '2025 is not a leap year, so the weekday moves on by one.'},
    ],
    study='Two previous-year questions per reasoning type, and the interleaving poster',
    action='Learn a method for eight reasoning types and run the first week of the maths and reasoning system',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    M,
    overview="""
Build speed and accuracy in PSC numerical ability and mental ability: mental-maths tricks made automatic, the core arithmetic topics solved from principles, a method for each reasoning type, and a weekly practice system.

For many aspirants, the mental ability section decides the rank. The good news is that it rewards method and practice more than talent. This module applies the course's strongest tools (worked examples, first principles, interleaving, immediate feedback and spaced cards) to the maths and reasoning in your syllabus.

The result is a maths and reasoning practice system that runs every week until your exam, with a monthly retest to measure progress.
""",
    outcomes=[
        'Use a dozen mental-maths tricks and check answers in seconds',
        'Make basic facts automatic with AnkiDroid and a daily warm-up',
        'Solve the core arithmetic topics from principles with a five-step method',
        'Solve eight common reasoning types with a method for each, drawing where it helps',
        'Run a weekly maths and reasoning system and measure it monthly',
    ],
    lessons=LESSONS,
    tools=[
        'The **mental maths warm-up log** and **checking an answer in seconds** list',
        '**Topic principle cards** and the **five-step solving sheet**',
        'The **reasoning methods card set** and the **weekly maths and reasoning system**',
    ],
    project='My maths and reasoning system',
    project_steps=[
        'Run the weekly system for two weeks in full.',
        'At the end, take a fresh mixed set of 30 (arithmetic and reasoning) under time and compare with the first mixed sets you did in this module.',
        'Choose the next two weakest types from your Errors tab and plan practice loops for them.',
    ],
    project_proof='Two weeks of the system log, the 30-question retest score and time compared with your first mixed sets, and your next two practice loops.',
    rubric=[
        ('Basics', 'Slow, error-prone calculations', 'Some tricks used', 'Daily warm-up with rising speed and accuracy'),
        ('Arithmetic topics', 'Formula hunting', 'Principles known for some topics', 'Principle cards for all core topics, PYQs solved with five steps'),
        ('Reasoning', 'Solved in the head, often wrong', 'Methods known', 'A method and a diagram where needed, for every type'),
        ('System', 'Practice when there is time', 'Some weekly practice', 'The weekly system run for two weeks with a measured retest'),
    ],
    short=[
        'Keep only the 10-minute daily warm-up and one mixed set of 15 a week.',
        'Draw every blood-relation and direction question.',
    ],
    flashcards=[
        ('Multiply by 25', '× 100, then divide by 4.'),
        ('Squares ending in 5', 'First digit × (first digit + 1), then 25.'),
        ('Successive percentage changes', 'a + b + (a × b) ÷ 100.'),
        ('Profit percentage is on...', 'The cost price.'),
        ('km/h to m/s', 'Multiply by 5/18.'),
        ('Average speed for a round trip', 'Total distance ÷ total time, not the average of the speeds.'),
        ('Angle between clock hands', 'The difference between 30 × hours and 5.5 × minutes.'),
        ('Odd days', 'An ordinary year moves the weekday by 1, a leap year by 2.'),
    ],
    mistakes=[
        ('Thinking you are "not a maths person".', 'Method and practice decide most of this section. Measure your progress.'),
        ('Practising only the types you like.', 'Your Errors tab chooses next week\'s practice.'),
    ],
)
