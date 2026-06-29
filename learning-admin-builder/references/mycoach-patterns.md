# MyCoach-Style Patterns

Use these as generalized product patterns. Do not copy private source code, project data, credentials, exports, or production details from any existing MyCoach installation.

## Product Shape

Build a dense learning-operations admin system:

- Top-level navigation by daily workflow.
- Role-aware pages and actions.
- Compact metrics above operational tables.
- Fast filtering, searching, and sorting.
- Learner detail pages that combine progress, risk, notes, and follow-up actions.
- Data freshness indicators when imports or syncs drive the app.

Avoid marketing-page structure, oversized hero sections, decorative card layouts, and explanatory in-app text.

## Core Module Pattern

Common v1 modules:

- Authentication and role-based access.
- Data dashboard for aggregate health and risk.
- Import page for spreadsheet or platform data.
- Learning structure page for stages, tasks, or milestones.
- Task board for per-learner completion state.
- Learner status page for segmentation.
- Learner detail page for roadmap, timeline, follow-ups, and manual operations.
- Report page for weekly or monthly action review.
- Settings or admin page for users and configuration.

Optional modules:

- Practice booking.
- Coach or mentor availability.
- Rubric scoring.
- Learner reflections.
- In-app and email notifications.
- Trend analytics.

## UI Pattern

Use a restrained operational dashboard:

- Compact page header with title, short description, and actions.
- Metric cards for a small number of decision-driving numbers.
- Panels for tables, charts, and queues.
- Tables as the default for repeated operational work.
- Charts only when they support a decision.
- Stable widths for navigation, filters, date cells, action buttons, and status chips.
- Responsive behavior that preserves task completion and scanning on small screens.

Use clear labels from the target project domain. Do not leave MyCoach-specific labels in a different project unless the new project uses that name.

## Data And State Pattern

Use durable state for:

- learners
- stages, tasks, milestones
- task progress
- manual overrides
- follow-ups
- scoring
- bookings
- notification records
- import logs
- report send history

Use transient browser state only for UI filters, selected tabs, and modal visibility.

## Import Pattern

Design imports as a first-class workflow:

- Detect file type from explicit user-selected slot, stable file naming, or inspected headers.
- Preview changes before applying when risk is high.
- Normalize status values.
- Keep import logs.
- Record data freshness.
- Block or surface identity conflicts.
- Avoid silently overwriting manual learner records unless the behavior is agreed.

## Optional Practice And Scoring Pattern

Only add these if required:

- Coaches or mentors open slots or initiate sessions.
- Learners book available slots when allowed.
- Booking records hold learner, coach, date, time, meeting link, type, purpose, and status.
- Scoring records reference a booking or assessment.
- Rubrics define dimensions, weights, item labels, score type, and pass threshold.
- Learners can review feedback and optionally submit reflection or improvement plans.

Keep scoring math explicit and project-specific. Do not reuse another project's rubric weights by default.

## Reports And Notifications Pattern

Reports should produce actions, not just metrics:

- owner
- due date
- risk reason
- next action
- unresolved blockers
- recently closed items

Notifications should have clear trigger, recipient, channel, link target, and deduplication rule.
