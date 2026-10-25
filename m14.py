from common import lesson, module, link, ASOF

L1 = lesson(
    14, 1,
    title='Disclosure: ASCI influencer guidelines and Indian endorsement rules',
    weeks=(34, 34), hours=2,
    outcome='Know exactly when a post must be labelled as paid or connected to a brand in India, which labels to use and where to place them in captions, Stories, videos, lives and audio, and what endorsers must check before promoting anything.',
    split='45 minutes study, 1 hour 15 minutes action',
    core=f"""
### Two sets of rules apply ({ASOF})

1. **ASCI's Guidelines for Influencer Advertising in Digital Media.** The Advertising Standards Council of India is the industry's self-regulatory body. Its guidelines cover influencers, brands and agencies, and it can ask for misleading or undisclosed ads to be changed or withdrawn.
2. **The law:** the Consumer Protection Act, 2019, with the CCPA's Guidelines for Prevention of Misleading Advertisements and Endorsements (June 2022) and the Department of Consumer Affairs' "Endorsement Know-hows!" guide for celebrities, influencers and virtual influencers (January 2023).

As a marketer you are responsible too: build disclosure into every brief, caption check and client agreement.

### When must a post be labelled?

Whenever there is a **material connection** between the advertiser and the person posting: anything that could affect how much weight the audience gives the recommendation. ASCI lists payment, free products (even unsolicited ones), discounts, gifts, contest entries, trips, media barters, awards, and family or employment relationships. ASCI is explicit: **"Disclosures are required even if the evaluations are unbiased."**

No label is needed when someone shares a product they bought themselves with no connection to the brand, or for genuinely editorial content.

### Which labels?

ASCI's guidelines list: **Advertisement, Ad, Sponsored, Collaboration, Partnership, Employee, Free gift** and **Affiliate**, plus the platforms' own tools such as Instagram's **Paid partnership** label and YouTube's **Includes paid promotion**. Use one or more. The government guide adds plain terms such as "advertisement", "sponsored" and "paid promotion". Use the platform tool **as well as** your own label, not instead of it.

### Where and how to place it

| Format | ASCI's rule |
| --- | --- |
| **Captions** | Upfront and prominent, hard to miss; not buried in hashtags or links, not only in the bio, not at the end or behind "more" |
| **Stories and images without text** | The label superimposed on the picture, clearly visible |
| **Videos of 15 seconds or less** | Label on screen for at least 3 seconds |
| **Videos from 15 seconds to 2 minutes** | Label on screen for at least a third of the video |
| **Videos of 2 minutes or more** | Label on screen for the whole section where the brand is mentioned |
| **Live streams** | Announced at the start and the end (and in the caption if the video stays up) |
| **Audio** | Announced at the start and end, and before and after each break |
| **Language** | English or the language of the post, easy for an average viewer to understand |

### Before you endorse anything

- The law expects an endorsement to reflect the endorser's **genuine, reasonably current opinion**, based on **adequate information or real experience** with the product. The government guide says endorsers shouldn't promote what they haven't personally used or properly vetted.
- ASCI advises influencers to check that the advertiser can back up its claims.
- **Health and finance:** ASCI's 2023 addendum requires influencers giving technical advice on health, nutrition, banking, investment or insurance to hold relevant qualifications (for example SEBI registration for investment advice) and to show them prominently.
- **Virtual influencers** must also disclose that people are not interacting with a real human.

### What happens if rules are broken

ASCI can ask for posts to be changed or removed. Under the Consumer Protection Act the CCPA can fine a manufacturer or endorser up to **₹10 lakh** for a false or misleading advertisement, and up to **₹50 lakh** for repeat offences (check current rules). Beyond penalties, hidden ads destroy the trust that makes influencer marketing work.
""",
    example="""
A Vatakara food creator posted a Reel about a new restaurant after a free meal for four. The caption began "Best biryani in Malabar!! 😍 #foodie #vatakara #ad" with "#ad" buried at the end of 15 hashtags, and nothing on screen. The restaurant had asked Anu (as their marketer) to arrange it.

Anu's fixes, agreed with both:

- Caption now starts: "Collaboration (free meal from @restaurant). Honest review below."
- "Free meal | Collaboration" on screen for the first 10 seconds of the 30-second Reel (more than a third).
- Instagram's Paid partnership label switched on, with the restaurant as the partner.
- "Best biryani in Malabar" changed to what the creator actually thought: "The mutton biryani was the highlight; the chicken was average."

She added a disclosure section to her influencer brief so it never happens again.

(Made-up example to show the method.)
""",
    resources=[
        ('asci-guidelines', 'Read the full guidelines and both addenda (health and finance; disputing a connection)', '25 min'),
        ('asci-faqs', 'Re-read the FAQs on labels and placement', '10 min'),
        ('pib-endorse', 'Read the government\'s summary of "Endorsement Know-hows!"', '5 min'),
        ('pib-misleading', 'Re-read the endorser standards and the penalties', '5 min'),
    ],
    steps=[
        'Study the resources (about 45 minutes).',
        'Find 10 sponsored or gifted posts from Kerala creators or businesses. For each, check: is there a material connection, a correct label, correct placement for the format, and the platform tool?',
        'Rewrite 3 of them so they follow the rules, keeping the creator\'s voice.',
        'Write your disclosure checklist and the label placement card for your sales kit, and add a disclosure clause to your influencer brief template.',
    ],
    proof='Your check of 10 posts, your 3 rewrites and your disclosure checklist with the placement card.',
    templates=[
        ('disclosure checklist', """
Is there a material connection? (payment, free product
even if unsolicited, discount, gift, trip, barter, contest
entry, award, family or employment tie) -> YES = label it
[ ] Label: Ad / Advertisement / Sponsored / Collaboration /
    Partnership / Employee / Free gift / Affiliate
[ ] Placed upfront: start of the caption, not in hashtags,
    bio, end of caption or behind "more"
[ ] Platform tool on (Paid partnership / Includes paid
    promotion) AS WELL AS the label
[ ] In the post's language, easy to understand
[ ] Claims are the endorser's genuine, current experience
[ ] Advertiser can back up every claim
[ ] Health or finance advice? Endorser has and shows the
    required qualification
[ ] Virtual influencer? Says it isn't a real human
""", ''),
        ('label placement card', """
CAPTION:   label at the start, before "more"
STORY/IMAGE (no text): label superimposed, clearly visible
VIDEO <=15 s:      on screen at least 3 s
VIDEO 15 s-2 min:  on screen at least 1/3 of the length
VIDEO >=2 min:     on screen through the whole brand section
LIVE:      say it at the start and end (+ caption if kept)
AUDIO:     say it at the start, end, and around each break
""", ''),
    ],
    mistakes=[
        ('#ad hidden among hashtags.', 'Labels must be upfront and hard to miss.'),
        ('"It was free but I was honest, so no label".', 'ASCI: disclosure is required even if the review is unbiased.'),
        ('Relying only on the platform tool.', 'Use it as well as your own clear label.'),
        ('Endorsing products you haven\'t used.', 'Endorsements must reflect genuine experience.'),
        ('Health or investment tips from unqualified creators.', 'ASCI requires relevant qualifications for technical advice.'),
    ],
    quiz=[
        {'q': 'A creator received a free phone without being asked to post, then posts a review. Does it need a label?',
         'o': ['No, it was unsolicited', 'Yes: a free product, even unsolicited, is a material connection', 'Only if they liked it', 'Only on YouTube'],
         'a': 'B', 'why': 'ASCI includes unsolicited free products.'},
        {'q': 'For a 90-second sponsored Reel, how long must the label stay on screen under ASCI\'s guidelines?',
         'o': ['1 second', 'At least a third of the video (30 seconds)', 'Only in the caption', 'The last frame only'],
         'a': 'B', 'why': 'Videos from 15 seconds to 2 minutes need the label for at least a third of their length.'},
        {'q': 'Where should a caption label go?',
         'o': ['At the end, after 20 hashtags', 'Upfront, at the start, where it\'s hard to miss', 'Only in the bio', 'In a comment'],
         'a': 'B', 'why': 'Labels must not be buried or hidden behind "more".'},
        {'q': 'What must an endorsement reflect under the 2022 guidelines?',
         'o': ['The brand\'s script', 'The endorser\'s genuine, reasonably current opinion based on adequate information or experience', 'Whatever gets views', 'Nothing in particular'],
         'a': 'B', 'why': 'That is the standard the CCPA guidelines set.'},
    ],
    study='ASCI\'s influencer guidelines and FAQs, the government endorsement guide and the misleading-ads rules (about 45 minutes)',
    action='check 10 sponsored posts against the rules, rewrite 3 and write your disclosure checklist',
)

L2 = lesson(
    14, 2,
    title='Copyright, music licensing and consent for photos of people',
    weeks=(35, 35), hours=2.5,
    outcome='Use only content you have the right to use, handle copyright claims correctly, get and keep consent before filming people (especially children), and handle customers\' personal data the way Indian law expects.',
    split='45 minutes study, 1 hour 45 minutes action',
    core=f"""
### Copyright in plain words

In India, the Copyright Act, 1957 protects original creative work: photos, videos, music, recordings, writing, designs. The creator (or the person they work for, in some cases) owns it, and using it without permission is infringement. Section 52 of the Act lists the acts that are **not** infringement, such as limited fair dealing for criticism, review or reporting current events, but these exceptions are narrow and don't cover using a popular film song as background music in a shop's Reel.

Three myths to drop:

- **"I gave credit."** Credit is not permission. YouTube's own help page says giving credit isn't a valid reason to dispute a copyright claim.
- **"It was on Google, so it's free."** Almost everything online belongs to someone.
- **"It's only 10 seconds."** There is no safe length.

### How platforms enforce it ({ASOF})

- **YouTube** uses **Content ID**: a claim can block your video, send its earnings to the owner or track it. A **copyright strike** is more serious: it follows a valid removal request and counts against your channel. Shorts over a minute with an active claim are blocked worldwide. Dispute a claim only if you have all the rights, the use is a genuine exception, or the claim is a mistake; abusing disputes can bring penalties, and a valid removal request leads to the video being removed and a strike.
- **Instagram and Facebook** can mute audio, block or remove content that uses music without a licence. Music added from the app's own library is licensed for use in the app, but business accounts may have a more limited library.

### Safe sources

- Your own photos, videos and voice
- Music and sounds added inside Instagram, Facebook or YouTube from their libraries
- The **YouTube Audio Library**: tracks with a Creative Commons licence need the artist credited in the description; you can filter for "Attribution not required"
- Canva's free media, used within its licence (not in logos or trademarks)
- Work by local musicians, photographers or artists with **written permission**

For clients, also get written permission for their logo, photos and any content they send you, and agree who owns the content you make for them (Module 15).

### Consent before you film or post people

- **Ask first** and save the yes: a consent note, a WhatsApp message or a short recorded "yes" (SMM-M04-L03 has a form).
- **Children:** ask a parent or guardian, and think twice even then. Avoid names, schools and locations of children.
- **Staff and customers in a client's shop:** the business should ask them, and you should check.
- **Sensitive places and moments:** hospitals, funerals, places of worship, accidents: don't film without clear permission, and often not at all.
- **Let people change their minds:** remove a post promptly if someone asks.

### Customers' personal data

Phone numbers, addresses, chats and photos of customers are personal data. India's Digital Personal Data Protection Rules, 2025 (with obligations phased in over 18 months) expect consent that is clear and informed, a notice saying what the data is for, the right to withdraw consent at any time, and verifiable consent from a parent or guardian for children's data. Penalties for businesses can be very large, up to ₹250 crore for security failures (check current rules). In practice for you:

- Never post screenshots of chats or reviews without hiding names and numbers, unless the customer agreed.
- Use customer lists only for the purpose people agreed to (for example, order updates), and let them stop.
- Don't paste customer data into AI tools or share it with anyone else.
""",
    example="""
Anu's early Short used 40 seconds of a popular Malayalam film song she had downloaded. It got a Content ID claim and the ad money went to the music label. A follower also messaged: "Please remove my daughter from your Onam video."

What she did:

1. Removed the film song in YouTube Studio's editor and replaced it with a track from the YouTube Audio Library ("Attribution not required"). The claim was released.
2. Deleted the Onam video the same day, apologised, and re-posted a version without the child.
3. Audited her last 20 posts: two more had downloaded songs (fixed), one had a customer's phone number visible in a screenshot (blurred).
4. Started using a consent note for every person she films, and a rule: no children unless it's her own family, with a parent's OK.

(Made-up example to show the method.)
""",
    resources=[
        ('copyright-act', 'Open the Act and read the arrangement of sections, including the title of section 52', '10 min'),
        ('yt-dispute', 'Read claims vs strikes and when you may dispute', '10 min'),
        ('yt-audio', 'Re-read how to use and credit Audio Library tracks', '5 min'),
        ('ig-music', 'Open Instagram\'s page on the licensed music library', '3 min'),
        ('canva-license', 'Re-read the limits of the free licence', '3 min'),
        ('dpdp', 'Read the summary of consent, withdrawal, children\'s data and penalties', '15 min'),
    ],
    steps=[
        'Study the resources (about 45 minutes).',
        'Audit your last 20 posts (and your pilot client\'s posts) with the rights and consent sheet: music source, images, people shown, consent saved, personal data visible.',
        'Fix every problem you find: replace music, remove or blur, ask for missing consent or take the post down.',
        'Make your consent form (English and Malayalam) and a list of your safe music and image sources.',
        'Write two sentences for clients explaining why you won\'t use film songs or Google images in their posts.',
    ],
    proof='Your completed audit sheet with the fixes made, your consent form and your safe sources list.',
    templates=[
        ('rights and consent audit sheet', """
Post link,Date,Music source (own/app library/Audio Library/other),Images (own/Canva free/other),People shown,Consent saved (Y/N/NA),Children shown (Y/N) with parent OK,Personal data visible (Y/N),Problem,Fix done
""", 'csv'),
        ('photo and video consent form (English and Malayalam)', """
CONSENT TO BE FILMED OR PHOTOGRAPHED
I, ______________, agree that ______________ (page or
business) may film or photograph me and post it on
Instagram, YouTube, Facebook and WhatsApp.
[ ] Face shown  [ ] Voice only  [ ] Hands only
I can ask for it to be removed at any time by messaging ____.
For a child: parent or guardian ______________ agrees.
Signature or recorded yes: ________  Date: ________

ചിത്രീകരണത്തിനുള്ള സമ്മതം
______________ (പേജ്/ബിസിനസ്) എന്നെ ചിത്രീകരിച്ച്
ഇൻസ്റ്റഗ്രാം, യൂട്യൂബ്, ഫേസ്ബുക്ക്, വാട്സാപ്പ് എന്നിവയിൽ പോസ്റ്റ്
ചെയ്യുന്നതിന് ഞാൻ ______________ സമ്മതിക്കുന്നു.
എപ്പോൾ വേണമെങ്കിലും ____ ൽ മെസ്സേജ് ചെയ്ത് നീക്കം ചെയ്യാൻ ആവശ്യപ്പെടാം.
കുട്ടിയാണെങ്കിൽ രക്ഷിതാവിന്റെ സമ്മതം: ______________
""", ''),
        ('safe sources list', """
MUSIC: in-app libraries (Instagram, Facebook, YouTube);
  YouTube Audio Library ("Attribution not required" or
  credit added); local musician ____ (written permission)
IMAGES: my own; client's own (written permission); Canva
  free media (not in logos)
NEVER: film songs, songs downloaded from YouTube, Google
  Images, other creators' videos, "no copyright" uploads
  from unknown channels
""", ''),
    ],
    mistakes=[
        ('"Credit to the owner" as a licence.', 'Credit isn\'t permission.'),
        ('Disputing claims you know are valid.', 'Abuse of disputes can bring penalties and strikes.'),
        ('Filming children at events.', 'Ask a parent, avoid identifying details, or leave them out.'),
        ('Posting chat screenshots with numbers.', 'Hide names and numbers, or get permission.'),
        ('Keeping posts someone asked you to remove.', 'Remove them promptly and apologise.'),
    ],
    quiz=[
        {'q': 'You used a film song and credited the composer. Is that a valid reason to dispute a Content ID claim?',
         'o': ['Yes', 'No: YouTube says giving credit isn\'t a valid reason', 'Only for Shorts', 'Only in Malayalam'],
         'a': 'B', 'why': 'Credit is not permission.'},
        {'q': 'What is the difference between a Content ID claim and a copyright strike?',
         'o': ['None', 'A claim attaches to a video; a strike follows a valid removal request and counts against the channel', 'Strikes are good', 'Claims delete your channel'],
         'a': 'B', 'why': 'Strikes are penalties on the channel; claims are about the video.'},
        {'q': 'A parent asks you to remove a video showing their child. What do you do?',
         'o': ['Ignore it', 'Remove it promptly and apologise', 'Ask them to pay', 'Blur it next month'],
         'a': 'B', 'why': 'Consent can be withdrawn, and children need extra care.'},
        {'q': 'What do the DPDP Rules, 2025 expect for consent?',
         'o': ['Nothing', 'Clear, informed consent with a notice of purpose, and the right to withdraw', 'Consent only for adults over 60', 'Consent only on paper'],
         'a': 'B', 'why': 'That is the summary in the government explainer.'},
    ],
    study='The Copyright Act, YouTube\'s claims and Audio Library rules, Instagram\'s music page, Canva\'s licence and the DPDP Rules summary (about 45 minutes)',
    action='audit 20 posts for rights, consent and personal data, fix every problem and make your consent form',
)

L3 = lesson(
    14, 3,
    title='Honest growth: platform rules, fake engagement, fake reviews and dark patterns',
    weeks=(35, 35), hours=2,
    outcome='Know the main platform rules that protect your accounts, explain to clients why fake followers, fake reviews, engagement bait and dark patterns are harmful and often against the law, and offer honest alternatives.',
    split='35 minutes study, 1 hour 25 minutes action',
    core=f"""
### The rules that keep accounts alive ({ASOF})

| Platform rule | What it covers | Where |
| --- | --- | --- |
| Community Guidelines and Standards | What can't be posted at all | Meta's Community Standards; YouTube's Community Guidelines |
| Recommendation Guidelines | What can stay up but won't be recommended to non-followers | Instagram's Account Status |
| Inauthentic behaviour and spam | Fake accounts, coordinated fakery, misleading pages | Meta's Community Standards |
| Fake engagement | Buying or faking views, likes, subscribers, comments; sub4sub; incentivised engagement | YouTube's fake engagement policy |
| Fake and incentivised reviews | Reviews that aren't genuine experiences; reviews in exchange for benefits | Google Maps content policies |
| Monetisation policies | Inauthentic, mass-produced and reused content doesn't earn | YouTube Partner Program policies |
| Engagement bait | Posts that ask for likes, comments, shares, tags or votes just for reach | Meta's content distribution guidelines |

### Fake followers and fake engagement

Buying followers, likes or views is cheap and tempting. It is also a bad deal:

- **It breaks the rules.** YouTube removes content and can terminate channels for fake engagement; artificial traffic isn't counted. Instagram removes inauthentic likes, follows and comments made through third-party growth apps and warns the accounts using them.
- **It ruins your numbers.** Fake followers never watch, so your views per follower and engagement fall, and recommendations get harder.
- **It deceives clients.** Selling a business "10,000 followers" that will never buy anything is dishonest, and showing inflated numbers to win clients can be a misleading claim.

### Fake reviews

Reviews written by owners, staff, family or paid strangers, or swapped between businesses, break Google's policies and can be removed, with the profile restricted. India's online review standard IS 19000:2022 expects paid reviews to be disclosed and bars reviews bought or written by people employed for that purpose. Fake testimonials in ads can also be misleading advertising under the Consumer Protection Act.

### Engagement bait and fake contests

"Like if you love Kerala", "Comment YES for part 2", "Tag 5 friends to win" ask for empty actions. Meta demotes engagement bait. If a client wants a giveaway, keep it honest: clear written terms, a real prize, a fair way to choose winners, no payment to enter, and no "tag 10 friends" requirement. Check the platform's promotion rules before you run one.

### Dark patterns

In November 2023 India's Central Consumer Protection Authority issued guidelines banning **13 dark patterns**: design and wording tricks that push people into choices they didn't intend. They include **false urgency** (fake countdowns and "only 2 left"), **bait and switch** (advertising one thing and delivering another), **drip pricing** (hiding part of the price until the end) and **disguised advertisements** (ads made to look like normal content). Social media marketers meet these every day; avoid them all (check current rules).

### Your answer to a client who asks for shortcuts

Say no to the shortcut and offer the honest alternative: "Buying followers would hurt your reach and could get the account restricted. Instead, let's run a collab with a local food page and a small, targeted ad to real people within 5 km." Clients respect a marketer who protects their business.
""",
    example="""
Before Onam, the owner of a new textile shop in Kuttiady asked Anu three things (made-up example):

1. "Can you get us 5,000 followers this week? My cousin knows a site."
2. "Write ten 5-star Google reviews from different names."
3. "Put 'Only 3 sarees left!' on every post so people hurry."

Her replies:

1. "Bought followers don't come to the shop, and Instagram removes fake follows from such apps. Let's do a Collab Reel with two local pages and a ₹1,000 ad to women within 8 km."
2. "Fake reviews break Google's rules and can get the profile restricted. Let's put a QR review card at the billing counter and ask every customer this week."
3. "If it isn't true, it's false urgency, which India banned in 2023. We can say 'Onam collection: new stock every Friday', which is true."

The owner agreed to all three alternatives. By Onam the shop had 36 genuine new reviews.
""",
    resources=[
        ('yt-fake', 'Re-read the fake engagement policy and its penalties', '5 min'),
        ('ig-fakeapps', 'Open Instagram\'s page on apps that offer likes and followers', '3 min'),
        ('meta-inauthentic', 'Open Meta\'s inauthentic behaviour standard', '5 min'),
        ('maps-fake', 'Re-read Google\'s fake engagement policy', '3 min'),
        ('pib-dark', 'Re-read the dark patterns press release', '5 min'),
        ('meta-ebait', 'Re-open the engagement bait page', '3 min'),
        ('yt-monetisation', 'Re-read the inauthentic and reused content rules', '5 min'),
    ],
    steps=[
        'Study the resources (about 30 minutes).',
        'Check your own accounts: Instagram Account Status and YouTube Studio for any warnings or limits. Screenshot them.',
        'Write your personal ethics code: at least 8 things you will always do and never do as a marketer.',
        'Write "no, but" replies to five unethical requests a client might make (followers, reviews, fake urgency, hidden ads, copied content).',
        'Find one example of a dark pattern or engagement bait in a real post or ad, and write how you\'d fix it.',
    ],
    proof='Your account status screenshots, your ethics code, your five "no, but" replies and your dark pattern fix.',
    templates=[
        ('my ethics code', """
I ALWAYS
1. use real numbers, and say when results are unclear
2. disclose paid, gifted and affiliate content clearly
3. get consent before filming people, and parents' OK
4. use music and images I have the right to use
5. tell clients when an idea breaks rules or law
I NEVER
6. buy followers, likes, views or reviews
7. write or arrange fake reviews or testimonials
8. use false urgency, hidden prices or disguised ads
9. copy other creators' content
10. ask for or keep clients' passwords
""", ''),
        ('"no, but" replies', """
FOLLOWERS: "Bought followers won't buy from you and can
  get the account restricted. Instead: ________."
REVIEWS: "Fake reviews break Google's rules. Instead:
  a QR review card and asking every customer."
URGENCY: "If it isn't true it's false urgency, banned in
  2023. Instead: a real deadline such as ________."
HIDDEN ADS: "The law and ASCI need a clear label. It
  won't hurt: honest labels build trust."
COPYING: "Copied videos get less reach and can bring
  claims. Let's make our own version of the idea."
""", ''),
    ],
    mistakes=[
        ('Thinking small fakery is harmless.', 'Platforms detect patterns; clients lose trust when they find out.'),
        ('Agreeing to bad requests to keep a client.', 'Say no with an honest alternative; good clients stay.'),
        ('"Tag 5 friends to win" giveaways.', 'That is engagement bait. Use clear terms and real entries.'),
        ('Fake countdowns and "only 2 left".', 'False urgency is a banned dark pattern.'),
    ],
    quiz=[
        {'q': 'What does YouTube do with artificial traffic?',
         'o': ['Counts it double', 'Doesn\'t count it, and it can lead to strikes', 'Pays for it', 'Ignores it with no effect'],
         'a': 'B', 'why': 'YouTube says artificial traffic isn\'t counted and can bring strikes.'},
        {'q': 'Which is a dark pattern banned in India in 2023?',
         'o': ['Showing the full price upfront', 'False urgency, such as a fake countdown', 'A clear Ad label', 'A real deadline'],
         'a': 'B', 'why': 'The CCPA\'s guidelines list false urgency among 13 dark patterns.'},
        {'q': 'A client asks you to write reviews under different names. What do you do?',
         'o': ['Write them carefully', 'Refuse and suggest asking real customers with a QR card', 'Ask family to write them', 'Buy them'],
         'a': 'B', 'why': 'Fake reviews break Google\'s policies and mislead customers.'},
        {'q': 'Why do bought followers hurt an account\'s reach?',
         'o': ['They don\'t', 'They never watch, so engagement and views per follower fall', 'They post spam', 'They change the bio'],
         'a': 'B', 'why': 'The system sees a large audience that ignores the posts.'},
    ],
    study='Platform rules on fake engagement, inauthentic behaviour, reviews, engagement bait and monetisation, and India\'s dark patterns guidelines (about 30 minutes)',
    action='check your account status, write your ethics code and "no, but" replies, and fix a real dark pattern example',
)

L4 = lesson(
    14, 4,
    title='Negative comments, crises and account security',
    weeks=(36, 36), hours=2.5,
    outcome='Respond calmly to negative comments, follow a crisis playbook when a problem spreads, and secure your own and your clients\' accounts against hacking and scams.',
    split='35 minutes study, 1 hour 55 minutes action',
    core=f"""
### Not every negative comment is the same

| Type | Example | What to do |
| --- | --- | --- |
| **Genuine complaint** | "Ordered a cake for 5 pm, came at 7" | Acknowledge, apologise if it's fair, take it to private messages, fix it, follow up |
| **Misunderstanding** | "Why ₹650? Bakeries charge ₹400" | Explain politely once, with facts |
| **Troll** | Insults with no real complaint | Don't feed it: hide, restrict or block under your house rules |
| **Spam and scams** | "DM for followers", fake links | Delete, block, report |
| **Hate or threats** | Abuse about religion, caste, gender; threats | Remove, report to the platform; for threats, keep evidence and contact the police |

**Never delete genuine complaints** just because they're negative; other customers notice, and a good public reply shows you care. **Never argue** in public, and never share a customer's private details while defending the business.

### The response ladder

1. **Acknowledge** quickly: "Sorry to hear this, Shabna."
2. **Apologise** if the business got it wrong. Don't make excuses.
3. **Move it private:** "Please WhatsApp us on ___ so we can sort it today."
4. **Fix it:** replace, refund or redo, as the business decides.
5. **Close the loop** publicly if the customer is happy: "Glad we could fix it. Thank you for telling us."

Use the moderation tools from SMM-M07-L03: Hidden Words and Limits on Instagram, and held comments and blocked words in YouTube Studio.

### When it becomes a crisis

A **crisis** is a problem that spreads fast and can hurt a business's reputation: a viral video of bad service, a food safety complaint, an offensive post, a data leak. The playbook:

1. **Pause** all scheduled posts. Cheerful ads during a crisis look careless.
2. **Get the facts** from the owner before saying anything detailed.
3. **One voice:** decide who speaks for the business.
4. **A holding statement within hours:** "We've seen the video and are looking into it urgently. We'll update you by this evening."
5. **Fix the real problem,** and involve professionals or authorities when health, safety or the law is involved.
6. **Update** honestly, apologise if the business was wrong, and say what changes.
7. **Review afterwards:** what will stop it happening again?

### Account security

- **Two-step verification** everywhere. For Google, use Google prompts, a passkey or an authenticator app rather than SMS where you can; save the backup codes.
- **A unique, strong password** for each account, ideally in a password manager.
- **Roles, not passwords,** for client accounts: manager on Google Business Profile, people added in Meta Business Suite. Remove access when someone leaves.
- **Phishing red flags:** messages claiming "copyright violation, your account will be deleted", "Meta support" asking for login codes, fake brand deals with attachments or login pages, "verify your account" links. Real platforms don't ask for your password or codes in DMs.
- **If an Instagram account is hacked:** go to **instagram.com/hacked** to report and recover access. For a Google account, use Google's account recovery.
- **If money or fraud is involved:** call the **1930** cyber crime helpline (24 hours) and report at the National Cyber Crime Reporting Portal ({ASOF}).
""",
    example="""
On a Friday evening a customer posted on **Nisha's Oven's** Reel: "Found a hair in my cake. Disgusting!!" with a photo, and it had 40 replies within an hour (made-up example).

Anu and Nisha followed the playbook:

- **Paused** the scheduled weekend offer post.
- **Facts:** Nisha checked the order: a 1 kg chocolate cake delivered that afternoon.
- **Holding reply within 30 minutes:** "We're very sorry, Reshma. This should never happen. We've messaged you to replace the cake and refund you today, and we're checking our kitchen process tonight."
- **Fix:** a full refund and a new cake the next morning; Nisha started wearing a hair cap in all baking videos and in the kitchen.
- **Update:** Reshma posted, "They refunded and replaced it the same day. Appreciate it." Nisha replied with thanks and a short note on the new kitchen rule.

The same week, Anu got an Instagram DM: "Your account will be deleted for copyright violation, appeal here: [link]". She didn't click; she checked Account Status (no issues) and reported the message.
""",
    resources=[
        ('ig-abuse', 'Re-read Limits and Hidden Words', '3 min'),
        ('yt-moderation', 'Re-read the comment moderation settings', '3 min'),
        ('yt-harassment', 'Read what YouTube\'s harassment policy covers and how to report', '5 min'),
        ('g-2sv', 'Re-read the second-step options and backup codes', '5 min'),
        ('tribune-hacked', 'Read how Instagram.com/hacked works', '5 min'),
        ('kp-1930', 'Read about the 1930 helpline and the reporting portal', '3 min'),
        ('cybercrime', 'Note the address of the national reporting portal', '2 min'),
    ],
    steps=[
        'Study the resources (about 25 minutes).',
        'Write replies to five scenarios using the response ladder: a late delivery, a price complaint, a troll, a scam comment and a hateful comment.',
        'Write a one-page crisis playbook for your pilot client, with names, phone numbers and a holding statement in Malayalam and English.',
        'Run the security audit on all your accounts, and on your pilot client\'s accounts with their permission. Fix every gap.',
        'Save the phishing red flags as a note and share it with your pilot client.',
    ],
    proof='Your five scenario replies, the crisis playbook and the completed security audit with the fixes made.',
    templates=[
        ('response ladder replies', """
ACKNOWLEDGE: Sorry to hear this, [name].
APOLOGISE (if fair): We got this wrong, and we're sorry.
MOVE PRIVATE: Please WhatsApp us on ____ so we can fix it
  today.
FIX: [replace / refund / redo]
CLOSE: Glad we could sort it, thank you for telling us.
ML: ക്ഷമിക്കണം, [പേര്]. ഇന്നുതന്നെ പരിഹരിക്കാൻ ____ ൽ
  വാട്സാപ്പ് ചെയ്യൂ.
""", ''),
        ('crisis playbook (one page)', """
BUSINESS: ________  SPOKESPERSON: ________ (phone ____)
BACK-UP: ________ (phone ____)
STEP 1: pause scheduled posts (who: ____ where: ____)
STEP 2: facts from the owner within 1 hour
STEP 3: holding statement within ___ hours:
  EN: "We've seen this and are looking into it urgently.
       We'll update you by ____."
  ML: "ഇത് ഞങ്ങളുടെ ശ്രദ്ധയിൽ പെട്ടിട്ടുണ്ട്, അടിയന്തരമായി പരിശോധിക്കുന്നു.
       ____ നുള്ളിൽ അറിയിക്കാം."
STEP 4: fix the problem; professionals or authorities if
  health, safety or law are involved
STEP 5: honest update; apology if we were wrong
STEP 6: review: what changes so it doesn't happen again?
NEVER: argue, delete genuine complaints, share customers'
  private details, make threats
""", ''),
        ('security audit checklist', """
FOR EACH ACCOUNT (Google/YouTube, Instagram, Facebook,
WhatsApp Business, LinkedIn, email)
[ ] Two-step verification on (prompts, passkey or app
    rather than SMS where possible)
[ ] Backup codes saved offline
[ ] Unique strong password (password manager)
[ ] Recovery email and phone up to date
[ ] Clients: access by roles, never shared passwords
[ ] Old staff and freelancers removed
[ ] No unknown apps connected
PHISHING RED FLAGS: "account will be deleted" / "copyright
  violation, appeal here" / "Meta support" asking for codes
  / brand deals with attachments or login pages
IF HACKED: instagram.com/hacked; Google account recovery;
  money or fraud: call 1930 and report on the national portal
""", ''),
    ],
    mistakes=[
        ('Deleting every negative comment.', 'Hide trolls and spam; answer genuine complaints in public, then fix them privately.'),
        ('Arguing with customers.', 'Acknowledge, move private, fix.'),
        ('Posting offers during a crisis.', 'Pause scheduled posts first.'),
        ('Clicking "copyright violation" links in DMs.', 'Check Account Status inside the app instead.'),
        ('Sharing client passwords.', 'Use roles, and remove access when people leave.'),
    ],
    quiz=[
        {'q': 'A genuine complaint appears under a Reel. What do you do first?',
         'o': ['Delete it', 'Acknowledge it publicly and move the details to private messages', 'Argue', 'Ignore it'],
         'a': 'B', 'why': 'Respond quickly and kindly, then fix it privately.'},
        {'q': 'What is the first step when a crisis starts?',
         'o': ['Post an offer', 'Pause scheduled posts and get the facts', 'Delete the account', 'Blame the customer'],
         'a': 'B', 'why': 'Stop careless posts and understand what happened before speaking.'},
        {'q': 'A DM says your account will be deleted for copyright violation and gives a link. What do you do?',
         'o': ['Click and log in quickly', 'Don\'t click; check Account Status in the app and report the message', 'Forward it to clients', 'Reply with your password'],
         'a': 'B', 'why': 'It is a common phishing trick.'},
        {'q': 'Where do you go if an Instagram account is hacked?',
         'o': ['A random recovery service', 'instagram.com/hacked', 'A Facebook group', 'Nowhere'],
         'a': 'B', 'why': 'Instagram\'s own page for reporting and resolving access problems.'},
    ],
    study='Moderation tools, YouTube\'s harassment policy, Google 2-Step Verification, Instagram\'s hacked-account help and cyber crime reporting (about 25 minutes)',
    action='write replies to five scenarios, a crisis playbook for your pilot client and complete a security audit',
)

LESSONS = [L1, L2, L3, L4]

MODULE = module(
    14,
    title='Ethics, law and safety',
    weeks=(34, 36), hours=10,
    overview="""
Work in a way that keeps you, your clients and the public safe: disclosure rules, copyright and music licensing, consent and personal data, honest growth, crisis handling and account security.

You've followed the "rules from day 1" all course. Now you learn them properly, the way a professional must before taking paid clients: ASCI's influencer guidelines and India's endorsement rules, copyright and music, consent for photos of people (especially children) and the DPDP Rules, the platform rules against fake engagement and fake reviews, India's ban on dark patterns, and what to do when comments turn negative or an account is attacked.

The module project is your compliance and safety kit, which goes into every client agreement.
""",
    outcomes=[
        'Apply ASCI\'s labels and placement rules and India\'s endorsement standards',
        'Use only licensed content and handle copyright claims correctly',
        'Get and keep consent for filming people and handle personal data carefully',
        'Explain why fake engagement, fake reviews and dark patterns harm clients, and offer alternatives',
        'Follow a crisis playbook and secure accounts with two-step verification and roles',
    ],
    lessons=LESSONS,
    project='Your compliance and safety kit',
    project_week=36,
    project_steps=[
        'Put in one folder (14 Compliance): the disclosure checklist and placement card, your consent form, your safe sources list, your ethics code and "no, but" replies, the response ladder, the crisis playbook template and the security audit checklist.',
        'Write a one-page "how I work safely" summary you can give clients.',
        'Confirm that the security audit is done for your accounts and your pilot client\'s.',
        'Fix anything in your own past posts that the kit shows is wrong.',
    ],
    project_proof='The 14 Compliance folder and your one-page "how I work safely" summary.',
    rubric=[
        ('Disclosure', 'Labels missing or hidden', 'Labels used inconsistently', 'Correct labels and placement for every format, platform tools on'),
        ('Copyright and music', 'Uses downloaded music and images', 'Mostly licensed', 'Only own or licensed content; claims handled correctly'),
        ('Consent and data', 'Films people without asking', 'Asks sometimes', 'Consent saved for everyone; children protected; personal data hidden'),
        ('Honest growth', 'Uses or would use fakes', 'Avoids fakes but can\'t explain why', 'Explains the rules and offers honest alternatives'),
        ('Crisis and security', 'No plan; weak security', 'Some 2FA', 'Crisis playbook ready; 2FA and roles on every account'),
    ],
    short=[
        'Learn the label placement card by heart and check 5 sponsored posts.',
        'Audit your last 10 posts for music and consent.',
        'Write your ethics code.',
        'Turn on two-step verification everywhere and save the backup codes.',
    ],
    flashcards=[
        ('ASCI: disclosure needed even if the review is honest?', 'Yes: "Disclosures are required even if the evaluations are unbiased."'),
        ('ASCI labels?', 'Advertisement, Ad, Sponsored, Collaboration, Partnership, Employee, Free gift, Affiliate.'),
        ('Label time for a 15-second-to-2-minute video?', 'At least a third of its length.'),
        ('CCPA maximum fine for a misleading ad, first and repeat?', '₹10 lakh; ₹50 lakh.'),
        ('Is giving credit a valid reason to dispute a Content ID claim?', 'No.'),
        ('What do the DPDP Rules expect for children\'s data?', 'Verifiable consent from a parent or guardian.'),
        ('Four dark patterns banned in 2023?', 'False urgency, bait and switch, drip pricing, disguised advertisements (13 in all).'),
        ('First step in a crisis?', 'Pause scheduled posts and get the facts.'),
        ('Hacked Instagram account?', 'instagram.com/hacked.'),
        ('Cyber fraud helpline?', '1930 (24 hours).'),
    ],
    mistakes=[
        ('Treating rules as optional for small accounts.', 'The rules apply to everyone, and clients rely on you to know them.'),
        ('Giving legal advice.', 'Explain the rules simply; for disputes and contracts, point clients to professionals.'),
        ('Assuming rules stay the same.', 'Check the official sources every few months.'),
    ],
)
