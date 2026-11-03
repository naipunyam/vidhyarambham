"""Module 7: Insurance."""
from common import lesson, module, link, fence, table, inr, ASOF, CHECK

M = 7


def irr_due(prem, n, maturity):
    lo, hi = -0.5, 0.5
    for _ in range(300):
        mid = (lo + hi) / 2
        fv = sum(prem * (1 + mid) ** (n - k) for k in range(n))
        if fv > maturity:
            hi = mid
        else:
            lo = mid
    return mid


def fv_due(amount, rate, n):
    return sum(amount * (1 + rate) ** (n - k) for k in range(n))


ENDOW_IRR = irr_due(30000, 20, 900000) * 100
TI_6 = fv_due(22000, 0.06, 20)
TI_8 = fv_due(22000, 0.08, 20)

L1 = lesson(
    M, 1,
    title='Insurance basics, and why not to mix it with investment',
    weeks=(13, 13), hours=2,
    outcome='Decide which risks you need to insure, list the policies you and your family already have, and calculate the real return on a policy that mixes insurance with saving.',
    split='30 minutes reading, 30 minutes resources, 60 minutes action',
    core=f"""
### What insurance is for

Insurance is paying a **small, certain amount** (the premium) to protect yourself from a **large, uncertain loss** that you couldn't afford. It is not for small losses you can pay from your emergency fund, and it is not an investment.

Ask about each risk: **how likely is it, and how bad would it be?**

{table(['Risk', 'How bad', 'What protects you'], [
    ('A big hospital bill', 'Can wipe out years of saving or force a gold loan', 'Health insurance (FIN-M07-L03)'),
    ('Your death while others depend on your income', 'Family loses its income and may inherit your loans', 'Term life insurance (FIN-M07-L02)'),
    ('Disability from an accident', 'Income stops, costs rise', 'Personal accident cover (FIN-M07-L04)'),
    ('Your vehicle damaging someone else or their property', 'Large legal liability', 'Third-party motor insurance, required by law (FIN-M07-L04)'),
    ('Fire, flood or storm damage to your house', 'Rebuilding can cost lakhs', 'Home insurance (FIN-M07-L04)'),
    ('A broken phone or a small repair', 'Annoying but affordable', 'Your emergency fund, not insurance'),
])}

### The order of priority

For most young people in Kerala: **health insurance first** (for you and your parents), then **term life insurance** once someone depends on your income or you have loans, then **accident cover**, then vehicle and home as needed. Note that from 22 September 2025, **individual life and health insurance policies are exempt from GST** ({link('gst-56', 'GST Council, September 2025')}, {CHECK}), so premiums no longer carry the 18% GST they used to.

### Why not mix insurance with investment

Many policies sold in India combine life cover with saving: **endowment**, **money-back** and some **unit-linked (ULIP)** plans. They are sold as "safe, tax-saving and you get your money back". The problem is that they usually do both jobs badly: the life cover is small and the return is low, and leaving early often means losing money.

**Worked example** (made-up but typical numbers): a 30-year-old is offered an endowment policy: ₹30,000 a year for 20 years, life cover of ₹5 lakh, and about ₹9,00,000 at maturity.

- The real return on that ₹30,000 a year, using the RATE function on the cash flows, is only about **{ENDOW_IRR:.1f}% a year**, which is below India's 4% inflation target. Your money loses buying power.
- The alternative: a **term policy** with ₹50 lakh cover (a made-up quote of ₹8,000 a year; get real quotes) plus investing the other ₹22,000 a year. If that investment earns 6% a year, it grows to about **{inr(TI_6)}** in 20 years; at 8%, about **{inr(TI_8)}**. Returns aren't guaranteed (Module 8), so it could also be less.
- Even in the weaker case, the second approach gave **ten times the life cover** for 20 years.

The lesson isn't "every bundled policy is bad". It is: **buy insurance for protection, invest for growth, and calculate the return of any policy before you buy.** Every policy comes with a benefit illustration; put its numbers into the template and see.

### If you already have such a policy

Don't stop paying in a panic. First make sure you have enough term and health cover. Then compare three options with the insurer's figures: continue, make it **paid-up** (stop paying and get a reduced amount at maturity), or **surrender** it. Judge only by what happens from today; what you have already paid is gone either way (the sunk-cost trap from Module 1).
""",
    example=f"""
**Rahul's** mother had bought him a money-back policy when he was 22: ₹18,000 a year, ₹3 lakh cover, with "money back every five years". When he started his government job, an agent at the office offered "a better plan" of the same type for ₹40,000 a year.

Rahul listed what his family already had: his mother's money-back policy for him, his father's old endowment policy (₹2 lakh cover), no health insurance for his parents except a government scheme they weren't sure about, and his new Medisep cover as an employee (Module 14).

His conclusions: the family had **₹5 lakh of total life cover** but his parents depended on him; a hospital stay for his father could cost more than their savings; and the new plan would have taken ₹40,000 a year from a family that most needed health cover. He said no to the agent, put his parents' health cover at the top of his list, and planned term cover for himself (FIN-M07-L02). He kept the old money-back policy for now, while he checked its surrender and paid-up values.
""",
    resources=[
        ('varsity', 'The "Personal Finance: Insurance" module: read the first chapters on why insurance exists and on term vs other plans', '30 minutes'),
        ('ncfe', 'The e-LMS module on safety nets and insurance', '15 minutes'),
        ('gst-56', 'The GST Council decision exempting individual life and health insurance (search the PDF for "insurance")', '5 minutes'),
    ],
    steps=[
        'Ask your family and check your papers and email: list every insurance policy held by you, your parents and your spouse, if any.',
        'Make an **Insurance** tab with the template and fill in one row per policy.',
        'Mark which risks from the table are covered and which are not.',
        'If anyone has an endowment, money-back or ULIP policy, take its benefit illustration or bond and calculate its return with the template formula.',
        'Write your priority list: which cover is missing, in order.',
    ],
    proof='A screenshot of your Insurance tab (policy numbers covered), your gaps list and, if relevant, the return calculation of one bundled policy, saved in 07 Insurance.',
    templates=[
        ('Insurance tab', """
Policy holder,Person covered,Type (term / health / accident / vehicle / home / endowment / money-back / ULIP / govt scheme),Insurer,Policy number (last 4 only),Cover (₹),Premium (₹ a year),Renewal date,Nominee,Waiting periods or limits,Claim helpline,Keep / review
""", 'csv'),
        ('return of a policy that mixes saving and cover', """
A2: yearly premium (₹)          30000
B2: years of premiums           20
C2: amount at maturity (₹)      900000   (from the benefit illustration; ignore "bonuses" that aren't guaranteed, or calculate both)
D2: yearly return %  =RATE(B2,-A2,0,C2,1)*100
(The last 1 means premiums are paid at the start of each year.)
Compare D2 with inflation (about 4%) and with a safe deposit rate.
""", ''),
    ],
    mistakes=[
        ('Buying insurance as an investment.', 'Protection and growth are different jobs. Buy them separately, and calculate the return of any bundled plan.'),
        ('Insuring small risks and missing big ones.', 'Phone insurance with no health cover is backwards. Insure what would ruin you.'),
        ('Buying from whoever asks first.', 'Relatives, colleagues and bank staff may earn commission. Compare before deciding.'),
        ('Stopping an old policy in a panic.', 'Check your cover first, then compare continue, paid-up and surrender using the insurer\'s numbers.'),
    ],
    quiz=[
        {'q': 'What is insurance mainly for?', 'o': ['Protecting against large losses you couldn\'t afford', 'Earning high returns', 'Saving tax only', 'Covering every small expense'], 'a': 'A', 'why': 'Small losses belong to the emergency fund; insurance is for the big ones.'},
        {'q': 'A policy takes ₹30,000 a year for 20 years and pays ₹9 lakh at maturity. Its return is about…', 'o': ['3.7% a year', '15% a year', '9% a year', '0%'], 'a': 'A', 'why': 'RATE on these cash flows gives about 3.7%, below the 4% inflation target.'},
        {'q': 'From 22 September 2025, what changed for individual life and health insurance?', 'o': ['They became exempt from GST', 'GST rose to 28%', 'They became compulsory', 'Premiums were fixed by RBI'], 'a': 'A', 'why': 'The 56th GST Council meeting exempted individual life and health policies (check current rules).'},
        {'q': 'You already pay into an old endowment policy. What should you do first?', 'o': ['Make sure you have enough term and health cover, then compare continue, paid-up and surrender', 'Stop paying today', 'Buy another endowment', 'Ignore it forever'], 'a': 'A', 'why': 'Protection first; then judge the old policy only by what happens from today.'},
    ],
    study='The Varsity insurance module\'s first chapters, the NCFE safety nets module and the GST decision on insurance',
    action='List every policy in your family in an Insurance tab, mark the gaps and calculate the return of any bundled policy',
)

L2 = lesson(
    M, 2,
    title='Term life insurance: how much, and how to compare',
    weeks=(13, 13), hours=1.5,
    outcome='Calculate how much life cover you need, if any, and compare term policies on the things that matter, without buying.',
    split='20 minutes reading, 25 minutes resources, 45 minutes action',
    core=f"""
### Who needs life insurance?

Life insurance replaces your income for the people who depend on it. You need it if **someone would struggle financially if you died**: a spouse, children, parents you support, or a co-borrower on your loans. If no one depends on you and you have no shared loans, you may not need it yet; buy it when that changes (often at marriage or a home loan).

### Term insurance

A **term policy** pays the **sum assured** to your nominee if you die during the term, and nothing if you survive. That is why it is cheap: you pay only for protection. Premiums depend on your age, health, habits (tobacco raises them a lot), the cover and the term; younger and healthier means cheaper, and the premium usually stays fixed for the whole term.

### How much cover?

Two ways; use both and take the higher:

**1. Rule of thumb:** many planners suggest **10 to 15 times your annual income**.

**2. Needs-based:** add up what your family would need, minus what they already have:

> **Cover = (yearly support your family needs × years) + loans + big goals you fund − savings and existing cover**

**Worked example** (made-up): Rahul gives his parents ₹60,000 a year and wants to cover them for 20 years (₹12,00,000), is co-borrower on his sister's education loan (₹6,00,000 expected), and wants his family to have ₹1,00,000 extra for a crisis. He has ₹50,000 saved and ₹5,00,000 in old policies. Needs-based cover = ₹12,00,000 + ₹6,00,000 + ₹1,00,000 − ₹50,000 − ₹5,00,000 = **₹13,50,000**. The rule of thumb (10 × his ₹3,60,000 yearly take-home) says ₹36,00,000. He chose **₹25 lakh**: above his needs, with room for inflation and a future spouse, at a premium he can afford.

### How long?

Until the people who depend on you no longer would: usually until your planned retirement age or until your youngest child is independent. Cover that runs to 85 or 99 is much more expensive and rarely needed.

### Comparing term policies (without buying)

- **The insurer's claim record:** look for its claim settlement figures and how quickly it settles claims, in its public disclosures. A low premium is worthless if claims get stuck.
- **Exclusions:** most term policies don't pay for suicide in the first year; read the list.
- **Riders:** add-ons such as accidental death or critical illness. Compare them with buying separate accident and health cover.
- **Honest disclosure:** tell the truth about your health, smoking and alcohol. Hiding something is the most common reason claims are rejected.
- **Nominee:** name one, and tell them the policy exists (Module 13).

### Government options

**PMJJBY** gives ₹2 lakh life cover for death from any cause, for people aged 18 to 50 with a bank account, at ₹436 a year by auto-debit; cover runs from 1 June to 31 May ({link('pmjjby', 'ICICI Bank scheme page')}, {CHECK}). It is a useful small base, not a full replacement for term cover when people depend on you.
""",
    example=f"""
**Rahul** asked three insurers for online term quotes for ₹25 lakh to age 60, giving honest answers (he doesn't smoke). He compared, without buying:

{table(['', 'Insurer A', 'Insurer B', 'Insurer C'], [
    ('Yearly premium (made-up)', '₹4,900', '₹5,600', '₹4,300'),
    ('Claims settled, from public disclosures', 'Check and write the figure', 'Check', 'Check'),
    ('Medical tests needed?', 'Yes', 'Yes', 'No'),
    ('Accidental death rider', '₹400 extra', 'Not offered', '₹350 extra'),
    ('Exclusions read?', 'Yes', 'Yes', 'Yes'),
])}

Insurer C was cheapest without medical tests, but Rahul noticed that a policy issued without proper medical checks can lead to disputes later if a claim is made, so he leaned towards one with tests. He also joined PMJJBY through his bank as a small extra layer. He'll decide after reading the policy wordings in full, which is the point of this lesson: compare first, buy later.
""",
    resources=[
        ('varsity', 'The "Personal Finance: Insurance" module: the chapters on term insurance and how much cover', '25 minutes'),
        ('pmjjby', 'PMJJBY: age, cover, premium and cover period', '5 minutes'),
    ],
    steps=[
        'Write down who depends on your income now, and who might in 5 years.',
        'Calculate your cover both ways with the template: rule of thumb and needs-based. Choose a number and a term.',
        'Get term quotes from three insurers\' official websites with honest answers. Don\'t buy, and don\'t share documents yet.',
        'Fill in the comparison template, including each insurer\'s claim settlement figures from its public disclosures.',
        'Check whether you are already enrolled in PMJJBY (your bank statement shows a ₹436 debit around June if so).',
        'If no one depends on you yet, write "not needed yet" and the life event that will change it.',
    ],
    proof='Your cover calculation and the three-way comparison (or your "not needed yet" note with the trigger event), saved in 07 Insurance.',
    templates=[
        ('how much life cover', """
Rule of thumb:  yearly take-home income × 10 = ₹____   × 15 = ₹____
Needs-based:
A. Yearly support my family needs from me: ₹____ × years: ____ = ₹____
B. Loans I owe or co-borrowed: ₹____
C. Goals I want funded if I'm not there (education, parents' care): ₹____
D. Savings and investments my family could use: ₹____
E. Life cover I already have (policies, PMJJBY, employer schemes): ₹____
Cover needed = A + B + C − D − E = ₹____
My choice: ₹____ until age ____
""", ''),
        ('term policy comparison (no purchase)', """
,Insurer 1,Insurer 2,Insurer 3
Cover and term,,,
Yearly premium (₹),,,
Claims settled (from public disclosures),,,
Medical tests?,,,
Main exclusions,,,
Riders and their cost,,,
Can I pay yearly by auto-debit?,,,
Notes,,,
""", 'csv'),
    ],
    mistakes=[
        ('Buying too little cover because "₹5 lakh sounds a lot".', 'Do the needs calculation; families need years of income, not months.'),
        ('Hiding health facts or habits.', 'Non-disclosure is a leading reason for claim rejection. Tell the truth.'),
        ('Cover to age 99 "to get something back".', 'Cover until people stop depending on you. Longer cover costs much more.'),
        ('Not telling your nominee.', 'A policy nobody knows about may never be claimed.'),
    ],
    quiz=[
        {'q': 'Who most needs term life insurance?', 'o': ['Someone whose family depends on their income or who has shared loans', 'A student with no dependants', 'Someone who wants high returns', 'Anyone who has a vehicle'], 'a': 'A', 'why': 'Life cover replaces income for people who depend on it.'},
        {'q': 'Family needs ₹10 lakh plus loans of ₹5 lakh; savings ₹1 lakh; existing cover ₹2 lakh. Needs-based cover?', 'o': ['₹12 lakh', '₹18 lakh', '₹15 lakh', '₹8 lakh'], 'a': 'A', 'why': '10 + 5 − 1 − 2 = ₹12 lakh.'},
        {'q': 'What does PMJJBY provide, as of November 2026?', 'o': ['₹2 lakh life cover for ₹436 a year, ages 18 to 50', '₹50 lakh cover free', 'Health insurance for hospital bills', 'A pension'], 'a': 'A', 'why': 'It is a small, low-cost life cover scheme (check current rules).'},
        {'q': 'What is a common reason for life claims being rejected?', 'o': ['Not disclosing health conditions or habits when buying', 'Paying the premium yearly', 'Choosing a 30-year term', 'Having a nominee'], 'a': 'A', 'why': 'Honest disclosure protects your family\'s claim.'},
    ],
    study='The Varsity insurance chapters on term cover and the PMJJBY scheme details',
    action='Calculate your life cover need and compare three term quotes without buying',
)

L3 = lesson(
    M, 3,
    title='Health insurance: floater, top-up and the fine print',
    weeks=(13, 14), hours=2,
    outcome='Choose the type and size of health cover for your family, read a policy\'s key terms, and compare two policies with a checklist, without buying.',
    split='30 minutes reading, 30 minutes resources, 60 minutes action',
    core=f"""
A hospital stay is the most common money shock in Indian families. Health insurance turns a possible ₹3 lakh bill into a manageable cost. It is also full of fine print, so this lesson is about reading it.

### Individual or family floater

- **Individual policy:** each person has their own sum insured.
- **Family floater:** one sum insured shared by the family, for example ₹5 lakh for you, your spouse and children. Cheaper, but one big claim can use it up for everyone that year.
- **Parents:** covering older parents in the same floater can raise the premium sharply for everyone. Many families buy parents a separate policy.

### Base policy, top-up and super top-up

- A **top-up** policy pays above a **deductible** (an amount you or your base policy cover first) for **each claim**.
- A **super top-up** pays once the **total** of all claims in the year crosses the deductible.
- **Worked example:** a ₹5 lakh base floater plus a ₹15 lakh super top-up with a ₹5 lakh deductible. A ₹8 lakh bill: the base pays ₹5 lakh, the super top-up pays ₹3 lakh. Super top-ups with a high deductible are usually much cheaper than a bigger base policy.

### The fine print that decides your claim

- **Waiting periods:** usually 30 days for most illnesses (except accidents), longer for specific diseases, and for **pre-existing diseases** (conditions you already have) the maximum waiting period is **36 months** under IRDAI's 2024 rules ({link('bu-health', 'summary of the IRDAI master circular')}, {CHECK}).
- **Moratorium:** after **60 months** of continuous cover, a claim can't be questioned for non-disclosure, except for proven fraud.
- **Room rent limits:** many policies cap the room rent, for example a percentage of the sum insured per day. If you take a costlier room, the insurer may also cut other bills **in proportion**. Look for "no room rent limit" or a cap that fits local hospitals.
- **Co-payment:** you pay a fixed share of every claim (common in senior citizen policies).
- **Sub-limits:** caps on specific treatments, such as cataract surgery.
- **Network hospitals:** cashless treatment works only at network hospitals; check the ones near you, in Kozhikode and Vatakara, for example.
- **Restoration and no-claim bonus:** extra cover after a claim, or more cover for claim-free years.

### Your rights under IRDAI's 2024 rules

Insurers must decide on **cashless requests within one hour** and give final authorisation **within three hours** of the hospital's discharge request; every policy comes with a **Customer Information Sheet** in simple language; and the insurer or its TPA collects documents from the hospital rather than asking you ({link('om-cashless', 'Outlook Money, May 2024')}). You get a **30-day free-look period** to return a new policy, and you can **port** your policy to another insurer without losing waiting-period credit ({link('bu-health', 'summary')}, {CHECK}).

### How much cover?

Think about a serious stay at a private hospital in your district, for the person most likely to need it. Many families find ₹5 lakh a sensible base for a young family, plus a super top-up for big events; parents usually need more. Ask a local hospital for typical package costs.

### Tax

Under the old tax regime, health premiums can be deducted (section 126 of the Income-tax Act, 2025, the old "80D"): up to ₹25,000 for yourself, spouse and children, and another ₹25,000 for parents (₹50,000 each if the insured person is a senior citizen), paid by a non-cash mode ({link('it-s126', 'section 126')}, {CHECK}). FIN-M10-L02 shows whether the old regime suits you.
""",
    example=f"""
**Anu** compared two family floater policies for herself and her parents (made-up policies; she didn't buy yet):

{table(['', 'Policy A', 'Policy B'], [
    ('Sum insured', '₹5 lakh floater', '₹5 lakh floater'),
    ('Yearly premium (made-up quotes)', '₹16,800', '₹21,500'),
    ('Room rent', 'Up to 1% of sum insured a day (₹5,000)', 'No limit'),
    ('Co-payment', '20% for members over 60', 'None'),
    ('Pre-existing disease waiting', '36 months', '24 months'),
    ('Network hospitals within 30 km', '4', '7'),
    ('Restoration', 'Yes', 'Yes'),
])}

Policy A looked cheaper, but her father is 63: a ₹2 lakh claim would cost him ₹40,000 in co-payment. And his blood pressure counts as pre-existing, so Policy B's shorter wait mattered. She also asked a hospital in Kozhikode about room charges: ₹5,000 a day was enough for a shared room but not a private one.

Her decision (for when she has the money): Policy B for her parents, or Policy A with no co-pay if the insurer offers it as an add-on, and a cheap super top-up later. She also checked whether her parents were eligible for KASP (FIN-M07-L04).
""",
    resources=[
        ('om-cashless', 'IRDAI\'s 2024 health rules: one-hour cashless decisions, three-hour discharge, Customer Information Sheet', '10 minutes'),
        ('bu-health', 'Waiting periods, moratorium, free-look and portability under the 2024 master circular', '15 minutes'),
        ('varsity', 'The "Personal Finance: Insurance" module: the health insurance chapters', '30 minutes'),
        ('it-s126', 'Section 126: health insurance deduction limits (old regime)', '5 minutes'),
    ],
    steps=[
        'Write down who needs cover in your family, their ages and any existing conditions.',
        'If anyone already has a policy, find its Customer Information Sheet or policy wording and fill in the checklist for it.',
        'Choose two policies from insurers\' official websites and fill in the comparison checklist for both, without buying.',
        'Check the network hospital list of each for hospitals near you.',
        'Decide the type and size of cover you would buy (floater, separate parents\' policy, super top-up), and write why.',
    ],
    proof='Your filled-in health policy checklist for two policies (or one existing and one alternative) and your written decision, saved in 07 Insurance.',
    templates=[
        ('health policy checklist (20 questions)', """
1. Individual or floater? Who is covered?
2. Sum insured (₹)?
3. Premium (₹ a year) and how it rises with age?
4. Initial waiting period (days)?
5. Pre-existing disease waiting period (months, max 36)?
6. Specific disease waiting periods?
7. Room rent limit? Proportionate deduction clause?
8. Co-payment (% and for whom)?
9. Sub-limits (cataract, joint replacement, etc.)?
10. Pre- and post-hospitalisation days covered?
11. Day-care procedures covered?
12. Restoration of sum insured?
13. No-claim bonus?
14. Network hospitals near me (names)?
15. Cashless process and helpline?
16. Exclusions that matter to my family?
17. Maternity or newborn cover (if relevant)?
18. Ambulance and domiciliary cover?
19. Lifelong renewal? Any age limits?
20. Claims record of the insurer (public disclosures)?
""", ''),
        ('two-policy comparison', """
Question,Policy A,Policy B,Which is better for my family?
(copy the 20 questions above into column A)
""", 'csv'),
    ],
    mistakes=[
        ('Choosing on premium alone.', 'Room rent caps, co-payments and long waiting periods can cost far more than the premium difference.'),
        ('Relying only on employer cover.', 'It may end when you change jobs, and it may not cover parents. Consider your own policy too.'),
        ('Hiding pre-existing conditions.', 'Declare them; the waiting period is far better than a rejected claim.'),
        ('Letting a policy lapse.', 'A break can restart waiting periods. Renew on time, within the grace period at most.'),
    ],
    quiz=[
        {'q': 'A ₹5 lakh base floater and a ₹15 lakh super top-up with a ₹5 lakh deductible. Who pays a ₹8 lakh bill?', 'o': ['Base ₹5 lakh, super top-up ₹3 lakh', 'Super top-up ₹8 lakh', 'Base ₹8 lakh', 'You pay ₹3 lakh'], 'a': 'A', 'why': 'The super top-up pays above the ₹5 lakh deductible, which the base covers.'},
        {'q': 'What is the maximum waiting period for pre-existing diseases under IRDAI\'s 2024 rules?', 'o': ['36 months', '48 months', '12 months', '96 months'], 'a': 'A', 'why': 'The 2024 master circular capped it at 36 months (check current rules).'},
        {'q': 'How quickly must an insurer decide on a cashless request, under the 2024 rules?', 'o': ['Within one hour', 'Within one week', 'Within 30 days', 'There is no limit'], 'a': 'A', 'why': 'One hour for cashless authorisation; three hours for discharge.'},
        {'q': 'What is the risk of a room rent limit?', 'o': ['If you choose a costlier room, other bills may be cut in proportion', 'There is no risk', 'It raises the premium every month', 'It cancels the policy'], 'a': 'A', 'why': 'Proportionate deduction can reduce the whole claim, not just the room charge.'},
    ],
    study='IRDAI\'s 2024 health rules (two summaries), the Varsity health insurance chapters and section 126',
    action='Compare two health policies with the 20-question checklist and write which cover your family needs',
)

L4 = lesson(
    M, 4,
    title='Accident, vehicle and home cover, and government schemes',
    weeks=(14, 14), hours=1.5,
    outcome='Know what accident, motor and home insurance cover, and check which central and Kerala government schemes you and your family can use.',
    split='20 minutes reading, 25 minutes resources, 45 minutes action',
    core=f"""
### Personal accident cover

Accident policies pay a fixed amount for accidental death and for permanent disability, and some pay a weekly amount while you can't work. They are cheap and especially useful if you ride a two-wheeler, travel a lot or do physical work. Life and health policies don't replace them: health insurance pays hospital bills, not lost income from a disability.

**PMSBY** gives ₹2 lakh for accidental death or full disability and ₹1 lakh for partial disability, for ages 18 to 70, at **₹20 a year** by auto-debit; cover runs from 1 June to 31 May ({link('pmjjby', 'ICICI Bank scheme page')}, {CHECK}). Few covers are cheaper. Government employees in Kerala also have a group accident scheme (Module 14).

### Vehicle insurance

- **Third-party cover is compulsory:** under the Motor Vehicles Act, every vehicle used in a public place must carry valid third-party insurance, which pays for injury or damage you cause to others. New private cars must have three years of third-party cover; own-damage cover can be added ({link('tg-motor', 'TaxGuru, September 2026')}, {CHECK}).
- **Own-damage cover** pays for damage to your vehicle. For an old, low-value vehicle it may not be worth it; for a new one it usually is.
- **No-claim bonus** lowers your own-damage premium for claim-free years; a small claim can cost you more in lost bonus than it pays.
- **Renew before the expiry date,** and keep the policy (or a DigiLocker copy) with you.

### Home insurance

Home insurance covers the building and, if chosen, its contents, against fire, floods, storms, landslides and other listed events. Kerala's floods showed how many families had no cover at all. If you own a house, compare a policy's cover for **flood and landslide**, the rebuilding cost it assumes, and the claims process. If you have a home loan, the lender may require it.

### Government schemes: check eligibility

{table(['Scheme', 'Who', 'What', 'As of'], [
    ('PMJJBY', 'Ages 18–50, bank account', '₹2 lakh life cover, ₹436 a year', 'November 2026, check current rules'),
    ('PMSBY', 'Ages 18–70, bank account', '₹2 lakh accidental death or full disability, ₹20 a year', 'November 2026, check current rules'),
    ('KASP (Karunya Arogya Suraksha Padhathi)', 'Eligible poorer families in Kerala', 'Kerala\'s version of Ayushman Bharat PM-JAY: ₹5 lakh family floater a year, with an extra ₹30,000 for members over 60', 'November 2025 report'),
    ('Karunya Benevolent Fund', 'Families with income below ₹3 lakh', 'Up to ₹3 lakh help for critical illnesses', 'November 2025 report'),
    ('Ayushman Vaya Vandana (70+)', 'Seniors aged 70+', 'Up to ₹5 lakh a year elsewhere; reported as **not implemented in Kerala "for the time being"**', 'November 2025 report; check current status'),
    ('Medisep', 'Kerala government employees and pensioners', 'Module 14', 'February 2026'),
])}

Sources: {link('pmjjby', 'scheme page')}; {link('om-seniors', 'Onmanorama, November 2025')} for KASP, Karunya and Vaya Vandana. Eligibility for KASP and Karunya depends on lists and income limits; check at a nearby empanelled hospital's helpdesk, an Akshaya centre or the local health office, with your ration card and Aadhaar.

### Schemes plus private cover

Government schemes are a valuable base, especially for parents. They may not cover every hospital or every treatment, so many families add a private policy or a super top-up when they can afford it.
""",
    example=f"""
**Joseph and Mary**, Anu's retired neighbours, had no health insurance: "too expensive at our age". Anu helped them check three things in one afternoon:

1. Their bank statement showed no PMJJBY or PMSBY debits. Joseph, at 66, is too old for PMJJBY but still within PMSBY's age range, so he enrolled at his bank for ₹20 a year.
2. Their ration card category made them eligible to check KASP at the helpdesk of an empanelled hospital in Vatakara; the helpdesk confirmed they were covered, which they hadn't known.
3. They asked about Vaya Vandana, which friends in Tamil Nadu had mentioned. As of the November 2025 report it wasn't implemented in Kerala, so they noted it to check again later.

Their remaining gap: KASP covers listed treatments at empanelled hospitals. Their son agreed to look at a senior citizen policy with a co-payment, using the checklist from FIN-M07-L03.
""",
    resources=[
        ('pmjjby', 'PMSBY and PMJJBY: ages, cover, premium and how to enrol', '10 minutes'),
        ('om-seniors', 'Kerala\'s options for seniors: KASP, Karunya Benevolent Fund, Vaya Vandana status', '15 minutes'),
        ('tg-motor', 'Motor insurance basics: third-party cover and add-ons', '10 minutes'),
    ],
    steps=[
        'Check your bank statements around June for PMJJBY (₹436) and PMSBY (₹20) debits. Note whether you, your parents and your spouse are enrolled.',
        'If eligible and not enrolled, enrol in PMSBY through your bank (it costs ₹20 a year), or write when you will.',
        'Check whether your family is eligible for KASP or other schemes, using your ration card, at an empanelled hospital helpdesk, an Akshaya centre or the local health office.',
        'If you own a vehicle, check its policy: third-party valid? own-damage? expiry date? no-claim bonus?',
        'If your family owns a house, write whether it is insured against flood and landslide.',
        'Add all of this to your Insurance tab.',
    ],
    proof='Your updated Insurance tab with government schemes, vehicle and home cover status, and proof of one action (an enrolment acknowledgement or a scheme eligibility check), saved in 07 Insurance.',
    templates=[
        ('family scheme check', """
Person,Age,PMJJBY (18-50)?,PMSBY (18-70)?,KASP eligible?,Other scheme (Medisep etc.),Private health cover?,Accident cover?,Action and date
""", 'csv'),
        ('vehicle and home cover check', """
Vehicle: ____  Third-party valid until: ____  Own-damage? Yes/No  No-claim bonus: ___%  Renewal reminder set? Yes/No
House: ____  Insured? Yes/No  Covers flood and landslide? Yes/No  Contents covered? Yes/No  Sum insured ₹____
""", ''),
    ],
    mistakes=[
        ('Assuming parents are covered "by some government scheme".', 'Check eligibility in writing; many families find out only at the hospital.'),
        ('Driving with lapsed third-party cover.', 'It is illegal and leaves you personally liable for injuries you cause.'),
        ('Ignoring accident cover.', 'Disability stops income without stopping costs, and health insurance doesn\'t replace income.'),
        ('Claiming small vehicle damage.', 'You may lose a no-claim bonus worth more than the claim.'),
    ],
    quiz=[
        {'q': 'What does PMSBY cost and cover, as of November 2026?', 'o': ['₹20 a year for ₹2 lakh accidental death or full disability cover', '₹436 a year for life cover', 'Free health insurance', '₹1,000 a year for vehicle cover'], 'a': 'A', 'why': 'PMSBY is the ₹20 accident cover for ages 18–70 (check current rules).'},
        {'q': 'Which motor cover is compulsory by law?', 'o': ['Third-party cover', 'Own-damage cover', 'Engine protection', 'None'], 'a': 'A', 'why': 'Third-party cover is required for every vehicle used in a public place.'},
        {'q': 'What did a November 2025 report say about Ayushman Vaya Vandana in Kerala?', 'o': ['Not implemented in Kerala for the time being', 'Fully implemented with ₹10 lakh cover', 'Only for government employees', 'Replaced by Medisep'], 'a': 'A', 'why': 'Check its current status before relying on it.'},
        {'q': 'Why have accident cover if you already have health insurance?', 'o': ['Health insurance pays hospital bills, not lost income from disability', 'It isn\'t needed', 'Health insurance excludes all accidents', 'Accident cover is compulsory'], 'a': 'A', 'why': 'Disability can stop income for a long time; accident cover pays a lump sum.'},
    ],
    study='The PMSBY/PMJJBY page, Kerala\'s senior health cover options and motor insurance basics',
    action='Check government schemes for your family, enrol in one if eligible, and check vehicle and home cover',
)

L5 = lesson(
    M, 5,
    title='Claims and complaints: getting what you paid for',
    weeks=(14, 14), hours=1.5,
    outcome='Follow the cashless and reimbursement claim steps, keep the right documents, and escalate a rejected claim to the insurer, Bima Bharosa and the Insurance Ombudsman.',
    split='20 minutes reading, 20 minutes resources, 50 minutes action',
    core=f"""
Insurance is only as good as the claim. Most claim problems come from missing documents, late intimation or undisclosed facts, and most can be avoided with preparation.

### Health claims: cashless

1. At a **network hospital**, show your health card or policy number at the insurance desk.
2. For a **planned** admission, the hospital sends a pre-authorisation request in advance; for an **emergency**, as soon as possible after admission. Tell your insurer too.
3. Under IRDAI's 2024 rules, the insurer must decide on cashless requests **within one hour**, and give final authorisation **within three hours** of the hospital's discharge request ({link('om-cashless', 'Outlook Money')}).
4. At discharge, you pay only what isn't covered (co-payment, non-medical items, room rent excess). Ask for an itemised bill.

### Health claims: reimbursement

At a non-network hospital, you pay first and claim later. Keep originals: discharge summary, final bill with breakup, payment receipts, prescriptions, test reports, pharmacy bills, and your bank details. Intimate the insurer quickly and submit within the time the policy states.

### Life claims

The nominee informs the insurer and submits the claim form, the death certificate, the policy document (or details), ID and address proof, bank details, and medical or police records if asked. Claims go faster when the family **knows the policy exists** and where the papers are (Module 13).

### When a claim is rejected or cut

IRDAI's rules say a claim rejection must be approved by the insurer's claims review committee ({link('bu-health', 'summary of the 2024 rules')}). Ask for the **reason in writing**, then:

1. **Complain to the insurer's grievance officer** in writing (email is fine). Keep copies.
2. **Bima Bharosa**, IRDAI's portal, lets you register and track a complaint against an insurer; it says complaints are attended to within 14 days, and it never asks for payments ({link('bima-bharosa', 'Bima Bharosa')}).
3. **The Insurance Ombudsman**, free: if the insurer doesn't reply within a month or you are unhappy with the reply, you can complain **within one year**, for claims up to **₹50 lakh** ({link('ins-ombudsman', 'Council for Insurance Ombudsmen')}). There is an office for Kerala; find yours on the site. If an insurer doesn't implement an ombudsman award within 30 days, it must pay the policyholder ₹5,000 a day ({link('om-cashless', 'Outlook Money')}).
4. Consumer commissions and courts remain options for larger disputes.

### Beware of claim "helpers" and fake refunds

Fraudsters call people after hospital stays offering to "speed up" claims or pay "pending bonuses", asking for fees or OTPs. Bima Bharosa itself warns that it never asks for money. Deal only with your insurer's official channels.
""",
    example=f"""
**Fathima's** mother had a gall bladder surgery at a network hospital in Kozhikode. The cashless request went in at admission; approval came within the hour. At discharge, the insurer cut ₹14,200 from the ₹1,36,000 bill: ₹6,000 for "non-medical items" and ₹8,200 for "proportionate deduction" because the room cost more than the policy's limit.

Fathima asked for the deduction details in writing. The non-medical items (gloves, admission kit) were genuinely excluded. But the room had been the only one available at admission, which the hospital confirmed in a letter. She emailed the insurer's grievance officer with the letter; when there was no reply in two weeks, she registered a complaint on Bima Bharosa. The insurer reviewed it and paid back the ₹8,200 within a month.

Her lessons for the family's Insurance tab: keep the policy wording on the phone, ask about room categories at admission, and get everything in writing.
""",
    resources=[
        ('om-cashless', 'The cashless and discharge timelines and other policyholder rights', '10 minutes'),
        ('bima-bharosa', 'How to register and track a complaint against an insurer', '10 minutes'),
        ('ins-ombudsman', 'When and how to approach the Insurance Ombudsman; find the office for Kerala', '15 minutes'),
    ],
    steps=[
        'For each health policy in your family, save the insurer\'s claim helpline, the TPA (if any) and the policy number (last four digits in your notes) in your phone.',
        'Make a claim kit: a folder (physical and in DigiLocker or Drive) with policy documents, health cards, ID copies and the claim steps from this lesson.',
        'Write down your nearest two network hospitals and their insurance desk numbers.',
        'Fill in the claim escalation letter template with your details, ready to adapt.',
        'Tell one family member where the claim kit is and how cashless works.',
    ],
    proof='A photo or screenshot of your claim kit contents (numbers covered), your saved helplines and the prepared escalation letter, saved in 07 Insurance.',
    templates=[
        ('claim kit checklist', """
[ ] Policy document / Customer Information Sheet for each policy
[ ] Health cards (photo on phone too)
[ ] Insurer and TPA claim helplines saved
[ ] Two nearest network hospitals and their insurance desk numbers
[ ] ID and address proof copies of everyone covered
[ ] Bank details for reimbursement (cancelled cheque)
[ ] This lesson's cashless and reimbursement steps
[ ] Nominee details for life policies, and nominees know the policies exist
""", ''),
        ('claim escalation letter', """
To: The Grievance Redressal Officer, ____ (insurer)
Subject: Review of claim number ____ under policy number ____
I received your decision dated ____ rejecting / reducing my claim by ₹____ for the reason: "____".
I request a review because: ____ (facts, with documents attached: ____).
Please reply in writing. If I don't receive a satisfactory reply, I will approach Bima Bharosa and the Insurance Ombudsman.
Name, phone, email, date
""", ''),
    ],
    mistakes=[
        ('Not reading the reason for a rejection.', 'Ask for it in writing; many rejections can be fixed with a missing document.'),
        ('Missing claim deadlines.', 'Intimate early and submit within the policy\'s time limit.'),
        ('Paying "agents" to speed up claims.', 'Insurers and IRDAI\'s portal never ask for such payments; it is a fraud.'),
        ('Giving up after the first "no".', 'The grievance officer, Bima Bharosa and the ombudsman exist for exactly this, and they are free.'),
    ],
    quiz=[
        {'q': 'Your claim of ₹3 lakh was rejected and the insurer didn\'t reply to your complaint for a month. Where can you go free, within a year?', 'o': ['The Insurance Ombudsman', 'Only a lawyer', 'Nowhere', 'A loan app'], 'a': 'A', 'why': 'The ombudsman handles complaints up to ₹50 lakh, free, within one year.'},
        {'q': 'What is Bima Bharosa?', 'o': ['IRDAI\'s portal to register and track complaints against insurers', 'A new insurance policy', 'A claim agent you pay', 'A bank account'], 'a': 'A', 'why': 'It is IRDAI\'s grievance portal, and it never asks for payments.'},
        {'q': 'For a reimbursement claim, which document is essential?', 'o': ['The discharge summary and itemised final bill', 'Your PAN card only', 'A photo of the hospital', 'Your credit report'], 'a': 'A', 'why': 'The insurer needs the medical record and the bill breakup to pay.'},
        {'q': 'Someone calls offering to release your "pending claim bonus" for a small fee. What is it?', 'o': ['A fraud: deal only with the insurer\'s official channels', 'A normal IRDAI process', 'A tax refund', 'A no-claim bonus'], 'a': 'A', 'why': 'Insurers and regulators don\'t collect fees this way.'},
    ],
    study='Policyholder rights on claims, the Bima Bharosa portal and the Insurance Ombudsman process',
    action='Build a claim kit, save helplines and network hospitals, and prepare an escalation letter',
)

LESSONS = [L1, L2, L3, L4, L5]

MODULE = module(
    M,
    title='Insurance',
    weeks=(13, 14), hours=10,
    overview="""
Protect yourself and your family from the big money shocks: illness, death, disability, accidents and damage, with the right cover, honestly compared and never bought as an investment.

One hospital bill or one death can undo years of careful saving. This module shows which risks to insure and which to carry yourself, why insurance and investment should be kept apart, how much term and health cover a family like yours needs, and how to read the fine print that decides claims.

You won't buy anything in this module. You will list every policy your family has, compare real policies with checklists, check government schemes in Kerala, and build a claim kit. The result is your **insurance checklist**, one of the eight parts of your final plan, ready for when you decide to buy.
""",
    outcomes=[
        'Decide which risks to insure and calculate the real return on bundled policies',
        'Calculate life cover needs and compare term policies without buying',
        'Read health policy terms: floater, super top-up, waiting periods, room rent, co-pay',
        'Check eligibility for PMJJBY, PMSBY, KASP and other schemes; understand motor and home cover',
        'Follow claim steps and escalate to Bima Bharosa and the Insurance Ombudsman',
    ],
    lessons=LESSONS,
    project='My insurance checklist and comparison, done without buying',
    project_steps=[
        'Complete the Insurance tab: every policy and scheme for you and your family, with gaps marked.',
        'Attach your two comparisons: two health policies (20-question checklist) and three term quotes (or your "not needed yet" note).',
        'Write your insurance plan: what to buy, for whom, how much, in what order and roughly when, with the premium added to your budget as a sinking fund.',
        'Write one decision about any existing bundled policy (continue, paid-up or surrender), with the numbers behind it.',
        'Show the plan and the claim kit to a family member.',
    ],
    project_proof='Your Insurance tab, the two comparisons and your written insurance plan, saved in 07 Insurance.',
    rubric=[
        ('Inventory', 'Not done', 'Your own policies only', 'Every policy and scheme in the family, with gaps marked'),
        ('Life cover', 'No calculation', 'Rule of thumb only', 'Needs-based and rule of thumb, with a chosen amount and term'),
        ('Health cover', 'Not compared', 'Compared on premium', 'Compared with the 20-question checklist, decision written'),
        ('Schemes', 'Not checked', 'Some checked', 'PMJJBY, PMSBY, KASP and others checked for everyone'),
        ('Claims', 'No plan', 'Helplines saved', 'Claim kit ready and a family member briefed'),
    ],
    short=[
        'List every family policy in the Insurance tab (FIN-M07-L01).',
        'Fill in the 20-question checklist for one health policy (FIN-M07-L03).',
        'Check PMJJBY and PMSBY enrolment for yourself and your parents (FIN-M07-L04).',
        'Save insurer helplines and the ombudsman link (FIN-M07-L05).',
    ],
    flashcards=[
        ('Insurance is for…', 'Large losses you couldn\'t afford, not small ones and not investment.'),
        ('Term insurance', 'Pure life cover for a term; pays the nominee on death, nothing on survival.'),
        ('Life cover rule of thumb', '10 to 15 times annual income; check with a needs-based calculation.'),
        ('Super top-up', 'Pays once the year\'s total claims cross the deductible; cheap way to add cover.'),
        ('Pre-existing disease waiting, 2024 rules', 'Maximum 36 months; moratorium after 60 months of continuous cover.'),
        ('Cashless decision time', 'Within one hour; discharge authorisation within three hours.'),
        ('PMJJBY and PMSBY', '₹436 a year for ₹2 lakh life cover (18–50); ₹20 a year for ₹2 lakh accident cover (18–70).'),
        ('Insurance Ombudsman', 'Free; within one year; claims up to ₹50 lakh; after the insurer replies or a month passes.'),
    ],
    mistakes=[
        ('Buying insurance to save tax or "get money back".', 'Buy protection for protection. Invest separately.'),
        ('Buying under pressure from a relative or colleague.', 'Use the checklists; a good policy is still good next week.'),
        ('Keeping policies secret.', 'If your family doesn\'t know a policy exists, they can\'t claim it.'),
    ],
    project_week=14,
)
