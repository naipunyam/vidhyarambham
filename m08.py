from common import lesson, module

L1 = lesson(
    8, 1,
    title='Bookkeeping and cash flow',
    weeks=(19, 19), hours=5,
    outcome='Keep simple, honest books from day one, with a separate account, a daily cash book, receipts and invoices, and make a 13-week cash flow forecast.',
    split='1 hour 10 minutes study, 3 hours 50 minutes action',
    core="""
### Why keep books from day one

- You can see whether the business really makes money.
- You spot problems early: a supplier's price rise, a customer who never pays.
- Banks and schemes ask for records before they lend.
- Filing tax is easy when records exist, and stressful when they don't.

### Four simple habits

1. **Separate the money.** Use one bank account only for the business. A savings account in your own name is fine at the start; you may need a current account once you register or grow (ask your bank). Take UPI payments into this account only.
2. **Record every rupee, every day.** In the Cashbook tab: date, description, category, money in, money out, payment mode and a receipt link. Cash counts too.
3. **Keep proof.** Photograph every bill and receipt and save it in a Drive folder for that month. Give customers a receipt or invoice for every sale.
4. **Review weekly.** Every Sunday, spend 20 minutes checking that your balance matches the bank and looking at what came in and went out.

### Invoices

An invoice is the bill you give a customer. Include your business name and contact, an invoice number (in order: 001, 002…), the date, the customer's name, what was sold, quantity, price, total, payment received and any balance due. A GST-registered business needs a GST invoice with more details, such as its GSTIN; check the GST portal or ask a tax professional when you get there.

### Cash flow is not profit

**Profit** is revenue minus costs over a period. **Cash flow** is the actual money moving in and out, and when. A profitable business can still run out of cash when:

- customers pay late or buy on credit
- you buy a big stock of ingredients before a festival
- equipment instalments fall due before the season's sales come in

Credit ("pattu" or "kadam") is common in Kerala shops. Set clear rules before you give any: who gets credit, how much and for how long.

### The 13-week cash forecast

For each week: **opening cash + money expected in − money expected out = closing cash.** Plan 13 weeks ahead, about three months. Any week where closing cash falls below zero, or below a small safety amount, is a warning. Chase payments, delay a purchase or ask for advances, before the week arrives.

### Tools

- **Google Sheets** on the phone or laptop, with the templates below.
- **LibreOffice Calc** on the laptop, which works offline.
- **GnuCash**, free and open source, on the laptop only, if you want proper double-entry accounts; its documentation includes a tutorial.

Start simple. A sheet you update every day beats accounting software you open once a month.
""",
    example="""
Nisha's cash book for one week in November:

| Date | Description | Category | In (₹) | Out (₹) | Mode |
| --- | --- | --- | --- | --- | --- |
| 3 Nov | Advance for a chocolate cake (Anju) | Sales | 400 | | UPI |
| 3 Nov | Flour, cocoa, butter, cream | Ingredients | | 1,240 | UPI |
| 4 Nov | Balance for the chocolate cake (Anju) | Sales | 400 | | Cash |
| 5 Nov | Boxes and boards, pack of 20 | Packaging | | 600 | Cash |
| 6 Nov | Two vanilla cakes (a school teacher) | Sales | 1,300 | | UPI |
| 7 Nov | Petrol for deliveries | Delivery | | 200 | Cash |
| 8 Nov | Recharge for the business number | Phone | | 299 | UPI |
| 9 Nov | Red velvet cake (an office party) | Sales | 950 | | UPI |
| | **Total** | | **3,050** | **2,339** | |

Money in minus money out: ₹711 for the week. But the 20 boxes and the big stock of flour will last several weeks, so her real profit for the week is higher than the change in cash. That difference is exactly why she also needs a profit and loss statement (next lesson).

Her 13-week forecast showed a problem in December: about ₹9,000 of Christmas ingredients and boxes had to be bought before most Christmas orders were paid. Her fix: a 50% advance on every Christmas order, collected before she buys the ingredients.
""",
    resources=[
        ('os9', 'Section 9.3 Accounting Basics for Entrepreneurs', '40 min'),
        ('gnucash-docs', 'Optional, laptop only: the first chapters of the Tutorial and Concepts Guide', '30 min'),
        ('ncfe', 'Optional: the e-learning module on money and transactions', '30 min'),
    ],
    steps=[
        'Choose the bank account you will use only for the business, and make sure your UPI QR code pays into it.',
        'Set up the Cashbook tab with the template below. Type your opening balance in H2; in H3 type =H2+D3-E3 and copy it down. Record every transaction for 7 days, including cash, and photograph every receipt into a Drive folder named for the month.',
        'Make an invoice template and give one to every customer this week.',
        'Build your 13-week cash forecast. In J2 type =B2+C2+D2+E2-F2-G2-H2-I2; next week\'s opening cash (B3) is =J2.',
        'Mark any week where cash falls below ₹500 (or your own safety amount), and write down what you will do about it.',
    ],
    proof='Seven days of cash book entries with receipt links, an invoice you sent, and your 13-week forecast with any warning weeks marked.',
    templates=[
        ('cash book (Cashbook tab)', """
Date,Description,Category,Money in (Rs),Money out (Rs),Mode (UPI / cash / bank),Receipt link,Running balance
,Opening balance,,,,,,
""", 'csv'),
        ('invoice', """
INVOICE No. ____             Date: ____
From: [business name], [address], [phone]
To: [customer name], [phone]

Item | Qty | Price (₹) | Amount (₹)
____ | ___ | ________ | _________
____ | ___ | ________ | _________
Total: ₹____
Paid: ₹____ (UPI ref ____ / cash) on ____
Balance due: ₹____ by ____
Thank you!
(Once you are GST-registered, use a GST invoice format.)
""", ''),
        ('13-week cash forecast (paste into Google Sheets)', """
Week starting,Opening cash,In: sales,In: advances,In: other,Out: stock,Out: bills,Out: loan or EMI,Out: other,Closing cash
""", 'csv'),
    ],
    mistakes=[
        ('Mixing personal and business money.', 'Use one account and one UPI QR code for the business only. Pay yourself a fixed amount instead of dipping in.'),
        ('Not recording cash.', 'Cash sales and small purchases are the ones that go missing. Write them down the same day.'),
        ('Giving credit without rules.', 'Decide who can buy on credit, how much and for how long, before anyone asks.'),
        ('Ignoring small fees.', 'Payment fees, recharges and packaging add up. Record them all.'),
        ('Throwing away receipts.', 'A photo in a monthly Drive folder takes five seconds and saves hours at tax time.'),
    ],
    quiz=[
        {'q': 'Why use a separate bank account for the business?',
         'o': ['Banks require it of everyone', 'So you can see what the business earns and spends', 'To avoid tax', 'To get loans faster'],
         'a': 'B', 'why': 'Separate money gives you clear numbers, which also helps with loans and tax.'},
        {'q': 'When can a profitable business still run out of cash?',
         'o': ['When customers pay late or you buy stock before sales come in', 'When prices are high', 'When it has many customers', 'When it keeps records'],
         'a': 'A', 'why': 'Timing matters: money out can come before money in.'},
        {'q': 'Opening cash is ₹2,000, money in ₹5,000 and money out ₹6,500. What is the closing cash?',
         'o': ['₹500', '₹13,500', '₹1,500', '−₹500'],
         'a': 'A', 'why': '₹2,000 + ₹5,000 − ₹6,500 = ₹500.'},
        {'q': 'How should invoice numbers run?',
         'o': ['Randomly', 'In order, without gaps', 'As the customer\'s phone number', 'As the date only'],
         'a': 'B', 'why': 'Numbers in order make records easy to check, for you and for any tax officer.'},
    ],
    study='OpenStax 9.3, plus GnuCash or NCFE if you have time (about 1 hour 10 minutes)',
    action='set up a business account and cash book, record 7 days, send invoices and build a 13-week cash forecast',
)

L2 = lesson(
    8, 2,
    title='Profit and loss, and break-even',
    weeks=(20, 20), hours=3,
    outcome='Prepare a monthly profit and loss statement from your records and calculate your break-even point in units and rupees.',
    split='1 hour 10 minutes study, 1 hour 50 minutes action',
    core="""
### The profit and loss statement (P&L)

A P&L shows whether you made a profit over a period, usually a month:

| Line | What it means |
| --- | --- |
| **Revenue** | All sales in the month (without GST, if you are registered) |
| − **Cost of goods sold** | Variable costs of what you sold: ingredients, packaging, delivery |
| = **Gross profit** | What sales contribute before fixed costs |
| − **Operating expenses** | Fixed costs: phone, rent, subscriptions, equipment, marketing |
| = **Operating profit** | Profit from running the business |
| − **Interest and tax** | Loan interest, and income tax set aside |
| = **Net profit** | What is truly left |

Two adjustments keep your P&L honest:

- **Stock bought for later**, such as a bag of flour that lasts a month, is a cost when you *use* it, not when you buy it. A simple way: at the end of the month, estimate the stock left and subtract it from that month's purchases.
- **Equipment** that lasts years, such as an oven or a ring light, loses value slowly. Spread its cost: a ₹12,000 oven expected to last 4 years costs about ₹250 a month. This is **depreciation**.

**Pay yourself.** If your "profit" exists only because you work for free, it isn't really profit. Always compare net profit with the hours you worked.

### Break-even

The **break-even point** is the level of sales where revenue just covers all costs, so profit is zero.

- **Break-even units = monthly fixed costs ÷ contribution per unit**
- **Break-even revenue = monthly fixed costs ÷ contribution margin**
- **Units for a target profit = (fixed costs + target profit) ÷ contribution per unit**

Then compare with reality. Can you make and sell that many units a month? This is where capacity (your time, your oven, your delivery radius) shows up.

### What-if checks

Try three changes in your sheet: price down 10%, costs up 10% and sales down 20%. If any one of them wipes out your profit, the business is fragile; look for ways to raise the contribution or cut fixed costs.
""",
    example="""
**Nisha's P&L for November** (her home bakery in Kuttiady):

| Line | ₹ |
| --- | --- |
| Revenue (24 cakes at an average of ₹780) | 18,720 |
| Ingredients used | 7,440 |
| Gas and electricity | 840 |
| Packaging | 960 |
| Delivery fuel | 720 |
| **Gross profit** | **8,760** |
| Phone and data | 300 |
| One Instagram boost (a test) | 200 |
| Oven depreciation (₹12,000 over 4 years) | 250 |
| Interest on the oven instalment | 120 |
| **Net profit before tax** | **7,890** |

She worked about 60 hours, so she earned roughly ₹130 an hour.

**Break-even:** her fixed costs are ₹870 a month, and her average contribution is ₹365 a cake (₹8,760 ÷ 24). Break-even = ₹870 ÷ ₹365, so 3 cakes a month. Her goal of ₹15,000 net profit a month needs (₹870 + ₹15,000) ÷ ₹365, which is about 44 cakes a month, or 11 a week.

**Capacity check:** her oven bakes 2 cakes at a time, and each cake takes about 2.5 hours of her time. Eleven cakes a week is about 27 hours, too much next to her family duties. Her options: raise prices, sell more high-margin items such as cupcake boxes, or find a part-time helper for decorating (Module 12).
""",
    resources=[
        ('os9', 'Section 9.4 Developing Startup Financial Statements and Projections', '40 min'),
        ('os9', 'Section 9.1 Overview of Entrepreneurial Finance and Accounting Strategies', '30 min'),
    ],
    steps=[
        'Build last month\'s P&L from your cash book (or this month\'s so far) with the template below.',
        'Adjust for stock bought for later, and add depreciation for any equipment.',
        'Calculate your break-even units and revenue, and the units you need for your target monthly profit.',
        'Do a capacity check: the hours and equipment those units need. Can you do it?',
        'Run the three what-if checks. Choose one change (price, cost or volume) and act on it this week, for example by quoting a new price to a customer or asking a supplier for a bulk rate.',
    ],
    proof='Your P&L, break-even and target calculations, the capacity check, the what-if results and the change you made.',
    templates=[
        ('P&L and break-even (paste into Google Sheets)', """
Line,Amount (Rs)
Revenue,
Cost of goods sold: materials used,
Cost of goods sold: packaging,
Cost of goods sold: delivery,
Cost of goods sold: other variable,
Gross profit,=B2-B3-B4-B5-B6
Operating expenses: phone and internet,
Operating expenses: rent,
Operating expenses: marketing,
Operating expenses: depreciation,
Operating expenses: other fixed,
Operating profit,=B7-B8-B9-B10-B11-B12
Interest,
Tax set aside,
Net profit,=B13-B14-B15
Hours worked this month,
Net profit per hour,=B16/B17
Units sold,
Contribution per unit,=B7/B19
Fixed costs this month,=B8+B9+B10+B11+B12+B14
Break-even units,=B21/B20
Target profit,
Units for target profit,=(B21+B23)/B20
""", 'csv'),
    ],
    mistakes=[
        ('Confusing cash with profit.', 'A good cash week can hide a loss, and a bad one can hide a profit. Use both the cash book and the P&L.'),
        ('Forgetting your own time.', 'Net profit per hour shows whether the business is worth your effort. Work it out every month.'),
        ('Putting a whole stock purchase into one month.', 'Count stock as a cost when you use it, or estimate what is left at month end.'),
        ('Ignoring capacity.', 'A break-even that needs more hours than you have is a warning, not a plan.'),
    ],
    quiz=[
        {'q': 'Revenue ₹20,000, cost of goods sold ₹9,000 and operating expenses ₹3,000. What is the operating profit?',
         'o': ['₹11,000', '₹8,000', '₹17,000', '₹32,000'],
         'a': 'B', 'why': '₹20,000 − ₹9,000 = ₹11,000 gross profit; minus ₹3,000 = ₹8,000.'},
        {'q': 'Fixed costs are ₹2,000 a month and the contribution is ₹250 a unit. How many units to break even?',
         'o': ['4', '8', '250', '2,250'],
         'a': 'B', 'why': '₹2,000 ÷ ₹250 = 8 units.'},
        {'q': 'A ₹24,000 machine lasts 4 years. Roughly how much depreciation is that a month?',
         'o': ['₹500', '₹2,000', '₹6,000', '₹24,000'],
         'a': 'A', 'why': '₹24,000 ÷ 48 months = ₹500.'},
        {'q': 'Your target needs 40 hours a week of work, but you have 6. What does that tell you?',
         'o': ['Work harder', 'The plan doesn\'t fit your capacity: change the price, the product mix or costs, or get help', 'Ignore it', 'Borrow money'],
         'a': 'B', 'why': 'Capacity is a real limit. Change the plan rather than burn out.'},
    ],
    study='OpenStax 9.4 and 9.1 (about 1 hour 10 minutes)',
    action='build a monthly P&L, calculate break-even and target units, check capacity and act on one change',
)

L3 = lesson(
    8, 3,
    title='Tax basics: GST and income tax for small businesses',
    weeks=(20, 20), hours=3,
    outcome='Check whether GST registration applies to you, understand presumptive income tax at a basic level, set up a tax calendar and know when to ask a professional.',
    split='1 hour 10 minutes study, 1 hour 50 minutes action',
    core="""
**Important:** this lesson is general information, checked on 24 October 2026. Tax law changes often: India's new Income-tax Act, 2025 applies to income from 1 April 2026, and GST rules and rates are revised regularly. Before you register, file or decide anything, check the official sources and talk to a chartered accountant or tax practitioner.

### GST: do you need to register?

GST registration depends mainly on your **aggregate turnover** in a financial year (April to March): your total sales, not your profit.

| Your situation in Kerala | Turnover threshold for registration (check current rules) |
| --- | --- |
| You supply only goods | ₹40 lakh a year (a few goods, such as ice cream, pan masala and tobacco, don't get this higher limit) |
| You supply services, or both goods and services | ₹20 lakh a year |

Kerala uses the ₹40 lakh limit for goods because it is not one of the states left out of Notification 10/2019-Central Tax.

**Some businesses must register even below these limits.** The law lists compulsory cases, including certain inter-state supplies of goods and some sales through e-commerce platforms. If you plan to ship goods to other states, or sell on Amazon, Flipkart or Meesho, check the current rules on the GST portal or with a professional before you start.

**If you are not registered, you must not charge GST** or show it on your bills.

**Voluntary registration** is allowed. It can help if your customers are GST-registered businesses that want GST invoices, but it brings regular returns and costs, so don't register "just in case" without advice.

**The composition scheme** is a simpler option for small registered businesses: goods suppliers with turnover up to ₹1.5 crore, and service providers up to ₹50 lakh (at 6% for services), pay tax at a fixed low rate and file less often. They can't charge GST to customers or claim input tax credit (check current rules).

### Income tax: your business income is your income

As a sole proprietor, your business profit is part of your personal income. You file an income tax return (ITR) each year, and the normal slab rates for individuals apply. Even when your income is below the taxable limit, a filed return builds a record that banks and loan schemes often ask for.

**Presumptive taxation, Section 58 of the Income-tax Act, 2025**, is a simpler scheme for small businesses and professionals; it replaced sections 44AD and 44ADA of the old Act. According to the Income Tax Department's pages (check current rules):

- **Eligible businesses** (resident individuals, HUFs and partnership firms other than LLPs) with turnover up to **₹2 crore**, or up to **₹3 crore** if cash receipts are no more than 5% of turnover, can declare profit as **8% of turnover received in cash and 6% of turnover received through banking or digital channels such as UPI**, or more if their real profit is higher.
- **Specified professions** (such as legal, medical, engineering, architecture, accountancy, technical consultancy and interior decoration, plus others listed or notified) with receipts up to **₹50 lakh** (₹75 lakh if cash receipts are no more than 5%) can declare **50%** of receipts as profit.
- Presumptive taxpayers can pay all their advance tax in one instalment by **15 March**.
- If you claim a lower profit than the presumptive rate and your income is above the basic exemption limit, you must keep books and have them audited.

Whether your work counts as a business or as a profession (Arun's setup service or Meera's CV writing, for example) changes the rules, so ask a tax professional.

### Other things to know

- **TDS:** business clients sometimes deduct tax at source before paying you. It isn't lost: it appears in your Annual Information Statement (AIS) on the income tax e-filing portal, and you claim it in your return.
- **Professional tax:** in Kerala, local bodies collect professional tax from people in trades and professions above certain income levels. Ask your panchayat or municipality.
- **Records:** keep your cash book, invoices and receipts for several years.

### When to get professional help

When you approach a GST threshold, when a compulsory case might apply, when you form a partnership, LLP or company, when you hire staff, or whenever you aren't sure. A local tax practitioner's fee is small compared with the cost of a mistake.
""",
    example="""
**Nisha** expects about ₹2.5 lakh of cake sales this year. She supplies only goods, far below the ₹40 lakh threshold, and none of the compulsory cases applies because she sells only locally and directly to customers. She doesn't register for GST and doesn't show GST on her bills. She plans to file an income tax return, using her cash book as the record. Most of her money comes by UPI, so under presumptive taxation the minimum profit she would declare is 6% of her UPI receipts plus 8% of her cash receipts. Her real profit is much higher than that, so she would declare the real figure. Whether she owes any tax depends on her total income and the current slab rates, which she will check with a local tax practitioner before filing.

**Arun** expects about ₹3 lakh this year from setups and care plans, far below the ₹20 lakh threshold for services. One client, a larger GST-registered mobile shop, asked for GST invoices; Arun explained that he isn't registered, and the client accepted a normal invoice. He set a reminder to review GST if his turnover passes ₹15 lakh, and asked a CA whether his work counts as a business or a profession for presumptive tax.
""",
    resources=[
        ('gst-council-32', 'Read the decisions on the threshold and the composition scheme', '10 min'),
        ('gst-notif-10', 'Read the conditions and the list of states left out (Kerala is not on it)', '10 min'),
        ('gst', 'Browse the help topics on registration (check current rules)', '15 min'),
        ('it-58', 'Read the table of who is eligible, the limits and the rates', '15 min'),
        ('it-faq', 'Read the questions on eligibility and advance tax', '20 min'),
    ],
    steps=[
        'Estimate your turnover for the next 12 months, month by month, from your price list and expected sales.',
        'Compare it with the GST threshold for your type of supply, and check the compulsory cases on the GST portal (inter-state supplies, e-commerce sales). Write your answer: register now, not yet, or ask a professional.',
        'Read the presumptive taxation limits. Write down which category you might fall into, and the question you need a professional to answer.',
        'Fill in the tax readiness checklist, and add a tax calendar to Google Calendar: the ITR due date, the advance tax date, and GST dates if you are registered.',
        'Ask one tax practitioner or CA one specific question, by phone or in person. Record the answer and the date.',
    ],
    proof='Your 12-month turnover estimate, your GST decision with reasons, the tax checklist, the calendar entries and the professional\'s answer.',
    templates=[
        ('tax readiness checklist and calendar', """
TAX READINESS CHECKLIST (check current rules on the official sites)
Expected turnover, next 12 months: ₹____
Type of supply: goods only / services / both
GST threshold that applies: ₹____ lakh
Compulsory registration cases that might apply:
[ ] Inter-state supply of goods
[ ] Selling through an e-commerce platform
[ ] Other: ____
GST decision: register now / not yet / ask a professional
If not registered: no GST on my bills [ ]
PAN [ ]   Business bank account [ ]
Income tax: presumptive (Section 58) or regular books? ____
Category: business / specified profession / not sure
Question for my tax professional: ____________
Answer, and the date: ____________

TAX CALENDAR (add to Google Calendar)
Advance tax (presumptive): by 15 March
Income tax return: due date for my category ____
GST returns (if registered): ____
Turnover against the threshold: review every 3 months
""", ''),
    ],
    mistakes=[
        ('Charging "GST" without being registered.', 'It isn\'t allowed. If you aren\'t registered, your bills must not show GST.'),
        ('Watching profit instead of turnover.', 'GST thresholds are about total sales, not profit. Track turnover every month.'),
        ('Missing the compulsory cases.', 'Selling on e-commerce platforms or across state borders can require registration even when you are small. Check before you start.'),
        ('Not filing a return because income is low.', 'A filed return is useful proof of income for loans and schemes. Ask a professional whether you should file.'),
        ('Relying on old rules.', 'Tax rules change. Check the official sources every year, and note the date you checked.'),
    ],
    quiz=[
        {'q': 'What are GST registration thresholds based on?',
         'o': ['Profit', 'Aggregate turnover in a financial year', 'The number of customers', 'Your bank balance'],
         'a': 'B', 'why': 'Total sales count, even if your profit is small.'},
        {'q': 'In Kerala, what is the general threshold for a business that supplies only goods? (Check current rules.)',
         'o': ['₹10 lakh', '₹20 lakh', '₹40 lakh', '₹1 crore'],
         'a': 'C', 'why': 'Kerala uses the ₹40 lakh limit for goods; services have a ₹20 lakh limit.'},
        {'q': 'An unregistered business shows "GST 18%" on its bills. Is that right?',
         'o': ['Yes, always', 'No: an unregistered business must not charge GST', 'Only for cakes', 'Only in December'],
         'a': 'B', 'why': 'Only registered businesses can collect GST.'},
        {'q': 'Under Section 58 presumptive taxation, what is the deemed profit on business turnover received through UPI or banking channels?',
         'o': ['50%', '8%', '6%', '0%'],
         'a': 'C', 'why': '6% for banking and digital receipts and 8% for cash; 50% applies to specified professions.'},
        {'q': 'When should you talk to a tax professional?',
         'o': ['Never', 'When you near a threshold, a compulsory case might apply, you change structure or hire, or you aren\'t sure', 'Only after a notice arrives', 'Only if you earn crores'],
         'a': 'B', 'why': 'A short consultation early is cheaper than fixing a mistake later.'},
    ],
    study='the GST Council decisions, Notification 10/2019, the GST portal\'s registration help and the two Income Tax Department pages (about 1 hour 10 minutes)',
    action='estimate turnover, decide on GST, set a tax calendar and ask a tax professional one question',
)

L4 = lesson(
    8, 4,
    title='Funding: bootstrapping, loans, schemes, grants and investors',
    weeks=(21, 21), hours=4,
    outcome='Choose the right source of money for your stage, find the main government schemes on official sources, and avoid dangerous debt.',
    split='1.5 hours study, 2.5 hours action',
    core="""
Many micro-businesses don't need outside money to start, and this course is designed so that you won't. But when you need equipment or stock to grow, choose carefully: the wrong money can sink a good business.

### The funding ladder

Use the lowest rung that works:

1. **Customers' money:** advances, pre-orders, deposits, subscriptions paid upfront. It is free, and it proves demand.
2. **Bootstrapping:** your profits and your own risk money. Slow, but safe.
3. **Friends and family:** only with a written note of the amount, whether it is a loan or a gift, the repayment dates and what happens if the business fails. Unwritten family loans damage relationships.
4. **Bank loans,** often under government schemes (below).
5. **Grants and competitions:** free money with conditions, mostly for innovation.
6. **Angel investors and venture capital:** money for a share of your company. Only for businesses that can grow very fast; a typical micro-business doesn't need it.

### Government schemes (check current rules)

| Scheme | What it offers | Key points |
| --- | --- | --- |
| **PM Mudra Yojana (PMMY)** | Loans for non-farm micro and small enterprises, through banks, NBFCs and microfinance institutions | Shishu up to ₹50,000; Kishore ₹50,000–₹5 lakh; Tarun ₹5–10 lakh; Tarun Plus ₹10–20 lakh for borrowers who repaid a Tarun loan. MUDRA says it uses no agents or middlemen. |
| **PMEGP** (run through KVIC) | A bank loan with a margin-money subsidy of 15–35% of the project cost, for new units | Project cost up to ₹50 lakh (manufacturing) or ₹20 lakh (business or service); own contribution 10% (5% for special categories); age 18+, Class VIII pass for larger projects; existing units not eligible. Apply on the PMEGP e-portal. |
| **CGTMSE** | Credit guarantees, so lenders can give micro and small enterprises loans without collateral | You apply through your bank; CGTMSE itself doesn't lend. |
| **Stand-Up India** | Bank loans of ₹10 lakh to ₹1 crore for new (greenfield) enterprises | For SC/ST and women entrepreneurs, in manufacturing, services or trading. |
| **Kerala: Margin Money Grant to Nano Units** | A grant for new nano units with a project cost up to ₹10 lakh | 30% of project cost up to ₹3 lakh (40% up to ₹4 lakh for special categories); needs a bank loan of at least 40%; covers manufacturing, food processing, job work and services. Apply through the Taluk Industries Office. |
| **Kerala: Entrepreneur Support Scheme** | Investment support for manufacturing MSMEs | Manufacturing only; service units are not eligible. |
| **KSUM innovation grants** | Grants in stages for innovative startups registered with KSUM | Amounts change between rounds. The Startup India page on Kerala's policy lists up to ₹2 lakh (idea), ₹7 lakh (productisation) and ₹12 lakh (scale-up); check KSUM's grant portal for the current call. |
| **Startup India** | DPIIT recognition, the Seed Fund scheme and more | For eligible registered startups working on innovation. |

Your District Industries Centre (DIC) and Taluk Industries Office help with these schemes, including project reports, and the MSME Clinic at every DIC offers expert advice.

### Debt safety rules

- Borrow only for something that will produce income, and only after you have evidence of demand.
- Make sure the monthly payment (EMI) could be paid from other income if sales are slow for a few months.
- Compare the total cost (interest, processing fees, insurance), not just the EMI.
- Never borrow from private lenders who charge daily or weekly interest ("blade" lenders), never pledge gold to start a business, and never use a loan app you can't confirm is linked to an RBI-regulated lender.
- **Never pay an agent to "get" you a scheme loan or subsidy.** Apply yourself through the official portal, your bank or the DIC.

### Investors: only for fast-growing startups

Angel investors and venture capital funds buy a share of your company in exchange for money. They expect very fast growth and a big exit, which suits a tech startup, not a bakery or a local service. If that is your path, Y Combinator's talk on fundraising and its seed fundraising guide explain how it works, and KSUM runs investor events.
""",
    example="""
Nisha wants a second, larger oven and a stand mixer before next Christmas, about ₹45,000 in all. Her options:

| Option | Cost | Risk |
| --- | --- | --- |
| Christmas advances (50% of about 40 orders) | Free | Low, but the money arrives only when the orders do |
| Savings within her risk limit (₹10,000) | Free | Low |
| A Mudra Shishu loan from her bank (₹25,000) | The bank's interest rate, plus any fees | Medium: the EMI is due even in the monsoon slump |
| A gold loan | Interest, with the family's gold at risk | High |
| A private "blade" lender | Very high interest | Very high |

She chose ₹10,000 of savings, ₹10,000 from advances and a ₹25,000 Mudra Shishu loan, after checking that she could pay the EMI from her part-time salary if sales dropped. She applied directly at her bank's branch with her Udyam certificate, cash book and bank statements, and paid no agent.

Arun needs no loan: his costs are bus fares and data. He is bootstrapping, and will only consider a loan if he hires a helper who needs a laptop.
""",
    resources=[
        ('mudra', 'Read the home page, especially the warning about agents', '10 min'),
        ('pib-tarun', 'Read the loan categories and the Tarun Plus limit', '5 min'),
        ('pmegp-sbi', 'Read the eligibility, project cost and subsidy', '10 min'),
        ('pmegp-portal', 'The official application portal; type the address yourself and check it is the KVIC site', '5 min'),
        ('cgtmse', 'Read what a credit guarantee is, and that it works only through lenders', '10 min'),
        ('standup', 'Read who is eligible', '5 min'),
        ('kerala-nano', 'Read the grant, the funding pattern and how to apply', '10 min'),
        ('kerala-ess', 'Read only if you plan a manufacturing unit', '10 min'),
        ('startupindia-kerala', 'Read the part on KSUM grants', '10 min'),
        ('yc-fund', 'Only if you are building a fast-growing startup', 'about 30 min'),
    ],
    steps=[
        'Write down your funding need: how much, for what, by when, and how it will increase your income.',
        'List at least three ways to fund it from the funding ladder, with the cost and risk of each.',
        'Read the official pages for the one or two schemes that might fit you, and note the eligibility and documents.',
        'Visit or call your bank\'s MSME desk, your Taluk Industries Office or the DIC in Kozhikode, and ask one specific question about one scheme. Record the answer, the person\'s role and the date.',
        'Decide: fund it now (and how), wait until you have more evidence or savings, or don\'t spend it at all.',
    ],
    proof='Your funding need, the options comparison, your notes from the bank or DIC conversation, and your decision.',
    templates=[
        ('funding plan', """
FUNDING PLAN
What I need: ₹____ for ____ by ____
How it increases income: ____________
Evidence of demand: ____________

OPTIONS
Option | Amount | Cost (interest, fees) | Risk | Monthly payment
Customer advances |
Own savings (within my risk limit) |
Family (written note) |
Bank / Mudra / scheme |
Grant |

EMI CHECK
Monthly EMI: ₹____
Could I pay it from other income for 3 slow months? Y / N

SCHEME ENQUIRY
Where: bank MSME desk / Taluk Industries Office / DIC
Person's role: ____  Date: ____
Question: ____________
Answer: ____________
Documents needed: ____________

DECISION: fund now / wait / don't spend
""", ''),
    ],
    mistakes=[
        ('Borrowing before proving demand.', 'A loan for a product nobody has paid for is a bet with borrowed money. Pre-sell first.'),
        ('Starting a business because of a subsidy.', 'A subsidy can\'t save a business without customers. Decide on demand first, then look for support.'),
        ('Paying agents.', 'MUDRA says it has no agents, and Udyam registration is free. Apply yourself through official channels.'),
        ('Looking only at the EMI.', 'Compare the total cost, including fees, and make sure you can pay in a bad month.'),
        ('Giving away equity casually.', 'A share of your company given to a friend for a small amount is hard to undo. Get advice before you offer any.'),
    ],
    quiz=[
        {'q': 'Which is the cheapest source of money for a new micro-business?',
         'o': ['A gold loan', 'Customer advances and pre-orders', 'A blade lender', 'A credit card balance'],
         'a': 'B', 'why': 'It costs nothing and proves that people want what you sell.'},
        {'q': 'What does Mudra\'s Shishu category cover? (Check current rules.)',
         'o': ['Loans up to ₹50,000', 'Loans of ₹5–10 lakh', 'Loans of ₹10–20 lakh', 'Loans above ₹1 crore'],
         'a': 'A', 'why': 'Kishore covers ₹50,000–₹5 lakh, Tarun ₹5–10 lakh and Tarun Plus ₹10–20 lakh.'},
        {'q': 'Someone offers to get you a PMEGP loan for a ₹5,000 "processing fee". What should you do?',
         'o': ['Pay quickly', 'Refuse, and apply yourself through the official portal, your bank or the DIC', 'Pay half now', 'Ask for a receipt and pay'],
         'a': 'B', 'why': 'Scheme applications don\'t need paid agents; such offers are a common scam.'},
        {'q': 'Who is Kerala\'s Entrepreneur Support Scheme for?',
         'o': ['All businesses', 'Manufacturing MSMEs only', 'Service units only', 'Students only'],
         'a': 'B', 'why': 'The scheme page puts service enterprises on its negative list.'},
        {'q': 'Who are venture capital investors a good fit for?',
         'o': ['Most home bakeries', 'Fast-growing, scalable startups', 'Every new business', 'People with a poor credit record'],
         'a': 'B', 'why': 'VCs need very fast growth to make their returns; most small businesses don\'t aim for that.'},
    ],
    study='the official scheme pages for Mudra, PMEGP, CGTMSE, Stand-Up India and Kerala\'s nano-unit grant (about 1.5 hours)',
    action='write your funding need, compare options, ask your bank or DIC about one scheme and decide',
)

LESSONS = [L1, L2, L3, L4]

MODULE = module(
    8,
    title='Money and finance',
    weeks=(19, 21), hours=17,
    overview="""
Money is where many small businesses quietly fail: profit on paper but an empty bank account, sales growing but nobody knows where the money went, a tax question nobody expected. This module gives you the money skills every founder needs: simple books, a cash forecast, a profit and loss statement, break-even, beginner-level GST and income tax, and safe ways to fund growth.

You don't need to become an accountant. You need to record every rupee, look at the numbers every week, and know when to ask a professional.
""",
    outcomes=[
        'Keep a daily cash book with receipts and invoices, separate from your personal money',
        'Make a 13-week cash flow forecast and see a cash crunch coming before it arrives',
        'Prepare a monthly profit and loss statement and calculate break-even',
        'Explain when GST registration applies and how presumptive income tax works, and keep a tax calendar',
        'Choose funding that fits your stage, from customer advances to Mudra and Kerala schemes, and avoid dangerous debt',
    ],
    lessons=LESSONS,
    project='Finance sheet',
    project_steps=[
        'Your cash book with 4 weeks of entries and receipts (L01).',
        'Your 13-week cash forecast (L01).',
        'Your monthly P&L and break-even calculations (L02).',
        'Your tax readiness checklist and tax calendar (L03).',
        'Your funding plan with the options compared (L04).',
        'Review it with someone who keeps accounts (a CA, an accountant friend or a shopkeeper who files GST) and note their comments.',
    ],
    project_proof='Your finance sheet (one Google Sheets file with these tabs) in Founder Toolkit/08 Money, with the reviewer\'s comments.',
    rubric=[
        ('Records', 'Mixed with personal money', 'Recorded, with gaps', 'Every rupee for 4 weeks, receipts saved, separate account'),
        ('Cash forecast', 'None', 'One month ahead', '13 weeks ahead, updated weekly'),
        ('P&L and break-even', 'None', 'Revenue only', 'A full monthly P&L, break-even and target units'),
        ('Tax', 'Unaware', 'Know GST exists', 'Threshold and compulsory cases checked, calendar set, a professional asked'),
        ('Funding', 'Borrow when short', 'Options listed', 'Options compared on cost and risk, using official sources'),
    ],
    short=[
        'L01: record every transaction for 2 weeks and skip the forecast for now.',
        'L02: a P&L for one month and break-even units only.',
        'L03: check the GST threshold and the compulsory cases.',
        'L04: write your funding need and two options.',
    ],
    mistakes=[
        ('Mixing personal and business money.', 'Use one account and one QR code for the business.'),
        ('Confusing profit with cash.', 'Keep both a cash book and a P&L, and look at both.'),
        ('Borrowing before demand is proven.', 'Fund growth from customers\' money first.'),
    ],
)
