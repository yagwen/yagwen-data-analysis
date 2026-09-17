---
name: wiki-agent
description: 个人知识库维护技能（llm-wiki-agent 格式）。当用户要求"摄入/ingest"新资料、"查询/query"知识库、"检查/health/lint"知识库健康度、"构建图谱/graph"时使用。用户丢进 raw/ 的任何文档都可摄入；查询答案可存为综合页；摄入后需更新索引、总览和日志。
---

# wiki-agent — 个人知识库维护工作流

本技能参照 [llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) 项目，维护仓库中的三层知识库结构。**你（AI）完全拥有 wiki/ 目录的写入权，用户只读。**

## 目录结构

```
raw/           # 源文档（不可修改）。新资料丢这里，按主题建子目录
wiki/          # AI 维护的知识层
  index.md     # 全部页面的目录 — 每次 ingest 后更新
  log.md       # 只追加的操作日志
  overview.md  # 跨源动态综合 — 每次 ingest 后修订
  sources/     # 每份源文档一个摘要页
  entities/    # 人物、公司、项目、产品
  concepts/    # 概念、方法、理论
  syntheses/   # 查询答案沉淀成的综合页
graph/         # 图谱输出（graph.json + graph.html）
tools/build_graph.py  # 图谱生成脚本（无第三方依赖）
```

## 页面格式

所有 wiki 页面使用以下 frontmatter：

```yaml
---
title: "页面标题"
type: source | entity | concept | synthesis
tags: []
sources: []        # 依据的源页面 slug 列表（entity/concept/synthesis 页必填）
last_updated: YYYY-MM-DD
---
```

页面之间用 `[[页面名]]` 双链互联（页面名 = 文件名去掉 .md）。

### source 页模板（wiki/sources/）

```markdown
---
title: "源标题"
type: source
tags: []
date: YYYY-MM-DD
source_file: raw/... 或原路径
---

## 摘要
2–4 句话概括。

## 关键要点
- ……

## 关键引述
> "……" —— 语境

## 关联
- [[实体或概念名]] — 关系说明

## 矛盾
（无，或：与 [[某页]] 在……上矛盾）
```

### entity / concept 页模板

简介（定义）→ 核心要点 → 在我的学习中的角色/我的实践 → 关联（双链）。

### synthesis 页模板

问题（frontmatter 加 `question:` 字段）→ 回答（带 [[双链]] 引用）→ 来源说明。

## 工作流

### 1. 摄入（ingest）

触发词：*"摄入 raw/xxx.md"*、*"ingest ..."*、*"帮我把这份资料加进知识库"*

步骤（按序执行）：
1. 完整读取源文档（非 markdown 格式先转换为文本再读）
2. 读取 `wiki/index.md` 和 `wiki/overview.md` 了解现状
3. 写 `wiki/sources/<日期-slug>.md`（用上面的 source 模板）
4. 更新 `wiki/index.md`（在 Sources 段添加条目）
5. 修订 `wiki/overview.md`（如有必要）
6. 为文中出现的关键人物/公司/项目更新或创建 entity 页
7. 为文中讨论的关键概念更新或创建 concept 页
8. 如与现有内容矛盾，在 source 页"矛盾"段明确标记
9. 追加日志：`## [YYYY-MM-DD] ingest | <标题>`
10. 校验：新页面均已进 index、双链无断链，输出变更摘要

### 2. 查询（query）

触发词：*"query: ……"*、*"知识库里关于 X 是怎么说的？"*

步骤：读 index 定位相关页 → 读相关页 → 用 [[双链]] 引用合成回答 → 询问用户是否将答案存为 `wiki/syntheses/<slug>.md`。

### 3. 健康检查（health，快速、零成本）

触发词：*"health"*、*"检查知识库"*

检查：空文件/只有 frontmatter 的页面；index 与磁盘文件是否同步；source 页是否都有对应 log 记录。可直接运行 `python tools/build_graph.py` 查看断链报告。

### 4. 诊断（lint，深度、定期）

触发词：*"lint"*、*"诊断知识库"*

检查：孤儿页面（无入链）、断链、跨页矛盾、过期摘要、被 3+ 页面提及但缺少独立页面的实体、知识缺口（建议补充什么源）。报告可存为 `wiki/lint-report.md`。

### 5. 图谱（graph）

触发词：*"构建图谱"*、*"build the knowledge graph"*

运行：`python tools/build_graph.py`（输出节点/边统计和断链报告），生成 `graph/graph.json` 与 `graph/graph.html`（浏览器打开 vis.js 交互图）。

## 命名规范

- source 页：`YYYY-MM-DD-slug.md`（kebab-case）
- entity / concept / synthesis 页：文件名即页面名，中文优先（如 `描述统计.md`、`Git.md`）
- 双链 `[[X]]` 必须与文件名（不含 .md）完全一致

## 注意事项

- `raw/` 与用户自己的目录（notes/、code/ 等）只读，不改动
- 每次 ingest 后**必须**同步更新 index、log，建议运行一次 build_graph.py 校验断链
- overview.md 是"活文档"，反映当前全部源的综合，不是流水账
