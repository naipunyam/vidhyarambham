from common import lesson, module, link, xref, table, fence, Q

L1 = lesson(
    20, 1,
    outcome='You can describe the main points of the ICMR-NIN Dietary Guidelines for Indians (2024), build a balanced plate from everyday Kerala food, and spot where a typical Kerala diet goes wrong.',
    split='20 minutes reading, 30 minutes of tasks',
    principle='Eat mostly whole foods with plenty of vegetables, fruit, pulses and some protein at every meal, with less refined rice, sugar, salt, fried food and ultra-processed snacks; no crash diets.',
    science=f"""
**The official Indian guidelines.** In May 2024, the ICMR-National Institute of Nutrition (Hyderabad) released updated **Dietary Guidelines for Indians**, the first full revision in 13 years, with **17 guidelines**. Key points reported at release ({link('icmr-sf', 'South First report')}; {link('icmr-air', 'All India Radio report')}):
- An estimated **56.4% of India's total disease burden** is linked to unhealthy diets.
- **Cereals and millets** should provide **no more than about 45%** of daily energy (many Indian diets get far more, mostly from white rice and wheat).
- **Pulses, beans and meat** together can provide **up to about 15%** of energy.
- **Sugar** should be **under 5%** of total energy; **total fat** at most about **30%**.
- **Restrict salt**, minimise high-fat, sugary and **ultra-processed foods**, and prevent abdominal obesity.
- **Avoid protein supplements** for building muscle mass.
- Be physically active.

The full guidelines are free as a PDF from NIN ({link('nin-dgi', 'ICMR-NIN PDF')}; the address came from a search and could not be opened for checking here, so confirm it on the NIN website). The WHO recommends **less than 5 g of salt a day** (just under a teaspoon) for adults ({link('who-salt', 'WHO')}).

**What a "balanced plate" means in practice.** Many public-health plate models use the same simple pattern, which fits the ICMR figures: **about half the plate vegetables and fruit, a quarter whole grains or millets, a quarter protein foods (pulses, eggs, fish, meat, milk products)**, plus a little healthy fat and water to drink. Use it as a rule of thumb, not a strict formula.

**The typical Kerala diet: strengths and risks.** Strengths: fish (a good protein and omega-3 source), vegetables in thoran, avial and sambar, pulses (cherupayar, kadala, parippu), bananas and seasonal fruit, fermented foods (idli, dosa, appam). Risks: very large portions of white (or matta) rice at two or three meals, frequent fried snacks (pazhampori, vada, banana chips), sweet tea several times a day, bakery items, and growing use of packaged foods. Kerala has among the highest rates of diabetes and high blood pressure in India in national surveys, so these risks matter. (Matta rice keeps a little more bran, but it is still mainly starch; portion size matters most.)

**No crash diets.** Very-low-calorie diets, extreme fasting and "detox" plans may cause short-term weight loss, but most people regain it, and they can cause muscle loss, low energy, poor concentration (bad for exam preparation), gallstones and disordered eating. Steady, sustainable changes to everyday meals work better and are safer. If you have a medical condition (such as diabetes or kidney disease), follow your doctor's or dietitian's advice.
""",
    evidence=[
        ('Diets high in vegetables, fruit, pulses and whole grains lower disease risk', 'strong', 'Large long-term studies and reviews; basis of national guidelines.'),
        ('Too much refined grain, sugar, salt and ultra-processed food raises risk', 'strong', 'Consistent evidence; reflected in ICMR-NIN and WHO guidance.'),
        ('Half-plate vegetables model', 'tool', 'A practical public-health rule of thumb consistent with the guidelines.'),
        ('Crash diets and extreme fasting for lasting weight loss', 'failed', 'Most weight is regained; risks include muscle loss and disordered eating.'),
        ('Matta rice is much healthier than white rice', 'mixed', 'Slightly more fibre; portion size matters more.'),
    ],
    example="""
Sreeja photographs everything she eats for three days. A typical day: puttu with kadala curry and sweet tea for breakfast; a big plate of rice with a little sambar, fish fry and a spoon of thoran at lunch; sweet tea and two pazhampori at 4 pm; rice again with curry at night. Most of her plate, by area, is rice.

Using the balanced-plate pattern, she makes small changes: at lunch she fills half the plate with thoran, avial or salad first, and reduces rice by about a third; she has fish curry instead of fish fry on most days; she keeps puttu and kadala but adds a banana; at 4 pm she has sundal (boiled kadala or cherupayar with coconut and curry leaves) and tea with half the sugar; at night she has two chapatis or a smaller rice portion with cherupayar curry and vegetables. She doesn't count calories or cut out favourite foods; pazhampori becomes a weekend treat. After a month, she says her afternoon sleepiness is less.
""",
    apply=f"""
**The balanced Kerala plate (lunch or dinner):**
{fence('''BALANCED KERALA PLATE (rule of thumb)
 Half the plate:   vegetables (thoran, avial, sambar vegetables, salad,
                   cheera, payar, cabbage, beans) + fruit on the side
 A quarter:        grains (rice, matta rice, chapati, puttu, millets like ragi)
 A quarter:        protein (fish curry, egg, kadala, cherupayar, parippu,
                   rajma, chicken, curd, paneer)
 A little fat:     coconut, coconut oil or other oil in cooking (measured)
 Drink:            water; tea or coffee with little or no sugar
 Less often:       fried snacks, bakery items, sweets, packaged chips,
                   sugary drinks, extra salt and pickles''')}

**Simple swaps (choose three):** fill the vegetables first, then add rice; fish curry instead of fry; sundal or fruit instead of bakery snacks; halve sugar in tea; one millet meal (ragi puttu or dosa) a week; pickle and papad only sometimes; water instead of soft drinks.

**With others:** food is family and culture in Kerala. Don't lecture relatives; cook or bring one balanced dish, offer to make the thoran, or suggest the family tries a "vegetables first" plate for a week together.
""",
    resources=[
        ('icmr-sf', 'Read the article: the 17 guidelines and key numbers', '10 minutes'),
        ('nin-dgi', 'Skim the guidelines for the plate model and the food groups (find it on the NIN site if the link fails)', '30 minutes'),
        ('who-salt', 'Read the key facts on salt', '5 minutes'),
    ],
    steps=[
        'Photograph or write down everything you eat for three normal days.',
        'For each lunch and dinner, estimate the share of the plate that is grains, vegetables and protein.',
        'Choose three swaps and use them for the next seven days.',
        'Write which swaps were easy, which were hard, and how you felt (energy, hunger, afternoon sleepiness).',
    ],
    proof='Three days of meal photos or notes with plate estimates, your three swaps and a seven-day note on how they went.',
    templates=[('Plate audit', """PLATE AUDIT (3 days)
Day | Meal | Grains share | Vegetables share | Protein share | Fried? | Sugar in drinks (spoons)
Typical day summary: grains ___% vegetables ___% protein ___%
MY THREE SWAPS (7 days): 1 ______ 2 ______ 3 ______
Day | Swaps done (1 2 3) | Energy (1-5) | Hunger between meals (1-5) | Note""", '')],
    mistakes=[
        ('Cutting out rice or any food group completely.', 'Reduce portions and balance the plate; extremes are hard to keep and unnecessary.'),
        ('Crash diets before a wedding or exam.', 'They hurt energy and concentration, and the weight usually returns.'),
        ('Believing "healthy" labels on packaged foods.', 'Read ingredients; many "health" snacks are high in sugar, salt or fat.'),
        ('Ignoring drinks.', 'Several sweet teas a day add a lot of sugar.'),
    ],
    quiz=[
        Q('According to the ICMR-NIN 2024 guidelines, cereals and millets should provide no more than about:', '45% of daily energy', '90% of daily energy', '5% of daily energy', 'There is no limit', why='Many Indian diets exceed this, mostly from refined grains.'),
        Q('What share of India\'s disease burden did ICMR-NIN link to unhealthy diets?', 'About 56%', 'About 5%', 'About 90%', 'None', why='The 2024 guidelines estimated 56.4%.'),
        Q('What is WHO\'s salt recommendation for adults?', 'Less than 5 g a day (just under a teaspoon)', 'At least 15 g a day', 'No salt at all', '50 g a day', why='WHO recommends under 2,000 mg of sodium, equal to under 5 g of salt.'),
        Q('Which is the best everyday change for a rice-heavy Kerala lunch?', 'Fill half the plate with vegetables first and reduce the rice portion', 'Stop eating lunch', 'Replace rice with biscuits', 'Add more fried snacks', why='Balance and portion size, not extremes.'),
    ],
    study='read the lesson and the ICMR guideline summary',
    action='audit three days of meals and use three plate swaps for seven days',
)

L2 = lesson(
    20, 2,
    outcome='You can get enough protein on a small budget from Kerala foods, plan a week of balanced meals, and judge common food myths and supplement claims.',
    split='20 minutes reading, 30 minutes of planning',
    principle='Most people can meet their protein needs cheaply from pulses, eggs, milk, curd and fish spread across meals; supplements, "superfoods" and detox products are rarely needed and often oversold.',
    science=f"""
**How much protein?** Indian and international guidelines suggest roughly **0.8 to 1 g of protein per kg of body weight a day** for healthy adults (for example, about 50 to 60 g for a 60 kg adult); people doing regular strength training may benefit from somewhat more, but most can reach it with food. Spreading protein across meals helps. (These figures are standard nutrition references; check the NIN guidelines for the exact Indian values.)

**Budget protein in Kerala (approximate protein per typical serving):**
- **Pulses and legumes:** a cup of cooked cherupayar, kadala, parippu or rajma gives roughly 12 to 15 g. Cheap, filling and high in fibre. Combining pulses with rice or wheat over the day gives a good mix of amino acids.
- **Eggs:** about 6 g per egg; among the cheapest high-quality proteins.
- **Milk and curd:** about 6 to 8 g per glass or cup.
- **Fish:** a medium piece of sardine (mathi) or mackerel (ayala) gives roughly 15 to 20 g, plus omega-3 fats. Sardines are cheap and nutritious.
- **Chicken:** about 20 to 25 g per 100 g cooked.
- **Groundnuts, soya chunks, paneer:** useful extras.

(Protein amounts are rough guides from standard food tables; actual values vary.)

**Supplements.** The ICMR-NIN 2024 guidelines advise **against protein supplements for building muscle**, noting risks such as bone mineral loss and kidney damage with prolonged high intake ({link('icmr-sf', 'report')}). Vitamin and mineral supplements are useful only for a diagnosed deficiency (for example, vitamin B12 or iron, confirmed by a test and advised by a doctor). This course does not recommend any supplement.

**Common myths:**
- **"Detox" drinks and cleanses:** the liver and kidneys detoxify the body; there is no good evidence for detox products.
- **"Superfoods":** no single food (chia, quinoa, "miracle" berries) transforms health; an overall pattern matters. Local foods (cheera, muringa leaves, payar, mathi) are excellent and cheap.
- **"Eating after 8 pm makes you fat":** total intake and food quality matter more than the clock, though late heavy meals can disturb sleep.
- **"Coconut oil is a superfood" / "coconut oil is poison":** it is high in saturated fat; use it in moderate amounts like any oil.
- **"Fasting is the best way to lose weight":** intermittent fasting works about as well as other ways of eating less for some people, but it is not magic and is not suitable for everyone (for example, people with diabetes on medication, or anyone with a history of disordered eating). This course does not recommend extended or extreme fasting.

**Disordered eating.** If you notice intense fear of weight gain, skipping meals to compensate, bingeing, or using exercise to "burn off" food, talk to a doctor or call Tele-MANAS (14416).
""",
    evidence=[
        ('Most adults can meet protein needs from food', 'strong', 'Standard nutrition science; supported by Indian guidance.'),
        ('Protein supplements needed for muscle building', 'failed', 'Not needed for most; ICMR-NIN advises against them.'),
        ('Detox products remove toxins', 'failed', 'No good evidence; the liver and kidneys do this.'),
        ('Single "superfoods" transform health', 'failed', 'Overall diet pattern matters, not single foods.'),
        ('Intermittent fasting for weight loss', 'mixed', 'Similar results to other calorie reduction for some; not for everyone.'),
    ],
    example="""
Vinod lifts no weights but now trains bodyweight three times a week and wants more protein. He was about to buy a ₹2,800 protein powder because a gym influencer said "you can't build muscle without it".

He plans a week with food instead. Breakfast: two eggs with puttu, or idli with sambar and a glass of milk. Lunch: rice (smaller portion) with fish curry (sardine or mackerel twice a week), cherupayar thoran and curd. Evening: sundal or a handful of roasted groundnuts with tea. Dinner: chapati with kadala curry or egg roast and vegetables. He estimates about 60 to 70 g of protein a day, enough for his 64 kg and his training. The week's extra cost is about ₹300 (eggs, fish, curd), much less than the powder, and the money he saved goes to his emergency fund.
""",
    apply=f"""
**Plan a week of balanced, budget meals:**
1. Use the balanced Kerala plate (PD-M20-L01) for lunch and dinner.
2. Add a protein food at **every meal**: egg, milk or curd at breakfast; fish, pulses or chicken at lunch; pulses or egg at dinner.
3. Add a protein snack (sundal, groundnuts, curd) instead of bakery items.
4. Shop locally and seasonally: fish on market days, pulses in bulk, local greens.
5. Estimate your daily protein roughly with the list above.

{fence('''WEEKLY MEAL PLAN (fill in)
Day | Breakfast (+ protein) | Lunch (half veg, quarter grain, quarter protein) | Snack | Dinner (+ protein)
Mon | ______ | ______ | ______ | ______
...
Shopping list: pulses ______ eggs ___ milk/curd ___ fish ___ vegetables ______ fruit ______
Rough protein per day: ___ g (target about 0.8-1 g per kg = ___ g)''')}

**Judge a food claim:** use the claim check from PD-M02-L01: who is selling it, what is the evidence, how big is the effect?

**With others:** be careful with advice to family members with diabetes, kidney or heart problems; their needs are specific. Encourage them to follow their doctor's or dietitian's plan.
""",
    resources=[
        ('nin-dgi', 'Find the section on protein and on dietary supplements; read it', '20 minutes'),
        ('icmr-sf', 'Re-read the part on protein supplements', '5 minutes'),
        ('os-psych', 'Optional: read OpenStax 10.2 Hunger and Eating (go to chapter 10 from the contents) for the psychology of appetite', '20 minutes'),
    ],
    steps=[
        'Write your weekly meal plan with a protein food at every meal.',
        'Estimate your daily protein for two days and compare with about 0.8 to 1 g per kg of your body weight.',
        'Follow the plan for one week and note the cost compared with your usual week.',
        'Find one food or supplement ad or influencer claim and run the claim check on it.',
    ],
    proof='Your weekly meal plan, two days of protein estimates, the week\'s cost note and one claim check.',
    templates=[('Food claim check', """FOOD CLAIM CHECK
Claim: "______________________________"   Source: ______ (selling something? Y/N)
Study type and size: ______   Effect size: ______   Compared with: ______
Does it fit ICMR-NIN / WHO guidance? ______
Verdict: trust / maybe / don't trust yet. Cheaper local alternative: ______""", '')],
    mistakes=[
        ('Buying protein powder before fixing meals.', 'Food first; ICMR-NIN advises against supplements for muscle building.'),
        ('Believing detox and superfood claims.', 'Check the evidence; local whole foods are excellent.'),
        ('Extreme fasting for quick results.', 'Not recommended; it harms energy and concentration and can trigger disordered eating.'),
        ('Giving diet advice to people with medical conditions.', 'They need their doctor\'s or dietitian\'s plan.'),
    ],
    quiz=[
        Q('About how much protein do healthy adults need per day, as a rough guide?', 'About 0.8 to 1 g per kg of body weight', '5 g per kg', 'No protein is needed', '100 g per kg', why='Standard reference figures; check NIN for exact values.'),
        Q('Which is a cheap, high-quality protein food?', 'Eggs', 'Biscuits', 'Banana chips', 'Soft drinks', why='About 6 g of protein per egg at low cost.'),
        Q('What does the ICMR-NIN 2024 guidance say about protein supplements for muscle?', 'Avoid them; get protein from a balanced diet', 'Everyone should take them', 'Take double doses', 'Nothing', why='It advises against them, citing health risks.'),
        Q('What is true about "detox" drinks?', 'There is no good evidence they remove toxins; the liver and kidneys do that', 'They clean the blood', 'They are required after festivals', 'They cure diabetes', why='Detox claims are not supported.'),
    ],
    study='read the lesson and the protein and supplement sections of the guidelines',
    action='plan and follow a week of balanced budget meals with protein at every meal, and check one food claim',
)

LESSONS = [L1, L2]

MODULE = module(
    20,
    overview=f"""
Nutrition with a Kerala diet: the main points of the ICMR-NIN Dietary Guidelines for Indians (2024), a balanced Kerala plate, budget protein, a week of meals, and honest notes on supplements, detox, superfoods and crash diets.

This module teaches **general healthy eating only**: no crash diets, no extreme fasting, no supplements. Kerala food already has great strengths (fish, vegetables, pulses, fermented foods); the common problems are large rice portions, fried snacks, sugary tea and packaged foods. Small, steady swaps fix most of it.

If you have diabetes, high blood pressure, kidney disease or any other condition, follow your doctor's or dietitian's advice. If eating, weight or body image is causing you distress, talk to a doctor or Tele-MANAS (14416).
""",
    outcomes=[
        'Summarise the key ICMR-NIN 2024 guidelines and the WHO salt limit.',
        'Build a balanced Kerala plate and audit your own meals.',
        'Get enough protein cheaply from local foods.',
        'Judge supplement, detox, superfood and fasting claims.',
    ],
    lessons=LESSONS,
    project='a week of balanced plates',
    project_steps=[
        'Audit three days of meals (PD-M20-L01).',
        'Plan and follow one week of balanced meals with protein at every meal (PD-M20-L02).',
        'Note energy, hunger, afternoon sleepiness and cost.',
        'Write your three keeper swaps and your plate rule into the Playbook.',
    ],
    project_proof='The plate audit, the weekly plan with notes, and your keeper swaps.',
    rubric=[
        ('Knowledge', 'Cannot name any guideline', 'Names a few', 'Explains cereal, protein, sugar, fat and salt guidance'),
        ('Audit', 'No audit', 'One day', 'Three days with plate estimates'),
        ('Plan', 'No plan', 'Partial week', 'Full week followed with protein at every meal'),
        ('Critical thinking', 'Believes supplement and detox claims', 'Unsure', 'Checks claims and prefers whole foods'),
    ],
    short=[
        'Fill half your lunch plate with vegetables first.',
        'Add an egg, curd or pulses to one more meal a day.',
    ],
    flashcards=[
        ('ICMR-NIN 2024: cereals limit', 'No more than about 45% of daily energy.'),
        ('Disease burden from unhealthy diets (ICMR-NIN)', 'About 56%.'),
        ('Sugar and fat limits', 'Sugar under 5% of energy; total fat at most about 30%.'),
        ('WHO salt limit', 'Less than 5 g a day.'),
        ('Balanced plate rule of thumb', 'Half vegetables and fruit, a quarter grains, a quarter protein.'),
        ('Protein rough guide', 'About 0.8–1 g per kg of body weight a day.'),
        ('Protein supplements (ICMR-NIN)', 'Avoid for muscle building; food first.'),
        ('Crash diets', 'Weight usually returns; risks include muscle loss and disordered eating.'),
    ],
    mistakes=[
        ('Thinking healthy eating means expensive food.', 'Pulses, eggs, sardines and local vegetables are cheap and excellent.'),
        ('All-or-nothing rules.', 'Treats are fine sometimes; patterns matter.'),
        ('Following influencers over guidelines.', 'Check claims against ICMR-NIN and WHO.'),
    ],
    tools=[
        'The balanced Kerala plate and plate audit (PD-M20-L01).',
        'The weekly meal plan and food claim check (PD-M20-L02).',
    ],
    playbook=[
        'My plate: half vegetables, a quarter grains, a quarter protein; protein at every meal.',
        'My three keeper swaps: ______. No crash diets, no supplements without a doctor.',
    ],
)
