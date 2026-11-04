from common import lesson, module, link, xref, table, fence, Q
import tools

L1 = lesson(
    28, 1,
    outcome='You can explain Cialdini\'s seven principles of influence with the evidence for each, use them honestly in your own requests, and spot when they are used against you.',
    split='25 minutes reading, 25 minutes of tasks',
    principle='People say yes more often when they feel they owe you, have already committed, see others like them doing it, trust your expertise, like you, fear missing out, or share an identity with you; use these only when they are true and the deal is good for both.',
    science=f"""
Robert Cialdini's *Influence* (1984) organised decades of research into six principles; in 2016 (*Pre-Suasion*) he added a seventh, **unity** ({link('wp-cialdini', 'summary')}). The book also drew on his time training with salespeople and fundraisers, so some examples are anecdotes rather than experiments. Here is each principle with its honest evidence.

**1. Reciprocity: we feel obliged to return favours.** In a 1971 study by Dennis Regan, people who received a free soft drink from a stranger later bought more raffle tickets from him. Field studies found that waiters who gave diners a sweet with the bill received slightly larger tips. Reciprocity is one of the most universal social norms. *Honest use:* give real value first (help, information, a sample) without strings. *Manipulative use:* small "gifts" to create pressure (free "gifts" at timeshare or MLM presentations).

**2. Commitment and consistency: we want to act consistently with what we've said or done.** In Jonathan Freedman and Scott Fraser's 1966 **foot-in-the-door** study, homeowners who first agreed to a small request (a small sign) were much more likely to later agree to a big one (a large, ugly "Drive Carefully" sign). Meta-analyses find the foot-in-the-door effect is real but **small** and varies. *Honest use:* ask people to commit to a small, specific first step they want ("Shall we meet once to try the study group?"). *Manipulative use:* trapping people with tiny agreements towards a big purchase.

**3. Social proof: we follow what others like us do.** A widely cited hotel study (Noah Goldstein, Cialdini and Vladas Griskevicius, 2008) found that a card saying "most guests reuse their towels" increased reuse compared with an environmental message. **Replications have been mixed**: some found no effect. Social-norm messages do often work for things like energy saving (for example, home energy reports comparing households with neighbours), with modest effects. *Honest use:* real numbers about real people. *Manipulative use:* fake reviews, fake "500 people are viewing this", paid crowds.

**4. Authority: we defer to experts and people in authority.** Stanley Milgram's obedience studies (PD-M30-L01) are the extreme case. Everyday versions include uniforms, titles and confident claims. *Honest use:* share your real, relevant credentials and evidence. *Manipulative use:* fake police, bank or CBI officers in scams (Module 32).

**5. Liking: we say yes to people we like** (similarity, compliments, cooperation, familiarity: Module 25). Well supported. *Honest use:* be genuinely friendly and find real common ground. *Manipulative use:* fake friendliness or flattery to sell.

**6. Scarcity: things seem more valuable when rare or running out.** In Stephen Worchel's 1975 study, cookies from a jar of two were rated more desirable than identical cookies from a jar of ten. Scarcity and loss framing are powerful but research effects vary. *Honest use:* tell people about real deadlines and limits. *Manipulative use:* fake countdown timers and "only 2 left" (banned as "false urgency" under India's 2023 dark-pattern guidelines).

**7. Unity: we are influenced by people we see as "one of us"** (family, hometown, school, religion, profession). Supported by research on shared identity. *Honest use:* real shared identities ("as fellow Kuttiady aspirants…"). *Manipulative use:* "affinity fraud", where scammers target their own community.

**One more: door-in-the-face.** Asking for a large request first, then a smaller one, can increase agreement to the smaller one (Cialdini and colleagues, 1975); meta-analyses find a small effect. It edges towards manipulation if the first request is fake.
""",
    evidence=[
        ('Reciprocity', 'strong', 'A universal norm; supported by many lab and field studies.'),
        ('Foot-in-the-door (commitment)', 'moderate', 'Real but small average effect in meta-analyses.'),
        ('Social proof (hotel-towel study)', 'mixed', 'The famous study had mixed replications; social norms often work modestly elsewhere.'),
        ('Authority', 'strong', 'From obedience studies to everyday compliance.'),
        ('Liking', 'strong', 'Many studies on similarity, familiarity and compliments.'),
        ('Scarcity', 'moderate', 'Classic studies; effect sizes vary.'),
        ('Unity (shared identity)', 'moderate', 'Supported by social-identity research; the "principle" is newer.'),
        ('Door-in-the-face', 'mixed', 'Small effect in meta-analyses.'),
    ],
    example="""
Vinod wants more customers for his phone-repair shop near Kuttiady bus stand.

**Honest uses:** he offers a free 5-minute check of any phone's battery health (**reciprocity**, real value, no pressure). He puts up a board with the real number of repairs done that month and two real customer quotes he asked permission to use (**social proof**). He displays his certificate from a mobile-repair course (**authority**, real). He learns regular customers' names and asks about their families (**liking**, genuine). He tells customers honestly, "The screen replacement offer from the supplier ends Saturday" when it really does (**scarcity**, true). He offers a small discount to students preparing for PSC, since he is one too (**unity**, real).

**What he refuses to do:** fake "only 1 left" signs, fake reviews, or "free gifts" that make customers feel obliged to buy expensive cases. When a supplier suggests putting "Original Apple parts" on non-original parts, he says no. A year later, his best source of new customers is word of mouth.
""",
    apply=f"""
**The ethics test (use before any persuasion):**
1. **Is it true?** Every claim, number and deadline.
2. **Is it good for them too?** Would they thank you in a month?
3. **Is it easy to say no?** No pressure, no traps, no guilt.
4. **Would I be comfortable if they saw my notes?** If you'd be embarrassed for them to know your tactic, it's manipulation.

**Honest use of each principle:**
{table(['Principle', 'Honest use', 'Red flag when used on you'], [
    ('Reciprocity', 'Give real value first, no strings', 'Free gift followed by pressure'),
    ('Commitment', 'A small first step they want', 'Tiny agreements leading to a big trap'),
    ('Social proof', 'Real numbers, real people, with permission', 'Fake reviews, fake viewers, paid crowds'),
    ('Authority', 'Real, relevant credentials and evidence', 'Uniforms, titles or logos without proof'),
    ('Liking', 'Genuine friendliness, real common ground', 'Sudden flattery from strangers'),
    ('Scarcity', 'Real deadlines and limits', 'Countdown timers, "only today", "last piece"'),
    ('Unity', 'Real shared identity', '"Trust me, we\'re from the same community" plus money'),
])}

**Spot it on you:** when you feel a sudden urge to say yes, ask: "Which principle is working on me right now? Is it true? Would I still say yes tomorrow?"
""",
    resources=[
        ('wp-cialdini', 'Read the summary of the principles', '5 minutes'),
        ('os-12', 'Read 12.3 Attitudes and Persuasion, and the compliance part of 12.4', '25 minutes'),
        ('darkpatterns', 'Read the list of 13 dark patterns: notice which principle each abuses', '10 minutes'),
    ],
    steps=[
        'For three days, notice influence attempts on you (ads, shops, WhatsApp, relatives). Log at least seven, naming the principle and whether it was honest or manipulative.',
        'Pick one real request you need to make (a discount, help, a favour, a sale) and plan which principles you can use honestly.',
        'Run the ethics test on your plan.',
        'Write one sentence for each principle about how you will use it honestly in your life.',
    ],
    proof='Seven logged influence attempts with principles and verdicts, your request plan with the ethics test, and seven honest-use sentences.',
    templates=[('Influence spotting log', """INFLUENCE SPOTTING LOG
Date | Where (ad / shop / message / person) | What they did or said | Principle(s) | True? | Honest or manipulative? | My response
ETHICS TEST for my own request: True? __ Good for them? __ Easy to say no? __ Fine if they saw my notes? __""", '')],
    mistakes=[
        ('Thinking influence is always bad.', 'Honest influence helps people make good choices: teachers, doctors and good salespeople use it.'),
        ('Quoting the hotel-towel study as proof.', 'Its replications were mixed. Social norms work modestly in many settings, not always.'),
        ('Using principles without the ethics test.', 'True, good for both, easy to refuse, comfortable if seen. All four.'),
        ('Believing you are immune.', 'Everyone responds to these principles; the defence is noticing and pausing.'),
    ],
    quiz=[
        Q('Which principle did Cialdini add in 2016?', 'Unity', 'Reciprocity', 'Scarcity', 'Authority', why='Unity: being influenced by people we see as "one of us".'),
        Q('What do meta-analyses say about foot-in-the-door?', 'The effect is real but small and variable', 'It always doubles compliance', 'It has no effect', 'It only works on children', why='Small average effects.'),
        Q('Which is an honest use of scarcity?', 'Telling customers about a real deadline', 'A countdown timer that resets', '"Only 2 left!" when there are 50', 'Fake "500 people viewing"', why='Scarcity is honest only when true.'),
        Q('What is the best defence when you feel a sudden urge to say yes?', 'Name the principle at work, check if it is true, and wait until tomorrow if possible', 'Say yes quickly', 'Trust the seller', 'Ask the seller if it is true', why='Noticing and pausing gives System 2 a chance.'),
    ],
    study='read the lesson and OpenStax 12.3',
    action='log seven influence attempts on you and plan one honest request with the ethics test',
)

L2 = lesson(
    28, 2,
    outcome='You can reframe a message honestly (gain and loss frames, concrete numbers), and run the persuasion lab: rewrite a real request, use it, and record the result.',
    split='20 minutes reading, 40 minutes for the lab',
    principle='How you present the same facts changes how people decide; frame honestly, make it easy to understand and easy to say yes or no, and test your request in real life.',
    science=f"""
**Framing.** Amos Tversky and Daniel Kahneman's "Asian disease problem" (1981) gave people two equivalent choices described either in terms of **lives saved** or **lives lost**. People preferred the sure option when it was framed as a gain ("200 people will be saved") and the risky option when it was framed as a loss ("400 people will die"), although the outcomes were identical. This framing effect replicated in the large Many Labs project. Everyday examples: "90% fat-free" sounds better than "10% fat"; "95% success rate" sounds better than "1 in 20 fails".

**Gain or loss frames for persuasion.** Health research has tested whether messages work better framed as gains ("Exercise gives you more energy") or losses ("Not exercising raises your risk"). Meta-analyses (for example, by Daniel O'Keefe and Jakob Jensen) found the differences are usually **small**; loss frames sometimes help for detection behaviours (screening), gain frames sometimes for prevention, but results vary. The honest lesson: **framing matters, but the facts and the offer matter more.**

**Making it easy.** Behavioural-science units such as the UK's Behavioural Insights Team summarised what helps people act as "EAST": make it **Easy**, **Attractive**, **Social** and **Timely**. Removing small hassles (a form already filled in, a clear next step, a reminder at the right time) often changes behaviour more than better arguments. Richard Thaler and Cass Sunstein's *Nudge* describes this "choice architecture"; a 2022 meta-analysis of nudges found an average effect that shrank substantially after correcting for publication bias, so nudges help modestly, not magically.

**Concrete beats abstract.** "You'll save about ₹600 a month" is clearer than "significant savings". "One hour, Saturday at 3 pm, at the library" is clearer than "sometime". Specific requests are easier to say yes to.

**The persuasion lab.** You will take a real request, rewrite it using honest principles and framing, run the ethics test, use it, and record the result. One request is not a scientific test (you can't compare with the old version on the same person), so treat it as practice with feedback; doing two or three such requests gives a better picture.
""",
    evidence=[
        ('Framing effects on choices', 'strong', 'Replicated, including in large multi-lab projects.'),
        ('Gain versus loss frames for persuasion', 'mixed', 'Differences are usually small and depend on the behaviour.'),
        ('Making actions easy changes behaviour', 'moderate', 'Many field studies; nudge effects modest after bias correction.'),
        ('Specific, concrete requests are easier to accept', 'moderate', 'Consistent with implementation-intention and compliance research.'),
    ],
    example=f"""
Sreeja wants her ward member to arrange evening lighting at the panchayat library so aspirants can study until 8 pm.

**Old request (a WhatsApp message):** "Sir, please do something about the library light, it's a big problem for students."

**Persuasion-lab rewrite:**
"Namaskaram sir. I'm Sreeja from the 6th ward, preparing for the LGS exam (**unity**: local). Eleven of us study at the library every evening (**social proof**, real number). After 6:30 the reading room is too dark, so we leave by 6:45 and lose about 1.5 hours of study a day (**concrete**, loss framed honestly). The librarian says two LED tube lights near the tables would be enough (**easy**, a specific fix). Could this be included in the next maintenance work? I can collect the students' signatures if that would help (**commitment**: an easy next step; **reciprocity**: offering help). Thank you, sir."

**Ethics test:** all true; good for students and the panchayat; easy for him to say no. **Result:** the ward member replies the same day, asks for the signatures, and the lights are installed three weeks later. She records the result in her lab sheet: what worked (specific fix, real numbers) and what she'd change (attach a photo of the dark room).
""",
    apply=f"""
**Reframe honestly:**
- Use **concrete numbers** and specifics (time, place, amount).
- Choose the frame that is **clearest and true**: what they gain, or what they avoid losing.
- **Make it easy:** one clear next step; remove hassles; time the request well (not when they are busy or upset).

**The persuasion lab:**
{fence(tools.PERSUASION_LAB)}

**Requests to try in the lab:** asking an employer or client for a better rate, asking a shop to stock something, asking your ward member or a local office for a small fix, asking a family member to support a new routine, inviting people to your talk (PD-M27-L03), pitching a small service to a local business.

**With others:** teach the ethics test to friends who sell (insurance, MLM, online businesses); it protects both them and their customers.
""",
    resources=[
        ('os-12', 'Re-read 12.3 on central and peripheral routes to persuasion', '10 minutes'),
        ('wp-loss', 'Re-read the framing link in the loss aversion article', '5 minutes'),
        ('ggsc', 'Search for an article on "nudge" or "behavioural science" for good causes and read one', '10 minutes'),
    ],
    steps=[
        'Choose one real request that matters to you this week.',
        'Fill in the persuasion lab: original version, what they gain, principles used truthfully, rewritten request (under 60 words) and the ethics test.',
        'Make the request (in person, by message or by phone).',
        'Record the result and what you learned. If possible, repeat with a second request.',
    ],
    proof='Your completed persuasion-lab sheet (original, rewrite, ethics test, result, lesson) for at least one real request.',
    templates=[('Persuasion lab', tools.PERSUASION_LAB, '')],
    mistakes=[
        ('Framing that misleads.', 'If the frame hides important facts, it is manipulation. Frame clearly and truthfully.'),
        ('Long requests.', 'Under 60 words, one clear ask, one easy next step.'),
        ('Pressing after a no.', 'Accept it; ask if there is a better time or person, once.'),
        ('Judging the technique on one request.', 'Do several and look at the pattern.'),
    ],
    quiz=[
        Q('What did the "Asian disease problem" show?', 'The same outcomes framed as gains or losses lead to different choices', 'Diseases spread faster in Asia', 'People always choose the risky option', 'Framing has no effect', why='Tversky and Kahneman\'s framing effect, which replicated.'),
        Q('What do meta-analyses say about gain versus loss frames in health messages?', 'Differences are usually small and depend on the behaviour', 'Loss frames always win', 'Gain frames always win', 'Framing doubles behaviour change', why='O\'Keefe and Jensen found small, variable differences.'),
        Q('What does EAST stand for?', 'Easy, Attractive, Social, Timely', 'Early, Accurate, Simple, True', 'Ethical, Active, Specific, Tested', 'Emotional, Authoritative, Scarce, Trusted', why='A summary of what helps people act.'),
        Q('Which request is easiest to say yes to?', '"Could we meet for one hour on Saturday at 3 pm at the library?"', '"Let\'s meet sometime."', '"You should help more."', '"Can you do something about it?"', why='Specific and easy.'),
    ],
    study='read the lesson and re-read OpenStax 12.3 on persuasion routes',
    action='run the persuasion lab on at least one real request and record the result',
)

LESSONS = [L1, L2]

MODULE = module(
    28,
    overview=f"""
Influence and persuasion, used honestly: Cialdini's seven principles (reciprocity, commitment and consistency, social proof, authority, liking, scarcity, unity) with honest evidence for each, framing and "make it easy" design, an ethics test, and a persuasion lab on a real request.

Influence is part of every request, sale, campaign and family discussion. This module teaches it for **honest, mutually beneficial use only**: every claim true, every deal good for both, every no easy to say. The same principles are what scammers and high-pressure sellers abuse, so learning them is also your first defence (Module 32).

Sales skills in a business context are covered in {xref('ent', 'ent-m07', 'the Entrepreneurship sales module')}; marketing in {xref('smm', 'smm-m05', 'the Social Media Marketing copywriting module')}.
""",
    outcomes=[
        'Explain the seven principles of influence and the strength of evidence for each.',
        'Apply the four-question ethics test.',
        'Frame messages honestly with concrete details and make actions easy.',
        'Spot influence principles being used on you.',
        'Run the persuasion lab on a real request.',
    ],
    lessons=LESSONS,
    project='the persuasion lab',
    project_steps=[
        'Complete the influence spotting log (PD-M28-L01).',
        'Run the persuasion lab on two real requests (PD-M28-L02).',
        'Write a half-page reflection: which honest principles worked, what you would change, and one situation where you resisted a principle used on you.',
        'Add the ethics test to your Playbook.',
    ],
    project_proof='The spotting log, two persuasion-lab sheets with results and your reflection.',
    rubric=[
        ('Knowledge', 'Names fewer than four principles', 'Names all seven', 'Explains all seven with evidence strength'),
        ('Ethics', 'No ethics test', 'Test done loosely', 'All four ethics questions answered for every request'),
        ('Lab', 'No real request', 'One request', 'Two real requests with results and lessons'),
        ('Defence', 'Doesn\'t notice influence on self', 'Notices some', 'Logs and resists manipulative attempts'),
    ],
    short=[
        'Learn the ethics test and use it on one request.',
        'Name the principle in two ads you see this week.',
    ],
    flashcards=[
        ('Seven principles', 'Reciprocity, commitment/consistency, social proof, authority, liking, scarcity, unity.'),
        ('Ethics test', 'True? Good for them? Easy to say no? Fine if they saw my notes?'),
        ('Foot-in-the-door evidence', 'Real but small.'),
        ('Hotel-towel social-proof study', 'Mixed replications.'),
        ('Framing effect', 'Same facts, gain versus loss wording, different choices; replicated.'),
        ('EAST', 'Easy, Attractive, Social, Timely.'),
        ('Unity', 'Influence from shared identity ("one of us").'),
        ('Defence against pressure', 'Name the principle, check if true, wait a day.'),
    ],
    mistakes=[
        ('Treating principles as tricks.', 'They work best, and only ethically, when true.'),
        ('Overclaiming effect sizes.', 'Most effects are modest; the offer itself matters most.'),
        ('Forgetting the other person\'s interest.', 'Mutual benefit is the test of honest influence.'),
    ],
    tools=[
        'The influence spotting log and honest-use table (PD-M28-L01).',
        'The persuasion lab (PD-M28-L02).',
    ],
    playbook=[
        'Influence code: only true, only mutual benefit, always easy to say no, fine if they saw my notes.',
        'When I feel a sudden urge to say yes: name the principle, check it, wait a day.',
    ],
)
