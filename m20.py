"""Module 20: Teaching others and study groups."""
from common import lesson, module, link, fence, table

M = 20

L1 = lesson(
    M, 1,
    outcome='Teach a PSC topic to a family member or study partner with a plan that makes you recall and explain without notes, collect feedback, and test both of you afterwards.',
    split='15 minutes reading, 30 minutes resources, 45 minutes preparing and teaching plus a 10-minute test later',
    core=f"""
### Why teaching teaches the teacher

You have probably noticed that you understand a topic better after explaining it to someone. Research on **learning by teaching** supports this, with some important details. In a review written for teachers, the educational psychologist Logan Fiorella explains that **preparing** to teach gives only a modest and mixed benefit, while **actually explaining** to others helps more. The benefit is strongest when you explain **without notes**, because teaching then becomes retrieval practice. It works best in a relaxed, low-stakes setting, and learners often need some support to explain well ({link('fiorella', 'Fiorella, Learning by Teaching')}).

So the useful part is not making beautiful teaching materials. It is standing in front of someone and producing the explanation from your own head.

### Who to teach

- **A study partner** preparing for the same exam: you can quiz each other afterwards.
- **A family member** who isn't preparing at all: a parent, a spouse, a sibling. Their simple questions ("but why?", "what does that word mean?") expose gaps quickly. Teach in Malayalam if that is easier for them; the explaining is what matters.

### A 10-minute lesson plan

1. **Choose one small topic** you have studied: one article, one movement, one maths method. Not a whole chapter.
2. **Write a one-card outline:** three or four key points, one example from daily life and one simple drawing (a timeline, a map, a diagram). No full script.
3. **Start with a question** to your learner: "Do you know why...?" It gets them thinking and shows what they know.
4. **Explain each point without reading,** with the example and the drawing.
5. **Check understanding:** ask them two questions, and ask them to explain one point back to you.
6. **Ask for feedback:** "What was clear? What was confusing? What would you ask me?"
7. **Test both of you** two or three days later with five questions.

Recording the lesson on your phone, with permission, lets you listen for the same gaps as in a Feynman explanation (Module 8).

### Teaching is a mirror

The moments when you hesitate, use a word you can't explain, or can't answer "why?" are exactly your gaps. Write them down straight after the lesson and fix them from your source. This lesson is the course's required teaching task, and it often becomes many people's favourite way to revise.
""",
    example="""
**Anu** taught the Fundamental Duties to her mother, who had never studied the Constitution. Her one-card outline had four points: what the duties are, when and how they were added, two examples, and why they can't be enforced in court like rights. Her drawing was a simple timeline: 1950 (Constitution), 1976 (42nd Amendment, ten duties), 2002 (86th Amendment, the eleventh duty).

She began with a question: "Amma, do you think citizens should have duties written in the Constitution, or only rights?" Her mother's answer led straight into the first point. The hardest moment came when her mother asked, "If they can't punish you for not doing them, what's the use?" Anu fumbled. Afterwards she looked it up in her textbook and wrote a better answer on the back of her card.

Three days later she gave her mother and herself five questions each. Her mother got 3; Anu got 5. Her mother's feedback was the most useful part: "Your drawing was clear, but you said 'Directive Principles' without telling me what they are."
""",
    evidence=[
        ('Explaining to others, especially without notes', 'moderate', 'Fiorella (2023): explaining helps more than only preparing to teach, most of all as a retrieval activity.'),
        ('Only preparing to teach', 'limited', 'Fiorella describes the benefit of preparing alone as modest and mixed.'),
        ('Collecting the learner\'s feedback and questions', 'limited', 'A practical way to find your gaps; little direct research on this step.'),
    ],
    resources=[
        ('fiorella', 'Read the whole chapter: when teaching helps, and why explaining without notes matters', '30 minutes'),
    ],
    steps=[
        'Choose a small PSC topic you have studied, and a learner: a family member or your study partner.',
        'Write a one-card outline with three or four points, one everyday example and one simple drawing.',
        'Teach a 10-minute lesson without reading: start with a question, explain each point, then ask two questions and have your learner explain one point back. Record it if they agree.',
        'Ask the three feedback questions, and write down every gap you noticed in yourself.',
        'Fix the gaps from your source. Two or three days later, give both of you the same five questions and score them.',
    ],
    proof='Your one-card outline, the feedback and gaps you wrote down, the fixes, and both test scores. This is the course\'s required teaching task.',
    templates=[
        ('10-minute lesson plan card', """
LESSON CARD     Topic: ______________________  Learner: ______________  Date: ______
Opening question: _________________________________________________________
Key points (3-4):
1. ______________________________  2. ______________________________
3. ______________________________  4. ______________________________
Everyday example: _________________________________________________________
Drawing: timeline / map / diagram (draw it on the back)
Check: Q1 ____________________  Q2 ____________________  Explain-back: point ___
""", ''),
        ('after the lesson', """
FEEDBACK (ask the learner)
What was clear? _____________________________________________
What was confusing? _________________________________________
What would you ask me? ______________________________________
MY GAPS (hesitations, words I couldn't explain, "why?" I couldn't answer)
1. ____________________ fixed from ____________ page ___
2. ____________________ fixed from ____________ page ___
TEST after ___ days (same 5 questions): learner ___/5   me ___/5
""", ''),
    ],
    mistakes=[
        ('Reading from notes while teaching.', 'Explain from memory; that is what makes teaching retrieval practice.'),
        ('Lecturing without questions.', 'Start with a question and check understanding twice.'),
        ('Choosing a whole chapter.', 'One small topic in 10 minutes is enough.'),
        ('Skipping the follow-up test.', 'Test both of you after a few days to see what stuck.'),
    ],
    quiz=[
        {'q': 'According to Fiorella, what makes learning by teaching most effective?', 'o': ['Actually explaining, especially without notes', 'Spending hours preparing slides', 'Reading your notes aloud', 'Teaching only experts'], 'a': 'A', 'why': 'Explaining without notes turns teaching into retrieval practice.'},
        {'q': 'What is the benefit of only preparing to teach, without teaching?', 'o': ['Modest and mixed', 'Larger than teaching itself', 'Zero in every study', 'Always harmful'], 'a': 'A', 'why': 'The bigger benefit comes from actually explaining.'},
        {'q': 'Why can teaching a family member who isn\'t preparing for PSC be useful?', 'o': ['Their simple questions expose your gaps quickly', 'They will correct every fact', 'They will take the exam for you', 'It isn\'t useful'], 'a': 'A', 'why': '"Why?" and "what does that mean?" reveal what you can\'t yet explain.'},
        {'q': 'What should you do with the moments you hesitated while teaching?', 'o': ['Write them down and fix them from your source', 'Forget them', 'Blame the learner', 'Teach faster next time'], 'a': 'A', 'why': 'They are exactly your gaps.'},
    ],
    study='Fiorella\'s chapter on learning by teaching',
    action='Teach a 10-minute PSC lesson to a family member or study partner, fix your gaps and test both of you',
)

L2 = lesson(
    M, 2,
    outcome='Set up or improve a study group, in person or online, with roles, rules and a meeting format that make every meeting active recall instead of chat.',
    split='15 minutes reading, 15 minutes resources, 20 minutes setting up plus two meetings',
    core=f"""
### What groups do well, and badly

A good study group gives you **accountability** (someone notices if you skip), **explanations** from different minds, **quizzing** that feels like a game, and **company** on a long road. A bad one becomes a chat session, a place where one strong member lectures and others listen passively, a source of unchecked forwards, or a daily reminder that someone else is "ahead".

The difference is structure.

### Set-up

- **Size:** 3 to 5 people. A single **accountability partner** works too.
- **Fixed time and place:** for example Saturday, 4 to 5 p.m., at the library, or a weekly video call.
- **Shared goal:** the same exam, or at least the same paper.
- **Roles that rotate each meeting:**
    - **Quizmaster:** brings 15 questions (previous papers, or written from the week's topics)
    - **Explainer of the week:** prepares one topic to teach without notes (LRN-M20-L01)
    - **Fact-checker:** checks any disputed fact against the textbook or an official source
    - **Timekeeper:** keeps the agenda moving

### A 60-minute meeting format

{table(['Minutes', 'What happens', 'Why'], [
    ('0–5', 'Check-in: each person says last week\'s goal and whether they met it', 'Accountability'),
    ('5–20', 'Quiz: the quizmaster asks questions; everyone answers on paper with options covered, then checks', 'Retrieval practice'),
    ('20–40', 'Teach-back: the explainer teaches one topic without notes; then each member explains one point back', 'Learning by teaching'),
    ('40–50', 'Error swap: each shares one mistake from their error log and its fix', 'Learning from others\' errors'),
    ('50–55', 'Plan: next week\'s goal for each person, written as an if-then plan', 'If-then plans'),
    ('55–60', 'Buffer', 'Meetings run late'),
])}

### Online groups

WhatsApp and Telegram groups can help or distract. Rules that keep them useful:

1. **No forwards without a source,** and the five-minute check before sharing anything (Module 16).
2. **One question a day,** posted by a rotating member; answers by reply, explanation the next morning.
3. **Voice notes for explanations,** two minutes, no notes: teaching in miniature.
4. **The group is muted** outside its daily window (Module 5).
5. **A weekly call** using the meeting format above.

### Share the work, not the learning

Groups can split work that takes time: tagging previous papers (each tags one paper), checking guide facts, collecting vocabulary from papers. But each member still **makes their own cards and does their own recall**. Sharing someone else's AnkiDroid deck skips the processing that helps you learn (Module 4).

### Handling comparison

Agree as a group to compare each person with their own past (their Weekly tab), not with each other. Celebrate improvements, not just top scores.
""",
    example="""
**Joseph sir**'s group at the Thottilpalam panchayat library had started as an evening chat about PSC news. Attendance was falling, and nobody could say what they had learned in a meeting.

They wrote a one-page charter with this lesson's template: Saturday 4 to 5 p.m., four rotating roles, and the 60-minute format. Their WhatsApp group got three rules: sources for every forward, one question a day, and mute outside 8 to 9 p.m.

In their first structured meeting, the quiz showed that everyone was weak on the same topic, Centre-State relations, so Sreeja volunteered to be the next week's explainer. The error swap was the surprise: hearing four different mistakes in ten minutes was, as Vinod said, "like four mocks for the price of one". After a month, all five members were coming every week, and their average quiz score had risen from 9 to 12 out of 15.
""",
    evidence=[
        ('Quizzing each other (retrieval practice)', 'strong', 'Practice testing is rated high utility; a group quiz is practice testing with company.'),
        ('Explaining to each other', 'moderate', 'Learning by teaching helps, especially without notes (Fiorella, 2023).'),
        ('Study groups in general', 'limited', 'Results depend heavily on structure; little direct research was checked for this course.'),
    ],
    resources=[
        ('fiorella', 'Reread the parts on low-stakes settings and on supporting explainers', '10 minutes'),
        ('ls-retrieval', 'Use the retrieval practice poster to explain the quiz part to your group', '5 minutes'),
        ('psc-pyq', 'The quizmaster\'s source: previous papers for the group\'s exam', 'As needed'),
    ],
    steps=[
        'Form a group of 3 to 5 PSC aspirants, or find one accountability partner. If you already have a group, use this lesson to improve it.',
        'Write and agree a one-page group charter with the template below: time, place, roles, rules and the meeting format.',
        'Run two meetings with the 60-minute format, rotating roles. Record each meeting\'s quiz scores and the topics taught.',
        'If the group is online, agree and pin the online rules.',
        'After two meetings, ask each member one question: "What should we change?" Change one thing.',
    ],
    proof='Your group charter, logs of two meetings with quiz scores and topics, and the one change you agreed.',
    templates=[
        ('study group charter', """
STUDY GROUP CHARTER     Name: ______________   Exam: ______________
Members (3-5): ____________________________________________________
Meeting: every ______ at ______ (place or call link)
Roles (rotate weekly): quizmaster | explainer | fact-checker | timekeeper
Rules:
1. Every meeting follows the 60-minute format.
2. No forwards without a source; check before sharing.
3. Everyone makes their own cards and does their own recall.
4. We compare each person with their own past, not with each other.
Online: one question a day by rotation; group muted outside ______.
""", ''),
        ('meeting log', """
MEETING ___   Date: ______   Present: ___/___
Quizmaster: ______  Explainer: ______ (topic: __________)
Quiz scores: ____ ____ ____ ____ ____ (out of ___)
Common weak topic: ______________ -> next explainer: ______
Errors swapped: ___________________________________________
Next week's if-then goals recorded [ ]   One thing to change: ____________
""", ''),
    ],
    mistakes=[
        ('Meetings without an agenda.', 'Use the 60-minute format; chat after the meeting, not instead of it.'),
        ('One strong member teaching everything.', 'Rotate the explainer role; everyone explains a point back.'),
        ('Sharing unchecked forwards and PDFs.', 'Sources for everything; the fact-checker settles disputes.'),
        ('Comparing scores between members.', 'Compare each person with their own past.'),
        ('Sharing one AnkiDroid deck for everyone.', 'Share the work of finding facts; make your own cards.'),
    ],
    quiz=[
        {'q': 'Which part of the meeting format is retrieval practice for everyone?', 'o': ['The quiz, answered on paper with options covered', 'The check-in', 'The buffer', 'Chatting about news'], 'a': 'A', 'why': 'Answering from memory, then checking, is practice testing.'},
        {'q': 'What does the fact-checker do?', 'o': ['Checks disputed facts against the textbook or an official source', 'Writes everyone\'s notes', 'Keeps time', 'Chooses the exam'], 'a': 'A', 'why': 'It keeps wrong facts out of the group.'},
        {'q': 'What should each member do on their own, even in a group?', 'o': ['Make their own cards and do their own recall', 'Copy the strongest member\'s deck', 'Only listen', 'Skip the weekly review'], 'a': 'A', 'why': 'Processing and retrieval are where each person\'s learning happens.'},
        {'q': 'How should a group handle comparison?', 'o': ['Compare each person with their own past progress', 'Rank members every week', 'Hide all scores', 'Remove the weakest member'], 'a': 'A', 'why': 'Comparing with others adds stress; comparing with yourself shows progress.'},
    ],
    study='Fiorella on low-stakes settings, with the retrieval practice poster',
    action='Write a study group charter and run two meetings with the 60-minute format',
)

LESSONS = [L1, L2]

MODULE = module(
    M,
    overview="""
Learn by teaching and learn with others: teach a PSC topic to a family member or study partner without notes, and run a study group whose meetings are built on quizzing, teach-backs and error swaps instead of chat.

Explaining to someone else is one of the most effective ways to find out what you really know, especially without notes. And a well-run group adds what solo study lacks: accountability, other people\'s explanations, and other people\'s mistakes to learn from. This module gives both a structure.

The required teaching task of the course is in the first lesson; the second gives you a group format you can use until your exam and beyond.
""",
    outcomes=[
        'Explain when learning by teaching helps, and why explaining without notes matters',
        'Plan and teach a 10-minute lesson with questions and an explain-back',
        'Use a learner\'s feedback to find and fix your gaps',
        'Set up a study group with roles, rules and a 60-minute meeting format',
        'Keep online study groups useful and free of unchecked forwards',
    ],
    lessons=LESSONS,
    tools=[
        'The **10-minute lesson plan card** and **after the lesson** sheet',
        'The **study group charter** and **meeting log**',
    ],
    project='Teach and be taught',
    project_steps=[
        'Teach one more topic, to a different learner if you can, using the lesson card.',
        'Run a third group meeting (or partner call) in which you are the explainer.',
        'Compare your own scores on the topics you taught with similar topics you only studied, using your Revision tab or a short test.',
        'Write half a page: what teaching showed you about your own knowledge, and how you will keep teaching in your routine.',
    ],
    project_proof='Your second lesson card with feedback, the third meeting log with you as explainer, the score comparison and your half-page reflection.',
    rubric=[
        ('Teaching', 'Read notes aloud', 'Taught with some notes', 'Taught from memory with questions, an explain-back and feedback'),
        ('Gaps', 'None noted', 'Gaps noted but not fixed', 'Gaps noted, fixed from the source and retested'),
        ('Group', 'Unstructured chat', 'Some structure', 'Charter agreed and meetings run with the format and rotating roles'),
        ('Reflection', 'None', 'General comments', 'Scores compared and a plan to keep teaching'),
    ],
    short=[
        'Teach one 10-minute lesson to a family member and test both of you three days later.',
        'Find one accountability partner and have a 15-minute call each week: quiz each other on 10 questions.',
    ],
    flashcards=[
        ('When learning by teaching works best (Fiorella)', 'When you actually explain, without notes, in a low-stakes setting.'),
        ('Benefit of only preparing to teach', 'Modest and mixed.'),
        ('The 10-minute lesson', 'Opening question, 3-4 points from memory, one example, one drawing, two checks, an explain-back, feedback.'),
        ('Four rotating group roles', 'Quizmaster, explainer, fact-checker, timekeeper.'),
        ('The 60-minute meeting', 'Check-in, quiz, teach-back, error swap, plan, buffer.'),
        ('Online group rule for forwards', 'No forwards without a source; check before sharing.'),
    ],
    mistakes=[
        ('Teaching only when preparing feels complete.', 'Teach early; the gaps it shows are the point.'),
        ('Letting the group replace your own recall.', 'The group adds to your system; your daily retrieval stays yours.'),
    ],
)
