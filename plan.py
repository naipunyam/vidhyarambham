"""The course plan: module titles, lesson titles and part-time hours.
Weeks are assigned here once, greedily, so every part-time week stays
near the target load (lessons + module projects + the two tracks)."""

MODULES = [
    # (title, [(lesson title, hours)], project hours)
    ('How your brain learns', [
        ('Attention, working memory and cognitive load', 1.25),
        ('Encoding, consolidation, sleep and neuroplasticity', 1.25),
        ('Retrieval and the forgetting curve', 1.25)], 1.0),
    ('Myths to drop', [
        ('Learning styles and other brain myths', 1.0),
        ('Rereading, highlighting, multitasking and speed-reading promises', 1.25)], 0.75),
    ('The six evidence-based strategies', [
        ('Retrieval practice: learn by pulling information out', 1.25),
        ('Spaced practice: a revision schedule that beats cramming', 1.25),
        ('Interleaving: mix problem types for maths and reasoning', 1.25),
        ('Elaboration and concrete examples: ask why, then make it real', 1.25),
        ('Dual coding, and one study session that uses all six', 1.5)], 1.5),
    ('Spaced repetition from zero with AnkiDroid', [
        ('How spaced repetition works, and setting up AnkiDroid', 1.5),
        ('Writing good cards', 1.5),
        ('Cloze deletions and image occlusion', 1.5),
        ('The daily review habit and managing your workload', 1.25)], 2.5),
    ('Focus and deep work', [
        ('Why focus breaks, and how to rebuild your attention span', 1.25),
        ('Pomodoro and time-blocking around real life', 1.25),
        ('Taming your Android phone', 1.25)], 1.0),
    ('Motivation, procrastination and habits', [
        ('Why we procrastinate', 1.25),
        ('Implementation intentions and tiny habits', 1.25),
        ('Rewards, streaks and restarting after a bad week', 1.0)], 1.0),
    ('Metacognition: knowing what you really know', [
        ('Illusions of knowing, and how to judge your learning', 1.25),
        ('Self-testing and confidence ratings', 1.25),
        ('The weekly learning review', 1.25)], 1.0),
    ('Deep understanding', [
        ('Self-explanation and the Feynman technique', 1.5),
        ('Asking good questions', 1.25),
        ('Concept maps, drawn from memory', 1.25),
        ('First-principles thinking', 1.25)], 2.0),
    ('Note-making that leads to recall', [
        ('Cornell notes and outlines', 1.25),
        ('Mind maps and sketchnotes', 1.25),
        ('Turning notes into questions and flashcards', 1.25)], 1.0),
    ('Reading', [
        ('Active reading with SQ3R', 1.25),
        ('Skimming and scanning', 1.0),
        ('Speed and comprehension: the honest truth', 1.25),
        ('Newspapers and current affairs for PSC', 1.25)], 1.0),
    ('Memory techniques', [
        ('Chunking, acronyms and stories for GK lists', 1.25),
        ('The memory palace', 1.5),
        ('Pegs and the major system for numbers, dates and articles', 1.5)], 1.5),
    ('Exam mastery for Kerala PSC', [
        ('Map the syllabus', 1.5),
        ('Analyse previous-year questions', 2.0),
        ('Mock tests and the error log', 1.5),
        ('Time management and negative marking', 1.25),
        ('Your 12-week study and revision plan', 2.0),
        ('Exam anxiety and exam day', 1.25)], 1.5),
    ('Deliberate practice and skill acquisition', [
        ('Deliberate practice and feedback loops', 1.25),
        ('Self-directed learning projects', 1.5)], 1.0),
    ('Numerical ability and reasoning', [
        ('Mental maths tricks', 1.5),
        ('PSC arithmetic: the core topics', 1.5),
        ('Reasoning practice and a maths practice system', 1.5)], 1.5),
    ('Language learning', [
        ('How languages are learned: input, output and vocabulary', 1.25),
        ('English for PSC', 1.5),
        ('Listening, speaking and shadowing', 1.25),
        ('PSC Malayalam, and a plan for any new language', 1.5)], 1.5),
    ('Thinking skills', [
        ('Critical thinking: claims, evidence and sources', 1.25),
        ('Logical reasoning', 1.25),
        ('Mental models and problem solving', 1.25),
        ('Cognitive biases', 1.25)], 1.0),
    ('Learning with AI', [
        ('AI as a Socratic tutor', 1.25),
        ('Quizzes, explanations and checking AI answers', 1.25),
        ('Avoiding over-reliance', 1.0)], 1.0),
    ('Personal knowledge management', [
        ('Linked notes: how a second brain works', 1.25),
        ('Your PSC knowledge base in Joplin or Logseq', 1.5)], 1.0),
    ('Brain health', [
        ('Sleep and learning', 1.0),
        ('Exercise, food and breaks', 1.0),
        ('Stress', 1.0)], 0.75),
    ('Teaching others and study groups', [
        ('Learning by teaching', 1.25),
        ('Study groups that work', 1.0)], 1.5),
    ('Capstone: a 30-day learning sprint', [
        ('Plan the sprint and take the before test', 2.0),
        ('Run the sprint', 22.5),
        ('After tests, reflection report and your learning system for life', 2.0)], 1.0),
]

CAPSTONE = 21
ANKI_MODULE = 4          # the 30-day deck track starts in this module's first week
TARGET = 6.0             # part-time hours a week to aim for
REVIEW_H = 1 / 3         # the weekly learning review, about 20 minutes
ANKI_H = 1.5             # about 15 minutes a day of reviews outside lessons


def assign():
    """Return weeks[(m, l)] = (a, b), project_week[m], anki_start, last_week, load."""
    load = {0: 4.0}
    weeks, pweek = {}, {}
    w = 1
    anki_start = None

    def base(week):
        h = REVIEW_H
        if anki_start and anki_start <= week < anki_start + 5:
            h += ANKI_H if week < anki_start + 4 else ANKI_H / 3
        return h

    def fits(week, h):
        cur = load.get(week, 0) + (0 if week in load else base(week))
        return cur + h <= TARGET + 0.4

    def put(week, h):
        if week not in load:
            load[week] = base(week)
        load[week] += h

    for m, (title, lessons, ph) in enumerate(MODULES, 1):
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
            if m == ANKI_MODULE and l == 1 and anki_start is None:
                if not fits(w, h + ANKI_H):
                    w += 1
                anki_start = w
                if w in load:
                    load[w] += ANKI_H
            put(w, h)
            weeks[(m, l)] = (w, w)
        if not fits(w, ph):
            w += 1
        put(w, ph)
        pweek[m] = w
    put(w, 1.5)  # final retest
    return weeks, pweek, anki_start, w, load


if __name__ == '__main__':
    weeks, pweek, anki, last, load = assign()
    n = sum(len(x[1]) for x in MODULES)
    for m, (title, lessons, ph) in enumerate(MODULES, 1):
        ws = [weeks[(m, l)] for l in range(1, len(lessons) + 1)]
        print(f'M{m:02d} {title}: weeks {ws[0][0]}-{max(b for a, b in ws)} (project week {pweek[m]}), {sum(h for _, h in lessons) + ph:.2f} h')
    print('lessons', n, 'anki start', anki, 'last week', last)
    print(' '.join(f'{k}:{v:.1f}' for k, v in sorted(load.items())))
    print('total', round(sum(load.values()), 1))
