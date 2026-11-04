from common import lesson, module, link, xref, table, fence, Q

L1 = lesson(
    23, 1,
    outcome='You can run a daily hygiene and grooming routine, build a small budget wardrobe that works for interviews, functions and daily life, and explain honestly how appearance affects first impressions.',
    split='20 minutes reading, 40 minutes of tasks',
    principle='Clean, neat and appropriate beats expensive: people form quick first impressions from grooming and clothes, so a simple routine and a few well-chosen, well-kept clothes help you, at low cost.',
    science=f"""
**Why appearance matters (and how much).** People form first impressions very fast, within a fraction of a second for faces in some studies (Janine Willis and Alexander Todorov, 2006), and use cues such as cleanliness, grooming and clothing to judge warmth, competence and trustworthiness (Module 24). These snap judgements are often inaccurate, and they are shaped by stereotypes, but they affect real decisions in interviews, shops and offices. A clean, neat appearance mainly **removes a negative signal**; it rarely needs to be expensive to do that. Some research on "enclothed cognition" (Hajo Adam and Adam Galinsky, 2012) claimed that wearing a lab coat improved attention; replications have been mixed, so don't expect clothes to change your brain. The more reliable effect is on **other people's impressions** and on your own comfort and confidence.

**Hygiene basics with good evidence:**
- **Handwashing with soap** for about 20 seconds, especially before eating and after the toilet, reduces diarrhoeal and respiratory infections substantially in many studies.
- **Teeth:** brush twice a day with fluoride toothpaste for about two minutes; clean between teeth; avoid tobacco; see a dentist yearly. Bad breath often comes from the tongue, gums or dry mouth; brushing the tongue and drinking water help.
- **Body odour:** daily bath (Kerala's humidity means sweat builds fast), clean underwear and socks daily, dry thoroughly (especially between toes and in skin folds, to prevent fungal infections common in humid weather), wash clothes regularly, and use deodorant or talc if you like.
- **Skin:** a gentle soap or cleanser, sunscreen for long outdoor time if you can afford it, and seeing a doctor for persistent rashes or acne rather than trying many products.
- **Nails and hair:** short, clean nails; a regular haircut; beard trimmed or shaved neatly.

**Dressing well on a budget.** Fashion advice is mostly opinion, not research, so the guidance here is practical:
- **Fit and condition** matter more than brand or price. A ₹500 shirt that fits well, is clean and ironed looks better than an expensive one that is creased or too big.
- **A small capsule wardrobe:** a few pieces in neutral colours (white, light blue, grey, navy, beige, black) that all go together.
- **Kerala dress codes:** formal interviews (including PSC interviews) usually expect conservative formal clothes: for men, a plain light shirt and dark trousers, or a mundu and shirt for some settings; for women, a saree or churidar in plain or subtle colours. Weddings and functions have their own norms; offices vary. When unsure, dress slightly more formally than you expect others to.
- **Care:** wash, dry in shade to keep colours, iron, polish shoes, mend small tears. Shops in Kozhikode and local tailors can alter second-hand or cheaper clothes to fit for a small cost.
""",
    evidence=[
        ('People form fast first impressions from appearance', 'strong', 'Many studies; impressions are fast but often inaccurate.'),
        ('Handwashing with soap reduces infections', 'strong', 'Many trials and reviews.'),
        ('Twice-daily brushing with fluoride toothpaste prevents tooth decay', 'strong', 'Well established in dental research.'),
        ('Clothes change your thinking ("enclothed cognition")', 'mixed', 'The original lab-coat finding did not consistently replicate.'),
        ('Fit and condition matter more than price', 'tool', 'Practical advice; little formal research.'),
    ],
    example="""
Ashiq has a PSC interview in six weeks and a cousin's wedding in two. His wardrobe: many T-shirts, two worn jeans, one oversized formal shirt from college, one mundu.

His plan, with a ₹2,000 budget: two plain shirts (white and light blue) from a local shop, one pair of dark grey trousers, altered by the tailor near the bus stand for ₹100 to fit properly; he polishes his old black shoes and buys a ₹150 plain black belt. With his mundu, the white shirt works for the wedding. He gets a haircut a week before each event, not the day before, so it looks natural.

His daily routine improves too: bath twice a day in the hot months, clean socks every day, dry feet properly (his itchy toes clear up in two weeks), tongue-brushing for breath, and a small comb and handkerchief in his bag. His mother says he looks "like a government officer already". He laughs and reminds himself that the interview is judged on his answers; his clothes just make sure nothing distracts from them.
""",
    apply=f"""
**Daily hygiene and grooming routine:**
{fence('''DAILY ROUTINE
Morning: brush teeth (2 min, fluoride) + tongue; bath (twice a day in hot
         months); dry well, especially feet and skin folds; deodorant/talc
         if you use it; clean clothes, underwear and socks; hair combed
During the day: wash hands with soap before eating and after the toilet;
         water bottle; handkerchief or tissue; comb in bag
Night:   brush teeth (2 min); wash face; clothes for tomorrow ready
Weekly:  trim nails; wash or change bedsheets and towels; polish shoes
Monthly: haircut (or as needed); check clothes for repairs
Yearly:  dental check''')}

**Budget capsule wardrobe (adjust to your style and culture):**
{fence('''CAPSULE WARDROBE CHECKLIST           Budget Rs ______
Formal (interviews, offices):
[ ] 2 plain shirts or tops (white / light blue / pastel)
[ ] 1 dark trousers or a plain formal saree / churidar set
[ ] 1 pair of clean, polished shoes or sandals; 1 plain belt (if needed)
Functions: [ ] 1 mundu or traditional outfit in good condition
Everyday: [ ] 3-4 clean, well-fitting T-shirts or tops; 2 trousers/jeans
Care kit: [ ] iron access  [ ] shoe polish  [ ] needle and thread
Fit check: shoulders, sleeve length, waist, trouser length (tailor: Rs ___)''')}

**With others:** never comment on other people's bodies, skin colour or clothes in a way that shames them. Colourism (preferring fair skin) is common and harmful; it is a stereotype, not a standard. If a friend asks for help with an interview outfit, focus on fit, cleanliness and the dress code.
""",
    resources=[
        ('os-12', 'Read 12.2 Self-presentation (how people manage impressions)', '15 minutes'),
        ('noba', 'Search for the module "Social Cognition and Attitudes" and read the part on first impressions', '15 minutes'),
        ('smiles', 'Read the last chapter, "Character—the True Gentleman", for a 19th-century view of manners and character; notice what still applies', '20 minutes'),
    ],
    steps=[
        'Write and follow the daily routine for seven days, ticking it in Loop or on paper.',
        'Do a wardrobe audit: list what fits, what needs repair or alteration, and what is missing for interviews and functions.',
        'Fix or buy one or two items within a small budget (alteration, polish, one shirt or top).',
        'Prepare and photograph one complete interview outfit and one function outfit.',
    ],
    proof='Seven days of the routine ticked, your wardrobe audit, what you fixed or bought (with cost), and photos of two complete outfits.',
    templates=[('Wardrobe audit', """WARDROBE AUDIT                    Date ______
Item | Fits? (Y/N) | Condition (good / repair / replace) | Use (formal / function / daily)
______ | __ | ______ | ______
Missing for interviews: ______   Missing for functions: ______
Fix or buy (max 2 items): 1 ______ Rs ___  2 ______ Rs ___
Interview outfit ready: [ ] clean [ ] ironed [ ] fits [ ] shoes polished""", '')],
    mistakes=[
        ('Spending on brands instead of fit and care.', 'Alteration, ironing and polish matter more than labels.'),
        ('A big change right before an event.', 'Haircuts and new shoes a week before, so they look natural and are comfortable.'),
        ('Overdoing perfume or products.', 'Clean and subtle is better; strong smells can put people off.'),
        ('Judging or shaming others\' looks.', 'Appearance cues are often misleading and shaped by stereotypes.'),
    ],
    quiz=[
        Q('What matters most for looking well dressed on a budget?', 'Fit, cleanliness and condition', 'Brand names', 'Bright colours', 'Expensive watches', why='Well-fitting, clean, ironed clothes look better than expensive creased ones.'),
        Q('Which hygiene habit has strong evidence for preventing infections?', 'Handwashing with soap for about 20 seconds', 'Wearing perfume', 'Drinking cold water', 'Changing hairstyle', why='Handwashing reduces diarrhoeal and respiratory infections.'),
        Q('What is the honest status of "enclothed cognition"?', 'The original lab-coat finding has had mixed replications', 'Proven by many studies', 'Never studied', 'Proven harmful', why='Treat it as uncertain.'),
        Q('For a PSC interview, what is a safe dress choice?', 'Conservative, clean, well-fitting formal clothes', 'Party wear', 'Gym clothes', 'Whatever is most fashionable', why='Formal and plain keeps attention on your answers.'),
    ],
    study='read the lesson and OpenStax 12.2',
    action='follow the daily routine for seven days, audit your wardrobe and prepare two complete outfits',
)

LESSONS = [L1]

MODULE = module(
    23,
    overview=f"""
Grooming, hygiene and dressing well on a budget: a daily routine with evidence behind it (handwashing, teeth, skin and feet in humid weather), honest notes on how appearance affects first impressions, and a small capsule wardrobe ready for interviews, functions and daily life.

Part C ends with the outside of the body. Appearance does not decide your worth, but it shapes quick first impressions (Module 24), and a clean, neat, appropriate look removes a distraction, especially in interviews. None of this needs much money.

Be kind about appearance, your own and other people's. Avoid colourism and body-shaming; these are stereotypes, not standards.
""",
    outcomes=[
        'Follow a daily and weekly hygiene and grooming routine.',
        'Explain how appearance affects first impressions, and the limits of that.',
        'Build a budget capsule wardrobe with interview and function outfits.',
        'Care for clothes so they last and look good.',
    ],
    lessons=LESSONS,
    project='a grooming routine and a budget wardrobe',
    project_steps=[
        'Follow the daily routine for two weeks.',
        'Complete the wardrobe audit and fix or buy at most two items.',
        'Prepare interview and function outfits and photograph them.',
        'Add your routine to your morning routine in the Playbook.',
    ],
    project_proof='Two weeks of routine ticks, the audit, costs and outfit photos.',
    rubric=[
        ('Routine', 'Irregular', 'Most days', 'Every day for two weeks'),
        ('Wardrobe', 'No audit', 'Audit only', 'Audit plus fixes within budget'),
        ('Readiness', 'No outfits ready', 'One outfit', 'Interview and function outfits ready'),
        ('Attitude', 'Judges others by looks', 'Neutral', 'Focuses on fit, care and respect for others'),
    ],
    short=[
        'Handwashing, twice-daily brushing and clean socks every day.',
        'One interview outfit, clean, ironed and ready.',
    ],
    flashcards=[
        ('Handwashing', 'Soap, about 20 seconds; before eating and after the toilet.'),
        ('Teeth', 'Brush twice a day with fluoride toothpaste for about two minutes; yearly dental check.'),
        ('Humid-weather foot care', 'Dry well between toes; clean socks daily.'),
        ('Budget dressing rule', 'Fit, cleanliness and condition beat brands.'),
        ('Interview dress', 'Conservative, plain, clean, well-fitting formal clothes.'),
        ('"Enclothed cognition" status', 'Mixed replications.'),
    ],
    mistakes=[
        ('Thinking grooming is vanity.', 'It is basic respect for yourself and others, and it removes a distraction.'),
        ('Buying many cheap clothes that don\'t fit.', 'Fewer, better-fitting pieces.'),
        ('Leaving outfit preparation to the last day.', 'Prepare a week ahead.'),
    ],
    tools=[
        'The daily grooming routine, capsule wardrobe checklist and wardrobe audit (PD-M23-L01).',
    ],
    playbook=[
        'Daily: bath, teeth twice, clean clothes, handwashing. Weekly: nails, sheets, shoes.',
        'My interview outfit is always clean, ironed and ready.',
    ],
)
