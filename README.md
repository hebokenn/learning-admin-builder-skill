# 用 AI 制作培训进度跟进网站

这是一个公开的方法论仓库，目标是帮助不懂技术的人，用 AI 复制出类似“培训进度跟进后台”的网站。它适合新员工培训、3PP 培训、经销商培训、岗位认证、讲师培养、课程进度跟进等场景。

这个仓库不是 MyCoach 管理网站源码，也不包含任何私密数据、数据库、账号密码、部署配置或学员资料。它沉淀的是一套可迁移的方法：如何准备资料、让 AI 问需求、设计页面、设计数据表、生成代码、本地运行、部署上线、日常维护。

## 最省事的用法

人只需要做三件事：

1. 打开 [ONE_CLICK.md](ONE_CLICK.md)，把“一键补水”提示词交给你正在使用的 AI 工具。
2. 提供培训项目的基本资料，真实数据要先脱敏。
3. 在 AI 给出第一版范围、页面、字段、权限和部署方案后确认。

其余能让 AI 做的事情，都交给 AI：读取项目、整理需求、分析表格字段、设计页面和数据表、生成代码、运行检查、整理部署步骤、更新交接记录。

如果同事会打开终端，也可以在本仓库目录运行：

```bash
python3 scripts/one_click_context.py --copy
```

这会把精简后的 AI 上下文复制到剪贴板，直接粘贴给任意 agent。

## 如果你是 AI，先读这里

这个仓库不只是给人看的教程，也给 AI 作为上下文使用。Codex、WorkBuddy、Kun、Cursor、ChatGPT Agent 或其他能读文件/改代码的 agent 都可以按同一套流程工作。

AI 代理应按这个顺序加载：

1. [AI_CONTEXT.md](AI_CONTEXT.md)：压缩版执行规程，先读。
2. [AI_MANIFEST.yaml](AI_MANIFEST.yaml)：文件地图和场景路由，快速判断该读哪些文件。
3. [docs/13-通用Agent执行指南.md](docs/13-通用Agent执行指南.md)：通用 agent 执行说明。
4. 需要实际执行时，再按场景读取 `docs/`、`templates/` 和 `learning-admin-builder/references/`。

如果目标工具支持 `AGENTS.md`，它会自动提示 AI 从 [AI_CONTEXT.md](AI_CONTEXT.md) 开始。

## 你最终会做出什么

按教程完成后，你会得到一个培训项目后台管理网站，通常包含：

- 首页统计看板
- 学员列表和学员详情
- 课程、阶段、任务管理
- 培训进度跟进
- Excel / CSV 导入
- 风险和待办提醒
- 周报、报表、导出
- 管理员后台设置
- 可选：预约、评分、证书、通知、自动化脚本

## 不用全部读完

主路径不是让人按顺序读完整文档，而是让 AI 按场景读取。人只需要先看：

1. [ONE_CLICK.md](ONE_CLICK.md)
2. [先读我：整体路线](docs/00-先读我.md)
3. [通用 Agent 执行指南](docs/13-通用Agent执行指南.md)

其余文档给 AI 按场景调用：

| 场景 | 让 AI 读取 |
|---|---|
| 需求不清 | [需求收集](docs/03-需求收集与AI提示词.md)、[需求收集表](templates/需求收集表.md) |
| 设计页面 | [页面和 UI 设计](docs/04-页面与UI设计.md)、[页面确认清单](templates/页面确认清单.md) |
| 分析表格和字段 | [数据模型和字段映射](docs/05-数据模型与字段映射.md)、[表格字段分析报告](templates/表格字段分析报告.md) |
| 写代码架构 | [架构与代码组织](docs/06-架构与代码组织.md)、[AI 执行前项目审查清单](templates/AI执行前项目审查清单.md) |
| 设计 API 和脚本 | [API 和自动化脚本](docs/07-API与自动化脚本.md)、[API 规格模板](templates/API规格模板.md)、[自动化脚本运行手册](templates/自动化脚本运行手册.md) |
| 本地验收 | [本地运行和验证](docs/08-本地运行与验证.md)、[本地验证报告](templates/本地验证报告.md) |
| 部署上线 | [部署上线和服务器](docs/09-部署上线与服务器.md)、[部署前 Go/No-Go 检查表](templates/部署前Go-No-Go检查表.md) |
| 后台维护 | [后台管理和日常维护](docs/10-后台管理与日常维护.md)、[维护记录模板](templates/维护记录模板.md) |

## 可直接复制的材料

- [一键补水](ONE_CLICK.md)
- [AI 提示词合集](docs/examples/AI提示词合集.md)
- [页面草图样例](docs/examples/页面草图样例.md)
- [AI 快速上下文](AI_CONTEXT.md)
- [AI 文件地图](AI_MANIFEST.yaml)
- [通用 Agent 执行任务单](templates/AI执行任务单.md)
- [AI 执行前项目审查清单](templates/AI执行前项目审查清单.md)
- [表格字段分析报告](templates/表格字段分析报告.md)
- [API 规格模板](templates/API规格模板.md)
- [自动化脚本运行手册](templates/自动化脚本运行手册.md)
- [本地验证报告](templates/本地验证报告.md)
- [部署前 Go/No-Go 检查表](templates/部署前Go-No-Go检查表.md)
- [需求收集表](templates/需求收集表.md)
- [页面确认清单](templates/页面确认清单.md)
- [数据字段清单](templates/数据字段清单.md)
- [权限矩阵](templates/权限矩阵.md)
- [API 与脚本清单](templates/API与脚本清单.md)
- [部署检查清单](templates/部署检查清单.md)
- [维护记录模板](templates/维护记录模板.md)

## 给不同 AI 工具使用

优先使用 [ONE_CLICK.md](ONE_CLICK.md)。需要长期放进项目规则时，再把 [AI_CONTEXT.md](AI_CONTEXT.md)、[AI_MANIFEST.yaml](AI_MANIFEST.yaml)、[portable-prompt.md](portable-prompt.md) 放进工具的项目规则、知识库或自定义指令。

如果你使用 Codex，可以额外把本仓库里的 skill 复制到本机：

```bash
git clone https://github.com/hebokenn/learning-admin-builder-skill.git
mkdir -p ~/.codex/skills
cp -R learning-admin-builder-skill/learning-admin-builder ~/.codex/skills/
```

重启 Codex 后，在目标项目里输入：

```text
Use $learning-admin-builder to turn my learning project into a training progress admin site.
```

如果你使用 WorkBuddy、Kun 或其他 AI 工具，参考 [WORKBUDDY_KUN_USAGE.md](WORKBUDDY_KUN_USAGE.md) 和 [docs/13-通用Agent执行指南.md](docs/13-通用Agent执行指南.md)。

如果工具支持项目级 skill，也可以复制整个目录：

```bash
mkdir -p .workbuddy/skills
cp -R /path/to/learning-admin-builder-skill/learning-admin-builder .workbuddy/skills/
```

## 工具链接

工具和安装说明统一放在 [docs/02-工具与安装.md](docs/02-工具与安装.md)，README 不重复维护链接清单。

## 安全提醒

- 不要把 `.env`、数据库文件、学员名单、成绩表、真实邮件地址、手机号、服务器密码上传到公开 GitHub 仓库。
- 教程和模板只能放假数据、字段样例和方法论。
- 真正上线前必须检查登录、权限、备份、导入回滚、删除操作和数据导出。
