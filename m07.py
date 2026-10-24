from common import lesson, module

L1 = lesson(
    7, 1,
    title='Get your first 10 customers',
    weeks=(16, 16), hours=6,
    outcome='Build a list of 50 prospects, run daily outreach with a simple pipeline, and close paying customers who are not friends or family.',
    split='1 hour study, 5 hours action',
    core="""
Sales is helping the right people decide. Your first customers won't find you by chance; you go to them. Paul Graham's "Do Things That Don't Scale" makes the point plainly: early on, founders recruit customers one at a time, by hand.

### Where the first 50 prospects come from

1. **People you interviewed**, and anyone who joined your waiting list in Module 4.
2. **Your second-degree network:** ask 10 friends and relatives for one introduction each.
3. **Walk-ins:** shops, offices, clinics and coaching centres near you, at quiet hours.
4. **Communities:** online and offline groups where your customers gather, within their rules.
5. **Partners:** businesses that serve the same customers (next lesson).

### Qualify before you pitch

A good prospect has four things. Check them gently in conversation:

- **Problem:** they have the problem now.
- **Budget:** they can pay your price.
- **Decision:** they decide, or you can talk to the person who does.
- **Timing:** they want it solved soon, not "maybe next year".

### Your pipeline

Track every prospect through these stages in your Customers tab:

**Prospect → Contacted → Conversation → Offer sent → Won (paid) or Lost → Delivered → Repeat or referral**

Every open prospect needs a **next step** and a **date**. A pipeline without dates is just a list.

### The numbers, honestly

Sales is partly a numbers game. An early funnel might look like this (an illustration, not a promise): 50 prospects → 25 replies → 12 conversations → 6 offers → 3 sales. Your rates will be different, so measure them. If 6 in every 100 prospects buy and you want 10 more customers, you need about 170 more prospects, or a better conversion rate.

### A daily habit beats a big push

Part-time: 3 new contacts each weekday evening, plus visits or calls at the weekend. Full-time: 10–15 a day. Small, steady effort keeps the pipeline full.

### Respect people and the rules

Send personal messages, not copy-pasted blasts. Don't add people to groups without asking. When someone says no, stop. WhatsApp can restrict accounts that send bulk unwanted messages, and pestering people ruins your name in a small town.
""",
    example="""
By week 16 Arun has 10 paying shops: 4 pilots from Module 4 and 6 from his price test. His goal is 30 by the end of the course.

His new list of 50 prospects: 22 shops from earlier conversations, 14 introductions from friends, uncles and existing clients, and 14 walk-in targets on the main roads of Kuttiady, Thottilpalam, Nadapuram and Vatakara. His habit: three WhatsApp messages or calls each weekday evening after PSC study, and a two-hour walk-in round on Saturday late mornings, when most owners have time to talk.

After two weeks: 50 prospects → 31 replied or met him → 17 real conversations → 9 offers → 5 sales (three Standard, two Basic). Three of the five were people he had never met before. His conversion from prospect to sale was 10%, so to win 15 more shops he needs about 150 more prospects, or a better close rate. That is what the next two lessons work on.
""",
    resources=[
        ('yc-first', 'Watch the whole talk', 'about 23 min'),
        ('hubspot-sales', 'Free. Start the Inbound Sales course with its first class', 'about 30 min'),
        ('pg-ds', 'Re-read the part on recruiting users by hand', '10 min'),
    ],
    steps=[
        'Build your list of 50 prospects in the Customers tab, using the five sources above.',
        'Mark what you already know about each one: problem, budget, decision and timing.',
        'Contact at least 25 of them this week with personal messages, calls or visits. A short opener is enough for now; the next lesson gives full scripts.',
        'Log every contact: its stage, the next step and the date.',
        'Aim for 3 or more real conversations and at least 1 paid sale to someone who is not a friend or family member. Count how many prospects are at each stage.',
    ],
    proof='The Customers tab with 50 prospects, at least 25 contacts logged with next steps, and your stage counts.',
    templates=[
        ('pipeline (Customers tab)', """
Code,Name,Phone (with consent),Source,Problem? (Y/N),Budget? (Y/N),Decides? (Y/N),Timing,Stage,Last contact,Next step,Next date,Offer,Value (Rs),Paid (Rs),Notes
P01,,,REF,,,,,Prospect,,,,,,,
""", 'csv'),
        ('daily outreach tracker', """
DAILY OUTREACH (part-time: 3 a day; full-time: 10-15 a day)
Date: ____
New contacts: 1. ____ 2. ____ 3. ____
Follow-ups due today: ____
Conversations booked: ____
Offers sent: ____  Sales: ____  Amount: ₹____
One thing I learned: ____________
""", ''),
    ],
    mistakes=[
        ('Waiting for customers to come to you.', 'Posting and hoping is not selling. Reach out personally every day.'),
        ('Mass messaging.', 'One personal message beats fifty copy-pasted ones, and blasts can get your WhatsApp restricted.'),
        ('Selling to people who can\'t buy.', 'Check problem, budget, decision and timing before you spend hours on someone.'),
        ('No next step.', 'Every conversation should end with an agreed next step and a date.'),
        ('Counting only friends.', 'Friends and family are welcome customers, but they don\'t prove the business works. Track strangers separately.'),
    ],
    quiz=[
        {'q': 'Which four things does a qualified prospect have?',
         'o': ['Name, age, phone and address', 'The problem, a budget, the power to decide and the right timing', 'Instagram, Facebook, WhatsApp and email', 'A shop, a car, a house and land'],
         'a': 'B', 'why': 'Without all four, a sale is unlikely however good your offer is.'},
        {'q': 'If 5% of your prospects buy, how many prospects do you need for 10 customers?',
         'o': ['20', '50', '200', '500'],
         'a': 'C', 'why': '10 ÷ 0.05 = 200. A better conversion rate means fewer prospects.'},
        {'q': 'What must every open prospect in your pipeline have?',
         'o': ['A discount', 'A next step and a date', 'A gift', 'A signed contract'],
         'a': 'B', 'why': 'Dates turn a list into a pipeline you can act on.'},
        {'q': 'Why track sales to strangers separately from sales to friends and family?',
         'o': ['Friends don\'t pay', 'Sales to strangers show the business works without personal favours', 'They are taxed differently', 'WhatsApp requires it'],
         'a': 'B', 'why': 'Strangers buy only because the offer is worth it.'},
    ],
    study='the YC first-customers talk, the first HubSpot sales class and the PG essay (about 1 hour)',
    action='build a 50-prospect pipeline, contact 25 and win a paying customer who is not a friend',
)

L2 = lesson(
    7, 2,
    title='Outreach scripts and partnerships',
    weeks=(17, 17), hours=5,
    outcome='Use short, tested scripts for WhatsApp, phone, walk-ins and email, follow up on a schedule, and set up one partnership that sends you customers.',
    split='1 hour 20 minutes study, 3 hours 40 minutes action',
    core="""
A script is not something to recite. It is a tested structure that keeps you clear and brief. Good outreach has five parts:

1. **A personal opener:** who you are and how you know of them ("Rasheed from the textile shop gave me your number").
2. **The reason:** why you are contacting this particular person.
3. **The value:** the problem you solve or the result, in one sentence, with proof if you have it.
4. **A small ask:** 10 minutes, a visit, a demo, a sample. Not "buy now".
5. **An easy exit:** "If it's not useful, no problem at all." People relax when they know they can say no.

### Tips for each channel

- **WhatsApp text:** under 60 words, ending with a question.
- **WhatsApp voice note:** common and personal in Kerala. Keep it under 30 seconds, speak slowly, then send a one-line text summary.
- **Phone call:** first ask, "Is this a good time for 2 minutes?"
- **Walk-in:** go at quiet hours, carry your one-page offer sheet, and leave a card or a sample.
- **Email:** for offices, schools and professionals. A clear subject line and three short paragraphs.

### Follow up

Most people don't reply to a first message because they are busy, not because they aren't interested. A polite schedule:

- **Day 0:** your first message
- **Day 2–3:** a short follow-up with something useful (a tip, a photo of a result)
- **Day 7:** a check-in offering a specific time
- **Day 14:** a last, friendly message: "I'll stop here so I don't disturb you. If it's ever useful, my number is ____."

Then stop, mark them "Lost: no reply" and move on.

### Partnerships: customers who come to you

A **partner** is a business that already serves your customers but doesn't compete with you:

| Your business | Good partners |
| --- | --- |
| Home bakery | Party decorators, photographers, event halls, gift shops |
| WhatsApp setup for shops | Mobile shops, printing shops, tax practitioners' offices, billing software sellers |
| PSC practice packs | Libraries, tuition centres, teachers with YouTube channels, stationery shops near colleges |
| CV service | Nursing and engineering coaching centres, language institutes, properly licensed recruitment agencies |

Common ways to partner: a **referral fee** (for example 10% of the first order), a **bundle** (their product with yours), **co-marketing** (you promote each other) or **white-label** (you deliver under their name).

Write the terms down in a short note or message that both of you confirm: what each side does, the fee and when it is paid, how referrals are tracked, and how either side can end it.

Choose partners carefully. A partner who makes wild promises damages your name, and for anything involving overseas jobs, deal only with properly licensed agencies: fake job offers are a common scam. Never let a partner promise customers anything that isn't in your offer sheet.
""",
    example="""
Arun tested two WhatsApp openers on 20 shops each:

- **A:** "Hi, I help shops with WhatsApp Business. Interested?" got 3 replies out of 20 (15%).
- **B:** "Hi Ramesh, Rasheed from the textile shop on Kuttiady main road told me you get a lot of WhatsApp enquiries in the evenings. I set up his WhatsApp Business so customers get photos and prices in minutes; two customers ordered from his catalogue without coming in. Can I show you on your phone for 10 minutes on Saturday? If it's not useful, no problem." got 11 replies out of 20 (55%).

He kept B. He also agreed a partnership with a printing shop in Kuttiady that sells visiting cards and shop boards: the printer recommends ShopAssist to new shops and receives ₹200 for each one that buys a setup. They wrote the terms in one WhatsApp message and both replied "agreed". In the first month, the printer sent three shops and two bought.

Nisha agreed a similar arrangement with a party decoration shop: the decorator suggests her cakes when families book a birthday, and she pays 10% of each cake order that comes through them.
""",
    resources=[
        ('hubspot-sales', 'Continue the Inbound Sales course: the classes on connecting with and exploring prospects', 'about 1 hour'),
        ('os12', 'Section 12.1 Building and Connecting to Networks', '20 min'),
    ],
    steps=[
        'Adapt the scripts below to your business, in English and Malayalam.',
        'Use each script at least 5 times this week, and track the reply rate for each one in your Customers tab.',
        'Follow up every open prospect on the schedule: day 2–3, day 7 and day 14.',
        'List 5 possible partners, and propose a partnership to at least 2 of them, in person or by phone.',
        'Agree one partnership with written terms. A WhatsApp message that both of you confirm is enough to start.',
    ],
    proof='Your adapted scripts, the reply rate for each script, and the written terms of your partnership.',
    templates=[
        ('outreach scripts and follow-ups', """
WHATSAPP (under 60 words)
Hi [name], [who referred you / how I know you]. I help
[type of customer] with [problem]. [One proof: a result
or a customer]. Could I show you in 10 minutes on [day]?
If it's not useful, no problem at all.

MALAYALAM
നമസ്കാരം [പേര്], [ആര് പറഞ്ഞിട്ട് / എങ്ങനെ അറിയാം].
[ഉപഭോക്താക്കൾക്ക്] [പ്രശ്നം] പരിഹരിക്കാൻ ഞാൻ സഹായിക്കുന്നു.
[ഒരു ഫലം]. [ദിവസം] 10 മിനിറ്റ് കാണിച്ചുതരട്ടെ?
ഉപകാരമില്ലെങ്കിൽ ഒരു പ്രശ്നവുമില്ല.

PHONE
"Hello [name], this is [your name] from [place]. Is this
a good time for 2 minutes? ... [reason and value] ...
Could I visit on [day] at [time] to show you?"

WALK-IN
"Namaskaram, I'm [name]. I help [type] shops with
[problem]. Is the owner free for 5 minutes now, or is
there a better time?" Leave your offer sheet.

EMAIL
Subject: [result] for [their business]
Paragraph 1: who you are, and why you are writing to them
Paragraph 2: the result you get, with one proof
Paragraph 3: a small ask, with two time options

FOLLOW-UPS
Day 2-3: "Sharing a quick example: [photo or tip]."
Day 7: "Would Saturday 11 am or Monday 4 pm suit you?"
Day 14: "I'll stop here so I don't disturb you. If it's
ever useful, my number is [number]. Thank you!"
""", ''),
        ('partnership note', """
PARTNERSHIP NOTE (both sides confirm by message)
Partners: [you] and [partner]
What [partner] does: recommends us to ____
What we do: ____ (for example: recommend them, bundle)
Fee: ____ (for example 10% of the first order, or ₹200
per paying customer), paid by ____ within ____ days
Tracking: the customer says "[partner] sent me" or uses
the code ____
Promises to customers: only what is in our offer sheet
Either side can end this with ____ days' notice
Start date: ____
""", ''),
    ],
    mistakes=[
        ('Long messages.', 'Nobody reads a paragraph from a stranger. Keep WhatsApp messages under 60 words.'),
        ('Talking about yourself.', 'Lead with their problem and the result, not your life story.'),
        ('No clear ask.', 'End with one small, specific request: a day and a time.'),
        ('Giving up after one message.', 'Follow up three times over two weeks, politely, then stop.'),
        ('Partnerships on a handshake only.', 'Write the terms in one message that both sides confirm, so nobody is surprised later.'),
    ],
    quiz=[
        {'q': 'Which opener is likely to work better?',
         'o': ['"Interested in my service?"', 'A personal opener naming who referred you, the result you get and a small ask with a specific time', 'A 300-word message', 'A forwarded poster with no text'],
         'a': 'B', 'why': 'Personal, specific and easy to say yes to. In Arun\'s test it got 55% replies against 15%.'},
        {'q': 'A prospect hasn\'t replied to your first message. What should you do?',
         'o': ['Never contact them again', 'Follow up politely on day 2–3, day 7 and day 14, then stop', 'Message them every day', 'Add them to a group'],
         'a': 'B', 'why': 'Busy people often reply to the second or third message. Stop after the fourth.'},
        {'q': 'Which is a good partner for a home bakery?',
         'o': ['Another home baker on the same street', 'A party decoration shop', 'A tyre shop', 'A bank'],
         'a': 'B', 'why': 'Same customers at the same moment, and no competition.'},
        {'q': 'What should a written partnership note cover, at least?',
         'o': ['Only the start date', 'What each side does, the fee and when it is paid, tracking, and how to end it', 'Nothing, trust is enough', 'The partner\'s family details'],
         'a': 'B', 'why': 'Clear terms keep good partners and avoid arguments.'},
    ],
    study='the HubSpot classes on connecting and exploring, and OpenStax 12.1 (about 1 hour 20 minutes)',
    action='test outreach scripts, follow up on schedule and agree one written partnership',
)

L3 = lesson(
    7, 3,
    title='Handle objections, close and follow up',
    weeks=(18, 18), hours=4,
    outcome='Respond calmly to common objections, ask for the sale clearly, collect payment with written terms, and set a follow-up for every open lead.',
    split='45 minutes study, 3 hours 15 minutes action',
    core="""
An objection is usually a question or a worry in disguise. "It's too expensive" often means "I'm not sure it's worth it" or "I can't pay it all at once". Your job is to understand, not to win an argument.

### A simple method: LAER

1. **Listen** to the whole objection without interrupting.
2. **Acknowledge** it: "That's a fair question."
3. **Explore** what is behind it: "When you say expensive, compared with what?"
4. **Respond** with facts, proof or an option, then check: "Does that answer your worry?"

### Common objections and calm responses

| What they say | What it may mean | A calm response |
| --- | --- | --- |
| "വില കൂടുതലാണ്" (it's too expensive) | Not sure it's worth it, or short of cash | "Compared with what? ... One extra sale a month covers it. We can also start with the Basic package." |
| "I'll think about it" | A worry they haven't said | "Of course. So I can help, what's the main thing you're unsure about?" |
| "I need to ask my husband / my son in Dubai" | A shared decision | "Good idea. Shall I send a 1-minute voice note you can forward, or join a call with both of you?" |
| "My nephew can do it" | Price, or doubt about the value | "That can work. The difference is ____, and I support you every month. Would a trial help you compare?" |
| "Send the details on WhatsApp" | A polite brush-off, or real interest | "Sure. So I send the right thing, which part matters most to you?" Then agree a time to follow up. |
| "I tried this before and it didn't work" | A bad past experience | "What happened? ... Here is what we do differently, and here is my money-back promise." |
| "Not now. After Onam." | Timing | "Understood. Shall I call on [date]? Here's one free tip until then." |

### Ask for the sale

Many beginners never actually ask. When the customer's questions have been answered, ask clearly:

- **Summary close:** "So: catalogue, quick replies and the Google profile for ₹1,800, set up this Saturday. Shall we go ahead?"
- **Choice close:** "Would the Basic or the Standard package suit you better?"
- **Trial close:** "Would you like to try it for two weeks with the money-back promise?"
- **Real deadline:** "The festival price ends on Sunday." Use it only if it is true.

Then be quiet and let them answer.

### Collect payment and put the terms in writing

- Take the advance by UPI and send a receipt the same day.
- Send a short written summary: what is and isn't included, the price, the date, the payment terms and your refund or redo policy. A WhatsApp message is enough for small jobs; for bigger ones, use the simple agreement in Module 9.

### Follow up after the sale, and after a no

Check in after delivery ("Is everything working well?"), then ask for a review and a referral at the happy moment (ENT-M06-L04). After a "no", ask politely: "Can I ask what made you decide not to?" Reasons for losing are valuable data.

### Never pressure or deceive

No false deadlines, no fake scarcity, no promises you can't keep, and no pushing people who have said no. In a small town, one pushy sale can cost you ten future customers.
""",
    example="""
Arun visited a mobile shop in Thottilpalam:

**Owner:** "₹1,800? Too much. My nephew can do it."
**Arun:** "That's fair; a nephew is a good option. Can I ask how many WhatsApp enquiries you get on a busy day?"
**Owner:** "Maybe 30. He only comes on Sundays."
**Arun:** "So on weekdays, who replies?"
**Owner:** "Nobody, until I close."
**Arun:** "That's the gap I fix. Rasheed in Kuttiady had two catalogue orders in his first week. If one extra phone sale a month covers the cost, would it be worth trying? I can do the Basic package for ₹999 now, and you can upgrade later."
**Owner:** "Okay, Basic. But what if it doesn't work?"
**Arun:** "Then I refund you within 14 days. Shall I set it up on Saturday at 11?"

He took a ₹500 advance by UPI, sent a receipt and a WhatsApp summary of what was included, and set a reminder to follow up a week after the setup. Two months later, the owner upgraded to the Standard package and joined the care plan.
""",
    resources=[
        ('hubspot-sales', 'Finish the Inbound Sales classes on advising and closing', 'about 45 min'),
    ],
    steps=[
        'List the 5 objections you hear most often, using the notes in your Customers tab.',
        'Write a calm LAER response to each one in the playbook below, in English and Malayalam.',
        'Role-play with a friend or family member: they raise each objection and you respond. Record it on your phone and listen back once.',
        'Use the playbook in real conversations this week. Ask for the sale clearly whenever the customer\'s questions have been answered.',
        'Make sure every open lead has a next step and a date. For every "no", ask the reason and record it.',
    ],
    proof='Your objection playbook, the role-play recording, and at least 1 closed sale or 5 recorded reasons for "no".',
    templates=[
        ('objection playbook and closing lines', """
OBJECTION PLAYBOOK
Objection 1: "____"
  What it may mean: ____
  Question to explore: ____
  Response: ____
  Proof or option: ____
(repeat for objections 2-5)

CLOSING LINES
Summary: "So: ____ for ₹____, starting ____.
Shall we go ahead?"
Choice: "Would ____ or ____ suit you better?"
Trial: "Would you like to try it for ____ with my
money-back promise?"

AFTER A NO
"Thank you for your time. Can I ask what made you
decide not to? It helps me improve."
""", ''),
        ('order confirmation', """
ORDER CONFIRMATION (send on WhatsApp after the yes)
Thank you, [name]! Here is what we agreed:
Included: ____
Not included: ____
Price: ₹____
Advance received: ₹____ on ____ (UPI ref ____)
Balance: ₹____ due on ____
Delivery or setup date: ____
Refund or redo policy: ____
Questions any time: [number]
""", ''),
    ],
    mistakes=[
        ('Arguing.', 'Proving the customer wrong loses the sale. Ask what is behind the objection instead.'),
        ('Discounting at the first objection.', 'Offer a smaller package or a trial before you cut the price.'),
        ('Never asking for the sale.', 'If you don\'t ask, many people won\'t decide. Ask clearly, then stay quiet.'),
        ('Nothing in writing.', 'A short written summary prevents "I thought it included…" arguments later.'),
        ('Forgetting lost leads.', 'Ask why, record it, and check in again when timing was the reason.'),
    ],
    quiz=[
        {'q': 'A customer says, "I\'ll think about it." What is a good response?',
         'o': ['"Okay, bye."', '"Of course. What\'s the main thing you\'re unsure about?"', 'Offer 50% off immediately', 'Argue with them'],
         'a': 'B', 'why': 'It uncovers the real worry so you can answer it.'},
        {'q': 'In LAER, what does the "E" stand for?',
         'o': ['Escape', 'Explore', 'Explain loudly', 'End'],
         'a': 'B', 'why': 'Exploring finds out what is behind the objection.'},
        {'q': 'Which of these is a choice close?',
         'o': ['"Would the Basic or the Standard package suit you better?"', '"Buy now or regret it"', '"Only 1 left!" when it isn\'t true', '"Let me know"'],
         'a': 'A', 'why': 'It asks for a decision between two good options, without pressure.'},
        {'q': 'Why send a written order confirmation?',
         'o': ['The law requires one for every sale', 'It records what was agreed, so there are no disputes later', 'To look busy', 'To collect personal data'],
         'a': 'B', 'why': 'Clear terms protect both you and the customer.'},
    ],
    study='the HubSpot classes on advising and closing (about 45 minutes)',
    action='build an objection playbook, role-play it, use it in real sales and log a reason for every no',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    7,
    title='Sales',
    weeks=(16, 18), hours=17,
    overview="""
Marketing makes people aware of you; sales turns interested people into paying customers. For a small business, sales is mostly honest conversations: finding the right people, asking good questions, making a clear offer, handling doubts and following up.

This module gives you a pipeline, scripts in English and Malayalam, an objection playbook and a follow-up system. Your target by the end of week 18: 50 sales conversations logged, and paying customers who are not friends or family.
""",
    outcomes=[
        'Build a list of 50 prospects and run a daily outreach habit with a simple pipeline',
        'Use tested scripts for WhatsApp, phone, walk-ins and email, and set up one partnership',
        'Handle common objections calmly, ask for the sale clearly and collect payment with written terms',
        'Follow up so that no lead is forgotten, and ask for reviews and referrals after delivery',
    ],
    lessons=LESSONS,
    project='Sales kit and results',
    project_steps=[
        'Your adapted scripts (L02) and objection playbook (L03), in one document.',
        'Your Customers tab with at least 50 prospects and every conversation logged (L01).',
        'One partnership with written terms (L02).',
        'Your numbers: conversations, offers, sales and the conversion rate at each step.',
        'Your top 5 reasons for "no", and what you will change because of them.',
    ],
    project_proof='The sales kit document in Founder Toolkit/07 Sales, plus your Customers tab.',
    rubric=[
        ('Pipeline', 'No list', 'A list, but no stages or dates', '50 or more prospects, with stages, next steps and dates'),
        ('Outreach', 'Mass messages', 'Personal, but irregular', 'Personal, a daily habit, with follow-ups'),
        ('Scripts', 'None', 'Written, not tested', 'Tested, reply rates compared, improved'),
        ('Objections and closing', 'Argue or discount', 'Answer some objections', 'Playbook used, a clear ask, payment terms in writing'),
        ('Results', 'No sales', 'Sales to friends and family only', 'Paying customers who are not friends or family'),
    ],
    short=[
        'L01: list 25 prospects and contact 10.',
        'L02: use one WhatsApp script and one follow-up.',
        'L03: prepare answers to your top 3 objections.',
    ],
    mistakes=[
        ('Waiting for customers to come.', 'Reach out personally, every day, even if only to three people.'),
        ('Mass messaging strangers.', 'Send personal messages to the right people instead.'),
        ('Giving up after one message.', 'Most sales need several polite follow-ups.'),
    ],
)
