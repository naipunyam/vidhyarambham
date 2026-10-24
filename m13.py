from common import lesson, module

L1 = lesson(
    13, 1,
    title='Decisions, failure and pivots',
    weeks=(29, 29), hours=3,
    outcome='Use simple decision tools and a decision journal, review a setback without blame, and set clear triggers for when to pivot or close.',
    split='1 hour 15 minutes study, 1 hour 45 minutes action',
    core="""
### Two kinds of decisions

Some decisions are easy to reverse: a new flavour, a new post format, a different price for one week. Make these quickly and learn from them. Others are hard to reverse: signing a shop lease, taking a large loan, quitting a job, giving away ownership. Slow down for these, gather evidence and get advice.

### Simple decision tools

- **Pre-mortem:** imagine it is six months later and the decision has failed badly. Write down why. Then reduce those risks before you decide.
- **10-10-10:** how will I feel about this in 10 minutes, in 10 months and in 10 years?
- **Weighted pros and cons:** list them, give each a weight from 1 to 5 and add them up.
- **Ask the evidence:** what do my numbers and my customers say? Not my fears, and not my hopes.
- **Sleep on it:** never make a big decision on a day when you are angry, scared or exhausted.

### Keep a decision journal

For each important decision, write down the date, the decision, what you expect to happen and why, how sure you are, and when you will check. Months later, compare what happened with what you expected. You will learn whether your judgement tends to be too hopeful or too fearful, which no book can tell you.

### Learn from failure without blame

In a young business, a failure is usually an experiment that didn't work, not proof that you are a failure. OpenStax's chapter on early failure makes the point that early failures can lead to later success, if you learn from them. Use a **blameless post-mortem**:

1. What happened? The facts, in order.
2. What did we expect, and what was different?
3. Why did it happen? Ask "why?" five times, and look for causes in the process, not someone to blame.
4. What will we change?
5. What went well, which we should keep?

### When to pivot, and when to close

Set your triggers **in advance**, with numbers and dates:

- **Pivot trigger:** "If my repeat rate stays below 15% for 3 months, I change the offer or the customer group."
- **Close trigger:** "If the business still can't cover its own costs after 6 more months, or needs more than my risk limit, I close it in an orderly way."

Paul Graham's essay "Default Alive or Default Dead?" asks whether, at your current growth and costs, the business will survive without new money. If the answer is "dead", act early: cut costs, raise prices, change course.

### Closing well

Closing a business is not shameful; closing it badly is. If you close: finish or refund every paid order, pay suppliers and helpers, tell customers honestly, cancel registrations you no longer need, keep your records for as long as the law requires, and write a post-mortem so your next venture starts smarter.

### Get help

You don't have to decide alone. The District Industries Centre and its MSME Clinic, KIED's programmes, KSUM (for tech startups), experienced business owners and your accountability buddy can all help.
""",
    example="""
**Fathima's pivot, three months on.** Her free weekly mock test grew to 600 members, but only 18 paid ₹49 a month for full answers and rank lists. Her pivot trigger, fewer than 50 paying members by month 3, had been hit. Her pre-mortem for the next step warned against building an app too early. Her decision: keep the free test, stop the ₹49 plan, and sell a ₹199 "last 30 days" pack before each major exam, testing a different way of charging. Her decision journal predicted 40 sales for the first pack; she sold 52.

**Nisha's post-mortem.** Her Onam payasam pre-order went wrong: 8 of 30 containers leaked during delivery. The five whys: the lids didn't seal → the containers were cheap → she bought them at the last minute → she had never tested the packaging → her SOP had no "test the packaging" step. The change: a packaging test for every new product, now in her SOP. She refunded the 8 customers the same day, and 6 of them ordered from her again at Christmas.
""",
    resources=[
        ('os10', 'Section 10.2 Why Early Failure Can Lead to Success Later', '30 min'),
        ('os15', 'Sections 15.2 Making Difficult Business Decisions in Response to Challenges and 15.3 Seeking Help or Support', '30 min'),
        ('pg-aord', 'Re-read it, this time thinking about your business', '10 min'),
        ('kied', 'Look at the programmes for people who already run a business', '5 min'),
    ],
    steps=[
        'Write a decision journal entry for one decision you face now, using the template below.',
        'Run a pre-mortem on it: "It is six months later and this failed. Why?" Reduce the two biggest risks.',
        'Write a blameless post-mortem on your biggest setback so far, and make one change because of it.',
        'Write your pivot trigger and your close trigger, with numbers and dates.',
        'Talk to one mentor (at the DIC, the MSME Clinic, KIED or KSUM, or an experienced business owner) about your biggest current decision, and note their advice.',
    ],
    proof='Your decision journal entry with its pre-mortem, your post-mortem with the change you made, your two triggers and the mentor\'s advice.',
    templates=[
        ('decision journal', """
DECISION JOURNAL
Date: ____   Decision: ____________
Easy to reverse? Y / N
What I expect to happen: ____________
Why: ____________
How sure I am: ___%
Pre-mortem: if this fails, the likely reasons are
1. ____  2. ____  3. ____
How I will reduce them: ____________
Check again on: ____
What actually happened (fill in later): ____________
""", ''),
        ('blameless post-mortem and triggers', """
BLAMELESS POST-MORTEM
What happened (facts, in order): ____________
What we expected: ____   What was different: ____
Why? (five whys)
1. ____  2. ____  3. ____  4. ____  5. ____
What we will change (SOP, price, process): ____________
What went well, and we will keep: ____________

TRIGGERS (decide now, while you are calm)
Pivot if: ____ (a number) by ____ (a date)
Close if: ____ (a number) by ____ (a date)
If I close: finish or refund orders, pay everyone,
tell customers, cancel registrations, keep records,
write a post-mortem.
""", ''),
    ],
    mistakes=[
        ('Deciding when tired or angry.', 'Big decisions made in a bad moment are rarely good ones. Sleep on them.'),
        ('Treating every decision as huge.', 'Most choices are easy to reverse. Make them quickly and learn.'),
        ('Hiding failures.', 'A failure nobody reviews will happen again. Write the post-mortem.'),
        ('Pivoting every week.', 'Give each change enough time and enough customers to show a result before the next one.'),
        ('Having no close trigger.', 'Without one, a dying business can eat years and savings. Decide your limit while you are calm.'),
    ],
    quiz=[
        {'q': 'Which decision is hard to reverse and deserves extra care?',
         'o': ['Trying a new flavour for a week', 'Signing a three-year shop lease', 'Changing a caption', 'Posting at a new time'],
         'a': 'B', 'why': 'A long lease commits money for years, whatever happens to sales.'},
        {'q': 'What is a pre-mortem?',
         'o': ['A medical check-up', 'Imagining a decision has failed and listing why, before you decide', 'A tax form', 'A party after a launch'],
         'a': 'B', 'why': 'It surfaces risks while you can still reduce them.'},
        {'q': 'What does a blameless post-mortem look for?',
         'o': ['Someone to punish', 'Causes in the process, and what to change', 'Excuses', 'Nothing in particular'],
         'a': 'B', 'why': 'Fixing the process stops the same failure happening again.'},
        {'q': 'Why set pivot and close triggers in advance?',
         'o': ['To give up quickly', 'So decisions rest on numbers set while calm, not on fear or hope later', 'The law requires it', 'To impress investors'],
         'a': 'B', 'why': 'In a hard moment, a rule you set earlier is clearer than your feelings.'},
    ],
    study='OpenStax 10.2, 15.2 and 15.3, "Default Alive or Default Dead?" and KIED\'s programmes (about 1 hour 15 minutes)',
    action='keep a decision journal with a pre-mortem, write a blameless post-mortem, set your triggers and ask a mentor',
)

L2 = lesson(
    13, 2,
    title='Avoid burnout and scams; build an ethical business',
    weeks=(29, 29), hours=3,
    outcome='Protect your health, time and money, spot common scams aimed at small businesses, know where to report them, and write your own ethics rules.',
    split='1.5 hours study, 1.5 hours action',
    core="""
### Burnout: the quiet business killer

Running a business alongside PSC study, family duties or a job is demanding, and burnout builds slowly. Warning signs include:

- feeling tired even after sleep, for weeks
- dreading messages from customers
- making careless mistakes
- losing interest in things you used to enjoy
- irritability, headaches or poor sleep

**A rhythm you can keep up:**

- Protect your sleep and your PSC study hours first.
- Take **one full day off** every week, with a WhatsApp Business away message.
- Set business hours and keep them; customers adapt.
- Move your body every day, even if it is a 20-minute walk.
- Share the load with SOPs and a helper (Module 12).
- Talk to someone: your accountability buddy, your family, your friends.

If you feel overwhelmed, anxious or low for a long time, that is a reason to get support, not a weakness. **Tele-MANAS** is the Ministry of Health and Family Welfare's toll-free, 24-hour mental health helpline: dial **14416** or 1-800-89-14416, and you can talk in your own language.

### Scams aimed at small businesses

Scammers target new businesses because their owners are busy, hopeful and new to the rules. Common patterns:

| Scam | What it looks like | The truth |
| --- | --- | --- |
| Fake scheme agents | "Pay ₹5,000 and I'll get your Mudra or PMEGP loan approved" | MUDRA says it has no agents or middlemen. Apply yourself. |
| Fake registration fees | "Your Udyam, GST or FSSAI registration will be cancelled. Pay the renewal fee today." | Udyam registration is free. Check any notice on the official portal yourself. |
| Payment tricks | A "customer" sends a UPI collect request or a QR code "to send you money", or a fake payment screenshot | You never need to enter your UPI PIN to receive money. Check your own bank app, not a screenshot. |
| The big-order advance | A "bulk order" from someone claiming to be an officer or a company, who asks you to pay a "registration" or "transport" fee first | Real customers don't make sellers pay first. |
| Phishing links and fake apps | Messages with links to "update KYC", or loan apps promising instant money | Banks don't ask for PINs or OTPs. Use only official apps and websites. |
| Fake jobs and tasks | "Earn ₹5,000 a day liking videos", after a small deposit | Paying a deposit to get work is a classic scam. |
| Pyramid and money-circulation schemes | "Join for ₹10,000 and earn by recruiting others" | Promoting pyramid and money-circulation schemes is prohibited under India's Direct Selling Rules. |

**Protect yourself:**

- Never share OTPs, UPI PINs or passwords. Turn on two-step verification for WhatsApp, Google and your UPI apps.
- Check before you trust: call the official number, not the one in the message.
- Before dealing with an unknown "finance company" or deposit scheme, check whether it is registered on the RBI's **Sachet** portal.
- Read the RBI's **BE(A)WARE** booklet on common fraud methods once, and share it with your family.

**Report quickly.** For financial cyber fraud, call **1930** or use the National Cyber Crime Reporting Portal; quick reporting improves the chance of action. For consumer complaints, use the **National Consumer Helpline, 1915**. Report illegal deposit schemes on **Sachet**.

### An ethical business

Ethics isn't an extra. In a small town, your reputation is your business. Write your own rules, for example:

1. Honest advertising: no fake reviews, discounts, scarcity or claims.
2. Fair prices, shown clearly, with no hidden charges.
3. Quality and safety first, especially with food.
4. Suppliers and helpers paid in full and on time.
5. Customers' privacy and consent respected.
6. The taxes and fees you owe, paid.
7. Promises kept, or fixed fast when you can't keep them.
8. Competitors treated fairly: win on value, not by running others down.
9. Less waste and plastic where you can manage it.
10. Never taking money for something you won't deliver.
""",
    example="""
**Arun's near miss.** A WhatsApp message said: "Your Udyam registration will be cancelled today. Pay the ₹2,999 renewal fee at this link." The link opened a site that looked official. Remembering that Udyam registration is free, he checked his certificate on the official portal himself: nothing had changed. He reported the number and warned two of his client shops.

**Nisha's near miss.** A caller who said he was from an army camp ordered 40 cakes for a function, and asked her to scan a QR code "to receive the advance". Knowing she never needs to enter a PIN to receive money, she asked for the advance by a normal UPI transfer instead, and the caller disappeared. She posted a warning in her family groups.

**Arun's weekly rhythm.** PSC study comes first every day; ShopAssist gets 45 minutes on weekday evenings and 2 hours on Saturday; Sunday is fully off, with an away message. When he worked every day through the Onam rush, his mistakes doubled, so the day off became a rule.
""",
    resources=[
        ('rbi-beaware', 'Open the booklet from this press release and read Part C, on general precautions', 'about 45 min'),
        ('sachet', 'See how to check a registered entity and file a complaint', '5 min'),
        ('kp-1930', 'Read why reporting financial cyber fraud to 1930 quickly matters', '5 min'),
        ('cybercrime', 'The national reporting portal; type the address yourself', '2 min'),
        ('nch', 'Note the helpline number and the WhatsApp option', '3 min'),
        ('telemanas', 'Note the Tele-MANAS number, 14416', '2 min'),
        ('os3', 'Sections 3.2 Corporate Social Responsibility and Social Entrepreneurship and 3.3 Developing a Workplace Culture of Ethical Excellence and Accountability', '30 min'),
    ],
    steps=[
        '**Scam audit (30 minutes):** turn on two-step verification for WhatsApp and Google, check app permissions on your phone and remove apps you don\'t trust, and save 1930, 1915 and 14416 in your contacts.',
        'Share the scam table with your family, or in a family WhatsApp group.',
        'Write your ethics card (8–10 rules) and pin it where you work.',
        'Plan your weekly rhythm with one full day off, and set a WhatsApp Business away message for that day.',
        'Keep your day off for the next 2 weeks, and note how you feel and how many mistakes you make.',
    ],
    proof='Your completed scam safety checklist (no codes or passwords written in it), your ethics card, your weekly rhythm and your notes from the 2 weeks.',
    templates=[
        ('scam safety checklist and red flags', """
SCAM SAFETY CHECKLIST
[ ] Two-step verification on WhatsApp
[ ] Two-step verification on Google
[ ] Unknown apps removed; permissions checked
[ ] Saved: 1930 (cyber fraud), 1915 (consumer helpline),
    14416 (Tele-MANAS)
[ ] Family told: never share OTPs or UPI PINs
[ ] I check notices on official portals myself
[ ] I never pay "fees" to receive orders, loans or jobs

RED FLAGS
Urgency ("today only"), secrecy, "pay first to receive",
links asking for KYC details or an OTP, deals that are
too good to be true, people who won't meet or call from
an official number.
""", ''),
        ('ethics and wellbeing card', """
ETHICS AND WELLBEING CARD
My business rules:
1. ____
2. ____
3. ____
(8-10 rules)

My weekly rhythm:
PSC study: ____   Business: ____   Day off: ____
Sleep: ____ hours   Exercise: ____
Warning signs I watch for: ____
Person I talk to when it gets too much: ____
Tele-MANAS: 14416
""", ''),
    ],
    mistakes=[
        ('Working seven days a week for months.', 'Tired founders make costly mistakes. Take one full day off every week.'),
        ('Paying "fees" to get loans, orders or registrations.', 'Official schemes don\'t need agents, and real customers don\'t make you pay first.'),
        ('Trusting payment screenshots.', 'Check your own bank app before you hand over an order.'),
        ('Joining MLM schemes for "passive income".', 'Earning by recruiting others is the mark of a pyramid scheme, and promoting one is prohibited under the Direct Selling Rules.'),
        ('Cutting corners on hygiene, tax or honesty.', 'A short-term saving can cost you your reputation, which in a small town is the whole business.'),
    ],
    quiz=[
        {'q': 'A "customer" sends a QR code and tells you to scan it to receive your advance. What should you do?',
         'o': ['Scan it and enter your PIN', 'Refuse: you never need to enter a UPI PIN to receive money', 'Ask for a bigger advance', 'Share your OTP'],
         'a': 'B', 'why': 'Entering your PIN sends money out of your account, not in.'},
        {'q': 'Where should you report financial cyber fraud quickly?',
         'o': ['Only at a police station, weeks later', 'On 1930 or the National Cyber Crime Reporting Portal', 'On your WhatsApp Status', 'Nowhere'],
         'a': 'B', 'why': 'Kerala Police stress that prompt reporting helps investigators act.'},
        {'q': 'Which of these is a warning sign of burnout?',
         'o': ['Feeling rested', 'Feeling tired even after sleep for weeks, and dreading customer messages', 'Enjoying your work', 'Taking a day off'],
         'a': 'B', 'why': 'Notice the signs early and change your rhythm.'},
        {'q': 'Someone offers to get your Mudra loan approved for a ₹5,000 fee. What does MUDRA say about agents?',
         'o': ['Agents are required', 'It has no agents or middlemen', 'Agents take 10%', 'Only banks use agents'],
         'a': 'B', 'why': 'Apply yourself at a bank or other lender, and pay nobody to "arrange" it.'},
        {'q': 'What is Tele-MANAS?',
         'o': ['A loan scheme', 'A toll-free, 24-hour mental health helpline (14416)', 'A tax portal', 'A business licence'],
         'a': 'B', 'why': 'It is run under the Ministry of Health and Family Welfare, with services in many languages.'},
    ],
    study='Part C of the RBI\'s BE(A)WARE booklet, the Sachet, 1930, 1915 and Tele-MANAS pages, and OpenStax 3.2 and 3.3 (about 1.5 hours)',
    action='do a scam audit, write your ethics card, and keep a weekly day off for two weeks',
)

LESSONS = [L1, L2]

MODULE = module(
    13,
    title='Resilience and ethics',
    weeks=(29, 29), hours=7,
    overview="""
Every founder has bad weeks: a failed test, a lost customer, a festival with no orders, a scam call that sounds real. Resilience isn't about never failing. It is about making good decisions under pressure, learning from mistakes without blaming yourself or others, protecting your health and your money, and running a business you are proud of.

This module gives you simple decision tools, a way to review failures, rules for when to pivot or close, protection against burnout and common scams, and your own ethics rules.
""",
    outcomes=[
        'Use simple decision tools and keep a decision journal',
        'Review a setback with a blameless post-mortem, and set pivot and close triggers',
        'Recognise burnout early and keep a weekly rhythm you can sustain',
        'Spot common scams aimed at small businesses and know where to report them',
        'Write your own ethics and wellbeing rules',
    ],
    lessons=LESSONS,
    project='Founder operating rules',
    project_steps=[
        'Two decision journal entries (L01).',
        'One blameless post-mortem, and your pivot and close triggers (L01).',
        'Your completed scam safety checklist, with 1930, 1915 and 14416 saved (L02).',
        'Your ethics and wellbeing card, and your weekly rhythm with a day off (L02).',
        'Share your rules with your accountability buddy and ask them to hold you to them.',
    ],
    project_proof='Your founder operating rules (one Google Doc) in Founder Toolkit/13 Founder rules.',
    rubric=[
        ('Decisions', 'Impulsive', 'Thought through, but not written down', 'A decision journal with reasons, reviewed later'),
        ('Failure', 'Hidden, or someone blamed', 'Talked about', 'A blameless post-mortem, with a change made'),
        ('Pivot and close triggers', 'None', 'Vague', 'Written triggers with numbers and dates'),
        ('Wellbeing', 'No rest', 'Some rest', 'A weekly day off, sleep protected, warning signs known'),
        ('Scam safety and ethics', 'Not considered', 'Some awareness', 'Checklist done, numbers saved, ethics card written and shared'),
    ],
    short=[
        'L01: write one decision journal entry and your close trigger.',
        'L02: save 1930, 1915 and 14416, turn on two-step verification and write 5 ethics rules.',
    ],
    mistakes=[
        ('Deciding when tired or angry.', 'Sleep on big decisions.'),
        ('Hiding failures.', 'Review them without blame and change the process.'),
        ('Working seven days a week for months.', 'Protect one full day off.'),
    ],
)
