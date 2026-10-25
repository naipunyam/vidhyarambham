from common import lesson, module, link, ASOF

L1 = lesson(
    11, 1,
    title='Google Business Profile and local discovery',
    weeks=(27, 27), hours=2,
    outcome='Explain how a free Google Business Profile helps local businesses get found, check any business\'s profile against Google\'s ranking factors, and connect it with the business\'s social accounts.',
    split='30 minutes study, 1 hour 30 minutes action',
    core=f"""
### Social media and Google work together

When people in Kuttiady hear about a shop on Instagram or WhatsApp, many then search for it on Google or Maps to check the location, timings and reviews. A missing or wrong **Google Business Profile** loses customers your social posts worked hard to win. The profile is free: Google says it lets a business manage how it appears on Search and Maps "at no charge" ({ASOF}).

The Entrepreneurship course covers setting up a profile from scratch in ENT-M06-L03. Here you learn to check and improve profiles as a social media marketer.

### How Google decides local ranking

Google's help page names three factors:

- **Relevance:** how well the profile matches the search, helped by complete, accurate information: category, description, products and services, attributes
- **Distance:** how far the business is from the searcher (you can't change this)
- **Prominence:** how well known the business is, helped by reviews and replies, photos, and links from other websites

It also says plainly: **there is no way to request or pay for a better local ranking**. Be suspicious of anyone who sells "Google ranking".

### What a strong profile has

- The correct **name** (the real business name, no extra keywords), **category**, **address or service area**, **phone** and **hours**, including holiday hours
- A clear **description** with what the business offers and where
- **Photos and videos** taken recently by the business: front of the shop (so people can find it), inside, products, staff with consent
- **Products or services** with prices where possible
- **Regular updates** (posts about offers, events, new stock)
- **Links**: website, WhatsApp, Instagram and Facebook, where the profile offers them
- **Reviews** with replies to most of them, including the negative ones (SMM-M11-L03)

### Getting access the safe way

To work on a client's profile, the owner adds you as a **manager** from their profile settings. Never ask for the owner's Google password, and never create a second profile for the same business; duplicates confuse customers and break Google's rules.

### Other local discovery routes

- **Instagram:** location tags on every post about a place, and the area in the bio
- **Local Facebook groups** and **WhatsApp Status**, where many local recommendations spread
- **Local pages** like your practice page, which can feature businesses honestly
- **Word of mouth**, helped by referrals (SMM-M11-L03 and ENT-M06-L04)
""",
    example="""
Riyas at **Malabar Mobiles** searched "mobile repair Kuttiady" on his phone and couldn't find his shop on the map. Anu looked at his profile with him (as a manager he added):

| Before | After |
| --- | --- |
| Category "Store" | Primary category "Mobile phone repair shop", plus a phone accessories category |
| Hours missing; closed on Friday afternoons not shown | Full hours, Friday break shown |
| 2 photos, one blurry | 14 recent photos: shop front from the road, counter, repair desk, products |
| No description | "Mobile phone repair and accessories in Kuttiady town, near the bus stand. Screens, batteries, charging ports. Most repairs same day." |
| 11 reviews, no replies | Replies to all 11; a review card with a QR code at the counter |
| No links | WhatsApp and Instagram links added |

Over the following weeks, calls and direction requests from the profile rose, and two customers said they found the shop on Maps.

(Made-up example to show the method.)
""",
    resources=[
        ('gbp-start', 'Read what a profile can include', '5 min'),
        ('gbp-rank', 'Read the three ranking factors and the tips', '10 min'),
        ('gbp-reviews', 'Read how to ask for and reply to reviews', '10 min'),
    ],
    steps=[
        'Study the resources (about 25 minutes).',
        'Choose 3 local businesses you might audit in SMM-M11-L04. Search for each on Google Maps the way a customer would.',
        'Check each public profile with the checklist and score it.',
        'For the weakest, write 5 specific improvements in plain words for the owner.',
        'Note each business\'s social links and whether the details (name, phone, hours) match across Google, Instagram and WhatsApp.',
    ],
    proof='Three completed Google Business Profile checklists with scores and 5 written improvements for one business.',
    templates=[
        ('Google Business Profile checklist (score 0-2 each)', """
[ ] Found when searching "[service] [town]"
[ ] Real business name (no keyword stuffing)
[ ] Correct primary category (+ useful extra ones)
[ ] Address or service area correct; pin in the right place
[ ] Phone works; hours correct, incl. holidays and breaks
[ ] Description: what, where, what's special
[ ] 10+ recent photos: shop front, inside, products
[ ] Products or services listed, with prices if possible
[ ] Updates in the last 30 days
[ ] Website, WhatsApp and social links added
[ ] Reviews: recent ones; replies to most, incl. negative
[ ] Same name, phone and hours as Instagram and WhatsApp
TOTAL: ___ / 24
""", ''),
        ('profile improvement note for an owner (English and Malayalam)', """
EN: Hi [name], I checked how [business] looks on Google
Maps. Five quick fixes could help more nearby customers
find you: 1. ____ 2. ____ 3. ____ 4. ____ 5. ____
I'm happy to help you do them.
ML: നമസ്കാരം [പേര്], [ബിസിനസ്] ഗൂഗിൾ മാപ്പിൽ എങ്ങനെ കാണുന്നു
എന്ന് നോക്കി. അഞ്ച് ചെറിയ മാറ്റങ്ങൾ കൊണ്ട് കൂടുതൽ ആളുകൾക്ക്
നിങ്ങളെ കണ്ടെത്താം: 1. ____ 2. ____ 3. ____ 4. ____ 5. ____
ചെയ്യാൻ സഹായിക്കാം.
""", ''),
    ],
    mistakes=[
        ('Keyword stuffing the business name.', 'Use the real name; add keywords in the description and services.'),
        ('Asking for the owner\'s password.', 'Ask the owner to add you as a manager.'),
        ('Ignoring negative reviews.', 'Reply calmly and helpfully; future customers read replies.'),
        ('Old or stock photos.', 'Recent, real photos, including the shop front.'),
        ('Paying for "Google ranking" services.', 'Google says ranking can\'t be bought.'),
    ],
    quiz=[
        {'q': 'Which three factors does Google name for local ranking?',
         'o': ['Price, ads and age', 'Relevance, distance and prominence', 'Followers, likes and shares', 'Hashtags, hours and colours'],
         'a': 'B', 'why': 'That is how Google\'s help page explains local results.'},
        {'q': 'Can a business pay Google for a better local ranking?',
         'o': ['Yes, monthly', 'No; Google says there is no way to request or pay for it', 'Only in Kerala', 'Only with reviews'],
         'a': 'B', 'why': 'Ranking comes from relevance, distance and prominence.'},
        {'q': 'How should you get access to a client\'s profile?',
         'o': ['Ask for their Google password', 'The owner adds you as a manager', 'Create a new profile for them', 'Use a fake account'],
         'a': 'B', 'why': 'It is safe and keeps the owner in control.'},
    ],
    study='Google Business Profile help on features, local ranking and reviews (about 25 minutes)',
    action='check 3 local businesses\' Google profiles and write 5 improvements for the weakest',
)

L2 = lesson(
    11, 2,
    title='Selling on WhatsApp and Instagram',
    weeks=(27, 27), hours=2,
    outcome='Design a simple, safe chat-to-order flow for a local business, from a Reel or Status to a confirmed, paid and delivered order, with message scripts and an order sheet.',
    split='25 minutes study, 1 hour 35 minutes action',
    core=f"""
### Social commerce, the Kerala way

For most small businesses near Kuttiady, selling online doesn't mean a website with a cart. It means a **chat**: people see a Reel, a Status or a catalogue, send a message, and pay by UPI or cash. The business that answers fastest and makes ordering easiest wins.

### The chat-to-order flow

| Step | What happens | Tools |
| --- | --- | --- |
| **1. Discover** | Sees a Reel, Status, Channel post or a friend's forward | Instagram, WhatsApp Status and Channel, local groups |
| **2. Browse** | Looks at products and prices | WhatsApp Business catalogue, a pinned price-list post, Instagram Highlights |
| **3. Ask** | Sends a message | Click-to-chat link in bios, quick replies, greeting message |
| **4. Confirm** | Business sends an order summary | A saved order-confirmation message |
| **5. Pay** | UPI QR or ID, or cash on delivery | The business's own UPI QR |
| **6. Deliver** | Delivery or pick-up | A delivery note with time |
| **7. Follow up** | Thank-you, review request, reorder reminder | Labels, business broadcasts to people who agreed |

Instagram's in-app shopping features vary by country and account, so for most Indian small businesses the flow runs through DMs and WhatsApp ({ASOF}).

### Make every step easier

- **Prices visible** in the catalogue and posts. "DM for price" loses customers.
- **One-tap contact:** WhatsApp link or button in every bio (Instagram allows up to five links).
- **Fast replies:** greeting and away messages, and quick replies for price, delivery and payment.
- **A clear order summary** before payment, so nobody is confused about what, how many, how much and when.
- **Labels** for each stage: New enquiry, Confirmed, Paid, Delivered, Repeat customer.
- **Business broadcasts** to people who agreed, for restocks and festival pre-orders, with a way to stop.

### Payment safety

- Share the **business's own** UPI QR or ID. Never ask a customer for their UPI PIN, OTP or card details; the business never needs them.
- **Check the money in the bank app** before you dispatch. Fake payment screenshots are a common trick.
- For cash on delivery, agree it before you send, and consider an advance for large or custom orders.

### Clear policies prevent fights

Write simple rules in a Highlight or the catalogue: delivery area and charges, order cut-off times, cancellation, what happens if something is wrong, and refunds. Consumer protection law applies to online sales too (ENT-M09-L03 covers it).
""",
    example="""
**Amma's Pickles** set up this flow (made-up example):

1. **Discover:** a Reel of the day's mango pickle batch; the same clip on WhatsApp Status.
2. **Browse:** catalogue with 8 pickles, weights and prices; "Price list" Highlight on Instagram.
3. **Ask:** "Hi, mango pickle 500 g?" → quick reply with the catalogue link and delivery areas.
4. **Confirm:** "Order: Mango pickle 500 g × 1 = ₹230. Delivery to Perambra town tomorrow by 1 pm, ₹20. Total ₹250. Pay by UPI to the QR below, or cash on delivery. Reply OK to confirm."
5. **Pay:** customer pays; Lakshmi checks the bank app before marking "Paid".
6. **Deliver:** "Your pickle is on the way, arriving about 12:30." Label "Delivered".
7. **Follow up:** "Thank you! If you liked it, a Google review helps us a lot: [link]." Three weeks later, a broadcast (to customers who agreed): "New batch of prawn pickle ready."

Their order sheet showed that most repeat orders came within a month, so they timed reminder broadcasts at three weeks.
""",
    resources=[
        ('wa-tools', 'Re-read the catalogue, quick replies, labels and notes features', '5 min'),
        ('wa-broadcasts', 'Re-read business broadcasts and their buttons', '5 min'),
        ('wa-business', 'Check the current features in the app listing', '3 min'),
        ('tc-links', 'Re-read how to add up to five bio links', '3 min'),
        ('ig-best', 'Look at the Profile pages in the best practices hub', '5 min'),
    ],
    steps=[
        'Study the resources (about 20 minutes).',
        'Choose one business (one you audited, or a friend\'s) and draw its current chat-to-order flow: what happens at each of the 7 steps today.',
        'Design the improved flow with the tools above.',
        'Write the message scripts: greeting, price reply, order confirmation, payment, delivery and follow-up, in Malayalam and English.',
        'Build an order sheet in Google Sheets for the business.',
    ],
    proof='The before and after flow, your message scripts and the order sheet.',
    templates=[
        ('order confirmation and follow-up (English and Malayalam)', """
CONFIRM
EN: Order: [item] x [qty] = Rs ____. Delivery to ____ on
____ by ____, Rs ____. Total Rs ____. Pay by UPI (QR below)
or cash on delivery. Reply OK to confirm.
ML: ഓർഡർ: [ഐറ്റം] x [എണ്ണം] = ₹____. ____ ന് ____ ൽ ഡെലിവറി,
₹____. ആകെ ₹____. UPI (താഴെ QR) അല്ലെങ്കിൽ ക്യാഷ് ഓൺ ഡെലിവറി.
ഉറപ്പിക്കാൻ OK എന്ന് മറുപടി തരൂ.

PAID (after checking the bank app)
EN: Payment received, thank you! We'll deliver by ____.
ML: പേയ്മെന്റ് കിട്ടി, നന്ദി! ____ നുള്ളിൽ എത്തിക്കാം.

FOLLOW-UP (2-3 days later)
EN: Hope you enjoyed it! A Google review helps us a lot:
[link]
ML: ഇഷ്ടമായെന്ന് കരുതുന്നു! ഒരു ഗൂഗിൾ റിവ്യൂ ഞങ്ങൾക്ക് വലിയ സഹായമാണ്:
[link]
""", ''),
        ('order sheet', """
Order ID,Date,Customer name,Phone (with consent),Source (Reel/Status/Channel/group/ad/referral),Items,Quantity,Amount (Rs),Delivery charge (Rs),Payment (UPI/cash),Paid checked in bank app (Y/N),Delivery date,Status,Review asked (Y/N),Repeat customer (Y/N),Notes
""", 'csv'),
        ('payment safety checklist', """
[ ] Share only the business's own UPI QR or ID
[ ] Never ask for a customer's PIN, OTP or card number
[ ] Check the credit in the bank app before dispatch
[ ] Don't trust payment screenshots alone
[ ] Advance for large or custom orders
[ ] Written delivery, cancellation and refund rules
""", ''),
    ],
    mistakes=[
        ('"DM for price".', 'Show prices; people who must ask often don\'t.'),
        ('Slow replies.', 'Use greeting, away and quick replies; answer within minutes during open hours.'),
        ('No order summary.', 'Confusion about quantity or delivery causes most complaints.'),
        ('Dispatching on a screenshot.', 'Check the bank app; fake screenshots are common.'),
        ('Broadcasting to everyone.', 'Only people who agreed, with a way to stop.'),
    ],
    quiz=[
        {'q': 'Before sending an order paid by UPI, you should:',
         'o': ['Trust the customer\'s screenshot', 'Check the credit in the business\'s bank app', 'Ask for their UPI PIN', 'Ask for their OTP'],
         'a': 'B', 'why': 'Screenshots can be faked; the bank app is the proof.'},
        {'q': 'Why send an order summary before payment?',
         'o': ['It\'s required by Instagram', 'It prevents confusion about item, quantity, price and delivery', 'To get more likes', 'To avoid replying'],
         'a': 'B', 'why': 'Most complaints start with misunderstandings.'},
        {'q': 'Which is the best way to show prices?',
         'o': ['"DM for price"', 'In the catalogue and posts, clearly', 'Only by phone', 'Never'],
         'a': 'B', 'why': 'Visible prices remove a barrier to ordering.'},
    ],
    study='WhatsApp Business tools and broadcasts and Instagram profile links (about 20 minutes)',
    action='design an improved chat-to-order flow with message scripts and an order sheet for one business',
)

L3 = lesson(
    11, 3,
    title='Genuine reviews, referrals and local events',
    weeks=(28, 28), hours=1.5,
    outcome='Help a business collect genuine reviews and reply to them well, design honest referral offers, and plan content around a local event, all within the rules on fake and incentivised reviews.',
    split='25 minutes study, 1 hour 5 minutes action',
    core=f"""
### Reviews: the most trusted posts a business has

Before choosing a new shop, many people read its Google reviews and look at what customers say on social media. Reviews also help **prominence** in Google's local ranking. The Entrepreneurship course covers word of mouth and reviews for owners in ENT-M06-L04; this lesson is about running it as a marketer.

### Ask the right way

- **Ask at the happy moment:** when the customer collects the cake, after a repair that worked, at check-out from the homestay.
- **Make it easy:** a short link or a QR code on a counter card, receipt or WhatsApp follow-up. Google's tips suggest exactly this.
- **Ask everyone,** not just the customers you think are happy.
- **Reply to reviews:** thank people by name, and reply to negative ones calmly with how you'll fix it. Google notes that thoughtful replies can lead customers to update their reviews.

### What is never allowed ({ASOF})

- **Incentives:** Google says offering free or discounted goods or services in exchange for reviews is **strictly prohibited**, and so is offering something to change or remove a review. Its policy on incentivised or biased reviews covers any payment, discount, free item or other benefit.
- **Fake engagement:** Google's Maps policy describes fake engagement as content that doesn't represent a genuine experience: reviews by owners, staff or family, reviews swapped between businesses, or bought reviews.
- **India's standard:** IS 19000:2022 from the Bureau of Indian Standards sets principles for collecting, moderating and publishing online reviews. It is voluntary for now, expects paid reviews to be disclosed, and bars publishing reviews bought or written by people employed for that purpose (check current rules).
- **Testimonials** used in your posts must be real and shared with the customer's permission.

### Referrals that stay honest

A referral offer rewards customers for bringing friends: "Bring a friend to Peak Fitness: you both get a free week." Keep it separate from reviews (never "review us and get a discount"), make the terms clear, and honour it every time.

### Local events

Events give you timely content and new audiences:

- **Before:** announce it, count down, collaborate with the organisers, plan pre-orders.
- **During:** Stories and short clips, a live if suitable; capture the atmosphere and the business's part in it.
- **After:** a recap Reel, thank the people involved, share customers' posts with permission.

At religious festivals, school events and funerals or memorials, be respectful: ask organisers before filming, avoid filming children who aren't yours without a parent's consent, and don't turn sacred moments into ads.
""",
    example="""
**Nisha's Oven** planned Onam (made-up example):

- **Two weeks before:** Reel "Onam payasam cakes: pre-orders open", Status countdown, a collab with a local caterer for sadya-plus-dessert combos, WhatsApp business broadcast to customers who agreed.
- **Onam week:** Stories of the packing, a 20-second Reel of the busiest morning, the order cut-off posted every day.
- **After:** thank-you Reel with customers' photos (shared with permission), a review card in every box ("Did you enjoy it? A Google review helps a small home bakery a lot", with a QR code) and a referral offer for the next order: "Recommend us to a friend: you both get ₹50 off your next cake."

She received 23 new Google reviews that month, all from real customers, and replied to every one, including two that mentioned a late delivery.
""",
    resources=[
        ('gbp-reviews', 'Re-read the tips and the rules on incentives', '5 min'),
        ('maps-incent', 'Read the policy on incentivised or biased reviews', '5 min'),
        ('maps-fake', 'Read the fake engagement policy', '5 min'),
        ('bt-is19000', 'Read what IS 19000:2022 says about paid and staff reviews', '5 min'),
    ],
    steps=[
        'Study the resources (about 20 minutes).',
        'Write a review-request flow for one business: when, how (link or QR) and the exact message, in Malayalam and English.',
        'Write replies to three sample reviews: a 5-star, a 3-star and a 1-star complaint.',
        'Design one honest referral offer with clear terms.',
        'Plan content for one upcoming local event or festival: before, during and after, with consent notes.',
    ],
    proof='Your review-request flow, three review replies, the referral offer and the event content plan.',
    templates=[
        ('review request (English and Malayalam)', """
COUNTER CARD
EN: Enjoyed it? A Google review helps a small business
a lot. Scan the QR (takes 1 minute). Thank you!
ML: ഇഷ്ടമായോ? ഒരു ഗൂഗിൾ റിവ്യൂ ചെറിയ ബിസിനസിന് വലിയ സഹായമാണ്.
QR സ്കാൻ ചെയ്യൂ (ഒരു മിനിറ്റ് മതി). നന്ദി!
WHATSAPP (2-3 days after the purchase)
EN: Hi [name], thank you for choosing us! If you have a
minute, a Google review would mean a lot: [link]
NEVER: "Review us and get a discount" / "5 stars for a
free gift" (incentives are prohibited)
""", ''),
        ('review replies', """
5 STARS: Thank you, [name]! So glad you liked [specific].
  See you again soon!
3 STARS: Thank you for the honest feedback, [name]. We're
  working on [issue]. Please tell us next time so we can
  make it right.
1 STAR:  We're sorry, [name]. This isn't the experience we
  want for you. Please WhatsApp us on ____ so we can fix
  it today. (Then fix it. Never argue in public.)
""", ''),
        ('event content plan', """
EVENT: __________  DATE: ____  ORGANISER: ________
PERMISSION TO FILM: from ______ (Y/N)
BEFORE (2 weeks): announce ____ / countdown ____ /
  collab with ____ / pre-orders ____
DURING: Stories ____ / short clips ____ / live? Y/N
  Consent: people featured ____; no children without
  a parent's OK
AFTER: recap Reel ____ / thank-you ____ / shared customer
  posts (with permission) ____ / review card ____
""", ''),
    ],
    mistakes=[
        ('Offering discounts for reviews.', 'Google strictly prohibits incentives for reviews.'),
        ('Asking family and staff to review.', 'That is fake engagement; their reviews can be removed and the profile restricted.'),
        ('Ignoring bad reviews.', 'Reply calmly, take it to private messages, fix the problem.'),
        ('Filming at events without asking.', 'Ask organisers and people; be careful with children and sacred moments.'),
    ],
    quiz=[
        {'q': 'Which is allowed by Google?',
         'o': ['A ₹50 discount for a 5-star review', 'Asking every customer for a review with a link or QR code', 'Staff writing reviews', 'Paying for reviews'],
         'a': 'B', 'why': 'Asking is fine; incentives and fake reviews are not.'},
        {'q': 'What does IS 19000:2022 cover?',
         'o': ['GST rates', 'Principles for collecting, moderating and publishing online consumer reviews', 'Instagram hashtags', 'Ad budgets'],
         'a': 'B', 'why': 'It is the BIS standard on online reviews (voluntary for now).'},
        {'q': 'An honest referral offer should be:',
         'o': ['Tied to leaving a review', 'Separate from reviews, with clear terms that are always honoured', 'Secret', 'Only for staff'],
         'a': 'B', 'why': 'Keep referrals and reviews separate and transparent.'},
    ],
    study='Google\'s review tips and policies and the BIS online review standard (about 20 minutes)',
    action='write a review-request flow, three review replies, a referral offer and an event content plan',
)

L4 = lesson(
    11, 4,
    title='Audit 3 local businesses and pitch a pilot',
    weeks=(28, 28), hours=3,
    outcome='Audit the social media of three real local businesses with a scored checklist, write clear recommendations they can act on, and pitch a free 4-week pilot to one of them.',
    split='20 minutes study, 2 hours 40 minutes action',
    core="""
### Why audits are your best door-opener

An audit is a structured check of what a business does well and badly online, with clear recommendations. Done well, it shows a busy owner in ten minutes that you understand their business and can help. It's also the best practice you can get: every audit trains your eye.

Ask before you audit: "I'm learning social media marketing and practising audits. Can I look at your pages and share what I find, free?" Most owners are happy to say yes.

### The eight-part audit

Score each part 0 (missing or poor), 1 (some) or 2 (good), using public information and a conversation with the owner:

| Part | What you check |
| --- | --- |
| **1. Findability** | Google Business Profile (SMM-M11-L01), search results, same handle and details everywhere |
| **2. Profiles** | Bios, links, contact buttons, hours, Highlights, profile photos |
| **3. Content** | Pillars, quality (light, sound, hooks), originality, consistency over the last 30 days |
| **4. Engagement** | Do they reply to comments and messages, and how fast (ask the owner)? |
| **5. Path to buy** | WhatsApp link, catalogue, visible prices, clear CTAs (SMM-M11-L02) |
| **6. Proof** | Reviews, replies, testimonials with permission |
| **7. Measurement** | Do they know where customers come from? Any tracking? |
| **8. Rules and safety** | Disclosure on paid posts, music use, consent, two-step verification on accounts |

Total out of 16. Then pick **three quick wins** (things the owner can fix in a day) and **three bigger recommendations** (a month or more).

### Writing recommendations owners act on

- **Specific:** "Add your shop's opening hours to Google and your Instagram bio" beats "improve your profiles".
- **Prioritised:** quick wins first.
- **Shown, not told:** a screenshot of the problem, and a mock-up of the fix where you can.
- **No jargon:** "people who don't follow you yet" rather than "non-follower reach".
- **Short:** one or two pages, plus a five-line summary in Malayalam if the owner prefers.

### Pitching the pilot

Offer one business a **free 4-week pilot**: you'll do a defined set of work, they'll provide access, photos and approvals, and at the end you'll give them a results report. In return you ask for permission to use the results as a case study and, if they're happy, a testimonial. Make the scope small enough to do well alongside your studies, for example: fix the Google profile and WhatsApp catalogue, three posts a week, daily Status ideas and a weekly update.

Put it in writing in a simple one-page **pilot agreement**: scope, dates, what each side does, how access is given (manager roles, never passwords), what you'll measure, consent for photos, and that either side can end it early. The Entrepreneurship course covers contract basics in ENT-M09-L03; Module 15 covers paid contracts.
""",
    example="""
Anu audited three businesses (made-up scores):

| Part | Nisha's Oven | Malabar Mobiles | Peak Fitness |
| --- | --- | --- | --- |
| Findability | 2 | 1 | 1 |
| Profiles | 2 | 0 | 1 |
| Content | 2 | 0 | 1 |
| Engagement | 2 | 1 | 1 |
| Path to buy | 2 | 1 | 1 |
| Proof | 1 | 1 | 0 |
| Measurement | 1 | 0 | 0 |
| Rules and safety | 1 | 1 | 1 |
| **Total (of 16)** | **13** | **5** | **6** |

Malabar Mobiles had the most to gain. Riyas's quick wins: hours on Google and Instagram, a WhatsApp link in the bio, a repair price list post. Bigger ones: a weekly repair-tip Reel, a review card at the counter, asking every customer "how did you hear about us?".

She pitched a 4-week pilot in the shop in Malayalam, showed two screenshots from the audit, and left a one-page agreement. Riyas signed the next day.
""",
    resources=[
        ('gbp-rank', 'Re-read the local ranking factors for part 1', '5 min'),
        ('ig-reco', 'Re-read the recommendation rules for part 3', '5 min'),
        ('asci-faqs', 'Re-read the disclosure placement rules for part 8', '5 min'),
        ('wa-tools', 'Re-read the WhatsApp Business tools for part 5', '5 min'),
    ],
    steps=[
        'Study the resources (about 20 minutes).',
        'Ask three local businesses (ideally of different types) whether you may audit their social media for free.',
        'Audit each with the eight-part checklist, from their public pages and a 10-minute talk with the owner. Take screenshots.',
        'Write a one-to-two-page audit report for each, with three quick wins and three bigger recommendations, and share it with the owner.',
        'Pitch a free 4-week pilot to the business that would gain most and is keen. Agree the scope and sign the one-page pilot agreement.',
    ],
    proof='Three scored audit checklists, three audit reports (shared with the owners), and the signed pilot agreement (or notes of the pitch if it was declined, and your next pitch).',
    fulltime='Do the audits and pitch as soon as the 30-day challenge is finished, so the 4-week pilot can run in real days while you study Modules 12 to 16.',
    templates=[
        ('audit checklist and scoring', """
BUSINESS: __________  TYPE: ______  DATE: ____
OWNER'S PERMISSION: yes, on ____
Score 0 (missing/poor), 1 (some), 2 (good)
1. Findability (Google profile, search, consistent
   details)                                      ___
2. Profiles (bios, links, buttons, hours)        ___
3. Content (pillars, quality, originality,
   consistency, last 30 days)                    ___
4. Engagement (replies, speed)                   ___
5. Path to buy (WhatsApp, catalogue, prices, CTAs) ___
6. Proof (reviews, replies, testimonials)        ___
7. Measurement (knows where customers come from) ___
8. Rules and safety (disclosure, music, consent,
   two-step verification)                        ___
TOTAL ___ / 16
QUICK WINS: 1. ____ 2. ____ 3. ____
BIGGER: 1. ____ 2. ____ 3. ____
""", ''),
        ('audit report outline (1-2 pages)', """
[BUSINESS] - SOCIAL MEDIA CHECK-UP, [DATE]
What's working well: 2-3 points (start positive)
Score: ___ / 16 (table of the 8 parts)
Quick wins (this week): 1-3, each with a screenshot
Bigger opportunities (this month): 1-3
What I'd measure: enquiries per week, from where
Malayalam summary (5 lines): ____________
Offer: a free 4-week pilot to do the quick wins and
test the bigger ideas, with a results report.
""", ''),
        ('pilot agreement (one page)', """
PILOT AGREEMENT
Between: [business, owner name] and [your name]
Dates: [start] to [end] (4 weeks)
I will: [e.g. fix Google profile and WhatsApp catalogue;
  3 posts a week; Status ideas daily; weekly update;
  final results report]
You will: give access as manager/editor (never
  passwords); send photos and offers; approve posts
  within 24 hours; tell customers to mention the page
Measuring: [enquiries, calls, WhatsApp chats, orders]
  starting from last week's numbers: ____
Photos of staff and customers: only with their consent
Cost: free. In return: permission to use the results
  (and a testimonial if you're happy) in my portfolio
Either side can end the pilot early with notice.
Signed: ________ (owner)  ________ (me)  Date: ____
""", ''),
    ],
    mistakes=[
        ('Auditing without asking.', 'Ask first; it builds the relationship you need for the pilot.'),
        ('Only criticism.', 'Start with what works, then the fixes.'),
        ('Vague advice.', 'Specific actions with screenshots get done.'),
        ('A pilot that\'s too big.', 'Promise less and deliver it well alongside your studies.'),
        ('Taking passwords.', 'Ask for manager or editor roles instead.'),
    ],
    quiz=[
        {'q': 'Why start an audit report with what\'s working?',
         'o': ['To pad the report', 'Owners listen better when you show you understand their business', 'It\'s legally required', 'To avoid giving advice'],
         'a': 'B', 'why': 'Respect first makes the recommendations land.'},
        {'q': 'Which is a good quick win?',
         'o': ['Rebuild the whole brand', 'Add correct hours and a WhatsApp link to the Instagram bio', 'Start a podcast', 'Run a ₹50,000 ad campaign'],
         'a': 'B', 'why': 'Quick wins can be done in a day and show results fast.'},
        {'q': 'What should a pilot agreement include about access?',
         'o': ['The owner\'s passwords', 'Manager or editor roles, never passwords', 'Nothing', 'A new account for the business'],
         'a': 'B', 'why': 'Roles keep the owner in control and you safe.'},
        {'q': 'What do you ask for in return for a free pilot?',
         'o': ['Nothing at all', 'Permission to use the results as a case study, and a testimonial if they\'re happy', 'Their customer list', 'Payment later no matter what'],
         'a': 'B', 'why': 'Case studies and testimonials build your portfolio honestly.'},
    ],
    study='Google\'s ranking factors, Instagram\'s recommendation rules, ASCI\'s disclosure FAQs and WhatsApp Business tools, as audit criteria (about 20 minutes)',
    action='audit 3 local businesses, share the reports and sign a pilot agreement with one',
)

L5 = lesson(
    11, 5,
    title='Run a 4-week pilot: a no-cost organic campaign for a real business',
    weeks=(29, 32), hours=8,
    outcome='Plan and run a 4-week organic campaign for a real local business with a clear goal, a baseline, weekly updates and honest measurement, without spending money.',
    split='30 minutes study and planning, about 7 hours 30 minutes of client work over 4 weeks',
    core="""
### A campaign is a plan with a goal and an end date

Posting for a business isn't a campaign. A **campaign** has one goal, one main message, a fixed time, a plan and a way to measure. Your pilot is a 4-week, no-cost organic campaign.

### The campaign brief

Write it on one page before you start, and agree it with the owner:

1. **Goal and KPI:** "More repair enquiries: WhatsApp chats and calls that mention Instagram, Google or the page."
2. **Baseline:** the same numbers for the week before the pilot (ask the owner to count, or use labels and Google profile insights).
3. **Target:** realistic, from the baseline: "from about 8 to 15 enquiries a week by week 4".
4. **Audience:** from a quick persona (SMM-M02-L02).
5. **Message and offer:** one main idea: "Most repairs the same day, near the bus stand." An offer only if the owner wants one and it's honest.
6. **Channels and rhythm:** for example, 3 Reels or posts a week, a daily Status idea, one Google profile update a week, replies within an hour.
7. **Tracking:** a keyword in the CTA, WhatsApp labels, "how did you hear about us?", UTM links for any website.
8. **Roles and approvals:** who sends photos, who approves, by when.
9. **Rules:** consent for photos, honest claims, disclosure if any creator gets a free service.

### No-cost tactics that work locally

- Fix the basics first (the audit's quick wins).
- Short videos of real work, with hooks (Module 4).
- Google profile updates and photos, and a review card at the counter.
- WhatsApp Status daily, and business broadcasts to customers who agreed.
- A collaboration with a complementary local account or your own page, disclosed if anything is given free.
- A post in local Facebook groups where the rules allow.
- A tie-in with a local event or season.

If the owner wants to try a small paid boost and pays for it, use Module 9's plan, and report it separately from the organic results.

### Onboarding in the first two days

- Access through roles: manager on the Google profile, the Page and Instagram connected in Meta Business Suite with you added as a partner or with a task role, and WhatsApp Business run by the owner unless agreed otherwise. Never passwords.
- Collect: logo and colours, photos, price list, FAQs, the owner's do's and don'ts.
- Set up the tracking (labels, keyword, the "how did you hear" question).

### The weekly cycle

Plan → create → owner approves → publish → reply and engage → count → send the weekly WhatsApp update (SMM-M08-L03). Fill in the **Pilot** tab every week.

### Finishing well

In week 4, write the results report (the module project), ask for a testimonial if the owner is happy, and talk about what comes next: continuing as a paid service (Module 15), or handing over a simple plan they can run themselves.
""",
    example="""
Anu's pilot for **Malabar Mobiles** (made-up numbers to show the method):

| Week | Main work | Posts | Enquiries (chats and calls) | Repairs from those enquiries |
| --- | --- | --- | --- | --- |
| Baseline (week before) | — | 0 | 8 | 5 |
| 1 | Google profile fixed, WhatsApp catalogue and quick replies, review card, 2 Reels | 3 | 11 | 7 |
| 2 | "Is your battery dying?" Reel, price-list carousel, Status daily | 3 | 14 | 9 |
| 3 | Collab with @kuttiady.diaries ("Shop story": Riyas, 12 years of repairs), disclosed | 3 | 19 | 12 |
| 4 | Screen-guard Reel, reviews push, Google update | 3 | 17 | 11 |

Enquiries roughly doubled from the baseline by weeks 3 and 4, and the shop got 14 new Google reviews. Riyas wrote a two-line testimonial and asked about a monthly package.
""",
    resources=[
        ('gbp-start', 'Re-read what you can add to the client\'s profile', '5 min'),
        ('wa-broadcasts', 'Re-read business broadcasts for the client\'s opted-in customers', '5 min'),
        ('ga4-utm', 'Re-read UTM rules if the business has a website', '5 min'),
        ('mbs-app', 'Re-read what Meta Business Suite manages for a Page and Instagram', '5 min'),
    ],
    steps=[
        'Study the resources (about 20 minutes) and write the one-page campaign brief with the owner, including the baseline week\'s numbers.',
        'Days 1–2: onboarding: roles not passwords, brand materials, tracking set up.',
        'Weeks 1–4: run the weekly cycle. Fill in the Pilot tab every week and send the owner a weekly WhatsApp update.',
        'Keep consent notes for anyone filmed, and label any collaboration correctly.',
        'In week 4, collect the final numbers, screenshots and (if the owner is happy) a testimonial.',
    ],
    proof='The signed-off campaign brief, 4 weekly Pilot tab rows and 4 weekly updates, links to every post, and the final numbers with screenshots.',
    fulltime='The pilot runs for 4 real weeks. On the full-time pace, start it right after the audits and keep studying Modules 12 to 16 while it runs; tick this task when week 4 is done.',
    templates=[
        ('campaign brief (one page)', """
BUSINESS: __________  DATES: ____ to ____ (4 weeks)
GOAL: ______________  KPI: ______________
BASELINE (week before): ____  TARGET (week 4): ____
AUDIENCE: ____________________________
MAIN MESSAGE: ________________________
OFFER (if any, honest): ______________
CHANNELS AND RHYTHM: __ posts/week on ____; Status
  daily; Google update weekly; replies within ___
TRACKING: keyword "____" / WhatsApp labels / "how did
  you hear about us?" / UTM links (if website)
ROLES: owner sends ____ by ____; approves within 24 h
RULES: consent for photos; honest claims; disclose any
  free service or product given to creators
WEEKLY UPDATE: every ____ on WhatsApp
""", ''),
        ('onboarding checklist', """
[ ] Manager role on Google Business Profile
[ ] Page + Instagram in Meta Business Suite; my access by
    role, not password
[ ] WhatsApp Business: who replies, quick replies ready
[ ] Logo, colours, fonts, photo library, price list, FAQs
[ ] Owner's do's and don'ts written down
[ ] Tracking: keyword, labels, "how did you hear" question
[ ] Baseline numbers for the week before
[ ] Consent forms or voice notes ready for staff/customers
""", ''),
        ('weekly pilot log (Pilot tab)', """
Week,Posts,Views,Accounts reached,Profile visits,Calls,WhatsApp chats,Direction requests or visits,Orders or bookings,Revenue (Rs) if shared,What worked,What I'll change
""", 'csv'),
    ],
    mistakes=[
        ('No baseline.', 'Without last week\'s numbers there is no "before". Count before you start.'),
        ('Changing the goal mid-way.', 'Agree one goal at the start and report against it.'),
        ('Posting without approval.', 'Agree approval times; never post a client\'s content they haven\'t seen.'),
        ('Overclaiming.', 'Report what changed and what you can connect to your work; say what you can\'t.'),
        ('Disappearing after week 4.', 'Deliver the report and a next-step plan, paid or not.'),
    ],
    quiz=[
        {'q': 'What makes a set of posts a campaign?',
         'o': ['Using hashtags', 'One goal, one main message, a fixed time, a plan and measurement', 'Posting every day', 'Paying for ads'],
         'a': 'B', 'why': 'Without a goal and an end date, it\'s just posting.'},
        {'q': 'Why record a baseline week before the pilot?',
         'o': ['It isn\'t needed', 'So you can show the before-and-after change honestly', 'To fill time', 'Platforms require it'],
         'a': 'B', 'why': 'The baseline is the "before" in your case study.'},
        {'q': 'How should you track WhatsApp enquiries in the pilot?',
         'o': ['Guess', 'A CTA keyword, WhatsApp labels and asking "how did you hear about us?"', 'Count likes', 'Only Google Analytics'],
         'a': 'B', 'why': 'WhatsApp chats can\'t be tracked by GA4, so build your own tracking.'},
        {'q': 'If the owner wants a small boost during the pilot, you should:',
         'o': ['Pay for it yourself secretly', 'Use the Module 9 plan, let the owner pay, and report it separately from organic results', 'Refuse all ads', 'Mix it into the organic numbers'],
         'a': 'B', 'why': 'Keep paid and organic results separate so the case study stays honest.'},
    ],
    study='Google profile features, WhatsApp broadcasts, UTM rules and Meta Business Suite, for running the pilot (about 20 minutes)',
    action='run the 4-week pilot with a brief, a baseline, weekly logs and updates, and collect the final numbers',
)

LESSONS = [L1, L2, L3, L4, L5]

MODULE = module(
    11,
    title='Local business and social commerce',
    weeks=(27, 32), hours=19,
    overview="""
Use everything so far for real local businesses: Google Business Profile, selling through WhatsApp and Instagram, genuine reviews and local events. Then audit three real businesses and run a 4-week pilot for one of them.

This is where you start working with clients. In weeks 27–28 you'll learn how local discovery, chat-based selling and reviews work, audit three businesses with an eight-part checklist, and pitch a free pilot. In weeks 29–32 you'll run a no-cost organic campaign for that business, with a baseline, weekly updates and honest measurement.

Your 90-day growth sprint on your own account continues alongside. The pilot's results report becomes your second case study.
""",
    outcomes=[
        'Check and improve a Google Business Profile against Google\'s ranking factors',
        'Design a safe chat-to-order flow on WhatsApp and Instagram',
        'Collect genuine reviews and plan event content within the rules',
        'Audit a business\'s social media and write recommendations owners act on',
        'Plan and run a 4-week organic campaign and report it honestly',
    ],
    lessons=LESSONS,
    project='Case study 2: your pilot results report',
    project_week=32,
    project_steps=[
        'Write the pilot results report for the owner: goal, baseline, what you did each week, results against the target, what worked, what didn\'t, and three recommendations for the next three months.',
        'Turn it into a one-page case study for your portfolio (with the owner\'s permission): the challenge, what you did, before and after numbers, a testimonial if given.',
        'Show only real numbers. Separate any paid boost from organic results.',
        'Present the report to the owner in person or on a call, and discuss next steps.',
    ],
    project_proof='The owner\'s results report, the one-page case study and a note of the owner\'s response (and testimonial if given).',
    fulltime='The audits come right after the 30-day challenge and the pilot runs for 4 real weeks, ending around calendar week 14 on the full-time pace.',
    rubric=[
        ('Local discovery', 'Ignores Google', 'Checks a profile', 'Scores profiles and writes specific fixes'),
        ('Social commerce', 'No flow', 'Some scripts', 'A complete, safe chat-to-order flow with scripts and an order sheet'),
        ('Reviews and events', 'Incentivised or fake reviews', 'Asks for reviews sometimes', 'A genuine review flow, good replies, honest referrals, event plan'),
        ('Audits', 'Vague opinions', 'Checklists without recommendations', 'Three scored audits with prioritised, specific recommendations shared with owners'),
        ('Pilot', 'Not started', 'Posted for a business without a plan', 'Brief, baseline, weekly logs and updates, honest results report'),
    ],
    short=[
        'Audit 2 businesses instead of 3 (keep the full checklist).',
        'Run a 2-week pilot with 2 posts a week, keeping the baseline and weekly update.',
        'Write the review-request flow only.',
        'Write a half-page case study.',
    ],
    flashcards=[
        ('Three local ranking factors?', 'Relevance, distance, prominence.'),
        ('Can a business pay for better local ranking on Google?', 'No.'),
        ('Seven steps of the chat-to-order flow?', 'Discover, browse, ask, confirm, pay, deliver, follow up.'),
        ('Before dispatching a UPI order, check what?', 'The credit in the bank app, not a screenshot.'),
        ('Are discounts for reviews allowed on Google?', 'No, incentives for reviews are strictly prohibited.'),
        ('The eight audit parts?', 'Findability, profiles, content, engagement, path to buy, proof, measurement, rules and safety.'),
        ('What do you ask for in return for a free pilot?', 'Permission to use the results as a case study, and a testimonial if they\'re happy.'),
        ('Nine parts of a campaign brief?', 'Goal and KPI, baseline, target, audience, message and offer, channels and rhythm, tracking, roles, rules.'),
    ],
    mistakes=[
        ('Treating local businesses like big brands.', 'They need enquiries this month, simple tools and plain words.'),
        ('Saying yes to everything in a pilot.', 'A small, clear scope done well wins the paid work.'),
        ('Forgetting your own account.', 'Keep your sprint going; it is case study 3.'),
    ],
)
