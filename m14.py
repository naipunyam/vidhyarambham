from common import lesson, module

L1 = lesson(
    14, 1,
    title='Plan your launch',
    weeks=(30, 30), hours=5,
    outcome='Write a two-week launch plan with a clear goal, offer, channels, capacity check, a budget within your risk limit and a list of risks, then run a soft launch to fix problems first.',
    split='1 hour 15 minutes study, 3 hours 45 minutes action',
    core="""
A **launch** is a planned push to tell the people who need your offer that it exists, and to make it easy for them to buy. For a micro-business it isn't one big day. It is one or two weeks of focused effort, after a small soft launch that catches problems early.

Y Combinator's talk on launching makes a useful point: you can launch more than once. A new offer, a new season or a new customer group is a reason to launch again.

### The parts of a launch plan

1. **Goal:** one or two numbers, such as "15 paying customers and ₹15,000 of sales in 14 days". Base it on your funnel rates from earlier modules.
2. **Offer:** what you are launching and at what price, with any honest launch offer: a real deadline, a real bonus.
3. **Audience:** your early adopters, and everyone in your pipeline.
4. **Channels:** personal messages, WhatsApp Status and groups (with permission), Instagram, Google profile posts, partners, a stall or an event.
5. **Content:** what you will post each day, prepared in advance.
6. **Outreach list:** the people you will contact personally, with dates.
7. **Partners:** who will tell their customers, and what they get.
8. **Capacity:** how many orders you can deliver well each day, and what you will do if more come in.
9. **Logistics:** stock, packaging, delivery slots, payment links, the order form.
10. **Compliance:** the registrations and labels you need (Module 9) are in place.
11. **Budget:** any spending (printing, samples, a stall fee), within your risk limit.
12. **Risks:** what could go wrong, and your plan for each.
13. **Measurement:** the daily scoreboard you will keep (next lesson).

### Work back from the goal

If your goal is 15 sales and 25% of conversations become sales, you need about 60 conversations. If half the people you contact reply, you need about 120 contacts over 14 days: roughly 9 a day. That is your daily outreach target.

### The soft launch

A few days before the public launch, sell to a small group of 10–20 people from your pipeline and your interviewees. Fix whatever breaks: the order form, the payment link, delivery times, the product itself. Then launch publicly.

### Prepare your story

People share stories, not features. Prepare a short launch message: who you are, the problem you saw in your town, what you built, what early customers said, and the offer. OpenStax's section on sharing your entrepreneurial story has good examples.
""",
    example="""
Arun's two-week plan to launch a "Festival-ready WhatsApp" package before the wedding season:

- **Goal:** 8 new setups and 5 new care-plan shops in 14 days: about ₹14,000 in setups, plus ₹2,500 a month in care plans.
- **Offer:** the Standard package at ₹1,800, with one free month of the care plan for shops that sign up during the launch. The launch really does end on day 14.
- **Audience:** 60 shops in his pipeline, plus introductions from his 15 current clients.
- **Channels:** personal visits and messages, referrals from clients, the printing-shop partner, before-and-after posts on his WhatsApp Status, and a short talk at a local traders' association meeting, with the organisers' permission.
- **Capacity:** at most one setup a day on weekdays and three on Saturday, with Fazil doing the photos. Beyond that, he books slots for the following week.
- **Budget:** ₹600 for printed offer sheets and bus fares, within his risk limit.
- **Risks:** owners too busy in the season (fix: early-morning setups); his PSC exam (fix: the launch ends three weeks before the exam).
- **Soft launch:** three friendly shops first, which showed that his instruction sheet needed Malayalam screenshots.

Working back: 8 sales at a 30% conversion rate need about 27 conversations; at a 50% reply rate, that is about 54 contacts, or 4 a day.
""",
    resources=[
        ('yc-launch', 'Watch the whole talk', 'about 25 min'),
        ('os15', 'Section 15.1 Launching Your Venture', '30 min'),
        ('os7', 'Section 7.2 Sharing Your Entrepreneurial Story', '20 min'),
    ],
    steps=[
        'Write your launch plan with the template below, working back from your goal to a daily outreach target.',
        'Check capacity and logistics: stock, packaging, delivery slots, the order form and the payment link.',
        'Prepare the launch content (at least 7 posts) and your launch story message.',
        'Brief your partners, and ask your current customers for introductions.',
        'Run a soft launch with 10–20 people, fix what breaks, and set the date for the public launch.',
    ],
    proof='Your launch plan, your prepared content and story, and your notes from the soft launch with the fixes you made.',
    templates=[
        ('launch plan', """
LAUNCH PLAN          Dates: ____ to ____
GOAL: ____ customers / ₹____ in ____ days
OFFER: ____ at ₹____; launch bonus ____
(a real deadline: ____)
AUDIENCE: ____
CHANNELS: ____

WORK BACK FROM THE GOAL
Sales needed ____ ÷ conversion ____% = ____ conversations
Conversations ____ ÷ reply rate ____% = ____ contacts
Contacts ____ ÷ days ____ = ____ a day

CONTENT: ____ posts ready (list them)
PARTNERS: ____ (what they get: ____)
CAPACITY: ____ orders a day; if more come in: ____
LOGISTICS: stock [ ] packaging [ ] delivery slots [ ]
order form [ ] payment link [ ]
COMPLIANCE: registrations and labels in place [ ]
BUDGET: ₹____ (my risk limit: ₹____)
RISKS AND FIXES
1. ____ → ____
2. ____ → ____
SOFT LAUNCH: ____ people on ____; fixes made: ____
""", ''),
        ('launch story message', """
LAUNCH STORY (a WhatsApp message under 100 words)
Hi [name]! I'm [your name] from [place].
I noticed that ____ (the problem you saw).
So I started ____ (what you offer).
"____" (an early customer's words, with permission)
From ____ to ____: ____ (the launch offer).
To order: ____
Thank you for supporting a local business!
""", ''),
    ],
    mistakes=[
        ('Launching without the capacity to deliver.', 'If you can\'t deliver what you sell, the launch damages your name. Set a daily limit and keep a waiting list.'),
        ('Fake deadlines and bonuses.', 'If the launch offer ends on Sunday, end it on Sunday. Honest offers build trust.'),
        ('Skipping the soft launch.', 'Problems with forms, payments or delivery are cheap to fix with 10 people and costly with 100.'),
        ('A goal with no daily target.', 'Work back to the number of contacts you need each day.'),
        ('Clashing with your exam.', 'Schedule the launch to end well before an exam, as your exam-mode rule says.'),
    ],
    quiz=[
        {'q': 'Your goal is 12 sales. 30% of conversations become sales, and half of the people you contact reply. About how many people do you need to contact?',
         'o': ['12', '40', '80', '24'],
         'a': 'C', 'why': '12 ÷ 0.3 = 40 conversations, and 40 ÷ 0.5 = 80 contacts.'},
        {'q': 'Why do a soft launch?',
         'o': ['To delay the launch', 'To find and fix problems with a small group before the public launch', 'To avoid customers', 'Because it is required'],
         'a': 'B', 'why': 'Small groups reveal problems while they are still cheap to fix.'},
        {'q': 'Which launch offer is honest?',
         'o': ['"Only 2 left!" when you have plenty', '"A free month of care for shops that join by 30 November", and it really ends on 30 November', '"The price doubles tomorrow", when it doesn\'t', 'A fake countdown timer'],
         'a': 'B', 'why': 'Real deadlines are persuasive and honest; fake ones are misleading.'},
        {'q': 'What should your capacity plan say?',
         'o': ['Nothing', 'How many orders you can deliver well each day, and what happens when demand is higher', 'Your logo colours', 'Your competitors\' prices'],
         'a': 'B', 'why': 'It protects quality when the launch works.'},
    ],
    study='the YC launch talk and OpenStax 15.1 and 7.2 (about 1 hour 15 minutes)',
    action='write a two-week launch plan worked back from your goal, prepare content and run a soft launch',
)

L2 = lesson(
    14, 2,
    title='Launch and win your first paying customers',
    weeks=(31, 31), hours=6,
    outcome='Run your launch for 7–14 days with a daily routine and scoreboard, adjust when sales are slow, and earn revenue from customers who are not friends or family.',
    split='about 15 minutes of optional study, 5 hours 45 minutes action',
    core="""
Launch week is steady daily work, not one big announcement. Keep your plan in front of you and your scoreboard up to date.

### A daily launch routine (part-time)

- **Morning (15 minutes):** post the day's content and reply to overnight messages.
- **Evening (45 minutes, after PSC study):** personal outreach to the day's contacts, follow-ups, and the scoreboard.
- **Weekend (2–3 hours):** visits, deliveries, a stall or an event, and the mid-launch review.

Full-time: the same blocks, with three or four times the outreach and more visits.

### The daily scoreboard

Track the same funnel every day: contacts, replies, conversations, offers, sales, revenue, deliveries, reviews and referrals. The numbers keep you steady when your mood swings.

### When sales are slow, diagnose before you discount

Work down the funnel and fix the first broken step:

| Symptom | Likely problem | Try |
| --- | --- | --- |
| Few people see it | Reach | More personal messages, partners, a stall; ask customers to share |
| They see it but don't reply | The message | A clearer hook, stronger proof, a simpler call to action |
| They reply but don't buy | The offer, trust or price | A smaller first package, a guarantee, a trial, a testimonial |
| They buy once and vanish | Delivery or follow-up | Check quality, follow up, ask for feedback |

Change one thing at a time, so you know what worked. Don't discount in a panic; it teaches customers to wait for the next discount.

### Handling a rush

If orders come in faster than you can deliver: stop taking orders for a slot, start a waiting list, tell customers honestly when they will get their order, and ask a helper or your family to do simple tasks. Never let quality drop to squeeze in more orders.

### Turn customers into proof

After each delivery, ask for an honest review (on Google, or a WhatsApp message you may share), ask for a referral at the happy moment, and with permission share a photo or a quote. Share only real, permitted testimonials.

### The mid-launch review

Halfway through, compare the scoreboard with your plan. Which channel brought the most conversations and sales for the time it took? Do more of that in the second half.

### Mark the milestone

Your first sale to someone who didn't know you before is the moment the business becomes real. Write down who it was, how they found you and what they said.
""",
    example="""
Arun's scoreboard for the first seven days:

| Day | Contacts | Replies | Conversations | Offers | Sales | Revenue (₹) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 3 | 1 | 1 | 0 | 0 |
| 2 | 5 | 2 | 2 | 1 | 1 | 1,800 |
| 3 | 4 | 3 | 1 | 1 | 0 | 0 |
| 4 | 5 | 2 | 1 | 0 | 0 | 0 |
| 5 | 6 | 4 | 3 | 2 | 1 | 1,800 |
| 6 (Saturday) | 10 | 7 | 5 | 4 | 2 | 3,600 |
| 7 (Sunday, day off) | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **36** | **21** | **13** | **9** | **4** | **7,200** |

The mid-launch review showed that Saturday visits in Kuttiady and Vatakara converted best and that two sales came through the printing-shop partner. Weekday WhatsApp messages got replies but few meetings. So in week two he put more effort into Saturday visits and asked every client for one introduction. By day 14 he had 9 setups (goal: 8) and 6 new care-plan shops (goal: 5). Five of the nine new shops belonged to owners he had never met before the launch.
""",
    resources=[
        ('yc-first', 'Optional refresher: the parts on reaching early customers', 'about 23 min'),
        ('pg-ds', 'Optional: re-read the part on delighting early customers', '10 min'),
    ],
    steps=[
        'Run your public launch for 7–14 days, following your daily routine.',
        'Update the scoreboard every day.',
        'At the halfway point, review the scoreboard, find the weakest step and change one thing.',
        'After every delivery, ask for an honest review and a referral. Collect at least 5 reviews or testimonials, with permission.',
        'At the end, add up your revenue and contribution, and count how many customers were not friends or family.',
    ],
    proof='Your daily scoreboard, notes from the mid-launch review, at least 5 real reviews or testimonials, and your totals: revenue, contribution and customers who weren\'t friends or family.',
    templates=[
        ('daily scoreboard (paste into Google Sheets)', """
Day,Date,Contacts,Replies,Conversations,Offers,Sales,Revenue (Rs),Deliveries,Reviews,Referrals,Notes
1,,,,,,,,,,,
""", 'csv'),
        ('mid-launch review, testimonial request and totals', """
MID-LAUNCH REVIEW (day __)
Goal so far: ____   Actual: ____
Best channel (sales for the time spent): ____
Weakest step in the funnel: ____
One change for the second half: ____

TESTIMONIAL REQUEST
"Thank you! Could I share a line of what you thought,
with your first name (or no name, if you prefer)? Only
if you're comfortable with it."

END-OF-LAUNCH TOTALS
Revenue ₹____   Contribution ₹____
Customers ____ (not friends or family: ____)
Reviews ____   Referrals ____
First customer who didn't know me before: ____
How they found us: ____
""", ''),
    ],
    mistakes=[
        ('Stopping after the first post.', 'Launches are won by daily outreach and follow-ups. Keep going for the full 7–14 days.'),
        ('Panic discounting.', 'Diagnose the funnel first. Fix reach, message or trust before you cut the price.'),
        ('Letting quality slip in a rush.', 'Use a waiting list instead. One bad delivery can undo ten good posts.'),
        ('Not logging numbers.', 'Without a daily scoreboard, you can\'t tell what worked.'),
        ('Fake or unpermitted testimonials.', 'Share only real words, with permission.'),
    ],
    quiz=[
        {'q': 'People reply to your messages but don\'t buy. What is the likely problem?',
         'o': ['Reach', 'The offer, trust or price', 'Your logo', 'Too many customers'],
         'a': 'B', 'why': 'They are interested, so something about the offer, the proof or the price is holding them back.'},
        {'q': 'Halfway through the launch, Saturday visits have sold best. What should you do?',
         'o': ['Stop the visits', 'Put more effort into Saturday visits in the second half', 'Change everything at once', 'Give up'],
         'a': 'B', 'why': 'Double down on what works, and change one thing at a time.'},
        {'q': 'Orders arrive faster than you can deliver well. What should you do?',
         'o': ['Rush, even if quality drops', 'Start a waiting list and tell customers honestly when they will get their order', 'Cancel all the orders', 'Raise prices without telling anyone'],
         'a': 'B', 'why': 'Honest waiting lists keep trust; poor deliveries destroy it.'},
        {'q': 'Why count the customers who are not friends or family?',
         'o': ['For fun', 'They show the business works on its own merits', 'For tax', 'It is required'],
         'a': 'B', 'why': 'Strangers pay only because the offer is worth it.'},
    ],
    study='optional refreshers only: the YC first-customers talk and "Do Things That Don\'t Scale"',
    action='run a 7–14 day launch with a daily scoreboard and a mid-launch change, and collect 5 real reviews',
)

L3 = lesson(
    14, 3,
    title='Review, one-page business plan and pitch',
    weeks=(32, 32), hours=4,
    outcome='Review your launch with real numbers, write a one-page business plan, give a 2-minute pitch to a real person and set your 90-day goals.',
    split='55 minutes study, 3 hours 5 minutes action',
    core="""
### Review the launch

Compare the results with the plan: the goal against the actual numbers, the funnel rates, the best and worst channels, your unit economics in practice (did deliveries cost what you expected?), customer feedback, and the problems and their fixes. Write it down while it is fresh. This is your launch report.

### The one-page business plan

Long business plans are rarely read. A one-page plan built on evidence is useful to you and to a bank manager, a partner or a mentor. OpenStax's section on the business plan explains the full version; this is the short one:

1. **Problem:** who has it and what it costs them, with evidence
2. **Customer:** your beachhead and early adopters
3. **Offer:** what you sell, with packages and prices
4. **Evidence:** interviews, pre-sales, launch results, repeat rate, reviews
5. **Business model:** how you earn, unit economics, recurring revenue
6. **Marketing and sales:** your best channels and conversion rates
7. **Operations:** how you deliver, capacity, SOPs, helpers
8. **Team:** you, helpers, partners, mentors
9. **Finances:** monthly revenue, contribution, fixed costs, break-even, cash
10. **Compliance:** your structure and the registrations in place
11. **Risks:** the top three, and how you manage them
12. **Next 90 days:** goals with numbers and dates
13. **Ask:** what you need, if anything: a loan, a partner, advice, introductions

### The 2-minute pitch

A pitch is a short spoken version of your plan that ends with a clear ask:

1. **Hook (10 seconds):** a striking fact from your evidence. "Eight of the eleven textile shops I interviewed lose customers every evening on WhatsApp."
2. **Problem (20 seconds):** who suffers, and what it costs them.
3. **Solution (20 seconds):** what you do, in plain words.
4. **Proof (30 seconds):** customers, sales, reviews, repeat rate, numbers.
5. **Business model (20 seconds):** how you earn, and why it works.
6. **Ask (20 seconds):** exactly what you want from this person.

Tailor it to the listener. A **bank manager** cares about steady cash flow and how you will repay. A **partner** cares about what is in it for them and their customers. A **mentor** wants to hear your biggest question. A **grant panel or KSUM** looks for innovation and the potential to grow. OpenStax's section on pitches for different audiences covers this.

### Your 90-day plan

Set three goals at most, each with a number and a date and linked to your KPIs, plus the weekly actions that get you there. Then put your next Sunday review in the calendar.
""",
    example="""
Arun's one-page plan after his launch:

| Section | ShopAssist |
| --- | --- |
| Problem | Small textile and mobile shops lose WhatsApp customers in the evening rush (8 of 11 owners interviewed) |
| Customer | Textile and mobile shops in Kuttiady, Thottilpalam, Nadapuram and Vatakara with 20 or more enquiries a day |
| Offer | Setup: Basic ₹999, Standard ₹1,800, Premium ₹2,900; care plan ₹500 a month |
| Evidence | 24 paying shops, 16 on the care plan; 14 Google reviews averaging 4.8; 1 of 16 care plans cancelled last month |
| Model | About ₹1,350 contribution per Standard setup after paying Fazil for photos; the care plan earns about ₹330 an hour |
| Sales | Best channels: Saturday visits (about 40% of conversations become sales) and partner referrals |
| Operations | An 18-step setup SOP, a photo SOP with Fazil, a monthly report template |
| Finances | Launch month: ₹21,200 revenue (9 setups and 10 care plans), about ₹17,000 contribution, ₹800 fixed costs; break-even reached in month 2 |
| Compliance | Sole proprietorship, Udyam-registered; turnover well below the ₹20 lakh GST threshold, reviewed every quarter |
| Risks | WhatsApp policy changes; competition from bigger agencies; limited time in exam season |
| Next 90 days | 30 care-plan shops; one new town (Perambra); an AI-assisted FAQ add-on at ₹700 |
| Ask | Introductions to traders' associations in Perambra |

He gave his two-minute pitch to an MSME Clinic expert at the District Industries Centre and to the president of a local traders' association. The association invited him to present at its next monthly meeting.
""",
    resources=[
        ('os11', 'Section 11.4 The Business Plan', '30 min'),
        ('os7', 'Section 7.3 Developing Pitches for Various Audiences and Goals', '25 min'),
        ('mit-s21', 'Optional: choose one lecture video on business plans (lengths not listed)', 'budget 30 min'),
        ('yc-seed', 'Only if you plan to raise investment', 'optional'),
    ],
    steps=[
        'Write your launch report: goal against actual, the funnel, your best channels, unit economics in practice, feedback, and problems with their fixes.',
        'Write your one-page business plan from your real numbers.',
        'Write and rehearse your 2-minute pitch. Record it on your phone and watch it once.',
        'Pitch to one real person who can help: your bank\'s MSME desk, an MSME Clinic expert at the DIC, a potential partner, a traders\' association, KSUM (if you are building a tech startup) or a mentor. Record their feedback.',
        'Set your 90-day goals and put your next weekly review in the calendar.',
    ],
    proof='Your launch report, your one-page business plan, your pitch video, the listener\'s feedback and your 90-day goals.',
    templates=[
        ('one-page business plan', """
ONE-PAGE BUSINESS PLAN    [business name]   Date: ____
1. Problem (with evidence): ____
2. Customer and early adopters: ____
3. Offer, packages and prices: ____
4. Evidence: interviews ____ / pre-sales ____ /
   launch sales ____ / repeat rate ____ / reviews ____
5. Business model and unit economics: ____
6. Best channels and conversion rates: ____
7. Operations, capacity, SOPs, helpers: ____
8. Team, partners and mentors: ____
9. Finances: revenue ₹____ / contribution ₹____ /
   fixed costs ₹____ / break-even ____ / cash ₹____
10. Structure and registrations: ____
11. Top 3 risks, and how I manage them: ____
12. Next 90 days (3 goals with numbers and dates): ____
13. My ask: ____
""", ''),
        ('2-minute pitch and 90-day goals', """
2-MINUTE PITCH
Hook (10 s): ____
Problem (20 s): ____
Solution (20 s): ____
Proof (30 s): ____
Business model (20 s): ____
Ask (20 s): "Would you ____?"
Listener: ____   Their feedback: ____

90-DAY GOALS
1. ____ by ____ (KPI: ____)
2. ____ by ____ (KPI: ____)
3. ____ by ____ (KPI: ____)
Weekly actions: ____
Next Sunday review: ____ (in the calendar [ ])
""", ''),
    ],
    mistakes=[
        ('A plan full of hopes.', 'Use your real numbers. Evidence persuades bank managers and partners; hopes don\'t.'),
        ('Pitching features.', 'Lead with the problem and the proof, not with how clever the solution is.'),
        ('No ask.', 'End every pitch with a clear, specific request.'),
        ('The same pitch for everyone.', 'A banker, a partner and a grant panel care about different things. Adjust the proof and the ask.'),
        ('No next goals.', 'Without 90-day goals, momentum fades after the launch. Set three, with numbers and dates.'),
    ],
    quiz=[
        {'q': 'What should a pitch end with?',
         'o': ['A joke', 'A clear, specific ask', 'Your life story', 'A long list of features'],
         'a': 'B', 'why': 'Without an ask, even a good pitch leads nowhere.'},
        {'q': 'What does a bank manager care about most?',
         'o': ['Your logo', 'Steady cash flow and your ability to repay', 'Your follower count', 'Your competitors\' names'],
         'a': 'B', 'why': 'A loan is repaid from cash flow, so that is what they check.'},
        {'q': 'Which belongs in the "Evidence" part of a one-page plan?',
         'o': ['"Everyone will love it"', 'Interviews done, pre-sales, launch sales, repeat rate and reviews', 'A famous quote', 'Your favourite colour'],
         'a': 'B', 'why': 'Evidence is what you have actually observed and sold.'},
        {'q': 'How many 90-day goals should you set?',
         'o': ['20', 'Three at most, each with a number and a date', 'None', 'One every day'],
         'a': 'B', 'why': 'A few clear goals keep your limited hours focused.'},
    ],
    study='OpenStax 11.4 and 7.3, plus an MIT 15.S21 lecture if you have time (about 55 minutes)',
    action='write a launch report and a one-page plan, pitch to a real person and set your 90-day goals',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    14,
    title='The capstone launch',
    weeks=(30, 32), hours=16,
    overview="""
This is where everything comes together. You plan a launch, run it for one to two weeks, win paying customers, and then step back to review the numbers, write a one-page business plan and pitch it to a real person.

The capstone has been running since week 1 as a set of milestones. By now you have a tested offer, a price, a brand, scripts, books and the registrations you need. The launch turns all of that into a business that people know about and pay for.
""",
    outcomes=[
        'Write a two-week launch plan with a goal, an offer, channels, a capacity check and a list of risks',
        'Run the launch with a daily routine and scoreboard, and adjust when sales are slow',
        'Earn revenue from customers who are not friends or family, with real reviews and referrals',
        'Write a launch report and a one-page business plan, pitch them to a real person and set 90-day goals',
    ],
    lessons=LESSONS,
    project='Capstone review with a mentor',
    project_steps=[
        'Gather your launch plan (L01), your daily scoreboard and results (L02), and your launch report, one-page plan and pitch video (L03).',
        'Present all three to one mentor or banker, and to your accountability buddy.',
        'Ask each of them: "What is the biggest risk you see, and what would you do next?"',
        'Update your one-page plan and 90-day goals with their feedback.',
        'Tick the final checklist and celebrate: you have built a real business.',
    ],
    project_proof='Your capstone folder (Founder Toolkit/14 Launch) with the plan, scoreboard, report, one-page plan, pitch video and the two people\'s feedback.',
    rubric=[
        ('Launch plan', 'No plan', 'A date and a post', 'Goal, offer, channels, capacity, budget and risks, worked back to a daily target'),
        ('Execution', 'One post, then silence', 'Some outreach', 'A daily routine and scoreboard for 7–14 days, adjusted halfway'),
        ('Revenue', 'None', 'From friends and family only', 'From customers who aren\'t friends or family, with real reviews'),
        ('Review and plan', 'None', 'Some notes', 'A launch report with numbers, a one-page plan and 90-day goals'),
        ('Pitch', 'None', 'Written only', 'A 2-minute pitch given to a real person, with feedback recorded'),
    ],
    short=[
        'L01: a one-page launch plan with a goal, an offer and two channels.',
        'L02: a 7-day launch with 3 contacts a day.',
        'L03: a one-page plan and a 2-minute pitch to your accountability buddy.',
    ],
    mistakes=[
        ('Launching without the capacity to deliver.', 'Check that you can deliver everything you sell.'),
        ('One big post, then silence.', 'A launch is daily work for one to two weeks.'),
        ('A plan full of hopes.', 'Build it from your real numbers.'),
    ],
)
