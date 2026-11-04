from common import lesson, module, link, xref, table, Q
import tools

L1 = lesson(
    3, 1,
    outcome='You can recognise confirmation bias, sunk cost, overconfidence, the planning fallacy, loss aversion, anchoring and availability in your own decisions, and use one counter-move for each.',
    split='25 minutes reading, 30 minutes of tasks',
    principle='Seven predictable thinking errors cost you time, money and relationships every week; each has a simple counter-move that works better than willpower.',
    science=f"""
A **cognitive bias** is a systematic error: not a random slip, but a mistake people make in the same direction again and again. Hundreds have been named; many overlap and some are weakly supported. These seven are well studied and matter most in daily life.

**1. Confirmation bias.** We look for, notice and remember evidence that supports what we already believe, and explain away the rest. In Peter Wason's classic tasks, people tested rules by looking only for confirming cases. In daily life it shapes which news we read, which relatives we believe and how we judge our own plans. *Counter-move:* before deciding, ask "What would change my mind?" and look for that.

**2. Sunk-cost fallacy.** Continuing something because of what you have already put in (money, time, effort) rather than what it will give you from now on. *Counter-move:* "If I were starting fresh today, with what I know now, would I choose this?"

**3. Overconfidence.** Being more sure than your accuracy justifies. When people give "90% sure" ranges for quantities, the true answer often falls outside far more than 10% of the time. *Counter-move:* write a confidence level, then track how often you are right (calibration).

**4. Planning fallacy.** Underestimating how long tasks take, even when past tasks ran late. Roger Buehler and colleagues found students' "realistic" estimates for finishing a thesis were badly optimistic. *Counter-move:* the **outside view**: look up how long similar tasks took you or others, and plan from that.

**5. Loss aversion.** Losses feel bigger than equal gains; a common estimate is that a loss hurts roughly twice as much as an equal gain feels good. This comes from Kahneman and Tversky's prospect theory. The size and generality are debated: some researchers (for example Gal and Rucker, 2018) argue many effects are better explained by inertia, while other replications find loss aversion but with a size that varies. *Counter-move:* reframe: "Am I avoiding this because it is bad, or because giving up the old thing feels like a loss?"

**6. Anchoring.** The first number you meet pulls your estimate (PD-M01-L02). It replicated strongly in multi-lab tests. *Counter-move:* make your own estimate first, from facts, before looking at anyone else's number.

**7. Availability.** Judging likelihood by how easily examples come to mind (PD-M01-L02). *Counter-move:* "What are the actual numbers over a long period?"

The {link('decisionlab', 'Decision Lab bias index')} and Wikipedia's list of biases describe many more. Be wary of long bias lists in pop articles; some "biases" on them have little research behind them.
""",
    evidence=[
        ('Confirmation bias', 'strong', 'Found across many tasks and settings, from lab puzzles to real-world reasoning.'),
        ('Sunk-cost fallacy', 'moderate', 'Clear in many studies; size varies, and some "sunk cost" choices have other reasons (reputation, learning).'),
        ('Overconfidence in judgements', 'strong', 'Calibration studies repeatedly find intervals that are too narrow.'),
        ('Planning fallacy', 'strong', 'Replicated across students, workers and big public projects.'),
        ('Loss aversion', 'moderate', 'Widely found, but its size and generality are debated.'),
        ('Anchoring', 'strong', 'Replicated in large multi-lab projects.'),
        ('Availability heuristic', 'moderate', 'Well supported in risk perception; effect sizes vary by task.'),
    ],
    example=f"""
Vinod runs a small mobile repair shop near Kuttiady bus stand and is preparing for the LDC exam in his spare time. In one week, all seven biases show up.

He believes a certain brand of phone is unreliable, so he remembers every one that comes in broken and forgets the many that don't (**confirmation**). He keeps paying for an expensive online test series he never uses because he has "already paid three months" (**sunk cost**). He tells a customer, "100%, your phone will be ready by evening," and it isn't (**overconfidence**). He plans to finish the whole Indian Constitution in one week, as he planned and failed to last month (**planning fallacy**). He refuses to sell an old stock of chargers at a small loss, so they keep taking up shelf space (**loss aversion**). A customer's first offer of ₹300 for a repair worth ₹600 makes him settle at ₹400 (**anchoring**). After one break-in in the next town, he spends ₹8,000 on a shutter alarm without checking how often it happens nearby (**availability**).

With the counter-moves, he cancels the unused subscription ("would I buy it today? No"), quotes repair times as "by tomorrow noon, usually today" (and is right more often), plans the Constitution over three weeks based on his last attempt, and writes his price before customers name one.
""",
    apply=f"""
**On yourself:** you cannot remove biases, but you can install counter-moves at the points where they cost the most:

| Bias | Where it costs you | Counter-move |
| --- | --- | --- |
| Confirmation | Opinions, news, judging people | "What would change my mind?" Read one good source from the other side. |
| Sunk cost | Courses, subscriptions, projects, arguments | "Starting fresh today, would I choose this?" |
| Overconfidence | Exam predictions, promises to others | Give ranges and confidence; check later. |
| Planning fallacy | Study plans, deadlines | Use your past record; add 50% for new kinds of task. |
| Loss aversion | Changing jobs, selling things, trying new methods | Compare both options as gains and losses from zero. |
| Anchoring | Prices, salaries, estimates | Write your own number first. |
| Availability | Fear of rare events, health scares | Ask for rates over years, not stories. |

**With others:** use these to understand people, not to label them. A relative who refuses to leave a failing business may be feeling loss aversion and sunk cost, not stupidity. Talk to the feeling ("It's hard to walk away after so much work") before the logic.
""",
    resources=[
        ('decisionlab', 'Read the entries for confirmation bias, sunk cost fallacy, planning fallacy, loss aversion, anchoring and availability heuristic', '30 minutes'),
        ('wp-loss', 'Read the introduction and the criticism section to see how the evidence is debated', '10 minutes'),
        ('os-7-3', 'Re-read the biases table and compare it with the seven here', '5 minutes'),
    ],
    steps=[
        'Write the seven biases on one card with their counter-moves (the table above).',
        'Look back over the last month and find one real decision for each of at least four biases. Write the decision, the bias and what the counter-move would have suggested.',
        'Pick one current decision (a subscription, a plan, a purchase, a disagreement) and apply the relevant counter-move this week. Record what you decided.',
        'Make three predictions about this week with a confidence percentage (for example, "I will study 8 hours: 70% sure"). Check them on Sunday.',
    ],
    proof='Your bias card, four past-decision examples, one current decision with the counter-move used, and three predictions with outcomes.',
    templates=[('Seven-bias card', """SEVEN BIASES AND COUNTER-MOVES
Confirmation  -> "What would change my mind?" Find the best opposing source.
Sunk cost     -> "Starting fresh today, would I choose this?"
Overconfidence-> Give a range and a % confidence. Check later.
Planning      -> Use my past record (outside view). New task type: +50%.
Loss aversion -> List both options' gains and losses from zero.
Anchoring     -> Write my own number before I see theirs.
Availability  -> "What are the numbers over years, not the stories?"
Prediction log: Date | Prediction | % sure | Outcome | Right?""", '')],
    mistakes=[
        ('Collecting bias names like trivia.', 'Seven well-understood biases with counter-moves beat a list of 100 names.'),
        ('Seeing biases in others but not yourself.', 'Researchers call this the "bias blind spot". Start every bias journal with yourself.'),
        ('Assuming every quick decision is biased.', 'Many quick decisions are fine. Use the counter-moves where stakes are high or the bias is known to bite you.'),
        ('Overstating loss aversion as a law.', 'Say "losses often feel bigger than gains"; the "exactly twice" figure is debated.'),
    ],
    quiz=[
        Q('You keep going to a gym you hate because you paid for a year. Which bias is this?', 'Sunk-cost fallacy', 'Anchoring', 'Availability', 'Planning fallacy', why='The money is spent either way; only the future value matters.'),
        Q('What is the "outside view" counter-move for the planning fallacy?', 'Base your estimate on how long similar tasks actually took', 'Work faster', 'Make the deadline shorter to push yourself', 'Ignore deadlines', why='Your track record, or others\' records, beats your hopes.'),
        Q('Which statement about loss aversion is most accurate?', 'Losses often feel bigger than equal gains, but the size and generality are debated', 'Losses always feel exactly twice as bad', 'Loss aversion has been disproved', 'It applies only to money', why='It is widely found but researchers dispute how big and universal it is.'),
        Q('What is the best counter-move against confirmation bias?', 'Ask what evidence would change your mind, and look for it', 'Read more of your favourite sources', 'Decide quickly', 'Avoid all news', why='Deliberately seeking disconfirming evidence counters the bias.'),
    ],
    study='read the lesson and six Decision Lab bias entries',
    action='make a seven-bias card, analyse four past decisions, apply one counter-move to a current decision and check three predictions',
)

L2 = lesson(
    3, 2,
    outcome='You can name ten CBT cognitive distortions, catch them in your own self-talk, and replace one with a balanced thought.',
    split='20 minutes reading, 25 minutes of tasks',
    principle='Many painful feelings are driven less by events than by the distorted way we interpret them; naming the distortion loosens its grip.',
    science=f"""
**Cognitive behavioural therapy (CBT)** grew from the work of psychiatrist Aaron Beck in the 1960s and psychologist Albert Ellis. Beck noticed that depressed patients had automatic, negative thoughts that followed predictable patterns. He called them **cognitive distortions**. David Burns popularised a list of them in his book *Feeling Good* (1980).

CBT is one of the best-tested psychological treatments: many trials and reviews show it helps anxiety disorders and depression, often about as much as medication for mild to moderate cases, with lower relapse for some people. It is a professional therapy; this lesson teaches only the everyday skill of noticing distortions, which you will build on with thought records in PD-M11-L02.

**Ten common distortions:**

1. **All-or-nothing thinking:** "If I don't clear this exam, I am a failure."
2. **Overgeneralisation:** one bad event becomes a pattern: "I always mess up interviews."
3. **Mental filter:** focusing on one negative detail and ignoring the rest: one critical comment wipes out ten kind ones.
4. **Discounting the positive:** "They only praised me to be polite."
5. **Mind reading:** "She didn't reply; she must be angry with me."
6. **Fortune telling:** "I'll definitely forget everything in the exam hall."
7. **Catastrophising:** imagining the worst and treating it as likely: "If I get a cold, I'll miss the exam, lose the job and ruin my life."
8. **Emotional reasoning:** "I feel stupid, so I must be stupid."
9. **"Should" statements:** rigid rules for yourself or others: "I should never make mistakes"; "People should always understand me."
10. **Labelling and personalising:** calling yourself names ("I'm useless") or blaming yourself for things you did not control.

**Biases and distortions are cousins.** Cognitive biases (PD-M03-L01) are errors in judging facts and probabilities; distortions are errors in interpreting events about ourselves and others, and they drive emotions. Both are predictable, both can be caught, and both get weaker with practice.

**What the evidence does and does not say.** Strong evidence supports CBT as a whole package delivered by trained therapists. The evidence for self-help versions (books, apps, worksheets) is also positive but weaker and varies by quality. Simply knowing the names does not cure anything; regular practice of catching and testing thoughts is what helps.
""",
    evidence=[
        ('CBT as a treatment for anxiety and depression', 'strong', 'Hundreds of trials and many reviews support it, delivered by trained professionals.'),
        ('Guided and unguided CBT self-help', 'moderate', 'Helps many people, especially with some support; less than full therapy for severe problems.'),
        ('The specific list of ten distortions', 'tool', 'A practical teaching list; research supports the general idea of negative automatic thoughts more than any one list.'),
    ],
    example=f"""
Ashiq's name is missing from a PSC short list he was hoping for. His thoughts in the first hour: "I'm never going to get a government job (fortune telling). Everyone in Kuttiady will think I'm a waste (mind reading). I wasted four years (all-or-nothing). I'm useless (labelling)."

That evening he writes them down and names each distortion. Then he asks what he would say to a friend in the same position. The answers: he has cleared two other preliminary exams this year; short lists often cut off by fractions of a mark; most people in town are busy with their own lives; and four years of study have given him knowledge that carries over to the next exam. He still feels disappointed (that is appropriate), but the feeling drops from "crushing" to "bad week". He books a time to analyse his errors the next morning, using the error log from the Learning Capabilities course.
""",
    apply=f"""
**The catch-name-check routine (2 minutes):**

1. **Catch:** when you feel a sudden drop in mood, ask "What was I just thinking?" Write the thought word for word.
2. **Name:** which of the ten distortions is it? Often more than one.
3. **Check:** ask one of these questions:
   - "What would I say to a friend who thought this?"
   - "What is the evidence for and against it?"
   - "What is the most likely outcome, not the worst?"
   - "Is this a fact or a feeling?"
4. **Replace:** write a balanced thought that is true and fair, not falsely positive. "I didn't make this list; I've cleared two others; I'll analyse my errors" beats "Everything is fine!"

**With others:** you can gently help a friend notice their distortions ("That sounds like a lot of 'always'. Is it really always?"), but do not play therapist or correct someone's feelings while they are upset. Listen first (Module 25), and suggest professional help if a friend seems stuck in low mood for weeks.
""",
    resources=[
        ('os-14-4', 'Read the section on coping and cognitive strategies in stress regulation', '15 minutes'),
        ('noba', 'Search for the module "Therapeutic Orientations" and read the cognitive-behavioural part', '20 minutes'),
        ('ggia', 'Search the site for "Putting Things in Perspective" or a reappraisal practice and read one', '10 minutes'),
    ],
    steps=[
        'Copy the list of ten distortions into your Playbook notebook, with one example from your own life for each that you can recognise.',
        'For five days, use catch-name-check-replace at least once a day when your mood drops. Write the thought, the distortion, the check question used and the balanced thought.',
        'At the end, count which distortions came up most. Circle your top two.',
        'Write one sentence you will say to yourself when your top distortion appears (for example, for mind reading: "I don\'t know what they think until I ask").',
    ],
    proof='Five dated catch-name-check-replace entries, your top two distortions, and your counter-sentence.',
    templates=[('Catch-name-check-replace', """CATCH, NAME, CHECK, REPLACE         Date ______
Situation (facts): ____________________________________________
Thought, word for word: "______________________________________"
Distortion(s): all-or-nothing / overgeneralising / mental filter / discounting
  positive / mind reading / fortune telling / catastrophising / emotional
  reasoning / should / labelling or personalising
Check question used: friend? evidence? most likely? fact or feeling?
Balanced thought (true and fair): ______________________________
Mood before (0-10): __  after (0-10): __""", '')],
    mistakes=[
        ('Replacing negative thoughts with fake positive ones.', '"I\'m the best!" is as distorted as "I\'m useless". Aim for accurate and fair.'),
        ('Arguing with every feeling.', 'Sadness after a real loss is not a distortion. Use the routine when the feeling is out of proportion or stays stuck.'),
        ('Using distortion labels on other people in an argument.', '"You\'re catastrophising" usually makes things worse. Use the names on yourself.'),
        ('Thinking this replaces therapy.', 'If low mood or anxiety lasts two weeks or more and affects daily life, see a professional (PD-M11-L01).'),
    ],
    quiz=[
        Q('"She hasn\'t replied in two hours; she must be angry with me." Which distortion is this?', 'Mind reading', 'All-or-nothing thinking', 'Discounting the positive', 'Should statement', why='It assumes you know what another person is thinking without evidence.'),
        Q('"I feel stupid, so I must be stupid." Which distortion?', 'Emotional reasoning', 'Catastrophising', 'Labelling', 'Mental filter', why='Treating a feeling as proof of a fact.'),
        Q('What is the best kind of replacement thought?', 'A balanced, true and fair statement', 'The most positive thought possible', 'The opposite of the original thought', 'No thought at all', why='Balanced thoughts are believable; falsely positive ones are not.'),
        Q('How strong is the evidence for CBT delivered by trained therapists for anxiety and depression?', 'Strong, from hundreds of trials', 'There is no evidence', 'Only one small study', 'It works only for children', why='CBT is one of the best-tested psychological treatments.'),
    ],
    study='read the lesson and the OpenStax stress-regulation section',
    action='use catch-name-check-replace on five days and find your top two distortions',
)

L3 = lesson(
    3, 3,
    outcome='You can use four debiasing techniques and keep a two-week bias journal with three entries a day: yourself, the news and an ad.',
    split='15 minutes reading, 10 minutes a day for two weeks',
    principle='Knowing about biases protects you surprisingly little; changing the situation (checklists, outside views, asking others, slowing down) works better.',
    science=f"""
A disappointing finding first: simply learning about biases does not reliably make people less biased. People also show a **bias blind spot**: they rate themselves as less biased than others, even after learning about biases. Intelligence protects less than you might think.

So what works? Researchers have tested several **debiasing** strategies:

1. **Consider the opposite.** Asking yourself "What are some reasons my first judgement might be wrong?" reduced several biases (anchoring, overconfidence, hindsight) in lab studies by Lord, Lepper and Preston and by Mussweiler and colleagues.
2. **Take the outside view.** Base predictions on what happened in similar cases (the reference class) before adjusting for your special case. This is the strongest single tool against the planning fallacy and overconfidence.
3. **Use checklists and procedures.** In medicine and aviation, checklists reduce errors because they do not depend on the person remembering to think. Your three-question pause and seven-bias card are checklists.
4. **Get other people's independent views.** Ask people to give their estimates or opinions *before* hearing yours, then combine them. Averages of independent guesses tend to beat most individuals ("wisdom of crowds"), but only if the guesses are really independent.
5. **Training with feedback.** Some studies (for example, Morewedge and colleagues, 2015) found that a single training session using games or videos with personal feedback reduced certain biases for weeks. Results are promising but not yet broad.

**Why a bias journal?** It combines two of these: it slows you down (System 2 has to look) and gives you feedback about your own patterns. Splitting entries between **yourself, the news and ads** helps because biases are easier to see in others first; seeing them in ads and news trains the eye, and the self-entries apply it where it matters.
""",
    evidence=[
        ('Learning about biases alone reduces them', 'mixed', 'Small or no effects in many studies; the bias blind spot persists.'),
        ('"Consider the opposite" reduces several biases', 'moderate', 'Supported in lab studies across several biases.'),
        ('Outside view (reference-class forecasting)', 'moderate', 'Improves forecasts in research and in planning large projects.'),
        ('Checklists reduce errors in high-stakes work', 'moderate', 'Good evidence in surgery and aviation; benefits depend on proper use.'),
        ('Debiasing training games with feedback', 'mixed', 'Promising lab results lasting weeks; transfer to real life is less clear.'),
        ('Bias journal as a habit', 'tool', 'Combines slowing down and feedback; judge it by your own two weeks of data.'),
    ],
    example=f"""
Sreeja keeps the bias journal for two weeks. Day 3 looks like this:

- **Me:** she decided a new classmate was arrogant after one short reply, then noticed only his short replies all week (**first impression + confirmation bias**). Counter-move: she asked him about his preparation; he was shy, not arrogant.
- **News:** a channel ran "Fourth child-kidnapping attempt this month!" with dramatic music, without saying how many reports turned out to be false (**availability**, and fear-driven framing). She looked for police figures and found none in the story.
- **Ad:** an online course ad: "Join 50,000 toppers! Price rises in 2 hours!" (**social proof** and **false urgency**). She checked: the timer reset when she reloaded the page.

By day 14 she sees that her own most common trap is mind reading about people, and she adds a line to her Playbook: "I don't decide what someone is like until I've asked them a real question."
""",
    apply=f"""
**Your two-week bias journal:**

- **Three entries a day,** about 10 minutes in total: one from **yourself**, one from **the news** (TV, paper or online), one from an **ad** (TV, YouTube, Instagram, a poster, a shop).
- **Use the list:** the seven biases (PD-M03-L01), the ten distortions (PD-M03-L02), plus the halo effect, fundamental attribution error and social proof (you will meet them properly in Part D).
- **Always add the better thinking:** what the counter-move suggests.
- **Weekly count:** on each Sunday reflection, count which bias you caught most often in *yourself*.

**Four debiasing habits to keep after the journal:**
1. Before big decisions: "What are three reasons I might be wrong?"
2. Before estimates: "How long did similar things take?"
3. In groups: ask for opinions before giving yours.
4. Use your checklists (pause card, seven-bias card) rather than trusting yourself to remember.
""",
    resources=[
        ('decisionlab', 'Browse the index and pick three biases you see often in ads; read them', '15 minutes'),
        ('wp-biases', 'Skim the list to see how many biases have been proposed; notice which ones you already know', '10 minutes'),
    ],
    steps=[
        'Set up the bias journal as a Joplin note (or a notebook page) using the template below.',
        'Add the habit "Bias journal: 3 biases spotted" to Loop Habit Tracker for 14 days.',
        'Write three entries every day for 14 days: one from yourself, one from news, one from an ad.',
        'On days 7 and 14, count your self-entries by bias and write your top three traps.',
        'At the end, write three lines: your top trap, the counter-move you will keep, and one example where the journal changed a decision.',
    ],
    proof='The 14-day bias journal (at least 36 entries), two weekly counts and your three-line summary.',
    templates=[('Bias journal (two weeks)', tools.BIAS_JOURNAL, '')],
    mistakes=[
        ('Doing only the news and ads.', 'They are training. The self-entries are where you gain. Write at least one every day, even a small one.'),
        ('Forcing a bias name on everything.', 'If no bias fits, write "unsure" and move on. Accuracy beats volume.'),
        ('Stopping after the two weeks with nothing kept.', 'Keep one or two debiasing habits and your top-trap sentence in the Playbook.'),
        ('Using the journal to judge people harshly.', 'Note the pattern, not a verdict on the person. Everyone has these biases, including you.'),
    ],
    quiz=[
        Q('What does research say about simply learning bias names?', 'It protects surprisingly little on its own', 'It removes biases completely', 'It makes biases worse', 'It works only for clever people', why='Knowledge alone gives small or no effects; the bias blind spot remains.'),
        Q('Which is the strongest single tool against the planning fallacy?', 'The outside view: base estimates on similar past cases', 'Trying harder', 'Setting shorter deadlines', 'Thinking positively', why='Reference-class forecasting corrects optimistic inside-view estimates.'),
        Q('Why should people give opinions before hearing yours in a group?', 'So their judgements stay independent and the group gets better information', 'To be polite', 'To save time', 'Because your opinion is less important', why='Independent views combine well; anchored views do not.'),
        Q('What is the "bias blind spot"?', 'Seeing yourself as less biased than other people', 'Being unable to see colours', 'Ignoring ads', 'Having no biases', why='People readily see bias in others but underrate it in themselves.'),
    ],
    study='read the lesson and set up the bias journal',
    action='keep the bias journal for 14 days with three entries a day and write the summary',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    3,
    overview=f"""
The thinking traps that cost you most: seven well-studied cognitive biases, ten CBT cognitive distortions, and debiasing methods that actually help. You keep a two-week bias journal (three entries a day: yourself, the news and an ad).

Module 1 showed how the fast mind takes shortcuts. This module names the most costly errors those shortcuts produce, in judgement (biases) and in how we talk to ourselves (distortions), and gives a counter-move for each.

The honest headline is that knowing about biases is not enough. What helps is changing your process: checklists, outside views, independent opinions and slowing down at the right moments. The bias journal is how you practise. If you did the Learning Capabilities course, {xref('lrn', 'lrn-m16', 'its thinking-skills module')} covered biases in study and exam reasoning; this module applies them to money, people and mood.
""",
    outcomes=[
        'Explain and spot confirmation bias, sunk cost, overconfidence, planning fallacy, loss aversion, anchoring and availability.',
        'Name ten cognitive distortions and use catch-name-check-replace.',
        'Use four debiasing habits: consider the opposite, outside view, checklists and independent opinions.',
        'Complete a two-week bias journal and name your own top three traps.',
    ],
    lessons=LESSONS,
    project='a two-week bias journal and your personal trap profile',
    project_steps=[
        'Complete the 14-day bias journal from PD-M03-L03.',
        'Write your trap profile: your top three biases or distortions, with a real example and a counter-move for each.',
        'Choose one decision coming up in the next month and plan which counter-move you will use.',
        'Add your top-trap sentence to your Personal Playbook.',
    ],
    project_proof='The completed journal, your trap profile (top three with examples and counter-moves) and the planned decision.',
    rubric=[
        ('Recognition', 'Names fewer than five biases or distortions', 'Names most but confuses some', 'Names all seven biases and ten distortions with own examples'),
        ('Journal', 'Fewer than 20 entries', '20 to 35 entries', '36 or more entries, at least 12 about yourself'),
        ('Counter-moves', 'None used', 'Used once or twice', 'Used on several real decisions, with results noted'),
        ('Self-insight', 'No pattern found', 'A vague pattern', 'A clear top-three profile with evidence'),
    ],
    short=[
        'Learn the seven-bias card and do one self-entry a day for 14 days.',
        'Use catch-name-check-replace on your worst mood moment each week.',
    ],
    flashcards=[
        ('Confirmation bias counter-move', '"What would change my mind?" Then look for it.'),
        ('Sunk-cost counter-move', '"Starting fresh today, would I choose this?"'),
        ('Planning fallacy counter-move', 'The outside view: use how long similar tasks took.'),
        ('Loss aversion: honest summary', 'Losses often feel bigger than gains; how much bigger is debated.'),
        ('Mind reading (distortion)', 'Assuming you know what others think without evidence.'),
        ('Catastrophising', 'Treating the worst outcome as likely.'),
        ('Balanced thought', 'A replacement thought that is true and fair, not falsely positive.'),
        ('Bias blind spot', 'Seeing yourself as less biased than others.'),
        ('Does learning bias names debias you?', 'Only a little. Process changes (checklists, outside view) work better.'),
    ],
    mistakes=[
        ('Treating the module as a vocabulary test.', 'The measure of success is changed decisions, recorded in the journal.'),
        ('Becoming suspicious of all your thoughts.', 'Most thoughts are fine. Look closely only when stakes are high or mood drops sharply.'),
        ('Using bias names as weapons in arguments.', 'It makes people defensive and blinds you to your own biases.'),
    ],
    tools=[
        'The seven-bias card with counter-moves and a prediction log (PD-M03-L01).',
        'Catch-name-check-replace for distortions (PD-M03-L02).',
        'The two-week bias journal (PD-M03-L03).',
    ],
    playbook=[
        'My top three thinking traps are ______, ______ and ______. Counter-moves: ______.',
        'Before big decisions I ask: "What are three reasons I might be wrong?" and "How long did similar things take?"',
    ],
)
