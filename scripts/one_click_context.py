#!/usr/bin/env python3
"""Build a compact copy-paste context bundle for generic AI agents."""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dist" / "learning-admin-builder-context.md"

FILES = [
    "AI_CONTEXT.md",
    "AI_MANIFEST.yaml",
    "docs/13-通用Agent执行指南.md",
    "templates/AI执行任务单.md",
]

STARTER = """# Learning Admin Builder 快速启动上下文包

把这份内容粘贴给 WorkBuddy、Kun、Cursor、ChatGPT Agent、Codex 或其他 AI 工具。

公开仓库：
https://github.com/hebokenn/learning-admin-builder-skill

## 任务启动语

请先读取这个公开方法论仓库：
https://github.com/hebokenn/learning-admin-builder-skill

如果你无法打开 GitHub 链接，请使用下面的上下文包内容。

你是一个通用 AI agent。请使用这个 Learning Admin Builder 方法论，帮我把学习、培训、入职、认证或课程进度项目做成可长期使用的后台管理网站。

工作方式：
- 先检查目标项目现有资料、样例数据、项目规则和运行命令。
- 不要一开始写代码。
- 每次最多问我 5 个关键问题，只问会影响范围、字段、权限、导入和部署的问题。
- 先输出第一版范围、页面清单、数据模型、权限矩阵、导入规则、API/脚本、验证和部署计划。
- 我确认后，你能执行的步骤直接执行：改代码、运行检查、浏览器验收、生成部署前清单、写交接记录。
- 只有业务范围、真实数据、账号授权、生产密钥、费用和正式部署需要问我。
- 不要暴露真实学员数据、.env、数据库、私有导出、账号密码或生产配置。
"""


def build_bundle() -> str:
    parts = [STARTER.rstrip(), ""]
    for rel in FILES:
        path = ROOT / rel
        content = path.read_text(encoding="utf-8").strip()
        parts.extend([f"## 文件：{rel}", "", content, ""])
    return "\n".join(parts).rstrip() + "\n"


def copy_to_clipboard(text: str) -> bool:
    pbcopy = shutil.which("pbcopy")
    if pbcopy:
        subprocess.run([pbcopy], input=text, text=True, check=True)
        return True
    return False


def main() -> None:
    parser = argparse.ArgumentParser(description="Build one-click AI context bundle.")
    parser.add_argument("--copy", action="store_true", help="Copy the bundle to clipboard on macOS.")
    args = parser.parse_args()

    text = build_bundle()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")

    copied = copy_to_clipboard(text) if args.copy else False
    print(f"Wrote {OUTPUT}")
    if args.copy:
        print("Copied to clipboard." if copied else "Clipboard copy unavailable; use the generated file.")


if __name__ == "__main__":
    main()
