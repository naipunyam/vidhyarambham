from common import lesson, module, link, xref, table, Q
import tools

RULES = """**The rules (all must be true for every request):**
- Every request must be **legal, safe, respectful and low-stakes**.
- **Accept "no" immediately and politely.** Say "No problem, thank you!" and leave. Never ask twice, argue or bargain after a no.
- **Never pressure, deceive or harass anyone.** No fake stories, no pretending to be someone else, no filming people without their permission.
- **Never make requests that could make someone feel unsafe,** including **romantic or personal-space requests** (no asking for numbers, dates, hugs, touching, following someone, or approaching people who are alone in isolated places).
- **Respect local culture:** dress, time of day, religious places and customs, and who you approach (in many places in Kerala, approaching women you don't know with unusual requests can cause real discomfort; choose shops, counters, offices and public settings where requests are normal).
- **Low-stakes for them:** saying no must cost them nothing and saying yes must cost them very little (a minute, a small favour, a small discount they can refuse).
- **Stop if someone seems uncomfortable,** even if they said yes."""

LADDER = [
    # (level, request, where, why it helps)
    ('1', 'Ask a stranger for the time or directions, even if you know', 'Bus stand, junction', 'The easiest first contact'),
    ('1', 'Ask a shopkeeper which brand of a product they recommend and why', 'Grocery or hardware shop', 'Asking for opinions'),
    ('1', 'Ask a tea-shop owner for a recommendation of the best local snack', 'Tea shop', 'Starting small talk'),
    ('1', 'Ask a librarian to recommend a book on a topic you like', 'Public or panchayat library', 'Asking experts'),
    ('2', 'Ask for a small discount on a purchase ("Can you do a little better on the price?")', 'Textile or vegetable shop', 'Price conversations'),
    ('2', 'Ask a stranger at a bus stop for a recommendation (a good tailor, a mechanic)', 'Bus stop', 'Talking to strangers'),
    ('2', 'Ask a restaurant if you can have a dish that is not on the menu, or a half portion', 'Hotel or restaurant', 'Unusual but reasonable requests'),
    ('2', 'Ask a shop for a free sample or to taste before buying', 'Bakery, spice or sweet shop', 'Asking for something free'),
    ('2', 'Return or exchange an item politely, with your reason', 'Any shop', 'Standing up for yourself'),
    ('3', 'Ask a restaurant if you can see the kitchen', 'Restaurant (quiet hours)', 'A bolder request'),
    ('3', 'Ask a bank or post office clerk to explain a scheme in detail', 'Bank, post office', 'Taking up people\'s time politely'),
    ('3', 'Ask a stranger to take a photo of you at a public place', 'Beach, park, tourist spot', 'Asking help from strangers'),
    ('3', 'Ask a shop to give you a carry bag free or a little extra', 'Market', 'Small favours'),
    ('3', 'Ask a bookshop if you can sit and read for 15 minutes', 'Bookshop', 'Testing flexible rules'),
    ('3', 'Ask for a "loyal customer" price at a shop you use often', 'Regular shop', 'Negotiation through relationship'),
    ('3', 'Ask a senior aspirant or ex-PSC rank holder for one study tip', 'Library, coaching centre, online group', 'Asking for advice'),
    ('4', 'Ask an autorickshaw driver for a lower fare on a regular route (before getting in)', 'Auto stand', 'Negotiating in public'),
    ('4', 'Ask a local business owner what their biggest problem is (research, no pitch)', 'Small shop', 'Customer discovery'),
    ('4', 'Ask an expert (doctor, teacher, officer, engineer) for 10 minutes of career advice', 'By message or in person, by appointment', 'Networking'),
    ('4', 'Ask three people for honest feedback on your English or Malayalam speaking', 'Friends, relatives, study group', 'Asking for feedback'),
    ('4', 'Ask a stranger at an event what they do and how they got into it', 'Library event, seminar, wedding', 'Networking conversations'),
    ('4', 'Ask a hotel if you could use their wifi or a table to study for an hour for the price of a tea', 'Hotel, cafe', 'Creative requests'),
    ('4', 'Ask a school or college if you can attend one free public lecture or seminar', 'College office', 'Getting access'),
    ('5', 'Ask a shop owner if you can put up a small notice for your tuition or service', 'Shop, library notice board', 'Selling yourself'),
    ('5', 'Pitch a service to a local business (posters, social media posts, accounts help, tuition for their child)', 'Small business', 'Real sales'),
    ('5', 'Ask your employer or a client for a raise, a better rate or a better shift', 'Workplace', 'High-value asks'),
    ('5', 'Ask a local club or library if you can give a 5-minute talk', 'Club, library, residents\' association', 'Public speaking'),
    ('5', 'Ask a respected local person to mentor you for one hour a month', 'By appointment', 'Mentorship'),
    ('5', 'Ask a newspaper, local channel or community page if they would feature a community event you help with', 'Office or message', 'Media and outreach'),
    ('5', 'Ask a stranger to join you in a small good act (picking up litter, donating blood together)', 'Public place', 'Leading others'),
    ('5', 'Ask five people in a row for something unusual but harmless (e.g. to recommend a book, write it on paper and sign it)', 'Market or event', 'Volume and resilience'),
    ('5', 'Ask a business for a paid trial task or a small contract', 'Small business, startup, office', 'Turning rejection skills into income'),
    ('5', 'Ask an audience for questions at the end of your talk', 'Your talk', 'Inviting judgement'),
]

L1 = lesson(
    14, 1,
    outcome='You can explain what rejection therapy is, where it came from, why it may work (exposure and desensitisation), and what the evidence does and does not show.',
    split='20 minutes reading, 25 minutes including the TED talk',
    principle='Fear of rejection shrinks when you deliberately collect small, safe "no"s; each one teaches your brain that rejection is survivable and often not about you.',
    science=f"""
**The original game.** Rejection Therapy was created by **Jason Comely**, a Canadian who, after a painful break-up, found himself avoiding people. He set himself a rule: get rejected by someone every day. He turned it into a self-help game, with optional suggestion cards, in which the "win" is being rejected, not getting a yes ({link('wp-rejection', 'background')}).

**Jia Jiang's 100 days.** In 2012, Jia Jiang, a Chinese-born entrepreneur in the United States, discovered the game after an investor rejected his startup and he realised how much fear of rejection controlled him. He set himself **100 days of rejection** and filmed them: asking a stranger to lend him $100, asking for a "burger refill", asking to play football in a stranger's back garden, and, most famously, asking a Krispy Kreme doughnut shop to make doughnuts linked like the Olympic rings, which the employee did. His TEDx talk (2015) describes what he learned: people say yes far more often than we fear; asking "Why?" after a no often opens a conversation; and rejection says as much about the other person's situation as about you. He later bought the Rejection Therapy brand (2016) ({link('ted-jiang', 'TED talk')}).

**The psychology: exposure and desensitisation.** Rejection therapy is a **fear ladder for rejection** (PD-M13-L02). Fear of rejection makes us avoid asking; avoidance keeps the fear strong. Deliberately seeking small rejections:
1. **Tests the feared prediction** ("If they say no, I'll be humiliated") and shows it is wrong or bearable (inhibitory learning).
2. **Reduces the fear response** through repeated contact (habituation).
3. **Builds self-efficacy** for asking (mastery experiences, PD-M13-L01).
4. **Corrects the spotlight effect:** most people forget your request within minutes.

**What the evidence shows, honestly.** There are **no controlled clinical trials of rejection therapy itself.** Its support is **indirect**: exposure therapy has strong evidence for social anxiety, and studies of asking show people underestimate how often others will say yes. In experiments by Francis Flynn and Vanessa Lake (2008), people asking strangers for favours (filling in a questionnaire, borrowing a phone) predicted they would need to ask about twice as many people as they actually did to get the yeses they needed. So treat rejection therapy as a **practical tool built on strong principles**, not a proven treatment.

**What it is not.** It is not about pushing people until they give in, tricking them, or collecting stunts for social media. Done that way, it becomes harassment. The rules in PD-M14-L02 are part of the method.
""",
    evidence=[
        ('Exposure reduces social fears', 'strong', 'Well-established for social anxiety as part of CBT.'),
        ('People underestimate how often others say yes to requests', 'moderate', 'Several experiments by Flynn, Lake, Bohns and colleagues.'),
        ('Rejection therapy as a specific method', 'tool', 'No controlled trials; a practical application of exposure principles.'),
        ('Jia Jiang\'s experience as evidence', 'mixed', 'One person\'s story: inspiring, but not research.'),
    ],
    example="""
Ashiq watches Jia Jiang's talk and laughs at the doughnut story, then feels the fear in his own stomach: he has wanted to offer tuition to students in his ward for a year, but cannot bring himself to ask parents. "What if they say no? What if they tell others I'm desperate?"

He writes his feared prediction: "If I ask and they say no, I'll feel humiliated for days, and people will gossip." Then he notices that he has been rejected many times already (by PSC short lists, by a girl in college, by a job interview) and survived each time. He also realises his fear is not of asking a shopkeeper for the time; it is of **asking for something that matters to him**. That tells him where his ladder should end.

He decides to start the challenge the following Monday (a fresh start), with simple requests at shops, and to aim, by day 30, at asking three parents about tuition.
""",
    apply="""
**Why "aim for a no" works:** if your goal is a yes, every no is a failure and you will avoid asking. If your goal is to **ask**, every request, yes or no, is a success. This takes the pressure off and keeps you practising.

**Three things to try after a no** (from Jiang's experience, used politely and only once):
1. **Thank them** sincerely.
2. If it feels right, **ask "Could I ask why?"** with curiosity, not argument. You often learn something useful ("We can't show the kitchen during lunch rush; come at 4").
3. **Accept and leave.** No second ask.

**Rejection is information, not a verdict.** A no can mean: not now, not this way, not me (the person can't), or not interested. Only rarely does it mean "not you as a person".

**With others:** notice how you say no. A kind, clear no ("I can't, but thanks for asking") is a gift to people practising courage. You will learn to say no well in PD-M26-L02.
""",
    resources=[
        ('ted-jiang', 'Watch the whole talk; write down his three lessons', '15 minutes'),
        ('wp-rejection', 'Read the article: origin, Jiang\'s project and how it is described', '5 minutes'),
        ('os-12', 'Read 12.4 Conformity, Compliance, and Obedience, the part on compliance (why people say yes to requests)', '15 minutes'),
    ],
    steps=[
        'Watch Jia Jiang\'s talk and write his three main lessons in your own words.',
        'Write your rejection history: five times you were rejected, how you felt then, and how you feel about each now.',
        'Write your main feared prediction about rejection and the request you most avoid making.',
        'Do one Level 1 request from the ladder in PD-M14-L02 (for example, ask a shopkeeper which brand they recommend). Write what happened.',
    ],
    proof='Jiang\'s three lessons, your five-item rejection history, your feared prediction, and one Level 1 request with its result.',
    templates=[('Rejection history and prediction', """REJECTION HISTORY
When | What I asked or wanted | How I felt then (0-10) | How I feel now (0-10) | What I learned
1. ______ | ______ | __ | __ | ______
...
MY FEARED PREDICTION: "If I ask ______ and they say no, then ______."
The request I most avoid making: ______________________
Jiang's three lessons (my words): 1 ______ 2 ______ 3 ______""", '')],
    mistakes=[
        ('Treating it as a prank or content stunt.', 'The aim is your courage, not their discomfort or your followers.'),
        ('Thinking it is proven therapy.', 'It is a practical tool built on exposure principles; there are no trials of it as such.'),
        ('Starting with the request that matters most.', 'Start at Level 1 and climb.'),
        ('Taking every no personally.', 'Most no\'s are about timing, rules or the other person\'s situation.'),
    ],
    quiz=[
        Q('Who created the Rejection Therapy game?', 'Jason Comely', 'Jia Jiang', 'Albert Bandura', 'Dale Carnegie', why='Comely created it; Jiang made it famous with 100 days of rejection.'),
        Q('What is the main psychological principle behind rejection therapy?', 'Exposure: facing a feared situation gradually so the fear shrinks', 'Hypnosis', 'Positive affirmations', 'Ego depletion', why='It is a fear ladder for rejection.'),
        Q('What did Flynn and Lake find about asking strangers for favours?', 'People predicted needing about twice as many asks as they actually did to get yeses', 'Strangers almost never help', 'People overestimate how often others say yes', 'Asking makes people angry', why='We underestimate others\' willingness to help.'),
        Q('What is the honest evidence status of rejection therapy?', 'No controlled trials; indirect support from exposure and asking research', 'Proven by many clinical trials', 'Shown to be harmful', 'Evidence comes only from animals', why='It is a practical tool, not a tested treatment.'),
    ],
    study='read the lesson and watch Jia Jiang\'s TED talk',
    action='write your rejection history and feared prediction, and make one Level 1 request',
)

ladder_rows = [(lvl, req, where, why) for lvl, req, where, why in LADDER]
assert len(LADDER) >= 30

L2 = lesson(
    14, 2,
    outcome='You can apply the safety and respect rules to every request and choose requests from a 33-step ladder realistic for Kerala.',
    split='20 minutes reading, 25 minutes of planning',
    principle='Courage practice is only good if it is good for the other person too: every request must be legal, safe, respectful and low-stakes, and every "no" must be accepted at once.',
    science=f"""
**Why the rules are part of the method.** Exposure works when the feared situation is faced **in a way that is safe**. For rejection, that means two kinds of safety:

1. **Safety for the other person.** A request that makes someone feel pressured, tricked, watched or unsafe is not courage practice; it is harassment. Research on compliance shows that people often find it **hard to say no** to direct requests. Vanessa Bohns's studies found that people agreed to unethical or uncomfortable requests (such as vandalising a library book) far more often than the askers predicted, because refusing feels awkward. That means the asker holds more power than they feel, and must use it carefully: **make it easy to say no.**
2. **Safety for you.** Requests that could lead to conflict, legal trouble or danger (asking to enter private property, approaching people at night in isolated places, anything with money transfers or personal data) teach the wrong lesson and can hurt you.

**Low-stakes means:** saying no costs them nothing, saying yes costs them very little, and nothing bad happens to either of you whatever the answer.

**Culture.** What is a normal request differs by place. In Kerala, bargaining is normal in markets and many small shops but not in supermarkets, pharmacies or hospitals; asking strangers for directions is normal; approaching women you don't know with unusual requests can cause real fear; religious places have their own norms; and gossip travels fast in small towns. Choose settings where requests are expected (shops, counters, offices, events) and behave as a polite customer or visitor would.

{RULES}

**Before every request, run the rules check** in the rejection log (PD-M14-L03). If any box is not ticked, choose another request.
""",
    evidence=[
        ('People find it hard to refuse direct requests', 'moderate', 'Studies by Bohns and others show askers underestimate compliance.'),
        ('Exposure should be safe and chosen', 'strong', 'A basic principle of exposure therapy.'),
        ('A graded ladder from easy to hard', 'strong', 'Graded exposure is standard practice for anxiety.'),
        ('The specific 33-step ladder', 'tool', 'Written for this course; adjust it to your town.'),
    ],
    example=f"""
Sreeja plans her first week. She crosses out "ask a stranger for their phone to make a call": it could worry people about theft or scams. She keeps "ask the bakery to taste a new snack before buying" and "ask the librarian for a recommendation".

Her cousin suggests a "funny" request: asking a girl at the bus stop to dance. Sreeja says no: it is a personal and romantic-type request, it could make the girl feel unsafe, and it would break two rules. Instead, she adds "ask an older man at the bus stop where to find a good tailor", which is normal, public and easy to refuse.

On day 3, she asks a textile shop for a discount on a churidar set. The owner says no, fixed price. She says, "No problem, thank you!" and leaves. Her fear before was 6/10; after, 3/10. Lesson: "A fixed-price shop isn't rejecting me; it's their rule."
""",
    apply=f"""
**The 33-step ladder (Level 1 easiest, Level 5 hardest).** Use it as a menu. Swap in requests that fit your town, as long as they pass the rules check.

{table(['Level', 'Request', 'Where', 'Builds'], ladder_rows)}

**How to choose each day:**
- Week 1: Levels 1–2. Week 2: Levels 2–3. Week 3: Levels 3–4. Week 4: Levels 4–5.
- Repeat a level until fear before a request is about 3/10 or less, then move up.
- Mix in requests linked to your goals: speaking (Level 5 talk), networking (expert advice), income (pitching a service).

**Phrasing that keeps it easy to say no:**
- "Would it be possible to…? It's completely fine if not."
- "I'm practising asking for things; would you mind if…?" (honest, and people often warm to it).
- "Can you do a little better on the price? If not, that's fine."
""",
    resources=[
        ('os-12', 'Re-read 12.4 on compliance techniques (foot-in-the-door, door-in-the-face) so you can recognise them and not misuse them', '15 minutes'),
        ('ted-jiang', 'Re-watch the section on asking "why" after a no', '5 minutes'),
    ],
    steps=[
        'Copy the rules into your rejection log note.',
        'Go through the 33-step ladder: cross out any request that doesn\'t fit your town or culture and add at least three of your own that pass the rules check.',
        'Plan your first seven requests (Levels 1–2), with day, place and exact words.',
        'Show your plan to one trusted person and ask: "Would any of these make someone uncomfortable?" Adjust.',
    ],
    proof='Your rules note, your edited ladder (with three of your own requests), the seven-day plan with exact words, and the trusted person\'s comment.',
    templates=[('Request planner', """REQUEST PLANNER (week ___)
Day | Level | Request (exact words) | Where | Rules check (legal / safe / respectful / low-stakes / easy no / not romantic or personal / fits culture) | Fear prediction (0-10)
1 | __ | "______________________" | ______ | [ ][ ][ ][ ][ ][ ][ ] | __
...
Easy-no phrases: "It's completely fine if not." "If not, no problem."
After a no: "No problem, thank you!" -> leave. Never ask twice.""", '')],
    mistakes=[
        ('Choosing requests that embarrass the other person.', 'The discomfort should be yours (asking), not theirs (being put on the spot).'),
        ('Asking again after a no, or arguing.', 'That turns practice into pressure. One ask, accept, leave.'),
        ('Requests involving money transfers, phones or personal data.', 'They trigger scam fears and can harm both of you. Avoid them.'),
        ('Ignoring local norms.', 'Bargaining in a pharmacy or making requests at a place of worship can offend. Choose normal settings.'),
    ],
    quiz=[
        Q('Which request breaks the rules?', 'Asking a woman you don\'t know at a bus stop for her phone number', 'Asking a shopkeeper for a small discount', 'Asking a librarian for a recommendation', 'Asking a restaurant for a half portion', why='Romantic or personal requests can make people feel unsafe.'),
        Q('What should you do after a "no"?', 'Say "No problem, thank you!" and leave', 'Ask again more firmly', 'Explain why they are wrong', 'Ask their manager', why='Accept every no immediately and politely.'),
        Q('Why must requests be easy to refuse?', 'People often find it hard to say no, so the asker must make refusal easy', 'To get more yeses', 'It doesn\'t matter', 'Because the law says so', why='Askers hold more power than they feel (Bohns).'),
        Q('When should you move up a level?', 'When your fear before a request is about 3/10 or less', 'After every request', 'Only after 30 days', 'When someone says yes', why='Graded exposure: repeat until manageable, then climb.'),
    ],
    study='read the lesson and the rules, and edit the ladder for your town',
    action='write your rules note, edit the ladder, and plan seven requests with exact words, checked by a trusted person',
)

L3 = lesson(
    14, 3,
    outcome='You can run a 30-day rejection challenge with a daily log, add five comfort-zone challenges, and use the skill in sales, networking and public speaking.',
    split='15 minutes reading, 5 to 15 minutes a day for 30 days',
    principle='Thirty days of small, safe requests turn asking into a habit; the same courage then transfers to selling, networking and speaking in public.',
    science=f"""
**Why 30 days?** Thirty days is not a magic number; it is long enough to climb a ladder from easy to hard requests, to see your fear ratings fall, and to make asking feel normal. Habit research suggests automaticity takes longer (a median of about 66 days, PD-M08-L02), so treat day 30 as the end of the training phase, not the end of asking.

**What to measure.** The daily log records five things: **the request, fear before (0–10), the result, fear after (0–10) and the lesson.** Over 30 days you should see (a) fear before falling, (b) the gap between fear before and after (anticipation is usually worse than the event), and (c) your yes-rate: often **higher** than you expected, consistent with the research on underestimating compliance (PD-M14-L01).

**Transfer to real life:**
- **Sales:** most sales involve hearing no many times. Salespeople who treat a no as information ("not now", "not this", "not me") keep going and learn. The {xref('ent', 'ent-m07', 'Entrepreneurship course sales module')} teaches the process; rejection practice gives you the nerve.
- **Networking:** asking an expert for 10 minutes, introducing yourself at an event, following up after a meeting (Module 31).
- **Public speaking:** the core fear is being judged (Module 27). Requests in front of others are a stepping stone.

**Comfort-zone challenges.** Five extra challenges, done at least once each during the 30 days:
1. **Talk to one new person a day** for a week (a neighbour you've never spoken to, a shopkeeper, a person at the library).
2. **Speak up in a group** (study group, family meeting, residents' association): one question or one idea.
3. **Post a short video of yourself** (on your WhatsApp status or a private group first), talking for 30–60 seconds about something you learned.
4. **Eat alone at a restaurant** without your phone for the first 10 minutes.
5. **A digital-detox day:** a whole day with your phone off except for calls (prepared in Module 16).

These are exposures to being **seen**, **judged** or **alone with yourself**, the cousins of rejection.
""",
    evidence=[
        ('Anticipated distress is usually higher than actual distress in feared social situations', 'moderate', 'Common finding in exposure and social anxiety research.'),
        ('People underestimate others\' willingness to say yes', 'moderate', 'Several experiments on help-seeking.'),
        ('Courage transfers from practice requests to sales and networking', 'tool', 'Plausible from exposure and self-efficacy research; not directly tested.'),
        ('Comfort-zone challenges', 'tool', 'Practical exposures to being seen and judged.'),
    ],
    example="""
Ashiq's 30-day log, selected days:

| Day | Request | Fear before | Result | Fear after | Lesson |
| --- | --- | --- | --- | --- | --- |
| 1 | Ask the tea-shop owner for his best snack | 3 | Yes, chatted 5 min | 1 | People like being asked for advice |
| 5 | Ask for ₹50 off a ₹650 shirt | 6 | No, fixed price | 3 | No about the rule, not me |
| 11 | Ask a hotel to show the kitchen | 7 | Yes, at 4 pm | 3 | Timing matters |
| 17 | Ask a retired headmaster for 10 minutes of career advice | 8 | Yes, gave 40 minutes | 2 | Experts enjoy helping |
| 23 | Ask a stationery shop to display my tuition notice | 7 | Yes | 3 | Locals support locals |
| 28 | Ask three parents about tuition for their children | 9 | 1 yes, 2 "next term" | 4 | "Not now" is not "no" |

His averages: fear before fell from about 6 in week 1 to about 4 in week 4; his yes-rate was about 55%. By day 30 he has one tuition student, earning ₹1,500 a month, and three parents who said "next term".
""",
    apply=f"""
**The 30-day rejection challenge:**
1. **One request a day,** from your edited ladder, passing the rules check.
2. **Log it the same day:** request, fear before, result, fear after, lesson.
3. **Climb weekly:** Levels 1–2 → 2–3 → 3–4 → 4–5.
4. **Weekly numbers** (Sunday reflection): average fear before and after, yes-rate.
5. **Comfort-zone challenges:** do each of the five at least once during the 30 days, logged in the same note.
6. **Day 30:** compare week 1 and week 4, and write how you will use asking in sales, networking or speaking.

**Bad days:** a Level 1 request counts. Never miss twice.

**With others:** if a friend wants to join, do it together but make separate requests; never gang up on one person, and never film people without consent.
""",
    resources=[
        ('ted-jiang', 'Re-watch the last five minutes (what he learned about himself)', '5 minutes'),
        ('loop', 'Add "Rejection request (one a day)" with a reminder', '5 minutes'),
    ],
    steps=[
        'Add the challenge to Loop and start on a fresh-start day.',
        'Make and log one request a day for 30 days.',
        'Complete each of the five comfort-zone challenges at least once and log them.',
        'On day 30, write your numbers (fear before and after, yes-rate, week 1 versus week 4) and a paragraph on using this in sales, networking or speaking.',
    ],
    proof='Your 30-day rejection log, five comfort-zone entries, your day-30 numbers and the transfer paragraph.',
    templates=[('30-day rejection log', tools.REJECTION_LOG + """

COMFORT-ZONE CHALLENGES (each at least once)
[ ] New person a day for a week   [ ] Speak up in a group   [ ] Post a 30-60 s video of myself
[ ] Eat alone at a restaurant (no phone for 10 min)   [ ] Digital-detox day
Date | Challenge | Fear before | What happened | Fear after | Lesson""", '')],
    mistakes=[
        ('Collecting only yeses.', 'If everything is a yes, your requests are too easy. Aim for some no\'s.'),
        ('Skipping the log.', 'The numbers show progress your feelings miss.'),
        ('Breaking the rules for a bigger thrill.', 'The challenge only works if it is respectful and safe.'),
        ('Stopping completely after day 30.', 'Keep one real ask a week tied to your goals.'),
    ],
    quiz=[
        Q('What five things does the daily rejection log record?', 'Request, fear before, result, fear after, lesson', 'Time, place, weather, mood, food', 'Only yes or no', 'Names and phone numbers', why='These show fear falling and lessons building.'),
        Q('What do people usually find about fear before and after a request?', 'Fear before is usually higher than fear after', 'Fear after is always higher', 'They are always the same', 'Fear disappears on day 1', why='Anticipation is usually worse than the event.'),
        Q('How does rejection practice help in sales?', 'It helps you treat "no" as information and keep asking', 'It guarantees sales', 'It teaches you to pressure customers', 'It has no connection', why='Sales involves many no\'s; courage keeps you learning.'),
        Q('Which is a comfort-zone challenge from this lesson?', 'Eating alone at a restaurant without your phone for 10 minutes', 'Asking strangers for money', 'Following people home', 'Arguing with a shopkeeper', why='It is an exposure to being seen alone.'),
    ],
    study='read the lesson and set up the 30-day log',
    action='complete the 30-day rejection challenge and the five comfort-zone challenges, and write your day-30 numbers',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    14,
    overview=f"""
A full rejection-therapy programme: the idea and the psychology (exposure and desensitisation), Jason Comely's original game and Jia Jiang's 100 days, strict safety and respect rules, a 33-step ladder realistic for Kerala, a 30-day challenge with a daily log, five comfort-zone challenges, and how the courage transfers to sales, networking and public speaking.

Fear of rejection quietly decides a lot: the tuition you never offered, the expert you never messaged, the raise you never asked for, the question you never asked in class. This module turns that fear into a skill you practise daily for a month.

It is built on exposure, one of the best-supported methods in psychology, but rejection therapy itself has not been tested in trials, so you will measure your own results. **The rules are part of the method:** every request must be legal, safe, respectful and low-stakes; every no is accepted at once; nothing romantic or personal; local culture respected.
""",
    outcomes=[
        'Explain rejection therapy, its origins and the honest evidence behind it.',
        'Apply the safety and respect rules to every request.',
        'Choose and adapt requests from a 33-step ladder.',
        'Complete a 30-day rejection challenge with a daily log and numbers.',
        'Complete five comfort-zone challenges and connect the skill to sales, networking and speaking.',
    ],
    lessons=LESSONS,
    project='the 30-day rejection challenge',
    project_steps=[
        'Plan with the rules and the ladder (PD-M14-L02).',
        'Run the 30-day challenge and the five comfort-zone challenges (PD-M14-L03).',
        'Make at least three requests linked to a real goal (income, networking, speaking).',
        'Write a one-page report: numbers, the most surprising yes, the most useful no, and how you will keep asking.',
    ],
    project_proof='Your 30-day log, the comfort-zone entries and the one-page report.',
    rubric=[
        ('Consistency', 'Fewer than 15 requests', '15 to 24 requests', '25 to 30 requests over the month'),
        ('Climbing', 'Stayed at Level 1', 'Reached Level 3', 'Reached Level 4 or 5 with goal-linked requests'),
        ('Respect', 'Any rule broken', 'Rules followed but some awkward choices', 'Every request passed the rules check'),
        ('Learning', 'No numbers', 'Some numbers', 'Fear before and after, yes-rate and lessons over four weeks'),
    ],
    short=[
        'Do 10 requests over 30 days (one every three days), still logged.',
        'Do two of the five comfort-zone challenges.',
    ],
    flashcards=[
        ('Who created Rejection Therapy?', 'Jason Comely; Jia Jiang made it famous with 100 days of rejection.'),
        ('Psychological principle', 'Exposure: facing small rejections gradually so the fear shrinks.'),
        ('Evidence status', 'No trials of the method itself; indirect support from exposure and asking research.'),
        ('Core rule after a no', '"No problem, thank you!" and leave. Never ask twice.'),
        ('Requests never allowed', 'Illegal, unsafe, deceptive, pressuring, romantic or personal-space requests.'),
        ('Daily log fields', 'Request, fear before (0–10), result, fear after, lesson.'),
        ('Why aim for a no?', 'Asking becomes the success, so you keep practising.'),
        ('Five comfort-zone challenges', 'New person daily, speak up in a group, post a video, eat alone, digital-detox day.'),
    ],
    mistakes=[
        ('Turning it into social-media content.', 'Filming people without consent breaks the rules and their trust.'),
        ('Pushing for yes.', 'That is pressure, not practice.'),
        ('Never connecting it to real goals.', 'Make some requests count: a pitch, an expert, a talk.'),
    ],
    tools=[
        'The rejection history and feared prediction (PD-M14-L01).',
        'The rules, the 33-step ladder and the request planner (PD-M14-L02).',
        'The 30-day rejection log with comfort-zone challenges (PD-M14-L03).',
    ],
    playbook=[
        'I ask. A no is information: not now, not this, not me. I accept it politely and once.',
        'Every request is legal, safe, respectful, low-stakes and easy to refuse.',
        'I make one real, goal-linked ask every week.',
    ],
)
