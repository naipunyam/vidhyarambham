from common import lesson, module, link, ASOF

L1 = lesson(
    6, 1,
    title='Content calendars and batching',
    weeks=(14, 14), hours=2,
    outcome='Plan a month of content around Kerala\'s seasons and your pillars, run it through a simple status workflow, and make a week of posts in one batch session.',
    split='25 minutes study, 1 hour 35 minutes action',
    core="""
### Why a calendar beats inspiration

Posting "when inspired" leads to three posts in one day and nothing for two weeks. A calendar turns your strategy into a schedule you can keep, shows gaps before they happen, and lets you prepare for busy weeks such as exams and festivals.

Plan at three levels:

| Level | What you decide | When |
| --- | --- | --- |
| **Month** | Themes: festivals, seasons, local events, launches | Last Sunday of the previous month |
| **Week** | Which pillar and series goes on which day | Saturday batch session |
| **Day** | The exact post, hook, caption and CTA | In the batch session, or the night before |

### A Kerala content year (check the dates every year)

- **Festivals:** Vishu (April), Onam (August or September), Eid and Ramadan (dates move each year), Christmas, Deepavali, local temple, church and mosque festivals
- **Seasons:** summer heat (March–May), monsoon (June–September), wedding seasons
- **Calendar moments:** school reopening (June), exam results, Gulf holiday travel, new academic year, salary days
- **Local:** your panchayat's events, sports, markets, new shop openings

Festival posts work when they are relevant to the business and to people's lives (an "Onam sadya pre-order" for a caterer), not a generic greeting card from every page.

### A simple status workflow

Every row in your Calendar tab moves through: **idea → scripted → shot → edited → scheduled → posted**. At a glance you can see what's ready and what's stuck. If Wednesday's post is still "idea" on Tuesday night, swap in a ready post from your buffer.

### Batching

Making one post at a time means changing tasks constantly. **Batching** groups similar work:

1. **Plan and script** all of the week's posts in one sitting (30–45 minutes).
2. **Shoot** everything at one location in one trip (45–60 minutes): one shop visit can give you a Reel, a carousel, Stories and a "shop story".
3. **Edit** all the videos in one sitting (45–60 minutes).
4. **Write and schedule** captions (20–30 minutes).

YouTube's own well-being tips for creators suggest batching similar tasks, such as replying to comments, making thumbnails or filming, on the same day.

### Keep a buffer

Always keep **three to five finished posts** ready for weeks when you're ill, travelling or close to an exam. Evergreen posts (tips, "then and now", FAQs) make the best buffer because they don't go out of date.
""",
    example="""
Anu planned her November with three themes: "Monsoon is over: outdoor spots", "Wedding season food", and her series "₹100 Friday" and "Shop story".

Her Saturday batch, about 3 hours:

| Time | Task | Output |
| --- | --- | --- |
| 9:00–9:40 | Script the week from the caption bank | 7 scripts |
| 9:45–11:00 | One trip to Kuttiady town: a bakery, a tailor, a juice shop (all with permission) | Clips for 4 Reels, 1 carousel, Stories |
| 2:00–3:00 | Edit 4 Reels in Edits | 4 videos exported |
| 3:00–3:30 | Captions and scheduling | 5 posts scheduled, 2 in the buffer |

During the week she spent only about 15 minutes a day: replying to comments and posting one Story.

(Made-up example to show the method.)
""",
    resources=[
        ('yt-wellbeing', 'Read the parts on routines and batching similar tasks', '10 min'),
        ('canva-mkt', 'Watch "Organizing and sharing content"', '10 min'),
    ],
    steps=[
        'Study the resources (about 20 minutes).',
        'Write next month\'s themes: festivals, seasons and local events, with dates you have checked.',
        'Fill the Calendar tab for the 30 days of your challenge (it starts this week): date, platform, format, pillar, topic, hook and CTA, using your caption bank from Module 5.',
        'Put two batch sessions a week in your Google Calendar for the next five weeks.',
        'Run your first batch session and get the first 7 days to "edited" or "scheduled". Make 2 extra posts for your buffer.',
    ],
    proof='Your monthly themes, the 30-day Calendar tab and screenshots showing at least 7 posts at "edited" or "scheduled" plus 2 buffer posts.',
    templates=[
        ('monthly theme planner', """
MONTH: ________
Festivals and dates (checked): __________________
Season or weather: ______________________________
Local events: ___________________________________
Business moments (launch, offer, new stock): ____
THEMES (2-3): 1. ________ 2. ________ 3. ________
SERIES this month: "________" every ________
Buffer posts ready: ___ (target 3-5)
""", ''),
        ('weekly batch routine', """
SATURDAY (about 3 hours)
[ ] 30-45 min  plan and script the week
[ ] 45-60 min  shoot at one location (consent!)
[ ] 45-60 min  edit all videos
[ ] 20-30 min  write captions, schedule, update Calendar
WEDNESDAY (about 45 minutes)
[ ] edit or design anything left; top up the buffer
DAILY (10-15 minutes)
[ ] reply to comments and messages
[ ] one Story or Status
[ ] log yesterday's post in the Posting Log
""", ''),
    ],
    mistakes=[
        ('Planning more than you can make.', 'A calendar you can\'t keep is worse than none. Plan for your real hours.'),
        ('No buffer.', 'One bad week breaks the habit. Keep three to five posts ready.'),
        ('Generic festival greetings.', 'Make festival posts useful and relevant to the business, or skip them.'),
        ('Shooting one post per trip.', 'One location visit can give you a week of content.'),
    ],
    quiz=[
        {'q': 'What is batching?',
         'o': ['Posting everything on one day', 'Grouping similar tasks, such as all scripting, then all shooting, then all editing', 'Buying followers in batches', 'Deleting old posts'],
         'a': 'B', 'why': 'It saves time and makes posting consistent.'},
        {'q': 'Why keep a buffer of finished posts?',
         'o': ['To post ten at once', 'So you can keep posting in weeks when you\'re ill, travelling or near an exam', 'Platforms require it', 'To avoid writing captions'],
         'a': 'B', 'why': 'Evergreen buffer posts protect your rhythm.'},
        {'q': 'What should you do before planning festival posts?',
         'o': ['Copy last year\'s dates', 'Check this year\'s dates and make the post relevant to the business', 'Post the same greeting as everyone', 'Skip all festivals'],
         'a': 'B', 'why': 'Festival dates move, and relevance beats generic greetings.'},
    ],
    study='YouTube\'s routine and batching tips and Canva\'s content organising lesson (about 20 minutes)',
    action='plan your 30-day challenge calendar and batch the first week plus 2 buffer posts',
)

L2 = lesson(
    6, 2,
    title='Repurpose one idea across platforms',
    weeks=(14, 14), hours=1.5,
    outcome='Turn one strong idea or video into several posts for different platforms without copying, watermarks or broken rules, and keep a repurposing map so it becomes a habit.',
    split='20 minutes study, 1 hour 10 minutes action',
    core=f"""
### Create once, publish many

Making a good piece of content takes most of the effort: the idea, the visit, the filming. Publishing it in several shapes takes little extra time and reaches people where they are. This is **repurposing**: one idea, adapted for each platform.

### A content tree

| Start with | Turn it into |
| --- | --- |
| **One long YouTube video** (10 minutes) | 3–5 Shorts or Reels of the best moments; a carousel of the key points; a Threads or LinkedIn post with the main lesson; a WhatsApp Channel update linking to the video |
| **One Reel** | A YouTube Short (from the original file); a Story with a poll about it; a Facebook Reel or Page post; a WhatsApp Status |
| **One carousel** | A LinkedIn document post (export the slides as a PDF); a Story sequence; a Google Business Profile update for a business |
| **One shop visit** | A Reel, a carousel of prices, a "shop story" interview, Stories, a Google review photo for the owner (with permission) |

### Adapt, don't copy

- **Shape:** 9:16 for Reels, Shorts and Stories; 16:9 for long YouTube videos; 4:5 or square for carousels and feed photos.
- **Length:** cut a longer video into short moments; don't stretch a Short.
- **Words:** rewrite the caption for each platform's mood (SMM-M05-L03).
- **Music:** add it inside each app, or use YouTube's libraries. For YouTube Shorts longer than a minute, a copyright claim blocks the Short worldwide ({ASOF}).
- **Files:** always upload your original export. Never download your own post from one app (with its watermark) and upload it to another.

### Repurposing your own work is welcome; reposting others' isn't

Platforms reward originality. Instagram recommends originals over near-identical copies and Facebook announced reduced reach in July 2025 for accounts that repeatedly repost other people's content. Turning **your own** video into a Short, a carousel and a Story is exactly what they expect creators to do.

### Make it a habit

Add a "repurpose" column to your Calendar: for every main post, note the two or three other places it will go. Do the repurposing in your batch session, not as an afterthought.
""",
    example="""
Fathima filmed one 12-minute YouTube video, "20 Kerala geography questions for PSC (Malayalam)". From it, in about 50 extra minutes, she made:

- 4 Shorts, each one tricky question with the answer
- a 7-slide carousel, "5 rivers questions that keep coming back", for Instagram
- a Telegram channel post with the questions as a quiz and the video link
- a WhatsApp Channel update: "New: 20 geography questions explained. Video: [link]"
- a LinkedIn post (on her personal profile) about what she learned making PSC content in Malayalam

The long video got most of its first views from the Shorts and the Telegram post. One idea filled her week.

(Made-up example to show the method.)
""",
    resources=[
        ('yt-shorts3', 'Re-read the music rule for Shorts over 1 minute', '5 min'),
        ('tc-fb-original', 'Re-read what counts as unoriginal content', '5 min'),
        ('li-pages', 'Re-read the tip on document (PDF) posts', '3 min'),
    ],
    steps=[
        'Study the resources (about 15 minutes).',
        'Pick your best post so far (highest 7-day views or shares).',
        'Draw its content tree: list at least 4 other formats or platforms it can become.',
        'Make and publish at least 2 of them this week, each adapted (shape, length, words, music) and uploaded from your original files.',
        'Add a "repurpose" column to your Calendar tab and fill it for the rest of the challenge.',
    ],
    proof='Your content tree, links to the 2 repurposed posts with their Posting Log rows, and a screenshot of the new Calendar column.',
    templates=[
        ('repurposing map', """
MAIN PIECE: _______________ (platform, link)
1. Short/Reel moments: ____ ____ ____
2. Carousel: title ____________ slides ___
3. Story: poll or question ____________
4. Text post (Threads/LinkedIn/Facebook): ____
5. WhatsApp: Status ____ / Channel ____
6. For a business: Google Business Profile post ____
CHECK EACH ONE:
[ ] right shape  [ ] right length  [ ] rewritten words
[ ] music added in-app or from YouTube's libraries
[ ] uploaded from the original file, no watermark
""", ''),
    ],
    mistakes=[
        ('Identical copies everywhere.', 'Adapt shape, length and words for each platform.'),
        ('Watermarked cross-posting.', 'Upload your original export to each app.'),
        ('Repurposing weak content.', 'Repurpose your winners; let the weak posts go.'),
        ('Repurposing other people\'s videos.', 'That is reposting, and platforms push it down. Only repurpose your own work.'),
    ],
    quiz=[
        {'q': 'Which is good repurposing?',
         'o': ['Downloading a viral Reel from another page and posting it', 'Cutting your own long video into Shorts and a carousel', 'Posting the same caption on every app', 'Re-uploading an Instagram download to YouTube'],
         'a': 'B', 'why': 'It adapts your own original work for other formats.'},
        {'q': 'Before cross-posting a video, you should:',
         'o': ['Download it from Instagram', 'Upload the original export to each platform', 'Add another app\'s watermark', 'Make it horizontal for Reels'],
         'a': 'B', 'why': 'Watermarked reposts get less reach.'},
        {'q': 'A carousel can become which LinkedIn format?',
         'o': ['A document (PDF) post', 'A Story', 'A Short', 'A voice note'],
         'a': 'A', 'why': 'Export the slides as a PDF and post them as a document.'},
    ],
    study='YouTube\'s Shorts music rule, Facebook\'s originality crackdown and LinkedIn\'s document tip (about 15 minutes)',
    action='turn your best post into at least 2 adapted posts and add a repurpose column to your calendar',
)

L3 = lesson(
    6, 3,
    title='Scheduling tools and templates',
    weeks=(15, 15), hours=1.5,
    outcome='Schedule posts with free official tools, choose posting times from your own data, and build a template library that halves the time each post takes.',
    split='20 minutes study, 1 hour 10 minutes action',
    core=f"""
### Schedule with the official tools first ({ASOF})

| Tool | What you can schedule |
| --- | --- |
| **Meta Business Suite** (app or computer) | Posts and Stories for a Facebook Page and its connected Instagram account, plus one inbox for messages and comments |
| **YouTube Studio** | Uploads set to publish at a chosen date and time (choose "Schedule" when you upload) |
| **LinkedIn** | Posts on your profile or Page at a chosen date and time |
| **WhatsApp Business broadcasts** | Messages to the customers you choose, sent now or later |

Official tools are free, don't need your password shared with another company, and support the formats properly. Third-party schedulers can be useful for agencies later; check their free plans and permissions carefully before connecting a client's account.

### Scheduled isn't the same as forgotten

Be around for the first hour after a scheduled post goes live, to reply to early comments. Stories and Status updates usually work better posted live, because they react to the day.

### Posting times: use your own data

There is no universal "best time". Once your account has enough followers, Instagram Insights shows when your followers are most active; YouTube Analytics shows when your viewers are on YouTube. Until then, pick a time when your persona is free (evenings for many, lunch break for workers) and test two time slots for two weeks each.

### A template library saves hours

Build once, reuse forever. Keep these in Drive folder **06 Systems**:

- **Canva templates:** Reel cover, carousel (cover, content, summary, CTA), Story frame, YouTube thumbnail, price list
- **Text templates:** caption formulas, CTA bank, reply templates, hashtag sets for each pillar (max 5 each)
- **Checklists:** shooting, editing, design, caption check, honest persuasion check
- **File naming:** date_series_topic_version (2026-11-07_shopstory_tailor_v1.mp4)

A good library makes a routine post take 30–40 minutes instead of two hours.
""",
    example="""
Anu's scheduling set-up for the challenge:

- Instagram and her new Facebook Page: scheduled in Meta Business Suite every Saturday after her batch session.
- YouTube Shorts: uploaded on Saturday and scheduled for 7:30 pm on the same days as the Reels.
- WhatsApp Channel: posted live, because it reacts to the day.

She tested two times for her Reels: 1 pm for the first two weeks, 7:30 pm for the next two. Average views were similar, but replies came faster at 7:30 pm when she was free to answer, so she kept the evening slot. Her template library cut her editing and design time roughly in half by week 3.

(Made-up example to show the method.)
""",
    resources=[
        ('mbs-app', 'Read what you can schedule and manage; install it if you use a Facebook Page', '5 min'),
        ('wa-broadcasts', 'Re-read the scheduling part', '3 min'),
        ('li-pages', 'Re-read the scheduling tip', '2 min'),
        ('canva-mkt', 'Re-watch "Organizing and sharing content" if you skipped it', '5 min'),
    ],
    steps=[
        'Study the resources (about 15 minutes).',
        'Schedule at least 3 challenge posts in advance with official tools (Meta Business Suite, YouTube Studio, or LinkedIn).',
        'Build your template library in Drive 06 Systems: at least 4 Canva templates, your text templates and your checklists.',
        'Choose two posting times to test, and write the test in the Experiments tab.',
    ],
    proof='Screenshots of 3 scheduled posts, a screenshot of your 06 Systems folder, and the posting-time test in the Experiments tab.',
    templates=[
        ('template library contents', """
06 Systems/
  Canva: reel-cover, carousel (4 slides), story-frame,
         yt-thumbnail, price-list
  Text:  caption-formulas, cta-bank, replies,
         hashtag-sets (pillar: 5 tags each)
  Checklists: shooting, editing, design, caption,
         honest-persuasion
  Naming: YYYY-MM-DD_series_topic_v1
""", ''),
        ('posting-time test (Experiments tab row)', """
Start date,Hypothesis,Change tested,Metric,Before,After,Result,Decision
____,Evening posts get faster replies,1 pm vs 7:30 pm (2 weeks each),Average 24 h views and replies in first hour,,,,
""", 'csv'),
    ],
    mistakes=[
        ('Giving your password to an unknown scheduling app.', 'Use official tools first; connect third-party tools only through official log-in screens.'),
        ('Scheduling and disappearing.', 'Reply to comments in the first hour.'),
        ('Copying someone\'s "best time to post".', 'Test times with your own audience.'),
        ('Templates that make every post look identical.', 'Keep the layout, change the photo, colour accent or headline.'),
    ],
    quiz=[
        {'q': 'Which free tool schedules posts and Stories for a Facebook Page and its Instagram account?',
         'o': ['Meta Business Suite', 'Google Trends', 'Snapseed', 'Telegram'],
         'a': 'A', 'why': 'Its listing says it creates, schedules and manages posts and Stories for both.'},
        {'q': 'What is the best way to choose posting times?',
         'o': ['Copy a viral post\'s time', 'Use your own Insights and test two time slots', 'Always post at midnight', 'Post at random'],
         'a': 'B', 'why': 'Your own audience\'s habits are what matter.'},
        {'q': 'Why be online for the first hour after a scheduled post?',
         'o': ['Platforms require it', 'To reply to early comments and start conversations', 'To delete it if views are low', 'To repost it'],
         'a': 'B', 'why': 'Quick replies build community and keep conversations going.'},
    ],
    study='Meta Business Suite, WhatsApp broadcast scheduling, LinkedIn scheduling and Canva\'s organising lesson (about 15 minutes)',
    action='schedule 3 posts with official tools, build your template library and set up a posting-time test',
)

L4 = lesson(
    6, 4,
    title='The 30-day content challenge',
    weeks=(14, 18), hours=12,
    outcome='Post every day for 30 days, log every post\'s numbers, review each week and run one small experiment a week, so that you finish with real data about what works for your audience.',
    split='30 minutes study, about 11 hours 30 minutes of posting and reviews over 30 days',
    core="""
### Why 30 days in a row

Posting every day for a month does three things that three posts a week can't. You learn faster, because you get ten times more data. You get faster at making content, because you repeat the whole process daily. And you find out which formats and topics your audience actually wants, instead of guessing.

### The rules

1. **Post once a day for 30 days** on your main platform: a Reel or Short, a carousel or a photo post. Stories and Status updates don't count (do them too).
2. **At least 12 of the 30 are short videos.**
3. **Quality floor:** every post has a hook, corrected captions, licensed sound and consent from anyone in it. Don't drop your standards to hit the count.
4. **Log everything:** a Posting Log row the day you post, views after 24 hours, views and other numbers after 7 days.
5. **Sunday review:** a Weekly Stats row and one decision for the next week.
6. **One experiment a week:** change one thing (hook type, length, format, language, posting time) and compare.
7. **Missed a day?** Post the next day and carry on. Don't post three times to "catch up".

Batch twice a week (SMM-M06-L01) and keep your buffer full, so the challenge takes about 20–30 minutes a day, not two hours.

### A four-week shape

| Week | Days | Focus | Experiment idea |
| --- | --- | --- | --- |
| 1 | 1–7 | Your usual formats, all pillars; find your baseline | None: just measure |
| 2 | 8–14 | Hooks | Question hooks vs result-first hooks |
| 3 | 15–21 | Formats and length | 15-second vs 45-second videos; carousel vs Reel on the same topic |
| 4 | 22–30 | Double down on what worked | Repeat your top 3 topics in new versions |

### Honest expectations

Some days a post will get almost no views. One or two posts may do far better than the rest. Most accounts don't "blow up" in 30 days, and that's fine: the goal is learning and a habit, and the numbers you collect become your first case study in Module 8. Judge the challenge by your averages week to week, not by one post.

### Look after yourself

Daily posting can be tiring. Sleep, PSC study and family come first. Batch so that most days are light, take screen breaks, and if a PSC exam falls inside the 30 days, move the challenge rather than squeezing it in. Module 16 covers creator burnout properly.
""",
    example="""
Anu's challenge (days 1–30, made-up numbers to show the method):

| Week | Posts | Average views after 7 days | Shares per 1,000 views | Followers gained | Experiment and result |
| --- | --- | --- | --- | --- | --- |
| 1 | 7 | 640 | 8 | 41 | Baseline |
| 2 | 7 | 910 | 11 | 66 | Question hooks beat result-first hooks for food posts |
| 3 | 7 | 820 | 14 | 58 | 15-second videos got more views; carousels got more saves |
| 4 | 9 | 1,450 | 17 | 132 | Repeated top topics: "₹100 Friday" and "shop stories" |

Her best post (day 23, a 40-second story of a 31-year-old tailoring shop) reached 9,800 accounts, mostly local, and 160 people shared it. Her worst (day 5, a long text post about bus timings) got 90 views. Her decision: shop stories and food under ₹100 become her two main series; text-heavy posts move to WhatsApp Channel.
""",
    resources=[
        ('ig-small', 'Re-read why posting regularly helps each reel reach new viewers', '5 min'),
        ('yt-wellbeing', 'Read the tips on routines and taking breaks', '10 min'),
        ('yt-burnout', 'Read the tips on avoiding burnout before you start', '10 min'),
    ],
    steps=[
        'Study the resources (about 25 minutes) and set your start date, at least two weeks away from any PSC exam.',
        'Days 1–30: post every day following the rules, from your Calendar and buffer. Log each post the same day, and add the 24-hour and 7-day numbers.',
        'Every Sunday: fill in Weekly Stats, write what worked and what didn\'t, and choose next week\'s one experiment (log it in Experiments).',
        'Day 30: screenshot your Insights overview for the 30 days and fill in the day-30 summary.',
    ],
    proof='Your Posting Log with 30 daily posts (24-hour and 7-day numbers), 4 Weekly Stats rows, 3 experiments, an Insights screenshot and your day-30 summary.',
    fulltime='The challenge runs for 30 real days, so on the full-time pace it continues while you study Modules 7 to 10. The app will show this task as overdue for a few weeks; tick it when day 30 is done.',
    templates=[
        ('challenge tracker (one row a day)', """
Day,Date,Platform,Format,Pillar,Hook type,Length (s),Language,Views 24 h,Views 7 days,Reach,Shares,Saves,Follows,Experiment?,Note
""", 'csv'),
        ('Sunday review', """
WEEK __ (days __-__)
Posts: ___/7   Average 7-day views: ___
Best post: ________ (why?) ______________
Worst post: _______ (why?) ______________
Experiment this week: __________________
  Result: ___________  Decision: _________
Energy check (1-5): ___  What will make next week easier?
_________________________________________
""", ''),
        ('day-30 summary', """
30-DAY CHALLENGE SUMMARY (dates ____ to ____)
Posts: ___/30 (short videos: ___)
Followers: start ___ end ___ (+___)
Average 7-day views: week 1 ___ week 4 ___
Shares per 1,000 views: week 1 ___ week 4 ___
Top 3 posts and why they worked:
  1. ____ 2. ____ 3. ____
3 things I'll keep doing: ____ ____ ____
3 things I'll stop doing: ____ ____ ____
What surprised me: ______________________
""", ''),
    ],
    mistakes=[
        ('Dropping quality to keep the streak.', 'A rushed post with no hook teaches you nothing. Use your buffer instead.'),
        ('Changing five things at once.', 'One experiment a week, so you know what made the difference.'),
        ('Judging by the best or worst single post.', 'Compare weekly averages.'),
        ('Burning out in week 2.', 'Batch, keep a buffer and protect your sleep and study time.'),
        ('Not logging.', 'Without the numbers, the challenge is just tiring. Log every day.'),
    ],
    quiz=[
        {'q': 'During the challenge, you miss day 12. What should you do?',
         'o': ['Restart from day 1', 'Post on day 13 and carry on; don\'t post three times to catch up', 'Give up', 'Buy views'],
         'a': 'B', 'why': 'Consistency matters more than a perfect streak.'},
        {'q': 'Why run only one experiment a week?',
         'o': ['Experiments are banned', 'So you know which change caused the difference', 'Platforms allow one change a week', 'It doesn\'t matter'],
         'a': 'B', 'why': 'Changing many things at once makes results impossible to read.'},
        {'q': 'How should you judge whether the challenge worked?',
         'o': ['By your single best post', 'By weekly averages and what you learned', 'By likes only', 'By follower count on day 1'],
         'a': 'B', 'why': 'Averages and lessons show real progress.'},
        {'q': 'A PSC exam falls on day 18 of your planned challenge. What\'s the sensible plan?',
         'o': ['Skip sleep to keep posting', 'Move the challenge so it doesn\'t overlap the exam weeks', 'Post low-quality filler', 'Stop studying'],
         'a': 'B', 'why': 'Your exam and wellbeing come first; the challenge can move.'},
    ],
    study='Instagram\'s advice on regular posting and YouTube\'s well-being and burnout tips (about 25 minutes)',
    action='complete the 30-day content challenge with every post logged, weekly reviews and a day-30 summary',
)

LESSONS = [L1, L2, L3, L4]

MODULE = module(
    6,
    title='Content systems',
    weeks=(14, 18), hours=18,
    overview="""
Build the system that lets you post consistently for months: a calendar, batching, repurposing, scheduling and templates. Then prove it with a 30-day content challenge.

Good marketers aren't more inspired than others; they have systems. In week 14 you plan your month around Kerala's seasons, batch a week of content in one session, and turn single ideas into several posts. In week 15 you schedule with free official tools and build a template library.

The 30-day challenge starts in week 14 and runs until week 18, alongside Module 7. It is the heart of the course's first half: every day you post, measure and learn.
""",
    outcomes=[
        'Plan a month of content around themes, pillars and series',
        'Batch a week of posts in one session and keep a buffer',
        'Repurpose one idea into several platform-ready posts',
        'Schedule posts with Meta Business Suite, YouTube Studio and LinkedIn',
        'Complete 30 days of daily posting with full measurement',
    ],
    lessons=LESSONS,
    project='Your content system, version 1',
    project_week=15,
    project_steps=[
        'Show your system working by the end of week 15: the 30-day Calendar tab with statuses, a "repurpose" column filled in, and at least 7 posts scheduled or posted from batches.',
        'Write your batching routine (days, times, tasks) as you actually do it.',
        'Organise your template library in 06 Systems with a short index.',
        'Keep 3–5 buffer posts ready.',
        'Write one paragraph: what in this system saves you the most time, and what still takes too long.',
    ],
    project_proof='Screenshots of your Calendar tab and 06 Systems folder, your batching routine and your one-paragraph review.',
    rubric=[
        ('Calendar', 'No plan', 'A plan for a week', 'A month of themes and a 30-day calendar with statuses'),
        ('Batching', 'One post at a time', 'Sometimes batched', 'Two regular batch sessions a week and a buffer of 3–5 posts'),
        ('Repurposing', 'One platform only', 'Copies across platforms', 'Adapted versions from original files, planned in the calendar'),
        ('Scheduling and templates', 'Posting live, from scratch', 'Some templates', 'Official scheduling plus a template library in use'),
        ('30-day challenge', 'Under 15 days', '15–29 days or weak logging', '30 days, all logged, 4 reviews, 3 experiments'),
    ],
    short=[
        'Plan only the first two weeks of the challenge in detail.',
        'One batch session a week instead of two.',
        'Repurpose one post into one other format.',
        'If 30 days is impossible right now, do 30 posts in 45 days, keeping all the logging and reviews.',
    ],
    flashcards=[
        ('Three levels of a content calendar?', 'Month (themes), week (pillars and series), day (the exact post).'),
        ('The six statuses of a post?', 'Idea, scripted, shot, edited, scheduled, posted.'),
        ('How big should your buffer be?', 'Three to five finished, evergreen posts.'),
        ('Why upload original files when cross-posting?', 'Watermarked reposts get less reach.'),
        ('Free tool to schedule Facebook and Instagram posts?', 'Meta Business Suite.'),
        ('Where do you find your best posting time?', 'Your own Insights and Analytics, plus a two-time-slot test.'),
        ('The 30-day challenge\'s experiment rule?', 'One change a week, so you know what made the difference.'),
        ('Missed a challenge day: what do you do?', 'Post the next day and carry on.'),
    ],
    mistakes=[
        ('A system on paper only.', 'If you don\'t use it in week 15, simplify it until you do.'),
        ('Treating the challenge as a race for followers.', 'It\'s a learning sprint. The data is the prize.'),
        ('Forgetting Module 7 during the challenge.', 'Use each growth lesson as that week\'s experiment.'),
    ],
)
