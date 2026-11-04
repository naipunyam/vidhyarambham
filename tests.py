"""Baseline and final knowledge quizzes (two parallel forms) and a skills
self-rating for the Kerala real estate course. Rates are as of November 2026."""

import hashlib
import random


def q(text, right, wrong, why):
    return {'q': text, 'o': [right] + wrong, 'why': why}


QUIZ_A = [
    q('How many square feet are in one cent?', 'About 435.6 sq ft', ['100 sq ft', '1,000 sq ft', '4,356 sq ft'], 'One cent is one-hundredth of an acre: 43,560 ÷ 100 = 435.6 sq ft (RE-M03-L01).'),
    q('One are equals about how many cents?', 'About 2.47 cents', ['10 cents', '1 cent', '0.5 cents'], 'One are is 100 square metres, about 2.47 cents (RE-M03-L01).'),
    q('What does an encumbrance certificate (EC) mainly show?', 'Registered transactions on the property, such as sales and mortgages, for the period searched', ['That the property has no flood risk', 'The government fair value', 'That the building has a permit'], 'An EC lists registered transactions; it does not prove there are no unregistered claims or court cases (RE-M06-L01).'),
    q('A seller says "the agreement for sale is enough; we don\'t need a sale deed." What is true?', 'Ownership passes only by a registered sale deed; an agreement for sale does not transfer ownership', ['An agreement for sale transfers ownership', 'A notarised agreement is the same as registration', 'Only flats need a sale deed'], 'Section 54 of the Transfer of Property Act (RE-M04-L01).'),
    q('As of November 2026, what are the usual stamp duty and registration fee for a sale deed in Kerala?', 'Stamp duty 8% and registration fee 2% of the higher of price or fair value', ['1% and 1%', '5% and 5%', 'A fixed Rs 5,000'], 'Check current rules before every deal (RE-M04-L01).'),
    q('Who must register with K-RERA under the RERA Act?', 'Real estate agents who facilitate sales in registrable projects, and promoters of such projects', ['Only buyers', 'Only banks', 'Nobody in Kerala'], 'Agents need registration and must quote the number (RE-M10-L01).'),
    q('Land shown in the paddy and wetland data bank:', 'Cannot be freely filled or built on; conversion needs legal approval and may not be allowed', ['Can be built on after paying land tax', 'Is always government land', 'Is the best land for a quick house'], 'The Kerala Conservation of Paddy Land and Wetland Act (RE-M04-L03).'),
    q('A buyer pays Rs 60 lakh for a house. Who deducts TDS, and roughly how much?', 'The buyer deducts 1% (about Rs 60,000) and deposits it for the seller', ['The seller pays 10%', 'The bank pays 5%', 'No TDS on houses'], 'TDS applies when the consideration or stamp duty value is Rs 50 lakh or more (RE-M09-L01).'),
    q('A house costs Rs 40 lakh and rents for Rs 12,000 a month. What is the gross rental yield?', 'About 3.6%', ['About 12%', 'About 30%', 'About 0.3%'], 'Rs 12,000 × 12 = Rs 1.44 lakh; ÷ Rs 40 lakh = 3.6% (RE-M08-L02).'),
    q('Which is the safest way to take a token advance?', 'By bank transfer, with a signed receipt stating the terms', ['In cash with no receipt', 'In cash with a verbal promise', 'Through the broker\'s personal cash'], 'Cash limits and proof matter (RE-M13-L02, RE-M04-L05).'),
    q('When is an advocate\'s title opinion most important?', 'Before signing the agreement for sale and paying a large advance', ['After registration', 'Only for flats', 'Never, the EC is enough'], 'Due diligence comes before commitment (RE-M06-L03).'),
    q('Which is a warning sign of a possible fraud?', 'The seller insists on a quick cash deal through a power of attorney holder and refuses to show originals', ['The seller provides a 30-year EC', 'The seller asks for payment by bank transfer', 'The seller asks for an advocate to check the title'], 'Forged or misused powers of attorney are a common fraud (RE-M21-L01).'),
]

QUIZ_B = [
    q('A plot is 10 cents. About how many square feet is that?', 'About 4,356 sq ft', ['About 1,000 sq ft', 'About 435 sq ft', 'About 43,560 sq ft'], '10 × 435.6 = 4,356 sq ft (RE-M03-L01).'),
    q('A deed says 4.05 ares. About how many cents is that?', 'About 10 cents', ['About 4 cents', 'About 40 cents', 'About 1 cent'], '4.05 × 2.47 ≈ 10 cents (RE-M03-L01).'),
    q('What does the thandaper (thandaper number) record?', 'The landholder\'s account in the village revenue records, used for land tax', ['The building permit number', 'The bank loan number', 'The sale price'], 'It links the owner to land-tax records (RE-M03-L02).'),
    q('An EC for 13 years shows no entries. What can you safely conclude?', 'Only that no registered transactions appear for those 13 years; older history and unregistered claims still need checking', ['The title is perfect', 'There are no court cases', 'The land is not paddy land'], 'Search 30+ years and check other sources (RE-M06-L01).'),
    q('A sale deed must be presented for registration within how long of signing?', 'Within four months', ['Within one week', 'Within ten years', 'There is no time limit'], 'Section 23 of the Registration Act (RE-M04-L01).'),
    q('Price Rs 30 lakh; fair value Rs 34 lakh. On what value is stamp duty calculated?', 'Rs 34 lakh, the higher of the two', ['Rs 30 lakh', 'Rs 32 lakh, the average', 'Rs 4 lakh, the difference'], 'Duty is on the higher of price or fair value (RE-M04-L01).'),
    q('What can a real estate agent registered with K-RERA NOT do?', 'Give a legal title opinion or draft and register deeds without the required licence', ['Market a property with the owner\'s mandate', 'Arrange site visits', 'Collect commission by bank transfer with an invoice'], 'Legal work needs an advocate; deeds need a licensed document writer or advocate (RE-M10-L01).'),
    q('Building near the coast may need clearance under which rules?', 'Coastal Regulation Zone (CRZ) rules', ['Rent control law', 'Benami law', 'RERA agent rules'], 'CRZ 2019 and Kerala\'s approved coastal plan (RE-M04-L04).'),
    q('Net operating income is Rs 1.2 lakh a year on a Rs 30 lakh property. What is the cap rate?', '4%', ['40%', '0.4%', '12%'], '1.2 ÷ 30 = 4% (RE-M08-L02).'),
    q('GST on the resale of a completed house with an occupancy certificate is:', 'Not charged', ['18%', '12%', '5% always'], 'GST applies to under-construction property, not resale (RE-M09-L02).'),
    q('Which step comes right after registration of a sale deed?', 'Mutation of the land records (pokkuvaravu) into the buyer\'s name', ['Paying the token advance', 'Signing the agreement for sale', 'Applying for an EC for the next 30 years'], 'Mutation updates revenue records (RE-M14-L03).'),
    q('A layout of plots is sold with "approval coming soon". What is the main risk?', 'Unapproved layouts may not get building permits, roads or utilities, and buyers can lose money', ['Prices always rise', 'No risk if the land is cheap', 'Banks prefer unapproved layouts'], 'Unapproved layouts are a common trap (RE-M16-L01, RE-M21-L01).'),
]
assert len(QUIZ_A) == len(QUIZ_B) == 12

SKILLS = [
    'I can explain the steps of a property sale from token advance to mutation.',
    'I can read a sale deed and an EC and point out what to check.',
    'I can convert cents, ares and square feet without a calculator app.',
    'I can find a property\'s fair value on the official portal.',
    'I can calculate the full cost of buying a property.',
    'I can calculate rental yield and cap rate.',
    'I know which tasks need an advocate, a surveyor, a CA or a document writer.',
    'I can write an honest listing and market it for free.',
    'I know at least five local brokers or property professionals.',
    'I can spot at least five common real estate frauds.',
]


def mcq(questions, form):
    qs, key = [], []
    for i, item in enumerate(questions, 1):
        rng = random.Random(int(hashlib.md5((form + item['q']).encode('utf-8')).hexdigest(), 16))
        order = list(range(len(item['o'])))
        rng.shuffle(order)
        opts = [item['o'][k] for k in order]
        letter = 'ABCD'[order.index(0)]
        qs.append(f"{i}. {item['q']}\n" + '\n'.join(f'    - {chr(65 + j)}) {o}' for j, o in enumerate(opts)))
        key.append(f"{i}. **{letter}.** {item['why']}")
    return '\n'.join(qs), '\n'.join(key)
