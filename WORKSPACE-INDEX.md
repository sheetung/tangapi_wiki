# Workspace Index

## 根目录保留
- `AGENTS.md` `SOUL.md` `USER.md` `MEMORY.md`：助手记忆与行为文件
- `my-skills/`：你的自建 skills（唯一源码目录）
- `.openclaw/`：本项目内部状态

## 项目目录
- `projects/hugo_bolg_file/`：博客项目（兼容软链：`hugo_bolg_file -> projects/hugo_bolg_file`）

## 产物目录
- `data/genshin/codes.json`：原神兑换码抓取结果
- `dist/skills/*.skill`：打包产物
- `data/legacy/*.tar.gz`：历史重复目录压缩备份

## 兼容路径（软链接）
- `genshin_codes.json -> data/genshin/codes.json`
- `umami-stats.skill -> dist/skills/umami-stats.skill`
- `umami-stats -> my-skills/umami-stats`

## 约定
- 新增脚本输出优先写到 `data/`
- 打包产物统一放 `dist/`
- skill 源码统一放 `my-skills/`
