#!/bin/sh
# Build, check and save progress: generator to re-course-src,
# course JSON to add-re-course (never main until the end).
set -e
MSG="$1"
cd /home/claude/re-src
python3 build.py
node check.mjs /home/claude/vidhyarambham/public/courses/kerala-real-estate.json /home/claude/vidhyarambham | grep -v "^hours by week\|^open tasks" | head -12
git add -A
git commit -q -m "$MSG

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_011VgQk6bf6HKHdHn9WC1HZs" || true
git push -q origin re-course-src
cd /home/claude/vidhyarambham
git checkout -q add-re-course 2>/dev/null || git checkout -q -b add-re-course
git add public/courses/kerala-real-estate.json
git commit -q -m "$MSG

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_011VgQk6bf6HKHdHn9WC1HZs" || true
git push -q origin add-re-course
git log --oneline -1
