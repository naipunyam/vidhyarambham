from common import lesson, module, link, ASOF

L1 = lesson(
    4, 1,
    title='Hooks, scripts and storytelling',
    weeks=(8, 8), hours=3,
    outcome='Write hooks that stop the scroll, structure short videos and carousels as small stories that keep people watching, and use copy-ready script formats for Reels, Shorts, carousels and long videos.',
    split='50 minutes study, 2 hours 10 minutes action',
    core="""
### The first three seconds decide everything

People scroll fast. Instagram's advice to creators is to hook viewers in the first 3 seconds and watch the **View Rate** in Insights; YouTube's retention report shows an **Intro** figure for long videos: the share of viewers still watching after the first 30 seconds. Both are telling you the same thing: if the opening doesn't earn attention, nothing after it matters.

A strong hook works on three layers at once:

- **Visual:** movement, a face, a finished result, a surprising object, in the very first frame
- **Text on screen:** 3–7 words that make the promise, readable without sound
- **Spoken:** the first sentence, said directly and quickly, with no "Hi guys, welcome back"

### Ten hook types that work in any niche

| Hook type | Example |
| --- | --- |
| Result first | Show the finished biryani, then "Here's how ₹150 gets you this in Kuttiady" |
| Question | "Why is this tea shop full at 6 am every day?" |
| Number or list | "3 places to eat under ₹100 near the bus stand" |
| Mistake | "Stop doing this when you charge your phone" |
| Before and after | A dull shop counter, then the same counter rearranged |
| "Watch before you..." | "Watch this before you order a birthday cake" |
| Myth vs fact | "Pickles must be full of preservatives? Not these." |
| Local surprise | "This 60-year-old shop still makes soda in glass bottles" |
| Direct address | "Kuttiady people, this is for you" |
| Curiosity gap | "The owner told me why he never raises the price" |

Rules: the hook must be **true** and the video must **deliver it**. A hook that tricks people makes them leave early and feel cheated, and the system notices both.

### Keep the promise: retention

- **Get to the point.** Cut every pause, every "um" and every second that doesn't move the story.
- **Change something every few seconds:** a new shot, a zoom, a new caption line, a sound.
- **Pay off the hook** before the end, then stop. Don't add a long outro.
- **End well:** a clear call to action ("Save this for Saturday") or a loop that flows back to the start.

### Stories, not information

Facts are forgotten; stories are shared. Five structures you can reuse:

1. **Problem → struggle → solution** ("My phone died every afternoon... until the shop showed me this")
2. **Before → after → bridge** (show both, then how)
3. **Mistake → lesson**
4. **How it's made / behind the scenes**
5. **Person story:** a shop owner's 45-second story in their own words (with consent)

### Scripts save time

Even a 30-second Reel goes faster with a script: you shoot only what you need. Write it in the template below, read it aloud once, cut 20% of the words, then shoot.

### AI can help brainstorm

An AI assistant can suggest twenty hook ideas in a minute. Use it to get unstuck, then choose, check the facts and rewrite in your own voice. Module 13 covers the risks, such as generic, same-sounding hooks and made-up facts.
""",
    example="""
Nisha's Oven wanted a Reel about her eggless chocolate cake. Her first draft started "Hi everyone, today I'm going to show you..." and people left in the first two seconds: in Insights, most viewers didn't make it past the start.

Her rewrite, scripted in 5 minutes:

| Time | Shot | On-screen text | Voiceover (Malayalam) |
| --- | --- | --- | --- |
| 0–2 s | Knife cutting into a gooey slice | "Eggless. You won't believe it." | "ഇതിൽ മുട്ടയില്ല!" |
| 2–8 s | Mixing bowl, three ingredients | "The secret: curd + one trick" | "രഹസ്യം തൈരും ഒരു ചെറിയ സൂത്രവും" |
| 8–20 s | Batter in the tin, oven, timer | "40 min at low heat" | "ചെറിയ ചൂടിൽ 40 മിനിറ്റ്" |
| 20–27 s | Slice on a plate, a child's hand reaching (her own child, filmed by her) | "₹650 for 1 kg, order by 6 pm" | "നാളത്തേക്ക് ഓർഡർ ചെയ്യൂ" |
| 27–30 s | Back to the cut slice (loops to the start) | "Order on WhatsApp 👇" | — |

The new version kept more viewers past the first 3 seconds and brought 11 WhatsApp enquiries in a week, against 2 for the first one.

(Made-up example to show the method.)
""",
    resources=[
        ('ig-reco', 'Re-read the "make engaging reels" tips: vertical video, 3-second hook, no watermarks', '5 min'),
        ('ig-small', 'Re-read the tips on hooks and View Rate', '5 min'),
        ('yt-retention', 'Read about the Intro, top moments, spikes and dips in retention', '10 min'),
        ('yt-shorts-guide', 'Read the steps for recording, adding sound and editing a Short', '15 min'),
        ('hubspot-social', 'Watch the lesson on social content strategy (lesson names may change)', '15 min'),
    ],
    steps=[
        'Study the resources (about 50 minutes).',
        'Write 10 hooks for your pillars, using at least 5 different hook types. Add them to the Hooks and Captions tab.',
        'Write 3 short-video scripts (30–60 seconds) with the template, each with a different story structure.',
        'Write 1 carousel script (6–10 slides) with the carousel template.',
        'Record and post the strongest script this week. Log it, and after 7 days compare its views and watch time with your earlier videos.',
    ],
    proof='Your 10 hooks, 3 video scripts and 1 carousel script, and the link to the posted video with its Posting Log row.',
    templates=[
        ('short video script (Reel or Short, 30-60 seconds)', """
TITLE: ____________  PILLAR: ________  LENGTH: ___ s
HOOK (0-3 s)
  Visual: ______________________________
  On-screen text (3-7 words): ___________
  First sentence: ______________________
SET-UP (3-10 s): why this matters ______
VALUE (10-45 s): 2-4 beats, one shot each
  1. ____________  2. ____________
  3. ____________  4. ____________
PAYOFF (last 5-10 s): ___________________
CALL TO ACTION: save / share / follow / WhatsApp
SHOT LIST: ____________________________
MUSIC: none / platform library / Audio Library
CONSENT NEEDED FROM: __________________
""", ''),
        ('carousel script (6-10 slides)', """
Slide 1 (cover): hook + promise, max 8 words
Slide 2: the problem or why it matters
Slides 3-8: one idea per slide, a short headline
            and 1-2 lines of text each
Slide 9: summary or "the one thing to remember"
Slide 10: call to action (save, share, DM, visit)
Caption first line repeats the hook in words.
""", ''),
        ('long video outline (YouTube)', """
0:00-0:30  Hook and promise (what they'll get)
0:30-1:00  Why trust you / what you checked
CHAPTER 1: ____________ (00:00 must be listed first)
CHAPTER 2: ____________
CHAPTER 3: ____________
PAYOFF: the answer or result, clearly
END (last 20 s): one call to action, one next video
""", ''),
    ],
    mistakes=[
        ('Starting with a greeting or your logo.', 'Start with the most interesting moment. Introduce yourself later, or not at all.'),
        ('Clickbait.', 'A hook the video doesn\'t deliver makes people leave and stop trusting you.'),
        ('Explaining everything.', 'One idea per short video. Save the rest for the next post.'),
        ('Scripts that sound written.', 'Read them aloud; cut long sentences; say it the way you\'d tell a friend.'),
        ('No call to action.', 'Tell people the one thing to do next.'),
    ],
    quiz=[
        {'q': 'Which opening is the strongest hook?',
         'o': ['"Hi everyone, welcome back to my page"', 'The finished result in the first frame with "₹150 gets you this in Kuttiady"', 'Your logo for 3 seconds', 'A long caption'],
         'a': 'B', 'why': 'It shows the result immediately and makes a clear, local promise.'},
        {'q': 'What does YouTube\'s "Intro" retention figure show?',
         'o': ['Your subscriber count', 'The share of viewers still watching after the first 30 seconds', 'The number of likes', 'Your upload schedule'],
         'a': 'B', 'why': 'It shows whether your opening matched what the title and thumbnail promised.'},
        {'q': 'Why must a hook be true?',
         'o': ['It isn\'t important', 'If the video doesn\'t deliver, people leave early and stop trusting you, and the system notices', 'Platforms read every hook', 'True hooks are shorter'],
         'a': 'B', 'why': 'Satisfaction and watch time fall when a hook misleads.'},
        {'q': 'A good way to end a short video is:',
         'o': ['A 20-second outro with music', 'A clear call to action or a loop back to the start', 'Fading to black slowly', 'Repeating the intro'],
         'a': 'B', 'why': 'Stop after the payoff and give one next step.'},
    ],
    study='Instagram\'s and YouTube\'s guidance on hooks and retention, YouTube\'s Shorts guide and HubSpot\'s content lesson (about 50 minutes)',
    action='write 10 hooks, 3 video scripts and a carousel script, then post the best one',
)

L2 = lesson(
    4, 2,
    title='Malayalam and English content',
    weeks=(8, 8), hours=1.5,
    outcome='Decide when to use Malayalam, English or both, type and design Malayalam text that renders correctly, add accurate subtitles, and test a post in two language versions.',
    split='20 minutes study, 1 hour 10 minutes action',
    core=f"""
### Choose the language for the job

| Language | Strengths | Watch out for |
| --- | --- | --- |
| **Malayalam** | Trust, warmth and humour for local audiences; older viewers; strong emotion | Smaller reach outside Kerala; some search happens in English |
| **English** | Search, people from other states, professional audiences (LinkedIn), some Gulf followers | Can feel distant to local customers |
| **Both** | Malayalam speech or text plus an English caption line reaches both groups | Two languages crammed on screen become unreadable |
| **Manglish** (Malayalam in English letters) | Natural in comments and chats for many young people | Hard for some older readers; looks informal; inconsistent spelling hurts search |

Your research (SMM-M02-L02) is the guide: use the language your audience uses in its own posts and messages. Many local pages do well with **Malayalam speech, short Malayalam on-screen text, and an English first line in the caption** that carries the keywords people search for.

### Typing Malayalam on your phone

- **Gboard:** add Malayalam from Gboard's settings (Languages → Add keyboard), then hold the space bar to switch languages.
- **Indic Keyboard:** a free, open-source keyboard from the Malayalam computing community, with transliteration: type "kuttiady" in English letters and pick കുറ്റ്യാടി.

### Fonts that render Malayalam correctly

Malayalam has conjunct letters and chillu letters that some fonts break. Use fonts made for Malayalam, such as **Manjari** (Malayalam and Latin), **Chilanka** (handwriting style) or **Noto Sans Malayalam**, all on Google Fonts. Swathanthra Malayalam Computing, which created Manjari and Chilanka, notes that Google Fonts only includes fonts under free licences. Always check a finished design for broken letters before you post.

### Subtitles and captions

Many people watch without sound, so on-screen captions are essential.

- **In editing apps:** use auto-captions, then correct every word; automatic Malayalam captions often contain mistakes.
- **On YouTube:** set the video's language correctly. YouTube's automatic captions come from speech recognition and are made in the video's default language only, so for English subtitles on a Malayalam video, add a second track in YouTube Studio → Subtitles: upload a file, auto-sync a transcript, or type them yourself ({ASOF}).

### Translation without embarrassment

- Don't paste machine translations straight into posts. Ask a native speaker to check, and rewrite idioms rather than translating them word for word.
- Local words and Malabar expressions make posts feel real; never use a dialect or accent to mock anyone.
- Keep spellings consistent, especially place names, so people can search for them.
""",
    example="""
**Amma's Pickles** tested the same Reel (a jar of mango pickle being filled) in two versions, one week apart:

| Version | Speech | On-screen text | Caption first line | Views (7 days) | WhatsApp enquiries |
| --- | --- | --- | --- | --- | --- |
| A | Malayalam | Malayalam only | Malayalam only | 2,100 | 9 |
| B | Malayalam | Malayalam, 4 words | "Malabar mango pickle, home-made in Perambra" | 3,400 | 14 |

Version B reached more people outside the immediate area, including Gulf-based Malayalis searching for "Malabar pickle", without losing local viewers. They kept B's pattern. One test isn't proof, so they planned to repeat it with two more products.

(Made-up numbers to show the method.)
""",
    resources=[
        ('gboard-ml', 'Follow the steps to add Malayalam and switch languages', '5 min'),
        ('indic-kbd', 'Install it if you want transliteration from English letters', '5 min'),
        ('font-manjari', 'Look at the Malayalam samples; download if you design on the laptop', '3 min'),
        ('font-chilanka', 'See the handwriting-style alternative', '2 min'),
        ('smc-fonts', 'Read the short post about these fonts in Google Fonts and Docs (in Malayalam)', '5 min'),
        ('yt-captions', 'Read the three ways to add subtitles on YouTube', '5 min'),
    ],
    steps=[
        'Study the resources (about 25 minutes) and set up Malayalam typing on your phone.',
        'Write your language rules: speech, on-screen text, caption first line, hashtags. Add them to your voice chart from SMM-M02-L04.',
        'Make one post in two language versions (like the example) and plan to publish them a week apart at a similar time.',
        'For a video with speech, correct the auto-captions word by word. On YouTube, add a second subtitle track in the other language.',
        'Check every Malayalam design for broken letters at full size on your phone.',
    ],
    proof='Your written language rules, links to both versions of the test post with their Posting Log rows, and a screenshot of corrected captions or a second subtitle track.',
    templates=[
        ('bilingual caption template', """
LINE 1 (English, with the search keywords):
  Malabar mango pickle, home-made in Perambra
LINES 2-3 (Malayalam, the story or the detail):
  അമ്മയുടെ കൈപ്പുണ്യം, ദിവസവും പുതിയ ബാച്ച്.
  250 ഗ്രാം ₹120.
CALL TO ACTION (both):
  Order on WhatsApp / വാട്സാപ്പിൽ ഓർഡർ ചെയ്യൂ: [number]
HASHTAGS (max 5): #malabarpickle #perambra
  #kozhikodefood #homemade #kudumbashree
""", ''),
        ('language and subtitle checklist', """
[ ] Language chosen from audience research, not habit
[ ] On-screen text: one language, max 7 words a line
[ ] Malayalam font checked for broken letters
[ ] Place names spelled the same way every time
[ ] Auto-captions corrected word by word
[ ] YouTube video language set correctly
[ ] Second subtitle track added (if useful)
[ ] Translations checked by a native speaker
[ ] No dialect used to mock anyone
""", ''),
    ],
    mistakes=[
        ('Two languages crammed on screen.', 'Pick one language for on-screen text; use the caption for the other.'),
        ('Unchecked auto-captions.', 'Wrong captions look careless and can change the meaning. Fix every word.'),
        ('Fonts that break Malayalam.', 'Use Manjari, Chilanka or Noto Sans Malayalam, and check at full size.'),
        ('Inconsistent place-name spellings.', 'Choose one spelling (Kuttiady) and use it everywhere so search works.'),
    ],
    quiz=[
        {'q': 'YouTube\'s automatic captions are made in:',
         'o': ['Every language', 'The video\'s default language only', 'English only', 'Malayalam only'],
         'a': 'B', 'why': 'For another language, add a subtitle track yourself.'},
        {'q': 'Which pattern often reaches both local and wider audiences?',
         'o': ['Manglish on screen and in the caption', 'Malayalam speech and short Malayalam text, with an English first line in the caption', 'English speech only', 'No text at all'],
         'a': 'B', 'why': 'The English line carries searchable keywords while the video stays local.'},
        {'q': 'Why use fonts such as Manjari or Noto Sans Malayalam?',
         'o': ['They are the only legal fonts', 'They are designed to render Malayalam letters correctly', 'They make posts go viral', 'Canva requires them'],
         'a': 'B', 'why': 'Some fonts break conjuncts and chillu letters.'},
    ],
    study='Malayalam typing, fonts and YouTube subtitles (about 25 minutes)',
    action='write your language rules and test one post in two language versions with corrected captions',
)

L3 = lesson(
    4, 3,
    title='Shooting on your phone: light, sound and framing',
    weeks=(9, 9), hours=4,
    outcome='Shoot clear, well-lit, steady vertical video with clean sound on an ordinary Android phone, using free tools and things you already have at home.',
    split='45 minutes study, 3 hours 15 minutes action',
    core="""
### Set up the phone before you shoot

- **Clean the lens** with a soft cloth. A smudged lens is the most common cause of hazy video.
- **Free up space** and charge the battery. Turn on Do Not Disturb so a call doesn't stop the recording.
- **Resolution:** 1080p at 30 frames per second is enough for social media and keeps files small on older phones. Use 4K only if your phone handles it smoothly.
- **Grid lines on** (in the camera settings) to help framing.
- **Lock focus and exposure:** tap and hold on your subject until the camera shows a lock, so brightness doesn't jump around.
- **Shape:** vertical 9:16 for Reels, Shorts and Stories; horizontal 16:9 for long YouTube videos. Decide before you press record.
- **Want manual control?** The free, open-source **Open Camera** app has manual controls, exposure lock and grids.

### Light: the cheapest upgrade

- **Face a window.** Soft daylight from the front or the side is the best free light. Put the window behind the phone, not behind the person.
- **Avoid harsh noon sun and bare tube lights overhead,** which make dark eye shadows. Outdoors, step into open shade.
- **Golden hour** (soon after sunrise and before sunset) gives warm, soft light for places and food.
- **Bounce light** with a white chart paper or a sheet of thermocol to brighten shadows; it costs a few rupees.
- **Keep it consistent** for a series, so your posts look like they belong together.

### Sound matters more than picture

Viewers forgive slightly soft video; they leave when they can't hear clearly.

- **Record in a quiet room** with soft things around (curtains, a bed, cupboards of clothes). Turn off fans and the TV.
- **Get the microphone close:** hold the phone at arm's length or closer when talking to camera.
- **Use what you have:** the wired earphones that came with many phones have a mic you can clip near your collar. A cheap clip-on microphone is an optional upgrade later.
- **Record voiceovers separately,** in the quietest corner, even under a blanket, then add them in the editor.
- **On the laptop,** Audacity is a free, open-source audio editor for recording and cleaning up voice.

### Framing

- **Eye level:** put the phone at the height of the person's eyes, not below the chin.
- **Rule of thirds:** place the eyes or the main object on a grid line, not dead centre.
- **Safe zones:** in vertical video the top and bottom are covered by the app's buttons and captions, so keep faces and text in the middle.
- **Clean background:** move clutter, switch off a flickering bulb, choose a plain wall.
- **Steady:** lean on a wall, rest the phone on a stack of books, hold with two hands and elbows tucked in. A phone stand is optional.
- **Hands-free:** the YouTube Shorts camera has a timer for hands-free recording.

### Shoot for the edit

For a 30-second Reel, shoot 8–12 short clips of 3–6 seconds each: a **wide** shot to show the place, **medium** shots of people or actions, and **close-ups** of details (hands, food, products). Shoot each action twice. These extra clips, called **B-roll**, make editing easy.

### Consent and safety while filming

- Ask before you film people, and ask shop owners before you film inside their shop. For children, ask a parent.
- Some places don't allow filming; respect the signs and the staff.
- Never film while driving or riding.
""",
    example="""
Anu filmed a "Shop story" Reel at a tailoring shop in Kuttiady town. Her first attempt was in the shop's back room under a tube light, with the tailor's sewing machine running: dark eyes, harsh shadows and a voice you could hardly hear.

Second attempt, same day, with zero spend:

- She moved the stool near the front door so daylight fell on his face from the side.
- She asked for the machine to be switched off while he spoke, and recorded the machine sounds separately as background.
- She clipped her own wired earphones to his collar and recorded his voice on a second phone placed in his shirt pocket, as a backup.
- She shot 11 clips: wide shot of the shop, his hands on the machine, the measuring tape, his face as he laughed, the finished shirt.
- She asked his permission on camera and saved it in her consent note.

The Reel was a 40-second story of a tailor who has worked on the same street for 31 years. It became her most-shared post that month.

(Made-up example to show the method.)
""",
    resources=[
        ('yt-shorts-guide', 'Read the recording steps: hold or tap to record, the timer and combining clips', '10 min'),
        ('opencamera', 'Read the feature list; install it if your camera app has no manual controls', '5 min'),
        ('ig-best', 'In "Creation", read the Reels pages', '15 min'),
        ('audacity', 'Optional, on the laptop: read what Audacity does', '5 min'),
    ],
    steps=[
        'Study the resources (about 35 minutes) and set up your camera: lens cleaned, 1080p 30 fps, grid on, Do Not Disturb.',
        'Light test: record the same 10-second talking clip in three places (under a tube light, facing a window, in open shade outside). Compare them on your phone and note the best.',
        'Sound test: record 10 seconds at arm\'s length with the phone mic, then with wired earphones clipped near your collar. Listen with earphones and note the difference.',
        'Write a shot list for one Reel (8–12 clips: wide, medium, close-ups, plus B-roll).',
        'Shoot it, with consent from anyone in it, and keep the clips for the editing lesson (SMM-M04-L04). If you can, edit it simply now and post it.',
    ],
    proof='Your three light-test clips and two sound-test clips (or screenshots and notes), your shot list, and the folder of clips for your Reel.',
    templates=[
        ('shooting checklist', """
BEFORE
[ ] Lens cleaned  [ ] Battery 50%+  [ ] 2 GB free
[ ] Do Not Disturb on  [ ] 1080p 30 fps  [ ] Grid on
[ ] Shape decided: vertical 9:16 / horizontal 16:9
[ ] Consent asked (people, shop, parents of children)
LIGHT
[ ] Facing a window or in open shade
[ ] No bright window behind the subject
[ ] Focus and exposure locked (tap and hold)
SOUND
[ ] Fan, TV, machines off  [ ] Mic close
[ ] 5 seconds of silence recorded (room tone)
FRAMING
[ ] Eye level  [ ] Subject on a third
[ ] Faces and text away from top and bottom
[ ] Background tidy  [ ] Phone steady
SHOTS
[ ] Wide  [ ] Medium  [ ] Close-ups  [ ] B-roll
[ ] Each action twice
""", ''),
        ('shot list', """
Shot,Type (wide/medium/close/B-roll),What happens,Length (s),Done?
1,Wide,Shop front with sign,4,
2,Medium,Owner at work,5,
3,Close,Hands on the product,4,
4,Close,Detail (price tag, texture),3,
5,Medium,Owner speaks: line 1,6,
6,B-roll,Customer or street (with consent),4,
""", 'csv'),
        ('consent note (save one per person)', """
Date: ____  Place: ____________
Name: ______________  Phone (optional): ________
I agree that [your page] may film me and post the
video on Instagram, YouTube and WhatsApp.
[ ] Yes, with my face  [ ] Voice only  [ ] Hands only
For a child: parent or guardian's name: _________
Can I ask to remove it later? Yes, message ______
(Record the yes on video or in a voice note too.)
""", ''),
    ],
    mistakes=[
        ('A bright window behind the person.', 'Their face goes dark. Turn around so the window lights the face.'),
        ('Recording next to a fan.', 'Fan noise ruins speech. Switch it off for the few minutes of recording.'),
        ('Filming everything in one long take.', 'Shoot short clips from different angles; they are much easier to edit.'),
        ('Text and faces at the very top or bottom.', 'App buttons cover them. Keep important things in the middle.'),
        ('Filming people without asking.', 'Always ask, and save the consent. For children, ask a parent.'),
    ],
    quiz=[
        {'q': 'Where should the window be when you film someone talking?',
         'o': ['Behind them', 'In front of them or to the side, lighting their face', 'Above them', 'It doesn\'t matter'],
         'a': 'B', 'why': 'Light on the face, not behind it, avoids a dark silhouette.'},
        {'q': 'What usually makes viewers leave a talking video faster?',
         'o': ['Slightly soft focus', 'Unclear, noisy sound', 'A plain background', 'Vertical video'],
         'a': 'B', 'why': 'Sound problems are less forgiven than picture problems.'},
        {'q': 'Why shoot B-roll clips?',
         'o': ['To make files bigger', 'To have extra shots that make editing and pacing easy', 'Platforms require it', 'To avoid captions'],
         'a': 'B', 'why': 'Close-ups and details let you cut quickly and keep attention.'},
        {'q': 'What does locking focus and exposure do?',
         'o': ['Makes the video private', 'Stops brightness and focus jumping around while you film', 'Adds music', 'Turns on 4K'],
         'a': 'B', 'why': 'Tap and hold on the subject to lock them.'},
    ],
    study='YouTube\'s Shorts recording guide, Open Camera and Instagram\'s Reels guidance (about 35 minutes)',
    action='run the light and sound tests, write a shot list and shoot the clips for a Reel',
)

L4 = lesson(
    4, 4,
    title='Editing on your phone',
    weeks=(10, 10), hours=4,
    outcome='Edit a short video entirely on your phone, from rough cut to captions, licensed sound and export, choosing a free editor that runs on your phone and leaves no watermark.',
    split='45 minutes study, 3 hours 15 minutes action',
    core=f"""
### Choose an editor that runs on your phone ({ASOF})

| App | Cost and watermark | Good for | Know this |
| --- | --- | --- | --- |
| **Edits** (by Instagram) | Free; exports with no watermark | Reels and Shorts: captions, green screen, cut-outs | Shows live insights for your reels |
| **YouTube Create** (by Google) | Free | Shorts and long videos: royalty-free music library, sound effects, auto-captions in some languages, voiceover | Needs Android 8.0 or later and at least 4 GB of RAM |
| **VN** | Free to download; has ads and in-app purchases | Multi-track timelines, auto-captions, teleprompter | Check the export screen for any paid features |
| **InShot** | Free to download; has ads and a Pro subscription | Quick trims, music, text, speed, resizing | Check export settings and watermarks before you rely on it |
| **Canva** | Free plan, no watermark on free elements | Video with text and templates | Paid Pro templates are marked |
| **Snapseed** (by Google) | Free, no ads or purchases | Photos: brightness, healing, perspective | Photos only |

On the old laptop, **Shotcut** and **Kdenlive** are free, open-source video editors. Kdenlive can make low-resolution proxy copies of your clips so that editing works even on a slow computer, and still export at full quality. **OBS Studio** records your screen for tutorials.

### The editing workflow

1. **Import** your clips and pick the best take of each.
2. **Rough cut:** put the clips in script order, hook first.
3. **Trim hard:** cut every pause, breath and "um". If a clip doesn't move the story, delete it.
4. **Captions:** generate auto-captions, then correct every word. Use large text with strong contrast, in the middle of the screen.
5. **Text overlays:** the hook in the first second; key numbers (prices, times) on screen.
6. **Sound:** voice first. Add music quietly underneath, from a licensed library (below).
7. **Colour:** small brightness and contrast fixes only; no heavy filters on food or faces.
8. **Cover:** choose a clear frame or upload a cover with the hook text in the centre.
9. **Export:** 1080 × 1920 (vertical) at 30 fps, then upload the file directly to each platform.

### Music and sound you're allowed to use

- **Add music inside the platform** when you post (Instagram's music library, YouTube's "Add sound"). Business accounts may have a smaller music library than creator accounts.
- **YouTube Audio Library** (in YouTube Studio) offers royalty-free music and sound effects. Tracks under a Creative Commons licence need the artist credited in your description; you can filter for "Attribution not required". YouTube says copyright-safe tracks downloaded from it won't be claimed through Content ID.
- **Never** download film songs or other creators' videos to use as background. "I gave credit" doesn't make it legal (Module 14).

### One video, every platform: export clean

Upload the original edited file to each app. Don't download your Reel from Instagram (with its watermark) and upload it to YouTube; platforms rank watermarked reposts lower.
""",
    example="""
Riyas at **Malabar Mobiles** filmed a screen guard being fitted: 14 clips, 3 minutes 20 seconds of raw footage. In Edits on his phone, Anu helped him:

- **Cut** it to 25 seconds: the cracked old guard (hook: "₹199 saves a ₹4,000 screen"), cleaning, alignment, the bubble-free finish, the price on screen.
- **Captions** in Malayalam, corrected word by word, in white text with a dark outline.
- **Sound:** his voice for the first line, then the actual fitting sounds, plus a quiet track from Instagram's library when posting.
- **Export:** 1080 × 1920, no watermark; the same file uploaded to YouTube Shorts.

On Instagram, more viewers watched to the end than on his earlier, unedited clip, and on YouTube the Short kept getting views in search for "screen guard Kuttiady" weeks later.

(Made-up example to show the method.)
""",
    resources=[
        ('edits', 'Read the features; install it if your phone supports it', '5 min'),
        ('yt-create', 'Read the features and device requirements', '5 min'),
        ('vn', 'Read the features, ads and in-app purchase notes', '5 min'),
        ('inshot', 'Read the features and the ads note', '5 min'),
        ('canva-mkt', 'Watch "Social video editing basics" and "Advanced social video"', '15 min'),
        ('yt-audio', 'Read how the Audio Library and attribution work', '10 min'),
        ('kdenlive', 'Optional, on the laptop: read about proxy clips', '3 min'),
    ],
    steps=[
        'Study the resources (about 45 minutes). Install one editor your phone can run smoothly.',
        'Edit the clips from SMM-M04-L03 into a 20–40 second vertical video using the workflow: rough cut, hard trim, corrected captions, hook text, licensed sound, cover.',
        'Edit a second video from new clips: a voiceover video (B-roll plus your recorded voice).',
        'Export both at 1080 × 1920 and post them as Reels and Shorts from the original files.',
        'After 7 days, compare their views and average watch time with your first videos from Module 1.',
    ],
    proof='Links to both edited videos on Instagram and YouTube with their Posting Log rows, and a screenshot of the editing timeline or captions screen.',
    templates=[
        ('editing checklist', """
[ ] Best take of each clip chosen
[ ] Hook in the first second (visual + text)
[ ] Every pause, "um" and dead second cut
[ ] One idea; anything else saved for another post
[ ] Captions generated AND corrected word by word
[ ] Text large, high contrast, in the middle
[ ] Voice clear; music quiet underneath
[ ] Music from a platform library or the YouTube
    Audio Library (credit added if needed)
[ ] Light colour fixes only
[ ] Cover frame chosen, text centred
[ ] Exported 1080 x 1920, 30 fps, no watermark
[ ] Original file uploaded to each platform
""", ''),
        ('export and upload card', """
REELS / SHORTS / STORIES: 1080 x 1920 (9:16), 30 fps
LONG YOUTUBE VIDEO: 1920 x 1080 (16:9), 30 fps
FILE NAMES: 2026-11-03_shopstory_tailor_v2.mp4
KEEP: the project file and the export, in Drive
      04 Content, until the post is 30 days old
UPLOAD: the original export to each app, not a
        download from another app
""", ''),
    ],
    mistakes=[
        ('Unedited auto-captions.', 'Errors look careless. Correct every word before export.'),
        ('Music louder than the voice.', 'Keep music low under speech. Voice first.'),
        ('Heavy filters.', 'They make food and faces look fake. Small brightness fixes are enough.'),
        ('Watermarked uploads.', 'Export your own file once and upload it to every platform.'),
        ('An editor that crashes your phone.', 'Choose one that runs smoothly on your device, even if it has fewer features.'),
    ],
    quiz=[
        {'q': 'What does YouTube Create need to run, according to its Play Store listing?',
         'o': ['Any Android phone', 'Android 8.0 or later and at least 4 GB of RAM', 'A laptop', 'A paid subscription'],
         'a': 'B', 'why': 'Older or low-memory phones may need another editor.'},
        {'q': 'Which music is safest for a 2-minute Short?',
         'o': ['A film song downloaded from YouTube', 'A royalty-free track from the YouTube Audio Library or YouTube\'s Shorts audio', 'A song from a friend\'s Reel', 'Any song if you give credit'],
         'a': 'B', 'why': 'Library tracks are licensed for use; credit alone doesn\'t give you rights.'},
        {'q': 'What does Kdenlive\'s proxy feature help with?',
         'o': ['Adding ads', 'Editing on a slow computer using low-resolution copies, then exporting at full quality', 'Removing watermarks from other videos', 'Translating captions'],
         'a': 'B', 'why': 'Proxy clips make editing smooth on older laptops.'},
        {'q': 'The best way to post the same video on Instagram and YouTube is:',
         'o': ['Download it from Instagram and upload to YouTube', 'Upload your original export to each platform', 'Screen-record it', 'Post only on one'],
         'a': 'B', 'why': 'Watermarked reposts are ranked lower.'},
    ],
    study='The phone editors\' listings, Canva\'s video lessons and YouTube\'s Audio Library guide (about 45 minutes)',
    action='edit two videos on your phone with corrected captions and licensed sound, and post them',
)

L5 = lesson(
    4, 5,
    title='Design basics, carousels and thumbnails',
    weeks=(11, 11), hours=2.5,
    outcome='Use simple design principles to make readable carousels, Reel covers and YouTube thumbnails in Canva, within the free licence, with templates you can reuse.',
    split='50 minutes study, 1 hour 40 minutes action',
    core=f"""
### Six principles for phone-sized design

Canva's free Design School teaches the elements and principles of design; for social media, six matter most:

1. **Contrast:** dark text on light, or light on dark. If you squint and can't read it, nobody will.
2. **Hierarchy:** one big headline, then smaller text. The eye should know where to start.
3. **Alignment:** line things up on one edge or centre. Random placement looks messy.
4. **Repetition:** the same fonts, colours and layout on every post builds recognition.
5. **Proximity:** keep related things together (a price next to its item).
6. **White space:** empty space makes the important thing stand out. Fewer words, bigger text.

Use your two brand colours plus white or black, and at most two fonts (one for Malayalam, such as Manjari, and one for English). Remember that most people see your design at the size of a matchbox.

### Carousels that get saved

- **Cover slide:** the hook and the promise, eight words at most, in the centre (the profile grid crops the edges).
- **One idea per slide:** a short headline and one or two lines.
- **Show, don't just tell:** photos, simple icons, numbers.
- **Summary slide:** the one thing to remember.
- **Last slide:** a call to action, such as "Save this" or "WhatsApp us to book".
- Instagram allows up to 20 items; most good carousels use 6–10.

### Thumbnails for YouTube

A thumbnail and a title are a promise; the video must keep it. YouTube's requirements ({ASOF}): a verified account; 16:9 for videos (9:16 for Shorts); JPG or PNG; at least 640 pixels wide; under 2 MB if you upload from the phone. In practice:

- **One clear subject:** a face showing emotion, or the product or place, big.
- **3–5 words** that add to the title rather than repeat it.
- **Strong contrast** and no clutter; check it at small size.
- **Consistent style** so viewers recognise your channel.

YouTube's **Test & compare** can try up to three titles or thumbnails and picks the winner by watch time, not clicks. It works on the computer only (SMM-M08-L03).

### Stay inside the free licence

Canva's free media licence lets you use its free photos, music and graphics in posts, ads and printed promotions, and you may edit them. You may not use them as part of a **trademark, logo or business name**, sell them as they are, or imply that people or brands in the images endorse your product. For logos, use your own text and shapes (ENT-M06-L01). Prefer your own photos anyway: real places beat stock images.

### Free tools beyond Canva

On the laptop: **GIMP** for photo editing, **Inkscape** for vector graphics such as logos and icons, and **Krita** for drawing and illustration, all free and open source.
""",
    example="""
**Kakkayam Hills Homestay** made a 7-slide carousel, "Monsoon trip? Pack these 7 things", in Canva using its two colours (forest green and cream) and Manjari for the Malayalam lines:

1. Cover: a photo of misty hills from the homestay balcony, "Monsoon trip? Pack these 7" in big cream text
2–6. One item per slide with a photo they took (rain jacket, leech socks, torch, power bank, dry bag), one short line each
7. "Book a monsoon stay: WhatsApp 9XXXXXXXXX", with the homestay's photo and a small map pin

It was saved 140 times and shared 60 times in a week, far more than their usual room photos, and three people mentioned it when they enquired. They turned the layout into a template and reused it for "5 dishes we serve at breakfast".

For their YouTube room tour they made a thumbnail: the balcony view, the words "₹2,500 a night, this view", and a small face of the owner smiling.

(Made-up example to show the method.)
""",
    resources=[
        ('canva-gde', 'Do the first 5 lessons: elements and principles of design', '25 min'),
        ('canva-license', 'Read what you can and can\'t do with free media, especially logos', '5 min'),
        ('yt-thumbs', 'Re-read the thumbnail requirements', '5 min'),
        ('gimp', 'Optional, on the laptop: look at what GIMP can do', '5 min'),
        ('inkscape', 'Optional, on the laptop: look at what Inkscape can do', '5 min'),
    ],
    steps=[
        'Study the resources (about 45 minutes).',
        'Make a carousel template in Canva with your colours and fonts: cover, content slide, summary slide and CTA slide.',
        'Use it to make one 6–10 slide carousel from your carousel script (SMM-M04-L01) and post it.',
        'Make one YouTube thumbnail for your planned long video, and one Reel cover, using the checklist.',
        'Check every design on your phone at small size, and once in Malayalam for broken letters.',
    ],
    proof='Your carousel post link with its Posting Log row, your reusable template, and your thumbnail and Reel cover images.',
    templates=[
        ('design checklist', """
[ ] Readable at matchbox size (squint test)
[ ] One headline, clearly the biggest thing
[ ] Max 2 fonts (Malayalam + English), 2 brand colours
[ ] Text aligned; nothing floating randomly
[ ] White space around the key message
[ ] Key text in the centre (grid and app overlays)
[ ] Malayalam checked for broken letters
[ ] Own photos, or Canva free media used within the
    licence (never in a logo or business name)
[ ] Same layout as my last posts (repetition)
""", ''),
        ('carousel and thumbnail specs', """
CAROUSEL SLIDE: 1080 x 1350 (portrait) or 1080 x 1080
  Slide 1 hook | slides 2-8 one idea each |
  summary | call to action
REEL COVER: 1080 x 1920, text in the middle third
YOUTUBE THUMBNAIL: 16:9, e.g. 1280 x 720, JPG or PNG,
  under 2 MB from the phone, 3-5 words, one subject
""", ''),
    ],
    mistakes=[
        ('Too much text.', 'If a slide needs a paragraph, it\'s two slides, or a caption.'),
        ('Five fonts and seven colours.', 'Two fonts and two colours look professional and recognisable.'),
        ('Thumbnails that lie.', 'Viewers leave quickly when the video doesn\'t match, which hurts it in recommendations.'),
        ('Canva library elements in a logo.', 'The free licence forbids it. Build logos from your own text and shapes.'),
    ],
    quiz=[
        {'q': 'What does Canva\'s free media licence forbid?',
         'o': ['Using free photos in social posts', 'Using free media as part of a logo, trademark or business name', 'Editing the photos', 'Printing posters'],
         'a': 'B', 'why': 'Others can use the same media, so you can\'t own it as your mark.'},
        {'q': 'How does YouTube\'s Test & compare choose a winning thumbnail?',
         'o': ['By clicks', 'By watch time', 'By likes', 'At random'],
         'a': 'B', 'why': 'YouTube optimises the test for watch time.'},
        {'q': 'Where should key text go on a carousel cover?',
         'o': ['At the very edges', 'In the centre, because the grid crops the edges', 'Only in the caption', 'Upside down'],
         'a': 'B', 'why': 'The profile grid shows a cropped rectangle of the cover.'},
        {'q': 'Which principle is "the same fonts, colours and layout every time"?',
         'o': ['Contrast', 'Repetition', 'Proximity', 'White space'],
         'a': 'B', 'why': 'Repetition builds recognition.'},
    ],
    study='Canva\'s design essentials, its free media licence and YouTube\'s thumbnail rules (about 45 minutes)',
    action='make a carousel template, post a carousel, and design a thumbnail and a Reel cover',
)

LESSONS = [L1, L2, L3, L4, L5]

MODULE = module(
    4,
    title='Content creation',
    weeks=(8, 11), hours=17.5,
    overview="""
Make content people stop for: strong hooks, simple scripts, Malayalam and English that read well, and videos and designs made entirely on your phone.

This is the craft module. In four weeks you'll write hooks and scripts, set language rules, learn to shoot with good light and sound using what you already have at home, edit on the phone with corrected captions and licensed sound, and design carousels, covers and thumbnails that are readable at phone size.

Every lesson ends with a real post. By week 11 you will have a phone content pack and a production kit of checklists and templates you'll use for the rest of the course.
""",
    outcomes=[
        'Write hooks and short scripts using proven story structures',
        'Use Malayalam and English deliberately, with correct fonts and subtitles',
        'Shoot steady, well-lit vertical video with clean sound on an Android phone',
        'Edit on the phone with corrected captions, licensed sound and clean exports',
        'Design readable carousels, Reel covers and YouTube thumbnails within Canva\'s licence',
    ],
    lessons=LESSONS,
    project='Your phone content pack',
    project_steps=[
        'Make, entirely on your phone: 3 short videos (at least one talking to camera and one voiceover with B-roll), 2 carousels and 1 YouTube thumbnail.',
        'Use the scripts, shooting, editing and design checklists for every piece, with consent notes where people appear.',
        'Post them across weeks 10–12 and log each one.',
        'Write a half-page production kit: your scripts template, shot list, editing steps and design template, in the order you actually use them.',
        'Note your best and worst piece by 7-day views and say why you think each did as it did.',
    ],
    project_proof='Links to the 3 videos and 2 carousels, the thumbnail image, your production kit and your best-and-worst notes.',
    rubric=[
        ('Hooks', 'Starts with greetings or logos', 'Some hooks, inconsistent', 'Every piece hooks in the first second, visually and in text'),
        ('Light and sound', 'Dark or noisy', 'Mostly clear', 'Clear light on faces and clean speech every time'),
        ('Editing', 'Unedited clips', 'Trimmed but slow, or caption errors', 'Tight cuts, corrected captions, licensed sound, clean export'),
        ('Design', 'Cluttered and hard to read', 'Readable but inconsistent', 'Readable at phone size, consistent template, within licence'),
        ('Language', 'Random mixing, broken letters', 'Mostly consistent', 'Clear language rules, checked fonts, accurate subtitles'),
    ],
    short=[
        'Write 5 hooks and 1 script; post one video.',
        'Do the light test only (skip the sound test) and shoot one Reel.',
        'Edit one video with corrected captions.',
        'Make one carousel from a template.',
    ],
    flashcards=[
        ('Three layers of a hook?', 'Visual, on-screen text and the first spoken sentence.'),
        ('What must every hook do?', 'Tell the truth, and be delivered by the video.'),
        ('Best free light for faces?', 'A window in front or to the side of the person.'),
        ('What matters more for talking videos: picture or sound?', 'Sound.'),
        ('Which free editor exports with no watermark and is made by Instagram?', 'Edits.'),
        ('YouTube Create needs at least how much RAM?', '4 GB (Android 8.0 or later).'),
        ('Where should you get music for posts?', 'The platform\'s own library or the YouTube Audio Library, never downloaded film songs.'),
        ('What does Canva\'s free licence forbid for logos?', 'Using free library media as part of a logo, trademark or business name.'),
        ('Three Malayalam fonts that render well?', 'Manjari, Chilanka, Noto Sans Malayalam.'),
    ],
    mistakes=[
        ('Buying gear before learning light and sound.', 'A window and a quiet room beat an expensive camera.'),
        ('Perfectionism.', 'Post the good-enough version; you learn more from ten posts than from one perfect one.'),
        ('Skipping consent because "it\'s just a small page".', 'Every person and shop deserves to be asked, and clients will expect it.'),
    ],
)
