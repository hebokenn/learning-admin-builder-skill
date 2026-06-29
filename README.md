# 用 AI 制作培训进度跟进网站

这是一个公开的方法论仓库，目标是帮助不懂技术的人，用 AI 复制出类似“培训进度跟进后台”的网站。它适合新员工培训、3PP 培训、经销商培训、岗位认证、讲师培养、课程进度跟进等场景。

这个仓库不是 MyCoach 管理网站源码，也不包含任何私密数据、数据库、账号密码、部署配置或学员资料。它沉淀的是一套可迁移的方法：如何准备资料、让 AI 问需求、设计页面、设计数据表、生成代码、本地运行、部署上线、日常维护。

## 如果你是 AI，先读这里

这个仓库不只是给人看的教程，也给 AI 作为上下文使用。

AI 代理应按这个顺序加载：

1. [AI_CONTEXT.md](AI_CONTEXT.md)：压缩版执行规程，先读。
2. [AI_MANIFEST.yaml](AI_MANIFEST.yaml)：文件地图和场景路由，快速判断该读哪些文件。
3. [docs/12-AI如何使用这套方法论.md](docs/12-AI如何使用这套方法论.md)：更详细的 AI 使用说明。
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

## 推荐阅读顺序

1. [先读我：整体路线](docs/00-先读我.md)
2. [从业务到网站：核心方法论](docs/01-从业务到网站方法论.md)
3. [工具和安装：小白准备清单](docs/02-工具与安装.md)
4. [让 AI 问需求：不要一上来就写代码](docs/03-需求收集与AI提示词.md)
5. [页面和 UI 设计：后台管理页面怎么设计](docs/04-页面与UI设计.md)
6. [数据模型和字段映射：Excel 怎么变成网站数据](docs/05-数据模型与字段映射.md)
7. [前后端架构：代码应该怎么组织](docs/06-架构与代码组织.md)
8. [API 和自动化脚本：导入、提醒、周报怎么做](docs/07-API与自动化脚本.md)
9. [本地运行和验收：先在自己电脑上跑通](docs/08-本地运行与验证.md)
10. [部署上线和服务器：Vercel、Render、VPS 怎么选](docs/09-部署上线与服务器.md)
11. [后台管理和日常维护：上线后怎么管](docs/10-后台管理与日常维护.md)
12. [案例：新员工培训和 3PP 培训](docs/11-案例-新员工培训和3PP培训.md)
13. [AI 如何使用这套方法论](docs/12-AI如何使用这套方法论.md)

## 可直接复制的材料

- [AI 提示词合集](docs/examples/AI提示词合集.md)
- [页面草图样例](docs/examples/页面草图样例.md)
- [AI 快速上下文](AI_CONTEXT.md)
- [AI 文件地图](AI_MANIFEST.yaml)
- [需求收集表](templates/需求收集表.md)
- [页面确认清单](templates/页面确认清单.md)
- [数据字段清单](templates/数据字段清单.md)
- [权限矩阵](templates/权限矩阵.md)
- [API 与脚本清单](templates/API与脚本清单.md)
- [部署检查清单](templates/部署检查清单.md)
- [维护记录模板](templates/维护记录模板.md)

## 最重要的原则

不要一开始就让 AI 写代码。正确顺序是：

```text
讲清楚业务
  -> 确认角色和权限
  -> 确认页面
  -> 确认数据字段
  -> 确认 API 和脚本
  -> 生成代码
  -> 本地运行
  -> 验收
  -> 部署上线
  -> 日常维护
```

如果直接说“帮我做一个培训网站”，AI 很容易做成好看的演示页，而不是每天能用的后台管理系统。

## 给 Codex 安装 Skill

如果你使用 Codex，可以把本仓库里的 skill 复制到本机：

```bash
git clone https://github.com/hebokenn/learning-admin-builder-skill.git
mkdir -p ~/.codex/skills
cp -R learning-admin-builder-skill/learning-admin-builder ~/.codex/skills/
```

重启 Codex 后，在目标项目里输入：

```text
Use $learning-admin-builder to turn my learning project into a training progress admin site.
```

## 给 WorkBuddy、Kun 或其他 AI 工具使用

如果工具支持项目级 skill，可以复制整个目录：

```bash
mkdir -p .workbuddy/skills
cp -R /path/to/learning-admin-builder-skill/learning-admin-builder .workbuddy/skills/
```

如果工具不支持 `SKILL.md`，使用 [portable-prompt.md](portable-prompt.md)，把里面的内容放到项目规则、知识库、自定义指令或第一条消息里。

更多说明见 [WORKBUDDY_KUN_USAGE.md](WORKBUDDY_KUN_USAGE.md)。

## 官方工具链接

常用工具入口：

- [ChatGPT](https://chatgpt.com/)
- [OpenAI Codex 文档](https://developers.openai.com/codex/cloud)
- [Cursor](https://cursor.com/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Git](https://git-scm.com/doc)
- [GitHub Docs](https://docs.github.com/en)
- [Node.js 下载](https://nodejs.org/en/download)
- [Next.js 文档](https://nextjs.org/docs)
- [Vercel 文档](https://vercel.com/docs)
- [Render 文档](https://render.com/docs)
- [PostgreSQL 文档](https://www.postgresql.org/docs/)
- [Supabase 文档](https://supabase.com/docs)
- [Neon 文档](https://neon.com/docs)
- [PM2 文档](https://pm2.keymetrics.io/docs/usage/quick-start/)
- [Nginx 文档](https://nginx.org/en/docs/)
- [Certbot](https://certbot.eff.org/)

## 安全提醒

- 不要把 `.env`、数据库文件、学员名单、成绩表、真实邮件地址、手机号、服务器密码上传到公开 GitHub 仓库。
- 教程和模板只能放假数据、字段样例和方法论。
- 真正上线前必须检查登录、权限、备份、导入回滚、删除操作和数据导出。
