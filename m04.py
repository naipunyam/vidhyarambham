from common import lesson, module

L1 = lesson(
    4, 1,
    title='Map your business on one page: Lean Canvas and Business Model Canvas',
    weeks=(8, 8), hours=3,
    outcome='Fill a Lean Canvas for your idea from interview evidence, rank your riskiest assumptions, and know when to use the Business Model Canvas instead.',
    split='1 hour study, 2 hours action',
    core="""
A 30-page business plan is out of date the day you finish it. A one-page canvas is quick to fill, easy to change and shows the whole business at a glance. Two canvases are widely used, and both are free.

### The Lean Canvas

Ash Maurya created the Lean Canvas in 2010 for new, untested ideas. It has nine boxes, filled roughly in this order:

1. **Customer segments:** who has the problem. Mark your **early adopters**.
2. **Problem:** the top 1–3 problems, plus the **existing alternatives** people use now.
3. **Unique value proposition:** one clear sentence on why you are different and worth attention. A **high-level concept** helps, such as "a WhatsApp shop assistant for small shops".
4. **Solution:** the simplest feature or offer for each problem.
5. **Channels:** how you will reach customers: WhatsApp, walk-ins, partners, Google.
6. **Revenue streams:** how and how much customers pay.
7. **Cost structure:** your main costs, fixed and variable.
8. **Key metrics:** the few numbers that show progress, such as orders a week or repeat customers.
9. **Unfair advantage:** something that can't easily be copied or bought: a trusted local network, special knowledge, a loyal community. "Nothing yet" is an honest answer.

LEANSTACK's LEANSpark tool lets you fill a Lean Canvas online for free after you sign up. The plain-text version below works just as well on a phone.

### The Business Model Canvas

Strategyzer's Business Model Canvas (a free PDF you may use with credit to Strategyzer.com) suits a business that already operates, or one that depends on partners. Its nine blocks are customer segments, value propositions, channels, customer relationships, revenue streams, key resources, key activities, key partnerships and cost structure. Use it when you need to think through suppliers, partners and the activities that keep the business running. While you are still testing the problem, the Lean Canvas is the better fit.

### Turn the canvas into a test list

Every box is an assumption until evidence confirms it. List the assumptions, then score each one for **importance** (if this is wrong, does the business fail?) and **evidence** (how much proof do you have?). The most important assumptions with the least evidence are your **riskiest assumptions**. Test those first. They come in three types:

- **Desirability:** do they want it? Tested with interviews and smoke tests.
- **Viability:** will they pay enough, at a profit? Tested with pre-sales and unit economics.
- **Feasibility:** can you deliver it? Tested with an MVP.
""",
    example="""
Nisha's Lean Canvas, with the evidence for each box:

| Box | Nisha's Oven | Evidence |
| --- | --- | --- |
| Customer segments | Parents within 5 km of Kuttiady town who order birthday cakes. Early adopters: mothers who already travel to Vatakara for cakes | 9 interviews |
| Problem | No trusted home baker nearby; bakery cakes too sweet, with artificial colour; an hour lost collecting. Alternatives: a Vatakara bakery, the local bakery, no cake | 7 of 9 interviews |
| Unique value proposition | Home-made birthday cakes with natural colours, delivered in Kuttiady | Guess |
| Solution | 4 designs, 2 sizes, order on WhatsApp 2 days ahead, delivery within 5 km | Guess |
| Channels | WhatsApp Status, school parents' groups (with permission), word of mouth, Instagram | 2 interviews |
| Revenue streams | ₹650–₹1,100 a cake, 50% advance by UPI | Mothers paid ₹900 in Vatakara |
| Cost structure | Ingredients, boxes, gas, delivery fuel; a bigger oven later | Her receipts |
| Key metrics | Orders a week, repeat customers, reviews | — |
| Unfair advantage | Neighbours already trust her; her mother's recipes | Weak, but real |

Her three riskiest assumptions: (1) parents will pay ₹800 or more for a home-made cake (viability, little evidence), tested next with pre-orders; (2) she can bake 6 cakes a week alongside her other work (feasibility); (3) WhatsApp Status reaches enough parents (desirability of the channel).
""",
    resources=[
        ('leancanvas', 'Sign up free and fill one canvas, or read the box list and use the text template below', '20 min'),
        ('bmc', 'Download the free PDF and read the nine blocks', '15 min'),
        ('strategyzer-use', 'Read how you may use and share the canvases', '5 min'),
        ('os11', 'Section 11.2 Designing the Business Model', '25 min'),
    ],
    steps=[
        'Fill the Lean Canvas template using your interview notes. Next to every box, write the evidence (an interview code or a number) or the word "guess".',
        'List 10 assumptions from your canvas.',
        'Score each one for importance (1–5) and evidence (1–5). Risk score = importance × (6 − evidence); in Sheets, type =C2*(6-D2) and copy it down. Mark the top 3 as your riskiest assumptions.',
        'Show the canvas to two people you interviewed, or to an experienced business owner, and ask: "What looks wrong or missing?"',
        'Write down how you will test each riskiest assumption. You will run these tests in the next two lessons.',
    ],
    proof='Your filled Lean Canvas, your scored assumption list and feedback from two people.',
    templates=[
        ('Lean Canvas (text version)', """
LEAN CANVAS: [business name]     Date: ____
(next to each box write the evidence, or "guess")

1. Customer segments:
   Early adopters:
2. Problem (top 3):
   Existing alternatives:
3. Unique value proposition:
   High-level concept:
4. Solution:
5. Channels:
6. Revenue streams:
7. Cost structure:
8. Key metrics:
9. Unfair advantage:
""", ''),
        ('assumption ranking (paste into Google Sheets)', """
Assumption,Type (desirability / viability / feasibility),Importance (1-5),Evidence (1-5),Risk score,How I will test it
Parents will pay 800 rupees for a home-made cake,viability,5,2,,Pre-orders with advance
""", 'csv'),
    ],
    mistakes=[
        ('Filling every box with guesses and calling it done.', 'Mark each box with its evidence. A canvas full of guesses is a to-do list, not a plan.'),
        ('"Everyone" as the customer segment.', 'Write the narrowest group you can reach, and name your early adopters.'),
        ('Copying a famous company\'s model.', 'A model that works for a national brand with crores of funding rarely works for a micro-business.'),
        ('Never updating it.', 'Date your canvas and update it after every test. Old versions show how far you have come.'),
    ],
    quiz=[
        {'q': 'Which tool suits a new, untested idea best?',
         'o': ['The Lean Canvas', 'A 30-page business plan', 'A balance sheet', 'A profit and loss statement'],
         'a': 'A', 'why': 'It was designed for early ideas and focuses on problems, customers and risks.'},
        {'q': 'What is an "unfair advantage"?',
         'o': ['A lower price', 'Something that can\'t easily be copied or bought, like a trusted network or special knowledge', 'A big advertising budget', 'A logo'],
         'a': 'B', 'why': 'Prices and ads can be copied. Trust and knowledge are harder to copy.'},
        {'q': 'Which assumption should you test first?',
         'o': ['The one you are most sure about', 'The most important one with the least evidence', 'The cheapest one, even if it is unimportant', 'The last box on the canvas'],
         'a': 'B', 'why': 'If an important assumption is wrong, nothing else matters.'},
        {'q': '"Parents will pay ₹800 for a home-made cake" is which type of assumption?',
         'o': ['Desirability', 'Viability', 'Feasibility', 'Legal'],
         'a': 'B', 'why': 'It is about whether customers will pay enough for the business to work.'},
    ],
    study='the Lean Canvas tool, the Business Model Canvas PDF and OpenStax 11.2 (about 1 hour)',
    action='fill a Lean Canvas from your evidence, rank 10 assumptions and get feedback from two people',
)

L2 = lesson(
    4, 2,
    title='Smoke tests and pre-sales: get proof people will pay',
    weeks=(8, 9), hours=5,
    outcome='Run an honest smoke test of your offer and ask for real commitments: pre-orders, deposits or paid trials.',
    split='1 hour study, 4 hours action over two weeks',
    core="""
A **smoke test** shows people your offer before the full product exists, to see whether they take a real step towards buying. A **pre-sale** goes further: they pay, or pay a deposit, before you deliver. Both test the riskiest assumption of all: will people pay?

### The evidence ladder

From weakest to strongest:

1. Likes, compliments and "nice idea"
2. Clicks, views and replies
3. Sign-ups: a name and number on a waiting list
4. Time: they book a demo or a visit
5. A deposit or advance payment
6. Full payment before delivery
7. A repeat purchase or a referral

Aim for steps 5 to 7. Step 1 is not evidence.

### Cheap ways to run a smoke test

- **WhatsApp offer:** a clear offer message and poster on your Status, sent personally to the people you interviewed and posted in groups with the admin's permission.
- **One-page site and form:** a free Google Site that explains the offer, with a Google Form to pre-order or join the waiting list.
- **Pilot offer:** "First 5 shops: full setup for ₹999 instead of ₹1,500, money back if you're not happy."
- **Pre-order with a delivery date:** "Christmas plum cakes delivered on 23–24 December. Book with a ₹200 advance."
- **Paid trial for services:** a small first job at a fair price, with a clear scope.

### Set success criteria before you start

Before the test, write down who will see it, how many people, for how long, and what result counts as success. For example: "Offer sent to 50 parents I don't know well, over 7 days. Success = 5 or more advance payments of ₹200." If you set the bar after seeing the results, you will always find a reason to call it a success.

### Be honest

- Say clearly what the customer gets and when.
- Take money only for something you can and will deliver. If you can't deliver, refund in full, fast.
- Never pretend something exists when it doesn't, invent reviews, or fake "only 2 left". That is deception, and misleading claims can break India's consumer protection law.
- A "coming soon" waiting list is fine, as long as you say it is coming soon.

### Payments

UPI to a bank account you use only for the business is the simplest. Record every payment in your Cashbook tab the same day. If you plan to use a payment gateway, check its fees first; Razorpay, for example, lists 2% plus GST per transaction on its standard plan.
""",
    example="""
**Nisha (local business).** In early December she made one poster in Canva and posted it on her WhatsApp Status and in three family groups, after asking the admins: "Home-made Christmas plum cakes. 500 g ₹450, 1 kg ₹850. Delivered in Kuttiady on 23–24 December. Book with a ₹200 advance by UPI." Her success criterion, written first: 8 bookings in 10 days. Result: 140 Status views, 22 replies, 11 bookings and ₹2,200 in advances. Two bookings came from people she had never met.

**Arun (freelance → agency).** He offered a pilot setup to the 11 shop owners he had interviewed: ₹999 for the first five shops (normal price ₹1,500), with a full refund if they weren't happy after two weeks. Criterion: 3 paid pilots in 14 days. Result: 4 paid, 3 said "maybe after Onam", 4 said no.

**Fathima (digital product).** She posted 10 original sample questions and a ₹99 early-bird offer for a 500-question practice pack for the PSC LDC exam in two aspirants' groups. Criterion: 20 pre-orders in a week. Result: 300 views and 9 pre-orders. That is below her bar, so she has to change something before she builds the full pack (see ENT-M04-L04).
""",
    resources=[
        ('lean-principles', 'Read the five principles, especially validated learning and Build-Measure-Learn', '10 min'),
        ('os6', 'Section 6.4 Lean Processes', '25 min'),
        ('gsites', 'Only if you want a one-page site: how to create and publish it', '10 min'),
        ('gforms', 'How to create, send and read a form', '10 min'),
        ('razorpay', 'Only if you plan to use a payment gateway: the standard fees (check current rules)', '5 min'),
    ],
    steps=[
        'Write your offer with the template below: what it is, who it is for, the price, the delivery date, how to book and your promise.',
        'Write your success criterion before you publish: who, how many people, how long, and the result that counts as success. Date it.',
        'Show the offer to at least 50 people in your target group: the people you interviewed first, then your Status, groups (with permission) and a Google Form or Site. At least half should not be close friends or family.',
        'Ask clearly for a commitment: a deposit, a pre-order or a paid trial.',
        'For 7–10 days, record every view, reply, sign-up and payment in the Experiments tab. Deliver to everyone who paid, or refund them.',
    ],
    proof='Your offer, your dated success criterion and the results in the Experiments tab, including the payments received.',
    templates=[
        ('offer message in English and Malayalam', """
OFFER MESSAGE
[Name of offer] for [who]
What you get: ____________
Price: ₹____ (early price for the first __ customers)
Delivery or start date: ____________
How to book: pay ₹____ advance by UPI to ____,
or fill in this form: [link]
My promise: if I can't deliver by [date], full refund.
Questions? WhatsApp [number]

MALAYALAM (short version)
[ഓഫറിന്റെ പേര്] — [ആർക്കുവേണ്ടി]
ലഭിക്കുന്നത്: ____________
വില: ₹____ (ആദ്യത്തെ __ പേർക്ക്)
ഡെലിവറി തീയതി: ____________
ബുക്ക് ചെയ്യാൻ ₹____ അഡ്വാൻസ് UPI വഴി അയയ്ക്കുക.
[തീയതി]ക്കകം നൽകാനായില്ലെങ്കിൽ മുഴുവൻ തുകയും തിരികെ നൽകും.
""", ''),
        ('smoke test log (Experiments tab)', """
Date,Experiment,Assumption tested,Success criterion,People reached,Replies,Sign-ups,Payments,Result,Decision
,WhatsApp pre-order for 1 kg plum cake,Parents will pay 850 rupees for a home-made cake,8 bookings with 200 rupees advance in 10 days,,,,,,
""", 'csv'),
    ],
    mistakes=[
        ('No success criterion.', 'Without a bar set in advance, every result looks like a success. Write it down first.'),
        ('Testing only on friends.', 'Friends buy out of kindness. At least half your reach should be people who owe you nothing.'),
        ('No clear call to action.', '"Let me know if interested" gets silence. Say exactly how to book and pay.'),
        ('Taking money you can\'t honour.', 'Pre-sell only what you can deliver, and refund fast if you can\'t. In a small town, your reputation is your biggest asset.'),
        ('Paying for ads first.', 'Test with free channels and your interviewees first. Ads multiply a working offer; they don\'t fix a weak one.'),
    ],
    quiz=[
        {'q': 'Which is the strongest evidence?',
         'o': ['200 likes', '30 sign-ups', '8 advance payments', '"Great idea!"'],
         'a': 'C', 'why': 'Money paid in advance is a real commitment.'},
        {'q': 'When should you set your success criterion?',
         'o': ['After seeing the results', 'Before the test starts', 'Never', 'When a friend asks'],
         'a': 'B', 'why': 'A bar set in advance can\'t be bent to fit the results.'},
        {'q': 'Nisha aimed for 8 bookings and got 11. Fathima aimed for 20 pre-orders and got 9. What should Fathima do?',
         'o': ['Call it a success anyway', 'Change one thing (offer, price, audience or message) and test again, or reconsider the idea', 'Build the full pack straight away', 'Buy ads'],
         'a': 'B', 'why': 'The test missed its bar. Learn why, change one thing and test again.'},
        {'q': 'Which smoke test is not honest?',
         'o': ['A "coming soon" waiting list', 'A pre-order with a refund promise', 'Showing fake reviews to look popular', 'A pilot at an early price'],
         'a': 'C', 'why': 'Fake reviews deceive customers and can break consumer protection law.'},
    ],
    study='the Lean Startup principles, OpenStax 6.4 and the Google Forms guide (about 1 hour)',
    action='run a smoke test to 50 or more people with a success criterion set in advance, and record every commitment',
)

L3 = lesson(
    4, 3,
    title='Build a no-code MVP and deliver it by hand',
    weeks=(9, 9), hours=4,
    outcome='Build the smallest version of your offer with free no-code tools, deliver it by hand to your first customers and collect their feedback.',
    split='50 minutes study, 3 hours 10 minutes action',
    core="""
An **MVP (minimum viable product)** is the smallest thing you can deliver that solves the core problem well enough for someone to pay. Michael Seibel of Y Combinator stresses launching something quickly and learning from real users instead of polishing in private. Your MVP will feel embarrassingly simple. That is correct.

### Four kinds of MVP that need no code

- **Concierge:** you do everything by hand for each customer. Arun sets up each shop himself; Meera rewrites each CV herself.
- **Wizard of Oz:** it looks automated to the customer, but you do the work behind the scenes, for example a "booking system" that is really a Google Form plus you replying.
- **Single feature:** one thing done well: only birthday cakes in two sizes, or one 100-question PSC pack.
- **Pre-order:** the pre-sale itself, with delivery to follow, as in the last lesson.

### MVPs by path

| Path | A good MVP | Free tools |
| --- | --- | --- |
| Local business | A small menu, small batches, orders on WhatsApp, pickup or nearby delivery | WhatsApp Business catalogue, Canva price list, UPI |
| Freelance → agency | One clear service, done by hand with a checklist | WhatsApp Business, Google Business Profile, a Google Docs checklist |
| Digital product | One small pack or one mock test, as a PDF or a Google Forms quiz | Google Docs (download as PDF), Google Forms, WhatsApp or Telegram |
| Online service | A fixed-scope package with an intake form and a template | Google Forms, Docs, Meet, Canva |

### Rules for your MVP

1. **Time-box it.** Build it in 7 days or less.
2. **Must-haves only.** List everything you could include, then cut until only what solves the core problem is left.
3. **Safe and legal is not optional.** Hygiene for food, accurate content, clear prices, honest descriptions.
4. **Do it by hand first.** Automate only once you have done it manually enough times to know exactly what to automate (Module 10).
5. **Plan the feedback.** Decide the five questions you will ask every customer after delivery.

Paul Graham's essay "Do Things That Don't Scale" explains why founders who personally recruit and delight their first customers learn faster than those who wait for a perfect product.
""",
    example="""
Arun's MVP for Rasheed's textile shop took one day and cost nothing but his time and ₹100 in bus fares:

- WhatsApp Business set up on the shop's number: profile, address, opening hours, location
- A catalogue of 30 sarees and salwar sets, photographed on Arun's phone by the shop window in daylight, with prices
- Five quick replies in Malayalam and English: prices, timings, location, delivery, new stock
- Labels for "new enquiry", "price sent", "ordered" and "paid"
- An away message for after 9 pm
- The shop's Google Business Profile claimed, with 15 photos
- A one-page instruction sheet for the staff, and 30 minutes of training

Price: ₹999 for the pilot. Two weeks later, Arun asked Rasheed his five feedback questions. Rasheed said evening replies were faster and that two customers had ordered from the catalogue without visiting. He also asked for help adding new stock every week, which became Arun's first monthly care plan.
""",
    resources=[
        ('yc-mvp', 'Watch the whole talk', 'about 17 min'),
        ('pg-ds', 'Read it all', '20 min'),
        ('wa-business', 'Read the feature list: catalogue, quick replies, labels, away messages', '5 min'),
        ('gsheets', 'Only if your MVP needs a sheet: create, edit and share one', '10 min'),
    ],
    steps=[
        'List everything your MVP could include. Cross out everything that isn\'t needed to solve the core problem for your first customers.',
        'Build it in 7 days or less with free tools. Write down each step as you go; this becomes your first SOP in Module 10.',
        'Deliver it by hand to every customer who paid in your smoke test, or to at least one paying customer.',
        'After delivery, ask the five feedback questions below and write the answers word for word.',
        'Note how long delivery took and what it cost you. You will need these numbers in Module 5.',
    ],
    proof='A photo, screenshot or file of your MVP, your build checklist, and feedback from at least one paying customer.',
    templates=[
        ('MVP scope and feedback questions', """
MVP SCOPE
Core problem it solves: ____________
Must-have (keep): ____________
Nice-to-have (later): ____________
Build by (7 days at most): ____
Delivered to: ____  Time per delivery: ____  Cost: ₹____

FEEDBACK QUESTIONS (ask every customer)
1. What did you hope this would do for you?
2. What happened when you used it?
3. What was confusing or annoying?
4. How would you feel if you could no longer use this?
   (very disappointed / a bit disappointed / not bothered)
5. Who else do you know who has this problem?
""", ''),
    ],
    mistakes=[
        ('Building too much.', 'If your MVP takes more than a week, you are building version 3. Cut features.'),
        ('Perfecting the brand first.', 'A plain WhatsApp catalogue that solves the problem beats a beautiful logo that doesn\'t. Branding comes in Module 6.'),
        ('Automating too early.', 'You don\'t yet know which steps matter. Do it by hand ten times first.'),
        ('Skipping feedback.', 'Delivery without feedback wastes your best moment for learning. Ask the five questions every time.'),
    ],
    quiz=[
        {'q': 'What is an MVP?',
         'o': ['The final, polished product', 'The smallest version that solves the core problem well enough for someone to pay', 'A free sample', 'A business plan'],
         'a': 'B', 'why': 'Its job is to deliver real value and real learning as early as possible.'},
        {'q': 'What does a "concierge" MVP mean?',
         'o': ['A hotel service', 'You do everything by hand for each customer', 'Fully automated software', 'Hiring staff to do it'],
         'a': 'B', 'why': 'Doing it by hand shows you exactly what customers need before you build anything.'},
        {'q': 'How long should building your first MVP take?',
         'o': ['6 months', 'About 7 days or less', 'A year', 'Until it is perfect'],
         'a': 'B', 'why': 'A short time-box forces you to keep only what matters.'},
        {'q': 'Why ask, "How would you feel if you could no longer use this?"',
         'o': ['To scare the customer', 'It shows whether the product really matters to them', 'To get a discount', 'The law requires it'],
         'a': 'B', 'why': '"Very disappointed" answers are a strong sign you are solving a real problem.'},
    ],
    study='the YC MVP talk, "Do Things That Don\'t Scale" and the WhatsApp Business features (about 50 minutes)',
    action='build a no-code MVP in 7 days or less, deliver it by hand to a paying customer and collect feedback',
)

L4 = lesson(
    4, 4,
    title='Measure results and decide: persevere, pivot or stop',
    weeks=(10, 10), hours=3,
    outcome='Turn your test results into a clear written decision (persevere, pivot or stop) using criteria set in advance, and plan the next experiment.',
    split='1 hour study, 2 hours action',
    core="""
You have run tests. Now be honest with the numbers. This lesson gives you a simple way to read them and decide.

### Read your funnel

Write your results as a funnel, step by step:

**People reached → replies or clicks → conversations → offers made → payments → delivered → happy (would be very disappointed without it) → repeat or referral**

Work out the conversion rate at each step, for example payments ÷ people reached. The step with the biggest drop is where to look first.

### Actionable numbers and vanity numbers

**Vanity numbers** feel good but don't guide decisions: likes, followers, Status views. **Actionable numbers** link a change to a result: "Sending the offer personally to interviewees converted at 30%; posting in groups converted at 2%." The Lean Startup calls this innovation accounting: measuring progress by what you have validated, not by how busy you were.

### Small numbers

With 50 people reached, one or two extra sales swing your percentage a lot. Treat early results as signals, not proof. If a result is close to your criterion, run the test once more with a fresh group before you make a big decision.

### The three decisions

- **Persevere:** you met your criteria. Keep the idea, improve the weakest step of the funnel and go on to Module 5.
- **Pivot:** part of the idea works. Change one big thing and test again. Common pivots:
    - **Customer:** the same offer for a different group (shops → clinics)
    - **Problem:** the same customers, a different problem (late replies → stock updates)
    - **Channel:** the same offer through a different route (groups → personal visits)
    - **Price or model:** the same offer, paid differently (one-off → monthly)
    - **Offer:** the same customers and problem, a different solution (a full pack → weekly mini-tests)
- **Stop:** after two or three well-run tests with no real commitments, when the numbers can never work (each sale loses money), or when the business would need you to do something unethical. Stopping a weak idea early is a success: you go back to your backup list with real skills.

### Beware the sunk-cost trap

"I've already spent 10 weeks on this" is not a reason to continue. The only question is: knowing what I know now, is this the best use of my next 10 weeks?

Write your decision down, with the numbers, and share it with someone. A written decision is much harder to drift away from.
""",
    example="""
Three decision memos:

**Arun: persevere.** 15 owners interviewed → 11 offered a pilot → 4 paid ₹999 → 4 delivered → 3 "very disappointed" without it → 2 asked for monthly help. His criterion was 3 paid pilots, so it was met. The weakest group: the pharmacies and the hardware shop said no (privacy worries, few WhatsApp enquiries). Decision: persevere with textile and mobile shops only, and test a ₹500 monthly care plan next.

**Fathima: pivot.** 300 views → 31 replies → 9 pre-orders at ₹99, against a criterion of 20. Replies said ₹99 was fine, but people wanted to try before buying and wanted weekly practice rather than one big pack. Decision: an offer pivot to a free weekly 20-question mock test in a WhatsApp channel, plus a ₹49-a-month paid group with full answers and rank lists. She will test it for 4 weeks.

**A stopped idea.** Arun's bill-payment help for elders: in 6 conversations, everyone said their children abroad already paid the bills online, and two nearby Akshaya centres helped for small fees. Decision: stop, and give the time to ShopAssist.
""",
    resources=[
        ('lean-principles', 'Re-read "Innovation Accounting" and "Build-Measure-Learn"', '5 min'),
        ('os10', 'Sections 10.1 Launching the Imperfect Business: Lean Startup and 10.4 Managing, Following, and Adjusting the Initial Plan', '45 min'),
        ('a16z', 'Skim the list; read the parts on customer acquisition cost and churn', '15 min'),
    ],
    steps=[
        'Write your funnel with the real numbers from your Experiments tab, and work out the conversion rate at each step.',
        'Compare the results with the success criterion you wrote before the test.',
        'Choose persevere, pivot (name the type) or stop, using the decision memo template.',
        'Plan your next experiment: what you will change, the new criterion and the date.',
        'Share the memo with your accountability buddy or a mentor and ask them to challenge it. Write down what they say.',
    ],
    proof='Your funnel numbers, the decision memo with your next experiment, and the reviewer\'s response.',
    templates=[
        ('decision memo', """
DECISION MEMO     Date: ____
Hypothesis tested: ____________
Success criterion (written on ____): ____________

FUNNEL
Reached ____ → replies ____ → conversations ____
→ offers ____ → payments ____ → delivered ____
→ "very disappointed" without it ____
→ repeat or referral ____
Biggest drop: from ____ to ____

Result against criterion: met / close / not met
Decision: PERSEVERE / PIVOT (type: ____) / STOP
Why, in 3 sentences: ____________

NEXT EXPERIMENT
Change: ____________
New criterion: ____________  By: ____
Reviewed by: ____  Their challenge: ____________
""", ''),
    ],
    mistakes=[
        ('Moving the goalposts.', 'If you lower the bar after seeing the results, you are fooling yourself. Judge against what you wrote first.'),
        ('Counting likes.', 'Views and likes are vanity numbers. Count replies, payments and repeat orders.'),
        ('Quitting after one weak test.', 'One test can fail because of the message or the channel. Change one thing and test again before you stop.'),
        ('Never stopping.', 'If three honest tests show no commitments, stop. Your backup ideas are waiting.'),
    ],
    quiz=[
        {'q': 'You reached 60 people and 6 paid. What is the conversion rate?',
         'o': ['6%', '10%', '60%', '1%'],
         'a': 'B', 'why': '6 ÷ 60 = 0.10, which is 10%.'},
        {'q': 'Which of these is an actionable number?',
         'o': ['1,000 Status views', 'Personal messages converted at 30% and group posts at 2%', '500 followers', '50 likes'],
         'a': 'B', 'why': 'It tells you what to do next: send more personal messages.'},
        {'q': 'You keep the same offer but switch from shops to clinics. What kind of pivot is that?',
         'o': ['A customer pivot', 'A price pivot', 'A channel pivot', 'It is not a pivot'],
         'a': 'A', 'why': 'The offer stays; the customer group changes.'},
        {'q': '"I\'ve already spent 10 weeks, so I must continue." What is this?',
         'o': ['Healthy persistence', 'The sunk-cost trap', 'A pivot', 'Innovation accounting'],
         'a': 'B', 'why': 'Time already spent can\'t be recovered. Decide on what you know now.'},
        {'q': 'When is stopping the right decision?',
         'o': ['After the first "no"', 'After two or three well-run tests with no real commitments, or when every sale loses money', 'Never', 'Whenever a friend says so'],
         'a': 'B', 'why': 'Stop on evidence, not on a single bad day or someone else\'s opinion.'},
    ],
    study='the Lean Startup principles, OpenStax 10.1 and 10.4, and the a16z metrics (about 1 hour)',
    action='turn your test numbers into a written persevere, pivot or stop decision and plan the next experiment',
)

LESSONS = [L1, L2, L3, L4]

MODULE = module(
    4,
    title='Validation and MVP',
    weeks=(8, 10), hours=18,
    overview="""
Validation is where you stop asking and start testing. You put a real offer in front of real people and watch what they do: reply, sign up, pay a deposit or ignore it. Then you deliver the smallest version of your product by hand and measure what happens.

By week 10 you have evidence, not opinions, and you make a written decision: carry on, change one big thing, or stop. For many learners, this is also where the first rupees arrive.
""",
    outcomes=[
        'Map your business on a Lean Canvas, rank your riskiest assumptions and know when to use the Business Model Canvas',
        'Run an honest smoke test and ask for real commitments: pre-orders, deposits or paid trials',
        'Build a no-code MVP with free tools and deliver it by hand',
        'Measure results against criteria set in advance and decide to persevere, pivot or stop',
    ],
    lessons=LESSONS,
    project='Validation evidence pack',
    project_steps=[
        'Your Lean Canvas, with the riskiest assumptions marked (L01).',
        'Your smoke-test offer, success criterion and results (L02).',
        'Your MVP and the feedback from your first customers (L03).',
        'Your decision memo: persevere, pivot or stop, with the numbers (L04).',
        'Share the pack with a mentor or an experienced business owner and add their reaction.',
    ],
    project_proof='The pack (one Google Doc, or four files) in Founder Toolkit/04 Validation, with the Experiments tab filled in.',
    rubric=[
        ('Canvas', 'Missing, or "everyone" as the customer', 'Filled with guesses', 'Filled from evidence, riskiest assumptions ranked'),
        ('Test design', 'No success criterion', 'Criterion set after seeing results', 'Criterion written and dated before the test'),
        ('Evidence strength', 'Likes and compliments', 'Sign-ups or "yes" replies', 'Deposits, pre-orders or paid trials'),
        ('MVP', 'Not built, or still building after weeks', 'Built but not delivered', 'Delivered to a paying customer, with feedback'),
        ('Decision', 'None', '"Let\'s see"', 'Written persevere, pivot or stop, with numbers'),
    ],
    short=[
        'L01: fill the Lean Canvas only, and skip the Business Model Canvas.',
        'L02: run one smoke test to 30 people on WhatsApp only.',
        'L03: deliver your MVP by hand to one customer.',
        'L04: write a half-page decision memo.',
    ],
    mistakes=[
        ('Building for weeks before any test.', 'Test with an offer first; build after people commit.'),
        ('Testing only on friends.', 'At least half of the people you reach should be strangers or friends of friends.'),
        ('Changing the success criterion after the results.', 'Write it down, with the date, before you start.'),
    ],
)
