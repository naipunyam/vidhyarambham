from common import lesson, module, link, xref, table, fence, Q
import tools

WARMUP = """WARM-UP (5-7 minutes, every session)
1. March on the spot or walk around the house       1 minute
2. Arm circles, small to big, forwards and back      30 seconds
3. Shoulder rolls and neck turns (slow, no circles)  30 seconds
4. Hip circles, hands on hips                        30 seconds
5. Bodyweight squats to a chair, slow                10
6. Wall push-ups, slow                               10
7. Alternate knee lifts or gentle high knees         30 seconds
8. Leg swings, holding a wall (front-back, side)     10 each leg
COOL-DOWN (5 minutes): walk slowly 2 minutes, then hold each stretch
20-30 seconds without bouncing: calf, thigh front, thigh back,
chest (in a doorway), upper back (hug yourself)."""

PROGRAMME = """BODYWEIGHT STRENGTH PROGRAMME (no equipment)
Do Session A and Session B on alternate days, 2-3 strength days a week.
Rest 60-90 seconds between sets. Effort: finish each set with 2-3 reps
"in the tank" (RPE 7-8 of 10). Form first, always.

SESSION A                         Level 1 -> 2 -> 3 -> 4
Squat        3 x 8-15   chair sit-to-stand -> bodyweight squat ->
                        slow 3-1-3 squat -> split squat (each leg)
Push         3 x 6-15   wall push-up -> push-up on a table/steps ->
                        knee push-up -> full push-up
Hinge        3 x 10-15  glute bridge -> single-leg-supported bridge ->
                        single-leg bridge -> slow single-leg bridge
Core         3 x 20-45 s  dead bug (slow) -> forearm plank on knees ->
                        forearm plank -> plank with shoulder taps

SESSION B
Lunge        3 x 8-12/leg  supported reverse lunge (hand on wall) ->
                        reverse lunge -> forward lunge -> step-up on a sturdy step
Pull         3 x 8-15   towel row on a door (door shut, towel round the handle,
                        lean back) -> table row under a sturdy table (only if stable)
                        -> slower, lower towel row
Shoulders    3 x 8-12   wall slides -> pike push-up with hips high (knees bent
                        allowed) -> slower pike push-up
Core side    3 x 15-30 s/side  side plank on knees -> full side plank
Calves       2 x 15-20  both feet -> slow -> one foot (hold a wall)

PROGRESSION RULE: when you can do the TOP of the rep range for all sets
with good form in two sessions in a row, move that exercise up one level
(or add 2 reps / 5 seconds). Change one exercise at a time.
DELOAD: every 6th week, do 2 sets instead of 3."""

L1 = lesson(
    17, 1,
    outcome='You can check whether you should see a doctor first, warm up and cool down properly, and take (or retake) the five baseline fitness tests safely.',
    split='15 minutes reading, 45 minutes of tests',
    principle='Start safe: check health risks, warm up every time, progress gradually, and measure where you start so you can see real change.',
    science=f"""
**Why fitness matters for everything else in this course.** The World Health Organization recommends that adults do **150 to 300 minutes a week of moderate** aerobic activity (brisk walking, cycling) or **75 to 150 minutes of vigorous** activity (running, fast cycling), or a mix, **plus muscle-strengthening activity on two or more days a week** ({link('who-pa', 'WHO fact sheet')}). Regular physical activity lowers the risk of heart disease, type 2 diabetes, some cancers and early death, and it improves mood, sleep and thinking. Exercise is also one of the better-supported treatments for mild to moderate depression and anxiety, often with effects comparable to other treatments in trials. Some activity is better than none, and the biggest health gains come from moving from **inactive to a little active**.

**Safety first.** Most people can safely start gentle exercise, but **see a doctor before starting** if you have (or think you might have) heart disease, high blood pressure, diabetes, asthma or other lung disease, joint problems or a recent injury, if you are pregnant, if you take medicines for these, or if you have ever had chest pain, fainting or dizziness during exertion. **Stop at once and get medical help** if exercise causes chest pain or pressure, severe breathlessness, dizziness, fainting or palpitations.

**Warm-ups.** A warm-up of 5 to 10 minutes of light movement raises body temperature and prepares joints. Evidence that warm-ups prevent injury is moderate, strongest for structured programmes in sport; static stretching before exercise is less useful than dynamic movement, and long static stretches just before strength work may slightly reduce performance. Gentle static stretches fit better in the cool-down.

**Kerala conditions.** Heat and humidity are high for much of the year: exercise in the early morning or evening, drink water, wear light cotton clothes, and slow down on very hot days. During the monsoon, train indoors (Session A and B need only a mat-sized space). Watch for slippery floors.

**The fitness tests.** You took these in week 0 (Baseline page). If you are starting the course with Part C, take them now. They measure upper-body strength endurance (push-ups), core endurance (plank), aerobic fitness (1 km walk or walk-run), resting heart rate (lower usually means fitter, though it varies with genes, medicines, stress and caffeine), and flexibility (sit and reach). These are simple field tests, not medical assessments; their value is comparing **you with you** over time.
""",
    evidence=[
        ('WHO activity guidelines (150–300 min moderate + strength 2 days)', 'strong', 'Based on large reviews linking activity to health outcomes.'),
        ('Exercise improves mild to moderate depression and anxiety', 'strong', 'Many trials and meta-analyses; effects comparable to other treatments in some reviews.'),
        ('Warm-ups reduce injury risk', 'moderate', 'Best evidence for structured sports warm-up programmes.'),
        ('Static stretching before strength work', 'mixed', 'May slightly reduce performance if long; dynamic warm-ups are preferred.'),
        ('Field fitness tests track personal change', 'tool', 'Simple, repeatable measures; not medical diagnoses.'),
    ],
    example="""
Vinod, 31, hasn't exercised since college. His father had a heart attack at 55. Before starting, he visits the Family Health Centre: his blood pressure is 138/88 (slightly high) and the doctor says walking and bodyweight strength work are fine, but to build up slowly and recheck blood pressure in three months.

He takes the tests at 6 am on a Sunday, after the warm-up: 7 knee push-ups (form broke at 8), plank 35 seconds, 1 km brisk walk 11 minutes 40 seconds on the road to the temple (measured with a maps app), resting heart rate averaged over three mornings 82, sit and reach −9 cm (couldn't reach his toes). He writes them in Baseline A and feels a little embarrassed. Then he remembers the spotlight effect, and that these numbers are only for comparing himself with himself.
""",
    apply=f"""
**Before your first workout:**
1. **Health check:** read the doctor list above. If anything applies, see a doctor (your Family Health Centre is free) and tell them what you plan to do.
2. **Set up a space:** a mat or folded bedsheet, a chair, a wall, a door with a handle, a sturdy step, water.
3. **Warm up** with the routine below every session.
4. **Test** (or retest) the five fitness tests from the Baseline page and write the numbers.

{fence(WARMUP)}

**Effort scale (RPE):** rate how hard each set felt from 1 (very easy) to 10 (maximum). Most beginner sets should feel like 6 to 8: hard but with good form and 2 or 3 reps left.

**With others:** a training partner (a cousin, a friend) makes you more likely to show up. Agree on times and test together, but compare progress, not absolute numbers.
""",
    resources=[
        ('who-pa', 'Read the key facts and the recommendations for adults', '10 minutes'),
        ('nhs-guide', 'Read the adult guidelines and the examples of moderate and vigorous activity', '10 minutes'),
        ('nhs-strvid', 'Watch one beginner strength video to see good form', '10 minutes'),
    ],
    steps=[
        'Go through the doctor checklist and, if any item applies, see a doctor before training. Write the outcome.',
        'Set up your training space and photograph it.',
        'Do the warm-up and the five fitness tests (or retest them if you took them in week 0). Record every number.',
        'Write your weekly activity minutes for the last week and compare them with the WHO range.',
    ],
    proof='Your health check note, a photo of your training space, the five test results with the date, and last week\'s activity minutes.',
    templates=[('Fitness baseline record', """HEALTH CHECK: any of heart/BP/diabetes/lung/joint/injury/pregnancy/
chest pain or dizziness when active?  No / Yes -> doctor visit on ______: advice ______
FITNESS TESTS           Date ______   Time ______
Push-ups (version: full / knees): ___ reps
Plank hold: ___ seconds
1 km walk / walk-run: ___ min ___ s   Route: ______
Resting heart rate (3-morning average): ___ bpm
Sit and reach: ___ cm (minus = short of toes)
Last week: moderate activity ___ min, vigorous ___ min, strength days ___
WHO target: 150-300 min moderate (or 75-150 vigorous) + strength 2+ days""", '')],
    mistakes=[
        ('Skipping the health check because you feel fine.', 'Silent high blood pressure and heart problems are common. The check is quick and free at the FHC.'),
        ('Testing without a warm-up.', 'Warm up for 5 to 7 minutes before any test.'),
        ('Testing to failure with bad form.', 'Count only clean reps; stop when form breaks.'),
        ('Comparing your numbers with others.', 'These tests compare you with you.'),
    ],
    quiz=[
        Q('What does WHO recommend for adults each week?', '150–300 minutes of moderate activity (or 75–150 vigorous), plus strength work on 2+ days', '30 minutes a month', 'Only strength training', '10,000 steps exactly', why='The WHO adult guidelines.'),
        Q('Which symptom means stop exercising and get medical help?', 'Chest pain or pressure', 'Mild muscle tiredness', 'Sweating', 'Feeling warm', why='Chest pain, fainting, severe breathlessness or palpitations need medical attention.'),
        Q('Which warm-up approach is generally preferred before strength work?', 'Light dynamic movement for 5–10 minutes', 'Long static stretches', 'No warm-up', 'A heavy meal', why='Dynamic warm-ups prepare the body; long static stretches fit better afterwards.'),
        Q('What are the fitness tests in this course for?', 'Comparing yourself with yourself over time', 'Diagnosing disease', 'Ranking you against others', 'Deciding if you can exercise', why='Simple field tests track personal change.'),
    ],
    study='read the lesson and the WHO recommendations',
    action='do the health check, set up your space and take the five fitness tests',
)

L2 = lesson(
    17, 2,
    outcome='You can perform eight bodyweight exercises with correct form and follow a two-session strength programme with safe progression.',
    split='20 minutes reading, 30 to 40 minutes per session',
    principle='Muscles and bones get stronger when you challenge them a little more over time (progressive overload); bodyweight exercises at the right level are enough for a beginner, if form comes first.',
    science=f"""
**Why strength training?** Muscle-strengthening activity improves strength, bone density, blood-sugar control, posture and the ability to do daily tasks, and is linked to lower risk of early death independent of aerobic exercise. It also helps back and joint pain for many people. WHO recommends it on at least two days a week.

**Progressive overload.** Muscles adapt to the demands placed on them. To keep improving, the demand must slowly increase: more reps, more sets, slower movements, harder versions (a full push-up instead of a knee push-up), or less rest. Research shows that **training with effort close to (but not always at) failure** builds strength and muscle across a wide range of reps, roughly 6 to 30, so bodyweight training can be effective for beginners if you choose the right level. Studies comparing bodyweight and gym training in beginners often find similar early gains in strength and muscle.

**Form first.** Good form means moving through a comfortable, controlled range, keeping the spine neutral (not rounded or over-arched), knees tracking over the toes in squats and lunges, and breathing (exhale on the effort; don't hold your breath, which raises blood pressure). Muscle soreness a day or two after a new exercise is normal (delayed-onset muscle soreness); **sharp or joint pain is not**: stop that exercise and try an easier version.

**How often?** Two or three strength sessions a week, with a rest day between sessions for the same muscles, suits beginners. Gains in the first two months come mostly from the nervous system learning the movements; muscle growth follows.

**Rest and food.** Sleep (Module 19) and enough protein from food (Module 20) support progress. The ICMR-NIN guidelines advise against protein supplements for building muscle; a balanced diet with pulses, milk, eggs, fish or meat is enough for most people.

The {link('nhs-strength', 'NHS strength exercises page')} shows several of these movements with pictures.
""",
    evidence=[
        ('Strength training improves strength, bone and metabolic health', 'strong', 'Many trials and reviews.'),
        ('Progressive overload drives continued gains', 'strong', 'A basic principle of exercise science.'),
        ('Wide rep ranges (about 6–30) build strength and muscle if effort is high', 'moderate', 'Supported by several meta-analyses.'),
        ('Bodyweight training gives good early gains for beginners', 'moderate', 'Supported by studies comparing bodyweight and gym training.'),
        ('Protein supplements needed for muscle', 'failed', 'Not needed for most people eating a balanced diet; ICMR-NIN advises against them for muscle building.'),
    ],
    example="""
Sreeja starts at Level 1 for most exercises: chair sit-to-stands, wall push-ups, glute bridges, dead bugs, supported reverse lunges, towel rows on her bedroom door, wall slides, knee side planks and calf raises. Session A on Monday and Friday, Session B on Wednesday, each about 35 minutes including the warm-up.

Week 1, wall push-ups 3 × 10 at RPE 6. Week 3, 3 × 15 in two sessions in a row, so she moves to push-ups on the kitchen table edge (Level 2), back to 3 × 6. By week 8 she does knee push-ups 3 × 10. Her squats progress from chair sit-to-stands to slow bodyweight squats. On one day her knee hurts sharply during lunges; she stops, switches to the supported version and the pain doesn't return. She logs every session in her workout log.
""",
    apply=f"""
**Form cues for the eight main exercises:**

| Exercise | Key cues | Common error |
| --- | --- | --- |
| Squat | Feet shoulder-width, sit back and down, knees over toes, chest up | Knees caving in; heels lifting |
| Push-up (any level) | Body straight from head to heels or knees, hands under shoulders, chest towards the surface | Hips sagging or piking up |
| Glute bridge | Feet flat, push through heels, squeeze seat at top, ribs down | Arching the lower back |
| Dead bug / plank | Lower back gently pressed down (dead bug) or body in a line (plank), breathe | Holding the breath, sagging hips |
| Reverse lunge | Step back, both knees about 90°, front knee over ankle | Front knee pushing far past toes |
| Towel row | Door shut firmly, lean back, pull chest to hands, squeeze shoulder blades | Pulling with arms only; door not secure |
| Pike push-up / wall slide | Hips high, lower head towards floor between hands / arms slide up the wall | Flaring elbows wide |
| Side plank | Elbow under shoulder, hips lifted, body in a line | Hips dropping |

{fence(PROGRAMME)}

**Safety for the towel row:** use only a solid door that opens away from you (so leaning back pulls it shut), check the handle is firm, and keep your feet close at first. If in doubt, do table rows only under a heavy, stable table, or skip pulling and do more bridges.

**With others:** train with a partner who checks your form against the cues; film one set on your phone and compare with an NHS video.
""",
    resources=[
        ('nhs-strength', 'Read the page and compare the pictures with your form', '10 minutes'),
        ('nhs-strvid', 'Do one full beginner strength video along with the instructor', '20 minutes'),
        ('nhs-flex', 'Read the flexibility exercises for your cool-down', '10 minutes'),
    ],
    steps=[
        'Choose your starting level for each exercise: the one where you can do the bottom of the rep range with good form.',
        'Film one set of squats and one set of push-ups and check them against the form cues.',
        'Do Session A and Session B on alternate days for two weeks (at least five sessions), logging each one.',
        'Apply the progression rule: write which exercises moved up a level.',
    ],
    proof='Your starting levels, a note on the filmed form check, five or more logged sessions and the exercises that progressed.',
    templates=[('Workout log', tools.WORKOUT_LOG, '')],
    mistakes=[
        ('Starting at a level that is too hard.', 'If you can\'t do the bottom of the rep range with good form, go down a level.'),
        ('Training to total failure every set.', 'Stop with 2 or 3 reps left; form breaks and injury risk rises at failure.'),
        ('Ignoring sharp or joint pain.', 'Stop the exercise and try an easier version. See a doctor if pain persists.'),
        ('Changing everything at once.', 'Progress one exercise at a time.'),
    ],
    quiz=[
        Q('What is progressive overload?', 'Gradually increasing the demand on muscles over time', 'Lifting the heaviest weight possible on day 1', 'Training every day without rest', 'Eating more protein', why='Muscles adapt to demand, so demand must slowly increase.'),
        Q('When should you move an exercise up a level, in this programme?', 'When you reach the top of the rep range with good form in two sessions in a row', 'After one session', 'When you feel bored', 'Never', why='The progression rule balances challenge and safety.'),
        Q('Which is normal after a new exercise?', 'Muscle soreness a day or two later', 'Sharp joint pain', 'Chest pain', 'Dizziness', why='Delayed-onset muscle soreness is normal; sharp pain is not.'),
        Q('Does the ICMR-NIN guidance recommend protein supplements for muscle building?', 'No; it advises against them and favours a balanced diet', 'Yes, for everyone', 'Only for students', 'It does not mention them', why='The 2024 guidelines advise avoiding protein supplements for muscle building.'),
    ],
    study='read the lesson and watch one NHS strength video',
    action='choose your levels, check your form on video and complete five logged sessions',
)

L3 = lesson(
    17, 3,
    outcome='You can plan safe cardio and mobility work, combine them with strength into a weekly plan, and complete a 30-day fitness challenge with a retest.',
    split='15 minutes reading, 20 to 30 minutes on five days a week for 30 days',
    principle='A balanced week mixes brisk walking or walk-running for the heart, strength twice or three times, and a few minutes of mobility daily; consistency over 30 days matters more than any single hard session.',
    science=f"""
**Cardio (aerobic exercise).** Activities that raise your heart rate and breathing for several minutes strengthen the heart and lungs. **Moderate intensity** means you can talk but not sing (brisk walking, easy cycling). **Vigorous** means you can say only a few words (running, fast cycling, skipping). The WHO target is 150 to 300 minutes a week of moderate activity, or half that of vigorous. Walking is underrated: brisk walking is linked to substantial health benefits, and in a large 2023 meta-analysis, risk of early death kept falling as daily steps rose, starting from around 4,000 a day and levelling off around 8,000 to 10,000 for many adults. (The "10,000 steps" number started as a 1960s marketing slogan in Japan, though it happens to sit in a reasonable range.)

**Starting to run.** The free {link('c25k', 'NHS Couch to 5K')} plan takes beginners from walking to running 5 km in nine weeks, with three sessions a week of alternating walking and running. It is a good structure if you want to run; if not, brisk walking with some uphill stretches is excellent.

**Interval training.** Short bursts of harder effort with recovery (for example, 1 minute fast, 2 minutes easy) improve fitness efficiently; high-intensity interval training (HIIT) can match longer moderate exercise for some outcomes. For beginners, keep intervals moderate and build up.

**Mobility and flexibility.** Gentle range-of-motion work and stretching improve or maintain flexibility, and many people find it reduces stiffness from long sitting. Evidence for stretching preventing injury is weak; its main value is comfort and range of motion. Five to ten minutes a day (or yoga, Module 18) is enough.

**Why a 30-day challenge?** Thirty days of 5 sessions a week builds the routine and lets you see early strength gains; it is a training phase, not a finish line. Expect noticeable changes in your push-up and plank numbers within a month, mainly from your nervous system learning the movements.
""",
    evidence=[
        ('Brisk walking improves health', 'strong', 'Large observational studies and trials.'),
        ('More daily steps linked to lower mortality, levelling off', 'moderate', 'Large meta-analyses; observational, so causation is partly inferred.'),
        ('"10,000 steps" as a scientific threshold', 'failed', 'Started as a marketing slogan; benefits begin well below it.'),
        ('Interval training improves fitness efficiently', 'moderate', 'Many trials; effects similar to longer moderate exercise for some outcomes.'),
        ('Stretching prevents injury', 'mixed', 'Weak evidence; main benefit is range of motion and comfort.'),
    ],
    example="""
Ashiq's weekly plan for the 30-day challenge:

| Day | Session | Time |
| --- | --- | --- |
| Monday | Strength A + 5 min mobility | 35 min |
| Tuesday | Brisk walk with two hill stretches | 30 min |
| Wednesday | Strength B + 5 min mobility | 35 min |
| Thursday | Walk-run intervals (1 min jog, 2 min walk × 6) | 25 min |
| Friday | Strength A + 5 min mobility | 35 min |
| Saturday | Long walk with his cousin, or a football game | 45 min |
| Sunday | Rest, or yoga (Module 18) | 20 min |

He counts five "challenge sessions" a week. Monsoon rain cancels two walks, so he does 20 minutes of brisk marching and step-ups inside instead. On day 30 he retests: push-ups (knees) from 7 to 16, plank from 35 to 70 seconds, 1 km from 11:40 to 9:55. His resting heart rate is 78 (from 82). Sit and reach is −6 cm (from −9). He writes: "Strength up a lot, heart a bit, flexibility a bit. Keep going: next goal is full push-ups."
""",
    apply=f"""
**Plan your week (choose five challenge sessions):**
- **Strength:** 2 or 3 sessions (A and B, PD-M17-L02).
- **Cardio:** 2 or 3 sessions of brisk walking, walk-run intervals or Couch to 5K, 20 to 45 minutes each.
- **Mobility:** 5 minutes after every session (the cool-down stretches) or the yoga routine.
- **Rest:** at least one full rest day.

**Talk test for intensity:** moderate = can talk, not sing; vigorous = only a few words.

**The 30-day fitness challenge:**
1. Five sessions a week for 30 days (about 20 to 22 sessions), logged.
2. Warm up every time; follow the progression rule.
3. On bad-weather or busy days, do a 10-minute indoor version (squats, push-ups, marching), which still counts.
4. Day 30: retest push-ups and plank (and ideally all five tests) and compare with your baseline.

**With others:** walk-run with a friend, join a local football or volleyball game, or start a 6 am walking group in your ward. Group exercise is linked to better adherence.
""",
    resources=[
        ('c25k', 'Read how the 9-week plan works; download the app if you want to run', '10 minutes'),
        ('nhs-aero', 'Do one aerobic video on a rainy day', '15 minutes'),
        ('nhs-flex', 'Use the flexibility exercises as your 5-minute mobility routine', '10 minutes'),
    ],
    steps=[
        'Write your weekly plan with five challenge sessions and a rest day.',
        'Add "Fitness challenge session" to Loop for 30 days.',
        'Complete and log the sessions for 30 days, using indoor versions when needed.',
        'On day 30, retest push-ups and plank (and ideally all five tests) and write the changes.',
    ],
    proof='Your weekly plan, a 30-day Loop screenshot or workout log, and day-30 retest numbers compared with your baseline.',
    templates=[('30-day fitness plan', """30-DAY FITNESS CHALLENGE        Start ______  End ______
Weekly plan:
Mon ______ Tue ______ Wed ______ Thu ______ Fri ______ Sat ______ Sun rest/yoga
Intensity: moderate = can talk, not sing; vigorous = a few words only
Indoor backup (10 min): 3 rounds of 10 squats, 5-10 push-ups (any level),
  30 s marching, 20 s plank
Sessions done: week 1 ___ week 2 ___ week 3 ___ week 4 ___
RETEST (day 30)      Baseline   Day 30   Change
Push-ups             ___        ___      ___
Plank (s)            ___        ___      ___
1 km                 ___        ___      ___
Resting HR           ___        ___      ___
Sit and reach (cm)   ___        ___      ___""", '')],
    mistakes=[
        ('Doing hard sessions every day.', 'Rest and easy days let your body adapt. Hard every day leads to injury or quitting.'),
        ('Skipping because of rain or a busy day.', 'Do the 10-minute indoor version; it keeps the habit.'),
        ('Running too much too soon.', 'Use walk-run intervals or Couch to 5K; increase gradually.'),
        ('Exercising hard in the midday heat.', 'Train early or late, drink water, slow down on hot days.'),
    ],
    quiz=[
        Q('What does "moderate intensity" feel like, by the talk test?', 'You can talk but not sing', 'You can sing easily', 'You can\'t say a word', 'You feel nothing', why='The talk test is a simple intensity guide.'),
        Q('Where did the "10,000 steps a day" figure come from?', 'A 1960s marketing slogan in Japan', 'A WHO study', 'An Indian government rule', 'The Olympic committee', why='Benefits start well below 10,000 steps.'),
        Q('What is the NHS Couch to 5K plan?', 'A free 9-week walk-run plan with three sessions a week', 'A paid gym membership', 'A diet plan', 'A 5-day fast', why='It builds from walking to running 5 km.'),
        Q('What is the main proven benefit of stretching?', 'Better range of motion and comfort', 'Guaranteed injury prevention', 'Weight loss', 'Bigger muscles', why='Evidence for injury prevention is weak.'),
    ],
    study='read the lesson and the Couch to 5K page',
    action='complete the 30-day fitness challenge with five sessions a week and retest on day 30',
)

LESSONS = [L1, L2, L3]

MODULE = module(
    17,
    overview=f"""
A complete, no-equipment home fitness programme for beginners: a health check and warm-up, five fitness tests, two bodyweight strength sessions with four levels each and a clear progression rule, cardio and mobility, and a 30-day fitness challenge with a retest.

Part C, Strengthen your body, starts with movement because it improves almost everything else: mood, sleep, stress, focus and long-term health. You need a mat-sized space, a chair, a wall, a door and a step, nothing else.

**Safety:** see a doctor first if you have heart, lung, joint or blood-pressure problems, diabetes, a recent injury or surgery, are pregnant, or get chest pain, dizziness or unusual breathlessness when active. Stop at once if any of these happen during exercise.
""",
    outcomes=[
        'Know when to see a doctor first and when to stop exercising.',
        'Warm up and cool down properly every session.',
        'Perform eight bodyweight exercises with correct form at the right level.',
        'Follow a strength programme with safe progression and plan cardio and mobility.',
        'Complete a 30-day fitness challenge with a retest.',
    ],
    lessons=LESSONS,
    project='the 30-day fitness challenge with a retest',
    project_steps=[
        'Do the health check and the five fitness tests (PD-M17-L01).',
        'Follow the strength programme and weekly plan (PD-M17-L02 and L03) for 30 days, logging every session.',
        'Retest on day 30 and compare with your baseline.',
        'Write your training plan for the next three months and add it to your Playbook.',
    ],
    project_proof='Your health check note, workout log, day-30 retest and three-month plan.',
    rubric=[
        ('Safety', 'No health check or warm-ups', 'Health check done, warm-ups sometimes', 'Health check done and warm-up every session'),
        ('Consistency', 'Fewer than 12 sessions in 30 days', '12 to 19 sessions', '20 or more sessions'),
        ('Progression', 'No exercise progressed', 'One or two progressed', 'Several exercises progressed using the rule'),
        ('Measurement', 'No retest', 'Partial retest', 'All five tests retested and compared'),
    ],
    short=[
        'Brisk walk 20 minutes on five days and do Session A once a week.',
        'Retest push-ups and plank after 30 days.',
    ],
    flashcards=[
        ('WHO adult activity target', '150–300 min moderate (or 75–150 vigorous) a week + strength on 2+ days.'),
        ('Stop exercising and seek help if…', 'Chest pain, fainting, dizziness, severe breathlessness or palpitations.'),
        ('Progressive overload', 'Slowly increase reps, sets, difficulty or slowness over time.'),
        ('Progression rule', 'Top of rep range with good form, two sessions in a row → next level.'),
        ('RPE target for beginner sets', '6–8 of 10: hard, with 2–3 reps left.'),
        ('Talk test', 'Moderate: talk, not sing. Vigorous: a few words.'),
        ('"10,000 steps" origin', 'A 1960s Japanese marketing slogan; benefits start well below it.'),
        ('Protein supplements for beginners?', 'Not needed; ICMR-NIN advises against them for muscle building.'),
    ],
    mistakes=[
        ('Starting too hard and quitting in week 2.', 'Start easy, progress by the rule.'),
        ('Training through sharp pain.', 'Stop, use an easier version, see a doctor if it persists.'),
        ('Comparing with gym videos and influencers.', 'Compare with your own baseline.'),
    ],
    tools=[
        'The fitness baseline record and warm-up routine (PD-M17-L01).',
        'The two-session bodyweight programme with levels, and the workout log (PD-M17-L02).',
        'The 30-day fitness plan with retest table (PD-M17-L03).',
    ],
    playbook=[
        'I train strength A/B ___ times a week and walk or walk-run ___ times; warm-up every time.',
        'Progression rule: top of the rep range twice with good form → next level. Sharp pain → stop.',
    ],
)
