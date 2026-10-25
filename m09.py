from common import lesson, module, link, ASOF

L1 = lesson(
    9, 1,
    title='Boosting vs Ads Manager: objectives, setup and policies',
    weeks=(22, 22), hours=3.5,
    outcome='Decide when an ad is worth paying for, choose between boosting a post and an Ads Manager campaign, pick the right objective, and set up an ad account safely and within the rules.',
    split='1 hour 15 minutes study, 2 hours 15 minutes action',
    core=f"""
### Organic first, then pay to amplify

Ads don't fix weak content; they show it to more people faster. The safest small-budget approach:

1. Post organically and find what works (Modules 6–8).
2. Put money behind a post or offer that already does well, or an offer with a real deadline.
3. Measure the cost of each result (a message, a booking, an order) and compare it with what that result is worth.

### Boosting or Ads Manager?

| | **Boost a post** | **Ads Manager campaign** |
| --- | --- | --- |
| Where | From the post, the Instagram or Facebook app, or Meta Business Suite | Ads Manager (in Meta Business Suite, or on a computer) |
| Goals | Basic: engagement, profile visits, website visits, messages | Full range of campaign objectives, including leads and sales |
| Targeting | Simple | Detailed: location, age, interests, custom and lookalike audiences |
| Placements and formats | Limited | Choose placements (Reels, Stories, Feed, Messenger); video, carousel and Stories ads |
| Testing and reports | Basic insights | A/B tests and detailed reports |
| Best for | A quick, small push for one good post | A planned test with a clear goal, running at least a week |

(Based on the Digital Culture Network's comparison, updated September 2026. Boost options change often; check what your app shows.)

### Choosing an objective

Ads Manager asks for your **objective** first, and the system then shows your ad to the people most likely to do that thing. As of October 2026 Ads Manager groups its objectives into six: **Awareness, Traffic, Engagement, Leads, App promotion and Sales** (check the current names in Ads Manager). For a small local business:

- Reach people nearby who haven't heard of you → **Awareness**
- Get people to message you on WhatsApp, Messenger or Instagram → an objective with **messages** as the conversion location (Meta's free Blueprint course "Selecting campaign objectives" explains conversion locations)
- Collect enquiries with a form → **Leads**
- Online sales on a website → **Sales** (needs tracking set up)

Pick the objective that matches the result you will pay for. Asking for "engagement" when you want orders gets you likes, not orders.

### Setting up an ad account safely

The Digital Culture Network's checklist (updated October 2026):

- Use your **real personal Facebook profile**; Meta often disables obviously fake ones.
- Have **admin access** to the Facebook Page and Instagram account you'll advertise.
- Keep the Page, Instagram account and ad account in one **Business Portfolio** in Meta Business Suite.
- Add a payment method and set a **monthly spending limit** as a safety net.
- The **Meta Pixel** (code on a website that tracks what people do after clicking) is optional for beginners; if you add it, the website's privacy policy must mention it.

**Taxes:** ad purchases can attract GST. Google's help page, for example, says Google Asia Pacific charges 18% GST on Google Ads purchases in India unless a valid GSTIN is given. Check the taxes shown on Meta's billing screen before you pay, and budget for them.

### Advertising rules

- Ads must follow Meta's advertising standards. Ads about **social issues, elections or politics** have extra requirements, including authorisation and disclaimers; keep clients' ads away from them unless you know the rules.
- Advertisers must disclose when certain political or social issue ads were digitally created or altered, and Meta labels AI-generated content ({ASOF}).
- Indian law applies to ads too: no misleading claims, no fake urgency, no unqualified health or money promises (SMM-M05-L02, Module 14).
- Use **Meta's Ad Library** to see the ads that other Pages are running; it's the free way to learn what local competitors advertise.
""",
    example="""
Nisha's Oven had two options for Christmas:

- **Boost** her best-performing Reel (a plum cake being sliced, 6,000 organic views) for ₹300 over 3 days to people within about 8 km, goal "messages".
- **Ads Manager campaign:** a 7-day campaign with a messages goal, three different videos, a 10 km radius around Kuttiady, and a spending limit of ₹1,500.

She chose to boost first, because it was quick and her post had already proved itself. It brought 19 WhatsApp chats and 7 orders. Encouraged, she planned an Ads Manager campaign for the next festival, to test which of three videos brought chats most cheaply.

Before either, she checked Meta's Ad Library: two bakeries in town were running Christmas ads, both with discounts and no price. Hers showed the price clearly.

(Made-up example to show the method.)
""",
    resources=[
        ('dcn-boost', 'Read the whole comparison of boosted posts and ad campaigns', '10 min'),
        ('dcn-setup', 'Read what you need to set up Meta ads', '10 min'),
        ('bp-ads', 'Free sign-up. Do all three 5-minute lessons', '15 min'),
        ('bp-objectives', 'Do both lessons on objectives and conversion locations', '16 min'),
        ('meta-ad-library', 'Open the Ad Library and search for 5 local businesses', '10 min'),
        ('meta-siep', 'Note the extra rules for social issue, election and political ads', '5 min'),
        ('gads-tax', 'Read the India section on GST', '5 min'),
    ],
    steps=[
        'Study the resources (about 1 hour 10 minutes).',
        'Set up (or check) a Business Portfolio with your Page, Instagram account and an ad account, following the checklist. Set a low monthly spending limit. Don\'t run an ad yet.',
        'For three scenarios (a bakery wanting orders, a homestay wanting bookings, your page wanting local followers), write which you\'d use (boost or Ads Manager) and which objective, with one sentence why.',
        'Search Meta\'s Ad Library for 5 businesses in your area or niche. For each, note the creative, the message, the call to action and how long the ad has run.',
    ],
    proof='A screenshot of your set-up (with personal details hidden), your three scenario decisions and your Ad Library notes on 5 advertisers.',
    templates=[
        ('ad readiness checklist', """
[ ] The post or offer already works organically
    (or has a real deadline)
[ ] One clear result to pay for (messages / leads /
    sales / reach)
[ ] Real personal profile; admin on Page and Instagram
[ ] Business Portfolio with Page + Instagram + ad account
[ ] Payment method added; monthly spending limit set
[ ] Taxes (GST) included in the budget
[ ] WhatsApp quick replies and labels ready for chats
[ ] Claims checked: no misleading, health or money promises
[ ] Not a social issue, election or political ad
""", ''),
        ('objective chooser', """
I want people to...                   -> choose
  notice us nearby                    -> Awareness
  visit our website                   -> Traffic
  message us (WhatsApp/Messenger/DM)  -> an objective with
                                         messages as the
                                         conversion location
  fill in an enquiry form             -> Leads
  buy on our website                  -> Sales (needs tracking)
  install our app                     -> App promotion
Boost when: one proven post, small budget, quick push.
Ads Manager when: a planned test, several creatives,
  detailed targeting, a week or more.
""", ''),
    ],
    mistakes=[
        ('Boosting a weak post.', 'If it didn\'t interest people for free, paying shows it to more people who won\'t care.'),
        ('The wrong objective.', 'Paying for engagement when you want orders buys likes.'),
        ('No spending limit.', 'Set a monthly limit before your first ad.'),
        ('Forgetting GST.', 'Budget for taxes on top of the ad spend.'),
        ('Fake or dummy profiles.', 'Meta often disables them, and your ad account with them.'),
    ],
    quiz=[
        {'q': 'When is boosting a post a sensible choice?',
         'o': ['For a planned test of three creatives', 'For a quick, small push of one post that already performed well', 'For political ads', 'Never'],
         'a': 'B', 'why': 'Boosts are simple; Ads Manager is better for planned tests.'},
        {'q': 'A homestay wants WhatsApp enquiries from an ad. What should it choose?',
         'o': ['An Awareness objective with no CTA', 'An objective with messages as the conversion location', 'App promotion', 'Nothing, just post more'],
         'a': 'B', 'why': 'Choose the objective that matches the result you will pay for.'},
        {'q': 'What should you set before running your first ad?',
         'o': ['A monthly spending limit', 'A fake profile', 'A political disclaimer', 'Ten hashtags'],
         'a': 'A', 'why': 'A limit protects you from overspending.'},
        {'q': 'What does Meta\'s Ad Library let you do?',
         'o': ['See competitors\' private results', 'See the ads that Pages are running', 'Buy cheaper ads', 'Remove ads'],
         'a': 'B', 'why': 'It is a free transparency tool for learning from others\' ads.'},
    ],
    study='The Digital Culture Network\'s guides, three free Meta Blueprint courses, the Ad Library and the tax rules (about 1 hour 10 minutes)',
    action='set up an ad account safely, choose objectives for three scenarios and study 5 advertisers in the Ad Library',
)

L2 = lesson(
    9, 2,
    title='Targeting, small budgets and creative testing',
    weeks=(23, 23), hours=3.5,
    outcome='Choose a sensible audience for a local business, plan a small test budget in rupees, and test two or three creatives so that the numbers tell you which message works.',
    split='45 minutes study, 2 hours 45 minutes action',
    core=f"""
### Audiences, from broad to narrow

| Audience | What it is | When to use it |
| --- | --- | --- |
| **Location + age** | People in or near a place, in an age range | Almost every local business: a radius around the shop |
| **Advantage+ audience** | Meta's automated targeting, which looks for the people most likely to get your result | Often a good default when the creative is clear; Meta Blueprint has a short free video on it |
| **Interests** | People Meta thinks are interested in a topic | When your product clearly fits an interest; don't stack many |
| **Custom audiences** | People who already interacted: watched your videos, engaged with your Page or Instagram, visited your website (with the Pixel), or a customer list | Retargeting (SMM-M09-L3). Customer lists only if people agreed when you collected their details |
| **Lookalike audiences** | New people similar to a custom audience | Later, once you have a few hundred engaged people or customers |

For a shop in Kuttiady, start simple: a radius around the shop that matches its real delivery or travel area, sensible ages, and either broad targeting or Advantage+ audience. With small budgets, narrow targeting often just makes ads cost more.

### Small budgets: plan in rupees

You don't need lakhs to learn. A test budget of **₹500–₹1,000 plus GST**, spread over 5–7 days, is enough to compare two or three creatives directionally. Ads Manager shows the minimum it will accept when you set a daily or lifetime budget. Decide in advance:

- **Daily or lifetime budget:** lifetime budgets stop automatically at the total.
- **How long:** at least 5–7 days, so the system has time to find people.
- **The result you're buying** and the most you'll pay for it (your break-even, SMM-M09-L03).

### Creative is the biggest lever

The audience and the budget matter, but the **ad itself** decides most results. Test creatives, not tiny settings:

- **Two or three versions** with different hooks or angles: price-first, result-first, a customer story.
- **Made for the placement:** vertical video for Reels and Stories, with captions. Meta's free Blueprint videos include one on adding Reels placements to campaigns.
- **The first 3 seconds** carry the message, as in organic posts.
- **One offer, one call to action,** and a clear price where possible.
- Ads Manager's **A/B test** feature can split the audience between versions; or put the versions in one ad set and compare cost per result.

### The numbers to watch

- **CPM:** cost per 1,000 impressions (how expensive it is to reach people)
- **CTR:** clicks ÷ impressions (how interesting the ad is)
- **Cost per result:** spend ÷ results (messages, leads, orders); the number that matters
- **Frequency:** how many times each person saw it on average; if it climbs high, people get tired of it

Small tests give **directional** answers. If one creative gets messages at half the cost of the others, that's a useful signal to test again with more budget.
""",
    example="""
Peak Fitness ran a 7-day test with ₹1,050 plus GST (made-up numbers to show the method):

- **Audience:** about 6 km around the gym, ages 20–45, Advantage+ audience
- **Result:** WhatsApp messages
- **Three Reels:** A "First session free" (offer-first), B a trainer fixing a squat (value-first), C a member's 90-day story (shared with her written permission)

| Creative | Spend (₹) | Messages | Cost per message (₹) |
| --- | --- | --- | --- |
| A Offer-first | 350 | 9 | 39 |
| B Value-first | 350 | 14 | 25 |
| C Member story | 350 | 6 | 58 |

Eleven of the 29 people who messaged booked a free session and 4 joined (₹1,500 a month each). The value-first Reel won this round; they planned to re-test it against a new member story before spending more.
""",
    resources=[
        ('bp-audiences', 'Do both lessons on audience types and creating audiences', '10 min'),
        ('bp-free', 'Watch "Use Advantage+ audience" and "Include Reels placements in your campaigns"', '5 min'),
        ('dcn-audience', 'Read cold, custom and lookalike audiences and the advice on ad fatigue', '10 min'),
        ('dcn-boost', 'Re-read the part on A/B testing', '5 min'),
        ('gads-copy', 'Re-read the advice on genuine, benefit-led copy', '5 min'),
    ],
    steps=[
        'Study the resources (about 35 minutes).',
        'Choose a real scenario: your page (for example, more local followers or "suggest a spot" messages) or a friendly local business.',
        'Write an audience plan: location and radius, ages, and broad, Advantage+ or interests, with your reason.',
        'Plan a budget in rupees including GST, with duration and the most you\'ll pay per result.',
        'Make 2–3 ad creatives with different hooks, sized for Reels and Stories, with captions and one CTA.',
        'Write the test plan. (You\'ll decide in the module project whether to run it.)',
    ],
    proof='Your audience plan, budget plan, 2–3 creatives and the complete test plan.',
    templates=[
        ('ad test plan', """
BUSINESS / PAGE: ______________  DATES: ____ to ____
RESULT I'M BUYING: messages / leads / follows / visits
MOST I'LL PAY PER RESULT: Rs ____ (break-even: Rs ____)
AUDIENCE: radius ___ km around ______; ages ___-___;
          broad / Advantage+ / interests: ________
BUDGET: Rs ____ + GST, lifetime, ___ days
CREATIVES: A ________ B ________ C ________
           (hook, offer, CTA for each)
PLACEMENTS: Reels / Stories / Feed (vertical first)
SUCCESS RULE: if one creative's cost per result is
  below Rs ____ after 5 days, re-test it with Rs ____
""", ''),
        ('budget calculator', """
Ad budget (Rs)                     A = ______
GST (check the rate on the bill)   B = A x ___% = ____
Total cost                         C = A + B = ______
Expected cost per result (guess)   D = ______
Expected results                   E = A / D = ______
Value of one result to the business F = ______
Worth it if                        E x F > C
""", ''),
    ],
    mistakes=[
        ('Very narrow targeting on a tiny budget.', 'It often raises costs. Start broad or with Advantage+ within your real area.'),
        ('Testing settings instead of creatives.', 'The ad\'s message matters most; test hooks and angles.'),
        ('Judging after one day.', 'Give a test 5–7 days.'),
        ('Customer lists without consent.', 'Upload lists only if people agreed when you collected their details.'),
        ('Horizontal videos for Reels ads.', 'Make vertical versions with captions.'),
    ],
    quiz=[
        {'q': 'For a small local test, which audience is usually a good start?',
         'o': ['Ten stacked interests across India', 'A radius around the shop with broad targeting or Advantage+ audience', 'A bought email list', 'Everyone over 13'],
         'a': 'B', 'why': 'Simple local targeting gives the system room to find the right people.'},
        {'q': 'Which number matters most when judging a messages campaign?',
         'o': ['Likes', 'Cost per message (and how many messages became customers)', 'Impressions only', 'Followers'],
         'a': 'B', 'why': 'You are paying for messages that lead to customers.'},
        {'q': 'What is the biggest lever in most small ad campaigns?',
         'o': ['The creative (hook, message, offer)', 'The time zone', 'The ad account name', 'The number of hashtags'],
         'a': 'A', 'why': 'Test different creatives, not tiny settings.'},
        {'q': 'When can you upload a customer list for a custom audience?',
         'o': ['Always', 'Only if people agreed when you collected their details', 'Never', 'Only for political ads'],
         'a': 'B', 'why': 'Consent is needed, as the Digital Culture Network\'s guide stresses.'},
    ],
    study='Meta Blueprint\'s audience courses and videos and the Digital Culture Network\'s audience guide (about 35 minutes)',
    action='plan an audience, a rupee budget and 2–3 creatives in a complete ad test plan',
)

L3 = lesson(
    9, 3,
    title='Retargeting, Click-to-WhatsApp, YouTube and Google ads, and ROI',
    weeks=(24, 24), hours=3,
    outcome='Plan a retargeting audience and a Click-to-WhatsApp ad, understand YouTube and Google ad formats, and calculate whether an ad made or lost money.',
    split='40 minutes study, 2 hours 20 minutes action',
    core=f"""
### Retargeting: talk to people who already know you

Retargeting means showing ads to people who have already interacted with you: watched your videos, engaged with your Instagram or Facebook, visited your website (tracked with the Meta Pixel) or are on a customer list they agreed to. They are warmer, so the message can be more direct: "Still thinking about that cake? Order by 6 pm." Vary the creative so the same people don't see one ad again and again.

### Click-to-WhatsApp ads

For many Kerala businesses the best ad sends people straight into a WhatsApp chat. WhatsApp's own business pages list **ads that click to WhatsApp** among the app's tools, and you can start them from the WhatsApp Business app or set WhatsApp as the destination in Ads Manager. Before you start:

- quick replies ready for price, delivery and payment
- labels for "From ad", "Ordered", "Not ordered"
- someone available to reply quickly during the ad's hours
- a keyword in the pre-filled message or CTA so you can count chats from the ad

### YouTube and Google ads in one page ({ASOF})

Google's free **Skillshop** has learning paths and certifications for Search, Display, Video, Shopping and Measurement. The basics:

- **Skippable in-stream video ads:** viewers can skip after 5 seconds. With cost-per-view bidding you pay when someone watches 30 seconds (or the whole ad if shorter) or interacts.
- **Non-skippable in-stream:** up to 60 seconds; paid per thousand impressions.
- **Bumper ads:** non-skippable, about 6 seconds; paid per thousand impressions.
- **In-feed video ads:** a thumbnail and text inviting people to click and watch.
- **Shorts ads:** between Shorts; viewers can swipe past straight away.
- **Search ads** (Google Ads): text ads shown to people searching, for example "mobile display change Kuttiady". They catch people who already want something, which suits local services.

Google charges 18% GST on Google Ads purchases in India unless a valid GSTIN is given (check current rules).

### Did the ad make money?

Work it out every time:

- **Cost per result** = total cost (with GST) ÷ results
- **Conversion rate** = customers ÷ results (for example, orders ÷ chats)
- **Cost per customer** = total cost ÷ customers
- **ROAS** (return on ad spend) = revenue from the ad ÷ ad spend
- **Profit** = (revenue × margin) − total ad cost
- **ROI** = profit ÷ total ad cost × 100

The **break-even cost per customer** is the profit you make on one customer's purchase (or on their first few purchases if they usually come back). If an ad costs more than that per customer, it loses money, however many likes it gets.
""",
    example="""
**Amma's Pickles** ran a Click-to-WhatsApp ad for 6 days (made-up numbers to show the method):

| Item | Number |
| --- | --- |
| Ad spend | ₹800 |
| GST at 18% (as shown on the bill) | ₹144 |
| Total cost | ₹944 |
| WhatsApp chats from the ad (keyword "PICKLE") | 46 |
| Orders | 12 |
| Average order | ₹300 |
| Revenue | ₹3,600 |
| Margin after ingredients, jars and delivery (40%) | ₹1,440 |
| Profit after the ad | ₹1,440 − ₹944 = ₹496 |
| Cost per chat / per customer | ₹21 / ₹79 |
| ROAS | ₹3,600 ÷ ₹800 = 4.5 |

The ad made a small profit on the first orders, and five of the twelve customers re-ordered within a month, so it was worth more than it first looked. They also learned that chats arriving after 9 pm rarely became orders, so they set the ad to run during the day.
""",
    resources=[
        ('wa-tools', 'Re-read the "ads that click to WhatsApp" part', '3 min'),
        ('dcn-audience', 'Re-read the retargeting section', '5 min'),
        ('gads-formats', 'Read the video ad formats and how you pay for each', '15 min'),
        ('skillshop-ads', 'Browse the free learning paths; note the Video and Search ones for later', '10 min'),
        ('gads-tax', 'Re-read the GST rules for India', '3 min'),
    ],
    steps=[
        'Study the resources (about 35 minutes).',
        'Write a retargeting plan for one business: who (video viewers, engagers, website visitors or customers with consent), what message, and how long.',
        'Write a Click-to-WhatsApp ad plan: creative, keyword, quick replies, labels and reply hours.',
        'Write one Google search ad idea for a local service: three short headlines and two descriptions, following Google\'s genuine copy advice.',
        'Use the ROI calculator on your Peak Fitness, Amma\'s Pickles or own test numbers and write whether the ad made money.',
    ],
    proof='Your retargeting plan, Click-to-WhatsApp plan, search ad idea and a completed ROI calculation with your conclusion.',
    templates=[
        ('ROI calculator', """
Ad spend (Rs)                     A = ______
GST and other charges (Rs)        B = ______
Total cost                        C = A + B = ______
Results (chats/leads)             R = ______
Customers                         N = ______
Revenue from those customers      V = ______
Margin %                          M = ______
Cost per result                   = C / R = ______
Conversion rate                   = N / R x 100 = ____%
Cost per customer                 = C / N = ______
ROAS                              = V / A = ______
Profit                            = V x M/100 - C = ______
ROI %                             = Profit / C x 100 = ____%
Break-even cost per customer      = profit on one
                                    customer's orders = ____
""", ''),
        ('Click-to-WhatsApp checklist', """
[ ] Destination: WhatsApp (from the WhatsApp Business app
    or Ads Manager)
[ ] Pre-filled message or CTA keyword: "_____"
[ ] Quick replies: price, delivery, payment, order steps
[ ] Labels: From ad / Ordered / Not ordered
[ ] Someone replies within ___ minutes during ad hours
[ ] Ad runs only during hours you can reply
[ ] Count chats and orders daily in a sheet
""", ''),
    ],
    mistakes=[
        ('Counting chats as sales.', 'Track how many chats became orders.'),
        ('Running WhatsApp ads when nobody can reply.', 'Slow replies waste the money. Run ads during reply hours.'),
        ('Ignoring GST and costs in ROI.', 'Use the total cost and the margin, not just revenue.'),
        ('Showing one retargeting ad for weeks.', 'Change the creative to avoid tiring people.'),
    ],
    quiz=[
        {'q': 'When can viewers skip a skippable in-stream YouTube ad?',
         'o': ['Immediately', 'After 5 seconds', 'After 30 seconds', 'Never'],
         'a': 'B', 'why': 'Google\'s format guide says viewers can skip after 5 seconds.'},
        {'q': 'An ad cost ₹944 in total and brought 12 customers. What was the cost per customer?',
         'o': ['About ₹79', '₹944', '₹12', 'About ₹20'],
         'a': 'A', 'why': '₹944 ÷ 12 is about ₹79.'},
        {'q': 'What is ROAS?',
         'o': ['Profit after tax', 'Revenue from the ad divided by ad spend', 'Number of chats', 'Cost per thousand impressions'],
         'a': 'B', 'why': 'Return on ad spend compares revenue with spend.'},
        {'q': 'Who is a retargeting audience?',
         'o': ['Random people in Kerala', 'People who already interacted with you, such as video viewers or website visitors', 'Competitors', 'Only new customers'],
         'a': 'B', 'why': 'Retargeting reaches warmer people with a more direct message.'},
    ],
    study='WhatsApp\'s ad tools, retargeting, Google\'s video ad formats, Skillshop and GST rules (about 35 minutes)',
    action='plan a retargeting audience, a Click-to-WhatsApp ad and a search ad, and calculate an ad\'s ROI',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    9,
    title='Paid ads',
    weeks=(22, 24), hours=11.5,
    overview="""
Learn to spend small amounts of money wisely: when to boost and when to use Ads Manager, how to choose objectives, audiences and budgets, how to test creatives, retarget and use Click-to-WhatsApp ads, the basics of YouTube and Google ads, and how to tell whether an ad made money.

Ads amplify what already works. In three weeks you'll set up an ad account safely, learn from other businesses\' ads in Meta's Ad Library, plan audiences and rupee budgets, test creatives, and calculate return on ad spend and profit.

Running a real ad is optional. The module project lets you choose a tiny test of ₹300–₹1,000 or a ₹0 dry run.
""",
    outcomes=[
        'Decide between boosting and an Ads Manager campaign',
        'Choose an objective that matches the result you\'re paying for',
        'Plan audiences, budgets and a creative test in rupees',
        'Plan retargeting and Click-to-WhatsApp ads, and explain YouTube and Google ad formats',
        'Calculate cost per result, ROAS, profit and ROI',
    ],
    lessons=LESSONS,
    project='Your ad plan and an optional tiny test ad',
    project_steps=[
        'Choose: run a tiny test (₹300–₹1,000 plus GST, your own money or a business that agrees to pay), or a ₹0 dry run.',
        'Tiny test: run your plan from SMM-M09-L02 for 5–7 days on a post that already did well organically, with a spending limit set. Track results daily.',
        'Dry run: build the full campaign in Ads Manager and save it as a draft without publishing, then write what you expect to happen and why.',
        'Either way, fill in the ROI calculator (with real or expected numbers) and write three lessons.',
        'Save screenshots with personal and payment details hidden.',
    ],
    project_proof='Your ad plan, screenshots of the test results or the saved draft, the ROI calculation and your three lessons.',
    rubric=[
        ('Decision', 'Boosts everything', 'Knows boost vs Ads Manager', 'Chooses the right tool and objective for each goal'),
        ('Set-up and rules', 'No limits, unclear ownership', 'Account set up', 'Portfolio, admin access, spending limit, policies and GST checked'),
        ('Targeting and budget', 'Random', 'Some plan', 'A local audience and a rupee budget with a break-even'),
        ('Creative testing', 'One ad', 'Two similar ads', '2–3 different creatives with a success rule'),
        ('ROI', 'Judges by likes', 'Counts results', 'Calculates cost per customer, ROAS, profit and ROI'),
    ],
    short=[
        'Do the three 5-minute Blueprint lessons and the Ad Library task.',
        'Write a test plan with two creatives.',
        'Do the ROI calculation with the Amma\'s Pickles example numbers.',
        'Choose the ₹0 dry run.',
    ],
    flashcards=[
        ('Boost or Ads Manager for a planned 3-creative test?', 'Ads Manager.'),
        ('Ads Manager\'s six objective groups (October 2026)?', 'Awareness, Traffic, Engagement, Leads, App promotion, Sales.'),
        ('Safety setting before your first ad?', 'A monthly spending limit.'),
        ('GST on Google Ads purchases in India without a GSTIN?', '18% (check current rules).'),
        ('Biggest lever in a small campaign?', 'The creative.'),
        ('Cost per result formula?', 'Total cost (with GST) ÷ results.'),
        ('ROAS formula?', 'Revenue from the ad ÷ ad spend.'),
        ('When can a skippable YouTube ad be skipped?', 'After 5 seconds.'),
        ('Customer lists for custom audiences need what?', 'Consent from the people when their details were collected.'),
    ],
    mistakes=[
        ('Spending before the organic content works.', 'Prove it organically first, then amplify.'),
        ('Hiding results from a client.', 'Report cost per customer honestly, good or bad.'),
        ('Promising results from ads.', 'Promise a clear test and honest numbers, not sales.'),
    ],
)
