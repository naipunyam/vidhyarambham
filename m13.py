from common import lesson, module, link, ASOF

L1 = lesson(
    13, 1,
    title='AI for ideas, research, scripts and captions',
    weeks=(33, 33), hours=3,
    outcome='Use free AI assistants to brainstorm, draft, rewrite and summarise faster, with prompts that carry your strategy and voice, while catching made-up facts, generic writing and privacy risks.',
    split='30 minutes study, 2 hours 30 minutes action',
    core=f"""
### What AI is good and bad at, for social media

| Good at | Bad at |
| --- | --- |
| Brainstorming many angles and hooks in seconds | Facts: it can state wrong things confidently ("hallucinations") |
| First drafts of scripts, captions and outlines | Current platform rules, limits and features |
| Rewriting for a platform, length or tone | Local knowledge: prices, timings, who runs which shop |
| Turning a long piece into several short ones | Natural Malayalam and local expressions (check every line) |
| Summarising 200 comments into themes | Originality: drafts often sound like everyone else's |
| Checklists and report structures | Legal, tax or medical advice |

The free plans of Gemini, ChatGPT and Claude are enough for this work ({ASOF}; limits change, check current rules). The Free AI Generalist Course in this app teaches prompting in depth (Level 1).

### Your strategy goes in; AI drafts come out

AI is a fast assistant, not the strategist. A good workflow:

1. **You decide** the goal, audience, pillar and message (Modules 2 and 5).
2. **AI drafts options:** 20 hooks, 3 script versions, 5 caption variants.
3. **You choose** the best and **add real details**: the owner's words, true prices, your own observations.
4. **You check every fact** against a real source or the business owner.
5. **You edit to your voice** using your voice chart, and read it aloud.

Meta's advice to Facebook creators in July 2025 was to write high-quality captions rather than relying on unedited automated AI captions; the same applies everywhere.

### A prompt pattern that works

Give the assistant what a new team member would need:

- **Role:** "You are a social media copywriter for small businesses in Kerala."
- **Context:** the business, the audience (your persona), your voice chart and language rules.
- **Task:** "Write 10 hooks for a 30-second Reel about ..."
- **Constraints:** length, language, "no hype or superlatives", "at most five hashtags", "no health claims".
- **Examples:** two of your best past captions.
- **Honesty:** "Ask me questions if anything is unclear. Mark any fact you're not sure about with [CHECK]."

### Summarising comments and reviews

Paste comments (with names and numbers removed) and ask: "Group these into themes, count each, and quote one example per theme." It turns an hour of reading into minutes. Check a few by hand to make sure it didn't invent themes.

### Privacy

Never paste customers' phone numbers, private chats, payment details or a client's confidential plans into an AI tool, and check each tool's privacy settings. Remove names before you ask for summaries.

### Avoid "AI sameness"

AI drafts tend to use the same phrases ("Unlock the secret...", "Elevate your..."). Delete them. Your local knowledge, real photos and the owner's own words are what make posts work; AI can't supply those.
""",
    example="""
Anu used a free AI assistant to prepare a "Shop story" Reel about a tailoring shop:

- **Prompt:** her role, the page's voice chart, the persona, "write 15 hooks for a 40-second Reel about a tailor who has worked on the same street for decades; Malayalam and English; no exaggeration; mark facts to check with [CHECK]".
- **Output:** 15 hooks in about 20 seconds. Three were good; one said "since 1950 [CHECK]".
- **Her edit:** the owner told her he started in 1987, so she wrote "Same street, same machine, since 1987". She rewrote the Malayalam hook herself because the AI's version used an unnatural word.
- **Caption:** she asked for "a 3-line caption in my voice chart, first line with 'Kuttiady tailor'", then changed two lines to the tailor's own words.

Time: 25 minutes instead of about an hour. Errors caught: one wrong date, one awkward Malayalam phrase, one cliché ("timeless craftsmanship").

(Made-up example to show the method.)
""",
    resources=[
        ('gemini-plans', 'Check what the free plan includes', '5 min'),
        ('chatgpt-plans', 'Check what the free plan includes', '5 min'),
        ('claude-plans', 'Check what the free plan includes', '5 min'),
        ('tc-fb-original', 'Re-read Meta\'s advice on authentic storytelling and AI captions', '5 min'),
    ],
    steps=[
        'Study the resources (about 20 minutes) and choose one free assistant to use this week.',
        'Write 5 reusable prompts with the pattern above: hooks, a short-video script, a caption rewrite for each platform, a comment or review summary, and a repurposing plan.',
        'Use them to prepare one week of posts for your sprint or your pilot client.',
        'For every AI draft, log the time it took, what you changed and every error you caught (wrong facts, awkward Malayalam, clichés).',
        'Publish the posts and note in the Posting Log which ones were AI-assisted.',
    ],
    proof='Your 5 prompts, the log of time saved and errors caught, and links to the published AI-assisted posts.',
    templates=[
        ('prompt template', """
ROLE: You are a social media copywriter for small
businesses in Kerala.
CONTEXT: Business: ______ in ______. Audience: ______
(persona). Voice: ______ (paste voice chart).
Language rules: ______.
TASK: Write ______ (e.g. 10 hooks / a 30-second script /
a 3-line caption) about ______.
CONSTRAINTS: max ___ words; English and Malayalam;
no hype or superlatives; no health or money promises;
max 5 hashtags; one call to action: ______.
EXAMPLES OF MY STYLE: "______" / "______"
HONESTY: Ask me questions if unclear. Mark any fact you
are not sure about with [CHECK]. Do not invent prices,
dates, names or reviews.
""", ''),
        ('AI output check', """
[ ] Every fact checked with the owner or a real source
[ ] No invented prices, dates, names, reviews or results
[ ] Malayalam read aloud by me (or a native speaker)
[ ] Clichés removed ("unlock", "elevate", "game-changer")
[ ] Real local details and the owner's own words added
[ ] Fits my voice chart and the platform's format
[ ] No private data was pasted into the tool
[ ] Claims pass the honest persuasion check (SMM-M05-L02)
""", ''),
    ],
    mistakes=[
        ('Posting AI drafts unedited.', 'They sound generic and may be wrong. Edit every line.'),
        ('Trusting AI on platform rules.', 'Check official help pages; AI can be out of date.'),
        ('Pasting private customer data.', 'Remove names and numbers first.'),
        ('Letting AI decide strategy.', 'You set the goal, audience and message; AI drafts options.'),
    ],
    quiz=[
        {'q': 'An AI draft says a shop opened "in 1950". What should you do?',
         'o': ['Post it', 'Check the real date with the owner before posting', 'Remove the shop\'s name', 'Ask the AI if it\'s sure and post anyway'],
         'a': 'B', 'why': 'AI can invent facts; confirm with a real source.'},
        {'q': 'Which job is AI weakest at?',
         'o': ['Brainstorming 20 hooks', 'Knowing a local shop\'s real prices and timings', 'Rewriting a caption shorter', 'Grouping comments into themes'],
         'a': 'B', 'why': 'Local, current facts must come from the business or a real source.'},
        {'q': 'What should you remove before asking AI to summarise customer comments?',
         'o': ['Emojis', 'Names, phone numbers and other personal details', 'Nothing', 'Positive comments'],
         'a': 'B', 'why': 'Protect customers\' privacy.'},
        {'q': 'What makes AI-assisted posts stand out from everyone else\'s?',
         'o': ['More AI phrases', 'Your real local details, photos and the owner\'s own words', 'Longer captions', 'More hashtags'],
         'a': 'B', 'why': 'AI can\'t supply your local knowledge or proof.'},
    ],
    study='The free AI plans and Meta\'s advice on authentic captions (about 20 minutes)',
    action='write 5 reusable prompts, use them for a week of posts and log time saved and errors caught',
)

L2 = lesson(
    13, 2,
    title='AI for images, video and analytics: risks and labels',
    weeks=(34, 34), hours=2,
    outcome='Use AI tools for visuals, editing and analysis without misleading anyone, know when YouTube, Meta and Indian rules require AI content to be labelled, and keep AI-made content worth watching.',
    split='40 minutes study, 1 hour 20 minutes action',
    core=f"""
### Where AI helps with visuals, video and numbers

- **Images:** backgrounds for thumbnails and covers, simple illustrations, mock-ups, removing a distracting object from your own photo. The free Gemini plan lists image generation and editing; ChatGPT's free plan lists limited image creation ({ASOF}).
- **Video:** auto-captions, cutting silences, voice clean-up, reframing for vertical. YouTube's Shorts tools include AI features such as effects and photo-to-video, and YouTube Create has AI editing features in some countries.
- **Analysis:** paste your Posting Log numbers (no personal data) and ask for patterns, then check the maths yourself; draft report wording.

The Free AI Generalist Course covers AI images, video and voice in Level 3.

### Where AI misleads

The line is **realistic content that makes people believe something false**:

- A "product photo" generated by AI that doesn't show the real product
- Adding a waterfall, a bigger room or a crowd that wasn't there
- A real person shown saying or doing something they didn't
- A fake "customer" testimonial video

Routine edits (brightness, removing a stray wire from a photo of the real place) are fine. Inventing what the customer will get is a misleading ad (SMM-M05-L02), whatever tool made it.

### Labels and disclosure ({ASOF})

- **YouTube** requires creators to disclose content that is **meaningfully altered or synthetically generated and looks realistic**: making a real person appear to say or do something they didn't, altering footage of real events or places, or realistic AI scenes. You don't need to disclose clearly unrealistic content, beauty filters, or using AI for scripts, outlines, thumbnails, titles or captions. You disclose in YouTube Studio (the "AI use" choice when uploading). Creators who repeatedly don't disclose may have a label added and face penalties such as content removal or suspension from the Partner Program.
- **Meta** adds "AI info" labels to images, video and audio when it detects industry AI signals or when people self-disclose, with a more prominent label for high-risk content that could deceive the public.
- **India:** the IT (Intermediary Guidelines and Digital Media Ethics Code) Amendment Rules, 2026, in force since 20 February 2026, require AI-generated or altered content that appears real ("synthetically generated information") to be clearly labelled, and social media platforms must ask users to declare such content before it is published. Routine editing, formatting and technical correction are not treated as synthetic content. Deepfakes that misrepresent real people or events, and non-consensual intimate imagery, are prohibited (check current rules).

When in doubt, disclose. A one-line label costs nothing; a deceived audience costs your reputation.

### AI-made content still has to be worth watching

YouTube says videos made with AI can be recommended as broadly as other videos, but its monetisation policies don't pay for **inauthentic content**: mass-produced, template-like or repetitive videos, a policy it clarified in July 2025. Use AI to make your own ideas faster, not to flood platforms with sameness.

### Other risks

- **Text in AI images** is often misspelled, especially Malayalam. Add text yourself in Canva.
- **Music and voices:** check the licence of any AI music or voice tool before using it in a client's ad.
- **Over-automated replies:** customers notice robotic answers. Use templates, but reply as a person.
""",
    example="""
**Kakkayam Hills Homestay** tried three AI uses (made-up example):

| Use | Decision | Why |
| --- | --- | --- |
| Remove a power line from a real sunrise photo taken on the balcony | ✅ Fine | Routine edit; the view is real |
| Generate a "waterfall view" image for the room page | ❌ Dropped | There is no waterfall; it would mislead guests |
| AI voice-over in English for a real room-tour video | ✅ With a note | The footage is real; they added "Voice-over made with AI" in the description and ticked YouTube's AI disclosure because the voice sounded like a real person |

They also asked an assistant to summarise 60 Google reviews (names removed): the top themes were "breakfast", "quiet" and "steep road at night". They added a "how to reach us after dark" Highlight.
""",
    resources=[
        ('yt-ai', 'Read what needs disclosure, what doesn\'t, and how to disclose', '10 min'),
        ('meta-ai-labels', 'Read how Meta labels AI content, including the updates', '10 min'),
        ('bt-it-rules', 'Read what the 2026 rules require for AI content', '10 min'),
        ('yt-monetisation', 'Read the section on inauthentic and reused content', '10 min'),
        ('yt-shorts-guide', 'Look at the AI tools listed for Shorts', '3 min'),
    ],
    steps=[
        'Study the resources (about 45 minutes).',
        'Make 2 AI-assisted visuals for your sprint or pilot (for example a thumbnail background and an illustration), adding all text yourself in Canva.',
        'Do 1 AI-assisted video edit (captions, silence cutting or voice clean-up) and compare the time with editing by hand.',
        'For each piece, decide with the decision tree whether a label is needed, and apply it.',
        'Write your AI disclosure rules for yourself and your clients.',
    ],
    proof='The 3 AI-assisted pieces (links or files), your decision-tree notes for each, and your written AI disclosure rules.',
    templates=[
        ('AI disclosure decision tree', """
1. Does it look realistic (photo, video, audio, voice)?
   NO  -> no AI label needed (e.g. a cartoon)
   YES -> go to 2
2. Is it only routine editing of real content?
   (brightness, colour, cropping, removing a stray wire,
   captions, script help)
   YES -> no label needed
   NO  -> go to 3
3. Could viewers believe something false about a real
   person, place, event or product?
   YES -> don't post it (or remake it with real content)
   NO, but AI made or changed realistic parts
       -> LABEL IT: YouTube "AI use: Yes"; a clear line such
          as "Made with AI" / "AI-ലൂടെ നിർമ്മിച്ചത്"; accept the
          platform's AI label
When unsure: label it.
""", ''),
        ('AI risk checklist', """
[ ] Nothing shows a product, place or result that isn't real
[ ] No real person shown saying or doing something they didn't
[ ] Text in images added by me (no AI spelling errors)
[ ] AI music or voice licence checked for this use
[ ] Labels applied where the decision tree says so
[ ] Not mass-produced: each piece adds something real
[ ] Numbers from AI analysis re-checked by hand
[ ] No personal data pasted into AI tools
""", ''),
    ],
    mistakes=[
        ('AI "product photos".', 'Customers expect what they see. Use real photos of the real product.'),
        ('Skipping disclosure because it\'s "just a voice".', 'A realistic AI voice can need a label. When unsure, label it.'),
        ('Flooding a channel with template videos.', 'YouTube doesn\'t monetise inauthentic, mass-produced content.'),
        ('Trusting AI maths.', 'Check every calculation in your report.'),
    ],
    quiz=[
        {'q': 'According to YouTube Help, which of these needs AI disclosure?',
         'o': ['Using AI to write the script', 'A beauty filter', 'Making a real person appear to say something they didn\'t', 'AI-generated captions'],
         'a': 'C', 'why': 'Realistic altered content about real people needs disclosure.'},
        {'q': 'Under India\'s 2026 IT rule amendments, what must happen to AI content that appears real?',
         'o': ['Nothing', 'It must be clearly labelled as synthetically generated', 'It must be deleted', 'It must be in English'],
         'a': 'B', 'why': 'Synthetic content that appears real must be labelled; routine edits are exempt.'},
        {'q': 'A homestay wants an AI image of a waterfall near the rooms, but there isn\'t one. What do you advise?',
         'o': ['Post it with nice music', 'Don\'t post it: it would mislead guests', 'Post it without a label', 'Post it only on WhatsApp'],
         'a': 'B', 'why': 'Showing something that isn\'t real is misleading, whatever the tool.'},
        {'q': 'What did YouTube clarify in July 2025?',
         'o': ['AI videos are banned', 'Inauthentic (mass-produced, repetitive) content isn\'t monetised', 'Shorts are paid per view', 'Captions are required'],
         'a': 'B', 'why': 'The "repetitious content" policy was renamed and clarified as inauthentic content.'},
    ],
    study='YouTube\'s AI disclosure rules, Meta\'s AI labels, India\'s 2026 IT rules and YouTube\'s inauthentic content policy (about 45 minutes)',
    action='make 3 AI-assisted pieces, decide and apply labels with the decision tree, and write your AI disclosure rules',
)

LESSONS = [L1, L2]

MODULE = module(
    13,
    title='AI for social media',
    weeks=(33, 34), hours=5.5,
    overview="""
Use AI to work faster on ideas, scripts, captions, visuals, editing and analysis, while protecting accuracy, originality, privacy and honesty, and following the labelling rules of YouTube, Meta and India.

AI can halve the time a post takes, or flood your account with generic, wrong or misleading content. In two weeks you'll build reusable prompts that carry your strategy and voice, check every AI output, use AI for visuals and editing within clear limits, and learn exactly when AI content must be labelled.

The module project is your AI playbook: the prompts, checks and rules you'll use with clients.
""",
    outcomes=[
        'Write prompts that include role, context, task, constraints, examples and an honesty instruction',
        'Catch made-up facts, awkward Malayalam and generic phrases in AI drafts',
        'Use AI for images, video editing and analysis without misleading anyone',
        'Apply YouTube\'s, Meta\'s and India\'s AI labelling rules',
        'Explain why mass-produced AI content doesn\'t pay',
    ],
    lessons=LESSONS,
    project='Your AI playbook',
    project_week=34,
    project_steps=[
        'Put your 5 prompts, the AI output check, the disclosure decision tree and the risk checklist in one document.',
        'Add your time-saved and errors-caught log from SMM-M13-L01.',
        'Add 3 AI-assisted posts as examples, with what you changed.',
        'Write a short "AI policy for clients": what you use AI for, what you never do, and how you label.',
    ],
    project_proof='Your AI playbook document in 13 AI.',
    rubric=[
        ('Prompts', 'One-line requests', 'Some context', 'Reusable prompts with role, context, constraints, examples and honesty'),
        ('Checking', 'Posts AI output unedited', 'Checks some facts', 'Checks every fact, Malayalam and claim; logs errors'),
        ('Visuals and video', 'Misleading or misspelled visuals', 'Some good uses', 'Realistic, honest visuals with own text; useful edits'),
        ('Labels', 'Unaware of rules', 'Knows YouTube\'s rule', 'Applies YouTube, Meta and Indian rules with a decision tree'),
        ('Privacy and quality', 'Pastes private data; template content', 'Some care', 'No private data; every piece adds something real'),
    ],
    short=[
        'Write 2 prompts (hooks and captions) and use them for 3 posts.',
        'Do the decision tree for one AI-assisted piece.',
        'Write a five-line AI policy for clients.',
    ],
    flashcards=[
        ('Six parts of a good prompt?', 'Role, context, task, constraints, examples, honesty instruction.'),
        ('What does AI do worst for local marketing?', 'Local, current facts such as prices, timings and names.'),
        ('Does YouTube need AI disclosure for script help or beauty filters?', 'No.'),
        ('What does YouTube need disclosed?', 'Realistic altered or synthetic content, such as real people saying things they didn\'t.'),
        ('Meta\'s label for AI content?', '"AI info".'),
        ('Since when are India\'s 2026 AI-content labelling rules in force?', '20 February 2026.'),
        ('Are routine edits "synthetic content" under India\'s rules?', 'No: routine editing, formatting and technical correction are exempt.'),
        ('What does YouTube not monetise (clarified July 2025)?', 'Inauthentic, mass-produced or repetitive content.'),
    ],
    mistakes=[
        ('Using AI to fake proof.', 'Never generate testimonials, results or product images that aren\'t real.'),
        ('Relying on one AI tool\'s answer about rules.', 'Check the official help page; rules change.'),
        ('Replacing your voice.', 'AI drafts; you decide and write the final version.'),
    ],
)
