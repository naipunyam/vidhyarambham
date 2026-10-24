from common import lesson, module

L1 = lesson(
    5, 1,
    title='Revenue models and your value proposition',
    weeks=(11, 11), hours=3,
    outcome='Choose how you will charge (your revenue model) and write a value proposition that customers understand and can repeat back.',
    split='1 hour 15 minutes study, 1 hour 45 minutes action',
    core="""
### Revenue models: how money comes in

| Model | How it works | Example | Good when |
| --- | --- | --- | --- |
| One-time sale | Pay once per item | A birthday cake | Clear, simple products |
| Repeat purchase | The same customer buys again and again | A weekly snack box for an office | Things that get used up |
| Project fee | A fixed price for a defined job | ₹1,500 WhatsApp setup | Services with a clear end |
| Hourly or daily rate | Pay for time | ₹300 an hour for design changes | Unclear scope (but it caps your income) |
| Productised service | The same package at the same price for many customers | ₹999 CV makeover | Repeated service work |
| Subscription or retainer | A fixed amount every month | ₹500 a month "shop care plan" | Ongoing needs; steady income |
| Freemium | A free basic version, with paid extras | A free weekly test; ₹49 a month for full answers | Digital products that cost little per user |
| Commission | A percentage of a sale you bring | 10% for sending cake orders to a decorator | Partnerships |
| Bundle | Several things together at one price | Setup plus 3 months of care for ₹2,700 | Raising the average order |

**Recurring revenue** (subscriptions, retainers, repeat orders) is gold for a small business: you start each month with income already expected, instead of from zero. Look for a recurring piece in your model.

Avoid models that only work at huge scale, such as advertising income from a channel or an app that is free for everyone. They need very large audiences, which you won't have in your first year.

### Your value proposition

A **value proposition** is the promise of value that makes a customer choose you. Strategyzer's Value Proposition Canvas (a free PDF) has two sides that you match:

- **Customer profile:** the customer's **jobs** (what they are trying to get done), **pains** (what annoys them or gets in the way) and **gains** (what they want to happen).
- **Value map:** your **products and services**, the **pain relievers** that remove particular pains and the **gain creators** that produce particular gains.

You have a fit when your pain relievers and gain creators match the jobs, pains and gains your interviews found.

### Say it in one breath

**We help [customer] [get the job done] by [how], unlike [alternative].**

Then add three proof points: a number, a quote and a guarantee. For example: "replies in under 5 minutes" (number), "two orders from the catalogue in the first week" (a customer's words), "money back within 14 days if it doesn't help" (guarantee).

Test it: say it to five target customers and ask, "What do you think this is, and who is it for?" If four of the five repeat it back correctly, it works.
""",
    example="""
**Arun's revenue model:** a ₹1,500 one-time setup (a project fee) plus an optional ₹500-a-month care plan (a retainer): new stock added to the catalogue every week, quick replies kept up to date and a one-page monthly report. The care plan matters most. With 10 shops on it, he starts every month with ₹5,000 already expected.

**His value proposition:** "We help textile and mobile shops in Kuttiady reply to every WhatsApp customer in minutes, with photos and prices, unlike late-night replies from the owner's phone." Proof points: replies in under 5 minutes during shop hours; Rasheed's words, "Two customers ordered from the catalogue without coming in"; money back within 14 days if it doesn't help.

When he tested it on five shop owners, three repeated it back correctly and two thought it was "a new app". He changed "a WhatsApp system" to "we set up WhatsApp Business on your own phone", and the next three all understood it.
""",
    resources=[
        ('yc-pricing', 'Watch the first half, on business models', 'about 16 min'),
        ('vpc', 'Download the free PDF and read both sides: the customer profile and the value map', '15 min'),
        ('blank-udacity', 'Lessons "Value Proposition" (if not done) and "Revenue Model"', 'about 45 min'),
    ],
    steps=[
        'List at least three revenue models that could fit your idea. Choose one main model, plus a recurring piece if you can.',
        'Fill in the value proposition worksheet with jobs, pains and gains from your interview notes, then your pain relievers and gain creators.',
        'Write your one-breath value proposition and three proof points.',
        'Test it on five target customers: say it, then ask, "What do you think this is, and who is it for?" Write down their answers word for word.',
        'Rewrite it until at least four out of five people repeat it back correctly.',
    ],
    proof='Your chosen revenue model with reasons, the value proposition worksheet and the test log with five answers.',
    templates=[
        ('value proposition worksheet', """
VALUE PROPOSITION WORKSHEET
Customer: ____________
Jobs (from interviews): 1. ____ 2. ____ 3. ____
Pains: 1. ____ 2. ____ 3. ____
Gains: 1. ____ 2. ____ 3. ____

My products and services: ____________
Pain relievers (one for each pain): ____________
Gain creators (one for each gain): ____________

ONE BREATH
We help ____ ____ by ____, unlike ____.
Proof points: number ____ / quote ____ / guarantee ____

TEST LOG (5 customers)
1. What they said it is: ____  Who it's for: ____  Correct? __
2. ____
3. ____
4. ____
5. ____

REVENUE MODEL
Main model: ____  Recurring piece: ____
Why it fits my customers: ____________
""", ''),
    ],
    mistakes=[
        ('Listing features instead of results.', '"Catalogue, labels, quick replies" are features. "Reply to every customer in minutes" is a result. Lead with results.'),
        ('Copying big companies\' models.', 'Free-for-everyone apps and advertising income need huge audiences. Charge from day one.'),
        ('Using jargon.', 'If a shop owner wouldn\'t say the words, don\'t use them. Test it in Malayalam too.'),
        ('Having no recurring piece.', 'Look for something customers need every month. It turns a stressful business into a steadier one.'),
    ],
    quiz=[
        {'q': 'Which of these is recurring revenue?',
         'o': ['A one-off cake order', 'A ₹500-a-month care plan', 'A single CV rewrite', 'A stall at one festival'],
         'a': 'B', 'why': 'It repeats every month without a new sale.'},
        {'q': 'In the Value Proposition Canvas, what are "pains"?',
         'o': ['Your costs', 'What annoys customers or gets in the way of their job', 'Your competitors', 'Your prices'],
         'a': 'B', 'why': 'Pains belong to the customer profile. Your pain relievers should match them.'},
        {'q': 'Which of these is a result rather than a feature?',
         'o': ['Quick replies', 'Labels', '"Reply to every customer within minutes"', 'A catalogue'],
         'a': 'C', 'why': 'It describes what changes for the customer.'},
        {'q': 'How do you know your value proposition works?',
         'o': ['You like it', 'At least 4 of 5 target customers can say what it is and who it is for', 'It is long and detailed', 'It uses technical words'],
         'a': 'B', 'why': 'If customers can repeat it, they can also repeat it to their friends.'},
    ],
    study='the first half of the YC pricing talk, the Value Proposition Canvas and two Steve Blank lessons (about 1 hour 15 minutes)',
    action='choose a revenue model, write a one-breath value proposition and test it on five customers',
)

L2 = lesson(
    5, 2,
    title='Unit economics: what one sale really earns',
    weeks=(11, 11), hours=3,
    outcome='Calculate the real profit on one sale or one customer, including materials, delivery, fees, your time and the cost of winning the customer.',
    split='1 hour study, 2 hours action',
    core="""
**Unit economics** answers one question: when I make one more sale, do I make money? A "unit" is one sale (a cake, a setup, a pack) or one customer over time.

### The key numbers

- **Price:** what the customer pays. If you are registered for GST, use the price without GST.
- **Variable costs:** costs that rise with each sale: ingredients or materials, packaging, delivery fuel, payment fees, platform commissions, wastage.
- **Contribution per unit = price − variable costs.** This is what each sale adds towards your fixed costs and profit.
- **Contribution margin = contribution ÷ price × 100%.**
- **Your time:** hours per unit. **Earnings per hour = contribution ÷ hours.** Compare it with what you could earn another way, such as an hour of tuition.
- **Customer acquisition cost (CAC):** what it costs to win one new customer: free samples, discounts, travel to meet them, ads, referral rewards. **CAC = money spent on winning customers ÷ number of new customers.**
- **Lifetime value (LTV), simple version:** contribution per order × the number of orders a typical customer makes. Use what you actually see, not what you hope.
- **LTV ÷ CAC:** if winning a customer costs more than they will ever contribute, growth makes you poorer. Investors often look for LTV several times bigger than CAC; your rule is simply that LTV must be clearly bigger.

### Hidden costs beginners forget

Wastage and failed batches, gas and electricity, phone data, boxes and stickers, travel to suppliers, payment gateway fees (Razorpay, for example, lists 2% plus GST per transaction on its standard plan; plain UPI into your bank account usually costs less), free extras such as candles and toppers, and the discount you give "just this once".

### Fixed costs come next

Rent, equipment instalments, phone plans and subscriptions don't change with each sale. In Module 8 you will compare them with your contribution to find your break-even point.
""",
    example="""
**Nisha's 1 kg chocolate cake** (prices from her Kuttiady supermarket in November):

| Item | ₹ |
| --- | --- |
| Price | 800 |
| Ingredients (flour, cocoa, butter, eggs, cream, sugar) | 310 |
| Gas and electricity | 35 |
| Box and cake board | 40 |
| Candles and topper (free extras) | 15 |
| Delivery fuel (4 km on average) | 30 |
| Wastage allowance (5% of ingredients) | 16 |
| **Variable cost** | **446** |
| **Contribution** | **354** |
| Contribution margin | 44% |

Time: 2.5 hours for baking, decorating and delivery. Earnings per hour: ₹354 ÷ 2.5 = **about ₹142**.

If she gives ₹100 off, her contribution falls to ₹254. A 12.5% cut in price takes away 28% of what she keeps. Discounts cost more than they look.

**Winning customers:** she gives a ₹200 tasting box to a new family, and about half of the boxes lead to an order, so her CAC is about ₹400. A typical family orders 3 cakes a year, so LTV = 3 × ₹354 = ₹1,062. LTV ÷ CAC is about 2.7: tasting boxes pay off, but only if families come back.

**Arun's setup:** price ₹1,500, variable costs ₹150 (bus fares and data), contribution ₹1,350, time 5 hours, so ₹270 an hour. His care plan: ₹500 a month for about 1.5 hours of work, roughly ₹330 an hour, and it repeats every month.
""",
    resources=[
        ('yc-pricing', 'Watch the second half, on pricing', 'about 17 min'),
        ('a16z', 'Read the parts on gross profit, lifetime value (LTV) and customer acquisition cost (CAC)', '20 min'),
        ('os9', 'Section 9.3 Accounting Basics for Entrepreneurs, for the cost terms', '20 min'),
        ('razorpay', 'Only if you will use a payment gateway: the fee per transaction (check current rules)', '5 min'),
    ],
    steps=[
        'Choose your main unit: one cake, one setup, one pack, one CV.',
        'Get real prices for every input. Check your receipts, or ask two suppliers by phone or WhatsApp.',
        'Time yourself delivering one unit, from start to finish.',
        'Fill in the unit economics sheet below: contribution, margin, earnings per hour, CAC and LTV.',
        'Write down one change that would improve your numbers (a cheaper supplier, a new price, less wastage, a bundle), and ask a supplier or customer about it this week.',
    ],
    proof='Your filled unit economics sheet with real prices, your timing and the improvement you plan.',
    templates=[
        ('unit economics calculator (Unit economics tab)', """
Item,Amount per unit (Rs),Notes
Price (without GST if registered),,
Materials or ingredients,,
Packaging,,
Delivery,,
Payment or platform fees,,
Wastage allowance,,
Free extras,,
Variable cost total,=SUM(B3:B8),
Contribution,=B2-B9,
Contribution margin %,=B10/B2*100,
Hours per unit,,
Earnings per hour,=B10/B12,
Spent on winning customers this month,,
New customers this month,,
Customer acquisition cost (CAC),=B14/B15,
Orders per customer per year,,
Lifetime value (LTV),=B10*B17,
LTV divided by CAC,=B18/B16,
""", 'csv'),
    ],
    mistakes=[
        ('Forgetting your time.', 'A cake that earns ₹142 an hour is a business; one that earns ₹40 an hour is a hobby. Always work out earnings per hour.'),
        ('Leaving out small costs.', 'Boxes, candles, data, fees and wastage add up to a big share of the price. List them all.'),
        ('Treating a discount as normal.', 'A small price cut takes a big bite out of contribution. Calculate before you discount.'),
        ('Ignoring CAC.', 'Free samples and travel are real costs of winning customers. If CAC is more than LTV, more customers means more loss.'),
    ],
    quiz=[
        {'q': 'Price ₹500, variable cost ₹300. What is the contribution?',
         'o': ['₹800', '₹200', '₹300', '₹500'],
         'a': 'B', 'why': '₹500 − ₹300 = ₹200.'},
        {'q': 'Contribution ₹200 on a price of ₹500. What is the contribution margin?',
         'o': ['20%', '40%', '60%', '250%'],
         'a': 'B', 'why': '₹200 ÷ ₹500 × 100% = 40%.'},
        {'q': 'You spent ₹1,200 on samples and travel and won 4 new customers. What is your CAC?',
         'o': ['₹300', '₹1,200', '₹4,800', '₹120'],
         'a': 'A', 'why': '₹1,200 ÷ 4 = ₹300 per customer.'},
        {'q': 'Contribution is ₹354 per order and a customer orders 3 times a year. What is the simple LTV?',
         'o': ['₹354', '₹1,062', '₹118', '₹3,540'],
         'a': 'B', 'why': '3 × ₹354 = ₹1,062.'},
        {'q': 'Which of these is a variable cost?',
         'o': ['A monthly phone plan', 'An oven instalment', 'Cake boxes', 'Shop rent'],
         'a': 'C', 'why': 'You need one more box for every extra cake; the others stay the same each month.'},
    ],
    study='the second half of the YC pricing talk, the a16z metrics and OpenStax 9.3 (about 1 hour)',
    action='cost out one unit with real prices and your timing, and calculate contribution, CAC and LTV',
)

L3 = lesson(
    5, 3,
    title='Set your price with confidence',
    weeks=(12, 12), hours=4,
    outcome='Choose a price and 2–3 packages using your costs, the value to the customer and the alternatives, then test them on at least 5 real customers.',
    split='1 hour study, 3 hours action',
    core="""
Many beginners price too low, out of fear. A low price doesn't make you more competitive if it leaves you exhausted and unable to deliver well. Look at price from three directions.

### 1. The floor: your costs

Your price must cover the variable cost, a share of fixed costs and a fair hourly earning for you. Below the floor, every sale loses money or your time.

**Floor = variable cost per unit + (monthly fixed costs ÷ units a month) + (hours per unit × your target hourly earning)**

### 2. The reference: the alternatives

What does the customer pay for the next-best option, including hidden costs? For Nisha's customers, the Vatakara cake costs ₹900 plus an hour of travel. That is the comparison in their minds.

### 3. The ceiling: the value to the customer

What is solving the problem worth to them? If one extra saree sale a week earns Rasheed ₹600 of profit, a ₹500-a-month care plan pays for itself in the first week. Value-based pricing charges a share of the value you create.

Set your price between the floor and the ceiling, near the reference, and above it if you are clearly better.

### Packages

Offer 2–3 options, so customers choose between your packages instead of between you and someone else:

| Package | Its job |
| --- | --- |
| Basic | The entry price: just the core job |
| Standard (most chosen) | What most people need; mark it as the popular choice |
| Premium | More service or speed; it makes the standard look reasonable |

Spell out exactly what each one includes and what it doesn't. Add-ons (extra photos, rush delivery, an extra revision) let customers pay for what they value.

### Payment terms and promises

- Ask for an **advance** on custom work. 50% before you start is common for cakes and services.
- Accept UPI and give a receipt for every payment.
- State your refund or redo policy before the sale, not after a complaint.
- Show prices clearly. For packed products, India's legal metrology rules require label details such as the MRP (check current rules).

### Test prices with real people

Quote your price confidently, then stop talking and listen. If everyone says yes at once, you may be too cheap. If nobody does, find out whether the problem is the price or the value. Try different prices with similar customers and record each response. Raise prices for new customers first, and give existing customers notice.

### Indian pricing habits

Prices like ₹499 or ₹999 are common, and customers are used to them. Festival offers work, but give them an end date and keep them occasional, or customers learn to wait for the next one.
""",
    example="""
**Arun's price test.** His floor for a setup: ₹150 variable cost + 5 hours × his ₹250 target = ₹1,400. The reference: a nephew does it "for free" but badly, and a Kozhikode agency quoted Rasheed ₹5,000. The ceiling: one extra sale a week is worth more than ₹2,000 a month to a shop.

He offered three packages to 8 shop owners:

| Package | What's included | Price | Chosen by |
| --- | --- | --- | --- |
| Basic | WhatsApp Business profile, 5 quick replies, away message | ₹999 | 1 |
| Standard | Basic, plus a 30-item catalogue, labels, Google Business Profile and staff training | ₹1,800 | 4 |
| Premium | Standard, plus 3 months of the care plan | ₹2,900 | 1 |

Two owners said all three were too expensive. Six of the eight bought, at an average of about ₹1,850, more than the ₹1,500 he had planned to charge. Standard became his main offer.

**Meera's CV Makeover** has three packages: ₹499 (CV only), ₹999 (CV and LinkedIn profile, the most chosen) and ₹1,799 (CV, LinkedIn and a 30-minute mock interview on Google Meet). She takes full payment upfront and includes one free revision.
""",
    resources=[
        ('yc-pricing', 'Re-watch the pricing part and note three ideas you will try', '15 min'),
        ('os8', 'Section 8.1 Entrepreneurial Marketing and the Marketing Mix, the part on price', '20 min'),
        ('blank-udacity', 'Lesson "Revenue Model", if you haven\'t done it', 'about 30 min'),
        ('legal-metrology', 'Only if you sell packed products: what the label must show (check current rules)', '5 min'),
    ],
    steps=[
        'Calculate your floor, write down the reference price and estimate the ceiling.',
        'Design 2–3 packages, listing exactly what is included and excluded, plus any add-ons.',
        'Quote them to at least 5 potential customers. Say the price, then wait. Record yes, no or hesitation, and the words they use.',
        'Set your launch price list and payment terms: the advance, and your refund or redo policy.',
        'Put the price list on a one-page offer sheet (Canva or Google Docs) and into your WhatsApp Business catalogue.',
    ],
    proof='Your floor, reference and ceiling numbers, the price test log with 5 or more people, and your one-page price list.',
    templates=[
        ('price calculator and packages', """
PRICE FLOOR
Variable cost per unit: ₹____
+ fixed costs a month ₹____ ÷ units a month ____ = ₹____
+ hours per unit ____ × target ₹____ an hour = ₹____
= FLOOR ₹____

REFERENCE (next-best option, with hidden costs): ₹____
CEILING (value to the customer): ₹____

PACKAGES
Basic ₹____: includes ____ / excludes ____
Standard ₹____ (most chosen): includes ____
Premium ₹____: includes ____
Add-ons: ____ ₹____
Payment terms: ____% advance by UPI, balance on ____
Refund or redo policy: ____________
""", ''),
        ('price test log (paste into Google Sheets)', """
Date,Customer code,Package offered,Price quoted,Response (yes / no / hesitated),Their exact words,Bought? (amount)
""", 'csv'),
    ],
    mistakes=[
        ('Pricing by fear.', 'Customers judge value partly by price. Set it from the floor, the reference and the value, not from fear of hearing no.'),
        ('Copying the cheapest competitor.', 'You can\'t win a price war against a bigger shop. Compete on what your customers care about: trust, speed, quality, language.'),
        ('Too many options.', 'Five packages confuse people. Two or three are enough.'),
        ('Unclear scope.', '"Full setup" means different things to different people. List what is included, or you will do extra work for free.'),
        ('No advance on custom work.', 'Ask for 50% before you start. It also filters out people who aren\'t serious.'),
    ],
    quiz=[
        {'q': 'Variable cost ₹200; fixed costs ₹3,000 a month over 30 units; 1 hour per unit at a ₹150 target. What is the floor?',
         'o': ['₹200', '₹300', '₹450', '₹350'],
         'a': 'C', 'why': '₹200 + (₹3,000 ÷ 30 = ₹100) + (1 × ₹150) = ₹450.'},
        {'q': 'Why offer three packages?',
         'o': ['To confuse customers', 'So customers choose between your options instead of between you and a competitor', 'The law requires it', 'To lower your prices'],
         'a': 'B', 'why': 'Packages also let customers who want more pay more.'},
        {'q': 'Every customer says yes to your price instantly. What might that mean?',
         'o': ['Your price may be too low', 'Your product is bad', 'You must lower the price', 'Nothing at all'],
         'a': 'A', 'why': 'Some hesitation is normal at a fair price. Test a higher price with new customers.'},
        {'q': 'What is a sensible payment term for a custom cake order?',
         'o': ['No payment until delivery', 'A 50% advance before you start', 'Payment after a month', 'A free first cake for everyone'],
         'a': 'B', 'why': 'An advance covers your ingredients and shows the order is real.'},
    ],
    study='the YC pricing section, OpenStax 8.1 on price and the Steve Blank revenue lesson (about 1 hour)',
    action='calculate your floor and ceiling, design packages and test them on at least 5 customers',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    5,
    title='Business models and pricing',
    weeks=(11, 12), hours=12,
    overview="""
Customers have shown interest. Now make sure each sale makes money. This module covers how you charge (the revenue model), what you promise (the value proposition), what one sale really earns you (unit economics) and what to charge (pricing).

Some small businesses with paying customers still fail here, because the price never covered the costs and the owner's time. You finish with an offer sheet you can send to any customer.
""",
    outcomes=[
        'Choose a revenue model that suits your customers and your path, with a recurring piece if possible',
        'Write a value proposition that customers understand and can repeat back',
        'Calculate contribution per sale, earnings per hour, customer acquisition cost and lifetime value',
        'Set a price floor and ceiling, design 2–3 packages and test prices with real customers',
    ],
    lessons=LESSONS,
    project='Offer sheet v1',
    project_steps=[
        'Your one-breath value proposition and three proof points (L01).',
        'Your revenue model and why it fits (L01).',
        'Your unit economics sheet for your main product or service (L02).',
        'Your price list: 2–3 packages, what each includes, add-ons, payment terms and refund policy (L03).',
        'Show the one-page offer sheet to 3 potential customers and write down the questions they ask. Fix anything that confused them.',
    ],
    project_proof='The one-page offer sheet, the unit economics sheet and the price test log, saved in Founder Toolkit/05 Offer.',
    rubric=[
        ('Value proposition', 'A list of features', 'Clear, but not tested', 'Tested: 4 of 5 customers repeat it back correctly'),
        ('Unit economics', 'Not calculated', 'Calculated without your time or fees', 'All variable costs, fees, your time and CAC included'),
        ('Price', 'Copied from the cheapest competitor', 'Cost-plus only', 'Floor, reference and ceiling used; tested with 5 or more people'),
        ('Packages and terms', 'One unclear price', 'Packages, but the scope is unclear', '2–3 packages with clear scope, advance and refund terms'),
    ],
    short=[
        'L01: write the one-breath value proposition and test it on 3 people.',
        'L02: calculate contribution per sale only; skip CAC and LTV for now.',
        'L03: set one price above your floor and quote it to 3 people.',
    ],
    mistakes=[
        ('Pricing by fear.', 'Base the price on value and your floor, not on fear of hearing no.'),
        ('Forgetting your own time.', 'Give your hours a rupee value in every calculation.'),
        ('Offering too many options.', 'Two or three packages are plenty.'),
    ],
)
