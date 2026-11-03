"""Module 13: Deliberate practice and skill acquisition."""
from common import lesson, module, link, fence, table

M = 13

L1 = lesson(
    M, 1,
    outcome='Design practice that targets your weakest PSC skill with immediate feedback, and run a practice loop that you can see improving session by session.',
    split='20 minutes reading, 15 minutes resources, 60 minutes action over three sessions',
    core=f"""
### Practice is not the same as repetition

Two aspirants each do maths for an hour a day. One solves the types she is already good at, checks the answers at the end, and feels productive. The other picks the type she gets wrong most, checks each answer immediately, works out exactly why it went wrong, and does two more of the same kind. After a month, the second one has improved far more. The difference is not the hours; it is the **kind** of practice.

The psychologist K. Anders Ericsson called the second kind **deliberate practice**: practice that

- **targets a specific weakness,** not the whole subject
- is **just beyond** what you can already do
- gives **immediate, specific feedback**
- **repeats with changes** until the weakness is fixed

### Honest evidence: practice matters, but it isn't everything

A popular idea says that practice is all it takes to become an expert ("10,000 hours"). In 2014, Macnamara, Hambrick and Oswald combined many studies and found that the amount of deliberate practice explained about **12%** of the differences in performance between people overall: about 26% in games, 21% in music, 18% in sports, 4% in education and less than 1% in professions ({link('macnamara', 'APS, 2014')}).

Read those numbers carefully. They describe **differences between people**: other things matter too, such as starting age, prior knowledge, teaching quality and individual ability. They do **not** mean that practice doesn't help **you** improve. For an exam, how you practise (retrieval, spacing, mixing, feedback) matters a great deal, as the research in Module 3 shows.

### Feedback loops

A **feedback loop** is the core of good practice:

1. **Attempt** one item: a problem, a sentence, a question.
2. **Check it immediately,** not after fifty items.
3. **Find the exact error:** which step, which rule, which fact.
4. **Fix it:** a rule card, a worked example, a contrast card.
5. **Attempt two more** of the same kind, to confirm the fix.

The faster and more specific the feedback, the faster you improve. Checking 100 answers at the end of a session tells you your score, but not much about what to change.

### Finding the edge

Practise where you get **some** items wrong but **most** right. If you get everything right, it is too easy; move on. If you get almost everything wrong, go back to worked examples (Module 1). Your Errors tab and Syllabus tab (Module 12) show you where the edge is.

### PSC feedback loops

{table(['Skill', 'Attempt', 'Immediate feedback', 'Fix'], [
    ('Arithmetic (e.g. time and work)', 'One problem at a time', 'Answer key after each problem', 'Rebuild the principle (LRN-M08-L04); two more of the same type'),
    ('English grammar (e.g. articles, prepositions)', 'Ten sentences', 'Check each against the key', 'A rule card with your wrong sentence corrected'),
    ('Malayalam grammar (e.g. sandhi, samasam)', 'Ten examples', 'Check with the textbook', 'A rule card with two examples'),
    ('Statement questions', 'One question', 'Check each statement\'s source', 'Note why each statement is true or false'),
])}
""",
    example="""
**Ashiq**'s Errors tab showed time-and-work problems as his weakest type. He used to practise them in sets of 25 and check at the end; his accuracy hovered around 55%.

He set up a practice loop: one problem, check immediately, name the exact error, fix it, and two more of the same kind. In session 1 he found that most of his errors came from one step: converting "A can do it in 12 days" into a daily rate. He made a rule card ("days → rate: 1/days") and a worked example.

Over three 20-minute sessions his accuracy went from 55% to 70% to 85%. By session 3 he was getting pipes-and-cisterns problems right too, because they use the same principle with one rate negative. He moved on to the next weak type in his Errors tab and set a review of time and work in his Revision tab for a week later.
""",
    evidence=[
        ('Practice on specific weaknesses with immediate feedback', 'moderate', 'Consistent with research on practice testing and feedback; the most useful form of practice for exam skills.'),
        ('Practice alone explains who becomes an expert ("10,000 hours")', 'none', 'Macnamara and others (2014): deliberate practice explained about 12% of performance differences overall, 4% in education.'),
        ('Practising at the edge: some wrong, most right', 'limited', 'A practical rule from skill learning; judge it by your accuracy trend.'),
    ],
    resources=[
        ('macnamara', 'Read the whole news release, including the numbers by field', '10 minutes'),
        ('dunlosky-aft', 'Reread the part on practice testing and feedback', '5 minutes'),
    ],
    steps=[
        'Use your Errors tab and Syllabus tab to choose your weakest PSC skill (a maths type, a grammar area or a question type).',
        'Prepare at least 40 items of that skill with answers: from previous papers, your guide or your textbook.',
        'Run three practice-loop sessions of about 20 minutes on different days: attempt one item, check it immediately, name the exact error, fix it, then attempt two more of the same kind.',
        'Record your accuracy in each session and the rule cards or worked examples you made.',
        'When accuracy passes about 80%, add the skill to your Revision tab and choose the next weakest skill.',
    ],
    proof='Your three practice-loop sheets with accuracy for each session, and the rule cards or worked examples you made.',
    templates=[
        ('practice loop sheet', """
PRACTICE LOOP     Skill: ______________________  Session ___  Date: ______
Item | Right? | Exact error (step / rule / fact)        | Fix (card / example / rule) | 2 more right?
1    | Y / N  | _______________________________________ | ___________________________ | __ / 2
2    | Y / N  | _______________________________________ | ___________________________ | __ / 2
...
Accuracy this session: ___ / ___ = ___%   (session 1 ___%  session 2 ___%  session 3 ___%)
Next: stay on this skill / move on (over 80%) / back to worked examples (under 40%)
""", ''),
        ('finding the edge', """
Almost all right (over 90%)   -> too easy: move to a harder type or mix it with others
Some wrong, most right        -> the edge: practise here with the loop
Almost all wrong (under 40%)  -> too hard: study worked examples first, then return
""", ''),
    ],
    mistakes=[
        ('Practising what you are already good at.', 'It feels good and teaches little. Practise your weakest skill.'),
        ('Checking answers only at the end.', 'Check each item immediately, so you can fix the error before repeating it.'),
        ('Repeating without changing anything.', 'Every error needs a specific fix: a rule, an example or a contrast.'),
        ('Reading the 12% figure as "practice doesn\'t work".', 'It describes differences between people; good practice still improves you.'),
    ],
    quiz=[
        {'q': 'Which is deliberate practice?', 'o': ['Picking your weakest maths type, checking each problem immediately and fixing the exact error', 'Solving 50 problems you already find easy', 'Watching a solved-problem video at 2x speed', 'Rereading the formula page'], 'a': 'A', 'why': 'It targets a weakness with immediate, specific feedback.'},
        {'q': 'What did Macnamara and others (2014) find?', 'o': ['Deliberate practice explained about 12% of performance differences overall, 4% in education', 'Practice explains 100% of expertise', 'Practice has no effect on anything', 'Only music needs practice'], 'a': 'A', 'why': 'Practice matters, but other factors also explain differences between people.'},
        {'q': 'Your accuracy on a skill is under 40%. What should you do?', 'o': ['Go back to worked examples, then return to practice', 'Practise faster', 'Skip the skill for good', 'Do 200 more problems the same way'], 'a': 'A', 'why': 'It is beyond your edge; worked examples build the base first.'},
        {'q': 'What makes feedback most useful?', 'o': ['It is immediate and specific', 'It comes once a month', 'It only gives the total score', 'It comes from a stranger'], 'a': 'A', 'why': 'Immediate, specific feedback lets you fix the exact error before repeating it.'},
    ],
    study='The APS release on Macnamara and others (2014) and Dunlosky on practice testing',
    action='Run three practice-loop sessions on your weakest PSC skill and track your accuracy',
)

L2 = lesson(
    M, 2,
    outcome='Plan and start a self-directed learning project for a new skill (AI tools, business, a language or anything else), with a clear outcome, a baseline test, free resources, a practice loop and a measure of progress.',
    split='20 minutes reading, 20 minutes resources, 50 minutes planning plus the first two hours of the project',
    core=f"""
### Your system works beyond PSC

The methods in this course work for anything you learn: AI tools, running a business, marketing, a new language, accounts, a craft. After PSC, or alongside it if your time allows, you will learn without a syllabus or an exam. That needs a plan you make yourself: a **self-directed learning project**.

### The learning project canvas

1. **Outcome:** what you will be able to **do**, so that someone could watch you do it. Not "learn AI", but "use an AI chat tool to draft and check a one-page letter in English and Malayalam". Not "learn Excel", but "build a monthly report with SUMIF and a chart".
2. **Why:** your reason (Module 6), in one line.
3. **Baseline:** a small test of the outcome now: try it and record the result, as you did in week 0.
4. **Skill map:** break the outcome into 4 to 8 sub-skills.
5. **Resources:** free, current and reliable: official guides, open textbooks, the other courses in this app. Choose one main resource per sub-skill; collecting twenty is a way to avoid starting.
6. **First 10 hours:** a concrete plan for the first 10 hours, with what you will **make or do** in each session.
7. **Practice loop:** how you will attempt, get feedback and fix (LRN-M13-L01).
8. **Feedback source:** an answer key, a test, a person who knows the skill, a community, or an AI tool whose answers you check (Module 17).
9. **Memory:** which facts or terms go into AnkiDroid.
10. **Measure and review:** repeat the baseline test at the end, with weekly reviews in between.

### Learn by making things

Projects work best when you **make something real** early: a spreadsheet, a short video, a one-page business plan, a conversation in a new language. You learn what you need, when you need it, and the thing you make shows your progress. Combine it with retrieval and spacing for the facts and terms that come up.

### Avoid tutorial traps

Watching course after course without making anything feels like learning but builds little skill: it is the fluency illusion again (Module 7). A good rule: for every hour of watching or reading, spend at least an hour doing.

### Where to start in this app

{table(['If you want to learn', 'Start with'], [
    ('AI tools for work, freelancing or business', 'The Free AI Generalist Course in this app'),
    ('Starting a small business', 'Practical Entrepreneurship in this app'),
    ('Marketing and freelancing with social media', 'Practical Social Media Marketing in this app'),
    ('Managing money', 'Practical Personal Finance in this app'),
    ('A new language', 'LRN-M15-L04 and ' + link('langtransfer', 'Language Transfer')),
])}

If your PSC exam is close, keep the project small (an hour or two a week) or plan it for after the exam. Your capstone (Module 21) can also be a 30-day sprint on a new skill instead of a PSC subject.
""",
    example="""
**Joseph sir** wanted his study group to be able to revise Malayalam grammar at home, so he decided to learn to make short explainer videos on his phone. At 61, he had never edited a video.

His canvas: the outcome was "a 3-minute video explaining one grammar rule, with clear sound, simple text on screen and one example". His baseline attempt took two hours and had echoing sound and no text. His skill map had five sub-skills: planning a script, recording clear audio, filming steady shots, simple editing with captions, and sharing. For feedback he asked the group to answer three questions after each video: Was it clear? Could you hear it? What would you change?

His first 10 hours each produced something: a script, an audio test in three rooms (a bedroom with curtains was best), a 30-second test video, and so on. After four weeks he made a 3-minute video on sandhi in 50 minutes, with clear sound and captions. The group now asks for one every week.
""",
    evidence=[
        ('Learning skills through practice with feedback', 'moderate', 'Consistent with research on practice testing and feedback.'),
        ('Self-directed, project-based learning', 'limited', 'Research on project-based learning is mixed; it works best with clear outcomes, feedback and retrieval of key knowledge.'),
        ('A baseline test repeated at the end', 'limited', 'A measuring tool rather than a technique; it makes progress visible.'),
    ],
    resources=[
        ('dunlosky-aps', 'Skim the ten techniques again and choose which you will use in your project', '10 minutes'),
        ('lhtl', 'Optional: Module 4 of Learning How to Learn on learning throughout life', 'About 3 hours'),
        ('langtransfer', 'If your project is a language: look at the free courses', '10 minutes'),
    ],
    steps=[
        'Choose one skill to learn on your own and fill in the learning project canvas below: a PSC skill that no lesson covers (for example letter or essay writing in English, or speaking for posts with an interview), or a skill for after PSC.',
        'Do the baseline test of your outcome and record the result.',
        'Choose one main free resource for each sub-skill, from this app\'s other courses or official and open sources.',
        'Plan your first 10 hours session by session, each producing something you make or do.',
        'Do the first two hours, log them in your Study Log, and put weekly project sessions and a review date in your calendar.',
    ],
    proof='Your completed learning project canvas, the baseline result and your log of the first two hours.',
    templates=[
        ('learning project canvas', """
LEARNING PROJECT CANVAS        Start: ______   Review date: ______
1. Outcome (what I will be able to DO): ______________________________________
2. Why: _____________________________________________________________________
3. Baseline test (try it now): _____________________  Result: _______________
4. Skill map (4-8 sub-skills): a. ______ b. ______ c. ______ d. ______ e. ______
5. Main resource per sub-skill (free): a. ______ b. ______ c. ______ d. ______
6. First 10 hours (what I make or do each session):
   1. ________ 2. ________ 3. ________ 4. ________ 5. ________
   6. ________ 7. ________ 8. ________ 9. ________ 10. _______
7. Practice loop: attempt ______ -> feedback from ______ -> fix -> repeat
8. Feedback source: ________________________________________________________
9. Facts and terms for AnkiDroid: deck name ______________
10. End test (repeat the baseline) on ______  Result: ______
""", ''),
        ('watch-to-do rule', """
For every hour of watching or reading, at least one hour of doing.
Doing = making something, solving something, saying something, or testing yourself.
Weekly check: watching/reading ___ h   doing ___ h   ratio OK?  yes / no
""", ''),
    ],
    mistakes=[
        ('A vague outcome ("learn AI").', 'Write an outcome someone could watch you do.'),
        ('Collecting resources instead of starting.', 'One main resource per sub-skill. Start the first session today.'),
        ('Skipping the baseline.', 'Without it, you can\'t see your progress.'),
        ('Running five projects at once.', 'One project at a time, especially while preparing for PSC.'),
        ('Watching tutorials without making anything.', 'Follow the watch-to-do rule.'),
    ],
    quiz=[
        {'q': 'Which is a well-written project outcome?', 'o': ['"Build a monthly report with SUMIF and a chart in Google Sheets"', '"Learn spreadsheets"', '"Get better at computers"', '"Watch an Excel course"'], 'a': 'A', 'why': 'It is something someone could watch you do.'},
        {'q': 'Why do a baseline test at the start of a project?', 'o': ['So you can measure your progress at the end', 'Because it is required by law', 'To decide whether to give up', 'It isn\'t useful'], 'a': 'A', 'why': 'Repeating it at the end shows what changed.'},
        {'q': 'What is the watch-to-do rule?', 'o': ['For every hour of watching or reading, at least an hour of doing', 'Watch three courses before doing anything', 'Never watch videos', 'Do first, never watch'], 'a': 'A', 'why': 'Doing builds skill; watching alone creates the fluency illusion.'},
        {'q': 'Your PSC exam is six weeks away. What does the lesson suggest for a new project?', 'o': ['Keep it very small, or plan it for after the exam', 'Start three projects now', 'Drop PSC study for the project', 'Never start projects'], 'a': 'A', 'why': 'The exam is the priority; the system will still work afterwards.'},
    ],
    study='Dunlosky\'s technique summary for choosing methods, and (optionally) Learning How to Learn Module 4',
    action='Fill in a learning project canvas for a new skill, take its baseline and do the first two hours',
)

LESSONS = [L1, L2]

MODULE = module(
    M,
    overview="""
Turn practice into improvement: target your weakest skills with immediate feedback in a practice loop, and plan self-directed learning projects for any skill you want after PSC.

Hours of practice are not equal. Practice that targets a weakness, gives immediate feedback and repeats with changes improves skills far faster than repeating what you can already do. This module is also honest about the limits: practice explains only part of why some people become experts, which is a reason to practise well, not a reason to stop.

The second lesson turns everything in this course into a plan for learning without a syllabus: the skill of learning anything you choose, for the rest of your life.
""",
    outcomes=[
        'Explain deliberate practice and the honest evidence about it',
        'Run a practice loop with immediate feedback on your weakest PSC skill',
        'Find the edge of your ability and adjust practice to it',
        'Plan a self-directed learning project with a clear outcome and baseline',
        'Avoid tutorial traps with the watch-to-do rule',
    ],
    lessons=LESSONS,
    tools=[
        'The **practice loop sheet** and **finding the edge** guide',
        'The **learning project canvas** and **watch-to-do rule**',
    ],
    project='My practice loop and learning project',
    project_steps=[
        'Show the accuracy trend from your three practice-loop sessions, and start a loop on the next weakest skill.',
        'Keep your learning project going for two more weeks with at least two sessions a week, each producing something.',
        'At the end of the two weeks, write a short review: what you can do now that you couldn\'t at the baseline.',
    ],
    project_proof='Your practice-loop accuracy trend for two skills, and your learning project canvas with logged sessions and the two-week review.',
    rubric=[
        ('Practice loop', 'Practising strengths', 'Weak skill chosen, feedback at the end', 'Weak skill, immediate feedback, specific fixes, rising accuracy'),
        ('Evidence', 'Believes "practice is everything" or "practice doesn\'t matter"', 'Knows the 12% figure', 'Can explain what the numbers do and don\'t mean'),
        ('Project plan', 'Vague goal', 'Outcome without baseline or plan', 'Complete canvas with baseline, 10-hour plan and feedback source'),
        ('Doing', 'Only watching', 'Some sessions with output', 'Every session produced something; watch-to-do rule kept'),
    ],
    short=[
        'Run one practice-loop session a week on your weakest skill.',
        'Fill in the learning project canvas and save the project for after your exam.',
    ],
    flashcards=[
        ('Four features of deliberate practice', 'Targets a weakness, just beyond your level, immediate feedback, repeats with changes.'),
        ('Macnamara and others (2014)', 'Deliberate practice explained about 12% of performance differences overall; 4% in education.'),
        ('What the 12% does not mean', 'It doesn\'t mean practice fails to help you; it describes differences between people.'),
        ('The five steps of a feedback loop', 'Attempt, check immediately, find the exact error, fix it, attempt two more.'),
        ('The edge of ability', 'Some items wrong, most right.'),
        ('A good project outcome', 'Something someone could watch you do.'),
        ('Watch-to-do rule', 'For every hour of watching or reading, at least an hour of doing.'),
    ],
    mistakes=[
        ('Counting practice hours instead of fixing errors.', 'Track accuracy and the fixes you made.'),
        ('Waiting for the perfect course before starting a project.', 'Start with one resource and make something in the first session.'),
    ],
)
