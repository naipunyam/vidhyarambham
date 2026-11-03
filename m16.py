"""Module 16: Thinking skills."""
from common import lesson, module, link, fence, table

M = 16

L1 = lesson(
    M, 1,
    outcome='Judge claims by their evidence and sources, check a forward or video claim in five minutes, and rank your PSC sources by reliability.',
    split='15 minutes reading, 30 minutes resources, 40 minutes action',
    core=f"""
### What critical thinking means

**Critical thinking** means judging a claim by its evidence and reasoning, not by who says it, how confident they sound or how many people share it. OpenStax's free *Introduction to Philosophy* explains how to gather information, evaluate sources and understand evidence ({link('os-phil-2', 'chapter 2, section 2.4')}).

For a PSC aspirant, this is practical every day: forwarded "notifications", coaching PDFs with wrong facts, guides that disagree with textbooks, and videos that promise secrets.

### Three kinds of claim

- **Facts:** can be checked ("The Temple Entry Proclamation was issued in 1936").
- **Opinions and values:** can be argued but not proved ("this is the best guide").
- **Predictions:** about the future ("these ten questions will come this year").

Facts need sources. Opinions need reasons. Predictions about exam questions deserve suspicion.

### Weighing evidence

Not all evidence is equal. From strongest to weakest, roughly:

1. **Official documents and data:** Kerala PSC notifications and syllabuses, Acts and government orders, PIB and PRD releases, official textbooks
2. **Reviews of research and expert consensus**
3. **Single studies and expert opinions**
4. **Personal stories and testimonials** ("I cleared PSC with this trick")
5. **Anonymous forwards and rumours**

### The five-minute check

Before you believe, save or share a claim:

1. **Stop.** Urgent tone, "forward to everyone", and claims that are too good or too bad to be true are warning signs.
2. **Find the original source.** Who first said it? Is there a link to an official page?
3. **Check it sideways.** Open the official website or a reliable source directly and search for the claim, instead of reading more of the same forward.
4. **Check the date.** Old notifications and old news are often recirculated as new.
5. **Decide:** believe, doubt or reject, and note the source you used.

### Ranking your PSC sources

When two sources disagree on a fact, the more official one usually wins. Final answer keys show what Kerala PSC accepted for a question (Module 12). Keep a short source ranking for your subjects, so you know where to check.

One warning: knowing a lot doesn't protect you automatically. In the neuromyths survey, teachers who knew more general facts about the brain believed **more** myths, probably because they read more popular material ({link('dekker', 'Dekker and others, 2012')}). Use the five-minute check, not your confidence.
""",
    example="""
**Joseph sir**'s study group WhatsApp group received a forward one evening: "URGENT: PSC changes negative marking to half a mark from next month. Share with all aspirants!" Three members had already shared it in other groups.

Joseph sir made it the evening's exercise. Stop: urgent tone, no link, "share with all". Original source: none given. Check sideways: the group opened the Kerala PSC website and found no such notification, and the OMR instructions on the site still showed the one-third rule. Date: the forward's image had an old-style logo. Verdict: reject.

Then each member checked one fact in their guide that disagreed with their SCERT textbook. Two of the five guide facts turned out to be wrong. The group agreed a rule: official source first, textbook second, guide third, forwards never without a check.
""",
    evidence=[
        ('Knowing more doesn\'t automatically protect against false beliefs', 'moderate', 'Dekker and others (2012): teachers with more general brain knowledge believed more neuromyths.'),
        ('Checking claims against original and official sources', 'limited', 'Standard advice in critical-thinking texts such as OpenStax Introduction to Philosophy; little research was checked for this course.'),
        ('A quick routine before believing or sharing', 'limited', 'A practical habit; judge it by how many errors it catches in your own sources.'),
    ],
    resources=[
        ('os-phil-2', 'Read 2.4 Gathering Information, Evaluating Sources, and Understanding Evidence', '25 minutes'),
        ('dekker', 'Reread the finding that more knowledge went with more myths', '5 minutes'),
        ('psc-home', 'Practise checking a claim about PSC rules against the official website', '10 minutes'),
    ],
    steps=[
        'Collect five claims: two from WhatsApp, YouTube or social media about PSC or current affairs, two facts where your guide and your textbook disagree, and one claim about learning or memory.',
        'Check each with the five-minute check. Write down the original source (if any), the official or reliable source you checked, the date, and your verdict.',
        'Write your source ranking for each PSC subject: what you check first, second and third.',
        'For one claim you rejected, write two lines on which warning signs you could have spotted earlier.',
    ],
    proof='Your five-claim check log with sources and verdicts, and your source ranking.',
    templates=[
        ('five-minute claim check', """
CLAIM CHECK      Date: ______
Claim: _______________________________________________________________
Where I saw it: _______________   Kind: fact / opinion / prediction
1. Stop: warning signs? urgent [ ] no source [ ] "share with all" [ ] too good/bad [ ]
2. Original source: _____________________________________ (none found [ ])
3. Checked sideways at: _________________________________
4. Date of the original: ______   Recirculated old item? yes / no
5. Verdict: believe / doubt / reject.   Source I will cite: ______________
""", ''),
        ('PSC source ranking', """
SUBJECT              1st check (official)          2nd (textbook)     3rd (guide/notes)
Constitution         ____________________          ______________     ______________
Kerala history       ____________________          ______________     ______________
Current affairs      PIB / PRD / ____________      ______________     ______________
Exam rules           Kerala PSC website            admission ticket   (never forwards)
""", ''),
    ],
    mistakes=[
        ('Believing claims because they sound confident.', 'Confidence is not evidence. Check the source.'),
        ('Sharing before checking.', 'Five minutes first. A wrong forward wastes many people\'s time.'),
        ('Trusting one source.', 'Check sideways against an official or reliable source.'),
        ('Checking only the claims you dislike.', 'Check claims you agree with too; that is where bias hides (LRN-M16-L04).'),
    ],
    quiz=[
        {'q': 'Which is the strongest evidence for a rule about PSC marking?', 'o': ['The instructions on the official Kerala PSC website', 'A forward with many shares', 'A coaching centre\'s poster', 'A friend\'s memory'], 'a': 'A', 'why': 'Official documents come first.'},
        {'q': 'What does "check it sideways" mean?', 'o': ['Open an official or reliable source directly and search for the claim', 'Read the forward again more slowly', 'Ask the person who forwarded it', 'Share it to see what people say'], 'a': 'A', 'why': 'Going outside the claim itself is how you test it.'},
        {'q': '"These ten questions will come in this year\'s exam." What kind of claim is it?', 'o': ['A prediction, which deserves suspicion', 'A checkable fact', 'An official rule', 'An opinion about books'], 'a': 'A', 'why': 'Predictions about exam questions can\'t be checked in advance.'},
        {'q': 'What did the neuromyths survey find about knowledge and myths?', 'o': ['Teachers with more general brain knowledge believed more myths', 'More knowledge always protects you', 'Nobody believed the myths', 'Only students believed myths'], 'a': 'A', 'why': 'Knowing more is not enough; use a checking routine.'},
    ],
    study='OpenStax Introduction to Philosophy 2.4 on sources and evidence',
    action='Check five claims with the five-minute routine and write your PSC source ranking',
)

L2 = lesson(
    M, 2,
    outcome='Tell deductive from inductive reasoning, test arguments for validity, solve syllogism and statement-conclusion questions with diagrams, and spot common fallacies.',
    split='15 minutes reading, 40 minutes resources, 35 minutes action',
    core=f"""
### Arguments

An **argument** gives reasons (premises) for a conclusion. OpenStax's *Introduction to Philosophy* covers arguments, types of inference and informal fallacies in its logic chapter ({link('os-phil-5', 'chapter 5')}).

### Deductive and inductive reasoning

- **Deductive:** if the premises are true and the form is valid, the conclusion **must** be true. "All rivers in this list flow west. The Periyar is in this list. So the Periyar flows west."
- **Inductive:** the premises make the conclusion **likely**, not certain. "Kerala history questions appeared in every one of my five previous papers, so they will probably appear this year."

**Validity is about form, not truth.** "All fish can fly; a shark is a fish; so a shark can fly" is valid (the conclusion follows) but unsound (a premise is false). In PSC reasoning questions, you are told to **accept the statements as true** even if they seem odd, and judge only whether the conclusion follows.

### Valid and invalid forms

{table(['Form', 'Pattern', 'Valid?'], [
    ('Affirming the condition (modus ponens)', 'If P, then Q. P. So Q.', 'Valid'),
    ('Denying the result (modus tollens)', 'If P, then Q. Not Q. So not P.', 'Valid'),
    ('Affirming the result', 'If P, then Q. Q. So P.', 'Invalid: Q could have other causes'),
    ('Denying the condition', 'If P, then Q. Not P. So not Q.', 'Invalid: Q could still happen'),
])}

Example: "If it rains, the match is cancelled. The match was cancelled. So it rained." Invalid: the match could have been cancelled for another reason.

### Syllogisms with Venn diagrams

PSC "statements and conclusions" questions are often **syllogisms**. Draw circles (Venn diagrams) and test every possible arrangement:

{table(['Statements', 'Conclusion', 'Follows?'], [
    ('All A are B. All B are C.', 'All A are C.', 'Yes'),
    ('Some A are B. All B are C.', 'Some A are C.', 'Yes'),
    ('All A are B. Some B are C.', 'Some A are C.', 'No: the C part of B may not include any A'),
    ('No A is B. All C are B.', 'No C is A.', 'Yes'),
])}

A conclusion **follows** only if it is true in **every** diagram you can draw from the statements. If you can draw even one diagram where it fails, it does not follow.

### Statements and assumptions

An **assumption** is something the statement takes for granted without saying it. "Use AnkiDroid daily to remember facts" assumes that AnkiDroid helps memory and that you want to remember facts. Ask: "What must be true for the speaker to say this?"

### Informal fallacies

Some arguments fail not in form but in content. Common ones:

- **Attacking the person** instead of the argument (ad hominem)
- **Straw man:** arguing against a weaker version of what someone said
- **False dilemma:** "either you join this coaching centre or you will fail"
- **Appeal to popularity:** "everyone uses this method, so it must work"
- **Hasty generalisation:** "my cousin passed using this book, so it is the best book"
- **Slippery slope:** "if you miss one day, you will never finish"
""",
    example="""
**Ashiq** lost marks in statements-and-conclusions questions because he answered from what he knew of the real world. For "All pens are birds; some birds are trees", he rejected every conclusion because "pens aren't birds".

He started drawing Venn diagrams for every syllogism and reminding himself: accept the statements, test every diagram. For "All A are B; some B are C; so some A are C", he drew two diagrams: one where the C part of B overlapped A and one where it didn't. Since the conclusion failed in the second, it didn't follow.

On ten previous-year syllogism questions he went from 5 right to 9 right. He also kept a fallacy log for a week from advertisements and forwards: a coaching centre ad that said "join us or stay unemployed" (false dilemma) and an app that boasted "a million downloads" as proof it works (appeal to popularity).
""",
    evidence=[
        ('Drawing Venn diagrams for syllogisms', 'moderate', 'Turns a working-memory task into a visual check (Modules 1 and 3); a standard method in logic teaching.'),
        ('Learning valid and invalid forms', 'limited', 'Helps with exam reasoning questions; evidence that logic training improves everyday reasoning is limited.'),
        ('Spotting informal fallacies', 'limited', 'A useful critical-thinking habit described in OpenStax; little research was checked for this course.'),
    ],
    resources=[
        ('os-phil-5', 'Read 5.3 Arguments, 5.4 Types of Inferences and 5.5 Informal Fallacies', '40 minutes'),
        ('psc-pyq', 'Collect 10 statements-and-conclusions or syllogism questions from previous papers', '10 minutes'),
    ],
    steps=[
        'Solve 10 syllogism or statements-and-conclusions questions from previous papers, drawing every possible Venn diagram before answering.',
        'Write three valid arguments and three invalid ones of your own on PSC topics, and name the form of each.',
        'Keep a fallacy log for a week: find five fallacies in advertisements, forwards or arguments you hear, and name each.',
        'Write two "statement and assumption" examples of your own and check them with a study partner.',
    ],
    proof='Your 10 diagram solutions with scores, your six arguments with their forms, and your fallacy log.',
    templates=[
        ('Venn diagram method for syllogisms', """
1. Accept every statement as true, even if it sounds strange.
2. Draw the circles for the statements. If more than one arrangement fits, draw each one.
3. A conclusion FOLLOWS only if it is true in EVERY diagram.
4. "Some A are B" means at least one A is B (it may be all).
5. Check: did I use real-world knowledge? If yes, start again.
""", ''),
        ('fallacy spotting card', """
FALLACY LOG      Week of ______
Where I met it            Claim                                  Fallacy
_______________________   ____________________________________   attacking the person / straw man /
_______________________   ____________________________________   false dilemma / popularity /
_______________________   ____________________________________   hasty generalisation / slippery slope
""", ''),
    ],
    mistakes=[
        ('Answering syllogisms with real-world knowledge.', 'Accept the statements as true; judge only the logic.'),
        ('Confusing valid with true.', 'Valid means the conclusion follows; true depends on the premises too.'),
        ('Drawing only one Venn diagram.', 'Draw every arrangement the statements allow.'),
        ('Treating "some" as "only some".', 'In logic, "some" means at least one, possibly all.'),
    ],
    quiz=[
        {'q': '"If it rains, the match is cancelled. The match was cancelled. So it rained." Is this valid?', 'o': ['No: affirming the result is invalid', 'Yes: it is modus ponens', 'Yes: the premises are true', 'No: denying the condition'], 'a': 'A', 'why': 'The match could have been cancelled for another reason.'},
        {'q': 'All A are B. Some B are C. Does "Some A are C" follow?', 'o': ['No', 'Yes', 'Only if A is large', 'Only on Sundays'], 'a': 'A', 'why': 'You can draw a diagram where the C part of B doesn\'t touch A.'},
        {'q': 'All A are B. All B are C. Does "All A are C" follow?', 'o': ['Yes', 'No', 'Only sometimes', 'Cannot be decided'], 'a': 'A', 'why': 'A sits inside B, which sits inside C.'},
        {'q': '"Either you join our coaching centre or you will fail the exam." Which fallacy is it?', 'o': ['False dilemma', 'Straw man', 'Attacking the person', 'Slippery slope'], 'a': 'A', 'why': 'It pretends there are only two options.'},
        {'q': 'What is the difference between deductive and inductive reasoning?', 'o': ['Deductive conclusions must follow from true premises; inductive ones are only likely', 'They are the same', 'Inductive is always wrong', 'Deductive needs numbers'], 'a': 'A', 'why': 'Deduction gives certainty from valid form; induction gives probability.'},
    ],
    study='OpenStax Introduction to Philosophy 5.3, 5.4 and 5.5',
    action='Solve 10 syllogism questions with Venn diagrams, write six arguments and keep a fallacy log',
)

L3 = lesson(
    M, 3,
    outcome='Use a four-step problem-solving process and a handful of mental models to handle unfamiliar PSC questions and everyday study decisions.',
    split='15 minutes reading, 35 minutes resources, 40 minutes action',
    core=f"""
### Problem-solving strategies

OpenStax *Psychology 2e* describes several strategies people use to solve problems: **trial and error**, **algorithms** (step-by-step procedures that always work, like a formula), **heuristics** (rules of thumb that usually work) and **working backwards** from the goal. It also names common obstacles: **functional fixedness** (seeing an object only in its usual role) and a **mental set** (sticking with a method that worked before, even when it doesn\'t fit) ({link('os-psych-7-3', 'OpenStax Psychology 2e, 7.3')}).

### Four steps for any problem

The mathematician George Pólya, in his classic book *How to Solve It*, set out four steps that suit almost any problem:

1. **Understand the problem.** What is being asked? What is given? What are the units? Is there a NOT or EXCEPT?
2. **Make a plan.** Which type is it? Which principle or method fits (Modules 8 and 14)?
3. **Carry out the plan,** step by step.
4. **Look back.** Does the answer make sense? Can you check it another way?

Most PSC errors happen in step 1 (misreading) or step 4 (no check), not in the calculation.

### A small set of mental models

A **mental model** is a simple idea that explains or guides many situations. A few are worth keeping:

{table(['Model', 'The idea', 'PSC use'], [
    ('First principles', 'Rebuild from basic truths', 'Arithmetic rules (LRN-M08-L04)'),
    ('Working backwards', 'Start from the goal or the options', 'Test MCQ options in the question; plan backwards from the exam date'),
    ('Elimination', 'Rule out what can\'t be true', 'Improve your odds before answering (LRN-M12-L04)'),
    ('Opportunity cost', 'Every hour on one thing is an hour not spent on another', 'Choosing topics by priority; an hour of Reels costs an hour of review'),
    ('Inversion', 'Ask "what would make me fail?" and avoid it', 'Exam planning: list the ways to fail, then prevent each'),
    ('Second-order thinking', 'Ask "and then what?"', 'Adding 50 new cards today means 500 reviews later (Module 4)'),
    ('The 80/20 rule of thumb', 'A few causes often produce most of the effect', 'A few topics may carry many marks; check with your PYQ data, as it is not a law'),
])}

Use models as **questions to ask**, not as fancy words. Their value is in making you look at a problem from another side.

### Getting unstuck

When you are stuck: reread the question (step 1 again), try a simpler version with small numbers, draw it, work backwards from the options, or take a short break. A break works partly because it lets you drop a mental set and see the problem fresh.
""",
    example="""
**Anu** used inversion on her 12-week plan. She asked: "How could I fail the next exam?" Her list: sleeping late before mocks, skipping AnkiDroid when tutoring ran late, leaving maths to the end, misreading NOT questions, and losing a week to a family function without a plan.

Next to each she wrote a countermeasure: a fixed bedtime the night before mocks, a 10-card minimum on tutoring days, maths blocks in the morning, underlining NOT, and a buffer week in the plan. She put the list inside her notebook cover.

She also used Pólya's four steps on five unfamiliar previous-year questions she would usually have skipped. Writing "what is being asked?" first made her notice that two of them asked for the difference, not the total. She got four of the five right, and for the fifth, working backwards from the options found the answer.
""",
    evidence=[
        ('Problem-solving strategies and obstacles', 'limited', 'Described in OpenStax Psychology 2e; useful structure, but teaching them alone has limited evidence of wide transfer.'),
        ('Pólya\'s four steps', 'limited', 'A classic, widely taught framework; little direct research was checked for this course.'),
        ('Mental models such as inversion and opportunity cost', 'limited', 'Practical thinking tools; judge them by the decisions and plans they improve.'),
    ],
    resources=[
        ('os-psych-7-3', 'Read the section on problem-solving strategies and the obstacles to problem solving', '20 minutes'),
        ('os-phil-2', 'Read 2.3 Developing Good Habits of Mind', '15 minutes'),
    ],
    steps=[
        'Choose five unfamiliar previous-year questions (maths, reasoning or GK). Solve each on paper using the four steps, writing a line for each step.',
        'Solve five MCQs by working backwards from the options, and note when it is faster than solving forwards.',
        'Use inversion on your exam plan: list at least five ways you could fail, and a countermeasure for each.',
        'Use opportunity cost and second-order thinking on one real decision this week (for example, whether to add a new subject deck, or how to spend Saturday), and write your reasoning in five lines.',
    ],
    proof='Your five four-step solutions, the five working-backwards solutions, your inversion list with countermeasures and your decision note.',
    templates=[
        ('four-step problem sheet', """
Q ___
1. UNDERSTAND: asked for ______________ | given ______________ | units ______ | NOT/EXCEPT? ___
2. PLAN: type ______________ | method or principle ______________________________
3. CARRY OUT: _________________________________________________________________
4. LOOK BACK: does it make sense? ___ | checked by ______________ | answer ______
""", ''),
        ('inversion list', """
GOAL: ______________________________________
How could I fail?                         Countermeasure
1. _____________________________________  _________________________________
2. _____________________________________  _________________________________
3. _____________________________________  _________________________________
4. _____________________________________  _________________________________
5. _____________________________________  _________________________________
""", ''),
    ],
    mistakes=[
        ('Calculating before understanding the question.', 'Step 1 first: what is asked, what is given, any NOT or EXCEPT?'),
        ('Sticking with a method that isn\'t working.', 'That is a mental set. Try another approach, or work backwards.'),
        ('Using mental models as jargon.', 'Use them as questions that make you look at the problem another way.'),
        ('Treating 80/20 as an exact law.', 'It is a rule of thumb. Check your own PYQ data.'),
    ],
    quiz=[
        {'q': 'What are Pólya\'s four steps?', 'o': ['Understand, plan, carry out, look back', 'Read, guess, mark, move on', 'Survey, question, read, review', 'Plan, practise, perform, praise'], 'a': 'A', 'why': 'They come from his classic book How to Solve It.'},
        {'q': 'What is a mental set?', 'o': ['Sticking with a method that worked before even when it doesn\'t fit', 'A set of flashcards', 'A group of study partners', 'A type of syllogism'], 'a': 'A', 'why': 'OpenStax lists it as an obstacle to problem solving.'},
        {'q': 'Which question uses inversion?', 'o': ['"How could I fail the next exam, and how do I prevent each cause?"', '"How do I get full marks?"', '"Which book is the best?"', '"What did I study yesterday?"'], 'a': 'A', 'why': 'Inversion looks at the goal from the opposite side.'},
        {'q': 'You add 50 new AnkiDroid cards today. What does second-order thinking ask?', 'o': ['"And then what?": about ten times as many reviews later', '"How do I add 50 more?"', '"Who made this app?"', '"Why not 100?"'], 'a': 'A', 'why': 'It looks at the consequences of the consequences (Module 4).'},
    ],
    study='OpenStax Psychology 2e 7.3 on problem solving and Introduction to Philosophy 2.3',
    action='Solve unfamiliar PYQs with the four steps and working backwards, and apply inversion to your exam plan',
)

L4 = lesson(
    M, 4,
    outcome='Recognise the cognitive biases that most affect study and exams, audit them in your own recent decisions, and use a debiasing checklist.',
    split='15 minutes reading, 35 minutes resources, 35 minutes action',
    core=f"""
### What a bias is

A **cognitive bias** is a systematic error in thinking: not a random slip, but a predictable way in which human minds go wrong. OpenStax *Psychology 2e* describes several, including anchoring, confirmation bias, hindsight bias, the representative bias and the availability heuristic ({link('os-psych-7-3', 'OpenStax Psychology 2e, 7.3')}), and OpenStax *Introduction to Philosophy* discusses how to overcome them ({link('os-phil-2', 'section 2.2')}).

### Seven biases in a PSC aspirant's life

{table(['Bias', 'What it is', 'How it shows up in study', 'Fix'], [
    ('Confirmation bias', 'Noticing only evidence that supports what you already believe', '"My method works": you remember the good mocks and forget the bad ones', 'Look at all your scores in the Weekly tab'),
    ('Anchoring', 'Being pulled by the first number or option you see', 'The first option looks right, so you stop thinking', 'Cover the options and answer first (Module 3)'),
    ('Availability', 'Judging by what comes to mind easily', 'A vivid question from last year feels "important"', 'Use your PYQ counts, not memorable questions'),
    ('Hindsight', '"I knew it all along" after seeing the answer', 'Marking a topic green after reading the key', 'Answer before checking (Module 7)'),
    ('Overconfidence', 'Feeling surer than your accuracy justifies', 'Sure-but-wrong answers under negative marking', 'Your calibration table (LRN-M07-L02)'),
    ('Sunk cost', 'Continuing something because of what you already spent', 'Using a poor guide or coaching material because you paid for it', 'Judge by what helps from now on, not by past cost'),
    ('Planning fallacy', 'Underestimating how long things take', 'A plan that needs 40 hours a week when you have 20', 'Plan from your Study Log hours (LRN-M12-L05)'),
])}

### Knowing isn't enough

Learning the names of biases doesn't make you immune to them. Remember the neuromyths survey: more knowledge went with more myths (LRN-M16-L01). What helps is **outside structure**: data, checklists and other people.

### A debiasing checklist for decisions

Before a decision that matters (a study plan, a coaching course, a change of method, whether to apply for a post):

1. **What would change my mind?** If nothing could, you are not deciding; you are defending.
2. **What does my data say?** Study Log, Weekly tab, Errors tab, mock scores.
3. **What is the outside view?** How long did similar plans take before? How did similar people do?
4. **What would I advise a friend?** Distance reduces bias.
5. **Sleep on it,** if it involves money or a big commitment.
6. **Ask someone** who will disagree with you honestly.

### Don't overcorrect

The goal is not to doubt everything until you can't act. Use the checklist for decisions that matter, trust your data, decide, and review the decision in a few weeks.
""",
    example="""
**Sreeja** did a bias audit of her last month. Sunk cost: she had kept working through a set of coaching PDFs she had paid ₹1,500 for, though her error log showed they had several wrong answers; she switched to previous papers and textbooks. Planning fallacy: her first 12-week plan assumed 25 hours a week, while her Study Log showed 14; she rebuilt the plan.

Confirmation bias was harder to see. She was sure evening study suited her, and she remembered her good evening sessions. Her Focus tab showed that her evening blocks had twice as many distractions as her morning ones.

She used the debiasing checklist on one decision: whether to join a new paid crash course. What would change her mind? Evidence that it covered her weak topics better than her free sources. Her data: her weakest areas were mental ability and English grammar, which the course barely covered. She decided not to join, and wrote a note to review the decision after her next mock.
""",
    evidence=[
        ('Cognitive biases exist and affect judgement', 'strong', 'A well-established area of psychology, described in OpenStax Psychology 2e.'),
        ('Learning about biases protects you from them', 'limited', 'Awareness alone helps little; outside structure (data, checklists, other people) helps more.'),
        ('Using data and checklists for decisions', 'limited', 'Practical debiasing tools; judge them by the decisions you review later.'),
    ],
    resources=[
        ('os-psych-7-3', 'Read the part on biases and heuristics, with its table of biases', '15 minutes'),
        ('os-phil-2', 'Read 2.2 Overcoming Cognitive Biases and Engaging in Critical Reflection', '20 minutes'),
    ],
    steps=[
        'For each of the seven biases in the table, write one example from your own study or decisions in the last month, and a fix.',
        'Check each example against your data where you can (Study Log, Weekly, Focus and Errors tabs).',
        'Choose one real decision you face this week and go through the debiasing checklist in writing.',
        'Put a review date for that decision in your calendar, two to four weeks away.',
    ],
    proof='Your seven-bias audit with examples and fixes, and your written checklist for one decision with its review date.',
    templates=[
        ('bias audit', """
BIAS AUDIT      Month: ______
Bias                My example (last month)                    Data that shows it      Fix
Confirmation        ________________________________________   ____________________    ______________
Anchoring           ________________________________________   ____________________    ______________
Availability        ________________________________________   ____________________    ______________
Hindsight           ________________________________________   ____________________    ______________
Overconfidence      ________________________________________   ____________________    ______________
Sunk cost           ________________________________________   ____________________    ______________
Planning fallacy    ________________________________________   ____________________    ______________
""", ''),
        ('debiasing checklist', """
DECISION: _____________________________________________   Date: ______
[ ] What would change my mind? ________________________________________
[ ] What does my data say? ____________________________________________
[ ] Outside view (similar cases before): ________________________________
[ ] What would I advise a friend? _____________________________________
[ ] Slept on it (if money or a big commitment) [ ]
[ ] Asked someone who will disagree honestly: ______________ said ______
Decision: ______________________   Review on: ______
""", ''),
    ],
    mistakes=[
        ('Seeing biases only in other people.', 'Audit your own decisions with your own data.'),
        ('Thinking "I know about biases, so I\'m safe".', 'Knowledge alone protects little. Use checklists and data.'),
        ('Doubting everything until you can\'t act.', 'Use the checklist for decisions that matter, then decide and review.'),
        ('Keeping a bad resource because you paid for it.', 'Past cost is gone. Judge by what helps from now on.'),
    ],
    quiz=[
        {'q': 'You keep using coaching notes you paid for, though your error log shows they have wrong answers. Which bias?', 'o': ['Sunk cost', 'Anchoring', 'Hindsight', 'Availability'], 'a': 'A', 'why': 'Past spending shouldn\'t decide future use.'},
        {'q': 'How do you reduce anchoring in MCQs?', 'o': ['Cover the options and answer first', 'Always pick the first option', 'Read the options twice before the question', 'Guess quickly'], 'a': 'A', 'why': 'The first option you see shouldn\'t pull your answer.'},
        {'q': 'Your plan needs 40 hours a week; your Study Log shows 20. Which bias?', 'o': ['Planning fallacy', 'Confirmation bias', 'Hindsight bias', 'Sunk cost'], 'a': 'A', 'why': 'People underestimate how long things take; plan from real data.'},
        {'q': 'What does the research suggest about learning the names of biases?', 'o': ['It alone protects little; data, checklists and other people help more', 'It makes you immune', 'It makes bias worse every time', 'It replaces all decisions'], 'a': 'A', 'why': 'Outside structure is what changes decisions.'},
    ],
    study='OpenStax Psychology 2e 7.3 on biases and Introduction to Philosophy 2.2',
    action='Audit seven biases in your own recent decisions and use the debiasing checklist on one real decision',
)

LESSONS = [L1, L2, L3, L4]

MODULE = module(
    M,
    overview="""
Think more clearly: judge claims by evidence and sources, test arguments with logic and Venn diagrams, solve unfamiliar problems with a four-step process and a few mental models, and catch the cognitive biases that distort study decisions.

Thinking skills appear in PSC papers directly (statements and conclusions, assumptions, syllogisms) and indirectly in every decision about how to prepare. This module uses free OpenStax books on philosophy and psychology, applies them to PSC questions and to forwards, guides and coaching claims, and is honest that knowing about thinking errors is not the same as avoiding them.

The result is a thinking toolkit: the five-minute claim check, the Venn method, the four-step sheet, the inversion list and the debiasing checklist.
""",
    outcomes=[
        'Judge claims by evidence and rank your PSC sources',
        'Tell deductive from inductive reasoning and test validity',
        'Solve syllogisms with Venn diagrams and spot common fallacies',
        'Use Pólya\'s four steps and a few mental models on unfamiliar problems',
        'Audit your own biases and use a debiasing checklist for decisions',
    ],
    lessons=LESSONS,
    tools=[
        'The **five-minute claim check** and **PSC source ranking**',
        'The **Venn diagram method** and **fallacy spotting card**',
        'The **four-step problem sheet** and **inversion list**',
        'The **bias audit** and **debiasing checklist**',
    ],
    project='My thinking toolkit',
    project_steps=[
        'Check five more claims you meet this week with the five-minute check.',
        'Solve a mixed set of 15 reasoning questions from previous papers (syllogisms, assumptions, statements and conclusions), with diagrams where needed.',
        'Review the decision you made with the debiasing checklist: was it right, given what happened?',
        'Put your five tools on one page: your thinking checklist for study and exams.',
    ],
    project_proof='Your five new claim checks, the 15-question mixed set with score, your decision review and your one-page thinking checklist.',
    rubric=[
        ('Claims and sources', 'Believes forwards', 'Checks sometimes', 'Checks claims with the routine and ranks sources'),
        ('Logic', 'Answers syllogisms from real-world knowledge', 'Draws one diagram', 'Draws every diagram and knows valid forms'),
        ('Problem solving', 'Calculates before understanding', 'Uses some steps', 'Uses all four steps and working backwards'),
        ('Biases', 'Sees biases only in others', 'Knows the names', 'Audited own biases and used the checklist on a real decision'),
    ],
    short=[
        'Use the five-minute claim check on every forward about PSC.',
        'Draw Venn diagrams for every syllogism question.',
    ],
    flashcards=[
        ('Critical thinking', 'Judging claims by evidence and reasoning, not by who says them or how confident they sound.'),
        ('The five-minute check', 'Stop, find the original source, check sideways, check the date, decide.'),
        ('Valid versus sound', 'Valid: the conclusion follows. Sound: valid and the premises are true.'),
        ('Affirming the result (invalid)', 'If P then Q; Q; so P.'),
        ('When a syllogism conclusion follows', 'Only if it is true in every possible diagram.'),
        ('Pólya\'s four steps', 'Understand, plan, carry out, look back.'),
        ('Inversion', 'Ask "what would make me fail?" and prevent each cause.'),
        ('Sunk cost bias', 'Continuing something because of what you already spent on it.'),
        ('Planning fallacy', 'Underestimating how long things take; plan from your real data.'),
    ],
    mistakes=[
        ('Treating thinking skills as theory.', 'Use them on today\'s forwards, questions and decisions.'),
        ('Judging other people\'s thinking more harshly than your own.', 'Audit your own decisions first.'),
    ],
)
