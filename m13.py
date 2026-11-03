"""Module 13: Estate basics."""
from common import lesson, module, link, fence, table, inr, ASOF, CHECK

M = 13

L1 = lesson(
    M, 1,
    title='Nominations and joint accounts',
    weeks=(26, 26), hours=1.5,
    outcome='Check and update nominees on every account, deposit, policy and investment under the 2025–2026 rules, and understand what a nominee and a joint holder can and can\'t do.',
    split='20 minutes reading, 20 minutes resources, 50 minutes action',
    core=f"""
Every year, money sits unclaimed in Indian banks, insurance companies and mutual funds because the owner died and the family didn't know about the account, or couldn't prove their right to it. A few minutes on nominations saves your family months of paperwork and stress.

### What a nomination does

A **nominee** is the person the bank, insurer or fund house pays when you die. With a nominee on record, your family can receive the money with simple documents, without court papers. Who finally **owns** the money can still depend on your will or on succession law; a will (FIN-M13-L02) makes your wishes clear to everyone. So do both: nominate, and write a will when you have dependants or significant assets.

### Bank accounts, deposits and lockers: up to four nominees

Under the Banking Laws (Amendment) Act, 2025, from **1 November 2025** you can nominate **up to four people** ({link('pib-nominee', 'PIB')}, {link('iibf-nominee', 'IIBF')}, {CHECK}):

- **Deposit accounts:** either **simultaneous** nomination (each nominee gets a share you specify, adding up to 100%) or **successive** nomination (the next nominee becomes entitled only if the one above has died).
- **Lockers and articles in safe custody:** **successive** nomination only.
- The detailed rules and forms come under the Banking Companies (Nomination) Rules, 2025; ask your bank for the current form.

### Demat accounts and mutual funds: up to three nominees

SEBI's circular of **29 May 2026**, effective **1 September 2026**, allows **up to three nominees** for demat accounts and mutual fund folios. For **single-holder** accounts and folios opened from that date, you must either **nominate or submit an opt-out declaration**; for joint holdings, nomination is optional and changes need all holders' consent. It replaced the January 2025 circular, which had allowed up to ten ({link('sebi-nominee', 'SEBI circular, via NSDL')}, {CHECK}). Your consolidated account statement shows each folio\'s nomination status ({link('amfi-cas', 'AMFI CAS')}).

### Insurance, EPF, PPF, NPS and government schemes

Each policy and account has its own nomination: life and accident policies, EPF (on the EPFO member services), PPF (at the post office or bank), NPS, PMJJBY and PMSBY, and for Kerala government employees, GPF and other schemes (Module 14). Check each one; a nomination made at 22 may name someone you wouldn't choose at 32.

### Joint accounts

A joint account is owned by two or more people. Its **operating instruction**, chosen when it was opened (for example "either or survivor"), decides who can use it, including after one holder dies. Ask your bank which instruction your joint accounts have. Joint accounts are useful for couples and for elderly parents who need help with banking, but every holder can usually withdraw money, so open them only with people you trust.

### Lost and unclaimed money

Deposits that stay unclaimed for many years are moved by banks to RBI's Depositor Education and Awareness (DEA) Fund, but they can still be claimed. RBI's **UDGAM** portal lets registered users search unclaimed deposits across many banks (30 banks covering about 90% of the fund's value, as of March 2024) by name, bank and an identifier such as PAN or date of birth; the claim itself is made at the bank ({link('udgam', 'RBI UDGAM FAQs')}). Use it for yourself and for relatives who have died.
""",
    example=f"""
**Fathima** made a list of everything in her name and checked nominees one by one. She found:

{table(['Account', 'Nominee before', 'Action'], [
    ('Savings account (Bank A)', 'None', 'Added her mother (simultaneous, 100%)'),
    ('Savings account (Bank B)', 'Her late grandfather', 'Changed to her mother and brother, 50% each'),
    ('PPF', 'Her father (opened when she was 20)', 'Kept, after checking he is still the right choice'),
    ('Two-wheeler insurance', 'Not applicable (property)', '—'),
    ('PMSBY (₹20 accident cover)', 'None recorded', 'Added her mother at the branch'),
    ('NPS (new)', 'Her mother', 'Already done at opening'),
])}

The grandfather was the shock: had something happened to her, Bank B would have been paying a dead person's estate. She also searched UDGAM for her grandfather, with her uncle's help, and found an old savings account with ₹38,000 at a bank in Thalassery, which the family then claimed at the branch with the documents the bank asked for.
""",
    resources=[
        ('pib-nominee', 'The four-nominee rules for bank deposits and lockers, from 1 November 2025', '10 minutes'),
        ('iibf-nominee', 'Simultaneous and successive nomination explained', '10 minutes'),
        ('sebi-nominee', 'SEBI\'s May 2026 circular on demat and mutual fund nominations: read the summary points', '15 minutes'),
        ('udgam', 'How to search for unclaimed deposits on UDGAM', '10 minutes'),
    ],
    steps=[
        'Make a **Documents** tab and start with the nomination audit template: every account, deposit, locker, policy, investment and retirement account in your name.',
        'For each, check the current nominee: in the bank app, the CAS, policy documents, EPFO member services, or by asking the branch.',
        'Update at least the most important missing or outdated nominee this week; note the acknowledgement.',
        'Ask your bank about the operating instruction on any joint account and write it down.',
        'Search UDGAM for yourself, and (with family) for a relative who has died, if relevant.',
    ],
    proof='Your nomination audit with every account checked and proof of at least one nominee update (acknowledgement or screenshot, numbers covered), saved in 13 Estate.',
    templates=[
        ('nomination audit (Documents tab)', """
Account or policy,Institution,Last 4 digits,Nominee(s),Shares % (simultaneous) or order (successive),Last checked,Needs change?,Done on
Savings account,,,,,,,
Fixed/recurring deposits,,,,,,,
Locker,,,,(successive only),,,
Demat account,,,,(up to 3),,,
Mutual fund folios (from CAS),,,,(up to 3),,,
Life/term insurance,,,,,,,
Health/accident insurance,,,,,,,
EPF / PPF / NPS,,,,,,,
PMJJBY / PMSBY / APY,,,,,,,
GPF / govt schemes (if employee),,,,,,,
""", 'csv'),
    ],
    mistakes=[
        ('Thinking "my family will manage".', 'Without nominees, claims can need legal heir certificates and months of visits.'),
        ('Never updating nominations.', 'Marriage, a death or a child should trigger a check of every nomination.'),
        ('Assuming a nominee always owns the money.', 'The nominee receives it; ownership can depend on your will or succession law. Write a will too.'),
        ('Opening joint accounts casually.', 'Every holder can usually withdraw. Choose joint holders you trust completely.'),
    ],
    quiz=[
        {'q': 'From 1 November 2025, how many nominees can you name for a bank deposit account?', 'o': ['Up to four', 'Only one', 'Up to ten', 'None'], 'a': 'A', 'why': 'The Banking Laws (Amendment) Act, 2025 allows up to four, simultaneously or successively.'},
        {'q': 'For a bank locker, which type of nomination is allowed?', 'o': ['Successive only', 'Simultaneous only', 'Both', 'None'], 'a': 'A', 'why': 'Lockers and safe custody articles allow only successive nomination.'},
        {'q': 'Under SEBI\'s circular effective 1 September 2026, how many nominees can a demat account have?', 'o': ['Up to three', 'Up to ten', 'Only one', 'Unlimited'], 'a': 'A', 'why': 'The May 2026 circular replaced the earlier ten-nominee rule (check current rules).'},
        {'q': 'What can UDGAM do?', 'o': ['Help you search unclaimed deposits across many banks', 'Pay the claim directly', 'Make your will', 'Change your nominee'], 'a': 'A', 'why': 'It shows where unclaimed deposits are; you claim at the bank.'},
    ],
    study='The four-nominee rules (PIB, IIBF), SEBI\'s May 2026 nomination circular and the UDGAM FAQs',
    action='Audit nominees on every account and policy, update at least one, and search UDGAM',
)

L2 = lesson(
    M, 2,
    title='Wills and your family money file',
    weeks=(26, 26), hours=1.5,
    outcome='Decide whether you need a will now, know the basic rules for a valid will in India, and build a family money file and document register so your family can find everything.',
    split='25 minutes reading, 20 minutes resources, 45 minutes action',
    core=f"""
### Why a will

A **will** says who gets your property after you die and who should handle it (the executor). Without one, your property passes under the succession law that applies to you, which may not match your wishes, and families often need court documents to prove who the heirs are. A will is not only for the rich: if you have a spouse, children, a house, a plot or savings, it protects them.

### Basics for a valid will in India

From a legal guide on making and registering a will ({link('will-guide', 'iPleaders')}):

- Any **adult of sound mind** can make a will.
- An ordinary written will must be **signed by you and attested by two witnesses**.
- **Registration is not compulsory** (Registration Act, 1908, section 18), but registering it makes it stronger if anyone disputes it.
- You can change or revoke a will at any time; **a later will replaces an earlier one**. Under the Indian Succession Act, a **marriage revokes an earlier will**, so make a new one after marrying.
- The Indian Succession Act's will rules don't apply to Muslims, who are generally governed by Muslim personal law; Muslims should get advice on what share can be willed.
- Probate (court confirmation of a will) is needed in some cases; a lawyer can tell you whether it applies to you.

### What a simple will includes

Your full name and details; a statement that you are making it freely and revoke earlier wills; a list of your main assets (described, not necessarily with full account numbers); who receives what, with backup beneficiaries; an **executor**; a **guardian** for minor children; the date and place; your signature and two witnesses' signatures (it is safer to choose witnesses who receive nothing under the will). For property, a business, family disputes or Gulf/NRI assets, **pay a lawyer**: a mistake in a will can't be fixed after you are gone.

### Your family money file

A will is useless if no one can find the accounts. A **family money file** is a simple document (paper, and a protected digital copy) that tells a trusted person:

- Every bank account, deposit, locker, investment, policy and loan: institution, branch, type, last four digits, nominee
- Where original documents are: property deeds, policy bonds, PAN, Aadhaar, certificates
- Digital accounts that matter (email, the Money Folder) and how to get help to access them, **without writing passwords** in the file (keep those separately, sealed, or in a password manager whose master password is shared safely)
- Who to call: a trusted relative, the employer, an insurance agent, a lawyer or tax helper
- Your wishes on important matters

### DigiLocker

**DigiLocker** (by MeitY under Digital India) stores digital copies of documents such as Aadhaar, PAN, voter ID, driving licence, vehicle registration and marksheets, and lets you share them ({link('digilocker', 'DigiLocker')}). Use it for government-issued documents; keep policy bonds and property papers safe too.

### Review

Check the file and nominations once a year (your yearly review), and update the will after marriage, children, a death in the family, or a big asset change.
""",
    example=f"""
**Joseph and Mary** had no will: "Our son is the only child; it's obvious." Anu asked them what would happen to the house if their son were abroad and Mary were unwell, or if a relative challenged it. They agreed to see a lawyer in Vatakara, who drafted simple wills for both (each leaving everything to the other, then to their son), with two neighbours as witnesses, and registered them at the sub-registrar office for a modest fee.

Their son built the family money file over a weekend: 3 bank accounts, 2 FDs, the post office MIS, the house deed (in the steel almirah), the pension papers, the KASP card and the locker key's location. The file is in a sealed envelope at home, with a copy in the son's DigiLocker-linked Drive folder (without passwords). Mary said the best part was "knowing he won't have to search in a hurry".
""",
    resources=[
        ('will-guide', 'How to make and register a will in India: validity, witnesses, registration, revoking', '20 minutes'),
        ('digilocker', 'What DigiLocker stores and how to fetch your documents', '10 minutes'),
        ('udgam', 'Revise: finding unclaimed deposits of a family member', '5 minutes'),
    ],
    steps=[
        'Add a **document register** to your Documents tab: every important document, where the original is, and whether a digital copy is in DigiLocker or your Money Folder.',
        'Sign in to DigiLocker and fetch at least your Aadhaar, PAN and one more issued document.',
        'Write your family money file using the template, without passwords, and decide where it is kept and who knows.',
        'Decide whether you need a will now (dependants, a house or land, significant savings). If yes, draft the outline and plan when you will see a lawyer or write and sign it with two witnesses. If not yet, write the life event that will trigger it.',
        'Tell your trusted person where the file is.',
    ],
    proof='A screenshot of your document register, the family money file (contents covered as needed) and your will decision, saved in 13 Estate.',
    templates=[
        ('document register', """
Document,Original kept at,Digital copy (DigiLocker / Money Folder / none),Valid until,Who knows where it is
PAN,,,,
Aadhaar,,,,
Birth certificate,,,,
Educational certificates,,,,
Property deed and tax receipts,,,,
Insurance policies,,,,
Vehicle RC and insurance,,,,
Bank passbooks and FD receipts,,,,
Pension / service records (if employee),,,,
Will (if made),,,,
""", 'csv'),
        ('family money file (no passwords)', """
IF SOMETHING HAPPENS TO ME (updated on ____)
1. Accounts and deposits: institution, branch, type, last 4 digits, nominee (see Documents tab)
2. Insurance policies: insurer, type, cover, where the policy is, claim helpline
3. Investments and retirement accounts: EPF/PPF/NPS/funds/demat, where statements are
4. Loans I owe and money owed to me
5. Where originals are kept: ____
6. Will: made? yes/no; kept at ____; executor ____
7. Digital: email and Money Folder; how to get help to access them: ____ (no passwords here)
8. People to contact: relative ____ employer ____ lawyer/tax helper ____
9. My wishes: ____
""", ''),
        ('simple will outline (take to a lawyer or adapt carefully)', """
I, ____ (name, parent's name, age, address), being of sound mind, make this will freely and revoke all earlier wills.
My assets include: ____ (describe)
I leave ____ to ____; if they die before me, to ____.
I appoint ____ as executor. For my minor children, I appoint ____ as guardian.
Signed on ____ at ____.   Signature: ____
Witness 1 (name, address, signature): ____   Witness 2: ____
""", ''),
    ],
    mistakes=[
        ('Thinking wills are only for the rich or old.', 'A spouse, a child or a plot is reason enough.'),
        ('Writing passwords in the money file.', 'Keep them separately and securely; the file says how to get help, not the secrets.'),
        ('Not updating after marriage.', 'Under the Indian Succession Act, marriage revokes an earlier will.'),
        ('DIY wills for complex situations.', 'Property disputes, businesses and NRI assets need a lawyer.'),
    ],
    quiz=[
        {'q': 'Is registering a will compulsory in India?', 'o': ['No, but it strengthens the will in a dispute', 'Yes, always', 'Only for women', 'Only in Kerala'], 'a': 'A', 'why': 'Section 18 of the Registration Act makes it optional.'},
        {'q': 'How many witnesses must attest an ordinary written will?', 'o': ['Two', 'None', 'One', 'Five'], 'a': 'A', 'why': 'An unprivileged will needs two witnesses.'},
        {'q': 'You made a will at 25 and married at 28. Under the Indian Succession Act, what happened to the will?', 'o': ['The marriage revoked it; make a new one', 'Nothing', 'It doubled', 'It became registered'], 'a': 'A', 'why': 'Marriage revokes an earlier will under the Act.'},
        {'q': 'What should a family money file never contain?', 'o': ['Passwords and OTPs', 'A list of accounts', 'Where documents are kept', 'Contact people'], 'a': 'A', 'why': 'Keep secrets separately; the file explains where things are.'},
    ],
    study='The guide to making and registering a will, DigiLocker and UDGAM',
    action='Build a document register and family money file, fetch documents into DigiLocker and make a will decision',
)

LESSONS = [L1, L2]

MODULE = module(
    M,
    title='Estate basics: nominations, wills and documents',
    weeks=(26, 26), hours=4,
    overview="""
Make sure your money reaches the right people with the least trouble if something happens to you: nominations on every account, a will when you need one, and a family money file that tells your family where everything is.

Estate planning sounds like something for old or wealthy people. It isn't. A missing nominee, a nominee who has died, or a family that doesn't know an account exists turns a sad time into months of visits and paperwork, and money can end up unclaimed for years.

This module uses the new rules: up to four nominees for bank deposits from November 2025, up to three for demat and mutual funds from September 2026, and RBI's UDGAM portal for finding unclaimed deposits. You audit every nomination, build a document register and family money file, and decide on a will. The result is part of your final plan.
""",
    outcomes=[
        'Explain what nominees and joint holders can and can\'t do',
        'Apply the 2025–2026 nomination rules for banks, lockers, demat and mutual funds',
        'Find unclaimed deposits with UDGAM',
        'Know the basic requirements for a valid will and when to use a lawyer',
        'Build a document register and family money file, without passwords',
    ],
    lessons=LESSONS,
    project='My document system and nomination audit',
    project_steps=[
        'Complete the nomination audit for every account and policy, with all urgent updates done.',
        'Complete the document register and fetch your key documents into DigiLocker.',
        'Finish the family money file and give its location to a trusted person.',
        'Write your will decision: made, booked with a lawyer, or the trigger event for making one.',
        'Add "nominations, money file and will" to your yearly review checklist.',
    ],
    project_proof='Screenshots of the nomination audit and document register, confirmation that the money file exists and who knows where it is, and your will decision, saved in 13 Estate.',
    rubric=[
        ('Nominations', 'Unknown', 'Some checked', 'Every account checked and urgent updates done'),
        ('Rules', 'Unaware', 'Know the bank rule', 'Know the bank, locker and demat/MF rules as of 2026'),
        ('Documents', 'Scattered', 'Listed', 'Register complete; key documents in DigiLocker'),
        ('Money file', 'None', 'Started', 'Complete, without passwords, and a trusted person knows where it is'),
        ('Will', 'Not considered', 'Thought about', 'Made, booked or a clear trigger written'),
    ],
    short=[
        'Check and fix nominees on your main bank account and any insurance policy (FIN-M13-L01).',
        'Fetch Aadhaar and PAN into DigiLocker (FIN-M13-L02).',
        'Write a one-page money file and tell one person where it is.',
    ],
    flashcards=[
        ('Bank deposit nominees from 1 November 2025', 'Up to four, simultaneous (shares adding to 100%) or successive.'),
        ('Lockers and safe custody', 'Successive nomination only.'),
        ('Demat and mutual fund nominees from 1 September 2026', 'Up to three; single holders must nominate or opt out.'),
        ('UDGAM', 'RBI\'s portal to search unclaimed deposits; claim at the bank.'),
        ('Valid will basics', 'Adult of sound mind, signed, attested by two witnesses; registration optional.'),
        ('Marriage and an old will', 'Under the Indian Succession Act, marriage revokes an earlier will.'),
        ('Family money file', 'Where everything is and who to call, without passwords.'),
    ],
    mistakes=[
        ('Leaving nominations from years ago unchecked.', 'People die, marry and fall out; nominations should follow your life.'),
        ('Keeping everything in your head.', 'If only you know where things are, your family will struggle.'),
        ('Waiting for "later" to make a will.', 'Make one when you have dependants or property, and update it after big changes.'),
    ],
    project_week=26,
)
