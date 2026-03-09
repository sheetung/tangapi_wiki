# Workspace Index

## 根目录放什么
- `AGENTS.md` `SOUL.md` `USER.md` `MEMORY.md`：助手记忆与行为文件
- `my-skills/`：你的自建 skills（唯一源码目录）
- `hugo_bolg_file/`：博客项目
- `.openclaw/`：本项目内部状态

## 产物目录（已整理）
- `data/genshin/codes.json`：原神兑换码抓取结果
- `dist/skills/*.skill`：打包出来的 skill 文件
- `data/legacy/`：历史/重复目录备份

## 兼容路径（软链接）
- `genshin_codes.json -> data/genshin/codes.json`
- `umami-stats.skill -> dist/skills/umami-stats.skill`
- `umami-stats -> my-skills/umami-stats`

## 约定
- 新增脚本输出优先写到 `data/`。
- 打包产物统一放 `dist/`。
- skill 源码统一放 `my-skills/`。
