from common import lesson, module, link, xref, table, fence, Q, CHECK
import tools

L1 = lesson(
    32, 1,
    outcome='You can recognise high-pressure sales tactics and MLM recruitment tactics, explain the psychology behind them, and use a script to leave without buying.',
    split='20 minutes reading, 30 minutes of tasks',
    principle='High-pressure sellers and MLM recruiters turn the normal principles of influence into traps: rush you, isolate you, flatter you and sell you a dream; slowing down, involving others and checking the numbers defeats them.',
    science=f"""
This lesson covers manipulation **only so you can recognise and resist it.**

**High-pressure sales tactics** use the influence principles from Module 28, but dishonestly:
- **False urgency and scarcity:** "This price is only for today", "Only two left", countdown timers.
- **Reciprocity traps:** free gifts, free meals or "free health check-ups" followed by a pitch you feel obliged to accept.
- **Commitment traps (foot-in-the-door):** "Just sign this form to see if you qualify" → "You qualify! Just the first payment now."
- **Authority theatre:** suits, certificates, "senior consultant", hospital-style uniforms, fake testimonials from "doctors".
- **Liking and flattery:** a seller who suddenly becomes your "brother" or "sister".
- **Isolation:** "Decide now, don't ask your family; they won't understand."
- **Fear:** "Without this policy, your family will be on the street."
- **Door-in-the-face:** an absurdly expensive option first so the second seems reasonable.
These tactics work because they push decisions into **fast thinking** (PD-M01-L01) under emotion and time pressure.

**Multi-level marketing (MLM).** In an MLM, people buy products to sell and earn commissions on sales by people they **recruit** ("downline"). The business model is legal in many countries if income comes mainly from real retail sales to customers, but it becomes a **pyramid scheme** (illegal in India) when income comes mainly from recruiting and from recruits' own purchases. Reviews of MLM income disclosures, for example by the US Federal Trade Commission, have found that **most participants earn little or nothing** after costs. India regulates direct selling through the Consumer Protection (Direct Selling) Rules, 2021, which prohibit pyramid schemes and money-circulation schemes ({CHECK}).

**MLM recruitment psychology:**
- **The dream:** luxury cars, foreign trips, "be your own boss", "passive income".
- **Social proof from the top:** stage events with a few high earners (survivorship bias: you don't see the thousands who lost money).
- **Unity and liking:** recruitment through friends, relatives and religious or community groups; loyalty makes refusal feel like betrayal.
- **Sunk cost:** "You've already invested ₹30,000; quitting now means losing it."
- **Blame:** "If you're not earning, you're not working hard enough / you have a poor-person mindset."

**The defence:** slow down, take the decision out of the room, involve someone you trust, ask for written numbers, and remember that a genuine offer will still be there tomorrow. The {xref('fin', 'fin-m15', 'Personal Finance scams module')} covers financial fraud in detail.
""",
    evidence=[
        ('Time pressure and emotion push people into fast, worse decisions', 'strong', 'Consistent with decision research.'),
        ('Free gifts create a sense of obligation', 'strong', 'Reciprocity research.'),
        ('Most MLM participants earn little or nothing after costs', 'moderate', 'Supported by income disclosures and regulator reviews.'),
        ('Survivorship bias in success stories', 'strong', 'A basic statistical error, widely documented.'),
        ('Taking decisions out of the room protects people', 'tool', 'Practical defence consistent with decision research.'),
    ],
    example="""
Vinod's old classmate Sanju invites him for "a quick tea to discuss a business opportunity". At the hotel, a smartly dressed "diamond director" shows photos of foreign trips and a car. "You just need to buy the ₹35,000 starter kit and bring in two people. They bring two each… In six months you'll earn ₹50,000 a month. But the launch offer ends tonight."

Vinod notices the tactics: **unity** (old classmate), **authority theatre** (the title, the suit), **the dream**, **false urgency** ("ends tonight"), and a focus on **recruiting** rather than selling to customers. He uses his script: "Thanks for explaining. I never decide on money the same day. Please give me the income disclosure and the company's registration details in writing; I'll discuss it with my family and reply this week." The director says the offer won't be there tomorrow. Vinod says, "Then it's not for me," and leaves.

At home he searches the company and finds complaints from people who bought kits and couldn't sell them. He messages Sanju kindly: "I'm not joining, but I hope it goes well for you. If you ever want to talk about getting your money back, I'll help."
""",
    apply=f"""
**The leave-without-buying script:**
1. **Pause the decision:** "I never decide on money the same day."
2. **Ask for it in writing:** "Please give me the price, terms, cancellation policy (and for MLMs, the income disclosure and registration) in writing."
3. **Involve others:** "I'll discuss it with my family."
4. **Leave:** "If the offer won't be there tomorrow, then it's not for me. Thank you."
5. **Don't give:** OTPs, bank details, signatures or advance payments on the spot.

**MLM questions to ask:**
- What share of income comes from **retail sales to non-members** versus recruiting?
- What did the **median** participant earn last year, after costs?
- What is the buy-back policy for unsold stock?
- Is the company registered and compliant with India's direct-selling rules?
If you can't get clear written answers, walk away.

**Red-flag check (use on any pitch):**
{fence(tools.MANIPULATION_CHECK)}

**With others:** if a friend is in an MLM, avoid mocking them (shame keeps people in). Ask the questions above with curiosity, and offer help if they want out.
""",
    resources=[
        ('os-12', 'Re-read the compliance techniques in 12.4 (foot-in-the-door, door-in-the-face, low-balling)', '10 minutes'),
        ('darkpatterns', 'Read the list of 13 dark patterns; the same tactics appear in face-to-face sales', '10 minutes'),
        ('wp-cialdini', 'Re-read the seven principles and think about how each can be abused', '5 minutes'),
    ],
    steps=[
        'Collect three real high-pressure pitches (a sales call, a shop, an online ad, an MLM message, an insurance pitch) and analyse each with the red-flag check.',
        'Write your leave-without-buying script in English and Malayalam.',
        'Practise saying it aloud three times. If a real pitch comes this week, use it and note what happened.',
        'Write the four MLM questions on your phone so you have them ready.',
    ],
    proof='Three analysed pitches with red flags ticked, your script in two languages, and (if it happened) a note of using it.',
    templates=[('Pitch analysis', """PITCH ANALYSIS           Date ______  Where ______  Product/offer ______
Red flags (tick): urgency / free-gift pressure / small-step trap / authority theatre /
  sudden friendliness / isolation ("don't ask family") / fear / huge first price /
  recruitment focus / income dreams / sunk-cost pressure
Influence principle(s) abused: ______
What they wanted me to do: ______  What I did: ______
MY SCRIPT: "I never decide on money the same day. Please give me ______ in writing.
I'll discuss it with my family. If the offer won't be there tomorrow, it's not for me." """, '')],
    mistakes=[
        ('Thinking "I\'m too smart to be fooled".', 'Pressure tactics work on intelligent people. Use the script, not confidence.'),
        ('Deciding at the event or on the call.', 'Always take the decision out of the room.'),
        ('Believing stage testimonials.', 'They are the survivors. Ask for median earnings.'),
        ('Shaming friends in MLMs.', 'Shame keeps people in. Ask questions and offer help.'),
    ],
    quiz=[
        Q('What turns an MLM into an illegal pyramid scheme?', 'Income comes mainly from recruiting and recruits\' own purchases rather than retail sales', 'Selling products door to door', 'Having more than 100 members', 'Selling online', why='Recruitment-driven income is the key sign.'),
        Q('Why do sellers say "this offer ends tonight"?', 'To push you into a fast, emotional decision', 'Because offers always end', 'To be helpful', 'Because of government rules', why='False urgency stops careful thinking.'),
        Q('What is the best first step when facing a high-pressure pitch?', 'Pause the decision: "I never decide on money the same day"', 'Sign quickly before the price rises', 'Share your OTP to check eligibility', 'Ask the seller if it is a good deal', why='Taking the decision out of the room defeats pressure.'),
        Q('Why are stage success stories misleading in MLMs?', 'Survivorship bias: you only see the few who succeeded', 'They are always fake', 'Successful people never speak', 'They are illegal', why='The many who lost money aren\'t on stage.'),
    ],
    study='read the lesson and re-read the compliance techniques in OpenStax 12.4',
    action='analyse three real pitches with the red-flag check and practise your leave-without-buying script',
)

L2 = lesson(
    32, 2,
    outcome='You can explain the psychology of scams (including "digital arrest" and phishing), spot dark patterns in apps, and know exactly what to do if you or a relative is targeted.',
    split='25 minutes reading, 35 minutes of tasks',
    principle='Scams work by creating fear, greed or urgency so you act before you think; real officials and banks never ask for OTPs, payments or "video arrests", and the fix is always: stop, hang up, verify independently, report.',
    science=f"""
**Scam psychology.** Researchers who study fraud (for example, Stephen Lea, Peter Fischer and Kath Evans in a report for the UK Office of Fair Trading, 2009) found that scams exploit predictable weak points: **authority** (pretending to be police, a bank, a government department), **urgency and scarcity**, **social proof**, **reciprocity**, **commitment** (small steps leading to bigger payments), **fear** and **greed or hope** (prizes, jobs, returns). Many scams also use **isolation** ("don't tell anyone, this is confidential"). Emotion narrows attention and pushes fast thinking (PD-M01-L01). Anyone can be targeted; victims are not stupid, they are **targeted when stressed, lonely, hopeful or frightened**.

**"Digital arrest" scams.** In India, criminals impersonate CBI, ED, police, customs or courts on video calls, claim a parcel with drugs or a bank account is linked to you, say you are under "digital arrest", keep you on the call for hours, and demand money to "clear your name". **There is no such thing as a digital arrest.** Real agencies do not arrest people over video calls or ask for money transfers. The Ministry of Home Affairs told Parliament in March 2025 that the Indian Cyber Crime Coordination Centre (I4C) had blocked over 3,962 Skype IDs and 83,668 WhatsApp accounts used for digital-arrest fraud ({link('pib-cyber', 'PIB, 12 March 2025')}).

**Other common scams in Kerala and India:** fake job offers (often "work from home" tasks, "like YouTube videos and earn", or overseas jobs needing a "processing fee"); fake PSC or government-job "agents" promising posts for money; investment and crypto "groups" on WhatsApp or Telegram; KYC update or electricity-bill disconnection SMS with links; UPI "collect requests" disguised as payments ("enter your PIN to receive money"; you never need your PIN to receive); loan apps with hidden fees and harassment; lottery and prize messages; sextortion; and impersonation of relatives ("I'm in trouble, send money").

**What to do:**
- **Stop:** hang up, don't click, don't pay, never share an **OTP, PIN, CVV or password**.
- **Verify independently:** call the bank or office on a number **you look up yourself** (official website, back of your card), not the one given.
- **Talk to someone** you trust before acting.
- **Report quickly:** the national cyber-crime helpline **1930** and the National Cyber Crime Reporting Portal (cybercrime.gov.in) are run under I4C for reporting cyber fraud; reporting quickly after money is lost improves the chance of freezing it ({link('pib-cyber', 'PIB')}; the portal blocks automated checks, so type the address yourself).

**Dark patterns.** In November 2023 India's Central Consumer Protection Authority notified guidelines listing **13 dark patterns** in apps and websites ({link('darkpatterns', 'summary')}): false urgency, basket sneaking (items added without consent), confirm shaming ("No thanks, I don't want to save money"), forced action, subscription traps, interface interference, bait and switch, drip pricing (hidden charges added late), disguised advertisements, nagging, trick questions, SaaS billing and rogue malware. Knowing the names helps you spot them.
""",
    evidence=[
        ('Scams exploit authority, urgency, fear, greed and isolation', 'strong', 'Consistent findings from fraud research and police data.'),
        ('Emotional states increase vulnerability to scams', 'moderate', 'Supported by fraud-victim research.'),
        ('Verifying independently and talking to others prevents losses', 'tool', 'Standard advice from banks, police and regulators.'),
        ('Quick reporting improves the chance of freezing money', 'moderate', 'Stated by Indian authorities about the 1930 system.'),
        ('India\'s 13 specified dark patterns', 'strong', 'Official CCPA guidelines (2023).'),
    ],
    example="""
Anu's father, 62, gets a video call from a man in a police uniform, with a "Mumbai Cyber Crime" background. "A parcel in your name contains drugs and passports. You are under digital arrest. Don't disconnect or tell anyone. Transfer ₹2,40,000 to this RBI verification account to prove your innocence."

Her father is terrified and starts opening his banking app. Anu, home that afternoon, sees his face and recognises the pattern: **authority** (uniform, logo), **fear**, **urgency**, **isolation** ("don't tell anyone") and a request for **money**. She says calmly, "Achan, there is no digital arrest. Hang up." He hangs up. She calls **1930** to report the number and helps him file a complaint on the cyber-crime portal. They save the screenshots.

The next week, Anu runs a 20-minute session for her family WhatsApp group, sharing a one-page list: "No police arrest on video calls. No bank asks for OTP. No PIN to receive money. Hang up, verify, call 1930." Two relatives say they had received similar calls.
""",
    apply=f"""
**The scam rule (teach it to your family):**
{fence('''STOP - HANG UP - VERIFY - TALK - REPORT
1. No real police, CBI, ED, court or customs officer arrests anyone on a video call
   or asks for money. "Digital arrest" does not exist.
2. No bank, RBI, PSC, KSEB or government office asks for your OTP, PIN, CVV or password.
3. You NEVER enter a UPI PIN to RECEIVE money.
4. Real jobs (and real PSC posts) never require a "processing fee" or an agent's payment.
5. Guaranteed high returns = scam.
6. Verify on a number YOU look up (official website, back of your card).
7. Talk to someone you trust before paying anything.
8. Money lost? Call 1930 IMMEDIATELY and report at cybercrime.gov.in.
   Also inform your bank to block the card or account.''')}

**Dark-pattern spotting:** when using shopping, food-delivery, travel and subscription apps, look for the 13 patterns. At checkout, check the final price, untick add-ons, and read what you are agreeing to. Cancel unwanted subscriptions immediately after a free trial starts if you don't want to keep it.

**With others:** older relatives and teenagers are frequent targets. Share the rule calmly, practise "hang up and verify", and make it safe for them to tell you if they've been caught: shame stops people from reporting.
""",
    resources=[
        ('pib-cyber', 'Read the release: digital-arrest action, the 1930 helpline and the reporting portal', '10 minutes'),
        ('darkpatterns', 'Read the 13 dark patterns with their meanings', '15 minutes'),
        ('cybercrime', 'Type the address yourself and look at the reporting options; note the steps for financial fraud', '10 minutes'),
    ],
    steps=[
        'Collect five real scam or suspicious messages (SMS, WhatsApp, email, calls) from your phone or family\'s phones. Analyse each with the red-flag check and name the scam type.',
        'Open three apps you use (shopping, food delivery, a subscription) and find at least three dark patterns. Screenshot and name them.',
        'Save 1930 in your phone and in one older relative\'s phone.',
        'Teach the scam rule to at least two family members, and note their questions.',
    ],
    proof='Five analysed scam messages, three named dark-pattern screenshots, saved 1930 contacts and a note on teaching two family members.',
    templates=[('Manipulation-spotting file', tools.MANIPULATION_CHECK + """

MANIPULATION-SPOTTING FILE
Date | Source (SMS / WhatsApp / call / app / ad) | Type (digital arrest / KYC / job / investment /
  prize / loan app / impersonation / dark pattern: which) | Red flags | Principle abused | Action taken""", '')],
    mistakes=[
        ('Staying on the call to "explain".', 'Hang up. Scammers are trained to keep you talking.'),
        ('Using numbers or links in the message to verify.', 'Look up the official number yourself.'),
        ('Feeling too ashamed to report.', 'Report immediately; speed matters, and you are a victim of crime.'),
        ('Thinking only old or uneducated people are scammed.', 'Anyone can be targeted, especially when stressed or hopeful.'),
    ],
    quiz=[
        Q('A caller on video says you are under "digital arrest" and must transfer money. What is true?', 'There is no such thing as a digital arrest; hang up and report', 'You must stay on the call', 'Pay and then complain', 'It is real if they wear a uniform', why='Real agencies do not arrest over video calls or demand transfers.'),
        Q('When do you need to enter your UPI PIN?', 'Only to send money, never to receive it', 'To receive money', 'To check your balance with a stranger', 'Whenever someone asks', why='A PIN request to "receive" money is a scam.'),
        Q('What is the national cyber-crime helpline number in India?', '1930', '14416', '1800-11-2356', '181', why='Call 1930 quickly after cyber fraud.'),
        Q('Which is a dark pattern listed in India\'s 2023 guidelines?', 'Drip pricing: hidden charges added late in checkout', 'A clear price list', 'A free return policy', 'A plain "unsubscribe" button', why='One of the 13 specified dark patterns.'),
    ],
    study='read the lesson, the PIB release and the dark-pattern list',
    action='analyse five real scam messages and three dark patterns, save 1930 and teach the scam rule to two family members',
)

L3 = lesson(
    32, 3,
    outcome='You can recognise gaslighting, emotional blackmail and coercive control, respond with boundaries, and know where to get help.',
    split='20 minutes reading, 25 minutes of reflection',
    principle='Manipulation in close relationships works by making you doubt your own perception (gaslighting) or by using fear, obligation and guilt (emotional blackmail); naming it, keeping records, holding boundaries and getting outside support protect you.',
    science=f"""
**Gaslighting.** The term comes from the 1938 play and 1944 film *Gaslight*, in which a husband makes his wife believe she is going mad. It describes repeatedly making someone **doubt their memory, perception or sanity**: denying things that happened ("I never said that"), trivialising ("You're too sensitive"), rewriting history, or turning others against them. Sociologist Paige Sweet (2019) argued that gaslighting works through **power differences** (gender, age, money, status) and is often part of **abusive relationships**. Research on gaslighting is newer and mostly qualitative, so treat details with care; the core pattern is well described by clinicians and survivors. Everyday disagreements about memory ("I thought you said 5 pm") are **not** gaslighting; the pattern is **repeated, one-sided and aimed at control**.

**Emotional blackmail.** Therapist Susan Forward (1997) described emotional blackmail as using **Fear, Obligation and Guilt** ("FOG") to control someone: "If you really loved your family, you'd marry who we choose"; "After everything I've done for you…"; "If you leave, I'll hurt myself." The pattern is **demand → resistance → pressure → threat → compliance → repetition**. This is a clinical description rather than a tested model, but it helps people name what is happening.

**Coercive control.** Evan Stark's concept describes a pattern of controlling behaviours (monitoring phones, controlling money, isolating from friends and family, threats, humiliation) that may or may not include physical violence. It is recognised as a core feature of domestic abuse in research and, in some countries, in law. In India, the Protection of Women from Domestic Violence Act, 2005 covers physical, sexual, verbal, emotional and economic abuse ({CHECK}).

**Kerala and family context.** Pressure from family is not always manipulation: parents often express real worry clumsily. The difference: healthy concern accepts your **no** and respects you as an adult; manipulation **punishes** your no with threats, silent treatment, humiliation, withdrawal of support or self-harm threats, and repeats. Abuse can happen to anyone, of any gender.

**What helps:**
1. **Name it** privately: "This is guilt being used to control me."
2. **Keep records:** dates, what was said, screenshots. Gaslighting depends on you doubting your memory.
3. **Hold boundaries calmly:** "I understand you're upset. My decision is still no." Don't over-explain (PD-M26-L02).
4. **Get outside perspective:** a trusted friend, relative, counsellor or helpline.
5. **Safety first:** if there are threats of violence or self-harm, get help immediately (112 in emergencies). Threats of self-harm should always be taken seriously; respond by getting help for the person, not by giving in to the demand.

**Help in India:** emergency **112**; **Tele-MANAS 14416** (mental health, including for people affected by abuse); the national women's helpline **181** and Kerala's women's support services; police; and the Protection Officers under the domestic-violence law (ask at the district women's protection office) ({CHECK}).
""",
    evidence=[
        ('Gaslighting as a pattern of control', 'moderate', 'Well described clinically; research is newer and mostly qualitative.'),
        ('Emotional blackmail (FOG)', 'tool', 'A clinical description that helps people name pressure; not a tested model.'),
        ('Coercive control is a core feature of domestic abuse', 'strong', 'Widely recognised in research and policy.'),
        ('Records and outside support help people resist manipulation', 'tool', 'Standard advice from abuse-support services.'),
    ],
    example="""
Sreeja's cousin Meera, 27, tells her about her fiancé. He checks her phone, says her friends are "a bad influence", and when she mentions something he said, he insists, "I never said that; you imagine things. Ask anyone, you're always confused." She has started doubting her memory and avoiding her friends.

Sreeja listens without judging (PD-M25-L02). She gently names the pattern: "Checking your phone, cutting you off from friends and saying you imagine things: that sounds like control, not care." She suggests Meera keep a private note of dates and what was said, and talk to someone she trusts. Meera says her family thinks she is "overreacting" because the engagement is fixed (**obligation and guilt**).

Sreeja gives her the numbers (181, Tele-MANAS 14416, 112 in an emergency) and offers to go with her to talk to a counsellor. Two weeks later, Meera shows her notes to her elder brother, who believes her. With his support, the family postpones the wedding while she decides.
""",
    apply=f"""
**Spotting checklist (in any close relationship):**
{fence('''GASLIGHTING, BLACKMAIL AND CONTROL CHECK (patterns, not one-off events)
[ ] They often deny things I clearly remember, and I've started doubting myself
[ ] "You're too sensitive / crazy / always confused" is a common reply
[ ] My no is punished: threats, silent treatment, shouting, withdrawing support
[ ] "After everything I've done for you..." used to make me comply
[ ] Threats of self-harm if I don't do what they want
[ ] They monitor my phone, money or movements
[ ] They isolate me from friends or family
[ ] I feel afraid of their reaction more than I feel cared for
Several ticks = talk to someone you trust and consider a helpline.
Any threat of violence = safety first: 112.''')}

**Boundary script:** "I understand you're upset. My decision is ______. I'm not going to discuss it further today." Repeat calmly (broken record). Leave the room if needed.

**Records:** a private note (on a phone with a lock, or with a trusted person) with dates, quotes and screenshots.

**Self-harm threats used as pressure:** say "I care about you and I'm worried. I'm going to get help for you," and contact Tele-MANAS (14416) or emergency services (112). Don't handle it alone, and don't give in to the demand.

**With others:** if someone confides in you: believe them, listen, don't blame them for staying, share helplines, offer practical help, and respect their decisions (pushing can make things harder).
""",
    resources=[
        ('telemanas', 'Note that Tele-MANAS can support people affected by abuse and emotional distress', '5 minutes'),
        ('os-12', 'Re-read 12.4 on obedience and compliance: the same pressures act within families', '10 minutes'),
        ('ggsc', 'Search the site for "gaslighting" or "healthy boundaries" and read one article', '10 minutes'),
    ],
    steps=[
        'Write the difference between healthy concern and manipulation in your own words, with one example of each (real or imagined).',
        'Write your boundary script in English and Malayalam.',
        'Save 112, 181 and 14416 in your phone, and know where your nearest police station and women\'s protection office are.',
        'Reflect privately: does the spotting checklist apply to any relationship in your life (yours or someone close)? If yes, write one step you will take (talk to someone, keep records, call a helpline).',
    ],
    proof='Your healthy-versus-manipulation note, your boundary script in two languages, a note that the helplines are saved, and (privately) your reflection and one step.',
    templates=[('Boundary script and help card', """BOUNDARY SCRIPT
English: "I understand you're upset. My decision is ______. I'm not going to
          discuss it further today." (repeat calmly; leave if needed)
Malayalam: "______________________________________________"
RECORD KEEPING (private): Date | What was said or done | Witness? | Screenshot saved?
HELP CARD: Emergency 112 | Women's helpline 181 | Tele-MANAS 14416
           Nearest police station: ______ | Trusted person: ______""", '')],
    mistakes=[
        ('Calling every disagreement gaslighting.', 'The word means a repeated, one-sided pattern aimed at control.'),
        ('Arguing endlessly with a manipulator.', 'State the boundary, don\'t over-explain, leave if needed.'),
        ('Keeping it secret out of shame.', 'Outside perspective and support are protective.'),
        ('Ignoring threats.', 'Threats of violence or self-harm need immediate help (112, 14416).'),
    ],
    quiz=[
        Q('What is gaslighting?', 'Repeatedly making someone doubt their memory or perception in order to control them', 'Any disagreement about what was said', 'A cooking method', 'Forgetting something once', why='It is a repeated, one-sided pattern.'),
        Q('What does FOG stand for in emotional blackmail?', 'Fear, Obligation and Guilt', 'Friends, Organisation, Goals', 'Focus, Order, Grace', 'Family, Office, Government', why='Susan Forward\'s description.'),
        Q('What is the healthiest response to pressure that punishes your no?', 'State your boundary calmly, don\'t over-explain, and get outside support', 'Give in to keep peace', 'Shout back', 'Argue until they agree', why='Boundaries plus support protect you.'),
        Q('Someone threatens self-harm if you don\'t do what they want. What should you do?', 'Take it seriously and get help for them (14416 or 112), without giving in to the demand', 'Ignore it', 'Give in immediately', 'Keep it secret', why='Safety first, and pressure should not be rewarded.'),
    ],
    study='read the lesson and save the help numbers',
    action='write the healthy-versus-manipulation note and your boundary script, save the helplines and reflect on your relationships',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    32,
    overview=f"""
Self-defence against manipulation: high-pressure sales and MLM tactics, scam psychology (including "digital arrest", fake jobs and UPI tricks), the 13 dark patterns in India's 2023 guidelines, gaslighting, emotional blackmail and coercive control, with scripts, a red-flag checklist and helplines (1930, 112, 181, 14416).

This module covers manipulation and "dark psychology" **only so you can recognise and resist it**, and protect the people around you. It does not teach anyone how to manipulate.

The same influence principles you learned in Module 28 become manipulation when they are false, harmful, or make it hard to say no. The defence is the same every time: slow down, take the decision out of the room, verify independently, talk to someone you trust, and report. Financial scams are covered in depth in {xref('fin', 'fin-m15', 'the Personal Finance scams module')}.
""",
    outcomes=[
        'Recognise high-pressure sales and MLM recruitment tactics, and leave without buying.',
        'Explain scam psychology and the common scams in India, including "digital arrest".',
        'Know exactly what to do if targeted: stop, hang up, verify, talk, report (1930).',
        'Spot the 13 dark patterns in apps.',
        'Recognise gaslighting, emotional blackmail and coercive control, hold boundaries and get help.',
    ],
    lessons=LESSONS,
    project='a manipulation-spotting file with 10 real examples',
    project_steps=[
        'Collect at least 10 real examples over two weeks: ads, scam messages, sales pitches, MLM messages and dark patterns.',
        'Analyse each with the red-flag check: type, red flags, principle abused, action taken.',
        'Teach the scam rule to at least two family members and save the helplines in their phones.',
        'Add your scripts and the scam rule to your Personal Playbook.',
    ],
    project_proof='The 10-example manipulation-spotting file, a note on teaching family members and your Playbook lines.',
    rubric=[
        ('Recognition', 'Fewer than five examples', 'Five to nine', 'Ten or more, across several types'),
        ('Analysis', 'Labels only', 'Some red flags named', 'Red flags and abused principles named for each'),
        ('Readiness', 'No scripts', 'Scripts written', 'Scripts practised and helplines saved'),
        ('Protection of others', 'None', 'Talked about it', 'Taught two family members and saved numbers in their phones'),
    ],
    short=[
        'Learn the scam rule and save 1930.',
        'Use "I never decide on money the same day" at the next pitch.',
    ],
    flashcards=[
        ('Pyramid scheme sign', 'Income mainly from recruiting, not retail sales.'),
        ('Leave-without-buying line', '"I never decide on money the same day."'),
        ('"Digital arrest"', 'Does not exist. Hang up and report.'),
        ('Never share', 'OTP, PIN, CVV, passwords. No PIN to receive money.'),
        ('Cyber-fraud helpline', '1930 (and cybercrime.gov.in).'),
        ('Number of dark patterns in India\'s 2023 guidelines', '13.'),
        ('Gaslighting', 'Repeatedly making someone doubt their perception, to control them.'),
        ('FOG', 'Fear, Obligation, Guilt (emotional blackmail).'),
        ('Emergency and support', '112 emergency, 181 women\'s helpline, 14416 Tele-MANAS.'),
    ],
    mistakes=[
        ('Believing you are immune.', 'Pressure works on everyone; use scripts and rules.'),
        ('Blaming victims.', 'Shame stops reporting; support and report quickly.'),
        ('Using this knowledge to manipulate.', 'That is the opposite of the course\'s purpose.'),
    ],
    tools=[
        'The pitch analysis and leave-without-buying script (PD-M32-L01).',
        'The scam rule, red-flag check and manipulation-spotting file (PD-M32-L02).',
        'The control checklist, boundary script and help card (PD-M32-L03).',
    ],
    playbook=[
        'Red flags that make me stop: urgency, secrecy, authority without proof, fear, too good to be true, payment pressure.',
        'Money decisions: never the same day; verify on a number I look up; 1930 if money is lost.',
        'In relationships: my no stands; I keep records and get support if pressure becomes control.',
    ],
)
