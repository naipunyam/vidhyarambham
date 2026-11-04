from common import lesson, module, link, xref, table, fence, Q

L1 = lesson(
    21, 1,
    outcome='You can set up your phone and laptop study space to reduce neck, back and eye strain, use movement breaks and the 20-20-20 habit, and know when to see a doctor about pain or eyes.',
    split='20 minutes reading, 30 minutes of setup and checks',
    principle='There is no single perfect posture; the best posture is the next one, so set the screen at a comfortable height, change position often, take eye breaks and move every half hour or so.',
    science=f"""
**Posture: what the evidence says.** Many people believe that one "correct" sitting posture prevents back pain and that slouching causes it. Research is more relaxed: reviews have found **no strong link** between specific sitting postures and back pain, and people with and without pain sit in similar ways. What does seem to matter is **long periods without moving**, overall physical activity, and how stressed and tired you are. So the advice from physiotherapists has shifted from "sit perfectly straight" to "**find a comfortable position and change it often**". That said, a setup that forces your head forward for hours (looking down at a phone in your lap) commonly causes neck and shoulder discomfort, so raising the screen helps.

**Ergonomics for a phone and an old laptop:**
- **Phone:** bring it up towards eye level (prop it on books or a cheap stand) instead of bending your neck down; hold it with both hands; take breaks.
- **Laptop:** the screen is attached to the keyboard, so you can't get both right at once. For long sessions, raise the laptop on books so the top of the screen is near eye level, and use a separate keyboard and mouse if you can (second-hand ones are cheap); for short sessions, tilt the screen and sit back.
- **Chair and desk:** feet flat on the floor or a box; knees roughly level with hips; lower back supported (a folded towel works); elbows near 90° when typing.
- **Light:** avoid a bright window directly behind the screen or behind you causing glare; match screen brightness to the room.

**Eyes.** The American Academy of Ophthalmology says that using screens **does not permanently damage your eyes**, but long sessions can cause **digital eye strain**: dryness, tired eyes, blurred vision and headaches. One reason: people blink much less when staring at screens (about 5 to 7 times a minute instead of about 15). Their advice includes sitting about arm's length (about 25 inches) from the screen, positioning it so your gaze is slightly downward, matching brightness to the room, **blinking consciously** and **regularly looking at something far away** ({link('aao-screen', 'AAO')}). The popular **20-20-20 rule** (every 20 minutes, look at something 20 feet away for 20 seconds) is an easy way to do that; it is a practical habit rather than a precisely tested formula. Studies on whether **blue-light-filtering glasses** reduce eye strain found little or no benefit. Children and young people who spend more time outdoors have lower rates of short-sightedness (myopia), so outdoor time matters too.

**See a doctor or eye specialist** if you have persistent blurred vision, eye pain, red eyes, frequent headaches, or need to hold things closer or further than before; and see a doctor for back or neck pain that lasts more than a few weeks, follows an injury, or comes with numbness, weakness, or loss of bladder or bowel control (urgent). Free eye checks are often available at government hospitals and camps.
""",
    evidence=[
        ('A single "correct" sitting posture prevents back pain', 'failed', 'Reviews find no strong link between specific postures and pain.'),
        ('Long periods without movement contribute to discomfort', 'moderate', 'Consistent with several studies and clinical advice.'),
        ('Raising screens reduces neck strain', 'moderate', 'Supported by ergonomic studies; strongest for long sessions.'),
        ('Screens do not permanently damage eyes but cause eye strain', 'strong', 'AAO position; consistent research.'),
        ('20-20-20 rule', 'tool', 'A practical way to follow advice to look far away regularly; not precisely tested.'),
        ('Blue-light glasses reduce eye strain', 'failed', 'Reviews found little or no benefit.'),
    ],
    example="""
Anu studies 6 to 8 hours a day: PSC videos on her phone in bed, notes on an old laptop on the dining table. By evening her neck aches and her eyes burn.

Her fixes cost ₹0 to ₹300: she stops studying in bed and watches videos at the table with the phone propped on two thick books at eye level; she raises the laptop on three old textbooks and uses a ₹250 second-hand keyboard from a repair shop; a folded towel supports her lower back; she moves the table so the window is to her side, not behind the screen. She sets a 25-minute study timer (her Pomodoro from the Learning Capabilities course) and, at each break, stands up, rolls her shoulders and looks out of the window at the coconut trees for 20 seconds. She reminds herself to blink when reading PDFs.

After two weeks her neck pain is much less. Her eyes still feel tired late at night, so she books a free eye check at the taluk hospital camp; she needs mild reading glasses.
""",
    apply=f"""
**Your study-space fix (30 minutes):**
{fence('''STUDY-SPACE CHECKLIST
[ ] Screen top near eye level (phone propped up; laptop on books)
[ ] Separate keyboard/mouse for long laptop sessions (if possible)
[ ] Feet flat (or on a box), knees about hip level, lower back supported
[ ] Elbows near 90 degrees when typing, shoulders relaxed
[ ] Screen about arm's length away, gaze slightly down
[ ] No bright window behind the screen; brightness matches the room
[ ] Water bottle on the desk (you'll drink more, and get up to refill)
EVERY 20-30 MINUTES
[ ] Look at something far away for 20 seconds; blink slowly 10 times
[ ] Stand up, roll shoulders, look left and right, stretch arms up
EVERY 60-90 MINUTES
[ ] A 5-10 minute break: walk, water, a few squats or a short stretch
WARNING SIGNS (see a doctor): persistent blurred vision, eye pain,
frequent headaches; back/neck pain lasting weeks or with numbness or weakness''')}

**Micro-movements:** neck: slowly look left, right, up, down (no fast circles); shoulders: roll back 10 times; chest: open arms wide, squeeze shoulder blades; back: stand, hands on hips, gently lean back; wrists: gentle circles.

**With others:** share the setup with family members who work on screens (shop billing, office work, online classes for children). Children especially benefit from outdoor time and screen breaks.
""",
    resources=[
        ('aao-screen', 'Read the tips for computer use and eye strain', '10 minutes'),
        ('nhs-flex', 'Pick two or three stretches for your study breaks', '10 minutes'),
        ('nhs-strength', 'Optional: strength exercises such as rows and bridges help posture muscles; link them to Module 17', '5 minutes'),
    ],
    steps=[
        'Rate your neck, back and eye discomfort 0–10 at the end of a normal study day.',
        'Set up your study space with the checklist and take a photo.',
        'For one week, take a 20-second far-look and stand-up break every 20 to 30 minutes and a 5 to 10 minute break every 60 to 90 minutes.',
        'Rate discomfort again at the end of the week and note any warning signs.',
    ],
    proof='A photo of your study setup, the checklist ticked, and before-and-after discomfort ratings for neck, back and eyes.',
    templates=[('Discomfort tracker', """DISCOMFORT TRACKER (end of study day, 0-10)
Day | Study hours | Neck | Back | Eyes | Headache (Y/N) | Breaks taken (20-30 min / 60-90 min)
Before setup: neck ___ back ___ eyes ___
After 1 week: neck ___ back ___ eyes ___
Warning signs noticed? ______ -> doctor or eye check on ______""", '')],
    mistakes=[
        ('Hunting for a perfect posture.', 'Comfortable and changing often beats rigid and perfect.'),
        ('Studying in bed for hours.', 'It forces your neck forward. Use a table, at least for long sessions.'),
        ('Buying blue-light glasses or expensive chairs first.', 'Fix screen height, breaks and blinking first; blue-light glasses show little benefit.'),
        ('Ignoring persistent symptoms.', 'See a doctor or eye specialist for warning signs.'),
    ],
    quiz=[
        Q('What do reviews say about sitting posture and back pain?', 'There is no strong link between specific postures and pain; changing position often matters more', 'Slouching always causes back pain', 'You must sit at exactly 90 degrees', 'Posture has nothing to do with comfort', why='The evidence does not support one correct posture.'),
        Q('Do screens permanently damage your eyes, according to the AAO?', 'No, but they can cause temporary eye strain', 'Yes, always', 'Only phone screens do', 'Only at night', why='Digital eye strain is uncomfortable but not permanent damage.'),
        Q('Why do eyes feel dry when using screens?', 'People blink much less when staring at screens', 'Screens heat the eyes', 'Blue light dries tears', 'Wi-Fi signals', why='Blinking drops from about 15 to 5–7 times a minute.'),
        Q('What is the best cheap fix for neck strain from a phone?', 'Prop the phone up towards eye level and take breaks', 'Buy blue-light glasses', 'Hold the phone in your lap', 'Use a smaller font', why='Raising the screen reduces forward head bending.'),
    ],
    study='read the lesson and the AAO tips',
    action='set up your study space, take regular breaks for a week and compare discomfort ratings',
)

LESSONS = [L1]

MODULE = module(
    21,
    overview=f"""
Posture, ergonomics and eye care for long phone and laptop study: what the evidence really says about posture, a ₹0 to ₹300 study-space setup, movement and eye breaks (including the 20-20-20 habit), and warning signs that need a doctor.

Kerala PSC preparation often means 6 to 10 hours a day on a phone or an old laptop. That is hard on necks, backs and eyes. The fixes are simple and cheap: raise the screen, change position often, take short breaks, blink and look far away.

The study-break rhythm here fits with the Pomodoro method in {xref('lrn', 'lrn-m05', 'the Learning Capabilities focus module')}.
""",
    outcomes=[
        'Explain what research says (and doesn\'t) about posture and back pain.',
        'Set up a phone and laptop study space that reduces strain.',
        'Use micro-breaks, movement breaks and far-looking to reduce eye strain.',
        'Recognise warning signs that need a doctor or eye specialist.',
    ],
    lessons=LESSONS,
    project='your study-space fix with before-and-after ratings',
    project_steps=[
        'Do the study-space checklist and photograph the result.',
        'Use the break rhythm for one week and track discomfort.',
        'Book an eye check if you have any eye warning signs (free camps and government hospitals often offer them).',
        'Add your break rhythm to your Playbook.',
    ],
    project_proof='The setup photo, a week of discomfort ratings and any check-up booked.',
    rubric=[
        ('Setup', 'No changes', 'Some changes', 'Checklist complete with photo'),
        ('Breaks', 'Rarely', 'Some days', 'Break rhythm used every study day for a week'),
        ('Measurement', 'No ratings', 'Before or after only', 'Before and after ratings for neck, back and eyes'),
        ('Safety', 'Ignores warning signs', 'Aware of them', 'Acts on them (check-up booked if needed)'),
    ],
    short=[
        'Prop your phone up and stop studying in bed.',
        'Look far away and blink slowly at every study break.',
    ],
    flashcards=[
        ('Best posture', 'The next one: comfortable and changing often.'),
        ('Screen height', 'Top of the screen near eye level; phone propped up.'),
        ('Blink rate at screens', 'About 5–7 a minute instead of about 15.'),
        ('20-20-20 habit', 'Every 20 minutes, look 20 feet away for 20 seconds.'),
        ('Blue-light glasses', 'Little or no evidence of benefit for eye strain.'),
        ('Eye warning signs', 'Persistent blurred vision, eye pain, red eyes, frequent headaches.'),
        ('Urgent back-pain signs', 'Numbness, weakness, or loss of bladder or bowel control.'),
    ],
    mistakes=[
        ('Spending money before fixing habits.', 'Books under the laptop and regular breaks fix most problems.'),
        ('Long unbroken study sessions.', 'Move every 20 to 30 minutes.'),
        ('Thinking pain is normal for students.', 'Persistent pain deserves a check.'),
    ],
    tools=[
        'The study-space checklist, break rhythm and discomfort tracker (PD-M21-L01).',
    ],
    playbook=[
        'Screen at eye level; I move every 20–30 minutes, look far away and blink; a real break every 60–90 minutes.',
    ],
)
