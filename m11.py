from common import lesson, module

L1 = lesson(
    11, 1,
    title='AI for research, marketing and content',
    weeks=(26, 26), hours=3,
    outcome='Use free AI assistants to speed up research, marketing and content, while checking facts and keeping your own voice.',
    split='1 hour 15 minutes study, 1 hour 45 minutes action',
    core="""
AI assistants such as Gemini, ChatGPT and Claude all have free plans (their limits change; check current rules). Used well, they are a fast, tireless assistant that drafts, summarises, brainstorms and explains. Used badly, they produce confident nonsense in your name. This lesson is about using them well.

### A prompt pattern that works

Give the AI what a new human assistant would need:

1. **Role:** "You are a marketing assistant for a home bakery in Kuttiady, Kerala."
2. **Context:** who your customers are, what you sell, your prices, your tone.
3. **Task:** exactly what you want: "Write 10 Instagram caption ideas for this week."
4. **Format:** "A numbered list, each under 25 words, with one line in Malayalam."
5. **Constraints:** "No made-up claims. No discounts. Don't mention competitors."
6. **Examples:** paste one or two of your best past posts, so it can follow your voice.

Then **iterate**: "Make number 3 shorter", "Use simpler words", "Give me five more like number 7."

### Good uses in this course

| Job | What to ask | Your check |
| --- | --- | --- |
| Summarise interview notes | "Group these notes by theme and count how often each appears" (remove names first) | Compare with your own counts |
| Draft interview questions | "Write 10 open questions about past behaviour; no leading questions" | Delete any "would you…?" questions |
| Market and competitor scan | "What should I check about home bakeries in a small Kerala town?" | Verify every fact on real websites, maps and visits |
| Content ideas and captions | "Give me 14 post ideas across these four pillars" | Edit into your own voice; have Malayalam checked if you are unsure |
| Reel and Short scripts | "A 30-second script: a hook, 3 steps, a call to action" | Film it yourself; keep it real |
| Google profile description | "Write a 600-character description using only these facts" | Make sure every fact is true |
| Explaining hard topics | "Explain break-even simply, with a cake example" | Cross-check with your lesson or OpenStax |

### Work from your own sources

**Gemini Notebook** (formerly NotebookLM) lets you upload your own documents, such as interview summaries, and ask questions about them. Answers based on your own files are less likely to be invented, but still check them.

### Know the limits

- **AI makes things up.** It can invent facts, statistics, laws, prices and links that look real. Never publish a fact, number, legal claim or link from AI without checking a real source. (This course uses only links that were opened and checked.)
- **AI doesn't know your town.** It can't tell you what Kuttiady parents want. Only interviews can.
- **Your voice matters.** Customers in a small town know you. Edit AI drafts until they sound like you.
- **Privacy:** never paste customers' names, phone numbers, addresses or private details. Google's Gemini API terms, for example, say that on free tiers your inputs may be used to improve Google's products and may be read by human reviewers, and they advise against submitting sensitive or personal information.
- **Honesty:** don't use AI to create fake reviews or testimonials, pictures of products you don't make, or results you didn't achieve. A misleading ad is illegal whoever, or whatever, wrote it.
""",
    example="""
Nisha's prompt for a week of content:

> You are a social media assistant for Nisha's Oven, a home bakery in Kuttiady, Kerala. Customers are parents within 5 km who want home-made birthday cakes with natural colours and less sugar. Prices: ₹650–₹1,100. Tone: warm, simple, honest. Write 7 post ideas for WhatsApp Status and Instagram, one a day, covering show, teach, prove and personal. For each: a one-line hook, a two-line caption in English, one line in Malayalam and a call to action. No discounts, no health claims, no made-up facts.

She kept four ideas, rewrote two in her own words and dropped one that called her cakes "100% sugar-free", which wasn't true. Her sister checked the Malayalam lines.

Arun pasted his 17 anonymised interview notes (codes, no names) into an AI assistant and asked it to group them by theme and count. It found the same top three patterns he had found, plus one he had missed: four owners mentioned trouble keeping prices updated during festival sales. He checked the notes himself, confirmed it, and added festival price updates to his care plan.
""",
    resources=[
        ('elements-ai', 'Free. Chapter 1 of "Introduction to AI", on what AI can and can\'t do (length not stated)', 'budget 1 hour'),
        ('gemini-plans', 'See what the free plan includes (check current rules)', '5 min'),
        ('claude-plans', 'See what the free plan includes (check current rules)', '5 min'),
        ('chatgpt-plans', 'See what the free plan includes (check current rules)', '5 min'),
        ('gemini-notebook', 'Optional: try it with one of your own documents', '15 min'),
    ],
    steps=[
        'Write your "business context" paragraph: who you serve, what you sell, your prices, your tone and your rules (no made-up claims). Save it to reuse.',
        'Build a prompt kit of 5 prompts for your business: a research summary, a content plan, captions, a Reel script and a reply draft.',
        'Run each prompt, then edit the outputs into your own voice.',
        'Fact-check one AI output against a real source (a website, a phone call or a visit), and note anything that was wrong.',
        'Publish 3 pieces of AI-assisted content that you edited, and track replies and orders as usual.',
    ],
    proof='Your business context paragraph, your 5-prompt kit, your fact-check notes and links to the 3 published posts with their results.',
    templates=[
        ('business context and prompt kit', """
BUSINESS CONTEXT (paste before any prompt)
Business: ____ in ____ (place)
Customers: ____ (who, where, what they want)
What I sell, and prices: ____
My tone: ____ (for example: warm, simple, honest)
Rules: no made-up facts, claims or reviews; no
discounts unless I say so; say "I'm not sure" if unsure.

PROMPT KIT
1. RESEARCH: "Group these anonymised notes by theme,
   count each theme and quote one example of each:
   [notes]"
2. CONTENT PLAN: "Plan 14 posts for [channel] across
   show, teach, prove, personal, and one offer a week."
3. CAPTIONS: "Write 3 caption options for this photo:
   [description]. Under 40 words, one line in Malayalam."
4. REEL SCRIPT: "Write a 30-second script: a 2-second
   hook, 3 steps and a call to action, in plain words."
5. REPLY DRAFT: "Draft a polite reply to this customer
   question: [question]. Use only these facts: [facts]."

BEFORE YOU PUBLISH
[ ] Every fact, price and claim is true
[ ] It sounds like me, not a robot
[ ] The Malayalam has been checked
[ ] No customer's personal data went into the AI
""", ''),
    ],
    mistakes=[
        ('Publishing AI text without editing.', 'Generic AI posts sound like everyone else\'s. Edit them into your own voice.'),
        ('Trusting AI facts, laws or links.', 'AI can invent convincing details. Check every fact against a real source.'),
        ('Pasting customer data.', 'Remove names, numbers and addresses before you ask AI to analyse notes.'),
        ('Fake reviews, results or product images.', 'They are dishonest and can break consumer law. Show only what is real.'),
        ('Asking AI instead of customers.', 'AI can help you prepare questions, but only real people can tell you what they want.'),
    ],
    quiz=[
        {'q': 'Which prompt is likely to give a better result?',
         'o': ['"Write a post"', 'One with a role, context, task, format, constraints and an example', '"Make it viral"', 'A single word'],
         'a': 'B', 'why': 'The more an assistant knows about your situation, the more useful its draft.'},
        {'q': 'An AI tool gives you a GST rule and a link. What should you do?',
         'o': ['Publish it', 'Check it on the official GST portal or with a professional before relying on it', 'Assume it is right', 'Share it in groups'],
         'a': 'B', 'why': 'AI can invent rules and links that look real.'},
        {'q': 'Why remove names and phone numbers before pasting interview notes into an AI tool?',
         'o': ['It is faster', 'To protect people\'s privacy, since free-tier inputs may be used and read by the provider', 'AI can\'t read names', 'WhatsApp requires it'],
         'a': 'B', 'why': 'Personal data shared with a free tool may not stay private.'},
        {'q': 'Which use of AI is not acceptable?',
         'o': ['Drafting captions that you then edit', 'Summarising anonymised notes', 'Writing fake customer reviews', 'Explaining break-even'],
         'a': 'C', 'why': 'Fake reviews deceive customers, whoever writes them.'},
    ],
    study='Elements of AI chapter 1 and the free-plan pages for Gemini, Claude and ChatGPT (about 1 hour 15 minutes)',
    action='write your business context and a 5-prompt kit, fact-check an output and publish 3 edited posts',
)

L2 = lesson(
    11, 2,
    title='AI for support and operations, with its risks and limits',
    weeks=(26, 26), hours=3,
    outcome='Use AI to draft customer replies, FAQs, SOPs and simple analyses safely, and set clear rules for when a human must decide.',
    split='30 minutes study, 2.5 hours action',
    core="""
### Useful jobs for AI behind the scenes

- **FAQs and quick replies:** paste your offer sheet and ask for the 10 questions customers are most likely to ask, with short answers that use only your facts. Edit them, then add the best ones to WhatsApp Business.
- **SOP drafts:** describe a task in a voice note, turn it into text (many phones can transcribe), and ask AI to turn it into numbered steps with quality checks. Then test the SOP with a person (ENT-M10-L01).
- **Tricky messages:** ask for a calm, polite draft for a complaint or a late payer, then send it in your own words.
- **Simple analysis:** paste a few rows of your sales or KPI sheet (no personal data) and ask "What patterns do you see?" or "Which formula would give weekly totals?" Check the result yourself.
- **Translation:** English to Malayalam and back, for menus, captions and notices. Have a native speaker check anything important.
- **Document drafts:** a first draft of terms of sale, a partnership note or a job description, which you then check against official sources or with a professional.

### AI as part of what you sell

If you sell services, AI can make you faster. Arun now offers "AI-assisted FAQ setup": he drafts a shop's FAQs and quick replies with AI, edits them with the owner and loads them into WhatsApp Business. What the shop pays for is his judgement and setup, not the AI.

Some platforms now offer AI agents that answer customers automatically. Before you switch one on, test it hard: an unsupervised bot can give wrong prices or make promises you can't keep. For a micro-business, replies that AI drafts and a human checks are the safer place to start.

### The risks, and how to manage them

| Risk | Example | Your rule |
| --- | --- | --- |
| Wrong answers | AI tells a customer the wrong price or delivery date | A human checks every message about money, dates or promises |
| Privacy | Customers' phone numbers pasted into a free AI tool | Never paste personal data; use codes |
| Tone and bias | A reply that sounds rude or stereotyped | Read every reply aloud before sending |
| Made-up facts | An invented legal rule in your terms of sale | Check laws and schemes on official sites |
| Copyright and trademarks | An AI image that copies a famous character or brand | Use AI images only for generic ideas, never for logos or other people's characters |
| Over-dependence | You can't do the job when a tool is down or changes | Keep your SOPs and templates, and know the work yourself |
| Cost creep | Several paid tools "just in case" | Stay on free plans until a tool clearly pays for itself |
| Platform rules | An unofficial WhatsApp bot gets your number banned | Use official tools only |

### Write an AI use policy

Write five or six rules on one card, for you and anyone who helps you: what AI may draft, what a human must always check, what data never goes into AI, and how you stay honest with customers about it.
""",
    example="""
Arun's AI use policy, stuck above his desk:

1. AI drafts; I decide and I send.
2. Any message about money, dates, refunds or promises: I check every word.
3. No customer names, numbers, addresses or chats go into AI tools. I use codes.
4. Laws, schemes and fees come from official sites, never from AI alone.
5. No AI-made reviews, testimonials or fake results.
6. If a client asks, I tell them which parts were AI-assisted.

His red-team test: he asked an AI assistant five tricky questions that a textile shop's customers might send, such as "Can I return a saree after wearing it?" and "Do you deliver to Kannur tomorrow?". It confidently invented a 7-day return policy and a Kannur delivery service that the shop doesn't offer. A wrong return promise on a ₹2,500 saree would have cost the shop money and trust, so both Arun and his client agreed to keep a human in every reply.
""",
    resources=[
        ('gemini-api-terms', 'Read how free-tier data may be used and reviewed', '10 min'),
        ('dpdp', 'Re-read the duties on consent and security (check current rules)', '10 min'),
        ('wa-business', 'Check which business tools the app offers today', '5 min'),
    ],
    steps=[
        'Paste your offer sheet (no personal data) into an AI assistant and ask for 10 likely customer questions with short answers that use only your facts. Edit them, and add the best as WhatsApp Business quick replies.',
        'Turn one task into an SOP draft with AI, from a voice note or rough notes, then test it with a person.',
        'Run a red-team test: ask the AI 5 tricky customer questions about your business and note every wrong or invented answer.',
        'Write your AI use policy in 5–6 rules.',
        'For one week, use AI for one support or operations job, following your policy. Note the time saved and any mistakes you caught.',
    ],
    proof='A screenshot of your edited FAQ quick replies, the AI-drafted and tested SOP, your red-team notes and your AI use policy.',
    templates=[
        ('AI use policy, red-team test and FAQ prompt', """
AI USE POLICY (one card)
1. AI drafts; a human decides and sends.
2. A human checks every message about money, dates,
   refunds or promises.
3. No personal data (names, numbers, addresses, chats)
   goes into AI tools.
4. Laws, schemes and fees come from official sources.
5. No AI-made reviews, testimonials, results or
   product photos.
6. If customers ask how we use AI, we tell them honestly.

RED-TEAM TEST (5 tricky questions)
Question | AI's answer | Right? | What was wrong
1.
2.
3.
4.
5.

FAQ PROMPT
"Here is my offer sheet: [paste]. List the 10 questions
customers are most likely to ask, with answers under 30
words. Use only facts from the offer sheet. If it doesn't
answer a question, write 'ASK OWNER'."
""", ''),
    ],
    mistakes=[
        ('Letting AI answer customers unsupervised.', 'A confident wrong answer about a price or delivery costs money and trust. Keep a human in the loop.'),
        ('Giving AI personal data.', 'Use codes instead of names and numbers, and keep customer lists out of AI tools.'),
        ('Believing AI analysis without checking.', 'Recalculate the key numbers yourself before you act on them.'),
        ('Paying for AI tools too early.', 'Free plans are enough for a micro-business at first. Upgrade only when the time saved is clearly worth it.'),
        ('Using unofficial WhatsApp bots.', 'They can break WhatsApp\'s terms and get your number banned.'),
    ],
    quiz=[
        {'q': 'Which job is safest to give AI?',
         'o': ['Sending refund decisions automatically', 'Drafting FAQ answers that you edit and check', 'Quoting prices to customers unsupervised', 'Writing reviews'],
         'a': 'B', 'why': 'The AI saves time on the draft, and a human makes sure it is right.'},
        {'q': 'In a red-team test, AI invents a return policy the shop doesn\'t have. What should you do?',
         'o': ['Adopt the policy', 'Keep a human checking every reply about policies, prices or promises', 'Stop using WhatsApp', 'Ignore it'],
         'a': 'B', 'why': 'The test showed exactly where unsupervised AI would hurt the business.'},
        {'q': 'What should an AI use policy include?',
         'o': ['Nothing', 'What AI may draft, what a human must check, what data never goes in, and honesty with customers', 'Only which tool to buy', 'The password for the AI tool'],
         'a': 'B', 'why': 'Clear rules keep you and any helpers consistent and safe.'},
        {'q': 'Why keep your own SOPs and templates even when AI can draft them?',
         'o': ['For decoration', 'So the business keeps running if a tool changes or fails, and you still understand the work', 'The law requires it', 'To use more paper'],
         'a': 'B', 'why': 'Tools change; your knowledge of the work is what stays.'},
    ],
    study='the Gemini API terms on free-tier data, the DPDP summary and the WhatsApp Business tools (about 30 minutes)',
    action='build AI-drafted FAQs, an AI-drafted SOP, run a red-team test and write your AI use policy',
)

LESSONS = [L1, L2]

MODULE = module(
    11,
    title='AI for entrepreneurs',
    weeks=(26, 26), hours=7,
    overview="""
You are also learning to be an AI generalist, so put those skills to work in your own business first. AI can save you hours each week on research, content, replies and paperwork. It can also make confident mistakes, leak private data and make your business sound like everyone else's.

This short module shows where AI helps a micro-business most, the prompts that work, and the rules that keep you honest and safe.
""",
    outcomes=[
        'Write prompts with a role, context, task, format, constraints and examples, and improve the output step by step',
        'Use free AI tools for research, content, FAQs, SOPs and simple analysis, always checking the result',
        'Name the main risks (made-up facts, privacy, wrong answers, copyright, over-dependence) and how to manage each',
        'Write an AI use policy for your business',
    ],
    lessons=LESSONS,
    project='AI playbook',
    project_steps=[
        'Your business context paragraph and 5-prompt kit (L01).',
        'Your edited FAQ quick replies and AI-drafted SOP (L02).',
        'Your red-team results and AI use policy (L02).',
        'A short note: the three AI uses that saved you the most time, and how much each week.',
    ],
    project_proof='Your AI playbook (one Google Doc) in Founder Toolkit/11 AI.',
    rubric=[
        ('Prompting', 'One-line prompts', 'Some context given', 'Role, context, task, format, constraints and examples; improves the output step by step'),
        ('Checking', 'Publishes AI output as it is', 'Checks sometimes', 'Checks every fact, price and claim; edits into own voice'),
        ('Privacy', 'Pastes customer data', 'Removes some details', 'Never pastes personal data; uses codes'),
        ('Policy', 'None', 'Informal rules', 'A written AI use policy, followed and tested with a red-team test'),
    ],
    short=[
        'L01: write the business context paragraph and one content prompt, and publish one edited post.',
        'L02: write your AI use policy and run a red-team test with 3 questions.',
    ],
    mistakes=[
        ('Treating AI as an oracle.', 'It is a drafting assistant; you are responsible for what goes out.'),
        ('Copy-pasting generic output.', 'Edit everything into your own voice.'),
        ('Pasting private data.', 'Never put customers\' personal details into AI tools.'),
    ],
)
