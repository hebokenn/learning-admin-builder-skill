# Adaptation Playbook

Use this playbook after requirements intake and before implementation.

## 1. Classify The Build

Choose one path:

- New app from scratch: create a compact admin app using the user's preferred stack or the repo's established stack.
- Existing app adaptation: preserve framework, routing, styling, auth, database, and component patterns unless they block the goal.
- MyCoach-derived pattern: reuse the product architecture and workflow ideas, not private code or private data.

## 2. Define The V1 Module Set

Create a module list with one of these states:

- required
- optional in v1
- explicitly out of scope

Do this for dashboard, imports, learning structure, task board, learner detail, follow-ups, reports, notifications, booking, scoring, and analytics.

Every enabled module must have:

- page or view
- API or data access path
- required tables or data source
- role permissions
- acceptance criteria

## 3. Map Data Model

Start from the target domain, not from an old schema. Common entities:

- user
- learner
- role
- cohort or project
- stage or module
- task or milestone
- progress record
- manual override
- follow-up
- import log
- report run
- notification
- optional booking
- optional rubric and score

Define unique keys and relationships before coding. Use email only when the user confirms it is stable and allowed.

## 4. Design Imports

For each import file or API:

- inspect sample shape
- define source type
- define required fields
- define normalization rules
- define insert, update, delete, and conflict behavior
- define preview output
- define import log fields
- define rollback or recovery expectation if needed

If sample files are unavailable, implement manual entry or seed data only if the user agrees.

## 5. Design Navigation

Default admin navigation:

- Dashboard
- Structure
- Tasks or Progress
- Learners or Status
- Reports
- Import
- Admin or Settings

Default learner navigation:

- My Progress
- Optional Booking
- Optional Scores
- Settings

Remove pages that do not exist. Keep labels short and domain-specific.

## 6. Implement Safely

Before editing an existing repo:

- read project handoff docs and agent instructions
- inspect git status
- inspect package, framework, routing, and styling conventions
- for Next.js projects with local version-specific docs, read the relevant local docs before coding

Then implement in thin vertical slices:

- schema and seed/config
- data access and APIs
- page shell and navigation
- core dashboard or list view
- import or manual data entry
- detail workflows
- optional modules

Avoid broad refactors unless required.

## 7. Acceptance Criteria

At minimum, a new learning admin site should allow the intended operator to:

- log in with the right role
- view current learner status
- understand who needs action today
- inspect one learner's progress
- update or import progress
- record follow-up or next action
- see whether data is fresh

Add module-specific acceptance criteria for reports, notifications, booking, and scoring.
