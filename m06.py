from common import lesson, module

L1 = lesson(
    6, 1,
    title='Positioning and low-budget branding',
    weeks=(13, 13), hours=5,
    outcome='Write a positioning statement, choose a name you can legally use, and build a simple brand kit and WhatsApp Business profile for ₹0–₹500.',
    split='1.5 hours study, 3.5 hours action',
    core="""
### Positioning: the place you hold in a customer's mind

Before any logo, decide what you want people to think when they hear your name. A useful positioning statement:

**For [target customer] who [need], [business name] is the [category] that [key benefit], because [proof]. Unlike [main alternative], we [key difference].**

Small businesses rarely win on price. Choose one or two differences that your interviews showed customers care about:

- **Specialisation:** "only for textile and mobile shops", "only LDC and LGS practice"
- **Speed:** "replies in 5 minutes", "your CV in 48 hours"
- **Local trust:** "your neighbour in Kuttiady", "we come to your shop"
- **Language:** "explained in Malayalam"
- **Quality or values:** "natural colours, no preservatives"
- **Personal service:** "the owner answers your call"

### Choosing a name

A good name is easy to say in Malayalam and English, easy to spell when someone searches for it, not misleading, and not too close to an existing brand. Before you fall in love with a name, check:

1. **Trademark search** on IP India's public search, in the class for your goods or services (cakes and services fall in different classes).
2. **Google and Google Maps:** is there a similar business name nearby?
3. **Instagram, YouTube and Facebook:** is the handle free?
4. **Meaning:** does it mean anything odd in Malayalam, Hindi or Arabic? Many customers have Gulf links.

A name too close to a well-known brand can bring a legal notice and a forced rename after you have printed everything. If you later register a trademark (Module 9), the online filing fee for individuals, startups and small enterprises is ₹4,500 per class, against ₹9,000 for others (check current rules).

### A brand kit for ₹0

- **Logo:** your name in one clear font, plus at most one simple symbol you make yourself. Canva's free licence does not allow content from its library in a logo, trademark or business name, so build your logo from text and shapes you draw.
- **Two colours** (a main colour and an accent) and **one or two fonts**, used everywhere.
- **A tagline** of 3–7 words, taken from your value proposition.
- **A photo style:** real photos of your own work, daylight, a plain background, no stock images.
- **A tone of voice:** friendly, simple and respectful, in both English and Malayalam.

### The same everywhere

Your WhatsApp Business profile, Instagram bio, Google profile, visiting card, stickers, receipts and price list should all use the same name, logo, colours, phone number and one-line description. Consistency is what makes a small business look trustworthy.
""",
    example="""
Nisha first wanted to call her bakery "Kuttiady Cake House". When she searched, she found a bakery with a very similar name in the next town, and similar marks for bakery goods in the trademark search. To avoid confusion and a possible legal problem, she chose **Nisha's Oven**, checked it the same way, and found the Instagram handle @nishasoven.kuttiady free.

Her positioning: "For parents in and around Kuttiady who want a birthday cake they can trust, Nisha's Oven is the home bakery that makes cakes with natural colours and less sugar, because every cake is baked in her own kitchen the day before. Unlike town bakeries, she bakes to order and delivers within 5 km."

Her brand kit cost ₹350, all of it for 200 round stickers from a local printer: the name in a rounded font, a small oven she drew from simple shapes, cream and deep red, the tagline "Baked at home, with care", and photos taken on her balcony in the morning light.
""",
    resources=[
        ('os8', 'Sections 8.4 Entrepreneurial Branding and 8.3 Marketing Techniques and Tools for Entrepreneurs', '50 min'),
        ('tm-search', 'Open the public search tool and practise with your name ideas (search by word mark)', '20 min'),
        ('canva-license', 'Read what you may and may not do with free content, especially the logo rule', '10 min'),
        ('wa-business', 'Read the features: business profile and catalogue', '5 min'),
    ],
    steps=[
        'Write your positioning statement, using evidence from your interviews.',
        'Shortlist 5 names. Check each one: IP India trademark search, Google and Google Maps, Instagram and YouTube handles, and meanings.',
        'Test your top 2 names: tell 5 target customers both names, then message them the next day and ask which one they remember.',
        'Make a brand kit in Canva from your own text and shapes: logo, two colours, fonts, tagline and three sample photos of your work.',
        'Complete your WhatsApp Business profile: logo, description, address or service area, hours, a catalogue with prices, and a greeting or away message.',
    ],
    proof='Your positioning statement, the name check table, a screenshot of your brand kit and a screenshot of your complete WhatsApp Business profile.',
    templates=[
        ('positioning statement and name check', """
POSITIONING
For ____ who ____,
[name] is the ____ that ____,
because ____.
Unlike ____, we ____.

NAME CHECK (Y = clear, N = problem)
Name | Trademark | Google/Maps | Instagram | YouTube | Meaning OK | Easy to spell
1.
2.
3.
4.
5.
Remembered the next day by ____ of 5 people
""", ''),
        ('brand kit', """
BRAND KIT
Name: ____________
Tagline (3-7 words): ____________
Main colour: ____  Accent colour: ____ (write the hex codes)
Fonts: ____ for headings, ____ for text
Logo: my own text and shapes, no Canva library elements
Photo style: real work, daylight, plain background
Tone: ____ (for example: friendly, simple, respectful)
One-line description (the same everywhere): ____________
Must appear on: WhatsApp Business, Instagram bio, Google
profile, visiting card, stickers, receipts, price list
""", ''),
    ],
    mistakes=[
        ('Spending thousands on a logo first.', 'A text logo and two colours are enough to start. Upgrade when customers are paying for it.'),
        ('A name that is hard to spell.', 'If people can\'t spell it, they can\'t search for it. Test it on five people.'),
        ('Copying a famous brand.', 'Look-alike names and logos invite legal trouble and confuse customers. Search before you print.'),
        ('Stock photos of food or products.', 'Customers want to see your real work, and stock photos can look dishonest.'),
        ('Different details on every platform.', 'One name, one number, one description, everywhere.'),
    ],
    quiz=[
        {'q': 'Which is the strongest positioning for a small business?',
         'o': ['"Best quality at the lowest price for everyone"', 'A specific customer, a clear benefit and a real difference, such as "natural-colour cakes baked to order for Kuttiady parents"', '"We do everything"', '"Cheapest in Kerala"'],
         'a': 'B', 'why': 'Specific positioning is believable and easy to remember.'},
        {'q': 'What does Canva\'s free media licence say about logos?',
         'o': ['Any Canva element can go in your logo', 'Content from Canva\'s library can\'t be used in a trademark, logo or business name', 'All logos made in Canva are free to trademark', 'It says nothing about logos'],
         'a': 'B', 'why': 'Other people can use the same content, so you can\'t own it as your mark.'},
        {'q': 'What should you check before printing stickers with your name?',
         'o': ['Only Instagram', 'The trademark search, Google and Maps, social handles and meanings', 'Nothing', 'Only what your family thinks'],
         'a': 'B', 'why': 'A rename after printing costs money and confuses customers.'},
        {'q': 'Why use the same name, number and description everywhere?',
         'o': ['WhatsApp requires it', 'Consistency builds trust and helps people find you', 'It is cheaper', 'To confuse competitors'],
         'a': 'B', 'why': 'Matching details look professional and make searching easy.'},
    ],
    study='OpenStax 8.4 and 8.3, the IP India search, Canva\'s licence and the WhatsApp Business features (about 1.5 hours)',
    action='write your positioning, check and test names, build a brand kit and complete your WhatsApp Business profile',
)

L2 = lesson(
    6, 2,
    title='Content that sells on WhatsApp, Instagram and YouTube',
    weeks=(14, 14), hours=6,
    outcome='Plan and publish two weeks of useful content on one or two channels, using content pillars, a simple calendar and honest disclosure, and track which posts bring replies and orders.',
    split='1 hour 40 minutes study, 4 hours 20 minutes action',
    core="""
**Content marketing** means helping, teaching or showing first, and selling second. People buy from businesses they know and trust, and useful content builds that trust before you ask for money.

### Choose one or two channels

| Channel | Best for | Notes |
| --- | --- | --- |
| WhatsApp Status and catalogue | Local customers who have your number | The highest trust in Kerala towns. Broadcast lists reach only people who have saved your number. |
| WhatsApp channel or group | Regular updates for followers | Ask before you add anyone to a group. |
| Instagram (professional account) | Things that look good: food, design, fashion, places | Reels, Stories, location tags, a link in your bio. |
| YouTube Shorts and videos | Teaching: tips, how-tos, explanations | Searchable for years; good for digital products. |
| Facebook groups | Older audiences and local communities | Follow each group's rules. |

Start where your customers already are; your interviews told you where. Two channels done well beat five done badly.

### Four content pillars

Plan posts around four themes:

1. **Show:** your product and process. A cake being decorated, a shop's new catalogue, the first page of a practice pack.
2. **Teach:** a useful tip. "3 ways to store a cream cake", "how to answer WhatsApp enquiries faster", "5 PSC questions on Kerala's rivers".
3. **Prove:** results and real reviews, shared with the customer's permission.
4. **Personal:** your story and values. Why you started, a day of your work, a lesson you learned.

A good rhythm is about three helpful posts for every offer, and always a clear way to order or get in touch.

### Make it on a phone

- **Hook in the first 2 seconds:** start with the result or a question, not your logo.
- **Keep it short:** 15–45 seconds for Reels and Shorts.
- **Natural light** and a steady phone (lean it on something). Use real sound or music from the app's own library.
- **Captions** in Malayalam or English, because many people watch with the sound off.
- **One call to action:** "WhatsApp 98XXXXXXXX to order" or "Link in bio".
- **Batch it:** shoot 6–8 short clips in one 2-hour session, then post them through the week.

### Stay honest and legal

- Use only photos, music and clips you made or have the right to use. Never take photos from Google.
- If you pay someone to promote you, give them free products, or have any other connection with them, the post must say so clearly. ASCI's guidelines list labels such as #ad, #collaboration and #sponsored, placed where viewers can't miss them.
- Never post fake reviews or invented before-and-after results. Misleading ads can break consumer protection law.

### Measure what matters

For each post, note the views, the replies or messages, and the orders. After two weeks, do more of what brought replies and orders, not of what got the most likes.
""",
    example="""
Nisha's first week on WhatsApp Status and Instagram:

| Day | Pillar | Post |
| --- | --- | --- |
| Mon | Show | A 20-second Reel of a rainbow cake being decorated with natural colours |
| Tue | Teach | "Why my red colour comes from beetroot" (photo with text) |
| Wed | Prove | A customer's thank-you message, shared with permission |
| Thu | Show | This week's flavours and prices, with the catalogue link |
| Fri | Personal | "Baking since I was 12, in my mother's kitchen" (photo) |
| Sat | Offer | "Weekend orders close tonight at 8 pm" |
| Sun | Teach | "How to cut a cake neatly" (a 15-second clip) |

Results: 7 posts, about 900 Status views, 140 Instagram views, 19 messages and 6 orders. Five of the six orders came after the Monday Reel and the Thursday price list, so in week two she posted two process Reels and kept the price list on Thursdays.

**Fathima** posts one PSC question a day as a YouTube Short, with the answer explained in Malayalam in 30 seconds, ending with "The full weekly test is free in our WhatsApp channel". **Arun** posts before-and-after screenshots of shops' WhatsApp catalogues, with the owners' permission.
""",
    resources=[
        ('hubspot-content', 'Free sign-up. Do the first 2 lessons (the whole course is about 8 hours 20 minutes)', 'about 1 hour'),
        ('yt-creators', 'Open the "Get started" and Shorts guides', '20 min'),
        ('ig-pro', 'If you use Instagram: set up a professional account', '10 min'),
        ('asci', 'Read which disclosure labels to use and where to put them', '10 min'),
    ],
    steps=[
        'Choose one or two channels, based on where your interviewees said they spend their time.',
        'Write your four content pillars, with three post ideas for each.',
        'Plan 14 days of posts in the content calendar below.',
        'Batch-shoot and publish at least 7 posts in the first week, and keep posting in the second week.',
        'Track views, replies and orders for every post. Write down which two posts worked best, and why you think they did.',
    ],
    proof='Your 14-day calendar, links or screenshots of at least 7 published posts, and the results table.',
    templates=[
        ('14-day content calendar (paste into Google Sheets)', """
Date,Channel,Pillar (show / teach / prove / personal / offer),Hook (first 2 seconds),Post idea,Call to action,Views,Replies,Orders
""", 'csv'),
        ('hooks and captions', """
HOOKS (the first 2 seconds)
- Show the result first: the finished cake, the full catalogue
- Ask a question: "Losing customers at night on WhatsApp?"
- Use a number: "3 CV mistakes that cost you interviews"
- Before and after
- "Watch this before you order a birthday cake"

CAPTION
Line 1: the hook again, in words
Lines 2-3: one useful point, or the story
Line 4: the call to action (how to order or contact you)
Hashtags: 3-5 local and topic tags
(#Kuttiady #Kozhikode #homebakery #KeralaPSC)

CALL TO ACTION IN MALAYALAM
ഓർഡർ ചെയ്യാൻ WhatsApp ചെയ്യൂ: [നമ്പർ]
കൂടുതൽ വിവരങ്ങൾക്ക് ബയോയിലെ ലിങ്ക് നോക്കൂ.
""", ''),
    ],
    mistakes=[
        ('Only posting offers.', 'Constant "buy now" posts get muted. Help, show and prove first.'),
        ('Posting irregularly.', 'Ten posts in one day and then nothing for a month builds no trust. Plan and batch.'),
        ('Chasing followers.', 'A thousand followers outside your area are worth less than fifty local parents. Track replies and orders.'),
        ('Using other people\'s photos or music.', 'It can get posts removed and accounts flagged, and it breaks trust. Use your own.'),
        ('No call to action.', 'Every post needs a clear next step: how to order or contact you.'),
    ],
    quiz=[
        {'q': 'Which mix of helpful posts and offers is a good starting rhythm?',
         'o': ['All offers', 'About 3 helpful posts to every offer', 'Never post an offer', '10 offers to every helpful post'],
         'a': 'B', 'why': 'Helpful posts earn the attention that makes offers work.'},
        {'q': 'Who receives your WhatsApp broadcast messages?',
         'o': ['Everyone in your contacts', 'Only people who have saved your number', 'Everyone on WhatsApp', 'Only groups'],
         'a': 'B', 'why': 'That is why asking customers to save your number matters.'},
        {'q': 'You gave an Instagram creator a free cake to post about. What must the post include?',
         'o': ['Nothing', 'A clear disclosure label such as #ad or #collaboration, where viewers can\'t miss it', 'Your phone number', 'A discount code'],
         'a': 'B', 'why': 'A free product is a material connection under ASCI\'s guidelines.'},
        {'q': 'Which number best tells you a post worked?',
         'o': ['Likes', 'The replies and orders it brought', 'New followers', 'The number of hashtags'],
         'a': 'B', 'why': 'Replies and orders are actionable; likes are vanity numbers.'},
    ],
    study='two HubSpot content lessons, the YouTube Creators guides, Instagram\'s professional account help and ASCI\'s labels (about 1 hour 40 minutes)',
    action='plan 14 days of content on one or two channels, publish at least 7 posts and track replies and orders',
)

L3 = lesson(
    6, 3,
    title='Google Business Profile and local SEO',
    weeks=(15, 15), hours=3,
    outcome='Create or claim a free Google Business Profile, complete every section accurately, and set up a weekly routine for photos, posts and real reviews.',
    split='40 minutes study, 2 hours 20 minutes action',
    core="""
When someone in Kuttiady searches "cake shop near me" or "mobile repair Vatakara", Google shows a map with a few businesses. A **Google Business Profile** is the free listing that puts you on that map and in Google Search. Google says creating one costs nothing.

### Can you have one?

Business Profiles are for businesses that meet customers in person: either customers come to you (a shop, or a home bakery with pickup) or you go to them (delivery, on-site service). If you work from home and don't want your address shown, list a **service area** (for example Kuttiady, Thottilpalam and Vatakara) and hide the address. A business that sells only online, such as a digital product, usually doesn't qualify; use WhatsApp, Instagram or YouTube instead.

### How Google ranks local results

Google's help page says local results depend mainly on three things:

- **Relevance:** how well your profile matches the search. Pick the right primary category and describe what you actually offer.
- **Distance:** how far you are from the person searching, or from the place in their search.
- **Prominence:** how well known you are, including your reviews and how often others mention and link to you.

You can't change distance, but you can improve relevance and prominence.

### A complete profile

- **Name:** your real business name, exactly as on your board. Don't add keywords such as "Best Cakes Kuttiady" to the name; it breaks Google's guidelines and can get the profile suspended.
- **Category:** the most specific primary category, plus a few secondary ones.
- **Contact:** phone or WhatsApp number, and a website or Instagram link.
- **Hours:** accurate, including holidays.
- **Address or service area.**
- **Products or services, with prices.**
- **Description:** what you offer, to whom and where, in plain words that people actually search for ("home-made birthday cakes in Kuttiady").
- **Photos:** at least 10 real ones: products, work in progress, you, and the outside of the shop if you have one. Add new photos every week.

### Reviews: ask, never fake

Ask every happy customer for an honest review, right after they thank you. Make it easy: send your review link or show a QR code at the counter. Reply to every review, good or bad, politely and within a few days. Never write reviews yourself, pay for them or give gifts only for five-star ratings. Fake reviews break Google's rules and destroy trust when they are found out.

### The same details everywhere

Use exactly the same name, address and phone number on Google, WhatsApp, Instagram, any directory such as JustDial, and your printed material. Mismatched details confuse customers and search engines alike.
""",
    example="""
Arun claimed Rasheed's existing listing, which had the wrong hours and no photos. He chose the most specific shop category, added 25 real photos, the WhatsApp number, the hours (including Sunday closing) and a description: "Sarees, salwar sets and kids' wear on Kuttiady main road, near the bus stand. New stock every week. WhatsApp us for photos and prices." He printed a QR code linking to the review page and placed it at the billing counter.

In the following month, the shop received 12 reviews from real customers, averaging 4.7 stars, and the calls and direction requests shown in the profile's performance page both went up.

Nisha, who bakes at home, listed Nisha's Oven as a service-area business covering Kuttiady and nearby places, with her home address hidden.
""",
    resources=[
        ('gbp-free', 'Read what a free Business Profile includes and who can have one', '10 min'),
        ('gbp-rank', 'Read how relevance, distance and prominence work', '10 min'),
        ('skillshop', 'Optional: look for the free Business Profile training', '20 min'),
    ],
    steps=[
        'Decide whether your business qualifies (customers come to you, or you serve them in your area). If it doesn\'t, write down which channel you will use instead, and do the steps below for that channel.',
        'Create or claim your profile and complete the verification Google asks for.',
        'Fill in every section using the checklist below, and add at least 10 real photos.',
        'Ask 5 real customers for honest reviews with the message below. Reply to every review.',
        'Put a 15-minute weekly Google routine in your calendar: a new photo, a post, and replies to reviews and questions.',
    ],
    proof='A screenshot of your complete profile (or of the channel you chose instead), your review requests and the weekly routine in your calendar.',
    templates=[
        ('profile checklist', """
GOOGLE BUSINESS PROFILE CHECKLIST
[ ] Business name exactly as on the board (no extra keywords)
[ ] Most specific primary category, plus 2-3 secondary
[ ] Phone or WhatsApp number (the same as everywhere else)
[ ] Website or Instagram link
[ ] Hours, including holidays
[ ] Address shown, or service area with the address hidden
[ ] Products or services with prices
[ ] Description: what, for whom, where, in plain words
[ ] 10 or more real photos (products, work, you, outside)
[ ] Review link or QR code ready
[ ] Weekly 15 minutes: a photo, a post, replies
""", ''),
        ('review requests and replies', """
REVIEW REQUEST (right after a happy customer says thanks)
Thank you so much! If you liked it, could you write a short,
honest review on Google? It really helps a small business
like mine: [review link]

MALAYALAM
വളരെ നന്ദി! ഇഷ്ടപ്പെട്ടെങ്കിൽ, ഗൂഗിളിൽ ഒരു ചെറിയ
സത്യസന്ധമായ റിവ്യൂ എഴുതാമോ? എന്നെപ്പോലുള്ള ഒരു
ചെറിയ സംരംഭത്തിന് അത് വലിയ സഹായമാണ്: [ലിങ്ക്]

REPLY TO A BAD REVIEW
Thank you for telling us, [name]. I'm sorry about [issue].
I'd like to put it right. Please WhatsApp me on [number].
""", ''),
    ],
    mistakes=[
        ('Stuffing keywords into the business name.', '"Nisha\'s Oven Best Cakes Kuttiady" breaks Google\'s guidelines. Put the keywords in the description instead.'),
        ('Fake or paid reviews.', 'They break Google\'s rules and, once discovered, destroy the trust your business depends on. Ask real customers.'),
        ('Wrong hours.', 'A customer who arrives at a closed shutter won\'t come back. Keep holiday hours up to date.'),
        ('Showing your home address by accident.', 'If you work from home, choose a service area and hide the address.'),
        ('Ignoring bad reviews.', 'A calm, helpful reply to a complaint shows future customers that you care.'),
    ],
    quiz=[
        {'q': 'Which three factors does Google name for local ranking?',
         'o': ['Price, size and age', 'Relevance, distance and prominence', 'Followers, likes and shares', 'Ads, budget and logo'],
         'a': 'B', 'why': 'Those are the three factors on Google\'s own help page.'},
        {'q': 'Nisha bakes at home and delivers. What should she do about her address?',
         'o': ['Hide it and list a service area', 'Use a fake shop address', 'Not create a profile at all', 'Put it in the business name'],
         'a': 'A', 'why': 'Service-area businesses can hide their address and show the areas they serve.'},
        {'q': 'Which business name follows Google\'s guidelines?',
         'o': ['"Nisha\'s Oven"', '"Nisha\'s Oven Best Birthday Cakes Kuttiady Cheap"', '"Cakes Near Me"', '"No. 1 Bakery Kerala"'],
         'a': 'A', 'why': 'Use your real name only; keywords belong in the description.'},
        {'q': 'What should you do after a bad review?',
         'o': ['Delete your profile', 'Reply calmly, apologise for the problem and offer to fix it', 'Argue in public', 'Ask friends for fake five-star reviews'],
         'a': 'B', 'why': 'Future customers read your reply as much as the complaint.'},
    ],
    study='the two Google Business Profile help pages, plus Skillshop if you have time (about 40 minutes)',
    action='create or claim your Google Business Profile, complete it, ask 5 customers for reviews and set a weekly routine',
)

L4 = lesson(
    6, 4,
    title='Word of mouth, referrals and reviews',
    weeks=(15, 15), hours=2,
    outcome='Design a simple, honest referral offer, ask happy customers for referrals at the right moment, and track where every customer comes from.',
    split='35 minutes study, 1 hour 25 minutes action',
    core="""
In Kerala towns, most new customers come from people talking to each other: family groups, neighbours, colleagues, people waiting at the bus stop. Word of mouth is free, but it doesn't happen by itself. You can make it more likely.

### Give people something to talk about

- **A remarkable moment:** something a little better than expected. A handwritten note, a free cupcake for the birthday child, a WhatsApp reply in two minutes, a call a week later to check everything is working.
- **Something easy to share:** a photo-worthy product, a short message that is ready to forward, a visiting card with a QR code.
- **A story:** "the young man from Kuttiady who set up our shop's WhatsApp" is easy to repeat.

### Ask at the happy moment

The best time to ask for a referral or a review is right after the customer says "thank you" or "it's perfect". Be specific: "Do you know one other shop owner who struggles with WhatsApp enquiries?" is easier to answer than "Please tell everyone".

### A simple referral offer

**Give-get:** the new customer gets something, and so does the person who referred them. For example ₹50 off for both, a free add-on, or one free month of care for every new shop referred.

Rules that keep it honest:

- Reward referrals that become paying customers, not sign-ups.
- Keep it to one level. Rewards for the referrals of your referrals start to look like a pyramid scheme, and India's Direct Selling Rules prohibit promoting pyramid and money-circulation schemes.
- Never pay for reviews, and never make a reward depend on a five-star rating.

### Be present in the community

Local events, markets and partnerships spread the word fast: a stall at a Kudumbashree market or a local festival (with the organisers' permission), a small prize at a school event, or cross-promotion with a business that has the same customers (cakes with a party decorator, CVs with a nursing coaching centre).

### Track where every customer comes from

Ask every new customer, "How did you hear about us?", and write the answer in the Source column of your Customers tab. After a month you will know which channel deserves your time.
""",
    example="""
Nisha slips a small card into every cake box: "Loved your cake? Share this card. Your friend gets ₹50 off their first order, and you get ₹50 off your next one. WhatsApp 98XXXXXXXX." She asks for a Google review the moment a customer sends a thank-you message. In her first month of tracking, her 26 new customers came from referral cards (9), WhatsApp Status (7), Instagram (4), family groups (3) and a stall at a Christmas market (3).

Arun gives an existing client one free month of the care plan (worth ₹500) for every new shop they refer that buys a setup. In the first month, two shop owners referred their brothers' shops in Vatakara.
""",
    resources=[
        ('pg-ds', 'Re-read the part about delighting your first users', '10 min'),
        ('os8', 'Section 8.6 Sales and Customer Service', '20 min'),
        ('direct-selling', 'Note that pyramid and money-circulation schemes are prohibited (check current rules)', '5 min'),
    ],
    steps=[
        'Design one "remarkable moment" you can afford to give every customer.',
        'Write a give-get referral offer and make a referral card or message (Canva or plain text).',
        'Ask your 5 happiest customers, at the happy moment, for one referral or one honest review each.',
        'Add a Source column to your Customers tab, and ask every new customer how they heard about you.',
        'Plan one community activity for next month: a market stall, an event or a partner business.',
    ],
    proof='Your referral card or message, your 5 asks and what happened, and a Source column with at least 5 entries.',
    templates=[
        ('referral card, referral ask and source codes', """
REFERRAL CARD (visiting-card size)
Loved it? Share this card.
Your friend gets ____ off their first order,
and you get ____ off your next one.
Order: WhatsApp [number]
[Business name] | [tagline]

ASKING FOR A REFERRAL (at the happy moment)
I'm so glad you liked it! Do you know one other
[parent / shop owner / nurse] who might need this?
If you share my number, you both get ____.

MALAYALAM
ഇഷ്ടപ്പെട്ടതിൽ വളരെ സന്തോഷം! ഇത് ആവശ്യമുള്ള
മറ്റൊരാളെ അറിയാമോ? എന്റെ നമ്പർ അവർക്ക്
കൊടുത്താൽ, നിങ്ങൾക്ക് രണ്ടുപേർക്കും ____ കിട്ടും.

SOURCE CODES (Customers tab)
REF = referral card   WA = WhatsApp Status
IG = Instagram        YT = YouTube
G = Google            GRP = group
EVT = event           PART = partner
OTH = other
""", ''),
    ],
    mistakes=[
        ('Asking too late.', 'A week later, the excitement has gone. Ask right after the thank-you.'),
        ('Complicated rules.', 'If your referral offer needs a paragraph, nobody will use it. One sentence, two rewards.'),
        ('Multi-level rewards.', 'Rewards for referrals of referrals drift towards a pyramid scheme. Keep it to one level.'),
        ('Spamming groups.', 'Posting the same offer in every group annoys people and gets you removed. Ask the admins, and add value first.'),
        ('Not tracking sources.', 'Without a Source column, you can\'t tell which effort is working.'),
    ],
    quiz=[
        {'q': 'When is the best time to ask for a referral?',
         'o': ['Before delivery', 'Right after the customer says thank you', 'A month later', 'Never'],
         'a': 'B', 'why': 'That is when the customer feels best about you.'},
        {'q': 'Which referral offer is the safest?',
         'o': ['Rewards for every level of referrals below you', 'A one-level give-get: the new customer and the referrer each get a small reward', 'Paying for five-star reviews', 'A joining fee'],
         'a': 'B', 'why': 'One level keeps it simple and clearly away from pyramid schemes.'},
        {'q': 'Why ask, "How did you hear about us?"',
         'o': ['As small talk', 'To track which channels bring customers', 'To collect data to sell', 'The law requires it'],
         'a': 'B', 'why': 'Source tracking tells you where to spend your limited time.'},
        {'q': 'Of 26 new customers, 9 came from referral cards and 7 from Status. What should Nisha do?',
         'o': ['Stop the referral cards', 'Keep and improve the cards and Status, and review the weaker channels', 'Start paying for ads', 'Change nothing'],
         'a': 'B', 'why': 'Put more effort into what works, and fix or drop what doesn\'t.'},
    ],
    study='"Do Things That Don\'t Scale" (the part on delight), OpenStax 8.6 and the Direct Selling Rules note (about 35 minutes)',
    action='create a referral offer, ask 5 happy customers for referrals or reviews and start tracking sources',
)

LESSONS = [L1, L2, L3, L4]

MODULE = module(
    6,
    title='Marketing',
    weeks=(13, 15), hours=17,
    overview="""
Marketing is how the right people find out about you, understand what you offer and trust you enough to try it. For a small business in Kerala, that happens mostly through WhatsApp, Instagram, YouTube, Google Maps and, above all, people talking to each other.

You don't need an advertising budget. You need a clear position, a simple brand, useful content posted regularly, a complete Google profile and a reason for happy customers to tell others.
""",
    outcomes=[
        'Write a positioning statement and choose a name you can legally use',
        'Build a basic brand kit and a complete WhatsApp Business profile for ₹0–₹500',
        'Plan and publish two weeks of useful content, following honest disclosure rules',
        'Create a complete Google Business Profile and a routine for real reviews',
        'Run an honest referral offer and track where each customer came from',
    ],
    lessons=LESSONS,
    project='Marketing kit',
    project_steps=[
        'Your positioning statement, name check results and brand kit (L01).',
        'A screenshot of your complete WhatsApp Business profile (L01).',
        'Your 14-day content calendar with at least 10 posts published, and their results (L02).',
        'Your Google Business Profile, live or waiting for verification, or a note on the channel you use instead (L03).',
        'Your referral offer and the Source column in your Customers tab (L04).',
        'One paragraph: which channel brought the most replies and orders this month, and what you will do more of.',
    ],
    project_proof='The Founder Toolkit/06 Marketing folder with your brand kit, screenshots, content results and channel summary.',
    rubric=[
        ('Positioning', '"For everyone, best quality"', 'Clear but generic', 'A specific customer, category, benefit and proof'),
        ('Name and brand', 'Not checked', 'Checked on Google only', 'Trademark search, handles checked, a simple consistent kit'),
        ('Content', 'Random offers', 'Regular posts, mostly offers', 'Planned pillars, 10 or more posts, replies and orders tracked'),
        ('Local presence', 'None', 'A profile with gaps', 'Complete Google profile and WhatsApp Business, with real reviews'),
        ('Word of mouth', 'Hoping it happens', 'Asking sometimes', 'Referral offer, review routine and source tracking'),
    ],
    short=[
        'L01: write the positioning statement and complete WhatsApp Business; use your name as plain text instead of a logo.',
        'L02: post one useful thing a day on WhatsApp Status for 7 days.',
        'L03: create the Google profile and ask 3 customers for reviews.',
        'L04: ask your 3 happiest customers for one referral each.',
    ],
    mistakes=[
        ('Spending on design before you have customers.', 'Start with free tools; upgrade from profits.'),
        ('Trying to be on every platform.', 'Pick the one or two channels where your customers already are.'),
        ('Fake reviews or bought followers.', 'They break platform rules and trust, and misleading claims can break the law.'),
    ],
)
