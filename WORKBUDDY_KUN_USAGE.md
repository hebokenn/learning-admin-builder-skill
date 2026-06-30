# WorkBuddy / Kun 使用说明

这套方法可以给 WorkBuddy、Kun、Cursor、ChatGPT Agent、Codex 或其他 AI 工具使用。关键不是工具名字，而是让 AI 能读到同一套执行规程，并尽量替人完成读取、整理、实现、验证和部署前准备。

## 最推荐：快速启动

复制公开仓库链接给 agent：

```text
请先读取这个公开方法论仓库：
https://github.com/hebokenn/learning-admin-builder-skill
```

如果 agent 不能打开 GitHub 链接，再使用 [ONE_CLICK.md](ONE_CLICK.md)。需要生成可粘贴上下文包时，在本仓库目录执行：

```bash
python3 scripts/one_click_context.py --copy
```

然后把剪贴板内容粘贴到 WorkBuddy、Kun、Cursor、ChatGPT Agent 或其他工具。

## 工具支持项目级 skill

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

## 工具支持项目规则或知识库

如果 WorkBuddy、Kun 或其他工具支持“项目规则”“知识库”“上下文文件”，最少放这些文件：

```text
AI_CONTEXT.md
AI_MANIFEST.yaml
docs/13-通用Agent执行指南.md
templates/AI执行任务单.md
```

需要更完整时再补：

```text
portable-prompt.md
learning-admin-builder/SKILL.md
learning-admin-builder/references/
```

## 工具只支持一段提示词

如果工具不能加载文件夹，只支持一段自定义指令或首条消息，优先复制 [ONE_CLICK.md](ONE_CLICK.md) 的启动语；需要更完整时复制 [portable-prompt.md](./portable-prompt.md) 全文。

```text
项目描述：
我有一个新员工培训项目，学员数据来自 Excel，每周要看完成率、逾期任务和经理周报。请用上面的规则帮我设计第一版后台管理网站。
```

## 给 Kun 这类工具的建议

如果 Kun 支持“项目说明 / 规则 / 文件上下文”，优先放：

1. `ONE_CLICK.md`
2. `AI_CONTEXT.md`
3. `AI_MANIFEST.yaml`
4. `docs/13-通用Agent执行指南.md`
5. 目标项目自己的需求文档和脱敏样例数据

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
