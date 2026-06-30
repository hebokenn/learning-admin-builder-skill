# WorkBuddy / Kun 使用说明

这套方法可以给 WorkBuddy、Kun、Cursor、ChatGPT Agent、Codex 或其他 AI 工具使用。关键不是工具名字，而是让 AI 能读到同一套执行规程，并尽量替人完成读取、整理、实现、验证和部署前准备。

## 最推荐：通用 agent 启动方式

把这段放到目标项目的第一条消息：

```text
请先阅读这个方法论仓库的 AI_CONTEXT.md、AI_MANIFEST.yaml 和 docs/13-通用Agent执行指南.md。
目标是把当前学习/培训项目做成培训进度后台管理网站。
你先读取项目资料和样例数据，再问我最多 5 个关键问题。
不要先写代码。先输出第一版范围、页面、数据字段、权限、导入、API、脚本、验证和部署计划。
我确认后，能由你执行的步骤请你直接执行；只有业务确认、真实数据、账号授权、生产密钥和正式部署需要问我。
```

## 推荐方式 1：工具支持项目级 skill

如果工具支持类似 `.workbuddy/skills` 的项目级 skill，把整个 skill 目录复制进去：

```bash
mkdir -p .workbuddy/skills
cp -R /path/to/learning-admin-builder-skill/learning-admin-builder .workbuddy/skills/
```

然后在目标项目里这样开头：

```text
Use $learning-admin-builder to turn this learning project into a training progress admin site.
请先做需求澄清，再输出页面、数据、权限、导入、后台管理和部署方案。
```

保持目录完整：

```text
learning-admin-builder/
  SKILL.md
  agents/openai.yaml
  references/
```

`agents/openai.yaml` 是 Codex 界面信息。其他工具不认识它也没关系，可以忽略。

## 推荐方式 2：工具支持项目规则或知识库

如果 WorkBuddy、Kun 或其他工具支持“项目规则”“知识库”“上下文文件”，建议放这些文件：

```text
AGENTS.md
AI_CONTEXT.md
AI_MANIFEST.yaml
portable-prompt.md
docs/13-通用Agent执行指南.md
templates/AI执行任务单.md
learning-admin-builder/SKILL.md
learning-admin-builder/references/requirements-intake.md
learning-admin-builder/references/mycoach-patterns.md
learning-admin-builder/references/adaptation-playbook.md
learning-admin-builder/references/validation-checklist.md
```

然后告诉工具：

```text
请先阅读本项目知识库里的 AI_CONTEXT.md、AI_MANIFEST.yaml 和 docs/13-通用Agent执行指南.md。
目标是把这个学习项目做成培训进度后台管理网站。请先读取项目资料，少问问题，输出方案；我确认后再分阶段执行。
```

## 推荐方式 3：工具只支持一段提示词

如果工具不能加载文件夹，只支持一段自定义指令或首条消息，复制 [portable-prompt.md](./portable-prompt.md) 全文。

然后在下面追加项目描述：

```text
项目描述：
我有一个新员工培训项目，学员数据来自 Excel，每周要看完成率、逾期任务和经理周报。请用上面的规则帮我设计第一版后台管理网站。
```

## 给 Kun 这类工具的建议

如果 Kun 支持“项目说明 / 规则 / 文件上下文”，优先放：

1. `AI_CONTEXT.md`
2. `AI_MANIFEST.yaml`
3. `docs/13-通用Agent执行指南.md`
4. `templates/AI执行任务单.md`
5. `portable-prompt.md`
6. 目标项目自己的需求文档和脱敏样例数据

如果 Kun 能执行代码，让它在目标项目中遵守：

- 先读目标项目规则。
- 先看样例数据。
- 分阶段实现。
- 每阶段后运行本地检查。
- 不把私有数据提交到公开仓库。

## 兼容性提醒

- 不要假设所有工具都支持 `$learning-admin-builder` 语法。
- 不要假设所有工具都会自动读取 `SKILL.md`。
- 不要把这个仓库当成源码模板复制进业务项目；它是方法论和 skill。
- 如果目标项目有自己的记忆或交接文件，只更新目标项目指定的位置，不要另建第二套记忆。
- 公开分享时只放方法、模板、假数据和脱敏样例。
