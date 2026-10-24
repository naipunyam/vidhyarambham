from common import lesson, module

L1 = lesson(
    10, 1,
    title='SOPs: write down how the work gets done',
    weeks=(24, 24), hours=3,
    outcome='Map your process from order to delivery, write SOPs for your three most repeated jobs, and test one with another person.',
    split='1 hour 10 minutes study, 1 hour 50 minutes action',
    core="""
An **SOP (standard operating procedure)** is a written checklist for doing a task the same way every time. It sounds like big-company paperwork, but in a small business it is the difference between "only I can do this" and "anyone I train can do this well".

### Why bother

- **Consistent quality:** every cake has the same taste and finish; every shop setup includes the same things.
- **Fewer mistakes:** a checklist catches the step you forget when you are tired.
- **Delegation:** you can't hand over a task that lives only in your head.
- **Improvement:** you can only improve a process that is written down.

### Start with a process map

Write the steps from the moment a customer contacts you to the moment they are happy, as a simple chain:

**Enquiry → quote → order confirmed → advance paid → prepare → make or deliver → quality check → handover → balance paid → follow-up → review request**

Mark where things go wrong or wait (bottlenecks), and where a mistake would hurt most.

### Write an SOP that people actually use

- **Title, purpose, owner and time needed**
- **What you need:** tools, ingredients, logins, materials
- **Numbered steps,** one action each, starting with a verb: "Check…", "Photograph…", "Send…"
- **Quality checks:** what "good" looks like, with a photo if possible
- **Common problems and their fixes**
- **A version number and date,** so everyone knows which copy is current

Keep it to one page. Use photos and voice notes where words are hard; a one-minute video of how you pipe a border is a perfectly good SOP step.

### Write it, then test it

The real test of an SOP is someone else following it without your help. Watch where they get stuck, and fix those steps. Review your SOPs every few months.

### Hygiene and safety belong in the SOP

For food, hygiene isn't optional: clean surfaces, handwashing, covered hair, raw and cooked items kept apart, safe storage and labelled dates. Food businesses registered with FSSAI are expected to follow its hygiene and safety requirements, so write them into the steps where they will happen every time, even on busy days.
""",
    example="""
Nisha's SOP for a custom birthday cake:

| Step | Action |
| --- | --- |
| 1 | Confirm the order on WhatsApp with the confirmation template: size, flavour, message, date, time, address |
| 2 | Take the 50% advance by UPI and record it in the cash book |
| 3 | The day before: check stock against the recipe card, and buy anything missing by 11 am |
| 4 | Clean the counter, wash hands, tie hair back, set out labelled bowls |
| 5 | Bake from the recipe card with a timer; cool for at least 2 hours |
| 6 | Decorate, write the message, and photograph the finished cake in daylight |
| 7 | Quality check: weight within 50 g of the order, message spelled right, no cracks, clean box |
| 8 | Box it with a board, a sticker, a referral card and a "best before" note |
| 9 | Deliver on time, collect the balance by UPI and record it |
| 10 | Next day: send a thank-you message and the review link |

Her sister followed it alone one Sunday and got stuck at step 6, on how much cream to use per layer. Nisha added a photo and "about 3 tablespoons per layer", and the next cake was right first time.

Arun's "Shop setup" SOP has 18 steps, from "Ask the owner for 30 product photos, or book a photo session" to "Send the instruction sheet and book the 30-minute training". It now takes him 4 hours instead of 5, and Fazil can do the catalogue part on his own.
""",
    resources=[
        ('os12', 'Section 12.3 Designing a Startup Operational Plan', '40 min'),
        ('os14', 'Section 14.1 Types of Resources', '30 min'),
    ],
    steps=[
        'Draw your process map from enquiry to review request, on paper or in a Doc, and mark the bottlenecks.',
        'List the tasks you repeat most often and pick the top 3.',
        'Write an SOP for each one with the template below.',
        'Ask a family member, friend or helper to follow one SOP without your help. Note where they get stuck.',
        'Fix the confusing steps and save version 2, with the date.',
    ],
    proof='Your process map, three SOPs (one marked version 2 after testing) and your notes from the test.',
    templates=[
        ('SOP', """
SOP: [task name]           Version __   Date ____
Purpose: ____________ (why this matters)
Owner: ____   Time needed: ____
You need: ____________ (tools, materials, logins)

STEPS
1. ____ (start with a verb)
2. ____
3. ____

QUALITY CHECK
Good looks like: ____ (add a photo link)
Never: ____

COMMON PROBLEMS
Problem: ____  Fix: ____

Tested by: ____ on ____   Changes made: ____
""", ''),
        ('process map', """
PROCESS MAP: from enquiry to a happy customer
Enquiry → ____ → ____ → ____ → ____ → ____ → review
Where do customers wait? ____
Where do mistakes happen? ____
Which step takes longest? ____
""", ''),
    ],
    mistakes=[
        ('Keeping everything in your head.', 'If you fall ill during the festival rush, the business stops. Write it down once.'),
        ('Writing a novel.', 'Long SOPs don\'t get read. One page, numbered steps, photos.'),
        ('Writing SOPs for things you haven\'t done yet.', 'Do the task a few times first, then write down what actually works.'),
        ('Never updating them.', 'Put a version and a date on each SOP and review it every few months.'),
        ('Leaving out hygiene and safety.', 'Write them into the steps so they happen even on busy days.'),
    ],
    quiz=[
        {'q': 'What is an SOP?',
         'o': ['A tax form', 'A written checklist for doing a task the same way every time', 'A loan scheme', 'A marketing post'],
         'a': 'B', 'why': 'Standard operating procedures make quality consistent and make delegation possible.'},
        {'q': 'What is the best way to test an SOP?',
         'o': ['Read it again yourself', 'Have someone else follow it without your help and see where they get stuck', 'Print it out', 'Show it to a customer'],
         'a': 'B', 'why': 'You know the gaps too well to notice them yourself.'},
        {'q': 'Which SOP step is written well?',
         'o': ['"Cake stuff"', '"Check stock against the recipe card the day before"', '"Be careful"', '"Do it nicely"'],
         'a': 'B', 'why': 'It starts with a verb and says exactly what to do and when.'},
        {'q': 'Why put a version number and date on an SOP?',
         'o': ['The law requires it', 'So everyone uses the current version and you can see when it was last improved', 'To make it longer', 'For tax purposes'],
         'a': 'B', 'why': 'Old copies cause the very mistakes the SOP was meant to stop.'},
    ],
    study='OpenStax 12.3 and 14.1 (about 1 hour 10 minutes)',
    action='map your process, write SOPs for your top 3 jobs and test one with another person',
)

L2 = lesson(
    10, 2,
    title='Inventory, delivery and customer service',
    weeks=(24, 24), hours=3,
    outcome='Track stock with reorder points, know your delivery cost per order, and handle questions and complaints in a way that builds trust.',
    split='55 minutes study, 2 hours 5 minutes action',
    core="""
### Stock: enough, but not too much

Running out loses orders. Buying too much ties up cash and, for food, ends up in the bin.

- Keep a **stock sheet** for your main items: the item, unit, quantity in stock, weekly use, supplier and lead time (how long the supplier takes).
- **Reorder point = daily use × lead time in days + safety stock.** When stock falls to this level, reorder.
- **First in, first out (FIFO):** use older stock first. Label containers with the date you bought or opened them.
- For food, track **expiry dates** and storage temperatures.
- Keep **two suppliers** for important items, and compare price, quality and reliability every few months. Once you know your usage, ask for a bulk rate.

Service and digital businesses have "stock" too: templates, tool subscriptions, photo props, printed cards and your available hours.

### Delivery: know what it costs

- **Cost per delivery** = fuel or fare + packaging + your time. Set a **free delivery radius** and charge beyond it, for example free within 5 km and ₹40 for 5–10 km.
- Set **order cut-off times** ("orders by 6 pm for next-day delivery") and delivery slots.
- For parcels to other places, compare a courier with **India Post's Speed Post**, which can be tracked. Pack well and photograph the parcel before sending it.
- For digital products, deliver through a link only buyers receive (a WhatsApp message, an email or a private channel), and put the buyer's name in each PDF to discourage sharing.

### Customer service standards

Write down your promises, then keep them:

- **Response time:** for example, "We reply within 2 hours, 9 am to 9 pm," with a WhatsApp Business away message outside those hours.
- **Quick replies** for common questions: prices, delivery areas, how to order, payment, timings.
- **Labels** in WhatsApp Business to track each chat: new enquiry, quoted, ordered, paid, delivered.
- **One place for every order** (your Customers tab), so nothing gets lost in chats.

### Handling complaints: HEARD

1. **Hear:** let them finish. Don't interrupt or defend yourself.
2. **Empathise:** "I'm sorry this happened. I understand why you're upset."
3. **Apologise** for the experience, even before you know whose fault it was.
4. **Resolve:** offer a fair fix quickly: a replacement, a redo, a refund or a discount next time.
5. **Diagnose:** later, find the cause and change your SOP so it doesn't happen again.

Log every complaint: the date, the customer, the problem, the fix, its cost, the cause and the change you made. A complaint handled well often creates a more loyal customer than no problem at all.
""",
    example="""
Nisha's stock sheet for her key items:

| Item | Use per week | Supplier lead time | Safety stock | Reorder point |
| --- | --- | --- | --- | --- |
| Flour (kg) | 6 | 2 days | 2 kg | 6 ÷ 7 × 2 + 2 ≈ 4 kg |
| Butter (500 g packs) | 8 | 1 day | 2 packs | 8 ÷ 7 × 1 + 2 ≈ 3 packs |
| Fresh cream (litres) | 3 | 1 day | 1 litre | 3 ÷ 7 × 1 + 1 ≈ 1.5 litres |
| Cocoa (kg) | 0.5 | 7 days (ordered online) | 0.25 kg | 0.5 ÷ 7 × 7 + 0.25 = 0.75 kg |
| Cake boxes | 8 | 3 days | 5 | 8 ÷ 7 × 3 + 5 ≈ 9 boxes |

Her delivery rule: free within 5 km (about ₹30 of petrol and 20 minutes), ₹40 for 5–10 km, and nothing beyond 10 km. Her service promise: replies within 2 hours between 9 am and 9 pm, with an away message at night.

**A complaint:** a customer said the writing on her cake was smudged. Nisha listened, apologised, sent ₹150 back by UPI within the hour and asked for a photo. The cause: the box lid had touched the top of the cake. The fix: a taller box for cakes with writing, now part of her SOP. The same customer ordered again the next month.
""",
    resources=[
        ('os8', 'Section 8.6 Sales and Customer Service, the part on customer service', '20 min'),
        ('os14', 'Section 14.3 Managing Resources over the Venture Life Cycle', '25 min'),
        ('wa-business', 'Read the features: quick replies, labels and away messages', '5 min'),
        ('indiapost', 'Only if you send parcels: Speed Post and tracking', '5 min'),
    ],
    steps=[
        'Make a stock sheet for your 5–10 key items with the template below. In H2 type =D2/7*F2+G2, and in I2 type =C2<=H2, which shows TRUE when it is time to reorder.',
        'Work out your delivery cost per order and set your delivery rules: radius, charges and cut-off times.',
        'Write your customer service standards, and set up 6 quick replies, labels and an away message in WhatsApp Business.',
        'Start a complaint log, and handle every complaint this week with HEARD.',
        'Ask one supplier for a better rate or better terms based on your regular usage, and record the answer.',
    ],
    proof='Your stock sheet with reorder points, your delivery rules and costs, screenshots of your quick replies and labels, your complaint log and the supplier\'s answer.',
    templates=[
        ('stock sheet (paste into Google Sheets)', """
Item,Unit,In stock,Use per week,Supplier,Lead time (days),Safety stock,Reorder point,Reorder now?
""", 'csv'),
        ('service standards and quick replies', """
CUSTOMER SERVICE STANDARDS
We reply within ____ hours, between ____ and ____.
Orders by ____ for delivery on ____.
Delivery: free within ____ km; ₹____ for ____ km.
Refunds or replacements: ____________

QUICK REPLIES (in WhatsApp Business, under Business tools)
/price   Our prices: ____ (catalogue link)
/order   To order, send: item, size, date, time, address.
/pay     Pay by UPI to ____ and send a screenshot, please.
/area    We deliver to ____. Outside that: ____.
/time    We're open ____ and reply within ____ hours.
/thanks  Thank you for your order! If you liked it, a
         Google review would help us a lot: [link]
""", ''),
        ('complaint log (paste into Google Sheets)', """
Date,Customer code,Problem,What I did (the fix),Cost (Rs),Cause,Change to the SOP,Customer happy afterwards? (Y/N)
""", 'csv'),
    ],
    mistakes=[
        ('Running out of key stock.', 'Set reorder points for the few items that would stop your business, and check them weekly.'),
        ('Free delivery everywhere.', 'A ₹40 delivery takes a big bite out of a ₹354 contribution. Set a radius and charge beyond it.'),
        ('Slow replies, or none.', 'To a customer, silence feels like a no. Promise a response time and use an away message.'),
        ('Arguing with an upset customer.', 'Listen, apologise and fix it first; find the cause later.'),
        ('Not logging complaints.', 'The same problem will come back unless you find its cause and change the SOP.'),
    ],
    quiz=[
        {'q': 'Daily use is 2 kg, the lead time is 3 days and safety stock is 2 kg. What is the reorder point?',
         'o': ['5 kg', '6 kg', '8 kg', '7 kg'],
         'a': 'C', 'why': '2 kg × 3 days + 2 kg = 8 kg.'},
        {'q': 'What does FIFO mean?',
         'o': ['Free in, free out', 'First in, first out: use older stock first', 'Fast in, fast out', 'Fill in forms online'],
         'a': 'B', 'why': 'Using older stock first reduces waste and expired food.'},
        {'q': 'What is the first step in handling a complaint with HEARD?',
         'o': ['Refund at once', 'Hear the customer out without interrupting', 'Explain why it wasn\'t your fault', 'Block them'],
         'a': 'B', 'why': 'People calm down once they feel heard; then you can fix the problem.'},
        {'q': 'Why set an order cut-off time?',
         'o': ['To annoy customers', 'So you can plan production and delivery reliably', 'The law requires it', 'To raise prices'],
         'a': 'B', 'why': 'Cut-offs turn last-minute chaos into a plan you can keep.'},
    ],
    study='OpenStax 8.6 (customer service) and 14.3, plus the WhatsApp Business features (about 55 minutes)',
    action='set reorder points, cost your delivery, set service standards with quick replies, and log and fix complaints',
)

L3 = lesson(
    10, 3,
    title='Automate with free and AI tools',
    weeks=(25, 25), hours=4,
    outcome='Automate 2–3 repetitive tasks (order intake, reminders, records or replies) with free tools after doing them by hand, and measure the time saved.',
    split='50 minutes study, 3 hours 10 minutes action',
    core="""
Automation means letting tools do the repetitive parts of your work, so you can spend your time on customers and quality. The rule: **automate only what you have already done by hand many times**, so you know exactly what the steps are.

### The automation ladder

Climb one step at a time, and stop as soon as the problem is solved:

1. **Templates:** saved messages, invoice and quote templates, Canva designs you reuse.
2. **Checklists and SOPs:** fewer mistakes and less thinking (last lesson).
3. **Forms:** a Google Form for orders, enquiries or bookings, so details arrive complete and land in a sheet.
4. **Spreadsheet formulas and formatting:** totals, due dates and overdue payments that highlight themselves.
5. **Reminders:** Google Calendar reminders for follow-ups, renewals and reorders.
6. **Simple scripts:** Google Apps Script can, for example, send an email when a form is filled in, or build a monthly summary. It is worth learning on the laptop once the basics work.
7. **AI assistants:** drafting replies, summaries and content for you to check and send (Module 11).

### Good first automations

| Task | Free tool | What it saves |
| --- | --- | --- |
| Taking orders | A Google Form feeding a responses sheet | Missing details and back-and-forth messages |
| Answering common questions | WhatsApp Business quick replies, greeting and away messages | Typing the same thing 20 times a day |
| Tracking payments | Sheets formulas, with overdue rows turning red | Forgetting who owes what |
| Follow-ups | Calendar reminders, or a "next date" column sorted daily | Lost leads |
| A monthly report for a client | A Sheets template you copy each month | An hour per client |
| Reorder alerts | The "reorder now?" column in your stock sheet | Running out |

### Rules for safe automation

- **Test it** with yourself as the customer before using it for real.
- **Keep the human touch** where it matters: complaints, big orders and anything involving money or health.
- **Protect data:** keep forms and sheets in your own Google account with two-factor login, share them "view only" unless someone must edit, and don't collect more personal data than you need.
- **Avoid unofficial "WhatsApp automation" apps** that send bulk messages or scrape contacts. They can break WhatsApp's terms and get your number banned. The free WhatsApp Business app's own tools are enough for a micro-business.
- **Use free tools first.** Pay for a tool only when a free one clearly can't do the job and the time saved is worth more than the fee.

### Measure the time saved

Before you automate a task, time it for a week. Afterwards, time it again. If an automation doesn't save time or reduce mistakes, remove it.
""",
    example="""
Nisha replaced her "which flavour, what size, what date?" chats with a Google Form: name, phone, pickup or delivery address, date and time, size, flavour, message on the cake, and allergies or special requests. Responses go straight into a sheet, where a formula works out the price. She shares the form through a quick reply. Orders now arrive complete, and she saves about 2 hours a week of messages.

Arun built a monthly care-plan report template in Sheets: catalogue items added, enquiries answered (counted from the owner's labels), the top questions and one suggestion. Copying it for each client takes 10 minutes instead of an hour. He also has a Calendar reminder for every client on the 1st of each month to update the catalogue, and any care-plan invoice unpaid after 7 days turns red.
""",
    resources=[
        ('gforms', 'Create a form, send it and open the responses in Sheets', '15 min'),
        ('gsheets', 'The basics of editing, formulas and sharing', '15 min'),
        ('wa-business', 'Quick replies, greeting and away messages, labels', '5 min'),
        ('appsscript', 'Optional, laptop only: what Apps Script can automate in Sheets, Gmail and Forms', '15 min'),
    ],
    steps=[
        'List 10 tasks you repeat, with roughly how long each takes per week. Time the top 3 properly this week.',
        'Pick 2–3 of them to automate, starting low on the ladder: templates, forms, formulas.',
        'Build each automation and test it yourself as the customer. (If you are also taking the Free AI Generalist Course in this app, its automation lessons go further.)',
        'Use the automations for a week, then time the same tasks again.',
        'Keep what saves time or reduces mistakes, and remove the rest. Write down the time saved per week.',
    ],
    proof='Your list of 10 tasks with times, links or screenshots of your 2–3 automations, and the before-and-after times.',
    templates=[
        ('automation candidates (paste into Google Sheets)', """
Task,Times per week,Minutes each,Minutes per week,Tool,Automation idea,Minutes per week after,Minutes saved
""", 'csv'),
        ('order form fields and useful formulas', """
ORDER FORM (Google Forms)
1. Your name (short answer, required)
2. WhatsApp number (short answer, required)
3. Pickup or delivery? (multiple choice)
4. Delivery address (paragraph; only for delivery)
5. Date and time needed (date and time)
6. Item and size (dropdown)
7. Special requests or allergies (paragraph)
8. How did you hear about us? (multiple choice:
   referral, WhatsApp Status, Instagram, Google, other)
At the top: "We use these details only to make and
deliver your order. We reply within 2 hours, 9 am-9 pm."

USEFUL SHEETS FORMULAS
Minutes per week (D2):     =B2*C2
Minutes saved (H2):        =D2-G2
Days since an invoice:     =TODAY()-B2
Overdue? (shows TRUE):     =TODAY()-B2>7
Number of paid orders:     =COUNTIF(F:F,"Paid")
Red overdue rows: Format > Conditional formatting >
Custom formula: =TODAY()-$B2>7
""", ''),
    ],
    mistakes=[
        ('Automating chaos.', 'If the process isn\'t clear, automation only makes mistakes faster. Write the SOP first.'),
        ('Skipping the test.', 'Fill in your own form and follow your own reminders before customers do.'),
        ('Removing the human touch.', 'Customers in a small town expect a person for complaints and special requests. Keep those personal.'),
        ('Unofficial bulk-messaging apps.', 'They can break WhatsApp\'s terms and get your number banned. Use the official app\'s tools.'),
        ('Paying for tools too early.', 'Free tools cover almost everything a micro-business needs. Pay only when the time saved is clearly worth it.'),
    ],
    quiz=[
        {'q': 'When should you automate a task?',
         'o': ['Before you have ever done it', 'After doing it by hand many times, when the steps are clear', 'Never', 'Only with paid software'],
         'a': 'B', 'why': 'You can only automate well what you understand well.'},
        {'q': 'Which is the lowest step on the automation ladder?',
         'o': ['Apps Script', 'AI assistants', 'Templates', 'Paid software'],
         'a': 'C', 'why': 'Saved templates are simple, free and often solve the problem.'},
        {'q': 'Why avoid unofficial WhatsApp bulk-messaging apps?',
         'o': ['They are slow', 'They can break WhatsApp\'s terms and get your number banned', 'They are too cheap', 'They don\'t work on Android'],
         'a': 'B', 'why': 'Losing your business number would cut you off from your customers.'},
        {'q': 'How do you know an automation is worth keeping?',
         'o': ['It looks clever', 'It saves time or reduces mistakes, measured before and after', 'Everyone uses it', 'It cost money'],
         'a': 'B', 'why': 'Measure, then keep what works.'},
    ],
    study='the Google Forms, Sheets and WhatsApp Business guides, plus Apps Script if you have time (about 50 minutes)',
    action='automate 2–3 repetitive tasks with free tools, test them and measure the time saved',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    10,
    title='Operations and systems',
    weeks=(24, 25), hours=12,
    overview="""
Operations is everything that happens between a customer saying yes and the customer being happy: making, delivering, answering questions and fixing problems. Good operations keep quality consistent, save your time and let someone else help you.

This module turns what you already do into written checklists (SOPs), gives you simple systems for stock, delivery and customer service, and then automates the most repetitive jobs with free tools, without losing the personal touch.
""",
    outcomes=[
        'Write SOPs for your three most repeated jobs and test one with another person',
        'Track stock with reorder points, cost your delivery and set customer service standards',
        'Handle complaints with a calm, repeatable method and log every one',
        'Automate 2–3 repetitive tasks with free tools after doing them by hand',
    ],
    lessons=LESSONS,
    project='Operations manual v1',
    project_steps=[
        'Your process map from enquiry to review request (L01).',
        'Three SOPs, one tested by someone else and improved (L01).',
        'Your stock sheet with reorder points, delivery rules and costs, and service standards (L02).',
        'Your complaint log and quick replies (L02).',
        'Your 2–3 automations, with the time saved each week (L03).',
    ],
    project_proof='One Google Doc called "Operations manual" that links to all of these, saved in Founder Toolkit/10 Operations.',
    rubric=[
        ('SOPs', 'All in my head', 'Written, but not tested', 'Three SOPs, one tested by another person and improved'),
        ('Stock and delivery', 'Often run out; delivery cost unknown', 'A stock list without reorder points', 'Reorder points set; delivery cost per order known'),
        ('Customer service', 'Reply when free', 'Some standards', 'A response-time promise, quick replies and a complaint log'),
        ('Automation', 'None, or automated chaos', 'One automation, not tested', '2–3 tested automations, with time saved measured'),
    ],
    short=[
        'L01: write one SOP, for your most frequent job.',
        'L02: set a response-time promise and write 3 quick replies.',
        'L03: build one automation, such as an order form or quick replies.',
    ],
    mistakes=[
        ('Keeping everything in your head.', 'Write it down once, and update it as you learn.'),
        ('Automating before the process is stable.', 'Do it by hand ten times first.'),
        ('Treating complaints as attacks.', 'They are free advice on what to fix.'),
    ],
)
