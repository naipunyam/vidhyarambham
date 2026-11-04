from common import lesson, module, link, xref, table, fence, Q

L1 = lesson(
    31, 1,
    outcome='You can map your relationships, explain why close relationships matter so much for health and happiness, and take weekly actions to deepen friendships and family bonds.',
    split='20 minutes reading, 30 minutes of tasks',
    principle='Close relationships are among the strongest predictors of happiness and health; they need regular time, small acts of care and responsiveness, and they can be built and repaired at any age.',
    science=f"""
**Why relationships matter.** A 2010 meta-analysis by Julianne Holt-Lunstad, Timothy Smith and Bradley Layton (148 studies, over 300,000 people) found that people with stronger social relationships had about **50% higher odds of survival** over the study periods; the size of the effect was comparable to well-known risk factors such as smoking. These are observational studies, so other factors may contribute, but the pattern is strong and consistent. The Harvard Study of Adult Development, which has followed people since the late 1930s, emphasises the same theme ({link('hsad', 'Harvard study')}; {link('ted-waldinger', 'Waldinger\'s TED talk')}): **the quality of relationships**, not just their number, predicted wellbeing and health in later life.

**Loneliness** is the painful feeling that your relationships are not enough. It is different from being alone: you can be lonely in a joint family or content living alone. Research links chronic loneliness with poorer sleep, higher blood pressure, depression and earlier death. It is common among young adults, including those preparing for exams in isolation.

**What builds closeness:**
- **Time together:** Jeffrey Hall's estimates suggest roughly 50 hours for a casual friend and 200 for a close friend (PD-M25-L01).
- **Responsiveness:** Harry Reis's research shows that feeling **understood, valued and cared for** by a partner is central to close relationships.
- **Capitalisation:** Shelly Gable found that how people respond to **good news** matters a lot: **active-constructive** responses ("That's wonderful! Tell me how it happened!") were linked to better relationships than passive ("Nice") or deflating ones ("Won't that mean more work?").
- **Small, regular acts:** checking in, remembering events, helping practically.
- **Self-disclosure** that grows step by step (PD-M25-L01).

**Family.** In Kerala, family relationships are central and often complex: expectations about careers, marriage and money; joint and nuclear families; parents who sacrificed for you. Many of the tools in this course help at home: listening first (PD-M25-L02), assertiveness with respect (PD-M26-L02), NVC (PD-M26-L03) and values conversations (PD-M05-L01).

**Friendship maintenance.** Studies of friendship (for example, by Robin Dunbar's group) find that friendships fade when contact drops, often within a few years, unless they are maintained. Short regular contact (a call, a message, a shared activity) keeps them alive.
""",
    evidence=[
        ('Strong social relationships predict survival', 'strong', 'Meta-analysis of 148 studies; observational but consistent.'),
        ('Relationship quality predicts later wellbeing (Harvard study)', 'moderate', 'Long-term cohort study; observational.'),
        ('Responsiveness is central to closeness', 'moderate', 'Supported by many studies (Reis and colleagues).'),
        ('Active-constructive responses to good news build relationships', 'moderate', 'Supported by Gable\'s studies; some replications show smaller effects.'),
        ('Friendships fade without contact', 'moderate', 'Supported by longitudinal friendship studies.'),
    ],
    example="""
Anu draws her relationship map: herself in the centre; inner circle (people she could call at 2 am): her mother and one school friend, Nisha; middle circle (good friends, regular contact): two study-group members and a cousin; outer circle (friendly acquaintances): neighbours, the librarian, former classmates. She notices that Nisha, her closest friend, hasn't heard from her in four months, and that she talks to her father mostly about exam results.

Her weekly actions: a 15-minute call with Nisha every Sunday; one evening walk a week with her father where she doesn't talk about exams; and **active-constructive** responses. When her cousin calls to say she got a nursing job in Bengaluru, Anu's first instinct is "So far away!". Instead she says, "That's fantastic! How did the interview go? When do you start?" Her cousin talks happily for 20 minutes.

After two months, Nisha visits during Onam, and Anu's father starts asking about her day, not just her scores.
""",
    apply=f"""
**Map your relationships:**
{fence('''RELATIONSHIP MAP              Date ______
INNER CIRCLE (could call at 2 am):        ______ ______ ______
MIDDLE (good friends, regular contact):   ______ ______ ______ ______
OUTER (friendly acquaintances):           ______ ______ ______ ______
Fading relationships I want to renew:     ______ ______
Relationships that drain or harm me:      ______ (limit? boundary? help?)
WEEKLY ACTIONS (pick 2-3)
[ ] A call or visit with an inner-circle person
[ ] Time with a family member, not about exams or money
[ ] An active-constructive response to someone's good news
[ ] Remember and ask about something from last time
[ ] One practical help (an errand, a lift, a meal)''')}

**Active-constructive responding:** when someone shares good news, respond with enthusiasm and questions: "That's great! How did it happen? How do you feel?" Avoid passive ("Okay"), deflating ("But what about…?") or hijacking ("When I got mine…").

**Loneliness plan:** if you feel lonely, start with **low-pressure regular contact** (a weekly class, a library group, volunteering, Module 35), reach out to one old friend, and talk to someone if loneliness comes with low mood (Tele-MANAS 14416).

**Harmful relationships:** if a relationship involves control, threats, humiliation or violence, it's not something to "fix with communication skills". See Module 32 and get support.
""",
    resources=[
        ('ted-waldinger', 'Re-watch the talk; write the three lessons about relationships', '13 minutes'),
        ('hsad', 'Read the study\'s homepage and one linked resource', '10 minutes'),
        ('ggsc', 'Search the site for "active constructive responding" and read the article', '10 minutes'),
    ],
    steps=[
        'Draw your relationship map.',
        'Choose two or three weekly actions and do them for two weeks.',
        'Use active-constructive responding at least three times and note the reactions.',
        'Renew one fading relationship with a message or call.',
    ],
    proof='Your relationship map, two weeks of weekly actions ticked, three active-constructive notes and the renewal message or call.',
    templates=[('Responding to good news', """RESPONDING TO GOOD NEWS
                 Active (engaged)                     Passive (low energy)
Constructive     "That's wonderful! How did it        "Nice."
(positive)       happen? How do you feel?"  <- AIM
Destructive      "But won't that mean ______?"        "Okay. Anyway, I..."
(negative)
LOG: Date | Who | Their good news | My response (type) | Their reaction""", '')],
    mistakes=[
        ('Waiting for others to reach out.', 'Most people are waiting too. Send the message.'),
        ('Talking to family only about exams and money.', 'Spend time on other things too.'),
        ('Deflating good news.', 'Celebrate first; concerns can wait.'),
        ('Trying to fix abusive relationships alone.', 'Get support (Module 32).'),
    ],
    quiz=[
        Q('What did the 2010 meta-analysis of 148 studies find?', 'Stronger social relationships were linked to about 50% higher odds of survival', 'Relationships don\'t affect health', 'Only family relationships matter', 'Friends shorten life', why='Holt-Lunstad and colleagues\' findings.'),
        Q('Which is an active-constructive response to "I got the job!"?', '"That\'s wonderful! How did the interview go?"', '"Nice."', '"Won\'t you have to move far away?"', '"I got a job once too."', why='Enthusiastic and curious.'),
        Q('What is loneliness?', 'The feeling that your relationships aren\'t enough, which can happen even among people', 'Living alone', 'Having no phone', 'A personality type', why='Loneliness is about felt connection.'),
        Q('What keeps friendships from fading?', 'Regular contact and shared activities', 'Waiting for special occasions', 'Social-media likes only', 'Nothing can', why='Friendships fade without maintenance.'),
    ],
    study='read the lesson and re-watch Waldinger\'s talk',
    action='draw your relationship map, do two weeks of weekly actions and renew one fading relationship',
)

L2 = lesson(
    31, 2,
    outcome='You can resolve everyday conflicts with a repair-focused approach, recognise the four patterns that damage relationships, and explain what research says makes relationships last.',
    split='20 minutes reading, 30 minutes of tasks',
    principle='Conflict is normal; what matters is how it is handled: soft starts, no contempt, taking responsibility for your part, repair attempts and calming down before continuing.',
    science=f"""
**The research on lasting relationships.** Psychologist John Gottman studied couples in his "love lab" for decades, recording how they argued. He described **four patterns** that predicted trouble, which he called the "Four Horsemen":
1. **Criticism:** attacking the person rather than the behaviour ("You're so selfish").
2. **Contempt:** mockery, sarcasm, eye-rolling, treating the other as beneath you; Gottman considered it the most damaging.
3. **Defensiveness:** counter-attacking or playing the victim instead of hearing the complaint.
4. **Stonewalling:** shutting down and withdrawing.
And their antidotes: **gentle start-up** (complaint about a specific behaviour with an "I" statement), **building a culture of appreciation**, **taking responsibility** for your part, and **self-soothing** (taking a break when flooded, then returning).

**Honest caveats.** Gottman's work is influential and his practical advice is widely used, but his famous claims of predicting divorce with over 90% accuracy have been **criticised**: researchers such as Richard Heyman pointed to small samples and models built after outcomes were known, which inflate accuracy; the models were not tested on fresh samples ({link('wp-gottman', 'summary')}). The **"5 to 1 ratio"** of positive to negative interactions in stable couples is a rough description from his observations, not a precise law (PD-M10-L01). The four patterns themselves are consistent with much other research showing that hostility and withdrawal damage relationships.

**Other well-supported findings about lasting relationships:**
- **Responsiveness** and **appreciation** (PD-M31-L01).
- **Repair attempts:** small gestures during conflict (a joke, a touch, "I'm sorry, let me try again") that de-escalate; how well couples repair matters more than how often they fight.
- **Shared meaning and novelty:** doing new, interesting things together is linked to relationship satisfaction (Arthur Aron's "self-expansion" research).
- **Fairness in work:** perceived unfairness in household work is linked to conflict.

**Conflict beyond couples.** The same patterns apply to friendships, siblings, parents, roommates and colleagues. **Repair** is a skill: a clear, specific apology ("I'm sorry I shouted at you in front of your friends; that was unfair; next time I'll talk to you privately") works better than "Sorry if you were hurt." Research on apologies (for example, Roy Lewicki and colleagues) found that **acknowledging responsibility** was the most important element, followed by offering repair.

**When conflict is abuse.** Control, threats, intimidation, isolation, humiliation, financial control or violence are not "communication problems"; they are abuse. Couples-communication techniques are not appropriate there. Seek help (see PD-M32-L03).
""",
    evidence=[
        ('Criticism, contempt, defensiveness and stonewalling damage relationships', 'moderate', 'Consistent with much research on hostility and withdrawal.'),
        ('Gottman\'s 90%+ divorce-prediction accuracy', 'mixed', 'Criticised: small samples, models built after outcomes, no fresh-sample tests.'),
        ('Exact 5:1 positive-to-negative ratio', 'mixed', 'A rough observation, not a precise law.'),
        ('Responsibility-acknowledging apologies work best', 'moderate', 'Supported by apology research.'),
        ('Shared novel activities increase satisfaction', 'moderate', 'Supported by self-expansion studies.'),
    ],
    example="""
Ashiq and his younger brother share a room and argue constantly about the light at night (Ashiq studies late; his brother has school). Their typical fight: "You're so selfish!" (**criticism**), "You think you're so important because of your exam" with an eye-roll (**contempt**), "It's not my fault, you're the one who…" (**defensiveness**), then silence for two days (**stonewalling**).

Ashiq tries a **gentle start-up**: "I know my late studying keeps you awake on school nights. I need about two hours after 9 pm. Can we work something out?" His brother, surprised, suggests Ashiq uses the hall after 10. Ashiq **takes responsibility**: "You're right, I've been inconsiderate about the light." When the conversation heats up again over the fan, Ashiq says, "Let's take ten minutes and come back," and they do (**self-soothing**).

Later he apologises for an earlier fight with a full apology: "I'm sorry I mocked your football in front of your friends. That was unkind. I won't do it again." His brother shrugs, but the next day he brings Ashiq tea while he studies.
""",
    apply=f"""
**The conflict-repair routine:**
1. **Gentle start-up:** "I feel ___ about ___ (specific behaviour). I need ___. Can we ___?" (NVC, PD-M26-L03).
2. **Listen and summarise their side** before replying (PD-M25-L02).
3. **Take responsibility for your part,** even if small: "You're right that I…"
4. **Watch for the Four Horsemen** in yourself; use the antidotes.
5. **Take a break if flooded** (heart racing, can't think): "Let's take 20 minutes and come back." Then come back.
6. **Repair:** a full apology: what I did, why it was wrong, what I'll do differently, and (if possible) how I'll make it right.

{fence('''FOUR HORSEMEN AND ANTIDOTES
Criticism ("You always / you're so...")  -> Gentle start-up: "I feel... about... I need..."
Contempt (mockery, eye-rolling)           -> Appreciation: notice and say what you value
Defensiveness ("It's not my fault")       -> Take responsibility for your part
Stonewalling (shutting down)              -> Self-soothe: break, breathe, return
FULL APOLOGY: "I'm sorry I ______. It was wrong because ______.
Next time I'll ______. Can I ______ to make it right?"''')}

**With others:** don't try to "Gottman" your parents' or friends' relationships; use these tools in your own.
""",
    resources=[
        ('wp-gottman', 'Read the article, including the criticism of the prediction claims', '10 minutes'),
        ('ggsc', 'Search the site for "how to apologize" and read one article', '10 minutes'),
        ('enchiridion', 'Read section 42 (when someone treats you badly, they act on what seems right to them)', '5 minutes'),
    ],
    steps=[
        'Think of a recurring conflict (with a family member, roommate, friend or colleague). Write which of the Four Horsemen appear and the antidote for each.',
        'Raise the issue once with a gentle start-up, and note how it went.',
        'Give one full apology for something you did, using the template.',
        'If you get flooded in a conflict this week, take a break and return. Note what happened.',
    ],
    proof='Your conflict analysis with horsemen and antidotes, notes on one gentle start-up, your full apology (or a note of it) and any break-and-return note.',
    templates=[('Conflict repair worksheet', """CONFLICT REPAIR WORKSHEET          With: ______
Recurring issue: ______________________
Horsemen I use: criticism / contempt / defensiveness / stonewalling
Antidotes I'll use: ______________________
Gentle start-up: "I feel ___ about ___. I need ___. Can we ___?"
Their side (my summary): ______________________
My part: ______________________
Apology: "I'm sorry I ___. It was wrong because ___. Next time I'll ___."
Outcome: ______""", '')],
    mistakes=[
        ('Treating Gottman\'s numbers as precise laws.', 'The patterns are useful; the exact predictions and ratios are disputed.'),
        ('"Sorry if you were hurt."', 'That is not an apology. Own the specific action.'),
        ('Continuing while flooded.', 'Take a break and come back; you can\'t think well with a racing heart.'),
        ('Using communication skills on abuse.', 'Abuse needs safety and support, not better phrasing.'),
    ],
    quiz=[
        Q('Which of Gottman\'s Four Horsemen did he consider the most damaging?', 'Contempt', 'Criticism', 'Defensiveness', 'Stonewalling', why='Mockery and disdain treat the other as beneath you.'),
        Q('What is the antidote to defensiveness?', 'Taking responsibility for your part', 'Counter-attacking', 'Leaving forever', 'Saying nothing', why='Owning your part de-escalates.'),
        Q('What is the honest status of Gottman\'s 90%+ divorce-prediction claims?', 'Criticised for small samples and models built after outcomes were known', 'Confirmed on many fresh samples', 'Proved false completely', 'Never published', why='Heyman and others raised these concerns.'),
        Q('What is the most important element of an apology, according to research?', 'Acknowledging responsibility', 'Explaining your reasons at length', 'Giving a gift', 'Saying it quickly', why='Lewicki and colleagues found acknowledgement mattered most.'),
    ],
    study='read the lesson and the Gottman article\'s criticism section',
    action='analyse a recurring conflict, use one gentle start-up and give one full apology',
)

L3 = lesson(
    31, 3,
    outcome='You can build a professional network honestly: map useful contacts, write outreach messages, ask for advice, follow up, and give value back.',
    split='20 minutes reading, 40 minutes of outreach',
    principle='Networking is building genuine relationships before you need them: be curious, ask for advice not favours, follow up, and help others; weak ties often bring new opportunities.',
    science=f"""
**The strength of weak ties.** Sociologist Mark Granovetter (1973) found that people often heard about the jobs they got through **acquaintances** ("weak ties") rather than close friends, because acquaintances move in different circles and have different information. A large 2022 study using LinkedIn's data (Karthik Rajkumar and colleagues, published in *Science*) tested this with randomised changes to friend suggestions across about 20 million people; **moderately weak ties** were the most useful for job mobility. For a PSC aspirant, weak ties can bring news of notifications, private jobs while you prepare, tuition students, freelance work or advice.

**Asking for advice.** Research by Alison Wood Brooks, Francesca Gino and Maurice Schweitzer (2015) found that people who asked for advice were seen as **more competent**, not less, especially when the task was hard and the person asked was an expert. Asking for **advice** ("How did you prepare for the KAS interview?") is easier to say yes to than asking for **favours** ("Can you get me a job?").

**Reciprocity in networks.** Adam Grant's research on "givers" (people who help others without keeping score) found that givers were over-represented among both the **least** and **most** successful people; the successful ones helped generously but also protected their time and avoided being exploited. Practical lesson: help others regularly, in ways that suit you, and don't let takers drain you.

**Follow-up.** Many networking contacts go nowhere because people never follow up. A short thank-you within a day, an update when you used their advice, and occasional contact afterwards turn one conversation into a relationship.

**Online and offline in Kerala.** Useful places: alumni groups (school, college, ITI, polytechnic), local libraries and reading rooms, Kudumbashree and panchayat events, professional associations, Toastmasters, LinkedIn (free), Telegram and WhatsApp study groups (useful, but verify claims), job fairs (including government ones), and religious or cultural organisations. The rejection skills from Module 14 and the conversation skills from Module 25 make these much easier.
""",
    evidence=[
        ('Weak ties bring new job information', 'strong', 'Classic study plus a large randomised LinkedIn study (2022).'),
        ('Asking for advice increases perceived competence', 'moderate', 'Experiments by Brooks, Gino and Schweitzer.'),
        ('Successful givers help but protect their time', 'moderate', 'Supported by Grant\'s research and related studies.'),
        ('Following up keeps contacts alive', 'tool', 'Practical advice consistent with relationship research.'),
    ],
    example=f"""
Ashiq wants to understand what Kerala Administrative Service officers actually do and how they prepared. He maps his network: two former classmates in government jobs (weak ties), a retired headmaster in his ward, a cousin's friend who cleared the KAS, and a Toastmasters member who works in a district office.

He sends this message to his cousin's friend, Anjana:
"Hello Anjana, I'm Ashiq, Rahul's cousin from Kuttiady. I'm preparing for the KAS and Rahul said you cleared it in 2022, congratulations! Could I ask you two or three questions about how you prepared, in a 10-minute call at a time that suits you? No problem at all if you're busy. Thank you!"

She replies in two days and talks to him for 25 minutes. He asks: "What would you do differently?" "Which resources were most useful?" "What does a normal week in your job look like?" The next day he sends a thank-you with one thing he will act on. A month later he messages again: "I followed your advice on answer-writing practice; my mock essay scores went up from 9 to 13 out of 20. Thank you!" Later, when a junior from his school asks him for help with the preliminary exam, he spends an hour with her, passing it on.
""",
    apply=f"""
**Build your network in four steps:**
1. **Map** (20 minutes): list 20 people across strong ties (family, close friends) and weak ties (old classmates, teachers, neighbours, colleagues of friends, alumni, people from events). Mark who knows about your goals.
2. **Reach out** (5 messages this week): ask for **advice**, specifically and briefly, with an easy no.
3. **Follow up:** thank-you within a day; an update after you use their advice; occasional contact (festival greetings, sharing something useful).
4. **Give back:** share notes, information about notifications, help juniors, introduce people who could help each other.

{fence('''OUTREACH MESSAGE TEMPLATE
"Hello ______, I'm ______ from ______ (how we're connected: ______).
I'm working on ______. I saw/heard that you ______ (specific, genuine).
Could I ask you two or three questions about ______ in a 10-minute call
or by message, at a time that suits you? No problem at all if you're busy.
Thank you!"
FOLLOW-UP (next day): "Thank you for your time. I'll ______ (one thing I'll act on)."
UPDATE (later): "I tried your advice on ______; the result was ______. Thank you!"''')}

**Ethics:** never pretend a closer connection than you have, never ask strangers for money or for "influence" to get a government job (that is corruption), and respect a no or a non-reply.

**Networking for your goals:** for business and customers, see {xref('ent', 'ent-m03', 'the Entrepreneurship customer-discovery module')}; for an online professional presence, see {xref('smm', 'smm-m12', 'the Social Media Marketing personal-branding module')}.
""",
    resources=[
        ('ted-jiang', 'Re-watch a section where strangers say yes to his unusual requests; notice how he explains why he is asking', '5 minutes'),
        ('ggsc', 'Search the site for "weak ties" or "acquaintances" and read one article', '10 minutes'),
        ('franklin', 'Read the passage on the Junto, the club Franklin formed for "mutual improvement" (search for "Junto")', '15 minutes'),
    ],
    steps=[
        'Map 20 people in your network (strong and weak ties).',
        'Send five advice-request messages this week using the template.',
        'For every reply, have the conversation, send a next-day thank-you, and note one thing you\'ll act on.',
        'Give value to two people in your network (share information, help a junior, introduce two people).',
    ],
    proof='Your 20-person network map, five sent messages (screenshots with names hidden if you prefer), notes on any conversations and thank-yous, and two give-back notes.',
    templates=[('Network map', """NETWORK MAP (20 people)          Goal: ______________________
Name | How I know them | Strong / weak tie | What they know about | Contacted? | Replied? | Follow-up done? | Way I could help them
1. ______ | ______ | ___ | ______ | __ | __ | __ | ______
...
Five outreach messages sent on: ______
Give-back this week: 1 ______ 2 ______""", '')],
    mistakes=[
        ('Only contacting people when you need something big.', 'Build relationships before you need them, with small asks and gives.'),
        ('Long, vague messages.', 'Short, specific, easy to say no.'),
        ('Never following up.', 'A next-day thank-you and a later update turn a contact into a relationship.'),
        ('Asking for influence in government jobs.', 'That is corruption and can harm you. Ask for advice only.'),
    ],
    quiz=[
        Q('What did Granovetter\'s "strength of weak ties" research find?', 'People often got jobs through acquaintances rather than close friends', 'Only close friends help', 'Weak ties are useless', 'Family always gets you jobs', why='Weak ties carry new information.'),
        Q('Why ask for advice rather than favours?', 'Advice requests are easier to accept and make you look more competent', 'Favours are illegal', 'Advice is always free', 'People hate favours', why='Brooks, Gino and Schweitzer\'s findings.'),
        Q('What is the best follow-up after a helpful conversation?', 'A thank-you the next day with one thing you\'ll act on, and a later update', 'Nothing', 'Asking for a job immediately', 'Adding them to many groups', why='Follow-up builds the relationship.'),
        Q('What did Adam Grant find about successful givers?', 'They help generously but protect their time from takers', 'They never help anyone', 'They help everyone with everything', 'They keep strict score', why='Givers succeed when they avoid exploitation.'),
    ],
    study='read the lesson and the Franklin Junto passage',
    action='map 20 contacts, send five advice requests, follow up every reply and give value to two people',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    31,
    overview=f"""
Relationships and networking: why close relationships matter so much for health and happiness, mapping and deepening friendships and family bonds, responding to good news, conflict repair (Gottman's Four Horsemen with honest caveats), full apologies, and professional networking through weak ties, advice requests and follow-up.

Of all the findings in this course, the importance of relationships is one of the most consistent. Yet relationships are often the first thing to go when people prepare for exams or build careers. This module helps you keep them, repair them and grow them, including the professional network that brings opportunities.

If a relationship involves control, threats or violence, communication skills are not the answer; see PD-M32-L03 for help.
""",
    outcomes=[
        'Explain the research linking relationships with health and happiness.',
        'Map your relationships and take weekly actions to deepen them.',
        'Use active-constructive responding and full apologies.',
        'Recognise the Four Horsemen and use their antidotes, with honest caveats about the research.',
        'Build a professional network with advice requests, follow-up and giving back.',
    ],
    lessons=LESSONS,
    project='a relationship map and five networking conversations',
    project_steps=[
        'Draw your relationship map and do two weeks of weekly actions (PD-M31-L01).',
        'Use the conflict repair worksheet on one recurring conflict (PD-M31-L02).',
        'Map your professional network and send five outreach messages, following up every reply (PD-M31-L03).',
        'Write a half-page reflection and add your relationship and networking routines to the Playbook.',
    ],
    project_proof='The relationship map with weekly actions, the conflict worksheet, the network map with outreach and follow-ups, and your reflection.',
    rubric=[
        ('Close relationships', 'No actions', 'A few contacts', 'Weekly actions for two weeks and one renewed relationship'),
        ('Conflict', 'Horsemen not recognised', 'Recognised but not changed', 'Gentle start-up and full apology used'),
        ('Networking', 'No outreach', 'One or two messages', 'Five messages with follow-ups'),
        ('Giving', 'Only taking', 'Some giving', 'Regular, specific help to others'),
    ],
    short=[
        'Call one inner-circle person each week.',
        'Send one advice request this month.',
    ],
    flashcards=[
        ('Social relationships and survival (meta-analysis)', 'About 50% higher odds of survival with stronger relationships.'),
        ('Active-constructive response', 'Enthusiastic, curious response to good news.'),
        ('Four Horsemen', 'Criticism, contempt, defensiveness, stonewalling.'),
        ('Most damaging horseman', 'Contempt.'),
        ('Gottman prediction caveat', 'Small samples; models built after outcomes; not tested on fresh samples.'),
        ('Full apology', 'What I did, why it was wrong, what I\'ll do differently, how I\'ll make it right.'),
        ('Weak ties', 'Acquaintances; often the source of new job information.'),
        ('Advice versus favours', 'Ask for advice: easier to accept, makes you look competent.'),
    ],
    mistakes=[
        ('Neglecting relationships during exam preparation.', 'Small regular contact protects them and you.'),
        ('Networking only online.', 'Combine it with real conversations and local events.'),
        ('Keeping score in relationships.', 'Give generously, but protect yourself from takers.'),
    ],
    tools=[
        'The relationship map and weekly actions (PD-M31-L01).',
        'The four horsemen and antidotes, and the conflict repair worksheet (PD-M31-L02).',
        'The network map and outreach templates (PD-M31-L03).',
    ],
    playbook=[
        'Relationships: one inner-circle call a week; active-constructive responses; time with family not about exams.',
        'Conflict: gentle start-up, my part first, break if flooded, full apologies.',
        'Network: ask for advice, follow up next day, update later, give back.',
    ],
)
