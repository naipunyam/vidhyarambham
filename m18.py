from common import lesson, module, link, xref, table, Q

CYP_ROWS = [
    ('1', 'Prayer (opening)', 'A short prayer or a calm, prayerful mood', '1 min'),
    ('2', 'Loosening practices (chalana kriya / sukshma vyayama)', 'Neck bending, shoulder movement, trunk movement, knee movement', '4 min'),
    ('3', 'Standing asanas', 'Tadasana, Vrikshasana, Pada-hastasana, Ardha chakrasana, Trikonasana', '7 min'),
    ('4', 'Sitting asanas', 'Bhadrasana, Vajrasana, Ardha ushtrasana, Ushtrasana, Shashankasana, Uttana mandukasana, Vakrasana', '7 min'),
    ('5', 'Prone asanas (lying on the front)', 'Makarasana, Bhujangasana, Shalabhasana', '4 min'),
    ('6', 'Supine asanas (lying on the back)', 'Setubandhasana, Uttanapadasana, Ardha halasana, Pavanamuktasana, Shavasana', '7 min'),
    ('7', 'Kapalabhati', 'Forceful exhalation, passive inhalation (see cautions)', '2 min'),
    ('8', 'Pranayama', 'Nadi shodhana (alternate nostril), Sheetali, Bhramari', '6 min'),
    ('9', 'Dhyana', 'Meditation', '5 min'),
    ('10', 'Sankalpa and Shanti patha', 'A resolution, and a closing peace chant', '2 min'),
]

L1 = lesson(
    18, 1,
    outcome='You can follow the Ministry of Ayush Common Yoga Protocol safely, know its cautions, and run a 20-minute routine of your own three times a week.',
    split='20 minutes reading, 45 minutes for one full session',
    principle='Yoga combines postures, breathing and meditation; it improves flexibility, balance and wellbeing modestly and safely for most people, when practised gently and within your own capacity.',
    science=f"""
**What yoga is.** Yoga is an Indian tradition of physical postures (**asanas**), breath regulation (**pranayama**), concentration and meditation (**dharana**, **dhyana**), with ethical and philosophical roots described in texts such as Patanjali's *Yoga Sutras*. Modern practice usually emphasises the physical and breathing parts. The **International Day of Yoga** (21 June) is observed worldwide, and the Government of India publishes a free **Common Yoga Protocol (CYP)** for it.

**The Common Yoga Protocol.** The protocol, prepared by the Morarji Desai National Institute of Yoga under the Ministry of Ayush, is a standard sequence of about **45 minutes** for beginners. The 4th revised edition (2019) lists the sequence below and detailed instructions with cautions for each practice ({link('cyp', 'Common Yoga Protocol, 2019 PDF')}; a 5th revised edition was published in 2022 with a slightly shorter list: {link('cyp-2022', '2022 PDF')}).

**What the research shows.** Reviews of yoga trials find **moderate** evidence that yoga improves **flexibility, balance and lower-back pain**, and **small to moderate** improvements in **anxiety, depression and stress**, often similar to other forms of exercise. Benefits for blood pressure and blood sugar have been found in some trials, but many studies are small, short or of mixed quality. Claims that particular asanas "cure" diseases, detoxify organs or balance chakras are not supported by good evidence. Yoga is generally safe; injuries are uncommon and mostly come from forcing advanced postures.

**General guidance from the protocol (paraphrased):**
- Practise in a calm, clean place, on an empty or light stomach (many teachers suggest waiting 2 to 3 hours after a full meal), with the bladder and bowels empty, in light cotton clothes.
- Don't practise when exhausted, ill, in a hurry or under acute stress.
- **Consult a doctor or yoga expert first** if you have a chronic illness, pain, heart problems, or are pregnant.
- Move slowly, with awareness of body and breath. Breathe through the nose unless told otherwise. Don't hold the breath unless the practice asks for it. **Practise within your own capacity**; no jerks or forcing.
- After practice, wait 20 to 30 minutes before bathing or eating.

**Key cautions in the protocol** include: avoid **Kapalabhati** with heart problems, high blood pressure, vertigo, epilepsy, migraine, a history of stroke, hernia, gastric ulcer, during pregnancy or menstruation; avoid **Pada-hastasana** with heart problems, disc problems, hernia, ulcers, glaucoma, high myopia or vertigo; avoid **Ushtrasana** with heart disease or hernia; avoid **Bhujangasana** for 2 to 3 months after abdominal surgery, and with hernia or ulcers; avoid **Shalabhasana** with high blood pressure, peptic ulcer or hernia; avoid **Pavanamuktasana** with abdominal injury, hernia, sciatica, severe back pain or pregnancy. Read the PDF for the full list.
""",
    evidence=[
        ('Yoga improves flexibility and balance', 'moderate', 'Several reviews of trials.'),
        ('Yoga helps chronic lower-back pain', 'moderate', 'Reviews find benefits similar to other exercise therapies.'),
        ('Yoga reduces anxiety, depression and stress', 'moderate', 'Small to moderate effects; study quality mixed.'),
        ('Specific asanas cure diseases or "detoxify" organs', 'failed', 'Not supported by good evidence.'),
        ('Yoga is generally safe when practised gently', 'moderate', 'Injury rates are low; most injuries come from forcing postures.'),
    ],
    example="""
Anu's mother, 56, has knee pain and mild high blood pressure; Anu, 29, has stiff shoulders from studying. They decide to practise together three mornings a week.

Before starting, her mother's doctor at the Family Health Centre approves gentle yoga but advises avoiding Kapalabhati because of her blood pressure. They follow the CYP from a phone video, skipping Kapalabhati and doing Bhadrasana and Vajrasana with a folded towel under the knees. Anu's mother cannot do Trikonasana fully, so she bends only a little, holding a chair.

After six weeks, Anu can reach 4 cm further in the sit-and-reach test and her shoulders feel looser. Her mother says she sleeps better and enjoys the morning routine with her daughter. Neither notices dramatic change in anything else, which matches the research: modest, real benefits, especially when it becomes a shared routine.
""",
    apply=f"""
**The Common Yoga Protocol sequence (about 45 minutes):**

{table(['Step', 'Practice', 'What it includes', 'About'], CYP_ROWS)}

(The timings in the last column are a rough guide for planning; the protocol describes the practices rather than a minute-by-minute schedule.)

**Your 20-minute routine (three times a week):** choose from the protocol, for example: loosening practices (4 min), Tadasana, Vrikshasana and Trikonasana (5 min), Vajrasana and Shashankasana (3 min), Bhujangasana and Makarasana (3 min), Setubandhasana and Shavasana (3 min), Nadi shodhana or Bhramari (2 min). Skip anything your health conditions rule out.

**Practising safely:** follow one clear video or the PDF pictures; enter and leave each posture slowly; stop at the point of stretch, never pain; use a wall or chair for balance postures; keep breathing.

**With others:** yoga is easy to share with family members of any age, with adjustments. A family or ward yoga session on Sundays (or on International Day of Yoga) builds connection as well as flexibility.
""",
    resources=[
        ('cyp', 'Read the general guidelines and the instructions and cautions for each practice', '40 minutes'),
        ('cyp-2022', 'Skim the 2022 edition to compare the sequence', '15 minutes'),
        ('nhs-yoga', 'Optional: try one beginner yoga video', '20 minutes'),
    ],
    steps=[
        'Read the CYP general guidelines and cautions; list any practices you should skip and why.',
        'Do one full CYP session (about 45 minutes) following the PDF or a clear video.',
        'Design your own 20-minute routine and do it three times a week for two weeks.',
        'Before and after the two weeks, measure sit and reach and rate how stiff you feel (0–10).',
    ],
    proof='Your list of practices to skip, a note on the full session, your 20-minute routine, six logged sessions and before-and-after sit-and-reach and stiffness ratings.',
    templates=[('Yoga routine and log', """MY YOGA ROUTINE (20 minutes)           Practices I skip, and why: ______
1. Loosening practices ............ 4 min
2. Standing: ______________ ........ 5 min
3. Sitting: _______________ ........ 3 min
4. Prone: ________________ ......... 3 min
5. Supine + Shavasana ............. 3 min
6. Pranayama: ________________ ..... 2 min
LOG: Date | Routine (full CYP / 20 min) | Minutes | Felt (stiff / ok / loose) | Any pain? (stop)
Before: sit and reach ___ cm, stiffness ___/10   After 2 weeks: ___ cm, ___/10""", '')],
    mistakes=[
        ('Forcing a posture to look like the picture.', 'Stop at a stretch, never pain. Use a wall or chair.'),
        ('Doing Kapalabhati with health conditions.', 'Check the cautions; skip it if you have blood-pressure, heart or other listed conditions.'),
        ('Practising after a heavy meal.', 'Practise on an empty or light stomach.'),
        ('Believing cure claims.', 'Yoga\'s benefits are real but modest; it does not replace medical treatment.'),
    ],
    quiz=[
        Q('About how long is the Common Yoga Protocol?', 'About 45 minutes', '5 minutes', '3 hours', 'It has no set length', why='It is a 45-minute standard sequence.'),
        Q('Who should avoid Kapalabhati, according to the protocol?', 'People with heart problems, high blood pressure, vertigo, epilepsy, hernia, during pregnancy and others listed', 'Everyone over 20', 'Only children', 'Nobody', why='The protocol lists several cautions.'),
        Q('What does research show yoga reliably improves?', 'Flexibility, balance and lower-back pain, with modest mental-health benefits', 'It cures diabetes', 'It removes toxins from the liver', 'It replaces all medicine', why='Moderate evidence for these outcomes; cure claims are unsupported.'),
        Q('When should you practise, relative to meals?', 'On an empty or light stomach (many teachers suggest 2 to 3 hours after a full meal)', 'Straight after a big meal', 'Only after eating sweets', 'Meals make no difference', why='The protocol advises an empty or light stomach.'),
    ],
    study='read the lesson and the CYP general guidelines and cautions',
    action='do one full CYP session, then your own 20-minute routine three times a week for two weeks',
)

LESSONS = [L1]

MODULE = module(
    18,
    overview=f"""
Yoga basics using the free Ministry of Ayush Common Yoga Protocol: the sequence, the general guidelines, the cautions for each practice, honest evidence, and your own 20-minute routine three times a week.

Yoga fits easily into a Kerala home routine: it needs a mat or a bedsheet, can be done by the whole family and complements the strength programme in Module 17 (it can replace the Sunday session). Its proven benefits are modest but real: flexibility, balance, back comfort and calm.

Check the cautions before you start. If you have high blood pressure, heart problems, hernia, a recent surgery, or are pregnant, some practices are not suitable; ask a doctor or a qualified yoga teacher.
""",
    outcomes=[
        'Follow the Common Yoga Protocol sequence.',
        'Apply the general guidelines and the cautions for each practice.',
        'Explain what yoga research supports and what it does not.',
        'Run your own 20-minute routine three times a week.',
    ],
    lessons=LESSONS,
    project='a safe 20-minute yoga routine, practised for two weeks',
    project_steps=[
        'Do one full CYP session.',
        'Write your 20-minute routine, leaving out any practices your health rules out.',
        'Practise it three times a week for two weeks, logged.',
        'Retest sit and reach and stiffness; decide whether yoga replaces or adds to one weekly session in your fitness plan.',
    ],
    project_proof='Your routine, six logged sessions and before-and-after measures.',
    rubric=[
        ('Safety', 'Cautions not read', 'Cautions read but not applied', 'Cautions applied to your own health'),
        ('Practice', 'Fewer than three sessions', 'Three to five sessions', 'Six or more sessions'),
        ('Form', 'Forcing postures', 'Mostly gentle', 'Slow, within capacity, breathing steadily'),
        ('Evaluation', 'No measures', 'Feelings only', 'Before-and-after measures and a decision'),
    ],
    short=[
        'Do 10 minutes of loosening practices and Shavasana three times a week.',
        'Learn one pranayama (Bhramari or Nadi shodhana) for stressful moments.',
    ],
    flashcards=[
        ('Common Yoga Protocol', 'A free, 45-minute standard sequence from the Ministry of Ayush (MDNIY).'),
        ('CYP order', 'Prayer, loosening, standing, sitting, prone, supine, Kapalabhati, pranayama, dhyana, sankalpa.'),
        ('Meals and yoga', 'Practise on an empty or light stomach.'),
        ('Kapalabhati cautions', 'Avoid with heart problems, high BP, vertigo, epilepsy, migraine, stroke, hernia, ulcer, pregnancy, menstruation.'),
        ('Best-supported yoga benefits', 'Flexibility, balance, lower-back pain; modest mental-health benefits.'),
        ('Golden rule', 'Practise within your own capacity: stretch, never pain.'),
    ],
    mistakes=[
        ('Copying advanced poses from social media.', 'Stay with the beginner protocol.'),
        ('Treating yoga as medicine.', 'Use it alongside, not instead of, medical care.'),
        ('Skipping the cautions.', 'Read them for every practice you choose.'),
    ],
    tools=[
        'The CYP sequence table and your 20-minute routine with log (PD-M18-L01).',
    ],
    playbook=[
        'Yoga: my 20-minute routine ___ times a week; practices I skip: ______.',
    ],
)
