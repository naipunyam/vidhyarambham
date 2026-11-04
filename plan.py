"""The course plan for Mind, Body and People: module titles, lesson titles and
part-time hours. Weeks are assigned here once, greedily, so every part-time
week stays near the target study load. Daily practices (meditation, workouts,
the habit tracker, challenges) are counted separately: they are the habits the
course builds, done in minutes a day, not study hours."""

PARTS = [
    # (letter, title, first module, last module)
    ('A', 'Understand your mind', 1, 4),
    ('B', 'Master yourself', 5, 16),
    ('C', 'Strengthen your body', 17, 23),
    ('D', 'Win with people (ethically)', 24, 33),
    ('E', 'Character and purpose', 34, 36),
]

MODULES = [
    # ---- Part A
    ('How the mind works', [
        ('Fast and slow thinking', 1.0),
        ('Mental shortcuts, and emotion versus reason', 1.0)], 0.75),
    ('Reading psychology research', [
        ('Experiments, correlations and sample sizes', 1.0),
        ('The replication crisis, and telling science from pop psychology', 1.0)], 0.75),
    ('Thinking traps', [
        ('Seven cognitive biases that cost you every week', 1.25),
        ('Cognitive distortions: the CBT list', 1.0),
        ('Debiasing, and the bias journal', 1.0)], 1.0),
    ('Critical thinking and decisions', [
        ('Deciding under uncertainty', 1.0),
        ('Pre-mortems, choice overload and regret', 1.0)], 0.75),
    # ---- Part B
    ('Self-awareness', [
        ('Values and the life wheel', 1.0),
        ('Big Five personality, VIA strengths, and the limits of type tests', 1.25)], 0.75),
    ('Motivation', [
        ('Self-determination theory: intrinsic and extrinsic motivation', 1.0),
        ('Goal-setting theory and the progress principle', 1.0)], 0.75),
    ('Goals and life design', [
        ('Vision and the 12-month plan', 1.25),
        ('The weekly plan and the weekly review', 1.0)], 0.75),
    ('Self-control and habits', [
        ('Present bias, commitment devices and temptation bundling', 1.0),
        ('Environment design and the habit loop', 1.0),
        ('If-then plans, tiny habits and identity-based change', 1.0),
        ('Procrastination, and a two-week personal experiment', 1.25)], 1.0),
    ('Mindset and self-talk', [
        ('Growth mindset: what the evidence really says', 1.0),
        ('Limiting beliefs and self-compassion', 1.0)], 0.75),
    ('Emotions and emotional intelligence', [
        ('What emotions are, negativity bias and labelling', 1.0),
        ('Reappraisal and empathy', 1.0)], 0.75),
    ('Stress and resilience', [
        ('The stress response, and when to get help', 1.0),
        ('CBT thought records', 1.0),
        ('Stoic practices and handling failure', 1.0)], 1.0),
    ('Mindfulness', [
        ('Meditation and breathwork', 1.0),
        ('Journaling and gratitude', 1.0)], 0.75),
    ('Confidence and courage', [
        ('Self-efficacy, the spotlight effect and impostor feelings', 1.0),
        ('Fear ladders: exposure step by step', 1.0)], 0.75),
    ('Rejection therapy', [
        ('The idea and the psychology behind it', 1.0),
        ('The rules and the 30-step ladder', 1.25),
        ('The 30-day challenge, comfort-zone challenges and where it pays off', 1.0)], 1.0),
    ('Happiness science', [
        ('Hedonic adaptation, social comparison, and money', 1.0),
        ('Meaning and flow', 1.0)], 0.75),
    ('Digital wellbeing and attention', [
        ('How apps capture attention', 1.0),
        ('Your phone plan and a digital-detox day', 1.0)], 0.75),
    # ---- Part C
    ('Fitness at home', [
        ('Safety, warm-ups and the fitness baseline', 1.0),
        ('Bodyweight strength with safe progression', 1.25),
        ('Cardio, mobility and the 30-day fitness challenge', 1.0)], 1.0),
    ('Yoga basics', [
        ('The Common Yoga Protocol, safely', 1.25)], 0.5),
    ('Sleep', [
        ('How sleep works', 1.0),
        ('Your sleep plan', 1.0)], 0.75),
    ('Nutrition with a Kerala diet', [
        ('The balanced Kerala plate', 1.0),
        ('Protein on a budget, and food myths', 1.0)], 0.75),
    ('Posture, ergonomics and eye care', [
        ('A phone and laptop setup that your body can live with', 1.0)], 0.5),
    ('Preventive health', [
        ('Check-ups, hydration, tobacco and alcohol', 1.0)], 0.5),
    ('Grooming, hygiene and dressing well', [
        ('Looking after yourself on a budget', 1.0)], 0.5),
    # ---- Part D
    ('Social perception', [
        ('First impressions, warmth and competence, and the halo effect', 1.0),
        ('The fundamental attribution error, stereotypes and bias', 1.0)], 0.75),
    ('Liking and rapport', [
        ('Why people like each other', 1.0),
        ('Conversation skills and active listening', 1.25),
        ('Names, genuine praise and making people feel important', 1.0)], 1.0),
    ('Communication', [
        ('Storytelling', 1.0),
        ('Assertiveness, saying no and face-saving', 1.0),
        ('Non-violent communication, feedback and difficult conversations', 1.25)], 1.0),
    ('Public speaking in English and Malayalam', [
        ('Building a talk', 1.0),
        ('Voice, body language, nerves and etiquette', 1.0),
        ('Practice that works, and your 5-minute talk', 1.0)], 1.5),
    ('Influence and persuasion', [
        ('The seven principles, honestly', 1.25),
        ('Framing, and the persuasion lab', 1.0)], 1.0),
    ('Negotiation', [
        ('Interests, BATNA and anchoring', 1.0),
        ('A real small negotiation', 1.0)], 0.75),
    ('Group psychology and leadership', [
        ('Conformity and obedience: the classic experiments, honestly', 1.25),
        ('Groupthink, social loafing and the bystander effect', 1.0),
        ('Trust and leading others', 1.0)], 1.0),
    ('Relationships and networking', [
        ('Friendships and family', 1.0),
        ('Conflict, and what makes relationships last', 1.0),
        ('Professional networking', 1.0)], 1.0),
    ('Self-defence against manipulation', [
        ('High-pressure sales and MLM tactics', 1.0),
        ('Scam psychology and dark patterns', 1.25),
        ('Gaslighting and emotional blackmail', 1.0)], 1.0),
    ('Psychology at work', [
        ('Sales, marketing and customer behaviour', 1.0),
        ('Job and PSC interviews, and exam nerves', 1.25)], 0.75),
    # ---- Part E
    ('Character', [
        ('Integrity and responsibility', 1.0),
        ('Humility and humour', 1.0)], 0.75),
    ('Purpose and contribution', [
        ('Meaning, volunteering and giving back', 1.0)], 0.75),
    ('Capstone: your personal operating system', [
        ('Plan the capstone projects', 1.5),
        ('Run the 30 days', 12.5),
        ('Final retest, your Personal Playbook and the next 12 months', 2.0)], 1.0),
]

CAPSTONE = 36
TARGET = 5.5             # part-time study hours a week to aim for
REVIEW_H = 1 / 3         # the weekly reflection, about 20 minutes


def part_of(m):
    for p in PARTS:
        if p[2] <= m <= p[3]:
            return p
    raise ValueError(m)


def assign():
    """Return weeks[(m, l)] = (a, b), project_week[m], last_week, load."""
    load = {0: 3.0}
    weeks, pweek = {}, {}
    w = 1

    def fits(week, h):
        cur = load.get(week, REVIEW_H)
        return cur + h <= TARGET + 0.4

    def put(week, h):
        if week not in load:
            load[week] = REVIEW_H
        load[week] += h

    for m, (title, lessons, ph) in enumerate(MODULES, 1):
        # Each part starts in a fresh week, so it can be taken on its own.
        if any(p[2] == m for p in PARTS) and m > 1 and load.get(w, 0) > 1:
            w += 1
        for l, (lt, h) in enumerate(lessons, 1):
            if m == CAPSTONE and l == 2:
                a = w + 1 if load.get(w, 0) > 1 else w
                for k in range(a, a + 5):
                    put(k, h / 5)
                weeks[(m, l)] = (a, a + 4)
                w = a + 4
                continue
            if not fits(w, h):
                w += 1
            put(w, h)
            weeks[(m, l)] = (w, w)
        if not fits(w, ph):
            w += 1
        put(w, ph)
        pweek[m] = w
    if load.get(w, 0) > TARGET - 1.5:
        w += 1
    put(w, 1.5)  # final retest
    return weeks, pweek, w, load


if __name__ == '__main__':
    weeks, pweek, last, load = assign()
    n = sum(len(x[1]) for x in MODULES)
    for m, (title, lessons, ph) in enumerate(MODULES, 1):
        ws = [weeks[(m, l)] for l in range(1, len(lessons) + 1)]
        print(f'M{m:02d} {title}: weeks {ws[0][0]}-{max(b for a, b in ws)} (project week {pweek[m]}), {sum(h for _, h in lessons) + ph:.2f} h')
    print('lessons', n, 'last week', last)
    print(' '.join(f'{k}:{v:.1f}' for k, v in sorted(load.items())))
    print('total', round(sum(load.values()), 1))
