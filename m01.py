from common import lesson, module, link, ASOF

L1 = lesson(
    1, 1,
    title='How social platforms and recommendation systems work',
    weeks=(1, 1), hours=3,
    outcome='Explain in your own words how Instagram, YouTube and Facebook decide what to show people, name the signals that matter most, and write five posting rules that will still work when the algorithms change.',
    split='1 hour study, 2 hours action',
    core=f"""
### "The algorithm" is many systems, not one

People say "the algorithm" as if one machine decides everything. Meta says plainly that there isn't a single AI system deciding what people see on Facebook and Instagram. Many systems each predict how likely you are to be interested in a post, or to interact with it, using thousands of signals, and those predictions decide the order of your feed ({ASOF}). YouTube works the same way. The details change every month; the purpose doesn't: **show each person what they are most likely to value.**

### Two ways people see your posts

| Who sees it | Where | What it depends on |
| --- | --- | --- |
| **People who follow you** | Feed, Stories, subscriptions, WhatsApp Status | Your relationship with them: how often they watch, like, reply to or message you |
| **People who don't follow you** | Instagram Reels tab and Explore, YouTube home and Shorts feed, Facebook feed recommendations, search | How well your post matches their interests and how earlier viewers reacted to it |

A new account has almost no followers, so nearly all its early views come from the second row: **recommendations**. That's good news. Instagram says its reels are now shown first to a small audience, and the ones that perform best go to wider and wider groups, "based on its engagement, not just the creator's follower count" ({ASOF}). A page with 50 followers can reach thousands of people with one good Reel.

### The signals that matter most

Platforms don't publish their exact formulas, but they do explain the main signals.

- **YouTube** names watch history, search history, subscriptions, likes, dislikes, "Not interested" and "Don't recommend channel" clicks, and satisfaction surveys. It uses surveys to understand "satisfaction, not just watch time" ({ASOF}).
- **Instagram's** explanation of Reels ranking lists your activity (which reels you liked, saved, shared or commented on), your history with the account, information about the reel (its audio, visuals and popularity) and information about the creator.
- **Meta** says engagement (likes, comments, views), how long and how often you watch, and your past interactions with the author all count, and that choosing "Not interested" or "Show less" lowers similar posts for a while.

Put simply, the system watches what real people **do** after seeing your post. Do they stop scrolling? Watch to the end? Watch again? Share it with a friend, save it, comment, follow, visit your profile? Or do they skip it in one second?

### What gets less reach

- **Copies.** Instagram recommends the original when it finds identical or near-identical content, and since 2024 it has removed accounts that repeatedly repost other people's content from recommendations. Facebook announced a similar crackdown on unoriginal content in July 2025.
- **Low quality.** Instagram's tips for creators: avoid watermarks from other apps and low-quality footage, use vertical video, hook viewers in the first 3 seconds.
- **Content that breaks the Recommendation Guidelines.** Instagram holds recommended content to "a higher standard" than what your followers may see. A professional account can check **Account Status** (Settings → Account → Account Status) to see whether its content can be recommended ({ASOF}).

### Principles that survive algorithm changes

Features and formulas change; these ideas have held for years on every platform:

1. **Make each post for one specific kind of person.** The system finds the right people more easily when the post is clearly for someone.
2. **Earn the first seconds.** Show the result, ask a sharp question or start with movement.
3. **Deliver what the hook promised.** Satisfied viewers watch longer, return and share; disappointed ones skip, and the system notices.
4. **Give people a reason to share or save it:** something useful, surprising, funny or local that they want to send to someone.
5. **Be original.** Your own photos, your own words, your own local knowledge.
6. **Be consistent and learn from your numbers.** Each post is a small experiment.
7. **Stay eligible.** Follow the rules, or nothing else matters.

### Common myths

- **"Post at the perfect time and you'll go viral."** Timing helps a little; content decides.
- **"30 hashtags = more reach."** Instagram began limiting captions to five hashtags in December 2025, and says fewer, more targeted hashtags work better than many generic ones ({ASOF}).
- **"I've been shadowbanned."** Usually the post just didn't interest people. Check Account Status first; if it shows no problem, look at your hook and watch time.
- **"Delete and repost it."** Reposting the same content doesn't fix it and may count as a duplicate. Make a better version instead.
""",
    example="""
Anu set up **@kuttiady.diaries** in Week 0. Her first post was a photo of a tea shop with a 12-line caption and 25 hashtags: 41 views, all from her friends.

Her second post was a 15-second vertical video: steam rising from glasses of chaya in the evening rush, with the text "₹12 chaya, since 1987: Kuttiady's oldest tea shop?" on screen in the first second, and the owner's permission. It got 1,300 views, and 82% of them came from accounts that didn't follow her. Seventeen people shared it, mostly to WhatsApp, and 23 followed the page.

Why? The first second showed movement and asked a local question. Local people watched to the end, then sent it to friends. Those shares told the system that this was worth showing to more people nearby. The photo post gave the system almost nothing to work with.

(Anu and her numbers are made up to illustrate the method.)
""",
    resources=[
        ('yt-recs', 'Read the whole page: the signals and where recommendations appear', '15 min'),
        ('meta-ai-ranking', 'Read the first half: how ranking works and how people control their feeds', '10 min'),
        ('ig-small', 'Read how reels are tested with small audiences first', '5 min'),
        ('ig-reco', 'Read the recommendation rules and the tips for creators', '10 min'),
        ('sel-ig-ranking', 'Skim the signals for Feed, Stories, Explore, Reels and Search', '10 min'),
    ],
    steps=[
        'Study the five resources above (about 50 minutes). Note any signal that surprises you.',
        'Keep a feed diary for 3 days. On your personal Instagram and YouTube, for 10 recommended posts a day (from accounts you don\'t follow), write one row each: what it was, why you think it was shown to you, whether you watched to the end, and what you did (skipped, liked, shared, saved, followed).',
        'On day 2, tap "Not interested" on 5 posts you dislike. On day 3, note whether your recommendations changed.',
        'Write your **5 rules that survive algorithm changes**, in your own words, using what you saw in your diary.',
        'Publish your first post on your practice account: a 15–30 second vertical video introducing the page ("What this page is about, in 15 seconds"). Log it in the Posting Log.',
    ],
    proof='Your 30-row feed diary, your 5 rules, and the link to your first post with its Posting Log row.',
    templates=[
        ('feed diary (paste into a new sheet)', """
Day,Platform,What the post was,Why I think I was shown it,Watched to the end? (Y/N),What I did (skip/like/share/save/follow/comment),Notes
""", 'csv'),
        ('my 5 rules that survive algorithm changes', """
MY 5 RULES (write them in your own words)
1. Who every post is for: ____________________
2. How I will earn the first 3 seconds: ________
3. How I will keep the promise of the hook: ____
4. Why someone would share or save my posts: ___
5. What I will never do (copy, buy, spam): _____

CHECK BEFORE EVERY POST
[ ] Is it original (my photo, my video, my words)?
[ ] Is the first second interesting without sound?
[ ] Is it clearly for one kind of person?
[ ] Would I send this to a friend?
[ ] Does it follow the rules from day 1?
""", ''),
    ],
    mistakes=[
        ('Chasing hacks.', 'Tricks that "beat the algorithm" stop working within months and can break the rules. Learn the principles instead.'),
        ('Judging a post in the first hour.', 'Recommended posts can keep getting views for days. Record views after 24 hours and after 7 days.'),
        ('Blaming a "shadowban".', 'Check Account Status first. If it shows no problem, improve the hook and the first 3 seconds.'),
        ('Reposting viral videos from other accounts.', 'Platforms recommend the original, label reposts and can stop recommending accounts that keep doing it.'),
        ('Writing for everyone.', 'A post for "everyone in Kerala" is for no one. Picture one viewer and make it for them.'),
    ],
    quiz=[
        {'q': 'According to YouTube Help, why does YouTube use viewer surveys in recommendations?',
         'o': ['To understand satisfaction, not just watch time', 'To count subscribers', 'To decide video prices', 'To check copyright'],
         'a': 'A', 'why': 'YouTube says surveys help the system understand satisfaction, not just watch time.'},
        {'q': 'A new account with 30 followers posts a Reel that gets 2,000 views. Where did most of those views probably come from?',
         'o': ['Its followers watching many times', 'Recommendations to people who don\'t follow it', 'Paid ads', 'Hashtags alone'],
         'a': 'B', 'why': 'New accounts grow mostly through recommendations, where a reel is tested on small groups first.'},
        {'q': 'Which of these is most likely to reduce a Reel\'s chance of being recommended on Instagram?',
         'o': ['Using vertical 9:16 video', 'Reposting someone else\'s video with another app\'s watermark', 'Adding audio', 'Posting regularly'],
         'a': 'B', 'why': 'Instagram recommends originals and advises avoiding watermarks and low-quality reposts.'},
        {'q': 'Your views drop for two weeks. What should you do first?',
         'o': ['Buy followers to restart growth', 'Delete all your posts', 'Check Account Status, then compare your hooks and watch time with your best posts', 'Add 30 hashtags'],
         'a': 'C', 'why': 'Rule out a policy problem, then look at the signals you control.'},
    ],
    study='YouTube\'s, Meta\'s and Instagram\'s own explanations of ranking (about 50 minutes)',
    action='keep a 3-day feed diary, write your 5 rules and publish your first post',
)

L2 = lesson(
    1, 2,
    title='The marketing funnel and the customer journey',
    weeks=(1, 1), hours=2,
    outcome='Map how a real customer moves from first seeing a business on social media to buying and recommending it, and choose the right content and the right number to watch at each stage.',
    split='1 hour 20 minutes study, 40 minutes action',
    core="""
### Why most posts don't sell (and why that's fine)

A person who sees a shop's Reel for the first time is rarely ready to buy. They need to notice the shop, trust it, and have a reason to act now. Marketers describe this path as a **funnel**: many people at the top, fewer at each step down.

| Stage | What the person thinks | Content that helps | Number to watch |
| --- | --- | --- | --- |
| **Awareness** | "Oh, I didn't know this place existed." | Short, entertaining or useful Reels and Shorts, local trends, collaborations | Views, accounts reached, share of non-followers |
| **Consideration** | "Is it good? Is it for me? How much?" | Proof: reviews, behind the scenes, prices, comparisons, FAQs, carousels | Profile visits, saves, follows, replies |
| **Conversion** | "I'll message, call, visit or order." | Clear offers, catalogue, "how to order", limited-time reasons | DMs and WhatsApp chats, calls, direction requests, orders |
| **Loyalty** | "I'll come back." | Updates for existing customers, Status, Channel posts, thank-yous | Repeat orders, Channel or broadcast replies |
| **Advocacy** | "You must try this." | Asking for reviews, sharing customers' posts with permission, referral offers | Reviews, tags, referrals |

Real people don't move in a straight line. Someone may see one post and order at once, or follow for months before buying. The funnel is still useful because it reminds you that **each post has a job**, and that you should judge it by the right number. A funny awareness Reel shouldn't be judged by orders, and a price-list post shouldn't be judged by views.

### The Kerala journey runs through WhatsApp

For most small businesses near Kuttiady, the conversion step isn't a website: it's a WhatsApp chat, a phone call or a visit. So a good social media plan always makes the next step easy: a WhatsApp button or link in the profile, the phone number in the bio, the location tagged, and opening hours that are correct.

### Owned, earned and paid

- **Owned:** channels you control: your Instagram page, YouTube channel, WhatsApp Business catalogue, Google Business Profile, website.
- **Earned:** what others say and share: shares, mentions, reviews, a local news page reposting you.
- **Paid:** ads and paid promotions (Module 9) and paid creator posts (Module 10).

Organic (unpaid) posting builds the owned and earned parts. Paid ads speed things up, but they work far better when the organic content is already good. This course starts with organic and adds paid later.

### One message everywhere

Your posts, profile, WhatsApp replies and shop counter should tell the same story. Marketers call this **integrated marketing communications**: every channel gives the customer the same message, so trust builds faster.
""",
    example="""
Riyas runs **Malabar Mobiles**, a phone shop with a repair counter in Kuttiady town. This is the path one customer, Shabna, took:

| Stage | What happened | Number Riyas could track |
| --- | --- | --- |
| Awareness | Saw a 20-second Reel, "3 signs your phone battery needs replacing", that a friend shared on WhatsApp | 4,200 views; 70% non-followers |
| Consideration | Visited the profile, saw the repair price list carousel and two customer reviews | 180 profile visits that week |
| Conversion | Tapped the WhatsApp button: "Battery for Redmi Note? How much?" Got a quick reply with a price and visited the next day | 26 WhatsApp chats; 9 repairs |
| Loyalty | Joined the shop's WhatsApp Channel for offers | 310 Channel followers |
| Advocacy | Left a Google review and told her sister | 1 review, 1 referral |

The Reel never "sold" anything, yet without it Shabna would never have heard of the shop. Riyas now judges his tip Reels by views and shares, and his price posts by WhatsApp chats.

(Malabar Mobiles and these numbers are made up to show the method.)
""",
    resources=[
        ('os-13-3', 'Read 13.3 to see why every channel should carry the same message', '30 min'),
        ('os-16-2', 'Read the social media marketing part of 16.2 (you can skip mobile marketing)', '40 min'),
        ('bp-intro', 'Free sign-up. Do the two short lessons on how businesses use Meta apps', '10 min'),
    ],
    steps=[
        'Study the three resources (about 1 hour 20 minutes).',
        'Map your own journey: think of something you bought in the last year after seeing it on social media. Fill in the five stages with what actually happened.',
        'Ask a friend or relative the same questions and map their journey. Note where WhatsApp, calls or visits came in.',
        'Pick one real local business you know. Fill in the funnel template for it: one content idea and one number for each stage.',
    ],
    proof='Two real customer journeys and one funnel map for a local business, saved in 01 Foundations.',
    templates=[
        ('funnel map', """
FUNNEL MAP: [business name]
Who the customer is: ____________________

AWARENESS
  Content idea: ____________________
  Number to watch: views / reach / % non-followers
CONSIDERATION
  Content idea: ____________________
  Number to watch: profile visits / saves / follows
CONVERSION
  How they act: WhatsApp / call / visit / order link
  Is it one tap away? Y / N
  Number to watch: chats / calls / orders
LOYALTY
  Content idea: ____________________
  Number to watch: repeat orders / Channel replies
ADVOCACY
  How I ask for reviews or referrals: __________
  Number to watch: reviews / referrals
""", ''),
        ('customer journey interview (5 questions)', """
1. What did you buy, and when?
2. Where did you first see it? (Reel, Status, friend, search...)
3. What made you trust it enough to ask or buy?
4. How did you contact them or buy? (WhatsApp, call, visit, app)
5. Did you tell anyone else about it, or leave a review?
""", ''),
    ],
    mistakes=[
        ('Expecting every post to sell.', 'Most posts build awareness and trust. Give each post one job and judge it by that job\'s number.'),
        ('Only posting offers.', 'Offers work for people at the bottom of the funnel. Without awareness and trust posts, there is no one left to buy.'),
        ('A hard-to-find next step.', 'If people can\'t message or call in one tap, they leave. Put the WhatsApp link and number where they can\'t miss them.'),
        ('Different details everywhere.', 'One name, one number, one address and the same message on every channel.'),
    ],
    quiz=[
        {'q': 'A carousel showing a bakery\'s prices and three customer reviews mainly helps which stage?',
         'o': ['Consideration', 'Awareness', 'Loyalty', 'None'],
         'a': 'A', 'why': 'Prices and proof help people who already know the bakery decide.'},
        {'q': 'Which number best shows whether a "how to order" post worked?',
         'o': ['Likes', 'WhatsApp chats and orders that came from it', 'Hashtags used', 'Followers of the page'],
         'a': 'B', 'why': 'Conversion posts are judged by actions such as chats, calls and orders.'},
        {'q': 'A customer\'s Google review that mentions the shop is an example of:',
         'o': ['Paid media', 'Owned media', 'Earned media', 'A boosted post'],
         'a': 'C', 'why': 'Earned media is what other people say and share about you.'},
        {'q': 'For most small shops near Kuttiady, what is the usual conversion step?',
         'o': ['A long website form', 'A WhatsApp chat, a call or a visit', 'An email newsletter', 'A podcast'],
         'a': 'B', 'why': 'That\'s why the WhatsApp link, phone number and location must be easy to find.'},
    ],
    study='OpenStax 13.3 and 16.2 and a short Meta Blueprint course (about 1 hour 20 minutes)',
    action='map two real customer journeys and a funnel for one local business',
)

L3 = lesson(
    1, 3,
    title='Career paths, your goal and your practice account',
    weeks=(2, 2), hours=2.5,
    outcome='Choose the career path you are aiming for, list the skills real employers and clients ask for, set your goals for the course, and confirm the niche of your practice account.',
    split='45 minutes study, 1 hour 45 minutes action',
    core="""
### What people pay social media marketers for

Businesses don't pay for posts. They pay for **results** (more enquiries, bookings, visits and sales) and for **time** (someone else handling it well). Keep that in mind and every skill in this course makes sense.

### Six paths

| Path | What you do day to day | How you usually start |
| --- | --- | --- |
| **Freelancer for local businesses** | Plan and make content, run WhatsApp and Google profiles, report results for 2–5 clients | A pilot for a business you know (Module 11), then monthly packages (Module 15) |
| **In-house job** | Social media executive or content creator for one company, institution or brand | Apply with a portfolio of real results; many roles ask for video and copy skills |
| **Agency job** | Work for many brands inside a team: content, ads, reports | Apply as a content creator, designer or social media executive |
| **Creator** | Grow your own channel or page and earn from it | Long-term; income usually comes later (Module 10) |
| **Specialist** | Video editor, ads specialist, community manager, analytics | Go deep in one skill after this course |
| **Your own business** | Market a business you run | Pair this course with the Entrepreneurship course |

You don't have to decide forever. Pick the path that excites you most now; the course works for all of them.

### The skills that get hired

Read real job ads and client requests and you'll see the same skills again and again: making short videos, writing captions, planning content, knowing the main platforms, reading insights, basic ads, and communicating with clients. **Proof beats certificates.** A portfolio with three real case studies and numbers persuades a shop owner or an employer more than any certificate. That's why this course makes you build one.

### Honest timelines

- Learning the skills well enough to help a small business: about 4–6 months at the part-time pace.
- First paid client: usually after a pilot or two, often with someone you already know.
- A steady income from several clients or a job: usually takes most of a year, sometimes longer.
- Growing your own account: slow for the first months for almost everyone.

These are not promises. They depend on how much you practise, your area and your luck. What you control is the work: posting, learning from numbers and talking to businesses.

### Researching your local market

Don't trust anyone's salary or price figures, including in this course, without checking. Instead, look at 10 real listings: job sites (search "social media executive Kozhikode", "content creator Kochi"), LinkedIn jobs, and the "we're hiring" posts of local businesses and agencies. Note the skills asked for and the pay, if it is stated. This also shows you what to put in your portfolio.

### Your practice account

In Week 0 you set up a practice account. Now confirm its niche with a quick scorecard. A good practice niche has:

- **Content supply:** you can make 3 posts a week for a year without running out
- **Audience demand:** people search for it and share it
- **Interest:** you enjoy it enough to keep going
- **Career link:** it helps you meet clients or shows skills employers want

The default, a **hyperlocal page about your area**, scores well on all four: there is always something new nearby, local people love sharing local posts, and every shop you feature is a future client who has already seen your work.
""",
    example="""
Anu scored three niche ideas from 1 to 5 on each point:

| Niche | Content supply | Demand | Interest | Career link | Total |
| --- | --- | --- | --- | --- | --- |
| Hyperlocal page, @kuttiady.diaries | 5 | 4 | 4 | 5 | 18 |
| Kerala PSC tips in Malayalam | 4 | 5 | 3 | 2 | 14 |
| Kozhikode food reviews | 4 | 4 | 5 | 3 | 16 |

She kept the hyperlocal page. Her research of 10 real listings (six job ads, four "need someone to handle our Instagram" posts) showed that 8 of 10 asked for short-video editing, 7 for Canva design and 5 for basic Meta ads. She set her goal: "By week 40, three case studies with numbers, two paying local clients, and a page of my own with steady weekly growth."

(Anu's scores and research are made up to illustrate the method; do your own.)
""",
    resources=[
        ('yt-creators', 'Open "Get started" and the "Grow" overview to see what creators learn first', '20 min'),
        ('ig-best', 'Browse the best practices hub: Reels, Profile, Grow and Monetize sections', '15 min'),
        ('hubspot-cert-blog', 'Read what a full social media certification covers, as a map of the skills', '10 min'),
    ],
    steps=[
        'Study the three resources (about 45 minutes).',
        'Find 10 real listings: job ads and businesses asking for social media help. Copy the skills and pay (if stated) into the skills table below.',
        'Choose your path for now and write your goals for week 13, week 26 and week 40.',
        'Score your practice niche (and up to two alternatives) with the scorecard. Keep or change it.',
        'Update your practice account\'s bio to say clearly what the page is about, in one line, in Malayalam or English.',
    ],
    proof='Your skills table from 10 real listings, your goals, your niche scorecard and a screenshot of your updated bio.',
    templates=[
        ('skills table from real listings', """
Source (site or business),Role or request,Location,Skills asked for,Tools named,Pay (if stated),Link,Date seen
""", 'csv'),
        ('career plan and niche scorecard', """
MY PATH (for now): ______________________

MY GOALS
By week 13: ___ posts published, ________________
By week 26: first case study done, ______________
By week 40: ___ case studies, ___ paying clients
            or job applications, _______________

SKILLS I SAW MOST OFTEN (top 5)
1. ________ 2. ________ 3. ________
4. ________ 5. ________

NICHE SCORECARD (1-5 each)
Niche | Supply | Demand | Interest | Career | Total
1. ___________ |   |   |   |   |
2. ___________ |   |   |   |   |
3. ___________ |   |   |   |   |
My choice: _______________
One-line bio: _______________________________
""", ''),
    ],
    mistakes=[
        ('Collecting certificates instead of results.', 'Certificates help a little; a portfolio with real numbers gets clients and jobs. Do both, but results first.'),
        ('Believing "₹1 lakh a month in 30 days" videos.', 'Income takes months of practice and client work. Check real listings for real figures.'),
        ('A niche you\'ll be bored of by week 6.', 'Score your interest honestly. You will post about this for 40 weeks.'),
        ('Waiting to feel ready before posting.', 'Your early posts are supposed to be weak. They become the "before" in your first case study.'),
    ],
    quiz=[
        {'q': 'What do small businesses mainly pay a social media marketer for?',
         'o': ['Pretty posts', 'More enquiries, bookings or sales, and saved time', 'Followers from anywhere', 'Hashtags'],
         'a': 'B', 'why': 'Businesses pay for results and for someone to handle it well.'},
        {'q': 'What persuades a local shop owner most that you can help them?',
         'o': ['A long list of certificates', 'A case study with real before and after numbers', 'A large personal follower count', 'A business card'],
         'a': 'B', 'why': 'Proof of results is what clients and employers look for.'},
        {'q': 'Why does a hyperlocal page score well as a practice niche?',
         'o': ['It needs no permissions', 'There is always local content, local people share it, and featured shops become future clients', 'It never needs posting', 'Platforms pay hyperlocal pages'],
         'a': 'B', 'why': 'It does well on content supply, demand and career link.'},
        {'q': 'Where should you get salary and price figures for your area?',
         'o': ['From viral videos', 'From 10 or more real, current job ads and client requests', 'From guessing', 'From one friend'],
         'a': 'B', 'why': 'Real listings show current local demand, skills and pay.'},
    ],
    study='YouTube Creators, Instagram\'s best practices hub and HubSpot\'s skills overview (about 45 minutes)',
    action='research 10 real listings, set your goals, score your niche and update your bio',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    1,
    title='Foundations',
    weeks=(1, 2), hours=9,
    overview="""
Learn how platforms decide what people see, how social media fits the path from stranger to customer, and what careers it can lead to. Your practice account starts posting this week.

Most beginners start by copying what's trending. This module starts one step earlier: understanding why some posts spread and others don't, so you can make good decisions when the platforms change. You'll study the platforms' own explanations, watch your own feed like a researcher, map real customer journeys, and research real jobs and client requests in your area.

By the end of week 2 your practice account is live with its first posts, and you have a one-page starter plan and the baseline numbers your growth will be measured against.
""",
    outcomes=[
        'Explain how recommendation systems use signals such as watch time, shares and satisfaction',
        'Map a customer\'s journey through the funnel and pick the right number for each stage',
        'Describe six career paths and the skills real listings ask for',
        'Choose and justify a practice niche',
        'Publish and log your first posts',
    ],
    lessons=LESSONS,
    project='Your starter plan and baseline snapshot',
    project_steps=[
        'Write a one-page starter plan: your path, your goals for weeks 13, 26 and 40, your practice niche and why, your main platforms for now (default: Instagram and YouTube Shorts), and your weekly time slots.',
        'Add your account baseline from Week 0 and today\'s numbers after your first posts.',
        'Plan your next 5 posts: topic, format and hook for each.',
        'Publish at least 3 posts in weeks 1–2 and log them in the Posting Log.',
        'Send your plan to your accountability buddy and agree when they will check on you.',
    ],
    project_proof='Your one-page starter plan and the links to at least 3 published, logged posts.',
    rubric=[
        ('Algorithm understanding', 'Can\'t explain why a post spreads', 'Can name some signals', 'Can explain signals and five lasting principles in own words'),
        ('Funnel thinking', 'Judges every post by likes', 'Knows the stages', 'Gives each post a job and the right number to watch'),
        ('Career clarity', 'No path or goals', 'A path but vague goals', 'A path, dated goals and skills from 10 real listings'),
        ('Practice account', 'Not set up', 'Set up, unclear niche', 'Live, clear one-line bio, niche scored and chosen'),
        ('Posting habit', 'No posts', '1–2 posts', '3 or more posts, all logged'),
    ],
    short=[
        'Read the YouTube and Instagram pages from SMM-M01-L01 (about 25 minutes).',
        'Keep the feed diary for one day instead of three.',
        'Map one customer journey instead of two.',
        'Publish 2 posts and log them. Skip the niche scorecard if your niche is already clear.',
    ],
    flashcards=[
        ('Where do most of a new account\'s views come from?', 'Recommendations to people who don\'t follow it yet.'),
        ('Name four signals YouTube uses for recommendations.', 'Watch history, search history, likes and dislikes, satisfaction surveys (also subscriptions and "Not interested").'),
        ('What does Instagram\'s Account Status show a professional account?', 'Whether its content and account can be recommended to non-followers.'),
        ('Why do reposts of other people\'s videos get less reach?', 'Platforms recommend the original and can stop recommending accounts that keep reposting.'),
        ('The five funnel stages?', 'Awareness, consideration, conversion, loyalty, advocacy.'),
        ('Owned, earned or paid: a customer\'s Google review?', 'Earned.'),
        ('What do businesses pay a social media marketer for?', 'Results (enquiries, bookings, sales) and saved time.'),
        ('Four tests of a good practice niche?', 'Content supply, audience demand, your interest, career link.'),
    ],
    mistakes=[
        ('Skipping the "why".', 'Without understanding signals, you can only copy trends. With it, you can design posts that work on any platform.'),
        ('Not logging posts from day 1.', 'Your first posts are your baseline. Without the numbers you can\'t show growth later.'),
        ('Comparing your week 2 with someone\'s year 5.', 'Compare yourself only with your own numbers from last month.'),
    ],
)
