# Requirements Intake

Use this intake before planning or implementing a learning-project admin site. Inspect local files, existing code, sample spreadsheets, and documentation first. Ask the user only for choices that cannot be discovered.

## 1. Product Goal

Capture:

- Project name and short domain description.
- Primary outcome: monitor progress, operate training delivery, certify learners, schedule coaching, report to managers, or another goal.
- Daily users: admins, trainers, mentors, learners, managers, external partners.
- Success criteria for v1.

Default: build the actual admin tool first, not a landing page.

## 2. Roles And Access

Define role boundaries:

- Admin: system setup, imports, users, reports, all learners.
- Trainer or mentor: assigned learners, follow-ups, scoring, coaching sessions.
- Learner: own progress, own tasks, optional bookings, own scoring feedback.
- Manager: read-only summary and reports if needed.

Record which pages and API actions each role can access. Avoid adding roles that do not map to real workflows.

## 3. Learning Structure

Identify whether the project is:

- Stage/task based: phases, modules, lessons, checklists.
- Milestone based: key deliverables and due dates.
- Cohort based: fixed calendar schedule.
- Freeform: manual progress notes and status.

For stage/task projects, collect stage name, type, duration, order, task names, task type, expected day or date, and pass/fail meaning.

## 4. Data Sources

Classify every data source:

- Excel or CSV export.
- Platform API.
- Manual admin entry.
- Existing database.
- Mixed source.

For spreadsheet imports, inspect sheets and headers before designing code. Capture:

- File purpose.
- Sheet names.
- Header row.
- Required columns.
- Unique learner key.
- Date formats.
- Status values and their normalized meaning.
- Whether imports replace, merge, or append data.

Do not reuse another project's file names or column names unless the user confirms the same platform/export format.

## 5. Operational Modules

Select only the modules the project needs:

- Dashboard: summary metrics, risk segments, action queue.
- Import: preview, validation, import logs, data freshness.
- Course structure: stages and tasks.
- Task board: learner-by-task status and manual override.
- Learner detail: roadmap, calendar, follow-ups, notes.
- Follow-ups: owners, due dates, open/closed status.
- Reports: weekly or monthly operational readout.
- Notifications: in-app, email, or both.
- Practice booking: slots, bookings, meeting links.
- Scoring: rubrics, scoring items, pass/fail, learner reflection.
- Trends: score or progress analytics over time.

If optional modules are omitted, remove their navigation, schema, APIs, and notification flows.

## 6. Risk Rules

Define risk rules in plain language before implementation:

- overdue tasks
- due today
- inactivity
- deadline approaching
- failed assessment
- missing score
- manual high-risk flag

For each rule, define threshold, source fields, display label, and severity.

## 7. Reporting And Notifications

Decide:

- Report cadence and audience.
- Whether reports are generated in-app, exported, emailed, or all three.
- Notification triggers and target roles.
- Whether links must use public URLs.
- Whether test-recipient mode is required.

## 8. Deployment And Operations

Capture:

- Hosting target.
- Database choice.
- Environment variable needs.
- Backup expectations.
- Admin bootstrap process.
- Handoff memory rules in the target repo.

Before finalizing, restate assumptions and get user confirmation when any assumption could change schema, imports, permissions, or workflow.
