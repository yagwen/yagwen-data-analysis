# raw/ — 源文档目录（不可修改）

本目录是知识库的**源材料层**，格式参照 [llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) 项目。

## 使用规则

1. **新资料丢进来**：文章、论文、笔记、PDF、DOCX、PPTX、HTML、CSV 等都可以放进 `raw/`（建议按主题建子目录，如 `raw/papers/`）。
2. **告诉 AI 摄入**：在 WorkBuddy 中说"摄入 raw/xxx.md"或"ingest raw/xxx.md"，AI 会读取源文档，把知识提取到 `wiki/` 中。
3. **源文档不可修改**：`raw/` 里的文件是原始存档，摄入后不要改动；修订应体现在 `wiki/` 页面里。

## 当前状态

知识库初始摄入的 9 份源材料来自本仓库已有目录，未做副本，`wiki/sources/` 页面的 frontmatter 中 `source_file` 字段记录了原始路径：

| 来源 | 原始路径 |
|---|---|
| 学习笔记 | `notes/` |
| 练习代码 | `code/` |
| 概念学习资料 | `learning-materials/`、根目录 `concept-relationship.html` |
| 仓库说明 | `README.md` |

今后新的外部资料请直接放入本目录再摄入。
