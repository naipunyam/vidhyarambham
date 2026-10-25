from common import lesson, module, link, ASOF

L1 = lesson(
    10, 1,
    title='Micro-influencers and UGC for local brands',
    weeks=(25, 25), hours=3,
    outcome='Find and vet local creators with real audiences, brief them well, agree fair terms, and make sure every partnership and piece of user-generated content is disclosed and used with permission.',
    split='50 minutes study, 2 hours 10 minutes action',
    core=f"""
### Why micro-influencers suit local businesses

A celebrity reaches millions who will never visit a shop in Kuttiady. A local food page, a college page or a community admin with a few thousand followers reaches the right people, who trust them like a friend's recommendation. For small budgets, **micro-influencers** (creators with small but engaged, often local audiences) usually give better value than big names.

### Finding creators

- Search your area's place names and hashtags on Instagram and YouTube, and note who appears again and again.
- Ask customers which local pages they follow.
- Look at who local businesses already collaborate with (and whether those posts are disclosed).
- **Instagram's Creator Marketplace**, launched in India in February 2024, lets brands find creators through Meta Business Suite; access and features vary ({ASOF}).

### Vetting: is the audience real and right?

Before you offer anything, check:

| Check | How | Red flag |
| --- | --- | --- |
| **Local audience** | Ask for screenshots of Insights: top towns and cities, age ranges | Most followers outside Kerala for a local shop |
| **Real engagement** | Read comments on recent posts; compare views with follower count | Comments like "nice 🔥" from random accounts; tiny views for huge followings |
| **Growth pattern** | Ask how they grew; look at older posts | Sudden jumps in followers with no viral post |
| **Fit and values** | Watch 10 recent posts | Content that clashes with the brand, or hateful or risky posts |
| **Disclosure habits** | Look for "Ad", "Collaboration" or Paid partnership labels on past sponsored posts | Obvious sponsored posts with no label |

### Deal types

- **Barter:** a free product, meal or stay in exchange for content
- **Paid fee:** a fixed price for agreed posts
- **Commission:** a percentage of sales through a code or link
- **Discount code:** followers get a discount; you can count the orders

Ask for the creator's rate card and decide from expected results: compare the price with what reaching the same people with ads would cost (Module 9). Start with one small, clear deliverable.

### A good brief

A brief prevents disappointment on both sides: the goal, the key message, must-include details (price, location, timing, disclosure), claims the creator must not make, deliverables (for example 1 Reel and 3 Stories), dates, who approves what, whether the brand may reuse the content in ads (usage rights, often for an extra fee), and payment terms.

### Disclosure is not optional

Under ASCI's guidelines a **material connection** (payment, free products even if unsolicited, discounts, gifts, trips, barters, family or work ties) must be disclosed with a clear label such as **Ad, Sponsored, Collaboration, Partnership, Free gift** or **Affiliate**, placed where the audience can't miss it: at the start of the caption, superimposed on Stories and images without text, and on screen for a set time in videos. Platform tools such as Instagram's **Paid partnership** label are used as well. The government's "Endorsement Know-hows!" guide adds that endorsers shouldn't promote products they haven't personally used or vetted. Module 14 covers the full rules.

### UGC: content made by customers and creators

**User-generated content (UGC)** means content made by customers or creators rather than the brand: a customer's photo of their birthday cake, or a video a creator makes for the brand to use in its own ads.

- **Customers' posts:** ask before you repost, credit them, and keep the permission (a screenshot of their "yes").
- **Creator-made UGC for ads:** agree in writing how and where the brand may use it, for how long, and the fee.
- **UGC is not fake reviews.** Never ask people to pretend to be customers.
""",
    example="""
**Kakkayam Hills Homestay** wanted more monsoon weekend bookings. They shortlisted five travel creators from Kozhikode and vetted three:

| Creator (made up) | Followers | Average Reel views | Top city in Insights | Disclosure habit | Decision |
| --- | --- | --- | --- | --- | --- |
| @malabar.trails | 18,000 | 9,000 | Kozhikode | Labels "Collaboration" | ✅ Invite |
| @kerala.wanderer | 120,000 | 4,000 | Outside Kerala | No labels on obvious ads | ❌ |
| @weekend.kozhikode | 6,500 | 5,500 | Kozhikode | Labels "Free stay" | ✅ Invite |

They offered each a free one-night stay (barter) with a brief: show the balcony mist, the breakfast and the trek path, state the price (₹2,500 a night for two), tag the location, start the caption with "Collaboration (free stay)" and use Instagram's Paid partnership label; no claims like "safest trek in Kerala". The homestay could reshare the Reels on its own page with credit, but not use them as paid ads without asking.

Results over three weeks: 31 WhatsApp enquiries mentioning the creators, 9 bookings.

(Made-up example to show the method.)
""",
    resources=[
        ('asci-guidelines', 'Read the definitions, the list of labels and the placement rules for each format', '20 min'),
        ('asci-faqs', 'Re-read the FAQs on barters and free products', '10 min'),
        ('pib-endorse', 'Read the government\'s summary of the endorsement guide', '5 min'),
        ('mn-creator-mkt', 'Read what Instagram\'s Creator Marketplace offers in India', '5 min'),
        ('ig-best', 'In "Monetize", look at Partnership Ads and Creator Marketplace from the creator\'s side', '10 min'),
    ],
    steps=[
        'Study the resources (about 50 minutes).',
        'Choose a local business (real or the one you\'ll pilot in Module 11) and shortlist 5 local creators who could suit it.',
        'Vet 3 of them with the checklist, using public posts and, if you contact them, Insights screenshots they choose to share.',
        'Write a complete influencer brief for one of them.',
        'Write a permission message for reposting a customer\'s post (UGC), in Malayalam and English.',
        'Optional: carry out one small barter collaboration with correct disclosure and log the results.',
    ],
    proof='Your shortlist, three vetting sheets, the influencer brief and the UGC permission message (plus the collaboration post link if you did one).',
    templates=[
        ('creator vetting checklist', """
CREATOR: @________  Platform: ______  Date: ____
Followers: ____  Avg views (last 9 posts): ____
Views / followers: ____%
Top towns (Insights screenshot): __________
Age ranges: __________
Comments: real conversations / generic / bots
Follower jumps without a reason? Y / N
Content fit with the brand (1-5): ___
Values or risk concerns: __________
Discloses past sponsorships? Y / N
Decision: invite / maybe / no   Reason: ______
""", ''),
        ('influencer brief', """
BRAND: ______________  CREATOR: @____________
GOAL: ______________ (e.g. weekend booking enquiries)
KEY MESSAGE (one line): __________________________
MUST INCLUDE: price ____ / location tag / timing ____
DISCLOSURE: caption starts "Collaboration" / "Free
  gift" / "Ad"; label on screen in videos; Paid
  partnership tool switched on
DO NOT CLAIM: ___________________________________
DELIVERABLES: __ Reel(s), __ Stories, by ____ (date)
APPROVAL: brand sees the draft ___ days before posting
USAGE RIGHTS: reshare with credit Y/N; use as paid ad
  Y/N (fee: ____, for ___ months)
PAYMENT: barter (what) / fee Rs ____ / commission __%,
  paid within ___ days of posting
CONTACT: ______________
""", ''),
        ('UGC permission message', """
EN: Hi [name]! We loved your photo of [product]. Could we
share it on our page with credit to you? Reply YES if
that's okay. Thank you! 🙏
ML: നമസ്കാരം [പേര്]! [product]-ന്റെ നിങ്ങളുടെ ഫോട്ടോ ഞങ്ങൾക്ക് വളരെ
ഇഷ്ടമായി. നിങ്ങളുടെ പേര് സഹിതം ഞങ്ങളുടെ പേജിൽ ഷെയർ ചെയ്യട്ടെ?
സമ്മതമാണെങ്കിൽ YES എന്ന് മറുപടി തരൂ. നന്ദി! 🙏
(Save a screenshot of their reply.)
""", ''),
    ],
    mistakes=[
        ('Choosing by follower count.', 'Check views, comments and where the audience lives.'),
        ('No written brief.', 'Misunderstandings about claims, dates and rights are common. Write it down.'),
        ('Undisclosed barters.', 'A free stay or meal is a material connection; it must be labelled.'),
        ('Reposting customers without asking.', 'Ask, credit and keep the permission.'),
        ('Using creator videos as ads without agreement.', 'Agree usage rights and any fee first.'),
    ],
    quiz=[
        {'q': 'Which creator is the best fit for a Kuttiady shop?',
         'o': ['120,000 followers, mostly outside Kerala', '6,500 followers, mostly Kozhikode, real comments and labelled sponsorships', 'Anyone with a blue tick', 'A page that never shows its audience'],
         'a': 'B', 'why': 'A real, local, engaged audience and good disclosure habits matter most.'},
        {'q': 'A creator gets a free night at a homestay. What does ASCI expect?',
         'o': ['No label, since no money changed hands', 'A clear label such as "Collaboration" or "Free gift" where the audience can\'t miss it', 'A label in the bio only', 'A label at the end of a long caption'],
         'a': 'B', 'why': 'Free products and stays are material connections; labels must be upfront.'},
        {'q': 'Before reposting a customer\'s photo, you should:',
         'o': ['Just repost it', 'Ask permission, credit them and keep their reply', 'Remove their name', 'Edit it to look like your own'],
         'a': 'B', 'why': 'It is their content.'},
        {'q': 'What does "usage rights" in a brief decide?',
         'o': ['The creator\'s password', 'Whether and how the brand may reuse the creator\'s content, for example in ads', 'The number of hashtags', 'The posting time'],
         'a': 'B', 'why': 'Reusing content as ads needs agreement and often a fee.'},
    ],
    study='ASCI\'s influencer guidelines and FAQs, the government endorsement guide and Instagram\'s creator tools (about 50 minutes)',
    action='shortlist and vet local creators, write an influencer brief and a UGC permission message',
)

L2 = lesson(
    10, 2,
    title='Affiliate marketing and creator monetisation',
    weeks=(26, 26), hours=2.5,
    outcome='Know the real ways creators earn in India, what each needs before it pays, how to disclose affiliate links and paid posts, and build a first rate card and money plan for your own account.',
    split='40 minutes study, 1 hour 50 minutes action',
    core=f"""
### Ways creators earn ({ASOF})

| Income | What it needs | Know this |
| --- | --- | --- |
| **Services** (social media help for local businesses) | Skills and proof; this course | The fastest route for most learners (Module 15) |
| **Local sponsorships** ("Shop of the week, presented by...") | A local audience that trusts you | Label every sponsored post clearly |
| **Brand deals** (paid posts) | An engaged audience in a niche brands want | Disclose with labels and the platform's paid partnership tool |
| **Amazon.in Associates** (affiliate) | A qualifying website or app; approval | Amazon says you can earn up to 10% in fees on qualifying purchases; rates differ by category, for example 8% for beauty, 2.8% for electronics and 0% for many phones in its Oct–Nov 2026 table. Social media influencers are pointed to a separate Amazon Influencer Program. |
| **YouTube Shopping affiliate** | Eligibility and registration in YouTube Studio | Launched in India in October 2024 with Flipkart and Myntra: tag products in videos, Shorts and lives and earn a commission |
| **YouTube Partner Program** | 500 subscribers and more for fan funding; 1,000 subscribers and 4,000 watch hours or 10 million Shorts views for ad revenue | A long road for most channels (SMM-M03-L02) |
| **Instagram tools** | Varies by country and account | Instagram's creator hub lists Subscriptions, Partnership ads, Creator Marketplace, Gifts, Badges and Bonuses; check which your professional dashboard offers |
| **Your own products** | Something people need | Digital products, workshops, local tours (see the Entrepreneurship course) |

Check current rules for every programme; thresholds, rates and eligibility change.

### Disclose affiliate links and paid posts

ASCI's guidelines list **Affiliate** among the labels for disclosing a material connection, alongside Ad, Sponsored, Collaboration, Partnership, Employee and Free gift. Put the label next to the link or at the start of the caption, not hidden among hashtags. Recommend only products you have used or properly checked; the government's endorsement guide says endorsers shouldn't promote products they haven't personally used or vetted.

### Your rate card

Brands and shops will ask "how much?". A simple rate card shows you're professional. Base it on your own numbers, not on someone else's:

- your **average views** for the format, and the share from your area
- your **engagement** (shares and saves per 1,000 views)
- the **work involved** (visit, shoot, edit, revisions)
- **usage rights** and **exclusivity** (extra if the brand wants to use your video as an ad, or wants you to avoid competitors)

One way to start: estimate what it would cost the business to reach the same local people with ads (Module 9), add a fair fee for your work, and offer a starter price for the first deal. Revisit it every three months.

### Money and tax

Income from sponsorships, affiliate fees and services is taxable income, and businesses may ask for an invoice. The Entrepreneurship course explains tax basics in ENT-M08-L03; ask a tax professional when the amounts grow.

### Honest expectations

Most new accounts earn little from ads or affiliate links for a long time. Local services and sponsorships usually pay sooner, because a local business values a local audience even when it's small.
""",
    example="""
Anu's money plan for @kuttiady.diaries at about 2,000 mostly local followers (made-up numbers to show the method):

| Stream | Prerequisite | First step | When |
| --- | --- | --- | --- |
| Local sponsorship: "Shop of the week, presented by Malabar Mobiles" | Average 2,500 views on shop stories | Offer 4 weeks at a starter price | Next month |
| Services for local shops | Case studies (Modules 8 and 11) | Pilot in Module 11 | Week 29 |
| Affiliate links for a "monsoon gear" list | A qualifying website or app; Amazon approval | Check eligibility first | Later |
| YouTube Partner Program | 500 subscribers and the watch-hour or Shorts-view thresholds | Keep posting long videos | Long term |

Her starter rate card: one shop-story Reel and two Stories, ₹1,500; four weeks of "Shop of the week", ₹5,000; reuse as an ad +₹1,000. Every sponsored post starts with "Ad" in the caption and on screen.
""",
    resources=[
        ('amazon-assoc', 'Read who can join and how fees work', '5 min'),
        ('amazon-fees', 'Look at the fee table for your niche\'s categories', '5 min'),
        ('yt-shopping-in', 'Read how the YouTube Shopping affiliate programme works in India', '5 min'),
        ('yt-ypp', 'Re-read the two Partner Program levels', '5 min'),
        ('ig-best', 'Look at the Monetize section and check your own professional dashboard', '10 min'),
        ('asci-guidelines', 'Re-read the labels, including Affiliate', '5 min'),
    ],
    steps=[
        'Study the resources (about 35 minutes).',
        'Check which monetisation tools your Instagram and YouTube accounts can see right now, and screenshot them.',
        'Write your money plan: three income streams, the prerequisite for each and your first step.',
        'Make your rate card v1 for two or three deliverables, based on your own average views and work time.',
        'Write a disclosure snippet for each kind of connection you might have (paid, free gift, affiliate), in Malayalam and English.',
    ],
    proof='Screenshots of your available monetisation tools, your money plan, your rate card and your disclosure snippets.',
    templates=[
        ('creator money plan', """
STREAM 1: ____________
  Needs first: ________  First step: ______  By: ____
STREAM 2: ____________
  Needs first: ________  First step: ______  By: ____
STREAM 3: ____________
  Needs first: ________  First step: ______  By: ____
Review this plan on: ____ (every 3 months)
""", ''),
        ('rate card v1', """
@[handle] - RATE CARD (valid until ____)
Audience: ____ followers, ___% from [area];
  average ___ views on Reels (last 30 days)
DELIVERABLES
  1 Reel + 2 Stories (visit, shoot, edit, 1 revision)  Rs ____
  4-week series ("Shop of the week")                   Rs ____
  Story-only mention (3 frames)                        Rs ____
EXTRAS
  Reuse of the video as a paid ad (3 months)          + Rs ____
  Exclusivity (no competitor for 30 days)              + Rs ____
TERMS: 50% before, 50% on posting; all paid or gifted
  posts are labelled clearly, as the law requires
""", ''),
        ('disclosure snippets', """
PAID:      Ad | പരസ്യം  (start of caption + on screen)
FREE GIFT: Free gift from @brand | @brand നൽകിയ സൗജന്യ സമ്മാനം
BARTER:    Collaboration (free stay) | കൊളാബറേഷൻ (സൗജന്യ താമസം)
AFFILIATE: Affiliate link: I may earn a commission |
           അഫിലിയേറ്റ് ലിങ്ക്: എനിക്ക് കമ്മീഷൻ ലഭിച്ചേക്കാം
+ Turn on the platform's paid partnership label
""", ''),
    ],
    mistakes=[
        ('Waiting for platform payouts.', 'For most, local services and sponsorships come first.'),
        ('Affiliate links without disclosure.', 'Label them clearly, next to the link or at the start.'),
        ('Promoting products you haven\'t tried.', 'Use or check them first; your trust is your income.'),
        ('Copying someone\'s rate card.', 'Base yours on your own numbers and work.'),
        ('Forgetting tax.', 'Keep records and invoices; get professional advice as income grows.'),
    ],
    quiz=[
        {'q': 'According to Amazon.in Associates, what is the maximum affiliate fee you can earn?',
         'o': ['Up to 50%', 'Up to 10%, depending on category', 'A fixed ₹100 per click', 'Nothing in India'],
         'a': 'B', 'why': 'Amazon says up to 10% from qualifying purchases; rates vary by category.'},
        {'q': 'Which label does ASCI list for affiliate links?',
         'o': ['#blessed', 'Affiliate', 'No label needed', '#love'],
         'a': 'B', 'why': 'Affiliate is one of the listed disclosure labels.'},
        {'q': 'For most new creators, which income usually comes first?',
         'o': ['YouTube ad revenue', 'Local services and sponsorships', 'Instagram Bonuses', 'Selling the account'],
         'a': 'B', 'why': 'Local businesses value local audiences even when they are small.'},
        {'q': 'What should a rate card be based on?',
         'o': ['A famous creator\'s prices', 'Your own views, audience, work involved, usage rights and exclusivity', 'Your follower count only', 'A random number'],
         'a': 'B', 'why': 'Your own numbers make the price fair and defensible.'},
    ],
    study='Amazon Associates, YouTube Shopping and Partner Program rules, Instagram\'s monetisation tools and ASCI\'s labels (about 35 minutes)',
    action='check your monetisation tools, write a money plan, a rate card and disclosure snippets',
)

LESSONS = [L1, L2]

MODULE = module(
    10,
    title='Influencer and creator marketing',
    weeks=(25, 26), hours=6.5,
    overview="""
Work with creators the right way, from both sides: as a marketer hiring local micro-influencers and using customer content, and as a creator who may earn from brand deals, affiliate links and platform programmes.

Trusted voices sell better than ads. In two weeks you'll find and vet local creators, write briefs, use user-generated content with permission, and learn the real ways creators earn in India, with the disclosure rules that apply to all of them.

Your 90-day growth sprint begins at the end of this module (SMM-M17-L01), so you'll also plan your sprint in week 26.
""",
    outcomes=[
        'Find and vet micro-influencers with real, local audiences',
        'Write a clear influencer brief with deliverables, claims and usage rights',
        'Use UGC only with permission and never as fake reviews',
        'Explain creator income options in India and their prerequisites',
        'Disclose paid, gifted and affiliate content correctly, and make a rate card',
    ],
    lessons=LESSONS,
    project='An influencer brief and your creator money plan',
    project_steps=[
        'Finalise one influencer brief for a real local business, including disclosure instructions and usage rights.',
        'Finalise your own creator money plan and rate card v1.',
        'Put your disclosure snippets in your template library.',
        'If you did a barter collaboration, add its results and what you would change.',
    ],
    project_proof='Your final influencer brief, money plan, rate card and disclosure snippets in 10 Influencers.',
    rubric=[
        ('Finding and vetting', 'Picks by follower count', 'Some checks', 'Checks location, engagement, growth, fit and disclosure habits'),
        ('Briefing', 'Verbal only', 'Partial brief', 'Complete brief with message, claims, deliverables, rights and payment'),
        ('UGC', 'Reposts without asking', 'Asks sometimes', 'Always asks, credits and keeps permission'),
        ('Monetisation', 'Unclear', 'Lists options', 'A money plan with prerequisites and a rate card based on own numbers'),
        ('Disclosure', 'Hidden or missing', 'Sometimes labelled', 'Correct labels for paid, gifted and affiliate content, every time'),
    ],
    short=[
        'Vet one creator with the checklist.',
        'Write a half-page brief.',
        'Write your money plan with two streams.',
        'Save the disclosure snippets.',
    ],
    flashcards=[
        ('Why micro-influencers for local shops?', 'Small but engaged, local, trusted audiences give better value.'),
        ('Five vetting checks?', 'Local audience, real engagement, growth pattern, fit and values, disclosure habits.'),
        ('Four deal types?', 'Barter, paid fee, commission, discount code.'),
        ('What are usage rights?', 'Whether and how the brand may reuse the creator\'s content, for example as ads.'),
        ('ASCI labels for material connections?', 'Ad, Sponsored, Collaboration, Partnership, Employee, Free gift, Affiliate.'),
        ('Maximum Amazon.in Associates fee?', 'Up to 10%, varying by category (check current rates).'),
        ('YouTube Shopping affiliate partners in India at launch (Oct 2024)?', 'Flipkart and Myntra.'),
        ('Which creator income usually comes first?', 'Local services and sponsorships.'),
    ],
    mistakes=[
        ('Treating influencer posts as ads without labels.', 'Every material connection needs a clear label.'),
        ('Paying before vetting.', 'Check the audience first; ask for Insights screenshots.'),
        ('Building income on one platform\'s programme.', 'Programmes change; keep several streams.'),
    ],
)
