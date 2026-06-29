# WorkBuddy And Kun Usage

This skill is portable. The best integration depends on whether the target tool can load a `SKILL.md` folder.

## Option 1: Project Skill Directory

Use this when the tool supports project-level skills.

For WorkBuddy-style projects:

```bash
mkdir -p .workbuddy/skills
cp -R /path/to/learning-admin-builder-skill/learning-admin-builder .workbuddy/skills/
```

Then start the task with:

```text
Use $learning-admin-builder to turn this learning project into a MyCoach-style admin site.
```

Keep the whole folder intact:

```text
learning-admin-builder/
  SKILL.md
  agents/openai.yaml
  references/
```

`agents/openai.yaml` is Codex UI metadata. Tools that do not use it can ignore it safely.

## Option 2: Project Rules Or Knowledge Base

Use this when the tool supports custom rules but not skill folders.

Add these files to the tool's project knowledge:

```text
learning-admin-builder/SKILL.md
learning-admin-builder/references/requirements-intake.md
learning-admin-builder/references/mycoach-patterns.md
learning-admin-builder/references/adaptation-playbook.md
learning-admin-builder/references/validation-checklist.md
```

Tell the tool:

```text
Use the Learning Admin Builder instructions from project knowledge before planning or implementing this learning admin site.
```

## Option 3: Portable Prompt

Use this when the tool only accepts a single prompt or custom instruction block.

Copy the full contents of [portable-prompt.md](./portable-prompt.md) into the tool's custom instructions, project prompt, or first message.

Then add the project-specific task below it, for example:

```text
Project brief:
I have a sales onboarding program with learners, weekly modules, Excel progress exports, and manager reports. Build a MyCoach-style admin site.
```

## Compatibility Notes

- Always inspect the target project or sample files before asking the user for details.
- Do not assume the project needs booking, scoring, notifications, or weekly reports.
- Do not copy private MyCoach code, databases, credentials, or learner data into another tool.
- Keep the dashboard dense, operational, and focused on repeated admin work.
- If the target project has a handoff or memory rule, update that project's required memory file after substantive work.
