---
name: learning-admin-builder
description: Build or adapt dense learning-project admin websites inspired by MyCoach-style operations dashboards. Use when a user wants to turn a training, course, onboarding, certification, coaching, or learning-progress project into a managed web app with roles, learner records, stages, tasks, Excel or platform imports, progress dashboards, risk tracking, follow-ups, reports, notifications, and optional practice booking or scoring workflows.
---

# Learning Admin Builder

## Overview

Use this skill to create or adapt operational admin websites for learning projects. The skill does not provide a one-click clone of any existing system; it gives a repeatable discovery, design, implementation, and validation workflow.

Default to a dense, restrained admin-dashboard product: fast scanning, compact tables, stable filters, role-specific navigation, clear operational queues, and practical reports. Do not create a marketing landing page unless the user explicitly asks for one.

## Workflow

1. Inspect the target repository or project brief before asking questions when local files are available.
2. Read `references/requirements-intake.md` and run the intake before implementing. If the user only wants a plan, stop after a decision-complete plan.
3. Read `references/mycoach-patterns.md` when choosing module architecture, UI density, navigation, and optional workflow patterns.
4. Read `references/adaptation-playbook.md` before mapping data sources, database schema, imports, pages, APIs, or optional modules.
5. Read `references/validation-checklist.md` before final verification and public handoff.

## Intake Rules

Always identify these items before writing code:

- Project goal and audience.
- Roles and permission boundaries.
- Learner identity fields and any privacy constraints.
- Learning structure: stages, tasks, milestones, deadlines, or freeform progress.
- Data source: Excel exports, platform API, manual entry, database, or mixed source.
- Required modules: dashboard, import, course structure, task board, learner detail, follow-ups, reports, notifications, practice booking, scoring, analytics.
- Deployment target and operational owner.

Ask only for decisions that cannot be discovered from the repo, files, or sample data. When sample Excel or CSV files exist, inspect their sheets and headers before proposing import logic.

## Implementation Defaults

- Prefer building a working admin tool over a broad framework abstraction.
- Keep optional modules removable. Practice booking, scoring, notifications, and weekly reports must not be assumed for every project.
- Treat import parsing as project-specific. Never hard-code another project's file names, stages, columns, scoring rules, or organization vocabulary unless the user confirms they apply.
- Use durable database state for operational records such as follow-ups, scoring, reports, notifications, and manual overrides.
- Keep user-facing labels aligned to the new project domain while preserving the operational layout pattern.
- Preserve existing project conventions, framework, and design system when adapting an existing codebase.

## Output Expectations

For planning work, produce a decision-complete implementation plan with module choices, data model, import mapping, pages, APIs, validations, and assumptions.

For implementation work, deliver the code changes, run relevant checks, and summarize:

- what changed
- files touched at a high level
- validation run
- remaining setup or data assumptions

Never include secrets, real learner data, private exports, database files, or production deployment credentials in public artifacts.
