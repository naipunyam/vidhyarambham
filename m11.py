"""Module 11: Memory techniques."""
from common import lesson, module, link, fence, table

M = 11

L1 = lesson(
    M, 1,
    outcome='Use chunking, acronyms, acrostics and stories to remember PSC lists, and know honestly when mnemonics help and when they don\'t.',
    split='20 minutes reading, 20 minutes resources, 40 minutes action plus short recalls over three days',
    core=f"""
### What mnemonics are for

A **mnemonic** is a trick that gives information without its own structure (a list, an order, a number) something to hold on to. PSC is full of such information: the five writs, the order of Kerala's districts, the three east-flowing rivers, the Malayalam Jnanpith winners.

Be honest about what they can and can't do:

- They are good for **arbitrary lists and orders**, where there is nothing to understand.
- They are **not** a substitute for understanding. Use Module 8 for reasons and processes.
- They need **practice**. A mnemonic you made once and never rehearsed is forgotten like anything else. Combine every mnemonic with spaced retrieval (cards or the Revision tab).
- The evidence varies by technique. Dunlosky and colleagues rated the **keyword mnemonic** (linking a word to a sound-alike image, mostly studied for vocabulary) as **low utility**: it can work, but it takes time and the benefit may not last ({link('dunlosky-aft', 'Dunlosky, 2013')}). The memory palace (next lesson) has much stronger training evidence.

### Chunking

Working memory holds about four chunks (Module 1). **Chunking** groups items into a few meaningful units. Kerala's 14 districts from north to south are hard as one list, easier as four chunks:

{table(['Chunk', 'Districts'], [
    ('North (4)', 'Kasaragod, Kannur, Wayanad, Kozhikode'),
    ('North-central (3)', 'Malappuram, Palakkad, Thrissur'),
    ('Central (4)', 'Ernakulam, Idukki, Kottayam, Alappuzha'),
    ('South (3)', 'Pathanamthitta, Kollam, Thiruvananthapuram'),
])}

Four chunks of three or four are easy to hold; then you learn each chunk on its own.

### Acronyms and acrostics

An **acronym** makes a word from first letters; an **acrostic** makes a sentence. Silly, local sentences are easier to remember:

- **The five writs:** Habeas corpus, Mandamus, Prohibition, Certiorari, Quo warranto. Acrostic: **"Hari's Mother Prepared Chakka Quickly."**
- **Kerala's three east-flowing rivers:** Kabani, Bhavani, Pambar. Acrostic: **"Kerala's Big Payasam."**

Malayalam acrostics work just as well, often better for Malayalam speakers. Make your own.

### Stories

A **story** links items in order through a vivid chain of events. The order of four landmarks of the Kerala renaissance (1888, 1903, 1924, 1936): *A guru places a sacred stone by a river (the Aruvippuram consecration); his followers form a club to spread his message (the SNDP Yogam); a crowd walks the roads around a temple demanding the right to use them (the Vaikom Satyagraha); and finally the temple doors are thrown open to all (the Temple Entry Proclamation).* The story holds the order; your cards hold the years.

### Rules for good mnemonics

1. **Vivid, personal, a little absurd:** you remember the strange and the funny.
2. **Check the facts** before you build the mnemonic; a mnemonic for a wrong fact is worse than none.
3. **Rehearse it:** recall the list from the mnemonic three times on the first day, then on your review days.
4. **Put it on a card:** the mnemonic on the back of the card that asks for the list.
""",
    example="""
**Joseph sir**'s study group spent one evening making mnemonics for lists that kept appearing in previous papers. Each member made one, and the group voted for the most memorable.

Vinod's acrostic for the writs, "Hari's Mother Prepared Chakka Quickly", won because everyone in the group could picture the jackfruit. Sreeja chunked the districts and drew the four chunks as four colours on a hand-drawn map. Joseph sir, the Malayalam teacher, made a Malayalam acrostic for a list of literary works, which the group found easiest of all.

They tested themselves three days later without warning. Lists with a mnemonic: 9 out of 10 recalled on average. Lists they had only read: 5 out of 10. One member's mnemonic turned out to be built on a wrong fact from a forward; the group fixed the fact and rebuilt it, and Joseph sir made "check before you build" the group rule.
""",
    evidence=[
        ('Chunking items into a few meaningful groups', 'strong', 'Working memory holds about four chunks (OpenStax 8.1; CESE review); grouping makes lists manageable.'),
        ('The keyword mnemonic', 'limited', 'Rated low utility by Dunlosky and others (2013): it can work, but takes time and the benefit may not last.'),
        ('Acronyms, acrostics and stories for lists', 'limited', 'Widely used, with mixed research; they help most when rehearsed with spaced retrieval.'),
    ],
    resources=[
        ('dunlosky-aft', 'Read the section on the keyword mnemonic and why it was rated low', '10 minutes'),
        ('os-psych-8-1', 'Reread the part on short-term memory capacity', '5 minutes'),
        ('lhtl', 'Optional: the memory videos in Module 3 of Learning How to Learn', 'About 1 hour'),
    ],
    steps=[
        'Choose three lists from your PSC syllabus or previous papers, each with 3 to 15 items. Check every item against your textbook first.',
        'Make one mnemonic of each kind: a chunking scheme for one list, an acronym or acrostic for another, and a story for a list with an order.',
        'Recall each list from its mnemonic three times today, with gaps of at least 10 minutes, and once tomorrow.',
        'On day 3, test yourself on all three lists without looking. Score each.',
        'Add a card for each list in AnkiDroid, with the mnemonic on the back.',
    ],
    proof='Your three checked lists with their mnemonics, the day-3 scores, and a screenshot of the three cards.',
    templates=[
        ('mnemonic builder', """
LIST: ______________________  Items (checked in ______ page ___):
1. ________ 2. ________ 3. ________ 4. ________ 5. ________ 6. ________
Does it have an order I must keep?  yes / no
Technique:  chunking / acronym / acrostic / story / memory palace (LRN-M11-L02)
My mnemonic: _______________________________________________________
Recall from the mnemonic: day 1 x3 [ ][ ][ ]  day 2 [ ]  day 3 test ___/___
Card added (mnemonic on the back): [ ]
""", ''),
        ('should I use a mnemonic?', """
Is there something to understand (a reason, a process)?  -> no mnemonic: explain it (Module 8)
Is it an arbitrary list, order or number?                -> yes, use a mnemonic
Have I checked the facts?                                -> if not, check first
Will I rehearse it on spaced review days?                -> if not, it will fade
""", ''),
    ],
    mistakes=[
        ('Making mnemonics for things you could understand.', 'Reasons and processes need explaining, not tricks.'),
        ('Dull, forgettable mnemonics.', 'Make them vivid, local and a little absurd.'),
        ('Making a mnemonic once and never rehearsing it.', 'Recall from it three times on day 1 and on your review days.'),
        ('Building a mnemonic on a wrong fact.', 'Check the list against your textbook before you build.'),
    ],
    quiz=[
        {'q': 'Which list from the PSC syllabus suits a mnemonic best?', 'o': ['The five writs in order', 'Why the monsoon reaches Kerala first', 'How a money bill passes Parliament', 'Why Directive Principles are not enforceable'], 'a': 'A', 'why': 'An arbitrary list suits a mnemonic; the others need understanding.'},
        {'q': 'How did Dunlosky and colleagues rate the keyword mnemonic?', 'o': ['Low utility: it can work but takes time and may not last', 'High utility for everything', 'Moderate utility for maths', 'They did not review it'], 'a': 'A', 'why': 'The memory palace has stronger training evidence (next lesson).'},
        {'q': 'What does "Hari\'s Mother Prepared Chakka Quickly" help you remember?', 'o': ['Habeas corpus, mandamus, prohibition, certiorari, quo warranto', 'Kerala\'s districts', 'The Fundamental Duties', 'The east-flowing rivers'], 'a': 'A', 'why': 'Each first letter stands for one writ.'},
        {'q': 'What must you do after making a mnemonic?', 'o': ['Rehearse it with spaced recall and put it on a card', 'Never look at it again', 'Share it and forget it', 'Make a second mnemonic for the same list'], 'a': 'A', 'why': 'Mnemonics are forgotten like anything else unless rehearsed.'},
    ],
    study='Dunlosky\'s section on the keyword mnemonic and OpenStax 8.1 on short-term memory capacity',
    action='Build and test three checked mnemonics (chunking, acrostic and story) for PSC lists',
)

L2 = lesson(
    M, 2,
    outcome='Build a memory palace in your own home that holds a real PSC topic, the Fundamental Rights from Article 14 to Article 32, and recall it forwards and backwards after a week.',
    split='20 minutes reading, 20 minutes resources, 50 minutes building plus short recalls over a week',
    core=f"""
### The method of loci

The **memory palace**, or **method of loci** ("places"), is more than two thousand years old. You take a route you know perfectly, such as the way through your own house, pick a series of places (**loci**) along it, and leave a vivid image of one item at each place. To recall, you walk the route in your mind and "see" each image.

It is the main method of memory champions, and it has unusually good training evidence. In a study published in *Neuron*, ordinary adults trained the method of loci in 40 sessions of 30 minutes over six weeks. Their memory improved substantially, the gain was still there four months later, and their brain networks shifted towards those of memory champions ({link('dresler', 'Dresler and others, 2017')}).

Be clear about what it is for: **ordered lists and sets of separate items**. It doesn't create understanding, and it takes practice to become fast.

### Building your palace

1. **Choose a route** you know with your eyes closed: your house from the gate to the backyard works well. Pick **10 to 20 loci** in a fixed order: gate, courtyard, verandah, front door, sitting room, TV, dining table, kitchen, and so on.
2. **Walk it in your mind** forwards and backwards until you know the order without thinking.
3. **Make a vivid image for each item and put it at its locus,** interacting with it. Exaggerate it, make it move, make noise, add smell or humour.
4. **Walk the route to recall** the items, forwards and backwards.
5. **Review on a spaced schedule:** after 10 minutes, 1 day, 3 days and 7 days.

### A worked example: the Fundamental Rights

Here are the first twelve loci of a palace built in a typical house:

{table(['Locus', 'Article', 'Content', 'Image'], [
    ('1. Gate', '14', 'Equality before law', 'A huge weighing scale at the gate: the rich man and the fish seller weigh exactly the same'),
    ('2. Courtyard', '15', 'No discrimination on grounds of religion, race, caste, sex or place of birth', 'One tea kettle in the courtyard pouring for everyone in the queue'),
    ('3. Verandah', '16', 'Equal opportunity in public employment', 'A PSC notification pinned to the verandah pillar: "all may apply"'),
    ('4. Front door', '17', 'Abolition of untouchability', 'The door wide open, an old "keep out" board smashed on the floor'),
    ('5. Sitting room', '18', 'Abolition of titles', 'A crown and a title badge thrown into the dustbin'),
    ('6. TV', '19', 'Six freedoms: speech, assembly, association, movement, residence, profession', 'Six people climbing out of the TV, one shouting into a microphone'),
    ('7. Dining table', '20', 'Protection in respect of conviction for offences', 'A man punished once refusing a second plate of punishment'),
    ('8. Kitchen', '21', 'Protection of life and personal liberty', 'A bird flying free from a cage on the kitchen window'),
    ('9. Store room', '21A', 'Education for children aged 6 to 14', 'A small school bag hanging on the store-room door'),
    ('10. Bedroom', '22', 'Protection against arrest and detention', 'A policeman at the bed showing an arrest memo, a lawyer beside him'),
    ('11. Bathroom', '23', 'No traffic in human beings or forced labour', 'Chains broken on the bathroom floor'),
    ('12. Backyard', '24', 'No employment of children in factories', 'A child flying a kite instead of working in a factory'),
])}

You continue in the garden or a second "floor" for Articles 25 to 28 (freedom of religion), 29 and 30 (cultural and educational rights) and 32 (constitutional remedies). Article 31 is missing because the right to property was removed from this Part in 1978; a locus with an empty chair can mark that.

### Tips

- **One palace per topic** at first. Using the same route for two lists at once causes interference.
- **Numbers** (such as article numbers) can come from the order, as above, or from number images (next lesson).
- **Keep a written plan** of the palace, but recall from your head.
""",
    example="""
**Anu** built her first palace in her family's house in Kakkattil for the Fundamental Rights. She walked the real route once with a notebook: gate, the courtyard with the mango tree, the verandah, the front door, the sitting room, the TV, the dining table, the kitchen, the store room, her bedroom, the bathroom, the backyard well, the coconut tree, the cowshed, the compost pit, the back gate and the lane. Seventeen loci.

She used the images in this lesson for the first twelve and made her own for the rest: a temple, a church and a mosque sharing one cowshed for freedom of religion, and the moon shining over the back gate for Article 32 (she remembered it as "go straight to the top"). She recalled the route after 10 minutes, the next morning, after 3 days and after 7 days.

On day 7 she recalled all 17 loci forwards and 16 backwards. In a 20-question test on Fundamental Rights from previous papers, she scored 17; her pre-module score on similar questions had been 10. She added "Article → locus" cards to AnkiDroid only for the three she had once confused.
""",
    evidence=[
        ('The memory palace (method of loci) for ordered lists', 'strong', 'One of the best-studied mnemonics; Dresler and others (2017) showed large, lasting gains in trained adults.'),
        ('The memory palace for understanding complex topics', 'limited', 'It holds items and their order, not reasons. Combine it with explanation (Module 8).'),
        ('Spaced recall walks of the palace', 'strong', 'Spaced retrieval, rated high utility, applied to the palace.'),
    ],
    resources=[
        ('dresler', 'Read the abstract and the description of the training', '15 minutes'),
        ('lhtl', 'Optional: the memory palace videos in Module 3 of Learning How to Learn', 'About 30 minutes'),
    ],
    steps=[
        'Choose a route you know perfectly (your house is best) and write down 15 to 20 loci in order.',
        'Walk it in your mind forwards and backwards until the order is automatic.',
        'Place the Fundamental Rights (Articles 14 to 32), or another PSC list of 15 or more items that you have checked, along the route: one vivid image per locus. Use the worked example for the first twelve if you choose the Fundamental Rights.',
        'Recall the whole palace forwards and backwards after 10 minutes, 1 day, 3 days and 7 days, without the plan. Score each recall.',
        'On day 7, answer 15 to 20 previous-year questions on the topic and compare with your earlier score, if you have one.',
    ],
    proof='Your palace plan (route, loci and images), the four recall scores forwards and backwards, and the day-7 question score.',
    templates=[
        ('memory palace planner', """
MEMORY PALACE     Topic: ______________________  Route: ______________________
Locus (in order)     Item (checked)                   Image (vivid, moving, funny)
1. ______________    _______________________________  _________________________
2. ______________    _______________________________  _________________________
3. ______________    _______________________________  _________________________
...
20. _____________    _______________________________  _________________________
Recall      10 min   day 1   day 3   day 7
Forwards    ___      ___     ___     ___
Backwards   ___      ___     ___     ___
""", ''),
        ('making images stick', """
Make it BIG, MOVING, NOISY, SMELLY or FUNNY.
Make it INTERACT with the locus (on, in, through, crashing into it).
Use PEOPLE and ANIMALS doing things.
For abstract ideas, use a symbol: scale = equality, cage = liberty, chains = slavery, crown = titles.
""", ''),
    ],
    mistakes=[
        ('A route you don\'t know perfectly.', 'If you hesitate over the order of rooms, the palace fails. Use your own home.'),
        ('Dull images ("a picture of equality").', 'Make every image vivid and interacting with its place.'),
        ('Several items on one locus.', 'One item per locus keeps the order clear.'),
        ('Building it and never walking it again.', 'Recall after 10 minutes, 1, 3 and 7 days, then on review days.'),
        ('Two lists in one palace at the same time.', 'Use a different route for each topic to avoid interference.'),
    ],
    quiz=[
        {'q': 'What did Dresler and others (2017) show?', 'o': ['Six weeks of method-of-loci training gave ordinary adults large, lasting memory gains', 'The memory palace works only for champions', 'Memory cannot be trained', 'Brain-training apps beat the memory palace'], 'a': 'A', 'why': 'The gain lasted four months, and brain networks changed.'},
        {'q': 'What is the memory palace best for?', 'o': ['Ordered lists and sets of separate items', 'Understanding why a law was passed', 'Solving maths problems', 'Speed reading'], 'a': 'A', 'why': 'It holds items and order; understanding needs explanation.'},
        {'q': 'In the worked example, what is at the kitchen locus?', 'o': ['A bird flying free from a cage: Article 21, life and personal liberty', 'A weighing scale: Article 14', 'A school bag: Article 21A', 'Broken chains: Article 23'], 'a': 'A', 'why': 'The cage image stands for liberty.'},
        {'q': 'Why is Article 31 missing from the Fundamental Rights list?', 'o': ['The right to property was removed from Part III in 1978', 'It was never written', 'It is in Part IV', 'It is a Directive Principle'], 'a': 'A', 'why': 'The 44th Amendment (1978) removed it from the Fundamental Rights.'},
    ],
    study='The abstract and training description of Dresler and others (2017)',
    action='Build a 15 to 20 locus memory palace for a PSC topic and recall it over a week',
)

L3 = lesson(
    M, 3,
    outcome='Turn numbers into words with the major system, use a simple peg list, and fix article numbers and dates to their PSC facts with vivid images.',
    split='20 minutes reading, 15 minutes resources, 55 minutes action plus short recalls over three days',
    core=f"""
### Why numbers are hard

PSC asks for many numbers: article numbers, amendment numbers, years, lengths, ranks. Numbers are abstract, so they have no meaning to hook onto (Module 1). Two classic systems turn numbers into pictures.

### A simple peg list

A **peg list** gives each number from 1 to 10 a fixed image that rhymes with it. Learn it once, then "hang" the items of any ordered list on the pegs:

{fence('''1 bun    2 shoe    3 tree    4 door    5 hive
6 sticks 7 heaven  8 gate    9 wine    10 hen''')}

To remember the first five items of a list in order, picture item 1 squashed in a bun, item 2 stuffed in a shoe, item 3 hanging from a tree, and so on. You can make a Malayalam peg list too, from rhymes or shapes that are natural for you.

### The major system

The **major system** turns digits into consonant sounds, then into words. Vowels and the sounds w, h and y are free fillers ({link('major-system', 'Wikipedia: Mnemonic major system')}):

{table(['Digit', 'Sounds', 'Memory hook'], [
    ('0', 's, z', '"z" for zero'),
    ('1', 't, d', 'one downstroke'),
    ('2', 'n', 'two downstrokes'),
    ('3', 'm', 'three downstrokes'),
    ('4', 'r', 'the last sound of "four"'),
    ('5', 'l', 'L is the Roman numeral for 50'),
    ('6', 'j, sh, ch, soft g', 'a reversed J looks like 6'),
    ('7', 'k, hard g', 'a K can be drawn from two 7s'),
    ('8', 'f, v', 'a handwritten f has two loops, like 8'),
    ('9', 'p, b', 'P is a mirrored 9'),
])}

It works by **sound, not spelling**: "knee" is just n (2), because the k is silent; a double letter that makes one sound counts once, so "shell" is sh-l, 65.

### PSC examples

{table(['Number', 'Fact', 'Word (sounds)', 'Image'], [
    ('14', 'Article 14: equality before law', 'DooR (d-r)', 'Everyone, rich or poor, enters through one door'),
    ('17', 'Article 17: abolition of untouchability', 'DuCK (d-k)', 'A duck that every child is allowed to touch'),
    ('19', 'Article 19: the six freedoms', 'TuB (t-b)', 'Six people singing freely in a bathtub'),
    ('21', 'Article 21: life and personal liberty', 'NeT (n-t)', 'A safety net catching a falling person'),
    ('32', 'Article 32: constitutional remedies', 'MooN (m-n)', 'Appealing all the way to the moon, the highest court'),
    ('51', 'Article 51A: Fundamental Duties', 'LighT (l-t)', 'A lamp that every citizen must keep burning'),
    ('1956', 'Kerala state formed', 'TaPe LaSH (t-p, l-sh)', 'A giant tape measure lashing Travancore-Cochin and Malabar together'),
    ('1965', 'First Jnanpith Award, to G. Sankara Kurup', 'TuB SHeLL (t-b, sh-l)', 'The poet in a tub, blowing a conch shell'),
])}

### Honest evidence and cost

The peg and major systems have **little modern research**, and Dunlosky and colleagues rated the related keyword mnemonic low utility. Learning the major system takes a few hours of practice before it becomes quick. It is worth it only if you have many numbers to learn, which, for PSC, you do. If you try it for a week and it stays slow, keep the numbers on cards instead; cards with spaced repetition always work.
""",
    example="""
**Ashiq** always confused article numbers in Part III: was it Article 16 or 15 for public employment? Was Article 22 arrest or education? He spent two evenings learning the major system with ten AnkiDroid cards, one per digit, until he could convert any two-digit number in a few seconds.

Then he made words for the ten article numbers he confused most, each tied to an image: DiSH (16) became a government canteen dish served to every job applicant; TiLe (15) a floor tile laid the same for every caste and religion. He recalled the ten images after 1 day and after 3 days: 10 out of 10 both times.

In his next previous-year paper, he got every Part III article number right for the first time. He found the system too slow for four-digit years at first, so for years he kept using cards and the stories from LRN-M11-L01, and he plans to try the major system for years again after more practice.
""",
    evidence=[
        ('The major system and peg lists for numbers', 'limited', 'Little modern research; they need practice to become quick and help most when you have many numbers to learn.'),
        ('The keyword mnemonic (a related technique)', 'limited', 'Rated low utility by Dunlosky and others (2013).'),
        ('Spaced-repetition cards for numbers', 'strong', 'Retrieval with spacing works whether or not you add a mnemonic.'),
    ],
    resources=[
        ('major-system', 'Read the introduction and the digit-to-sound table', '10 minutes'),
        ('dunlosky-aft', 'Reread the keyword mnemonic section, for the honest limits', '5 minutes'),
    ],
    steps=[
        'Learn the major system: make 10 AnkiDroid cards (digit → sounds) and study them until you can convert any two-digit number in about 5 seconds.',
        'Learn the 10-word peg list and use it once, for an ordered list of up to 10 items from your syllabus that you have checked.',
        'Choose 10 PSC numbers you often confuse (article numbers, amendments or years). For each, make a major-system word and a vivid image tied to the fact.',
        'Recall all 10 number facts after 1 day and after 3 days, without looking. Score both.',
        'Add the images to the backs of the matching AnkiDroid cards.',
    ],
    proof='Your digit cards, the peg-list use, your 10 number images with facts, and the day-1 and day-3 scores.',
    templates=[
        ('major system word builder', """
NUMBER: ______  FACT: ______________________________  (checked in ______)
Digits -> sounds:  __ = ___   __ = ___   __ = ___   __ = ___
Word(s) (sounds only; vowels, w, h, y are free): __________________
Image tying the word to the fact: _________________________________
Recall: day 1 [ ]  day 3 [ ]   Added to the card's back: [ ]
""", ''),
        ('peg list (learn once, reuse forever)', """
1 bun    2 shoe    3 tree    4 door    5 hive
6 sticks 7 heaven  8 gate    9 wine    10 hen
My list: 1 ________ 2 ________ 3 ________ 4 ________ 5 ________
         6 ________ 7 ________ 8 ________ 9 ________ 10 _______
Picture each item interacting with its peg. Recall in order, then backwards.
""", ''),
    ],
    mistakes=[
        ('Encoding by spelling instead of sound.', '"Knee" is 2, not 72. Silent letters don\'t count; double letters making one sound count once.'),
        ('Building words without fixing them to the fact.', 'The word must appear in an image together with the fact it stands for.'),
        ('Giving up after one slow evening.', 'The system takes a few hours to become quick. If it stays slow after a week, use cards.'),
        ('Using the major system for everything.', 'It is for numbers. Lists suit the palace; reasons suit explanation.'),
    ],
    quiz=[
        {'q': 'In the major system, which word encodes 21?', 'o': ['NeT', 'TeN', 'MooN', 'DooR'], 'a': 'A', 'why': 'n = 2 and t = 1, so "net" is 21.'},
        {'q': 'Which number does "moon" encode?', 'o': ['32', '23', '33', '22'], 'a': 'A', 'why': 'm = 3 and n = 2.'},
        {'q': 'What number is "shell"?', 'o': ['65', '655', '56', '6'], 'a': 'A', 'why': 'sh = 6 and the double l makes one sound, l = 5.'},
        {'q': 'What is the honest position on the major system?', 'o': ['Little modern research; it needs practice and helps most with many numbers', 'Proven to double memory for everyone', 'Proven useless', 'Works instantly without practice'], 'a': 'A', 'why': 'Cards with spaced repetition remain the reliable fallback.'},
    ],
    study='The Wikipedia article on the major system and Dunlosky\'s note on the keyword mnemonic',
    action='Learn the major system and a peg list, and fix 10 PSC numbers to images',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    M,
    overview="""
Learn the memory techniques that work for PSC lists, orders and numbers: chunking, acronyms, acrostics and stories; the memory palace, with real training evidence; and pegs and the major system for article numbers and dates. Build a memory palace for the Fundamental Rights or another real PSC topic.

PSC rewards memory for many arbitrary facts. Memory techniques can make that much easier, but they are often oversold. This module is honest: the memory palace has strong training evidence, other techniques have less, and all of them need rehearsal with spaced retrieval to last.

The module project brings the techniques together into your PSC memory toolkit, with a palace tested after a week.
""",
    outcomes=[
        'Use chunking, acronyms, acrostics and stories for PSC lists, after checking the facts',
        'Build a memory palace with vivid images and recall it forwards and backwards',
        'Use a peg list and the major system for ordered items and numbers',
        'Say honestly which techniques have strong evidence and which don\'t',
        'Combine every mnemonic with spaced retrieval',
    ],
    lessons=LESSONS,
    tools=[
        'The **mnemonic builder** and **should I use a mnemonic?** check',
        'The **memory palace planner** and **making images stick** rules',
        'The **major system table**, **word builder** and **peg list**',
    ],
    project='My PSC memory toolkit',
    project_steps=[
        'Keep your memory palace from LRN-M11-L02 alive: recall it once more two weeks after building it, and score it.',
        'Make sure your three list mnemonics and your ten number images are on AnkiDroid cards.',
        'Write one page: which technique worked best for which kind of PSC content (lists, orders, numbers), with your scores as evidence.',
        'Teach one of your mnemonics or your palace to your study partner or a family member, and test them the next day.',
    ],
    project_proof='Your palace plan with all recall scores including the two-week one, your one-page technique summary, and your partner\'s next-day result.',
    rubric=[
        ('Palace', 'Not built', 'Built but not reviewed', 'Built, reviewed at 10 minutes, 1, 3, 7 and 14 days'),
        ('Lists and numbers', 'No mnemonics', 'Mnemonics made but not tested', 'Checked mnemonics tested after 3 days and put on cards'),
        ('Honesty about evidence', 'Believes every claim', 'Knows some limits', 'Can say which techniques have strong, limited or low evidence'),
        ('Use', 'Techniques kept separate from study', 'Used sometimes', 'Each technique matched to the content it suits'),
    ],
    short=[
        'Build only the memory palace (LRN-M11-L02) and review it on schedule.',
        'Make one acrostic for a list that keeps appearing in previous papers.',
    ],
    flashcards=[
        ('What mnemonics are for', 'Arbitrary lists, orders and numbers, not understanding.'),
        ('Dunlosky\'s rating of the keyword mnemonic', 'Low utility.'),
        ('Acrostic for the five writs', '"Hari\'s Mother Prepared Chakka Quickly": habeas corpus, mandamus, prohibition, certiorari, quo warranto.'),
        ('Method of loci', 'Vivid images placed along a familiar route, recalled by walking it in your mind.'),
        ('Dresler and others (2017)', 'Six weeks of loci training gave ordinary adults large memory gains, still there after four months.'),
        ('Major system: digits 1 to 5', '1 t/d, 2 n, 3 m, 4 r, 5 l.'),
        ('Major system: digits 6 to 0', '6 j/sh/ch, 7 k/hard g, 8 f/v, 9 p/b, 0 s/z.'),
        ('Why Article 31 is missing from Part III', 'The right to property was removed in 1978.'),
    ],
    mistakes=[
        ('Collecting techniques without rehearsing them.', 'Every mnemonic needs spaced recall to last.'),
        ('Using mnemonics instead of understanding.', 'Explain reasons (Module 8); use mnemonics for arbitrary facts.'),
    ],
)
