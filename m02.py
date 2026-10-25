from common import lesson, module, link, ASOF

L1 = lesson(
    2, 1,
    title='Goals, objectives and KPIs',
    weeks=(3, 3), hours=2,
    outcome='Turn a business goal into a social media objective, a KPI and a dated target, for your own account and for a local business, starting from your own baseline numbers.',
    split='40 minutes study, 1 hour 20 minutes action',
    core="""
### From "be on Instagram" to a goal you can measure

Most small businesses say "we should be on Instagram". That's not a goal. A useful plan has four layers, each one serving the one above it:

| Layer | Question | Example for Nisha's Oven |
| --- | --- | --- |
| **Business goal** | What does the business need? | More weekday cake orders |
| **Social media objective** | What must social media do for that? | Get people within 5 km to message on WhatsApp |
| **KPI** | Which number shows it is working? | WhatsApp chats that start from Instagram |
| **Target** | How much, by when? | 30 chats a month by the end of March, from about 8 now |

Write targets the SMART way: **specific, measurable, actionable, realistic and time-bound**. "Grow the page" fails every test. "Reach 1,000 local followers by week 26, with at least 15% of views coming from shares" passes them all.

### Inputs, outputs and outcomes

- **Inputs** are what you control: posts a week, hooks tested, comments answered within an hour.
- **Outputs** are what the platform reports: views, reach, followers, shares.
- **Outcomes** are what the business feels: enquiries, bookings, sales, repeat customers.

Beginners set only output goals ("10,000 followers") and feel helpless when the numbers don't move. Set at least one input goal you fully control, such as "3 posts a week, every week", and judge yourself first on that.

### Which KPI for which objective

| Objective | KPIs that fit | Watch out for |
| --- | --- | --- |
| Awareness | Views, accounts reached, share of views from non-followers | Big reach outside your area is worth little to a local shop |
| Engagement | Shares, saves and comments per 1,000 views; engagement rate | Likes alone are the weakest signal |
| Leads | DMs, WhatsApp chats, calls, form fills, link clicks | Count them where they arrive: label chats "from Instagram" |
| Sales | Orders or bookings you can trace (ask "how did you hear about us?", use a code word) | Don't claim sales you can't trace |
| Loyalty | Repeat orders, WhatsApp Channel or broadcast replies | Needs a simple customer list |

**Engagement rate** = (likes + comments + shares + saves) ÷ accounts reached × 100. Platforms count slightly differently, so always say which formula you used, and compare a page only with its own past numbers. There is no universal "good" engagement rate.

### Vanity metrics

A vanity metric looks impressive but doesn't change decisions: total followers, total likes, "impressions" with no context. Use them as background, never as the headline of a report.

### Start from your baseline

Targets come from your own numbers, not from someone else's success story. If your first five posts averaged 120 views, a target of 300 views a post by week 13 is a stretch but believable; 50,000 is a wish.
""",
    example="""
Anu's goal ladder for **@kuttiady.diaries**:

- **Learning goal (input):** 3 posts a week, every week, and one experiment a month.
- **Growth objective:** become the page people in and around Kuttiady share for local news and food.
- **KPIs:** average views per post; shares per 1,000 views; followers within 25 km (Insights shows top towns once the page is bigger).
- **Baseline (first 5 posts):** 260 average views, 6 shares per 1,000 views, 48 followers.
- **Targets:** by week 13, 500 average views and 10 shares per 1,000; by week 26, 1,500 average views and 1,000 followers, mostly local.

For **Nisha's Oven** she wrote: business goal, more weekday orders; objective, WhatsApp chats from nearby parents; KPI, chats labelled "Instagram" in WhatsApp Business; target, from 8 to 30 a month by March; input, two process Reels and one price post a week.

(Made-up numbers to show the method.)
""",
    resources=[
        ('os-2-3', 'Read the "Objectives and Issues" part on SMART objectives', '15 min'),
        ('hubspot-social', 'Free sign-up. Watch the first lesson, on social media strategy (lesson names may change)', '25 min'),
    ],
    steps=[
        'Study the two resources (about 40 minutes).',
        'Work out your account\'s baseline from your posts so far: average views, shares per 1,000 views and followers.',
        'Write your own goal ladder: one input goal, one growth objective, two KPIs and targets for weeks 13 and 26.',
        'Write a goal ladder for one real local business you know, from business goal to target.',
        'For both, mark each number as an input, an output or an outcome.',
    ],
    proof='Your two goal ladders with baselines and dated targets, saved in 02 Strategy.',
    templates=[
        ('goal ladder', """
GOAL LADDER: [account or business]
Business goal: ____________________________
Social media objective: ___________________
KPI 1: ______________ (input / output / outcome)
KPI 2: ______________ (input / output / outcome)
Baseline today: ___________ (date: ____)
Target by week 13: ________
Target by week 26: ________
Input goal I fully control: ___ posts a week,
  plus ________________________________
How I will measure it: Posting Log / Insights /
  WhatsApp labels / "how did you hear about us?"
""", ''),
        ('KPI formulas', """
Engagement rate (%) = (likes + comments + shares + saves)
                      / accounts reached x 100
Shares per 1,000 views = shares / views x 1000
Non-follower share (%) = views from non-followers
                         / total views x 100
Follower growth (%) = (followers end - followers start)
                      / followers start x 100
Cost per enquiry (Rs) = money spent / enquiries
""", ''),
    ],
    mistakes=[
        ('Only output goals.', 'You can\'t control views directly. Add an input goal you can meet every week.'),
        ('Copying someone else\'s targets.', 'Start from your own baseline and stretch it.'),
        ('Reporting likes as success.', 'Lead with the KPI that matches the objective, such as chats or shares.'),
        ('No date.', 'A target without a date never fails, so it never teaches you anything.'),
    ],
    quiz=[
        {'q': 'Which is a SMART target?',
         'o': ['Grow the page', 'Get more engagement soon', '30 WhatsApp chats a month from Instagram by 31 March', 'Become famous in Kerala'],
         'a': 'C', 'why': 'It is specific, measurable, realistic for a small shop and time-bound.'},
        {'q': '"3 posts every week" is an example of:',
         'o': ['An outcome', 'An input you control', 'A vanity metric', 'A KPI for sales'],
         'a': 'B', 'why': 'Inputs are the actions fully in your control.'},
        {'q': 'For a lead-generation objective, which KPI fits best?',
         'o': ['Total likes', 'WhatsApp chats and calls that came from social media', 'Number of hashtags', 'Follower count'],
         'a': 'B', 'why': 'Leads are people who start a conversation about buying.'},
        {'q': 'Where should your first targets come from?',
         'o': ['A famous creator\'s numbers', 'Your own baseline, stretched', 'A random number', 'The highest number you can imagine'],
         'a': 'B', 'why': 'Targets based on your own numbers are believable and useful.'},
    ],
    study='OpenStax 2.3 on SMART objectives and HubSpot\'s first strategy lesson (about 40 minutes)',
    action='write goal ladders with baselines and dated targets for your account and one local business',
)

L2 = lesson(
    2, 2,
    title='Audience research and personas',
    weeks=(3, 3), hours=3,
    outcome='Find out what your audience really wants by talking to five people, mining comments and using Google Trends, then turn it into one or two evidence-based personas.',
    split='1 hour study, 2 hours action',
    core="""
### Research beats guessing

Most accounts fail because they post what the creator likes, not what the audience needs. You don't need surveys or money to find out. You need four free sources.

**1. Short conversations.** Talk to five people in your target audience, in person or on a call, for about 10 minutes each. Ask about their real behaviour, not their opinions about your idea:

- "When did you last look for [a good bakery / a phone repair / a place to eat] nearby? How did you search?"
- "Which pages or channels do you actually watch? Why those?"
- "What was the last post you sent to someone? Why?"
- "What do you wish someone explained better about [topic]?"

**2. Comment mining.** Open 3 to 5 popular accounts in your niche and read 50 comments on their best posts. Copy the questions, complaints and praise into a sheet. Comments are your audience telling you, for free, what they care about.

**3. Search data.** Google Trends shows how search interest in a topic changes over time and by region, on a 0–100 scale. A 100 means the peak for that topic in your chosen time and place, not a number of searches, and very low interest shows as 0 ({ASOF}). Set the region to Kerala, compare two or three terms, and switch to **YouTube Search** to see video interest. Also type your topic into YouTube and Instagram search and note the suggestions that appear.

**4. Your own numbers.** Once your page has more followers, its insights show top towns, age ranges and when followers are online. Until then, use the first three sources.

### Segment before you write

OpenStax describes four common ways to divide a market. For a social account:

- **Geographic:** Kuttiady and nearby panchayats; people from the area working in the Gulf
- **Demographic:** age, gender, family stage, income band
- **Psychographic:** values, interests, lifestyle ("loves trying new food spots", "careful with money")
- **Behavioural:** how they use the platform ("watches Reels at night", "searches on YouTube before buying")

### A persona built from evidence

A persona is a one-page profile of a typical person in your audience. Give it a name, but fill it only with things your research showed: quotes, real habits, real questions. A persona made from guesses is fiction; one made from five conversations and fifty comments is a tool.

### Malayalam, English or both?

Your research will tell you. Many audiences in Malabar are comfortable with Malayalam speech, English or Manglish text, and a mix. Gulf-based followers from the area often want local news and food nostalgia. Note what language your interviewees actually use in their own posts and messages (more in SMM-M04-L02).
""",
    example="""
Anu talked to five people: two college students, a shop owner, a mother of two and her cousin in Dubai. Comment mining on three Kozhikode food and news pages gave her 50 comments. The most common themes:

| Theme | How often (of 55 notes) | Example quote |
| --- | --- | --- |
| "Where is this? Send location" | 14 | "Ithu evideya? Location idu" |
| Prices | 11 | "Rate ethra?" |
| Nostalgia for home (Gulf followers) | 9 | "Missing naadu food" |
| Timings and parking | 7 | "Sunday open aano?" |
| Complaints about outdated posts | 5 | "Ithu ippo illa" |

Google Trends for Kerala showed that interest in "biryani" and "Onam sadya" rises before the festivals, so she noted them for her calendar. Her persona, "Shahana, 24, Kuttiady, college student", came straight from these notes: watches Reels at night, sends food spots to friends, always asks for location and price.

Her first change: every food post now shows the price and has the location tagged. Saves on food posts doubled the next week.

(Made-up research results to show the method.)
""",
    resources=[
        ('os-5-1', 'Read the four ways of segmenting consumer markets', '35 min'),
        ('gtrends-start', 'Read how to compare terms, explore by region and refine by category', '10 min'),
        ('gtrends-faq', 'Read what the 0–100 numbers mean (and don\'t mean)', '10 min'),
        ('yt-creators', 'In "Grow", read "Understand your audience"', '10 min'),
    ],
    steps=[
        'Study the resources (about 1 hour).',
        'Talk to 5 people in your target audience, about 10 minutes each, using the questions in the template. Take notes in their own words.',
        'Mine 50 comments from 3–5 popular accounts in your niche into the comment sheet. Tag each one with a theme.',
        'Run 3 Google Trends comparisons for Kerala (one on YouTube Search). Screenshot each and write one sentence on what it shows.',
        'Write one persona (two if your audience has two clear groups) using only what your research showed.',
    ],
    proof='Notes from 5 conversations, the 50-comment sheet with themes, 3 Trends screenshots and your persona, saved in 02 Strategy.',
    templates=[
        ('conversation questions (English and Malayalam)', """
1. When did you last look for [topic] nearby? How?
   [topic] അവസാനമായി എപ്പോഴാണ് അന്വേഷിച്ചത്? എങ്ങനെ?
2. Which pages or channels do you actually watch? Why?
   ഏതൊക്കെ പേജുകൾ/ചാനലുകൾ ശരിക്കും കാണാറുണ്ട്? എന്തുകൊണ്ട്?
3. What was the last post you sent to someone? Why?
   അവസാനം ആർക്കെങ്കിലും അയച്ച പോസ്റ്റ് ഏതാണ്? എന്തിന്?
4. What do you wish someone explained better?
   ആരെങ്കിലും നന്നായി വിശദീകരിച്ചിരുന്നെങ്കിൽ എന്ന് തോന്നുന്നത് എന്താണ്?
5. Malayalam, English or both: what do you prefer to read?
   വായിക്കാൻ ഇഷ്ടം മലയാളമോ ഇംഗ്ലീഷോ രണ്ടുമോ?
""", ''),
        ('comment mining sheet', """
Account,Post (topic),Comment (copy exactly),Type (question/complaint/praise/request),Theme,Language
""", 'csv'),
        ('persona card', """
PERSONA: [name], [age], [place]
Evidence: [5 conversations, 50 comments, Trends]
Language: Malayalam / English / Manglish / mix
Phone and data: ______________________
Platforms used and when: ______________
Wants: _______________________________
Problems and frustrations: ____________
Questions they ask (real quotes):
  1. "____________"  2. "____________"
What makes them trust a page: _________
What makes them share or save: ________
What makes them act (message, visit, buy): ____
What I must never do (turn-offs): _____
""", ''),
    ],
    mistakes=[
        ('Asking "would you follow a page like this?"', 'People say yes to be polite. Ask about what they actually did last time.'),
        ('Inventing the persona.', 'If a detail didn\'t come from research, delete it or mark it as a guess to test.'),
        ('Reading Trends as search counts.', 'The 0–100 scale is relative interest in that place and time, not a number of searches.'),
        ('Only talking to friends who love you.', 'Include at least two people who don\'t know your page.'),
    ],
    quiz=[
        {'q': 'Which question gives the most reliable information in an audience conversation?',
         'o': ['"Would you like my page?"', '"What was the last post you sent to someone, and why?"', '"Is my idea good?"', '"Will you follow me?"'],
         'a': 'B', 'why': 'Questions about real past behaviour are more honest than opinions about the future.'},
        {'q': 'In Google Trends, a value of 100 means:',
         'o': ['100 searches', 'The peak of relative interest for that term in your chosen time and place', '100% of people searched it', 'A trending hashtag'],
         'a': 'B', 'why': 'Trends shows relative interest on a 0–100 scale.'},
        {'q': '"Watches Reels at night and searches YouTube before buying" is which kind of segmentation?',
         'o': ['Geographic', 'Demographic', 'Behavioural', 'None'],
         'a': 'C', 'why': 'It describes how people behave on the platforms.'},
        {'q': 'What should a persona be built from?',
         'o': ['Your imagination', 'Real conversations, comments and search data', 'A stock photo', 'A competitor\'s bio'],
         'a': 'B', 'why': 'Evidence-based personas are tools; invented ones are fiction.'},
    ],
    study='OpenStax 5.1, Google Trends help and YouTube\'s audience guide (about 1 hour)',
    action='talk to 5 people, mine 50 comments, run 3 Trends comparisons and write your persona',
)

L3 = lesson(
    2, 3,
    title='Niche, positioning and competitor analysis',
    weeks=(4, 4), hours=2.5,
    outcome='Study 3 to 5 competing accounts, find the gap you can fill, and write a positioning statement for your account that makes it different and easy to remember.',
    split='50 minutes study, 1 hour 40 minutes action',
    core="""
### A niche is topic + audience + angle

"Food" is a topic. "Food in Kozhikode" adds a place. "Honest, under-₹200 food spots around Kuttiady, with price and location in every post" adds an angle. The narrower and clearer your niche, the easier it is for people (and recommendation systems) to understand who your posts are for. You can widen it later.

### Competitor analysis in five steps

1. **Choose 3–5 accounts:** two **direct** competitors (same topic, same area), one **indirect** (same audience, different topic) and one or two **aspirational** (bigger accounts you'd like to be like).
2. **Record the basics:** followers, posts a week, main formats, language, how they write bios and captions.
3. **Find their best posts.** On YouTube, open the channel and sort videos by **Popular**. On Instagram, scroll their Reels tab and note the ones with the highest view counts. Write down the topic, the hook and the format of the top 3.
4. **Read the comments** on those posts: what do people ask that isn't answered?
5. **Check if they run ads:** Meta's Ad Library lets anyone search the ads a Page is running on Facebook and Instagram. If a competitor has run the same ad for months, it's probably working.

Then look for **gaps**: questions nobody answers, formats nobody uses well, a language gap (no good Malayalam explanations), a place gap (no one covers your panchayat), or a quality gap (everyone posts blurry photos).

### Positioning: the place you want in people's minds

OpenStax describes positioning as deciding and communicating how you want your market to think and feel about you, either **head-to-head** (better at the same thing) or by **differentiation** (different in a way that matters). Small accounts almost always win by differentiation.

Write it as one statement:

**For [audience] who [want or need], [@handle] is the [kind of account] that [main benefit], unlike [alternatives], because [proof or angle].**

If you are positioning a business rather than an account, the Entrepreneurship course covers business positioning and naming in ENT-M06-L01.

### Don't copy, learn

Study competitors for patterns (formats, hooks, posting rhythm), never to copy their words, photos or videos. Copying breaks platform rules and the law, and it makes you a weaker version of them.
""",
    example="""
Anu analysed four accounts:

| Account (made up) | Type | Followers | Posts a week | Best format | What they do well | Gap |
| --- | --- | --- | --- | --- | --- | --- |
| @kozhikode.eats | Direct, bigger city | 85,000 | 6 | Reels with price on screen | Fast cuts, clear prices | Almost nothing from Kuttiady side |
| @vatakara.news | Direct, local news | 22,000 | 10 | Photo posts with long text | Quick news | Often no source; no food or shops |
| A Malayalam vlogger | Aspirational | 400,000 | 2 | 10-minute YouTube videos | Storytelling | Never covers small towns |
| A local college page | Indirect | 6,000 | 3 | Event Stories | Students share everything | Only campus |

Gap: nobody gives honest, current, price-and-location posts for the Kuttiady area, in Malayalam, with checked facts. Her positioning:

"For people in and around Kuttiady (and those missing home in the Gulf) who want to know what's good nearby, @kuttiady.diaries is the local page that shows real places with price and location in every post, unlike big city pages and unchecked forwards, because Anu visits every place herself and checks before she posts."

(Made-up accounts and numbers.)
""",
    resources=[
        ('os-5-6', 'Read positioning statements and perceptual maps', '30 min'),
        ('meta-ad-library', 'Open the Ad Library from this page and search for two local businesses or competitors', '10 min'),
        ('ig-best', 'In "Get started", read the Profile and Reels pages', '10 min'),
    ],
    steps=[
        'Study the resources (about 50 minutes).',
        'Choose 3–5 accounts: two direct, one indirect, one or two aspirational.',
        'Fill in the competitor sheet for each, including their top 3 posts and the questions people ask in comments.',
        'Write down at least three gaps you could fill.',
        'Write your positioning statement and test it on two people from your research: can they repeat what your page is about after hearing it once?',
    ],
    proof='Your competitor sheet for 3–5 accounts, your list of gaps and your positioning statement, saved in 02 Strategy.',
    templates=[
        ('competitor sheet (the Competitors tab)', """
Account,Platform,Type (direct/indirect/aspirational),Followers,Posts a week,Main formats,Language,Top 3 posts (topic and views),Hooks they use,Questions in comments,Runs ads? (Ad Library),What they do well,Gap I can fill
""", 'csv'),
        ('positioning statement', """
For ______________________ (audience)
who ______________________ (want or need),
@________ is the ______________ (kind of account)
that ______________________ (main benefit),
unlike ____________________ (alternatives),
because ___________________ (proof or angle).

Test: two people repeat it back in their own words?
Person 1: ______________  Person 2: ______________
""", ''),
    ],
    mistakes=[
        ('Only studying huge accounts.', 'Include direct local competitors; their audience is your audience.'),
        ('Copying a competitor\'s posts.', 'Learn the pattern, never take the content.'),
        ('A niche too wide to remember.', 'If you need two sentences to explain the page, narrow it.'),
        ('Competing head-to-head with a much bigger page.', 'Differentiate: a different place, language, angle or quality.'),
    ],
    quiz=[
        {'q': 'Which is the clearest niche?',
         'o': ['Food', 'Kerala', 'Honest under-₹200 food spots around Kuttiady, with price and location in every post', 'Everything local'],
         'a': 'C', 'why': 'It combines a topic, an audience and an angle.'},
        {'q': 'What does Meta\'s Ad Library let you do?',
         'o': ['See a page\'s private messages', 'Search the ads that Pages are running on Facebook and Instagram', 'Buy followers', 'Download competitors\' videos'],
         'a': 'B', 'why': 'It\'s a public transparency tool for ads.'},
        {'q': 'How do small accounts usually win against much bigger ones?',
         'o': ['Head-to-head on the same posts', 'By differentiation: a place, language, angle or quality the big ones don\'t serve', 'By copying them', 'By posting at midnight'],
         'a': 'B', 'why': 'Differentiation gives people a reason to follow you as well.'},
        {'q': 'An "aspirational" competitor is:',
         'o': ['An account you copy', 'A bigger account you learn patterns from', 'A fake account', 'A client'],
         'a': 'B', 'why': 'You study it for patterns in formats, hooks and rhythm.'},
    ],
    study='OpenStax 5.6 on positioning, Meta\'s Ad Library and Instagram\'s profile guidance (about 50 minutes)',
    action='analyse 3–5 competitors, list the gaps and write a tested positioning statement',
)

L4 = lesson(
    2, 4,
    title='Content pillars and brand voice',
    weeks=(4, 4), hours=1.5,
    outcome='Choose 3 to 5 content pillars that serve your persona, fill your Ideas tab with 20 ideas, and write a brand voice chart for Malayalam and English.',
    split='25 minutes study, 1 hour 5 minutes action',
    core="""
### Pillars: the few things you always talk about

A content pillar is one of the 3 to 5 big themes your page covers. Pillars keep you consistent (people know what to expect) and stop you running out of ideas (each pillar has endless posts in it). Build them from your research: each pillar should answer a real need of your persona.

For a hyperlocal page, for example:

1. **Eat:** honest food spots with price and location
2. **Know:** useful local updates: timings, new shops, events, roadworks (checked)
3. **People:** short stories of local shop owners, craftspeople and helpers (with consent)
4. **Nostalgia and places:** old photos (your own or with permission), rivers, hills, festivals

A rough rule: most posts should help, entertain or inform; only a few should sell. For a business, pillars might be **show** (product and process), **teach** (useful tips), **prove** (results and reviews with permission), **personal** (the story behind it) and **offer**. The Entrepreneurship course uses these for business content in ENT-M06-L02.

### Series: pillars on autopilot

A **series** is a repeating format inside a pillar: "₹100 Friday" (a food spot under ₹100 every Friday), "Shop of the week", "Then and now". Series are easier to make, easier for followers to recognise and easier to batch.

### Brand voice: how you sound

Your voice is your page's personality in words. Write it down so it stays the same whether you're tired, happy or writing at midnight. A **voice chart** lists three to four traits, each with what it means and what it doesn't:

| We are | That means | We are not |
| --- | --- | --- |
| Friendly | Talk like a helpful neighbour; use "നമ്മുടെ" | Over-familiar or slangy with strangers |
| Honest | Say the price, say when something was average | Paid hype or fake "best ever" |
| Local | Use place names, local words and humour | Cliquey or mocking other areas |
| Careful | Check facts; say "as of today" | Rumours, forwards, politics |

### Language rules

Decide, and write down, how you'll mix languages: for example "Malayalam in speech and on-screen text, English in the first line of the caption for search, Manglish never in the on-screen text". SMM-M04-L02 goes deeper.

### A light visual identity

Two colours, one or two fonts (one that supports Malayalam well, such as Manjari or Noto Sans Malayalam), and one photo style (daylight, real places, no stock photos). Use them on every cover and thumbnail.
""",
    example="""
Anu's pillars and series for @kuttiady.diaries:

| Pillar | Share of posts | Series | Funnel job |
| --- | --- | --- | --- |
| Eat | 40% | "₹100 Friday" | Awareness, shares |
| Know | 25% | "This week near you" (Sunday) | Follows, saves |
| People | 20% | "Shop story" (owner speaks, 45 seconds) | Trust, shares |
| Places and nostalgia | 15% | "Then and now" (her own old family photos) | Shares from the Gulf |

Her voice: friendly, honest, local, careful. Her rule: "If I can't check it, I don't post it." Her language rule: Malayalam speech and on-screen text, an English first line for search.

She filled her Ideas tab with 24 ideas in 40 minutes, six per pillar.

(Made up to show the method.)
""",
    resources=[
        ('ig-best', 'In "Creation", read the pages on creating engaging and original content', '15 min'),
        ('canva-mkt', 'Free sign-up. Watch the lesson "Optimizing brand presence"', '10 min'),
    ],
    steps=[
        'Study the two resources (about 25 minutes).',
        'Choose 3–5 pillars from your research, each linked to a need of your persona.',
        'Create 2 series ideas you could repeat every week.',
        'Fill your Ideas tab with at least 20 ideas: at least 4 per pillar, each with a format and a hook idea.',
        'Write your voice chart and language rules, and pick your two colours and fonts.',
    ],
    proof='Your pillars and series, 20 or more ideas in the Ideas tab, and your voice chart with language rules, saved in 02 Strategy.',
    templates=[
        ('content pillars', """
PILLAR 1: ________  (share of posts: __%)
  Persona need it serves: ______________
  Funnel job: awareness / trust / action
  Series: "__________" every ________
  Ideas: 1. ______ 2. ______ 3. ______ 4. ______
PILLAR 2: ________  (repeat)
PILLAR 3: ________
PILLAR 4: ________ (optional)
PILLAR 5: ________ (optional)
""", ''),
        ('voice chart and language rules', """
WE ARE      | THAT MEANS            | WE ARE NOT
____________ | _____________________ | __________
____________ | _____________________ | __________
____________ | _____________________ | __________

WORDS WE USE: ________________________
WORDS WE NEVER USE: __________________
LANGUAGE RULES
  Speech in videos: Malayalam / English / mix
  On-screen text: ______________________
  Caption first line: __________________
  Hashtags: ____________________________
VISUALS
  Colours: ______ (hex) and ______ (hex)
  Fonts: ______ (Malayalam) ______ (English)
  Photo style: _________________________
""", ''),
    ],
    mistakes=[
        ('Too many pillars.', 'Eight themes means none of them is clear. Start with 3 or 4.'),
        ('Pillars about you, not them.', 'Each pillar must answer a need from your research.'),
        ('Voice that changes with your mood.', 'Write the chart and check every caption against it.'),
        ('Mixing scripts randomly.', 'Decide where Malayalam, English and Manglish go, and stick to it.'),
    ],
    quiz=[
        {'q': 'What is a content pillar?',
         'o': ['One viral post', 'One of 3–5 main themes your page always covers', 'A hashtag', 'A paid ad'],
         'a': 'B', 'why': 'Pillars give a page consistency and an endless source of ideas.'},
        {'q': 'Why are series useful?',
         'o': ['Platforms pay for them', 'They are easier to make, batch and recognise', 'They avoid all rules', 'They replace pillars'],
         'a': 'B', 'why': 'A repeating format saves time and builds habits in your audience.'},
        {'q': 'A voice chart line "Honest, not paid hype" helps you:',
         'o': ['Write captions that sound the same and stay trustworthy', 'Get more hashtags', 'Avoid using Malayalam', 'Post less'],
         'a': 'A', 'why': 'A written voice keeps your tone consistent across every post.'},
    ],
    study='Instagram\'s guidance on engaging, original content and Canva\'s brand presence lesson (about 25 minutes)',
    action='choose your pillars and series, add 20 ideas and write your voice chart',
)

LESSONS = [L1, L2, L3, L4]

MODULE = module(
    2,
    title='Strategy',
    weeks=(3, 4), hours=10,
    overview="""
Decide what your account is for, who it serves, how it is different and what it talks about, using real research instead of guesses.

A strategy is a short set of decisions that make every later decision easier. In two weeks you'll set goals and KPIs from your own baseline, talk to real people in your audience, mine comments and search data, study your competitors, write a positioning statement, and choose your content pillars and brand voice.

You keep posting while you do it: two posts a week, and from now on each post should fit a pillar.
""",
    outcomes=[
        'Turn a business goal into a social objective, a KPI and a dated target',
        'Research an audience with conversations, comment mining and Google Trends',
        'Write an evidence-based persona',
        'Analyse competitors and find gaps',
        'Write a positioning statement, content pillars and a brand voice chart',
    ],
    lessons=LESSONS,
    project='A one-page social media strategy',
    project_steps=[
        'Put your work from this module on one page (Google Docs): goal ladder, persona, positioning statement, top 3 competitor lessons and gaps, pillars and series, voice chart and language rules.',
        'Add the platforms you plan to use (you will confirm them in Module 3) and your posting rhythm.',
        'Add the KPIs you will report every month.',
        'Ask one person from your research to read it and tell you what is unclear. Fix it.',
    ],
    project_proof='Your one-page strategy (link) with a note of the feedback you got and what you changed.',
    rubric=[
        ('Goals', 'No targets', 'Targets without baseline or date', 'Input and output goals from a baseline, with dates'),
        ('Audience research', 'Guesses only', 'Some research', '5 conversations, 50 comments and Trends behind the persona'),
        ('Positioning', 'Unclear what the page is', 'A statement others can\'t repeat', 'A statement two people repeated correctly'),
        ('Competitors', 'None studied', 'One or two, no gaps', '3–5 studied with clear gaps'),
        ('Pillars and voice', 'Random posting', 'Pillars but no voice', 'Pillars, series, 20 ideas and a written voice chart'),
    ],
    short=[
        'Write one goal ladder (your account) with one input goal.',
        'Have 3 conversations instead of 5, and mine 30 comments.',
        'Study 3 competitors.',
        'Choose 3 pillars and write 12 ideas.',
    ],
    flashcards=[
        ('The four layers of a goal ladder?', 'Business goal, social objective, KPI, target.'),
        ('What does SMART stand for (OpenStax)?', 'Specific, measurable, actionable, realistic, time-bound.'),
        ('Inputs, outputs, outcomes: which is "WhatsApp orders"?', 'An outcome.'),
        ('Engagement rate formula?', 'Interactions ÷ accounts reached × 100 (say which formula you used).'),
        ('Four free audience research sources?', 'Conversations, comment mining, search data (Google Trends, search suggestions), your own insights.'),
        ('What does 100 mean in Google Trends?', 'Peak relative interest for that term in the chosen time and place.'),
        ('A niche is topic + audience + ...?', 'Angle.'),
        ('Head-to-head or differentiation for a small account?', 'Differentiation.'),
        ('What is a content series?', 'A repeating format inside a pillar, like "₹100 Friday".'),
    ],
    mistakes=[
        ('Skipping research because "I know my audience".', 'Everyone is surprised by what five honest conversations reveal.'),
        ('A strategy nobody reads.', 'Keep it to one page and check new post ideas against it.'),
        ('Changing strategy every week.', 'Give a strategy at least a month of posts before you judge it.'),
    ],
)
