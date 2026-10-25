from common import lesson, module, link, ASOF

L1 = lesson(
    7, 1,
    title='Social SEO: keywords, hashtags and YouTube search',
    weeks=(16, 16), hours=2.5,
    outcome='Find the words your audience types into search, and put them where Instagram, YouTube and Google look: handles, names, bios, captions, titles, descriptions, chapters, alt text and a few specific hashtags.',
    split='40 minutes study, 1 hour 50 minutes action',
    core=f"""
### People search social apps too

Recommendations bring people who weren't looking for you. **Search** brings people who are: "biryani near Kuttiady", "phone screen guard price", "PSC Kerala history questions Malayalam". These viewers already want what you offer, and search keeps sending them to good posts for months. **Social SEO** (search engine optimisation) means making your posts easy to find in that search.

### Find the words people really use

1. **Your audience's own words:** the questions in your comment mining sheet (SMM-M02-L02) and in DMs.
2. **Search suggestions:** start typing your topic in YouTube, Instagram and Google search and note the suggestions that appear.
3. **Google Trends:** compare candidate terms for Kerala, and switch to **YouTube Search** to see video interest. Remember the numbers are relative interest, not counts.
4. **Spelling and language variants:** people search "kuttiady", "kuttiadi", "കുറ്റ്യാടി"; "biriyani" and "biryani". Note which ones appear in suggestions.

Choose one **main keyword** per post (what it's mostly about) and one or two related ones.

### Where Instagram looks ({ASOF})

Instagram's tips for creators say to put keywords in your **handle, profile name, bio and captions**, and to put keywords and hashtags in the caption rather than in the comments. Its search matches usernames, bios, captions, hashtags and places. So:

- **Name field and bio:** your niche and place ("Kuttiady | Food, shops, local news").
- **Caption:** the main keyword in the first line, written naturally ("New juice shop near Kuttiady bus stand").
- **Location tag:** tag the real place on posts about places.
- **Alt text:** for photos, write a short description in the post's accessibility settings; it helps people who use screen readers and describes the image in words.
- **Hashtags:** at most five, specific and relevant: place (#kuttiady #kozhikode), niche (#kozhikodefood) and community (#kudumbashree). Instagram says fewer, targeted hashtags work better than generic ones such as #reels.

### Where YouTube looks

YouTube's search ranks by **relevance** (how well the title, description, tags and the video's content match the search), **engagement** (for example, watch time for that search) and **quality** (signs of expertise, authority and trust). Practical steps:

- **Title:** the search phrase near the start, in the language people search, then a reason to click.
- **Description:** first two lines say what viewers get, using the keyword naturally; then details, links and chapters.
- **Chapters** for long videos (timestamps from 00:00, at least three, each at least 10 seconds).
- **Captions and subtitles:** correct ones make your video understandable to more people (SMM-M04-L02).
- **Hashtags:** in the title or description; up to three appear above the title. YouTube ignores all hashtags on a video with more than 60, and unrelated hashtags can get a video removed from search.
- **Playlists** that group videos on one topic help viewers keep watching.

YouTube says it doesn't accept payment for better placement in organic search. The only route is relevance, engagement and quality.

### Don't stuff

Repeating a keyword ten times, or adding unrelated popular hashtags, makes posts harder to read and can break platform rules. Write for people first; keywords should appear where a human would naturally use them.
""",
    example="""
Riyas at **Malabar Mobiles** wanted more repair customers. Anu listened to his customers and checked search suggestions: people typed "screen guard price", "mobile display change Kuttiady" and "phone battery replacement near me". In Google Trends for Kerala, "mobile display" had more interest than "phone screen".

They changed:

- Name field: "Malabar Mobiles | Phone repair Kuttiady"
- First caption lines: "Mobile display change in Kuttiady: ₹ price for common models 👇"
- Hashtags (five): #kuttiady #kuttiadymobiles #mobilerepair #kozhikode #screenguard
- A YouTube video "Mobile display change price in Kuttiady (Malayalam)" with chapters for three common models.

Within two months, their video was getting views from YouTube search every day, and the shop asked every repair customer how they found them: "YouTube search" came up about once a week.

(Made-up example to show the method.)
""",
    resources=[
        ('ig-reco', 'Re-read "Optimize for Search": keywords in handle, name, bio and captions', '5 min'),
        ('sel-ig-ranking', 'Re-read how Instagram search matches queries', '5 min'),
        ('yt-search', 'Re-read relevance, engagement and quality', '5 min'),
        ('yt-hashtags', 'Read the hashtag rules, including the 60-hashtag limit', '5 min'),
        ('ss-hashtags', 'Re-read why Instagram moved to five hashtags', '3 min'),
        ('gtrends-start', 'Re-read how to compare terms and switch to YouTube Search', '5 min'),
    ],
    steps=[
        'Study the resources (about 30 minutes).',
        'Build a list of 20 keywords for your niche from four sources: comments and DMs, search suggestions on YouTube and Instagram, Google Trends (Kerala, web and YouTube), and spelling variants.',
        'Make three hashtag sets of five each (place, niche, community) and save them in your template library.',
        'Optimise 5 challenge posts: keyword in the first caption line, location tag, alt text on photos, one hashtag set.',
        'Publish one YouTube video or Short with an optimised title, description and (for long videos) chapters.',
        'Note in the Experiments tab which posts had keywords, so you can compare their search traffic later in Module 8.',
    ],
    proof='Your 20-keyword list with sources, your three hashtag sets, and links to the 5 optimised posts and the optimised YouTube upload.',
    templates=[
        ('keyword research sheet', """
Keyword or phrase,Language or spelling,Source (comments/suggestions/Trends),Trends note,Main or related,Used in (post link)
""", 'csv'),
        ('social SEO checklist', """
INSTAGRAM
[ ] Name field: niche + place
[ ] Bio: keywords written naturally
[ ] Caption line 1: main keyword
[ ] Location tagged (posts about places)
[ ] Alt text written for photos
[ ] Max 5 specific hashtags (one saved set)
YOUTUBE
[ ] Title: search phrase near the start
[ ] Description lines 1-2: what viewers get + keyword
[ ] Chapters (long videos): 00:00 first, 3+, 10 s+
[ ] Correct captions or subtitles
[ ] 1-3 relevant hashtags; never unrelated ones
[ ] Added to a topic playlist
""", ''),
    ],
    mistakes=[
        ('Guessing keywords.', 'Use your audience\'s words and search suggestions.'),
        ('Keyword stuffing.', 'Write naturally; one main keyword and one or two related ones.'),
        ('Generic or unrelated hashtags.', 'They don\'t help and, on YouTube, can get a video removed from search.'),
        ('Ignoring spelling variants.', 'Note how people actually spell place names and dishes.'),
    ],
    quiz=[
        {'q': 'Where does Instagram suggest putting keywords for search?',
         'o': ['Only in comments', 'Handle, profile name, bio and captions', 'In your password', 'Only in hashtags'],
         'a': 'B', 'why': 'Those are the places Instagram\'s own tips name.'},
        {'q': 'What happens on YouTube if a video has more than 60 hashtags?',
         'o': ['It goes viral', 'YouTube ignores all of its hashtags', 'It gets a badge', 'Nothing'],
         'a': 'B', 'why': 'YouTube Help says it will ignore each hashtag on that content.'},
        {'q': 'Which three elements does YouTube search prioritise?',
         'o': ['Relevance, engagement and quality', 'Length, colour and price', 'Followers, likes and time', 'Payment, tags and emojis'],
         'a': 'A', 'why': 'YouTube also says it doesn\'t accept payment for organic placement.'},
        {'q': 'A good Instagram hashtag set for a Kuttiady bakery is:',
         'o': ['#reels #viral #explore #love #instagood', '#kuttiady #kuttiadycakes #kozhikodefood #homebakery #eggless', '30 random tags', 'No text at all'],
         'a': 'B', 'why': 'Specific place, niche and community tags.'},
    ],
    study='Instagram\'s and YouTube\'s search guidance, hashtag rules and Google Trends (about 30 minutes)',
    action='build a 20-keyword list and hashtag sets, optimise 5 posts and publish an optimised YouTube upload',
)

L2 = lesson(
    7, 2,
    title='Trends and collaborations',
    weeks=(17, 17), hours=2.5,
    outcome='Spot trends early and use only the ones that fit your niche, with a local twist and licensed audio, and grow faster by collaborating with complementary accounts, disclosing any material connection.',
    split='35 minutes study, 1 hour 55 minutes action',
    core="""
### Four kinds of trends

| Trend | Where to spot it | How to use it |
| --- | --- | --- |
| **Audio** | Sounds you hear repeatedly in the Reels tab and Shorts feed | Use the sound from inside the app (so it's licensed there), with your own local idea |
| **Format** | A structure everyone is copying ("POV", "things that just make sense", "day in my life") | Keep the structure, change the content to your niche |
| **Topic and news** | Local news, Google Trends "Trending now", what people talk about in groups | Only if it fits your niche, after checking facts |
| **Seasonal** | Festivals, monsoon, exams, school reopening | Plan ahead in your calendar (SMM-M06-L01) |

### Use trends that fit, with a twist

A trend helps only if the right people watch. A hyperlocal page joining a format trend with a Kuttiady twist works; a bakery jumping on a national political trend doesn't. Ask three questions:

1. Does it fit my niche and my voice chart?
2. Can I add something local or useful, not just copy?
3. Is it respectful? Never joke about accidents, deaths, disasters or communities.

Speed matters a little; accuracy and taste matter more. For news trends, check with two reliable sources before posting, or don't post.

### Collaborations: borrow trust

Collaborating with another account introduces you to an audience that already trusts them. Options:

- **Instagram Collabs:** a co-authored post that appears on both accounts. Instagram suggests using Collabs or tags when working with other creators, instead of reposting each other's content.
- **Guest appearances:** you appear in their video and they appear in yours, on YouTube or Reels.
- **Complementary local accounts:** a bakery and a florist, a gym and a juice shop, a homestay and a trekking guide.
- **Community pages and groups:** contribute a useful post or a series.
- **Story shout-outs** between friendly accounts in the same area.

The best partners share your audience but don't compete with you, and have a similar size or a little bigger.

### Disclose material connections

If a collaboration involves money, a free product, a discount, a free stay or a family or business relationship, ASCI's guidelines treat it as a **material connection**, even if nobody asked you to promote anything, and the post must carry a clear label such as "Collaboration", "Free gift" or "Ad" where viewers can't miss it. Use the platform's paid partnership label as well when it applies. Module 14 has the full rules; Module 10 covers paid creator work.
""",
    example="""
Anu and Nisha's Oven made a Collab Reel: "Guess the cake flavour blindfolded", filmed in Nisha's kitchen with Anu's cousin as the taster (both agreed to be filmed). Nisha gave them the cakes for free, so the caption started with "Collaboration with @nishasoven (cakes given free)", and the post appeared on both accounts.

| | Anu's page | Nisha's Oven |
| --- | --- | --- |
| Followers before | 1,180 | 2,300 |
| New followers that week | 210 | 160 |
| WhatsApp enquiries mentioning the Reel | — | 14 |

The same week Anu joined an audio trend from the Reels tab with a local twist ("Kuttiady things that just make sense"): 3,900 views, mostly local, and 70 shares.

(Made-up example to show the method.)
""",
    resources=[
        ('ig-reco', 'Re-read the tip on Collabs and tags instead of reposting', '3 min'),
        ('gtrends-start', 'Read about the "Trending now" page', '5 min'),
        ('yt-shorts-guide', 'Re-read how to add sound to a Short', '5 min'),
        ('asci-faqs', 'Read the FAQs on free products, barters and where labels go', '15 min'),
        ('yt-creators', 'In "Grow", read "Engage your community"', '5 min'),
    ],
    steps=[
        'Study the resources (about 35 minutes).',
        'Keep a trend log for 3 days: find 5 trends (audio, format, topic or seasonal) that could fit your niche.',
        'Use 2 of them in challenge posts with a local or useful twist, using in-app audio.',
        'List 5 possible collaboration partners (complementary, similar size, same audience) and send 3 of them a collaboration message.',
        'Make and publish at least one collaboration post (a Collab, a guest appearance or a shout-out swap), with a correct disclosure if there is any material connection.',
    ],
    proof='Your trend log, links to the 2 trend posts, screenshots of your 3 collaboration messages, and the link to your collaboration post showing the disclosure if one was needed.',
    templates=[
        ('trend checklist', """
TREND: ____________  Type: audio / format / topic / seasonal
Where I saw it: ____________  Date: ____
[ ] Fits my niche and voice chart
[ ] I can add a local or useful twist: ___________
[ ] Respectful (no tragedy, no community jokes)
[ ] Facts checked with 2 sources (news trends)
[ ] Audio added inside the app (not downloaded)
Decision: use / skip
""", ''),
        ('collaboration message (English and Malayalam)', """
EN: Hi [name]! I run @[page], a local page about
[niche] in [area] (about [n] followers, mostly local).
I love your [specific post]. Would you like to make a
Collab Reel together, maybe [specific idea]? It would
appear on both our pages. Happy to do it on a day
that suits you.

ML: നമസ്കാരം [പേര്]! ഞാൻ @[page] എന്ന [ഏരിയ]യിലെ ലോക്കൽ പേജ് നടത്തുന്നു.
നിങ്ങളുടെ [പോസ്റ്റ്] വളരെ ഇഷ്ടമായി. നമുക്ക് ഒരുമിച്ച് ഒരു Collab
Reel ചെയ്താലോ? [ആശയം]. രണ്ടു പേജിലും വരും. നിങ്ങൾക്ക്
സൗകര്യമുള്ള ദിവസം ചെയ്യാം.
""", ''),
        ('collaboration agreement checklist', """
[ ] Idea, date and place agreed
[ ] Who films, who edits, who approves the final cut
[ ] Consent from everyone in the video
[ ] Any money, free product, discount or gift?
    -> label "Collaboration" / "Free gift" / "Ad" at the
       start of the caption and on screen (Module 14)
[ ] Collab invite sent and accepted
[ ] Both share in Stories on the day
""", ''),
    ],
    mistakes=[
        ('Jumping on every trend.', 'Use only trends that fit your niche, with a twist.'),
        ('Downloading trending songs.', 'Add trending audio inside the app, where it\'s licensed.'),
        ('Joking about tragedies.', 'Some trends hurt people. Skip them.'),
        ('Hidden free gifts.', 'A free cake or stay is a material connection; label it clearly.'),
        ('Collaborating with competitors only.', 'Look for complementary accounts with the same audience.'),
    ],
    quiz=[
        {'q': 'Which trend use is best for a hyperlocal page?',
         'o': ['A national political argument', 'A format trend with a Kuttiady twist', 'Reposting the original trend video', 'A joke about a recent accident'],
         'a': 'B', 'why': 'It fits the niche, adds something local and is respectful.'},
        {'q': 'A bakery gives you free cakes for a Collab Reel. What must the post include?',
         'o': ['Nothing, it\'s a collaboration', 'A clear label such as "Collaboration" or "Free gift" where viewers can\'t miss it', 'Only a thank-you in the comments', 'Your phone number'],
         'a': 'B', 'why': 'Free products are a material connection under ASCI\'s guidelines.'},
        {'q': 'Who makes the best collaboration partner?',
         'o': ['A direct competitor', 'A complementary account with the same audience and similar size', 'Any huge celebrity', 'A fake account'],
         'a': 'B', 'why': 'Both audiences benefit and nobody loses customers.'},
        {'q': 'How should you add trending audio to a Reel?',
         'o': ['Download it from YouTube', 'Select it inside the app when posting', 'Record it from a speaker', 'Use a film song file'],
         'a': 'B', 'why': 'In-app audio is licensed for use in the app.'},
    ],
    study='Instagram\'s collab tip, Google Trends, YouTube\'s Shorts sound guide and ASCI\'s disclosure FAQs (about 35 minutes)',
    action='log 5 trends and use 2, pitch 3 partners and publish a collaboration post with correct disclosure',
)

L3 = lesson(
    7, 3,
    title='Community, DMs and engagement',
    weeks=(18, 18), hours=2.5,
    outcome='Run a daily engagement routine that turns viewers into a community, handle DMs quickly and kindly, set up moderation filters, and grow without pods, sub4sub or fake engagement.',
    split='30 minutes study, 2 hours action',
    core=f"""
### Small accounts win by talking to people

A big brand can't reply to everyone. You can. Replying to comments, answering questions and remembering regular followers builds a **community**: people who come back, talk to you and each other, and defend you when someone is rude. Communities also send strong signals to platforms: replies, saves, shares and repeat viewers.

### A daily engagement routine (15–20 minutes)

1. **Reply to every comment** on your recent posts, ideally within a few hours. Answer the actual question; ask a follow-up when it's natural.
2. **Pin the most useful comment** on a post, or one that answers a common question.
3. **Comment meaningfully on 5 posts** from accounts in your niche or area: add something, don't just write "Nice 👍".
4. **One Story with a poll or question sticker**, and reply to the answers.
5. **Check DMs and WhatsApp** and move order or payment conversations to WhatsApp Business.

### Places for your community to gather

- **Instagram Stories and Broadcast channels** for your followers
- **WhatsApp Channel** (one-way updates) or a **WhatsApp group or Community** for two-way chat, only with people who chose to join
- **A Facebook Group** if your audience likes discussion
- **YouTube's Posts tab and comment replies**
- **A Telegram channel with a discussion group** for education niches

Start with one; a dead group is worse than none.

### DMs: fast, kind, useful

- Reply within the same day; set a WhatsApp away message for nights.
- Use your reply templates (SMM-M05-L03), then personalise one line.
- Never send unsolicited sales messages to strangers ("cold DMs") in bulk. They get you blocked and reported.

### Moderation tools ({ASOF})

- **Instagram:** **Hidden Words** filters offensive words, phrases and emojis (and likely spam DM requests) into a hidden folder; **Limits** temporarily hides comments and DM requests from people who don't follow you or only recently followed.
- **YouTube Studio** (Settings → Content controls): hold comments for review, block specific words, and hold comments with links or hashtags.

Write simple **house rules** ("Be kind, no hate, no spam, no personal attacks") in a Highlight or pinned post, and apply them calmly. SMM-M14-L04 covers negative comments and crises.

### Growth tricks that break the rules

- **Engagement pods** (groups that like and comment on each other's posts) and **follow-for-follow** fill your account with people who don't care about your content.
- **Sub4sub** (subscribe to me and I'll subscribe to you) is prohibited by YouTube's fake engagement policy, and so is promoting services that inflate views, likes or subscribers.
- **Third-party "growth" apps:** Instagram removes inauthentic likes, follows and comments made by such apps and warns the accounts that use them.

Real engagement grows slower and lasts. Fake engagement can get your account restricted and makes your numbers useless for case studies.
""",
    example="""
Anu set up a 15-minute routine at 8 pm daily and started a WhatsApp Channel, "Kuttiady Diaries updates", linked in her bio. She also began a Story series, "Ask a shop owner": followers send questions and she asks the owners on her visits.

After three weeks:

- Replies per post went from about 2 to 9, and many came from the same regulars.
- 380 people followed the Channel; her Channel posts sent 40–80 people to each new Reel.
- Two shop owners messaged her asking whether she could help them with their own pages: her first warm leads for Module 11.

She turned on Hidden Words and blocked two spam accounts that kept posting "DM for followers".

(Made-up example to show the method.)
""",
    resources=[
        ('ig-abuse', 'Read how Limits and Hidden Words work', '5 min'),
        ('yt-moderation', 'Read the moderation settings in YouTube Studio', '5 min'),
        ('yt-fake', 'Read what YouTube counts as fake engagement, including sub4sub', '10 min'),
        ('ig-inauthentic', 'Read why Instagram removes likes and follows from third-party apps', '5 min'),
        ('wa-channels', 'Re-read how channels work if you plan one', '3 min'),
    ],
    steps=[
        'Study the resources (about 30 minutes).',
        'Run the daily engagement routine for 7 days and log the minutes and replies each day.',
        'Leave 20 meaningful comments on posts in your niche or area over the week.',
        'Turn on Hidden Words on Instagram and the YouTube comment settings that suit you; write house rules in a pinned post or Highlight.',
        'Start one community place (a WhatsApp Channel, a group people choose to join, or a Story series) and add its link to your bio.',
    ],
    proof='Your 7-day engagement log, screenshots of your moderation settings and house rules, and the link to your new community place.',
    templates=[
        ('daily engagement routine log', """
Date,Minutes,Comments replied,Meaningful comments on others,Story poll or question (Y/N),DMs answered,Notes
""", 'csv'),
        ('house rules (English and Malayalam)', """
EN: Welcome! Be kind, disagree politely, no hate, no
    spam, no personal attacks, no fake news. We hide
    or remove comments that break these rules.
ML: സ്വാഗതം! മാന്യമായി പെരുമാറുക, വിയോജിപ്പ് മര്യാദയോടെ മാത്രം.
    വിദ്വേഷം, സ്പാം, വ്യക്തിപരമായ ആക്രമണം, വ്യാജ വാർത്ത
    ഇവ അനുവദനീയമല്ല. ഇത്തരം കമന്റുകൾ മറയ്ക്കുകയോ നീക്കം
    ചെയ്യുകയോ ചെയ്യും.
""", ''),
        ('comment and DM replies that build community', """
QUESTION:   Great question! [answer]. Have you tried ___?
PRAISE:     Thank you, [name]! What should we feature next?
SUGGESTION: Love this idea, adding it to our list 🙌
REGULAR:    [Name], you're always first! 😄 [answer]
ORDER:      Thanks! Please WhatsApp us on ___ and we'll
            sort it in minutes.
""", ''),
    ],
    mistakes=[
        ('Replying with only emojis.', 'Answer the person and, where natural, ask a question back.'),
        ('Joining engagement pods.', 'They inflate numbers without real interest and break the spirit of the rules.'),
        ('Mass cold DMs.', 'They get you blocked and reported. Talk to people who show interest.'),
        ('Starting three community groups at once.', 'Start one and keep it alive.'),
        ('Arguing publicly with rude commenters.', 'Use filters, house rules and calm replies (SMM-M14-L04).'),
    ],
    quiz=[
        {'q': 'What does Instagram\'s Hidden Words do?',
         'o': ['Hides your posts', 'Filters offensive words, phrases and emojis into a hidden folder', 'Deletes your account', 'Translates comments'],
         'a': 'B', 'why': 'It keeps abusive comments and spammy DM requests out of sight.'},
        {'q': 'Is "sub4sub" allowed on YouTube?',
         'o': ['Yes, it\'s encouraged', 'No, YouTube\'s fake engagement policy prohibits it', 'Only for small channels', 'Only on Shorts'],
         'a': 'B', 'why': 'Offering to subscribe back for a subscription is fake engagement.'},
        {'q': 'What is the best daily habit for a small account?',
         'o': ['Buying likes', 'Replying meaningfully to every comment and engaging with others in the niche', 'Posting ten times a day', 'Using a growth app'],
         'a': 'B', 'why': 'Real conversations build a community and send strong signals.'},
        {'q': 'Where should order and payment conversations move to?',
         'o': ['Public comments', 'WhatsApp Business or DMs', 'A Story poll', 'Nowhere'],
         'a': 'B', 'why': 'Keep private details private and use your labels and quick replies.'},
    ],
    study='Instagram\'s and YouTube\'s moderation tools and fake engagement rules (about 30 minutes)',
    action='run a 7-day engagement routine, set moderation filters and house rules, and start one community place',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    7,
    title='Growth',
    weeks=(16, 18), hours=8.5,
    overview="""
Grow with methods that last: social search, smart use of trends, collaborations and a real community, while the 30-day challenge gives you daily posts to test them on.

Growth isn't a trick; it's being findable, timely and worth talking to. In weeks 16–18 you'll research keywords and hashtags and optimise posts for Instagram and YouTube search, use trends with a local twist, collaborate with complementary accounts, and build a daily engagement routine with moderation in place.

Each lesson gives you that week's challenge experiment, so by the end you'll know which growth methods work for your audience.
""",
    outcomes=[
        'Research keywords and optimise posts for Instagram and YouTube search',
        'Use at most five specific hashtags on Instagram and follow YouTube\'s hashtag rules',
        'Use trends that fit, with licensed audio and a local twist',
        'Plan and disclose collaborations correctly',
        'Run a daily engagement routine, moderate comments and start a community space',
    ],
    lessons=LESSONS,
    project='Two growth experiments',
    project_steps=[
        'Choose two experiments from this module, for example keyword captions versus plain captions, or a Collab Reel versus a solo Reel on the same kind of topic.',
        'Write each as a hypothesis in the Experiments tab before you start.',
        'Run each for at least 4 posts per version during the challenge.',
        'Compare the right metric for each (search views, follows, shares, replies) and write a decision.',
    ],
    project_proof='Two completed rows in the Experiments tab, with the post links and the decision for each.',
    rubric=[
        ('Social SEO', 'No keywords', 'Some keywords, guessed', 'Researched keywords used naturally in profiles, captions and YouTube metadata'),
        ('Hashtags', 'Many generic tags', 'Fewer but generic', 'At most five specific tags from saved sets; YouTube rules followed'),
        ('Trends', 'Copies trends blindly or never uses them', 'Some fitting trends', 'Fitting trends with a twist, in-app audio, checked facts'),
        ('Collaborations', 'None', 'Pitched, not done', 'At least one collaboration published with correct disclosure'),
        ('Community', 'Ignores comments', 'Replies sometimes', 'Daily routine, moderation set, a community space running'),
    ],
    short=[
        'Find 10 keywords and make one hashtag set.',
        'Use one trend with a twist.',
        'Pitch one collaboration partner.',
        'Reply to every comment for 7 days; turn on Hidden Words.',
    ],
    flashcards=[
        ('What is social SEO?', 'Making posts easy to find in a platform\'s search with the words people really use.'),
        ('Four sources of keywords?', 'Audience comments and DMs, search suggestions, Google Trends, spelling variants.'),
        ('Instagram hashtag limit and style?', 'At most five, specific and relevant, in the caption.'),
        ('YouTube hashtag limit?', 'More than 60 and YouTube ignores all of them; up to three show above the title.'),
        ('Three questions before using a trend?', 'Does it fit? Can I add a twist? Is it respectful?'),
        ('What counts as a material connection?', 'Money, free products, discounts, gifts, trips, or family and work ties with the brand.'),
        ('What does Limits on Instagram do?', 'Temporarily hides comments and DM requests from non-followers and recent followers.'),
        ('Is sub4sub allowed on YouTube?', 'No: it is fake engagement.'),
    ],
    mistakes=[
        ('Chasing virality instead of the right audience.', 'A thousand local viewers can be worth more than a million random ones.'),
        ('Growth without measurement.', 'Log which method you used on which post, or you\'ll never know what worked.'),
        ('Fake growth to "look bigger" for clients.', 'Clients check, and fake numbers make your case studies worthless.'),
    ],
)
