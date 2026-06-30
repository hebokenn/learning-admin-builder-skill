# 快速启动

这份文件给用户快速启动任意 AI agent。目标是：不用读完整仓库，先把 GitHub 项目链接交给 agent，让 agent 自动读取方法论并开始下一步。

## 最简单做法

复制下面这段给你的 agent：

```text
请先读取这个公开方法论仓库：
https://github.com/hebokenn/learning-admin-builder-skill

你是一个通用 AI agent。请使用这个仓库的 Learning Admin Builder 方法论，帮我把学习、培训、入职、认证或课程进度项目做成可长期使用的后台管理网站。

请先读取：
1. AI_CONTEXT.md
2. AI_MANIFEST.yaml
3. docs/13-通用Agent执行指南.md
4. templates/AI执行任务单.md

工作方式：
- 先检查目标项目现有资料、样例数据、项目规则和运行命令。
- 不要一开始写代码。
- 每次最多问我 5 个关键问题，只问会影响范围、字段、权限、导入和部署的问题。
- 先输出第一版范围、页面清单、数据模型、权限矩阵、导入规则、API/脚本、验证和部署计划。
- 我确认后，你能执行的步骤直接执行：改代码、运行检查、浏览器验收、生成部署前清单、写交接记录。
- 只有业务范围、真实数据、账号授权、生产密钥、费用和正式部署需要问我。
- 不要暴露真实学员数据、.env、数据库、私有导出、账号密码或生产配置。
```

如果 agent 不能打开 GitHub 链接，再使用下面的方式生成可粘贴的上下文包。

## 生成可粘贴上下文包

在本仓库目录运行：

```bash
python3 scripts/one_click_context.py --copy
```

它会把精简后的 AI 上下文复制到剪贴板。然后直接粘贴到任意 AI 工具里。

如果不想复制到剪贴板，只想生成文件：

```bash
python3 scripts/one_click_context.py
```

生成文件在：

```text
dist/learning-admin-builder-context.md
```

## 人只需要做什么

- 提供业务目标。
- 提供脱敏样例数据。
- 确认第一版范围。
- 授权账号、费用、生产密钥和正式部署。

其他读取、整理、写代码、验证、部署前检查，都优先让 AI 做。
