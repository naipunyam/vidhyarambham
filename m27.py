from common import lesson, module, link, xref, table, fence, Q
import tools

TALK = """5-MINUTE TALK PLANNER                Audience: ______  Language: EN / ML
ONE MESSAGE (one sentence the audience should remember):
  ______________________________________________
OPENING (30 s): hook = a question / a short story / a surprising true fact
  ______________________________________________
POINT 1 (1 min): ______ | example or story: ______
POINT 2 (1 min): ______ | example or story: ______
POINT 3 (1 min): ______ | example or story: ______
CLOSE (30-45 s): repeat the message + one action for the audience
  ______________________________________________
Cue card (keywords only): hook | P1 | P2 | P3 | message | action
Timing check: ___ min ___ s (aim 4:30-5:00)"""

L1 = lesson(
    27, 1,
    outcome='You can build a clear 5-minute talk with one message, a hook, three points with examples and a strong close, in English or Malayalam.',
    split='20 minutes reading, 40 minutes of planning',
    principle='A talk works when the audience can remember one message; structure (hook, three points, close), concrete examples and repetition make that happen.',
    science="""
**Why structure matters.** Listeners, unlike readers, cannot go back. Research on memory and comprehension shows that organised information (with a clear overview, signposts and summaries) is understood and remembered better than the same content without structure. Working memory is limited (the Learning Capabilities course, Module 1), so a talk with one main message and a small number of points is easier to follow than a talk with ten.

**A simple structure that works for most short talks:**
1. **Hook (about 30 seconds):** a question, a short true story or a surprising true fact that makes the audience care.
2. **Message:** one sentence: what you want them to remember or do.
3. **Three points:** each with an example, story or picture. "Three" is a convention (the "rule of three" in rhetoric goes back to classical speakers); it is not a scientific law, but three items are easy to hold in mind.
4. **Close:** repeat the message and give one clear action.

**Signposting** ("First…", "The second reason…", "Finally…", "So, to sum up…") helps listeners follow. In Malayalam, similar phrases ("ആദ്യമായി…", "രണ്ടാമതായി…", "അവസാനമായി…", "ചുരുക്കത്തിൽ…") do the same job.

**Know your audience.** Ask: Who are they? What do they already know? What do they care about? What do I want them to think, feel or do afterwards? A talk on the library for parents is different from one for teenagers.

**English or Malayalam?** Choose the language the audience is most comfortable with, unless the setting requires English (interviews, some college events). Mixing a few English terms into Malayalam is normal in Kerala. If English is your second language, you don't need perfect grammar; clear structure, simple sentences and good examples matter more. Slow down a little and use short sentences. Many great speakers speak with an accent.

**Slides?** For a 5-minute talk to a small group, you usually don't need slides. If you use them, use pictures and a few words, not paragraphs to read; research on multimedia learning (Richard Mayer) shows that reading lots of on-screen text while listening overloads people.
""",
    evidence=[
        ('Organised information is understood and remembered better', 'strong', 'Supported by memory and comprehension research.'),
        ('Limited working memory: fewer points are easier to follow', 'strong', 'Well-established cognitive science.'),
        ('Rule of three', 'tool', 'A rhetorical convention; easy to remember, not a law.'),
        ('Heavy on-screen text while talking overloads listeners', 'moderate', 'Supported by multimedia-learning research.'),
    ],
    example=f"""
Sreeja plans a 5-minute talk for her residents' association on "Why young people should use the panchayat library". **Audience:** parents and teenagers, mostly Malayalam speakers. **Language:** Malayalam with a few English words.

**One message:** "The library can be your quiet study room and your study group, for free."
**Hook:** "How many of you have a quiet place at home to study for two hours without interruption?" (A few hands go up.)
**Point 1:** quiet space: Divya's story from PD-M26-L01.
**Point 2:** free material: PSC rank files, newspapers, previous papers; she holds up one rank file.
**Point 3:** people: the Saturday test group of eight aspirants.
**Close:** "So the library is a quiet room, a free bookshop and a study group. Visit once this week; the Saturday group meets at 3 pm."

Her cue card has six words: hands, Divya, rank file, Saturday, message, visit.
""",
    apply=f"""
**Plan your 5-minute talk:**
{fence(TALK)}

**Topic ideas** (choose something you know and care about): what I learned from 30 days of rejection; how to prepare for PSC on ₹0; a local place or history (a temple festival, a river, a freedom fighter from Kozhikode); why sleep matters for students; a skill you can teach (a recipe, a maths trick).

**Rules for the script:**
- Write the talk once in full, then reduce it to a **keyword cue card**. Don't memorise word for word; you'll sound like you're reading and freeze if you lose a word.
- Use short sentences, everyday words and one example per point.
- Time it: 5 minutes is about 600 to 700 words spoken at a calm pace.

**With others:** ask one person what they would want to hear about your topic before you write it.
""",
    resources=[
        ('tm-find', 'Look up Toastmasters clubs near you (Kozhikode has at least one) and read what a meeting involves', '10 minutes'),
        ('ted-waldinger', 'Re-watch the opening minute and the close: notice the hook, the message and the repetition', '5 minutes'),
        ('james-talks', 'Read the preface of Talks to Teachers, where James explains why he kept the talks in their spoken, informal style', '10 minutes'),
    ],
    steps=[
        'Choose a topic and audience for a real 5-minute talk you will give in this module.',
        'Fill in the talk planner and write the full talk once.',
        'Make a keyword cue card and time a first run-through aloud.',
        'Ask one person to listen to a run-through and tell you the one message they remember. Compare with yours.',
    ],
    proof='Your filled planner, full draft, cue card, timed run-through (minutes and seconds) and the listener\'s one-message answer.',
    templates=[('Talk planner', TALK, '')],
    mistakes=[
        ('Too many points.', 'One message and three points. Cut the rest.'),
        ('Starting with "Good morning, my name is…, today I will talk about…"', 'Start with the hook; introduce yourself briefly after it, or let the host do it.'),
        ('Memorising word for word.', 'Use a keyword cue card and speak naturally.'),
        ('Waiting for perfect English.', 'Clear structure and simple sentences matter more than perfect grammar.'),
    ],
    quiz=[
        Q('What should a short talk be built around?', 'One message the audience should remember', 'As many facts as possible', 'Your full biography', 'A long list of thanks', why='Listeners can\'t go back; one message makes the talk memorable.'),
        Q('Which is a good hook?', 'A question, a short true story or a surprising true fact', 'Reading your CV', 'Apologising for being nervous', 'Explaining the history of the topic in detail', why='Hooks make people care in the first 30 seconds.'),
        Q('Why use a keyword cue card instead of memorising?', 'You sound natural and don\'t freeze if you forget a word', 'Cards are required', 'Memorising is impossible', 'Cue cards make talks longer', why='Keywords guide; word-for-word scripts trap you.'),
        Q('About how many words is a 5-minute talk at a calm pace?', 'About 600 to 700', 'About 100', 'About 2,000', 'About 50', why='Roughly 120 to 140 words a minute.'),
    ],
    study='read the lesson and look up Toastmasters clubs near you',
    action='plan a 5-minute talk with the planner, write it, make a cue card, time it and test the message on one listener',
)

L2 = lesson(
    27, 2,
    outcome='You can manage speaking nerves with reappraisal and breathing, use voice and body language naturally, follow Kerala event etiquette, and spot body-language myths.',
    split='20 minutes reading, 30 minutes of practice',
    principle='Nerves are normal and usually invisible; reframe them as energy, slow your breathing, speak a little slower than feels natural, look at friendly faces, and let your body move naturally.',
    science="""
**Fear of public speaking is common.** Surveys in many countries find that public speaking is among the most common fears. Physical signs (racing heart, dry mouth, shaking) come from the stress response (Module 11). Two research findings help:
1. **The illusion of transparency:** Kenneth Savitsky and Thomas Gilovich (2003) found that speakers overestimated how nervous they looked to the audience. When speakers were **told** about this illusion, they felt calmer and were rated as better speakers. So: your nerves show much less than you feel.
2. **Reappraisal as excitement:** Alison Wood Brooks (2014) found that saying "I am excited" before a speech or a maths test led to better performance than trying to calm down ("I am calm"). The idea is that excitement and anxiety feel similar in the body, and "excited" points the energy forward. Later replications were mixed, so treat it as a promising tip.

Slow breathing (in for 4, out for 6) before you start calms the body (PD-M11-L01). Practice and exposure (Module 13) reduce fear more than anything else; that is why PD-M27-L03 is about practice.

**Voice.** Speak a little **slower** than in conversation, **pause** after important points (pauses feel long to you, short to listeners), **vary** your pitch and volume, and project to the back of the room (breathe from the belly). Filler words ("um", "ah", "like", "basically", "pinne", "athayathu") are normal; a few don't matter, but many distract. Replacing fillers with pauses is a trainable skill.

**Body language.** Stand steady with weight on both feet, use open, natural hand gestures, and make eye contact with different parts of the room (a few seconds each). Smile where it fits. A famous figure claims that communication is "7% words, 38% tone, 55% body language". That comes from Albert Mehrabian's 1960s studies about how people judged **feelings** when words and tone **contradicted** each other (for example, saying "I like you" in a cold voice). Mehrabian himself has said it doesn't apply to communication in general. Content matters a great deal. Also remember that claims about reading lies or hidden thoughts from gestures are mostly myths (PD-M02-L02), and power posing doesn't change hormones (PD-M13-L01).

**Kerala event etiquette:** greet the chief guest and dignitaries first, using respectful titles ("Respected President…", "ബഹുമാനപ്പെട്ട…"); keep introductions short; stay within your time (organisers and audiences appreciate this more than anything); avoid jokes about religion, caste, politics or appearance; thank the organisers at the end; and turn your phone off.
""",
    evidence=[
        ('Speakers overestimate how nervous they look', 'moderate', 'Savitsky and Gilovich experiments; telling speakers helped them.'),
        ('Reappraising anxiety as excitement improves performance', 'mixed', 'Promising study (Brooks, 2014); mixed replications.'),
        ('Practice and exposure reduce speaking anxiety', 'strong', 'Supported by exposure and skills-training research.'),
        ('"7% words, 38% tone, 55% body language"', 'failed', 'A misreading of narrow studies about contradictory feelings; not a general rule.'),
        ('Pausing and slower pace improve clarity', 'tool', 'Standard speaking advice; consistent with comprehension research.'),
    ],
    example="""
Ashiq is about to speak at the residents' association. His hands are cold and his heart is racing. He takes five slow breaths (in 4, out 6) at his seat and quietly says, "I'm excited; this matters." He reminds himself: "They can't see most of this nervousness."

He starts with the respectful greeting ("Bahumaanappetta President, members…"), then his hook. He looks at the friendly faces first (his neighbour nodding in the third row), then around the room. When he loses his place, he pauses, looks at his cue card and continues; nobody notices. He finishes at 4 minutes 50 seconds, within his time.

Afterwards, his friend says he spoke "quite fast in the middle" and said "pinne" a lot. Ashiq notes both for his next recording. He also notices he enjoyed the last two minutes.
""",
    apply=f"""
**Before you speak (5 minutes):**
1. Five slow breaths (in 4, out 6), or two physiological sighs.
2. Say "I'm excited" (or "ഞാൻ ഉത്സാഹത്തിലാണ്") rather than "calm down".
3. Remind yourself: "They can't see most of my nerves."
4. Check your cue card and first sentence.

**While speaking:**
- **Voice:** slower than feels natural; pause after key points; vary pitch; speak to the back row.
- **Body:** stand steady; natural hand gestures; eye contact with different parts of the room; start with friendly faces.
- **If you lose your place:** pause, breathe, check the card, continue. A pause looks like thinking.
- **Fillers:** replace "um" and "pinne" with a short silence.

**Etiquette checklist:** greet dignitaries in order; keep to time; no jokes about religion, caste, politics or appearance; thank the organisers; phone off.

**With others:** when you are in the audience, nod, smile and look interested; you are helping the speaker. Afterwards, give specific, kind feedback (SBI, PD-M26-L03).
""",
    resources=[
        ('tm-find', 'Find a nearby club and note its meeting time; many allow guests (check with the club)', '10 minutes'),
        ('nhs-yoga', 'Optional: a short breathing or relaxation routine to use before speaking', '10 minutes'),
        ('ted-jiang', 'Watch Jia Jiang\'s talk again with the sound off for one minute: notice his gestures and eye contact', '5 minutes'),
    ],
    steps=[
        'Practise your 5-minute talk twice using the before-you-speak routine. Record one run on your phone (video if possible).',
        'Watch or listen back and count filler words per minute and note your pace (too fast, okay, slow).',
        'Practise replacing fillers with pauses in a 1-minute section; record it again and count again.',
        'Write the etiquette opening and close for your real talk (greetings in the right order, thanks).',
    ],
    proof='Two recordings (before and after filler practice) with filler counts per minute and pace notes, and your etiquette opening and close.',
    templates=[('Speaking self-review', """SPEAKING SELF-REVIEW         Recording: ______  Length: ___ min
Filler words: count ___ / minutes ___ = ___ per minute
Pace: too fast / ok / slow    Pauses after key points? Y/N
Eye contact (video): 1-5 ___  Gestures: natural / stiff / too many
Voice: monotone / some variety / lively
One thing that worked: ______  One fix for next time: ______
ETIQUETTE: Greeting order: ______ ; time limit ___ min ; closing thanks: ______""", '')],
    mistakes=[
        ('Trying to eliminate all nerves.', 'Some nerves give energy. Aim to function with them.'),
        ('Rushing.', 'Nerves speed you up; plan to speak slower than feels natural.'),
        ('Quoting "55% body language".', 'It\'s a myth when applied to all communication; content matters.'),
        ('Overrunning your time.', 'Keeping to time is one of the most appreciated courtesies.'),
    ],
    quiz=[
        Q('What is the "illusion of transparency" in public speaking?', 'Speakers overestimate how nervous they look', 'Audiences can read speakers\' minds', 'Glass podiums', 'Speakers underestimate their nerves', why='Savitsky and Gilovich; knowing this helps speakers relax.'),
        Q('What did Brooks (2014) suggest saying before a stressful performance?', '"I am excited"', '"I am calm"', '"I will fail"', 'Nothing', why='Reappraising arousal as excitement improved performance in her studies; replications are mixed.'),
        Q('What is the honest status of "7% words, 38% tone, 55% body language"?', 'A misapplication of narrow studies; not a general rule', 'A proven law of communication', 'From a large modern meta-analysis', 'True only in English', why='Mehrabian\'s studies were about contradictory feelings.'),
        Q('What should you do if you lose your place?', 'Pause, breathe, check your cue card and continue', 'Apologise repeatedly', 'Start again from the beginning', 'Leave the stage', why='A pause looks like thinking.'),
    ],
    study='read the lesson and find a nearby Toastmasters club',
    action='record your talk, count fillers and pace, practise pauses and record again, and write your etiquette opening and close',
)

L3 = lesson(
    27, 3,
    outcome='You can run a weekly speaking practice (recording, feedback, filler and pace targets) in English and Malayalam, and give a 5-minute talk to a real audience.',
    split='15 minutes reading, 20 minutes a week of practice, plus the real talk',
    principle='Speaking skill grows through many short practices with feedback and through real audiences; weekly recordings and one real talk do more than reading about speaking.',
    science=f"""
**Deliberate practice for speaking.** Skills grow fastest with focused practice on specific weaknesses, immediate feedback and repetition (the {xref('lrn', 'lrn-m13', 'Learning Capabilities deliberate-practice module')}). For speaking that means: record, review against two or three criteria (fillers, pace, structure), fix one thing, and record again. Studies of public-speaking training, including virtual-reality exposure and courses, find reduced anxiety and improved ratings; the biggest gains come from **repeated speaking with feedback**, which is also how clubs like Toastmasters work.

**Toastmasters.** Toastmasters International is a non-profit network of speaking clubs where members give prepared speeches, short impromptu speeches ("Table Topics") and evaluations of each other. Membership has fees, but many clubs let guests visit. {link('tm-calicut', 'Calicut Toastmasters')} in Kozhikode lists Sunday meetings from 3 to 5 pm and allows online attendance (check current details with the club); the {link('tm-find', 'Find a Club')} page lists others. Research on Toastmasters specifically is limited, but its format (regular practice, structured feedback, supportive audience) matches what works.

**Bilingual speaking.** If you practise in both English and Malayalam, you build two skills: clear thinking (which transfers) and fluency in each language (which doesn't fully transfer). Shadowing (repeating after a good speaker) and reading aloud help fluency; the Learning Capabilities {xref('lrn', 'lrn-m15', 'language module')} covers them. For Malayalam, practise the formal register used at functions as well as everyday speech.

**Impromptu speaking.** Many real situations are unplanned: an interview question, being asked to "say a few words" at a function. A simple structure helps: **Point** (your answer in one sentence), **Reason** (why), **Example** (a short story), **Point** again (PREP). Practise it with random topics.

**The real talk.** A 5-minute talk to a real audience (family, friends, a residents' association, a library event, a club, a Toastmasters guest slot) is the final exposure step for speaking. Afterwards, ask for one strength and one improvement (SBI).
""",
    evidence=[
        ('Repeated speaking with feedback improves skill and lowers anxiety', 'strong', 'Supported by training and exposure research.'),
        ('Recording and self-review', 'tool', 'A form of deliberate practice; consistent with feedback research.'),
        ('Toastmasters format', 'tool', 'Little direct research; matches principles of practice and feedback.'),
        ('PREP for impromptu answers', 'tool', 'A practical structure widely taught.'),
    ],
    example=f"""
Anu's weekly practice on Sunday evenings (part of her weekly reflection): a 2-minute recording, alternating English and Malayalam. Week 1 (English): 14 fillers in 2 minutes (7 per minute), very fast. Week 3: 9 per minute in Malayalam ("pinne, athayathu"). Week 6: 3 per minute in English, with pauses.

She practises impromptu answers with PREP using random topics from a jar her brother writes: "Is social media good for students?" "Point: it helps if you use it with a plan. Reason: it has great free material but also endless distraction. Example: I get PYQ discussions from one Telegram group but lost hours to reels. Point: so, a plan first, then the app."

For her real 5-minute talk she visits Calicut Toastmasters as a guest on a Sunday (she messages the club first), and the next month gives her "30 days of rejection" talk at her ward's library day to about 25 people. An evaluator's feedback: strong story, good eye contact, rushed ending. She adds "slow down in the close" to her checklist.
""",
    apply=f"""
**Weekly speaking practice (20 minutes, every Sunday with your reflection):**
1. Record 1 to 2 minutes (English one week, Malayalam the next): your week, a topic from a jar, or a section of your talk.
2. Review with the speaking log: fillers per minute, pace, one strength, one fix.
3. Record the same piece again with the fix.
4. Once a month, do a PREP impromptu answer on a random topic.

{fence(tools.SPEAKING_LOG)}

**Your real 5-minute talk:**
1. Choose the audience: family gathering, friends, residents' association, library or club event, a Toastmasters guest visit (ask the club first).
2. Confirm a date, time and time limit with the organiser.
3. Practise three times with the before-you-speak routine (PD-M27-L02).
4. Give the talk. Record it if the organiser and audience agree.
5. Ask two people for one strength and one improvement.

**Targets over the course:** halve your fillers per minute from your first recording; speak at a calm pace; finish within time.
""",
    resources=[
        ('tm-calicut', 'Check the meeting details and contact the club before visiting as a guest', '5 minutes'),
        ('tm-find', 'Search for other clubs near you if Calicut is too far', '5 minutes'),
        ('ted-waldinger', 'Use the first two minutes as a shadowing exercise for English pace and pauses', '10 minutes'),
    ],
    steps=[
        'Do weekly 2-minute recordings for at least four weeks (alternating languages) with the speaking log.',
        'Practise two PREP impromptu answers on random topics.',
        'Arrange and give your 5-minute talk to a real audience.',
        'Collect feedback from two people and compare your filler rate in the first and latest recordings.',
    ],
    proof='Four or more logged weekly recordings, two PREP answers, evidence of the real talk (photo, recording if permitted, or organiser\'s message), two pieces of feedback, and your filler-rate comparison.',
    templates=[('PREP impromptu card', """PREP (for unplanned questions, 30-90 seconds)
P - Point: my answer in one sentence: ______
R - Reason: because ______
E - Example: a short true story or fact: ______
P - Point again: "So, ______."
Random topic jar ideas: my village; a book I liked; phones and students;
a person I admire; the best advice I got; why sleep matters; my favourite food""", '')],
    mistakes=[
        ('Practising only in your head.', 'Speak aloud and record; that\'s where the feedback comes from.'),
        ('Waiting until you feel ready for a real audience.', 'Book the talk; preparation follows the date.'),
        ('Judging yourself on one recording.', 'Track fillers and pace over weeks.'),
        ('Recording people without permission.', 'Ask organisers and audiences before recording a talk.'),
    ],
    quiz=[
        Q('What makes speaking practice most effective?', 'Repeated speaking with feedback on specific points', 'Reading books about speaking', 'Watching famous speakers only', 'Waiting until you feel confident', why='Deliberate practice with feedback builds skill.'),
        Q('What does PREP stand for?', 'Point, Reason, Example, Point', 'Plan, Rehearse, Explain, Pause', 'Prepare, Repeat, Evaluate, Practise', 'Pace, Rhythm, Emphasis, Pitch', why='A structure for impromptu answers.'),
        Q('How do you calculate fillers per minute?', 'Filler count divided by minutes spoken', 'Total words divided by fillers', 'Fillers times minutes', 'Count only "um"', why='A simple rate lets you compare recordings.'),
        Q('What should you do before visiting a Toastmasters club as a guest?', 'Check meeting details and contact the club', 'Just walk in at any time', 'Pay a membership fee first', 'Nothing', why='Details and guest rules vary; check first.'),
    ],
    study='read the lesson and check the Toastmasters club details',
    action='do four weekly recordings with the log, two PREP answers, and give your 5-minute talk to a real audience',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    27,
    overview=f"""
Public speaking in English and Malayalam: building a 5-minute talk (one message, hook, three points, close), handling nerves (the illusion of transparency, reappraisal, breathing), voice, body language and Kerala event etiquette, myths to drop (the "55% body language" rule), weekly recordings, impromptu answers and a 5-minute talk to a real audience.

Speaking confidently is the skill that most often separates people with similar knowledge: in interviews, meetings, functions and business. Like every skill in this course, it grows with practice and feedback, not with reading about it.

You have been recording yourself weekly since week 1 (the Sunday reflection). This module adds structure, feedback criteria and a real audience. If you can, visit a Toastmasters club as a guest; Kozhikode has at least one.
""",
    outcomes=[
        'Build a clear 5-minute talk with a cue card, in English or Malayalam.',
        'Manage nerves with breathing, reappraisal and knowing the illusion of transparency.',
        'Use voice and body language naturally and follow Kerala event etiquette.',
        'Explain why the "7-38-55" rule is a myth.',
        'Run weekly speaking practice and give a 5-minute talk to a real audience.',
    ],
    lessons=LESSONS,
    project='a 5-minute talk to a real audience',
    project_steps=[
        'Plan and script the talk (PD-M27-L01).',
        'Practise it at least three times with recordings and the self-review (PD-M27-L02).',
        'Give it to a real audience (PD-M27-L03) and collect two pieces of feedback.',
        'Write a half-page reflection: what you feared, what happened, your filler-rate change, next speaking goal.',
    ],
    project_proof='The planner and cue card, practice recordings with self-reviews, evidence of the real talk, feedback and your reflection.',
    rubric=[
        ('Structure', 'No clear message', 'Message but loose structure', 'One message, hook, three points with examples, strong close'),
        ('Delivery', 'Reads a script, very fast', 'Some pauses and eye contact', 'Calm pace, pauses, natural gestures, eye contact'),
        ('Practice', 'No recordings', 'One or two recordings', 'Weekly recordings with filler and pace tracking'),
        ('Real audience', 'Not done', 'Planned', 'Given within time, with feedback collected'),
    ],
    short=[
        'Keep the weekly 1-minute recording going and count fillers.',
        'Give a 2-minute talk at a family gathering.',
    ],
    flashcards=[
        ('Talk structure', 'Hook, message, three points with examples, close with message + action.'),
        ('Words per minute (calm)', 'About 120–140; a 5-minute talk is about 600–700 words.'),
        ('Illusion of transparency', 'Speakers overestimate how nervous they look.'),
        ('Reappraisal before speaking', 'Say "I\'m excited" rather than "calm down" (promising, mixed replications).'),
        ('"55% body language"', 'A myth when applied to communication in general.'),
        ('Replacing fillers', 'Use a short pause instead.'),
        ('PREP', 'Point, Reason, Example, Point.'),
        ('Top etiquette rule', 'Keep to your time.'),
    ],
    mistakes=[
        ('Avoiding every chance to speak.', 'Each small chance is a rung on your fear ladder.'),
        ('Perfectionism about language.', 'Clear and simple beats perfect and frozen.'),
        ('No feedback.', 'Ask for one strength and one improvement every time.'),
    ],
    tools=[
        'The 5-minute talk planner and cue card (PD-M27-L01).',
        'The speaking self-review and etiquette checklist (PD-M27-L02).',
        'The speaking recording log and PREP card (PD-M27-L03).',
    ],
    playbook=[
        'Before speaking: five slow breaths, "I\'m excited", they can\'t see most of my nerves.',
        'Talks: one message, hook, three points, close with action; keep to time.',
        'Weekly 2-minute recording, alternating English and Malayalam; fillers → pauses.',
    ],
)
