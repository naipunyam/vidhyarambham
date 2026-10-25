from common import lesson, module, link, ASOF

L1 = lesson(
    5, 1,
    title='Headlines, hooks and captions that get read',
    weeks=(12, 12), hours=2.5,
    outcome='Write first lines and headlines that make people read on, and captions that are easy to read on a phone, using six reusable caption formulas in Malayalam and English.',
    split='40 minutes study, 1 hour 50 minutes action',
    core="""
### The first line is the headline

On most platforms people see only the start of your words before they decide: the first line of an Instagram or Facebook caption before "more", the title of a YouTube video, the opening of a LinkedIn post, the on-screen text of a Reel. Treat that line as a headline. It has two jobs: **make the right person want to read on**, and **carry the keyword** they would search for.

Weak: "Today we visited a very nice place in our town and had a great time."
Strong: "Kuttiady's ₹60 meals with 9 curries (yes, really)"

### Headline formulas

Formulas aren't cheating; they are patterns that have worked for decades. Fill them with true, specific details:

| Formula | Example |
| --- | --- |
| How to [result] without [pain] | How to keep cream cakes fresh without a big fridge |
| [Number] [things] for [audience] | 5 phone habits that kill your battery |
| Stop [mistake] | Stop charging your phone overnight like this |
| Why [surprising fact] | Why this shop still sells soda in glass bottles |
| [Result] in [time] | A neat wardrobe in 15 minutes |
| [Place] people, [news] | Kuttiady people, the new bus timings are out |
| I tried [x] so you don't have to | I tried every chaya near the bus stand |
| The [specific] guide to [topic] | The honest monsoon packing list for Kakkayam |

### Make captions easy to read on a phone

- **Short lines** and blank lines between ideas. A wall of text gets skipped.
- **Simple words:** write like you speak to a neighbour.
- **Specific details:** prices (₹650), times (6 pm), places (near the bus stand), numbers. Specific feels true; vague feels like an ad.
- **One idea per caption.** If you have three ideas, you have three posts.
- **Emojis as signposts,** not decoration: one at the start of a list item is enough.
- **Keywords in the text**, written naturally, so search can find you. At most five specific hashtags at the end.

### Six caption formulas

1. **Hook – story – CTA:** the first line hooks, three to five lines tell the story, one line asks for action.
2. **Hook – 3 points – CTA:** best for tips and carousels.
3. **AIDA:** Attention (hook), Interest (a surprising detail), Desire (what they get), Action (what to do).
4. **PAS:** Problem, Agitate (why it matters), Solution. Keep the agitation gentle and true; don't scare people.
5. **BAB:** Before, After, Bridge (how to get from one to the other).
6. **FAQ caption:** the three questions people always ask, answered in one post.

### Length: match the format

- **Reels and Shorts:** the video does the work; one to three lines plus the CTA.
- **Carousels and photo stories:** longer captions are fine if every line earns its place.
- **LinkedIn and Threads:** the text is the post; hook in the first line, short paragraphs.

### Proof in every caption

Add one piece of proof whenever you can: a number, a real customer quote (with permission), a fact you checked, years of experience. Proof turns a claim into something people believe.
""",
    example="""
Peak Fitness's original caption under a Reel of a trainer correcting a squat:

"Come and join Peak Fitness!!! Best gym in Vatakara with all facilities. Contact now. #gym #fitness #workout #motivation #viral #explore #reels #fit #health #instagood"

Rewritten with Hook – 3 points – CTA:

"Your knees hurt after squats? It's probably this. 👇

1️⃣ Knees caving in: push them out over your toes
2️⃣ Heels lifting: sit back, weight on your heels
3️⃣ Going too low too soon: start with a box behind you

Beginners' batch, 6–8 am, first session free. WhatsApp 'SQUAT' to 9XXXXXXXXX.

#vatakara #vatakaragym #kozhikodefitness #beginnerworkout"

Same video. The new caption was saved four times as often, and nine people sent "SQUAT" on WhatsApp in the first week.

(Made-up example to show the method.)
""",
    resources=[
        ('gads-copy', 'Read Google\'s advice on genuine copy: user benefits, specific calls to action, earned urgency', '10 min'),
        ('hubspot-social', 'Watch the lesson on social content (lesson names may change)', '20 min'),
        ('ig-reco', 'Re-read the tip on keywords and hashtags in captions', '5 min'),
    ],
    steps=[
        'Study the resources (about 35 minutes).',
        'Take your 5 most recent captions. Rewrite each first line with a headline formula, and each body with one of the six caption formulas.',
        'Write 10 new headlines from the formula table for your coming posts.',
        'Publish two posts this week with the new captions, and log them.',
        'After 7 days, compare saves, shares and replies with your older posts.',
    ],
    proof='Your 5 before-and-after captions, 10 new headlines and links to the 2 published posts with their Posting Log rows.',
    templates=[
        ('caption formulas', """
HOOK - STORY - CTA
  Line 1: [hook with keyword]
  Lines 2-5: [what happened, specific details]
  Last line: [one action]

HOOK - 3 POINTS - CTA
  Line 1: [problem or promise]
  1. ______  2. ______  3. ______
  Last line: [save / share / WhatsApp keyword]

AIDA: Attention ____ / Interest ____ /
      Desire ____ / Action ____
PAS:  Problem ____ / Agitate (true, gentle) ____ /
      Solution ____
BAB:  Before ____ / After ____ / Bridge ____
FAQ:  Q1 ____ A1 ____ / Q2 ____ A2 ____ /
      Q3 ____ A3 ____ / CTA ____
""", ''),
        ('caption check before posting', """
[ ] First line works alone as a headline
[ ] The keyword someone would search is in the text
[ ] Short lines, blank lines between ideas
[ ] At least one specific detail (Rs, time, place, number)
[ ] One idea only
[ ] One clear call to action
[ ] Max 5 specific hashtags
[ ] Read aloud once: sounds like me (voice chart)
""", ''),
    ],
    mistakes=[
        ('Starting with "Hello friends" or the date.', 'Start with the most interesting line.'),
        ('Walls of text.', 'Break it into short lines; delete anything that doesn\'t add.'),
        ('"Best in Kerala!!!"', 'Unprovable superlatives sound like ads and can mislead. Use specific, true details.'),
        ('Ten generic hashtags.', 'Five specific ones; and remember Instagram now allows only five.'),
    ],
    quiz=[
        {'q': 'Which first line is strongest?',
         'o': ['"Today we visited a nice place"', '"Kuttiady\'s ₹60 meals with 9 curries (yes, really)"', '"Hello friends"', '"Please like and share"'],
         'a': 'B', 'why': 'It is specific, local and makes you want to read on.'},
        {'q': 'What does PAS stand for?',
         'o': ['Post, Add, Share', 'Problem, Agitate, Solution', 'Price, Ask, Sell', 'Photo, Audio, Story'],
         'a': 'B', 'why': 'Keep the agitation gentle and true.'},
        {'q': 'Why include specific details such as ₹650 or 6 pm?',
         'o': ['They make posts longer', 'Specific details feel true and answer questions before people ask', 'Platforms require numbers', 'They replace the call to action'],
         'a': 'B', 'why': 'Specificity builds belief and saves a message.'},
    ],
    study='Google\'s guide to genuine copy, HubSpot\'s content lesson and Instagram\'s caption tips (about 35 minutes)',
    action='rewrite 5 captions, write 10 headlines and publish 2 posts with the new captions',
)

L2 = lesson(
    5, 2,
    title='Calls to action and persuasion without hype',
    weeks=(12, 12), hours=2.5,
    outcome='Write clear calls to action for each funnel stage, and persuade with honest proof, real reasons and true urgency, staying within Indian advertising rules.',
    split='40 minutes study, 1 hour 50 minutes action',
    core="""
### A call to action is one clear next step

Every post should end with exactly one thing to do, matched to its job in the funnel (SMM-M01-L02):

| Funnel job | Good calls to action |
| --- | --- |
| Awareness | "Send this to someone who loves biryani", "Follow for one food spot every Friday" |
| Consideration | "Save this for your next trip", "Comment your question, we'll answer in the next post" |
| Conversion | "WhatsApp 'CAKE' to 9XXXXXXXXX", "Book on the link in bio", "Visit before 8 pm today" |
| Loyalty | "Join our WhatsApp Channel for weekly specials" |
| Advocacy | "Tag the friend who came with you", "Leave us a Google review: link in bio" |

Make it **specific** ("WhatsApp 'SQUAT'" beats "contact us"), **easy** (one tap: a WhatsApp link or button), and **worth it for them** ("get the price list", not "message us"). Google's own advice for ads makes the same point: generic calls to action such as "sign up today" or "call us today" don't tell people what they get.

### Honest persuasion

People decide with feelings and check with facts. These principles work and are fair:

- **Proof:** real reviews and messages shared with permission, photos of real work, numbers you can show.
- **Authority:** say why you know: "baking since 2014", "certified trainer", "we visited and paid for our own meal".
- **Usefulness first:** helpful posts earn the right to make an offer.
- **Clarity:** show the price, the size, the delivery area and the timing. Hiding the price feels like a trick.
- **Real urgency:** "Onam orders close on Thursday because we bake by hand" is true and useful. Google's advice is to make any urgency "earned and valued".
- **Risk reversal you can honour:** "If the cake isn't right, we'll make it again", only if you will.

### What hype looks like, and why it's dangerous

- **Superlatives you can't prove:** "best", "No. 1", "100% guaranteed".
- **Fake urgency and scarcity:** "Only 2 left!" every day; countdown timers that restart. India's Central Consumer Protection Authority lists **false urgency** and **disguised advertisements** among the dark patterns it banned in 2023 (SMM-M14-L03).
- **Health, money and miracle claims:** "lose 10 kg in 10 days", "guaranteed returns". These can be misleading advertisements, and ASCI's guidelines expect health and finance advice to come from qualified people (SMM-M14-L01).
- **Fake reviews and testimonials.**
- **Before-and-after photos** that are edited or not typical.

Under the Consumer Protection Act, the CCPA can fine a manufacturer or an endorser up to ₹10 lakh for a false or misleading advertisement, and up to ₹50 lakh for repeat offences, and the 2022 guidelines expect endorsements to reflect a genuine, current opinion based on real experience (check current rules). That applies to you when you write ads or posts for clients.

### Engagement bait isn't a call to action

"Comment YES if you agree", "Like for part 2", "Tag 5 friends to win" ask for empty actions to trick the feed. Meta's content distribution guidelines include a policy on **engagement bait**, and Facebook has demoted such posts for years. Ask for actions that mean something: a real question, a save, a share with a reason.
""",
    example="""
**Kakkayam Hills Homestay** wrote two versions of its monsoon offer.

Hype version: "🔥🔥 BEST homestay in Kerala!!! Only 1 room left!!! Book NOW before it's gone!!! 100% satisfaction guaranteed!!!" They had three empty rooms, so "only 1 room left" was false, and "best in Kerala" couldn't be proved.

Honest version: "Monsoon weekends, 3 rooms only. Mist from the balcony at 7 am, Kerala breakfast included, ₹2,500 a night for two. We have just 3 rooms, so weekends usually fill first: check dates on WhatsApp ('MONSOON' to 9XXXXXXXXX). Free cancellation until 3 days before."

The honest version got fewer likes but more WhatsApp chats, and none of the guests complained that the place didn't match the post.

(Made-up example to show the method.)
""",
    resources=[
        ('gads-copy', 'Re-read the parts on specific calls to action and earned urgency', '5 min'),
        ('pib-misleading', 'Read what the misleading advertisement guidelines expect from endorsers, and the penalties', '10 min'),
        ('pib-dark', 'Read the press release on the 13 dark patterns', '10 min'),
        ('meta-ebait', 'Open the page; read it in full in a browser if you can', '5 min'),
    ],
    steps=[
        'Study the resources (about 30 minutes).',
        'Write a CTA bank: at least 3 calls to action for each of the five funnel stages, in English and Malayalam, and add them to the Hooks and Captions tab.',
        'Take one offer (yours or a local business\'s) and write it twice: a hype version and an honest version. Mark every claim in the hype version that you couldn\'t prove.',
        'Make a WhatsApp click-to-chat link for your page or a client (wa.me/ followed by 91 and the number) and put it in a post with a keyword CTA.',
        'Publish two posts this week with specific, honest CTAs, and count the actions they bring.',
    ],
    proof='Your CTA bank, your hype-versus-honest pair with the unprovable claims marked, and links to the 2 posts with the actions they brought.',
    templates=[
        ('CTA bank (English and Malayalam)', """
AWARENESS
  Send this to someone who ___ / ___ ഇഷ്ടമുള്ള ഒരാൾക്ക് അയക്കൂ
  Follow for ___ every ___ / എല്ലാ ___ നും ___ കാണാൻ ഫോളോ ചെയ്യൂ
CONSIDERATION
  Save this for later / പിന്നീട് നോക്കാൻ സേവ് ചെയ്യൂ
  Comment your question / സംശയം കമന്റ് ചെയ്യൂ
CONVERSION
  WhatsApp '___' to ___ / '___' എന്ന് വാട്സാപ്പ് ചെയ്യൂ
  Visit before ___ today / ഇന്ന് ___ ന് മുൻപ് വരൂ
LOYALTY
  Join our WhatsApp Channel / വാട്സാപ്പ് ചാനലിൽ ചേരൂ
ADVOCACY
  Tag the friend who came with you / കൂടെ വന്ന സുഹൃത്തിനെ ടാഗ് ചെയ്യൂ
  Leave a Google review (link in bio)
""", ''),
        ('honest persuasion check', """
For every claim in the post:
[ ] Can I prove it today? (photo, review, number)
[ ] Is the price, size, area and timing clear?
[ ] Is any urgency true? (real deadline, real stock)
[ ] No "best / No. 1 / 100% / guaranteed" I can't prove
[ ] No health, weight-loss or money-return promises
[ ] Reviews and photos are real, used with permission
[ ] Before/after photos are unedited and typical
[ ] Paid or gifted? Disclosed clearly (Module 14)
[ ] No engagement bait (like/comment/tag for reach)
""", ''),
    ],
    mistakes=[
        ('Several CTAs in one post.', 'Follow, like, share, DM and visit means people do none. Pick one.'),
        ('"Contact us for details".', 'Give the details, then a specific action with a benefit.'),
        ('Fake scarcity.', 'False urgency is a banned dark pattern and destroys trust.'),
        ('Promising what the client can\'t deliver.', 'Check every claim with the business owner before posting.'),
    ],
    quiz=[
        {'q': 'Which CTA is best for a conversion post?',
         'o': ['"Contact us"', '"WhatsApp \'CAKE\' to 9XXXXXXXXX for today\'s price list"', '"Like and share"', '"Follow for more"'],
         'a': 'B', 'why': 'It is specific, easy and tells people what they get.'},
        {'q': '"Only 2 rooms left!" posted every day when rooms are empty is:',
         'o': ['Good marketing', 'False urgency, a dark pattern banned in India in 2023', 'Required by Instagram', 'An honest CTA'],
         'a': 'B', 'why': 'The CCPA\'s dark patterns guidelines list false urgency.'},
        {'q': 'What maximum penalty can the CCPA impose on an endorser for a false or misleading advertisement (first offence)?',
         'o': ['₹10,000', '₹1 lakh', '₹10 lakh', 'No penalty'],
         'a': 'C', 'why': 'Up to ₹10 lakh, and up to ₹50 lakh for repeat offences (check current rules).'},
        {'q': '"Comment YES if you agree!" written only to boost reach is:',
         'o': ['A strong CTA', 'Engagement bait, which Meta demotes', 'Required for growth', 'A legal disclosure'],
         'a': 'B', 'why': 'Ask for meaningful actions instead.'},
    ],
    study='Google\'s ad copy advice, the CCPA misleading-ads and dark-patterns releases and Meta\'s engagement bait page (about 30 minutes)',
    action='build a CTA bank, write a hype-versus-honest offer and post 2 honest CTAs',
)

L3 = lesson(
    5, 3,
    title='Writing for each platform: bios, posts, titles and messages',
    weeks=(13, 13), hours=2.5,
    outcome='Adapt one message to Instagram, YouTube, Facebook, LinkedIn, Threads, WhatsApp and Google Business Profile, using the format, length and tone each one rewards.',
    split='30 minutes study, 2 hours action',
    core=f"""
### Same message, different shapes

People use each platform in a different mood, so the same idea needs different words. Here is how one idea, "Nisha's Oven now makes eggless cakes", changes:

| Platform | What to write | Example |
| --- | --- | --- |
| **Instagram Reel** | On-screen hook (3–7 words), a 1–3 line caption, keyword, max 5 hashtags | "Eggless. You won't believe it." / "Eggless chocolate cake, Kuttiady. ₹650 for 1 kg. WhatsApp 'CAKE' 👇" |
| **Instagram carousel** | Cover headline, one idea per slide, a longer caption that adds detail | "5 eggless cakes we bake every day" |
| **YouTube Short title** | The search phrase first, short enough to read in the feed | "Eggless chocolate cake, Malayalam recipe tip" |
| **YouTube long video** | Title with the search phrase; description's first 2 lines say what viewers get; chapters; links | "Eggless chocolate cake without an oven? (Malayalam)" |
| **Facebook Page or group** | Conversational, a little longer, a real question for comments | "Many of you asked for eggless cakes for your parents. Which flavour should we add next?" |
| **LinkedIn** | A professional lesson or result, short paragraphs, no hashtag walls | (For your own profile:) "What I learned helping a home bakery get 30 WhatsApp orders a month" |
| **Threads** | One thought or question that starts a conversation | "Eggless cakes: hit or miss? Honest opinions welcome." |
| **WhatsApp Status** | One photo or short video, one line | "Fresh eggless batch today 🎂 order by 6 pm" |
| **WhatsApp Channel or broadcast** | Personal, short, one CTA, how to stop | "Hi from Nisha's Oven! Eggless cakes are now daily. Reply STOP to stop these messages." (Channels can't receive replies, so give a number to WhatsApp instead.) |
| **Google Business Profile post** | An update, offer or event, with a button | "Eggless cakes now available daily. Order: call or WhatsApp." |

### YouTube titles and descriptions

YouTube's search looks at how well the **title, description, tags and the video itself** match a search ({ASOF}). So:

- Put the words people actually search near the start of the title, in the language they search in.
- Use the first two lines of the description to say what viewers get; YouTube shows only the start before "more".
- Add **chapters** for long videos: timestamps in the description, starting at 00:00, at least three, each at least 10 seconds long.
- Up to three hashtags from the description can show above the title; don't use unrelated hashtags.

### Messages and replies

Quick, warm replies turn interest into customers. Reply to comments within a few hours, answer the actual question, and move private details (phone numbers, addresses, payments) to WhatsApp or DMs. Save your best replies as templates.

### Bios are copy too

Each platform's bio should say who it's for, what they get and what to do, in the space that platform allows (SMM-M03-L01 has the formula).
""",
    example="""
Anu turned one visit, a new juice shop in Kuttiady, into posts for four places:

- **Reel** (main): hook "₹40 fresh juice, no sugar added?" + 25 seconds of the shop + caption "New juice shop near Kuttiady bus stand: ₹40 seasonal juices, no sugar unless you ask. Open 10–9, closed Fridays. 📍 tagged."
- **YouTube Short:** the same video file; title "₹40 fresh juice in Kuttiady (no sugar)".
- **WhatsApp Channel:** "New spot: ₹40 juices near the bus stand, no sugar unless you ask. Video on Instagram: [link]."
- **Threads:** "What's your go-to juice in summer? Found a ₹40 place that doesn't add sugar."

Total extra time after the Reel: about 12 minutes. The Channel post brought 40 people to the Reel within an hour.

(Made-up example to show the method.)
""",
    resources=[
        ('yt-search', 'Re-read the relevance section: titles, descriptions and tags', '5 min'),
        ('yt-chapters', 'Read the rules for chapters', '5 min'),
        ('yt-hashtags', 'Read the rules for hashtags on YouTube', '5 min'),
        ('li-pages', 'Re-read the content tips (documents, images, hashtags)', '5 min'),
        ('gbp-start', 'Read what you can add to a Business Profile', '5 min'),
    ],
    steps=[
        'Study the resources (about 25 minutes).',
        'Choose one strong idea from your Ideas tab and write it for five places using the table: a Reel caption, a YouTube title and description, a WhatsApp Channel or Status line, a Threads or Facebook post, and a LinkedIn post about what you learned making it.',
        'Write 5 reply templates for common comments and DMs (price, location, timing, complaint, thank you).',
        'Publish at least three of the versions this week and log them separately.',
    ],
    proof='Your five platform versions of one idea, your 5 reply templates and the links to the published versions.',
    templates=[
        ('one idea, five places', """
IDEA: ______________________________
INSTAGRAM: on-screen hook ___________
           caption (1-3 lines + CTA + 5 tags) ____
YOUTUBE:   title (search phrase first) _________
           description line 1 ____ line 2 ____
           chapters (long videos) 00:00 ____
WHATSAPP:  Status line ____ / Channel post ____
FACEBOOK or THREADS: question or thought ____
LINKEDIN:  what I learned + one number ________
""", ''),
        ('reply templates', """
PRICE:     Thanks for asking! It's ₹___ for ___. WhatsApp ___ to order.
LOCATION:  We're at ___ (pinned in the post). Open ___ to ___.
TIMING:    Yes, open on ___ from ___ to ___. See you!
COMPLAINT: Sorry about this. Please WhatsApp ___ so we can fix it today.
THANK YOU: Thank you so much! Can we share your message? 🙏
(Malayalam versions in the Hooks and Captions tab)
""", ''),
    ],
    mistakes=[
        ('Copy-pasting the same caption everywhere.', 'Keep the idea, change the words for each platform\'s mood and format.'),
        ('Keyword-stuffed YouTube titles.', 'One natural search phrase near the start, then a reason to click.'),
        ('Arguing in public replies.', 'Acknowledge, then move the conversation to WhatsApp or DMs (SMM-M14-L04).'),
        ('Broadcasts with no way to stop.', 'Always say how to opt out, and respect it.'),
    ],
    quiz=[
        {'q': 'Where should the search phrase go in a YouTube title?',
         'o': ['At the end, hidden', 'Near the start, in the words people actually search', 'Only in tags', 'Nowhere'],
         'a': 'B', 'why': 'Search compares titles, descriptions and the video with the query.'},
        {'q': 'What are the rules for YouTube chapters?',
         'o': ['Any order, any length', 'Start at 00:00, at least three timestamps, each chapter at least 10 seconds', 'Only for Shorts', 'Only paid channels'],
         'a': 'B', 'why': 'That is what YouTube Help requires.'},
        {'q': 'Why should a WhatsApp Channel post give a number to message?',
         'o': ['Channels are illegal', 'Channel followers can\'t reply to updates', 'It looks longer', 'Numbers are required'],
         'a': 'B', 'why': 'Channels are one-way; give another way to reach you.'},
    ],
    study='YouTube\'s search, chapters and hashtag rules, LinkedIn\'s content tips and Google Business Profile basics (about 25 minutes)',
    action='write one idea for five platforms, make 5 reply templates and publish at least three versions',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    5,
    title='Copywriting',
    weeks=(12, 13), hours=9.5,
    overview="""
Write words that make people stop, read, believe and act: headlines, captions, calls to action and platform-specific copy, persuasive without hype.

Good copy is clear, specific and honest. In two weeks you'll learn headline and caption formulas, write calls to action for every stage of the funnel, practise honest persuasion inside Indian advertising rules, and adapt one idea to every platform you use.

The module ends with a caption bank for your 30-day challenge, so that when the challenge starts in week 14 you're never stuck for words.
""",
    outcomes=[
        'Write first lines that work as headlines and carry keywords',
        'Use six caption formulas in English and Malayalam',
        'Write specific calls to action for each funnel stage',
        'Persuade honestly, avoiding hype, false urgency and engagement bait',
        'Adapt one idea to Instagram, YouTube, WhatsApp, Facebook, LinkedIn, Threads and Google Business Profile',
    ],
    lessons=LESSONS,
    project='A caption bank for your 30-day challenge',
    project_steps=[
        'Plan the topics for the 30 days of your challenge (you\'ll finalise the calendar in SMM-M06-L01): at least 6 per pillar.',
        'For each day, write a headline or on-screen hook and a caption using one of the six formulas. Use at least four different formulas across the 30.',
        'Add one specific call to action to each, matched to the post\'s funnel job.',
        'Check all 30 with the honest persuasion check and the caption check.',
        'Keep them in the Hooks and Captions tab, marked by day.',
    ],
    project_proof='The Hooks and Captions tab with 30 hooks and captions, each with a CTA, marked by challenge day.',
    rubric=[
        ('Headlines', 'First lines are greetings or dates', 'Some strong first lines', 'Every first line works alone and carries a keyword'),
        ('Caption craft', 'Walls of text', 'Readable, sometimes vague', 'Short lines, specific details, one idea, the right formula'),
        ('Calls to action', 'None or several at once', 'Generic CTAs', 'One specific, easy CTA matched to the funnel stage'),
        ('Honesty and rules', 'Hype and false urgency', 'Mostly honest', 'Every claim provable; no dark patterns or engagement bait'),
        ('Platform fit', 'Same text everywhere', 'Some adaptation', 'Each platform gets the right format, length and tone'),
    ],
    short=[
        'Rewrite 3 captions with formulas and post one.',
        'Write a CTA bank with one CTA per funnel stage.',
        'Adapt one idea to two platforms.',
        'Write 15 challenge hooks (captions can be written during the challenge).',
    ],
    flashcards=[
        ('Two jobs of a caption\'s first line?', 'Make the right person read on, and carry the search keyword.'),
        ('What do AIDA and PAS stand for?', 'Attention, Interest, Desire, Action; Problem, Agitate, Solution.'),
        ('Three qualities of a good CTA?', 'Specific, easy (one tap) and worth it for the person.'),
        ('Google\'s rule for urgency in ads?', 'Make any urgency earned and valued.'),
        ('Two dark patterns banned in India in 2023 that copywriters must avoid?', 'False urgency and disguised advertisements.'),
        ('Maximum CCPA penalty for a misleading ad, first and repeat?', 'Up to ₹10 lakh; up to ₹50 lakh for repeats.'),
        ('What is engagement bait?', 'Posts that ask for likes, comments, shares, tags or votes just to boost reach; Meta demotes it.'),
        ('Where does YouTube look to match a search?', 'Title, description, tags and the video itself.'),
    ],
    mistakes=[
        ('Writing for yourself, not the reader.', 'Every line should answer "why should they care?"'),
        ('Hype to make up for weak content.', 'Fix the content; keep the words honest.'),
        ('Never testing copy.', 'Change one thing at a time (the first line, the CTA) and compare results.'),
    ],
)
