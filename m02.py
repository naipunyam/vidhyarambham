from common import lesson, module

L1 = lesson(
    2, 1,
    title='Find real problems worth solving',
    weeks=(3, 3), hours=3,
    outcome='Collect 20 real problems from your town, your own life and online groups, written as clear problem statements.',
    split='1 hour study, 2 hours action',
    core="""
Many beginners start with a solution ("I'll make an app for…") and then look for people who need it. It works much better the other way round. Find a problem people already have, already spend time or money on, and would be glad to see solved. Then build the business around it.

### Where problems hide

- **Your own life.** What annoys you every week? Paul Graham's advice is to look first at problems you have yourself, because you already understand them.
- **People around you.** Shop owners, farmers, students, parents, elders, families with someone working in the Gulf. Ask what wastes their time or money.
- **Complaints.** One-star and two-star Google Maps reviews of local businesses are a list of unmet needs. So are the complaints that repeat in WhatsApp and Facebook groups.
- **Queues and workarounds.** A queue, a handwritten notice, a relative who "helps out every evening": each one is a problem being solved badly.
- **Boring jobs.** Paul Graham calls it schlep blindness: people overlook problems because the work looks dull, like paperwork, follow-ups or online applications. Dull problems often pay well, because few people want to solve them.

### What makes a problem worth solving

| Test | Good sign | Bad sign |
| --- | --- | --- |
| Frequency | Happens every week or every season | Once in a lifetime |
| Pain | Costs money, sales, time or sleep | "It would be nice" |
| Current spending | People already pay, or spend hours on a workaround | Nobody does anything about it |
| Reach | You can talk to 20 of these people this month | You don't know any of them |
| Growth | More people will have it next year | It is disappearing |

### Write it as a problem statement

Use this shape: **[Who] struggles to [do what] because [why]. It costs them [time, money or stress]. Today they [workaround].**

For example: "Textile shop owners in Kuttiady struggle to reply to WhatsApp enquiries in the evening rush because they are at the counter. They lose sales to shops that reply faster. Today a family member replies late at night."

To dig deeper, ask "why?" up to five times. "Why do you reply late?" "Because I'm billing." "Why can't someone else reply?" "Because only I know the prices." Now you have found the real problem: the prices live only in the owner's head.
""",
    example="""
In one week, Arun logged problems like these (the people are made up; the patterns are common):

1. Textile and mobile shops get dozens of WhatsApp enquiries in the evening and reply hours later, after customers have bought elsewhere. (Heard from three shop owners.)
2. Parents want home-made birthday cakes without artificial colours, but the nearest home baker they trust is in Vatakara. (Two mothers at a school gate.)
3. PSC aspirants in nearby villages can't afford ₹1,000 or more for coaching-centre mock tests, and the free tests they find online don't follow the latest pattern. (Four aspirants in a study group.)
4. Nurses applying abroad send CVs in old formats and rarely hear back. (A cousin in Dubai and two nursing students.)
5. Elderly parents of Gulf workers struggle with online bill payments and pension updates. (Overheard in an Akshaya centre queue.)

Each of these became an idea later in this module. None of them started as an idea.
""",
    resources=[
        ('pg-ideas', 'Read the first half, up to and including the part on noticing problems', '30 min'),
        ('pg-schlep', 'Read it all', '10 min'),
        ('os6', 'Section 6.1 Problem Solving to Find Entrepreneurial Solutions', '20 min'),
    ],
    steps=[
        '**Observation walk (45 minutes).** Walk through your town\'s main road, market or bus stand. Note every queue, complaint, handwritten notice and workaround you see.',
        '**Five quick conversations (45 minutes).** Ask five different people: "What was the most annoying thing about [shopping, your shop, studying, your phone] this month?" Then ask: "What did you do about it?" Don\'t mention any idea.',
        '**Review mining (20 minutes).** On Google Maps, open five businesses in your area and read their one-star and two-star reviews. Write down the problem behind each complaint.',
        '**Online groups (10 minutes).** Scan two groups you belong to (WhatsApp, Facebook, a subreddit) for complaints and questions that repeat.',
        'Log 20 problems in the Ideas tab of your Founder Workbook as problem statements. Mark each with how often it happens, how painful it is and whether people pay for a workaround today.',
    ],
    proof='Your problem log with at least 20 problems, each with its source.',
    templates=[
        ('problem log (paste into the Ideas tab)', """
No,Date,Who has it,Problem statement,How often,Pain (1-5),Current workaround,Do they pay now? (amount),Source
1,,,,,,,,
2,,,,,,,,
3,,,,,,,,
""", 'csv'),
    ],
    mistakes=[
        ('Starting with a solution.', '"An app for farmers" is not a problem. Ask what the farmer struggled with this month.'),
        ('Asking "Would you use…?"', 'People say yes to be polite. Ask what they did the last time the problem happened.'),
        ('Logging only your own problems.', 'Your life is one data point. Aim for at least 15 of the 20 problems to come from other people.'),
        ('Skipping boring problems.', 'Paperwork, follow-ups and record-keeping are often the problems people pay most to escape.'),
    ],
    quiz=[
        {'q': 'Which of these is a problem statement rather than a solution?',
         'o': ['An app for tuition centres', 'Tuition centre owners in Perambra struggle to collect fees on time because parents forget; they spend about 5 hours a month making calls', 'A WhatsApp bot for parents', 'A website for students'],
         'a': 'B', 'why': 'It names who has the problem, why it happens and what it costs. The others are solutions.'},
        {'q': 'Which sign best shows that a problem is worth solving?',
         'o': ['People say it is a great idea', 'People already spend money or hours on a workaround', 'It is trending on Instagram', 'Your friend likes it'],
         'a': 'B', 'why': 'Spending, in money or time, is evidence. Compliments are not.'},
        {'q': 'What does Paul Graham mean by "schlep blindness"?',
         'o': ['Avoiding hard physical work', 'Overlooking good problems because solving them looks tedious', 'Ignoring your competitors', 'Being afraid of risk'],
         'a': 'B', 'why': 'Tedious problems are often left unsolved, which makes them good opportunities.'},
        {'q': 'Why read one-star reviews of local businesses?',
         'o': ['To copy those businesses', 'They reveal unmet needs that customers care about', 'To reply to them', 'To improve your own search ranking'],
         'a': 'B', 'why': 'Each complaint points to something customers wanted and didn\'t get.'},
    ],
    study='the first half of "How to Get Startup Ideas", "Schlep Blindness" and OpenStax 6.1 (about 1 hour)',
    action='do an observation walk, five conversations and review mining, then log 20 problems',
)

L2 = lesson(
    2, 2,
    title='Local and online opportunities',
    weeks=(3, 3), hours=3,
    outcome='Map opportunities in your area and online, turn your best problems into 10 idea statements and roughly size the market for your top three.',
    split='1 hour 15 minutes study, 1 hour 45 minutes action',
    core="""
A problem becomes an opportunity when enough people have it, you can reach them, and they can pay. This lesson shows you where to look and how to do a quick size check.

### Where opportunities show up around Kuttiady

- **What people leave town for.** If people travel to Vatakara, Perambra or Kozhikode for something (a cake, a repair, a document service, coaching), there may be room for it nearer home.
- **Seasons and festivals.** Onam, Vishu, Christmas, Ramadan and Eid, the wedding season, school reopening in June and the monsoon all change what people buy. Some businesses earn most of their year in a few weeks, so plan for both the peak and the slack.
- **Gulf families.** Many households have someone working abroad. The family back home often needs help with what that person used to do: payments, paperwork, repairs, shopping for elderly parents.
- **Tourism.** Places near Kuttiady such as Peruvannamuzhi, Janakikkad and Kakkayam draw visitors, who need stays, food, guides and transport.
- **Farm produce.** Coconut, arecanut, pepper and banana can become value-added products. Check food-safety and licence rules before you sell any food.
- **Local schemes.** Kerala's One Local Body One Product (OLOP) scheme asks each local body to pick and promote a local product, which can point you to products your panchayat wants to back.

### Online opportunities

- **Services for people anywhere:** CV writing, design, video editing, Malayalam–English translation, setting up online tools for small businesses.
- **Digital products for Malayali learners:** PSC practice, spoken English, exam notes, templates.
- **Local products for Malayalis elsewhere:** selling to other cities or abroad brings shipping, GST and food-safety rules, so check them first.

### Check demand quickly

**Google Trends** shows whether searches for a topic are growing, falling or seasonal. Set the region to Kerala and compare terms such as "home made cake" and "birthday cake". It shows relative interest, not exact numbers, so use it to compare, not to count.

**A bottom-up market size** is a rough count you build yourself:

**Market per year = customers you can reach × purchases per customer per year × price**

Always start from customers you could actually reach this year, never from "everyone in Kerala".

### Look at the alternatives

List at least five things your customer could do instead of buying from you, including "do nothing" and "do it myself". Your real competition is often a habit, not another business.

### The idea statement

**For [customer] who [problem], [offer] helps them [result], unlike [current alternative].**
""",
    example="""
Arun turned the best problems into idea statements:

- **ShopAssist:** For shop owners in Kuttiady and Vatakara who lose evening WhatsApp enquiries, a one-day WhatsApp Business and Google profile setup helps them answer in minutes with prices and photos, unlike a family member replying late at night.
- **Nisha's Oven:** For parents near Kuttiady who want home-made birthday cakes without artificial colours, a home bakery with WhatsApp ordering delivers within 5 km, unlike a trip to Vatakara.

A rough size check for Nisha: about 3,000 households in her delivery area (her own estimate from ward lists), 2 cakes per household per year, and perhaps 1 in 5 of those cakes bought from a home baker. That gives 3,000 × 2 × 0.2 = 1,200 cakes a year. At ₹750 a cake, the reachable market is about ₹9 lakh a year. She needs only a small share, say 4 cakes a week, for a useful side income. The inputs are guesses, but they show the idea is worth testing.
""",
    resources=[
        ('gtrends', 'Set the region to Kerala and compare 3 search terms linked to your problems over the past 5 years', '20 min'),
        ('os5', 'Sections 5.2 Researching Potential Business Opportunities and 5.3 Competitive Analysis', '45 min'),
        ('kerala-olop', 'Read what the scheme supports (check current rules)', '10 min'),
    ],
    steps=[
        'List 10 things people in your area travel out of town to buy or get done. Ask two older relatives to add to the list.',
        'Ask three shopkeepers: "What do customers ask for that you don\'t sell?" Write down their answers word for word.',
        'In Google Trends (region: Kerala), compare search interest for terms linked to your top problems. Note which ones are growing or seasonal.',
        'Write 10 idea statements in the Ideas tab using the template below. Cover at least two of the four paths.',
        'For your top three ideas, do a bottom-up size check and list five alternatives each.',
    ],
    proof='Your 10 idea statements, the three shopkeepers\' answers, and size checks with alternatives for your top three ideas.',
    templates=[
        ('idea statement and size check', """
IDEA STATEMENT
For [customer] ____________ who [problem] ____________,
[offer] ____________ helps them [result] ____________,
unlike [current alternative] ____________.

QUICK SIZE CHECK
Customers I can reach: ____
Purchases per customer per year: ____
Price (₹): ____
Market per year = customers x purchases x price = ₹ ____
Sales a week I need for my goal: ____

ALTERNATIVES (at least 5)
1. Do nothing
2. Do it themselves
3. ____
4. ____
5. ____
""", ''),
    ],
    mistakes=[
        ('Using huge numbers.', '"India is a big market" tells you nothing. Count the customers you could reach this month.'),
        ('Ignoring seasons.', 'A cake business in Christmas week and in the monsoon are two different businesses. Plan for the slow months too.'),
        ('Opening the sixth copy.', 'If your town already has five mobile shops, a sixth must be clearly different. Count competitors before you choose.'),
        ('Forgetting that "do nothing" competes.', 'Many customers simply live with a problem. Your offer must be clearly better than doing nothing.'),
    ],
    quiz=[
        {'q': 'What does Google Trends show?',
         'o': ['The exact number of searches', 'Relative search interest over time and by region', 'Your competitors\' sales', 'How many customers you will get'],
         'a': 'B', 'why': 'Use it to compare terms and spot seasons, not to count customers.'},
        {'q': 'You can reach 500 shops, each might buy 1 setup a year, at ₹1,500. What is the bottom-up market per year?',
         'o': ['₹75,000', '₹7.5 lakh', '₹75 lakh', '₹1,500'],
         'a': 'B', 'why': '500 × 1 × ₹1,500 = ₹7,50,000.'},
        {'q': 'Which is the best idea statement?',
         'o': ['"A great bakery"', '"For parents near Kuttiady who want home-made birthday cakes without artificial colours, a home bakery with WhatsApp ordering delivers within 5 km, unlike a trip to Vatakara"', '"Cakes for everyone"', '"The best cakes in Kerala"'],
         'a': 'B', 'why': 'It names the customer, the problem, the offer, the result and the alternative.'},
        {'q': 'Why list "do nothing" as an alternative?',
         'o': ['To fill the list', 'Many customers will simply live with the problem, so your offer has to beat that', 'It is a legal requirement', 'Investors ask for it'],
         'a': 'B', 'why': 'Inaction is the most common competitor for a new small business.'},
    ],
    study='Google Trends practice, OpenStax 5.2 and 5.3, and the OLOP page (about 1 hour 15 minutes)',
    action='map opportunities, ask three shopkeepers, write 10 idea statements and size your top three',
)

L3 = lesson(
    2, 3,
    title='Score your ideas and choose one to test',
    weeks=(4, 4), hours=4,
    outcome='Score your ideas with a weighted scorecard, choose one idea and two backups, and write a test hypothesis with a kill signal.',
    split='1.5 hours study, 2.5 hours action',
    core="""
You now have more ideas than time. Scoring them makes your choice honest, and lets you explain it to someone else.

### Kill criteria come first

Before scoring, cross out any idea that:

- is illegal, unsafe or misleading
- needs more money than your risk limit before the first sale
- needs a licence you can't get, such as one for selling medicines
- needs full-time hours you don't have

### The weighted scorecard

Score each remaining idea from 1 to 5 on each row, multiply by the weight and add up. The highest possible total is 90.

| Criterion | Weight | Ask yourself |
| --- | --- | --- |
| Problem pain | 3 | How much does the problem hurt, in money, time or stress? |
| Willingness to pay | 3 | Do people already pay for a workaround? |
| Customer access | 2 | Can I reach 20 of these customers this month? |
| Fit with my path and skills | 2 | Can I deliver it now, or learn how in 4 weeks? |
| Low start cost | 2 | Can I test it within my risk limit? |
| Time to first rupee | 2 | Could someone pay me within 30 days? |
| Simple rules | 1 | Can I start without hard-to-get licences? |
| Different from others | 1 | Is it clearly different from what people use now? |
| Interest | 1 | Will I still care about it in six months? |
| Long-term potential | 1 | Could it grow into a real income? |

Pain and willingness to pay carry the most weight because a business without them can't survive, however clever it is.

### Sanity questions

Y Combinator's talk on evaluating ideas asks questions like these. Answer them honestly for your top three:

1. Are you the right person for this idea (founder–market fit)?
2. How big could the market be, and is it growing?
3. How urgent is the problem? Will people pay to fix it now?
4. Who else solves it, and why would people choose you?
5. Do you want this yourself, or personally know people who do?

### Write a test hypothesis

A hypothesis turns your choice into something you can prove wrong:

**I believe [customer] will pay [₹ amount] for [offer] because [problem]. I'll know I'm wrong if [kill signal] by [date].**

The kill signal is the result that tells you to stop or change course, for example "fewer than 3 of 15 shop owners agree to a paid trial by the end of week 10".

Scores are a starting bet, not the truth. The next two modules exist to test them with real people.
""",
    example="""
Arun scored four ideas (each cell shows score × weight):

| Criterion (weight) | ShopAssist | PSC Sprint | Bill-pay help for elders | Home bakery |
| --- | --- | --- | --- | --- |
| Pain (3) | 4 = 12 | 3 = 9 | 4 = 12 | 3 = 9 |
| Pay (3) | 4 = 12 | 3 = 9 | 2 = 6 | 4 = 12 |
| Access (2) | 5 = 10 | 4 = 8 | 3 = 6 | 3 = 6 |
| Fit (2) | 4 = 8 | 4 = 8 | 3 = 6 | 1 = 2 |
| Start cost (2) | 5 = 10 | 5 = 10 | 5 = 10 | 3 = 6 |
| First ₹ (2) | 5 = 10 | 3 = 6 | 3 = 6 | 4 = 8 |
| Rules (1) | 5 | 4 | 3 | 2 |
| Different (1) | 3 | 3 | 4 | 2 |
| Interest (1) | 4 | 4 | 3 | 1 |
| Potential (1) | 4 | 3 | 2 | 3 |
| **Total (of 90)** | **78** | **64** | **58** | **51** |

ShopAssist wins for Arun. His hypothesis: "I believe textile and mobile shop owners in Kuttiady and Vatakara will pay ₹1,500 for a one-day WhatsApp Business and Google profile setup, because they lose evening enquiries. I'll know I'm wrong if fewer than 3 of 15 owners agree to a paid setup by the end of week 10." PSC Sprint and the bill-pay help are his backups. Nisha, a keen baker with no interest in shop software, or Fathima, who ranked on a PSC list last year, would score the same ideas very differently, and that is the point.
""",
    resources=[
        ('yc-ideas', 'Watch the whole talk; pause at the list of questions for evaluating an idea and write your answers', 'about 25 min'),
        ('os4', 'Section 4.3 Developing Ideas, Innovations, and Inventions', '30 min'),
        ('os11', 'Section 11.3 Conducting a Feasibility Analysis', '30 min'),
    ],
    steps=[
        'Cross out every idea that fails a kill criterion.',
        'Score the rest with the scorecard below. In the "Weighted total" row, type =SUMPRODUCT($B3:$B12,C3:C12) in column C and copy it across. Score one row at a time across all ideas; it is harder to favour your pet idea that way.',
        'Ask two people who know you to score only "fit" and "interest" for your top five. If they disagree strongly and you can\'t explain why, change your score.',
        'For your top idea, have three 5-minute chats with people who have the problem. Ask: "When did this last happen? What did you do?" Don\'t pitch. If none of the three recognise the problem, look again at your second idea.',
        'Write your test hypothesis with a kill signal and a date, and name your two backups.',
    ],
    proof='Your completed scorecard, notes from the three quick chats and your written hypothesis.',
    templates=[
        ('weighted scorecard (paste into the Ideas tab)', """
Criterion,Weight,Idea 1,Idea 2,Idea 3,Idea 4,Idea 5
Idea name,,,,,,
Problem pain,3,,,,,
Willingness to pay,3,,,,,
Customer access,2,,,,,
Fit with my skills,2,,,,,
Low start cost,2,,,,,
Time to first rupee,2,,,,,
Simple rules,1,,,,,
Different from others,1,,,,,
Interest,1,,,,,
Long-term potential,1,,,,,
Weighted total,,,,,,
""", 'csv'),
        ('test hypothesis', """
TEST HYPOTHESIS
I believe [customer] ____________
will pay [₹] ____ for [offer] ____________
because [problem] ____________.
I'll know I'm wrong if [kill signal] ____________
by [date] ____________.

Backup 1: ____________
Backup 2: ____________
""", ''),
    ],
    mistakes=[
        ('Scoring your favourite idea high everywhere.', 'Score one row across all ideas at a time, and get a second opinion on fit and interest.'),
        ('Ignoring access.', 'A great idea for customers you can\'t reach is a poor first idea. Access is what makes testing fast.'),
        ('Treating the scores as truth.', 'They are guesses until customers confirm them. Modules 3 and 4 test them.'),
        ('A hypothesis with no kill signal.', 'Without a number and a date, you will keep going on hope alone.'),
    ],
    quiz=[
        {'q': 'Why multiply each score by a weight?',
         'o': ['To make the numbers bigger', 'Because some criteria, like pain and willingness to pay, matter more than others', 'Banks require it', 'To confuse competitors'],
         'a': 'B', 'why': 'Weights make the criteria that decide survival count for more.'},
        {'q': 'Which idea should be crossed out before scoring?',
         'o': ['One that needs ₹50,000 before any sale when your risk limit is ₹5,000', 'One with little competition', 'One you love', 'One in your own town'],
         'a': 'A', 'why': 'It breaks a kill criterion: it needs more money than you can afford to lose.'},
        {'q': 'Which is a good kill signal?',
         'o': ['"If people don\'t like it"', '"If fewer than 3 of 15 owners agree to a paid setup by the end of week 10"', '"If I get bored"', '"If it doesn\'t go viral"'],
         'a': 'B', 'why': 'It has a number, a group of people and a date, so you can\'t argue with it later.'},
        {'q': 'Your top idea scores 78, but none of three people with the problem recognise it. What next?',
         'o': ['Ignore them and build it', 'Look again at your second idea, or rewrite the problem and test again', 'Raise the price', 'Register a company'],
         'a': 'B', 'why': 'Real people outrank your scores. Adjust before you spend more time.'},
    ],
    study='the YC talk on evaluating ideas, OpenStax 4.3 and 11.3 (about 1.5 hours)',
    action='score your ideas, have three quick chats about the top one and write your hypothesis',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    2,
    title='Problems and ideas',
    weeks=(3, 4), hours=12,
    overview="""
Good businesses start from real problems, not clever ideas. In this module you collect problems from your town, your own life and online groups, turn the best ones into business ideas, and score them to pick one to test.

You finish with one idea, two backups and a test hypothesis that says exactly what result would prove you wrong.
""",
    outcomes=[
        'Collect 20 real problems from observation and conversations, written as clear problem statements',
        'Spot local, seasonal and online opportunities and estimate a market from the bottom up',
        'Score your ideas with a weighted scorecard and choose one to test, with a hypothesis, a kill signal and a date',
    ],
    lessons=LESSONS,
    project='Idea shortlist',
    project_steps=[
        'In the Ideas tab: your problem log of 20 problems (L01).',
        'Below it: your 10 idea statements and the size checks for your top three (L02).',
        'Your weighted scorecard, with your chosen idea and two backups (L03).',
        'One paragraph at the top: your test hypothesis, kill signal and date, and why you chose this idea over the backups.',
    ],
    project_proof='The Ideas tab of your Founder Workbook with 20 problems, 10 ideas, the scorecard and your hypothesis paragraph.',
    rubric=[
        ('Problem quality', 'Ideas with no problems behind them', 'Problems, but vague ("people need X")', 'Specific statements with who, how often, cost and workaround'),
        ('Evidence', 'Only my own guesses', 'A few conversations', 'Observation, at least 8 conversations and online sources'),
        ('Scoring', 'Not done', 'Done alone; my favourite won', 'Weighted, second opinion, kill criteria applied honestly'),
        ('Hypothesis', 'None', '"People will like it"', 'Customer, price, offer, kill signal and date'),
    ],
    short=[
        'L01: log 10 problems instead of 20, from five conversations and Google Maps reviews.',
        'L02: write 5 idea statements and skip Google Trends.',
        'L03: score only your top 5 ideas, but still do the three quick chats.',
    ],
    mistakes=[
        ('Falling in love with the first idea.', 'Log 20 problems before you let yourself choose.'),
        ('Picking a problem nobody pays to solve today.', 'Look for current spending or time spent on workarounds.'),
        ('Saying the market is "everyone".', 'Name one group you can reach this month.'),
    ],
)
