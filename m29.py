from common import lesson, module, link, xref, table, fence, Q
import tools

L1 = lesson(
    29, 1,
    outcome='You can separate interests from positions, work out your BATNA and walk-away point, use anchoring honestly, and look for win-win trades.',
    split='20 minutes reading, 30 minutes of tasks',
    principle='Good negotiators focus on what each side really needs (interests) rather than what they demand (positions), know their best alternative if there is no deal (BATNA), and create value before dividing it.',
    science=f"""
**Principled negotiation.** Roger Fisher, William Ury and Bruce Patton of the Harvard Negotiation Project set out four ideas in *Getting to Yes* (first published in 1981):
1. **Separate the people from the problem:** be soft on the person, firm on the problem.
2. **Focus on interests, not positions.** A **position** is what someone says they want ("₹15,000 rent"); an **interest** is why ("a reliable tenant who pays on time and doesn't damage the house"). Their classic example: two sisters fight over one orange and cut it in half; one wanted the juice and the other the peel for a cake. Knowing interests reveals better deals.
3. **Invent options for mutual gain** before deciding.
4. **Insist on objective criteria:** market prices, official rates, precedent.

**BATNA.** Your **Best Alternative To a Negotiated Agreement** is what you will do if this negotiation fails: buy from another shop, take another offer, keep the old phone. The Harvard Program on Negotiation calls your BATNA "the true measure by which you should judge any proposed agreement" ({link('pon-batna', 'PON')}). A strong BATNA gives you power; improving it before negotiating (getting a second quote) is often the best preparation. Your **walk-away point** (reservation price) comes from your BATNA: the worst deal you would accept. The **zone of possible agreement** (ZOPA) is the overlap between your walk-away point and theirs.

**Anchoring.** The first number in a negotiation pulls the final agreement towards it (PD-M01-L02, PD-M03-L01). Meta-analyses of negotiation research find that first offers strongly predict final outcomes. Adam Galinsky and Thomas Mussweiler (2001) found that the party who made the first offer often got a better result, especially when they had good information. If you know the market, an ambitious but justifiable first offer helps; if you don't, let the other side go first and research. When the other side anchors extremely, don't argue from their number: restate your own based on objective criteria. **Honest anchoring** means your first number is ambitious but defensible, not a lie.

**Win-win (integrative) negotiation.** Many negotiations have more than one issue (price, timing, delivery, warranty, extras). Trading across issues that each side values differently ("I'll pay a little more if you include free delivery and a 3-month warranty") creates value for both. Research by Leigh Thompson and others found that negotiators often wrongly assume the other side wants the opposite of everything (the "fixed-pie" bias).

**Culture.** In Kerala, bargaining is normal in markets, auto stands, some textile and electronics shops and for services, but not in supermarkets, pharmacies, hospitals or fixed-price government services. Relationships matter: a respectful, friendly negotiation that leaves the shopkeeper happy brings better deals next time.
""",
    evidence=[
        ('Focusing on interests produces better agreements', 'moderate', 'Supported by negotiation experiments and practice.'),
        ('A strong BATNA increases negotiating power', 'strong', 'Consistent in negotiation research.'),
        ('First offers anchor final outcomes', 'strong', 'Meta-analyses and many experiments.'),
        ('Making the first offer is better when you have good information', 'moderate', 'Several studies; depends on information.'),
        ('Fixed-pie bias leads to worse deals', 'moderate', 'Supported by experiments.'),
    ],
    example="""
Anu needs a second-hand laptop for online mock tests. A shop in Kozhikode offers a 5-year-old laptop for ₹14,000.

**Interests:** hers: a reliable laptop for 2–3 years of study, under ₹12,000, with the battery working. The shop's (probably): selling old stock quickly, a happy customer who returns. **BATNA:** she finds a similar model online for ₹12,500 with a 1-month warranty, and another shop quoting ₹13,000 (two **objective criteria**). **Walk-away:** ₹12,500 (her online BATNA). **Target:** ₹11,000.

She **anchors** honestly: "I like this one. I've seen the same model for ₹12,500 online with a warranty. Could you do ₹10,500?" The shopkeeper laughs and says ₹13,000. She stays friendly and adds **another issue**: "If you can include a new battery check and a 3-month shop warranty, I can do ₹11,500." They settle at ₹11,800 with a 3-month warranty and a free laptop bag. Both are happy; the shopkeeper gives her his number for repairs.
""",
    apply=f"""
**Prepare any negotiation in 5 minutes:**
{fence(tools.NEGOTIATION_PREP)}

**Interest questions to ask the other side:** "What's most important to you in this?" "What would make this work for you?" "Is there flexibility on timing, delivery or extras?"

**Rules:**
- Be friendly; separate the person from the problem.
- Never lie about other offers or your budget. You may decline to share your walk-away point.
- After you name a number, **pause** and let them respond.
- Trade across issues instead of only splitting the price.
- Be ready to walk away politely: "Thanks; I'll think about it." (Often the best offer comes then.)

**With others:** in family decisions (dividing chores, planning a wedding budget), the same tools work: ask about interests, invent options, use objective criteria ("What did similar weddings in our family cost?").
""",
    resources=[
        ('pon-batna', 'Read the article: what BATNA is and how to improve yours', '15 minutes'),
        ('decisionlab', 'Re-read the anchoring entry, focusing on negotiation', '5 minutes'),
        ('os-12', 'Re-read the persuasion part of 12.3', '10 minutes'),
    ],
    steps=[
        'Think of a past negotiation (a purchase, a salary, a family decision). Write the positions and the interests of each side, and what a better deal could have looked like.',
        'For an upcoming purchase or service, fill in the negotiation prep sheet, including two objective criteria (other prices or quotes) and your BATNA.',
        'Write three interest questions you will ask.',
        'Write two things that cost you little but could help the other side, and two that cost them little but help you.',
    ],
    proof='Your past-negotiation analysis and a completed prep sheet for an upcoming negotiation with BATNA, criteria, questions and trades.',
    templates=[('Negotiation prep', tools.NEGOTIATION_PREP, '')],
    mistakes=[
        ('Negotiating without a BATNA.', 'Get at least one other price or option first.'),
        ('Lying about other offers.', 'It is dishonest and often discovered. Use real criteria.'),
        ('Splitting the difference too early.', 'Look for trades across issues first.'),
        ('Treating the other side as an enemy.', 'Friendly and firm gets better long-term results.'),
    ],
    quiz=[
        Q('What is a BATNA?', 'Your best alternative if this negotiation fails', 'Your first offer', 'The other side\'s price', 'A type of discount', why='Fisher, Ury and Patton\'s concept.'),
        Q('In the orange story, what was the lesson?', 'Knowing interests (juice versus peel) reveals better deals than splitting positions', 'Always cut things in half', 'Sisters should not share', 'Oranges are scarce', why='Interests, not positions.'),
        Q('When does making the first offer tend to help?', 'When you have good information about the market', 'Always, even without information', 'Never', 'Only when you are the seller', why='An informed ambitious anchor pulls the outcome your way.'),
        Q('What is the "fixed-pie" bias?', 'Wrongly assuming the other side wants the opposite of everything', 'Always choosing pie', 'Splitting things equally', 'A fixed price shop', why='It blinds negotiators to win-win trades.'),
    ],
    study='read the lesson and the PON BATNA article',
    action='analyse a past negotiation and prepare an upcoming one with the prep sheet',
)

L2 = lesson(
    29, 2,
    outcome='You can negotiate a real small purchase or service in Kerala respectfully, record the result, and learn from it.',
    split='15 minutes reading, 30 to 60 minutes for the real negotiation',
    principle='Negotiation is a skill learned by doing: prepare, be friendly, anchor honestly, ask about interests, trade, be ready to walk away, and review what happened.',
    science="""
**Why practise on small deals?** Negotiation research shows that preparation and experience improve outcomes, and that anxiety lowers them: anxious negotiators make lower first offers, exit early and accept worse deals (studies by Alison Wood Brooks and Maurice Schweitzer, 2011). Small, low-stakes negotiations are exposure practice (Module 13) that make bigger ones (salary, rent, business deals) less frightening.

**Gender and negotiation.** Research finds that women are often penalised socially for negotiating assertively for themselves, and are less likely to initiate negotiations (Linda Babcock and Sara Laschever). Framing requests around shared interests or others' interests ("This would help the team / my family") and using objective criteria reduce the backlash. This is a real constraint, not a personal failing.

**Emotions.** Showing anger can sometimes win concessions in one-off deals but damages relationships and backfires when the other side has alternatives. Warmth, curiosity and calm firmness work best for repeated relationships (your local shops, your landlord, your employer).

**Silence and patience.** After making an offer, pausing feels uncomfortable but often leads the other side to improve their offer. Rushing to fill the silence often means conceding against yourself.

**Salary and rate negotiation.** The same principles apply: research the market (objective criteria), know your BATNA (other offers or your current situation), ask about interests ("What does success in this role look like?"), and negotiate the package (salary, hours, training, leave), not just one number. For government jobs, pay is fixed by rules, but many private jobs, freelance work and tuition rates are negotiable.

**Reviewing.** After each negotiation, compare your result with your target and walk-away point, note what worked, and write one lesson. Over several small deals, you'll see your own patterns (do you concede too fast? forget to ask questions?).
""",
    evidence=[
        ('Preparation improves negotiation outcomes', 'strong', 'Consistent in research and training studies.'),
        ('Anxiety leads to worse negotiation outcomes', 'moderate', 'Experiments by Brooks and Schweitzer.'),
        ('Women face backlash for self-advocating negotiation', 'moderate', 'Several studies; framing around shared interests reduces it.'),
        ('Anger wins concessions', 'mixed', 'Sometimes in one-off deals; harms relationships and backfires when the other side has alternatives.'),
        ('Practising small negotiations', 'tool', 'Exposure and skill practice, consistent with research.'),
    ],
    example=f"""
Ashiq needs his scooter serviced. His usual mechanic quotes ₹1,800. **Prep:** a second mechanic quoted ₹1,500 for the same work; the authorised service centre ₹2,200 (**objective criteria**). His **BATNA**: the ₹1,500 mechanic, though farther away. **Target:** ₹1,500 with a free wash. **Walk-away:** ₹1,700.

**Negotiation:** "Chetta, you've always done good work on my scooter. Another place quoted ₹1,500 for the same service. Could you do ₹1,450? I'll keep coming to you." The mechanic says ₹1,700. Ashiq pauses and says nothing for a few seconds. The mechanic adds, "₹1,600, and I'll check the brakes free." Ashiq asks, "Could you include a wash?" Deal: ₹1,600 with brake check and wash.

**Review:** target ₹1,500, result ₹1,600 plus extras, relationship good. Lesson: the pause worked; next time ask what's included before naming a price.
""",
    apply=f"""
**Your real negotiation (this week):**
1. **Choose** a real purchase or service where bargaining is normal: a market purchase, a second-hand item, a tailor, a mechanic, an auto fare agreed before the ride, tuition rates, a small freelance job. Avoid places where it is inappropriate (pharmacies, hospitals, supermarkets, fixed-price government services).
2. **Prepare** with the prep sheet: two objective criteria, BATNA, walk-away, target, first ask, trades.
3. **Negotiate** respectfully: warm greeting, interest question, honest anchor, pause, trade across issues, polite walk-away if needed.
4. **Record** the result and review it.

{fence('''NEGOTIATION REVIEW
What: ______  With: ______  Where: ______
First quote Rs ___  My first ask Rs ___  Target Rs ___  Walk-away Rs ___
Final: Rs ___ + extras ______  Relationship after: better / same / worse
Did I: [ ] ask about their interests  [ ] use objective criteria  [ ] pause
       [ ] trade across issues  [ ] stay friendly  [ ] avoid lying
What worked: ______  One lesson for next time: ______''')}

**With others:** never squeeze a poor street vendor over ₹5 when the deal is already fair; negotiation is about fair value, not winning. Win-win includes their living.
""",
    resources=[
        ('pon-batna', 'Re-read the section on improving your BATNA before you negotiate', '5 minutes'),
        ('ted-jiang', 'Optional: Jia Jiang\'s requests are also small negotiations; notice how he asks "why?" after a no', '5 minutes'),
        ('franklin', 'Read the passage on Franklin\'s habit of modest, non-dogmatic language in discussions (search for "the habit of expressing myself in terms of modest diffidence")', '10 minutes'),
    ],
    steps=[
        'Choose a real negotiation for this week and fill in the prep sheet.',
        'Negotiate respectfully and record the result.',
        'Fill in the negotiation review.',
        'If possible, do a second small negotiation and compare your two reviews.',
    ],
    proof='Your prep sheet, the negotiation review with first quote, target, walk-away and final result, and (optionally) a second review.',
    templates=[('Negotiation review', """NEGOTIATION REVIEW
What: ______  With: ______  Where: ______
First quote Rs ___  My first ask Rs ___  Target Rs ___  Walk-away Rs ___
Final: Rs ___ + extras ______  Relationship after: better / same / worse
Checklist: interests asked / criteria used / paused / traded / friendly / no lies
What worked: ______  Lesson: ______""", '')],
    mistakes=[
        ('Bargaining where it is inappropriate.', 'Pharmacies, hospitals and supermarkets have fixed prices; respect them.'),
        ('Conceding to fill silence.', 'After your offer, pause.'),
        ('Squeezing people with little power.', 'Seek fair value, not a "win" over a poor vendor.'),
        ('Forgetting extras.', 'Warranty, delivery, a check-up or a wash can matter as much as price.'),
    ],
    quiz=[
        Q('What did Brooks and Schweitzer find about anxious negotiators?', 'They made lower first offers, exited early and got worse deals', 'They got better deals', 'Anxiety has no effect', 'They always walked away', why='Anxiety lowers negotiation outcomes; practice helps.'),
        Q('What is often the best thing to do right after you name your price?', 'Pause and let the other side respond', 'Lower it immediately', 'Explain at length', 'Leave', why='Silence often brings a better offer.'),
        Q('Where is bargaining usually inappropriate in Kerala?', 'Pharmacies and hospitals', 'Second-hand markets', 'Auto fares agreed before the ride', 'A tailor\'s quote', why='Respect fixed-price settings.'),
        Q('What does a good negotiation review include?', 'First quote, target, walk-away, final result, what worked and one lesson', 'Only the final price', 'Only how you felt', 'Nothing', why='Reviews turn deals into learning.'),
    ],
    study='read the lesson and the Franklin passage on modest language',
    action='negotiate a real small purchase or service with the prep sheet and write the review',
)

LESSONS = [L1, L2]

MODULE = module(
    29,
    overview=f"""
Negotiation for everyday life: interests versus positions, BATNA and walk-away points, honest anchoring, win-win trades across issues, Kerala bargaining etiquette, and a real small negotiation with a prep sheet and review.

Everyone negotiates: prices, rent, salaries, chores, deadlines. Most people either avoid it (and overpay) or treat it as a fight (and damage relationships). Principled negotiation gives you a calm, fair method that gets better results and keeps relationships good.

You practise on a small, real deal first. The same method scales to salary, rent and business deals; the {xref('fin', 'fin-m16', 'Personal Finance "Growing income" module')} covers income negotiations in more detail.
""",
    outcomes=[
        'Separate interests from positions and ask interest questions.',
        'Work out your BATNA, walk-away point and target using objective criteria.',
        'Use honest anchoring and pauses.',
        'Create win-win trades across issues.',
        'Negotiate a real small purchase or service and review it.',
    ],
    lessons=LESSONS,
    project='a real small negotiation, prepared and reviewed',
    project_steps=[
        'Prepare with the prep sheet (PD-M29-L01).',
        'Negotiate a real purchase or service respectfully (PD-M29-L02).',
        'Write the review and compare your result with your target and walk-away point.',
        'Add your negotiation rules to the Playbook.',
    ],
    project_proof='The prep sheet, the negotiation review and your Playbook rules.',
    rubric=[
        ('Preparation', 'No preparation', 'Price only', 'BATNA, criteria, walk-away, target and trades prepared'),
        ('Process', 'Argued or conceded quickly', 'Some good steps', 'Interest questions, honest anchor, pause, trades'),
        ('Ethics', 'Lied or bullied', 'Mostly fair', 'Fully honest, respectful, fair to both sides'),
        ('Learning', 'No review', 'Result noted', 'Full review with a lesson'),
    ],
    short=[
        'Get one extra quote before your next purchase over ₹1,000 (your BATNA).',
        'Pause after naming a price once this week.',
    ],
    flashcards=[
        ('Position versus interest', 'What they demand versus why they want it.'),
        ('BATNA', 'Best Alternative To a Negotiated Agreement: your plan if no deal.'),
        ('Walk-away point', 'The worst deal you\'ll accept, based on your BATNA.'),
        ('ZOPA', 'The overlap between both sides\' walk-away points.'),
        ('Honest anchor', 'An ambitious but defensible first number.'),
        ('Fixed-pie bias', 'Assuming they want the opposite of everything; blocks win-win trades.'),
        ('After your offer…', 'Pause.'),
        ('Four principles (Getting to Yes)', 'People vs problem, interests, options, objective criteria.'),
    ],
    mistakes=[
        ('Negotiating only on price.', 'Add timing, warranty, delivery, extras.'),
        ('Ruining relationships for small wins.', 'Your local shopkeeper is a long-term relationship.'),
        ('Avoiding negotiation out of fear.', 'Small practice deals build courage.'),
    ],
    tools=[
        'The negotiation prep sheet (PD-M29-L01).',
        'The negotiation review (PD-M29-L02).',
    ],
    playbook=[
        'Before any deal: BATNA, two objective prices, walk-away, target, first ask, trades.',
        'In the deal: friendly, ask about interests, honest anchor, pause, trade, walk away politely if needed.',
    ],
)
