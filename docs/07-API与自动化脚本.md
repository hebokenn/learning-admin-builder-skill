# 07-API 和自动化脚本：导入、提醒、周报怎么做

API 可以理解为页面和数据库之间的“办事窗口”。脚本可以理解为“自动帮你重复做事的小程序”。

## API 设计方法

先从页面动作拆 API：

| 页面 | 用户动作 | API 示例 |
|---|---|---|
| 登录页 | 登录、退出、获取当前用户 | `POST /api/auth/login`、`GET /api/auth/me` |
| 首页看板 | 查看指标和风险 | `GET /api/dashboard/summary` |
| 学员列表 | 查询、新增、编辑 | `GET /api/learners`、`POST /api/learners` |
| 学员详情 | 查看和更新进度 | `GET /api/learners/:id`、`PATCH /api/progress/:id` |
| 导入页 | 上传、预览、确认导入 | `POST /api/import/preview`、`POST /api/import/commit` |
| 跟进页 | 创建、完成跟进 | `POST /api/follow-ups`、`PATCH /api/follow-ups/:id` |
| 报表页 | 生成、导出报表 | `GET /api/reports/weekly`、`POST /api/reports/export` |

## 命名规则

- 查询列表用 `GET`。
- 新增用 `POST`。
- 修改用 `PATCH`。
- 删除用 `DELETE`。
- 批量操作单独写，例如 `POST /api/learners/bulk-update`。
- 不要写模糊名字，例如 `/api/data`、`/api/update`。

## 常见 API 清单

```text
POST /api/auth/login
POST /api/auth/logout
GET  /api/auth/me

GET  /api/dashboard/summary
GET  /api/dashboard/risk-learners

GET    /api/learners
POST   /api/learners
GET    /api/learners/:learnerId
PATCH  /api/learners/:learnerId

GET    /api/stages
POST   /api/stages
PATCH  /api/stages/:stageId

GET    /api/tasks
POST   /api/tasks
PATCH  /api/tasks/:taskId

GET   /api/progress
PATCH /api/progress/:progressId

POST /api/import/preview
POST /api/import/commit
GET  /api/import/jobs/:jobId

GET   /api/follow-ups
POST  /api/follow-ups
PATCH /api/follow-ups/:followUpId

GET  /api/reports/weekly
POST /api/reports/export

GET  /api/notifications
POST /api/notifications/send
```

可选：

```text
GET  /api/bookings
POST /api/bookings
GET  /api/scorings
POST /api/scorings
```

## API 必须写清楚的内容

每个 API 都要说明：

- 谁能访问。
- 需要哪些参数。
- 返回什么数据。
- 失败时怎么提示。
- 是否要记录操作日志。
- 是否涉及敏感信息。

示例：

```text
PATCH /api/learners/:learnerId
用途：修改学员信息
权限：admin、trainer
限制：trainer 只能修改自己负责的学员
请求：name、department、mentorId、status
错误：无权限、学员不存在、字段格式错误
日志：需要记录谁改了什么
```

## 导入脚本设计

导入流程：

```text
上传文件
  -> 解析文件
  -> 字段映射
  -> 数据预览
  -> 字段校验
  -> 冲突检查
  -> 用户确认
  -> 正式导入
  -> 写入日志
```

导入必须支持：

- 预览，不直接写入。
- 行级错误，例如第 18 行邮箱格式错误。
- 冲突处理，例如邮箱已存在。
- 导入日志。
- 失败原因。
- 必要时回滚。

## 自动化脚本

| 脚本 | 作用 |
|---|---|
| 部署脚本 | 拉代码、安装依赖、构建、重启服务 |
| 备份脚本 | 定时备份数据库和上传文件 |
| 每日提醒 | 找出逾期和即将截止的人，发送提醒 |
| 周报脚本 | 每周生成培训摘要 |
| 同步脚本 | 从第三方系统或导出文件同步数据 |
| 健康检查 | 检查网站、数据库、邮件、备份是否正常 |

## 小白怎么理解脚本

脚本就是把重复操作交给电脑：

```text
每天早上 8 点
  -> 检查哪些学员逾期
  -> 生成名单
  -> 发提醒
  -> 保存发送记录
```

如果一个操作满足下面任意两条，就值得写脚本：

- 经常重复。
- 容易出错。
- 数据量大。
- 有固定时间要求。
- 需要留下记录。
- 需要多人协作。

## 给 AI 的脚本提示词

```text
请帮我设计一个【用途】脚本。

背景：
这是培训进度跟进网站，不依赖任何私有项目。

输入：
- 文件类型：Excel / CSV / API / 数据库
- 字段示例：
  - name：学员姓名，必填
  - email：邮箱，唯一
  - stage：当前培训阶段
  - completedAt：完成时间，可为空

处理规则：
- 邮箱重复时：跳过 / 更新 / 报错
- 阶段不存在时：报错并记录行号
- 空姓名：不导入
- 日期格式错误：不导入该行

安全要求：
- 不要把密钥写死在代码里
- 正式写入前支持预览模式
- 支持 dry-run
- 出错时不要破坏已有数据

请输出：
1. 脚本设计说明
2. 伪代码
3. 需要的配置项
4. 测试用例
```
