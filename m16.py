from common import lesson, module, link, ASOF

L1 = lesson(
    16, 1,
    title='Avoiding burnout and comparison',
    weeks=(37, 37), hours=1.5,
    outcome='Recognise the early signs of creator burnout, set limits on your time, notifications and posting that you can keep alongside PSC study and client work, and use your numbers as information rather than a measure of your worth.',
    split='25 minutes study, 1 hour 5 minutes action',
    core=f"""
### What burnout is

The World Health Organization describes burn-out as a syndrome resulting from **chronic workplace stress that has not been successfully managed**, with three signs: **exhaustion**, **mental distance or cynicism about the work**, and **feeling less effective**. WHO classes it as an occupational phenomenon, not a medical condition. Social media work makes it easy: the work never closes, the numbers update every minute, and comments arrive at midnight.

### Early warning signs

- You dread posting, or feel sick before checking your numbers
- You check insights many times a day
- Sleep, meals or PSC study slip because of content or clients
- You feel irritable with followers, clients or family
- Nothing feels good enough, and you've stopped enjoying ideas you used to love

If several of these sound familiar, change something this week, not "after the sprint".

### What actually helps

YouTube's own tips for creators:

- **Schedule breaks** in your calendar, both short (a walk) and long (days off from creating), so you don't feel guilty taking them.
- **Set boundaries:** a work area, set work hours, and a fixed time limit for replying to comments.
- **Check in with yourself weekly** and be honest about how you feel.
- **Get help** with tasks that drain you, such as editing.
- **Batch similar tasks** to protect the rest of your week.

YouTube also says its system "doesn't intentionally penalize creators for taking breaks", and that negative comments and low views "are just feedback", not a verdict on you.

On Instagram, **Sleep mode** (formerly Quiet mode) turns off notifications and sends an auto-reply to messages during the hours you choose ({ASOF}). Use your phone's own focus and notification settings too.

### Comparison

You see other people's best posts and none of their bad days. Comparing your week 30 with someone's year 6 is unfair to you.

- **Compare only with your own past numbers,** monthly, in the Weekly Stats tab.
- **Mute** accounts that make you feel worse, even ones in your niche.
- **Judge the inputs you control:** posts made, experiments run, clients helped.
- **Remember the goal:** a skill, a portfolio and an income, not a follower count.

### PSC study, clients and posting together

Write your priority order and stick to it, for example: health and sleep → PSC study → paying clients → your own page → extras. Use exam mode (see the weekly schedule) in the four weeks before an exam, with batched posts.

### Getting help

Talking to someone you trust helps more than pushing through alone. **Tele-MANAS** is the government's free mental health helpline, on **14416** or 1-800-89-14416, 24 hours a day, in the language of your choice. If stress is affecting your sleep, health or daily life for weeks, please see a doctor.

The Entrepreneurship course looks at burnout from a business owner's side in ENT-M13-L02; read it if you are also running a business.
""",
    example="""
In week 33 Anu was running her sprint, finishing the pilot report and preparing for a PSC exam. She noticed she was checking Insights about twenty times a day and sleeping less (made-up example).

Her changes:

- **Limits:** content work only 7–8:30 pm on weekdays; Saturday morning batch; Sunday off from creating.
- **Insights:** checked once a day at 8 pm, and properly on Sunday for Weekly Stats.
- **Instagram Sleep mode** from 10 pm to 7 am; notifications off for likes, on for messages from clients only.
- **Exam mode** for the last three weeks before the PSC exam: two batched posts a week, no new clients.
- **Help:** she asked a cousin to edit two Reels a week for a small fee.

Two weeks later she slept better, her posting stayed steady, and her average views didn't drop.
""",
    resources=[
        ('who-burnout', 'Read WHO\'s definition of burn-out', '5 min'),
        ('yt-burnout', 'Read the tips on breaks, boundaries and getting help', '5 min'),
        ('yt-wellbeing', 'Read the tips on routines, performance anxiety and breaks', '10 min'),
        ('ig-sleep', 'Read how to set up Sleep mode', '3 min'),
        ('telemanas', 'Note the helpline numbers', '2 min'),
    ],
    steps=[
        'Study the resources (about 25 minutes).',
        'Do the warning-signs check honestly and note your score.',
        'Write your wellbeing plan: priority order, work hours, rest day, posting rhythm, comment-reply limit, and when you check insights.',
        'Set up Instagram Sleep mode and your phone\'s notification settings to match the plan.',
        'Mute 3–5 accounts that make you compare yourself unhelpfully.',
        'Follow the plan for 7 days, then do the weekly check-in.',
    ],
    proof='Your wellbeing plan, screenshots of your Sleep mode and notification settings, and your 7-day check-in.',
    templates=[
        ('wellbeing plan', """
MY PRIORITY ORDER: 1. ____ 2. ____ 3. ____ 4. ____ 5. ____
WORK HOURS FOR CONTENT AND CLIENTS: ________
REST DAY (no creating): ________
POSTING RHYTHM I CAN KEEP: ___ posts a week
COMMENT REPLIES: ___ minutes, at ________
INSIGHTS: check once a day at ____; review on Sunday
NOTIFICATIONS: off for ________; on for ________
SLEEP MODE: from ____ to ____
EXAM MODE starts ___ weeks before an exam
SOMEONE I CAN TALK TO: ________
HELPLINE: Tele-MANAS 14416 (free, 24 hours)
""", ''),
        ('weekly check-in', """
Energy (1-5): ___  Sleep OK? Y/N  Enjoying the work? Y/N
Warning signs this week: ____________________
What drained me: ___________________________
What helped: _______________________________
One change for next week: __________________
""", ''),
    ],
    mistakes=[
        ('Waiting until you\'re exhausted.', 'Act on the early signs.'),
        ('Treating views as your value as a person.', 'They are feedback on a post, nothing more.'),
        ('No days off during sprints.', 'Schedule rest; YouTube says breaks aren\'t penalised on purpose.'),
        ('Saying yes to every client.', 'Protect your study and health; a full calendar isn\'t a goal.'),
    ],
    quiz=[
        {'q': 'How does WHO describe burn-out?',
         'o': ['A medical disease', 'A syndrome from chronic workplace stress that hasn\'t been successfully managed', 'Laziness', 'A social media trend'],
         'a': 'B', 'why': 'WHO classes it as an occupational phenomenon with three dimensions.'},
        {'q': 'What does YouTube say about taking breaks?',
         'o': ['Your channel will be deleted', 'Its system doesn\'t intentionally penalise creators for taking breaks', 'You lose all subscribers', 'You must post daily'],
         'a': 'B', 'why': 'Schedule videos or tell your audience, and rest.'},
        {'q': 'Who should you compare your growth with?',
         'o': ['The biggest creator in Kerala', 'Your own past numbers', 'Your friends\' best posts', 'Nobody\'s, ever'],
         'a': 'B', 'why': 'Comparing with your past self shows real progress.'},
    ],
    study='WHO\'s definition of burn-out, YouTube\'s burnout and well-being tips, Instagram Sleep mode and Tele-MANAS (about 25 minutes)',
    action='write and follow a wellbeing plan for 7 days, with Sleep mode and notification limits set',
)

L2 = lesson(
    16, 2,
    title='Handling trolls and online harassment',
    weeks=(38, 38), hours=1.5,
    outcome='Tell critics from trolls, use the platforms\' tools to protect yourself and your clients, keep evidence, and know when and where to report serious harassment or threats.',
    split='25 minutes study, 1 hour 5 minutes action',
    core=f"""
### Critics, trolls and harassment

- A **critic** disagrees or complains about something real. Answer them (SMM-M14-L04).
- A **troll** wants a reaction, not an answer. Replying usually feeds them.
- **Harassment** is repeated or targeted abuse: insults about someone's looks, religion, caste or gender, threats, sharing private information ("doxxing"), or impersonation. YouTube's harassment policy, for example, doesn't allow prolonged insults or slurs, threats or doxxing.

### Your toolkit ({ASOF})

- **Instagram:** **Hidden Words** filters offensive words, phrases and emojis (and spammy message requests) into a hidden folder; **Limits** temporarily hides comments and message requests from people who don't follow you or only followed recently, and can be set so only Close Friends can comment and message for a while; you can also restrict, block and report accounts.
- **YouTube Studio:** hold comments for review, add blocked words, and hold comments with links.
- **Every platform:** report the content and the account.

Turn these on before you need them, especially before posting about anything that might attract attention.

### What to do, step by step

1. **Don't reply** to trolls or abusers.
2. **Save evidence:** screenshots that show the content, the account name, the date and the link, before you hide or delete anything.
3. **Hide, restrict or block,** and **report** to the platform.
4. **Tell someone you trust,** and for a client account, the owner.
5. **Serious cases:** threats, doxxing, impersonation, blackmail, morphed or fake intimate images, or any demand for money. Don't pay or negotiate. Report to the platform, call the **1930** cyber crime helpline (24 hours) and report on the National Cyber Crime Reporting Portal, and contact the police; YouTube's policy also advises contacting local law enforcement if someone makes specific threats and you feel unsafe.

### Protect your privacy before anything happens

- Keep your personal accounts private and separate from your page.
- Don't share your home address, daily routine or family details.
- Add location tags after you leave a place, not while you're there.
- Check photos you're tagged in, and who can tag and mention you.

### For client accounts

Agree a **moderation policy** with each client: what gets hidden, what gets answered, who handles abuse, and when to escalate. Never argue on a client's behalf in public.

### Look after yourself afterwards

Abuse hurts even when you know it's not about you. Step away from the screen, talk to someone, and if it stays with you, call **Tele-MANAS on 14416** (free, 24 hours) or see a doctor.
""",
    example="""
Anu posted a "Shop story" about an elderly tailor. A few accounts started posting abusive comments about his community, and others joined in (made-up example).

What she did, in order:

1. Didn't reply to any of the abusive comments.
2. Screenshotted them with the account names, dates and link, and saved them in a folder.
3. Turned on **Limits** for a week and added the slurs to **Hidden Words**; restricted and reported the accounts.
4. Pinned a comment: "This page is about our local people and shops. Hate isn't welcome here; such comments will be removed."
5. Called the tailor to tell him what happened and asked if he wanted the post down. He said keep it, so she did.
6. When one account sent her threatening DMs, she reported it, kept the evidence, and with her father went to the local police station.

The wave stopped in two days. The post ended up with hundreds of supportive comments from local people.
""",
    resources=[
        ('ig-abuse', 'Re-read Limits and Hidden Words, including the Close Friends option', '5 min'),
        ('yt-moderation', 'Re-read the moderation settings', '3 min'),
        ('yt-harassment', 'Read what the harassment policy covers and how to report', '5 min'),
        ('kp-1930', 'Re-read the 1930 helpline information', '3 min'),
        ('cybercrime', 'Note the address of the national reporting portal', '2 min'),
        ('telemanas', 'Note the helpline again', '2 min'),
    ],
    steps=[
        'Study the resources (about 20 minutes).',
        'Set up your protections now: Hidden Words with your own list of words, YouTube blocked words and held comments, and check who can tag and mention you.',
        'Review your privacy: separate personal and page accounts, remove details that reveal your home or routine.',
        'Write your harassment response plan (for you and for clients) using the template.',
        'Create an evidence log in Drive, ready to use.',
    ],
    proof='Screenshots of your protection and privacy settings, your harassment response plan and the empty evidence log.',
    templates=[
        ('harassment response plan', """
1. DON'T REPLY to trolls or abusers.
2. SAVE EVIDENCE first (screenshot: content, account,
   date, link) -> evidence log.
3. HIDE / RESTRICT / BLOCK and REPORT on the platform.
4. TELL: ________ (trusted person); for clients: owner ____
5. SERIOUS (threats, doxxing, impersonation, blackmail,
   morphed images, money demands):
   - don't pay or negotiate
   - report to the platform
   - call 1930; report on the national cyber crime portal
   - police station: ________
6. AFTER: step away; talk to someone; Tele-MANAS 14416
CLIENT MODERATION POLICY: hide ____; answer ____;
  escalate to the owner when ____
""", ''),
        ('evidence log', """
Date and time,Platform,Account name and link,What happened,Screenshot file,Reported to platform (Y/N and date),Other reports (1930 / portal / police),Notes
""", 'csv'),
    ],
    mistakes=[
        ('Arguing with trolls.', 'It gives them what they want. Hide, restrict, block, report.'),
        ('Deleting before saving evidence.', 'Screenshot first, with dates and links.'),
        ('Paying blackmailers.', 'Don\'t pay; report to 1930, the portal and the police.'),
        ('Sharing your live location.', 'Tag places after you leave.'),
        ('Carrying it alone.', 'Tell someone you trust; Tele-MANAS is free and 24 hours.'),
    ],
    quiz=[
        {'q': 'What should you do before hiding or deleting abusive comments?',
         'o': ['Reply angrily', 'Save evidence: screenshots with the account, date and link', 'Share them widely', 'Nothing'],
         'a': 'B', 'why': 'Evidence matters if you need to report it.'},
        {'q': 'Someone threatens you and demands money to stop posting fake images. What do you do?',
         'o': ['Pay quickly', 'Don\'t pay; report to the platform, call 1930, report on the portal and go to the police', 'Delete your account and say nothing', 'Argue with them'],
         'a': 'B', 'why': 'Paying rarely ends it; report it through the proper channels.'},
        {'q': 'What does Instagram\'s Limits feature do?',
         'o': ['Limits your posting', 'Temporarily hides comments and message requests from non-followers and recent followers', 'Deletes your followers', 'Makes posts private forever'],
         'a': 'B', 'why': 'It\'s designed for sudden waves of unwanted attention.'},
    ],
    study='Instagram\'s and YouTube\'s protection tools, YouTube\'s harassment policy, cyber crime reporting and Tele-MANAS (about 20 minutes)',
    action='set up your protections and privacy, and write a harassment response plan and evidence log',
)

LESSONS = [L1, L2]

MODULE = module(
    16,
    title='Creator wellbeing',
    weeks=(37, 38), hours=3.5,
    overview="""
Protect your energy, your mind and your safety: recognise burnout early, set limits you can keep, stop unhelpful comparison, and handle trolls and harassment calmly with the right tools and help.

A marketer who burns out helps nobody. You have already used batching, buffers and exam mode; now you'll make them a personal plan. You'll also set up protection before you need it, know exactly what to do if someone harasses you or a client, and know where to get help.

If you are struggling at any point in the course, come to this module first. Your health and your PSC exam come before any post.
""",
    outcomes=[
        'Explain burnout using WHO\'s definition and spot its early signs',
        'Write and follow a wellbeing plan with limits on time, notifications and posting',
        'Use numbers as feedback and avoid unhelpful comparison',
        'Use platform tools to prevent and handle trolling and harassment',
        'Keep evidence and know when to report to platforms, 1930, the portal and the police',
    ],
    lessons=LESSONS,
    project='Your wellbeing and safety plan',
    project_week=38,
    project_steps=[
        'Combine your wellbeing plan, your 7-day check-in and your harassment response plan into one document.',
        'Add screenshots of your settings (Sleep mode, notifications, Hidden Words, YouTube moderation).',
        'Share the harassment plan with your pilot client and agree their moderation policy.',
        'Put a monthly reminder in your calendar to do the weekly check-in honestly.',
    ],
    project_proof='Your combined wellbeing and safety plan with settings screenshots, and the client\'s agreed moderation policy.',
    rubric=[
        ('Burnout awareness', 'Ignores warning signs', 'Notices signs late', 'Checks signs weekly and acts early'),
        ('Limits', 'Always on', 'Some limits', 'Written limits on hours, notifications, insights and rest, followed for a week'),
        ('Comparison', 'Compares with big creators daily', 'Sometimes', 'Compares only with own past numbers; unhelpful accounts muted'),
        ('Protection', 'No settings', 'Some filters', 'Hidden Words, Limits, YouTube moderation and privacy checks set up'),
        ('Response plan', 'No plan', 'Knows to block', 'Evidence, reporting routes (platform, 1930, portal, police) and support written down'),
    ],
    short=[
        'Set Sleep mode and one rest day a week.',
        'Turn on Hidden Words and YouTube held comments.',
        'Save the 1930 and 14416 numbers in your phone.',
    ],
    flashcards=[
        ('WHO\'s three signs of burn-out?', 'Exhaustion, mental distance or cynicism about work, reduced effectiveness.'),
        ('Does YouTube intentionally penalise breaks?', 'No, it says its system doesn\'t.'),
        ('What does Instagram Sleep mode do?', 'Turns off notifications and auto-replies to messages during set hours.'),
        ('Who should you compare yourself with?', 'Your own past numbers.'),
        ('First step with a troll?', 'Don\'t reply.'),
        ('Before hiding abuse, do what?', 'Save evidence with account, date and link.'),
        ('Cyber crime helpline?', '1930.'),
        ('Free mental health helpline?', 'Tele-MANAS, 14416, 24 hours.'),
    ],
    mistakes=[
        ('Treating wellbeing as optional.', 'It decides whether you can keep doing this for years.'),
        ('Letting one bad comment ruin a week.', 'Hide it, report it if needed, talk to someone, and move on.'),
        ('Hiding problems from clients.', 'Tell them early when you need to adjust; good clients understand.'),
    ],
)
