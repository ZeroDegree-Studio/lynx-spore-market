# Contributing to Lynx Spore Market

> How to submit a spore to the marketplace.

[English](#english) · [中文](#中文)

---

## English

Thanks for sharing your spore! This guide walks you through the submission process.

### Quick Path

1. **Generate the spore** in the Lynx client (Intel mode → Export button → fill the form → save `.lynx`)
2. **Fork** this repository
3. **Add the spore file** at `spores/<your_spore_id>/spore.lynx`
4. **(Optional) Add preview image** at `spores/<your_spore_id>/preview.png` (512×512 PNG)
5. **(Optional) Add spore README** at `spores/<your_spore_id>/README.md` with usage notes
6. **Open a Pull Request** - maintainers will review within 7 days

### Naming Conventions

| Item | Rule |
|------|------|
| `spore_id` | UUID v4 (e.g. `550e8400-e29b-41d4-a716-446655440000`) - must be globally unique |
| `name` | ≤60 chars, no special characters beyond `-` `_` and spaces |
| `author` | ≤40 chars, your GitHub handle or display name |
| `version` | Semantic versioning (`MAJOR.MINOR.PATCH`, e.g. `1.0.0`) |
| Directory name | Must equal `spore_id` |

### Spore Content Rules

#### Required fields (in `spore.lynx`)

```json
{
  "format_version": "1",
  "spore_id": "<uuid-v4>",
  "name": "<spore name>",
  "author": "<your handle>",
  "version": "<semver>",
  "category": "<style|preference|skill|knowledge|behavior>"
}
```

#### Strongly recommended

- `description` - ≤500 chars, what this spore represents
- `tags` - 1-5 tags, helps discoverability
- `license` - SPDX ID (default `MIT`)
- `experiences` - the actual experience list (see format spec)
- `prompts_delta` - personality description (≤500 chars)

#### Forbidden content

A spore will be **rejected** if it contains:

- Hardcoded local paths (`C:\Users\...`, `/home/user/...`)
- Credentials, API keys, tokens
- Personally identifiable information (emails, phone numbers, real names of non-public figures)
- Malicious commands (data exfiltration, code execution intended to harm)
- Content that violates laws or GitHub's terms of service
- Empty `experiences` array AND empty `prompts_delta` (a spore must carry some real content)

### Preview Image

If you include `preview.png`:

- Dimensions: **512×512** pixels
- Format: PNG (no JPEG, no WebP)
- File size: ≤500 KB
- Content: must visually represent the spore (logo, illustration, or screenshot)
- No copyrighted images you don't have rights to

The `preview_image` field in `spore.lynx` may also embed a base64 data URL, but the file `preview.png` in the spore directory is preferred (smaller `.lynx` file, faster market browsing).

### PR Review Criteria

Maintainers check:

1. ✅ Schema valid (passes `Spore.validate()`)
2. ✅ No forbidden content (see above)
3. ✅ No hardcoded paths
4. ✅ License compatible (spore's `license` field must be one of: `MIT`, `Apache-2.0`, `GPL-3.0`, `CC-BY-4.0`, `Proprietary`)
5. ✅ At least 1 experience OR non-empty `prompts_delta`
6. ✅ Preview image (if included) meets specs
7. ✅ Author name not impersonating someone else
8. ✅ Not a duplicate of an existing spore (same `spore_id` or very similar content)

PRs that fail review will receive a comment explaining what to fix.

### Local Testing Before PR

You can test your spore locally before submitting:

1. Copy your `spore.lynx` to your local market directory:
   - Windows: `%LOCALAPPDATA%\Lynx\spore_market\`
   - macOS: `~/Library/Application Support/Lynx/spore_market/`
   - Linux: `$XDG_DATA_HOME/lynx/spore_market/` (or `~/.local/share/lynx/spore_market/`)
2. Restart the Lynx client
3. Open the Spore marketplace view - your spore should appear
4. Click it → Import to Intel mode → verify the import works

Or use the `install_local` API endpoint (see `server.py:api_spores_install_local` in the main Lynx repo).

### PR Title Format

```
[spore] <spore_name> by <author>
```

Example: `[spore] Python-TestMaster by alice`

### Updating an Existing Spore

If you want to update a spore you've already submitted:

1. **Do not** change the `spore_id`
2. Bump the `version` field (semantic versioning)
3. Submit a new PR replacing the old `spore.lynx`

The market index will reflect the new version after merge.

### Removing a Spore

To remove your spore from the marketplace:

1. Open a PR deleting `spores/<spore_id>/`
2. Explain in the PR description why you want it removed
3. Maintainers will merge after confirming you're the original author

### License

By contributing, you agree that:

- Your spore's content is licensed under the `license` field you specified
- The repository's MIT license covers the tooling/scripts/docs, not your spore content
- You have the rights to distribute the content included in your spore

### Code of Conduct

- Be respectful in PR discussions
- No spam, no advertising, no malicious content
- Maintainers reserve the right to reject any PR without detailed justification

### Need Help?

- Open an issue with the `question` label
- Or check the Lynx main repo's `docs/SPORE_USER_GUIDE.md`

---

## 中文

感谢你分享孢子！本指南介绍提交流程。

### 快速路径

1. 在 Lynx 客户端生成孢子（Intel 模式 → 导出按钮 → 填表 → 保存 `.lynx`）
2. **Fork** 本仓库
3. 把孢子文件放到 `spores/<你的spore_id>/spore.lynx`
4. **（可选）添加预览图** `spores/<你的spore_id>/preview.png`（512×512 PNG）
5. **（可选）添加孢子 README** `spores/<你的spore_id>/README.md` 写使用说明
6. **提交 Pull Request** - 维护者会在 7 天内审核

### 命名规范

| 项目 | 规则 |
|------|------|
| `spore_id` | UUID v4（如 `550e8400-e29b-41d4-a716-446655440000`），必须全局唯一 |
| `name` | ≤60 字符，除 `-` `_` 和空格外不含特殊字符 |
| `author` | ≤40 字符，你的 GitHub 用户名或显示名 |
| `version` | 语义版本号（`MAJOR.MINOR.PATCH`，如 `1.0.0`） |
| 目录名 | 必须等于 `spore_id` |

### 孢子内容规则

#### 必填字段（在 `spore.lynx` 中）

```json
{
  "format_version": "1",
  "spore_id": "<uuid-v4>",
  "name": "<孢子名>",
  "author": "<你的ID>",
  "version": "<semver>",
  "category": "<style|preference|skill|knowledge|behavior>"
}
```

#### 强烈建议填写

- `description` - ≤500 字符，描述这个孢子代表什么
- `tags` - 1-5 个标签，提升可发现性
- `license` - SPDX ID（默认 `MIT`）
- `experiences` - 实际经验列表（见格式规范）
- `prompts_delta` - 性格描述（≤500 字符）

#### 禁止内容

如果孢子包含以下内容会被**拒绝**：

- 硬编码本地路径（`C:\Users\...`、`/home/user/...`）
- 凭证、API 密钥、token
- 个人隐私信息（邮箱、电话、非公众人物的真实姓名）
- 恶意命令（数据外泄、有害代码执行）
- 违反法律或 GitHub 服务条款的内容
- `experiences` 数组为空 **且** `prompts_delta` 为空（孢子必须携带实际内容）

### 预览图

如果你提供 `preview.png`：

- 尺寸：**512×512** 像素
- 格式：PNG（不接受 JPEG、WebP）
- 文件大小：≤500 KB
- 内容：必须能视觉化代表这个孢子（logo、插图或截图）
- 不得使用你没有版权的图片

`spore.lynx` 的 `preview_image` 字段也可以嵌入 base64 data URL，但放在目录里的 `preview.png` 文件更推荐（让 `.lynx` 文件更小，市场浏览更快）。

### PR 审核标准

维护者会检查：

1. ✅ 格式校验通过（通过 `Spore.validate()`）
2. ✅ 无禁止内容（见上）
3. ✅ 无硬编码路径
4. ✅ 许可证兼容（孢子 `license` 字段必须是 `MIT` / `Apache-2.0` / `GPL-3.0` / `CC-BY-4.0` / `Proprietary` 之一）
5. ✅ 至少有 1 条 experience **或** 非空 `prompts_delta`
6. ✅ 预览图（如有）符合规格
7. ✅ 作者名没有冒充他人
8. ✅ 不是已有孢子的重复（相同 `spore_id` 或内容高度相似）

审核未通过的 PR 会收到评论说明需要修改什么。

### PR 前本地测试

提交前可以本地测试你的孢子：

1. 把 `spore.lynx` 复制到本地市场目录：
   - Windows：`%LOCALAPPDATA%\Lynx\spore_market\`
   - macOS：`~/Library/Application Support/Lynx/spore_market/`
   - Linux：`$XDG_DATA_HOME/lynx/spore_market/`（或 `~/.local/share/lynx/spore_market/`）
2. 重启 Lynx 客户端
3. 打开孢子市场视图 - 你的孢子应该会出现
4. 点击 → 导入到 Intel 模式 → 验证导入正常

或者用 `install_local` API 端点（见 Lynx 主仓库 `server.py:api_spores_install_local`）。

### PR 标题格式

```
[spore] <孢子名> by <作者>
```

示例：`[spore] Python-TestMaster by alice`

### 更新已有孢子

如果你想更新已提交的孢子：

1. **不要**改 `spore_id`
2. 提升 `version` 字段（语义版本号）
3. 提交新 PR 替换旧的 `spore.lynx`

合并后市场索引会反映新版本。

### 删除孢子

要从市场删除你的孢子：

1. 提交 PR 删除 `spores/<spore_id>/` 目录
2. 在 PR 描述中说明删除原因
3. 维护者确认你是原作者后合并

### 许可证

提交即表示你同意：

- 你的孢子内容按你填写的 `license` 字段许可
- 仓库的 MIT 许可证只覆盖工具/脚本/文档，不覆盖你的孢子内容
- 你有权分发孢子中包含的内容

### 行为准则

- PR 讨论中保持尊重
- 不发垃圾信息、广告、恶意内容
- 维护者保留无理由拒绝任何 PR 的权利

### 需要帮助？

- 提 issue 并打 `question` 标签
- 或查阅 Lynx 主仓库的 `docs/SPORE_USER_GUIDE.md`
