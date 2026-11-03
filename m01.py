"""Module 1: Money mindset and behavioural finance."""
from common import lesson, module, link, fence, table, inr

M = 1

L1 = lesson(
    M, 1,
    title='Your money story and values',
    weeks=(1, 1), hours=1.5,
    outcome='Write down the money beliefs you grew up with, name your top three money values and turn them into spending rules you can follow.',
    split='20 minutes reading, 30 minutes resources, 40 minutes action',
    core=f"""
Every money decision you make is shaped by two things you rarely look at: the **money story** you learned growing up, and the **values** you actually hold today. When the two don't match, you feel guilty about spending you enjoy, or you spend on things you don't care about because "that's what people do". This lesson makes both visible.

### Your money story

Most of us learned about money by watching our family, not from lessons. In Kerala, some common family money beliefs are:

- **"Gold is the safest saving."** Many families save in jewellery for weddings and emergencies.
- **"A government job means you are settled."** Security is valued above income.
- **"Land never loses value."** Money goes into plots and houses, even when it means big loans.
- **"Money from the Gulf solves everything."** Remittances paid for houses and weddings, sometimes without savings for the person who earned them.
- **"Don't talk about money."** Children rarely know what the family earns, owes or has saved.
- **"Chitty and the co-operative society are like family."** Trust comes from people you know, not from rules.

None of these is simply right or wrong. Some protected families for generations; some caused real harm when a belief met a changed world. The point is to **notice which beliefs drive you**, so you choose them instead of following them automatically.

### Values: what money is for

A value is something that matters to you for its own sake: security, learning, family, freedom, health, generosity, comfort, adventure, status, faith, independence, beauty. Money is a tool for living your values. **Values-based spending** is a simple rule:

> Spend freely on what you value most. Cut hard on what you don't.

This is different from "spend less on everything". A person who values learning should not feel guilty about buying PSC books; a person who doesn't care about clothes should not buy new ones for every function just because others do.

### From values to rules

Values become useful when you turn them into **spending rules**, short sentences you can follow without thinking:

- "Books, courses and PSC materials: always yes, up to ₹1,500 a month."
- "Gold only for planned gifts, never as an impulse."
- "Eating out once a week with friends; no delivery on weekdays."
- "₹500 from every income goes to my parents' medicine fund first."

Good rules are **specific** (a number or a frequency), **positive where possible** (what you will do) and **few** (three to five).

### Why this comes first

Budgets fail when they fight your values. If you value time with friends and your budget says "no eating out", you will break it within a week and feel bad. If your budget gives friends ₹800 a month and cuts the ₹900 of food delivery you don't really care about, you keep it. Modules 2 and 3 build your goals and budget on the values you write today.
""",
    example=f"""
**Anu**, 27, lives in Kakkattil and is preparing for the LD Clerk and LGS exams. She tutors school students in the evenings and earns about ₹14,000 a month, more in exam season and less in vacations. Her parents value gold and land; her father once lost money in a "deposit scheme" run by a friend, and the family never spoke about it.

When Anu wrote her money story, she noticed two beliefs: "money talk causes fights" and "gold is the only safe saving". When she ranked her values, she put **independence**, **learning** and **family** at the top. Comfort and status came last.

Then she looked at her first week of the expense log:

{table(['Spend', 'Amount', 'Matches a top value?'], [
    ('PSC test series app', '₹399', 'Yes: learning'),
    ('Food delivery, three times', '₹735', 'No'),
    ('Medicine for her mother', '₹620', 'Yes: family'),
    ('New earrings in a sale', '₹1,150', 'No: bought because a friend did'),
    ('Bus pass top-up', '₹300', 'A need'),
])}

Her rules: "Learning spend up to ₹1,000 a month, no guilt"; "Delivery only on Sundays"; "Jewellery only from a planned gift list"; "₹1,000 a month into my own savings before I give money at home, because independence matters". She showed the rules to her mother and, for the first time, the two of them talked about the old deposit scheme.
""",
    resources=[
        ('sebi-investor', 'The "Learn to manage your money for financial well-being" guide: read the part on managing money and setting priorities', '20 minutes'),
        ('ncfe', 'Register free, then do the module on managing income and expenditure', '20 minutes'),
        ('rbi-fe', 'Browse the Financial Awareness Messages (FAME) and note two that apply to you', '10 minutes'),
    ],
    steps=[
        'Answer the five money-story questions in the template, honestly, in English or Malayalam. Write at least three lines each.',
        'Rank the 12 values in the template from 1 to 12. Circle your top three.',
        'Open your expense log (or your bank app\'s UPI history for the last 14 days if the log has just started). Find three spends that match a top value and three that don\'t.',
        'Write three to five spending rules that follow from your values. Each must have a number or a frequency.',
        'Make a new tab in the Money Workbook called **Values** and copy the template into it.',
        'Tell one person (your money buddy or a family member) your top value and one rule. Their reaction is useful information.',
    ],
    proof='A screenshot of the Values tab with your top three values and at least three rules, saved in 01 Mindset.',
    templates=[
        ('money story questions', """
MY MONEY STORY (date: ____)
1. What did my family say or show about money when I was a child?
2. One money event I still remember (good or bad), and what it taught me:
3. What do I believe about gold, land, loans, government jobs and the Gulf?
4. When I spend money, what do I feel: guilty, happy, anxious, nothing?
5. One belief I want to keep, and one I want to change:
""", ''),
        ('Values tab', """
Value,Rank (1-12),Why it matters to me,Spending that supports it,Spending that doesn't,My rule (with a number)
Security,,,,,
Independence,,,,,
Family,,,,,
Learning,,,,,
Health,,,,,
Freedom of time,,,,,
Generosity and giving,,,,,
Comfort,,,,,
Status and appearance,,,,,
Adventure and travel,,,,,
Faith and community,,,,,
Beauty and creativity,,,,,
""", 'csv'),
    ],
    mistakes=[
        ('Writing the values you think you should have.', 'If you rank "security" first but spend every spare rupee on clothes, your real value may be appearance. That is allowed; just be honest, then decide.'),
        ('Rules without numbers.', '"Spend less on food" is a wish. "Delivery only on Sundays, up to ₹300" is a rule you can check.'),
        ('Too many rules.', 'Ten rules are forgotten in a week. Start with three to five.'),
        ('Blaming family beliefs.', 'Your parents\' beliefs made sense in their world. Keep what still works, change what doesn\'t, without contempt.'),
    ],
    quiz=[
        {'q': 'What is values-based spending?', 'o': ['Spending freely on what you value most and cutting hard on what you don\'t', 'Cutting every category by 10%', 'Spending only on needs, never on wants', 'Copying the budget of someone who is rich'], 'a': 'A', 'why': 'It doesn\'t cut everything equally; it moves money from what you don\'t care about to what you do.'},
        {'q': 'Which of these is a good spending rule?', 'o': ['Eat out once a week, up to ₹400', 'Try to spend less on food', 'Be careful with money', 'Never enjoy anything'], 'a': 'A', 'why': 'A good rule is specific: it has a frequency and a number you can check.'},
        {'q': 'Why does the course look at values before building a budget?', 'o': ['Budgets that fight your values get broken quickly', 'Values decide your tax regime', 'Banks ask for your values', 'It is a legal requirement'], 'a': 'A', 'why': 'A budget that funds what you care about is one you keep.'},
        {'q': 'Anu values learning. How should she treat her ₹399 PSC test series?', 'o': ['As a planned, guilt-free spend within her learning limit', 'As a waste to be cut first', 'As an investment that must earn a return', 'As something to hide from her family'], 'a': 'A', 'why': 'It matches a top value, so it belongs in her plan, within the limit she set.'},
    ],
    study='SEBI money-management guide, the NCFE module on income and expenditure, and two RBI awareness messages',
    action='Write your money story, rank your values and set 3–5 spending rules in the Values tab',
)

L2 = lesson(
    M, 2,
    title='The biases that cost you money',
    weeks=(1, 2), hours=1.5,
    outcome='Recognise seven common money biases in your own spending and put two simple rules in place that stop them.',
    split='25 minutes reading, 25 minutes resources, 40 minutes action',
    core=f"""
Behavioural finance studies why intelligent people make money decisions that hurt them. The problem is rarely a lack of knowledge. It is how human brains work: we prefer now over later, hate losses more than we enjoy gains, and copy the crowd. You can't remove these biases, but you can **design rules around them**.

### Seven biases, with the rule that beats each one

{table(['Bias', 'What it does', 'How it costs you', 'The rule that beats it'], [
    ('Present bias', 'Today feels far more real than next year', 'Saving "from next month" never starts', 'Save first, automatically, on the day money arrives'),
    ('Loss aversion', 'A loss hurts about twice as much as a gain pleases', 'You hold a bad policy or investment to avoid "booking a loss"', 'Judge by the future, not by what you already paid'),
    ('Herd behaviour (FOMO)', 'Doing what everyone around you does', 'Buying a hot stock, a crypto coin or a "scheme" because others are', 'Never invest in anything you can\'t explain in two sentences'),
    ('Anchoring', 'The first number you see shapes your judgement', '"MRP ₹4,000, now ₹1,999" feels like saving ₹2,001', 'Ask "would I pay ₹1,999 for this if there was no MRP?"'),
    ('Mental accounting', 'Treating money differently by where it came from', 'A bonus, gift or arrears is spent as "free money"', 'Every rupee goes through the same plan, whatever its source'),
    ('Overconfidence', 'Believing you know more than you do', 'Trading, picking stocks, or skipping insurance because "nothing will happen"', 'Write down your reasons; check them later against what happened'),
    ('Social pressure', 'Spending to match what others expect', 'Weddings, functions, phones and gold beyond your means', 'Decide your amount before the event, privately'),
])}

### Two more traps scammers use

- **Urgency:** "Offer ends tonight", "your account will be blocked in 30 minutes". Urgency switches off careful thinking. Real banks, insurers and government offices give you time.
- **Authority:** a uniform, a logo or a confident voice makes us obey. Scammers pretend to be the police, RBI or a bank (Module 15).

### Why small leaks matter: a worked example

Small daily spends feel too small to matter, but they add up:

{table(['Daily habit', 'Per day', 'Per month (30 days)', 'Per year (365 days)'], [
    ('Tea and a snack outside', '₹40', inr(40 * 30), inr(40 * 365)),
    ('Food delivery, average per day', '₹100', inr(100 * 30), inr(100 * 365)),
    ('Unused subscriptions, per day', '₹10', inr(10 * 30), inr(10 * 365)),
])}

₹100 a day is {inr(36500)} a year: for many people that is a whole emergency fund. The point is not to ban tea. It is to choose these spends on purpose.

### Commitment devices: rules that work when willpower doesn't

- **Pay yourself first:** a standing instruction moves savings on the day income arrives (Module 5).
- **The 24-hour rule:** for any want above an amount you choose (say ₹1,000), wait 24 hours. For above ₹10,000, wait 30 days.
- **Friction:** remove saved cards from shopping apps, turn off sale notifications, delete apps you use only to browse.
- **Pre-decide:** write the amount for a wedding gift or festival budget before you go.
""",
    example=f"""
**Fathima**, 31, a freelance designer in Kuttiady, finished a big branding project for a Gulf client and received ₹60,000 at once. Her first thought: "This is extra; I'll finally buy the new phone." That is mental accounting: the money felt like a bonus because it came in one lump.

Before buying, she used the 24-hour rule and looked at her numbers. Her average income over the last six months was ₹32,000 a month, but two months had been under ₹15,000. The ₹60,000 was really **two months of normal income**, and she had to set aside money for income tax on it (Module 10).

Her decision: ₹15,000 to her tax and slow-month buffer, ₹10,000 to her emergency fund, ₹25,000 for normal monthly spending over the next month, and ₹10,000 towards a phone, with the rest saved from the next two projects. She bought the phone two months later, without a loan, and noticed she no longer wanted the most expensive model.
""",
    resources=[
        ('varsity', 'Module 12, "Innerworth: Mind over markets": read any two chapters on emotions and biases in money decisions', '30 minutes'),
        ('sebi-investor', 'The fraud-warning topics (fake trading apps, "stock market guru" scams): read one and notice which biases it uses', '15 minutes'),
    ],
    steps=[
        'Open the days you have logged so far. Mark every **want** (not a need) with the bias that best explains it, using the table in the core lesson. Some wants have no bias; that\'s fine.',
        'Count which bias appears most often. That is your main leak.',
        'Pick two rules from the core lesson that fight your top two biases, such as the 24-hour rule and removing saved cards.',
        'Set them up today: remove the saved card, turn off sale notifications, write the 24-hour rule on your phone\'s lock-screen note, or whatever your rules need.',
        'Calculate your own "small leak" in the template: one daily habit × 365.',
    ],
    proof='Your bias audit (the template, filled in) and a screenshot showing one rule set up, such as a removed saved card or a lock-screen note, saved in 01 Mindset.',
    templates=[
        ('bias audit', """
BIAS AUDIT (days logged: ____)
Want,Amount (₹),Bias (present / loss / herd / anchor / mental accounting / overconfidence / social / none),What I'd do differently
,,,
,,,
,,,

Most common bias: ____
Rule 1 that beats it: ____ (set up on ____)
Rule 2: ____ (set up on ____)

My small leak: ____ per day x 365 = ₹____ a year
""", ''),
        ('formula: yearly cost of a daily habit', """
A2: daily amount, for example 100
B2: =A2*365          yearly cost
C2: =A2*30           monthly cost
""", ''),
    ],
    mistakes=[
        ('Thinking biases are only for "other people".', 'Everyone has them, including experts. The aim is better rules, not shame.'),
        ('Relying on willpower.', 'Willpower runs out by evening. Friction and automation work every day.'),
        ('Banning every small pleasure.', 'A plan with no joy gets abandoned. Choose your small spends; don\'t eliminate them.'),
        ('Treating lump sums as free money.', 'Arrears, bonuses, gifts and big client payments go through the same plan as your salary.'),
    ],
    quiz=[
        {'q': 'A shirt shows "MRP ₹4,000, today ₹1,999". Which bias makes this feel like a saving of ₹2,001?', 'o': ['Anchoring', 'Loss aversion', 'Present bias', 'Overconfidence'], 'a': 'A', 'why': 'The first number (the MRP) anchors your judgement. You still spend ₹1,999.'},
        {'q': 'You keep paying for a policy you know is poor only because "I have already paid three years". Which bias is this?', 'o': ['Loss aversion and the sunk-cost trap', 'Herd behaviour', 'Anchoring', 'Mental accounting'], 'a': 'A', 'why': 'Money already paid is gone either way; judge by what happens from today (Module 7 shows how to evaluate such policies).'},
        {'q': 'What is the best defence against present bias?', 'o': ['Saving automatically on the day income arrives', 'Promising yourself to save next month', 'Reading more about markets', 'Keeping all savings in cash at home'], 'a': 'A', 'why': 'Automation removes the daily choice, so "later" can\'t win.'},
        {'q': '₹100 a day on delivery food costs about how much in a year?', 'o': ['₹36,500', '₹3,000', '₹12,000', '₹1,00,000'], 'a': 'A', 'why': '₹100 × 365 = ₹36,500.'},
        {'q': 'A caller says your bank account will be blocked in 30 minutes unless you act now. What is the scammer using?', 'o': ['Urgency', 'Diversification', 'Compounding', 'Anchoring on MRP'], 'a': 'A', 'why': 'Urgency stops careful thinking. Real banks give you time and never ask for OTPs or PINs.'},
    ],
    study='Two chapters of Varsity\'s "Innerworth" module and one SEBI fraud-warning topic',
    action='Do a bias audit of your logged spending and set up two rules that beat your top biases',
)

L3 = lesson(
    M, 3,
    title='Needs, wants and lifestyle inflation',
    weeks=(2, 2), hours=1.5,
    outcome='Split your spending into needs, wants and upgrades with a formula, price a want in hours of work, and write a rule for future raises.',
    split='20 minutes reading, 20 minutes resources, 50 minutes action',
    core=f"""
### Needs, wants and the hidden third type

- **A need** is something you must pay for to live, work or stay healthy: basic food, rent, electricity, bus fare, medicines, a working phone, insurance, loan EMIs you already owe.
- **A want** is something you would like but can live without: eating out, a new dress for a function, a streaming plan, a bike upgrade.
- **An upgraded need** is the one that tricks us: a need, bought in a more expensive version. A working phone (about ₹12,000) is a need; the ₹45,000 model is the need plus a ₹33,000 want. Rice is a need; daily restaurant meals are mostly want.

When you classify spending, split upgraded needs in your head: the basic part is a need, the extra is a want. In your log, mark the whole spend by its bigger part and add a note.

### Lifestyle inflation

**Lifestyle inflation** (or lifestyle creep) means your spending rises every time your income rises, so you never save more. It is very common after a first job, a pay rise, DA arrears or a move to the Gulf. Signs:

- Your income doubled in five years but your savings didn't.
- "We can afford it now" is said about every upgrade.
- Each new comfort becomes a "need" within months: a car, an AC, a bigger house, daily delivery.

The fix is simple to state: **decide what happens to a raise before it arrives.** A common rule is the **half-raise rule**: at least half of every increase in take-home income goes to savings, goals or debt payoff, and the rest improves your life. You enjoy the raise and still get ahead.

### Price a want in hours of your life

Money is time you have already spent working. Converting a price to hours makes wants honest:

> Your hourly income = monthly take-home ÷ hours you work in a month
> Hours of work for a want = price ÷ hourly income

**Worked example:** Rahul takes home ₹30,000 a month for about 176 working hours (8 hours × 22 days). His hourly income is ₹30,000 ÷ 176 = about ₹170. A ₹45,000 phone costs him ₹45,000 ÷ ₹170 = about **265 hours**, which is about **33 working days**. The ₹12,000 phone costs about 71 hours. Is the better camera worth 194 extra hours of work? Sometimes yes. But now it is a choice.

### Needs come first, wants are planned

The order of your money each month: needs, then savings and debt payments, then wants. Wants are not bad. A plan with zero wants fails. The 50/30/20 method in Module 3 gives wants a fixed share, so you enjoy them without guilt.
""",
    example=f"""
**Rahul**, 29, from Thottilpalam, joined a Kerala government office as an LD clerk this year after his PSC exam. (His numbers here are made up to show the method; your pay depends on your post and the pay scale.) Before the job he lived on about ₹6,000 a month from tuition. Now he takes home about ₹30,000.

Within three months his spending rose from ₹6,000 to ₹27,000: a ₹2,900 EMI for a phone, eating out three times a week, a gym he went to twice, new clothes, and more help to his parents (which he valued). He was saving ₹3,000 a month and felt he had "no money left".

He split his last month using the method in this lesson:

{table(['Type', 'Amount', 'Share of ₹30,000'], [
    ('Needs (food at home, rent share, bus, phone bill, parents\' medicines)', '₹12,400', '41%'),
    ('Upgraded needs, extra part only (expensive phone EMI, branded clothes)', '₹4,600', '15%'),
    ('Wants (eating out, gym, subscriptions)', '₹10,000', '33%'),
    ('Saved', '₹3,000', '10%'),
])}

He kept the parents' help and his weekly dinner with friends, cancelled the gym (₹1,200) and two subscriptions (₹500), and set a half-raise rule for his next DA increase. His saving went from ₹3,000 to ₹6,500 a month without feeling poor.
""",
    resources=[
        ('ncfe', 'In the e-LMS course, finish the managing income and expenditure module and its quiz', '20 minutes'),
    ],
    steps=[
        'In the Expenses tab, make sure every row has **Need** or **Want** in column D. Use "Want" for the extra part of an upgraded need if you can split it; otherwise mark the row by its bigger part and add a note.',
        'In an empty area of the Expenses tab, add the three formulas from the template to total needs, wants and everything.',
        'Work out the percentage of needs and wants so far.',
        'Calculate your hourly income (from income, tuition, pocket money or family support; if you have no income, use what you hope to earn in your first job) and price one want you are considering in hours.',
        'Write your raise rule: what percentage of any future increase in income will go to savings and goals.',
        'Pick one want to pause for 30 days and write it down. You decide in Module 3 whether to bring it back.',
    ],
    proof='A screenshot of your needs and wants totals with percentages, your hours-of-work calculation for one want, and your raise rule, saved in 01 Mindset.',
    templates=[
        ('needs and wants formulas (Expenses tab)', """
J2: Needs total      K2: =SUMIF(D2:D500,"Need",B2:B500)
J3: Wants total      K3: =SUMIF(D2:D500,"Want",B2:B500)
J4: All spending     K4: =SUM(B2:B500)
J5: Needs %          K5: =IF(K4>0,K2/K4*100,0)
J6: Wants %          K6: =IF(K4>0,K3/K4*100,0)
""", ''),
        ('hours of work for a want', """
A2: monthly take-home income (₹)        30000
B2: hours worked in a month             176
C2: hourly income  =A2/B2
D2: price of the want (₹)               45000
E2: hours of work  =D2/C2
F2: working days   =E2/8
""", ''),
        ('my raise rule', """
When my take-home income rises, at least ____% of the increase goes to:
1. ____ (for example, emergency fund until it is full)
2. ____ (for example, my goals and retirement)
The rest I can use to improve my life, starting with: ____
Signed: ____  Date: ____
""", ''),
    ],
    mistakes=[
        ('Calling every want a need.', 'Ask: "What happens if I don\'t buy this for a month?" If the honest answer is "nothing serious", it is a want.'),
        ('Feeling guilty about all wants.', 'Wants are part of a good life. The goal is to choose them, not to remove them.'),
        ('Letting EMIs turn wants into needs.', 'Once you take an EMI for a phone, the EMI is a need. Avoid that trap for wants (Module 6).'),
        ('Waiting for the raise to decide.', 'Decide your raise rule now, while the money doesn\'t exist yet. It is much easier.'),
    ],
    quiz=[
        {'q': 'A basic working phone costs ₹12,000; you buy a ₹45,000 model. How should you think of the ₹33,000 difference?', 'o': ['As a want inside an upgraded need', 'As a need, because phones are essential', 'As an investment', 'As a tax deduction'], 'a': 'A', 'why': 'The basic phone is the need; the extra cost is a want you are choosing.'},
        {'q': 'What is lifestyle inflation?', 'o': ['Spending rising every time income rises, so savings don\'t grow', 'General price rise measured by CPI', 'An insurance premium increase', 'The interest rate on a credit card'], 'a': 'A', 'why': 'It is personal: your own spending creeping up with income.'},
        {'q': 'Rahul earns ₹170 an hour. About how many hours of work is a ₹17,000 purchase?', 'o': ['100 hours', '10 hours', '1,000 hours', '17 hours'], 'a': 'A', 'why': '₹17,000 ÷ ₹170 = 100 hours.'},
        {'q': 'Which formula totals the "Need" rows when amounts are in column B and types in column D?', 'o': ['=SUMIF(D2:D500,"Need",B2:B500)', '=SUM(D2:D500)', '=COUNT(B2:B500)', '=AVERAGE(B2:D500)'], 'a': 'A', 'why': 'SUMIF checks column D for "Need" and adds the matching amounts from column B.'},
    ],
    study='The NCFE module on managing income and expenditure, with its quiz',
    action='Split your logged spending into needs and wants with formulas, price one want in hours and write your raise rule',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    M,
    title='Money mindset and behavioural finance',
    weeks=(1, 2), hours=5.5,
    overview="""
Understand the beliefs, values and biases behind your money decisions, and turn them into a few clear spending rules.

Most money problems are not maths problems. People know they should save; they just don't. This module looks at why: the money story you grew up with, the values you actually hold, the biases every brain has, and the slow creep of lifestyle inflation.

You start your 30-day expense log in the same week (see the **Money habits track**), so every lesson here uses your real spending, not imaginary examples. By the end of week 2 you have a short list of spending rules that fit your values and protect you from your own biases. Every later module builds on them.
""",
    outcomes=[
        'Describe the money beliefs you grew up with and choose which to keep',
        'Rank your money values and turn them into specific spending rules',
        'Recognise seven common biases in your own spending and set up rules that beat them',
        'Separate needs, wants and upgraded needs with a spreadsheet formula',
        'Price a want in hours of work and write a rule for future raises',
    ],
    lessons=LESSONS,
    project='My money values and spending rules',
    project_steps=[
        'Open your Values tab. Make sure your top three values are clear and each has a "why".',
        'Write your final list of five spending rules: at least one from your values, one 24-hour or 30-day rule, one friction rule (such as no saved cards), your raise rule, and one rule about family or functions.',
        'Under the rules, add evidence from your expense log: two spends that followed a rule and one that broke it, and what you learned.',
        'Write one paragraph: "The money belief I am changing, and why."',
        'Show the rules to your money buddy or a family member and ask, "Which of these will be hardest for me?" Write their answer down.',
    ],
    project_proof='A screenshot or PDF of your Values tab with the five rules, the evidence and the paragraph, saved in 01 Mindset.',
    rubric=[
        ('Money story', 'Not written', 'Written, but vague', 'Written honestly, with one belief to keep and one to change'),
        ('Values', 'Not ranked', 'Ranked, without reasons', 'Top three ranked, each with a reason'),
        ('Rules', 'None, or no numbers', 'Some rules have numbers', 'Five specific rules, each with a number or frequency'),
        ('Evidence', 'None', 'Examples, but not from the log', 'Real spends from your log, kept and broken'),
        ('Rules in action', 'Nothing set up', 'One rule set up', 'At least two rules set up (friction or automation)'),
    ],
    short=[
        'Rank your values and write three rules (FIN-M01-L01, steps 2 and 4).',
        'Remove saved cards from one shopping app (FIN-M01-L02).',
        'Add the needs and wants formulas and write your raise rule (FIN-M01-L03).',
        'Keep the 30-day log going; it matters more than anything else in these weeks.',
    ],
    flashcards=[
        ('Values-based spending in one sentence', 'Spend freely on what you value most, cut hard on what you don\'t.'),
        ('Present bias', 'Today feels more real than the future, so saving "later" never starts. Beat it by saving automatically first.'),
        ('Anchoring', 'The first number you see, such as an MRP, shapes your judgement of a price.'),
        ('Mental accounting', 'Treating money differently by its source, so bonuses and gifts get wasted.'),
        ('Upgraded need', 'A need bought in an expensive version; the extra part is a want.'),
        ('Lifestyle inflation', 'Spending rising with income so that savings never grow.'),
        ('The half-raise rule', 'At least half of every increase in income goes to savings, goals or debt payoff.'),
        ('Hours of work for a want', 'Price ÷ (monthly take-home ÷ hours worked in a month).'),
    ],
    mistakes=[
        ('Skipping this module as "soft".', 'Rules built here are what keep your budget alive in month three.'),
        ('Pausing the 30-day log.', 'The log is the raw material for Modules 2 and 3. Ten minutes a day, every day.'),
        ('Judging yourself.', 'You are collecting information, not grading yourself. Honest data beats a good-looking month.'),
    ],
    project_week=2,
)
