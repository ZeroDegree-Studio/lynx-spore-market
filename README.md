# Lynx Spore Market

> The official community marketplace for sharing Lynx Intelligence-mode agent experiences.

[English](#english) · [中文](#中文)

---

## English

### What is a Spore?

A **spore** is a shareable carrier of a Lynx Intelligence-mode AI agent's accumulated experience. It bundles the agent's preferences, skills, personality, and behavioral patterns into a single `.lynx` file that can be:

- **Exported** — saved from your local Intel-mode agent
- **Imported** — loaded into someone else's Intel-mode agent
- **Shared** — published to this marketplace for the global community
- **Purchased** — premium spores (first version uses mock payment; real payment adapters are reserved for future integration)

### Repository Structure

```
lynx-spore-market/
├── README.md                      # This file
├── CONTRIBUTING.md                # How to contribute a spore
├── LICENSE                        # Repository license (MIT)
├── .gitignore
├── index.json                     # Auto-generated spore index (updated by GitHub Actions)
└── spores/
    └── <spore_id>/
        ├── spore.lynx             # The spore file (JSON payload)
        ├── preview.png            # (Optional) Preview image
        └── README.md              # (Optional) Spore-specific docs
```

### Spore Format (`.lynx`)

A `.lynx` file is a UTF-8 encoded JSON document with these required fields:

```json
{
  "format_version": "1",
  "spore_id": "uuid-v4",
  "name": "My Spore",
  "author": "your-handle",
  "version": "1.0.0",
  "category": "skill"
}
```

Full specification: see the Lynx main repository at `docs/SPORE_FORMAT.md`.

### Experience Categories

Every spore is tagged with one of 5 experience categories:

| Category | Meaning |
|----------|---------|
| `style` | Speaking / writing style preferences |
| `preference` | General working preferences (tool choice, format) |
| `skill` | Concrete capabilities (what the agent can do) |
| `knowledge` | Domain facts and user context (what the agent knows) |
| `behavior` | Trigger conditions (when the agent acts) |

### Official Spores

Lynx ships with 5 native spores, auto-seeded into your local market on first launch:

| Name | Category | Description |
|------|----------|-------------|
| Lynx-Concise | style | Concise code style preferences |
| Lynx-General | preference | General assistant preferences |
| Lynx-CodeHelper | skill | Code skill pack (testing / refactoring / git) |
| Lynx-KnowledgeBase | knowledge | General knowledge base |
| Lynx-Proactive | behavior | Proactive behavior patterns |

Official spores display an **Official** blue badge in the client UI.

### Contributing a Spore

Quick steps (full guide: [CONTRIBUTING.md](CONTRIBUTING.md)):

1. Use the Lynx client's **Export** button to generate a `.lynx` file from your Intel-mode agent
2. Fork this repository
3. Add your spore at `spores/<spore_id>/spore.lynx`
4. (Optional) Add `preview.png` (512×512) and `README.md`
5. Open a pull request — maintainers will review

Spore PRs are reviewed for: schema validity, no malicious content, no hardcoded paths, license compatibility.

### License

- **This repository** (tooling, scripts, docs): [MIT License](LICENSE)
- **Each spore** carries its own `license` field (default `MIT`, also supports `Apache-2.0`, `GPL-3.0`, `CC-BY-4.0`, `Proprietary`)

The repository MIT license **does not** override individual spore licenses. Users must respect each spore's own license field when redistributing or modifying spore content.

### Client Integration

The Lynx client reads this marketplace via the **GitHubMarketAdapter**: it fetches `index.json` from this repository (via `raw.githubusercontent.com`, with a configurable mirror URL for CDN access) and downloads spores on demand. The client can switch between the **local market** (default, offline-friendly) and this **GitHub market** at any time.

### Links

- **Lynx main repository**: [github.com/ZeroDegree-Studio/LYNX](https://github.com/ZeroDegree-Studio/LYNX)
- **Spore format spec**: [`docs/SPORE_FORMAT.md` in the main repo](https://github.com/ZeroDegree-Studio/LYNX/blob/main/docs/SPORE_FORMAT.md)
- **User guide**: [`docs/SPORE_USER_GUIDE.md` in the main repo](https://github.com/ZeroDegree-Studio/LYNX/blob/main/docs/SPORE_USER_GUIDE.md)
- **ZeroDegree Studio**: [zerodegree.cc](https://zerodegree.cc)

---

## 中文

### 什么是孢子？

**孢子**（Spore）是 Lynx Intelligence 模式 AI 智能体积累经验的可分享载体。它把智能体的偏好、技能、性格、行为模式打包成一个 `.lynx` 文件，可以：

- **导出** — 从你的本地 Intel 模式智能体保存出来
- **导入** — 加载到别人的 Intel 模式智能体
- **分享** — 发布到本市场供全球用户使用
- **购买** — 付费孢子（首版用 Mock 支付模拟，真实支付通道后期接入）

### 仓库结构

```
lynx-spore-market/
├── README.md                      # 本文件
├── CONTRIBUTING.md                # 如何贡献孢子
├── LICENSE                        # 仓库许可证（MIT）
├── .gitignore
├── index.json                     # 自动生成的孢子索引（GitHub Actions 自动更新）
└── spores/
    └── <spore_id>/
        ├── spore.lynx             # 孢子文件（JSON 内容）
        ├── preview.png             # （可选）预览图
        └── README.md              # （可选）孢子专属文档
```

### 孢子格式（`.lynx`）

`.lynx` 文件是 UTF-8 编码的 JSON，必填字段：

```json
{
  "format_version": "1",
  "spore_id": "uuid-v4",
  "name": "我的孢子",
  "author": "你的ID",
  "version": "1.0.0",
  "category": "skill"
}
```

完整规范：见 Lynx 主仓库 `docs/SPORE_FORMAT.md`。

### 经验分类

每个孢子标记为 5 类经验之一：

| 分类 | 含义 |
|------|------|
| `style` | 说话/写作风格偏好 |
| `preference` | 通用做事偏好（工具选择、格式偏好） |
| `skill` | 具体能力（智能体会做什么） |
| `knowledge` | 知识/用户上下文（智能体知道什么） |
| `behavior` | 触发条件（智能体何时行动） |

### 原生孢子

Lynx 客户端首版自带 5 个原生孢子，首次启动时自动种入本地市场：

| 名称 | 分类 | 描述 |
|------|------|------|
| Lynx-Concise | style | 简洁代码风格偏好 |
| Lynx-General | preference | 通用助手偏好 |
| Lynx-CodeHelper | skill | 代码技能包（测试/重构/git） |
| Lynx-KnowledgeBase | knowledge | 通用知识库 |
| Lynx-Proactive | behavior | 主动型行为模式 |

原生孢子在客户端 UI 显示蓝色 **Official** 徽章。

### 贡献孢子

快速步骤（完整指南：[CONTRIBUTING.md](CONTRIBUTING.md)）：

1. 用 Lynx 客户端的「导出」按钮从你的 Intel 模式生成 `.lynx` 文件
2. Fork 本仓库
3. 把孢子放到 `spores/<spore_id>/spore.lynx`
4. （可选）添加 `preview.png`（512×512）和 `README.md`
5. 提交 Pull Request，等待维护者审核

审核标准：格式校验通过 / 无恶意内容 / 无硬编码路径 / 许可证兼容。

### 许可证

- **本仓库**（工具脚本、文档）：[MIT License](LICENSE)
- **每个孢子**带自己的 `license` 字段（默认 `MIT`，可选 `Apache-2.0` / `GPL-3.0` / `CC-BY-4.0` / `Proprietary`）

仓库的 MIT **不覆盖**孢子内容本身。用户在再分发或修改孢子时必须遵守每个孢子自己的 `license` 字段。

### 客户端对接

Lynx 客户端通过 **GitHubMarketAdapter** 读取本市场：直接拉取本仓库的 `index.json`（走 `raw.githubusercontent.com`，支持配置镜像地址走国内 CDN），按需下载孢子文件。客户端可在**本地市场**（默认，离线可用）与 **GitHub 市场**之间随时切换。

### 链接

- **Lynx 主仓库**：[github.com/ZeroDegree-Studio/LYNX](https://github.com/ZeroDegree-Studio/LYNX)
- **孢子格式规范**：主仓库 [`docs/SPORE_FORMAT.md`](https://github.com/ZeroDegree-Studio/LYNX/blob/main/docs/SPORE_FORMAT.md)
- **用户指南**：主仓库 [`docs/SPORE_USER_GUIDE.md`](https://github.com/ZeroDegree-Studio/LYNX/blob/main/docs/SPORE_USER_GUIDE.md)
- **零度工作室**：[zerodegree.cc](https://zerodegree.cc)
