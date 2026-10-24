from common import lesson, module

L1 = lesson(
    3, 1,
    title='Plan and book customer interviews',
    weeks=(5, 5), hours=6,
    outcome='Decide who to interview and what you need to learn, find 15 people who have the problem, and complete your first 3 interviews.',
    split='1.5 hours study, 4.5 hours action including your first 3 interviews',
    core="""
An interview is a short, focused conversation about someone's life and the problem you care about. It is not a survey and not a sales call. You are a detective collecting facts.

### Who to talk to

Talk to people who have the problem **now**, or had it in the last month. The most useful are **early adopters**: they have the problem, know they have it, have already tried to solve it, and have some money or authority to spend on it. For ShopAssist that is a shop owner who already pays a nephew to answer messages; for PSC Sprint, an aspirant who already buys mock tests.

Don't interview only friends and family. They have the problem less often, and they want to be kind to you.

### Decide what you need to learn

Write three learning goals before you start. For example:

1. How do shop owners handle WhatsApp enquiries today, and what does it cost them?
2. What have they tried, and why didn't it work?
3. Who decides on spending, and how do they pay for services?

Every question you ask should serve one of these goals.

### Where to find people near Kuttiady

- **Your second-degree network:** friends of friends, relatives' colleagues. Ask: "Do you know a shop owner who struggles with WhatsApp orders?"
- **Walk-ins:** visit shops in quiet hours, such as late morning on weekdays, never during the evening rush.
- **Groups:** WhatsApp and Facebook groups for your town, profession or interest. Ask the admin before you post.
- **Places:** coaching centres, libraries, Akshaya centres, Kudumbashree meetings, college entrepreneurship (IEDC) clubs, community events. Be polite and brief.
- **Online:** LinkedIn for professionals, Facebook groups and forums for wider topics.

### How many

Aim for 10 to 15 interviews for a first pass, and keep going until new interviews stop surprising you. If after 10 interviews every story is very different, your customer group is too broad, so narrow it.

### How to ask for time

Keep the request short and specific, say clearly that you are not selling, and make it easy to say yes: "10 minutes, at your shop, at a time that suits you". Offer something small in return if you can, such as a useful tip or a summary of what others told you.

### Respect and privacy

Ask before you record anything. Store notes under a code (S1, S2…) rather than full names and phone numbers. Never repeat what one person told you in a way that identifies them. These habits also match the spirit of India's data protection law, the DPDP Act, which you will meet properly in Module 9.
""",
    example="""
For ShopAssist, Arun wrote three learning goals and then listed 15 shop owners: six textile shops, four mobile shops, two bakeries, two pharmacies and a hardware shop across Kuttiady, Thottilpalam and Vatakara. Eight came through an uncle and two friends; seven were walk-ins.

He visited at about 11 in the morning on weekdays, when shops were quiet, and used the Malayalam script below. Ten of the 15 agreed, three said "come next week" and two said no. By Sunday he had done three interviews of about 15 minutes each, all in person, and booked four more for the following week. His only cost was about ₹120 in bus fares.
""",
    resources=[
        ('yc-users', 'Watch the whole talk and write down the questions it recommends', 'about 20 min'),
        ('blank-udacity', 'Free sign-up. Lessons "What We Now Know" and the first "Business Models and Customer Development" lesson', 'about 1 hour'),
        ('dpdp', 'Read the part on notice and consent, so you handle interview notes respectfully (check current rules)', '10 min'),
    ],
    steps=[
        'Write your three learning goals at the top of the Interviews tab.',
        'List 15 people who have the problem now and how you will reach each one. At least 10 must not be close friends or family.',
        'Send or make at least 10 requests using the scripts below, and track who said yes.',
        'Do your first 3 interviews of 15–20 minutes each. Use the interview guide in the next lesson, or these three questions: "Tell me about the last time [problem] happened." "What did you do about it?" "What did that cost you?"',
        'Write your notes within an hour of each interview.',
    ],
    proof='Your learning goals, the list of 15 people (codes, not full names), your request tracker and notes from 3 interviews.',
    templates=[
        ('interview requests in English and Malayalam', """
ENGLISH (WhatsApp or in person)
Hi [name], I'm [your name] from [place]. I'm studying how
[shop owners / parents / PSC aspirants] handle [problem].
I'm not selling anything. Could I ask you a few questions
for 10 minutes? Any time that suits you is fine.

MALAYALAM
നമസ്കാരം [പേര്], ഞാൻ [നിങ്ങളുടെ പേര്], [സ്ഥലം] സ്വദേശി.
[കടയുടമകൾ / രക്ഷിതാക്കൾ / PSC ഉദ്യോഗാർത്ഥികൾ]
[പ്രശ്നം] എങ്ങനെ കൈകാര്യം ചെയ്യുന്നു എന്നതിനെക്കുറിച്ച്
ഒരു ചെറിയ പഠനം നടത്തുകയാണ്. ഒന്നും വിൽക്കാനല്ല.
10 മിനിറ്റ് സംസാരിക്കാൻ പറ്റുമോ? നിങ്ങൾക്ക്
സൗകര്യമുള്ള സമയം പറഞ്ഞാൽ മതി.

ASKING FOR AN INTRODUCTION
Do you know someone who [has the problem]? I'd like to ask
them a few questions for a small study. Could you share my
number with them, or introduce us?
""", ''),
        ('request tracker (paste into the Interviews tab)', """
Code,Who (role and place),How I'll reach them,Asked on,Reply,Interview date,Notes done
S1,Textile shop owner in Kuttiady,Uncle's friend,,,,
S2,,,,,,
""", 'csv'),
    ],
    mistakes=[
        ('Interviewing anyone who will talk.', 'Pick people who had the problem in the last month. A neighbour with no shop can\'t tell you how shops handle WhatsApp.'),
        ('Asking at the wrong time.', 'Never interview a shop owner at the evening rush or a student just before an exam.'),
        ('Sounding like a salesperson.', 'Say clearly that you are not selling, and mean it. Selling comes later.'),
        ('Relying on online forms.', 'Forms are useful for counting later, but they can\'t ask "why?". Talk first.'),
    ],
    quiz=[
        {'q': 'Who is the best person to interview for ShopAssist?',
         'o': ['Your cousin, who has no shop', 'A textile shop owner who lost a WhatsApp order last week', 'A famous entrepreneur', 'Anyone who fills in an online form'],
         'a': 'B', 'why': 'They have the problem now, so they can describe what really happens.'},
        {'q': 'What is an early adopter?',
         'o': ['Someone who likes new phones', 'Someone who has the problem, knows it, has tried to solve it and can spend on it', 'A close friend', 'An investor'],
         'a': 'B', 'why': 'These people feel the problem most and are most likely to try something new.'},
        {'q': 'Why write three learning goals before interviewing?',
         'o': ['To impress people', 'So every question serves something you actually need to learn', 'The law requires it', 'To make interviews longer'],
         'a': 'B', 'why': 'Goals keep interviews short and focused.'},
        {'q': 'After 10 interviews, every story is very different. What does that suggest?',
         'o': ['Stop interviewing', 'Your customer group is too broad, so narrow it', 'Everyone loves your idea', 'Raise your price'],
         'a': 'B', 'why': 'A good target group shares the same problem, so their stories start to repeat.'},
    ],
    study='"How To Talk To Users", two Steve Blank lessons and the DPDP consent section (about 1.5 hours)',
    action='list 15 people with the problem, send 10 requests and complete 3 interviews',
)

L2 = lesson(
    3, 2,
    title='Ask unbiased questions and take good notes',
    weeks=(6, 6), hours=6,
    outcome='Run interviews that reveal what people actually do rather than polite opinions, take structured notes, and reach at least 10 interviews in total.',
    split='1.5 hours study, 4.5 hours action with at least 7 more interviews',
    core="""
People are kind. If you ask "Is this a good idea?", most will say yes, especially in a small town where everyone knows everyone. That kindness is useless as evidence. Good interviews ask about real past behaviour, because the past doesn't flatter you the way predictions do.

Rob Fitzpatrick's book *The Mom Test* (a paid book; you don't need it) sums up three rules:

1. Talk about their life, not your idea.
2. Ask about specific things that happened in the past, not opinions about the future.
3. Talk less and listen more.

### Bad questions and better ones

| Don't ask | Ask instead |
| --- | --- |
| Would you buy this? | Tell me about the last time this happened. |
| Do you think it's a good idea? | What did you do about it? |
| How much would you pay? | What have you spent on solving it so far? |
| Would you use an app for this? | What have you tried? What didn't work? |
| Is this a problem for you? | How often does it happen? What does it cost you? |
| Do you like this design? | What happens if you don't solve it? |

### Sort what you hear

- **Compliments** ("Nalla idea aanu!", "That's a great idea"): polite. Ignore them.
- **Fluff** ("I usually…", "I would probably…", "Everyone needs this"): vague or hypothetical. Ask for a specific example.
- **Facts** ("Last Saturday I got 40 messages and replied to 12"): this is data.
- **Commitments:** their time ("Come back and show me"), their reputation ("Talk to my brother, he has two shops") or their money ("I'll pay ₹500 to try it"). These are the strongest evidence of all.

### A 20-minute interview guide

1. **Warm-up (2 minutes):** thank them, repeat that you are not selling, ask about their work or study.
2. **Context (5 minutes):** "Walk me through a normal week. Where does [topic] fit in?"
3. **The last time (8 minutes):** "Tell me about the last time [problem] happened." Then: what happened next, what they did, who helped, how long it took, what it cost.
4. **Workarounds and spending (3 minutes):** "What have you tried? What do you pay for now?"
5. **Close (2 minutes):** "Is there anything I should have asked? Who else should I talk to? Can I come back when I have something to show?"

To dig deeper, use: "Why was that hard?", "Can you show me?", "What happened then?", "Can you give me an example?"

### Notes you can use later

Write notes within an hour, while you still remember the exact words. Keep facts, quotes and your own ideas in separate columns. Tag each note so you can count patterns later, for example #late-replies, #family-helps, #pays-now. Write down every number you hear.
""",
    example="""
Nisha asked two mothers about birthday cakes. Compare her first interview with her second.

**First (unhelpful):** "I'm starting a home bakery with no artificial colours. Would you order from me?" "Oh yes, definitely! Very good idea." Nisha felt great, and learned nothing.

**Second (useful):** "Tell me about the last birthday cake you bought." "For my daughter's birthday in August. I ordered from a bakery in Vatakara, ₹900 for 1 kg. My husband went to collect it; that was an hour there and back." "How did you choose that bakery?" "My sister-in-law recommended it. It looked nice, but my daughter said it was too sweet, and the colour stained her mouth." "What did you do about that?" "Nothing. There's no other good option nearby."

Now Nisha knows what people pay (₹900), the hidden cost (an hour of travel), how they choose (recommendations) and a real complaint (too sweet, artificial colour). All facts, no compliments.
""",
    resources=[
        ('yc-users', 'Re-watch the part on what to ask, then compare it with the guide above', '10 min'),
        ('blank-udacity', 'Lessons "Value Proposition" and "Customer Segments"', 'about 1 hour'),
        ('os8', 'Section 8.2 Market Research, Market Opportunity Recognition, and Target Market', '20 min'),
    ],
    steps=[
        'Copy the interview guide and the notes template onto your phone (Google Keep or Docs).',
        'Do at least 7 more interviews this week, so you reach at least 10 in total. Mix in-person and phone interviews if you need to.',
        'In each one, ask about the last time the problem happened, what they did and what it cost. Don\'t describe your idea until the final two minutes, and only if they ask.',
        'Fill in the notes template within an hour of each interview, and tag it.',
        'At the end of the week, count how many people have the problem, how often, what they do now and how many already pay for a workaround.',
    ],
    proof='Notes for at least 10 interviews in the Interviews tab, each tagged, plus your counts.',
    templates=[
        ('pocket interview guide', """
INTERVIEW GUIDE (20 minutes)
Warm-up: Thank you. I'm not selling anything.
  Tell me about your work / your study.
Context: Walk me through a normal week.
  Where does [topic] fit in?
The last time: Tell me about the last time [problem]
  happened.
  - What happened next? What did you do?
  - Who helped? How long did it take? What did it cost?
Workarounds: What have you tried? What do you pay for now?
Close: What should I have asked? Who else should I talk
  to? Can I come back when I have something to show you?
Dig deeper: Why was that hard? Can you show me?
  Can you give me an example?
""", ''),
        ('interview notes (paste into the Interviews tab)', """
Code,Date,Who (role and place),Had the problem in the last month? (Y/N),How often,Last-time story (facts),What they did,What it cost (time or money),Pays for a workaround now? (amount),Best quote,Commitment offered,Tags,My own thoughts
S1,,,,,,,,,,,,
""", 'csv'),
    ],
    mistakes=[
        ('Leading questions.', '"Don\'t you hate it when…?" puts words in their mouth. Ask "What happened last time?" instead.'),
        ('Asking about the future.', '"Would you…?" gets guesses. "When did you last…?" gets facts.'),
        ('Not asking about money.', 'If they already spend on the problem, that is your best evidence. Ask what they pay now.'),
        ('Writing notes the next day.', 'By then you remember your own opinions, not their words. Write within an hour.'),
        ('Counting "yes, I\'d buy" as evidence.', 'Only past behaviour and real commitments count.'),
    ],
    quiz=[
        {'q': 'Which question gives the most reliable answer?',
         'o': ['Would you buy this?', 'How much would you pay?', 'Tell me about the last time this happened.', 'Is this a good idea?'],
         'a': 'C', 'why': 'It asks about real past behaviour, which people can\'t easily dress up.'},
        {'q': 'A shop owner says, "Super idea, everyone needs this!" What is that?',
         'o': ['A commitment', 'A fact', 'A compliment: polite, so ignore it', 'A pre-order'],
         'a': 'C', 'why': 'Compliments feel good but tell you nothing about behaviour or money.'},
        {'q': 'Which of these is a commitment?',
         'o': ['"I would probably use it"', '"Talk to my brother, he has two shops. I\'ll call him now."', '"Nice idea"', '"Everyone needs this"'],
         'a': 'B', 'why': 'They are putting their reputation and time on the line.'},
        {'q': 'When should you write your interview notes?',
         'o': ['Within an hour', 'At the end of the week', 'Only if the interview went well', 'There is no need; memory is enough'],
         'a': 'A', 'why': 'Exact words and numbers fade within hours.'},
        {'q': 'Why ask what people pay for a workaround now?',
         'o': ['To copy competitors', 'Current spending is the strongest sign the problem is worth money', 'To find out their income', 'It is polite'],
         'a': 'B', 'why': 'People who already pay for a poor solution may pay for a better one.'},
    ],
    study='the interview part of the YC talk, two Steve Blank lessons and OpenStax 8.2 (about 1.5 hours)',
    action='complete at least 7 more interviews (10 or more in total) with tagged notes and counts',
)

L3 = lesson(
    3, 3,
    title='Personas and jobs to be done',
    weeks=(7, 7), hours=4,
    outcome='Turn your interview notes into one evidence-based persona, three job statements and a clear definition of your early adopters.',
    split='1 hour study, 3 hours action',
    core="""
You now have notes from 10 or more people. This lesson turns them into a clear picture of who you serve and what they are trying to get done.

### Find the patterns

1. Put all your notes in one sheet, one row per interview.
2. Group the tags. Which ones appear again and again?
3. Count them. "7 of 11 shop owners reply to evening messages after 9 pm" is a pattern. "One person said…" is an anecdote.
4. Note the surprises: anything that contradicts what you believed before.

### Build a persona from evidence

A **persona** is a short profile of a typical customer, built only from what your interviews showed. Give it a name so it is easy to talk about, but make sure every detail can be traced to real notes:

- Who they are: role, place and situation, not just age and gender
- What they are trying to achieve
- The problem, how often it happens and what it costs
- What they do today and what they pay for it
- Where they get information and whom they trust
- How they decide and how they pay
- Two or three real quotes

### Jobs to be done

The Jobs to Be Done idea, from Clayton Christensen's work, says people don't simply buy products: they "hire" them to make progress in a particular situation. In the well-known milkshake example, morning commuters hired a milkshake to make a long, boring drive bearable, so its real competition was bananas and bagels, not other milkshakes.

Write job statements in this form:

**When [situation], I want to [motivation], so I can [expected outcome].**

A job has three sides: **functional** (get the task done), **emotional** (how they want to feel) and **social** (how they want others to see them). A good offer serves all three.

### Choose your first customers: the beachhead

You can't serve everyone at first. MIT's Bill Aulet calls your first narrow target market the **beachhead**: a group whose members share the same problem, buy in the same way and talk to each other. Win them first, then expand. Your **early adopters** are the most eager people inside that group. Write down what makes someone an early adopter, so you can find more of them.
""",
    example="""
A persona for ShopAssist, built from 11 interviews (every detail comes from the notes; the person is made up):

**Rasheed, 45, owns a textile shop on Kuttiady's main road.** He has two staff. In the wedding season he gets around 40 WhatsApp enquiries a day; 8 of the 11 owners said evenings are the worst time. He replies after closing at 9 pm, by which time some customers have bought in Vatakara. His son, now working in Qatar, used to send photos and prices; since he left, nobody does it well. Rasheed trusts other shop owners and his supplier more than ads. He already pays ₹600 a month for billing software and decides alone on anything under about ₹2,000.

*Quote:* "If they don't get the price in ten minutes, they go to the next shop."

**Job statements**

1. When customers message me during the evening rush, I want them to get photos and prices quickly, so I don't lose the sale to another shop. *(functional)*
2. When I close the shop, I want my messages under control, so I can rest instead of replying till midnight. *(emotional)*
3. When customers compare shops, I want to look as modern as the big Vatakara shops, so they trust me. *(social)*

**Early adopters:** textile and mobile shop owners in Kuttiady and nearby towns who get 20 or more WhatsApp enquiries a day, lost a sale to a slow reply in the last month, and already pay for some software or help.
""",
    resources=[
        ('jtbd', 'Read the page, including the milkshake example', '15 min'),
        ('mit-390', 'Lecture 7: What is a Beachhead Market (length not listed)', 'budget 25 min'),
        ('os6', 'Section 6.3 Design Thinking', '20 min'),
    ],
    steps=[
        'Put all your interview notes in one sheet and count the tags.',
        'Write your top 3 patterns, each with a count and one quote.',
        'Fill in the persona card and three job statements, using only evidence from your notes.',
        'Write your early-adopter conditions in one sentence.',
        'Send a short persona summary (no names) to two people you interviewed and ask: "Does this sound like you? What is wrong?" Fix it using their replies.',
    ],
    proof='Your pattern counts, persona card, job statements, early-adopter sentence and the two replies.',
    templates=[
        ('persona card', """
PERSONA (every line must come from your interview notes)
Name and one line: ____________
Role, place, situation: ____________
Trying to achieve: ____________
Problem, how often, what it costs: ____________
What they do today, what they pay: ____________
Where they get information, whom they trust: ____________
How they decide and pay: ____________
Quotes:
1. "____________"
2. "____________"
Based on interviews: S__, S__, S__
""", ''),
        ('job statements and early adopters', """
JOB STATEMENTS
Functional: When ____, I want to ____, so I can ____.
Emotional:  When ____, I want to ____, so I can ____.
Social:     When ____, I want to ____, so I can ____.

EARLY ADOPTERS
People who ____, who ____ in the last month,
and who already ____.
Where I can find more of them: ____________
""", ''),
    ],
    mistakes=[
        ('Inventing personas.', 'If a detail isn\'t in your notes, it doesn\'t belong in the persona. Made-up personas lead to products nobody needs.'),
        ('Demographics only.', '"Women aged 25–40" says nothing about the problem. Describe situations and behaviour.'),
        ('Too many segments at once.', 'Pick one beachhead. You can expand once you have won it.'),
        ('Ignoring surprises.', 'Notes that contradict your belief are the most valuable ones you have.'),
    ],
    quiz=[
        {'q': 'Which of these is a pattern rather than an anecdote?',
         'o': ['"One owner said he hates WhatsApp"', '"8 of 11 owners said evenings are the worst time for messages"', '"I think owners are busy"', '"My uncle agrees with me"'],
         'a': 'B', 'why': 'A pattern is counted across many interviews.'},
        {'q': 'Complete the job statement: "When [situation], I want to [motivation], so I can [___]."',
         'o': ['price', 'expected outcome', 'competitor', 'persona name'],
         'a': 'B', 'why': 'The outcome is the progress the customer is trying to make.'},
        {'q': 'In the milkshake example, what was the real morning competition?',
         'o': ['Other milkshakes', 'Bananas, bagels and other things to eat on a long drive', 'Coffee shop prices', 'Television ads'],
         'a': 'B', 'why': 'Competition is whatever else customers could hire for the same job.'},
        {'q': 'What is a beachhead market?',
         'o': ['A tourist area', 'A narrow first group with the same problem, who buy the same way and talk to each other', 'The whole country', 'Your competitors\' customers'],
         'a': 'B', 'why': 'Winning one tight group first makes the next group easier.'},
    ],
    study='the Christensen JTBD page, the MIT beachhead lecture and OpenStax 6.3 (about 1 hour)',
    action='count your patterns and write a persona, job statements and early-adopter conditions, checked by two interviewees',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    3,
    title='Customer discovery',
    weeks=(5, 7), hours=18,
    overview="""
Customer discovery means talking to the people you hope will pay you, to learn how they live with the problem today. It is the cheapest way to avoid building something nobody wants. Steve Blank calls it "getting out of the building".

Over three weeks you plan, book and run at least 10 interviews, ask questions that get honest answers, and turn your notes into a persona and job statements based on what people actually said.
""",
    outcomes=[
        'Choose who to interview and find 15 people who have the problem now',
        'Run 15–20 minute interviews about past behaviour, without pitching or leading',
        'Take structured notes and count patterns across interviews',
        'Write an evidence-based persona, job statements and early-adopter conditions',
    ],
    lessons=LESSONS,
    project='Customer discovery report',
    project_steps=[
        'One page: how many interviews you did and with whom (use codes like S1 and S2, not names).',
        'Your top 3 patterns, each with a count ("7 of 11 said…") and one quote.',
        'Your persona, job statements and early-adopter conditions.',
        'What surprised you, and what you now believe was wrong in your hypothesis.',
        'Your decision: continue with this idea, adjust it (say how), or switch to a backup.',
    ],
    project_proof='Your one-page report in the Founder Toolkit folder, plus the interview notes in the Interviews tab.',
    rubric=[
        ('Interviews', 'Fewer than 5, mostly friends', '5–9, a mix of people', '10 or more, with people who have the problem now'),
        ('Question quality', 'Asked "would you buy?"', 'Mostly past behaviour, a few leading questions', 'Past behaviour, workarounds and spending; no pitching'),
        ('Notes', 'From memory, days later', 'Same day, but no tags', 'Within an hour, tagged, with quotes and numbers'),
        ('Synthesis', 'Opinions', 'Patterns without counts', 'Counted patterns, persona and jobs built from evidence'),
        ('Decision', 'None', 'Vague', 'A clear continue, adjust or switch, with reasons'),
    ],
    short=[
        'Do 6 interviews instead of 10 (3 in week 5 and 3 in week 6), by phone if you must.',
        'Use the interview guide exactly as written, and skip every reading except "How To Talk To Users".',
        'Write the persona and one job statement only.',
    ],
    mistakes=[
        ('Interviewing friends who don\'t have the problem.', 'Talk to people who had the problem in the last month.'),
        ('Pitching your idea during the interview.', 'No pitch until the final two minutes, if at all.'),
        ('Stopping at 3 interviews because "everyone agrees".', 'Patterns need 10 or more conversations.'),
    ],
)
