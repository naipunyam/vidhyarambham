"""Module 15: Scams and fraud protection."""
from common import lesson, module, link, fence, table, inr, ASOF, CHECK

M = 15

SCAM_MESSAGES = [
    ('A', 'WhatsApp: "Join our VIP stock group. Our analyst gives 5% daily profit. 2,300 members earning. Install this app to trade with our institutional account."', 'Fake trading app and unregistered tipster: guaranteed daily profit, an unknown app, no SEBI registration. SEBI warns about exactly these.'),
    ('B', 'A relative: "Put ₹1 lakh in this company. It pays 4% every month, and you get ₹5,000 for every friend who joins."', 'Ponzi pattern: high fixed monthly returns plus recruitment rewards. 4% a month is about 60% a year compounded.'),
    ('C', 'SMS: "Your KSEB connection will be disconnected tonight at 9.30 pm. Call 98XXXXXXXX immediately."', 'Phishing by urgency: utilities don\'t send such SMS from personal numbers. Check through the official app or office.'),
    ('D', 'Video call from a "CBI officer" in uniform: "A parcel in your name has drugs. You are under digital arrest. Transfer money for verification."', '"Digital arrest" fraud: agencies don\'t arrest people on video calls. Hang up, call 1930.'),
    ('E', 'Instagram ad: "Earn ₹3,000 a day liking YouTube videos. Small deposit to unlock higher tasks."', 'Task scam: small payouts first, then deposits that never come back.'),
    ('F', 'A KSFE branch notice about a new chitty, with the official chitty rules and a registered agreement.', 'Not a scam: a regulated, government-owned institution with written terms. Still compare it as a loan or saving (FIN-M09-L07).'),
]

L1 = lesson(
    M, 1,
    title='Investment scams: Ponzi schemes, MLM, fake apps and finfluencers',
    weeks=(28, 28), hours=2,
    outcome='Recognise the patterns of Ponzi schemes, pyramid MLMs, fake trading apps and unregistered tipsters, and check any offer against official registers before parting with money.',
    split='30 minutes reading, 30 minutes resources, 60 minutes action',
    core=f"""
Kerala has seen large investment frauds that ruined thousands of families, some running for years with apparently steady payments. News reports describe victims of the **Highrich** case in Kasaragod still waiting for justice ({link('om-highrich', 'Onmanorama headline, December 2024')}) and the High Court criticising inaction in the **₹2,000 crore Popular Finance** case ({link('om-popular', 'Onmanorama headline, November 2025')}). The people who lost money were not foolish; the schemes were designed to look trustworthy.

### Ponzi schemes

A **Ponzi scheme** pays "returns" to earlier investors from the money of newer ones. It works only while new money keeps coming, then collapses. Signs:

- **High, steady, "guaranteed" returns**, such as 2–5% a month, regardless of markets
- **Rewards for bringing in others**
- Vague explanations: "trading", "gold", "crypto", "foreign projects"
- **Pressure and secrecy:** "limited slots", "don't tell the bank"
- **Early payouts arrive on time** to build trust, often through people you know

India's **Banning of Unregulated Deposit Schemes Act, 2019** bans deposit schemes that aren't registered or regulated; its rules were notified to act against Ponzi schemes ({link('ml-buds', 'Moneylife headline')}). RBI's **Sachet** portal lets you check lists of entities registered with different regulators and file a complaint ({link('sachet', 'RBI Sachet')}).

### Pyramid schemes dressed as MLM

Real direct selling earns from **selling products to real customers**. A pyramid scheme earns mainly from **recruiting people who pay to join**. The Consumer Protection (Direct Selling) Rules, 2021 prohibit direct sellers from promoting pyramid schemes or money circulation schemes, or from persuading people to buy on the promise that they can recover the price by recruiting others ({link('ml-mlm', 'Moneylife, December 2021')}). Ask: "If no one new joined, would anyone still buy the product at this price?"

### Fake trading apps, tip groups and finfluencers

A very common pattern now: a WhatsApp or Telegram group shares "expert" stock or crypto tips, then asks you to install an app or join an "institutional account". The app shows huge profits; when you try to withdraw, you are asked for a "tax" or "fee". The money was never invested. SEBI's investor website warns about **fake trading apps, "stock market guru" scams, pump-and-dump and dabba trading** ({link('sebi-investor', 'SEBI investor site')}).

- Anyone giving paid investment advice or stock recommendations must be **registered with SEBI**; check the {link('sebi-ia-list', 'list of registered investment advisers')} and SEBI's guidance ({link('sebi-ia-caution', 'SEBI')}).
- SEBI-regulated firms can't be associated with unregistered finfluencers who give advice or claim returns ({link('bt-finfluencer', 'Business Today')}).
- Registered intermediaries collect money through **@valid UPI handles**, and **SEBI Check** verifies a UPI ID or bank account before you pay ({link('sebi-valid', 'Moneylife')}).
- "Digital gold" and similar products sit outside SEBI's regulation ({link('sebi-digigold', 'Moneylife')}).

### Five questions before any investment

1. **Who regulates it?** RBI, SEBI, IRDAI, PFRDA or a state law? Check the register yourself.
2. **Can I explain how it makes money** in two sentences?
3. **Are returns promised?** Real investments can't promise high returns.
4. **Can I get my money out, and how?** Test small, and read the exit terms.
5. **Who benefits if I say yes today?** Urgency is a sales tool.
""",
    example=f"""
**Anu's** aunt, Rajani, was invited to a "business opportunity" meeting at a hotel in Kozhikode. The company sold health supplements and promised that members earned "₹50,000 a month" by building a team. Joining cost ₹25,000 in products.

Anu and Rajani applied the tests. The products cost three times similar ones in shops, so almost nobody would buy them except new members; the presentation spent 5 minutes on products and 50 on recruitment; and the "income proof" was screenshots, not tax returns. Under the 2021 Direct Selling Rules, a scheme like that, which depends on recruitment, is the kind of pyramid structure direct sellers are banned from promoting.

Rajani didn't join. Two of her friends did and lost most of their ₹25,000 in unsold products within a year. "The meeting felt like a celebration," Rajani said. "That was the trick."
""",
    resources=[
        ('sebi-investor', 'SEBI\'s warnings on fake trading apps, "stock market guru" scams, pump and dump and dabba trading', '20 minutes'),
        ('ml-mlm', 'What the 2021 Direct Selling Rules prohibit', '10 minutes'),
        ('sachet', 'RBI Sachet: registered entities and how to complain', '10 minutes'),
        ('sebi-ia-list', 'Practise searching the SEBI adviser list', '10 minutes'),
        ('ncfe', 'The e-LMS module on scams and frauds', '15 minutes'),
    ],
    steps=[
        'Do the spot-the-scam exercise in the template: for each message, write "scam" or "not a scam" and the red flags, before reading the answers.',
        'List every investment offer, group or "opportunity" you or your family have been approached with in the last year.',
        'Run the five questions on each, and check the regulator\'s register where relevant (SEBI list, RBI Sachet).',
        'Leave or report any group that gives paid tips without registration.',
        'Write your personal investment-scam rule in one sentence.',
    ],
    proof='Your answers to the spot-the-scam exercise, the five-question check of real offers and your rule, saved in 15 Scams.',
    templates=[
        ('spot the scam (cover the answers, then check)', '\n'.join(f'{k}. {m}\n   Answer: {a}' for k, m, a in SCAM_MESSAGES), ''),
        ('five-question investment check', """
Offer: ____  From: ____
1. Regulator and registration number (checked myself): ____
2. How it makes money, in two sentences: ____
3. Returns promised? Yes / No (if yes: walk away)
4. How I get my money out, and test result: ____
5. Who benefits if I say yes today? ____
Decision: ____
""", ''),
    ],
    mistakes=[
        ('Trusting because a relative or friend invested.', 'Ponzi schemes spread through trust; early payouts are bait. Check the regulator, not the person.'),
        ('Believing screenshots of profits.', 'Screenshots are easy to fake and never show the losers.'),
        ('Paying a "withdrawal fee" to get money out.', 'Real platforms don\'t ask for fees to release your own money. Stop and report.'),
        ('Staying silent after a loss.', 'Report quickly; it helps police stop the scheme and protects others.'),
    ],
    quiz=[
        {'q': 'A scheme pays 3% a month, guaranteed, plus bonuses for recruits. What is it most likely to be?', 'o': ['A Ponzi scheme', 'A government bond', 'A bank FD', 'An index fund'], 'a': 'A', 'why': 'High guaranteed returns and recruitment rewards are the classic pattern.'},
        {'q': 'Under the 2021 Direct Selling Rules, what can\'t direct sellers do?', 'o': ['Promote pyramid or money circulation schemes', 'Sell products', 'Give receipts', 'Have customers'], 'a': 'A', 'why': 'Selling real products is allowed; recruitment-driven schemes are not.'},
        {'q': 'An app shows big profits but asks for a "tax" before you can withdraw. What should you do?', 'o': ['Stop paying and report it', 'Pay quickly before profits disappear', 'Borrow to pay the fee', 'Recruit friends to cover it'], 'a': 'A', 'why': 'This is how fake trading apps take more money.'},
        {'q': 'How can you check whether someone giving paid stock advice is genuine?', 'o': ['Search SEBI\'s list of registered investment advisers', 'Count their followers', 'Ask for profit screenshots', 'Trust their certificate photo'], 'a': 'A', 'why': 'Registration on SEBI\'s list is the test.'},
    ],
    study='SEBI\'s fraud warnings, the Direct Selling Rules, RBI Sachet, the SEBI adviser list and the NCFE scams module',
    action='Do the spot-the-scam exercise and check real offers with the five questions and official registers',
)

L2 = lesson(
    M, 2,
    title='Payment frauds: UPI and OTP tricks, phishing and "digital arrest"',
    weeks=(28, 28), hours=2,
    outcome='Recognise the main payment frauds in India, including "digital arrest", and set up habits and settings that stop them, for yourself and your family.',
    split='30 minutes reading, 25 minutes resources, 65 minutes action',
    core=f"""
Payment fraudsters rarely hack anything. They **persuade you** to send money, approve a request, share a code or install an app. The script changes; the tricks stay the same: **urgency, fear, authority, greed and kindness**.

### Common frauds and the truth that defeats each

{table(['The trick', 'What they say', 'The truth'], [
    ('Fake KYC update', '"Your account/SIM/electricity will be blocked today. Update KYC at this link."', 'Banks and utilities never ask through links from unknown numbers. Use the official app or office.'),
    ('"Refund" by QR or UPI request', '"Scan this QR to receive your refund."', 'Scanning a QR or entering your PIN only sends money. You never need your PIN to receive.'),
    ('Fake customer care', 'A number found by search or social media', 'Use only numbers from the official website, app or passbook.'),
    ('Remote access apps', '"Install this app so I can help you."', 'Screen-sharing lets them see your OTPs and apps. Never install apps on a caller\'s instruction.'),
    ('APK files on WhatsApp', '"Traffic fine", "wedding invitation", "bank update" as an .apk file', 'Never install app files from messages; only from the official app store.'),
    ('Task and job scams', '"Earn by liking videos or rating hotels. Deposit to unlock higher tasks."', 'Real jobs don\'t ask you to pay. Small early payouts are bait.'),
    ('Marketplace scams', 'A "buyer" or "army officer" sends a QR to "pay you"', 'QR codes are for paying, not receiving.'),
    ('SIM swap', 'Your phone suddenly loses network', 'Contact your mobile operator immediately; someone may be getting your OTPs.'),
])}

### "Digital arrest"

In a **digital arrest** fraud, callers pretend to be from the CBI, police, customs, ED or even judges, often by video call with uniforms and fake offices. They claim you or a relative are linked to drugs or money laundering, keep you on camera "under arrest" for hours, and demand money transfers to "clear your name". India's Indian Cyber Crime Coordination Centre (I4C) issued an advisory: **"CBI/Police/Custom/ED/Judges DO NOT arrest you on video call"**; don't panic, and report on **1930** or **cybercrime.gov.in** ({link('etv-arrest', 'ETV Bharat, October 2024')}).

**There is no such thing as a digital arrest in Indian law.** Hang up, and call a family member and 1930.

### Report attempts before any loss: Chakshu

If you receive a suspicious call, SMS or WhatsApp message but **haven't lost money**, you can report it on **Chakshu**, a facility on the Department of Telecommunications' Sanchar Saathi portal, which acts against numbers used for fraud. If money has already gone, use **1930** or the cyber crime portal instead ({link('chakshu', 'Factly')}).

### Settings and habits that block most frauds

1. **A separate, low-balance account for UPI:** keep most money in an account that isn't linked to UPI apps.
2. **Transaction alerts on** (Module 4), and a **daily UPI limit** that fits your needs.
3. **Two-step verification** on email and important apps; a screen lock; app locks on payment apps.
4. **Type addresses yourself:** bank websites end in **.bank.in** ({link('bs-bankin', 'Business Standard headline')}).
5. **Pause and verify:** any message with urgency, fear or a prize gets a 10-minute pause and a call to an official number or a family member.
6. **Never share** OTPs, PINs, passwords or CVVs, with anyone.
""",
    example=f"""
**Joseph**, Anu's neighbour, got a video call from a "Mumbai Police officer" who said a parcel in Joseph's name contained drugs and that a "CBI judge" would decide his case online. Joseph was told not to tell anyone and to stay on camera. After an hour of fear, the "officer" asked him to transfer his FD money to a "verification account" that would be returned after the inquiry.

Joseph remembered the fraud response card on his kitchen cupboard (FIN-M04-L02): 1930. He said he needed the bathroom, called his daughter from the landline, and she told him what the I4C advisory says: real agencies don't arrest people on video calls. He hung up. Then they reported the number on Chakshu, because no money had been lost.

His daughter later set up two protections: his FD account is no longer linked to any UPI app, and his UPI account holds only his monthly expenses.
""",
    resources=[
        ('etv-arrest', 'I4C\'s "digital arrest" advisory', '10 minutes'),
        ('chakshu', 'What Chakshu is for, and when to use 1930 instead', '10 minutes'),
        ('rbi-liability', 'Revise your rights after an unauthorised transaction', '10 minutes'),
        ('rbi-fe', 'RBI\'s Financial Awareness Messages on safe digital banking', '15 minutes'),
    ],
    steps=[
        'Check your payment set-up: which accounts are linked to UPI apps? Consider keeping savings in an account that isn\'t.',
        'Set or lower your daily UPI limit in your bank app or UPI app.',
        'Check two-step verification on your email and screen locks on your phone; turn them on if off.',
        'Fill in the scam-proof habits checklist for yourself.',
        'Teach one family member (ideally an older one) the "digital arrest" truth and the 10-minute pause, and write what you discussed.',
    ],
    proof='Your completed scam-proof habits checklist, a screenshot of your UPI limit or account set-up (numbers covered) and a note on the family conversation, saved in 15 Scams.',
    templates=[
        ('scam-proof habits checklist', """
[ ] Savings kept in an account not linked to any UPI app
[ ] Daily UPI limit set to what I really need: ₹____
[ ] Transaction alerts (SMS and email) on for every account
[ ] Two-step verification on email and important apps
[ ] Screen lock and app locks on
[ ] I never install apps or .apk files because a caller or message tells me to
[ ] I never scan a QR code or enter a PIN to "receive" money
[ ] I find customer care numbers only on official websites, apps or passbooks
[ ] I pause 10 minutes and verify when a message has urgency, fear or a prize
[ ] I know: no agency arrests anyone on a video call
[ ] I know: 1930 and cybercrime.gov.in if money is lost; Chakshu for attempts
""", ''),
    ],
    mistakes=[
        ('Thinking frauds only target the careless.', 'They target fear and kindness. Habits and settings protect you when emotions run high.'),
        ('Keeping all savings in the UPI-linked account.', 'A low-balance UPI account limits the damage of any mistake.'),
        ('Engaging with scammers to "teach them a lesson".', 'Hang up and report; they are skilled at pulling you back in.'),
        ('Not telling elderly family members.', 'Older people are targeted most; a 10-minute conversation can save their savings.'),
    ],
    quiz=[
        {'q': 'A video caller in police uniform says you are under "digital arrest". What is true?', 'o': ['No agency arrests anyone on a video call; hang up and call 1930', 'You must stay on camera', 'You should transfer money for verification', 'You need a lawyer on the call'], 'a': 'A', 'why': 'The I4C advisory says CBI, police, customs, ED and judges don\'t arrest people on video calls.'},
        {'q': 'You got a suspicious SMS but lost no money. Where can you report it?', 'o': ['Chakshu on the Sanchar Saathi portal', 'Nowhere', 'Only the bank', 'The income tax portal'], 'a': 'A', 'why': 'Chakshu is for suspected fraud communications; 1930 is for money already lost.'},
        {'q': 'A "buyer" sends you a QR code to pay you for your old phone. What should you do?', 'o': ['Refuse; QR codes are for paying, not receiving', 'Scan it and enter your PIN', 'Send your OTP', 'Install their app'], 'a': 'A', 'why': 'Scanning and entering a PIN sends your money out.'},
        {'q': 'Which set-up limits damage from payment fraud?', 'o': ['A separate low-balance account for UPI, with a daily limit', 'All savings in the UPI account', 'Alerts turned off', 'Sharing your PIN with family'], 'a': 'A', 'why': 'If something goes wrong, only a small amount is exposed.'},
    ],
    study='The I4C digital arrest advisory, Chakshu, your liability rights and RBI\'s awareness messages',
    action='Lock down your payment set-up, complete the habits checklist and brief one family member',
)

L3 = lesson(
    M, 3,
    title='Report fast, recover what you can, and protect your family',
    weeks=(29, 29), hours=1.5,
    outcome='Know exactly where to report each kind of fraud, keep the evidence that helps, avoid "recovery" scams, and run a family scam briefing.',
    split='20 minutes reading, 20 minutes resources, 50 minutes action',
    core=f"""
### Where to report what

{table(['What happened', 'Report to', 'Why'], [
    ('Money lost through UPI, card, net banking or an online fraud', '**1930** (24 hours) and **cybercrime.gov.in**; then block and report to your bank in writing', 'Fast reports give the best chance to freeze money in the fraudster\'s account; your bank liability depends on how fast you report (FIN-M04-L02)'),
    ('A suspicious call, SMS or WhatsApp message, no money lost', '**Chakshu** on the Sanchar Saathi portal', 'Helps block numbers used for fraud'),
    ('A company taking deposits illegally, a Ponzi or chit fraud', '**RBI Sachet** complaint and the police', 'Brings regulators and state authorities in'),
    ('A problem with a SEBI-registered broker, adviser or fund', '**SEBI SCORES**, after complaining to the entity', 'The entity must respond within 21 days'),
    ('A bank or NBFC doesn\'t resolve your complaint', '**RBI Ombudsman** (cms.rbi.org.in)', 'Free, after 30 days or a rejection'),
    ('An insurance problem', '**Bima Bharosa**, then the **Insurance Ombudsman**', 'Free escalation (FIN-M07-L05)'),
    ('Threats, harassment, large losses', '**Police station** (FIR) as well as the above', 'For investigation and legal action'),
])}

Sources: {link('kp-1930', 'Kerala Police on 1930')}, {link('cybercrime', 'National Cyber Crime Reporting Portal')}, {link('chakshu', 'Chakshu')}, {link('sachet', 'RBI Sachet')}, {link('scores', 'SEBI SCORES')}, {link('rbi-ios', 'RBI Ombudsman scheme')}, {link('bima-bharosa', 'Bima Bharosa')}.

### The first hour: speed beats everything

Kerala Police says reporting online financial scams promptly is crucial, so that investigators can gather evidence and act before it is destroyed ({link('kp-1930', 'Kerala Police')}). Call 1930 first, then block your card or UPI, then file online and in writing.

### Evidence to keep

- Screenshots of messages, chats, call logs, profiles, websites and apps (with the URL)
- Transaction IDs (UTR numbers), dates, amounts, the receiver's UPI ID or account
- Any names, numbers and links the fraudster used
- Your complaint and acknowledgement numbers

Don't delete chats in anger or shame; they are evidence.

### Recovery scams: the second fraud

After a loss, victims are often contacted by "recovery agents", "cyber lawyers" or even fake police officers who promise to get the money back for a fee. Genuine police and regulators don't charge for investigations. Anyone asking for a fee to recover lost money is almost certainly running a second scam.

### Shame is the fraudster's best friend

Victims often stay silent, which lets frauds continue and stops recovery. Fraud happens to doctors, engineers, bank staff and police officers. Tell your family, report, and use your experience to warn others.

### A family scam briefing

Once a year, or whenever a new scam is in the news, spend 20 minutes with your family:

1. Share the three rules: **never share codes, never install apps for callers, never pay to "receive" or "recover" money**.
2. Explain "digital arrest" and the five-question investment check.
3. Agree a **family code**: anyone who gets a scary call or a "great scheme" calls a named family member before doing anything.
4. Put the fraud response card and 1930 where everyone can see them.
""",
    example=f"""
**Fathima** lost ₹18,000 when she paid an advance to a fake "furniture supplier" she found on social media. She noticed within an hour, when the seller's profile vanished.

She called **1930** at once and gave the UTR number and the receiver's UPI ID; the call centre registered her complaint and asked her to complete it on the cyber crime portal, which she did within the hour. She reported the transaction to her bank in writing. Some days later, the police informed her that part of the money had been frozen in the receiving account; she received ₹11,000 back through the process the police and bank followed.

Two days after her loss, a "cyber recovery expert" messaged her offering to recover the rest for a ₹3,000 fee. She recognised the second scam, reported the number on Chakshu, and told the story at her family's next briefing so her cousins wouldn't fall for either trick.
""",
    resources=[
        ('kp-1930', 'Kerala Police on the 1930 helpline and prompt reporting', '5 minutes'),
        ('chakshu', 'When to use Chakshu and when to use 1930', '5 minutes'),
        ('sachet', 'Filing a complaint on RBI Sachet', '10 minutes'),
        ('scores', 'How SEBI SCORES works', '10 minutes'),
        ('ncfe', 'Finish the NCFE scams and frauds module and its quiz', '15 minutes'),
    ],
    steps=[
        'Save 1930 in your phone as "Cyber Fraud Helpline" and bookmark the official portals from this lesson.',
        'Make a **Scam Check** tab with the incident log template, ready to use.',
        'Write your family code: who family members should call before acting on a scary call or a "scheme".',
        'Hold a 20-minute family scam briefing using the four points, and write who attended and what questions came up.',
        'Put the fraud response card and 1930 in a visible place at home.',
    ],
    proof='The incident log ready in your Scam Check tab, your family code and notes from the family briefing, saved in 15 Scams.',
    templates=[
        ('incident log (fill in immediately if something happens)', """
Date and time noticed: ____
What happened (short): ____
Amount and transaction IDs (UTR): ____
Receiver's UPI ID / account / phone / website: ____
1930 called at (time): ____  Complaint number: ____
cybercrime.gov.in acknowledgement: ____
Bank informed at (time, how): ____  Card/UPI blocked: Yes / No
Other reports (Chakshu, Sachet, SCORES, police FIR): ____
Evidence saved (screenshots folder): ____
Follow-up dates: ____
""", ''),
        ('family scam briefing card', """
OUR FAMILY RULES
1. We never share OTPs, PINs or passwords. With anyone.
2. We never install apps or files because a caller or message says so.
3. We never pay to receive money, release profits or recover losses.
4. No agency arrests anyone on a video call.
5. Before acting on a scary call or a "great scheme", call: ____ (family code person)
LOST MONEY? Call 1930 at once, then the bank. Report at cybercrime.gov.in.
""", ''),
    ],
    mistakes=[
        ('Waiting before reporting.', 'Every hour matters for freezing money. Call 1930 first.'),
        ('Deleting chats out of shame.', 'They are the evidence investigators need.'),
        ('Paying "recovery agents".', 'It is a second scam. Real investigations don\'t charge you.'),
        ('Briefing family only once.', 'Scams change; repeat the briefing yearly and when new tricks appear.'),
    ],
    quiz=[
        {'q': 'You lost money through a UPI fraud an hour ago. What is the first step?', 'o': ['Call 1930', 'Wait a day to see if it comes back', 'Post on social media', 'Pay a recovery agent'], 'a': 'A', 'why': 'Fast reporting gives the best chance of freezing the money.'},
        {'q': 'A company in your town takes deposits promising 3% a month. Where can you complain?', 'o': ['RBI Sachet and the police', 'SEBI SCORES only', 'Bima Bharosa', 'Nowhere'], 'a': 'A', 'why': 'Sachet handles complaints about illegal deposit-taking; police can act too.'},
        {'q': 'Someone offers to recover your lost money for a fee. What is it most likely to be?', 'o': ['A second scam', 'The police', 'A bank refund', 'A legal requirement'], 'a': 'A', 'why': 'Genuine investigations don\'t charge victims.'},
        {'q': 'Which evidence is most useful after a payment fraud?', 'o': ['Transaction IDs (UTR), the receiver\'s UPI ID or account, screenshots', 'Only your memory', 'Your credit score', 'Your PAN card'], 'a': 'A', 'why': 'Investigators trace money through transaction details.'},
    ],
    study='The 1930 helpline, Chakshu, RBI Sachet, SEBI SCORES and the NCFE scams module',
    action='Prepare your incident log, write a family code and hold a family scam briefing',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    M,
    title='Scams and fraud protection',
    weeks=(28, 29), hours=6.5,
    overview="""
Recognise investment and payment scams before they reach your money, set up habits and settings that block them, and know exactly where to report if something goes wrong.

Everything else in this course can be undone in one afternoon by a fraud: a "guaranteed" scheme, a fake trading app, a QR code "to receive a refund", or a video call from a fake police officer. Kerala has seen large investment frauds, and payment frauds reach every family with a phone.

This module teaches the patterns behind the tricks (urgency, fear, authority, greed and kindness), the official registers you can check yourself (SEBI, RBI Sachet), the I4C advisory on "digital arrest", and the reporting routes: 1930, the cyber crime portal, Chakshu, Sachet, SCORES and the ombudsmen. Your **scam-proof habits** and a family briefing become part of your final plan.
""",
    outcomes=[
        'Recognise Ponzi schemes, pyramid MLMs, fake trading apps and unregistered tipsters',
        'Check any investment offer against official registers',
        'Recognise payment frauds, including "digital arrest", and set up protective settings',
        'Report each kind of fraud to the right place, fast, with evidence',
        'Brief your family and agree a family code',
    ],
    lessons=LESSONS,
    project='My scam-proof habits and family briefing',
    project_steps=[
        'Complete the scam-proof habits checklist with every item ticked or a date to fix it.',
        'Make sure your payment set-up limits damage: a low-balance UPI account and a daily limit.',
        'Keep the incident log and reporting routes ready in your Scam Check tab.',
        'Hold the family scam briefing and agree the family code.',
        'Add "family scam briefing" to your yearly review.',
    ],
    project_proof='Your completed checklist, the incident log template ready, the family code and briefing notes, saved in 15 Scams.',
    rubric=[
        ('Investment scams', 'Can\'t spot them', 'Knows some signs', 'Applies the five questions and checks registers'),
        ('Payment frauds', 'Unaware', 'Knows the common tricks', 'Settings and habits in place, including UPI limits'),
        ('Digital arrest', 'Unaware', 'Has heard of it', 'Can explain it and has briefed a family member'),
        ('Reporting', 'Doesn\'t know where', 'Knows 1930', 'Knows every route and has the incident log ready'),
        ('Family', 'Not discussed', 'One person told', 'Briefing held and a family code agreed'),
    ],
    short=[
        'Save 1930 and the fraud response card (FIN-M15-L03).',
        'Set a daily UPI limit and keep savings in a non-UPI account (FIN-M15-L02).',
        'Teach one older family member about "digital arrest".',
    ],
    flashcards=[
        ('Ponzi pattern', 'High "guaranteed" returns paid from new investors\' money, plus rewards for recruiting.'),
        ('Pyramid vs real direct selling', 'Pyramid: income from recruiting. Real: income from selling products to customers.'),
        ('Fake trading app sign', 'Big profits you can\'t withdraw without paying a "fee" or "tax".'),
        ('Digital arrest', 'Not real: CBI, police, customs, ED and judges don\'t arrest anyone on video calls.'),
        ('Lost money?', 'Call 1930, block with the bank, report at cybercrime.gov.in.'),
        ('Suspicious call or SMS, no loss?', 'Report it on Chakshu (Sanchar Saathi).'),
        ('Illegal deposit scheme?', 'Complain on RBI Sachet and to the police.'),
        ('Recovery agent asking a fee', 'A second scam.'),
    ],
    mistakes=[
        ('Believing "it won\'t happen to me".', 'Frauds succeed through emotion, not ignorance. Habits protect everyone.'),
        ('Keeping quiet after a loss.', 'Report fast and tell family; silence helps the fraudster.'),
        ('Protecting only yourself.', 'Parents, grandparents and teenagers are targeted too. Brief them.'),
    ],
    project_week=29,
)
