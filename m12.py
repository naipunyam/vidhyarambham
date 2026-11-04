from common import lesson, module, link, rules, xref, table, fence, Q, RULE, ASOF, CHECK
import tools

SHOTS = [
    ('Plot', 'Front from the road; road in both directions; each boundary corner; the view from the middle; any well, trees or structures; the nearest landmark'),
    ('House exterior', 'Front at a slight angle; sit-out; the road; side and back; compound wall and gate; well, tank and parking'),
    ('House interior', 'Each room from the doorway corner (wide); kitchen counters; bathrooms (clean, lid down); stairs; balcony view'),
    ('Honest details', 'Any crack, damp patch or slope you will mention in the listing'),
]

L1 = lesson(
    12, 1,
    outcome='You can take clear, honest listing photos and a walkthrough video on an Android phone and put together a simple virtual tour.',
    split='15 minutes reading, 45 minutes shooting and editing',
    core=f"""
Most buyers, especially NRIs, decide whether to visit from photos and video. Good, honest visuals save everyone time.

**Before you shoot:** the owner's written permission to photograph and publish (mandate, RE-M10-L02); clean and tidy the property; open curtains and windows; switch on lights; remove personal items (photos, documents, vehicles with number plates visible, people). Shoot in **soft daylight** (morning or late afternoon); avoid harsh noon sun and rainy darkness.

**Phone settings:** clean the lens; turn on gridlines; hold the phone horizontally (landscape) for portal photos and vertically for Reels and Status; use 0.5x (wide) only if it doesn't distort badly; keep the phone level (vertical lines straight); tap to focus and slide exposure down slightly if windows are blown out.

**Shot list:**
{table(['Property', 'Shots'], SHOTS)}

**Walkthrough video (60 to 120 seconds):**
1. Start at the road: show road width and the gate.
2. Walk slowly in one continuous path, holding the phone at chest height with both hands (or a cheap gimbal later).
3. Pause 2 to 3 seconds in each room.
4. Record a short voice-over or add captions afterwards: size, cents, distance to town, honest notes.
5. End with the location (village and a landmark, not the exact address).
Free editing: the phone's built-in editor, or apps covered in the {xref('smm', 'smm-m04-l04', 'Social Media Marketing lesson on editing on your phone')}. For lighting and framing basics, see the {xref('smm', 'smm-m04-l03', 'lesson on shooting with your phone')}.

**Simple virtual tour:** an ordered photo album (Google Photos shared album or a PDF), the walkthrough video and, for land, a **Google Earth** view with the boundary drawn ({link('gearth', 'Google Earth')}), so NRIs see the surroundings. Use your phone's panorama mode for 180° views of plots.

**Honesty rules:** no heavy filters, no fake sky replacement, no hiding defects, no wide-angle tricks that make rooms look twice their size, no photos of a different property. Every photo must be of the property and recent.
""",
    example="""
For the 15-cent Thottilpalam house (mandate signed), Sachin shoots at 8 am: 4 road and exterior photos, 2 of each room, the well and the back slope (which the listing will mention), and a 95-second walkthrough with captions: "15 cents · 1,350 sq ft · 3 bedrooms · 6 m panchayat road · 2.5 km to Thottilpalam town · part of the back plot slopes". He blurs the neighbour's vehicle number plate. The owner approves the photos on WhatsApp before anything is posted; Sachin saves the approval message.
""",
    resources=[
        ('gearth', 'Draw the boundary of a plot and save a view', '15 minutes'),
        ('canva', 'Optional: make a simple photo collage cover for the listing', '10 minutes'),
    ],
    steps=[
        'With an owner\'s written permission (your mandate property, or your own family\'s house), shoot the full shot list.',
        'Record a 60 to 120 second walkthrough and add captions with honest key facts.',
        'Make a simple virtual tour: an ordered album, the video and a Google Earth view.',
        'Get the owner\'s approval of the photos and video in writing (a WhatsApp message is fine; save it).',
    ],
    proof='The photo set, video, tour link (private) and the owner\'s approval.',
    templates=[('Photo and video checklist', """PHOTO AND VIDEO CHECKLIST     Property ______  Date ______
BEFORE: written permission [ ] tidy [ ] lights on, curtains open [ ] personal items removed [ ]
PHOTOS (landscape for portals, vertical for Status/Reels)
Road both ways [ ] front [ ] boundaries [ ] each room [ ] kitchen [ ] bathrooms [ ] well/tank [ ] view [ ] honest defects [ ]
VIDEO 60-120 s: road -> gate -> one continuous walk -> pause in each room -> location end card [ ]
Captions: cents | sq ft | rooms | road width | distance to town | honest notes [ ]
VIRTUAL TOUR: ordered album [ ] video [ ] Google Earth boundary view [ ]
PRIVACY: no people, number plates, documents, exact address [ ]
OWNER APPROVAL saved on ______""")],
    mistakes=[
        ('Shooting in dark or harsh light.', 'Shoot in soft daylight with lights on.'),
        ('Tilted, distorted photos.', 'Use gridlines; keep the phone level; limit ultra-wide.'),
        ('Posting without the owner\'s approval.', 'Get written approval first.'),
    ],
    fraud="""
**Old or borrowed photos.** Some listings use photos from years ago, from a different house or from the internet. Buyers who visit feel cheated, and it can be misrepresentation. Use only recent photos of the actual property.
""",
    quiz=[
        Q('When is the best light for property photos?', 'Soft morning or late afternoon daylight', 'Harsh noon sun', 'Night without lights', 'Heavy rain', why='Soft light shows rooms well.'),
        Q('What should a walkthrough video start with?', 'The road and gate', 'The bathroom', 'The owner\'s face', 'A random room', why='Road access matters to buyers.'),
        Q('What must you get before publishing photos?', 'The owner\'s written approval', 'Nothing', 'The neighbour\'s approval', 'A police NOC', why='Act only with consent.'),
        Q('Which is misrepresentation?', 'Using photos of a different, nicer house', 'Showing a crack you mention', 'Using natural light', 'Using gridlines', why='Every photo must be of the property.'),
    ],
    study='read the lesson and the shot list',
    action='shoot photos, a walkthrough video and a simple virtual tour for one property, with the owner\'s approval',
)

L2 = lesson(
    12, 2,
    outcome='You can write honest, specific listing copy in English and Malayalam and post a listing on free portals with the owner\'s written permission.',
    split='15 minutes reading, 45 minutes writing and posting',
    core=f"""
**Honest listing copy.** Facts first, no hype, no hidden problems. Buyers trust brokers whose listings match reality, and misrepresentation can create legal liability. The toolkit's listing template is below.

**Writing tips:**
- Title: size, type, sale or rent, locality and a landmark distance.
- Put **price per cent** for land: buyers compare that way.
- Key facts in a short list; the description in 3 to 5 short lines.
- Include **honest notes** (slope, narrow last stretch of road, needs painting). It builds trust and avoids wasted visits.
- Avoid vague hype ("prime", "best investment", "sure appreciation"), and never promise returns, permits or conversion.
- Malayalam version for local groups; English for portals and NRIs. Check the Malayalam with someone fluent if you're unsure.
- No owner's phone number or exact address in public; give the village and landmark, and share the location pin after qualifying the lead.

**Free portals:**
- **NoBroker:** owner listings are free ({link('nobroker', 'NoBroker')}); as an agent, follow the platform's rules for brokers.
- **MagicBricks, 99acres, Housing.com:** free basic listings are usually available, with paid upgrades; check each portal's current rules for agents and owners ({link('magicbricks', 'MagicBricks')}, {link('99acres', '99acres')}, {link('housing', 'Housing.com')}).
- **OLX and Facebook Marketplace:** widely used for local rentals and plots.
Always show your K-RERA number where required (project listings) and post only with a signed mandate. Remove listings promptly when sold, let or withdrawn.

For persuasive writing without hype, see the {xref('smm', 'smm-m05-l02', 'Social Media Marketing lesson on calls to action and persuasion without hype')}.
""",
    example="""
**English (portal):**
"15 cents with a 3-bedroom house for sale, 2.5 km from Thottilpalam town. ₹38 lakh (negotiable) · about ₹2.53 lakh per cent including the house. Land 15 cents · house 1,350 sq ft (as per permit) · 6 m panchayat road · own well and KWA connection · single-phase electricity. Built 2012, well maintained; kitchen updated 2022. Honest notes: the back 3 cents slope down; the house needs exterior painting. Documents: deed, 30-year EC, tax receipts, permit and building number available for verification. Contact Sachin (agent)."

**Malayalam (local WhatsApp):**
"തൊട്ടിൽപ്പാലം ടൗണിൽ നിന്ന് 2.5 കി.മീ., 15 സെന്റ് സ്ഥലവും 3 ബെഡ്‌റൂം വീടും വിൽപ്പനയ്ക്ക്. വില ₹38 ലക്ഷം (ചർച്ച ചെയ്യാം). 6 മീറ്റർ പഞ്ചായത്ത് റോഡ്, കിണർ, KWA വെള്ളം. പിൻഭാഗത്തെ 3 സെന്റ് ചരിവാണ്. രേഖകൾ പരിശോധനയ്ക്ക് ലഭ്യം."
""",
    resources=[
        ('nobroker', 'Read the listing steps for owners and the rules for brokers', '10 minutes'),
        ('magicbricks', 'Check current free listing options', '10 minutes'),
        ('99acres', 'Check current free listing options', '10 minutes'),
        ('housing', 'Check current free listing options', '10 minutes'),
    ],
    steps=[
        'Write the English and Malayalam listing for your mandated property using the template, including honest notes.',
        'Get the owner\'s written approval of the text.',
        'Post on at least two free portals (or help the owner post on NoBroker in their own name) and on OLX or Facebook Marketplace.',
        'Record each listing link, date and any enquiries in your Inventory and CRM.',
    ],
    proof='The approved text, the owner\'s approval, links and screenshots of the live listings, and the CRM entries.',
    templates=[('Listing template', tools.LISTING)],
    mistakes=[
        ('Hype words and promises.', 'State facts; never promise returns or permits.'),
        ('Leaving out problems.', 'Honest notes build trust and save time.'),
        ('Forgetting to remove sold listings.', 'Update status promptly.'),
    ],
    fraud="""
**Bait listings.** Posting a cheap fake property to collect enquiries and then pushing other properties is common and dishonest. Every listing you post must be real, mandated, available and correctly priced.
""",
    quiz=[
        Q('What should a land listing always include for comparison?', 'Price per cent', 'The owner\'s phone number', 'A promise of appreciation', 'The owner\'s Aadhaar', why='Buyers compare that way.'),
        Q('Why include honest notes about problems?', 'To build trust and avoid wasted visits', 'To lower the price', 'It is required by portals', 'It is not useful', why='Surprises at visits kill deals.'),
        Q('Which phrase should you avoid?', '"Sure appreciation, best investment"', '"6 m panchayat road"', '"2.5 km to town"', '"Documents available for verification"', why='Never promise returns.'),
        Q('Before posting, what do you need?', 'A signed mandate and the owner\'s approval of the text and photos', 'Nothing', 'A building permit for the broker', 'A GST number', why='Consent first.'),
    ],
    study='read the lesson and the listing template',
    action='write an honest bilingual listing and post it on free portals with the owner\'s permission',
)

L3 = lesson(
    12, 3,
    outcome='You can market properties and your service through social media, WhatsApp and a Google Business Profile, honestly and within platform rules.',
    split='15 minutes reading, 45 minutes setting up and posting',
    core=f"""
**Your brand:** a simple, consistent name ("Sachin · Property Services, Kuttiady"), a clear photo, one line on what you do and your values (honest dealing, proper papers, no cash deals), and your K-RERA number once registered.

**WhatsApp Business** (free): set up a business profile with hours, area and catalogue; use labels for lead stages; use a **Status** for new listings; and consider a **WhatsApp Channel** for interested people to follow. Never add people to groups or broadcast lists without consent. See the {xref('smm', 'smm-m03-l03', 'Social Media Marketing lesson on Facebook and WhatsApp Business')}.

**Instagram, Facebook and YouTube:**
- Short walkthrough videos (Reels, Shorts) with honest captions.
- Useful content: "How to check an EC in Kerala", "What is fair value?", "5 questions to ask before buying land". This builds trust, especially with NRIs.
- Local Facebook groups: follow rules; post rarely and helpfully.
- Disclose that you are an agent; don't pose as an owner.

**Google Business Profile (GBP).** Free; it puts you on Google Maps and local search. A home-based agent should set up as a **service-area business**: hide the home address and list the areas you serve (up to 20 service areas), per {link('gbp', 'Google\'s guidelines')}. Add your real business name (no keyword stuffing), category (real estate agency or agent), hours, phone, photos of your work and a short description. Ask genuine clients for reviews; never write fake ones or offer rewards for positive reviews. See the {xref('smm', 'smm-m11-l01', 'Social Media Marketing lesson on Google Business Profile')} and the {xref('ent', 'ent-m06-l03', 'Entrepreneurship lesson on local SEO')}.

**A simple weekly plan (1 to 2 hours):** 2 listing posts (only mandated properties), 1 educational post, replies to every enquiry within a day, and a review request after every completed deal.
""",
    example="""
Sachin sets up:
- WhatsApp Business: "Sachin · Property Services · Kuttiady" with hours, area and a catalogue of 3 mandated properties.
- A Facebook page and an Instagram account with the same name; first posts: the Thottilpalam walkthrough and a short video "What is an EC and why you must check 30 years".
- GBP: service-area business, address hidden, service areas Kuttiady, Kayakkody, Velom, Kunnummal, Thottilpalam, Nadapuram, Vadakara and others (under 20). He asks his first rental client for an honest review.
After a month, the EC video has brought two NRI enquiries; the listing posts brought five local enquiries.
""",
    resources=[
        ('gbp', 'Read the service-area business guidelines', '10 minutes'),
        ('canva', 'Make a simple profile cover and listing template', '15 minutes'),
    ],
    steps=[
        'Set up WhatsApp Business with your profile and a catalogue of your mandated properties.',
        'Create or tidy one social account and post one walkthrough and one educational video.',
        'Set up a Google Business Profile as a service-area business (address hidden) and complete every field honestly.',
        'Write your weekly marketing plan and follow it for two weeks.',
    ],
    proof='Screenshots of your WhatsApp Business profile, two posts and your GBP, and your two-week plan with what you did.',
    templates=[('Weekly marketing plan', """WEEKLY MARKETING PLAN (1-2 hours)     Week ______
Mon: 1 listing post (mandated, owner-approved)   [ ]
Wed: 1 educational post (EC, fair value, nilam, cash rules, rental tips) [ ]
Fri: 1 listing post or a "just let/sold" update with owner consent [ ]
Daily: reply to every enquiry within 24 h; log in CRM [ ]
After each deal: ask for an honest review (no rewards) [ ]
Monthly: update GBP photos and hours; remove stale listings [ ]
Rules: no spam, no adding people without consent, disclose that I'm an agent, show K-RERA no. when registered""")],
    mistakes=[
        ('Showing your home address on GBP.', 'Use a service-area business and hide it.'),
        ('Buying or faking reviews.', 'Only genuine reviews; no rewards.'),
        ('Spamming groups and contacts.', 'Consent and useful content.'),
    ],
    fraud="""
**Fake profiles and impersonation.** Scammers copy real agents' names and photos to collect advances. Make your official accounts easy to verify (same name, number and GBP), and warn clients to pay only by bank transfer after agreements.
""",
    quiz=[
        Q('How should a home-based agent set up a Google Business Profile?', 'As a service-area business with the home address hidden', 'With the home address shown', 'With keywords in the name', 'With fake reviews', why='Google\'s guidelines.'),
        Q('Which content builds trust with NRI buyers?', 'Honest walkthroughs and educational videos', 'Hype and promises', 'Stock photos', 'Fake reviews', why='Trust is the product.'),
        Q('What is allowed for reviews?', 'Asking genuine clients for honest reviews', 'Paying for 5-star reviews', 'Writing your own', 'Offering discounts for positive reviews', why='Fake reviews break rules.'),
        Q('Before adding someone to a WhatsApp broadcast list, you should:', 'Get their consent', 'Do nothing', 'Add everyone in your contacts', 'Buy a number list', why='Respect privacy.'),
    ],
    study='read the lesson and the weekly plan',
    action='set up WhatsApp Business, social posts and a Google Business Profile and follow the plan for two weeks',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    12,
    overview=f"""
Marketing properties: phone photography, walkthrough video and simple virtual tours; honest bilingual listing copy; free portals; and social media, WhatsApp Business and a Google Business Profile.

The practical milestone is a **real listing, with the owner's written permission**, live on free portals and social media. The Social Media Marketing course goes deeper on content and platforms; this module applies it to property. Everything is {RULE}.
""",
    outcomes=[
        'Shoot honest photos, video and a simple virtual tour.',
        'Write honest listing copy in English and Malayalam.',
        'Post on free portals with consent.',
        'Market through WhatsApp, social media and Google Business Profile.',
    ],
    lessons=LESSONS,
    project='one real, owner-approved listing live everywhere',
    project_steps=[
        'Signed mandate and owner approval of photos, video and text.',
        'Listing live on at least two portals and one social or WhatsApp channel.',
        'GBP set up as a service-area business.',
        'Track every enquiry in the CRM for two weeks and write what worked.',
    ],
    project_proof='Approval, links, screenshots and the CRM summary.',
    rubric=[
        ('Visuals', 'Dark or misleading', 'Clear but incomplete', 'Full shot list, video and tour, honest'),
        ('Copy', 'Hype, no facts', 'Facts but missing honest notes', 'Specific, honest, bilingual'),
        ('Channels', 'One channel', 'Two channels', 'Portals, social, WhatsApp and GBP'),
        ('Consent and ethics', 'No written approval', 'Partial', 'Mandate and approvals saved; no spam'),
    ],
    short=[
        'Shoot one property with the shot list.',
        'Post one honest listing with the owner\'s approval.',
    ],
    flashcards=[
        ('Best light', 'Soft morning or late afternoon.'),
        ('Walkthrough length', '60 to 120 seconds.'),
        ('Must-have land listing figure', 'Price per cent.'),
        ('Honest notes', 'Say the problems up front.'),
        ('GBP for home-based agents', 'Service-area business, address hidden.'),
        ('Service areas on GBP', 'Up to 20.'),
        ('Reviews', 'Genuine only; no rewards.'),
    ],
    mistakes=[
        ('Posting unmandated properties.', 'Mandate first.'),
        ('Overediting photos.', 'Keep them true to life.'),
        ('Ignoring enquiries.', 'Reply within a day.'),
    ],
    tools=[
        'Photo and video checklist (RE-M12-L01).',
        'Listing template (RE-M12-L02).',
        'Weekly marketing plan (RE-M12-L03).',
    ],
    toolkit=[
        'Photo and video checklist.',
        'Listing template (English and Malayalam).',
        'Weekly marketing plan.',
    ],
)
