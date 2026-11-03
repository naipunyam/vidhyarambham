"""Module 3: Budgeting."""
from common import lesson, module, link, fence, table, inr

M = 3

ANU_30 = [
    ('Food and groceries', 2650, 'Need'),
    ('Eating out and snacks', 1980, 'Want'),
    ('Transport and fuel', 1120, 'Need'),
    ('Phone and internet', 399, 'Need'),
    ('Health and medicines', 860, 'Need'),
    ('Education and PSC', 1240, 'Need'),
    ('Clothes and personal care', 1450, 'Want'),
    ('Family support', 2500, 'Need'),
    ('Gifts, functions and festivals', 1000, 'Want'),
    ('Subscriptions and apps', 448, 'Want'),
    ('Other', 610, 'Want'),
]
ANU_TOTAL = sum(v for _, v, _ in ANU_30)
ANU_WANTS = sum(v for _, v, t in ANU_30 if t == 'Want')

L1 = lesson(
    M, 1,
    title='Read your 30 days: where the money really went',
    weeks=(5, 5), hours=2,
    outcome='Turn your 30-day log into a category summary with formulas, find your three biggest leaks, and list the yearly costs a 30-day log misses.',
    split='20 minutes reading, 20 minutes resources, 80 minutes action',
    core=f"""
Your 30-day log is finished (or nearly). It is the most honest picture of your money you have ever had. This lesson turns 30 days of rows into answers.

### Step 1: totals by category

A **category summary** adds up every category with one formula per row. In a new area of the Expenses tab (or a new tab called **Summary**), list your categories and use SUMIF:

{fence('=SUMIF(Expenses!C2:C500, A2, Expenses!B2:B500)')}

This means: in the Expenses tab, find rows where column C (category) matches the category written in A2, and add their amounts from column B. Add a **share** column (category ÷ total × 100) and a **count** column with COUNTIF to see how often you spend in each category.

### Step 2: three questions

1. **What are my three biggest categories?** These are where any real change happens. Cutting a ₹200 category by half saves ₹100; cutting a ₹3,000 category by a third saves ₹1,000.
2. **Where are the leaks?** A leak is frequent, small and unplanned: snacks, delivery, small app purchases, impulse UPI payments. COUNTIF finds them: a category with 40 payments a month is a habit, not an event.
3. **How far was my guess?** Compare the real total with the guess in your Baseline money snapshot. Most people underestimate by 20% or more. The gap is not a failure; it is why we log.

### Step 3: what 30 days misses

Some costs come once or twice a year, so a 30-day log may not show them. These are the costs that "suddenly" break budgets. List them now and divide each by 12 to get a monthly amount. Common ones in Kerala:

- Insurance premiums: health, vehicle, life
- School or college fees, books and uniforms when schools reopen in June
- Onam, Vishu, Christmas, Eid and other festival spending, including gifts and new clothes
- Weddings, house-warmings and other functions: gifts and travel
- Vehicle servicing, repairs and the yearly insurance renewal
- House repairs, often before or after the monsoon
- Property tax, annual subscriptions, gadget replacement

You will turn these into **sinking funds** in the next lesson: small monthly savings for known future bills.

### Step 4: a daily average

> **Daily average = 30-day total ÷ 30**

It is a simple number to watch in future months without a full log: if your average day costs ₹420, a ₹1,000 day stands out.

### What not to do with the results

Don't start cutting everything tomorrow. The goal of this lesson is to **see**. You decide what to change with a method in FIN-M03-L02, so the changes stick.
""",
    example=f"""
**Anu's** 30 days, summarised with SUMIF (she earned about ₹14,000 that month):

{table(['Category', 'Total', 'Share', 'Type'], [(c, inr(v), f'{v / ANU_TOTAL * 100:.0f}%', t) for c, v, t in ANU_30] + [('**Total**', f'**{inr(ANU_TOTAL)}**', '100%', '')])}

Her guess in week 0 had been ₹9,500; the real total was {inr(ANU_TOTAL)}. Her wants came to {inr(ANU_WANTS)}, about {ANU_WANTS / ANU_TOTAL * 100:.0f}% of spending.

Her three findings: **eating out and snacks** had 31 separate payments, almost all tea and snacks with friends after tuition, about ₹64 a day; **clothes** were one sale purchase (the earrings from Module 1) plus a kurta for a cousin's wedding; and the **subscriptions** were two video apps she rarely opened. Her yearly-costs list added another ₹1,850 a month: her share of the family health insurance premium, Onam, two weddings she already knew about, and her bus pass renewal.
""",
    resources=[
        ('ncfe', 'Revise the managing income and expenditure module and try the budget calculator if the site offers it', '20 minutes'),
    ],
    steps=[
        'Check the log is complete for 30 days. Fill gaps from your UPI history and note any days you are unsure about.',
        'Build the category summary with the template formulas: total, share and count for each category.',
        'Write your three biggest categories and your three biggest leaks.',
        'Compare the 30-day total with your week 0 guess and write the difference in rupees and percent.',
        'List every yearly or irregular cost you can think of, with its amount and month, and divide each by 12.',
        'Calculate your daily average.',
    ],
    proof='A screenshot of your category summary, your three biggest leaks, the guess-versus-real comparison and your yearly-costs list, saved in 03 Budget.',
    templates=[
        ('category summary (Summary tab, categories in A2:A16)', """
A: Category | B: Total (₹) | C: Share % | D: Number of payments | E: Average payment
B2: =SUMIF(Expenses!C$2:C$500,A2,Expenses!B$2:B$500)
C2: =IF(B$17>0,B2/B$17*100,0)
D2: =COUNTIF(Expenses!C$2:C$500,A2)
E2: =IF(D2>0,B2/D2,0)
Copy row 2 down to row 16.
B17: =SUM(B2:B16)          (total)
B18: =B17/30               (daily average)
B19: your week 0 guess     B20: =B17-B19 (difference)   B21: =IF(B19>0,B20/B19*100,0) (% off)
""", ''),
        ('yearly costs list', """
Cost,Amount (₹),Month it comes,Monthly amount (=Amount/12)
Health insurance premium,,,
Vehicle insurance and service,,,
School or college fees and books,,,
Onam and other festivals,,,
Weddings and functions (gifts and travel),,,
House repairs,,,
Other,,,
Total monthly amount for sinking funds:,,,=SUM(D2:D8)
""", 'csv'),
    ],
    mistakes=[
        ('Judging the month as "good" or "bad".', 'It is data. The only bad log is an incomplete one.'),
        ('Cutting small categories first.', 'Start with the biggest three; that is where real money is.'),
        ('Forgetting yearly costs.', 'They are certain, just not monthly. Without sinking funds they arrive as "emergencies".'),
        ('Category names typed differently.', '"Food" and "food " (with a space) are different to SUMIF. Use the same words every time.'),
    ],
    quiz=[
        {'q': 'What does =SUMIF(Expenses!C2:C500, A2, Expenses!B2:B500) do?', 'o': ['Adds amounts in column B where the category matches A2', 'Counts the number of rows', 'Adds all amounts in the sheet', 'Finds the largest amount'], 'a': 'A', 'why': 'SUMIF adds the values whose category equals the one in A2.'},
        {'q': 'A category has 31 payments in 30 days, mostly small. What is it most likely to be?', 'o': ['A leak: a frequent, small habit worth looking at', 'A one-time emergency', 'A sinking fund', 'An investment'], 'a': 'A', 'why': 'High frequency of small, unplanned spends is the classic leak pattern.'},
        {'q': 'Why list yearly costs after a 30-day log?', 'o': ['A 30-day log can miss bills that come once or twice a year', 'They are tax-deductible', 'Banks require the list', 'They are always wants'], 'a': 'A', 'why': 'Premiums, fees and festivals are certain but not monthly; dividing by 12 makes them plannable.'},
        {'q': 'Your 30 days total ₹12,600. What is your daily average?', 'o': ['₹420', '₹126', '₹1,260', '₹42'], 'a': 'A', 'why': '₹12,600 ÷ 30 = ₹420.'},
    ],
    study='The NCFE income and expenditure module (revision) and its budget calculator',
    action='Summarise your 30-day log by category with formulas, find three leaks and list your yearly costs',
)

L2 = lesson(
    M, 2,
    title='Budget methods: 50/30/20, zero-based and envelopes',
    weeks=(5, 5), hours=1.5,
    outcome='Compare the three main budgeting methods, adapt one to your income, and plan sinking funds for yearly costs.',
    split='25 minutes reading, 15 minutes resources, 50 minutes action',
    core=f"""
A budget is a **plan for money before it arrives**. Tracking (what you did in 30 days) looks back; budgeting looks forward. There are three main methods. All work; the best one is the one you will actually follow.

### Method 1: 50/30/20

Split take-home income into three buckets: **50% needs, 30% wants, 20% savings and debt payoff**.

- **Good for:** beginners and steady incomes. Only three numbers to watch.
- **Adapt it:** on a small income, needs may take 60–70%. Then try **70/20/10** or **60/20/20** and move towards 20% savings as income grows. On a high income, try 40/20/40.
- **Watch out:** it hides detail. "Wants 30%" can still hide a leak.

**Worked example:** Rahul takes home ₹30,000. 50/30/20 gives needs ₹15,000, wants ₹9,000, savings ₹6,000. His real needs are ₹12,400 (Module 1), so needs are fine; his wants were ₹14,600 including the upgraded phone, so that bucket must shrink.

### Method 2: zero-based budget

Give **every rupee a job** until income minus all planned amounts equals zero. Savings and goals are jobs too.

> **Income − (needs + sinking funds + savings + debt payments + wants) = 0**

- **Good for:** tight budgets, people paying off debt, anyone who wants full control.
- **Watch out:** it takes 30–60 minutes a month to plan, and you must adjust when life changes. Keep a small "miscellaneous" line so one surprise doesn't break it.

### Method 3: envelopes

The traditional method: cash in labelled envelopes ("groceries ₹3,000", "bus ₹1,100"). When an envelope is empty, spending in that category stops. Today you can do this digitally:

- A **second savings account** or a separate pocket in your bank app for wants, so your main account holds only needs money
- **Recurring deposits** or a separate account for sinking funds, so festival money isn't spent in August
- Cash envelopes for the categories where you overspend most, such as snacks

- **Good for:** people whose leaks are in one or two categories, and households sharing money.
- **Watch out:** too many accounts become confusing. Two or three "envelopes" are enough.

### Pay yourself first, whichever method

On the day income arrives, move savings and sinking-fund money out **first**, using a standing instruction or a recurring deposit, and live on the rest. This one habit beats present bias (Module 1).

### Sinking funds: yearly costs, saved monthly

Take your yearly-costs list from FIN-M03-L01. Each item gets a monthly amount, saved into one separate account or RD. When Onam or the insurance renewal arrives, the money is waiting. Example: a ₹9,600 yearly health premium becomes ₹800 a month.

### Choosing

{table(['If you…', 'Try'], [
    ('Want something simple and have steady income', '50/30/20, adapted to your income'),
    ('Are paying off debt or living on a very tight income', 'Zero-based'),
    ('Overspend in one or two categories', 'Envelopes for those categories, with 50/30/20 or zero-based for the rest'),
    ('Have irregular income', 'Zero-based, using the method in FIN-M03-L04'),
])}
""",
    example=f"""
**Anu** chose a **zero-based budget with two envelopes**, because her income is small and irregular and her leaks were snacks and clothes. Her plan for a ₹14,000 month:

{table(['Job', 'Amount'], [
    ('Family support (to her mother on the 1st)', '₹2,500'),
    ('Needs: food share, bus, phone, medicines, PSC materials', '₹6,200'),
    ('Sinking funds RD (health premium share, Onam, weddings, bus pass)', '₹1,850'),
    ('Starter emergency fund (standing instruction on the 2nd)', '₹1,500'),
    ('Wants envelope: snacks and outings, in cash, ₹300 a week', '₹1,200'),
    ('Wants: clothes and personal care', '₹500'),
    ('Miscellaneous', '₹250'),
    ('**Total**', '**₹14,000**'),
])}

Income minus jobs = ₹0. In a month when tuition brings in ₹18,000, the extra ₹4,000 goes to her emergency fund until it reaches its target. The cash envelope works because when the week's ₹300 is gone, she drinks tea at home, and she says she doesn't miss it as much as she expected.
""",
    resources=[
        ('ncfe', 'The NCFE financial calculators: try the budget or savings calculator with your own numbers', '15 minutes'),
    ],
    steps=[
        'Read your category summary and yearly-costs list from FIN-M03-L01.',
        'Choose one method (or a mix) using the table, and write one sentence on why it fits you.',
        'Draft next month\'s plan on paper or in a note: every category with an amount, using your chosen method. For zero-based, income minus plan must be ₹0.',
        'Set up your sinking-fund place: a recurring deposit or a separate account, and the monthly amount.',
        'If you chose envelopes, set them up: cash envelopes or a second account for wants.',
        'Set up one pay-yourself-first standing instruction for the day after income usually arrives (even ₹200 is fine to start).',
    ],
    proof='Your written plan for next month (method, categories, amounts, total = income for zero-based) and a screenshot of the standing instruction or RD set up (cover account numbers), saved in 03 Budget.',
    templates=[
        ('50/30/20 calculator', """
A2: take-home income (₹)
B2: needs %   (0.5, or 0.6 / 0.7 on a small income)
C2: wants %   (0.3 or 0.2)
D2: savings % =1-B2-C2
E2: needs ₹   =A2*B2
F2: wants ₹   =A2*C2
G2: savings ₹ =A2*D2
""", ''),
        ('zero-based plan', """
Income this month: ₹____
1. Family support:          ₹____
2. Needs (list them):       ₹____
3. Debt payments:           ₹____
4. Sinking funds:           ₹____
5. Emergency fund / goals:  ₹____
6. Wants (with envelopes):  ₹____
7. Miscellaneous:           ₹____
Income minus all jobs = ₹0?  ____
""", ''),
    ],
    mistakes=[
        ('Copying 50/30/20 when needs are 65% of income.', 'Adapt the percentages to your reality, then improve them over time.'),
        ('No wants in the budget.', 'A budget with no fun breaks in weeks. Plan your wants on purpose.'),
        ('Saving "whatever is left".', 'Usually nothing is left. Pay yourself first, by standing instruction.'),
        ('Too many envelopes.', 'Two or three envelopes are manageable; ten accounts become a mess.'),
    ],
    quiz=[
        {'q': 'Take-home income ₹30,000. Under 50/30/20, how much goes to savings and debt payoff?', 'o': ['₹6,000', '₹9,000', '₹15,000', '₹3,000'], 'a': 'A', 'why': '20% of ₹30,000 = ₹6,000.'},
        {'q': 'What is the rule of a zero-based budget?', 'o': ['Income minus all planned jobs, including savings, equals zero', 'You spend nothing', 'You save zero', 'You only track expenses'], 'a': 'A', 'why': 'Every rupee is given a job before the month starts.'},
        {'q': 'A ₹9,600 yearly health premium as a sinking fund needs how much a month?', 'o': ['₹800', '₹960', '₹96', '₹9,600'], 'a': 'A', 'why': '₹9,600 ÷ 12 = ₹800.'},
        {'q': 'What does "pay yourself first" mean?', 'o': ['Move savings out on the day income arrives, then live on the rest', 'Buy yourself a gift every month', 'Pay your loans last', 'Spend first and save what is left'], 'a': 'A', 'why': 'It puts saving before spending, so it actually happens.'},
    ],
    study='The NCFE calculators, used with your own numbers',
    action='Choose a budget method, draft next month\'s plan and set up sinking funds and one pay-yourself-first transfer',
)

L3 = lesson(
    M, 3,
    title='Your budget sheet: formulas, alerts and tools',
    weeks=(6, 6), hours=2.5,
    outcome='Build a Budget tab that compares planned and actual spending by formula, flags overspending automatically, and fits a 10-minute weekly check.',
    split='20 minutes reading, 30 minutes resources, 100 minutes action',
    core=f"""
Your plan from FIN-M03-L02 becomes a **Budget tab** that fills itself in from the Expenses tab. You type each payment once in Expenses; the Budget tab does the adding.

### The layout

{table(['Column', 'What it holds', 'Formula (row 4)'], [
    ('A: Category', 'The same category names as the Expenses tab', '(typed)'),
    ('B: Type', 'Need, Want, Saving, Debt or Sinking', '(typed)'),
    ('C: Planned', 'This month\'s planned amount', '(typed)'),
    ('D: Actual', 'Spent this month so far', '=SUMIFS(Expenses!$B$2:$B$1000,Expenses!$C$2:$C$1000,A4,Expenses!$A$2:$A$1000,">="&$B$1,Expenses!$A$2:$A$1000,"<"&$D$1)'),
    ('E: Left', 'Planned minus actual', '=C4-D4'),
    ('F: % used', 'How much of the plan is gone', '=IF(C4>0,D4/C4*100,0)'),
    ('G: Status', 'A word you can see at a glance', '=IF(D4>C4,"OVER",IF(D4>0.8*C4,"Careful","OK"))'),
])}

Cell **B1** holds the first day of this month and **D1** the first day of next month, typed as `=DATE(2026,12,1)` and `=DATE(2027,1,1)`, so changing two dates resets the whole tab for a new month. The `$` signs keep ranges fixed when you copy the formula down.

### Totals and the zero check

- Total planned: `=SUM(C4:C20)`; total actual: `=SUM(D4:D20)`
- Income for the month in a cell, say C22, and the zero-based check: `=C22-SUM(C4:C20)` should show 0.
- Savings rate this month: `=SUMIF(B4:B20,"Saving",D4:D20)/C22*100`

### Colour alerts

Both Google Sheets and LibreOffice Calc have **conditional formatting** (in the Format menu): make the Status cell red when it says OVER and orange for Careful. Colour gets your attention faster than numbers.

### The 10-minute weekly check

Every Sunday: log any missing payments, open the Budget tab, look at the Status column. For anything at "Careful", decide now: slow down, or move money from another category (in zero-based, a move keeps the total at zero). Don't wait for the month to end.

### Tools: what to use

- **Google Sheets** on the phone: the course's default; works offline once set up for offline use, syncs with the laptop.
- **{link('libreoffice', 'LibreOffice Calc')}** on the laptop: free and open source; opens .xlsx files. Remember the separator note in Week 0 ({link('lo-separators', 'formula options')}).
- **{link('gnucash', 'GnuCash')}**: free, open-source double-entry accounting for Windows, macOS and Linux, with bank, investment and scheduled-transaction features. Useful later if your finances or freelance work grow complicated; overkill for most beginners.
- **Your bank app's spending analysis:** helpful for a quick look, but it can't see cash or other banks.
- **Budgeting apps that read your SMS:** some ask for permission to read all your messages, including bank alerts and OTPs. Think carefully before allowing that; this course doesn't need any such app.

### When a month goes over budget

It will happen. Ask: was the plan unrealistic (change the plan) or was it a one-off (absorb it from miscellaneous or wants)? Two months over in the same category means the plan is wrong, not you.
""",
    example=f"""
**Rahul** built his Budget tab on his laptop in LibreOffice Calc, then moved it to Google Sheets so he could check it on his phone. His formulas showed an error in LibreOffice at first; changing the commas to semicolons fixed it, and Google Sheets accepted the commas again after he uploaded the file.

Mid-month, his Status column showed:

{table(['Category', 'Planned', 'Actual', 'Status'], [
    ('Food and groceries', '₹4,000', '₹2,150', 'OK'),
    ('Eating out and snacks', '₹2,000', '₹1,780', 'Careful'),
    ('Clothes and personal care', '₹800', '₹1,250', 'OVER'),
    ('Family support', '₹5,000', '₹5,000', 'Careful (fully paid, as planned)'),
])}

The OVER was a shirt for a colleague's wedding. He moved ₹450 from his miscellaneous line, and with "Careful" on eating out, he skipped one restaurant dinner that week. At month end he was within ₹200 of his plan, and he noticed the Sunday check took eight minutes.
""",
    resources=[
        ('lo-separators', 'Formula options: how LibreOffice separates the parts of a formula', '5 minutes'),
        ('gnucash', 'What GnuCash does, to know when you might need it', '10 minutes'),
        ('libreoffice', 'Download and install LibreOffice on the laptop if you want to work offline', '15 minutes'),
    ],
    steps=[
        'Make a **Budget** tab with the template. Type your categories and planned amounts from your plan in FIN-M03-L02.',
        'Enter the month\'s first day in B1 and the next month\'s first day in D1. Copy the Actual, Left, % used and Status formulas down.',
        'Add totals, the zero check and the savings rate formula.',
        'Add conditional formatting so OVER shows red and Careful orange.',
        'Test it: add a test payment in Expenses, check that Budget updates, then delete the test row.',
        'Put a 10-minute weekly check in your calendar for every Sunday.',
    ],
    proof='A screenshot of your Budget tab with working formulas, totals and colour alerts for the current month, saved in 03 Budget.',
    templates=[
        ('Budget tab', """
A1: Month starts   B1: =DATE(2026,12,1)   C1: Next month starts   D1: =DATE(2027,1,1)
(Change the two dates each month. DATE avoids confusion between day/month orders.)
Row 3 headings: Category,Type,Planned,Actual,Left,% used,Status
Row 4 formulas (copy down to row 20):
D4: =SUMIFS(Expenses!$B$2:$B$1000,Expenses!$C$2:$C$1000,A4,Expenses!$A$2:$A$1000,">="&$B$1,Expenses!$A$2:$A$1000,"<"&$D$1)
E4: =C4-D4
F4: =IF(C4>0,D4/C4*100,0)
G4: =IF(D4>C4,"OVER",IF(D4>0.8*C4,"Careful","OK"))
Row 21: Totals   C21: =SUM(C4:C20)   D21: =SUM(D4:D20)
Row 22: Income this month   C22: (type it)
Row 23: Zero check          C23: =C22-C21
Row 24: Savings rate %      C24: =IF(C22>0,SUMIF(B4:B20,"Saving",D4:D20)/C22*100,0)
In LibreOffice: if a formula shows an error, use ; instead of , and click the other sheet's cells instead of typing Expenses!
""", ''),
        ('weekly check', """
SUNDAY MONEY CHECK (10 minutes)
[ ] Log any missing payments (check UPI history and wallet)
[ ] Look at the Status column: any OVER or Careful?
[ ] Decide: slow down, or move money from: ____ to: ____
[ ] One sentence in the note: what I learned this week
""", ''),
    ],
    mistakes=[
        ('Typing actual amounts by hand into the Budget tab.', 'Let SUMIFS do it from Expenses; typing twice creates errors.'),
        ('Forgetting the $ signs.', 'Without them, ranges shift when you copy the formula down and totals go wrong.'),
        ('Checking only at month end.', 'By then it is too late to change anything. The Sunday check is where budgets succeed.'),
        ('Giving apps access to all your SMS.', 'Your messages include OTPs and bank alerts. A spreadsheet does the job without that risk.'),
    ],
    quiz=[
        {'q': 'Why does the Budget tab use SUMIFS with dates in B1 and D1?', 'o': ['So each month\'s actual spending is added automatically for each category', 'To calculate interest', 'To count categories', 'Because SUM doesn\'t work'], 'a': 'A', 'why': 'SUMIFS adds a category\'s payments between the month\'s start and the next month\'s start.'},
        {'q': 'Planned ₹2,000, actual ₹1,780. What does the status formula show?', 'o': ['Careful', 'OK', 'OVER', 'Error'], 'a': 'A', 'why': '₹1,780 is more than 80% of ₹2,000 (₹1,600) but not over it.'},
        {'q': 'A formula copied from this course shows an error in LibreOffice. What should you try first?', 'o': ['Replace commas with semicolons', 'Delete the sheet', 'Buy a budgeting app', 'Switch off the laptop'], 'a': 'A', 'why': 'LibreOffice may be set to use semicolons as separators.'},
        {'q': 'What is the main risk of budgeting apps that read all your SMS?', 'o': ['They can see bank alerts and OTPs', 'They make spreadsheets slower', 'They change your tax regime', 'There is no risk'], 'a': 'A', 'why': 'Your messages hold sensitive financial information; share it only if you truly need to.'},
    ],
    study='LibreOffice formula separators, the GnuCash overview and (optionally) installing LibreOffice',
    action='Build a Budget tab with SUMIFS formulas, totals, a zero check and colour alerts, and schedule the weekly check',
)

# ---- irregular income example (made up)
F_PAY = 45000
F_TAX = 0.10
F_BIZ = 0.10
F_SPLIT = [
    ('Tax reserve (10%, an assumption until Module 10)', F_PAY * F_TAX),
    ('Business costs (software, internet share, 10%)', F_PAY * F_BIZ),
    ('To the holding account (the rest)', F_PAY * (1 - F_TAX - F_BIZ)),
]

L4 = lesson(
    M, 4,
    title='Budgeting an irregular income',
    weeks=(6, 6), hours=2,
    outcome='Build a budget that survives slow months by paying yourself a fixed salary from a holding account, with tax and business money set aside from every payment.',
    split='25 minutes reading, 25 minutes resources, 70 minutes action',
    core=f"""
Freelancers, tutors, commission agents, farmers, small shop owners and people waiting for their first job all face the same problem: **bills are regular, income isn't**. A normal budget breaks in the first slow month. This lesson gives you a system that works even if you have no income yet: you can set it up now and use it the day income starts.

### The core idea: pay yourself a salary

1. **All income goes into one holding account** (a separate savings account), never straight into spending.
2. **Every payment is split** the day it arrives: tax reserve, business costs, then the rest into holding.
3. **On the 1st of each month, you pay yourself a fixed "salary"** from holding to your spending account. The salary is your **baseline budget**: what you need to live on, based on your lowest normal month, not your best.
4. **When holding has more than 3 months of salary,** the extra goes to your goals.

Good months fill the holding account; slow months draw it down; your life sees the same salary either way.

### Step 1: the baseline budget

From your 30-day log and cash-flow history, list the **minimum** you need each month: needs, debt payments, sinking funds and a small amount for wants. This is the salary you pay yourself. If your average income is well above it, you can raise the salary later.

### Step 2: percentages for every payment

Decide fixed percentages so you don't think each time:

- **Tax reserve:** income tax isn't deducted from most freelance payments the way it is from a salary, and some clients deduct TDS (tax deducted at source) that you claim back when filing. Set aside a percentage until you calculate your real tax in Module 10. On a small income your tax may be zero under the new regime (FIN-M10-L02), but keep the habit.
- **Business costs:** software, data, travel, equipment.
- **GST:** if your turnover grows past the registration limit, GST you collect is not your money at all (FIN-M10-L05).

### Step 3: the buffer

The holding account needs a starting buffer. Aim for one month of salary first, then three. This **is not** your emergency fund (Module 5); the buffer covers normal slow months, the emergency fund covers shocks such as illness or a lost laptop.

### If income is seasonal

Tuition peaks before exams; some agriculture pays at harvest; tourism peaks in certain months. Look at 12 months of income, plan your salary on the yearly total ÷ 12 (minus a safety margin), and expect the holding account to rise and fall with the seasons.

### For a business

Keep business and personal money in separate accounts, and pay yourself a salary from business profit. Bookkeeping, profit and cash flow for a business are covered in the Entrepreneurship course (ENT-M08-L01 and ENT-M08-L02); this lesson covers your personal side.
""",
    example=f"""
**Fathima's** lowest normal month in the last year was ₹12,000 and her average ₹32,000. Her baseline budget (needs, her loan EMI, sinking funds and modest wants) is ₹20,000. She opened a second savings account as her holding account.

When a client pays {inr(F_PAY)}, she splits it the same day:

{table(['Where', 'Amount'], [(w, inr(a)) for w, a in F_SPLIT])}

On the 1st of every month she transfers ₹20,000 from holding to her spending account. Over six months: her income varied from ₹12,000 to ₹55,000, but her spending account received ₹20,000 every month. By the sixth month the holding account held ₹38,000 above her salaries, almost two months of buffer. When it passes ₹60,000 (three months), the extra goes to her goals.

She found two side benefits: she stopped "celebrating" big payments with spending (mental accounting, Module 1), and at tax time the reserve was waiting.
""",
    resources=[
        ('it-s58', 'Skim what "presumptive taxation" means for small businesses and professionals; you study it properly in FIN-M10-L05', '10 minutes'),
        ('cbic-reg', 'Read when GST registration becomes necessary, to know the limit exists', '10 minutes'),
        ('ncfe', 'Revise the income and expenditure module with irregular income in mind', '15 minutes'),
    ],
    steps=[
        'From your log and cash-flow history, calculate your baseline budget: the minimum monthly amount you need. Write the list.',
        'Look at your income for as many months as you have. Write your lowest normal month and your average.',
        'Choose your split percentages for each payment: tax reserve, business costs and holding.',
        'Decide your holding account: a separate savings account (open one only if you have income to manage; otherwise write which account you would use).',
        'Fill in the holding-account tracker in the template with your last three months, or with planned numbers if your income starts later.',
        'Write your rule for extra money above three months of salary.',
        'No income yet? Do steps 1, 3 and 6 with the income you expect from your first job or freelance work, and set a reminder to switch the plan on when the first payment arrives.',
    ],
    proof='Your irregular-income plan (baseline budget, lowest and average income, split percentages, holding account and the tracker), saved in 03 Budget.',
    templates=[
        ('payment split calculator', """
A2: payment received (₹)
B2: tax reserve %          (e.g. 0.10)
C2: business costs %       (e.g. 0.10)
D2: tax reserve ₹          =A2*B2
E2: business costs ₹       =A2*C2
F2: to holding account ₹   =A2-D2-E2
""", ''),
        ('holding account tracker', """
Month,Income received,Tax reserve,Business costs,Into holding,Salary paid to me,Holding balance,Months of buffer
(row 2) ,,,,=B2-C2-D2,,=E2-F2,=IF(F2>0,G2/F2,0)
(row 3) ,,,,=B3-C3-D3,,=G2+E3-F3,=IF(F3>0,G3/F3,0)
Rule: when months of buffer > 3, move the extra to: ____
""", 'csv'),
    ],
    mistakes=[
        ('Budgeting on the best month.', 'Plan on the lowest normal month. Good months then become progress, not lifestyle.'),
        ('Spending client money as it arrives.', 'Everything goes to holding first; your life runs on the salary.'),
        ('No tax reserve.', 'Tax on a year\'s freelance income can be a shock in July. Set aside from every payment.'),
        ('Mixing the buffer and the emergency fund.', 'The buffer smooths normal slow months; the emergency fund is for shocks. Keep both.'),
    ],
    quiz=[
        {'q': 'In the salary system, where does all freelance income go first?', 'o': ['A holding account', 'The spending account', 'An investment', 'Cash at home'], 'a': 'A', 'why': 'Holding receives everything; you pay yourself a fixed salary from it.'},
        {'q': 'What should the monthly salary be based on?', 'o': ['Your baseline budget, from your lowest normal month', 'Your best month', 'Your friend\'s income', 'Last month\'s income'], 'a': 'A', 'why': 'A salary you can pay even in slow months keeps the system stable.'},
        {'q': 'A ₹30,000 payment, with a 10% tax reserve and 10% business costs. How much goes to holding?', 'o': ['₹24,000', '₹27,000', '₹30,000', '₹21,000'], 'a': 'A', 'why': '₹30,000 − ₹3,000 − ₹3,000 = ₹24,000.'},
        {'q': 'How is the buffer different from the emergency fund?', 'o': ['The buffer covers normal slow months; the emergency fund covers shocks', 'They are the same', 'The buffer is invested in shares', 'The emergency fund pays your tax'], 'a': 'A', 'why': 'Slow months are expected; illness or a lost laptop are shocks.'},
    ],
    study='The idea of presumptive taxation (section 58), when GST registration applies, and the NCFE income module',
    action='Write your irregular-income plan: baseline budget, split percentages, holding account and tracker',
)

LESSONS = [L1, L2, L3, L4]

MODULE = module(
    M,
    title='Budgeting',
    weeks=(5, 6), hours=9,
    overview="""
Turn your 30-day log into a budget you will actually keep: a method that fits you, a formula-driven sheet, sinking funds for yearly costs, and a system for irregular income.

Your 30-day expense log ends in week 5. This module reads it, chooses a budgeting method that fits your income and personality, and builds a **Budget tab** that updates itself from the Expenses tab, with colour alerts when a category runs hot. Yearly costs such as insurance, fees and festivals become **sinking funds**, so they stop arriving as emergencies.

If your income is irregular, or will be (freelancing, tuition, a business), the last lesson gives you the salary system: a holding account, fixed splits for tax and costs, and a monthly salary to yourself. By the end of week 6 your budget system is running, and it becomes one of the eight parts of your final plan.
""",
    outcomes=[
        'Summarise 30 days of spending by category with SUMIF and COUNTIF',
        'Choose and adapt 50/30/20, zero-based or envelope budgeting',
        'Plan sinking funds for yearly costs',
        'Build a Budget tab with planned vs actual, a zero check and colour alerts',
        'Run an irregular income through a holding account and a fixed monthly salary',
    ],
    lessons=LESSONS,
    project='My budget system',
    project_steps=[
        'Write one page (or a note at the top of the Budget tab) describing your system: the method, your categories, your sinking funds, your pay-yourself-first transfer and, if relevant, your irregular-income salary.',
        'Make sure next month\'s Budget tab is ready, with planned amounts that add up to your income.',
        'Check that the standing instruction or RD for savings and sinking funds is set up.',
        'Do one complete Sunday check and write what you changed.',
        'At the end of the month, add a row to the Review tab: planned vs actual and one decision.',
    ],
    project_proof='The one-page system description and a screenshot of next month\'s Budget tab with working formulas, saved in 03 Budget.',
    rubric=[
        ('30-day data', 'Log incomplete', 'Log complete, not summarised', 'Summarised by category, with leaks and yearly costs listed'),
        ('Method', 'None chosen', 'Chosen, not adapted', 'Chosen and adapted to your income, with a reason'),
        ('Budget tab', 'No formulas', 'Some formulas', 'SUMIFS actuals, zero check and colour alerts all working'),
        ('Automation', 'None', 'Planned, not set up', 'Pay-yourself-first and sinking funds set up'),
        ('Irregular income', 'Not considered', 'Partly planned', 'Salary system planned (or ready for when income starts)'),
    ],
    short=[
        'Category summary of your 30 days with SUMIF (FIN-M03-L01, step 2).',
        'A 50/30/20 split of your income (FIN-M03-L02 template).',
        'One standing instruction for savings, even ₹200.',
        'A Budget tab with planned and actual for your three biggest categories only.',
    ],
    flashcards=[
        ('50/30/20', '50% needs, 30% wants, 20% savings and debt payoff, adapted to your income.'),
        ('Zero-based budget', 'Income minus every planned job, including savings, equals zero.'),
        ('Envelope method', 'A fixed amount per category in cash or a separate account; when it\'s empty, spending stops.'),
        ('Sinking fund', 'Monthly saving for a known yearly cost: yearly cost ÷ 12.'),
        ('Pay yourself first', 'Move savings out the day income arrives, then live on the rest.'),
        ('Holding account', 'For irregular income: everything comes in here, and you pay yourself a fixed salary from it.'),
        ('Status formula', '=IF(D4>C4,"OVER",IF(D4>0.8*C4,"Careful","OK"))'),
    ],
    mistakes=[
        ('A budget that is never checked.', 'The weekly 10-minute check is the budget. Without it, the sheet is decoration.'),
        ('A perfect budget in month one.', 'Expect two or three months of adjusting before the plan matches reality.'),
        ('Treating yearly costs as emergencies.', 'Festivals, premiums and fees are certain. Sinking funds make them painless.'),
    ],
    project_week=6,
)
