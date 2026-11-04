from common import lesson, module, link, xref, table, fence, Q
import tools

L1 = lesson(
    26, 1,
    outcome='You can tell a short, clear story (in English or Malayalam) using a simple structure, to explain, persuade or connect.',
    split='20 minutes reading, 30 minutes of practice',
    principle='People remember and are moved by stories more than by lists of facts; a good short story has a person, a problem, a turning point and a point.',
    science="""
**Why stories work.** Psychologists Melanie Green and Timothy Brock described **narrative transportation**: when we are absorbed in a story, we are less likely to argue against its message and more likely to remember it. A 2014 meta-analysis by Tom van Laer and colleagues found that transportation was linked to changes in beliefs, attitudes and intentions. Research on memory supports the same idea: facts connected in a causal chain (this happened, *because* of that, *so* this) are easier to recall than isolated facts. Some popular claims, such as "stories are 22 times more memorable than facts", have no clear source and should not be repeated.

**The building blocks.** Most effective short stories, from folk tales to TED talks, share a simple shape:
1. **A person** the listener can picture (you, a friend, a customer).
2. **A situation and a problem** (what they wanted; what got in the way).
3. **A turning point** (a decision, a discovery, a change).
4. **An outcome** (what happened).
5. **The point** (what it means for the listener).

Concrete details (a place, a time, a sound, an exact sentence someone said) make stories vivid; too many details make them drag. Malayalam has a rich storytelling tradition, from Aithihyamala's legends to kathaprasangam performances; many of the same techniques (vivid characters, suspense, a moral) apply.

**Uses in daily life:**
- **Explaining:** "Let me tell you what happened when I first tried…" makes advice concrete.
- **Persuading:** a true story of one person helped by an idea often moves people more than statistics (but use both: a story to make it real, a number to show it is not a one-off).
- **Interviews:** answer "Tell me about a time…" questions with a short story (the STAR method, PD-M33-L02).
- **Connecting:** sharing a small personal story invites others to share (gradual self-disclosure, PD-M25-L01).

**Ethics.** Stories persuade partly because they lower critical thinking. That is why scams and ads use them (Module 32). Tell **true** stories, say when a story is an example rather than evidence, and never invent testimonials.
""",
    evidence=[
        ('Narrative transportation changes beliefs and attitudes', 'moderate', 'Supported by a meta-analysis of many studies.'),
        ('Causally connected information is easier to remember', 'moderate', 'Supported by memory research.'),
        ('"Stories are 22 times more memorable"', 'failed', 'No clear research source; don\'t repeat it.'),
        ('Person–problem–turning point–outcome–point structure', 'tool', 'A practical structure drawn from storytelling practice.'),
    ],
    example="""
Sreeja is asked at a residents' association meeting to encourage young people to use the panchayat library. Her first draft is a list: "The library has 4,000 books, free wifi, PSC guides, and it's open 9 to 7."

She rewrites it as a 60-second story:
"Last year, my friend Divya was studying for the LGS exam at home (**person**). Every evening her little brothers' cartoons were on, and she couldn't concentrate; her scores were stuck at 40 (**problem**). One day she came to the library just to escape the noise, and found the PSC rank files and a group of four aspirants who tested each other every Saturday (**turning point**). Three months later she was scoring 65, and she got into the rank list in February (**outcome**). The library has 4,000 books and free wifi, but what it really gave Divya was a quiet place and people on the same journey. It can do that for you too (**point**)."

Two parents come up afterwards to ask about the Saturday group.
""",
    apply=f"""
**The 60-second story template:**
{fence('''60-SECOND STORY            Purpose: explain / persuade / connect / interview
PERSON:        Who? (name, one detail)  ______________________
PROBLEM:       What did they want, and what got in the way? ______
TURNING POINT: What changed or what did they decide? ______________
OUTCOME:       What happened? (one concrete result) ______________
POINT:         What does it mean for the listener? (one sentence) ______
One vivid detail (a place, a sound, an exact quote): ______________
Check: true? short (about 60-90 s)? clear point? permission if it is someone else's story?''')}

**Practice method:**
1. Write the five parts in one line each.
2. Tell it aloud without reading; record it on your phone.
3. Listen back: cut anything that doesn't serve the point; add one vivid detail.
4. Tell it again, in English and then in Malayalam.

**Build a story bank:** five true stories from your life (a failure, a success, a kindness received, a lesson learned, a funny moment) that you can tell in 60 seconds. They will serve you in interviews, talks and friendships.

**With others:** ask people for their stories ("How did you get into this?"); it is one of the warmest questions you can ask.
""",
    resources=[
        ('ted-jiang', 'Re-watch the first three minutes and notice the story structure (person, problem, turning point)', '5 minutes'),
        ('os-12', 'Re-read the part of 12.3 on persuasion routes (central and peripheral)', '10 minutes'),
        ('smiles', 'Read any short biography story in chapter 4, "Application and Perseverance"; notice how it is told', '15 minutes'),
    ],
    steps=[
        'Write five true stories for your story bank using the template (one line per part).',
        'Record two of them as 60-second stories: one in English, one in Malayalam.',
        'Listen back, cut and add one vivid detail; record again.',
        'Tell one story to a real person in conversation and note their reaction.',
    ],
    proof='Your five-story bank, two pairs of recordings (first and improved versions) and a note on telling one story to a real person.',
    templates=[('Story bank', """STORY BANK (true stories, 60-90 seconds each)
1. A failure and what I learned: P ___ | Prob ___ | Turn ___ | Out ___ | Point ___
2. A success I worked for:       P ___ | Prob ___ | Turn ___ | Out ___ | Point ___
3. A kindness I received:        ...
4. A lesson that changed me:     ...
5. A funny moment:               ...
Recordings: file names ______ ______  Told to a real person: ______ (reaction ______)""", '')],
    mistakes=[
        ('Starting with background.', 'Start with the person and the problem; add background only if needed.'),
        ('No clear point.', 'End with one sentence that tells the listener why it matters.'),
        ('Inventing or exaggerating.', 'Tell true stories. Invented testimonials are deception.'),
        ('Using a story as proof.', 'A story shows something is possible; numbers show how common it is.'),
    ],
    quiz=[
        Q('What is "narrative transportation"?', 'Being absorbed in a story, which makes its message more persuasive and memorable', 'Travelling to tell stories', 'Reading quickly', 'Translating stories', why='Green and Brock\'s concept, supported by a meta-analysis.'),
        Q('Which is the right order for the 60-second story?', 'Person, problem, turning point, outcome, point', 'Point, background, facts, list, ending', 'Outcome, person, problem', 'Statistics, quote, joke', why='This shape keeps stories clear and short.'),
        Q('What is the honest status of "stories are 22 times more memorable than facts"?', 'No clear research source; don\'t repeat it', 'A proven figure', 'From a large meta-analysis', 'From the WHO', why='Popular but unsourced.'),
        Q('Why should you use a story and a number together when persuading?', 'The story makes it real; the number shows it is not a one-off', 'Numbers are always boring', 'Stories are always false', 'It makes the talk longer', why='Stories move, numbers generalise.'),
    ],
    study='read the lesson and notice the story structure in the Jia Jiang talk',
    action='build a five-story bank, record two stories in English and Malayalam, improve them, and tell one to a real person',
)

L2 = lesson(
    26, 2,
    outcome='You can make requests and refuse requests assertively (not passively or aggressively), say no without long excuses, and help others save face.',
    split='20 minutes reading, 30 minutes of practice',
    principle='Assertiveness means stating your needs and limits clearly and respectfully, while respecting the other person\'s; it protects relationships better than silent resentment or anger.',
    science="""
**Three styles.** Psychologists describe three broad ways of handling needs and conflicts:
- **Passive:** not saying what you need; agreeing to avoid conflict; resentment later. ("Okay, okay, I'll do it.")
- **Aggressive:** getting your way at others' expense; blaming, shouting, threatening. ("You always dump this on me!")
- **Assertive:** saying what you think, feel and need, clearly and calmly, while respecting the other person. ("I can't do it this week because of my exam. I can help next Saturday.")
A related pattern, **passive-aggressive**, means appearing to agree while resisting indirectly (sulking, "forgetting", sarcasm).

**Evidence.** Assertiveness training is a standard part of CBT and social-skills programmes. Studies, many small, find it can reduce anxiety and stress and improve self-esteem and relationships; it is often part of treatment for social anxiety and depression. The evidence is moderate and varies by programme.

**Saying no.** People often say yes because refusing feels awkward and they overestimate how much a no will damage the relationship (Vanessa Bohns's research on compliance, PD-M14-L02). Research by Vanessa Patrick and Henrik Hagtvedt (2012) found that people resisted temptations more effectively when they framed refusals as "I don't…" (a personal rule) rather than "I can't…"; later replications were mixed, so treat it as a tip, not a law.

**Face-saving.** Sociologist Erving Goffman described "face" as the positive image people want to keep in social interactions. In many Asian cultures, including India, losing face in front of others is especially painful. Penelope Brown and Stephen Levinson's **politeness theory** describes how people soften requests and refusals to protect each other's face. Assertiveness in Kerala works best when it is clear **and** face-saving: private rather than public, with respect for age and role, and with an offer or alternative where possible.

**Culture and family.** Saying no to elders, relatives and seniors is hard in Kerala culture. Assertiveness does not mean disrespect: you can be warm, use respectful forms of address, and still be clear about what you can and cannot do.
""",
    evidence=[
        ('Assertiveness training reduces anxiety and improves relationships', 'moderate', 'Many studies, often small; part of standard CBT and social-skills programmes.'),
        ('People overestimate the social cost of saying no', 'moderate', 'Supported by research on compliance and refusals.'),
        ('"I don\'t" refusals beat "I can\'t"', 'mixed', 'One influential study; mixed replications.'),
        ('Face-saving matters in conflict, especially in many Asian cultures', 'moderate', 'Supported by cross-cultural communication research.'),
    ],
    example="""
Anu's aunt calls: "Can you come and help with my daughter's engagement preparations? Three days, from tomorrow." The prelims are in nine days.

**Passive:** "Okay, Ammayi…" (then three days lost and resentment). **Aggressive:** "Why does everyone think I have nothing to do?" (hurt feelings, family gossip). **Assertive and face-saving:** "Ammayi, congratulations! I really want to help. My exam is on the 14th, so I can't come for three days. I can come on Saturday afternoon to help with the decorations, and I'll be there for the whole engagement day."

Her aunt is disappointed but says, "Good, study well; Saturday is fine." Anu notices her hands were shaking before the call and that the actual conversation took two minutes. She also helps her aunt save face with the rest of the family by telling her cousin, "Ammayi was so understanding about my exam."
""",
    apply=f"""
**The assertive request (DESC, shortened):**
- **Describe** the situation in neutral words: "The last two weeks, the study room has been used for guests in the evenings."
- **Express** how it affects you, using "I": "I've lost about six hours of study."
- **Specify** what you'd like: "Could we keep the room free from 7 to 9 on weekdays?"
- **Consequence / benefit:** "That way I can help with guests at the weekend."

**The assertive no (clear, kind, short):**
1. **Appreciate:** "Thanks for thinking of me."
2. **No, with a short reason (optional):** "I can't take this on this week; my exam is close." Avoid long excuses; they invite argument.
3. **Offer an alternative if you genuinely can:** "I can help on Saturday afternoon."
4. **Broken record if pressed:** repeat calmly: "I understand. I still can't this week."

**Face-saving:** refuse or criticise in private; acknowledge the other person's good intention; give them a way to agree without losing face ("I know you need it urgently; maybe Rahul is free this week?").

**Practice sentences (English and Malayalam):** write your own versions of "I can't this week, but I can on Saturday" in both languages, in the respectful form you would use with an elder.

**With others:** accept others' no's gracefully; it makes it easier for them to be honest with you.
""",
    resources=[
        ('ggsc', 'Search the site for "assertive" or "how to say no" and read one article', '10 minutes'),
        ('noba', 'Search for the module "Love, Friendship, and Social Support" and read the part on relationships and conflict', '15 minutes'),
        ('enchiridion', 'Read sections 33 and 34 on speaking little and well, and on handling pleasures and requests calmly', '10 minutes'),
    ],
    steps=[
        'Write three situations from the last month where you were passive or aggressive. For each, write an assertive version.',
        'Write your assertive "no" in English and Malayalam, in the respectful form you\'d use with an elder.',
        'Say no assertively to at least one real request this week (a small one is fine). Note the response.',
        'Make one assertive request using DESC. Note the response.',
    ],
    proof='Three rewrites (passive or aggressive to assertive), your no-script in both languages, and notes on one real no and one real request.',
    templates=[('No-script and DESC', """MY ASSERTIVE NO
English: "Thanks for asking. I can't ______ this week because ______.
          I can ______ instead." (If pressed: "I understand. I still can't.")
Malayalam (respectful form): "______________________________"
DESC REQUEST
Describe (neutral facts): ______________________
Express (I feel / it affects me): ______________________
Specify (what I'd like): ______________________
Consequence/benefit: ______________________
LOG: Date | Situation | Style I used (passive / aggressive / assertive) | Response""", '')],
    mistakes=[
        ('Long excuses.', 'Each excuse gives the other person something to argue with. Keep the reason short.'),
        ('Confusing assertive with aggressive.', 'Calm, respectful and clear, not loud or blaming.'),
        ('Refusing or criticising in public.', 'Do it privately to save face.'),
        ('Never giving in to anyone.', 'Assertiveness includes compromise; it is about honest negotiation, not winning.'),
    ],
    quiz=[
        Q('Which response is assertive?', '"I can\'t this week because of my exam. I can help on Saturday."', '"Okay, I\'ll do it." (then resentment)', '"Why do you always ask me?"', '"Sure!" (then not doing it)', why='Clear, respectful, with an alternative.'),
        Q('Why avoid long excuses when saying no?', 'They invite argument and make the no weaker', 'They are rude', 'They take too long to type', 'They are always lies', why='A short, clear reason is enough.'),
        Q('What is "face-saving" in conflict?', 'Helping the other person keep their dignity, for example by disagreeing in private', 'Washing your face', 'Hiding your real feelings always', 'Winning in public', why='Goffman\'s idea of "face", important in many Asian cultures.'),
        Q('What is the "broken record" technique?', 'Calmly repeating your position when pressed', 'Playing music to end the conversation', 'Changing your answer each time', 'Recording the conversation', why='It avoids getting drawn into arguments.'),
    ],
    study='read the lesson and one article on saying no',
    action='rewrite three past situations assertively, write your no-script in two languages, and use one real no and one real DESC request',
)

L3 = lesson(
    26, 3,
    outcome='You can use non-violent communication, give one piece of constructive feedback with a script, receive feedback without defensiveness, and prepare for a difficult conversation.',
    split='20 minutes reading, 40 minutes of preparation and practice',
    principle='Difficult conversations go better when you describe facts without judgement, share feelings and needs, make a clear request, and listen to the other side before defending yourself.',
    science=f"""
**Non-violent communication (NVC).** Psychologist Marshall Rosenberg developed NVC in the 1960s. It has four steps:
1. **Observation** without evaluation: "You arrived at 10:40 for our 10:00 study session" (not "You're always late").
2. **Feeling:** "I felt frustrated…"
3. **Need:** "…because I need our sessions to start on time to finish the mock."
4. **Request:** "Could you message me if you'll be more than 10 minutes late?"
NVC is widely used in mediation, schools and families. Research on it is limited: small studies suggest it can improve empathy and reduce conflict, but there are few rigorous trials. It is best treated as a **practical tool** that fits well-supported ideas (describing behaviour rather than character reduces defensiveness; "I" statements are heard as less hostile than "you" accusations in some studies).

**Giving feedback.** Feedback research (for example, a large 1996 review by Avraham Kluger and Angelo DeNisi) found that feedback improved performance on average, but in about **a third of cases it made performance worse**, especially when it focused on the person ("you're careless") rather than the task. The **SBI** model (Situation, Behaviour, Impact) from the Center for Creative Leadership is a practical way to keep feedback about the task. Asking for the other person's view and agreeing on next steps makes feedback a conversation, not a verdict.

**Receiving feedback and defensiveness.** Hearing criticism triggers a threat response (Module 11). Common defensive reactions: denying, explaining, counter-attacking, or collapsing ("I'm useless"). Douglas Stone and Sheila Heen (*Thanks for the Feedback*) suggest separating three things: **Is it right? What is it about? Who is saying it?** A simple approach: **listen, thank, ask for an example, take time, then decide** what to use. Good listening by the receiver also lowers defensiveness in the giver (PD-M25-L02).

**Difficult conversations.** Stone, Patton and Heen (*Difficult Conversations*, from the Harvard Negotiation Project) describe three layers in every hard conversation: **what happened** (each person's story), **feelings**, and **identity** (what it says about me). Preparing for all three, and opening with curiosity about the other person's story, helps more than preparing arguments.
""",
    evidence=[
        ('Describing behaviour rather than character reduces defensiveness', 'moderate', 'Consistent with feedback and conflict research.'),
        ('Feedback can make performance worse when person-focused', 'strong', 'Kluger and DeNisi\'s large review: about a third of effects were negative.'),
        ('NVC improves empathy and reduces conflict', 'mixed', 'Small studies; few rigorous trials. A practical tool.'),
        ('SBI feedback model', 'tool', 'Widely used practical model consistent with feedback research.'),
        ('Listening reduces defensiveness in conflicts', 'moderate', 'Supported by experiments on listening.'),
    ],
    example=f"""
Ashiq's study partner Rahul keeps sharing their group's mock-test answers in a public Telegram channel without asking, and some of Ashiq's own notes have appeared with Rahul's name.

Ashiq prepares with the feedback script. **Ask:** "Rahul, can I share something that's been bothering me?" **Situation and behaviour:** "In the last two weeks, three sets of my handwritten notes were posted in the Telegram channel under your name." **Impact:** "I felt upset, because I spent hours on them, and people in my village think I copied." **Their view:** "How did it look from your side?" (Ashiq listens: Rahul thought posting with his name was normal because he was the channel admin, and he didn't think Ashiq would mind.) **Request:** "Could you ask me before posting my notes, and put my name on them?" **Close:** "I really value studying with you."

Rahul apologises and edits the posts. The next week Rahul gives Ashiq feedback: "In mocks you rush the reasoning section." Ashiq's first urge is to explain; instead he says, "Thanks, can you show me one example?" They look at it together.
""",
    apply=f"""
**Give one piece of constructive feedback (this week) with the script:**
{fence(tools.FEEDBACK_SCRIPT)}

**NVC for personal conflicts:** Observation → Feeling → Need → Request. Replace "You never help at home" with "This week I cooked dinner five nights (observation). I'm exhausted (feeling) and need some rest before the exam (need). Could you cook on Tuesday and Thursday (request)?"

**Receive feedback without defensiveness:** listen to the end; say "Thank you"; ask "Can you give me an example?"; summarise; say "Let me think about it"; later decide what to use.

**Prepare for a difficult conversation:**
1. **What happened?** My story, their likely story, and what I don't know.
2. **Feelings:** mine and probably theirs.
3. **Identity:** what this means to me (and to them).
4. **Purpose:** what outcome is good for both of us?
5. **Opening line:** start with curiosity: "I'd like to understand how you see what happened with…"
6. **Time and place:** private, calm, not when either of you is tired or hungry.
""",
    resources=[
        ('ggsc', 'Search the site for "nonviolent communication" or "difficult conversations" and read one article', '15 minutes'),
        ('os-12', 'Read 12.6 Aggression: what escalates conflict and what calms it', '15 minutes'),
        ('meditations', 'Read the opening of the second book again: Marcus Aurelius preparing himself for difficult people', '5 minutes'),
    ],
    steps=[
        'Write one piece of constructive feedback you have been avoiding, using the feedback script.',
        'Give it in private this week. Note what you said, how they responded and what you agreed.',
        'Rewrite one personal complaint in NVC form (observation, feeling, need, request).',
        'Ask one person for feedback on something you do (your speaking, your notes, your cooking) and receive it with the five receiving steps. Note what you will use.',
    ],
    proof='Your written feedback script, a note on giving it (response and agreement), one NVC rewrite, and a note on feedback you received and what you will use.',
    templates=[('Difficult conversation planner', """DIFFICULT CONVERSATION PLANNER       With: ______  When/where: ______
1. What happened: my story ______ ; their likely story ______ ; unknowns ______
2. Feelings: mine ______ ; theirs (probably) ______
3. Identity: what it means to me ______ ; to them ______
4. Good outcome for both: ______________________
5. Opening line (curious): "I'd like to understand how you see ______."
6. NVC: Observation ______ Feeling ______ Need ______ Request ______
RECEIVING FEEDBACK: listen -> thank -> "an example?" -> summarise -> "let me think"
After: what we agreed ______ ; what I'll use ______""", '')],
    mistakes=[
        ('Feedback about the person.', '"You\'re careless" makes things worse. Describe the behaviour and its impact.'),
        ('Ambushing people in public.', 'Ask permission and talk in private.'),
        ('Defending yourself immediately.', 'Listen, thank, ask for an example, then decide.'),
        ('Using NVC as a script to win.', 'It works only with genuine curiosity about the other person\'s needs.'),
    ],
    quiz=[
        Q('Which is an NVC "observation"?', '"You arrived at 10:40 for our 10:00 session"', '"You\'re always late"', '"You don\'t respect me"', '"You\'re lazy"', why='An observation describes facts without evaluation.'),
        Q('What did Kluger and DeNisi\'s review find about feedback?', 'It usually helps, but about a third of the time it made performance worse', 'Feedback always helps', 'Feedback never helps', 'Only negative feedback works', why='Person-focused feedback is especially risky.'),
        Q('What are the parts of SBI feedback?', 'Situation, Behaviour, Impact', 'Speed, Balance, Intelligence', 'Smile, Blame, Ignore', 'Story, Background, Ideas', why='SBI keeps feedback about the task.'),
        Q('What is a good first response when you receive criticism?', 'Listen to the end and say thank you', 'Explain why they are wrong', 'Criticise them back', 'Leave the room', why='Listening and thanking lower defensiveness on both sides.'),
    ],
    study='read the lesson and one article on difficult conversations',
    action='give one real piece of constructive feedback with the script, write one NVC rewrite and receive one piece of feedback well',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    26,
    overview=f"""
Communication that works with real people: short stories that explain and persuade, assertiveness and saying no (with face-saving for Kerala family life), non-violent communication, giving and receiving feedback, and preparing for difficult conversations. You give one real piece of constructive feedback with a script.

Many relationship problems come from two failures: saying nothing (and resenting it) or saying it badly (and hurting people). This module gives you clear, respectful scripts for both directions: asking, refusing, criticising and being criticised.

Stories and scripts are tools for honesty. Using stories to deceive, or scripts to pressure, is manipulation (Module 32).
""",
    outcomes=[
        'Tell a 60-second story with a clear point, in English and Malayalam.',
        'Tell passive, aggressive and assertive responses apart and use assertive ones.',
        'Say no clearly and kindly, and help others save face.',
        'Use NVC and the SBI feedback script.',
        'Receive feedback without defensiveness and prepare for difficult conversations.',
    ],
    lessons=LESSONS,
    project='one real piece of constructive feedback, given with the script',
    project_steps=[
        'Prepare the feedback with the script and the difficult-conversation planner (PD-M26-L03).',
        'Give it in private and listen to the other person\'s view.',
        'Write what happened, what you agreed and what you would do differently.',
        'Add your no-script and feedback script to the Playbook.',
    ],
    project_proof='Your prepared script and planner, a note on the conversation and agreement, and your reflection.',
    rubric=[
        ('Stories', 'No story bank', 'Two or three stories', 'Five-story bank with recordings in both languages'),
        ('Assertiveness', 'Still mostly passive or aggressive', 'Some assertive responses', 'A real assertive no and a DESC request'),
        ('Feedback given', 'Not given', 'Given but person-focused', 'Given with SBI, in private, with their view heard'),
        ('Feedback received', 'Defended immediately', 'Listened but argued', 'Listened, thanked, asked for an example and used it'),
    ],
    short=[
        'Write your no-script and use it once.',
        'Give one small piece of SBI feedback (praise counts too).',
    ],
    flashcards=[
        ('Story structure', 'Person, problem, turning point, outcome, point.'),
        ('Narrative transportation', 'Absorption in a story increases its persuasive power.'),
        ('Assertive', 'Clear and respectful about your needs and theirs.'),
        ('Assertive no', 'Appreciate, no with a short reason, alternative if genuine, broken record if pressed.'),
        ('Face-saving', 'Helping others keep dignity: private, respectful, with a way out.'),
        ('NVC', 'Observation, Feeling, Need, Request.'),
        ('SBI', 'Situation, Behaviour, Impact.'),
        ('Receiving feedback', 'Listen, thank, ask for an example, summarise, decide later.'),
    ],
    mistakes=[
        ('Avoiding all hard conversations.', 'Small, early, private conversations prevent big blow-ups.'),
        ('Scripts read like robots.', 'Use the structure, in your own warm words.'),
        ('Ignoring culture and age.', 'Respectful forms of address and private settings matter in Kerala.'),
    ],
    tools=[
        'The 60-second story template and story bank (PD-M26-L01).',
        'The no-script and DESC request (PD-M26-L02).',
        'The feedback script and difficult-conversation planner (PD-M26-L03).',
    ],
    playbook=[
        'My no: "Thanks for asking. I can\'t ______ because ______. I can ______ instead."',
        'Feedback: private, Situation–Behaviour–Impact, their view, a request. Receiving: listen, thank, example, decide later.',
        'My five go-to stories: ______.',
    ],
)
