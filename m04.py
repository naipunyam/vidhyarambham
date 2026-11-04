from common import lesson, module, link, xref, table, Q
import tools

L1 = lesson(
    4, 1,
    outcome='You can make a decision under uncertainty using options, rough probabilities, base rates and the reversible-or-not test, and judge decisions by process rather than luck.',
    split='20 minutes reading, 30 minutes of tasks',
    principle='You cannot control outcomes, only the quality of your decisions: list real options, think in rough probabilities, start from base rates, and match the effort to how reversible the choice is.',
    science="""
Most life decisions are made with incomplete information: which exam to focus on, whether to take a private job while preparing, whether to lend money to a relative. Decision research offers a few robust ideas.

**1. Separate decisions from outcomes.** A good decision can turn out badly (bad luck), and a bad decision can turn out well (good luck). Poker players call judging decisions by outcomes "resulting". If you judge yourself only by results, you learn the wrong lessons. Instead, review the *process*: Did I consider the options? Did I use the information available?

**2. Think in rough probabilities.** "Will I clear this exam?" is not yes or no. Saying "maybe 20%" forces you to ask what the base rate is (how many candidates get selected for how many vacancies) and what would move your chances up. Research on forecasting, notably Philip Tetlock's work with volunteer forecasters, found that people who think in numbers, update often and start from base rates make better predictions than confident pundits.

**3. Start from the base rate, then adjust.** Ask how things usually go for people in your situation (the outside view, PD-M03-L03), then adjust for what is genuinely special about you. People do the reverse: they start from their special story and forget the base rate.

**4. Expected value, roughly.** For choices with money or time at stake, multiply rough chances by rough payoffs. A ₹500 "lucky draw" ticket with a 1-in-10,000 chance of ₹10 lakh is worth about ₹100 on average: a bad deal. You do not need exact numbers; even rough ones expose bad bets.

**5. Reversible or not.** Some decisions are easy to undo ("two-way doors": trying a new study timetable, a one-month gym trial). Decide them quickly and learn by doing. Others are hard to undo ("one-way doors": quitting a job, a big loan, signing a property deal, marriage). Slow down, gather information, sleep on it and ask people you trust.

**6. Satisficing for small things.** Herbert Simon described "satisficing": choosing the first option that meets your standards rather than searching for the best. Research by Barry Schwartz and colleagues found that people who always try to maximise tend to report more regret and less satisfaction, though later studies debate how the scales measure this. For everyday choices, "good enough" is a strategy, not laziness.
""",
    evidence=[
        ('Judging decisions by outcomes misleads learning (outcome bias)', 'strong', 'Shown in many studies where identical decisions are rated differently depending on results.'),
        ('Base rates and probability thinking improve forecasts', 'strong', 'Large forecasting tournaments found trained, probabilistic forecasters beat others.'),
        ('Maximisers are less satisfied than satisficers', 'mixed', 'Found in early studies; later work questions how maximising is measured.'),
        ('Reversible versus irreversible decisions', 'tool', 'A practical rule from decision practice; little direct testing, but it matches how errors cost.'),
    ],
    example="""
Anu has been offered a job as a billing assistant in a supermarket in Kozhikode: ₹12,000 a month, 9 to 6, six days a week. She is preparing for the LDC and LGS exams and has a notification due in four months.

She uses the decision sheet. **Options:** take the job; decline and study full time; ask for a part-time arrangement; take it for three months and review. **Reversible?** Mostly: she could leave the job later, though the employer may not take her back. **Base rate:** she asks two friends who studied while working; one cleared a list, one dropped out of the exam schedule. She looks up the PSC vacancies and applicants for the last LDC list and sees that only a small share of candidates get selected, so her chances are uncertain either way. **Expected value:** the job gives certain income and less family pressure; studying full time gives perhaps a modestly better chance at a job that pays more for decades.

She decides to ask for a 9-to-2 shift, and if refused, to take the full-time job for three months while keeping a fixed 2-hour study block each evening, with a review date. Whatever the exam result, she will judge the decision by whether she followed the plan and reviewed it, not only by luck.
""",
    apply="""
**For any decision you will live with for months, use the decision sheet (template below).** The most important lines are:

1. **At least three options,** including "wait" and a middle path. Most bad decisions come from considering only two (yes or no).
2. **Reversible or not.** If reversible, decide within a day and set a review date. If not, slow down: wait 48 hours, gather one more piece of information, ask one experienced person.
3. **Base rate:** "How does this usually go for people like me?"
4. **Rough probabilities:** write a percentage, even a guess. It makes your thinking visible.
5. **A review date,** where you judge the process, not just the outcome.

**For small daily choices:** set a "good enough" standard and pick the first option that meets it.

**With others:** when friends or family ask your advice, help them list options and ask about reversibility before giving your opinion. You will help more by improving their process than by telling them what to do.
""",
    resources=[
        ('os-7-3', 'Re-read the problem-solving strategies (trial and error, algorithms, heuristics)', '10 minutes'),
        ('noba', 'Search for the module "Judgment and Decision Making" and read the main sections', '25 minutes'),
        ('mit-psych', 'Optional: browse the course list of sessions and choose one on thinking or decision-making to watch', '50 minutes'),
    ],
    steps=[
        'Choose a real decision you face now or in the next three months (study plan, job, purchase, family issue).',
        'Fill in the decision sheet for it, with at least three options, a base rate from two people or a source, and a probability for each option\'s main outcome.',
        'Mark it reversible or not, and follow the matching rule (decide within a day with a review date, or wait 48 hours and gather one more piece of information).',
        'Write a review date in your calendar. On that date, judge the decision process in three lines.',
    ],
    proof='A completed decision sheet for a real decision and a calendar screenshot or note with the review date.',
    templates=[('Decision sheet', tools.DECISION_SHEET, '')],
    mistakes=[
        ('Only two options.', 'Add "wait", "a smaller version" and "a middle path". The best option is often a third one.'),
        ('Waiting for certainty.', 'Most decisions never become certain. Decide when more information would not change your choice.'),
        ('Treating a bad outcome as proof of a bad decision.', 'Ask whether you used the information you had. Bad luck exists.'),
        ('Overthinking small reversible choices.', 'Satisfice: pick the first good-enough option and move on.'),
    ],
    quiz=[
        Q('You decided carefully, but the result was bad because of an unexpected event. What should you conclude?', 'The process may still have been good; review what you knew at the time', 'It was a bad decision', 'Planning is useless', 'You should always decide by instinct', why='Outcomes include luck; judge the decision by the process.'),
        Q('Which decision is a "one-way door"?', 'Taking a large loan to buy land', 'Trying a new study timetable for a week', 'Choosing a new tea shop', 'Testing a different morning routine', why='Big loans are hard to reverse, so they deserve slower decisions.'),
        Q('A ₹100 ticket gives a 1 in 1,000 chance of winning ₹50,000. What is its rough expected value?', 'About ₹50, so on average you lose about ₹50 per ticket', 'About ₹50,000', 'About ₹100, a fair deal', 'It cannot be calculated', why='₹50,000 × 1/1,000 = ₹50, less than the ₹100 price.'),
        Q('Why include "wait" as an option?', 'It is often a real option, and waiting can bring useful information at low cost', 'Waiting is always best', 'It makes the sheet longer', 'It avoids all risk', why='Waiting is a genuine choice; its cost should be compared, not ignored.'),
    ],
    study='read the lesson and the Noba judgement and decision-making module',
    action='fill in a decision sheet for a real decision and set a review date',
)

L2 = lesson(
    4, 2,
    outcome='You can run a pre-mortem on a plan, cut down options when choices overwhelm you, and handle regret in a useful way.',
    split='20 minutes reading, 30 minutes of tasks',
    principle='Imagining that your plan has already failed reveals risks you would otherwise miss; too many options rarely matter as much as claimed, but when they do, limit them; regret is information, not a sentence.',
    science=f"""
**Pre-mortems.** Psychologist Gary Klein described the **pre-mortem** in the Harvard Business Review in 2007. Before starting a project, the team imagines it is the future and the project has failed badly, then each person writes down every reason why. Klein based it on research by Mitchell, Russo and Pennington (1989), who found that imagining an event *has already happened* ("prospective hindsight") increased people's ability to identify reasons for an outcome by about 30%. A pre-mortem also makes it safe to voice doubts that people would otherwise keep quiet ({link('klein', 'Klein, 2007')}).

**Choice overload.** In a famous study, Sheena Iyengar and Mark Lepper set up a jam-tasting stall in a supermarket. When 24 jams were on display, more people stopped, but only about 3% bought; with 6 jams, about 30% of those who stopped bought. This "paradox of choice" became a business and self-help favourite. But when Benjamin Scheibehenne and colleagues pooled 50 experiments with over 5,000 people in 2010, the **average effect was virtually zero**, with large differences between studies. Choice overload seems to happen only in some conditions: when you have no clear preference, no option clearly stands out, the options are hard to compare and you are short of time ({link('scheibehenne', 'Scheibehenne et al., 2010')}). So the honest rule is: more choice is not always bad, but when you are stuck, reduce the options deliberately.

**Regret.** Research by Thomas Gilovich and Victoria Medvec suggests that in the short term people regret actions that went wrong, but over the long term they regret **inactions** more: the things they did not try. Regret can be useful when it points to something you can still change. It becomes harmful when it turns into rumination (going over the same loss again and again, PD-M11-L01).
""",
    evidence=[
        ('Prospective hindsight improves identifying risks', 'moderate', 'Supported by the 1989 study and practical use; few large trials of pre-mortems themselves.'),
        ('Choice overload as a general rule', 'mixed', 'The famous jam study was striking, but a meta-analysis found an average effect near zero.'),
        ('Choice overload in specific conditions', 'moderate', 'More likely with no clear preference, hard-to-compare options and time pressure.'),
        ('Long-term regret is more about inaction', 'moderate', 'Found in several studies by Gilovich and colleagues; depends on how regret is asked about.'),
    ],
    example="""
Joseph sir is helping five aspirants in Thottilpalam plan a 12-week study group before the Degree Level prelims. Before starting, he runs a pre-mortem: "It's twelve weeks from now. The group fell apart and nobody's scores improved. Write down why."

In five minutes, they write: "Meetings at 7 pm clashed with family duties," "Two people dominated," "We chatted instead of testing," "Monsoon power cuts killed online mocks," "Nobody knew what to study each week." They fix each before starting: meetings move to Sunday 3 pm, a timer gives each person a turn, every meeting starts with a 20-question test, mocks are downloaded in advance, and a shared plan lists each week's topics.

One member, Shamna, is overwhelmed by choosing among nine YouTube channels and four apps. Joseph sir asks her to pick one source per subject using two criteria (covers the syllabus, has practice questions) and to ignore the rest for 12 weeks.
""",
    apply="""
**Pre-mortem in 10 minutes (alone or with others):**

1. Describe the plan in two lines.
2. Say: "It is [date]. The plan has failed badly."
3. Each person writes, silently, every reason it failed (5 minutes).
4. Go round, one reason each, until all are listed.
5. For the three most likely or most damaging, write one change to the plan now.

**When choices overwhelm you:**
- Set two or three **must-have criteria** before looking at options.
- **Cut to three** options that meet them, then compare only those.
- For small choices, take the first good-enough option (satisfice).
- Set a decision deadline.

**Using regret well:** write the regret in one line, ask "Is there anything I can still do?", and if yes, schedule one small step. If no, write what you learned and close it. If you keep replaying the same regret for weeks, use a thought record (PD-M11-L02).
""",
    resources=[
        ('klein', 'Read the whole short article on the premortem method', '10 minutes'),
        ('scheibehenne', 'Read the abstract and the discussion section (when does choice overload happen?)', '15 minutes'),
        ('wp-overchoice', 'Read the conditions for choice overload', '10 minutes'),
    ],
    steps=[
        'Run a pre-mortem on one real plan (your study plan for the next month, a purchase, a family event). Write at least eight failure reasons and three fixes.',
        'Make one of the fixes this week.',
        'Find one place where choice overwhelms you (apps, books, courses, clothes, phone plans). Write two or three must-have criteria, cut to three options and choose.',
        'Write one regret from the last year: action or inaction? Is there one small step you can still take? Schedule it or write the lesson and close it.',
    ],
    proof='Your pre-mortem list with three fixes (one done), a criteria-and-three-options note with your choice, and a regret note.',
    templates=[('Pre-mortem and choice-cutting', """PRE-MORTEM                 Plan: ______________________________
"It is ______ (date). The plan has failed badly. Why?"
1. ________________ 2. ________________ 3. ________________
4. ________________ 5. ________________ 6. ________________
7. ________________ 8. ________________
Top 3 (most likely or most damaging) -> fix now:
A. ______________ -> ______________
B. ______________ -> ______________
C. ______________ -> ______________

CHOICE CUTTING        Choosing: ______________   Deadline: ______
Must-haves: 1. ________ 2. ________ 3. ________
Three options that meet them: A ______ B ______ C ______
Choice: ______  (good enough? Y)  Stop looking until: ______""", '')],
    mistakes=[
        ('Turning the pre-mortem into general worry.', 'It is a 10-minute exercise with fixes at the end, not permission to imagine disaster all week.'),
        ('Quoting the jam study as proof that choice is bad.', 'The average effect across studies is close to zero. Say "sometimes too many options can stall us".'),
        ('Comparing every option forever.', 'Set criteria first, cut to three, set a deadline.'),
        ('Letting regret become rumination.', 'One step or one lesson, then close it. Seek help if it persists.'),
    ],
    quiz=[
        Q('What makes a pre-mortem different from ordinary risk thinking?', 'You imagine the plan has already failed and explain why', 'You only list the good outcomes', 'You wait until after the project fails', 'You ask one expert to predict the result', why='Prospective hindsight ("it has failed; why?") surfaces more reasons.'),
        Q('What did the 2010 meta-analysis of 50 choice-overload experiments find?', 'An average effect of virtually zero, with large differences between studies', 'Choice overload always reduces buying', 'More choice always increases happiness', 'Only jam is affected', why='The effect depends on conditions and is not a general rule.'),
        Q('When is choice overload most likely?', 'When you have no clear preference and options are hard to compare', 'When there are only two options', 'When you know exactly what you want', 'When one option is clearly best', why='These are the conditions identified in the research.'),
        Q('According to Gilovich and Medvec\'s work, what do people regret most in the long run?', 'Things they did not do', 'Things they did that went well', 'Small purchases', 'Nothing', why='Over time, regrets of inaction tend to dominate.'),
    ],
    study='read the lesson and Klein\'s premortem article',
    action='run a pre-mortem on a real plan and make one fix, cut one overwhelming choice to three options and write one regret note',
)

LESSONS = [L1, L2]

MODULE = module(
    4,
    overview="""
Practical decision-making under uncertainty: options, base rates, rough probabilities, reversible and irreversible choices, pre-mortems, choice overload (honestly) and regret. You make a real decision with a decision sheet.

Part A ends here, with the step from understanding your mind to using it well. Big life choices (career, money, family) are made with incomplete information. You cannot control the outcomes, but you can control the process, and a good process makes good outcomes more likely over a lifetime.

Money decisions get their own deep treatment in {xref('fin', 'fin-m01', 'the Personal Finance course')}; here you learn the general tools that work for every kind of choice.
""",
    outcomes=[
        'Separate decision quality from outcome luck.',
        'Use options, base rates, rough probabilities and expected value on a real choice.',
        'Apply the reversible-or-not rule to decide how much effort a choice deserves.',
        'Run a 10-minute pre-mortem and fix the top three risks.',
        'Cut overwhelming choices and use regret as information.',
    ],
    lessons=LESSONS,
    project='a real decision made with the decision sheet and a pre-mortem',
    project_steps=[
        'Choose one decision that matters in the next three months.',
        'Fill in the decision sheet (PD-M04-L01), run a pre-mortem on your chosen option (PD-M04-L02) and adjust the plan.',
        'Make the decision, or set the date by which you will.',
        'Write a one-paragraph decision memo: options, chosen option, why, main risks and fixes, review date.',
    ],
    project_proof='The decision sheet, pre-mortem list and one-paragraph decision memo with a review date.',
    rubric=[
        ('Options', 'Only yes or no', 'Three options, but similar', 'Three or more genuinely different options including wait or a middle path'),
        ('Evidence', 'No base rate', 'A base rate guessed', 'A base rate from people or a source, plus rough probabilities'),
        ('Risk', 'No pre-mortem', 'Pre-mortem without fixes', 'Pre-mortem with three fixes built into the plan'),
        ('Follow-up', 'No review date', 'Review date set', 'Review date set and process criteria written'),
    ],
    short=[
        'For one decision, list three options and mark it reversible or not.',
        'Do a 5-minute solo pre-mortem on your current study plan.',
    ],
    flashcards=[
        ('Resulting (outcome bias)', 'Judging a decision only by its outcome, ignoring luck.'),
        ('Two-way door decision', 'Easy to reverse: decide quickly and review.'),
        ('One-way door decision', 'Hard to reverse: slow down, gather information, consult.'),
        ('Expected value, roughly', 'Chance × payoff, compared with the cost.'),
        ('Pre-mortem', 'Imagine the plan failed; list why; fix the top risks.'),
        ('Prospective hindsight finding', 'Imagining an event has happened helped people find about 30% more reasons.'),
        ('Choice overload: honest status', 'Famous jam study, but the average effect across 50 experiments is near zero; happens only in some conditions.'),
        ('Satisficing', 'Choosing the first option that meets your standards.'),
    ],
    mistakes=[
        ('Using the full sheet for every small choice.', 'Save it for decisions you will live with for months.'),
        ('Never reviewing decisions.', 'Without a review date you cannot learn whether your process works.'),
        ('Asking only people who agree with you.', 'Ask at least one person who might see it differently.'),
    ],
    tools=[
        'The decision sheet (PD-M04-L01).',
        'The 10-minute pre-mortem and choice-cutting template (PD-M04-L02).',
    ],
    playbook=[
        'For one-way-door decisions I wait 48 hours, gather one more fact, ask one experienced person and run a pre-mortem.',
        'I judge decisions by process: options, base rate, probabilities, risks, review.',
    ],
)
