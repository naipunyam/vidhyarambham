from common import lesson, module, link, xref, table, Q

L1 = lesson(
    10, 1,
    outcome='You can explain what emotions are and why bad feelings weigh more than good ones, and use precise emotion labelling to calm strong feelings.',
    split='20 minutes reading, 25 minutes of tasks',
    principle='Emotions are fast whole-body evaluations of what matters to you; bad experiences weigh more than good ones, and putting a feeling into precise words can turn its volume down.',
    science=f"""
**What an emotion is.** Psychologists describe emotions as short, fast responses to something that matters to you, with several parts working together: an **appraisal** (how you interpret the situation), **body changes** (heart rate, breathing, muscle tension), a **feeling**, an **urge to act** (fight, flee, hug, hide) and an **expression** (face, voice). OpenStax 10.4 describes the main theories: James-Lange (body change comes first and we feel it), Cannon-Bard (they happen together), and Schachter-Singer's two-factor theory (we feel arousal and then label it from context). Modern views, such as Lisa Feldman Barrett's theory of constructed emotion, stress that the brain **predicts and constructs** emotions using past experience and context. Researchers still debate how many "basic" emotions there are and whether faces express them the same way everywhere.

**Why emotions exist.** Each one carries information and prepares action: fear prepares you to escape danger, anger to remove an obstacle or injustice, sadness to slow down and seek support after a loss, guilt to repair a wrong, joy to connect and explore. Emotions are not the enemy of good decisions (PD-M01-L02); they become problems when they don't fit the facts, are too strong, or last too long.

**Negativity bias.** "Bad is stronger than good," wrote Roy Baumeister and colleagues in a 2001 review: losses, criticism, conflict and bad events tend to affect us more and longer than equal good ones. Paul Rozin and Edward Royzman described the same "negativity dominance". This made sense in evolution (missing a snake was costlier than missing a fruit), but today it makes one harsh comment outweigh ten kind ones. Some popular "magic ratios" (such as exactly five positive interactions for every negative one in relationships) are rough rules of thumb with weak evidence, not laws (PD-M31-L02).

**Labelling emotions.** In brain-imaging studies led by Matthew Lieberman (2007), people who put feelings into words while looking at emotional faces ("angry", "scared") showed less activity in the amygdala, a brain region involved in threat. Other studies found that labelling feelings while facing a feared spider reduced physical fear responses. This is called **affect labelling**. Related work by Lisa Feldman Barrett and Todd Kashdan suggests that people with more **emotional granularity** (who can tell apart "frustrated", "disappointed", "hurt" and "embarrassed" instead of just "bad") cope better with stress. Effects are moderate and the brain findings come from small studies, but the practice costs nothing.
""",
    evidence=[
        ('Emotions involve appraisal, body, feeling, urge and expression', 'strong', 'Broad agreement across theories, despite debates about details.'),
        ('Negativity bias: bad events weigh more than good ones', 'strong', 'Large reviews across many areas of psychology.'),
        ('Exact "magic ratios" such as 5:1', 'mixed', 'Rough rules of thumb; the precise numbers are not well supported.'),
        ('Affect labelling reduces emotional intensity', 'moderate', 'Several lab and brain-imaging studies; mostly small samples.'),
        ('Emotional granularity helps coping', 'moderate', 'Supported by several studies; mostly correlational.'),
    ],
    example="""
Sreeja's aunt says at a family function, "Still no job? Your cousin got posted already." Sreeja smiles, but on the bus home she feels "terrible" and replays the comment all evening, forgetting the twelve kind things relatives said (negativity bias).

At home she tries labelling. "Terrible" becomes more precise: **embarrassed** (in front of others), **hurt** (by someone she loves), **anxious** (about the next exam) and a little **angry** (it was unfair). Saying each word slowly, she notices her chest loosen a little. Each label also points to a different need: the embarrassment fades with time; the hurt might need a calm conversation with her aunt later; the anxiety is about the exam, which she can act on; the anger tells her she values fairness. She writes three lines in her journal and sleeps better than she expected.
""",
    apply="""
**Name it to tame it (1–2 minutes, when a feeling is strong):**

1. **Notice** the body: where is it? (chest, throat, stomach, jaw)
2. **Label** it as precisely as you can, in English or Malayalam. Use the word list in the template. Try for two or three words.
3. **Rate** each 0–10.
4. **Ask:** "What is this feeling telling me? What do I need?"

**Balance negativity bias:** at the end of the day, write down three things that went well (you will make this a practice in PD-M12-L02). When one criticism stings, deliberately recall two or three pieces of good feedback too.

**With others:** labelling also helps other people. Instead of "Don't worry" or "Calm down", try a guess: "It sounds like you're really frustrated with the office." People feel understood when you name the emotion correctly, and calmer. Don't insist if your guess is wrong; ask.
""",
    resources=[
        ('os-10', 'Read 10.4 Emotion fully: theories, facial expressions and culture', '30 minutes'),
        ('noba', 'Search for the module "Functions of Emotions" and read the main sections', '20 minutes'),
        ('ggsc', 'Take the free Emotional Intelligence quiz (find it under Quizzes) and read the feedback', '15 minutes'),
    ],
    steps=[
        'Copy the emotion word list into your phone or Playbook notebook.',
        'For five days, twice a day (once at a calm moment, once when a feeling is strong), label your emotions with two or three precise words and rate them 0–10.',
        'Once, use labelling with another person: guess their feeling aloud ("It sounds like you\'re…") and note how they responded.',
        'At the end, write your three most common emotions and what each was telling you.',
    ],
    proof='Ten dated labelling entries over five days, one note about labelling someone else\'s feeling, and your three most common emotions.',
    templates=[('Emotion labelling log and word list', """EMOTION WORD LIST (use 2-3 words; English or Malayalam)
Anger family:   annoyed, irritated, frustrated, resentful, furious     (ദേഷ്യം)
Fear family:    uneasy, nervous, worried, anxious, scared, panicky       (ഭയം, ഉത്കണ്ഠ)
Sadness family: disappointed, hurt, lonely, discouraged, grieving        (സങ്കടം)
Shame family:   embarrassed, awkward, guilty, ashamed, humiliated        (നാണക്കേട്, കുറ്റബോധം)
Joy family:     content, relieved, pleased, proud, excited, grateful     (സന്തോഷം)
Others:         bored, jealous, envious, confused, overwhelmed, hopeful, calm
LOG
Date/time | Situation | Body (where?) | Words (2-3) | 0-10 each | What it tells me / what I need""", '')],
    mistakes=[
        ('Stopping at "good" or "bad".', 'Precise words carry more information and calm more. Push for two or three specific words.'),
        ('Judging the emotion.', '"I shouldn\'t feel jealous" adds shame on top. Name it, then decide what to do.'),
        ('Labelling others\' feelings as a fact.', 'Offer a guess and accept correction.'),
        ('Believing exact ratios like "5 good for 1 bad".', 'Negativity bias is real; the precise numbers are not.'),
    ],
    quiz=[
        Q('What is "negativity bias"?', 'Bad experiences tend to affect us more strongly and longer than equal good ones', 'Always thinking negatively', 'A mental illness', 'Preferring negative people', why='Baumeister\'s review: bad is stronger than good across many areas.'),
        Q('What did affect-labelling studies find?', 'Putting feelings into words reduced emotional intensity and threat-related brain activity', 'Talking about feelings makes them stronger', 'Labelling has no effect', 'Only writing in English works', why='Labelling turned down the volume in several studies.'),
        Q('Which is the best response to a friend upset about work?', '"It sounds like you\'re really frustrated with your boss."', '"Calm down."', '"Don\'t worry about it."', '"At least you have a job."', why='Naming the likely feeling helps people feel understood.'),
        Q('What does high "emotional granularity" mean?', 'Being able to tell similar emotions apart precisely', 'Having very strong emotions', 'Having no emotions', 'Hiding emotions well', why='Fine distinctions are linked to better coping.'),
    ],
    study='read the lesson and OpenStax 10.4',
    action='label your emotions twice a day for five days and name one other person\'s feeling',
)

L2 = lesson(
    10, 2,
    outcome='You can use cognitive reappraisal instead of suppression, and practise empathy (both understanding and caring) without burning out.',
    split='20 minutes reading, 25 minutes of tasks',
    principle='Changing how you interpret a situation (reappraisal) usually works better than hiding your feelings (suppression); empathy means understanding and caring about others\' feelings, and it can be trained.',
    science=f"""
**Emotion regulation.** James Gross's widely used "process model" describes several points where we can regulate emotions: choosing or changing situations, shifting attention, changing how we think about the situation (**reappraisal**), and changing our response (for example, **suppression**: hiding the expression).

**Reappraisal versus suppression.** In studies by Gross and Oliver John, people who habitually **reappraise** ("This interview is practice for the next one"; "He's rude because he's stressed, not because of me") reported more positive emotion, better relationships and wellbeing. People who habitually **suppress** (keeping a straight face while boiling inside) reported less positive emotion and, in experiments, remembered less of conversations, and their conversation partners felt less connected. A meta-analysis by Thomas Webb and colleagues (2012) found reappraisal strategies had small to moderate effects on emotion, while suppressing expression changed what others saw more than what people felt. Important caveats: suppression is sometimes the right short-term choice (at a funeral, in front of a hostile officer), and some research suggests cultural differences: in some Asian samples, suppression is less strongly linked to harm, possibly because emotional restraint is more valued. Reappraisal is not about pretending; it is about finding an interpretation that is **also true** but more helpful. The {link('ggia-silver', 'Finding Silver Linings')} practice is a structured form of it.

**Empathy.** Psychologists distinguish:
- **Cognitive empathy:** understanding what someone feels and thinks (perspective-taking).
- **Emotional empathy:** feeling some of what they feel.
- **Compassion (empathic concern):** caring about them and wanting to help.

Research by Tania Singer and Olga Klimecki suggests that strong emotional empathy alone, without compassion, can lead to distress and burnout (common among carers and nurses), while compassion training was linked to more positive feelings and helping. Empathy can be improved with practice: perspective-taking exercises, listening (Module 25), reading fiction (some studies, mixed replications) and meeting people different from you.

**Emotional intelligence (EI).** Peter Salovey and John Mayer defined EI as the ability to perceive, use, understand and manage emotions. Daniel Goleman's 1995 bestseller claimed EI matters more than IQ for success; that claim was overstated. Ability-based EI tests predict some outcomes modestly, but measures vary in quality and overlap with personality and intelligence. The *skills* in this module are useful whatever the label.
""",
    evidence=[
        ('Reappraisal is linked to better wellbeing than habitual suppression', 'strong', 'Many studies, including experiments and a meta-analysis; effects small to moderate.'),
        ('Suppression is always harmful', 'mixed', 'Context and culture matter; sometimes suppression is the right short-term choice.'),
        ('Compassion training reduces empathic distress', 'moderate', 'Supported by several studies, mostly from a few labs.'),
        ('"EI matters more than IQ" for success', 'failed', 'Overstated; EI measures predict some outcomes modestly.'),
        ('Perspective-taking improves understanding of others', 'moderate', 'Supported, though people often still guess others\' thoughts poorly; asking works better.'),
    ],
    example="""
Vinod's customer shouts at him because a repaired phone failed again. Vinod's first reaction is anger, and his urge is to shout back.

**Suppression** would mean smiling while fuming, then snapping at his mother at home. Instead, he tries **reappraisal**: "This man's phone is his work; he's scared of losing customers, not attacking me personally" (a true and more helpful view). His anger drops enough to listen.

He uses **cognitive empathy** ("You must have lost calls all morning"), and the customer calms down. He checks the phone, finds a loose connector he missed, fixes it free, and the customer thanks him. Vinod notices that he doesn't have to *feel* the customer's panic (emotional empathy) to help; understanding and caring (compassion) are enough, and they leave him less drained. That evening he writes a reappraisal for his own frustration about the mistake: "One missed connector in 40 repairs this month; I'll add a final checklist."
""",
    apply="""
**Reappraisal questions (choose one when a feeling is too strong or doesn't fit):**
- "What else could explain this?" (other people's behaviour)
- "How will I see this in a week, a year?" (distance)
- "What can I learn or gain from this?" (silver lining, without denying the bad)
- "What would I tell a friend?" (perspective)

**When suppression is right:** if expressing a feeling now would cause harm, hold it, but come back to it later (journal, talk to a friend, reappraise).

**Empathy practice:**
1. **Ask, don't guess:** "How are you finding this?" beats imagining their feelings.
2. **Reflect:** "So you're worried that…; is that right?"
3. **Shift to compassion when it gets heavy:** from "I feel their pain" to "I care about them; what small thing can I do?" That protects you from burnout.

**With others:** never use "reframe it!" to dismiss someone's real problem. Reappraisal is a tool you offer yourself; with others, listen first.
""",
    resources=[
        ('ggia-silver', 'Do the Finding Silver Linings practice once, following its steps', '15 minutes'),
        ('ggia', 'Search for an empathy or perspective-taking practice (for example "Active Listening" or "Shared Identity") and read it', '10 minutes'),
        ('meditations', 'Read the opening paragraph of the second book: Marcus Aurelius reminds himself each morning that he will meet difficult people, and why they act as they do', '10 minutes'),
    ],
    steps=[
        'Pick three situations this week that trigger strong emotions. For each, write the first interpretation and one reappraisal that is also true.',
        'Do the Finding Silver Linings practice once on something that went wrong recently.',
        'In two conversations, practise ask-and-reflect empathy ("How are you finding…?" then "So you\'re…; is that right?"). Note how the other person responded.',
        'Note one moment you used suppression and whether it was the right choice.',
    ],
    proof='Three reappraisals (first interpretation and reappraisal), one silver-linings entry, two empathy-conversation notes and one suppression note.',
    templates=[('Reappraisal and empathy log', """REAPPRAISAL LOG
Date | Situation | Feeling (0-10) | First interpretation | Reappraisal (also true) | Feeling after (0-10)
Questions: What else could explain this? How will I see this in a year?
           What can I learn from this? What would I tell a friend?
EMPATHY CONVERSATIONS
Date | Who | My question ("How are you finding...?") | My reflection ("So you're...; is that right?") | Their response
SUPPRESSION CHECK
When I held back a feeling: ______ Was it the right choice? ______ Did I come back to it? ______""", '')],
    mistakes=[
        ('Reappraising into denial.', 'A reappraisal must be true. "The loss doesn\'t matter" is denial; "I can learn from this loss" may be true.'),
        ('Suppressing as a habit.', 'Hiding feelings long-term costs connection and memory. Hold them only when needed, then process them.'),
        ('Assuming you know what others feel.', 'Ask and reflect; perspective-taking alone is often wrong.'),
        ('Drowning in others\' feelings.', 'Move from feeling their pain to caring and helping; take breaks.'),
    ],
    quiz=[
        Q('Which strategy is generally linked to better wellbeing?', 'Reappraisal: changing how you interpret a situation', 'Suppression: hiding your feelings', 'Ignoring all emotions', 'Venting angrily every time', why='Habitual reappraisal is linked to more positive emotion and better relationships.'),
        Q('A good reappraisal must be:', 'True as well as more helpful', 'As positive as possible', 'The opposite of your first thought', 'Agreed by everyone', why='Reappraisal is not pretending; it is a truer, more helpful view.'),
        Q('What protects carers from empathic burnout, according to Singer and Klimecki\'s work?', 'Compassion (caring and wanting to help) rather than only sharing distress', 'Avoiding all emotions', 'Working longer hours', 'Suppression', why='Compassion training was linked to positive feelings and helping, empathic distress to burnout.'),
        Q('What is the honest status of "EI matters more than IQ"?', 'Overstated; EI measures predict some outcomes modestly', 'Proven by many studies', 'IQ does not matter', 'EI cannot be measured at all', why='Goleman\'s popular claim went beyond the evidence.'),
    ],
    study='read the lesson and do the Finding Silver Linings practice',
    action='write three reappraisals, do two ask-and-reflect empathy conversations and one suppression check',
)

LESSONS = [L1, L2]

MODULE = module(
    10,
    overview=f"""
Emotions and emotional intelligence: what emotions are and what they are for, negativity bias, precise labelling, reappraisal versus suppression, and empathy without burnout. You keep an emotion log and practise reappraisal on real situations.

Emotions shape almost every decision, conversation and habit. This module treats them as information, not enemies, and gives you three of the best-supported regulation skills: labelling, reappraisal and compassion-based empathy.

It is the foundation for stress and resilience (Module 11), mindfulness (Module 12) and all of Part D (people skills). It is **not therapy**: if strong emotions regularly overwhelm you or last for weeks, read "When to get help" in PD-M11-L01 and talk to a professional.
""",
    outcomes=[
        'Describe the parts of an emotion and what different emotions are for.',
        'Explain negativity bias and balance it deliberately.',
        'Label emotions precisely and use labelling to calm strong feelings.',
        'Use reappraisal and know when suppression is the right short-term choice.',
        'Practise empathy as understanding plus caring, without burning out.',
    ],
    lessons=LESSONS,
    project='a two-week emotion log with reappraisal practice',
    project_steps=[
        'Keep the labelling log for two weeks (at least one entry a day).',
        'Add a reappraisal to at least six entries where the feeling was too strong or didn\'t fit the facts.',
        'Review: your three most common emotions, their usual triggers, and which reappraisal question worked best.',
        'Write a half-page "emotion manual" for yourself: my triggers, what they tell me, what helps.',
    ],
    project_proof='Two weeks of emotion log entries, six reappraisals and your half-page emotion manual.',
    rubric=[
        ('Labelling', 'Only "good" or "bad"', 'Some specific words', 'Two or three precise words in most entries'),
        ('Regulation', 'No reappraisals', 'Reappraisals that deny the problem', 'True, helpful reappraisals with ratings before and after'),
        ('Empathy', 'No practice', 'Guessed others\' feelings', 'Asked and reflected in real conversations'),
        ('Self-knowledge', 'No review', 'A list of emotions', 'A personal emotion manual with triggers and what helps'),
    ],
    short=[
        'Label your strongest feeling each day with two precise words.',
        'Use one reappraisal question when you are upset this week.',
    ],
    flashcards=[
        ('Parts of an emotion', 'Appraisal, body change, feeling, urge to act, expression.'),
        ('Negativity bias', 'Bad events weigh more and last longer than equal good ones.'),
        ('Affect labelling', 'Naming feelings precisely can turn down their intensity.'),
        ('Reappraisal', 'Changing how you interpret a situation; must be true and more helpful.'),
        ('Suppression', 'Hiding expression; changes what others see more than what you feel; costly as a habit.'),
        ('Three kinds of empathy', 'Cognitive (understanding), emotional (sharing), compassion (caring and helping).'),
        ('Protects against empathic burnout', 'Compassion: caring and helping rather than only sharing distress.'),
        ('"EI beats IQ" status', 'Overstated.'),
    ],
    mistakes=[
        ('Trying to have only positive emotions.', 'All emotions carry information. The goal is fit and flexibility, not constant happiness.'),
        ('Using emotional skills to manipulate.', 'Labelling and empathy are for understanding. Using someone\'s feelings against them is manipulation (Module 32).'),
        ('Ignoring persistent distress.', 'If feelings overwhelm daily life for weeks, get professional help.'),
    ],
    tools=[
        'The emotion word list and labelling log (PD-M10-L01).',
        'The reappraisal and empathy log (PD-M10-L02).',
    ],
    playbook=[
        'When a feeling is strong: notice the body, name it precisely, ask what it needs.',
        'My best reappraisal question: "______". With others: ask, reflect, then care.',
    ],
)
