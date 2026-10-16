# Arknights Codex Pets

[English](README.md) | **简体中文**

持续扩充的《明日方舟》同人动画桌宠合集，供 ChatGPT 和 Codex 使用。每个角色使用稳定的英文 ID，配有可导入图集、动画预览和角色资料。

**[浏览角色目录](CATALOG.zh-CN.md)**，选择角色并下载对应文件。目录由 [pets.json](pets.json) 生成，新增角色时无需重写本导入指南。

## 选择导入方式

| 使用环境 | 方法 | 文件或角色包 |
| --- | --- | --- |
| 可调用 Pets 插件的 ChatGPT Work / Codex 聊天 | 上传完整图集，让助手校验、创建并选用 | `<character-id>.png` |
| 读取本地自定义宠物的桌面客户端 / Codex CLI | 安装本地兼容包 | `codex/<character-id>/` |
| 提供 Upload pet 设置的 ChatGPT 网页端 | 上传 v1 兼容图集 | `codex/<character-id>/spritesheet.webp` |

从角色目录中选择文件；Pets 的入口与可用性取决于账号、工作区和客户端版本。

## 通过 Pets 插件导入

1. 打开[角色目录](CATALOG.zh-CN.md)，下载对应的**完整 PNG**，保留原始尺寸和透明度。
2. 将文件上传至能够调用 **Pets** 插件的聊天。Codex 本地任务也可以读取已授权访问的仓库文件。
3. 将以下提示词中的 `CHARACTER_NAME` 替换为角色名称：

```text
请使用 Pets 插件，把我提供的完整透明动画图集导入为名为 CHARACTER_NAME 的宠物。
先校验图集，校验通过后创建并选用。使用现有图集，无需重新绘制。
```

角色目录中的资料链接可提供名称、描述和创作背景。完整 v2 图集为 1536 × 2288，含九种基础动作与十六个视线方向；各角色的具体格式以 `pets.json` 条目为准。

如果目录条目提供**公开分享**链接，也可以把链接发给启用了 Pets 的助手，要求导入并选用，获得自己的副本。分享链接失效或撤回时，可使用仓库中的图集。

## 安装本地兼容包

克隆仓库，或在 GitHub 点击 **Code → Download ZIP** 并解压：

```bash
git clone https://github.com/xiaotwu/arknights-codex-pets.git
cd arknights-codex-pets
python3 install.py --list
```

从列表选择角色 ID，将下面的 `CHARACTER_ID` 替换为实际值：

```bash
python3 install.py CHARACTER_ID
```

可一次传入多个 ID。省略 ID 会安装**所有可用角色包**：

```bash
python3 install.py
```

Windows 上可按需将 `python3` 换成 `py -3`。使用 `--dest /path/to/pets` 可以指定其他宠物目录。

安装脚本自动发现 `codex/` 下的角色包，复制到 `$CODEX_HOME/pets/`；未设置 `CODEX_HOME` 时使用 `~/.codex/pets/`。已有同名目录时会停止，避免覆盖。

```text
<CODEX_HOME>/pets/
└── <character-id>/
    ├── pet.json
    └── spritesheet.webp
```

安装后，在提供此设置的桌面客户端打开 **Settings → Pets → Refresh**，或在兼容的 Codex CLI 会话中使用 `/pets` 选择角色。本地宠物与网页宠物分别管理，详见 [OpenAI Pets 文档](https://learn.chatgpt.com/docs/pets)。

本地包结构依据 [OpenAI hatch-pet 技能](https://github.com/openai/skills/blob/main/skills/.curated/hatch-pet/SKILL.md)。v1 图集以 1536 × 1872 保留前九行动作，额外的十六方向视线位于完整 v2 PNG 中。

## 在 ChatGPT 网页设置上传

如果账号提供此入口，打开 **Settings → Personalization → Pet → Select pet → Upload pet**，上传角色目录所链接的本地包内的 v1 `spritesheet.webp`。截至 2026 年 10 月 15 日，[官方上传规范](https://learn.chatgpt.com/docs/pets)要求透明 PNG / WebP、1536 × 1872，且不超过 20 MiB。

## 仓库结构

```text
<character-id>.png                  完整动画图集
codex/<character-id>/pet.json       本地角色包清单
codex/<character-id>/spritesheet.webp
previews/<character-id>-*.gif       动画预览
docs/<character-id>.md              角色资料与来源
pets.json                          角色目录元数据
CATALOG.md / CATALOG.zh-CN.md       自动生成的角色目录
scripts/update_catalog.py          目录与校验和生成脚本
SHA256SUMS                         下载完整性校验
```

GIF 用于预览，导入时使用 PNG 或 WebP 图集，并保留原始尺寸、透明度与单元格布局。

## 新增角色

1. 选择唯一的小写英文 ID，多词可用连字符连接。文件名、角色包目录和清单中的 `id` 保持一致。
2. 按上述结构加入完整图集、本地兼容包、预览与角色资料；角色包清单沿用现有格式。
3. 在 `pets.json` 添加条目，填写角色名称、描述、提供的文件格式、相对路径和正确的 SHA-256。已有公开分享链接时可一并添加。角色资料中区分游戏事实、引用来源和创作解读。
4. 校验图集后，重新生成中英文角色目录与下载校验和：

```bash
python3 scripts/update_catalog.py
python3 install.py --list
```

生成脚本会检查引用文件、元数据和声明的校验和。角色专属信息集中在目录与角色资料中，这两份中英文导入指南可以随着合集扩充继续复用。

## 来源与说明

本项目为非官方同人项目，与 Hypergryph、Yostar 或 OpenAI 无官方合作关系。《明日方舟》角色与原作内容的权益归其原权利方所有；各角色的参考来源和演绎细节见对应资料文档。
