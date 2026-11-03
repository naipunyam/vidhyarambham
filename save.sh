#!/bin/sh
# Build, check and save progress: generator to learning-course-src,
# course JSON to add-learning-course (never main until the end).
set -e
MSG="$1"
cd /home/claude/lrn-src
python3 build.py
node check.mjs /home/claude/vidhyarambham/public/courses/learning-capabilities.json /home/claude/vidhyarambham | head -8
git add -A
git commit -q -m "$MSG

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_011VgQk6bf6HKHdHn9WC1HZs" || true
git push -q origin learning-course-src
cd /home/claude/vidhyarambham
git checkout -q add-learning-course 2>/dev/null || git checkout -q -b add-learning-course
git add public/courses/learning-capabilities.json
git commit -q -m "$MSG

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_011VgQk6bf6HKHdHn9WC1HZs" || true
git push -q origin add-learning-course
git log --oneline -1
