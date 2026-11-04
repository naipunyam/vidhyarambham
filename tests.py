"""Baseline and final test materials: two parallel forms (A at the start,
B at the end) of the list-recall, reading and digit-span tests, plus the
learning-habits rating. All passages are original fiction written for this
course, so nobody has an advantage from prior knowledge."""

import hashlib
import random

LIST_A = ['umbrella', 'tiger', 'candle', 'onion', 'bicycle', 'newspaper', 'drum', 'mango', 'ladder', 'pillow',
          'key', 'bucket', 'elephant', 'scissors', 'boat', 'mirror', 'rope', 'coconut', 'kite', 'bottle']
LIST_B = ['hammer', 'lion', 'lantern', 'garlic', 'scooter', 'envelope', 'flute', 'jackfruit', 'spade', 'blanket',
          'lock', 'basket', 'peacock', 'needle', 'train', 'comb', 'chain', 'pumpkin', 'balloon', 'cup']
assert len(LIST_A) == len(LIST_B) == 20 and not set(LIST_A) & set(LIST_B)

PASSAGE_A_TITLE = 'The reading room at Puthenpura'
PASSAGE_A = """
Puthenpura is a small village on the bank of a slow, brown river. For many years it had a post office, two tea shops, a mosque, a temple and a school that went up to class seven, but no place where an adult could sit and read. Devaki, a mathematics teacher who retired in 1998, decided to change that.

She began with what she had: forty-two books from her own shelves and a promise from the owner of an empty ration shop near the bus stop. He let her use the room for nothing, on one condition: it had to be swept every day and locked every night. Devaki wrote the rules on a sheet of chart paper and pinned it beside the door. Members would pay two rupees a month. Books could be taken home for one week. Anyone who returned a book late would have to read a page of it aloud to the others on Sunday evening.

In the first month only nine people joined. Most of them were retired men who came for the newspaper, not the books. Devaki did not mind. She noticed that they argued every morning about the news, so she started a small notebook in which anyone could write one question about the day's paper. Every Saturday, she pinned the best question on the wall with the answer underneath. Within a few months, the notebook had become the most read item in the room.

The first real problem came during the monsoon of 1999. The room flooded twice, and termites attacked the wooden shelves. About a third of the books were damaged. A carpenter from the next village suggested raising the shelves on bricks and painting the legs with old engine oil. Devaki's former students collected money for the bricks and the paint, and the shelves have stood on the same bricks ever since.

The second change came from an unexpected direction. In 2001 the bus timetable changed, and the last bus to the town now left at seven in the evening instead of five. Women who worked in the town's tailoring shops had a long wait at the bus stop, right outside the reading room. A few of them began to step in while they waited. Devaki started a Thursday group for them, in which each person read one short story and then told it to the others in her own words. By the end of that year, membership had grown to more than eighty, and for the first time most members were women.

Not everything worked. A plan to lend books by post to people in the hills was dropped after a year, because the stamps cost more than the fees. A computer donated in 2006 sat unused for a long time, since no one knew how to repair it when the power supply failed.

Today the reading room has about two thousand books, a wall of old question notebooks and a waiting list for the Thursday group. Devaki still visits on Sundays. When young people ask her how she built it, she says that she did not build anything. "I opened the door," she says, "and then I watched what people did when they came in, and gave them more of that."
"""

QUESTIONS_A = [
    ('Where did the reading room first open?', ['In an empty ration shop near the bus stop', 'In a room of the village school', "In Devaki's house", 'Beside the post office']),
    ('What did a member who returned a book late have to do?', ['Read a page of it aloud on Sunday evening', 'Pay a fine of two rupees', 'Sweep the room for a week', 'Give up borrowing for a month']),
    ('What became the most read item in the room within a few months?', ["The notebook of questions about the day's newspaper", 'The newspaper itself', 'The chart of rules', 'A book of short stories']),
    ('How were the shelves protected after the 1999 monsoon?', ['They were raised on bricks and the legs painted with old engine oil', 'They were replaced with steel shelves', 'They were moved to a higher room', 'They were wrapped in plastic sheets']),
    ('Why did more women start using the reading room in 2001?', ['A change in the bus timetable left them waiting right outside it', 'Devaki put up notices in the tailoring shops', 'The fee was cut for women', 'The school asked them to come']),
    ('Why was the plan to lend books by post dropped?', ['The stamps cost more than the fees', 'Books were lost in the post', 'People in the hills did not want books', 'The post office closed']),
    ("Which statement best matches Devaki's own view of how the reading room grew?", ['She watched what members did and gave them more of it', 'She followed a detailed plan written in 1998', 'Her former students did most of the work', 'The donated computer brought in new members']),
    ('Which of these is NOT stated in the passage?', ['The reading room received a government grant', 'Membership passed eighty by the end of 2001', 'The donated computer was unused after its power supply failed', 'Devaki was a mathematics teacher']),
]

PASSAGE_B_TITLE = 'The ferry at Kannankadavu'
PASSAGE_B = """
For thirty-one years, the only way to cross the river at Kannankadavu without a long walk to the bridge downstream was Ummer's ferry. The ferry was a wide country boat that could carry twelve people, or eight people and two bicycles. Ummer pushed it across with a long bamboo pole, and on a calm day the crossing took about six minutes.

He had taken over the ferry from his uncle in 1987. The panchayat owned the crossing and leased it every three years to whoever offered the most money. Ummer kept the lease by doing one thing better than anyone else: he was never late. Schoolchildren, fish sellers and office workers set their watches by the first crossing at six in the morning. He charged fifty paise a person when he started and three rupees by the end, and children in school uniform always crossed free. On Fridays, when the market on the far bank was busiest, he made an extra crossing every half hour until noon, and his wife sold boiled peanuts in paper cones to the people waiting at the landing.

The monsoon was the hardest season. When the water rose above a mark he had painted on a coconut tree, Ummer stopped the ferry, however many people were waiting. Some passengers shouted at him. Once, in 1994, a man offered him a hundred rupees to cross in a flood. Ummer refused. That evening a branch the size of a lorry came down the river past the exact spot where the boat would have been. After that, nobody argued with the coconut tree.

In 2009 the government announced that a bridge would be built at Kannankadavu. Everyone expected Ummer to be angry, since the bridge would end his work. Instead he went to the engineers' office and asked to see the plans. The engineers were surprised; most visitors came only to complain about the noise. He noticed that the bridge would be built about two hundred metres upstream, close to a temple path, so people from his side would still have to walk past his landing to reach it. He used his savings to start a tea stall at the landing, and he began serving tea to the construction workers.

The bridge took six years instead of the two that had been promised. During that time the tea stall slowly became more important than the ferry. Ummer added newspapers, a bench and, later, a small shelf of snacks. When the bridge finally opened in 2015, he sold the boat to a tourism group that wanted it for evening rides.

Not all of his ideas worked. He tried to sell fish from the stall, but the smell kept tea customers away, and he stopped after a month. A plan to rent out bicycles to people crossing the new bridge failed because almost everyone already owned one.

Today his daughter Shabna runs the stall, which now has four tables and a name for the best banana fritters on that stretch of road. Ummer still sits on the bench every morning at six. When people ask whether he misses the ferry, he points at the river and says, "The river did not stop. I only changed which side of it I stood on."
"""

QUESTIONS_B = [
    ('How long did the crossing take on a calm day?', ['About six minutes', 'About ten minutes', 'About two minutes', 'About thirty minutes']),
    ('How did Ummer keep the ferry lease?', ['He was never late', 'He always offered the most money', 'He was related to a panchayat member', 'He carried bicycles free']),
    ('What did Ummer do when the water rose above the mark on the coconut tree?', ['He stopped the ferry', 'He doubled the fare', 'He used a bigger boat', 'He carried only children']),
    ('Why did nobody argue with the coconut tree after 1994?', ['A huge branch came down the river where the boat would have been', 'The panchayat made a new rule', 'Ummer bought a stronger boat', 'The tree was carried away by the flood']),
    ('Why did Ummer start a tea stall at the landing?', ['He saw that people would still walk past his landing to reach the new bridge', 'The engineers asked him to feed their workers', 'His uncle had once run a tea stall there', 'The tourism group paid him to start it']),
    ('How long did the bridge take to build?', ['Six years', 'Two years', 'Three years', 'Nine years']),
    ('Why did the bicycle rental plan fail?', ['Almost everyone already owned a bicycle', 'The bicycles were stolen', 'Bicycles were not allowed on the bridge', 'It cost too much to start']),
    ('Which of these is NOT stated in the passage?', ['Ummer received compensation from the government for losing the ferry', 'Children in school uniform crossed free', 'The boat was sold to a tourism group', "Ummer's daughter now runs the stall"]),
]


def words(text):
    return len(text.split())


WORDS_A = words(PASSAGE_A)
WORDS_B = words(PASSAGE_B)


def mcq(questions, seed):
    """Fixed shuffled order; the first option given is the correct one."""
    out, key = [], []
    for i, (q, opts) in enumerate(questions, 1):
        rng = random.Random(int(hashlib.md5((seed + q).encode('utf-8')).hexdigest(), 16))
        order = list(range(len(opts)))
        rng.shuffle(order)
        shown = [opts[k] for k in order]
        letter = 'ABCD'[order.index(0)]
        out.append(f'{i}. {q}\n' + '\n'.join(f'    - {chr(65 + j)}) {o}' for j, o in enumerate(shown)))
        key.append(f'{i}{letter}')
    return '\n'.join(out), ', '.join(key)


def _digits(seed, length):
    rng = random.Random(seed)
    while True:
        seq = rng.sample('0123456789', length)
        d = [int(y) - int(x) for x, y in zip(seq, seq[1:])]
        ok = all(abs(k) != 1 for k in d) and all(p != q for p, q in zip(d, d[1:]))
        if ok:
            return ' '.join(seq)


def digit_sets(form):
    fwd = [(n, _digits(f'{form}-f-{n}-{t}', n)) for n in range(3, 10) for t in (1, 2)]
    bwd = [(n, _digits(f'{form}-b-{n}-{t}', n)) for n in range(2, 9) for t in (1, 2)]
    return fwd, bwd


HABITS = [
    'When I study, I test myself more than I reread',
    'I review topics on a schedule, not only just before an exam',
    'I mix different types of questions when I practise',
    'I explain ideas in my own words, aloud or on paper',
    'I use pictures, maps, timelines or diagrams with my notes',
    'I review flashcards with spaced repetition every day',
    'I can study for 45 minutes without checking my phone',
    'I start study sessions on time, without long delays',
    'I know which topics I really know and which I only recognise',
    'I keep a record of my mistakes and fix them',
    'I practise with previous-year questions and timed tests',
    'I sleep at least 7 hours on most nights',
    'I have a written study plan for my exam',
    'I can learn a new skill on my own with free resources',
    'I check facts from AI tools or social media against a reliable source',
]
