from common import lesson, module, link, ASOF

L1 = lesson(
    8, 1,
    title='Key metrics and built-in insights',
    weeks=(19, 19), hours=3.5,
    outcome='Read Instagram Insights, YouTube Studio analytics and WhatsApp Business statistics, work out the few ratios that matter, and turn your 30-day challenge numbers into clear decisions.',
    split='45 minutes study, 2 hours 45 minutes action',
    core=f"""
### The numbers that matter, in plain words

| Metric | What it means | Why it matters |
| --- | --- | --- |
| **Views** | How many times a post was seen, counting repeats | Instagram's main metric across formats since August 2024 |
| **Accounts reached** | How many different accounts saw it | Real audience size |
| **Non-follower share** | Views or reach from people who don't follow you | Your growth from recommendations |
| **Interactions** | Likes, comments, shares, saves | Signals of interest |
| **Shares and saves** | Sending to others, keeping for later | The strongest signs a post was valuable |
| **Watch time and retention** | How long people watch, and where they leave | Shows whether the hook and story worked |
| **Follows** | New followers from a post | Whether people want more from you |
| **Profile visits and link clicks** | People looking for more, or going to your link | Consideration |
| **Messages and enquiries** | DMs, WhatsApp chats, calls | Leads, the number businesses care about |

### Where to find them ({ASOF})

- **Instagram:** open a post and tap **View insights**, or open the **professional dashboard** for the account. Look at Views, the split between followers and non-followers, interactions, and for Reels the watch time. Instagram's creator advice is to watch your **View Rate** in Insights to see whether your hook keeps people watching.
- **YouTube Studio** (phone app or computer): **Impressions** count when your thumbnail was shown for more than a second with at least half of it visible on YouTube. **Impressions click-through rate** shows how often an impression led to a view. **Average view duration** and the **audience retention** graph (intro, top moments, spikes and dips) show where people leave. **Traffic sources** show whether views came from search, the Shorts feed, browse or suggested videos. Data usually takes a day or two to appear.
- **Facebook:** Page insights in Meta Business Suite.
- **WhatsApp Business:** message statistics, and read and reply rates for business broadcasts.
- **LinkedIn:** analytics for your posts and Page.

### Ratios beat raw numbers

A post with 5,000 views and 2 shares did worse than one with 800 views and 40 shares, if your goal is to be shared. Calculate a few ratios per post:

- **Share rate** = shares ÷ views × 1,000 (shares per 1,000 views)
- **Save rate** = saves ÷ views × 1,000
- **Follow rate** = follows ÷ views × 1,000
- **Engagement rate** = interactions ÷ accounts reached × 100
- **Non-follower share** = views from non-followers ÷ views × 100

### From numbers to decisions

Look for **patterns** across many posts, not single surprises. Group your 30 challenge posts by pillar, format, hook type, length and language, and compare the averages. Then write each finding as **"So what? Now what?"**:

- "Shop stories have twice the share rate of food posts → so local people love people stories → post two shop stories a week."

### Be careful with small numbers

With 30 posts, differences of a few per cent can be chance. Treat findings as **directional** and test them again. And remember platforms change how they count: compare with your own past numbers, measured the same way.
""",
    example="""
Anu put her 30 challenge posts in a sheet and grouped them (made-up numbers to show the method):

| Group | Posts | Average views | Shares per 1,000 | Follows per 1,000 |
| --- | --- | --- | --- | --- |
| Shop stories | 6 | 3,100 | 19 | 9 |
| ₹100 food | 9 | 1,400 | 12 | 6 |
| Local updates (text-heavy) | 5 | 420 | 3 | 2 |
| Places and nostalgia | 6 | 1,050 | 15 | 4 |
| Collabs | 4 | 2,200 | 10 | 11 |
| Question hooks (all pillars) | 13 | 1,700 | 14 | 7 |
| Result-first hooks | 12 | 1,350 | 11 | 6 |

Her decisions: two shop stories a week; text-heavy updates move to the WhatsApp Channel; one collab a month, because collabs bring the most follows per view; keep testing question hooks, since the difference was small.
""",
    resources=[
        ('ss-views', 'Re-read how Views became Instagram\'s main metric', '5 min'),
        ('ig-small', 'Re-read the View Rate tip', '3 min'),
        ('yt-impressions', 'Read what counts as an impression and how CTR works', '10 min'),
        ('yt-retention', 'Re-read the retention key moments and how to use them', '10 min'),
        ('wa-broadcasts', 'Re-read the broadcast metrics (read and reply rates)', '3 min'),
        ('hubspot-social', 'Watch the lesson on measuring social media results (lesson names may change)', '15 min'),
    ],
    steps=[
        'Study the resources (about 45 minutes).',
        'For all 30 challenge posts, make sure your Posting Log has 7-day views, reach, shares, saves, follows and (for videos) watch time or retention.',
        'Add the five ratio columns and fill them with formulas.',
        'Group the posts by pillar, format, hook type, length and language, and compare the averages.',
        'Write 5 "So what? Now what?" findings with a decision each, and mark which ones need re-testing.',
    ],
    proof='Your Posting Log with ratio columns, the grouped comparison table and your 5 findings with decisions.',
    templates=[
        ('ratio formulas for Google Sheets', """
(Assuming views in column J, shares in N, saves in O,
 follows in P, reach in K, interactions in Q, views from
 non-followers in R)
Share rate per 1,000:   =IFERROR(N2/J2*1000,0)
Save rate per 1,000:    =IFERROR(O2/J2*1000,0)
Follow rate per 1,000:  =IFERROR(P2/J2*1000,0)
Engagement rate %:      =IFERROR(Q2/K2*100,0)
Non-follower share %:   =IFERROR(R2/J2*100,0)
Group averages:         =AVERAGEIF(D:D,"Shop story",J:J)
""", ''),
        ('findings: so what, now what', """
FINDING 1: ______________________ (numbers: ____)
  So what? _______________________
  Now what? ______________________
  Confidence: strong / directional (re-test)
FINDING 2: ...
(5 findings)
""", ''),
    ],
    mistakes=[
        ('Reading only views.', 'Use ratios such as shares, saves and follows per 1,000 views.'),
        ('Comparing with other people\'s accounts.', 'Compare with your own past numbers, measured the same way.'),
        ('Deciding from one post.', 'Look at averages across groups of posts.'),
        ('Checking too early.', 'Use 7-day numbers; recommended posts keep growing for days.'),
    ],
    quiz=[
        {'q': 'Which post did better at being shared?',
         'o': ['5,000 views and 2 shares', '800 views and 40 shares', 'They are equal', 'Impossible to say'],
         'a': 'B', 'why': '50 shares per 1,000 views against 0.4 per 1,000.'},
        {'q': 'When does YouTube count a thumbnail impression?',
         'o': ['Every time a video is uploaded', 'When the thumbnail is shown for more than a second with at least half of it visible', 'Only when clicked', 'When a video is shared'],
         'a': 'B', 'why': 'That is YouTube\'s definition, on YouTube surfaces.'},
        {'q': 'Your findings come from 30 posts and the difference is small. How should you treat it?',
         'o': ['As proof', 'As directional, and test it again', 'Ignore all data', 'Delete the worse posts'],
         'a': 'B', 'why': 'Small samples can mislead; re-test before big changes.'},
        {'q': 'Which number best shows growth from recommendations?',
         'o': ['Total likes', 'The share of views from non-followers', 'Number of hashtags', 'Posting time'],
         'a': 'B', 'why': 'Non-follower views show the system is showing you to new people.'},
    ],
    study='Instagram\'s and YouTube\'s metric definitions, WhatsApp broadcast stats and HubSpot\'s measurement lesson (about 45 minutes)',
    action='add ratios to your 30 challenge posts, compare groups and write 5 findings with decisions',
)

L2 = lesson(
    8, 2,
    title='Google Analytics 4 and UTM links',
    weeks=(20, 20), hours=3.5,
    outcome='Set up a free Google Analytics 4 property on a simple site, tag your social links with UTM parameters, and read which platform and post sent visitors.',
    split='45 minutes study, 2 hours 45 minutes action',
    core=f"""
### Why bother with Google Analytics

Platform insights tell you what happened **on** the platform. When a post sends people to a website (a business's booking page, a menu, your portfolio), **Google Analytics 4 (GA4)** tells you what happened next: how many arrived, from which platform and campaign, and what they did. GA4 is free; Google's setup guide says it gives insights "at no cost".

### Set up GA4 in four steps ({ASOF})

1. **Account:** sign in at analytics.google.com and create an account.
2. **Property:** name it ("Anu portfolio"), choose India's time zone and rupees.
3. **Web data stream:** add your site's address; turn on enhanced measurement.
4. **Add the tag:** copy the **Measurement ID** (it starts with "G-") into your site. On **Google Sites**, open Settings → Analytics and enter the ID. Google Sites' help notes that data can take up to 24 hours to show, and that visitors who reject cookies make the numbers lower than real.

Test it: open your site on your phone and check the **Realtime** report.

### A simple site to practise on

If you don't have a site yet, make a one-page **Google Sites** page now, such as "About @kuttiady.diaries" or a menu page for a friendly business. You'll turn it into your portfolio in Module 12.

### UTM links: labels on your links

A UTM link is a normal link with labels added at the end, so GA4 knows where each visitor came from. Google's rules:

- **Always use** `utm_source`, `utm_medium` and `utm_campaign`. Missing ones show up as "(not set)".
- **Optional:** `utm_content` (to tell apart two links in the same place), `utm_term` (paid keywords) and `utm_id`.
- **Values are case-sensitive:** `instagram` and `Instagram` are different, so always use lowercase.

Example:

`https://sites.google.com/view/yourpage?utm_source=instagram&utm_medium=social&utm_campaign=bio_link`

Use Google's free **Campaign URL Builder** to make them without typing mistakes. Never put names, phone numbers or other personal details in a UTM.

### Read the results

In GA4, open **Reports → Acquisition → Traffic acquisition**. The **session source / medium** shows "instagram / social", "whatsapp / social" and so on; **session campaign** shows your campaign names; the default channel groups include **Organic Social** and **Paid Social**.

### WhatsApp is different

A WhatsApp click-to-chat link opens a chat, not a website, so GA4 can't see it. Track WhatsApp enquiries with **keywords** in your CTA ("send 'SQUAT'"), **labels** in WhatsApp Business and the question "how did you hear about us?".
""",
    example="""
Peak Fitness made a one-page Google Site with its timetable and fees, connected GA4, and used three UTM links for two weeks:

| Where | utm_source | utm_medium | utm_campaign | Sessions (2 weeks) |
| --- | --- | --- | --- | --- |
| Instagram bio | instagram | social | bio_link | 96 |
| WhatsApp Status | whatsapp | social | status_timetable | 41 |
| YouTube description | youtube | social | gym_tour | 18 |

Instagram sent the most visitors, but WhatsApp visitors stayed on the page longer and more of them messaged afterwards. The gym kept the bio link and started posting the timetable on Status every Monday.

(Made-up numbers to show the method.)
""",
    resources=[
        ('ga4-setup', 'Read the four setup steps', '10 min'),
        ('sites-ga', 'Read how to connect Analytics to Google Sites', '5 min'),
        ('gsites', 'Read how to create and publish a Google Site', '5 min'),
        ('ga4-utm', 'Read the UTM rules and the example', '10 min'),
        ('ga-builder', 'Open the Campaign URL Builder', '5 min'),
        ('ga4-traffic', 'Read how to find and read the Traffic acquisition report', '5 min'),
        ('ga-academy', 'Optional: note the free Analytics Academy courses for later', '5 min'),
    ],
    steps=[
        'Study the resources (about 45 minutes).',
        'Create a one-page Google Site (or use a page you already have) and publish it.',
        'Create a GA4 property and web data stream, and add the Measurement ID to the site. Check Realtime from your phone.',
        'Write your UTM naming rules (lowercase, underscores) and make 3 UTM links with the Campaign URL Builder: Instagram bio, WhatsApp Status or Channel, and a YouTube description.',
        'Use them for at least 7 days, then read the Traffic acquisition report and note sessions by source and campaign.',
    ],
    proof='Your published site link, a screenshot of GA4 Realtime or Traffic acquisition showing your UTM sources, and your UTM tracker sheet.',
    fulltime='Leave the UTM links running while you continue; read the report after 7 real days.',
    templates=[
        ('UTM naming rules and tracker', """
RULES: lowercase only; underscores, no spaces;
       source = the platform; medium = social / paid_social /
       email / qr; campaign = what or when (bio_link,
       onam_2026, pilot_week1); no personal data
Link name,Destination URL,utm_source,utm_medium,utm_campaign,utm_content,Full UTM link,Where used,Date added
""", ''),
        ('GA4 setup checklist', """
[ ] Account created (analytics.google.com)
[ ] Property: name, India time zone, INR
[ ] Web data stream with the site URL
[ ] Enhanced measurement on
[ ] Measurement ID (G-...) added to the site
[ ] Realtime shows my own visit
[ ] 3 UTM links in use, recorded in the tracker
[ ] After 7 days: Reports > Acquisition > Traffic acquisition
""", ''),
    ],
    mistakes=[
        ('Mixed capitals in UTMs.', '"Instagram" and "instagram" become two sources. Use lowercase always.'),
        ('Missing source, medium or campaign.', 'You\'ll see "(not set)". Always use all three.'),
        ('Expecting GA4 to track WhatsApp chats.', 'It can\'t; use keywords, labels and asking customers.'),
        ('Personal data in links.', 'Never put names or phone numbers in UTMs.'),
    ],
    quiz=[
        {'q': 'Which three UTM parameters should you always use?',
         'o': ['utm_term, utm_id, utm_content', 'utm_source, utm_medium, utm_campaign', 'utm_name, utm_phone, utm_city', 'None'],
         'a': 'B', 'why': 'Google says to always use these three.'},
        {'q': 'Why must UTM values be lowercase every time?',
         'o': ['They are case-sensitive, so different capitals split your data', 'Capitals are illegal', 'It hides them', 'GA4 deletes capitals'],
         'a': 'A', 'why': 'utm_source=google and utm_source=Google are different values.'},
        {'q': 'Where do you see which platform sent visitors in GA4?',
         'o': ['Admin → Property settings', 'Reports → Acquisition → Traffic acquisition', 'Realtime only', 'YouTube Studio'],
         'a': 'B', 'why': 'The report shows session source / medium and campaign.'},
        {'q': 'How should you measure enquiries from a WhatsApp click-to-chat link?',
         'o': ['GA4 tracks them automatically', 'With CTA keywords, WhatsApp labels and asking customers', 'You can\'t measure them at all', 'With UTMs inside the chat'],
         'a': 'B', 'why': 'The link opens a chat, not a website, so GA4 can\'t see it.'},
    ],
    study='Google\'s GA4 setup, Sites, UTM and Traffic acquisition guides (about 45 minutes)',
    action='set up GA4 on a simple Google Site, run 3 UTM links for 7 days and read the results',
)

L3 = lesson(
    8, 3,
    title='A/B tests and client reports',
    weeks=(21, 21), hours=3,
    outcome='Run fair A/B tests with the tools platforms provide, judge results honestly, and write a monthly report that a busy shop owner can understand in two minutes.',
    split='40 minutes study, 2 hours 20 minutes action',
    core=f"""
### Testing on social media is noisy

Every post is different: the topic, the day, the weather, what else was trending. So a "test" between two different posts is never perfectly fair. You can still learn a lot if you:

1. **Write a hypothesis first:** "A question hook will get more 3-second views than a result-first hook on food Reels."
2. **Change one thing** and keep everything else as similar as you can.
3. **Repeat it:** at least 3–4 posts per version, or use a tool that splits the audience for you.
4. **Choose the metric before you start:** the one that matches the hypothesis.
5. **Decide:** keep, drop or test again, and write it in the Experiments tab.

### Tools that split the audience for you ({ASOF})

- **YouTube Test & compare:** test up to three titles, three thumbnails or combinations on a long video. YouTube shows the versions to different viewers and picks the winner by **watch time**, not clicks, usually within two weeks. It works in YouTube Studio on a computer only, not for Shorts, and needs advanced features turned on. Your old laptop is enough.
- **Instagram trial reels:** show a reel to non-followers first and see how it does after about 24 hours, before deciding whether to share it with followers. Useful for testing a risky idea.
- **Meta Ads A/B tests:** in Ads Manager (Module 9), with a budget.

### How sure can you be?

With small accounts, most results are **directional**. Say "this seemed to work, we'll test it again" rather than "this works". If a difference repeats in two or three tests, act on it.

### The monthly client report

Owners are busy. A good report fits on **one page**, with details after it:

1. **Goal and KPI:** "Goal: more weekday orders. KPI: WhatsApp chats from Instagram. Target: 30 a month."
2. **Headline numbers:** this month against last month and the target, with arrows and plain words.
3. **What worked:** the top 3 posts with one-line reasons.
4. **What didn't,** honestly, and why you think so.
5. **What we tested and learned.**
6. **Next month's plan:** 3 actions.
7. **What I need from you:** photos, offers, approvals.

Write in plain language (Malayalam for owners who prefer it), show screenshots, and never claim results you can't connect to your work. A short **weekly WhatsApp update** ("This week: 4 posts, 2,300 views, 11 chats; best post was ...") keeps clients confident between reports.
""",
    example="""
Anu wrote a practice report for her own page after the challenge (made-up numbers):

> **@kuttiady.diaries, report for 1–30 November**
> **Goal:** become the page local people share. **KPIs:** views per post, shares per 1,000 views, local followers.
> **Headline:** 30 posts (target 30) ✅. Average 7-day views 1,150 (October: 310) ⬆. Shares per 1,000 views 13 (October: 6) ⬆. Followers 1,640 (start 820) ⬆.
> **What worked:** shop stories (19 shares per 1,000), collabs (most follows per view), question hooks (small lead, re-testing).
> **What didn't:** text-heavy updates (3 shares per 1,000) → moving to the WhatsApp Channel.
> **Tested:** posting at 1 pm vs 7:30 pm: similar views, faster replies at 7:30 pm.
> **December plan:** 2 shop stories a week; 1 collab; test 15 vs 30 seconds again.
> **Needs:** permission from 4 more shops for stories.

She also ran a Test & compare on her first long video's thumbnail from the laptop: the version with a face won on watch time.
""",
    resources=[
        ('yt-abtest', 'Read how Test & compare works, its limits and how the winner is chosen', '10 min'),
        ('tc-trial', 'Re-read how trial reels work', '3 min'),
        ('ig-reels-2025', 'Re-read the trial reels tip', '3 min'),
        ('dcn-boost', 'Read the part on A/B testing in Ads Manager (you\'ll use it in Module 9)', '5 min'),
        ('hubspot-social', 'Watch the lesson on reporting and ROI (lesson names may change)', '15 min'),
    ],
    steps=[
        'Study the resources (about 35 minutes).',
        'Plan one A/B test with the template: a YouTube Test & compare on a long video (on the laptop), a trial reel test, or a two-version test across 3–4 posts each.',
        'Run it, and record the result honestly as strong or directional in the Experiments tab.',
        'Write a one-page monthly report for your own account using the template, with screenshots.',
        'Write a weekly WhatsApp update for a pretend client in Malayalam or English.',
    ],
    proof='Your A/B test plan and result, your one-page monthly report and your weekly WhatsApp update.',
    templates=[
        ('A/B test plan', """
HYPOTHESIS: If I ________, then ________ will rise,
            because ________.
ONE CHANGE: version A ________ / version B ________
KEPT THE SAME: topic type, length, time, day, pillar
TOOL: Test & compare / trial reel / 3-4 posts each
METRIC (chosen before): ________
RESULT: A ____ B ____  Confidence: strong / directional
DECISION: keep / drop / test again on ____
""", ''),
        ('monthly report (one page)', """
[BUSINESS or ACCOUNT] - SOCIAL MEDIA REPORT, [MONTH]
GOAL: ______________  KPI: ____________  TARGET: ____
HEADLINE NUMBERS     This month  Last month  Target
  [KPI]              ____        ____        ____
  Posts              ____        ____        ____
  Views/reach        ____        ____
  Enquiries (chats)  ____        ____
WHAT WORKED (top 3 posts): 1. ____ 2. ____ 3. ____
WHAT DIDN'T, AND WHY: ____________________________
WHAT WE TESTED: __________ RESULT: _____________
NEXT MONTH (3 actions): 1. ____ 2. ____ 3. ____
WHAT I NEED FROM YOU: ____________________________
(Screenshots and full numbers on the next pages)
""", ''),
        ('weekly WhatsApp update', """
EN: Hi [name], this week on Instagram: [n] posts,
[n] views, [n] WhatsApp chats. Best post: [link]
([reason]). Next week: [plan]. Can you send [photos/offer]
by [day]?
ML: നമസ്കാരം [പേര്], ഈ ആഴ്ച: [n] പോസ്റ്റുകൾ, [n] വ്യൂസ്,
[n] വാട്സാപ്പ് ചാറ്റുകൾ. മികച്ച പോസ്റ്റ്: [link].
അടുത്ത ആഴ്ച: [പ്ലാൻ]. [ഫോട്ടോ/ഓഫർ] [ദിവസം] മുൻപ് അയക്കാമോ?
""", ''),
    ],
    mistakes=[
        ('Calling one comparison "proof".', 'Say directional, and re-test.'),
        ('Changing the metric after seeing the results.', 'Choose it before the test.'),
        ('Ten-page reports nobody reads.', 'One page first; details after.'),
        ('Taking credit for everything.', 'Say what you can connect to your work and what you can\'t.'),
    ],
    quiz=[
        {'q': 'How does YouTube\'s Test & compare decide the winning thumbnail?',
         'o': ['Most clicks', 'Highest watch time', 'Most likes', 'Your choice'],
         'a': 'B', 'why': 'YouTube optimises these tests for watch time.'},
        {'q': 'Which is a well-written hypothesis?',
         'o': ['"Let\'s see what happens"', '"If I use a question hook on food Reels, 3-second views will rise, because it creates curiosity"', '"Post more"', '"Make it viral"'],
         'a': 'B', 'why': 'It names one change, one metric and a reason.'},
        {'q': 'What should come first in a monthly client report?',
         'o': ['Every post\'s screenshot', 'The goal, KPI and headline numbers against last month and the target', 'Your hourly rate', 'Hashtags used'],
         'a': 'B', 'why': 'Owners need the result in two minutes; details can follow.'},
        {'q': 'Where can you run YouTube Test & compare?',
         'o': ['On the phone app', 'In YouTube Studio on a computer, for long videos', 'On Shorts only', 'In Instagram'],
         'a': 'B', 'why': 'It is computer-only and not available for Shorts.'},
    ],
    study='YouTube\'s Test & compare, Instagram trial reels, A/B testing in ads and HubSpot\'s reporting lesson (about 35 minutes)',
    action='run one A/B test, write a one-page monthly report and a weekly WhatsApp update',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    8,
    title='Analytics',
    weeks=(19, 21), hours=12,
    overview="""
Measure what matters, find patterns in your numbers, track visits with Google Analytics and UTM links, test fairly, and report results clearly. Then turn your 30-day challenge into your first case study.

Numbers are only useful when they change what you do next. In three weeks you'll learn the metrics that matter on each platform and the ratios that compare posts fairly, set up Google Analytics 4 on a simple site with UTM links, run A/B tests with YouTube's and Instagram's own tools, and write the kind of one-page report that keeps clients.

The module project is your first portfolio piece: a results report on your 30-day challenge, with real before and after numbers.
""",
    outcomes=[
        'Find and explain the key metrics in Instagram, YouTube, WhatsApp, Facebook and LinkedIn',
        'Calculate share, save, follow and engagement rates and compare groups of posts',
        'Set up GA4 with UTM links and read the Traffic acquisition report',
        'Run fair A/B tests and judge how sure you can be',
        'Write a one-page monthly report and a weekly client update',
    ],
    lessons=LESSONS,
    project='Case study 1: your 30-day challenge results report',
    project_steps=[
        'Use your challenge data, your ratio analysis and your day-30 summary.',
        'Write a one-to-two-page case study with the template in SMM-M12-L02 if you want to look ahead, or simply: the goal, the starting numbers (week 0 baseline and the week before the challenge), what you did, the results after 30 days, the top 3 learnings and what you\'ll do next.',
        'Include 3–5 screenshots of Insights or Studio.',
        'Use only real numbers, and say which results are directional.',
        'Save it in 08 Analytics and 12 Portfolio.',
    ],
    project_proof='Your case study document with before and after numbers and screenshots.',
    fulltime='Your challenge may still be running. Analyse the days you have now, then finish the case study as soon as day 30 is done.',
    rubric=[
        ('Metrics', 'Only looks at likes', 'Knows the main metrics', 'Explains each platform\'s key metrics and where to find them'),
        ('Analysis', 'Reads single posts', 'Some ratios', 'Ratios and group comparisons turned into decisions'),
        ('Tracking', 'No tracking', 'GA4 or UTMs, not both', 'GA4 working with consistent UTM links and a tracker'),
        ('Testing', 'No tests', 'Tests without hypotheses', 'Planned tests with one change, a set metric and honest confidence'),
        ('Reporting', 'No report', 'Long or unclear report', 'A one-page report a busy owner understands, plus a case study'),
    ],
    short=[
        'Calculate share rate and follow rate for your challenge posts only.',
        'Make one UTM link for your Instagram bio (GA4 setup can wait).',
        'Skip the A/B test; write the monthly report.',
        'Write a half-page case study.',
    ],
    flashcards=[
        ('Instagram\'s main metric since August 2024?', 'Views.'),
        ('Share rate formula?', 'Shares ÷ views × 1,000.'),
        ('What does YouTube impressions CTR show?', 'How often an impression of your thumbnail led to a view.'),
        ('Three UTM parameters to always use?', 'utm_source, utm_medium, utm_campaign.'),
        ('Where are UTM results in GA4?', 'Reports → Acquisition → Traffic acquisition.'),
        ('How does Test & compare choose a winner?', 'Watch time.'),
        ('Two YouTube Test & compare limits?', 'Computer only; not for Shorts (also needs advanced features).'),
        ('First things in a monthly report?', 'Goal, KPI and headline numbers against last month and the target.'),
    ],
    mistakes=[
        ('Collecting numbers without decisions.', 'Every report ends with three actions.'),
        ('Hiding bad months.', 'Clients trust honest reports; explain and show the plan.'),
        ('Inventing or rounding up results.', 'Use exact, real numbers. Your reputation depends on it.'),
    ],
)
