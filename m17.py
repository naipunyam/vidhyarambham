"""Module 17: Learning with AI."""
from common import lesson, module, link, rules, fence, table

M = 17

TUTOR_V2 = """
You are my Socratic tutor for the Kerala PSC exam. Topic: [topic]. I have
already studied it from [source]. My goal today: [goal].
Rules for you:
1. Do NOT start by explaining. First ask me 2-3 questions to find out what I
   already know and what I get wrong.
2. Teach one small idea at a time. After each, ask me to explain it back in my
   own words or answer a question about it.
3. When I am wrong, give a hint first. Give the answer only if I am still
   stuck after two hints.
4. Point out any misconception you notice, clearly.
5. At the end, give me 5 PSC-style questions one at a time and wait for my
   answer to each before telling me if it is right.
6. Then list what I should review. If you are unsure about any fact, say so
   and tell me which official source or textbook to check.
You may explain a hard idea in simple Malayalam if I ask, but ask me to answer
in English.
"""

QUIZ_PROMPT = """
Use ONLY the text below (my notes) to write 10 Kerala PSC-style multiple-choice
questions, with 4 options each. Include 3 statement-type questions ("Which of
the statements is/are correct?"). Do not show the answers yet. Ask me the
questions one at a time, wait for my answer, then tell me if I am right and
explain in two lines, quoting the sentence from my notes that supports the
answer. If a question can't be answered from my notes alone, don't ask it.
NOTES:
[paste your notes here]
"""

L1 = lesson(
    M, 1,
    outcome='Set up an AI chat tool as a Socratic tutor that questions you instead of answering for you, and run three tutoring sessions on PSC topics.',
    split='15 minutes reading, 20 minutes resources, 60 minutes for three sessions',
    core=f"""
### Two ways to use an AI tutor

AI chat tools such as ChatGPT, Gemini and Claude have free plans that can explain ideas, answer questions and quiz you. Used one way, they make you think: they ask questions, give hints and check your understanding. Used the other way, they think for you: they give you finished answers and notes, which feels efficient and teaches little. This module is about using them the first way.

If you want to understand how these tools work and why they sometimes make things up, the **Free AI Generalist Course** in this app covers it in Level 0, and prompting in Level 1.

### Built-in learning modes

Some tools now have modes designed for learning:

- **ChatGPT study mode** combines Socratic questioning, hints and self-reflection prompts with quizzes and knowledge checks. OpenAI says it is available to logged-in users on the Free plan; you turn it on from the tools menu by choosing "Study and learn" ({rules('oai-study', 'OpenAI, July 2025')}).
- **Gemini Guided Learning** breaks problems down step by step, asks probing questions and can add diagrams and quizzes ({rules('gemini-guided', 'Google, August 2025')}).

Features, names and free limits change often, so check what your app offers today. Any good chat tool can behave like a Socratic tutor if you ask it to, with a prompt like the one below.

### What a good tutoring session looks like

1. **You set the goal:** the topic, your source, what you want to be able to do.
2. **The tutor asks first:** two or three questions to find what you know and where you are wrong.
3. **One idea at a time:** after each, you explain it back or answer a question.
4. **Hints before answers:** you do the thinking; the tutor nudges.
5. **A quiz at the end,** answered one question at a time.
6. **You write the summary yourself:** what you learned, what to review, any fact to check.

This turns the AI into a partner for retrieval practice and self-explanation (Modules 3 and 8), the two things that build memory and understanding.

### Language

You can ask for a hard idea to be explained in simple Malayalam, then answer in English, which practises both. You can also ask the tutor to correct your English answers.

### Privacy

Don't paste personal details (Aadhaar, phone numbers, addresses, passwords) into AI chats. Your study notes and questions are fine.
""",
    example="""
**Sreeja** opened ChatGPT on her phone, chose "Study and learn" from the tools menu, and pasted the Socratic tutor prompt below with the topic "Panchayati Raj after the 73rd Amendment".

Instead of a long explanation, it asked her three questions. Her answer to the second showed a misconception: she thought the State Election Commission and the Election Commission of India were the same body. The tutor pointed it out, gave her a hint, and asked her to explain the difference back. Twenty minutes later she answered five PSC-style questions, one at a time, and got four right.

She wrote her own summary in her notebook: the misconception, the corrected idea, and two facts to check. Checking them in her textbook, one was right and one was slightly off in the tutor's wording, which she corrected on her card. She did two more sessions that week, on the Directive Principles and on time-and-work problems, and found the questions more useful than any explanation.
""",
    evidence=[
        ('AI tutoring that gives hints, not answers', 'limited', 'In a large school study, a hint-based GPT tutor did not harm exam results, unlike an answer-giving one (Bastani and others, reported by Wharton); benefits for adults are not yet proven.'),
        ('Retrieval and self-explanation inside tutoring', 'strong', 'The session design uses practice testing (high utility) and self-explanation (moderate).'),
        ('Built-in study modes in AI apps', 'limited', 'New features with little independent research yet; judge them by your own delayed test scores.'),
    ],
    resources=[
        ('oai-study', 'Read what ChatGPT study mode does and how to turn it on', '5 minutes'),
        ('gemini-guided', 'Read what Gemini Guided Learning does', '5 minutes'),
        ('wharton-ai', 'Read how a hint-based tutor differed from an answer-giving one', '10 minutes'),
    ],
    steps=[
        'Choose one AI chat tool with a free plan. If it has a study or guided-learning mode, turn it on; either way, paste the Socratic tutor prompt below.',
        'Run three sessions of 20 to 30 minutes on PSC topics you have already studied (one GK, one Constitution or history, one maths or English).',
        'In each session, answer every question yourself before asking for hints, and answer the final quiz one question at a time.',
        'After each session, write your own summary: misconceptions found, the corrected ideas, what to review.',
        'Check at least one fact from each session against your textbook or an official source, and correct your notes or cards if needed.',
    ],
    proof='Your three session summaries (written by you, not the AI) with the facts you checked and what you found.',
    templates=[
        ('Socratic tutor prompt (version 2)', TUTOR_V2, ''),
        ('tutoring session log', """
AI TUTOR SESSION     Date: ______  Tool: ______________  Topic: ______________
Questions it asked me first: ____________________________________________
Misconceptions it found: _______________________________________________
Corrected idea, in MY words: ___________________________________________
Quiz: ___/5 (answered one at a time)
Facts checked in: ______________  Right? Y / N   Fixed: __________________
To review / cards to make: ______________________________________________
""", ''),
    ],
    mistakes=[
        ('Asking for notes or answers instead of questions.', 'Ask the AI to question you; you do the explaining.'),
        ('Reading long AI explanations passively.', 'One idea at a time, then explain it back.'),
        ('Trusting every fact the AI states.', 'Check facts against your textbook or an official source (LRN-M17-L02).'),
        ('Pasting personal details into the chat.', 'Share study material only.'),
    ],
    quiz=[
        {'q': 'What should a good AI tutor do first in a session?', 'o': ['Ask you questions to find what you know and where you are wrong', 'Give a long explanation', 'Write your notes for you', 'Show all the answers'], 'a': 'A', 'why': 'Diagnosing first, then teaching one idea at a time, keeps you thinking.'},
        {'q': 'According to OpenAI, how do you turn on ChatGPT study mode?', 'o': ['From the tools menu, by choosing "Study and learn"', 'By paying for a special plan only', 'By typing "exam" three times', 'It can\'t be turned on'], 'a': 'A', 'why': 'OpenAI says it is open to logged-in Free users; features can change.'},
        {'q': 'Who should write the summary at the end of a tutoring session?', 'o': ['You, in your own words', 'The AI', 'Nobody', 'A friend'], 'a': 'A', 'why': 'Writing it yourself is retrieval and self-explanation.'},
        {'q': 'What did the school study find about a hint-based AI tutor?', 'o': ['It did not harm exam results, unlike an answer-giving version', 'It doubled exam scores', 'It harmed results more than the answer-giving version', 'It was not tested'], 'a': 'A', 'why': 'Students with answer-giving AI did worse in exams without AI; the hint-based tutor avoided that harm.'},
    ],
    study='The ChatGPT study mode and Gemini Guided Learning announcements, and the Wharton summary of the tutoring study',
    action='Run three Socratic AI tutoring sessions on PSC topics and write your own summaries with fact checks',
)

L2 = lesson(
    M, 2,
    outcome='Use AI to generate practice questions and explanations at the right level, and check every AI fact against your textbook or an official source before you learn it.',
    split='15 minutes reading, 15 minutes resources, 60 minutes action',
    core=f"""
### AI as a question machine

One of the best uses of AI for PSC study is turning your own notes into practice questions. Give it your notes, ask for PSC-style questions, and answer them one at a time. That is retrieval practice (Module 3) on exactly the material you studied.

Two settings make the questions much better:

1. **"Use only the text below."** Questions built from your own notes are tied to your source, so they are easier to check, and the AI is less likely to invent facts.
2. **"Don't show the answers yet."** Answer each question before you see whether you were right, ideally with the options covered first (Module 3).

### AI makes things up

AI chat tools can state false facts in a fluent, confident voice: a wrong year, a wrong article number, an invented scheme, a mixed-up name. This is widely documented, and the Free AI Generalist Course in this app explains why it happens (Level 0). It matters especially for PSC, where one wrong year costs a third of a mark.

### Five checking rules

1. **Check any fact before you learn it.** Before a fact becomes a card or a note, confirm it in your textbook or an official source. If it can't be confirmed, don't learn it.
2. **Prefer questions from your own notes.** "Use only the text below" keeps the AI close to a source you trust.
3. **Never rely on AI for current affairs.** Many tools have a knowledge cutoff and may not know recent events, or may get them wrong. Use PIB, PRD Kerala and All India Radio News (Module 10).
4. **When AI and your textbook disagree, the textbook or official source wins.** For PSC questions, the final answer key shows what PSC accepted ({rules('psc-keys', 'Kerala PSC answer keys')}).
5. **Ask for the supporting sentence.** Ask the AI to quote the line from your notes that supports each answer; if it can't, be suspicious.

### Explanations at the right level

When you don't understand something, ask for the explanation you need, not a lecture:

- "Explain this as if I were 12, with one example from Kerala life."
- "Explain the difference between X and Y in a two-column table."
- "Give me one worked example, then a similar problem for me to solve."
- "Explain it in simple Malayalam, in five lines."

Then close the chat and explain it back in your own words (Module 8). If you can't, the explanation didn't land; ask again differently.
""",
    example="""
**Ashiq** pasted his notes on the Fundamental Rights into an AI chat with the quiz prompt from this lesson. He answered the ten questions one at a time and got seven right.

Then he checked every question and explanation against his textbook. Eight were fine. Two had problems: one explanation said Article 21A was added to the Constitution in 1976, when his textbook says it came with the 86th Amendment in 2002; another question gave the right answer but a wrong year for the 44th Amendment, which removed the right to property in 1978. He reported both errors back to the AI and logged them.

Over three quizzes, he found 4 errors in 30 questions. "That is too many to trust," he wrote, "but few enough that checking is worth it." He made cards only from his three missed questions whose facts he had confirmed.
""",
    evidence=[
        ('Practice questions from your own notes (retrieval practice)', 'strong', 'Practice testing is rated high utility; AI is a new way to produce the questions.'),
        ('AI tools can state false facts confidently', 'moderate', 'Widely documented and explained in the AI Generalist course; no single source was checked for this course. Checking is essential.'),
        ('Asking AI for tailored explanations', 'limited', 'Little research yet on learning gains; useful when followed by explaining it back yourself.'),
    ],
    resources=[
        ('oai-study', 'Note the "knowledge checks" feature: quizzes with feedback', '5 minutes'),
        ('psc-keys', 'Remember that final answer keys show what PSC accepted', '5 minutes'),
        ('scert', 'Have your textbook ready as the checking source', 'As needed'),
    ],
    steps=[
        'Choose three sets of your own notes on PSC topics (for example from Module 9).',
        'For each, use the quiz prompt below to get 10 questions. Answer each before seeing whether you were right.',
        'Check every question, answer and explanation against your textbook or an official source, and log each AI error you find.',
        'Ask for one explanation at the right level on something you found hard, then close the chat and explain it back in your own words.',
        'Make cards only from missed questions whose facts you have confirmed.',
    ],
    proof='Your three quizzes with your answers, the fact-check log with the number of AI errors, your explain-back, and the confirmed cards.',
    templates=[
        ('quiz-from-my-notes prompt', QUIZ_PROMPT, ''),
        ('AI fact-check log', """
AI FACT CHECK      Date: ______  Tool: ______________  Topic: ______________
Q  | AI's fact or answer               | Checked in (book/page or official) | Correct?
1  | _________________________________ | __________________________________ | Y / N
2  | _________________________________ | __________________________________ | Y / N
...
AI errors found: ___ of ___   Errors reported back to the AI [ ]
Cards made only from confirmed facts [ ]
""", ''),
    ],
    mistakes=[
        ('Learning facts from AI without checking.', 'Confirm every fact in a textbook or official source before it becomes a card.'),
        ('Using AI for current affairs.', 'Use PIB, PRD Kerala and All India Radio News instead.'),
        ('Letting the AI show answers at once.', 'Answer first; that is where the learning happens.'),
        ('Vague prompts ("give me questions on history").', 'Paste your notes and say "use only the text below".'),
    ],
    quiz=[
        {'q': 'Why ask the AI to "use only the text below" when making a quiz?', 'o': ['Questions tied to your notes are easier to check and less likely to include invented facts', 'It makes the AI faster', 'It is required by PSC', 'It avoids all errors for certain'], 'a': 'A', 'why': 'It keeps the AI close to a source you trust; you still check.'},
        {'q': 'The AI says Article 21A was added in 1976; your textbook says 2002. Which do you trust?', 'o': ['The textbook (it came with the 86th Amendment, 2002)', 'The AI, because it sounds confident', 'Neither; skip the topic', 'Whichever you read first'], 'a': 'A', 'why': 'Textbooks and official sources win over AI.'},
        {'q': 'Where should you get current-affairs facts?', 'o': ['PIB, PRD Kerala and All India Radio News', 'An AI chat tool', 'Random forwards', 'Old guides'], 'a': 'A', 'why': 'AI tools may have a knowledge cutoff and can get recent events wrong.'},
        {'q': 'After an AI explains an idea, what should you do?', 'o': ['Close the chat and explain it back in your own words', 'Copy the explanation into your notes', 'Ask for a longer explanation', 'Move on immediately'], 'a': 'A', 'why': 'Explaining back shows whether you understood, and builds memory.'},
    ],
    study='The study-mode description of knowledge checks, with your textbook ready for checking',
    action='Generate three quizzes from your own notes, check every AI fact, and make cards only from confirmed facts',
)

L3 = lesson(
    M, 3,
    outcome='Use AI in ways that build your own skill instead of replacing it, test the difference on yourself, and write clear rules for when to use it and when not to.',
    split='15 minutes reading, 15 minutes resources, 60 minutes action over three days',
    core=f"""
### The crutch problem

In a large field study reported by Knowledge at Wharton, nearly 1,000 high-school maths students in Turkey practised with one of two AI tools. One, like an ordinary chatbot, gave answers ("GPT Base"). The other gave hints, with safeguards designed with teachers ("GPT Tutor"). During practice, both groups did better than students without AI: 48% better with GPT Base and 127% better with GPT Tutor. But in the exam, taken without AI, the GPT Base group scored **17% lower** than students who had never used AI, while the GPT Tutor group scored about the same as them ({link('wharton-ai', 'Knowledge at Wharton, 2024')}).

The lesson: AI that gives answers can make practice look better while making learning worse. It works like a crutch. The study was with school students in maths, so results for adults and other subjects may differ, but the warning fits everything you have learned in this course.

### Why it happens

- **Retrieval is where learning happens.** When the AI produces the answer, you skip the effortful recall that strengthens memory (Module 3).
- **The fluency illusion.** A smooth AI explanation feels like understanding, just like a reread page (Module 7).
- **No struggle, no feedback.** If you never try first, you never find out what you can't do.

### Seven rules for learning with AI

1. **Try first.** Attempt the problem or recall the topic yourself, for at least 10 minutes or one full attempt, before asking.
2. **Ask for hints, not answers.** "Give me a hint for the next step" instead of "solve this".
3. **Explain back.** After any explanation, close the chat and explain it in your own words.
4. **No AI during retrieval practice, mocks or tests.** These measure and build what is in your head.
5. **Check facts** before learning them (LRN-M17-L02).
6. **Use AI where it adds thinking:** questioning you, judging your explanation, giving a different example, helping you plan. Not where it removes thinking: writing your notes, solving your practice sets, writing your answers.
7. **Track it.** Once a week, compare your AI minutes with your own practice minutes in the weekly review.

### AI for work, later

After PSC, AI tools can make your work much more productive, and the Free AI Generalist Course teaches that. The difference is purpose: at work you want the output; while learning you want the skill in your head. Keep the effort yours when the goal is learning.
""",
    example="""
**Ashiq** noticed that his maths mock scores had dropped. For three weeks he had pasted every hard problem into an AI chat and read its neat solutions. It felt like progress.

He tried the experiment in this lesson. Set A: 10 time-and-distance problems, where he asked the AI for a full solution whenever he was stuck. Set B: 10 similar problems, where he tried each for at least five minutes and asked only for hints. Two days later he solved 10 new problems of the same types without any AI: 4 right from set A's types, 8 right from set B's.

He wrote his AI rules on a card: try first; hints, not answers; explain back; no AI in practice sets or mocks; facts checked; AI for questions and feedback. He kept a one-week AI log. His AI minutes fell from about 90 a week to 35, and his next maths mock score went back up.
""",
    evidence=[
        ('Answer-giving AI can harm learning while improving practice', 'moderate', 'One large field experiment (Bastani and others, reported by Wharton): exam scores 17% lower with answer-giving AI; school maths, so results may differ for adults.'),
        ('Trying first and recalling yourself (retrieval)', 'strong', 'The testing effect: effortful retrieval strengthens memory (Dunlosky and others, 2013).'),
        ('Explaining back after an AI explanation', 'limited', 'A practical safeguard based on self-explanation and retrieval; not directly tested with AI.'),
    ],
    resources=[
        ('wharton-ai', 'Read the whole article on the study and its numbers', '10 minutes'),
        ('oai-study', 'Compare: how study mode is designed to avoid giving answers straight away', '5 minutes'),
    ],
    steps=[
        'Write your AI rules for learning (start from the seven in this lesson and adapt them) on a card.',
        'Run the experiment: set A of 10 problems or questions where you may ask AI for full answers; set B of 10 similar ones where you try first and ask only for hints. Note the time each set takes.',
        'Two days later, without any AI, answer 10 new questions of the same types. Score which types you got right.',
        'Keep a one-week AI log: what you used AI for, for how long, and whether you tried first.',
        'In your weekly review, compare your AI minutes with your own practice minutes, and adjust your rules if needed.',
    ],
    proof='Your AI rules card, the experiment with both sets and the two-day scores, and your one-week AI log.',
    templates=[
        ('my AI rules for learning', """
MY AI RULES (learning)                         Date: ______
1. Try first: at least ___ minutes or one full attempt before asking.
2. Hints, not answers.
3. Explain back in my own words after every explanation.
4. No AI in retrieval practice, practice sets, mocks or tests.
5. Every fact checked before it becomes a card or note.
6. AI for: questioning me, judging my explanation, other examples, planning.
   Not for: writing my notes, solving my practice, writing my answers.
7. Weekly: AI minutes ___ vs own practice minutes ___
""", ''),
        ('AI use log', """
AI USE LOG     Week of ______
Day | What I used AI for              | Minutes | Tried first? | Hints or answers? | Rule kept?
Mon | ______________________________  | ___     | Y / N        | H / A             | Y / N
Tue | ______________________________  | ___     | Y / N        | H / A             | Y / N
...
Total AI minutes ___   Own practice minutes ___
""", ''),
    ],
    mistakes=[
        ('Opening AI before trying yourself.', 'Try first; the struggle is part of learning.'),
        ('Copying AI-written notes.', 'Write notes in your own words (Module 9); use AI to question you on them.'),
        ('Using AI during practice sets or mocks.', 'Those measure and build what is in your head. Keep them AI-free.'),
        ('Outsourcing your English writing practice.', 'Write it yourself, then ask the AI for feedback.'),
    ],
    quiz=[
        {'q': 'In the study reported by Wharton, how did the answer-giving AI group do in the exam without AI?', 'o': ['About 17% lower than students who never used AI', 'About 48% higher', 'Exactly the same', '127% higher'], 'a': 'A', 'why': 'Practice looked better, but learning was worse: a crutch.'},
        {'q': 'What happened with the hint-based "GPT Tutor"?', 'o': ['Exam scores were about the same as students without AI', 'Exam scores fell by half', 'Students stopped practising', 'It was not tested'], 'a': 'A', 'why': 'Hints and safeguards avoided the harm.'},
        {'q': 'Why does answer-giving AI weaken learning?', 'o': ['It skips the effortful retrieval and struggle that build memory and skill', 'It is too slow', 'It uses too much data', 'It is in English'], 'a': 'A', 'why': 'Learning comes from your own effortful recall and practice.'},
        {'q': 'Which is a good use of AI while learning?', 'o': ['Asking it to question you and judge your explanation', 'Asking it to solve your whole practice set', 'Using it during a mock test', 'Copying its notes into your notebook'], 'a': 'A', 'why': 'It adds thinking instead of removing it.'},
    ],
    study='The Knowledge at Wharton article on the AI tutoring study',
    action='Write your AI rules, run the hints-versus-answers experiment on yourself and keep a one-week AI log',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    M,
    overview="""
Use AI tools to learn more, not less: as a Socratic tutor that questions you, as a question machine built on your own notes, and as a source of explanations you always check. Write clear rules so AI never does the thinking that builds your memory and skill.

Free AI chat tools can be excellent study partners or very effective crutches. Research is still young, but one large study already shows the difference: an AI that gave answers improved practice and harmed exam results, while a hint-based tutor did not cause that harm. This module turns that warning into a practical setup, consistent with everything else in the course: retrieval, explanation and checking.

For using AI as a work skill, the Free AI Generalist Course in this app goes much further. Here the goal is learning.
""",
    outcomes=[
        'Set up an AI tool as a Socratic tutor and run good tutoring sessions',
        'Generate practice questions from your own notes and answer before seeing answers',
        'Check every AI fact against a textbook or official source',
        'Explain why answer-giving AI can harm learning',
        'Write and follow your own rules for learning with AI',
    ],
    lessons=LESSONS,
    tools=[
        'The **Socratic tutor prompt** and **tutoring session log**',
        'The **quiz-from-my-notes prompt** and **AI fact-check log**',
        'Your **AI rules for learning** and **AI use log**',
    ],
    project='My AI study setup',
    project_steps=[
        'Save your tutor prompt, quiz prompt, fact-check log template and AI rules together in one note on your phone.',
        'Run one more tutoring session and one more quiz from your notes, following your rules.',
        'Count the AI errors you found across all your quizzes and sessions, and write your rule for which facts you will never take from AI unchecked.',
        'In your weekly review, record your AI minutes against your own practice minutes for two weeks.',
    ],
    project_proof='Your saved AI setup note, the new session and quiz logs, your total AI error count with your checking rule, and two weeks of AI minutes in your weekly reviews.',
    rubric=[
        ('Tutoring', 'AI used to get answers', 'Some questioning sessions', 'Socratic sessions with my own summaries'),
        ('Questions', 'AI quizzes with answers shown at once', 'Answered first sometimes', 'Quizzes from my notes, answered one at a time'),
        ('Checking', 'AI facts learned unchecked', 'Some facts checked', 'Every fact checked, errors logged and reported'),
        ('Reliance', 'AI first for everything', 'Some rules', 'Written rules followed and AI minutes tracked weekly'),
    ],
    short=[
        'Use AI only for quizzes from your own notes, answered before seeing answers, with every fact checked.',
        'Never use AI during practice sets or mocks.',
    ],
    flashcards=[
        ('Good AI tutor behaviour', 'Asks first, one idea at a time, hints before answers, quiz at the end.'),
        ('ChatGPT study mode, per OpenAI', 'Socratic questions, hints and knowledge checks; tools menu, "Study and learn".'),
        ('The quiz prompt\'s two key settings', '"Use only the text below" and "don\'t show the answers yet".'),
        ('When AI and the textbook disagree', 'The textbook or official source wins; for PSC questions, the final answer key.'),
        ('The Wharton study in one line', 'Answer-giving AI: practice up, exam score 17% lower; hint-based tutor: no harm.'),
        ('Try-first rule', 'Attempt it yourself before asking AI.'),
        ('Where AI should never be used while learning', 'Retrieval practice, practice sets, mocks and tests.'),
    ],
    mistakes=[
        ('Treating AI as an answer key.', 'Treat it as a questioner whose facts you check.'),
        ('Judging AI help by how smooth practice feels.', 'Judge it by your scores days later without AI.'),
    ],
)
