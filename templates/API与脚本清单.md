# API 与脚本清单

用这张表把页面动作、API、后台脚本和验收条件串起来。

## API 清单

| 页面 | 用户动作 | API | 方法 | 允许角色 | 输入 | 输出 | 错误处理 | 是否记录日志 |
|---|---|---|---|---|---|---|---|---|
| 登录 | 登录 | `/api/auth/login` | POST | 所有人 | 邮箱、密码 | 当前用户 | 账号禁用、密码错误 | 是 |
| 首页 | 查看指标 | `/api/dashboard/summary` | GET | admin、trainer、manager | 项目、批次 | 指标、风险、待办 | 无权限 | 否 |
| 学员列表 | 查询学员 | `/api/learners` | GET | admin、trainer、manager | 搜索、筛选、分页 | 学员列表 | 无权限 | 否 |
| 学员详情 | 更新基础信息 | `/api/learners/:id` | PATCH | admin、trainer | 字段变更 | 更新后学员 | 无权限、字段错误 | 是 |
| 任务进度 | 更新进度 | `/api/progress/:id` | PATCH | admin、trainer | 状态、备注 | 更新后进度 | 无权限、状态非法 | 是 |
| 导入 | 预览导入 | `/api/import/preview` | POST | admin、training_admin | 文件、数据类型 | 预览、错误行 | 文件错误、字段缺失 | 是 |
| 导入 | 确认导入 | `/api/import/commit` | POST | admin、training_admin | importJobId | 导入结果 | 冲突、过期预览 | 是 |
| 跟进 | 新建跟进 | `/api/follow-ups` | POST | admin、trainer | 学员、负责人、截止 | 跟进事项 | 无权限、字段错误 | 是 |
| 报表 | 导出报表 | `/api/reports/export` | POST | admin、manager | 周期、范围 | 下载链接 | 无权限、无数据 | 是 |

## 脚本清单

| 脚本 | 触发方式 | 输入 | 输出 | 失败处理 | 日志 |
|---|---|---|---|---|---|
| `seed-demo-data` | 手动 | 假数据配置 | 演示数据 | 可重复执行或先清理 | 控制台 |
| `send-due-reminders` | 定时 / 手动 | 今日到期和逾期规则 | 通知记录 | 失败重试，记录失败原因 | notifications |
| `generate-weekly-report` | 每周 / 手动 | 周期、项目范围 | 周报记录或导出文件 | 无数据时生成空报告 | reports |
| `backup-database` | 每日定时 | 数据库连接 | 备份文件 | 失败报警 | backup_logs |
| `health-check` | 定时 / 手动 | 网站、数据库、邮件配置 | 健康状态 | 失败报警 | health_logs |

## 每个 API 必须说明

- 谁能访问。
- 参数从哪里来。
- 返回给页面什么。
- 错误文案是什么。
- 是否涉及敏感数据。
- 是否需要操作日志。
- 是否影响导入、报表或通知。

## 验收

- [ ] 页面动作都有对应 API。
- [ ] API 命名清楚，不使用 `/api/data` 这类模糊名字。
- [ ] API 权限和权限矩阵一致。
- [ ] 导入 API 支持预览和确认两步。
- [ ] 自动脚本有输入、输出、失败处理和日志。
- [ ] 密钥来自环境变量，不写死在代码里。
