# arknights-codex-pets

《明日方舟》角色同人动画桌宠：**普瑞赛斯（Priestess）**与**塑心（Virtuosa）**。提供完整动画图集、Codex 本地兼容包、预览和角色资料。

| 角色 | 完整图集 v2 | 本地兼容包 v1 | 角色设定 |
| --- | --- | --- | --- |
| 普瑞赛斯 Priestess | [priestess.png](priestess.png) | [codex/priestess](codex/priestess) | [角色分析](docs/priestess.md) |
| 塑心 Virtuosa | [virtuosa.png](virtuosa.png) | [codex/virtuosa](codex/virtuosa) | [角色设定](docs/virtuosa.md) |

![普瑞赛斯待机](previews/priestess-idle.gif)
![塑心待机](previews/virtuosa-idle.gif)

## 选择导入方式

| 使用环境 | 推荐方式 | 使用的文件 |
| --- | --- | --- |
| 可调用 Pets 插件的 ChatGPT Work / Codex 聊天 | 上传完整 PNG，让助手校验、创建并选用 | 根目录的 `priestess.png` 或 `virtuosa.png` |
| 读取本地自定义宠物的桌面客户端 / Codex CLI | 安装本地兼容包 | `codex/<角色名>/pet.json` 与 `spritesheet.webp` |
| 提供 Upload pet 的 ChatGPT 网页设置 | 上传 v1 兼容图集 | `codex/<角色名>/spritesheet.webp` |

Pets 的入口与可用性取决于账号、工作区和客户端版本。获取仓库文件后，再按以下步骤导入。

## 方法一 通过 Pets 插件导入完整图集

1. 下载 [priestess.png](https://raw.githubusercontent.com/xiaotwu/arknights-codex-pets/main/priestess.png) 或 [virtuosa.png](https://raw.githubusercontent.com/xiaotwu/arknights-codex-pets/main/virtuosa.png)，保留原始尺寸和透明度。
2. 在能够调用 **Pets** 插件的 ChatGPT / Codex 聊天中上传该文件。Codex 本地任务也可以直接读取已授权的仓库文件。
3. 发送下面的提示词，把名字替换为对应角色：

```text
请使用 Pets 插件，把我提供的完整透明动画图集导入为名为「普瑞赛斯」的宠物。
先校验图集，校验通过后创建并选用。使用现有图集，无需重新绘制。
```

塑心使用名字「塑心」和文件 `virtuosa.png`。可附上对应的 `docs/` 角色资料作为名称、描述和后续创作参考。

这两个 PNG 均为 **1536 × 2288 的 v2 图集**，含九种基础动作和十六个视线方向；已通过本次 Pets 插件环境的格式校验。助手应完成图集校验、创建和选用，再核对当前宠物。

### 普瑞赛斯分享链接

[直接获取普瑞赛斯的 Pets 分享链接](https://chatgpt.com/s/sharepet_6ad1706508f88191bf295be53b0ad12e)

把该链接发给启用了 Pets 的助手，并说「请导入并选用这个 Pet」。此流程会在接收者账号创建副本。分享链接失效时，可改用仓库中的 PNG。

## 方法二 安装 Codex 本地兼容包

克隆仓库，或在 GitHub 点击 **Code → Download ZIP** 并解压：

```bash
git clone https://github.com/xiaotwu/arknights-codex-pets.git
cd arknights-codex-pets
python3 install.py
```

Windows 上可使用 `py -3 install.py`。仅安装其中一个角色：

```bash
python3 install.py priestess
python3 install.py virtuosa
```

安装脚本将兼容包复制到 `$CODEX_HOME/pets/`；未设置 `CODEX_HOME` 时使用用户目录下的 `.codex/pets/`。已存在的同名目录会使安装停止，避免覆盖现有宠物。也可以用 `--dest /path/to/pets` 指定目标宠物目录。

安装后的结构为：

```text
<CODEX_HOME>/pets/
├── priestess/
│   ├── pet.json
│   └── spritesheet.webp
└── virtuosa/
    ├── pet.json
    └── spritesheet.webp
```

在提供宠物设置的桌面客户端打开 **Settings → Pets → Refresh**，选择普瑞赛斯或塑心。Codex CLI 可输入 `/pets` 打开选择器；需要支持图片显示的终端。桌面本地宠物与网页端的宠物分别管理。参见 [OpenAI Pets 文档](https://learn.chatgpt.com/docs/pets)。

本地包结构依据 [OpenAI 官方 hatch-pet 技能](https://github.com/openai/skills/blob/main/skills/.curated/hatch-pet/SKILL.md)。兼容包使用 **1536 × 1872 的 v1 图集**：从完整版本无损提取前九行动作，保留九种基础动作；十六方向视线包含在根目录的 v2 PNG 中。

## 方法三 在 ChatGPT 网页上传

如果账号提供此入口，打开 **Settings → Personalization → Pet → Select pet → Upload pet**，选择 [普瑞赛斯 v1 WebP](codex/priestess/spritesheet.webp) 或 [塑心 v1 WebP](codex/virtuosa/spritesheet.webp)。截至 2026 年 10 月 15 日，[官方网页上传说明](https://learn.chatgpt.com/docs/pets)要求透明 PNG / WebP、1536 × 1872，且不超过 20 MiB；该入口使用仓库的 v1 兼容文件。

## 文件与动画说明

- 根目录的 `priestess.png`、`virtuosa.png`：完整透明图集，8 列 × 11 行，每格 192 × 208，73 个有效帧。
- `codex/`：本地可安装的 v1 兼容包，8 列 × 9 行，57 个有效帧。
- `pets.json`：通用角色目录与文件信息；安装使用各包内的 `pet.json`。
- `previews/`：待机、全部动作、视线循环与逐帧总览。GIF 用于预览，导入时使用 PNG / WebP 图集。
- `docs/`：游戏设定、性格分析与桌宠演绎说明，包含部分剧情信息。
- `SHA256SUMS`：可用于核对下载的图集与仓库版本一致。

九种基础动作依次为待机、向右移动、向左移动、招手、轻跃、受挫、等待输入、专注工作、检查成果。导入时保留原始图集尺寸、透明度和行列布局。

完整预览：[普瑞赛斯动作](previews/priestess-animations.gif) · [塑心动作](previews/virtuosa-animations.gif) · [普瑞赛斯视线](previews/priestess-look.gif) · [塑心视线](previews/virtuosa-look.gif)。

## 角色与素材来源

普瑞赛斯使用参考角色图生成 Q 版动画；塑心沿用已有 Q 版动画，并补齐游戏设定。角色解读、引用和创作取舍见各自的角色文档。

本项目为非官方同人桌宠整理项目，与鹰角网络、Hypergryph、Yostar 或 OpenAI 无官方合作关系。《明日方舟》角色及相关原作内容的权益归其原权利方所有。
