from common import lesson, module

L1 = lesson(
    12, 1,
    title='Retention and referrals: grow from the customers you have',
    weeks=(27, 27), hours=3,
    outcome='Measure repeat purchases and churn, and run two retention actions and a win-back push, measuring the results.',
    split='1 hour study, 2 hours action',
    core="""
Winning a new customer takes interviews, posts, visits, samples and follow-ups. Keeping one usually takes a good experience and a timely reminder. That is why growth from existing customers is often the cheapest growth a small business has.

### Measure it

- **Repeat rate**, for one-off purchases: customers who bought 2 or more times ÷ all customers, over the last 6 months.
- **Churn**, for subscriptions and care plans: customers who cancelled this month ÷ customers at the start of the month.
- **Average orders per customer** and **average order value**.
- **Simple cohorts:** of the customers who first bought in a given month, how many bought again in the next 3 months? Compare months to see whether you are improving.

Paul Graham's essay "Startup = Growth" argues that a startup should focus on its growth rate and let it guide decisions. For a micro-business, watch monthly numbers: is the repeat rate going up, and is churn going down?

### Ways to keep customers coming back

1. **Get the basics right every time:** on time and as promised. Customers often leave because of a poor or forgettable experience, not only because of price.
2. **Follow up:** a thank-you, a check-in a few days later, and one question: "Anything we could do better?"
3. **Remind, with permission:** occasion reminders (birthdays, anniversaries, school reopening, festival orders) for customers who say yes to them.
4. **Make repeating easy:** a "same as last time?" message, a subscription or care plan, a saved order form.
5. **Reward loyalty carefully:** a small thank-you, such as a free add-on with every fifth order, rather than permanent discounts that eat your margin.
6. **Win back lapsed customers:** a personal message to someone who hasn't ordered in 3 months: "It's been a while; here's what's new."
7. **Build a community:** a WhatsApp channel or a customer group (with consent) for updates and offers.

### Referrals at the right moment

Combine retention with the referral offer from ENT-M06-L04. Your happiest repeat customers are your best referrers, so ask them at the moment they are delighted.

### Respect consent

Collect birthdays and other dates only with the customer's clear permission, explain why ("so we can remind you"), and remove anyone who asks. It follows the DPDP Act's emphasis on consent, and it is simply good manners.
""",
    example="""
Nisha checked her last 6 months: 52 customers, 17 of whom ordered twice or more. Repeat rate: 17 ÷ 52 = 33%. She started two actions:

1. **Occasion reminders, with consent.** At delivery she asks, "Shall I remind you a week before next year's birthday?" 31 customers said yes, and their dates went into her calendar.
2. **"Same as last time?" messages** every Thursday to customers who had ordered a weekend snack box.

She also sent a win-back message to 12 Kuttiady customers who hadn't ordered for 3 months; 4 of them ordered within two weeks, about ₹3,000 of sales from one evening's messages.

Arun's care plan had 10 shops, and one cancelled in October: a churn of 10%. The reason: the owner couldn't see what he was paying for. Arun added a one-page monthly report with three numbers (new catalogue items, enquiries answered and the top question). Nobody cancelled the next month.
""",
    resources=[
        ('pg-growth', 'Read it all, thinking of your own business in monthly numbers', '25 min'),
        ('a16z', 'Read the parts on churn and active users', '10 min'),
        ('os10', 'Section 10.5 Growth: Signs, Pains, and Cautions', '25 min'),
    ],
    steps=[
        'Work out your repeat rate (or churn, for subscriptions) from your Customers tab for the last 3–6 months.',
        'Message 5 past customers to thank them and ask one question: "Anything we could do better?" Record their answers.',
        'Start two retention actions from the list, for example reminders with consent and "same as last time?" messages.',
        'Send a personal win-back message to customers who haven\'t bought for 3 months.',
        'After 2 weeks, measure the results: replies, repeat orders and referrals.',
    ],
    proof='Your repeat rate or churn calculation, the 5 customers\' feedback, your two retention actions and their results after 2 weeks.',
    templates=[
        ('retention tracker and messages', """
RETENTION TRACKER
Period: ____ to ____
Customers in the period: ____
Bought 2 or more times: ____
Repeat rate = ____ ÷ ____ = ___%
(Subscriptions) At the start: ____  Cancelled: ____
Churn = ____ ÷ ____ = ___%
Main reasons for leaving: ____________

ACTIONS (two at a time)
1. ____  Started ____  Result after 2 weeks: ____
2. ____  Started ____  Result after 2 weeks: ____

THANK-YOU CHECK-IN
"Hi [name], thank you for ordering from us! Was
everything right? Anything we could do better?"

IN MALAYALAM
"ഓർഡർ ചെയ്തതിന് നന്ദി! എല്ലാം ശരിയായിരുന്നോ?
ഞങ്ങൾ എന്തെങ്കിലും മെച്ചപ്പെടുത്തണോ?"

OCCASION REMINDER (ask at delivery first)
"Shall I remind you a week before next year's
[occasion]? Just reply YES. You can say stop any time."

WIN-BACK
"Hi [name], it's been a while! This month we have ____.
Would you like your usual ____ again?"
""", ''),
    ],
    mistakes=[
        ('Chasing only new customers.', 'Your existing customers already trust you. Look after them first.'),
        ('Spamming past customers.', 'One useful message beats five promotions. Respect "stop".'),
        ('Loyalty discounts that kill your margin.', 'Check your unit economics before offering a reward. A free add-on often costs less than a discount.'),
        ('Collecting dates without consent.', 'Ask clearly, explain why, and delete on request.'),
        ('Not asking why people leave.', 'A one-line question to a lost customer can save the next ten.'),
    ],
    quiz=[
        {'q': 'You had 60 customers in 6 months, and 15 bought twice or more. What is the repeat rate?',
         'o': ['15%', '25%', '4%', '75%'],
         'a': 'B', 'why': '15 ÷ 60 = 0.25, which is 25%.'},
        {'q': 'A care plan had 20 clients at the start of the month, and 2 cancelled. What is the monthly churn?',
         'o': ['2%', '10%', '20%', '18%'],
         'a': 'B', 'why': '2 ÷ 20 = 0.10, which is 10%.'},
        {'q': 'Which retention action respects consent?',
         'o': ['Adding all customers to a group without asking', 'Asking at delivery whether they want a reminder next year, and removing anyone who says stop', 'Messaging every customer daily', 'Sharing their numbers with partners'],
         'a': 'B', 'why': 'Clear permission, a clear reason and an easy way out.'},
        {'q': 'A care-plan client cancels because "I don\'t see what I\'m paying for." What is a good fix?',
         'o': ['Cut the price', 'Show the value with a short monthly report', 'Ignore it', 'Add features nobody asked for'],
         'a': 'B', 'why': 'Often the value is real but invisible. Make it visible.'},
    ],
    study='"Startup = Growth", the a16z metrics on churn and OpenStax 10.5 (about 1 hour)',
    action='measure your repeat rate or churn, ask 5 customers for feedback and run two retention actions and a win-back',
)

L2 = lesson(
    12, 2,
    title='KPIs: the few numbers that run your business',
    weeks=(27, 27), hours=3,
    outcome='Choose 5–7 KPIs, build a one-page weekly dashboard in Google Sheets and run a 30-minute weekly review that ends with actions.',
    split='40 minutes study, 2 hours 20 minutes action',
    core="""
A **KPI (key performance indicator)** is one of the few numbers that tell you whether the business is healthy and where to act. Paul Graham's advice to measure what you care about applies here: what gets measured tends to improve.

### Choose 5–7 KPIs

Pick a mix of **leading** indicators, which predict future results (conversations held, quotes sent), and **lagging** ones, which report results (revenue, profit).

| Path | Useful KPIs |
| --- | --- |
| Local business | Orders a week, average order value, contribution margin, repeat rate, new reviews, cash in the bank |
| Freelance → agency | Pipeline value, conversations a week, conversion rate, monthly recurring revenue from care plans, churn, unpaid invoices |
| Digital product | Visitors or views, conversion rate, sales, refunds, channel or list growth, revenue |
| Online service | Leads, close rate, average delivery time, customer satisfaction, revenue, hours per job |

Choose **one main number**, sometimes called a North Star, that best captures the value you deliver: repeat customers a month for Nisha, or monthly recurring revenue for Arun.

### Set targets and colours

For each KPI, write a target and a warning level: **green** (on target), **amber** (watch it), **red** (act now). Colours make a dashboard readable in ten seconds.

### Leave out vanity numbers

Followers, likes and views feel good but rarely guide decisions. Keep them off the main dashboard unless they clearly lead to orders.

### The 30-minute weekly review

Every Sunday evening:

1. **Update the numbers** (10 minutes) from your cash book and Customers tab.
2. **What changed, and why?** (10 minutes) Look at the red and amber KPIs first.
3. **Choose three actions for next week** (5 minutes), each linked to a KPI.
4. **Check last week's actions** (5 minutes): were they done, and what happened?

A dashboard you don't act on is decoration. The actions are the point.
""",
    example="""
Arun's weekly dashboard for ShopAssist's shops in Kuttiady and Vatakara:

| KPI | Target | This week | Status |
| --- | --- | --- | --- |
| Monthly recurring revenue (care plans) | ₹6,000 | ₹5,000 (10 shops) | Amber |
| Sales conversations this week | 6 | 4 | Amber |
| Conversion (conversation → sale) | 30% | 25% | Amber |
| New setups this month | 4 | 3 | Green |
| Invoices unpaid for over 7 days | ₹0 | ₹1,500 | Red |
| Hours worked this week | 6–8 | 9 | Amber |

His three actions for the next week: (1) call the two shops with overdue invoices on Monday; (2) book two more conversations through the printing-shop partner; (3) save an hour by using the report template for every client.
""",
    resources=[
        ('a16z', 'Read the metrics that match your model, such as recurring revenue, churn and CAC', '20 min'),
        ('pg-13', 'Re-read the point about measuring what you care about', '5 min'),
        ('gsheets', 'Optional: a refresher on formulas and sharing', '15 min'),
    ],
    steps=[
        'Choose 5–7 KPIs for your business, including one main number and a mix of leading and lagging indicators.',
        'Set a target and a warning level for each.',
        'Build the dashboard in your KPIs tab from your cash book and Customers tab. Add colours with Format → Conditional formatting (for example, red when a value is below its warning level).',
        'Run your first 30-minute weekly review and write three actions.',
        'Run the review again the next week, and record what happened with last week\'s actions.',
    ],
    proof='A screenshot of your dashboard and your notes from two weekly reviews, each with three actions and their results.',
    templates=[
        ('KPI dashboard and weekly review', """
KPI DASHBOARD (KPIs tab)
Main number (North Star): ____
KPI | Leading or lagging | Target | Warning level | This week | Status
1.
2.
3.
4.
5.
6.
7.

WEEKLY REVIEW (Sunday, 30 minutes)    Date: ____
1. Numbers updated [ ]
2. Red and amber KPIs, and why:
   ____________
3. Three actions for next week, each linked to a KPI:
   a. ____ (KPI: ____)
   b. ____ (KPI: ____)
   c. ____ (KPI: ____)
4. Last week's actions: done? What happened?
   ____________
""", ''),
    ],
    mistakes=[
        ('Too many KPIs.', 'With twenty numbers, none gets attention. Pick 5–7.'),
        ('No targets.', 'A number without a target can\'t be good or bad. Set one, even a rough one.'),
        ('Only lagging numbers.', 'Revenue tells you about last month. Leading numbers, such as conversations, tell you about next month.'),
        ('Reviewing without acting.', 'End every review with three actions, and check them the next week.'),
        ('A dashboard you never update.', 'If it takes an hour to update, simplify it until it takes 10 minutes.'),
    ],
    quiz=[
        {'q': 'Which of these is a leading indicator?',
         'o': ['Last month\'s profit', 'Sales conversations held this week', 'Last year\'s revenue', 'Tax paid'],
         'a': 'B', 'why': 'Conversations this week predict the sales of the coming weeks.'},
        {'q': 'For most small businesses, which is a vanity number?',
         'o': ['Repeat rate', 'Instagram likes', 'Cash in the bank', 'Unpaid invoices'],
         'a': 'B', 'why': 'Likes rarely tell you what to do next.'},
        {'q': 'What should every weekly review end with?',
         'o': ['A new logo', 'Three actions linked to KPIs', 'A party', 'Deleting old data'],
         'a': 'B', 'why': 'Actions turn numbers into progress.'},
        {'q': 'Why use green, amber and red?',
         'o': ['It looks nice', 'So you can see in seconds which numbers need action', 'Google requires it', 'To confuse helpers'],
         'a': 'B', 'why': 'A quick glance shows where to focus.'},
    ],
    study='the a16z metrics for your model and "Startups in 13 Sentences" (about 40 minutes)',
    action='build a 5–7 KPI dashboard with targets and run two weekly reviews with actions',
)

L3 = lesson(
    12, 3,
    title='Hiring, delegating and when to scale',
    weeks=(28, 28), hours=4,
    outcome='Judge whether you are ready to scale using evidence, delegate one task with an SOP, and know how to hire help fairly and legally.',
    split='1 hour 20 minutes study, 2 hours 40 minutes action',
    core="""
### Are you ready to scale?

Scaling means growing sales faster than your costs and your hours. Before you spend on growth, check honestly:

| A sign you are ready | A sign you are not |
| --- | --- |
| Demand has been steady, and more than you can handle, for 2–3 months | Sales come and go, or come only from friends |
| Each sale makes a healthy contribution | Profit exists only because you work for free |
| Your main tasks have SOPs that others can follow | Everything depends on you |
| You have a cash buffer for slow months | One slow month would mean borrowing |
| Customers come back and refer others | You must keep finding new customers just to stand still |
| You know your numbers every week | You don't know your margins |

If you are not ready, fix the weakest row first. Scaling a broken process only makes its problems bigger.

### Ways to scale a micro-business

- **More capacity:** better equipment, a helper, longer hours on peak days.
- **More customers like your best ones:** a nearby town or a related customer group.
- **More from each customer:** add-ons, bundles, a premium package, subscriptions.
- **New channels:** partners, a marketplace, online sales (check GST and other rules first).
- **Productise:** turn a repeated service into a fixed package or a digital product.
- **The agency model,** for freelancers: you win the clients and keep the quality; trained helpers or subcontractors do part of the delivery.

### Delegate step by step

**Do it → document it (SOP) → delegate it → review it.** Start with a small, repeated task that doesn't need your judgement: packing, product photos, catalogue updates, deliveries. Give a clear brief, train once using the SOP, check the first few results closely, then less often.

### Hiring help fairly and legally

- **Options:** freelancers paid per task, part-time helpers (students, Kudumbashree members, relatives who want paid work) or employees.
- **Fair pay, on time:** agree the rate in writing before work starts, pay on the agreed day, and never pay below the legal minimum wage for the work (check current rules for Kerala).
- **Written terms:** the work, hours or tasks, pay and when it is paid, a trial period, confidentiality of customer data and who owns the work.
- **The law:** once you employ people, rules such as the Kerala Shops and Commercial Establishments Act, EPF and ESI may apply, depending on your business and the number of workers (check current rules). Never employ children.
- **Safety and respect:** safe working conditions, clear instructions and respect for helpers' time.

### Your job changes

As you grow, your job moves from doing everything yourself to finding customers, setting standards, training people and watching the numbers. Sam Altman's Startup Playbook has a short part on hiring and managing that is worth reading if you plan to build a team.
""",
    example="""
**Nisha** scored herself on the readiness table: steady demand (yes, in festival months), a healthy contribution (yes), SOPs (yes), a cash buffer (small), repeat customers (yes) and weekly numbers (yes). Her bottleneck was decorating time. For the December weekends she hired her neighbour Shabna as a part-time helper, at a day rate agreed in writing and above the legal minimum she had checked, with a one-week trial. Shabna learned packing and simple decorating from Nisha's SOPs, and Nisha's weekend capacity went from 6 cakes to 10.

**Arun** delegated product photography to Fazil at ₹300 a shop, with a photo SOP: daylight, a plain background, 30 items, file names that include prices. He checked the photos for the first three shops himself, then spot-checked one shop in five. That freed about 1.5 hours per setup, which he now spends on sales conversations: his first step from freelancer towards a small agency.
""",
    resources=[
        ('os12', 'Section 12.2 Building the Entrepreneurial Dream Team', '30 min'),
        ('os10', 'Section 10.5 Growth: Signs, Pains, and Cautions, if you haven\'t read it', '25 min'),
        ('altman', 'Read the "Hiring & Managing" part of Part IV', '15 min'),
        ('epfo', 'Only when you plan to hire: when EPF applies (check current rules)', '5 min'),
        ('kerala-labour', 'Only when you plan to hire: Labour Department notices and registration (check current rules)', '5 min'),
    ],
    steps=[
        'Score yourself on the scale-readiness checklist below, and find your weakest row.',
        'Decide: grow now, hold steady, or fix the weakest row first. Write one paragraph explaining why.',
        'Choose one repeated task to delegate, and write a delegation brief that links to its SOP.',
        'Try it with a helper (a friend, a relative or a freelancer) on a small paid task, with written terms and fair pay.',
        'Review the result with the helper: what went well and what should change. Update the SOP.',
    ],
    proof='Your readiness score and decision paragraph, the delegation brief and written terms, and your notes from the review with the helper.',
    templates=[
        ('scale readiness checklist', """
SCALE READINESS (Y or N for each)
[ ] Demand steady and above my capacity for 2-3 months
[ ] Each sale makes a healthy contribution
[ ] My main tasks have SOPs that others can follow
[ ] I have a cash buffer for slow months
[ ] Customers come back and refer others
[ ] I know my numbers every week
Score: __ / 6
Weakest row: ____   Fix first: ____
Decision: grow now / hold steady / fix first
Why: ____________
""", ''),
        ('delegation brief and helper agreement', """
DELEGATION BRIEF
Task: ____ (link to the SOP)
Done when: ____ (what "good" looks like)
Time it should take: ____
Tools and materials provided: ____
Customer data rules: ____ (for example: don't save
customers' numbers on your own phone)
Checks: the first ____ jobs checked fully, then ____

HELPER AGREEMENT (signed, or confirmed by message)
Name: ____   Work: ____
Pay: ₹____ per ____ (task / day / hour), paid on ____
Trial period: ____
Confidentiality: customer details stay private
Ownership: photos and work made for the business
belong to the business
Either side can stop with ____ days' notice
Signed or confirmed: ____   Date: ____
""", ''),
    ],
    mistakes=[
        ('Hiring before demand is steady.', 'A helper you can\'t keep busy, or pay, is bad for both of you. Wait for 2–3 months of steady demand.'),
        ('Hiring friends without clear roles.', 'Write down the work, the pay and the expectations, even with friends and relatives.'),
        ('Paying late.', 'Late pay destroys trust fast. Pay on the agreed day, every time.'),
        ('No training.', 'Hand over the SOP, train once, then check the first jobs closely.'),
        ('Scaling a broken process.', 'Fix quality and margins first; growth makes every problem bigger.'),
    ],
    quiz=[
        {'q': 'Which of these is a sign you are not ready to scale?',
         'o': ['Steady demand above your capacity for 3 months', 'Profit exists only because you work for free', 'Customers refer others', 'You know your weekly numbers'],
         'a': 'B', 'why': 'Scaling would only multiply unpaid work. Fix the margin first.'},
        {'q': 'What is the right order for delegating?',
         'o': ['Delegate first, then document', 'Do it, document it as an SOP, delegate it, review it', 'Hire first, then decide the task', 'Never delegate'],
         'a': 'B', 'why': 'You can only hand over a task you have done and written down.'},
        {'q': 'Which task is best to delegate first?',
         'o': ['Pricing decisions', 'A small, repeated task with an SOP, like packing or product photos', 'Handling an angry big client', 'Choosing your business structure'],
         'a': 'B', 'why': 'It frees your time with little risk.'},
        {'q': 'What should a helper agreement include?',
         'o': ['Only a name', 'The work, the pay and payment date, a trial period, confidentiality and notice', 'Their family details', 'Nothing; trust is enough'],
         'a': 'B', 'why': 'Clear terms make the arrangement fair and easy to keep.'},
    ],
    study='OpenStax 12.2 and 10.5 and the hiring part of Sam Altman\'s Startup Playbook (about 1 hour 20 minutes)',
    action='score your scale readiness, decide, and delegate one task with an SOP, written terms and fair pay',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    12,
    title='Growth and scaling',
    weeks=(27, 28), hours=12,
    overview="""
Growth isn't only about new customers. For a small business, the cheapest growth comes from the customers you already have: buying again, buying more and bringing their friends. Next come the numbers that show what is working, and the decision every founder faces: when to get help, and when to grow bigger.

This module covers retention and referrals, a simple KPI dashboard with a weekly review, and an honest test of when to hire, delegate and scale, including how to do it fairly and legally.
""",
    outcomes=[
        'Measure repeat rate and churn, and run retention and win-back actions',
        'Choose 5–7 KPIs and run a 30-minute weekly review from a one-page dashboard',
        'Judge whether you are ready to scale, using evidence rather than hope',
        'Delegate a task with an SOP and hire help fairly and legally',
    ],
    lessons=LESSONS,
    project='Growth plan',
    project_steps=[
        'Your retention numbers (repeat rate or churn) and two retention actions with their results (L01).',
        'Your KPI dashboard and notes from two weekly reviews (L02).',
        'Your scale-readiness score and decision (L03).',
        'One delegated task, with its brief, the helper\'s agreement and the result (L03).',
        'A one-page plan for the next 3 months: which customers, which channels, what capacity and which numbers you will watch.',
    ],
    project_proof='Your growth plan and its supporting sheets in Founder Toolkit/12 Growth.',
    rubric=[
        ('Retention', 'Not measured', 'Measured once', 'Measured monthly, with two retention actions and their results'),
        ('KPIs', 'None, or only likes', 'Numbers without targets', '5–7 KPIs with targets and a weekly review with actions'),
        ('Scale decision', '"Grow fast", on hope', 'Some numbers', 'A readiness score from evidence and a clear grow, hold or fix decision'),
        ('Delegation', 'I do everything myself', 'Asked someone informally', 'A task delegated with an SOP, written terms, fair pay and a review'),
    ],
    short=[
        'L01: count your repeat customers and send 5 thank-you and feedback messages.',
        'L02: track 3 KPIs every week.',
        'L03: score your scale readiness and delegate one small task to a relative, with an SOP.',
    ],
    mistakes=[
        ('Chasing new customers and forgetting existing ones.', 'Look after the people who already trust you.'),
        ('Too many KPIs and no actions.', 'Track a few numbers and act on them weekly.'),
        ('Hiring before demand is steady.', 'Wait for 2–3 months of demand above your capacity.'),
    ],
)
