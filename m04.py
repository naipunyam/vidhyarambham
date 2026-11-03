"""Module 4: Banking and payments."""
from common import lesson, module, link, fence, table, inr, ASOF, CHECK

M = 4


def fd_maturity(p, rate, years, per_year=4):
    return p * (1 + rate / per_year) ** (per_year * years)


L1 = lesson(
    M, 1,
    title='Bank accounts and KYC: the right account, kept clean',
    weeks=(7, 7), hours=1.5,
    outcome='List every account you hold, know which type each one is and what it costs, and keep your KYC, contact details and deposit insurance limits in order.',
    split='25 minutes reading, 25 minutes resources, 40 minutes action',
    core=f"""
Many people in Kerala have three or four bank accounts: one from school, one for a scholarship, one for salary, one at the co-operative bank near home. Some charge fees for low balances, some have old phone numbers, some have no nominee. This lesson cleans them up.

### Types of accounts

{table(['Account', 'What it is for', 'Watch out for'], [
    ('Savings account', 'Everyday money; earns a little interest', 'Minimum balance rules and charges vary by bank'),
    ('Basic savings bank deposit (BSBD)', 'A savings account with no minimum balance', 'Some limits on free withdrawals; see below'),
    ('Salary account', 'Opened by your employer for salary credit', 'Its terms may change if salary stops coming; ask the bank'),
    ('Current account', 'Business payments, many transactions', 'Usually no interest; higher balance rules'),
    ('Joint account', 'Shared with a spouse or parent', 'How it can be operated after a death (Module 13)'),
    ('Post office savings account', 'Small savings, linked to post office schemes', 'Interest 4% a year, as of November 2026'),
])}

### The basic savings account (BSBD)

RBI expanded the free services of BSBD accounts in December 2025 ({link('ml-bsbd', 'Moneylife, December 2025')}): **no minimum balance and no initial deposit**; free deposits; **at least four free withdrawals a month**, with digital payments not counted in that limit; an ATM or debit card with no annual fee; 25 cheque leaves a year; internet and mobile banking; and a passbook or statement. You can ask your bank to **convert an existing savings account into a BSBD account**, which it must do within 7 days of your request. {CHECK.capitalize()} with your bank.

If you keep a low balance and pay mostly by UPI, a BSBD account can end minimum-balance charges completely.

### KYC: Know Your Customer

Banks must verify who you are (identity) and where you live (address), usually with Aadhaar, PAN, a voter ID or a passport. Some points:

- **Re-KYC:** banks ask you to update KYC from time to time. A genuine request comes through your branch, the bank's official app or its official website, never through a link in an SMS from an unknown number.
- **Central KYC Registry (CKYC):** your KYC record can be shared between financial institutions, so you don't repeat it everywhere. RBI chose "KYC: Your First Step to Safe Banking" as the theme of Financial Literacy Week 2026 ({link('rbi-fe', 'RBI Financial Education')}).
- **PAN** is needed for many transactions and for income tax; keep it linked to Aadhaar.
- **Your mobile number and email** must be current in every account. Fraud alerts and OTPs go there; an old number is a security hole.

### Deposit insurance: the ₹5 lakh rule

Deposits in banks are insured by the DICGC (a subsidiary of RBI) **up to ₹5 lakh per depositor per bank, including principal and interest** ({link('dicgc', 'DICGC flyer')}). It covers commercial banks, small finance banks, payments banks, regional rural banks and co-operative banks registered with DICGC. If a bank fails, insured deposits are paid back up to that limit. Accounts in different branches of the same bank count together.

So **keep no more than about ₹5 lakh in any one bank**, counting all your accounts and FDs there, if safety matters to you. Co-operative **societies** that are not licensed banks are **not** covered by DICGC; RBI has warned that some of them wrongly use the word "bank" ({link('rbi-coop', 'RBI, November 2021')}). Kerala has its own guarantee scheme for co-operative society deposits (FIN-M09-L07).

### Account hygiene

- Close accounts you don't need, after moving any balance and linked payments.
- An account with no transactions for a long time can become inoperative, and very old unclaimed balances are moved to an RBI fund; you can still claim them (FIN-M13-L02).
- Check the charges in your last six months of statements: SMS charges, minimum-balance penalties, card fees.
""",
    example=f"""
**Anu** found four accounts in her name:

{table(['Account', 'Status', 'Problem', 'Action'], [
    ('Bank A savings, opened for a school scholarship', 'Active, old mobile number', '₹1,180 in minimum-balance charges over 6 months', 'Converted to BSBD at the branch; updated mobile number'),
    ('Bank B savings, her main tuition account', 'Active', 'No nominee', 'Added a nominee (Module 13 explains the new rules)'),
    ('Post office savings', 'Rarely used', 'None', 'Kept, for a future post office RD'),
    ('Co-operative society deposit account her father opened', '₹4,000', 'Not a licensed bank; no DICGC cover', 'Kept small; will review in FIN-M09-L07'),
])}

The conversion took one visit and a written request. The bank's charges stopped from the next month, saving her more than ₹2,000 a year, which she moved straight into her emergency fund.
""",
    resources=[
        ('ml-bsbd', 'What a BSBD account must offer free, and the 7-day conversion rule', '10 minutes'),
        ('dicgc', 'What deposit insurance covers, the ₹5 lakh limit and which banks are covered', '10 minutes'),
        ('rbi-coop', 'Why some co-operative societies are not banks, and what that means for your deposit', '5 minutes'),
        ('rbi-fe', 'The Financial Literacy Week 2026 KYC material in Downloads', '10 minutes'),
    ],
    steps=[
        'List every account in your name: banks, post office, co-operative banks and societies, payments banks, wallets. Ask family if you are unsure about old accounts.',
        'Make an **Accounts** tab with the template. Use only the last four digits of each account number.',
        'For each account, check in the app or passbook: mobile number, email, nominee, KYC status and charges in the last six months.',
        'Add up deposits in each bank to check the ₹5 lakh insurance limit (most people are far below it; note it anyway).',
        'Choose one clean-up action and do it this week: convert to BSBD, update a mobile number, add a nominee, or start closing an unused account.',
    ],
    proof='A screenshot of your Accounts tab (last four digits only) and proof of one clean-up action, such as an acknowledgement or a screenshot of the updated details, saved in 04 Banking.',
    templates=[
        ('Accounts tab', """
Institution,Type (savings / BSBD / salary / current / joint / post office / co-op bank / co-op society / wallet),Last 4 digits,Insured by DICGC? (Yes/No/Check),Balance (₹),Mobile number current?,Email current?,Nominee?,KYC up to date?,Charges in last 6 months (₹),Keep / convert / close,Action date
""", 'csv'),
        ('formula: total in one bank (insurance check)', """
=SUMIF(A2:A20,"Bank A",E2:E20)     (add FDs in that bank too)
Over ₹5,00,000 in one bank? Consider spreading deposits.
""", ''),
    ],
    mistakes=[
        ('Ignoring small charges.', '₹200 a month in penalties is ₹2,400 a year. Ask for a BSBD conversion or move to an account that suits your balance.'),
        ('Old mobile numbers on accounts.', 'Fraud alerts go to that number. Update it in every account.'),
        ('Updating KYC through an SMS link.', 'Use only the branch, the official app or the bank\'s own website.'),
        ('Treating a co-operative society like a bank.', 'Not every society is a licensed bank, and DICGC cover depends on that. Check before depositing.'),
    ],
    quiz=[
        {'q': 'What is the DICGC deposit insurance limit, as of November 2026?', 'o': ['₹5 lakh per depositor per bank, including interest', '₹1 lakh per account', 'Unlimited', '₹5 lakh per branch'], 'a': 'A', 'why': 'It is ₹5 lakh per depositor per bank, with all branches of the bank counted together.'},
        {'q': 'Which is true of a BSBD account after RBI\'s December 2025 changes?', 'o': ['No minimum balance, and at least four free withdrawals a month, not counting digital payments', 'A ₹10,000 minimum balance', 'No ATM card allowed', 'No internet banking'], 'a': 'A', 'why': 'BSBD accounts must offer these basic services free.'},
        {'q': 'You get an SMS: "Your KYC expires today, update here: [link]". What should you do?', 'o': ['Ignore the link and check through the branch or official app', 'Click quickly before the account is blocked', 'Reply with your Aadhaar number', 'Forward it to friends'], 'a': 'A', 'why': 'Genuine KYC updates come through official channels; SMS links like this are a common fraud.'},
        {'q': 'Your deposit is in a co-operative credit society that isn\'t a licensed bank. Is it covered by DICGC?', 'o': ['No', 'Yes, up to ₹5 lakh', 'Yes, unlimited', 'Only the interest'], 'a': 'A', 'why': 'RBI has said DICGC cover is not available for deposits in such societies.'},
    ],
    study='BSBD rules, DICGC deposit insurance, RBI\'s caution on co-operative societies and the KYC material',
    action='Build your Accounts tab and complete one clean-up action',
)

L2 = lesson(
    M, 2,
    title='UPI, cards and net banking: using them safely',
    weeks=(7, 7), hours=2,
    outcome='Use UPI, cards and net banking with safe habits, know your rights when money is taken without your permission, and have a written plan for the first hour after a fraud.',
    split='25 minutes reading, 30 minutes resources, 65 minutes action',
    core=f"""
UPI made payments in India fast and free. It also made fraud fast. Almost every payment fraud works by tricking **you** into approving a payment or sharing a code; the technology itself is rarely broken. So safety is mostly a set of habits.

### Five UPI facts that stop most frauds

1. **Your UPI PIN is only for paying money out.** You never need it to receive money. Anyone who says "enter your PIN to receive the refund" is a fraudster.
2. **Scanning a QR code is for paying.** A QR code never brings money in.
3. **A "collect request" asks you to pay.** Read every request before approving it; decline anything you didn't expect.
4. **Never share OTPs, PINs or passwords,** and never install a screen-sharing app because a caller asks you to. Banks, RBI, the police and courier companies never ask.
5. **Check the name before you pay.** UPI shows the registered name of the receiver. If it doesn't match who you think you are paying, stop.

### Cards and net banking

- Use your bank's app or type the bank's address yourself; don't search for it and click an ad. Banks in India moved their websites to addresses ending in **.bank.in**, which only regulated banks can use; RBI asked banks to complete the move by 31 October 2025 ({link('bs-bankin', 'Business Standard, April 2025')}).
- Use the card controls in your bank app: turn off international and online use when you don't need them, and set limits.
- Keep SMS and email alerts on, and read them. An alert you ignore is a fraud you discover late.
- Don't save cards on websites you rarely use.

### Your rights: the RBI liability rules

RBI's rules ({link('rbi-liability', 'RBI, July 2017')}, {CHECK}) decide who pays when money leaves your account without your permission:

{table(['Situation', 'Your liability'], [
    ('The bank\'s fault (its system, staff or fraud)', 'Zero, whether or not you reported it'),
    ('A third party\'s fraud (not you, not the bank), reported within 3 working days of the alert', 'Zero'),
    ('Same, reported in 4 to 7 working days', 'Limited: up to ₹5,000 for BSBD accounts, ₹10,000 for other savings accounts and credit cards with limits up to ₹5 lakh, ₹25,000 for others (or the transaction amount, if lower)'),
    ('You were negligent, for example you shared your OTP or PIN', 'You bear the loss until you report it; the bank covers losses after your report'),
])}

The bank must credit the disputed amount to your account (a "shadow reversal") within 10 working days of your report and resolve the complaint within 90 days. The lesson is simple: **report within hours, not days.**

### The first hour after a fraud

1. **Call 1930,** the national cyber crime helpline, available 24 hours ({link('kp-1930', 'Kerala Police')}). Fast reporting gives police the best chance to freeze the money in the fraudster's account.
2. **Block** your card or UPI through the bank app or the bank's official helpline, and report the transaction to the bank.
3. **Report online** on the National Cyber Crime Reporting Portal, {link('cybercrime', 'cybercrime.gov.in')}, and keep the acknowledgement number.
4. **Write to your bank** with the details and keep a copy. If the bank rejects your complaint or doesn't reply within 30 days, complain free to the RBI Ombudsman at cms.rbi.org.in under the Integrated Ombudsman Scheme, 2026, which can award up to ₹30 lakh for loss plus up to ₹3 lakh for harassment ({link('rbi-ios', 'scheme features')}, {CHECK}).
""",
    example=f"""
**Joseph**, Anu's 66-year-old neighbour, received an SMS: "Dear consumer, your electricity will be disconnected tonight at 9.30 pm as your last bill was not updated. Call this number immediately." The caller was polite, said he was "from the electricity office", and asked Joseph to install an app "to update the bill" and pay ₹10.

Joseph's daughter had shown him Anu's fraud response card a month earlier. Two things stopped him: the caller wanted him to install an app (screen sharing), and the message created **urgency**. He hung up, checked his bill in the official way, and found nothing was due.

Anu then helped him set up three safety habits: SMS alerts on every transaction, a daily UPI limit lower than his pension, and the fraud response card stuck inside his kitchen cupboard, with 1930 written in large numbers.
""",
    resources=[
        ('rbi-liability', 'The customer liability table and the timelines (3 days, 4 to 7 days, shadow credit in 10 days)', '20 minutes'),
        ('kp-1930', 'What the 1930 helpline and the reporting portal are for', '5 minutes'),
        ('rbi-ios', 'How to complain to the RBI Ombudsman, and when', '15 minutes'),
        ('bs-bankin', 'Why bank websites now end in .bank.in (headline)', '2 minutes'),
    ],
    steps=[
        'In your bank app, turn on SMS and email alerts for every transaction if they aren\'t on already.',
        'Open the card controls: turn off international use, and online use if you don\'t shop online. Set a daily limit that fits your spending.',
        'Check your UPI app: remove linked accounts you don\'t use, and check your UPI ID and the name it shows.',
        'Save your bank\'s official helpline number in your contacts, from the bank\'s own website or passbook.',
        'Fill in the fraud response card from the template, print it or save it as a photo, and share it with one family member.',
        'Do the 10-question payment safety check with a family member and talk through any "no" answers.',
    ],
    proof='Screenshots of transaction alerts on and card controls set (cover card numbers), and your fraud response card, saved in 04 Banking.',
    templates=[
        ('fraud response card', """
IF MONEY GOES WITHOUT MY PERMISSION, IN THE FIRST HOUR:
1. Call 1930 (national cyber crime helpline, 24 hours)
2. Block card/UPI in the bank app, or call my bank: ____ (official number)
3. Report at cybercrime.gov.in and write down the acknowledgement number
4. Email/visit my bank in writing; keep a copy
5. If no reply in 30 days or rejected: RBI Ombudsman, cms.rbi.org.in (free)
NEVER: share OTP, PIN or password; install an app because a caller asks; scan a QR code to receive money
""", ''),
        ('10-question payment safety check', """
1. Transaction alerts on for every account?                        Yes / No
2. Mobile number current in every account?                        Yes / No
3. Card controls set (international off, limits)?                 Yes / No
4. Do I know my UPI PIN is never needed to receive money?         Yes / No
5. Do I check the receiver's name before paying?                  Yes / No
6. Bank's official helpline saved from the official site?         Yes / No
7. Do I open the bank website by typing its .bank.in address?     Yes / No
8. Screen lock and app lock on the phone?                         Yes / No
9. Would I hang up on a caller asking for an OTP, even "from the bank"? Yes / No
10. Does my family know about 1930?                               Yes / No
""", ''),
    ],
    mistakes=[
        ('Thinking "I am too smart to be fooled".', 'Fraudsters use urgency, fear and authority; educated people lose money every day. Habits protect you when you are tired or scared.'),
        ('Waiting to report "in case it comes back".', 'Your liability depends on how fast you report. Report within hours.'),
        ('Searching for "customer care" numbers online.', 'Fake numbers appear in search results and ads. Use the number on the bank\'s own website, app or passbook.'),
        ('Keeping alerts off to avoid "too many messages".', 'Alerts are how you catch fraud in minutes instead of weeks.'),
    ],
    quiz=[
        {'q': 'Someone says you must enter your UPI PIN to receive a refund. What is true?', 'o': ['You never need a UPI PIN to receive money; it is a fraud', 'You need the PIN for refunds above ₹1,000', 'Only for refunds from banks', 'Only on weekends'], 'a': 'A', 'why': 'The UPI PIN only authorises payments going out of your account.'},
        {'q': 'A third party steals money from your savings account and you report it on the same day. Your liability under RBI rules?', 'o': ['Zero', '₹10,000', 'The full amount', '₹25,000'], 'a': 'A', 'why': 'Third-party fraud reported within 3 working days means zero liability.'},
        {'q': 'What is 1930?', 'o': ['The national cyber crime helpline', 'RBI\'s head office number', 'A bank\'s customer care', 'The income tax helpline'], 'a': 'A', 'why': 'It is the 24-hour helpline for reporting cyber and financial fraud.'},
        {'q': 'Your bank rejected your fraud complaint. Where can you complain next, free?', 'o': ['The RBI Ombudsman at cms.rbi.org.in', 'A loan app', 'Social media only', 'Nowhere'], 'a': 'A', 'why': 'The Integrated Ombudsman Scheme handles complaints after the bank rejects them or doesn\'t reply in 30 days.'},
        {'q': 'What is the safest way to open your bank\'s website?', 'o': ['Type its official address, which ends in .bank.in', 'Click the first search ad', 'Use a link from an SMS', 'Ask a caller for the link'], 'a': 'A', 'why': 'Ads and SMS links can lead to fake sites; .bank.in is reserved for banks.'},
    ],
    study='RBI\'s customer liability rules, the 1930 helpline, the RBI Ombudsman scheme and the .bank.in change',
    action='Turn on alerts and card controls, fill in your fraud response card and do the safety check with family',
)

FD_P = 50000
FD_R = 0.07
FD_N = 3
FD_M = fd_maturity(FD_P, FD_R, FD_N)

L3 = lesson(
    M, 3,
    title='FDs, RDs and where to park money',
    weeks=(8, 8), hours=2,
    outcome='Calculate the maturity value of an FD and an RD, compare banks and post office deposits on rate, safety, tax and penalties, and choose where short-term money should wait.',
    split='25 minutes reading, 25 minutes resources, 70 minutes action',
    core=f"""
Money you need within about three years, such as your emergency fund, sinking funds and short goals, should be **safe and easy to reach**, not chasing high returns. Fixed and recurring deposits are the usual home for it.

### Fixed deposits (FDs)

You deposit a lump sum for a fixed period at a fixed rate.

- **Rates differ** by bank, tenure and type of depositor (senior citizens usually get more). Small finance banks often pay more than large banks; their deposits have the same DICGC cover up to ₹5 lakh.
- **Cumulative FD:** interest is added to the deposit, usually every quarter, and paid at maturity. **Payout FD:** interest is paid monthly or quarterly, useful for retirees like Joseph and Mary.
- **Breaking an FD early** usually costs a penalty on the interest. Check the bank's rule before you deposit.
- **Tax:** FD interest is added to your income and taxed at your slab rate. Banks deduct TDS when your interest from that bank crosses a yearly limit, ₹50,000 for most people and higher for senior citizens ({link('fb26-notes', 'Finance Bill 2026 notes')}, {CHECK}). If your total income is below the taxable limit, you can give the bank a self-declaration so it doesn't deduct TDS (known as Form 15G, or 15H for seniors, under the old law; ask the bank for the current form).

**Worked example: cumulative FD with quarterly compounding**

> Maturity = deposit × (1 + rate ÷ 4) ^ (4 × years)

{inr(FD_P)} for {FD_N} years at {FD_R * 100:.0f}% a year: {inr(FD_P)} × (1 + 0.07/4)^12 = **{inr(FD_M)}**, so interest of {inr(FD_M - FD_P)}. Simple interest would have given {inr(FD_P * FD_R * FD_N)}; the extra {inr(FD_M - FD_P - FD_P * FD_R * FD_N)} is compounding.

### Recurring deposits (RDs)

You deposit a fixed amount every month for a fixed period; the bank pays interest on each instalment. RDs suit **sinking funds and goals**: ₹1,000 a month for a festival, a premium or a two-wheeler down payment. A post office RD runs for 5 years and paid **6.7%** a year in October to December 2026 ({link('indiapost', 'India Post')}, {CHECK}). Bank RDs come in many lengths.

### Post office time deposits

Post office time deposits (TDs) of 1, 2, 3 and 5 years paid **6.9% to 7.5%** in October to December 2026, set by the government every quarter ({link('small-rates', 'quarterly rates')}, {CHECK}). They are backed by the Government of India. FIN-M09-L03 covers all the small savings schemes.

### Where should money wait?

{table(['When you need it', 'Where it can wait', 'Why'], [
    ('This month', 'Savings account', 'Instant access'),
    ('In 1 to 12 months', 'FD or RD in a bank you trust, or a post office deposit', 'Safe, a bit more interest, small penalty if broken'),
    ('In 1 to 3 years', 'FDs, RDs, post office deposits; Module 9 adds other options', 'Safety still matters more than return'),
    ('More than 3 to 5 years away', 'Module 9: a mix that can beat inflation', 'Time to recover from ups and downs'),
])}

### Comparing deposits

Compare four things, not just the rate: **safety** (bank type, DICGC cover, how much you already have there), **rate** for your exact tenure, **flexibility** (penalty for early withdrawal), and **tax** (interest is taxed at your slab; post-tax return is what you keep).
""",
    example=f"""
**Joseph and Mary**, the retired couple next door, kept ₹8 lakh in one FD at a co-operative society because "the secretary is from our church and the rate is half a percent higher". Anu showed them two things: a co-operative society that is not a licensed bank has no DICGC cover ({link('rbi-coop', 'RBI caution')}), and even at a bank, cover is ₹5 lakh per depositor per bank.

They decided, together with their son, to move the deposit at maturity: ₹4 lakh in an FD in Joseph's name at one bank, ₹3 lakh in Mary's name at another, and ₹1 lakh in a post office time deposit, with monthly interest payouts for their expenses. Their interest fell by about ₹1,500 a year. In exchange, every rupee was within deposit insurance or backed by the government. "We sleep better," Mary said.
""",
    resources=[
        ('indiapost', 'Current post office interest rates for RD, TD and the other schemes', '10 minutes'),
        ('small-rates', 'The October to December 2026 small savings rates table', '5 minutes'),
        ('dicgc', 'Revise what deposit insurance covers', '5 minutes'),
        ('fb26-notes', 'Optional: the clause on TDS on interest (search the PDF for "interest")', '10 minutes'),
    ],
    steps=[
        'Pick a deposit amount and period that fits one of your short goals or sinking funds.',
        'Find the current rate for that period at three places: your own bank, one other bank, and the post office (rates are on their official websites or at the branch).',
        'Fill in the deposit comparison template with rate, maturity value (by formula), penalty rule, deposit insurance or government backing, and tax note.',
        'Decide where your sinking funds and emergency fund money will wait. Write one sentence for each.',
        'Optional, only if you have the money and it fits your plan: open the RD or FD you chose. ₹100 to ₹500 is enough to learn the steps.',
    ],
    proof='Your filled-in deposit comparison with formulas and your one-sentence decisions (and a screenshot of any deposit opened, numbers covered), saved in 04 Banking.',
    templates=[
        ('deposit comparison (formulas work in both apps)', """
Row 1: Where,Type (FD/RD/post office TD),Rate (e.g. 0.07),Years,Deposit or monthly amount (₹),Maturity value (₹),Interest earned (₹),Early-withdrawal penalty,Insured or govt-backed?,Notes
FD, quarterly compounding (row 2):  F2: =E2*(1+C2/4)^(4*D2)        G2: =F2-E2
RD, approximate value with monthly deposits (row 3):  F3: =FV(C3/12,D3*12,-E3,0,1)   G3: =F3-E3*D3*12
(Banks compound RD interest quarterly, so their maturity figure may differ slightly from this FV approximation; use the bank's calculator to confirm.)
""", ''),
    ],
    mistakes=[
        ('Choosing only on the highest rate.', 'Half a percent extra is worth little if the deposit isn\'t insured or you can\'t withdraw it in an emergency.'),
        ('Putting more than ₹5 lakh in one bank without thinking.', 'Spread larger amounts across banks or government schemes if safety matters to you.'),
        ('Forgetting tax on interest.', 'FD interest is taxed at your slab. Compare what you keep, not just the rate.'),
        ('Locking emergency money in long FDs.', 'Use shorter deposits or a ladder (Module 5) so you can reach it without big penalties.'),
    ],
    quiz=[
        {'q': '₹50,000 in a 3-year FD at 7% compounded quarterly. Which formula gives the maturity value?', 'o': ['=50000*(1+0.07/4)^(4*3)', '=50000*0.07*3', '=50000/(1+0.07)^3', '=50000+7*3'], 'a': 'A', 'why': 'Quarterly compounding: rate ÷ 4, and 4 × years compounding periods.'},
        {'q': 'How is FD interest taxed?', 'o': ['Added to your income and taxed at your slab rate', 'Always tax-free', 'At a flat 30%', 'Only if the FD is in a co-operative bank'], 'a': 'A', 'why': 'Interest is income; TDS is only an advance part of the tax.'},
        {'q': 'What suits a sinking fund for an Onam budget, saved monthly?', 'o': ['A recurring deposit', 'A 10-year FD', 'Shares', 'A gold loan'], 'a': 'A', 'why': 'An RD takes fixed monthly amounts and matures when you need the money.'},
        {'q': 'What was the post office RD rate for October to December 2026?', 'o': ['6.7% a year', '4% a year', '8.2% a year', '12% a year'], 'a': 'A', 'why': 'India Post listed 6.7% for the RD in that quarter (check current rates).'},
    ],
    study='Current post office and small savings rates, deposit insurance and (optionally) the TDS clause',
    action='Compare an FD or RD at three places with formulas and decide where your short-term money will wait',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    M,
    title='Banking and payments',
    weeks=(7, 8), hours=6.5,
    overview="""
Clean up your bank accounts, make UPI and cards safe, know your rights after a fraud, and choose the right deposit for money you need soon.

Banking is the plumbing of your money life. When it leaks, through charges, old phone numbers, missing nominees or a careless UPI approval, everything else suffers. This module audits every account you have, sets up safety habits for UPI, cards and net banking, and gives you a written plan for the first hour after a fraud.

The last lesson compares fixed deposits, recurring deposits and post office deposits on rate, safety, flexibility and tax, so your emergency fund (Module 5) and sinking funds (Module 3) have a sensible home.
""",
    outcomes=[
        'List and clean up every account you hold, including KYC, contacts and charges',
        'Explain deposit insurance and the ₹5 lakh per-bank limit',
        'Use UPI, cards and net banking with safe habits',
        'Explain your liability under RBI\'s rules and act within hours after a fraud',
        'Calculate FD and RD maturity values and choose where short-term money waits',
    ],
    lessons=LESSONS,
    project='Bank and payments safety audit',
    project_steps=[
        'Complete the Accounts tab: every account, type, contacts, nominee, KYC, charges and a keep/convert/close decision.',
        'Score the 10-question payment safety check for yourself and one family member, and fix every "No" you can fix this week.',
        'Put your fraud response card where you and your family can find it in a hurry.',
        'Check the ₹5 lakh deposit insurance limit for every bank where you or your parents hold deposits.',
        'Write a short summary: three things you fixed, and one thing still to do.',
    ],
    project_proof='Accounts tab screenshot (last four digits only), the safety check scores before and after, and your summary, saved in 04 Banking.',
    rubric=[
        ('Accounts', 'Not listed', 'Listed without checks', 'Every account listed with contacts, nominee, KYC and charges checked'),
        ('Clean-up', 'Nothing done', 'Planned', 'At least one action completed with proof'),
        ('Payment safety', 'Alerts and controls off', 'Some set', 'Alerts on, card controls and limits set'),
        ('Fraud plan', 'None', 'Card written', 'Card written, shared with family and easy to find'),
        ('Deposits', 'Not compared', 'Rates noted', 'Compared on rate, safety, penalty and tax, with a decision'),
    ],
    short=[
        'Turn on transaction alerts and card controls (FIN-M04-L02, steps 1 and 2).',
        'Write the fraud response card and tell your family about 1930.',
        'Check every account has your current mobile number.',
    ],
    flashcards=[
        ('DICGC deposit insurance limit', '₹5 lakh per depositor per bank, principal plus interest (as of November 2026).'),
        ('BSBD account', 'No minimum balance; free basic services, including at least four free withdrawals a month (digital payments not counted).'),
        ('When do you need your UPI PIN?', 'Only to pay money out. Never to receive.'),
        ('Third-party fraud reported within 3 working days', 'Zero liability for you.'),
        ('The first call after a payment fraud', '1930, the national cyber crime helpline.'),
        ('RBI Ombudsman', 'cms.rbi.org.in, free, after the bank rejects or doesn\'t reply in 30 days.'),
        ('Cumulative FD formula', 'Deposit × (1 + rate ÷ 4) ^ (4 × years) for quarterly compounding.'),
        ('Bank website addresses', 'End in .bank.in.'),
    ],
    mistakes=[
        ('Treating safety as a one-time setup.', 'Revisit the safety check every year and whenever you get a new phone or number.'),
        ('Chasing the highest deposit rate.', 'For short-term money, safety and access come first.'),
        ('Keeping fraud knowledge to yourself.', 'Elderly parents and neighbours are targeted most. Share the card.'),
    ],
    project_week=8,
)
