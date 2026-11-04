from common import lesson, module, link, xref, table, fence, Q
import tools

L1 = lesson(
    30, 1,
    outcome='You can explain the Asch, Milgram and Stanford prison studies accurately, including their criticisms, and keep field notes on conformity and social proof in daily life.',
    split='25 minutes reading, 25 minutes of field notes over a week',
    principle='Groups and authorities pull us to go along, often more than we expect; but the famous experiments are more complicated than the legends, and one dissenting voice makes a big difference.',
    science=f"""
**Asch's conformity studies (1951 onwards).** Solomon Asch asked students to match the length of a line to one of three comparison lines, an easy task with obvious answers. In each group, all but one person were actors who gave the **same wrong answer** on certain trials. About **one in three** of the real participants' answers on those trials went along with the wrong majority, compared with under 1% errors when people judged alone; **about three-quarters** conformed at least once. When **one other person** gave the right answer, conformity dropped dramatically (to around 5% of answers) ({link('wp-asch', 'summary')}). Later research found conformity varies by culture (a 1996 meta-analysis by Rod Bond and Peter Smith found higher conformity in more collectivist cultures) and by time. Asch himself emphasised that most answers stayed independent.

**Milgram's obedience studies (1961 onwards).** At Yale, Stanley Milgram told participants they were helping a study on learning: they had to give increasing electric shocks to a "learner" (an actor; no real shocks) for wrong answers. In the best-known version, **all** participants continued to 300 volts and **65%** went to the maximum 450 volts, despite the learner's protests. Obedience fell when the learner was closer (40% when in the same room, 30% when participants had to press his hand onto a shock plate) and when orders came by phone (about 21%). **Criticisms:** Gina Perry's archive research (2012) found that Milgram's published descriptions did not always match what happened, and that only about half of participants fully believed the shocks were real; analyses by Alex Haslam, Stephen Reicher and colleagues found participants responded less to direct orders ("You have no other choice") than to appeals to science, suggesting people continued partly because they **identified with the research goal**, not from blind obedience. Jerry Burger's partial replication (2009), stopping at 150 volts for ethical reasons, found rates similar to Milgram's ({link('wp-milgram', 'summary')}). These studies would not be allowed today; they caused real distress.

**The Stanford prison experiment (1971).** Philip Zimbardo assigned 24 male students to be "guards" or "prisoners" in a mock prison; it was stopped after six days because guards became abusive. It became a famous story about how situations turn good people bad. **Criticisms are serious:** Thibault Le Texier (2018, 2019) showed guards were coached towards harshness; participants may have played the roles they thought were wanted (demand characteristics); the advertisement may have attracted particular people; and it was never a controlled experiment. Many psychologists now treat it as a **demonstration, not evidence** ({link('wp-spe', 'summary')}).

**What holds up:** people often conform and obey more than they predict; social roles, group pressure and authority matter; but people also resist, especially with **allies**, when they can **see the harm**, and when they **don't identify** with the authority's goals.

**Social proof in daily life** (PD-M28-L01): queues attract more people, busy restaurants seem better, WhatsApp forwards with "already shared by 1,000 people" spread faster.
""",
    evidence=[
        ('People conform to group answers more than expected (Asch)', 'strong', 'Replicated many times; varies by culture and time.'),
        ('One dissenter greatly reduces conformity', 'strong', 'Found in Asch\'s variations and later studies.'),
        ('Many people obey harmful orders from authority (Milgram)', 'moderate', 'Partial replications agree; interpretation and methods are debated.'),
        ('Stanford prison experiment shows situations make people cruel', 'failed', 'Serious methodological criticisms; best seen as a demonstration, not evidence.'),
        ('Identification with leaders\' goals explains much obedience', 'moderate', 'Supported by re-analyses and newer studies.'),
    ],
    example=f"""
Sreeja keeps field notes for a week:
- **Tea shop:** a new tea stall has a crowd; three people say they joined "because it looked popular" (**social proof**).
- **Family WhatsApp group:** a forward about a "miracle cure for diabetes" gets 12 thumbs-up; her uncle, a diabetic, says he'll try it. Nobody questions it, until Sreeja writes, "Let's ask the doctor first." Two others then agree (**one dissenter** frees others).
- **Exam hall:** at a mock test, one person stands up to leave early; within five minutes ten more leave, though time remains (**conformity**).
- **Office counter:** a man in a uniform-like shirt tells the queue to move to another counter; everyone does, though he turns out to be a fellow applicant (**authority** cues).

She notices she conformed twice herself: she laughed at a joke she found mean, and agreed in a group that a mock was "impossible" when she found it fine. She writes: "One ally changes everything. I can be that ally."
""",
    apply=f"""
**Resisting harmful conformity and obedience:**
1. **Notice the pull:** "Am I agreeing because I think it's right, or because everyone else is?"
2. **Find or be one ally:** a single dissenter breaks the pressure for others. Speak first, calmly: "I see it differently."
3. **Check authority:** "Is this person really an authority on this? Is the request legitimate? Can I verify it?" (Scammers depend on fake authority: Module 32.)
4. **Make harm visible:** ask "Who could be hurt by this?"
5. **Delay:** "Let me think about it" breaks the momentum.

**Field observation notes (one week):**
{fence(tools.FIELD_NOTES)}

**With others:** when you lead (Module 30 L3), invite dissent explicitly: "What are we missing? Who disagrees?" It protects the group.
""",
    resources=[
        ('wp-asch', 'Read the article, including the variations', '15 minutes'),
        ('wp-milgram', 'Read the results, variations and criticism sections', '20 minutes'),
        ('wp-spe', 'Read the criticism section', '10 minutes'),
        ('os-12', 'Read 12.4 Conformity, Compliance, and Obedience', '25 minutes'),
    ],
    steps=[
        'Keep field observation notes for one week: at least six observations of social proof, conformity, authority or bystander behaviour.',
        'Note at least two times you conformed yourself, and what you would do differently.',
        'Once, be the "one ally" in a group: calmly give a different view or a correct fact. Note what happened.',
        'Explain one of the three classic studies, including its criticisms, to a friend in five minutes.',
    ],
    proof='Your week of field notes (six or more), two self-conformity notes, one "ally" note and a two-line summary of the study you explained.',
    templates=[('Field notes', tools.FIELD_NOTES, '')],
    mistakes=[
        ('Repeating the Stanford prison experiment as proof.', 'Its methods were seriously flawed; describe it as a demonstration with major criticisms.'),
        ('Saying "65% of people would torture on command".', 'The Milgram results are real but complex; belief in the shocks and identification with science mattered.'),
        ('Thinking conformity is always bad.', 'Following good norms (queuing, safety rules) is useful. The question is whether the norm is right.'),
        ('Staying silent when something is wrong.', 'One calm dissenter changes groups.'),
    ],
    quiz=[
        Q('In Asch\'s studies, what happened when one other person gave the right answer?', 'Conformity dropped dramatically', 'Conformity increased', 'Nothing changed', 'Everyone left', why='One ally breaks group pressure.'),
        Q('Which criticism applies to Milgram\'s studies?', 'Many participants may not have fully believed the shocks were real, and published accounts didn\'t always match the archives', 'No one obeyed at all', 'They were done on animals', 'They were never published', why='Gina Perry\'s archive research.'),
        Q('What is the best description of the Stanford prison experiment today?', 'A demonstration with serious methodological flaws, not strong evidence', 'Definitive proof that situations make people cruel', 'A large randomised trial', 'A fake study that never happened', why='Guards were coached; demand characteristics; no controls.'),
        Q('What reduced obedience in Milgram\'s variations?', 'Being closer to the learner and orders given by phone', 'Higher pay', 'Wearing uniforms', 'Louder instructions', why='Proximity to harm and distance from authority lowered obedience.'),
    ],
    study='read the lesson and the three Wikipedia articles',
    action='keep a week of field notes, note your own conformity twice and be "one ally" once',
)

L2 = lesson(
    30, 2,
    outcome='You can recognise groupthink, social loafing and the bystander effect, explain what the research really shows, and use counter-moves in groups and emergencies.',
    split='20 minutes reading, 25 minutes of tasks',
    principle='Groups can decide badly when nobody voices doubts, slack off when effort is invisible, and hesitate in emergencies; clear roles, invited dissent and direct requests fix much of this, and real bystanders help more often than the myth says.',
    science=f"""
**Groupthink.** Irving Janis (1972) coined "groupthink" for cohesive groups that make poor decisions because members suppress doubts to keep harmony, believe the group can't be wrong, and shield the leader from bad news. His examples included the US Bay of Pigs invasion. **Evidence:** case studies are vivid, but controlled tests of the full groupthink model have given **mixed** support; researchers agree more on the parts: **directive leaders**, **pressure for agreement** and **no process for dissent** do lead to worse group decisions. Counter-moves with support: ask for independent opinions **before** discussion, appoint a **devil's advocate**, run a **pre-mortem** (PD-M04-L02), and have the leader speak last.

**Social loafing.** Max Ringelmann observed in the 1880s and 1910s that people pulling a rope in a group pulled less hard per person than alone. Bibb Latané and colleagues found the same for clapping and shouting. A 1993 meta-analysis by Steven Karau and Kipling Williams (78 studies) confirmed social loafing is **reliable**, and smaller when individual contributions are **identifiable**, the task is **meaningful**, the group is **small** and members **value** the group. Study groups and family chores suffer from it.

**The bystander effect.** In the 1964 Kitty Genovese case in New York, the New York Times reported that 38 witnesses watched a murder and did nothing; later investigations found this **grossly exaggerated**: there were far fewer eyewitnesses, many only heard noises, and at least one called the police (the Times acknowledged this in 2016). John Darley and Bibb Latané's lab studies (1968) did find that people were **slower and less likely** to help when others were present: diffusion of responsibility ("someone else will act"), uncertainty ("is it an emergency?") and fear of embarrassment. But a 2019–2020 study by Richard Philpot and colleagues of **over 200 real CCTV-recorded public conflicts** in the UK, the Netherlands and South Africa found that **in over 90%** someone intervened, and the **more bystanders, the more likely** someone helped ({link('wp-bystander', 'summary')}). The honest view: the lab effect is real for individuals, but in real groups help is the norm.

**What helps in emergencies:** be the one who acts: **notice**, **decide it's an emergency**, **take responsibility**, **know what to do**, **act**. Point at a specific person: "You in the blue shirt, call 112!" (direct requests beat general calls). Learn basic first aid and CPR if you can (local hospitals, the Red Cross or NSS units sometimes run courses).
""",
    evidence=[
        ('Groupthink as a full model', 'mixed', 'Vivid case studies; controlled tests give mixed support.'),
        ('Directive leadership and no dissent process worsen group decisions', 'moderate', 'Supported by group-decision research.'),
        ('Social loafing', 'strong', 'Meta-analysis of 78 studies; reduced by identifiability and meaningful tasks.'),
        ('Bystander effect in lab studies', 'moderate', 'Classic studies; individual likelihood of helping drops with more bystanders.'),
        ('Real-world bystanders usually help', 'moderate', 'CCTV study of 200+ incidents: help in over 90%.'),
        ('Kitty Genovese "38 silent witnesses"', 'failed', 'The original report was grossly exaggerated.'),
    ],
    example="""
Joseph sir's study group of eight is choosing a mock-test series. The most senior member says, "Series X is clearly the best" in the first minute, and everyone agrees (**groupthink** risk). Joseph sir stops them: "Let's each write our choice and one doubt on paper first." Three people had doubts about X's outdated questions; they choose a cheaper, newer series.

In the same group, a shared notes project stalls: "everyone" is supposed to summarise topics, and nobody does (**social loafing**). He assigns each person two named topics with a date, and posts progress in the group chat (**identifiable contributions**). Within two weeks, 14 of 16 topics are done.

At the bus stand in Kuttiady, an elderly man collapses. People gather and look at each other. Ashiq, remembering the lesson, says: "Chetta in the white shirt, please call 108 (ambulance) now. You, please bring water. I'll check if he's breathing." Three people move at once.
""",
    apply="""
**In group decisions (study groups, family, committees):**
1. **Independent first:** everyone writes their view before discussion.
2. **Leader speaks last.**
3. **Devil's advocate:** one person argues the other side, on rotation.
4. **Pre-mortem** for big decisions.

**Against social loafing:**
1. **Named tasks, deadlines and visible progress.**
2. **Small groups** (3 to 6).
3. **Meaningful goals:** say why it matters.

**In emergencies (the five steps):**
1. Notice. 2. Decide it may be an emergency (better safe). 3. Take responsibility: "I'll act." 4. Know what to do: call **112** (all emergencies) or **108** (ambulance in Kerala), check safety, check breathing. 5. Act, and **give specific people specific jobs**.

**Online:** when someone is bullied or a false forward spreads in a group, be the first to say something calm. Others often follow.
""",
    resources=[
        ('wp-bystander', 'Read the sections on Kitty Genovese and the CCTV study', '15 minutes'),
        ('os-12', 'Read 12.7 Prosocial Behavior (the bystander part) and re-read 12.4 on groupthink and social loafing', '20 minutes'),
        ('klein', 'Re-read the premortem steps for use in groups', '5 minutes'),
    ],
    steps=[
        'In one real group decision (study group, family, friends), use "independent first" and "leader last". Note what changed.',
        'In one shared task, give named jobs with deadlines and visible progress. Note the result after a week.',
        'Write your emergency plan: the numbers (112, 108), the five steps and the exact words you will use to give people jobs.',
        'Find out where you could learn basic first aid or CPR locally (hospital, Red Cross, NSS, Kudumbashree or panchayat programmes) and note it.',
    ],
    proof='Notes on one group decision and one shared task, your emergency plan with exact words, and a note on a first-aid training option.',
    templates=[('Group tools and emergency card', """GROUP DECISION
Question: ______  Independent views written first? Y/N  Leader spoke last? Y/N
Devil's advocate: ______  Pre-mortem risks: ______  Decision: ______
SHARED TASK (anti-loafing)
Task | Person | Deadline | Done? (posted in group)
EMERGENCY CARD
112 (all emergencies) | 108 (ambulance, Kerala) | ______ (local hospital)
1 Notice 2 Decide it may be an emergency 3 "I'll act" 4 Know what to do 5 Act
Words: "You in the ______ shirt, call 108 now. You, bring ______. I'll ______." """, '')],
    mistakes=[
        ('Agreeing quickly to keep harmony.', 'Write views first; disagreement early is cheaper than failure later.'),
        ('"Everyone do a bit" tasks.', 'Name people, tasks and dates.'),
        ('Assuming someone else will help.', 'Act, and give specific people specific jobs.'),
        ('Repeating the "38 witnesses" story.', 'It was exaggerated; real bystanders usually help.'),
    ],
    quiz=[
        Q('Which counter-move best reduces groupthink?', 'Asking everyone for independent views before discussion, with the leader speaking last', 'Letting the leader decide first', 'Voting by show of hands immediately', 'Avoiding all disagreement', why='Independent views and invited dissent counter pressure for agreement.'),
        Q('When is social loafing reduced?', 'When individual contributions are identifiable and the task is meaningful', 'When groups are very large', 'When nobody checks progress', 'When tasks are boring', why='Karau and Williams\' meta-analysis.'),
        Q('What did the CCTV study of real public conflicts find?', 'Someone intervened in over 90% of cases, more often with more bystanders', 'Nobody ever helped', 'Help fell to zero in groups', 'Only police helped', why='Philpot and colleagues\' findings.'),
        Q('What is the best way to get help in an emergency crowd?', 'Give specific people specific jobs ("You in the blue shirt, call 108")', 'Shout "Someone help!"', 'Wait for others', 'Film it', why='Direct requests overcome diffusion of responsibility.'),
    ],
    study='read the lesson and the bystander article',
    action='use group-decision and anti-loafing tools in real groups and write your emergency plan',
)

L3 = lesson(
    30, 3,
    outcome='You can explain what builds trust, lead a small group task using evidence-based basics (clear goals, psychological safety, recognition), and get feedback on your leadership.',
    split='20 minutes reading, 40 minutes including leading a task',
    principle='People trust leaders who are competent, honest and caring, and who keep promises; good small-group leadership means a clear goal, roles, a safe place to speak up, and credit for others.',
    science=f"""
**What builds trust.** Roger Mayer, James Davis and David Schoorman's widely used model (1995) says we trust people based on three things: **ability** (can they do it?), **benevolence** (do they care about me?) and **integrity** (do they keep to principles I accept, and keep promises?). These map onto warmth and competence (PD-M24-L01). Trust builds slowly through **kept promises** and breaks quickly with one betrayal (negativity bias). Some popular claims about trust are weaker: research claiming that sniffing the hormone oxytocin increases trust (2005) **failed to replicate** in later, larger studies.

**Psychological safety.** Amy Edmondson's research on hospital and work teams found that the best teams **reported more errors**, not because they made more, but because members felt safe to admit them. She called this **psychological safety**: a shared belief that it's safe to speak up, ask questions and admit mistakes. Google's internal "Project Aristotle" study of its own teams reported psychological safety as the most important factor in team effectiveness (a company study, not peer-reviewed). Research across many organisations supports a link between psychological safety and learning and performance.

**What good leaders do (small groups):**
- **Clear goal and roles:** goal-setting research (PD-M06-L02) applies to teams.
- **Support autonomy, competence and relatedness** (self-determination theory, Module 6): involve people in decisions, help them grow, care about them.
- **Recognition:** specific, sincere credit (PD-M25-L03), in public.
- **Fairness:** research on **procedural justice** (Tom Tyler and others) finds people accept decisions more when the process is fair, transparent and they had a voice, even if the result isn't what they wanted.
- **Model the behaviour:** admit your own mistakes first; it makes it safe for others.

**Leadership styles.** Research on "transformational leadership" (inspiring with a vision, caring for individuals, stimulating thinking) links it with better follower motivation and performance, though the measures overlap and some researchers criticise the concept as vague. Simpler, well-supported points: listen, be fair, be clear, keep promises.

**Leading without a title.** Most leadership is informal: organising a study group, a clean-up drive, a family event or a Kudumbashree activity. The same principles apply.
""",
    evidence=[
        ('Trust based on ability, benevolence and integrity', 'moderate', 'Widely used model with good research support.'),
        ('Oxytocin increases trust', 'failed', 'The 2005 finding did not replicate in larger studies.'),
        ('Psychological safety supports team learning and performance', 'moderate', 'Supported across many organisations; Google\'s study was internal.'),
        ('Fair processes increase acceptance of decisions', 'strong', 'Procedural-justice research across many settings.'),
        ('Transformational leadership improves performance', 'mixed', 'Positive links, but concept and measurement are criticised.'),
    ],
    example="""
Ashiq volunteers to lead a Sunday clean-up of the Kuttiady river bank with eight young people from his ward.

**Clear goal and roles:** "Clear the 200 metres from the bridge to the temple steps by 10 am; separate plastic for the Haritha Karma Sena." He gives roles: two people for bags and gloves, two for sorting, four for collecting, one for photos (with permission).
**Psychological safety:** at the start he says, "If anything seems unsafe near the water, say so immediately; nobody will be blamed." When a younger boy admits he forgot the gloves, Ashiq thanks him for saying so early and sends someone to the shop.
**Fair voice:** he asks the group which section to start with; they choose.
**Recognition:** at the end, he thanks each person by name for something specific ("Ameen, your sorting made the Haritha handover easy").
**Integrity:** he promised tea and snacks; he brings them.

Afterwards he asks two people for feedback: "One thing I did well, one thing to change?" Answers: "clear roles"; "start 30 minutes earlier, before the sun gets hot". He notes both.
""",
    apply="""
**The small-group leadership checklist:**
1. **Goal:** one sentence: what, by when, how we'll know it's done.
2. **Roles:** who does what; matched to people's strengths where possible.
3. **Voice:** ask for ideas and concerns before deciding; leader speaks last on big choices.
4. **Safety:** say out loud that mistakes and concerns are welcome; thank people who raise them.
5. **Fairness:** explain how decisions are made; share tasks fairly; don't play favourites.
6. **Keep promises:** small ones especially.
7. **Recognition:** specific thanks by name, in public.
8. **Feedback on yourself:** ask "one thing I did well, one thing to change?"

**Building trust day to day:** do what you say you'll do (and say less if you can't); admit mistakes quickly; share credit; protect people's dignity in front of others.

**With others:** when you are not the leader, you can still increase psychological safety: ask the "silly" question, thank people who admit mistakes, and back up a quiet person's idea.
""",
    resources=[
        ('os-12', 'Re-read 12.4 and the group sections of 12.7, thinking as a leader', '15 minutes'),
        ('ggsc', 'Search the site for "psychological safety" or "trust" and read one article', '10 minutes'),
        ('meditations', 'Read the first book, where Marcus Aurelius lists what he learned from each person in his life about character and leadership', '20 minutes'),
    ],
    steps=[
        'Choose a small real group task you can lead this week or next: a study session, a clean-up, a family event, a club activity.',
        'Plan it with the leadership checklist.',
        'Lead it. Note what happened at each checklist step.',
        'Ask at least two people for "one thing I did well, one thing to change", and write a short reflection.',
    ],
    proof='Your leadership plan, notes on leading the task, two pieces of feedback and your reflection.',
    templates=[('Leadership plan', """SMALL-GROUP LEADERSHIP PLAN          Task: ______  Date: ______
Goal (what, by when, how we'll know): ______________________
Roles: ______ -> ______ ; ______ -> ______ ; ______ -> ______
Voice: question I'll ask the group before deciding: ______
Safety line I'll say: "If anything ______, say so; no blame."
Promises I'm making (and will keep): ______
Recognition: specific thanks for each person: ______
FEEDBACK: from ______: well ______ / change ______ ; from ______: well ______ / change ______""", '')],
    mistakes=[
        ('Doing everything yourself.', 'That is not leading. Give roles and trust people.'),
        ('Punishing people for admitting mistakes.', 'Then they hide them. Thank them for speaking up.'),
        ('Breaking small promises.', 'Trust is built and broken by small things.'),
        ('Believing "trust hormone" hacks.', 'The oxytocin-trust finding failed to replicate.'),
    ],
    quiz=[
        Q('What three things does the Mayer, Davis and Schoorman model say we trust people for?', 'Ability, benevolence and integrity', 'Wealth, age and height', 'Speed, luck and charm', 'Status, power and fame', why='A widely used model of trust.'),
        Q('What did Edmondson find about the best hospital teams?', 'They reported more errors because members felt safe to speak up', 'They made no errors', 'They hid errors better', 'They had no leaders', why='Psychological safety, not more mistakes.'),
        Q('Why do fair processes matter?', 'People accept decisions more when the process is fair and they had a voice', 'Fairness slows everything down', 'Only results matter', 'They don\'t matter', why='Procedural-justice research.'),
        Q('What happened to the finding that oxytocin increases trust?', 'It failed to replicate in larger studies', 'It was confirmed by many studies', 'It was never published', 'It applies only to leaders', why='A popular claim that did not hold up.'),
    ],
    study='read the lesson and the first book of Meditations',
    action='plan and lead a small real group task with the checklist, and collect two pieces of feedback',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    30,
    overview=f"""
Group psychology and leadership: conformity (Asch), obedience (Milgram) and the Stanford prison experiment explained honestly with their criticisms; groupthink, social loafing and the bystander effect (including what real CCTV studies show); trust, psychological safety, fairness and leading small groups. You keep field notes and lead a real group task.

Groups shape what we think and do more than we notice. The classic experiments are famous partly because they were dramatic; this module tells you what they really found, what is disputed, and what holds up, so you can resist harmful pressure and lead groups that decide well.

Leadership here means everyday leadership: a study group, a ward clean-up, a family event, a club. No title needed.
""",
    outcomes=[
        'Explain the Asch, Milgram and Stanford studies accurately, with criticisms.',
        'Resist harmful conformity and be "one ally".',
        'Recognise and counter groupthink and social loafing.',
        'Act effectively in emergencies, and explain what real bystander research shows.',
        'Build trust and lead a small group with clear goals, psychological safety and fairness.',
    ],
    lessons=LESSONS,
    project='field notes on conformity and a led group task',
    project_steps=[
        'Keep a week of field observation notes (PD-M30-L01).',
        'Use the group-decision and anti-loafing tools in a real group (PD-M30-L02).',
        'Plan and lead a small group task with the leadership checklist and collect feedback (PD-M30-L03).',
        'Write a half-page reflection and add your leadership checklist and emergency card to the Playbook.',
    ],
    project_proof='Your field notes, group-tool notes, leadership plan with feedback and your reflection.',
    rubric=[
        ('Classic studies', 'Repeats the legends', 'Knows some criticisms', 'Explains findings and criticisms accurately'),
        ('Observation', 'Fewer than three notes', 'Three to five', 'Six or more, including own conformity'),
        ('Group tools', 'Not used', 'Used once', 'Independent-first and named tasks used with results noted'),
        ('Leadership', 'Not done', 'Led without a plan', 'Planned, led and got feedback'),
    ],
    short=[
        'Be "one ally" once this week.',
        'Use "independent views first" in one group decision.',
    ],
    flashcards=[
        ('Asch: effect of one ally', 'Conformity drops dramatically.'),
        ('Milgram baseline', '65% to 450 V; lower when closer to the learner or orders by phone.'),
        ('Milgram criticisms', 'Not all believed the shocks; archives differ from accounts; identification with science mattered.'),
        ('Stanford prison experiment status', 'Seriously flawed: guards coached, demand characteristics; a demonstration, not evidence.'),
        ('Social loafing fix', 'Identifiable contributions, meaningful tasks, small groups.'),
        ('Real bystanders (CCTV study)', 'Someone helped in over 90% of conflicts.'),
        ('Emergency request', '"You in the blue shirt, call 108."'),
        ('Psychological safety', 'Safe to speak up and admit mistakes; linked to team learning.'),
        ('Trust model', 'Ability, benevolence, integrity.'),
    ],
    mistakes=[
        ('Treating classic studies as settled truths.', 'Know their criticisms.'),
        ('Leading by control.', 'Clear goals, voice and fairness work better.'),
        ('Waiting to be appointed.', 'Lead small things now.'),
    ],
    tools=[
        'Field observation notes (PD-M30-L01).',
        'Group decision tools, anti-loafing table and emergency card (PD-M30-L02).',
        'The small-group leadership plan (PD-M30-L03).',
    ],
    playbook=[
        'In groups: views first, leader last, invite dissent; named tasks and dates.',
        'In emergencies: I act and give specific people specific jobs (112, 108).',
        'Leading: clear goal, roles, voice, safety, fairness, kept promises, specific thanks.',
    ],
)
