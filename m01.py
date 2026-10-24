from common import lesson, module, link

L1 = lesson(
    1, 1,
    title="The founder's job, honest odds and when not to start",
    weeks=(1, 1), hours=3,
    outcome="Explain what a founder actually does each week, state the real odds of a new business surviving, and write your own start conditions.",
    split="1.5 hours study, 1.5 hours action",
    core="""
**A business is simple to describe.** You solve a problem for people, they pay you more than it costs you to solve it, and they come back or tell others. Everything else is detail. Your job as a founder is to make that loop work, one customer at a time.

In a small business, a founder's week usually looks like this:

- **Finding customers:** talking to people, posting, following up. Many beginners spend far too little time here.
- **Delivering:** baking the cake, setting up the shop's WhatsApp, writing the question pack.
- **Collecting money and keeping records:** every rupee in and out, written down.
- **Improving:** asking customers what to fix, then fixing it.

"Being the boss" is not on the list. Early on, you are the salesperson, the delivery person and the accountant.

### Startup or small business?

You will hear two words. A **startup**, in the Y Combinator sense, is a company built to grow very fast, often with investors' money, and many of them fail. A **small business** (a micro-enterprise) aims to be profitable early and grow steadily: a home bakery, a design service, a tuition centre. This course aims for the second first: a business that earns real money within months. Paul Graham calls a startup that earns just enough to cover its founders' living costs "ramen profitable". That is a good first target for you too.

### The honest odds

Many new businesses close. The best long-run public data comes from the US Bureau of Labor Statistics. Of new business establishments that opened in 2014, about 80% were still open after one year, about 51% after five years and about 35% after ten years. India has no equally reliable public figure, so treat this as a rough guide. Remember too that some closures are owners moving on, not failures.

Small businesses usually close for a few repeating reasons:

- **No real demand.** Not enough people wanted it enough to pay.
- **Running out of cash.** Money was spent before money came in.
- **Prices too low.** Sales came in, but each sale lost money.
- **The founder burned out or lost interest.**

Every module of this course attacks one of these.

### The founder mindset

OpenStax's section on the entrepreneurial mindset describes the attitudes behind successful founders. In practice they come down to a few habits you can build:

- **Bias to action:** try a small version this week instead of planning for months.
- **Customer focus:** spend more time with customers than with your own ideas.
- **Learning from failure:** treat a failed test as information, not as a verdict on you.
- **Persistence with flexibility:** stay committed to the problem, but change the solution when the evidence says so.
- **Ownership:** take responsibility for results, including the dull parts such as records and follow-ups.

### Think in experiments, not bets

The safest way to start is with small, cheap tests that each answer one question. Do people have this problem? Will they pay? Can I deliver it at a profit? Decide in advance how much money and time you can afford to lose, and never go past it. When a test fails, you lose a little and learn a lot.

### When not to start (yet)

Pause, or start smaller, if any of these is true:

1. You would have to borrow to start: a gold loan, a credit card balance, a private money lender, or family money without written terms.
2. You have less than three months of essential expenses saved and no other income.
3. Your PSC exam is only a few weeks away. Exam weeks come first; the business can wait.
4. The idea needs a big spend (a shop lease, machines, stock) before a single customer has paid.
5. You are in the middle of a health or family crisis.
6. Someone wants a joining fee for you to "start your own business". That is the classic sign of a pyramid scheme, not a business.

None of these means "never". They mean "not like this, and not now".
""",
    example="""
These two people are made up, but their stories are common in Kerala towns.

**Shibu** saw busy juice shops in Kozhikode and opened one on Kuttiady's main road with a ₹4 lakh loan: ₹1.5 lakh for interiors, ₹1 lakh for machines, a ₹1 lakh rent deposit and ₹50,000 of stock. Rent was ₹15,000 a month. In the monsoon months, sales fell to about ₹800 a day, below his costs. He closed after eight months, still owing most of the loan.

**Nisha** wanted to sell home-made cakes. She first baked for two neighbours' birthdays at ₹650 each, using her own oven and about ₹2,000 of ingredients. Both ordered again and told friends. After two months she had 15 regular customers. She bought a bigger oven only when she already had ₹10,000 of advance orders for Christmas.

Same town, same years. The difference was not talent. Nisha tested demand before she spent; Shibu spent before he tested.
""",
    resources=[
        ('yc-should', 'Watch the whole talk', 'about 20 min'),
        ('pg-13', 'Read it all; mark points 8 and 9, on spending little and ramen profitability', '10 min'),
        ('pg-notnot', 'Read the list of reasons people give for not starting, and note which ones apply to you', '25 min'),
        ('os1', 'Sections 1.1 Entrepreneurship Today and 1.3 The Entrepreneurial Mindset', '40 min'),
        ('bls', 'Optional: find establishments that opened in March 2014 and read their survival rate year by year', '10 min'),
    ],
    steps=[
        'Pick two people near you who run a small business: a shop owner, a home baker, a tailor, a tuition teacher. Choose people you can meet or call this week.',
        'Ask for 15 minutes: "I\'m learning how small businesses start. Can I ask you five questions? I\'m not selling anything."',
        'Ask the five questions in the first template below. Write their answers within an hour, while you still remember the details.',
        'Fill in "My start conditions" honestly. For every "no", write what would have to change and by when. (You set your exact risk limit in ENT-M01-L03; for now, write a rough number.)',
        'Save both in your Founder Toolkit folder as "M01 founder reality notes".',
    ],
    proof='Notes from two conversations with business owners and your filled start-conditions checklist, saved in your Founder Toolkit folder.',
    templates=[
        ('founder reality interview', """
FOUNDER REALITY INTERVIEW (15 minutes)
Name, business, years running:

1. How did you get your first 5 customers?
2. How much did you spend before your first sale? On what?
3. When did the business first make a profit?
4. What was your hardest month, and what happened?
5. If you started again, what would you do differently?

One thing that surprised me:
""", ''),
        ('my start conditions', """
MY START CONDITIONS (write yes or no)
___ I can start without borrowing money
___ I have 3 months of essential expenses saved,
    or another income that covers them
___ My next PSC exam is more than 4 weeks away
___ My first test costs less than my risk limit
___ My family knows my plan and my time limits
___ Nobody is asking me for a joining fee

For each "no":
What must change: ____________________
By when: ____________________
""", ''),
    ],
    mistakes=[
        ('Starting with a big spend.', 'Shops, machines and stock come after paying customers, not before. Test with what you already have.'),
        ('Believing only success stories.', 'For every shop that made it, others closed quietly. Ask owners about their hardest month, not only their best one.'),
        ('Treating doubts as weakness.', 'Writing down when not to start is a strength. It stops you from making a bad bet on an excited day.'),
        ('Asking only family for advice.', 'Family often fears risk and friends want to encourage you. Talk to people who actually run businesses.'),
    ],
    quiz=[
        {'q': 'What is a founder\'s main job in a new small business?',
         'o': ['Managing staff', 'Finding customers, delivering, collecting money and improving', 'Designing the logo and the shop', 'Applying for loans'],
         'a': 'B', 'why': 'Early on you run the core loop yourself. Staff, logos and loans come later, if at all.'},
        {'q': 'In US government data for establishments that opened in 2014, roughly how many were still open five years later?',
         'o': ['About 10%', 'About half', 'About 90%', 'Nearly all'],
         'a': 'B', 'why': 'About 51% were still open after five years (BLS Table 7). India has no equally reliable figure.'},
        {'q': 'Which of these is a reason to pause or start smaller?',
         'o': ['One customer has already paid you', 'You would need a gold loan to start', 'Your exam is four months away', 'Your first test costs ₹500'],
         'a': 'B', 'why': 'Borrowing to start means you can lose more than you can afford. Start with what you have.'},
        {'q': 'What does "ramen profitable" mean?',
         'o': ['Selling noodles', 'Earning just enough to cover the founders\' living costs', 'Making a profit in the first week', 'Raising money from investors'],
         'a': 'B', 'why': 'Paul Graham uses it for a business that pays its founders\' basic living costs, which gives you time and freedom.'},
        {'q': 'Someone offers you a "business opportunity" for a ₹15,000 joining fee, with earnings from recruiting others. What should you do?',
         'o': ['Pay, because high returns are promised', 'Ask for a discount', 'Treat it as a sign of a pyramid scheme and walk away', 'Recruit your family first'],
         'a': 'C', 'why': 'India\'s Consumer Protection (Direct Selling) Rules, 2021 ban promoting pyramid and money circulation schemes. Real businesses earn from customers, not joining fees.'},
    ],
    study='the resources in the table (about 1.5 hours)',
    action='interview two local business owners and fill in your start conditions',
)

L2 = lesson(
    1, 2,
    title='Choose your business path',
    weeks=(1, 1), hours=3,
    outcome='Compare the four beginner business paths and pick one to test first, plus a backup, using scores and one real conversation.',
    split='1 hour 15 minutes study, 1 hour 45 minutes action',
    core="""
There are many kinds of business, but four paths suit a beginner with little money. Each one makes money differently and fits a different life.

| Path | How you earn | Rough start cost | Time to first ₹ | Can it grow? | Main risk |
| --- | --- | --- | --- | --- | --- |
| Freelance → agency | You sell a skill (design, setup, writing) job by job, then hire or partner to take on more work | ₹0–₹5,000 | Days to weeks | Yes, once others do part of the work | Income stops when you stop; late payments |
| Local business | You sell a product or service in your area: food, repairs, tuition | ₹2,000–₹50,000 or more | Days to weeks | Slowly: more capacity, more areas | Stock, rent, licences, spoilage |
| Digital products | You make something once (a question pack, templates, a course) and sell it many times | ₹0–₹2,000 | Weeks to months | Yes: another copy costs almost nothing | Needs an audience; easy to copy |
| Online services | You sell one fixed package online (a ₹999 CV rewrite, online classes) to many customers | ₹0–₹3,000 | Days to weeks | Yes, with templates and helpers | Competition; your time is the limit |

The start costs are rough examples for very small first versions. Check real costs for your own idea.

**Freelancing or online service?** A freelancer does custom work for each client. An online service sells the same package, at the same price, to many people. Many people start as freelancers and turn their most common job into a packaged service. An **agency** is the next step: you win the clients and others help deliver.

### What makes a path fit you

Score each path from 1 (poor) to 5 (excellent):

1. **Time to first rupee:** how soon could you earn from it?
2. **Start cost:** can you start within your risk limit?
3. **Your skills:** can you deliver it now, or after a few weeks of practice?
4. **Your time:** does it fit about 6 hours a week next to PSC prep, without fixed shop hours?
5. **Your network:** do you already know people who would buy, or who know buyers?
6. **Interest:** would you still do it in a bad week?
7. **Long-term potential:** could it grow into a real income?

Your network matters more than most people think. If your uncle runs three textile shops, a service for shops has a head start. If you have helped PSC aspirants before, a PSC product does.

You are not choosing forever. Pick one path to test first and one backup. Paths combine well over time: an AI-assisted service for local shops now, and a digital product for the same shops next year.
""",
    example="""
Here is how Arun, a made-up learner much like you (near Kuttiady, about 6 hours a week, an Android phone, an old laptop and new AI skills), scores four ideas, one per path. All four come back as running examples throughout the course: Arun builds ShopAssist, Nisha runs Nisha's Oven, Fathima makes PSC Sprint and Meera runs CV Makeover.

| Question | ShopAssist: WhatsApp and Google setup for shops | Nisha's Oven: home-made cakes | PSC Sprint: practice-question packs | CV Makeover: ₹999 CV and LinkedIn for Gulf jobs |
| --- | --- | --- | --- | --- |
| Path | Freelance → agency | Local business | Digital product | Online service |
| Time to first ₹ | 5 | 4 | 2 | 4 |
| Start cost | 5 | 3 | 5 | 5 |
| Skills | 4 | 2 | 4 | 3 |
| Fits 6 h a week | 3 | 2 | 4 | 4 |
| Network | 4 | 3 | 4 | 3 |
| Interest | 4 | 2 | 4 | 3 |
| Potential | 4 | 3 | 3 | 3 |
| **Total (of 35)** | **29** | **19** | **26** | **25** |

For Arun, ShopAssist is the first test and PSC Sprint the backup. Nisha, who loves baking and owns a good oven, would score the home bakery much higher. The scores belong to the person, not to the idea.
""",
    resources=[
        ('os2', 'Sections 2.3 Entrepreneurial Pathways and 2.4 Frameworks to Inform Your Entrepreneurial Path', '45 min'),
        ('pg-ramen', 'Read it all', '10 min'),
        ('mit-390', 'Lecture 4: Three Ways to Start a Company (length not listed)', 'budget 20 min'),
    ],
    steps=[
        'For each of the four paths, write one concrete idea you could start from your town or your phone. One line each.',
        'Score all four with the template below. Be strict: a 5 means "I could do this next week".',
        'Ask one person who knows you well to score only the "skills" and "network" rows for you, before they see your scores. Compare the two.',
        'Find one person already on your top path (a freelancer, a home baker, someone selling a digital product) and ask: "What do you wish you had known in your first month?" Write down the answer.',
        'Write your choice: first path, backup path, and one sentence on why.',
    ],
    proof='Your scored path table (including the second person\'s scores) and your notes from the conversation with someone on your top path.',
    templates=[
        ('path scores (paste into Google Sheets)', """
Question,Freelance to agency,Local business,Digital product,Online service
My idea (one line),,,,
Time to first rupee (1-5),,,,
Start cost (1-5),,,,
My skills (1-5),,,,
Fits my time (1-5),,,,
My network (1-5),,,,
My interest (1-5),,,,
Long-term potential (1-5),,,,
Total,=SUM(B3:B9),=SUM(C3:C9),=SUM(D3:D9),=SUM(E3:E9)
""", 'csv'),
        ('my path choice', """
First path to test: ____________
Backup path: ____________
Why (one sentence): ____________
Person I asked on this path: ____________
What they wish they had known: ____________
""", ''),
    ],
    mistakes=[
        ('Choosing the most fashionable path.', 'Dropshipping, trading and "passive income" videos make things look easy. Score them like any other path; most score low on start cost or risk.'),
        ('Ignoring your network.', 'People you already know are your fastest first customers. A path that uses them can save you months.'),
        ('Starting with a digital product and no audience.', 'Digital products sell to people who already trust you. With no audience yet, a service usually earns sooner and builds that trust.'),
        ('Treating the choice as permanent.', 'You are choosing what to test first. You will review this choice at the end of Module 4 with real evidence.'),
    ],
    quiz=[
        {'q': 'What is the main difference between freelancing and an online service?',
         'o': ['Freelancing is always offline', 'An online service sells one fixed package to many customers; freelancing is custom work for each client', 'An online service needs a registered company', 'There is no difference'],
         'a': 'B', 'why': 'Packaging the work (same scope, same price) is what turns freelancing into a service that can grow.'},
        {'q': 'Which path usually costs least to sell one more unit?',
         'o': ['Local business', 'Freelancing', 'Digital products', 'Online services'],
         'a': 'C', 'why': 'Once a digital product is made, another copy costs almost nothing. The hard part is finding buyers.'},
        {'q': 'Why does the "network" score matter?',
         'o': ['Banks check it', 'People you know can buy or introduce buyers, which shortens the time to your first rupee', 'It decides your tax rate', 'It doesn\'t matter'],
         'a': 'B', 'why': 'Your first customers almost always come from people you know or people they know.'},
        {'q': 'Your scores are freelance → agency 29 and digital product 26. What should you do?',
         'o': ['Start both, full-time', 'Test freelancing first and keep the digital product as a backup', 'Pick the digital product because it scales', 'Wait until one path scores 35'],
         'a': 'B', 'why': 'Test one path at a time. The backup is ready if the first test fails.'},
    ],
    study='OpenStax 2.3 and 2.4, "Ramen Profitable" and the MIT lecture (about 1 hour 15 minutes)',
    action='score the four paths, get a second opinion and talk to someone on your top path',
)

L3 = lesson(
    1, 3,
    title='Your personal runway and time plan',
    weeks=(2, 2), hours=4,
    outcome='Know your monthly survival number, your runway in months, the most money and time you will risk, and the weekly hours you can protect next to PSC prep.',
    split='30 minutes study (plus an optional hour), 3.5 hours action spread over the week',
    core="""
Money and time are your two limits. Writing them down now stops you from spending too much on an excited day, or quitting on a tired one.

### Your survival number and runway

Your **survival number** is what you need each month for essentials: your share of household costs, food, phone, travel, loan payments (EMIs), insurance and study materials. It is not what you would like to spend. It is what you can't avoid.

Your **runway** is how many months you could manage if your income stopped:

**Runway (months) = savings you can use ÷ (survival number − other monthly income)**

If your other income already covers your survival number, your runway has no limit. That is the best position to start a business from, because you can test ideas without needing them to pay the bills.

### Keep three pots of money

1. **Emergency money:** ideally 3 months of your survival number. Never use it for the business.
2. **Living money:** your normal monthly spending.
3. **Risk money:** the most you will spend on the business before it pays you back. This is your **risk limit**.

Choose a risk limit you could lose completely without hurting your family or your exam plan. Because this course tests before it spends, ₹2,000 to ₹10,000 for the first three months is enough for most learners. Add a time limit too, for example "6 hours a week, and only 1 hour a week in the 4 weeks before an exam".

### Money you should never use to start

- Gold loans, or pledging family gold
- A credit card balance you can't clear in full that month
- Private money lenders who charge daily or weekly interest (often called "blade" lenders in Kerala)
- Loan apps you can't confirm are linked to an RBI-regulated lender
- Family money without a written note of the amount, how it will be repaid and what happens if the business fails

### Your time plan

Six hours a week is enough to start a small business if the hours are fixed. Here is one plan that works next to PSC study:

| Day | Time | What |
| --- | --- | --- |
| Monday to Thursday | 45 minutes after PSC study | Lessons, messages, records |
| Saturday | 1 hour | Planning and content |
| Sunday | 2 hours | Customer conversations, sales, delivery |

**Exam mode:** in the 4 weeks before a PSC exam, drop to about 1 hour a week. Reply to customers and keep records; start nothing new. In this app, move your start date later so the schedule matches your real pace. Your ticks are kept.

**Full-time track:** about 24 hours a week, for example 4 hours a day for 6 days, with at least half of that time spent with customers rather than at a screen.

This is general information, not financial advice. If you have debts or people who depend on you, talk your limits through with someone you trust.
""",
    example="""
Arun, a learner near Kuttiady who appears all through this course, lists his essentials: ₹4,000 to the household, ₹1,200 for food outside, ₹1,500 for bus and petrol, ₹300 for the phone, ₹500 for PSC materials and ₹1,500 for everything else. Survival number: **₹9,000 a month**. Usable savings: ₹30,000. No other income right now.

Runway = ₹30,000 ÷ (₹9,000 − ₹0) = **about 3.3 months**.

That is short. So Arun keeps ₹27,000 as emergency money and sets a risk limit of **₹3,000 for the first three months**, plus 6 hours a week. Any spending above ₹3,000 must come out of money customers have already paid. He also looks for a small steady income, such as two evening tuition students, so the business never has to pay the household bills in its first year.
""",
    resources=[
        ('ncfe', 'Optional: register free and take the e-learning module on financial planning (budgets and saving)', 'about 1 hour'),
        ('os1', 'Section 1.2 Entrepreneurial Vision and Goals', '20 min'),
        ('pg-aord', 'Read it all, thinking of your own household as the "startup"', '10 min'),
    ],
    steps=[
        'Starting today, write down every rupee you spend for 7 days, in a notebook or a sheet. Include small things: tea, recharges, bus fares.',
        'At the end of the 7 days, fill in the runway calculator below with your real numbers.',
        'Decide your three pots. Write down your emergency amount, your risk limit in rupees and your time limit in hours a week.',
        'Block your weekly business slots in Google Calendar, or write them on paper and stick it where you study.',
        'Tell one family member your plan, your risk limit and your exam-mode rule. Ask them to remind you if you break it.',
    ],
    proof='Your 7-day spending record, the filled runway calculator and a photo or screenshot of your weekly time plan.',
    templates=[
        ('runway calculator (paste into Google Sheets)', """
Item,Monthly amount in rupees
Household share,
Food,
Travel,
Phone and internet,
Loan EMIs,
Insurance,
Study materials,
Other essentials,
SURVIVAL NUMBER,=SUM(B2:B9)
Other monthly income,
Savings I can use,
RUNWAY in months,=B12/(B10-B11)
Emergency pot (3 months),=3*B10
Risk limit for the first 3 months,
Time limit in hours a week,
""", 'csv'),
        ('weekly time plan', """
MY WEEKLY TIME PLAN
Business hours a week: ___
Mon to Thu: ___ to ___ (lessons, messages, records)
Saturday: ___ to ___ (planning, content)
Sunday: ___ to ___ (customers, sales, delivery)

Next exam date: ___
Exam mode starts (4 weeks before): ___
In exam mode I only reply to customers and keep records.
Person who will remind me: ___
""", ''),
    ],
    mistakes=[
        ('Guessing your expenses.', 'Small daily spends add up and are easy to forget. Track a full week before you calculate anything.'),
        ('Mixing the pots.', 'If business money and household money share one wallet, you can\'t tell whether the business makes money. Keep separate records from day one.'),
        ('Planning 20 hours a week on paper.', 'Plan the hours you really have. Six fixed hours beat twenty imaginary ones.'),
        ('Having no exam-mode rule.', 'Decide now what you will pause before an exam, so you neither panic nor feel guilty when the time comes.'),
    ],
    quiz=[
        {'q': 'Your survival number is ₹8,000, other income is ₹3,000 a month and usable savings are ₹20,000. What is your runway?',
         'o': ['2.5 months', '4 months', '6.7 months', '10 months'],
         'a': 'B', 'why': '₹20,000 ÷ (₹8,000 − ₹3,000) = 4 months.'},
        {'q': 'Which money is fine to use for your first business test?',
         'o': ['A gold loan', 'Your emergency pot', 'Your risk money, set in advance', 'A loan app you found on social media'],
         'a': 'C', 'why': 'Risk money is the amount you decided you can lose without harm.'},
        {'q': 'What is a risk limit?',
         'o': ['The most a bank will lend you', 'The most money and time you will put in before the business pays you back', 'Your monthly salary', 'The GST threshold'],
         'a': 'B', 'why': 'It is your own rule, set while you are calm, so excitement never decides how much you spend.'},
        {'q': 'What should you do in the 4 weeks before a PSC exam?',
         'o': ['Launch a new product', 'Switch to exam mode: reply to customers and keep records only', 'Close the business', 'Work double hours to get ahead'],
         'a': 'B', 'why': 'Exam mode keeps existing customers happy without stealing study time.'},
        {'q': 'Why is it good to start when other income covers your survival number?',
         'o': ['You can borrow more', 'You can test ideas without needing the business to pay your bills yet', 'You no longer need records', 'Your taxes are lower'],
         'a': 'B', 'why': 'Without pressure to earn at once, you can run honest tests and walk away from bad ideas.'},
    ],
    study='OpenStax 1.2 and "Default Alive or Default Dead?" (30 minutes), plus NCFE if you have time',
    action='track 7 days of spending, calculate your runway and set your risk and time limits',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    1,
    title='Founder foundations',
    weeks=(1, 2), hours=12,
    overview="""
Before you look for ideas, get clear on three things: what running a business really involves, which kind of business fits your life right now, and how much money and time you can safely put in. This module turns those into numbers and rules you will use for the rest of the course.

One idea runs through it: a business is a series of small, cheap experiments, not one big bet. You set your limits now, while you are calm, so you never risk more than you can afford to lose.
""",
    outcomes=[
        'Explain what a founder does each week and the real odds of a new business surviving',
        'Choose one business path to test first, and a backup, using scores and a real conversation',
        'State your survival number, runway, risk limit and weekly time plan',
        'Decide your personal start conditions: when to start, when to pause and when not to start',
    ],
    lessons=LESSONS,
    project='Founder Fit Sheet',
    project_steps=[
        'Make one Google Doc called "Founder Fit Sheet" with four parts: your start conditions (L01), your path scores and choice (L02), your runway and risk limit (L03), and your weekly time plan (L03).',
        'Add your notes from the two business-owner conversations (L01) and the conversation with someone on your top path (L02).',
        'At the top, write three sentences: the path you will test first, the most you will risk (rupees and hours a week), and the date you will review this choice (the end of week 10).',
        'Show it to one person you trust and ask, "What am I not seeing?" Write down their answer at the bottom.',
    ],
    project_proof='Your Founder Fit Sheet, saved in your Founder Toolkit folder, with the reviewer\'s comment at the bottom.',
    rubric=[
        ('Honesty about limits', 'Time and money not stated', 'Stated, but the numbers are guesses', 'Real numbers from a week of tracking'),
        ('Path choice', 'Picked on feeling', 'Scored, but no talk with anyone on that path', 'Scored, discussed with someone on that path, backup chosen'),
        ('Risk limit', 'None', 'A rupee limit only', 'A rupee limit, an hours limit and a stop rule'),
        ('Time plan', '"Whenever I\'m free"', 'Weekly hours, but no fixed slots', 'Fixed slots that protect PSC study, shared with family'),
    ],
    short=[
        'L01: fill in "My start conditions" (20 minutes) and skip the readings.',
        'L02: score the four paths; move the conversation with someone on your top path to week 3.',
        'L03: work out your survival number and risk limit, tracking spending for 3 days instead of 7.',
    ],
    mistakes=[
        ('Quitting PSC prep or a job "to focus" before any customer has paid.', 'Keep your income and your exam plan, and test on the side.'),
        ('Copying a success story.', 'You only hear from the people who survived. Ask what the closed businesses had in common too.'),
        ('Leaving limits vague.', '"I\'ll spend a little" can turn into ₹40,000. Write a number down.'),
    ],
)
