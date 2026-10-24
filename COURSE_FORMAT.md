# Vidhyarambham course format

A course is one JSON file. The app shows its sections in order and tracks a tick for every task.

This guide covers format version 1.

## Add a course in 3 steps

1. Write the course as a document, with sections, tasks and links.
2. Turn the document into a course file. Paste the prompt at the end of this guide into any AI chat, followed by your document, and save the answer as `your-course-id.json`.
3. Add the file in one of two ways:
   - **For everyone:** put it in `public/courses/` and add its file name to `public/courses/index.json`. The site rebuilds by itself, and the course appears after a few minutes.
   - **On one phone only:** open the app, tap **Add a course**, and choose the file or paste a link to it.

Before a file goes into `public/courses/`, the build runs `npm run check-courses`. A course file with a mistake stops the deploy, and the error message names the field to fix. The live site stays as it was.

## The smallest valid course

```json
{
  "format": "vidhyarambham-course",
  "formatVersion": 1,
  "id": "spoken-english",
  "version": 1,
  "title": "Spoken English in 8 weeks",
  "sections": [
    {
      "id": "week-1",
      "title": "Week 1: Introducing yourself",
      "kind": "level",
      "weeks": [1, 1],
      "content": "Practise a 1-minute introduction every day.",
      "tasks": [
        { "id": "w1-intro", "text": "Record a 1-minute introduction", "kind": "project" }
      ]
    }
  ]
}
```

## Course fields

| Field | Required | What it is |
| --- | --- | --- |
| `format` | Yes | Always `"vidhyarambham-course"` |
| `formatVersion` | Yes | Always `1` for this guide |
| `id` | Yes | A short name that never changes, such as `ai-generalist`. Lowercase letters, numbers and hyphens, up to 64 characters. |
| `version` | Yes | Start at `1`. Raise it by 1 every time you update the course. |
| `title` | Yes | The name shown in the app |
| `summary` | No | One or two sentences shown under the title |
| `language` | No | For example `en` or `ml` |
| `updated` | No | Date of the last change, written as `2026-10-21` |
| `totalWeeks` | No | Number of course weeks; the schedule stops counting after it |
| `paces` | No | Ways to take the course (see below). Without it, one course week is one calendar week. |
| `sections` | Yes | The parts of the course, in reading order |

## Paces

```json
"paces": [
  { "id": "full", "label": "Full pace", "hoursPerWeek": 15, "weekLength": 1, "note": "24 weeks" },
  { "id": "light", "label": "Light pace", "hoursPerWeek": 7.5, "weekLength": 2, "note": "About 12 months" }
]
```

`weekLength` is how many calendar weeks one course week takes: `1` for full pace, `2` for half pace. The first pace in the list is the default.

## Section fields

| Field | Required | What it is |
| --- | --- | --- |
| `id` | Yes | Unique inside the course, such as `level-0` |
| `title` | Yes | Shown as the section heading |
| `kind` | Yes | One of `intro`, `setup`, `level`, `gate`, `track`, `capstone`, `reference` |
| `weeks` | No | `[startWeek, endWeek]`, such as `[1, 2]`. Week 0 is allowed for setup. Sections with weeks appear in "This week". |
| `hours` | No | Rough hours at full pace |
| `summary` | No | One short paragraph shown under the title |
| `content` | No | The lesson text, in Markdown (see below) |
| `tasks` | No | Things to tick off |
| `roadmap` | No | Shows the course roadmap on this section's page, above its content (see below) |

Use `reference` for sections people read but don't do, such as a tool list or sources. Use `track` for work that runs alongside the levels, such as a weekly business track.

## The roadmap

Add `roadmap` to one section, usually the first, to show a picture of the whole course on its page:

```json
"roadmap": {
  "title": "Skills first, a path in Week 14, clients by Week 24",
  "note": "Full pace: 24 weeks at about 15 hours a week",
  "trackNote": "Saturdays from Week 3",
  "caption": "The levels run top to bottom. The business track runs beside them."
}
```

All four fields are optional. The app draws the roadmap from the course itself:

- Sections of kind `setup`, `level`, `gate` and `capstone` run top to bottom, in course order. A `gate` is drawn as a decision point.
- The first `track` section runs beside them as a band, over the steps its `weeks` cover. Each track task sits next to the step whose weeks contain the task's `week`.
- Each step opens its section when tapped and shows "Done" once all its tasks are ticked.

## Task fields

| Field | Required | What it is |
| --- | --- | --- |
| `id` | Yes | Unique in the **whole course**, such as `l0-p1` |
| `text` | Yes | A short name for the task |
| `kind` | No | `task` (default), `project` or `exit` (an exit test you must pass before moving on) |
| `detail` | No | Instructions, in Markdown |
| `week` | No | The course week it is due. In a `track` section, a task shows up in "This week" from the week after the previous task's week. |

## The rule that keeps progress safe

**Never change or reuse a task `id` once people have started the course.** Ticks are saved against the id.

- To reword a task, change its `text` and keep the `id`.
- To drop a task, delete it. Its old tick is kept but no longer counted.
- To add a task, give it a new `id`.
- Raise `version` with every update. A phone that already has the course takes the file with the higher version.

## Markdown you can use in `content`, `summary` and `detail`

- Paragraphs, separated by a blank line
- `**bold**`, `*italic*` and `` `code` ``
- Links: `[text](https://example.com)`. Only `https://`, `http://` and `mailto:` links work.
- Bullet lists with `- ` and numbered lists with `1. `. Indent by 4 spaces to nest.
- Tables with `|` columns and a `| --- |` line under the header
- Code blocks between lines of three backticks
- Quotes with `> `
- Headings with `#`, `##` or `###`

HTML tags are shown as plain text, never run. In JSON, write a new line as `\n` and a double quote as `\"`.

## Prompt for turning a document into a course file

Copy everything inside the box, then paste your course document after it.

```
Convert the course document below into a Vidhyarambham course file.
Reply with only the JSON, no explanation.

Rules:
- Top level: "format": "vidhyarambham-course", "formatVersion": 1,
  "id" (lowercase-with-hyphens, from the title), "version": 1, "title",
  "summary", "language", "updated" (today, YYYY-MM-DD), "totalWeeks",
  "paces" (only if the document describes paces), "sections".
- One section per main heading, in the same order. Choose "kind" from:
  intro, setup, level, gate, track, capstone, reference.
- If a heading names weeks, add "weeks": [start, end] and remove the
  weeks from the title.
- Projects, exercises, checklists and exit tests become "tasks", each with a
  short "text", a "kind" (task, project or exit) and the full instructions
  in "detail". Remove them from "content" so nothing appears twice.
- Everything else in the section goes in "content" as Markdown, word for
  word. Keep every link, table and list. Do not add or drop information.
- Task ids are short, unique in the whole course, and never reused,
  for example "l0-p1", "l0-exit", "w0-accounts".
- Use only these Markdown features: paragraphs, bold, italic, code, links,
  lists, tables, code blocks, quotes and headings. No HTML.

The document:
```

## Updating an existing course

Ask the AI to update the existing JSON file instead of making a new one, and add: "Keep every existing task id. Raise version by 1." Then check the result with `npm run check-courses`, or add it in the app, which tells you about any problem.
