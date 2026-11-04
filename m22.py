from common import lesson, module, link, xref, table, fence, Q, CHECK

L1 = lesson(
    22, 1,
    outcome='You can make a personal prevention plan: which free check-ups to get and how often, how much to drink, how to cut tobacco and alcohol harm, and where to get help to quit.',
    split='20 minutes reading, 30 minutes of planning plus one clinic visit',
    principle='Most serious illness in Kerala builds silently (high blood pressure, diabetes, cholesterol, some cancers) and is caught early by simple, often free, check-ups; avoiding tobacco and limiting alcohol prevent much of the rest.',
    science=f"""
**Why prevention matters at 30.** Non-communicable diseases (heart disease, stroke, diabetes, chronic lung disease and cancers) cause most deaths in India, and Kerala has some of the highest rates of diabetes and high blood pressure in the country. Many people with high blood pressure or diabetes have **no symptoms** for years, while damage builds in the heart, kidneys, eyes and brain. Finding them early allows simple lifestyle changes or medicines that greatly reduce risk.

**Check-ups for a healthy adult around 30** (a general guide; your doctor may advise differently):
- **Blood pressure:** at least once a year (more often if it is borderline). Normal is generally below about 120/80; readings at or above about 140/90 on repeated checks usually need medical attention (thresholds vary between guidelines).
- **Blood sugar (fasting or HbA1c):** at least every one to three years from 30, yearly if you have a family history of diabetes, are overweight, or had high readings before.
- **Weight and waist:** measured at the same time.
- **Cholesterol (lipid profile):** discuss with a doctor, especially with a family history of early heart disease.
- **Teeth:** a dental check once a year; brush twice a day with fluoride toothpaste.
- **Eyes:** if you notice changes, and periodically if you have diabetes.
- **Cancer screening:** in India, government programmes offer screening for **oral, breast and cervical cancers** for adults from 30; ask at your Family Health Centre or Primary Health Centre about what is offered locally ({'check current rules'}).
- **Vaccinations:** check your tetanus (Td) booster (generally every 10 years) and hepatitis B status with a doctor.

Government health facilities in Kerala (Family Health Centres, PHCs, CHCs, taluk and district hospitals) provide free blood-pressure and blood-sugar checks; details vary by place, so ask locally.

**Hydration.** The "8 glasses a day" rule has no strong scientific basis; water needs vary with body size, activity and climate, and food (rice, curries, fruit) provides some water. Practical guidance: **drink when thirsty, drink more in heat and when exercising**, and check that your urine is **pale yellow**. Kerala's heat and humidity mean many people need more than they think, especially outdoors. Plain water, buttermilk (moru) and tender coconut water are good choices; sugary drinks are not. People with heart or kidney conditions may need limits; follow medical advice.

**Tobacco.** Smoking and chewing tobacco (including gutka, pan masala with tobacco and beedis) are major causes of cancer (especially mouth cancer, very common in India), heart disease, stroke and lung disease. There is **no safe level** of tobacco use. Quitting at any age brings benefits, starting within weeks. India's **National Tobacco Quitline, 1800-11-2356** (toll-free), offers counselling ({link('quitline', 'NTQLS')}; hours listed as 8 am to 8 pm, Tuesday to Sunday, so {CHECK}). Doctors can also help, including with nicotine replacement where suitable.

**Alcohol.** Alcohol is linked to liver disease, several cancers, high blood pressure, accidents, violence, depression and family and money problems. In 2023 the World Health Organization stated that no level of alcohol consumption is safe for health. If you drink, less is better; never drink and drive; avoid binge drinking. Using alcohol to cope with stress or sleep is a warning sign (PD-M11-L01). Help is available from doctors, de-addiction centres in government hospitals and Tele-MANAS (14416).
""",
    evidence=[
        ('Screening finds silent high blood pressure and diabetes early', 'strong', 'Early detection and treatment reduce complications.'),
        ('Tobacco causes cancer, heart and lung disease; no safe level', 'strong', 'Overwhelming evidence.'),
        ('Quitting tobacco brings benefits at any age', 'strong', 'Large long-term studies.'),
        ('Alcohol increases risk of many diseases and injuries', 'strong', 'Large body of evidence; WHO states no level is safe for health.'),
        ('"8 glasses of water a day" for everyone', 'failed', 'No strong basis; needs vary. Drink to thirst, more in heat.'),
        ('Annual full-body check-up packages for healthy young adults', 'mixed', 'Targeted checks (BP, sugar) are useful; large packages often find little and can cause false alarms.'),
    ],
    example="""
Vinod (31) has never had a check-up. His father had a heart attack at 55 and his mother has diabetes. He goes to the Family Health Centre one morning before opening his shop.

Results: blood pressure 138/88 (high-normal), fasting sugar 104 (slightly raised), waist 94 cm. The doctor advises lifestyle changes, a repeat in three months, and a lipid profile because of his family history. Vinod also chews pan masala with tobacco "only after lunch" and drinks with friends most Saturdays.

His prevention plan: walk five days a week and continue strength training (Module 17); balanced plates and less salt and sugar (Module 20); quit tobacco: he calls the quitline (1800-11-2356), picks a quit date, tells his friends, and replaces the after-lunch habit with a walk to the tea shop and fennel seeds; alcohol: no more than one evening a month, never before driving. He sets a phone reminder for his three-month recheck. At the recheck, his blood pressure is 128/82 and his sugar 98.
""",
    apply=f"""
**Make your personal prevention plan:**
{fence('''MY PREVENTION PLAN                           Date ______
Family history (parents, siblings): BP __ diabetes __ heart disease __
  stroke __ cancer __ (which) ______
CHECK-UPS                     Last done    Result     Next due
Blood pressure                ______       ______     ______
Blood sugar (fasting/HbA1c)   ______       ______     ______
Weight and waist              ______       ______     ______
Cholesterol (if advised)      ______       ______     ______
Dental check                  ______       ______     ______
Eyes (if symptoms)            ______       ______     ______
Cancer screening offered?     ______ (ask at FHC/PHC)
Tetanus booster / hep B       ______ (ask a doctor)
HYDRATION: water bottle on desk; pale-yellow urine; more in heat/exercise
TOBACCO: none / quitting -> quit date ______; Quitline 1800-11-2356
ALCOHOL: none / limit ______ ; never before driving
Reminders set for: ______''')}

**If you use tobacco:** set a quit date within two weeks; tell people; remove tobacco, lighters and ashtrays; plan for triggers (after meals, with tea, with certain friends) with if-then plans (PD-M08-L03); call the quitline or see a doctor; expect cravings to peak in the first week and fade.

**With others:** encourage parents over 40 to have yearly blood pressure and sugar checks (go with them). Never shame someone for tobacco or alcohol; offer help and the quitline number.
""",
    resources=[
        ('quitline', 'Read about the services and save the number', '5 minutes'),
        ('telemanas', 'Save the number if you haven\'t already (for alcohol or substance concerns too)', '2 minutes'),
        ('who-pa', 'Re-read the health benefits of physical activity as part of prevention', '5 minutes'),
    ],
    steps=[
        'Write your family history and fill in what you know of your last check-ups.',
        'Visit your Family Health Centre, PHC or a doctor for a blood-pressure and blood-sugar check (and ask what cancer screening is offered).',
        'Fill in your prevention plan with results and next due dates, and set reminders.',
        'Write your tobacco and alcohol plan, and track water for three hot days (bottle refills or urine colour).',
    ],
    proof='Your completed prevention plan with check-up results and next due dates, reminder screenshots, your tobacco and alcohol plan, and three days of hydration notes.',
    templates=[('Quit plan (tobacco or alcohol)', """QUIT OR CUT-DOWN PLAN
What: tobacco / alcohol    Current use: ______    Goal: quit / limit to ______
Quit or change date: ______ (within 2 weeks)  Told: ______
Triggers -> if-then plans:
  If ______ (after lunch / with tea / with friends), then I will ______.
  If I get a craving, then I will wait 10 minutes, drink water, walk.
Help: Tobacco Quitline 1800-11-2356 | Tele-MANAS 14416 | doctor ______
Days without: ______  Money saved: Rs ______""", '')],
    mistakes=[
        ('Waiting for symptoms.', 'High blood pressure and diabetes are often silent. Check them.'),
        ('Buying expensive full-body packages instead of the basics.', 'Blood pressure and sugar checks, guided by your doctor, cover the essentials.'),
        ('Forcing "8 glasses".', 'Drink to thirst, more in heat; watch urine colour.'),
        ('Thinking chewing tobacco is safer than smoking.', 'Chewing tobacco is a major cause of mouth cancer.'),
    ],
    quiz=[
        Q('Why are blood-pressure and sugar checks important at 30 even if you feel well?', 'High blood pressure and diabetes are often silent for years', 'They are only for old people', 'They cure disease', 'They are required by law', why='Early detection allows early action.'),
        Q('What is a sensible hydration guide?', 'Drink when thirsty, more in heat and exercise; aim for pale-yellow urine', 'Exactly 8 glasses for everyone', 'Only drink at meals', 'Soft drinks count the same as water', why='Needs vary; thirst and urine colour are practical guides.'),
        Q('What is the National Tobacco Quitline number?', '1800-11-2356', '14416', '1930', '112', why='Toll-free counselling for quitting tobacco.'),
        Q('What did WHO state about alcohol in 2023?', 'No level of alcohol consumption is safe for health', 'Two drinks a day protect the heart', 'Alcohol is safe for young people', 'Only spirits are harmful', why='WHO\'s 2023 statement; less is always better.'),
    ],
    study='read the lesson and save the quitline and Tele-MANAS numbers',
    action='get a blood-pressure and sugar check, write your prevention plan with reminders, and write your tobacco and alcohol plan',
)

LESSONS = [L1]

MODULE = module(
    22,
    overview=f"""
Preventive health for a 30-year-old in Kerala: which simple check-ups to get and when (blood pressure, blood sugar, teeth, eyes, cancer screening, vaccinations), sensible hydration, and cutting tobacco and alcohol harm, with free helplines.

Prevention is boring and enormously valuable. Kerala's high rates of diabetes and high blood pressure mean the most useful health action you can take this month may be a free check at your Family Health Centre.

This is general information, not medical advice for your situation. Your doctor's advice comes first, especially if you have a family history or existing condition.
""",
    outcomes=[
        'List the key check-ups for an adult around 30 and how often to get them.',
        'Use thirst, heat and urine colour to guide hydration.',
        'Explain tobacco and alcohol risks and where to get help to quit.',
        'Write a personal prevention plan with reminders.',
    ],
    lessons=LESSONS,
    project='a personal prevention plan with a real check-up',
    project_steps=[
        'Get a blood-pressure and blood-sugar check.',
        'Complete the prevention plan with results and next due dates.',
        'Set reminders and help one family member over 40 book a check.',
        'Add your check-up dates and any quit plan to your Playbook.',
    ],
    project_proof='The completed plan with results, reminder screenshots and a note on helping a family member.',
    rubric=[
        ('Check-up', 'None done', 'Booked', 'Done, with results recorded'),
        ('Plan', 'No plan', 'Partial plan', 'Complete plan with next due dates and reminders'),
        ('Tobacco and alcohol', 'Not considered', 'Considered', 'A clear plan (none, quit or limit) with help numbers saved'),
        ('Family', 'No action', 'Talked about it', 'Helped a family member book or attend a check'),
    ],
    short=[
        'Get your blood pressure checked this month.',
        'Save the quitline and Tele-MANAS numbers.',
    ],
    flashcards=[
        ('Two silent conditions to check from 30', 'High blood pressure and diabetes.'),
        ('Blood pressure check frequency', 'At least once a year for adults; more if borderline.'),
        ('Hydration guide', 'Drink to thirst, more in heat; pale-yellow urine.'),
        ('"8 glasses" rule', 'No strong basis; needs vary.'),
        ('Tobacco Quitline', '1800-11-2356 (toll-free).'),
        ('Safe level of tobacco', 'None.'),
        ('WHO on alcohol (2023)', 'No level is safe for health.'),
    ],
    mistakes=[
        ('Avoiding check-ups for fear of bad news.', 'Early news is the good kind: easier to act on.'),
        ('Relying on internet self-diagnosis.', 'See a doctor for symptoms and results.'),
        ('Quitting tobacco without a plan.', 'Use a date, triggers, if-then plans and the quitline.'),
    ],
    tools=[
        'The personal prevention plan and quit or cut-down plan (PD-M22-L01).',
    ],
    playbook=[
        'Check-ups: BP and sugar every ______; dental yearly; next due ______.',
        'Tobacco: none. Alcohol: ______. Water: to thirst, more in heat.',
    ],
)
