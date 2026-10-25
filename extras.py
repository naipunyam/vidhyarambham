"""Course-level sections: start here, schedule, week 0, baseline, posting
track, final checklist, what next, glossary and the sources page."""
from common import R, STATUS, VDATE, ASOF, link, rules, fence, bullets, numbered, table, use, fmt_hours

MODULE_MAP = [
    (1, 'Foundations', 'How platforms rank content, the funnel, career paths; your practice account goes live', 'Starter plan and baseline'),
    (2, 'Strategy', 'Goals, audience research, personas, niche, competitors, pillars, voice', 'One-page social media strategy'),
    (3, 'Platforms in depth', 'Instagram, YouTube, Facebook, WhatsApp Business, LinkedIn, X, Threads, Telegram, Indian apps', 'Platform plan and optimised profiles'),
    (4, 'Content creation', 'Hooks, scripts, Malayalam and English, shooting and editing on the phone, design', 'Phone content pack'),
    (5, 'Copywriting', 'Headlines, captions, calls to action, honest persuasion, writing for each platform', 'Caption bank'),
    (6, 'Content systems', 'Calendars, batching, repurposing, scheduling, templates, the 30-day challenge', 'Content system and 30 days of posts'),
    (7, 'Growth', 'Social SEO, hashtags, YouTube search, trends, collaborations, community, DMs', 'Growth experiments'),
    (8, 'Analytics', 'Metrics, insights, Google Analytics, UTM links, A/B tests, reports', 'Case study 1: your 30-day challenge'),
    (9, 'Paid ads', 'Boosting vs Ads Manager, targeting, small budgets, testing, retargeting, ROI', 'Ad plan and optional test ad'),
    (10, 'Influencer and creator marketing', 'Micro-influencers, UGC, affiliate links, creator income', 'Influencer brief and creator money plan'),
    (11, 'Local business and social commerce', 'Google Business Profile, selling on WhatsApp and Instagram, reviews, events, audits, a real pilot', 'Three audits and case study 2: the pilot'),
    (12, 'Personal branding', 'Your authority online, portfolio and case studies', 'Portfolio site'),
    (13, 'AI for social media', 'AI for ideas, scripts, captions, images, video, analytics, and its risks', 'AI playbook'),
    (14, 'Ethics, law and safety', 'Disclosure rules, copyright, music, consent, honest growth, crises, security', 'Compliance and safety kit'),
    (15, 'Earning', 'Packages, pricing, clients, proposals, contracts, onboarding, reports, agency', 'Sales kit'),
    (16, 'Creator wellbeing', 'Burnout, comparison, trolls and harassment', 'Wellbeing plan'),
    (17, 'Capstone', 'A 90-day growth project, client-ready portfolio, service package and price sheet', 'Case study 3, portfolio, price sheet'),
]

# Posting checkpoints in the posting track: (task id, due week, text, evidence)
CHECKPOINTS = [
    ('smm-post-01', 3, 'Posting checkpoint 1 (weeks 1–3): at least 5 posts published and logged', 'Links to the posts and the Posting Log rows'),
    ('smm-post-02', 6, 'Posting checkpoint 2 (weeks 4–6): 6 more posts, two of them after your profile was optimised', 'Posting Log rows for weeks 4–6'),
    ('smm-post-03', 9, 'Posting checkpoint 3 (weeks 7–9): 9 more posts, including your first phone-shot Reel or Short', 'Posting Log rows and the Reel or Short link'),
    ('smm-post-04', 13, 'Posting checkpoint 4 (weeks 10–13): 12 more posts and four Weekly Stats rows', 'Posting Log and Weekly Stats rows'),
    ('smm-post-05', 21, 'Posting checkpoint 5 (weeks 19–21): 9 more posts after the challenge, still on schedule', 'Posting Log rows for weeks 19–21'),
    ('smm-post-06', 24, 'Posting checkpoint 6 (weeks 22–24): 9 more posts; one used as an ad or ad test', 'Posting Log rows for weeks 22–24'),
    ('smm-post-07', 27, 'Posting checkpoint 7 (weeks 25–27): 9 more posts; your 90-day sprint has started', 'Posting Log rows and your sprint plan'),
    ('smm-post-08', 30, 'Sprint checkpoint 1 (weeks 28–30): posts on plan, first sprint experiment logged', 'Posting Log, Weekly Stats and Experiments rows'),
    ('smm-post-09', 33, 'Sprint checkpoint 2 (weeks 31–33): posts on plan, second experiment logged', 'Posting Log, Weekly Stats and Experiments rows'),
    ('smm-post-10', 36, 'Sprint checkpoint 3 (weeks 34–36): posts on plan, third experiment logged', 'Posting Log, Weekly Stats and Experiments rows'),
]


def posting_hours(w):
    """Hours for posting outside lessons, by part-time week."""
    if 1 <= w <= 13:
        return 1.25
    if 14 <= w <= 18:
        return 0  # the 30-day challenge lesson holds these hours
    if 19 <= w <= 26:
        return 1.25
    if 27 <= w <= 39:
        return 1.75
    return 0


TOOLKIT = [
    ('smm-final-workbook', 'SMM Workbook with every tab filled in: Posting Log, Weekly Stats, Experiments and the rest', 'Week 0, used all course'),
    ('smm-final-strategy', 'One-page social media strategy, updated with what you learned', 'Module 2'),
    ('smm-final-profiles', 'Optimised profiles on your main and support platforms', 'Module 3'),
    ('smm-final-production', 'Production kit: script formats, shot list, editing checklist, design templates', 'Module 4'),
    ('smm-final-copy', 'Caption bank and copy formulas, in Malayalam and English', 'Module 5'),
    ('smm-final-system', 'Content system: calendar, batching routine, repurposing map, scheduling', 'Module 6'),
    ('smm-final-growth', 'Growth playbook: keyword and hashtag sets, collab list, engagement routine', 'Module 7'),
    ('smm-final-reports', 'Report templates: weekly stats, monthly client report, UTM sheet', 'Module 8'),
    ('smm-final-ads', 'Ad plan template and your test results (or dry-run plan)', 'Module 9'),
    ('smm-final-influencer', 'Influencer brief, creator rate card and money plan', 'Module 10'),
    ('smm-final-audits', 'Three local business audits, the pilot agreement and the pilot report', 'Module 11'),
    ('smm-final-portfolio', 'Portfolio site with three case studies and before/after numbers', 'Modules 12 and 17'),
    ('smm-final-ai', 'AI playbook: prompts, checks and disclosure rules', 'Module 13'),
    ('smm-final-compliance', 'Compliance and safety kit: disclosure checklist, consent form, crisis playbook, security audit', 'Module 14'),
    ('smm-final-sales', 'Sales kit: packages, price sheet, proposal, agreement, onboarding checklist', 'Module 15'),
    ('smm-final-wellbeing', 'Wellbeing plan with your posting limits and rest days', 'Module 16'),
]


def _mods(modules):
    for m, mod in modules:
        yield m, mod.MODULE, mod.LESSONS


def total_hours(modules):
    h = 4 + 1  # week 0 (with the baseline) and the final checklist
    for _, overview, _lessons in _mods(modules):
        h += overview['hours']
    h += sum(posting_hours(w) for w in range(0, 41))
    return h


def week_plan(modules):
    """Return {week: (items, hours)} at part-time pace."""
    plan = {0: (['Week 0: free toolkit, practice account and baseline self-assessment'], 4)}

    def add(w, item, hrs):
        items, h = plan.get(w, ([], 0))
        if item and item not in items:
            items.append(item)
        plan[w] = (items, h + hrs)

    for m, overview, lessons in _mods(modules):
        for s in lessons:
            a, b = s['weeks']
            code = s['title'].split(':')[0]
            for w in range(a, b + 1):
                label = code if a == b else f'{code} (weeks {a}–{b})'
                add(w, label, s['hours'] / (b - a + 1))
        project_hours = overview['hours'] - sum(s['hours'] for s in lessons)
        pw = next(t['week'] for t in overview['tasks'] if t['id'].endswith('-project'))
        add(pw, f'Module {m} project and rubric', project_hours)
    for w in range(1, 40):
        if posting_hours(w):
            add(w, 'posting', posting_hours(w))
    for tid, w, text, _ in CHECKPOINTS:
        add(w, text.split(' (')[0] + ' due', 0)
    add(40, 'final self-assessment and checklist', 1)
    return plan


def full_time_rows(modules):
    """Calendar weeks at full-time pace (weekLength 0.35)."""
    names = {m: name for m, name, _, _ in MODULE_MAP}
    mod_weeks = {m: ov['weeks'] for m, ov, _ in _mods(modules)}
    notes = {
        1: 'Week 0 setup, then post every day from day 2.',
        3: 'When Module 3 is done, your growth project starts: from now on every day of posting counts towards it.',
        5: 'The 30-day challenge starts with SMM-M06-L04 (about day 34). It runs in real days, to about day 64.',
        6: 'The challenge keeps running while you study Modules 7 and 8.',
        8: 'Analyse the challenge days you have so far; finish the results report when day 30 is done.',
        10: 'Challenge finished. Do the three audits (SMM-M11-L04) and pitch your pilot this week.',
        11: 'The 4-week pilot starts (SMM-M11-L05). It runs in real days, to about day 99.',
        14: 'Pilot results report, capstone report, portfolio and price sheet. Your growth project now covers about 78 days.',
    }
    rows = []
    for c in range(1, 15):
        lo = int(7 * (c - 1) / 2.45)
        hi = min(int((7 * c - 0.01) / 2.45), 40)
        if c == 14:
            hi = 40
        focus = [f'M{m:02d} {names[m]}' for m, (s, e) in sorted(mod_weeks.items()) if s <= hi and e >= lo and not (m == 17 and lo < 26)]
        if lo == 0:
            focus.insert(0, 'Week 0')
        rows.append((str(c), f'{lo}–{hi}', '; '.join(focus) or '—', notes.get(c, '')))
    return rows


def start_section(modules):
    total = total_hours(modules)
    weeks_of = {m: ov['weeks'] for m, ov, _ in _mods(modules)}
    map_rows = []
    for m, name, does, output in MODULE_MAP:
        w = weeks_of.get(m)
        wl = '' if not w else (f'{w[0]}' if w[0] == w[1] else f'{w[0]}–{w[1]}')
        map_rows.append((f'{m}. {name}', wl, does, output))
    content = f"""
## What this course is

A free, practical course in social media marketing, built for Kerala. You learn by doing it for real: you grow your own account from zero, run a no-cost campaign for a real local business, and finish with a portfolio, a service package and a price sheet you can show to clients or employers.

It is written for a beginner near Kuttiady in Kozhikode district who is preparing for Kerala PSC exams, has an Android phone and an old laptop, and has ₹0 to spend on learning. Content is made in Malayalam and English. It works just as well for anyone in a similar situation.

Platforms change fast, so every platform fact in this course is marked with the date it was checked: **{ASOF}**. The lessons teach principles that survive algorithm changes, and they show you where to check the current rules.

## By the end you will have

- A real account grown from zero, with 40 weeks of posting logged and a 90-day growth project measured from start to finish
- Three case studies with before and after numbers: your 30-day challenge, a 4-week pilot for a real local business, and your 90-day growth project
- Three written audits of real local businesses
- A client-ready portfolio site, a service package and a price sheet
- A complete toolkit of templates, built one module at a time

## How long it takes

{table(['Pace', 'Calendar time', 'Hours a week', 'Total work'], [
    ('Part-time (the default)', 'Week 0, then 40 weeks: about 9.5 months', 'About 6', f'About {total:.0f} hours'),
    ('Full-time', 'About 14 weeks', 'About 17, posting every day', f'About {total:.0f} hours'),
])}

Pick your pace and start date on the course page; the app then shows which week you are in and what is due. The hours are honest estimates.

**Why so long?** Growth takes real days. The 30-day challenge, the 4-week pilot and the 90-day growth project can't be rushed, even on the full-time pace. The full-time schedule shows how they overlap with the later modules.

## Honest expectations about growth

- **Most new accounts grow slowly at first.** Expect weeks where a post gets a few dozen views. That is normal, not failure.
- **Growth is lumpy.** One post may do ten times better than the rest, then views drop again. Judge your progress by monthly trends, not single posts.
- **You control inputs, not outputs.** You decide how often you post, how good your hooks are and how fast you learn from your numbers. The platform decides who sees each post.
- **Followers are not the goal.** Clients pay for enquiries, bookings and sales. This course tracks those from Module 2 onwards.
- **There are no shortcuts.** Bought followers, engagement groups and fake reviews break platform rules, can break Indian consumer law and ruin your account (Module 14).

This course never invents statistics. Where a number comes from a platform or a study, the source is linked. The people, businesses and numbers in the examples are made up to show how the methods work.

## How each lesson works

Every lesson has the same parts, in this order:

1. **ID, title, outcome and time** at the top of the page, such as SMM-M01-L01
2. **Core lesson:** the idea, explained simply, with platform facts dated
3. **Local example:** the idea applied in or near Kuttiady, with rupee numbers
4. **Free resources:** exactly what to study, how long it takes and when the link was checked
5. **Action task:** real work on your account or for a real business, and the **proof to record**
6. **Template:** copy-ready calendars, scripts, formulas, checklists and reports
7. **Common mistakes** and how to avoid them
8. **Quiz:** 3 to 5 questions, with the answers at the very bottom
9. **Progress checklist:** the ticks under **Your tasks**

Each module starts with an overview page: outcomes, total time, the module project, a self-assessment rubric, a "short on time?" version and revision flashcards.

## How to use the app for this course

- Tick each task under **Your tasks** when it is done. Ticks are saved on this phone, so save a backup now and then from **Backup and courses**.
- Paste the link to your proof (a post, a Google Drive file or a screenshot) into the task's note.
- **This week**, on the course page, lists what is due, plus your next posting checkpoint.
- Exam coming? Use exam mode (in the weekly schedule) and move your start date later so the weeks match. Your ticks are kept.

## Module map

{table(['Module', 'Part-time weeks', 'What you do', 'Output for your toolkit'], map_rows)}

## Key assumptions

These decisions were made for you when the course was written. Change them if your situation is different.

1. **Pace:** part-time, about 6 hours a week next to PSC study. The full-time pace does the same work in about 14 weeks.
2. **Money:** learning costs ₹0. The only optional spend is a tiny test ad in Module 9 (₹300–₹1,000, or a ₹0 dry run). A cheap clip-on microphone (Module 4) is optional too.
3. **Devices:** an Android phone does almost everything. The old laptop is for spreadsheets, longer writing and, if it copes, desktop-only tools such as YouTube's title and thumbnail tests.
4. **Practice account:** by default a hyperlocal page about your area, in Malayalam with English captions: local shops, food, events and useful updates. It gives you endless content nearby, grows faster with a local audience, introduces you to future clients and becomes your portfolio. Module 1 lets you choose another niche or your own brand instead.
5. **Main platforms:** Instagram and YouTube Shorts for growth, WhatsApp Business for local selling, LinkedIn for your career. Module 3 helps you confirm or change this.
6. **The pilot:** a free 4-week pilot for a real local business in Module 11, in exchange for permission to use the results as a case study.
7. **Facts and rules** were checked on {VDATE}. Platform features, limits and policies change often. Anything marked **check current rules** links to the official source; check it before you act, and before you advise a client.
8. **Not legal or tax advice.** The course explains Indian rules simply. For contracts, GST and disputes, ask a qualified professional.
9. **Every resource is free.** A few need a free sign-up (Meta Blueprint, HubSpot Academy, Canva, Google Skillshop).

## The running examples (all made up)

- **Anu**, a PSC aspirant from Kakkattil, runs the practice page **@kuttiady.diaries** and takes this course at the part-time pace.
- **Nisha's Oven**, a home bakery in Kuttiady (you may know her from the Entrepreneurship course)
- **Malabar Mobiles**, a phone shop with a repair counter in Kuttiady town
- **Kakkayam Hills Homestay**, a three-room homestay near Kakkayam
- **Peak Fitness**, a gym in Vatakara
- **Amma's Pickles**, a Kudumbashree pickle unit in Perambra
- **Fathima's PSC Sprint**, a Malayalam YouTube channel for PSC practice
- **Arun's ShopAssist**, a freelancer who sets up WhatsApp Business and Google profiles for shops

## Other courses in this app

This course links to two others instead of repeating them:

- **Practical Entrepreneurship** for positioning (ENT-M06-L01), pricing (ENT-M05-L03), sales conversations (Module 7), GST and tax (ENT-M08-L03) and contracts (ENT-M09-L03)
- **Free AI Generalist Course** for prompting (Level 1), AI images, video and voice (Level 3) and automation (Level 4)
"""
    return {
        'id': 'smm-start',
        'title': 'Start here: how this course works',
        'kind': 'intro',
        'summary': 'What you will build, how long it takes, honest growth expectations, how every lesson works and the assumptions behind the course.',
        'content': content.strip(),
    }


def schedule_section(modules):
    plan = week_plan(modules)
    rows = []
    for w in sorted(plan):
        items, hrs = plan[w]
        items = [i for i in items if i != 'posting'] + (['posting'] if 'posting' in items else [])
        rows.append((str(w), '; '.join(items), f'{hrs:.1f}'.rstrip('0').rstrip('.')))
    ft = full_time_rows(modules)
    content = f"""
## Part-time: about 6 hours a week

One course week is one calendar week. This is the default pace on the course page. "Posting" means the posts on your posting track, about 1 to 2 hours a week outside the lessons.

{table(['Week', 'What you do', 'Hours'], rows)}

## Full-time: about 17 hours a week

Choose **Full-time** on the course page. The app then moves about three course weeks every calendar week (one course week is 0.35 of a calendar week), so lessons come quickly. Real-day projects don't speed up, so they overlap the later modules:

- **Post every day** from the first week, not just on the part-time schedule.
- **Your growth project** is your whole posting period from the end of Module 3, about 78 days, instead of the part-time 90-day sprint.
- **The 30-day challenge** still takes 30 days, and **the pilot** still takes 4 weeks. Tick them when the real days are done. The app will show them as overdue for a while; that is expected.

{table(['Calendar week', 'Course weeks', 'Modules', 'Real-day notes'], ft)}

## A weekly rhythm that fits around PSC study

- **Weekdays:** 40–50 minutes after your PSC study block, not before it, so the exam keeps your best hours. Reply to comments for 10 minutes, then do the lesson.
- **Saturday:** a 2-hour batch session: script, shoot and edit the coming week's posts.
- **Sunday:** 30 minutes to fill in Weekly Stats and decide one thing to change next week.
- **Full-time:** mornings for creating and client work, afternoons for lessons, 15 minutes at the end of the day for numbers.

## When you fall behind

- **This week** shows earlier open tasks as overdue. Do the action tasks and your posts first; readings can wait.
- More than two weeks behind? Set a new start date on the course page so the weeks match your real progress. Your ticks are kept.
- Use each module's "short on time?" version when you need it.

## Exam mode

In the four weeks before a PSC exam: post twice a week from posts you batched earlier, reply to comments, and pause the lessons. Move your start date later by the same number of weeks. Your account keeps its rhythm, and the course waits for you.
"""
    return {
        'id': 'smm-schedule',
        'title': 'Weekly schedule: part-time and full-time',
        'kind': 'reference',
        'summary': 'What to do each week at both paces, how real-day projects fit the full-time pace, and a weekly rhythm around PSC study.',
        'content': content.strip(),
    }


WORKBOOK_HEADERS = """
Posting Log:
Date,Platform,Format,Pillar,Topic,Hook (first line),Language (ML/EN/both),Link,Views after 24 h,Views after 7 days,Accounts reached,Likes,Comments,Shares,Saves,Follows,Profile visits,Link clicks or DMs,Average watch % or time,Notes

Weekly Stats:
Week,Start date,Followers at start,Followers at end,Posts,Total views,Accounts reached,Interactions,Profile visits,Link clicks,Enquiries (DMs/calls),What I will change

Ideas:
Date,Idea,Pillar,Format,Hook idea,Source (comment/search/trend/own),Score 1-5,Used on (date)

Calendar:
Date,Day,Platform,Format,Pillar,Topic,Hook,Call to action,Status (idea/scripted/shot/edited/scheduled/posted),Link

Hooks and Captions:
Type,English,Malayalam,Used on,Result

Competitors:
Account,Platform,Followers,Posts a week,Best format,Top 3 posts (topic and views),What they do well,Gap I can fill

Experiments:
Start date,Hypothesis,Change tested,Metric,Before,After,Result,Decision

Leads and Clients:
Business,Contact person,Phone (with consent),Area,Source,Stage,Last contact,Next step,Next date,Offer,Value (Rs),Notes

Pilot:
Week,Posts,Views,Accounts reached,Profile visits,Calls,WhatsApp chats,Direction requests or visits,Orders or bookings,Revenue (Rs) if shared,Notes
"""

COACH_PROMPT = """
You are my social media marketing coach. I live near
Kuttiady, Kozhikode, Kerala. I am a beginner taking a
practical course, about 6 hours a week, next to Kerala
PSC exam prep. I make content in Malayalam and English.
Rules for you:
1. Ask me one question at a time.
2. Push me to post, test and look at real numbers
   instead of guessing.
3. Use rupee examples and Kerala context.
4. If you are not sure about a platform feature, rule or
   number, say so and tell me to check the official help
   page. Platform rules change often.
5. Never suggest fake followers, fake reviews, copied
   content or hidden paid promotions.
6. Don't write everything for me; improve what I write.
Today I am working on: [lesson ID and task].
"""

RULES = [
    '**Only post what you have the right to post.** Your own photos and videos, or music from the app\'s own library. Never download photos from Google or film songs from YouTube to use in your posts.',
    '**Ask before you film or photograph people,** and before you post a shop, its staff or its customers. For children, ask a parent, and when in doubt leave them out.',
    '**Say when something is paid or free.** If a shop gives you a free meal, a discount or money to post about it, the post must say so clearly, for example "Ad" or "Free gift" (Module 14 explains the Indian rules).',
    '**No fake engagement.** Never buy followers, likes, views or reviews, and don\'t join "engagement groups". It breaks platform rules and can get your account restricted.',
    '**Check before you share local news.** A wrong post about an accident, a strike or a shop closing can hurt real people. When unsure, don\'t post.',
    '**Stay away from politics, religion and communal topics** on your practice page. Arguments there can bring trolls, reports and real-life trouble.',
    '**Keep your accounts safe:** two-step verification on, a password you use nowhere else, and never share login codes with anyone, even "Meta support".',
]


def setup_section():
    content = f"""
Week 0 takes about 4 hours, including the baseline self-assessment on the next page. You set up free tools once, so every lesson has a place to save its work, and your practice account goes live.

## 1. An SMM Toolkit folder in Google Drive

Make a folder called **SMM Toolkit** with these subfolders: 00 Baseline, 01 Foundations, 02 Strategy, 03 Platforms, 04 Content, 05 Copy, 06 Systems, 07 Growth, 08 Analytics, 09 Ads, 10 Influencers, 11 Local business, 12 Portfolio, 13 AI, 14 Compliance, 15 Sales, 16 Wellbeing, 17 Capstone. Every lesson's proof goes into one of them. When a task asks for proof, copy the file's or post's link and paste it into the task's note in this app.

## 2. The SMM Workbook

Make one Google Sheets file called **SMM Workbook** with nine tabs: Posting Log, Weekly Stats, Ideas, Calendar, Hooks and Captions, Competitors, Experiments, Leads and Clients, and Pilot. Put each tab's header row (below) in row 1.

- **On the laptop:** copy a header line, paste it into cell A1, then choose Data → Split text to columns.
- **On the phone:** type the headings into row 1, or do this step once on the laptop.

{fence(WORKBOOK_HEADERS, 'csv')}

The Posting Log is the heart of the course. Every post you publish gets a row, with its numbers after 24 hours and after 7 days.

## 3. Get your phone ready

- **Free up space:** at least 5 GB free, so videos don't fail to save. Move old photos to Google Photos or the laptop.
- **Install now:** {link('canva-app', 'Canva')}, {link('snapseed', 'Snapseed')}, {link('yt-studio-app', 'YouTube Studio')}, Google Sheets and Google Drive. You'll add a video editor in Module 4 and WhatsApp Business and Meta Business Suite in Module 3.
- **Malayalam typing:** add Malayalam to Gboard ({link('gboard-ml', 'how to')}), or install the free, open-source {link('indic-kbd', 'Indic Keyboard')}, which can turn Manglish typing into Malayalam script.

## 4. Your practice account

Choose a provisional niche now; you'll test and refine it in Module 2. The default is a **hyperlocal page about your area**: "Kuttiady diaries: local food, shops, events and useful updates, in Malayalam". Other good options: a hobby you know well, Kerala PSC study tips, or your own brand as a social media marketer.

1. Pick a handle that is short, easy to spell in English and free on Instagram and YouTube (search for it on both).
2. Create a **new** Instagram account for the page (not your personal one) and switch it to a professional account, choosing **Creator** ({link('ig-pro', 'Instagram Help: professional accounts')}). Professional accounts get insights and are public, which the recommendation system needs.
3. Create a YouTube channel with the same name and handle from the YouTube app or YouTube Studio.
4. Add a profile photo (a simple logo or a clear local photo you took) and a one-line bio. You will improve it in Module 3.

## 5. Turn on two-step verification

Do this before your first post. Use Google's {link('g-2sv', '2-Step Verification')} for the Google account behind YouTube (Google recommends its prompts, or a passkey, over SMS codes), and turn on two-factor authentication in Instagram's Accounts Centre security settings. Save the backup codes in a safe place offline. Module 14 covers account security in depth.

## 6. Rules from day 1

These protect you, the people you post about, and your future clients. Each one is explained fully in Module 14, but they apply from your first post:

{bullets(RULES)}

## 7. An AI assistant as your coach

The free plans of {link('gemini-plans', 'Gemini')}, {link('chatgpt-plans', 'ChatGPT')} and {link('claude-plans', 'Claude')} are enough for this course (limits change; check current rules). Save this prompt and paste it at the start of a session:

{fence(COACH_PROMPT)}

Never paste a client's private details, customers' phone numbers or your passwords into an AI tool. Module 13 covers AI properly.

## 8. Your calendar and a buddy

Block your weekly slots in Google Calendar, including the Saturday batch session and the Sunday review. Choose an accountability buddy: a friend who will ask you every Sunday, "How many posts this week, and what did you learn from the numbers?"

Every link on this page was checked on {VDATE}. The **Sources and verification log** at the end of the course lists each one with its status.
"""
    tasks = [
        ('smm-w0-folder', 'SMM Toolkit folder made in Google Drive, with its 18 subfolders'),
        ('smm-w0-workbook', 'SMM Workbook made, with all 9 tabs and their header rows'),
        ('smm-w0-phone', 'Phone ready: 5 GB free, apps installed, Malayalam typing works'),
        ('smm-w0-account', 'Practice account created on Instagram (professional) and YouTube, same handle'),
        ('smm-w0-2fa', 'Two-step verification on for Google and Instagram, backup codes saved'),
        ('smm-w0-rules', 'Rules from day 1 read and saved as a note on your phone'),
        ('smm-w0-ai', 'AI coach prompt saved and tried once'),
        ('smm-w0-calendar', 'Weekly slots in your calendar and an accountability buddy chosen'),
    ]
    return {
        'id': 'smm-w0',
        'title': 'Week 0: free toolkit, practice account and rules from day 1',
        'kind': 'setup',
        'weeks': [0, 0],
        'hours': 3.5,
        'summary': 'Free tools, one Drive folder, one workbook, a practice account with two-step verification, and the rules that apply from your first post.',
        'content': content.strip(),
        'tasks': [{'id': i, 'text': t, 'kind': 'task', 'week': 0} for i, t in tasks],
    }


SKILLS = [
    'Explain how recommendation systems decide what people see',
    'Turn a business goal into a social media objective and a KPI',
    'Describe a target audience from real research, not guesses',
    'Choose the right platform and format for a goal',
    'Write a hook that stops the scroll, in Malayalam and English',
    'Shoot a clear, well-lit video with clean sound on a phone',
    'Edit a short video on a phone, with captions and licensed music',
    'Design a readable carousel or YouTube thumbnail',
    'Write a caption with a clear call to action and no hype',
    'Plan and batch a week of content',
    'Use keywords and hashtags so people can find your posts',
    'Read Instagram and YouTube insights and decide what to change',
    'Make a UTM link and read the result in Google Analytics',
    'Plan and run a small, measured paid ad test',
    'Work with a creator and disclose the partnership correctly',
    'Audit a local business\'s social media and recommend fixes',
    'Follow Indian disclosure, copyright and consent rules',
    'Handle negative comments and secure an account',
    'Price, propose and report on a social media service',
    'Protect your energy and deal with trolls',
]

LEVELS = [
    ('1', 'Never heard of it, or can\'t do it'),
    ('2', 'Understand it, but haven\'t done it'),
    ('3', 'Can do it with help or a guide open'),
    ('4', 'Can do it alone, reliably'),
    ('5', 'Can teach it and do it for a client'),
]


def baseline_section():
    rows = [(str(i), s, '', '') for i, s in enumerate(SKILLS, 1)]
    content = f"""
Before you start, record where you are. You'll take exactly the same self-assessment in week 40 and compare. Be honest: low scores now make your progress visible later. It takes about 30 minutes.

## Part 1: rate 20 skills from 1 to 5

{table(['Score', 'Means'], LEVELS)}

Copy this table into a new tab called **Baseline** in your SMM Workbook. Fill in the **Start** column now; leave **End** for week 40.

{table(['No', 'Skill', 'Start (week 0)', 'End (week 40)'], rows)}

## Part 2: your account's starting numbers

Write these in the same tab. For a brand-new account most will be 0, and that's fine: a zero baseline makes the clearest before and after.

{fence('''ACCOUNT BASELINE (date: ____)
Handle and platforms: ____
Followers: Instagram ____  YouTube ____  other ____
Posts so far: ____
Average views of your last 9 posts: ____ (0 if none)
Accounts reached in the last 30 days: ____
Profile visits in the last 30 days: ____
Enquiries or DMs about anything you promote: ____''')}

## Part 3: three sentences

1. Why I am doing this course: ____
2. What I want to be able to do by week 40: ____
3. What usually stops me finishing things, and my plan for it: ____

Save a screenshot of the Baseline tab in **00 Baseline**.
"""
    return {
        'id': 'smm-baseline',
        'title': 'Baseline self-assessment (you repeat it at the end)',
        'kind': 'setup',
        'weeks': [0, 0],
        'hours': 0.5,
        'summary': 'Rate 20 skills, record your account\'s starting numbers and write why you are doing this. You take the same assessment in week 40.',
        'content': content.strip(),
        'tasks': [
            {'id': 'smm-baseline-skills', 'text': 'Baseline: 20 skills rated, Start column filled in', 'kind': 'task', 'week': 0},
            {'id': 'smm-baseline-account', 'text': 'Baseline: account starting numbers and three sentences written', 'kind': 'task', 'week': 0},
        ],
    }


def posting_section():
    cp_rows = [(str(w), t.split(': ', 1)[1], ev) for _, w, t, ev in CHECKPOINTS]
    content = f"""
Your account is the course's main practice ground. You post on a schedule from week 1 to week 39, log every post, and look at the numbers every Sunday. **This week** on the course page shows one checkpoint at a time.

## How often to post

{table(['Weeks', 'Part-time rhythm', 'What it is for'], [
    ('1–4', '2 posts a week, at least one short video', 'Build the habit; your early posts are your "before"'),
    ('5–13', '3 posts a week', 'Use each new skill from Modules 3–5 in a real post'),
    ('14–18', 'Every day: the 30-day challenge (SMM-M06-L04)', 'Volume, speed and lots of data'),
    ('19–26', '3 posts a week', 'Apply what the challenge numbers taught you'),
    ('27–39', 'Your 90-day sprint plan, usually 4 a week (SMM-M17-L01)', 'A focused, measured growth project'),
])}

**Full-time:** post every day from week 1. **Exam weeks:** two batched posts a week (see the weekly schedule).

Stories, Status updates and replies don't count as posts here, but do them too; they keep your existing audience close.

## What counts as a post

A Reel, a Short, a carousel, a photo post, a LinkedIn post or a YouTube video that is public on your practice account, that you made yourself and that follows the rules from day 1. Re-posting other people's content doesn't count, and platforms rank it lower anyway ({link('ig-reco', 'Instagram says')} it recommends original content).

## Log every post

Fill in a Posting Log row when you publish, then add the views after 24 hours and after 7 days. Every Sunday, add a Weekly Stats row and write one thing you'll change. This takes 10–15 minutes a week and is the most valuable habit in the course: it turns posting into learning.

## Checkpoints

{table(['Due by week', 'Checkpoint', 'Evidence'], cp_rows)}

The 30-day challenge (weeks 14–18) and the end of the 90-day sprint (week 39) are tracked in their lessons, SMM-M06-L04 and SMM-M17-L01.

## When a checkpoint is missed

Missing one is information, not failure. Ask why: too ambitious a format, no batch session, exam pressure, or a topic you dislike? Fix that one thing, then catch up by batching two weeks of simple posts on one Saturday.
"""
    return {
        'id': 'smm-posting',
        'title': 'Posting track: post on a schedule all course',
        'kind': 'track',
        'weeks': [1, 39],
        'summary': 'Post on a schedule from week 1 to week 39, log every post and review your numbers weekly. Ten checkpoints keep you on track.',
        'content': content.strip(),
        'tasks': [
            {'id': tid, 'text': text, 'kind': 'project', 'week': w,
             'detail': f'**Evidence:** {ev}. Paste the link to your Posting Log in this note.'}
            for tid, w, text, ev in CHECKPOINTS
        ],
    }


def front(modules):
    return [start_section(modules), schedule_section(modules), setup_section(), baseline_section(), posting_section()]


# ---------------------------------------------------------------- back matter

def final_section():
    rows = [(t, where) for _, t, where in TOOLKIT]
    content = f"""
Two things to finish the course: retake the baseline self-assessment, and check that your toolkit is complete.

## 1. Retake the self-assessment

Open the **Baseline** tab in your SMM Workbook and fill in the **End** column for all 20 skills, without looking at your start scores first. Then compare:

- Which three skills grew the most? Put them on your portfolio's About section.
- Any skill still at 1 or 2? Note which module covers it and plan one practice task in the next month.
- Write your account's numbers now next to the week 0 numbers: followers, average views of the last 9 posts, reach and profile visits in the last 30 days, and enquiries.

## 2. Check your toolkit

Each item should be a file or link in your SMM Toolkit folder that you could show a client or an employer tomorrow. If something is missing, the module listed has its template.

{table(['Toolkit item', 'Where the template is'], rows)}

## Before you call the course done

- Save a backup of your progress from **Backup and courses** in this app, and keep it in your SMM Toolkit folder.
- Download a copy of your SMM Workbook (File → Download) so you have it offline.
- Put your next Sunday review in your calendar. The course ends; posting and learning from your numbers don't.
"""
    tasks = [
        {'id': 'smm-final-reassess', 'text': 'Final self-assessment: End column filled in and compared with week 0', 'kind': 'exit', 'week': 40},
        {'id': 'smm-final-numbers', 'text': 'Account numbers at week 40 written next to your baseline', 'kind': 'task', 'week': 40},
    ] + [{'id': i, 'text': t, 'kind': 'task', 'week': 40} for i, t, _ in TOOLKIT]
    return {
        'id': 'smm-final',
        'title': 'Final self-assessment and toolkit checklist',
        'kind': 'capstone',
        'weeks': [40, 40],
        'hours': 1,
        'summary': 'Retake the baseline self-assessment, compare your account\'s numbers with week 0, and check that every part of your toolkit exists.',
        'content': content.strip(),
        'tasks': tasks,
    }


def next_section():
    content = f"""
Finishing the course is the start of the real work. Here is a sensible order for the next twelve months.

## The next 90 days: first paying clients

- Keep posting on your own account at a rhythm you can hold, and keep the Sunday review.
- Turn your pilot business into a paying client, or use the case study to win the next one. Aim for two or three small monthly retainers (Module 15).
- Ask every client for a testimonial and a referral when results are good, with their permission to share.

## Months 4–6: get solid

- Choose a niche you enjoy and can win in, such as restaurants and bakeries, clinics and gyms, or homestays, and build templates for it.
- Do the free certifications that clients and employers recognise: {link('hubspot-social', 'HubSpot Social Media')} and the {link('skillshop-ads', 'Google Ads')} certifications on Skillshop.
- Raise your prices once you have three case studies with real numbers.

## Months 7–12: choose your path

{table(['If you enjoy', 'Consider'], [
    ('Working with many local businesses', 'A small agency: one niche, two or three packages, a part-time helper (Module 15, ENT-M12-L03)'),
    ('One brand, steady pay and a team', 'Jobs such as social media executive or content creator; your portfolio is your CV'),
    ('Making content yourself', 'Growing your own channel towards YouTube Partner Program thresholds, affiliate income and brand deals (Module 10)'),
    ('Ads and numbers', 'Paid media specialist: go deeper into Meta and Google Ads with the free official courses'),
])}

## Keep learning, free

- {link('bp-free', 'Meta Blueprint free courses')}: ads, audiences and measurement
- {link('skillshop-ads')}: Search, Display, Video and Measurement paths
- {link('ga-academy', 'Analytics Academy')}: Google Analytics courses and certification
- {link('yt-creators')}: the Grow and Earn sections
- {link('os-pom')}: chapters 5, 13 and 16 in full
- The **Practical Entrepreneurship** course in this app, if you want to build your own business or agency properly

## Keep up with platform changes

Platform rules change every few months. Once a month, spend 20 minutes on the official sources: {link('ig-best', 'Instagram\'s creator best practices')}, {link('yt-creators', 'YouTube Creators')} and the policy pages in this course's sources log. When something changes, update your templates and tell your clients.

Every link on this page was checked on {VDATE}; see the **Sources and verification log** for each one's status.
"""
    return {
        'id': 'smm-next',
        'title': 'What next: your 12-month roadmap',
        'kind': 'reference',
        'summary': 'How to keep going after the course: first paying clients, then a niche and certifications, then an agency, a job or your own channel.',
        'content': content.strip(),
    }


GLOSSARY = [
    ('Social media marketing', 'സോഷ്യൽ മീഡിയ വിപണനം', 'Using social platforms to reach, engage and win customers'),
    ('Algorithm', 'അൽഗോരിതം (നിർദ്ദേശക്രമം)', 'The rules and models a platform uses to decide what to show'),
    ('Recommendation system', 'ശുപാർശ സംവിധാനം', 'The part of an app that picks posts for people who don\'t follow you'),
    ('Feed', 'ഫീഡ്', 'The stream of posts you scroll through'),
    ('Signal', 'സൂചന', 'A piece of information the system uses, such as watch time or shares'),
    ('Reach', 'എത്തിച്ചേരൽ', 'The number of different accounts that saw your post'),
    ('Views', 'കാഴ്ചകൾ', 'How many times your post was seen, counting repeats'),
    ('Impression', 'ഇംപ്രഷൻ (പ്രദർശനം)', 'One time your post or thumbnail was shown'),
    ('Engagement', 'ഇടപെടൽ', 'Likes, comments, shares, saves and other actions on a post'),
    ('Engagement rate', 'ഇടപെടൽ നിരക്ക്', 'Interactions divided by reach (or views), as a percentage'),
    ('Watch time', 'കണ്ട സമയം', 'The total time people spent watching your video'),
    ('Retention', 'പിടിച്ചുനിർത്തൽ', 'How much of your video people keep watching'),
    ('Hook', 'ആകർഷണ തുടക്കം', 'The first line or 1–3 seconds that make people stop and watch'),
    ('Call to action (CTA)', 'പ്രവർത്തനാഹ്വാനം', 'The clear next step you ask people to take'),
    ('Caption', 'അടിക്കുറിപ്പ്', 'The text that goes with a post'),
    ('Subtitles', 'ഉപശീർഷകങ്ങൾ (സബ്‌ടൈറ്റിൽ)', 'On-screen text of what is said in a video'),
    ('Thumbnail', 'ലഘുചിത്രം (തംബ്‌നെയിൽ)', 'The small image people see before they click a video'),
    ('Carousel', 'കറൗസൽ (സ്ലൈഡ് പോസ്റ്റ്)', 'A post with several photos or slides to swipe through'),
    ('Reel', 'റീൽ', 'A short vertical video on Instagram or Facebook'),
    ('Short', 'ഷോർട്ട്', 'A short vertical or square video on YouTube'),
    ('Story', 'സ്റ്റോറി', 'A post that disappears after 24 hours'),
    ('Status', 'സ്റ്റാറ്റസ്', 'WhatsApp\'s 24-hour updates, seen by your contacts'),
    ('Broadcast', 'പ്രക്ഷേപണ സന്ദേശം', 'One message sent privately to many contacts'),
    ('Channel', 'ചാനൽ', 'A one-way feed of updates that people follow'),
    ('Community', 'സമൂഹം (കമ്മ്യൂണിറ്റി)', 'A group of people who interact around shared interests'),
    ('Niche', 'പ്രത്യേക മേഖല', 'The specific topic and audience an account serves'),
    ('Target audience', 'ലക്ഷ്യ പ്രേക്ഷകർ', 'The people you most want to reach'),
    ('Persona', 'ഉപഭോക്തൃ മാതൃക', 'A profile of a typical person in your audience, based on research'),
    ('Positioning', 'സ്ഥാനനിർണയം', 'The place you want to hold in your audience\'s mind'),
    ('Competitor analysis', 'എതിരാളി വിശകലനം', 'Studying similar accounts to learn and find gaps'),
    ('Content pillar', 'ഉള്ളടക്ക സ്തംഭം', 'One of the 3–5 main themes you post about'),
    ('Brand voice', 'ബ്രാൻഡ് ശബ്ദം', 'The consistent personality and tone of your writing'),
    ('Funnel', 'ഫണൽ (വിൽപന വഴി)', 'The stages from first seeing you to buying and recommending'),
    ('Awareness', 'അവബോധം', 'The stage where people first learn you exist'),
    ('Consideration', 'പരിഗണന', 'The stage where people compare and think about buying'),
    ('Conversion', 'പരിവർത്തനം', 'The moment someone takes the action you want, such as buying'),
    ('Loyalty', 'വിശ്വസ്തത', 'Customers coming back again and again'),
    ('Objective', 'ഉദ്ദേശ്യം', 'What social media should achieve for the business'),
    ('KPI (key performance indicator)', 'പ്രധാന പ്രകടന സൂചകം', 'The main number that shows whether you are meeting a goal'),
    ('Vanity metric', 'പൊങ്ങച്ച സംഖ്യ', 'A number that looks good but doesn\'t show business results'),
    ('Content calendar', 'ഉള്ളടക്ക കലണ്ടർ', 'A plan of what to post, where and when'),
    ('Batching', 'ഒന്നിച്ചു തയ്യാറാക്കൽ', 'Making several posts in one session'),
    ('Repurposing', 'പുനരുപയോഗം', 'Turning one idea or video into posts for several platforms'),
    ('Scheduling', 'സമയക്രമീകരണം', 'Setting a post to publish automatically later'),
    ('Template', 'മാതൃകാരൂപം (ടെംപ്ലേറ്റ്)', 'A ready layout or text you reuse'),
    ('Keyword', 'മുഖ്യപദം', 'A word or phrase people type when they search'),
    ('Hashtag', 'ഹാഷ്‌ടാഗ്', 'A word with # that groups posts on a topic'),
    ('Social SEO', 'സോഷ്യൽ തിരയൽ ക്രമീകരണം', 'Making posts easy to find in a platform\'s search'),
    ('Alt text', 'ചിത്ര വിവരണം', 'A text description of an image for screen readers and search'),
    ('Trend', 'പ്രവണത (ട്രെൻഡ്)', 'A topic, sound or format many people are using right now'),
    ('Collaboration (collab)', 'സഹകരണം', 'A post or project made together with another account'),
    ('Direct message (DM)', 'നേരിട്ടുള്ള സന്ദേശം', 'A private message to an account'),
    ('Insights (analytics)', 'സ്ഥിതിവിവരക്കണക്കുകൾ', 'The numbers a platform gives about your posts and audience'),
    ('Click-through rate (CTR)', 'ക്ലിക്ക് നിരക്ക്', 'Clicks divided by impressions, as a percentage'),
    ('UTM link', 'യുടിഎം ലിങ്ക് (ട്രാക്കിംഗ് ലിങ്ക്)', 'A link with tags that tell Google Analytics where a visitor came from'),
    ('A/B test', 'താരതമ്യ പരീക്ഷണം', 'Trying two versions to see which works better'),
    ('Hypothesis', 'അനുമാനം', 'A guess you can test, such as "a question hook gets more views"'),
    ('Report', 'റിപ്പോർട്ട് (വിവരണപത്രിക)', 'A summary of results and next steps for a client'),
    ('Boost', 'ബൂസ്റ്റ്', 'Paying to show an existing post to more people'),
    ('Ads Manager', 'ആഡ്‌സ് മാനേജർ', 'Meta\'s full tool for creating and measuring ads'),
    ('Campaign', 'പ്രചാരണം (ക്യാമ്പെയ്ൻ)', 'A planned set of posts or ads with one goal and a time limit'),
    ('Targeting', 'ലക്ഷ്യമിടൽ', 'Choosing who sees your ad'),
    ('Budget', 'ബജറ്റ് (ചെലവ് പരിധി)', 'The most money you will spend'),
    ('Cost per result', 'ഓരോ ഫലത്തിനുമുള്ള ചെലവ്', 'Ad spend divided by the number of results'),
    ('Retargeting', 'പുനർലക്ഷ്യമിടൽ', 'Showing ads to people who already interacted with you'),
    ('Return on investment (ROI)', 'നിക്ഷേപത്തിന്മേലുള്ള ആദായം', 'Profit gained compared with money spent'),
    ('ROAS', 'പരസ്യച്ചെലവിന്മേലുള്ള വരുമാനം', 'Revenue from ads divided by ad spend'),
    ('Influencer', 'സ്വാധീനശക്തിയുള്ളയാൾ (ഇൻഫ്ലുവൻസർ)', 'Someone whose content affects what their audience buys or thinks'),
    ('Micro-influencer', 'ചെറുകിട ഇൻഫ്ലുവൻസർ', 'A creator with a small but close, often local, audience'),
    ('UGC (user-generated content)', 'ഉപയോക്തൃ ഉള്ളടക്കം', 'Content made by customers or creators rather than the brand'),
    ('Affiliate marketing', 'അഫിലിയേറ്റ് വിപണനം', 'Earning a commission when people buy through your link'),
    ('Monetisation', 'വരുമാനമാക്കൽ', 'Earning money from content or an audience'),
    ('Disclosure', 'വെളിപ്പെടുത്തൽ', 'Clearly saying that a post is paid, gifted or connected to a brand'),
    ('Material connection', 'ഭൗതിക ബന്ധം', 'Any link with a brand, such as payment or free products, that must be disclosed'),
    ('Endorsement', 'അംഗീകാര പ്രസ്താവന', 'Recommending a product as if from your own experience'),
    ('Copyright', 'പകർപ്പവകാശം', 'Ownership of original creative work, such as music, photos and videos'),
    ('Licence', 'ഉപയോഗാനുമതി (ലൈസൻസ്)', 'Permission to use someone\'s work under set conditions'),
    ('Consent', 'സമ്മതം', 'Clear permission from a person before you film or post them'),
    ('Fake engagement', 'വ്യാജ ഇടപെടൽ', 'Bought or automated likes, follows, views or reviews'),
    ('Engagement bait', 'ഇടപെടൽ കെണി', 'Posts that beg for likes, comments or shares to trick the algorithm'),
    ('Dark pattern', 'വഞ്ചനാപരമായ രൂപകൽപ്പന', 'A design trick that pushes people into choices they didn\'t intend'),
    ('Crisis', 'പ്രതിസന്ധി', 'A problem that spreads fast and can damage a reputation'),
    ('Troll', 'ട്രോൾ (ശല്യക്കാരൻ)', 'Someone who posts to provoke or hurt, not to discuss'),
    ('Two-step verification', 'ഇരട്ട സ്ഥിരീകരണം', 'A second check, besides your password, when you log in'),
    ('Phishing', 'ഫിഷിംഗ് (തട്ടിപ്പ് സന്ദേശം)', 'A fake message or page that tries to steal your login'),
    ('Google Business Profile', 'ഗൂഗിൾ ബിസിനസ് പ്രൊഫൈൽ', 'A free listing that shows a business on Google Search and Maps'),
    ('Social commerce', 'സോഷ്യൽ വ്യാപാരം', 'Selling directly through social apps and chats'),
    ('Catalogue', 'ഉൽപ്പന്ന പട്ടിക', 'A list of products or services with photos and prices'),
    ('Review', 'അഭിപ്രായം (റിവ്യൂ)', 'A customer\'s public opinion of a business'),
    ('Testimonial', 'സാക്ഷ്യപത്രം', 'A customer\'s quote about you, shared with their permission'),
    ('Audit', 'പരിശോധന (ഓഡിറ്റ്)', 'A structured check of what an account does well and badly'),
    ('Pilot', 'പരീക്ഷണ പദ്ധതി', 'A short trial project to show results before a paid contract'),
    ('Case study', 'കേസ് സ്റ്റഡി (വിജയകഥ)', 'A short story of a project with before and after numbers'),
    ('Portfolio', 'പ്രവൃത്തി ശേഖരം', 'A collection of your best work to show clients'),
    ('Personal brand', 'വ്യക്തിഗത ബ്രാൻഡ്', 'What people know and trust you for'),
    ('Retainer', 'മാസവരി കരാർ', 'A monthly fee for ongoing work'),
    ('Proposal', 'നിർദ്ദേശപത്രിക', 'A document that offers your service, price and plan to a client'),
    ('Onboarding', 'തുടക്ക നടപടികൾ', 'The steps to start work with a new client'),
    ('Agency', 'ഏജൻസി', 'A business that does marketing work for several clients'),
    ('Burnout', 'അമിതജോലി മൂലമുള്ള തളർച്ച', 'Exhaustion from long-term work stress that isn\'t managed'),
    ('Synthetic content', 'കൃത്രിമമായി നിർമ്മിച്ച ഉള്ളടക്കം', 'AI-generated or AI-altered images, video or audio that look real'),
]


def glossary_section():
    rows = [(f'**{en}**', ml, meaning) for en, ml, meaning in GLOSSARY]
    content = f"""
Key words from the course, roughly in the order you meet them. Many English words, such as Reel, hashtag and brand, are used as they are in Malayalam conversation; the Malayalam is given so you can explain them to shop owners and family.

{table(['English', 'മലയാളം (Malayalam)', 'Simple meaning'], rows)}
"""
    return {
        'id': 'smm-glossary',
        'title': 'Glossary with Malayalam meanings',
        'kind': 'reference',
        'summary': f'{len(GLOSSARY)} key social media marketing terms in English and Malayalam, with simple meanings.',
        'content': content.strip(),
    }


def back(modules):
    return [final_section(), next_section(), glossary_section()]


def finish(course):
    """Add the sources page, built from every link the course actually uses."""
    sections = course['sections']
    used_in = {}
    for s in sections:
        texts = [s.get('content', ''), s.get('summary', '')] + [t.get('detail', '') for t in s.get('tasks', [])]
        blob = '\n'.join(texts)
        code = s['title'].split(':')[0]
        for key, r in R.items():
            if f"]({r['url']})" in blob:
                used_in.setdefault(key, [])
                if code not in used_in[key]:
                    used_in[key].append(code)
    groups = {}
    for key in used_in:
        groups.setdefault(R[key]['group'], []).append(key)
    order = ['YouTube and Google help', 'Meta: Instagram, Facebook, WhatsApp and Threads', 'Other platforms',
             'News reports on platform changes', 'Free courses and guides', 'Free apps for your phone',
             'Free and open-source software for the laptop', 'Malayalam fonts and typing', 'AI tools',
             'India: rules and law', 'Earning programmes', 'Help and safety', 'Other']
    parts = [f"""
Every link in this course is listed here with the date it was checked. Links were opened and read on {VDATE}; nothing here was copied from memory. If a link stops working, search for its title on the same website.

- **verified {VDATE}:** the page was opened and its content matched what the course says.
- **verified {VDATE} (page title checked):** the page only shows its text in a full browser, so its title and description were checked. The facts the course takes from it come from another linked source.
- **check current rules:** a rule, feature, limit or fee that changes often. Open the official source before you act or advise a client.
- **unverified:** the site blocks automated checks, so the page could not be opened for this course. The address is the official one named by other government sources; type it yourself and check it is the real site.

Several Meta help pages (facebook.com and parts of WhatsApp's help) block automated checks completely, so this course doesn't link to them; it uses Meta's readable official blogs, the Blueprint course pages and dated news reports instead. OpenStax *Principles of Marketing* is licensed CC BY-NC-SA 4.0 and this course only links to it.
"""]
    for g in order:
        if g not in groups:
            continue
        rows = []
        for key in groups[g]:
            r = R[key]
            where = ', '.join(used_in[key][:6]) + (' and more' if len(used_in[key]) > 6 else '')
            rows.append((f"[{r['title']}]({r['url']})", where, STATUS[r['s']]))
        parts.append(f'## {g}\n\n' + table(['Resource', 'Used in', 'Status'], rows))
    unverified = [k for k in used_in if R[k]['s'] == 'u']
    rules_keys = [k for k in used_in if R[k]['s'] == 'vr']
    parts.append('## Marked "unverified"\n\n' + bullets([f"[{R[k]['title']}]({R[k]['url']})" for k in unverified]))
    parts.append('## Marked "check current rules"\n\n' + bullets([f"[{R[k]['title']}]({R[k]['url']})" for k in rules_keys]))
    sections.append({
        'id': 'smm-sources',
        'title': 'Sources and verification log',
        'kind': 'reference',
        'summary': f'Every link in the course, where it is used and when it was checked ({VDATE}).',
        'content': '\n\n'.join(p.strip() for p in parts),
    })
