# Vidhyarambham

A course library and progress tracker that installs on your phone and works offline.

**Open the app:** https://naipunyam.github.io/vidhyarambham/

## What it does

- Lists your courses with how far you've come in each
- Shows every course section, with lessons, links and tasks to tick off
- Works out which week you're in from your start date and pace, and shows that week's tasks
- Saves a note against any task, such as a link to your finished project
- Adds new courses from a file or a link, without changing any code
- Saves and restores a backup of all your progress

Progress is stored in the browser on your phone, not on a server. Save a backup from **Backup and courses** now and then, because clearing Chrome's data erases it.

## Install it on Android

1. Open the link above in Chrome.
2. Tap the menu, then **Install app** or **Add to Home screen**.

## Add a new course

See [COURSE_FORMAT.md](COURSE_FORMAT.md). In short: put the course file in `public/courses/`, add its name to `public/courses/index.json`, and commit. GitHub checks the file, builds the app and publishes it.

## How it's built

- React and Vite, with `vite-plugin-pwa` for offline use and installing
- No server and no accounts: course files are plain JSON in `public/courses/`
- Every push to `main` runs the course check and the tests, then deploys to GitHub Pages (`.github/workflows/deploy.yml`)

| Folder | What's in it |
| --- | --- |
| `public/courses/` | Course files and `index.json`, the list of courses |
| `src/lib/` | Course format checks, progress maths, saving, backup, Markdown |
| `src/components/` | The screens |
| `tests/` | Tests for everything in `src/lib/` |

### Work on it locally

You need Node.js 22 or later.

```
npm install
npm test
npm run dev
```

`npm run check-courses` checks every course file. `npm run build` makes the site in `dist/`.

If the repository is ever renamed, change `base` in `vite.config.js` and the two icon paths in `index.html` to the new name.
