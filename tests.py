"""Baseline and final test materials for Mind, Body and People: the life wheel,
self-rating scales, fitness test protocols and two parallel forms (A at the
start, B at the end) of a 10-question thinking-traps quiz. All questions are
original to this course, modelled on classic problem types."""

import hashlib
import random

LIFE_AREAS = [
    ('Health and fitness', 'energy, strength, sleep, food'),
    ('Mind and emotions', 'calm, mood, handling stress'),
    ('Learning and career', 'PSC preparation, skills, work'),
    ('Money', 'income, savings, control over spending'),
    ('Family', 'relationships at home'),
    ('Friends and social life', 'people you can call, new connections'),
    ('Fun and rest', 'hobbies, play, real breaks'),
    ('Purpose and contribution', 'meaning, helping others, community'),
]

SELF_RATINGS = {
    'Confidence': [
        'When I set myself a hard task, I believe I can do it if I keep working.',
        'I try new things even when I might fail at first.',
        'I can say what I think in a group without rehearsing it many times.',
        'A setback or a "no" does not ruin my week.',
        'I feel comfortable being seen by others (on video, on a stage, in a shop).',
    ],
    'Social confidence': [
        'I can start a conversation with a stranger (a shopkeeper, a person at a bus stop).',
        'I can keep a conversation going for five minutes with someone new.',
        'I can ask for help, advice or a discount without much fear.',
        'I can say no to a friend or relative politely and clearly.',
        'I have at least three people I could call if I needed help.',
    ],
    'Listening': [
        'I let people finish their sentences before I reply.',
        'I ask follow-up questions about what people tell me.',
        'I can sum up what someone said to their satisfaction.',
        'I remember the names of people I meet.',
        'People tell me things they do not tell others.',
    ],
}

QUIZ_A = [
    {'q': 'A pen and a notebook cost Rs 110 together. The notebook costs Rs 100 more than the pen. How much does the pen cost?',
     'o': ['Rs 5', 'Rs 10', 'Rs 15', 'Rs 1'], 'a': 'A',
     'why': 'Rs 5 (the notebook is Rs 105). The quick answer, Rs 10, comes from fast thinking: then the notebook would cost Rs 110 and the total Rs 120. Trap: answering before checking (PD-M01-L01).'},
    {'q': 'Ravi from Kozhikode district is quiet, loves books and keeps everything in order. Which is he more likely to be?',
     'o': ['A farmer or farm worker', 'A librarian', 'Both are equally likely', 'Impossible to say anything'], 'a': 'A',
     'why': 'There are far more people in farming than librarians, so even if quiet book-lovers are more common among librarians, a random quiet book-lover is still more likely to farm. Trap: ignoring base rates (the representativeness heuristic, PD-M01-L02).'},
    {'q': 'Meera studied economics and was active in her college union. Which is more probable?',
     'o': ['Meera works in a bank', 'Meera works in a bank and is active in a trade union', 'Both are equally probable', 'The second, because it fits her better'], 'a': 'A',
     'why': 'Two things being true together can never be more likely than one of them alone. The second sounds more like her, which is the trap (the conjunction fallacy, PD-M01-L02).'},
    {'q': 'You paid Rs 300 for a film ticket. After 30 minutes the film is awful and you have a headache. What is the sensible way to decide whether to stay?',
     'o': ['Ignore the Rs 300 and ask whether the next 90 minutes are worth more than what else you could do', 'Stay, or the Rs 300 is wasted', 'Stay only if the ticket cost more than Rs 200', 'Leave only if friends leave first'], 'a': 'A',
     'why': 'The Rs 300 is spent whether you stay or leave. Only future costs and benefits matter. Trap: the sunk-cost fallacy (PD-M03-L01).'},
    {'q': 'The last three times you planned to finish a PSC topic "in one week", it took about two weeks. How long should you plan for the next similar topic?',
     'o': ['About two weeks, based on your record', 'One week, because this time you will focus harder', 'Four days, to push yourself', 'You cannot plan at all'], 'a': 'A',
     'why': 'Your own track record (the outside view) is a better guide than your hopes for this time. Trap: the planning fallacy (PD-M03-L01).'},
    {'q': 'A coach shouts at players after their worst match and praises them after their best. Next match, the shouted-at players improve and the praised ones do worse. What is the most likely reason?',
     'o': ['Unusually good or bad results tend to be followed by more ordinary ones anyway', 'Shouting works better than praise', 'Praise makes people lazy', 'The players were trying to upset the coach'], 'a': 'A',
     'why': 'Extreme results are partly luck, so the next result is usually closer to average whatever the coach does. This is regression to the mean (PD-M02-L01).'},
    {'q': 'A survey finds that people who drink tea at a tea shop every day have more friends. What does this show?',
     'o': ['Tea-shop visits and friendships go together; it does not show that one causes the other', 'Tea makes people friendly', 'Having friends makes people drink tea', 'Nothing, because surveys are always wrong'], 'a': 'A',
     'why': 'A correlation can come from a third factor (sociable people visit tea shops and make friends) or run either way. Trap: treating correlation as causation (PD-M02-L01).'},
    {'q': 'A fair coin has landed heads five times in a row. What is the chance of heads on the next toss?',
     'o': ['50%', 'Less than 50%, because tails is due', 'More than 50%, because heads is on a streak', 'Exactly 1 in 32'], 'a': 'A',
     'why': 'The coin has no memory: still 50%. Trap: the gambler\'s fallacy (PD-M01-L02).'},
    {'q': 'A TV channel shows three house fires in Kozhikode this week. Your aunt says house fires are now very common. What should you check first?',
     'o': ['How many house fires happen in a normal year, from official or long-term figures', 'Whether the videos looked real', 'How many people shared the news on WhatsApp', 'Nothing: three fires in a week proves it'], 'a': 'A',
     'why': 'Vivid recent stories make events feel common. Only base figures over time tell you if they are. Trap: the availability heuristic (PD-M03-L01).'},
    {'q': 'A shop shows "MRP Rs 4,999, today Rs 1,999" on a pair of earphones. What is the best way to judge the price?',
     'o': ['Compare the Rs 1,999 with what other shops and sites charge for the same model', 'Rs 3,000 off is a great deal', 'Buy now, because "today" means it ends tonight', 'Higher MRP means better quality'], 'a': 'A',
     'why': 'The MRP is a number the seller chose; it anchors your sense of value. Real comparison prices are the only fair test. Traps: anchoring and false urgency (PD-M03-L01, PD-M32-L02).'},
]

QUIZ_B = [
    {'q': 'A bat and a ball (for gully cricket) cost Rs 220 together. The bat costs Rs 200 more than the ball. How much is the ball?',
     'o': ['Rs 10', 'Rs 20', 'Rs 2', 'Rs 22'], 'a': 'A',
     'why': 'Rs 10 (the bat is Rs 210). The quick answer, Rs 20, would make the total Rs 240. Same trap as before: fast thinking unchecked (PD-M01-L01).'},
    {'q': 'Salma from Vadakara is shy, precise and loves numbers. Which is she more likely to work as?',
     'o': ['A shop or office worker', 'A professional statistician', 'Equally likely', 'There is no way to reason about it'], 'a': 'A',
     'why': 'Shop and office workers vastly outnumber statisticians, so the base rate wins even though the description "sounds like" a statistician (representativeness, PD-M01-L02).'},
    {'q': 'Arun loves cricket and coaches children on weekends. Which is more probable?',
     'o': ['Arun is a teacher', 'Arun is a teacher and plays in a local cricket club', 'Both are equally probable', 'The second, because the details fit'], 'a': 'A',
     'why': 'Adding a detail can only make a story less probable, even when it makes it more convincing (conjunction fallacy, PD-M01-L02).'},
    {'q': 'You have spent eight months and Rs 6,000 on a coaching class that you now find much worse than free material. What matters most in deciding whether to continue?',
     'o': ['Which option will help you most from now on, counting only future time and money', 'The Rs 6,000 already paid', 'What the class teacher will think', 'That you have already spent eight months'], 'a': 'A',
     'why': 'Money and time already spent cannot be recovered either way. Judge only the future (sunk cost, PD-M03-L01).'},
    {'q': 'Your friend says he will finish building his YouTube channel "in a month". Projects like his usually take three to four months. What is the best estimate?',
     'o': ['Three to four months, unless he has a specific reason to be faster', 'One month: he is very motivated', 'Two weeks', 'It will never happen'], 'a': 'A',
     'why': 'The typical time for similar projects (the outside view, or reference class) beats an inside-view guess (planning fallacy, PD-M03-L01).'},
    {'q': 'A student scores 98% in one mock test after months of 70s. In the next mock he scores 78%. What is the likeliest explanation?',
     'o': ['Part of the 98% was luck, and scores tend to drift back towards the usual level', 'He became lazy after the high score', 'The second test was rigged', 'He forgot everything in one week'], 'a': 'A',
     'why': 'An extreme score is usually partly luck, so the next one is closer to average: regression to the mean (PD-M02-L01).'},
    {'q': 'Students who use a certain study app score higher in exams. What can we conclude?',
     'o': ['Users score higher; without an experiment we don\'t know if the app causes it', 'The app raises scores', 'Good students avoid the app', 'Apps never help'], 'a': 'A',
     'why': 'Keen students may both download apps and score well. Only a fair comparison (ideally random assignment) shows cause (PD-M02-L01).'},
    {'q': 'In a lottery, the number 7 has not come up as the first digit for 20 draws. What is the chance it comes up next time?',
     'o': ['The same as any other digit', 'Higher, because it is overdue', 'Lower, because it is unlucky', 'Certain within two more draws'], 'a': 'A',
     'why': 'Each draw is independent: past draws do not change the odds (gambler\'s fallacy, PD-M01-L02).'},
    {'q': 'After a friend\'s phone was hacked, you feel that most phones in your town are being hacked. What would tell you if that is true?',
     'o': ['Figures on how often phones are hacked, compared with how many phones there are', 'How upset your friend was', 'How many forwards about hacking you received', 'Your feeling, because it is strong'], 'a': 'A',
     'why': 'One vivid case feels like many. Rates and base numbers decide (availability, PD-M03-L01).'},
    {'q': 'A salesman first shows you a Rs 45,000 phone and then a Rs 22,000 one, which suddenly feels cheap. What is happening?',
     'o': ['The first price is acting as an anchor for the second', 'The second phone is objectively good value', 'Phones are always cheaper the second time', 'The salesman made a mistake'], 'a': 'A',
     'why': 'The first number you see pulls your judgement towards it. Compare with your own budget and with other shops instead (anchoring, PD-M03-L01, PD-M29-L01).'},
]
assert len(QUIZ_A) == len(QUIZ_B) == 10


def mcq(questions, form):
    """Shuffle options with a fixed seed so the paper is stable between builds."""
    qs, key = [], []
    for i, q in enumerate(questions, 1):
        rng = random.Random(int(hashlib.md5((form + q['q']).encode('utf-8')).hexdigest(), 16))
        order = list(range(len(q['o'])))
        rng.shuffle(order)
        opts = [q['o'][k] for k in order]
        letter = 'ABCD'[order.index('ABCD'.index(q['a']))]
        qs.append(f"{i}. {q['q']}\n" + '\n'.join(f'    - {chr(65 + j)}) {o}' for j, o in enumerate(opts)))
        key.append(f"{i}. **{letter}.** {q['why']}")
    return '\n'.join(qs), '\n'.join(key)


FITNESS_TESTS = [
    ('Push-ups', 'Full push-ups on the floor, or from the knees if you cannot do 5 full ones. Body straight from head to knees or heels, chest to a fist\'s height from the floor, arms fully straight at the top. Count clean reps until form breaks. Write which version you did and use the same version at the end.', 'reps'),
    ('Plank hold', 'Forearms under shoulders, body in a straight line, squeeze your seat. Time it until your hips sag or lift. Stop at 3 minutes at most.', 'seconds'),
    ('1 km walk or walk-run', 'A flat, safe 1 km route (a marked km stone, a school ground, or measured with a maps app). Brisk walk, or walk-run if you already run. Time it.', 'minutes:seconds'),
    ('Resting heart rate', 'In the morning before tea or coffee, sit quietly for 5 minutes, find the pulse at your wrist or neck and count for 30 seconds, then double it. Do it on 3 mornings and take the average.', 'beats per minute'),
    ('Sit and reach', 'Sit on the floor, legs straight, feet against a wall or step. Reach forward slowly with both hands, no bouncing. Measure with a ruler or tape from fingertips to toes: minus if short of the toes, plus if past them.', 'centimetres'),
]
