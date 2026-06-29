# Validation Checklist

Run this checklist before final handoff.

## Skill Or Public Artifact Safety

For public skill repositories:

- No `.env` files.
- No database files.
- No private exports or uploaded spreadsheets.
- No real learner names, emails, phone numbers, meeting links, or company-only records.
- No production server addresses, SSH remotes, tokens, SMTP credentials, cookies, or API keys.
- No copied private application source unless the user explicitly wants to publish that code.
- No generated build artifacts or dependency folders.

Use repository scans such as `find`, `git status`, and targeted text search for secret-like strings before pushing.

## App Validation

Use the target repo's own commands. Typical checks:

- format or diff check when available
- lint
- typecheck
- build
- unit or integration tests when available

For web apps, run a local server and inspect key pages in a real browser when feasible.

## Browser QA

Check representative pages:

- dashboard
- import or data entry
- learning structure
- task or progress board
- learner detail
- reports
- optional booking/scoring pages
- settings or admin

Check viewport widths:

- 1280
- 1100
- 900
- 760
- 560

Look for:

- horizontal overflow
- clipped buttons
- overlapping text
- unstable table or card layouts
- unreadable charts
- modals that do not fit
- broken role-based redirects

## Data QA

Validate with representative data:

- empty state
- one learner
- many learners
- completed learner
- overdue learner
- learner with manual override
- import conflict
- unknown status value
- optional booking or scoring records when enabled

## Handoff

If the target repo has a handoff file or agent instructions, update it after substantive work. Record:

- what changed
- files touched
- why the approach was chosen
- validation run
- known follow-ups

Do not create a second persistent memory location when the target repo already defines one.
