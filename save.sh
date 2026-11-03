#!/bin/sh
# Build, check and save progress: generator to personal-finance-course-src,
# course JSON to add-personal-finance-course (never main until the end).
set -e
MSG="$1"
cd /home/claude/fin-src
python3 build.py
node check.mjs /home/claude/vidhyarambham/public/courses/personal-finance.json /home/claude/vidhyarambham | head -8
git add -A
git commit -q -m "$MSG

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_011VgQk6bf6HKHdHn9WC1HZs" || true
git push -q origin personal-finance-course-src
cd /home/claude/vidhyarambham
git checkout -q add-personal-finance-course 2>/dev/null || git checkout -q -b add-personal-finance-course
git add public/courses/personal-finance.json
git commit -q -m "$MSG

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_011VgQk6bf6HKHdHn9WC1HZs" || true
git push -q origin add-personal-finance-course
git log --oneline -1
