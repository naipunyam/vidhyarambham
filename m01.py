"""Module 1: How your brain learns."""
from common import lesson, module, link, fence, table, bullets
import tools

M = 1

L1 = lesson(
    M, 1,
    outcome='Explain why attention and working memory limit how fast you learn, and cut the load of one hard PSC page so it becomes learnable.',
    split='20 minutes reading, 20 minutes resources, 35 minutes action',
    core=f"""
Everything you learn for PSC takes the same path through your mind:

1. **Attention** picks what you work on. Whatever you don't attend to, you don't learn. A phone that buzzes every few minutes keeps pulling attention away.
2. **Working memory** holds what you are thinking about right now, while you make sense of it. It is like a small desk: only a few things fit at once.
3. **Long-term memory** is the huge store of what you know. Learning means getting knowledge from the desk into this store, organised so you can find it again.

This is the classic three-store model of memory, explained in {link('os-psych-8-1', 'OpenStax Psychology 2e, section 8.1')}.

### The desk is small

Working memory is tiny and short-lived. Without rehearsal, information in short-term memory fades in about 15 to 30 seconds. The old estimate was that it holds about seven items, give or take two; newer research puts the limit nearer four "chunks" (OpenStax 8.1; {link('cese-clt', 'NSW CESE review of cognitive load theory')}).

That is why a dense page in a PSC guide can feel impossible. Eight new names, five dates and three article numbers arrive together, and the desk overflows. You read the page, turn it, and almost nothing remains.

### Long-term memory changes the size of the desk

Long-term memory has no practical limit, and it stores knowledge in organised patterns called **schemas**. When you already know something well, it takes up almost no space on the desk. If you know multiplication tables by heart, a percentage problem uses your working memory for the reasoning, not for "7 × 8". If you already know the structure of the Constitution (Parts, Articles, Schedules), a new fact about Article 21A has somewhere to go.

So the more you know, the easier new learning becomes. Beginners need smaller steps; experts can take bigger ones.

### Cognitive load: what fills the desk

**Cognitive load** is how much a task demands from working memory. Two kinds matter for you:

- **Load from the material itself.** Centre-State relations, compound interest or Malayalam sandhi rules are hard because many ideas interact. You can't remove this load, but you can split it into smaller pieces.
- **Load from how you study.** A phone on the table, a guide that puts the answers on another page, notes in three different notebooks, unknown English words, noise from the TV. This load adds nothing to learning. Remove as much of it as you can.

### What this means for your study

- **One thing at a time.** Study one chunk, check you have it, then move on.
- **Split hard pages** into 3 to 5 chunks of one idea each.
- **Worked examples first, for beginners.** In maths and reasoning, study a fully solved example step by step before solving alone. Beginners who study worked examples do better on later tests than those who struggle with problems unaided (the "worked example effect" in the CESE review). As you improve, switch to solving on your own: the same review describes this "expertise reversal".
- **Build background knowledge.** Basic facts in long-term memory (tables, key dates, the structure of the Constitution) make everything else easier. That is why Module 4 puts them into AnkiDroid.
- **Don't buy "brain training".** Apps that promise to enlarge working memory make you better at the app's own games, but a large review of 87 publications found no convincing gains in reading, arithmetic or intelligence ({link('wm-training', 'Melby-Lervåg, Redick and Hulme, 2016')}).
""",
    example="""
**Sreeja** studies in Nadapuram in two 45-minute slots, one while her children are at school and one after they sleep. Her guide's page on Centre-State relations has three lists, a dozen article numbers and two tables. She read it four times in a week and still mixed up the lists.

She did a load audit of her last session. From the setup: the phone was face-up on the table (seven WhatsApp notifications), the TV was on in the next room, and she kept flipping to the end of the guide for the meaning of "concurrent". From the material: three lists with similar names.

She changed the setup first: the phone went into the bedroom, she wrote the five unknown words on a slip of paper beside the book, and she used the morning slot, when the house is quiet. Then she split the page into four chunks: legislative relations, administrative relations, financial relations, and the three lists. For each chunk she read, closed the book, wrote two lines from memory and checked.

The page that had taken four readings took one 40-minute session. She rated its difficulty 8 out of 10 before and 5 after. The material hadn't changed; the load had.
""",
    evidence=[
        ('Working memory is small (a few chunks) and brief', 'strong', 'A core finding of memory research, summarised in OpenStax Psychology 2e and the CESE review.'),
        ('Worked examples help beginners; problem solving helps once you are skilled', 'strong', 'The worked example and expertise reversal effects, described in the CESE review of cognitive load theory.'),
        ('Removing distractions and split sources lowers load', 'moderate', 'Consistent with cognitive load research; your own load audit is the best test of what distracts you.'),
        ('Working memory training apps make you smarter', 'none', 'Melby-Lervåg and others (2016): short-term, narrow gains with no convincing transfer to reading, arithmetic or intelligence.'),
    ],
    resources=[
        ('os-psych-8-1', 'Read the parts on the three memory stores (sensory, short-term, long-term) and short-term memory', '20 minutes'),
        ('cese-clt', 'Read the sections on working memory, long-term memory and the worked example effect', '25 minutes'),
        ('wm-training', 'Read the abstract only: what working memory training can and cannot do', '5 minutes'),
    ],
    steps=[
        'Pick the hardest page or section in the PSC subject you are studying this week: a dense GK page, a Constitution topic or a maths chapter.',
        'Do a load audit of the last time you studied it, with the template below. Mark each item as "material" or "setup".',
        'Remove at least two setup loads before your next session: for example, phone in another room, unknown words on a slip beside the book, answers on the same page as the questions.',
        'Split the page into 3 to 5 chunks of one idea each. For each chunk: read it, close the book, write one or two lines from memory, then check and correct in a different colour.',
        'If it is a maths or reasoning topic: study one worked example step by step, cover it, solve the same problem yourself, then solve one similar problem.',
        'Rate the difficulty of the page from 1 to 10 before and after, and add a row to your Study Log.',
    ],
    proof='A photo of your load audit and the chunked page with your one-line recalls, and the Study Log row.',
    templates=[
        ('cognitive load audit', """
COGNITIVE LOAD AUDIT      Page / topic: ______________   Date: ______
Difficulty before (1-10): ___

What competed for my working memory?          Material or setup?   Fix
1. ____________________________________       ________             ______________
2. ____________________________________       ________             ______________
3. ____________________________________       ________             ______________
4. ____________________________________       ________             ______________

Chunks (one idea each):
1. ______________  my 2-line recall: ________________________  checked [ ]
2. ______________  my 2-line recall: ________________________  checked [ ]
3. ______________  my 2-line recall: ________________________  checked [ ]
4. ______________  my 2-line recall: ________________________  checked [ ]

Difficulty after (1-10): ___   Time taken: ___ minutes
""", ''),
        ('Study Log headings (if you have not made the tab yet)', tools.STUDY_LOG, 'csv'),
    ],
    mistakes=[
        ('Studying with the phone face-up.', 'Every notification takes a piece of your small desk. Put it in another room during study blocks; Module 5 goes further.'),
        ('Trying to swallow a whole chapter in one go.', 'Split it into chunks of one idea and check each one from memory before moving on.'),
        ('Attacking hard maths problems with no worked example.', 'Study a fully solved example first, then solve. Switch to solving alone once the steps feel easy.'),
        ('Rereading a page that overloads you.', 'Rereading adds the same overload again. Reduce the load first, then recall.'),
        ('Paying for "brain training" apps.', 'They train the app, not your exam skills. Spend the time on your syllabus.'),
    ],
    quiz=[
        {'q': 'According to newer research, about how many chunks can working memory hold at once?', 'o': ['About four', 'About forty', 'An unlimited number', 'Exactly one'], 'a': 'A', 'why': 'Newer estimates put the limit near four chunks; the older estimate was about seven, give or take two.'},
        {'q': 'Which of these is load from how you study, which you can remove?', 'o': ['Flipping between the questions and an answer key at the back of the book', 'The number of ideas in Centre-State relations', 'The fact that compound interest has several steps', 'The length of the syllabus'], 'a': 'A', 'why': 'Split sources add load without adding learning. Put questions and answers together.'},
        {'q': 'You are new to percentages. What should you do first?', 'o': ['Study a worked example step by step, then solve a similar problem', 'Attempt 50 hard problems with no help', 'Read the theory three times', 'Watch a speed-maths video'], 'a': 'A', 'why': 'The worked example effect: beginners learn more from studying solved examples first.'},
        {'q': 'What did a large review find about working memory training apps?', 'o': ['Gains on trained tasks, but no convincing transfer to reading, arithmetic or intelligence', 'They raise IQ by 10 points', 'They work only for children', 'They double reading speed'], 'a': 'A', 'why': 'Melby-Lervåg and others (2016) reviewed 87 publications and found narrow, short-term effects.'},
    ],
    study='OpenStax 8.1 on the memory stores and the CESE review sections on working memory and worked examples',
    action='Audit and chunk one hard PSC page, and log the session',
)

L2 = lesson(
    M, 2,
    outcome='Explain how memories are made and stabilised, encode PSC facts through meaning instead of repetition, and protect the sleep that consolidates them.',
    split='20 minutes reading, 25 minutes resources, 30 minutes action plus a 7-night sleep log',
    core=f"""
### Encoding: getting it in

**Encoding** is turning what you read or hear into a memory. Not all encoding is equal. Repeating "Article 21, life and liberty, Article 21, life and liberty" keeps it on the desk for a while; psychologists call that **maintenance rehearsal**. Connecting it to meaning lasts much longer: **elaborative rehearsal** ({link('os-psych-8-1', 'OpenStax Psychology 2e, 8.1')}).

Compare two ways to learn that Article 21 protects life and personal liberty:

- **Repetition:** say "21: life and personal liberty" ten times.
- **Meaning:** ask "why is this right so important?" It protects you from losing your life or freedom except by procedure established by law, and courts have read many other rights into it, such as the right to live with dignity. Link it to something you know: a news story about an illegal detention. Picture a 21-year-old walking free out of a prison gate.

The second way takes a minute longer and is remembered far better, because it gives the fact many hooks in long-term memory. Everything in Module 3 (elaboration, concrete examples, dual coding) is a way to encode through meaning.

### Consolidation: making it stick

A new memory is fragile. Over the following hours, and especially during sleep, the brain stabilises it; this is **consolidation**. Sleep researchers have linked parts of sleep, including the sleep spindles of stage 2 and REM sleep, to learning and memory ({link('os-psych-4-3', 'OpenStax Psychology 2e, 4.3')}). In a careful repeat of Ebbinghaus's forgetting experiment, Murre and Dros (2015) even saw memory scores jump upward at the 24-hour point, which they suggest may be an effect of sleep, though it is not proven ({link('murre', 'PLOS ONE')}).

The practical message is simple:

- **Adults need 7 hours of sleep or more a night, regularly.** Less is linked with impaired performance and more errors ({link('aasm', 'AASM and Sleep Research Society consensus')}).
- **An all-nighter before an exam trades memory for time.** You gain hours of reading and lose the consolidation of what you read.
- **Sleep after learning is part of learning.** A short recall of the day's topic before bed is a sensible habit, though the research on the best timing is limited.

### Neuroplasticity: you can still change your brain

**Neuroplasticity** is the brain's ability to change with learning and experience. It is greatest in early childhood, but substantial change continues in adults ({link('os-psych-3-4', 'OpenStax Psychology 2e, 3.4')}). In one study, adults with ordinary memories trained the memory palace for six weeks; their memory improved and their brain networks changed towards those of memory champions ({link('dresler', 'Dresler and others, 2017')}).

At 30, 40 or 60 you can learn a subject, a language or a skill from zero. What changes with age is mostly how much time and practice you can give it, not whether learning is possible.
""",
    example="""
**Ashiq**, 22, used to study until 2 a.m. with YouTube running in another tab, then slept until 9. He believed night study suited him.

He tried a small experiment on the Fundamental Rights. He learned five articles by repeating them, and five by meaning: for each he wrote one line on why it matters and linked it to something he knew (Article 17, the abolition of untouchability, to the temple-entry movements he had studied in Kerala history). The next morning he recalled 2 of the repeated five and 5 of the meaningful five.

Then he kept a sleep log for a week. He averaged under 6 hours, with a different bedtime every night. He moved his last study block to 9 p.m., did a 5-minute recall of the day's topic at 10:45, and put the phone on the charger in the kitchen at 11. After two weeks his average was 7 hours 20 minutes, and his morning recall scores were steadier. One week is not a scientific study, but it was enough to convince him.
""",
    evidence=[
        ('Encoding through meaning beats repetition', 'strong', 'Elaborative rehearsal and meaning-based encoding are well established (OpenStax 8.1); Dunlosky rates elaborative interrogation and self-explanation as promising study methods.'),
        ('Enough sleep protects learning and performance', 'strong', 'AASM and SRS consensus: adults need 7 or more hours; less is linked with impaired performance and errors.'),
        ('Sleep stages help consolidate memories', 'moderate', 'Spindles and REM sleep are linked to learning and memory (OpenStax 4.3); exactly how is still being researched.'),
        ('Reviewing just before sleep is the best timing', 'limited', 'Plausible and harmless, but the research on precise timing is limited. Judge it by your own morning recall.'),
        ('Adult brains change with training', 'strong', 'OpenStax 3.4 on neuroplasticity; Dresler and others (2017) on adults who trained the method of loci.'),
    ],
    resources=[
        ('os-psych-8-1', 'Read the part on encoding, including semantic encoding and maintenance versus elaborative rehearsal', '20 minutes'),
        ('os-psych-4-3', 'Read the stages of sleep, noting what each stage is linked to', '15 minutes'),
        ('aasm', 'Read the one-page recommendation for adults', '5 minutes'),
        ('os-psych-3-4', 'Read the paragraph on neuroplasticity', '5 minutes'),
    ],
    steps=[
        'Choose 10 new facts from your current PSC topic: for example 10 Fundamental Rights articles, 10 Kerala river facts or 10 Jnanpith winners with years.',
        'Learn 5 of them by repetition only: read and repeat each one for one minute.',
        'Learn the other 5 by meaning: for each, write one line on why it matters, link it to something you already know, or draw a tiny picture. Spend about one minute on each.',
        'Next morning, after sleep and before looking at anything, write all 10 from memory. Score each group out of 5.',
        'Keep a 7-night sleep log: time in bed, time up, hours slept, and how rested you feel (1 to 5).',
        'Write one change for next week based on your log, such as a fixed bedtime, the phone charging outside the bedroom, or a 5-minute recall before bed.',
    ],
    proof='Your 10-fact experiment with both scores, and the 7-night sleep log with your one change.',
    templates=[
        ('encoding experiment', """
ENCODING EXPERIMENT     Topic: ______________   Date learned: ______

REPETITION ONLY (1 minute each)        MEANING (1 minute each: why / link / picture)
1. ____________________________        6. ____________________________
2. ____________________________           why or link: _________________
3. ____________________________        7. ____________________________
4. ____________________________           why or link: _________________
5. ____________________________        8. ____________________________
                                       9. ____________________________
                                       10. ___________________________

Next-morning recall (no looking):  repetition ___/5    meaning ___/5
What I conclude: ____________________________________________________
""", ''),
        ('7-night sleep log', """
Night | In bed | Up    | Hours | Rested (1-5) | Screen in last hour? | Note
1     | ______ | _____ | _____ | ____         | yes / no             | ____
2     | ______ | _____ | _____ | ____         | yes / no             | ____
3     | ______ | _____ | _____ | ____         | yes / no             | ____
4     | ______ | _____ | _____ | ____         | yes / no             | ____
5     | ______ | _____ | _____ | ____         | yes / no             | ____
6     | ______ | _____ | _____ | ____         | yes / no             | ____
7     | ______ | _____ | _____ | ____         | yes / no             | ____
Average hours: ____   My one change for next week: ________________________
""", ''),
    ],
    mistakes=[
        ('Learning facts by chanting them.', 'Repetition alone fades fast. Spend the same minute asking why, linking or picturing.'),
        ('All-nighters before an exam.', 'You lose the sleep that consolidates what you studied. Stop new topics the evening before and sleep.'),
        ('Believing you are too old to learn.', 'Adult brains keep changing with practice. Time and method matter more than age.'),
        ('Treating sleep as wasted study time.', 'Sleep is when memories settle. Seven hours or more is part of the plan, not a break from it.'),
    ],
    quiz=[
        {'q': 'Which way of learning "Article 17: abolition of untouchability" creates the strongest memory?', 'o': ['Linking it to the temple-entry movements and asking why it was needed', 'Repeating it twenty times', 'Copying it five times', 'Highlighting it in yellow'], 'a': 'A', 'why': 'Meaning-based (elaborative) encoding gives the fact many hooks in long-term memory.'},
        {'q': 'How much sleep does the AASM and Sleep Research Society consensus recommend for adults?', 'o': ['7 hours or more a night, regularly', '5 hours if you study hard', '4 hours plus naps', '10 hours or more'], 'a': 'A', 'why': 'Less than 7 hours regularly is linked with impaired performance and more errors.'},
        {'q': 'What is consolidation?', 'o': ['The brain stabilising new memories over hours and during sleep', 'Reading a chapter twice', 'Writing a summary', 'Joining a study group'], 'a': 'A', 'why': 'New memories are fragile at first and are stabilised over time, with sleep playing a part.'},
        {'q': 'What did Dresler and others (2017) show about adults?', 'o': ['Six weeks of memory-palace training improved memory and changed brain networks', 'Adults cannot improve their memory', 'Only memory champions can use the memory palace', 'Brain training apps raise intelligence'], 'a': 'A', 'why': 'It is good evidence of adult neuroplasticity; you build your own memory palace in Module 11.'},
    ],
    study='OpenStax 8.1 on encoding, 4.3 on sleep stages and the AASM sleep recommendation',
    action='Run the 10-fact encoding experiment and keep a 7-night sleep log',
)

L3 = lesson(
    M, 3,
    outcome='Explain the forgetting curve and the testing effect, and prove to yourself with your own PSC facts that recalling beats rereading.',
    split='15 minutes reading, 30 minutes resources, 30 minutes action over three days',
    core=f"""
### The forgetting curve

In the 1880s Hermann Ebbinghaus learned lists of nonsense syllables and tested himself after different delays. He found that forgetting is fast at first and then slows down: much of what you learn today is gone within a day or two unless you do something about it. In 2015, Murre and Dros repeated his experiment carefully and got a very similar curve ({link('murre', 'PLOS ONE, open access')}).

You have felt this curve. You read a chapter on the Kerala renaissance on Monday, understood it, and on Saturday you can name only two reformers. Nothing was wrong with your brain: that is how memory works.

### Retrieval changes the curve

**Retrieval** means pulling information out of memory: answering a question, writing what you remember on a blank page, explaining it aloud. Every time you retrieve something successfully, the memory becomes stronger and is forgotten more slowly next time.

The classic demonstration is by Roediger and Karpicke (2006). Students read short prose passages. Some reread them several times; others read once and then recalled them on blank paper several times. After 5 minutes, rereading did slightly better. After a week, the picture reversed: in one experiment, students who had studied once and recalled three times remembered 61% of the ideas, while those who had studied four times remembered 40% ({link('roediger', 'Roediger and Karpicke, PDF')}).

The same study found something important about feelings: the rereaders were **more confident** they had learned the material, although they remembered least. Rereading feels like learning because the page looks familiar. Recall feels harder, and that effort is exactly what makes it work.

### Desirable difficulty, with feedback

Effortful recall that mostly succeeds is ideal. Some struggle is good; complete failure is not. So:

- **Recall first, then check.** After recalling, open the book and fix what you missed or got wrong, preferably in a different colour so you can see your gaps.
- **Don't wait too long for the first review.** A first recall the same day or the next day catches facts before they fall off the curve.
- **Space the next reviews out:** 1 day, 3 days, 7 days and so on. Each review flattens the curve a little more. Module 3 turns this into a revision schedule, and Module 4 lets AnkiDroid do it for single facts.

### Forgetting is useful

Forgetting tells you what to review. A fact you recall easily needs less attention; a fact you keep forgetting needs a better hook (Module 3), a flashcard (Module 4) or a mnemonic (Module 11). Your weekly review (from this week) is where you look at what you forgot and decide what to do.
""",
    example="""
**Anu** used to prepare a chapter by reading it twice in the evening with a highlighter, and she felt she knew it. A week later, in a practice test, she could not remember who founded the Sree Narayana Dharma Paripalana Yogam or when the Vaikom Satyagraha began, although she had highlighted both.

She ran the experiment in this lesson on the Kerala renaissance. She took 20 facts and split them into two sets of 10. Set A she read three times on Monday. Set B she read once, then wrote everything she could remember on a blank page, checked it, and did the same again 20 minutes later and once more on Tuesday.

On Thursday she tested both sets without looking. Set A: 4 out of 10. Set B: 8 out of 10. The extra time for set B was about ten minutes. She now ends every reading session by closing the book and writing for five minutes, and she says it feels harder, which is the point.
""",
    evidence=[
        ('Retrieval practice (the testing effect)', 'strong', 'Rated high utility by Dunlosky and others (2013); shown in labs and classrooms, including Roediger and Karpicke (2006).'),
        ('The forgetting curve: fast loss, then slower', 'strong', 'Ebbinghaus\'s result was replicated by Murre and Dros (2015).'),
        ('Spaced reviews slow forgetting', 'strong', 'Distributed practice is rated high utility by Dunlosky and others (2013).'),
        ('Rereading feels effective', 'strong', 'It feels effective but isn\'t: rereaders were more confident and remembered less after a week (Roediger and Karpicke).'),
    ],
    resources=[
        ('ncase', 'Read the whole comic: the forgetting curve, the Leitner box and why spacing works', '25 minutes'),
        ('roediger', 'Read the abstract and look at the results of Experiment 2 (repeated study versus repeated testing)', '15 minutes'),
        ('murre', 'Read the abstract and look at the forgetting curve figure', '10 minutes'),
        ('ls-retrieval', 'Download the retrieval practice poster and keep it on your phone', '5 minutes'),
    ],
    steps=[
        'Take 20 new facts from your current PSC topic (a chapter you haven\'t studied yet). Split them into set A and set B, 10 each, of similar difficulty.',
        'Day 1, set A: read the 10 facts three times, carefully. No recall, no writing.',
        'Day 1, set B: read the 10 facts once. Close the book and write everything you remember on a blank page. Check and correct in another colour. Twenty minutes later, recall them again on a fresh page and check.',
        'Day 2: recall set B once more on a blank page and check. Don\'t look at set A.',
        'Day 3 or 4: test both sets without looking, on a fresh page. Score each out of 10.',
        'Write three lines: your two scores, how confident you felt about each set on day 1, and the study rule you will follow from now on.',
    ],
    proof='Your recall pages for set B, the final test page with both scores, and your three lines.',
    templates=[
        ('recall versus reread experiment', """
RECALL vs REREAD      Topic: ______________   Start date: ______

SET A (reread 3 times on day 1)        SET B (read once, recall twice on day 1, once on day 2)
1. ________________________            1. ________________________
2. ________________________            2. ________________________
...                                     ...
10. _______________________            10. _______________________

Day 1 confidence (1-5): set A ___  set B ___
Final test on day ___ (no looking):  set A ___/10   set B ___/10
My rule from now on: _________________________________________________
""", ''),
        ('blank-page recall routine (use after every reading session)', """
1. Close the book and turn the phone over. Timer: 5 minutes.
2. Write everything you remember: names, dates, causes, a diagram. No peeking.
3. Open the book. In a different colour, add what you missed and fix errors.
4. Circle the gaps. They are tomorrow's first recall.
5. Log it: Study Log -> Method = "retrieval", and what you recalled.
""", ''),
    ],
    mistakes=[
        ('Rereading until the page feels familiar.', 'Familiar is not the same as remembered. Close the book and recall instead.'),
        ('Recalling without checking.', 'Always check after recall, so errors are corrected instead of strengthened.'),
        ('Waiting a week for the first review.', 'By then most of it is gone. Do the first recall the same day or the next day.'),
        ('Judging methods by how they feel.', 'Effortful recall feels worse and works better. Judge by your test scores days later.'),
    ],
    quiz=[
        {'q': 'In Roediger and Karpicke\'s experiment, which group remembered more after a week?', 'o': ['Students who read once and recalled three times', 'Students who read four times', 'Both groups remembered the same', 'Students who highlighted the passage'], 'a': 'A', 'why': 'In Experiment 2, repeated testing gave 61% after a week and repeated studying 40%.'},
        {'q': 'What is the shape of the forgetting curve?', 'o': ['Fast forgetting at first, then slower', 'Slow at first, then fast', 'A straight line down', 'No forgetting for a week, then sudden loss'], 'a': 'A', 'why': 'Ebbinghaus found it, and Murre and Dros (2015) replicated it.'},
        {'q': 'Why do many students prefer rereading?', 'o': ['The page feels familiar, so they feel they have learned it', 'It produces better results after a week', 'It is recommended by research', 'It uses more effort'], 'a': 'A', 'why': 'Familiarity creates confidence without lasting memory.'},
        {'q': 'What should you do right after a blank-page recall?', 'o': ['Check against the book and fix gaps in another colour', 'Move straight to a new chapter', 'Recall again immediately without checking', 'Throw the page away'], 'a': 'A', 'why': 'Feedback corrects errors so you don\'t strengthen wrong answers.'},
    ],
    study='Nicky Case\'s comic and the key results of Roediger and Karpicke (2006)',
    action='Run the recall-versus-reread experiment on 20 PSC facts and write your rule',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    M,
    overview="""
Learn how attention, working memory, encoding, sleep, retrieval and forgetting work, and test each idea on your own PSC facts. Three small experiments in your first week show you why the rest of the course works.

You don't need biology to learn well, but a simple model of your mind explains almost every method in this course. Working memory is small, so you chunk and remove distractions. Meaning makes memories last, so you ask why. Sleep consolidates memories, so you protect it. Retrieval strengthens memory and forgetting is fast, so you recall instead of rereading and you review on a schedule.

Each lesson ends with an experiment on your real PSC material. By Sunday you will have your own evidence, not just someone else's.
""",
    outcomes=[
        'Explain attention, working memory, long-term memory and cognitive load, and reduce the load of a hard page',
        'Explain encoding, consolidation and neuroplasticity, and encode facts through meaning',
        'Explain the forgetting curve and the testing effect',
        'Show with your own data that recall beats rereading',
        'Draw a one-page model of how you learn, with three personal rules',
    ],
    lessons=LESSONS,
    tools=[
        'The **Study Log** tab, now with a "Method" column you fill in every session',
        'The **cognitive load audit** for hard pages',
        'The **blank-page recall routine** you will use after every reading session',
        'The **7-night sleep log**',
    ],
    project='My one-page learning model',
    project_steps=[
        'On one page, draw the path from attention to working memory to long-term memory. Add encoding, consolidation (sleep), retrieval and forgetting, with arrows. Use your own words and small pictures.',
        'Next to it, write the results of your three experiments: the load audit, the encoding experiment and recall versus reread.',
        'Write your three personal study rules for the coming month, each based on one result (for example: "Phone in the kitchen during study", "Ask why for every fact", "Five minutes of recall after every reading").',
        'Explain the page aloud to someone at home in under three minutes.',
    ],
    project_proof='A photo of your one-page model with the three experiment results and your three rules.',
    rubric=[
        ('Model', 'Missing parts or copied from the book', 'All parts, with some unclear links', 'All parts in your own words, with arrows and examples'),
        ('Experiments', 'None run', 'One or two run', 'All three run and recorded'),
        ('Rules', 'Vague ("study better")', 'Specific but not based on results', 'Three specific rules, each linked to a result'),
        ('Explaining', 'Could not explain it', 'Explained with the page in hand', 'Explained in under three minutes, page face down'),
    ],
    short=[
        'Read Nicky Case\'s comic.',
        'Do only the recall-versus-reread experiment (LRN-M01-L03).',
        'Write one rule: five minutes of blank-page recall after every reading session.',
    ],
    flashcards=[
        ('The three stores in the classic memory model', 'Sensory memory, short-term (working) memory and long-term memory.'),
        ('About how many chunks working memory holds (newer estimate)', 'About four.'),
        ('Two kinds of cognitive load you can act on', 'Load from the material (split it up) and load from how you study (remove it).'),
        ('Worked example effect', 'Beginners learn more from studying solved examples first, then solving.'),
        ('Maintenance versus elaborative rehearsal', 'Repeating keeps it briefly; linking it to meaning makes it last.'),
        ('Recommended sleep for adults', '7 hours or more a night, regularly (AASM and SRS).'),
        ('Shape of the forgetting curve', 'Fast at first, then slower.'),
        ('The testing effect in one line', 'Recalling information strengthens memory more than rereading it.'),
    ],
    mistakes=[
        ('Reading the lessons without running the experiments.', 'The experiments are what change your habits. Each takes under an hour.'),
        ('Expecting to feel the difference immediately.', 'Recall feels harder than rereading. Trust the scores you get days later.'),
    ],
)
