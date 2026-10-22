# Arknights & Endfield Codex Pets

[English](README.md) | **简体中文**

持续扩充的《明日方舟》与《明日方舟·终末地》同人动画桌宠合集，供 ChatGPT 和 Codex 使用。每个角色使用稳定的英文 ID，配有可导入图集、动画预览和角色资料；角色目录按两部作品分别展示。

**[浏览角色目录](CATALOG.zh-CN.md)**，选择角色并下载对应文件。目录由 [pets.json](pets.json) 生成，新增角色时无需重写本导入指南。

## 选择导入方式

| 使用环境 | 方法 | 文件或角色包 |
| --- | --- | --- |
| 可调用 Pets 插件的 ChatGPT Work / Codex 聊天 | 上传完整图集，让助手校验、创建并选用 | `<character-id>.png` |
| 通过 codex-pets.net 导入 Codex | 打开角色页面，点击 **Install in Codex**，或使用页面显示的终端命令 | 目录中的 **codex-pets.net** 链接 |
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

每个角色默认提供**公开分享**链接。把目录中的链接发给启用了 Pets 的助手，要求导入并选用，即可获得自己的副本。分享链接失效或撤回时，可使用仓库中的图集。

## 通过 codex-pets.net 导入

1. 打开[角色目录](CATALOG.zh-CN.md)，点击角色条目中提供的 **codex-pets.net** 链接。
2. 在角色页面点击 **Install in Codex**。网站会打开 Codex 并填入安装请求，请在 Codex 中查看并完成安装。
3. 安装完成后，使用当前 Codex 客户端支持的宠物选择入口选用该角色。

也可以复制角色页面显示的终端命令，在已安装 Node.js、可使用 `npx` 的环境中运行：

```bash
npx codex-pets add SITE_PET_ID
```

这里应使用网站上的 ID，它可能与仓库角色 ID 不同。本合集的网站条目使用 `arknights-` 前缀；《明日方舟·终末地》条目统一使用 `arknights-endfield-<角色英文名>`。网站还提供 **Download sprite kit**，下载的 `.codex-pet.zip` 包含 `pet.json` 和 `spritesheet.webp`；该下载方式请按网站说明使用。

网站发布的角色包使用完整 v2 图集，尺寸为 1536 × 2288，含十六个视线方向；下文的仓库本地兼容包使用 v1。网站入口与安装功能的可用性取决于网站服务及客户端支持。

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

更新已有本地宠物时，先下载最新角色包或更新仓库副本。备份并将原来的 `<CODEX_HOME>/pets/<character-id>/` 整个目录移到宠物目录之外，再使用相同 ID 运行安装脚本；旧目录仍存在时，脚本会停止。角色目录中的链接始终指向当前发布的文件和预览。

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

1. 选择唯一的小写英文 ID，多词可用连字符连接。《明日方舟·终末地》的仓库与网站 ID 统一使用 `arknights-endfield-<角色英文名>`。文件名、角色包目录和清单中的 `id` 保持一致；`game` 填写 `Arknights` 或 `Arknights: Endfield`，目录会按作品分区。
2. 按上述结构加入完整图集、本地兼容包、预览与角色资料；角色包清单沿用现有格式。
3. 在 `pets.json` 添加条目，填写角色名称、描述、提供的文件格式、相对路径和正确的 SHA-256。默认为每个角色创建 ChatGPT Pets 公开分享链接，将返回的地址填入 `shareUrl`；已有有效链接时复用。若分享功能不可用或用户明确限制公开，记录例外原因，不得编造链接。已发布到 codex-pets.net 的角色可填写可选的 `codexPets` 元数据，包含网站 `id` 和 `url`；遵循上文各作品的 ID 规则，并保留既有 ID。角色资料中区分游戏事实、引用来源和创作解读。
4. 校验图集后，重新生成中英文角色目录与下载校验和：

```bash
python3 scripts/update_catalog.py
python3 install.py --list
```

生成脚本会检查引用文件、元数据和声明的校验和。角色专属信息集中在目录与角色资料中，这两份中英文导入指南可以随着合集扩充继续复用。

## 来源与说明

本项目为非官方同人项目，与 Hypergryph、Yostar 或 OpenAI 无官方合作关系。《明日方舟》《明日方舟·终末地》角色与原作内容的权益归其原权利方所有；各角色的参考来源和演绎细节见对应资料文档。
