# Learning Admin Builder Skill

Reusable Codex skill for turning learning, training, onboarding, certification, or coaching projects into dense admin-dashboard web apps inspired by MyCoach-style learning operations.

This repository contains only the skill instructions and generalized reference material. It does not include private MyCoach application source code, databases, exports, credentials, or learner data.

## Install For Codex

Clone the repository:

```bash
git clone https://github.com/hebokenn/learning-admin-builder-skill.git
```

Copy the skill folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R learning-admin-builder-skill/learning-admin-builder ~/.codex/skills/
```

Restart Codex so the new skill is discovered.

## Install For WorkBuddy Or Project-Level Skill Loaders

If the tool supports project-level skills with a `SKILL.md` entry point, copy the skill folder into that tool's project skill directory. For WorkBuddy-style project skills:

```bash
mkdir -p .workbuddy/skills
cp -R /path/to/learning-admin-builder-skill/learning-admin-builder .workbuddy/skills/
```

Then invoke the skill by name in the target project:

```text
Use $learning-admin-builder to turn this learning project into a MyCoach-style admin site.
```

See [WORKBUDDY_KUN_USAGE.md](./WORKBUDDY_KUN_USAGE.md) for details.

## Use With Kun Or Prompt-Only Tools

If the tool does not load `SKILL.md` folders directly, use [portable-prompt.md](./portable-prompt.md). Put it in the tool's project rules, knowledge base, custom instruction area, or paste it at the start of the task.

## Use

Start a Codex thread in the project you want to adapt, then ask:

```text
Use $learning-admin-builder to turn my learning project into a MyCoach-style admin site.
```

The skill will guide Codex through:

- demand discovery
- role and permission design
- data source and import mapping
- module selection
- dashboard and operational workflow design
- optional booking, scoring, reports, and notifications
- validation and handoff

## Recommended Inputs

Prepare any of these if available:

- project brief
- sample Excel or CSV exports
- existing course or task structure
- learner status examples
- desired roles and permissions
- reporting requirements
- deployment constraints

The skill is designed to inspect real files before asking for missing decisions.

## Validate The Skill

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py ./learning-admin-builder
```

If your Codex install stores system skills elsewhere, use the matching `quick_validate.py` path.
