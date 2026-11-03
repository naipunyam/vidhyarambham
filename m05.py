"""Module 5: Emergency fund."""
import math
from common import lesson, module, link, fence, table, inr

M = 5

ANU_ESS = 9000
RAHUL_ESS = 16500
FATIMA_ESS = 20000


def months_to_target(target, monthly, rate=0.0, start=0):
    if rate == 0:
        return math.ceil((target - start) / monthly)
    r = rate / 12
    n = math.log((target * r + monthly) / (start * r + monthly)) / math.log(1 + r)
    return math.ceil(n)


L1 = lesson(
    M, 1,
    title='How big should your emergency fund be?',
    weeks=(9, 9), hours=1.5,
    outcome='Work out your essential monthly expenses and choose a starter target and a full target for your emergency fund, based on how stable your income is.',
    split='20 minutes reading, 20 minutes resources, 50 minutes action',
    core=f"""
An **emergency fund** is money kept aside only for real emergencies: losing your income, illness or an accident, an urgent repair, a family crisis. It is the foundation of every plan in this course. Without it, the first shock pushes you into a credit card, a loan app or a gold loan, and your goals stop.

### What counts as an emergency

- **Yes:** job or income loss, hospital costs insurance doesn't cover, an accident, urgent house repairs after heavy rain, a family emergency far away, a broken phone or laptop you need for work.
- **No:** festivals, weddings, a sale, a new phone you want, a trip, school fees. Those are known costs: they belong in sinking funds (Module 3) or goals (Module 2).

### Size it on essential expenses, not income

Your **essential monthly expenses** are what you must pay even in a crisis: needs from your budget, loan EMIs, insurance premiums (as a monthly amount), and the family support you can't stop. Wants are cut in an emergency, so they are left out.

> **Full emergency fund = essential monthly expenses × number of months**

### How many months?

{table(['Your situation', 'Suggested months', 'Why'], [
    ('Permanent salaried job, two incomes in the family', '3 months', 'Income is stable; another earner can help'),
    ('Salaried job, single income, or dependants', '6 months', 'More people rely on one income'),
    ('Freelance, tuition, commission or seasonal income', '6 to 12 months', 'Slow months and gaps between clients are normal'),
    ('Own business, or the only earner in a large family', '9 to 12 months', 'Business shocks can hit income and savings together'),
    ('Student or PSC aspirant with little income', 'Start with 1 month, then 3', 'Small, steady progress matters most'),
])}

These are rules of thumb, not laws. A government job is stable, but illness still costs money; a freelancer with three steady clients is safer than one with a single big client.

### A starter fund first

A full fund can take a year or more to build. So set two targets:

1. **Starter fund:** one month of essential expenses, or a round number like ₹10,000 to ₹25,000. This handles most small shocks. Build it before anything except paying essential bills.
2. **Full fund:** the months from the table. Build it after the starter fund, alongside paying off expensive debt (Module 6).

### Insurance and the emergency fund work together

Health insurance (Module 7) covers big hospital bills; the emergency fund covers what insurance doesn't: co-payments, items not covered, waiting periods, travel and lost income while you recover. Insurance lets your emergency fund be smaller; it doesn't replace it.

### Worked examples (made-up numbers)

- **Anu:** essential expenses {inr(ANU_ESS)}; irregular income, so 6 months = **{inr(ANU_ESS * 6)}**; starter fund **{inr(ANU_ESS)}**.
- **Rahul:** essential expenses {inr(RAHUL_ESS)} (including help to his parents); permanent job, single income, parents depend on him, so 6 months = **{inr(RAHUL_ESS * 6)}**.
- **Fathima:** essential expenses {inr(FATIMA_ESS)}; freelance, so 9 months = **{inr(FATIMA_ESS * 9)}**, plus her separate business buffer from FIN-M03-L04.
""",
    example=f"""
**Rahul** first thought his emergency fund could be small: "It's a government job; the salary will come." Then he listed what had happened in his extended family in the last three years: his father's knee surgery (partly covered by insurance, with ₹38,000 of extras), roof repairs after a heavy monsoon (₹22,000), and his cousin losing a Gulf job and needing help for four months.

None of these was a job loss for Rahul himself, but each one needed money within days. He decided on 6 months of essential expenses, {inr(RAHUL_ESS * 6)}, with a starter fund of {inr(RAHUL_ESS)}. He also noticed something about his old habit: in each of those three events, the family had pledged gold for a loan. "The emergency fund is what lets the gold stay in the locker," his mother said.
""",
    resources=[
        ('ncfe', 'The e-LMS module on safety nets and insurance', '20 minutes'),
    ],
    steps=[
        'From your Budget tab, add up your essential monthly expenses: needs, EMIs, monthly share of insurance premiums and the family support you can\'t stop.',
        'Choose your number of months from the table, and write one sentence on why.',
        'Calculate your starter fund and your full fund.',
        'Make an **Emergency** tab with the template and fill in the target section.',
        'Write your list of what counts as an emergency for you, and what doesn\'t.',
    ],
    proof='A screenshot of the target section of your Emergency tab (essential expenses, months, starter and full targets) and your emergency/not-emergency list, saved in 05 Emergency.',
    templates=[
        ('Emergency tab: targets', """
B2: essential monthly expenses (₹)      (needs + EMIs + premiums/12 + family support you can't stop)
B3: months chosen                        (3, 6, 9 or 12)
B4: full fund target  =B2*B3
B5: starter fund      =B2               (or a round amount)
B6: saved so far (₹)
B7: % of full target  =IF(B4>0,B6/B4*100,0)
B8: starter done?     =IF(B6>=B5,"Yes","Not yet")
""", ''),
        ('my emergency rules', """
IT IS AN EMERGENCY IF: income stops / illness or accident / urgent repair / family crisis / a tool I need for work breaks
IT IS NOT AN EMERGENCY IF: festival / wedding / sale / trip / a gadget I want / a known yearly bill
Before I use it, I ask: is it urgent, necessary and unexpected? All three must be yes.
""", ''),
    ],
    mistakes=[
        ('Sizing it on income instead of essential expenses.', 'In a crisis you cut wants. Size the fund on what you must still pay.'),
        ('Waiting until the full fund is possible.', 'Start with a small starter fund now. ₹5,000 handles many small shocks.'),
        ('Thinking a government job needs no emergency fund.', 'Illness, family crises and repairs don\'t check your job type.'),
        ('Counting gold as the emergency fund.', 'Using gold means a loan or a sale at a bad moment. Keep cash savings for emergencies.'),
    ],
    quiz=[
        {'q': 'Essential expenses are ₹12,000 a month and you choose 6 months. What is the full emergency fund?', 'o': ['₹72,000', '₹12,000', '₹1,44,000', '₹36,000'], 'a': 'A', 'why': '₹12,000 × 6 = ₹72,000.'},
        {'q': 'Which of these is a real emergency?', 'o': ['A hospital bill not covered by insurance', 'Onam shopping', 'A sale on phones', 'A friend\'s wedding gift'], 'a': 'A', 'why': 'Festivals, sales and gifts are known or optional costs, not emergencies.'},
        {'q': 'Who usually needs the most months of expenses saved?', 'o': ['A freelancer or business owner with irregular income', 'A person in a permanent job with two family incomes', 'Everyone needs exactly 3 months', 'Nobody needs an emergency fund with insurance'], 'a': 'A', 'why': 'Irregular income has more gaps and shocks.'},
        {'q': 'Why build a starter fund first?', 'o': ['It handles most small shocks while you build the full fund', 'Banks require it', 'It earns the highest interest', 'It replaces insurance'], 'a': 'A', 'why': 'A small fund now beats a perfect fund someday.'},
    ],
    study='The NCFE module on safety nets and insurance',
    action='Calculate your essential expenses and set starter and full emergency fund targets in the Emergency tab',
)

L2 = lesson(
    M, 2,
    title='Where to keep it and how to build it',
    weeks=(9, 9), hours=1.5,
    outcome='Choose safe, quick-to-reach places for your emergency fund, set up an automatic monthly transfer, and calculate how many months it will take to reach your target.',
    split='20 minutes reading, 20 minutes resources, 50 minutes action',
    core=f"""
### Three rules for where the money waits

1. **Safe:** the amount must not fall. No shares, crypto, chitties or "schemes".
2. **Reachable within a day or two:** emergencies don't wait for an FD to mature.
3. **Separate from spending money:** if it sits in your everyday account, it gets spent.

### A simple three-layer setup

{table(['Layer', 'How much', 'Where', 'Why'], [
    ('1. Cash at home', 'A small amount, say ₹2,000 to ₹5,000', 'Somewhere safe at home', 'For when the network, UPI or ATMs are down, as happens during floods'),
    ('2. Instant money', 'About one month of essential expenses', 'A separate savings account, ideally at a different bank from your spending account, with no card for daily use', 'Reachable today'),
    ('3. The rest', 'The remaining months', 'FDs at banks you trust, in a ladder, within the ₹5 lakh deposit insurance limit per bank', 'A bit more interest; reachable in a day by breaking one FD'),
])}

**An FD ladder** means splitting layer 3 into several smaller FDs with different maturity dates, for example every three months. If you need ₹20,000, you break one small FD, not the whole fund, and pay a small penalty on that one only. When an FD matures and you don't need it, renew it at the end of the ladder.

Some banks offer an **auto-sweep** facility, where money above a limit in your savings account moves into an FD automatically and comes back when needed. Ask your bank whether it offers this and what it costs. Later, once you understand them (Module 9), some people keep part of a large emergency fund in very low-risk mutual funds; that isn't needed to start.

### Where it should not wait

- **Gold jewellery:** you would need a gold loan or a sale. In a real emergency, a gold loan from a bank is still far better than a loan app (Module 6), but it is a fallback, not the plan.
- **A chitty, shares or crypto:** the value or timing isn't in your control.
- **Money lent to friends and relatives:** it may not come back when you need it.
- **A co-operative society beyond what you can afford to have stuck:** see FIN-M04-L01 and FIN-M09-L07.

### How to build it on a small income

- **Automate:** a standing instruction moves a fixed amount to the emergency account the day after income arrives. Start with any amount: ₹500 a month is ₹6,000 a year.
- **Windfalls:** put at least half of every bonus, gift, DA arrears or big client payment into the fund until it is full.
- **One cut:** use one leak from Module 3 (snacks, subscriptions) and send that amount to the fund.
- **Sell what you don't use:** an old phone, books after an exam, unused items.

### How long will it take?

> **Months to target = (target − saved so far) ÷ monthly saving** (ignoring interest)

The spreadsheet function **NPER** includes interest: `=NPER(rate/12, -monthly, -saved, target)`.

**Worked example:** Anu's full target is {inr(ANU_ESS * 6)}; she has ₹6,000 and can save ₹2,500 a month. Without interest: ({inr(ANU_ESS * 6)} − ₹6,000) ÷ ₹2,500 = about **{months_to_target(ANU_ESS * 6, 2500, 0, 6000)} months**. If she puts half of her exam-season extra income (about ₹2,000 a month for four months a year) in too, it drops to about 16 months.

### Using it and refilling it

When you use the fund for a real emergency, don't feel guilty: that is what it is for. Then pause other goals and refill it first, using the same monthly transfer.
""",
    example=f"""
**Fathima** set up her emergency fund like this:

{table(['Layer', 'Amount', 'Where'], [
    ('Cash at home', '₹3,000', 'In a sealed envelope in her cupboard'),
    ('Instant money', '₹20,000', 'A savings account at a second bank, no UPI app linked, net banking only'),
    ('Ladder', '₹40,000 so far', 'Four FDs of ₹10,000 each, maturing every three months'),
])}

Her standing instruction moves ₹4,000 on the 2nd of every month, and her rule from FIN-M03-L04 sends anything above three months of business buffer into the fund. When her laptop failed in July, she broke one ₹10,000 FD, paid a small penalty on its interest, and bought a replacement within a day, without touching her credit card.
""",
    resources=[
        ('dicgc', 'Revise: deposit insurance per bank, to decide how to spread the ladder', '5 minutes'),
        ('indiapost', 'Current deposit rates, if you are considering a post office deposit for part of the fund', '10 minutes'),
        ('ncfe', 'Finish the safety nets and insurance module if you didn\'t in FIN-M05-L01', '15 minutes'),
    ],
    steps=[
        'Decide your three layers: how much in cash, in instant money and in the ladder, and where each one lives.',
        'Choose or open the separate account for instant money (one you don\'t use for daily spending).',
        'Set up a standing instruction for a monthly amount, starting next income day. Any amount counts.',
        'Fill in the build-up section of the Emergency tab and calculate the months to your starter and full targets.',
        'Make your first transfer today, even ₹100.',
        'Write your refill rule: what you pause if you use the fund.',
    ],
    proof='A screenshot of the standing instruction or first transfer (account numbers covered) and the build-up section of your Emergency tab, saved in 05 Emergency.',
    templates=[
        ('Emergency tab: build-up', """
B10: monthly transfer (₹)
B11: interest rate while saving (e.g. 0.065, or 0)
B12: months to starter  =IF(B6>=B5,0,IF(B11=0,ROUNDUP((B5-B6)/B10,0),ROUNDUP(NPER(B11/12,-B10,-B6,B5),0)))
B13: months to full     =IF(B6>=B4,0,IF(B11=0,ROUNDUP((B4-B6)/B10,0),ROUNDUP(NPER(B11/12,-B10,-B6,B4),0)))
Layers:
Layer,Target (₹),Where,Current (₹)
Cash at home,,,
Instant money,,,
FD ladder,,,
""", ''),
        ('FD ladder planner', """
FD,Amount (₹),Opened,Matures,Bank,Rate
1,,,,,
2,,,,,
3,,,,,
4,,,,,
Rule: when one matures and I don't need it, renew it for the longest gap in the ladder.
""", 'csv'),
    ],
    mistakes=[
        ('Keeping the fund in your spending account.', 'It disappears into daily life. Separate account, no daily card.'),
        ('Locking it all in one long FD.', 'Use a ladder so you break only what you need.'),
        ('Investing it for higher returns.', 'Its job is to be there, at full value, on a bad day.'),
        ('Never using it out of guilt, and borrowing instead.', 'Use it for real emergencies, then refill it.'),
    ],
    quiz=[
        {'q': 'What is the main job of an emergency fund?', 'o': ['To be available, at full value, when a shock hits', 'To earn the highest return', 'To save tax', 'To buy gold'], 'a': 'A', 'why': 'Safety and access matter far more than return here.'},
        {'q': 'Why use an FD ladder for part of the fund?', 'o': ['You break only one small FD when you need money', 'It removes all penalties', 'It doubles the interest', 'It is required by RBI'], 'a': 'A', 'why': 'Several small FDs with different dates give flexibility.'},
        {'q': 'Target ₹60,000, saved ₹10,000, saving ₹2,500 a month. Ignoring interest, how many months?', 'o': ['20', '24', '4', '25'], 'a': 'A', 'why': '(60,000 − 10,000) ÷ 2,500 = 20.'},
        {'q': 'Why keep a small amount of cash at home?', 'o': ['For days when the network, UPI or ATMs are down', 'Cash earns interest', 'Banks require it', 'To avoid tax'], 'a': 'A', 'why': 'During floods and outages, digital payments can stop for days.'},
    ],
    study='Deposit insurance per bank, current deposit rates and the NCFE safety nets module',
    action='Set up your emergency fund layers, a monthly standing instruction and your first transfer',
)

LESSONS = [L1, L2]

MODULE = module(
    M,
    title='Emergency fund',
    weeks=(9, 9), hours=4,
    overview="""
Decide how big your emergency fund should be, where it should wait, and start building it this week with an automatic transfer.

An emergency fund is boring and it changes everything. It turns a hospital bill, a lost client or a flooded kitchen from a debt crisis into an inconvenience. It is also what lets you take sensible risks later, because you won't be forced to sell investments or pledge gold at a bad moment.

This module sizes your fund on your real essential expenses from Module 3, sets a starter target and a full target, puts the money in safe places you can reach quickly, and starts the monthly transfer. It is one of the eight parts of your final plan, and your first monthly money review falls this week too.
""",
    outcomes=[
        'Explain what counts as an emergency and what doesn\'t',
        'Calculate essential monthly expenses and choose a starter and a full target',
        'Choose safe, quick-to-reach places for the fund, including an FD ladder',
        'Set up an automatic monthly transfer and calculate months to target',
        'Write rules for using and refilling the fund',
    ],
    lessons=LESSONS,
    project='My emergency fund plan, with the first deposit made',
    project_steps=[
        'Complete the Emergency tab: essential expenses, months, starter and full targets, layers, monthly transfer and months to target.',
        'Write your emergency rules and refill rule at the top of the tab.',
        'Show that the first transfer has happened and the standing instruction is set.',
        'Tell one family member where the fund is and what it is for, so they don\'t treat it as spare money.',
        'Add the emergency fund balance to your Net Worth and Review tabs.',
    ],
    project_proof='Screenshots of the completed Emergency tab and the standing instruction (numbers covered), saved in 05 Emergency.',
    rubric=[
        ('Size', 'A guess', 'Based on income', 'Based on essential expenses and your income stability'),
        ('Targets', 'None', 'One target', 'Starter and full targets with months to reach each'),
        ('Place', 'Spending account', 'Separate but all in one place', 'Layers: cash, instant account and a ladder, within insurance limits'),
        ('Automation', 'None', 'Planned', 'Standing instruction set and first transfer made'),
        ('Rules', 'None', 'In your head', 'Written use and refill rules'),
    ],
    short=[
        'Calculate essential expenses × months (FIN-M05-L01).',
        'Open or choose a separate account and set a monthly standing instruction, any amount (FIN-M05-L02).',
        'Make the first transfer today.',
    ],
    flashcards=[
        ('Emergency fund size', 'Essential monthly expenses × months (3 to 12, depending on how stable your income is).'),
        ('Starter fund', 'About one month of essential expenses, built first.'),
        ('Three rules for where it waits', 'Safe, reachable within a day or two, separate from spending.'),
        ('FD ladder', 'Several small FDs maturing at different times, so you break only what you need.'),
        ('Months to target, no interest', '(Target − saved) ÷ monthly saving.'),
        ('NPER in this course', '=NPER(rate/12, -monthly, -saved, target) gives months to a target with interest.'),
        ('Emergency test', 'Urgent, necessary and unexpected: all three must be yes.'),
    ],
    mistakes=[
        ('Skipping the fund to invest sooner.', 'Without it, the first shock forces you to sell investments or borrow at high interest.'),
        ('Mixing the fund with sinking funds.', 'Known yearly costs have their own sinking funds; the emergency fund is only for shocks.'),
        ('Forgetting to refill after using it.', 'Refill first, then restart other goals.'),
    ],
    project_week=9,
)
