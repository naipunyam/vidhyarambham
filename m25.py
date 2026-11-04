from common import lesson, module, link, xref, table, fence, Q
import tools

L1 = lesson(
    25, 1,
    outcome='You can explain the main research findings on why people like each other (similarity, familiarity, reciprocity, self-disclosure and the liking gap) and use them honestly to build rapport.',
    split='20 minutes reading, 25 minutes of tasks',
    principle='We like people who are similar to us, whom we see often, who like us, and who open up to us step by step; and other people usually like us more than we think after a conversation.',
    science=f"""
**Similarity.** Donn Byrne's research from the 1960s found that people are attracted to others who share their attitudes and values; later work showed that **perceived** similarity (what we think we share) matters even more than actual similarity. Shared experiences (the same exam, the same hometown, the same struggles) create a sense of "us".

**Familiarity and proximity.** Robert Zajonc's **mere-exposure effect** (1968): people tend to like things and people more the more often they see them, at least at first and when the first impression is not negative. A classic study by Leon Festinger, Stanley Schachter and Kurt Back of a student housing complex found that people were most likely to become friends with neighbours whose doors were closest. Friendships grow from **repeated, low-pressure contact**: the same tea shop, the same bus, the same library table. Research by Jeffrey Hall (2019) estimated that it takes roughly 50 hours together to move from acquaintance to casual friend and around 200 hours for a close friend (estimates from surveys, so approximate).

**Reciprocity of liking.** We tend to like people who show they like us. Genuine interest and warmth often come back to you.

**Self-disclosure.** Arthur Aron and colleagues (1997) had pairs of strangers take turns answering 36 questions that became gradually more personal (the "fast friends" procedure). Pairs who did this felt much closer after 45 minutes than pairs who made small talk. The key is **gradual and mutual**: you share a little, they share a little, and the depth increases step by step. Oversharing too early tends to make people uncomfortable.

**The liking gap.** Erica Boothby, Gus Cooney, Gillian Sandstrom and Margaret Clark (2018) found that after conversations with strangers, people consistently **underestimated how much their partner liked them** and enjoyed the talk. Related studies by Nicholas Epley and Juliana Schroeder found that people expect talking to strangers on trains and buses to be awkward, but those asked to do it reported a more pleasant journey than those who sat in silence. Together these findings are encouraging: **people are friendlier, and conversations go better, than our fears predict.**

**Ethics.** These principles are about genuine connection. Faking similarity ("Oh, I love cricket too!" when you don't) or creating artificial familiarity to sell something is manipulation (Module 32). Find real common ground; there is almost always some.
""",
    evidence=[
        ('Similarity increases liking', 'strong', 'Many studies; perceived similarity matters most.'),
        ('Mere exposure and proximity increase liking', 'moderate', 'Robust in many studies; weaker or reversed if first impressions are negative.'),
        ('Gradual mutual self-disclosure builds closeness', 'moderate', 'The 36-questions procedure replicated in several labs.'),
        ('The liking gap: people underestimate how much others like them', 'moderate', 'Several studies by Boothby and colleagues.'),
        ('Hours needed to become friends', 'mixed', 'Survey estimates; useful as a rough guide.'),
    ],
    example="""
Anu moved to a rented room near a Kozhikode library to study. After two months she knows nobody. She applies the research:

**Proximity and familiarity:** she studies at the same library table at the same time every day, and has tea at the same stall at 4 pm. **Similarity:** she notices two other aspirants with LDC guides and says, "Are you also writing the LDC? Which district?" **Reciprocity and warmth:** she remembers what they tell her and asks about it the next day ("How did the mock go?"). **Gradual self-disclosure:** over two weeks, talk moves from exam dates to why they want a government job, to family pressure and worries.

After their first conversation, Anu feels she talked too much and "they probably found me boring" (**the liking gap**). The next day one of them, Divya, saves her a seat. Within a month the three study together on Saturdays.
""",
    apply="""
**Build rapport honestly:**
1. **Be around:** choose regular places and times (library, tea shop, a club, a group). Familiarity needs repetition.
2. **Find real common ground** in the first minutes: the place, the exam, the town, the weather, a shared struggle. Ask: "What brings you here?"
3. **Show genuine interest:** remember one detail and bring it up next time.
4. **Disclose gradually and mutually:** share something a little personal after they do; let depth grow.
5. **Remember the liking gap:** after a conversation, assume it went better than you think, and follow up.

**Conversation starters that work in Kerala settings:**
- "Is this seat free? Are you preparing for something too?"
- "That looks like a good book: is it useful?"
- "Have you been coming here long? Any tips for this place?"
- "How do you know the bride/groom?" (at a wedding)

**With others:** include people who are on the edge of a group; you know how it feels.
""",
    resources=[
        ('os-12', 'Read 12.7 Prosocial Behavior, the section on interpersonal attraction (proximity, similarity)', '15 minutes'),
        ('ggsc', 'Search the site for "36 questions" and read the article with the questions', '15 minutes'),
        ('ggia', 'Search for the "36 Questions for Increasing Closeness" practice and read the instructions', '10 minutes'),
    ],
    steps=[
        'Choose one regular place where you can meet the same people repeatedly, and go there at the same time at least four times this week.',
        'Start at least three conversations using real common ground. After each, rate how much you think they liked it (1–10).',
        'Follow up with one person: remember a detail and ask about it next time.',
        'With a friend or family member, try the first set of the 36 questions (12 questions) and note how it felt.',
    ],
    proof='A note of your regular place and visits, three conversation notes with your liking-gap ratings, one follow-up, and a note on the 36-questions practice.',
    templates=[('Rapport builder', """RAPPORT BUILDER
Regular place and time: ______  Visits this week: [ ][ ][ ][ ]
Conversations: Date | Who | Common ground found | One detail to remember | I think they liked it (1-10) | Follow-up done?
Starters I'll use: 1 "______" 2 "______" 3 "______"
36 questions practice: with ______ ; questions ___ to ___ ; how it felt ______""", '')],
    mistakes=[
        ('Waiting for friends to appear.', 'Friendship needs repeated contact. Choose regular places.'),
        ('Faking common interests.', 'People notice, and it is manipulative. Find something real.'),
        ('Oversharing too early.', 'Disclose gradually and match the other person.'),
        ('Believing your post-conversation doubts.', 'The liking gap means you probably underestimate how it went.'),
    ],
    quiz=[
        Q('What did the "liking gap" studies find?', 'People underestimate how much their conversation partners liked them', 'People overestimate how much others like them', 'Strangers dislike conversations', 'Liking has no gap', why='Boothby and colleagues found consistent underestimation.'),
        Q('Why do friendships often form between neighbours or classmates?', 'Proximity and repeated exposure increase liking', 'They are forced to', 'Because of luck only', 'Because of similar height', why='Familiarity and proximity effects.'),
        Q('What made the 36-questions procedure work?', 'Gradual, mutual, increasingly personal self-disclosure', 'Asking the most personal questions first', 'Talking only about yourself', 'Avoiding eye contact', why='Depth grew step by step on both sides.'),
        Q('Which use of similarity is ethical?', 'Finding and mentioning real common ground', 'Pretending to share interests to sell something', 'Copying someone\'s opinions to please them', 'Hiding your views always', why='Genuine common ground builds real rapport.'),
    ],
    study='read the lesson and the 36 questions article',
    action='visit one regular place four times, start three conversations, follow up once and try the first 12 of the 36 questions',
)

L2 = lesson(
    25, 2,
    outcome='You can hold a listening-first conversation, ask good follow-up questions, summarise what someone said, and complete 14 days of conversation challenges.',
    split='20 minutes reading, 10 minutes a day for 14 days',
    principle='Most people want to be heard more than advised; asking follow-up questions and summarising what someone said make them like you more and help you understand them.',
    science=f"""
**Questions and liking.** Karen Huang, Alison Wood Brooks and colleagues (2017) analysed thousands of conversations, including speed dates. People who asked more questions, especially **follow-up questions** (questions that build on what the other person just said), were liked more. Yet people underestimate this and tend to ask too few questions, especially when trying to impress.

**Active listening.** The term comes from Carl Rogers's client-centred therapy: listening to understand the speaker's meaning and feelings, without judging, and showing it. Common components: full attention, encouraging signals (nods, "hmm", "then?"), **paraphrasing** ("So you felt…"), **reflecting feelings** and **asking open questions**. Studies of active-listening training show it makes speakers **feel more understood**; one study (Weger and colleagues, 2014) found that mechanical paraphrasing alone did not increase liking much, so it must be genuine, not a formula. Research by Guy Itzchakov and Avraham Kluger found that high-quality listening made speakers less defensive and more willing to reflect on their views.

**Talking time.** In conversations, many of us talk more than we listen, partly because talking about ourselves is rewarding: a brain-imaging study by Diana Tamir and Jason Mitchell (2012) found that sharing information about oneself activated reward-related brain regions. So letting others talk is a gift they enjoy.

**Open versus closed questions.** Closed questions get yes/no answers ("Was the exam hard?"); open questions invite stories ("What was the exam like?"). Both have a place; conversations grow on open and follow-up questions.

**Culture.** In Kerala, conversations often start with family and food ("Did you eat?", "Where's your house?", "Which batch?"), which are warm openers. Be careful with intrusive questions about marriage, salary, caste or why someone has "no job yet"; many people find them hurtful (and you probably do too).
""",
    evidence=[
        ('Asking follow-up questions increases liking', 'moderate', 'Large conversation datasets and experiments (Huang et al., 2017).'),
        ('Active listening makes speakers feel understood', 'moderate', 'Several studies; mechanical paraphrasing alone helps less.'),
        ('Good listening reduces defensiveness', 'moderate', 'Experiments by Itzchakov and Kluger.'),
        ('Talking about oneself is intrinsically rewarding', 'moderate', 'Brain-imaging and behavioural studies (Tamir and Mitchell).'),
    ],
    example=f"""
Ashiq's cousin Shabeer calls, upset about his new job in a Kochi IT company. Ashiq's old habit: give advice within 30 seconds ("Just quit and prepare for PSC!").

This time he listens first. **Open question:** "What's been happening?" **Encouraging signals:** "Hmm… then?" **Follow-up:** "You said your manager changed the deadline twice; what happened the second time?" **Reflect the feeling:** "That sounds really frustrating, like nothing you do is enough." **Summarise:** "So it's not the work itself, it's the changing deadlines and not being told. Is that right?" Shabeer: "Exactly! That's it." Only then does Ashiq ask, "Do you want ideas, or did you just need to let it out?" Shabeer wants one idea; they talk about asking the manager for a weekly priority list.

Shabeer later says it was the most helpful conversation he'd had all month, and Ashiq gave almost no advice.
""",
    apply=f"""
**The listening-first conversation (LIFT):**
- **L**et them talk: aim for them speaking about two-thirds of the time.
- **I**nvite more: open questions ("What was that like?", "How did that happen?") and encouragers ("Then?", "Hmm", nodding).
- **F**ollow up: build on what they just said ("You mentioned X; tell me more").
- **T**ell it back: summarise, and reflect the feeling ("So you felt… Is that right?").
Then ask: "Do you want ideas, or just someone to listen?"

**Follow-up question formulas:**
- "What happened next?"
- "How did you feel about that?"
- "What made you decide to…?"
- "What was the hardest/best part?"
- "You said ___; what did you mean?"

**The 14-day conversation challenge** (on the Daily system track): one conversation a day using one rotation: listening first, two follow-up questions, using and remembering the person's name (PD-M25-L03), or one genuine compliment (PD-M25-L03). Log each in the conversation log.

{fence(tools.CONVERSATION_LOG)}

**With others:** when someone shares a problem, resist fixing it at once. Listening first is respect; advice can come later, if they want it.
""",
    resources=[
        ('ggia', 'Search for the "Active Listening" practice and read it', '10 minutes'),
        ('ggsc', 'Search for an article on "how to listen" or "asking questions" and read one', '10 minutes'),
        ('os-12', 'Re-read 12.3 Attitudes and Persuasion (why people who feel heard are more open)', '15 minutes'),
    ],
    steps=[
        'Rate your listening (1–10) and your share of talking time in a recent conversation.',
        'Do the 14-day conversation challenge: one conversation a day using the rotation, logged.',
        'In at least three conversations, use the full LIFT steps and note whether the person said "yes, exactly" (or similar) to your summary.',
        'After 14 days, re-take the listening self-rating from the baseline and compare.',
    ],
    proof='Your 14-day conversation log, three LIFT notes and your before-and-after listening ratings.',
    templates=[('LIFT card', """LISTENING-FIRST CONVERSATION (LIFT)
L - Let them talk (about 2/3 of the time)
I - Invite more: "What was that like?" "Then?" (nod)
F - Follow up: "You mentioned ___ ; tell me more."
T - Tell it back: "So you ___ and felt ___ . Is that right?"
Then: "Do you want ideas, or just someone to listen?"
Avoid: interrupting, topping their story with mine, advice in the first minute,
intrusive questions (marriage, salary, caste, "still no job?")""", '')],
    mistakes=[
        ('Waiting to talk instead of listening.', 'Focus on understanding; your turn will come.'),
        ('Topping their story with yours.', '"That\'s nothing, I once…" steals the conversation. Ask a follow-up first.'),
        ('Mechanical paraphrasing.', 'Parroting words sounds fake. Summarise the meaning and the feeling in your own words.'),
        ('Giving advice too early.', 'Ask whether they want ideas.'),
    ],
    quiz=[
        Q('What kind of question most increased liking in Huang and colleagues\' research?', 'Follow-up questions that build on what the other person just said', 'Questions about the weather', 'Questions about yourself', 'No questions at all', why='Follow-up questions show you listened.'),
        Q('What is the best response after someone shares a problem?', 'Listen, summarise their meaning and feeling, then ask whether they want ideas', 'Give advice immediately', 'Tell a bigger problem of your own', 'Change the subject', why='Listening first makes people feel understood.'),
        Q('Which is an open question?', '"What was the interview like?"', '"Was the interview hard?"', '"Did you go?"', '"Is it at 10?"', why='Open questions invite stories.'),
        Q('Why did mechanical paraphrasing help less in one study?', 'It can sound formulaic; genuine understanding matters', 'Paraphrasing is always rude', 'People dislike being understood', 'It takes too long', why='Listening must be genuine, not a technique.'),
    ],
    study='read the lesson and the Active Listening practice',
    action='complete 14 days of conversation challenges and three full LIFT conversations, and re-rate your listening',
)

L3 = lesson(
    25, 3,
    outcome='You can remember names using a simple method, give genuine specific praise, and make people feel important without flattery.',
    split='15 minutes reading, 25 minutes of tasks',
    principle='People love hearing their own name and being genuinely appreciated; remembering names takes a method, and praise works when it is specific, sincere and about effort or choices.',
    science="""
**Names.** Dale Carnegie wrote in *How to Win Friends and Influence People* (1936) that a person's name is to them "the sweetest and most important sound in any language". The book is not a research study, but some findings fit: hearing your own name grabs attention automatically (the "cocktail party" effect in attention research), and being remembered signals that you matter. Names are hard to remember because they are arbitrary labels with no meaning attached; we often aren't paying attention when they are said.

**What helps you remember names** (from memory research, Module 3 of the Learning Capabilities course):
1. **Attend:** decide in advance to catch the name; ask again at once if you missed it.
2. **Repeat and use it:** say it back ("Nice to meet you, Divya"), and use it once more in the conversation.
3. **Link it:** connect the name to something meaningful (someone you know with the same name, a feature, a place: "Rafeeq from Feroke").
4. **Retrieve it:** recall it a few minutes later, and write it down within an hour with one detail (retrieval practice and spacing).

**Genuine praise.** Studies by Xuan Zhao and Nicholas Epley (2021) found that people **underestimate how good a sincere compliment makes others feel** and overestimate how awkward it will be, so they give fewer compliments than would help. Research on praise in children and adults suggests that **specific** praise (about a concrete action or choice) is more credible and useful than vague praise ("You're great"), and that praise for **effort and strategy** supports learning better than praise for fixed traits (PD-M09-L01). Flattery (insincere or exaggerated praise to gain something) can work briefly, but it damages trust once noticed.

**Making people feel important.** Carnegie's advice to "make the other person feel important, and do it sincerely" has support from research on basic needs (Module 6: relatedness and competence) and on **gratitude**: Amit Kumar and Nicholas Epley (2018) found that people underestimate how much recipients value gratitude letters. Concretely: remember details, ask their opinion, credit their ideas in front of others, and thank them specifically.
""",
    evidence=[
        ('Own name captures attention', 'moderate', 'Attention research (cocktail-party effect).'),
        ('Attend, repeat, link and retrieve improves name recall', 'moderate', 'Based on well-supported memory principles.'),
        ('People underestimate how good compliments make others feel', 'moderate', 'Experiments by Zhao and Epley (2021).'),
        ('Specific, sincere praise is more effective than vague praise', 'moderate', 'Supported by studies on feedback and praise.'),
        ('Carnegie\'s book as research', 'tool', 'Practical advice from experience; some principles match later research.'),
    ],
    example="""
At his cousin's wedding reception, Ashiq meets about 15 new people. His old pattern: forget every name within a minute.

This time: **attend** ("Sorry, what was your name again?"); **repeat** ("Nice to meet you, Sajna"); **link** ("Sajna, like my aunt; she teaches at the Vadakara school"); **use** it once ("Sajna, how did you get into teaching?"); **retrieve and record**: in the car, he writes six names with one detail each in his phone. A month later at another function, he greets Sajna by name and asks about her school's science fair. Her face lights up.

He also practises **specific praise**. Instead of "Nice food!" to the caterer, he says, "The avial was perfect: the coconut wasn't overpowering at all. How do you get it like that?" The caterer, an old man, smiles and explains for five minutes. Ashiq notices he enjoyed giving the compliment as much as the man enjoyed getting it.
""",
    apply=f"""
**Remember names (ARLR):**
1. **Attend:** decide to catch it; ask again if you missed it.
2. **Repeat:** say it back immediately.
3. **Link:** connect it to a person, place or feature you know.
4. **Retrieve:** recall it after five minutes; write it with one detail within an hour.

**Give genuine praise (the SSE rule):**
- **Specific:** name the exact thing ("the way you explained the map question").
- **Sincere:** only say it if you mean it.
- **Effort or choice:** praise what they did ("You prepared those notes so clearly") more than fixed traits ("You're so smart").

**Make people feel important (without flattery):**
- Remember and ask about details from last time.
- Ask for their opinion or advice on something they know.
- Credit their idea in front of others ("As Divya suggested…").
- Thank them specifically, in person or in a message.

**With others:** praise in public, correct in private. Never use names and compliments as tools to get something; people sense it.
""",
    resources=[
        ('ggia', 'Search for the "Gratitude Letter" practice and read it again for the "thank them specifically" step', '10 minutes'),
        ('ggsc', 'Search the site for "compliments" and read one article about the Zhao and Epley research', '10 minutes'),
        ('franklin', 'Read the passage in Franklin\'s Autobiography where he wins over a rival legislator by asking to borrow a book (search for "lending it to me")', '10 minutes'),
    ],
    steps=[
        'Use ARLR with every new person you meet for a week; write each name and one detail within an hour.',
        'A week later, test yourself: how many names can you recall from your list? Write the score.',
        'Give at least five specific, sincere compliments over the week and note each person\'s reaction.',
        'Write one specific thank-you message to someone who helped you recently.',
    ],
    proof='Your names list with details and the recall score a week later, five compliment notes with reactions, and your thank-you message.',
    templates=[('Names and praise log', """NAMES LOG (write within an hour)
Date | Name | Where we met | Link I used | One detail | Recalled a week later? (Y/N)
Recall score after one week: ___ / ___
PRAISE LOG (Specific, Sincere, about Effort or choice)
Date | Who | What exactly I praised | Their reaction
THANK-YOU MESSAGE: To ______ for ______ (specific): "______" """, '')],
    mistakes=[
        ('Saying "I\'m bad with names".', 'It is a method problem, not a talent problem. Use ARLR.'),
        ('Overusing someone\'s name.', 'Once or twice in a conversation feels warm; ten times feels like a sales pitch.'),
        ('Vague or exaggerated praise.', 'Be specific and sincere; flattery damages trust.'),
        ('Praising to get something.', 'That is manipulation. Praise because it is true and kind.'),
    ],
    quiz=[
        Q('What is the first step in remembering a name?', 'Attend: decide to catch it, and ask again if you missed it', 'Write it down a week later', 'Guess it', 'Avoid using it', why='Most names are lost because we never really heard them.'),
        Q('What did Zhao and Epley find about compliments?', 'People underestimate how good sincere compliments make others feel', 'Compliments always embarrass people', 'Compliments have no effect', 'People overestimate their effect', why='So we give fewer compliments than would help.'),
        Q('Which praise follows the SSE rule?', '"The way you organised those notes by topic made them easy to revise."', '"You\'re amazing."', '"Nice."', '"You\'re so naturally smart."', why='It is specific, sincere and about a choice.'),
        Q('What is the main difference between genuine praise and flattery?', 'Genuine praise is true and sincere; flattery is exaggerated or insincere to gain something', 'Flattery is shorter', 'Genuine praise is always public', 'There is no difference', why='Flattery damages trust when noticed.'),
    ],
    study='read the lesson and the Franklin passage',
    action='use ARLR for a week and test recall, give five specific compliments and send one specific thank-you',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    25,
    overview=f"""
Liking and rapport, built honestly: similarity, familiarity, reciprocity, gradual self-disclosure and the liking gap; listening-first conversations and follow-up questions; remembering names; genuine praise; and making people feel important without flattery. Includes the 14-day conversation challenge.

These are the everyday skills that turn strangers into acquaintances and acquaintances into friends, colleagues and supporters. The research is encouraging: conversations usually go better than we fear, people like us more than we think, and the most liked people are often the best listeners, not the best talkers.

Everything here is about **genuine** connection. Faking interest, similarity or praise to get something is manipulation; it is covered in Module 32 so you can spot it.
""",
    outcomes=[
        'Explain similarity, familiarity, reciprocity, self-disclosure and the liking gap.',
        'Hold listening-first conversations with follow-up questions and summaries.',
        'Remember names with the ARLR method.',
        'Give specific, sincere praise and make people feel important honestly.',
        'Complete the 14-day conversation challenge.',
    ],
    lessons=LESSONS,
    project='14 days of conversation challenges',
    project_steps=[
        'Do the 14-day challenge (PD-M25-L02), rotating listening first, follow-up questions, names and genuine praise.',
        'Log every conversation in the conversation log.',
        'At the end, count: conversations, names remembered a week later, compliments given, and people who said "yes, exactly" to your summary.',
        'Re-take the social-confidence and listening self-ratings and add your best conversation rules to the Playbook.',
    ],
    project_proof='The 14-day conversation log, your counts and your before-and-after self-ratings.',
    rubric=[
        ('Consistency', 'Fewer than 7 days', '7 to 11 days', '12 to 14 days logged'),
        ('Listening', 'Mostly talking', 'Some follow-ups', 'Listening first with follow-ups and summaries most days'),
        ('Names', 'Not tried', 'Some names recorded', 'Names recorded with a week-later recall score'),
        ('Sincerity', 'Flattery or faked interest', 'Mostly genuine', 'Genuine, specific interest and praise throughout'),
    ],
    short=[
        'One listening-first conversation every two days for two weeks.',
        'Use ARLR for every new name for one week.',
    ],
    flashcards=[
        ('Liking gap', 'People underestimate how much others liked talking to them.'),
        ('Mere-exposure effect', 'Repeated contact tends to increase liking (if first impressions are not negative).'),
        ('Fast friends procedure', 'Gradual, mutual self-disclosure (36 questions) builds closeness.'),
        ('Best question for liking', 'Follow-up questions.'),
        ('LIFT', 'Let them talk, Invite more, Follow up, Tell it back.'),
        ('ARLR for names', 'Attend, Repeat, Link, Retrieve.'),
        ('SSE praise rule', 'Specific, Sincere, about Effort or choice.'),
        ('Praise and correction', 'Praise in public, correct in private.'),
    ],
    mistakes=[
        ('Treating people as networking targets.', 'Be interested in them as people.'),
        ('Collecting techniques but not practising.', 'The 14-day log is where the skill grows.'),
        ('Intrusive questions.', 'Avoid marriage, salary, caste and "still no job?" questions.'),
    ],
    tools=[
        'The rapport builder and starters (PD-M25-L01).',
        'The LIFT card and conversation log (PD-M25-L02).',
        'The names and praise log (PD-M25-L03).',
    ],
    playbook=[
        'In conversations: listen first, two follow-up questions, summarise, then ask "ideas or just listening?"',
        'Names: attend, repeat, link, retrieve. Praise: specific, sincere, about effort or choice.',
    ],
)
