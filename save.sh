#!/bin/sh
# Build, check and save progress: generator to social-media-course-src,
# course JSON to add-social-media-course (never main until the end).
set -e
MSG="$1"
cd /home/claude/smm-src
python3 build.py
node check.mjs /home/claude/vidhyarambham/public/courses/social-media-marketing.json /home/claude/vidhyarambham | head -5
git add -A
git commit -q -m "$MSG

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_011VgQk6bf6HKHdHn9WC1HZs" || true
git push -q origin social-media-course-src
cd /home/claude/vidhyarambham
git checkout -q add-social-media-course 2>/dev/null || git checkout -q -b add-social-media-course
git add public/courses/social-media-marketing.json
git commit -q -m "$MSG

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_011VgQk6bf6HKHdHn9WC1HZs" || true
git push -q origin add-social-media-course
git log --oneline -1
