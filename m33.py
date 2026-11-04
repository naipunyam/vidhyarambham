from common import lesson, module, link, xref, table, fence, Q, CHECK

L1 = lesson(
    33, 1,
    outcome='You can explain how customers really decide (needs, trust, risk, price perception), use honest, question-led selling, and see common marketing effects in shops and ads.',
    split='20 minutes reading, 35 minutes of tasks',
    principle='Customers buy solutions to their problems from people they trust; the honest seller asks questions first, explains clearly, reduces risk and never tricks; many famous "marketing hacks" are weaker than claimed.',
    science=f"""
**How customers decide.** Customers buy to solve a problem or meet a need (a reliable phone for work, a tuition teacher their child likes, a tasty lunch near the bus stand). They weigh **value** against **price**, **risk** (Will it work? Can I return it?) and **effort** (How hard is it to buy?). They use shortcuts (Module 1): brand familiarity, social proof (reviews, crowds), authority (experts, certificates) and how the price is presented. Most decisions are made quickly, and the feeling of trust in the seller weighs heavily, especially in small towns where reputation spreads by word of mouth.

**Question-led selling.** Research on large-scale sales by Neil Rackham's team (Huthwaite, 1980s, observing over 35,000 sales calls) found that successful salespeople in complex sales asked more questions about the customer's situation and problems, and talked less about features, than less successful ones. Their "SPIN" sequence: **Situation, Problem, Implication, Need-payoff** questions. It is industry research rather than peer-reviewed science, but it fits what we know about listening (PD-M25-L02) and interests (PD-M29-L01). The {xref('ent', 'ent-m07', 'Entrepreneurship sales module')} teaches a full sales process.

**Price perception effects (honest status):**
- **Charm prices** (₹499 instead of ₹500) can increase sales because people read the left digit first; studies find real but modest effects that vary by product.
- **Anchoring** (a high "MRP" or a premium option shown first) strongly affects perceived value (PD-M03-L01).
- **The decoy effect:** adding a clearly worse third option can make one option look better (Joel Huber and colleagues, 1982). Later replications found the effect is **weaker and less reliable** than early studies suggested, especially outside the lab.
- **Free shipping, free trials and bundles** reduce perceived risk and effort.
- **Loss framing** ("Don't lose your discount") can push people, but becomes a dark pattern when false.

**Customer psychology after the sale.** Satisfied customers who feel respected return and recommend; research on the "service recovery paradox" suggests a problem fixed very well can sometimes leave a customer even more loyal than before, though results are mixed. Handling complaints with listening, apology and a fix (PD-M26-L03, PD-M31-L02) is one of the best marketing tools for a small business.

**Ethics.** Honest marketing tells the truth about the product, its price and its limits. Fake reviews, hidden charges and false scarcity are illegal under Indian consumer law in many cases and destroy trust (PD-M32-L02).
""",
    evidence=[
        ('Trust and reputation strongly affect buying', 'strong', 'Consistent across marketing and consumer research.'),
        ('Question-led selling (SPIN)', 'moderate', 'Large industry observation study; consistent with listening research.'),
        ('Charm pricing', 'moderate', 'Real but modest effects; varies by product.'),
        ('Anchoring on prices', 'strong', 'Well replicated.'),
        ('Decoy effect', 'mixed', 'Early lab findings; later replications weaker.'),
        ('Service recovery paradox', 'mixed', 'Some studies support it; others don\'t.'),
    ],
    example="""
Ashiq starts weekend tuition for two Class 9 students and wants more. His first flyer listed features: "Maths and Science, Class 8–10, experienced tutor, ₹1,500/month."

He changes approach. He visits three parents and asks **questions first**: "How is your child finding maths this year?" (situation) "What's hardest for her?" (problem) "How is that affecting her marks or confidence?" (implication) "If she could do one chapter's problems on her own each week, what would that mean for you?" (need-payoff). One mother says her daughter cries before tests; another worries about the Class 10 board exam.

His new offer **reduces risk**: "First two classes free; if she doesn't improve in a month, you don't pay for the second month." He shows **real social proof** (two current students' parents agree to be called) and a **clear, honest price** (₹1,500 a month for two classes a week). He refuses to write "only 2 seats left" when he has six. Within six weeks he has five students, three through word of mouth.
""",
    apply=f"""
**Honest selling in five steps:**
1. **Ask before telling:** situation, problem, implication, need-payoff questions.
2. **Summarise their need** in their words (PD-M25-L02).
3. **Explain how your product or service meets that need,** including what it **won't** do.
4. **Reduce risk:** a trial, a guarantee, references, clear terms.
5. **Make the next step easy and the no easy** (PD-M28).

{fence('''CUSTOMER CONVERSATION CARD
S - Situation: "How do you ______ at the moment?"
P - Problem:   "What's hardest about ______?"
I - Implication: "How does that affect ______?"
N - Need-payoff: "If ______ were solved, what would that mean for you?"
Summary: "So what you need is ______. Is that right?"
Offer: what it does ______ ; what it doesn't do ______ ; risk reducer ______
Next step: ______  (easy no: "No problem if it's not right for you.")''')}

**Shop-floor psychology walk:** next time you go to a supermarket, textile shop or mobile shop, look for: anchors (MRP, "was" prices), charm prices, bundles, end-of-aisle displays, decoys, social proof (bestseller tags), scarcity signs and checkout impulse items.

**With others:** if friends run small businesses, offer to be a "mystery customer" and give SBI feedback on the experience.
""",
    resources=[
        ('decisionlab', 'Search the index for the decoy effect and read it', '5 minutes'),
        ('darkpatterns', 'Re-read the list: which of these have you seen in shops or apps this month?', '5 minutes'),
        ('os-12', 'Re-read 12.3 on persuasion routes, thinking about advertising', '10 minutes'),
    ],
    steps=[
        'Do a shop-floor psychology walk in one shop and one app, and list at least eight techniques you see, each with an honest-or-not verdict.',
        'Collect five real ads and note the customer need each targets and the influence principle used.',
        'Have one real customer-style conversation using the SPIN card (selling a service you offer, or helping a friend or family business with a customer).',
        'Write a 60-word honest offer for something you could sell (tuition, a skill, a product), with a risk reducer.',
    ],
    proof='Your list of eight shop and app techniques with verdicts, five ad notes, a SPIN conversation note and your 60-word honest offer.',
    templates=[('Shop-floor psychology walk', """SHOP-FLOOR PSYCHOLOGY WALK      Shop/app: ______  Date: ______
Technique | Where I saw it | Honest or manipulative? | Did it affect me?
Anchor (MRP / "was" price) | ______ | ______ | ______
Charm price | ______ | ______ | ______
Bundle / free gift | ______ | ______ | ______
Decoy option | ______ | ______ | ______
Bestseller / social proof tag | ______ | ______ | ______
Scarcity / urgency sign | ______ | ______ | ______
Placement (eye level, checkout) | ______ | ______ | ______
MY HONEST OFFER (60 words): ______________________""", '')],
    mistakes=[
        ('Talking features before understanding needs.', 'Ask questions first.'),
        ('Overselling.', 'Say what your product won\'t do; trust grows.'),
        ('Believing marketing "hacks" are magic.', 'Many effects (decoys, charm prices) are modest and inconsistent; value and trust matter most.'),
        ('Faking scarcity or reviews.', 'It is dishonest, often illegal, and destroys reputation.'),
    ],
    quiz=[
        Q('What did Rackham\'s large study of sales calls find successful salespeople did?', 'Asked more questions about the customer\'s situation and problems', 'Talked more about features', 'Spoke faster', 'Offered bigger discounts', why='Question-led selling (SPIN).'),
        Q('What is the honest status of the decoy effect?', 'Early lab findings; later replications weaker and less reliable', 'Proven in every setting', 'Never studied', 'Illegal', why='Effects outside the lab are inconsistent.'),
        Q('Which is the best way to reduce a customer\'s perceived risk?', 'A free trial, a guarantee or references', 'Fake reviews', 'A countdown timer', 'Hiding the price', why='Honest risk reducers build trust.'),
        Q('What does "N" in SPIN stand for?', 'Need-payoff', 'Negotiation', 'Number', 'Network', why='What solving the problem would mean for the customer.'),
    ],
    study='read the lesson and the decoy-effect entry',
    action='do a shop-floor psychology walk, analyse five ads, hold one SPIN conversation and write an honest offer',
)

L2 = lesson(
    33, 2,
    outcome='You can prepare for job and Kerala PSC interviews with structured answers (STAR), handle interview and exam nerves with tested tools, and run a recorded mock interview.',
    split='25 minutes reading, 45 minutes including a mock interview',
    principle='Interviewers judge what you say and how clearly you say it; prepared, structured answers with real examples, calm delivery and honest humility beat memorised speeches, and nerves can be managed with practice, reappraisal and good sleep.',
    science=f"""
**What interviews measure.** Decades of research on hiring (for example, the meta-analyses by Frank Schmidt and John Hunter) find that **structured interviews** (the same job-related questions for everyone, scored against clear criteria) predict job performance much better than unstructured chats. Many organisations, including public-service commissions, use panels and structured elements. So preparation for **likely questions** pays off.

**Kerala PSC interviews.** For posts with an interview, the Kerala PSC holds interviews after the written test; the interview marks add to the written marks for the rank list. Panels typically ask about your background, your education, the post and its duties, Kerala and current affairs, and sometimes your hometown or hobbies. Interview marks, procedures and which posts have interviews vary by post and notification: always read the official notification and instructions ({CHECK}). The {xref('lrn', 'lrn-m12', 'Learning Capabilities exam-mastery module')} covers the written exam.

**The STAR method** for "Tell me about a time…" questions: **Situation** (brief context), **Task** (what you had to do), **Action** (what *you* did, specifically), **Result** (what happened, ideally with a number, and what you learned). It keeps answers focused and evidence-based; it is widely taught and consistent with structured-interview research.

**Impression management in interviews.** Research finds that moderate **self-promotion** combined with **genuine interest** and **warmth** helps, but exaggeration and arrogance hurt; **honesty** about what you don't know ("I'm not sure, but I would find out by…") is judged better than bluffing. Panels in public service often value **humility, integrity and service attitude** (Module 34).

**Interview and exam nerves.** Test anxiety is common and can lower performance by taking up working memory with worry. Tools with evidence:
- **Expressive writing** about worries for 10 minutes before an exam improved scores for anxious students (Ramirez and Beilock, 2011) ({link('rb-writing', 'summary')}).
- **Reappraisal** of arousal as excitement ("I'm excited", Brooks, 2014; mixed replications) (PD-M27-L02).
- **Slow breathing** before and during (PD-M11-L01).
- **Practice under realistic conditions:** mock interviews and timed mocks are exposure (Module 13).
- **Sleep:** a normal night's sleep before the exam beats late-night cramming (Module 19).
- **Self-compassion** after a bad section: one breath, "this is hard; others feel it too", then move to the next question (PD-M09-L02).
""",
    evidence=[
        ('Structured interviews predict performance better than unstructured', 'strong', 'Large meta-analyses of hiring research.'),
        ('STAR answers', 'tool', 'Widely taught; consistent with structured-interview research.'),
        ('Honesty about not knowing is judged better than bluffing', 'moderate', 'Supported by impression-management research.'),
        ('Expressive writing reduces the effect of test anxiety', 'moderate', 'Classroom and lab studies; later replications varied.'),
        ('Mock practice reduces interview anxiety', 'moderate', 'Supported by exposure and interview-training studies.'),
    ],
    example="""
Sreeja has a PSC interview for an office post. With Joseph sir's help, she prepares:

**Likely questions:** "Introduce yourself." "Why do you want this post?" "What are the duties of this post?" "Tell us about your village/panchayat." "A current issue in Kerala and your view." "What will you do if a member of the public is rude at the counter?"

**A STAR answer** for the last one: "**Situation:** when I volunteered at our panchayat help desk during the flood relief registration, a man shouted because his name wasn't on the list. **Task:** I had to calm him and solve the problem. **Action:** I listened, repeated his concern, apologised for the wait, checked the list and found his name was spelled differently. **Result:** he got registered in ten minutes and later thanked me. I learned that listening first calms most people."

**Mock interview:** Joseph sir and two friends form a panel; she records it on her phone. Watching it, she notices she says "actually" often and looks at the floor when unsure. In the second mock, she pauses instead and makes eye contact with each panel member. On the morning of the interview she writes her worries for 10 minutes, takes five slow breaths outside the hall and tells herself, "I'm excited; I'm prepared."
""",
    apply=f"""
**Interview preparation plan:**
1. **Read the notification and the post's duties** ({CHECK}).
2. **List 15 likely questions** (background, motivation, post duties, Kerala and current affairs, your district, situational questions).
3. **Prepare key points** (not scripts) for each, and **STAR stories** for three or four "Tell me about a time" questions (use your story bank, PD-M26-L01).
4. **Mock interview:** a panel of two or three people, 15 minutes, recorded; review and repeat.
5. **Practical prep:** documents, outfit (Module 23), route and timing, sleep.

{fence('''STAR ANSWER CARD
S - Situation (1-2 lines): ______________________
T - Task (what I had to do): ______________________
A - Action (what I did; "I", not "we"): ______________________
R - Result (what happened; a number if possible; what I learned): ______
MOCK INTERVIEW REVIEW
Questions asked: ______  Answers clear? ___/5  Examples used? Y/N
Fillers per minute: ___  Eye contact with each panelist? Y/N
Honest "I don't know, but..." when needed? Y/N  One fix: ______
EXAM / INTERVIEW DAY NERVES
Night before: normal sleep. Morning: 10 min worry writing, 5 slow breaths,
"I'm excited; I'm prepared." During: pause, breathe, next question.''')}

**With others:** run mock interviews for each other in your study group; use the same questions and scoring sheet for everyone (structured, fair, PD-M24-L01).
""",
    resources=[
        ('rb-writing', 'Read the summary of the expressive-writing study and plan when you will use it', '5 minutes'),
        ('os-12', 'Re-read 12.2 Self-presentation with interviews in mind', '10 minutes'),
        ('telemanas', 'Remember: if exam anxiety is severe or persistent, talk to a professional', '2 minutes'),
    ],
    steps=[
        'List 15 likely interview questions for a post or job you want, with key points for each.',
        'Write four STAR stories.',
        'Run a recorded 15-minute mock interview with two or three people as the panel; review it with the mock interview review.',
        'Run a second mock with one fix, and write your exam and interview day nerves plan.',
    ],
    proof='Your 15 questions with key points, four STAR stories, two mock interview reviews (with recording file names) and your nerves plan.',
    templates=[('Interview question bank', """INTERVIEW QUESTION BANK                Post/job: ______
Background:   1. Introduce yourself  2. ______
Motivation:   3. Why this post?  4. ______
Post duties:  5. What are the duties of ______?  6. ______
Kerala/district/current affairs: 7. ______ 8. ______ 9. ______
Situational:  10. Rude member of the public  11. A mistake you made  12. ______
"Tell me about a time" (STAR): 13. ______ 14. ______ 15. ______
Key points for each (not scripts): ______""", '')],
    mistakes=[
        ('Memorising word-for-word answers.', 'You\'ll sound rehearsed and freeze if interrupted. Prepare key points and stories.'),
        ('Bluffing.', '"I\'m not sure, but I would find out by…" is better than a wrong confident answer.'),
        ('Skipping mock interviews.', 'Recorded mocks are the fastest way to improve.'),
        ('Cramming the night before.', 'Sleep protects recall and calm.'),
    ],
    quiz=[
        Q('Which interview type best predicts job performance in research?', 'Structured interviews with the same job-related questions and clear criteria', 'Unstructured chats', 'Handwriting analysis', 'Personality type tests', why='Meta-analyses of hiring research.'),
        Q('What does STAR stand for?', 'Situation, Task, Action, Result', 'Smile, Talk, Answer, Relax', 'Start, Think, Act, Review', 'Story, Theme, Answer, Reason', why='A structure for behavioural questions.'),
        Q('What helped anxious students in Ramirez and Beilock\'s study?', 'Writing about their worries for 10 minutes before the exam', 'Studying all night', 'Skipping breakfast', 'Avoiding thinking about the exam', why='Expressive writing freed up working memory.'),
        Q('A panel asks something you don\'t know. What is best?', '"I\'m not sure, but I would find out by…"', 'Make up an answer confidently', 'Stay silent', 'Change the subject', why='Honesty is judged better than bluffing.'),
    ],
    study='read the lesson and check your target post\'s notification',
    action='prepare 15 questions and four STAR stories, run two recorded mock interviews and write your nerves plan',
)

LESSONS = [L1, L2]

MODULE = module(
    33,
    overview=f"""
Psychology at work: how customers really decide, honest question-led selling, price and marketing effects with honest evidence (anchors strong, decoys weak), and preparation for job and Kerala PSC interviews with STAR stories, mock interviews and tested tools for interview and exam nerves.

Part D ends where people skills meet earning a living. Whether you sell a service, work in a shop, or face a PSC interview panel, the same psychology applies: understand the other person's needs, communicate clearly, build trust and stay calm.

For business sales, see {xref('ent', 'ent-m07', 'the Entrepreneurship sales module')}; for PSC written exams, see {xref('lrn', 'lrn-m12', 'the Learning Capabilities exam module')}.
""",
    outcomes=[
        'Explain how customers decide and sell honestly with question-led conversations.',
        'Spot common price and marketing techniques and judge their honesty and evidence.',
        'Prepare structured interview answers with STAR stories.',
        'Run and review recorded mock interviews.',
        'Manage interview and exam nerves with tested tools.',
    ],
    lessons=LESSONS,
    project='a recorded mock PSC or job interview',
    project_steps=[
        'Prepare 15 questions with key points and four STAR stories (PD-M33-L02).',
        'Run two recorded mock interviews with a panel and review them.',
        'Write your interview-day plan (documents, outfit, route, sleep, nerves routine).',
        'Add your STAR stories and nerves routine to your Playbook.',
    ],
    project_proof='Question bank, STAR stories, two mock reviews with recordings and your interview-day plan.',
    rubric=[
        ('Preparation', 'No question list', 'Some questions prepared', '15 questions with key points and four STAR stories'),
        ('Practice', 'No mock interview', 'One mock', 'Two recorded mocks with a fix between them'),
        ('Delivery', 'Memorised, rushed or bluffing', 'Mostly clear', 'Clear, calm, honest, with examples'),
        ('Selling skills', 'Features only', 'Some questions', 'SPIN conversation and an honest offer with a risk reducer'),
    ],
    short=[
        'Write three STAR stories.',
        'Do one 10-minute recorded mock interview with a friend.',
    ],
    flashcards=[
        ('SPIN', 'Situation, Problem, Implication, Need-payoff questions.'),
        ('Strongest price effect', 'Anchoring.'),
        ('Decoy effect status', 'Weaker and less reliable than early studies suggested.'),
        ('Best interview type for prediction', 'Structured interviews.'),
        ('STAR', 'Situation, Task, Action, Result.'),
        ('Not sure of an answer?', '"I\'m not sure, but I would find out by…"'),
        ('Exam-morning anxiety tool', '10 minutes of writing about worries.'),
    ],
    mistakes=[
        ('Thinking selling means pushing.', 'Honest selling is understanding needs and solving them.'),
        ('Preparing only facts for interviews.', 'Prepare stories and delivery too.'),
        ('Ignoring severe anxiety.', 'If it is persistent, talk to a professional (Tele-MANAS 14416).'),
    ],
    tools=[
        'The customer conversation card and shop-floor psychology walk (PD-M33-L01).',
        'The interview question bank, STAR card, mock review and nerves plan (PD-M33-L02).',
    ],
    playbook=[
        'Selling: questions first, honest offer, a risk reducer, an easy no.',
        'Interviews: key points not scripts, STAR stories, honest "I\'ll find out", mock interviews recorded.',
        'Exam and interview mornings: worry writing, slow breathing, "I\'m excited; I\'m prepared".',
    ],
)
