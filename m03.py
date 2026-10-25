from common import lesson, module, link, ASOF

L1 = lesson(
    3, 1,
    title='Instagram: Reels, Stories, carousels and your profile',
    weeks=(5, 5), hours=3.5,
    outcome='Know what each Instagram format is for and its current limits, optimise your profile so the right people understand and find it in seconds, and publish a Reel, a carousel and Stories.',
    split='1 hour study, 2 hours 30 minutes action',
    core=f"""
### The formats and what each is for ({ASOF})

| Format | What it is | Best for | Current limits and tips |
| --- | --- | --- | --- |
| **Reels** | Vertical video, shown to followers and non-followers | Reaching new people | Reels up to 3 minutes can be recommended to non-followers in the Reels tab and Explore. Use 9:16, hook in the first 3 seconds, no other app's watermark. |
| **Trial reels** | A reel shown first only to non-followers | Testing an idea without risking your followers\' feed | Results after about 24 hours; then share it to your profile or leave it. For professional accounts. |
| **Carousels** | Up to 20 photos or videos in one post | Saving and sharing: guides, lists, before and after, price lists | The profile grid shows rectangles since January 2025, so keep key text in the middle of the cover. Adding audio can help photos and carousels show in the Reels tab. |
| **Stories** | Photos or videos that disappear after 24 hours | Talking to people who already follow you | Polls, questions and link stickers start conversations. Save the best in **Highlights** on your profile. |
| **Live** | Real-time video | Q&A, events, launches | Announce it in Stories first. |
| **Broadcast channels** | One-to-many messages to followers who join | Updates for your keenest followers | Listed among Instagram's creator tools. |
| **DMs** | Private messages | Turning interest into enquiries | Reply fast; set up saved replies. |

### Professional account: creator or business

A professional account is public, gets **Insights** and can check **Account Status** (whether its content can be recommended). Choose **Creator** for a page or a personal brand and **Business** for a shop or service. Instagram's help pages explain the difference and how to switch. One practical difference to check: Instagram's licensed music library isn't available in the same way to every account, so business accounts may see a smaller selection of music, such as Meta's royalty-free Sound Collection ({ASOF}).

### Your profile is a 3-second test

A new visitor decides in seconds whether to follow. Instagram's own tips say to put **keywords in your handle, profile name, bio and captions**, because search reads them. Optimise each part:

- **Username (handle):** short, easy to spell, the same on every platform: @kuttiady.diaries
- **Name field:** the keyword people search for, not just your name: "Kuttiady | Food, Shops, Local news"
- **Bio (who + what + proof + action):** "Real places around Kuttiady with price and location. Visited and checked by Anu. New post every Mon, Wed, Fri. Tag us or DM to suggest a spot."
- **Links:** Instagram allows up to five links in your bio (since April 2023): for example your WhatsApp Channel, YouTube and a Google Form for suggestions.
- **Contact buttons** (business accounts): call, WhatsApp, directions.
- **Highlights:** 3–5 with simple covers: "Start here", "Food", "Ask us", "Rules".
- **Pinned posts:** pin your best and most typical posts to the top of your grid.

### Hashtags and captions

Since December 2025 Instagram limits captions to **five hashtags**, and says fewer, more targeted ones work better than many generic ones such as #reels or #explore ({ASOF}). Put keywords and hashtags in the caption, not in a comment.

### Views is the main number

Since August 2024, **Views** is the main metric across Reels, photos, carousels and Stories in Insights, counting repeat views. Look at how many views came from **non-followers**: that is your growth.
""",
    example="""
**Peak Fitness**, a gym in Vatakara, had the handle @peak_fitness_vtk_official_2019, the name field "Peak Fitness", a bio with three emojis and no location, and no Highlights. New visitors couldn't tell what it was or where.

After an hour of work: handle @peakfitness.vatakara; name field "Gym in Vatakara | Peak Fitness"; bio "Strength and weight-loss training for beginners. Women's batch 6–8 am. First session free. WhatsApp below 👇"; links to WhatsApp and the timetable; Highlights "Batches", "Fees", "Results (with permission)", "Find us".

They posted a carousel, "5 machines beginners use wrongly", and a 30-second Reel of a trainer fixing a squat. Over the next four weeks, profile visits rose from about 40 to 160 a week, and the gym started asking every new member how they'd heard about it: 6 of 19 said Instagram.

(Peak Fitness and its numbers are made up to show the method.)
""",
    resources=[
        ('ig-reels-2025', 'Read the whole post: 3-minute reels, trial reels and audio on photos', '10 min'),
        ('ig-pro', 'Open it and follow the steps if your account isn\'t professional yet', '5 min'),
        ('ig-pro-types', 'Read the difference between business and creator accounts', '5 min'),
        ('tc-trial', 'Read how trial reels work', '5 min'),
        ('mc-carousel', 'Note the 20-item carousel limit', '3 min'),
        ('ss-hashtags', 'Read why Instagram cut hashtags to five', '5 min'),
        ('ss-views', 'Read what changed when Views became the main metric', '5 min'),
        ('tc-links', 'Read how to add up to five links', '3 min'),
    ],
    steps=[
        'Study the resources (about 45 minutes).',
        'Check your account is professional (Creator for a page or personal brand). Open Account Status and screenshot it.',
        'Screenshot your profile as it is now ("before").',
        'Optimise it with the checklist: handle, name field keyword, bio formula, links, Highlights with simple covers, pinned posts.',
        'Publish one Reel (vertical, hook in the first 3 seconds) and one carousel (5–10 slides) that fit your pillars. If trial reels are available to you, publish the Reel as a trial first.',
        'Post 3 Stories over the week, including one poll or question sticker, and save one to a Highlight.',
        'Screenshot your profile again ("after") and log the posts.',
    ],
    proof='Before and after screenshots of your profile, your Account Status screenshot, and links to the Reel and carousel with their Posting Log rows.',
    templates=[
        ('Instagram profile checklist', """
[ ] Professional account (Creator or Business)
[ ] Account Status checked: no issues
[ ] Handle: short, easy to spell, same everywhere
[ ] Name field includes the keyword people search
[ ] Bio: who it's for + what they get + proof + action
[ ] Links (up to 5): WhatsApp / YouTube / form / site
[ ] Contact buttons (business): call, WhatsApp, directions
[ ] 3-5 Highlights with simple covers
[ ] Best posts pinned to the top
[ ] Profile photo clear at small size
[ ] Location or service area clear
""", ''),
        ('bio formula (English and Malayalam)', """
[Who it's for] + [what they get] + [proof] + [action]

EN: Real places around Kuttiady with price and
    location. Visited and checked. New posts Mon,
    Wed, Fri. DM us a spot to feature!
ML: കുറ്റ്യാടിയിലെ നല്ല സ്ഥലങ്ങൾ, വിലയും ലൊക്കേഷനും സഹിതം.
    നേരിട്ട് പോയി നോക്കിയവ മാത്രം.
    പുതിയ പോസ്റ്റ് തിങ്കൾ, ബുധൻ, വെള്ളി.
    നിങ്ങളുടെ ഇഷ്ട സ്ഥലം DM ചെയ്യൂ!
""", ''),
        ('format quick card', """
REEL: 9:16 vertical, 1080 x 1920, hook in 3 s,
      up to 3 min, no other app's watermark,
      captions on screen, audio added
CAROUSEL: up to 20 slides; cover slide = hook;
      last slide = call to action; key text
      in the middle (grid shows rectangles)
STORY: 9:16; 24 hours; add a poll or question;
      save the best to a Highlight
CAPTION: first line = hook; keywords in the text;
      max 5 hashtags, specific not generic
""", ''),
    ],
    mistakes=[
        ('A handle full of underscores and numbers.', 'If people can\'t remember or spell it, they can\'t find you. Make it short and clear.'),
        ('A bio about you instead of the visitor.', 'Say who it\'s for and what they get, then give one action.'),
        ('Posting horizontal videos as Reels.', 'Shoot vertical 9:16 from the start (SMM-M04-L03).'),
        ('Generic hashtags.', 'Five specific tags (#kuttiady #kozhikodefood) beat #reels #viral #explore.'),
        ('Ignoring Stories.', 'Stories are where followers talk back. Use polls and questions every week.'),
    ],
    quiz=[
        {'q': 'How many hashtags does Instagram now allow in a caption, as reported in December 2025?',
         'o': ['30', '10', '5', 'Unlimited'],
         'a': 'C', 'why': 'Instagram limited captions to five hashtags and says fewer, targeted ones work better.'},
        {'q': 'What is a trial reel?',
         'o': ['A paid ad', 'A reel shown first to non-followers so you can test it', 'A reel only your followers see', 'A deleted reel'],
         'a': 'B', 'why': 'Trial reels go to non-followers first; you see results after about 24 hours.'},
        {'q': 'Where does Instagram suggest putting keywords so people can find you in search?',
         'o': ['Only in comments', 'In your handle, profile name, bio and captions', 'In your password', 'Nowhere; search ignores text'],
         'a': 'B', 'why': 'Instagram\'s tips name the handle, profile name, bio and captions.'},
        {'q': 'Which format is usually best for reaching people who don\'t follow you yet?',
         'o': ['Stories', 'Reels', 'DMs', 'Highlights'],
         'a': 'B', 'why': 'Reels are recommended to non-followers in the Reels tab and Explore.'},
    ],
    study='Instagram\'s creator posts and help pages, plus dated reports on reels, carousels, hashtags and views (about 45 minutes)',
    action='optimise your Instagram profile and publish a Reel, a carousel and Stories',
)

L2 = lesson(
    3, 2,
    title='YouTube: Shorts, long-form and your channel',
    weeks=(5, 6), hours=3,
    outcome='Set up and optimise a YouTube channel, understand when to use Shorts and when to use long videos, and publish your first Short.',
    split='1 hour study, 2 hours action',
    core=f"""
### Two kinds of YouTube

| | **Shorts** | **Long-form videos** |
| --- | --- | --- |
| Shape and length | Square or vertical, up to 3 minutes (for uploads since 15 October 2024) | Usually horizontal 16:9, any length |
| How people find them | Swiping in the Shorts feed | Search, home page, suggested videos |
| What they build | Reach and discovery | Trust, depth and search traffic for months or years |
| Effort | Low to medium | Medium to high |

A good beginner plan: **Shorts for discovery, long videos for trust.** For example, a 40-second Short answers one question; a 10-minute video answers the whole topic and appears in search for years.

### Music and Shorts: a trap to avoid

YouTube's rule ({ASOF}): a Short **longer than 1 minute** with an active Content ID copyright claim is **blocked worldwide**. It can't be watched, recommended or earn money until the claim is released. So for Shorts over a minute, use music from YouTube's own libraries: most Shorts audio library songs can be used for up to 90 seconds in a 3-minute Short, and royalty-free tracks from the **YouTube Audio Library** in YouTube Studio won't get a Content ID claim. Module 14 covers copyright properly.

### How YouTube decides what to show

Recommendations use watch history, search history, subscriptions, likes, dislikes, "Not interested" clicks and satisfaction surveys. Search ranks videos by **relevance** (how well the title, description, tags and the video itself match the search), **engagement** (for example watch time for that search) and **quality** (signs of expertise and trustworthiness). YouTube says it doesn't accept payment for better placement in organic search. SMM-M07-L01 covers YouTube SEO.

### Set up your channel properly

- **Name and handle:** the same as your Instagram page.
- **Description:** the first two lines say who it's for and what they get, with your main keywords: "Kuttiady food, shops and local news in Malayalam. New Shorts every Mon, Wed and Fri."
- **Banner and profile picture:** make the banner in Canva; keep text in the centre so it isn't cut off on phones.
- **Links and contact:** WhatsApp Channel, Instagram, a business email.
- **Verify your account** with a phone number. Custom thumbnails need a verified account, and custom thumbnails for Shorts can only be added in YouTube Studio on a computer ({ASOF}).
- **Upload defaults** (in YouTube Studio settings): a default description with your links saves time on every upload.

### Thumbnails in one paragraph

For long videos, upload a 16:9 image (YouTube recommends high resolution and a minimum width of 640 pixels; 1280 × 720 is a common, light size). From the phone the file must be under 2 MB. One face or object, 3–5 big words, strong contrast (SMM-M04-L05).

### The YouTube Partner Program, honestly

YouTube's expanded Partner Program is available in India ({ASOF}). The first level (fan funding and Shopping features) needs **500 subscribers, 3 public uploads in the last 90 days, and either 3,000 watch hours in 12 months or 3 million Shorts views in 90 days**. Sharing ad revenue needs **1,000 subscribers and either 4,000 watch hours in 12 months or 10 million Shorts views in 90 days**. Most new channels take many months to get there, and many never do, so treat it as a later bonus, not the plan (Module 10). Check current rules before you rely on these numbers.

### Apps

- **YouTube Studio** (phone and computer): analytics, comments, video details.
- **YouTube Create**: Google's free phone editor with a royalty-free music library, captions and voiceover. It needs Android 8.0 or later and at least 4 GB of RAM, so it may not run on older phones (SMM-M04-L04 has alternatives).
""",
    example="""
**Fathima's PSC Sprint** (from the Entrepreneurship course) runs a Malayalam YouTube channel for Kerala PSC learners:

- **Shorts, Monday to Saturday:** one PSC question in 30–45 seconds, answer explained in Malayalam, ending "Full weekly test every Sunday".
- **One long video every Sunday:** "This week's 20 questions explained", 12–15 minutes with chapters, a thumbnail with the week number and a clear title such as "Kerala PSC LDC 2026: 20 Kerala history questions explained (Malayalam)".
- **Music:** none in the questions; a soft track from the YouTube Audio Library in the intro of long videos.

After three months, most new subscribers came from Shorts, but most watch time came from the Sunday videos, because people searched for them. Each format did a different job.

(Made-up example to show the method.)
""",
    resources=[
        ('yt-shorts3', 'Read the whole page, especially the copyright rule for Shorts over 1 minute', '10 min'),
        ('yt-creators', 'In "Create", read the Shorts and Longform pages', '20 min'),
        ('yt-search', 'Read how search ranks videos', '10 min'),
        ('yt-thumbs', 'Read the thumbnail requirements', '5 min'),
        ('yt-ypp', 'Read the eligibility thresholds and what each level unlocks', '10 min'),
    ],
    steps=[
        'Study the resources (about 55 minutes).',
        'Set up your channel with the checklist: handle, keyword description, banner, links, contact email and upload defaults.',
        'Verify your account with your phone number in YouTube Studio settings.',
        'Upload your first Short: a 20–45 second vertical video that fits a pillar. Use your original video file (not one downloaded from Instagram with its watermark).',
        'Write a one-paragraph plan for one long video you will make in Module 4: topic, title, 5 chapter headings.',
    ],
    proof='Screenshots of your channel page and verification status, the link to your first Short with its Posting Log row, and your long-video plan.',
    templates=[
        ('channel setup checklist', """
[ ] Channel name and handle match your Instagram
[ ] Description: line 1 who it's for, line 2 what they
    get + main keywords; posting schedule
[ ] Banner made in Canva, text in the safe centre
[ ] Profile picture clear at small size
[ ] Links: WhatsApp Channel, Instagram, email
[ ] Account verified (phone number)
[ ] Upload defaults: description with links, category,
    language set to Malayalam or English
[ ] YouTube Studio app installed, comments notifications on
""", ''),
        ('Shorts and long-form plan', """
SHORTS (discovery)
  Series name: ______________  How often: ______
  Length: ___ seconds  Hook style: ____________
  Music: none / Shorts library / Audio Library
  Ending line: points to the long video or Channel

LONG VIDEO (trust and search)
  Topic: ____________________________________
  Title with the search phrase: ______________
  Chapters: 00:00 Intro / ____ / ____ / ____ / ____
  Thumbnail idea (3-5 words): ________________
""", ''),
    ],
    mistakes=[
        ('Copyrighted film songs in Shorts.', 'Over a minute, a claim blocks the Short worldwide. Use YouTube\'s libraries or no music.'),
        ('Uploading Instagram downloads with the watermark.', 'Export your original file and upload that.'),
        ('An empty channel description.', 'The first two lines help viewers and search understand the channel.'),
        ('Chasing the Partner Program in month one.', 'Build useful videos first; the thresholds come later, if at all.'),
    ],
    quiz=[
        {'q': 'What happens to a 2-minute Short with an active Content ID claim, according to YouTube Help?',
         'o': ['It earns money for you', 'It is blocked worldwide until the claim is resolved', 'Nothing', 'It becomes a long video'],
         'a': 'B', 'why': 'Shorts over one minute with an active claim are blocked globally.'},
        {'q': 'Which three elements does YouTube say it prioritises in search?',
         'o': ['Relevance, engagement and quality', 'Price, length and colour', 'Hashtags, likes and time of day', 'Subscribers only'],
         'a': 'A', 'why': 'YouTube lists relevance, engagement and quality.'},
        {'q': 'Why is verifying your YouTube account useful early on?',
         'o': ['It doubles your views', 'Custom thumbnails need a verified account', 'It removes ads', 'It is required to watch videos'],
         'a': 'B', 'why': 'You can upload your own thumbnails only if your account is verified.'},
        {'q': 'Which is a sensible beginner plan?',
         'o': ['Only 1-hour videos', 'Shorts for discovery and long videos for trust and search', 'Only reposts', 'Wait for 1,000 subscribers before posting long videos'],
         'a': 'B', 'why': 'The two formats do different jobs and support each other.'},
    ],
    study='YouTube\'s Shorts, search, thumbnail and Partner Program help pages and the Creators guides (about 55 minutes)',
    action='set up and verify your channel, publish your first Short and plan one long video',
)

L3 = lesson(
    3, 3,
    title='Facebook Pages and Groups, and WhatsApp Business',
    weeks=(6, 6), hours=3,
    outcome='Set up WhatsApp Business with a catalogue, quick replies and labels, understand Status, Channels and business broadcasts and their rules, and decide how Facebook Pages and local Groups fit your plan.',
    split='50 minutes study, 2 hours 10 minutes action',
    core=f"""
### Facebook: older audiences, local groups and Reels

Many local customers, especially older ones, still discover and discuss businesses on Facebook, often in local Groups. A **Facebook Page** gives a business a public presence with posts, Reels, reviews and events. You can post to a Page and an Instagram account together from **Meta Business Suite**, which also lets you schedule posts and Stories for both and reply to messages and comments in one inbox.

Two rules to know ({ASOF}):

- **Original content wins.** In July 2025 Meta said Facebook accounts that repeatedly repost other people's text, photos or videos get lower distribution and can lose access to monetisation. Reactions, commentary and joining trends are fine; plain reposting is not.
- **Groups have their own rules.** Local buy-and-sell and community groups are powerful, but each admin sets rules about promotion. Read them, help first, and promote only where it's allowed.

### WhatsApp Business: the shop counter in your customer's pocket

For most small businesses in Kerala, WhatsApp is where enquiries turn into sales. The free **WhatsApp Business** app adds tools on top of normal WhatsApp ({ASOF}):

- **Business profile:** description, address or service area, hours, email, website
- **Catalogue:** products or services with photos, prices and descriptions that customers can browse and share
- **Greeting and away messages:** automatic replies when someone first messages or when you're closed
- **Quick replies:** saved answers to common questions, typed with a shortcut such as /price
- **Labels and lists:** sort chats, such as New enquiry, Order confirmed, Paid, Delivered
- **Customer notes:** remember details like "prefers eggless cakes"
- **Message statistics** and **ads that click to WhatsApp** (Module 9)

### Status, Channels and broadcasts

| Tool | Who sees it | Good for | Know this |
| --- | --- | --- | --- |
| **Status** | Your contacts who have your number saved, for 24 hours | Daily specials, behind the scenes | Feels personal; post 1–3 a day at most |
| **Channel** | Anyone who follows it | Regular updates for many people | One-way: followers can't reply, only react with emoji or vote in polls. Followers don't see the admin's name, photo or number. Creating a channel is still rolling out, so it may not be available to everyone yet. |
| **Business broadcasts** | The customers you choose, as private one-to-one messages | Offers, reminders, restock alerts | Can reach customers even if they haven't saved your number; can be scheduled; shows read and reply rates. WhatsApp has been testing monthly limits and paid tiers for broadcasts, so check current rules. |

### Message only people who agreed

Send offers only to people who gave you their number for that purpose and are happy to hear from you. Tell them how to stop ("Reply STOP"). Spamming people gets you blocked and reported, and WhatsApp has been {link('tc-wa-unreplied', 'testing limits on messages that get no reply')}. India's data protection rules also expect clear consent for using personal data (Module 14).
""",
    example="""
**Amma's Pickles**, a Kudumbashree unit in Perambra, set up WhatsApp Business on a second SIM:

- **Profile:** "Home-made Malabar pickles. Orders by 6 pm, delivered next day within 10 km. Mon–Sat 9–6."
- **Catalogue:** 8 pickles with photos taken in daylight, the weight and the price (₹120 for 250 g mango, ₹180 for 250 g prawn).
- **Quick replies:** /price (catalogue link), /delivery (areas and charges), /pay (UPI ID and QR), /order (how to order in three steps), in Malayalam and English.
- **Labels:** New enquiry, Confirmed, Paid, Delivered, Repeat customer.
- **Status:** one photo a day of the day's batch.
- **Channel:** "Amma's Pickles updates": weekly new flavours and festival pre-orders.

In the local Facebook group "Perambra Market" (whose rules allow selling posts on Saturdays), they post one Reel each Saturday and answer every comment. After a month, they could see from labels that 40% of new enquiries mentioned the group.

(Made-up example to show the method.)
""",
    resources=[
        ('wa-tools', 'Read the list of built-in business tools', '10 min'),
        ('wa-broadcasts', 'Read how business broadcasts work', '10 min'),
        ('wa-channels', 'Read how channels work and who sees what', '5 min'),
        ('tc-wa-limits', 'Read about broadcast limits and paid tiers being tested', '5 min'),
        ('mbs-app', 'Read what Meta Business Suite does; install it if you will use a Facebook Page', '5 min'),
        ('tc-fb-original', 'Read what counts as unoriginal content on Facebook', '5 min'),
        ('bp-free', 'Watch the 1-minute videos "How to create a Facebook Page" and "How to post on a Facebook Page"', '5 min'),
    ],
    steps=[
        'Study the resources (about 45 minutes).',
        'Install WhatsApp Business, ideally on a separate number for your page or a future client. Fill in the business profile completely.',
        'Build a catalogue with 3–5 items. For a practice page, use services such as "Feature your shop (free)" or "Local event listing".',
        'Write 4 quick replies in Malayalam and English, set a greeting message and an away message, and create 4 labels.',
        'Post one Status and, if Channels are available to you, create a Channel for your page and post one update.',
        'Facebook: either create a Page for your practice account and connect it to Instagram in Meta Business Suite, or join 3 local Facebook Groups and write down each group\'s promotion rules.',
    ],
    proof='Screenshots of your WhatsApp Business profile, catalogue, quick replies and labels, plus your Facebook Page link or the rules of 3 local groups.',
    templates=[
        ('WhatsApp Business setup checklist', """
[ ] Separate number (or decided to use mine)
[ ] Profile: description, address or area, hours,
    email, links
[ ] Catalogue: 3+ items, daylight photos, prices
[ ] Greeting message (first contact)
[ ] Away message (outside hours)
[ ] Quick replies: /price /delivery /pay /order
[ ] Labels: New enquiry, Confirmed, Paid, Delivered,
    Repeat customer
[ ] Status plan: 1-3 a day at most
[ ] Channel (if available) and its link in your bios
[ ] Broadcasts only to people who agreed, with a way
    to stop
""", ''),
        ('quick replies (English and Malayalam)', """
/order
EN: Thanks for your message! To order: 1. Choose from
    our catalogue 2. Send the item and quantity
    3. Share your location. We confirm in 10 minutes.
ML: മെസ്സേജിന് നന്ദി! ഓർഡർ ചെയ്യാൻ: 1. കാറ്റലോഗിൽ നിന്ന്
    തിരഞ്ഞെടുക്കുക 2. ഐറ്റവും എണ്ണവും അയക്കുക
    3. ലൊക്കേഷൻ ഷെയർ ചെയ്യുക. 10 മിനിറ്റിനുള്ളിൽ ഉറപ്പിക്കാം.

/away
EN: We're closed now (open Mon-Sat, 9-6). We'll reply
    first thing tomorrow.
ML: ഇപ്പോൾ കട അടച്ചിരിക്കുന്നു (തിങ്കൾ-ശനി, 9-6).
    നാളെ രാവിലെ തന്നെ മറുപടി തരാം.
""", ''),
        ('Facebook group etiquette', """
Before posting in a group:
[ ] Read the rules and pinned posts
[ ] Check which days or posts allow promotion
[ ] Comment helpfully on others' posts for a week first
[ ] Post useful content, not only offers
[ ] Reply to every comment within a few hours
[ ] Never tag strangers or post the same thing in 10
    groups at once
""", ''),
    ],
    mistakes=[
        ('Adding people to broadcasts or groups without asking.', 'Message only people who agreed, and give an easy way to stop.'),
        ('A catalogue without prices.', '"Price?" is the first question. Answer it before they ask.'),
        ('Ten Status updates a day.', 'People mute you. One to three good ones are enough.'),
        ('Spamming Facebook groups.', 'Admins remove you. Help first, follow the rules, then promote.'),
        ('Reposting other people\'s videos on a Page.', 'Facebook lowers their reach and can remove monetisation. Make your own.'),
    ],
    quiz=[
        {'q': 'Can followers reply to a WhatsApp Channel update?',
         'o': ['Yes, with any message', 'No; they can react with emoji or vote in polls', 'Only on weekends', 'Only if they pay'],
         'a': 'B', 'why': 'Channels are one-way; followers react or vote.'},
        {'q': 'What are WhatsApp Business quick replies?',
         'o': ['Automatic ads', 'Saved answers to common questions, typed with a shortcut', 'Voice calls', 'A payment method'],
         'a': 'B', 'why': 'They save time and keep answers consistent.'},
        {'q': 'What did Meta announce in July 2025 about Facebook accounts that keep reposting others\' content?',
         'o': ['They get a badge', 'Lower distribution and possible loss of monetisation', 'More reach', 'Nothing'],
         'a': 'B', 'why': 'Meta is reducing distribution and monetisation for unoriginal content.'},
        {'q': 'Who should get your business broadcast offers?',
         'o': ['Every number you can find', 'Only people who agreed to hear from you, with a way to stop', 'Competitors\' customers', 'Random groups'],
         'a': 'B', 'why': 'Consent protects customers, your reputation and your number.'},
    ],
    study='WhatsApp Business tools, broadcasts and channels, plus Facebook basics (about 45 minutes)',
    action='set up WhatsApp Business with a catalogue, quick replies and labels, and set up a Facebook Page or study 3 local groups',
)

L4 = lesson(
    3, 4,
    title='LinkedIn, X, Threads, Telegram and Indian platforms: choosing your mix',
    weeks=(7, 7), hours=2.5,
    outcome='Know what LinkedIn, X, Threads, Telegram and Indian regional apps are good for, choose one main and one support platform for your account and for a client, and set up a LinkedIn profile for your career.',
    split='40 minutes study, 1 hour 50 minutes action',
    core=f"""
### The other platforms in one table ({ASOF})

| Platform | What it's good for | Know this |
| --- | --- | --- |
| **LinkedIn** | Careers, B2B services, professional credibility | Your personal profile matters more than a company Page for freelancers. LinkedIn says Pages with complete information get 30% more weekly views and that weekly posting doubles engagement (its own figures). Creator mode was removed in 2024 and its tools opened to everyone. Document (PDF) posts work well for guides. |
| **X (Twitter)** | News, public conversation, journalists, tech | Its recommendation code is published on GitHub: about half of the "For You" feed comes from accounts you follow, the rest from others, ranked by a neural network. Rarely the first choice for local shops. |
| **Threads** | Text conversations linked to your Instagram account | Meta said it reached 500 million monthly users in June 2026, and that India was one of its most active countries in 2024. It has topic Communities. Easy to repurpose Instagram ideas into short text posts. |
| **Telegram** | Education, exam prep, updates and files | Channels can have unlimited subscribers and keep the full history for new subscribers; add a discussion group for comments. |
| **ShareChat and Moj** | Indian-language feeds and short video | Both support Malayalam among many Indian languages; worth testing for some audiences. |
| **Koo** | — | Shut down in July 2024. |
| **TikTok** | — | Blocked in India since June 2020, along with 58 other apps. |

### Choose your mix: go deep before wide

Every extra platform costs time every week. A beginner does better with **one main platform** (where you post your best work and try to grow), **one support platform** (where you repurpose, with little extra work) and **WhatsApp** for conversations. Add more only when you can keep up without dropping quality.

Score each candidate from 1 to 5:

- **Audience:** are your persona's people really there? (Use your research from SMM-M02-L02.)
- **Format fit:** does your content suit it (short video, photos, text, long video)?
- **Goal fit:** does it serve your objective (awareness, trust, leads, career)?
- **Effort:** can you post there every week without burning out? (5 = easy)
- **Your skill:** do you enjoy and do well in that format?

### Your career profile on LinkedIn

Whatever your main platform, set up LinkedIn for your career now; Module 12 builds it further.

- **Headline:** "Learning social media marketing | Helping local businesses in Kozhikode get more enquiries" (be honest that you are learning)
- **About:** three short paragraphs: what you're learning, what you've done so far (your page, your challenge), and what you want to do next
- **Featured:** link your practice page now; add case studies later
""",
    example="""
Anu scored platforms for three different accounts:

| Account | Main | Support | Conversations | Why |
| --- | --- | --- | --- | --- |
| @kuttiady.diaries (her page) | Instagram Reels | YouTube Shorts | WhatsApp Channel | Local young audience on Reels; Shorts reuse the same videos |
| Kakkayam Hills Homestay | Instagram | YouTube long videos (room and trek tours) | WhatsApp Business for bookings | Travellers watch long tours before booking; Google reviews matter too |
| Fathima's PSC Sprint | YouTube | Telegram channel | WhatsApp Channel | Learners search YouTube; Telegram suits daily question files |

She also wrote her LinkedIn headline: "Learning social media marketing | Building a local page in Kuttiady | Open to helping small businesses in Kozhikode".

(Made-up example to show the method.)
""",
    resources=[
        ('li-pages', 'Read the best practices; note which figures are LinkedIn\'s own claims', '10 min'),
        ('smt-linkedin', 'Read what changed when Creator mode was removed', '5 min'),
        ('threads-500m', 'Read the Threads update: user numbers, Communities, live chats', '5 min'),
        ('tg-channels', 'Read how Telegram channels and discussion groups work', '5 min'),
        ('sharechat', 'Check the languages listed', '3 min'),
        ('x-algo', 'Skim the first part of the README: how "For You" is built', '5 min'),
        ('bt-koo', 'Read why Koo shut down', '3 min'),
        ('pib-apps', 'Read the June 2020 order that blocked TikTok and other apps', '3 min'),
    ],
    steps=[
        'Study the resources (about 40 minutes).',
        'Fill in the platform matrix for your practice account and choose your main and support platforms.',
        'Fill it in again for one real local business you might help later.',
        'Set up or update your LinkedIn profile: photo, headline, About and a Featured link to your practice page.',
        'If Threads suits you, make one short text post from an idea that did well on Instagram.',
    ],
    proof='Your two platform matrices with decisions, and a screenshot of your LinkedIn headline and About section.',
    templates=[
        ('platform selection matrix', """
Score 1-5 (effort: 5 = easy)
Platform   | Audience | Format | Goal | Effort | Skill | Total
Instagram  |          |        |      |        |       |
YouTube    |          |        |      |        |       |
Facebook   |          |        |      |        |       |
WhatsApp   |          |        |      |        |       |
LinkedIn   |          |        |      |        |       |
Threads    |          |        |      |        |       |
Telegram   |          |        |      |        |       |
ShareChat  |          |        |      |        |       |

MAIN: ________  SUPPORT: ________
CONVERSATIONS: WhatsApp Business / Channel / DMs
Posts a week: main ___ support ___
Review this choice in week 21 (after Module 8).
""", ''),
        ('LinkedIn headline and About formula', """
HEADLINE
[What you're learning or do] | [who you help] |
[proof or current project]

ABOUT (3 short paragraphs)
1. I'm learning social media marketing, focused on
   [niche or area].
2. So far I have [built @page / posted X times /
   run a 30-day challenge]. What I learned: ______
3. I'd like to help [kind of business] with
   [result]. Contact: ______
""", ''),
    ],
    mistakes=[
        ('Starting on six platforms at once.', 'Quality drops everywhere. One main, one support, plus WhatsApp.'),
        ('Planning around a blocked or closed app.', 'Check an app is available in India and still running before you plan.'),
        ('Treating LinkedIn like Instagram.', 'LinkedIn rewards useful, professional posts and a complete profile.'),
        ('Believing platform-published figures without saying so.', 'When you quote a platform\'s own numbers, say they are its claims.'),
    ],
    quiz=[
        {'q': 'What is a sensible platform mix for a beginner?',
         'o': ['Every platform at once', 'One main, one support, plus WhatsApp for conversations', 'Only X', 'None until you have 1,000 followers'],
         'a': 'B', 'why': 'Going deep before wide protects quality and your time.'},
        {'q': 'What is true about Telegram channels?',
         'o': ['They are limited to 256 members', 'They can have unlimited subscribers', 'They are banned in India', 'They show only the last post'],
         'a': 'B', 'why': 'Telegram\'s FAQ says channels can have unlimited subscribers.'},
        {'q': 'Why shouldn\'t a Kerala business plan its marketing around TikTok?',
         'o': ['It\'s too expensive', 'It has been blocked in India since June 2020', 'It has no videos', 'It only works in Malayalam'],
         'a': 'B', 'why': 'TikTok was among 59 apps blocked in June 2020.'},
        {'q': 'For a freelancer\'s career on LinkedIn, what matters most at first?',
         'o': ['A company Page with no posts', 'A complete personal profile with an honest headline and Featured work', 'Thousands of connections', 'A paid subscription'],
         'a': 'B', 'why': 'Clients and employers look at your personal profile and proof.'},
    ],
    study='LinkedIn, Threads, Telegram, X and Indian platform sources (about 40 minutes)',
    action='choose your platform mix with the matrix and set up your LinkedIn career profile',
)

LESSONS = [L1, L2, L3, L4]

MODULE = module(
    3,
    title='Platforms in depth',
    weeks=(5, 7), hours=14,
    overview="""
Learn what each platform is for and its current rules, optimise every profile you'll use, and choose a platform mix you can keep up.

Platforms differ in who uses them, what formats they reward and how people find content. In three weeks you'll go deep on Instagram, YouTube, Facebook and WhatsApp Business, then look at LinkedIn, X, Threads, Telegram and Indian apps, and choose one main and one support platform for your page. Every platform fact is dated, because they change.

From week 5 you post three times a week. By the end of week 7 your profiles are optimised and your platform plan is written.
""",
    outcomes=[
        'Use Instagram Reels, trial reels, carousels and Stories for the right jobs',
        'Set up a YouTube channel and plan Shorts and long videos',
        'Run WhatsApp Business with a catalogue, quick replies, labels, Status and Channels',
        'Use Facebook Pages and local Groups within their rules',
        'Choose a platform mix with a scored matrix and set up a LinkedIn career profile',
    ],
    lessons=LESSONS,
    project='Your platform plan and optimised profiles',
    project_steps=[
        'Put before and after screenshots of every profile you optimised (Instagram, YouTube, WhatsApp Business, Facebook if used, LinkedIn) in 03 Platforms.',
        'Write a one-page platform plan: main and support platforms and why, posts a week on each, which formats, and how one post becomes several (you\'ll refine this in Module 6).',
        'Add your rules for each platform: hashtag count, music source, caption language, posting days.',
        'Check every bio, link and phone number works by opening them from another phone.',
    ],
    project_proof='Before and after screenshots of each profile and your one-page platform plan.',
    rubric=[
        ('Instagram', 'Profile unclear', 'Some fields optimised', 'Every checklist item done; Reel, carousel and Stories posted'),
        ('YouTube', 'No channel', 'Channel without description or verification', 'Verified, described, first Short live, long video planned'),
        ('WhatsApp Business', 'Not installed', 'Profile only', 'Profile, catalogue, quick replies, labels and Status working'),
        ('Platform choice', 'Posting everywhere at random', 'A choice without reasons', 'A scored matrix with one main and one support platform'),
        ('Rules and accuracy', 'Unaware of current limits', 'Knows some', 'Knows and follows current limits, with dates, and checks them'),
    ],
    short=[
        'Optimise only your Instagram profile and post one Reel.',
        'Set up the YouTube channel basics and post one Short; skip the long-video plan.',
        'Set up the WhatsApp Business profile and two quick replies.',
        'Fill in the platform matrix for your own account only.',
    ],
    flashcards=[
        ('Longest Instagram Reel that can be recommended to non-followers?', '3 minutes (as of October 2026).'),
        ('Maximum items in an Instagram carousel?', '20 photos or videos.'),
        ('Hashtag limit in an Instagram caption since December 2025?', 'Five.'),
        ('What does a trial reel do?', 'Shows a reel to non-followers first so you can test it, with results after about 24 hours.'),
        ('YouTube Shorts: maximum length and shape?', 'Up to 3 minutes, square or vertical (uploads since 15 October 2024).'),
        ('What happens to a Short over 1 minute with an active Content ID claim?', 'It is blocked worldwide until the claim is resolved.'),
        ('YouTube first Partner Program level in India?', '500 subscribers, 3 uploads in 90 days, and 3,000 watch hours in 12 months or 3 million Shorts views in 90 days.'),
        ('Can WhatsApp Channel followers reply?', 'No: they can react with emoji or vote in polls.'),
        ('A beginner\'s platform mix?', 'One main, one support, plus WhatsApp for conversations.'),
        ('TikTok in India?', 'Blocked since June 2020.'),
    ],
    mistakes=[
        ('Optimising once and forgetting.', 'Check your profiles every month; links break and hours change.'),
        ('Using one video file everywhere without adjusting.', 'Same idea, but check shape, length, music and captions for each platform.'),
        ('Ignoring WhatsApp because it isn\'t "social media".', 'For local business it is where most sales happen.'),
    ],
    fulltime='When you finish this module, your growth project starts: every day of posting from now on counts towards it. Read SMM-M17-L01 now and set your growth target, then carry on with Module 4.',
)
