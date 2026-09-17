# 操作日志（append-only）

> 只追加、不修改。每条记录格式：`## [YYYY-MM-DD] <操作> | <标题>`，可用
> `grep "^## \[" wiki/log.md | tail -10` 快速查看最近操作。

## [2026-09-03] ingest | 环境搭建与 Git 基础
- 源文件：notes/01_环境搭建与Git基础.md
- 新建 source 页：sources/2026-09-03-环境搭建与git基础.md
- 关联实体/概念：[[Git]]、[[GitHub]]、[[Git工作流]]

## [2026-09-03] ingest | 描述性统计入门练习
- 源文件：code/01_描述性统计入门.py
- 新建 source 页：sources/2026-09-10-描述性统计入门练习.md
- 关联实体/概念：[[Python]]、[[pandas]]、[[描述统计]]

## [2026-09-10] ingest | 统计学基础概念
- 源文件：notes/01_统计学基础概念.md
- 新建 source 页：sources/2026-09-10-统计学基础概念.md
- 关联概念：[[描述统计]]、[[推断统计]]、[[总体与样本]]、[[数据类型]]、[[集中趋势与离散程度]]

## [2026-09-10] ingest | 数据类型与统计量练习
- 源文件：code/02_数据类型与统计量练习.py
- 新建 source 页：sources/2026-09-10-数据类型与统计量练习.md
- 关联概念：[[数据类型]]、[[集中趋势与离散程度]]

## [2026-09-10] ingest | Agent 学习资料
- 源文件：learning-materials/agent.html
- 新建 source 页：sources/2026-09-10-agent学习资料.md
- 关联概念：[[智能体]]；关联实体：[[Anthropic]]、[[LilianWeng]]

## [2026-09-10] ingest | LLM 上下文学习资料
- 源文件：learning-materials/llm-context.html
- 新建 source 页：sources/2026-09-10-llm上下文学习资料.md
- 关联概念：[[LLM上下文]]

## [2026-09-10] ingest | Skill 学习资料
- 源文件：learning-materials/skill.html
- 新建 source 页：sources/2026-09-10-skill学习资料.md
- 关联概念：[[Skill]]、[[概念学习]]；关联实体：[[WorkBuddy]]

## [2026-09-10] ingest | 概念关系综合分析
- 源文件：learning-materials/agent-context-skill-relationship.html（根目录 concept-relationship.html 为早期版本）
- 新建 source 页：sources/2026-09-10-概念关系综合分析.md
- 关联概念：[[智能体]]、[[LLM上下文]]、[[Skill]]

## [2026-09-10] ingest | 课程仓库说明
- 源文件：README.md
- 新建 source 页：sources/2026-09-10-课程仓库说明.md
- 关联实体：[[统计与数据分析课程]]、[[WorkBuddy]]、[[GLM]]

## [2026-09-10] bootstrap | 知识库初始化
- 按照 [llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) 格式搭建 raw/、wiki/、graph/、tools/ 目录
- 摄入 9 份源文档，创建 9 个实体页、10 个概念页、1 个综合页
- 建立工作流配置：.workbuddy/skills/wiki-agent/SKILL.md
- 运行 tools/build_graph.py 生成 graph/graph.json 与 graph/graph.html

## [2026-09-10] graph | 知识图谱构建
- 解析全部 wiki 页面的双链（wikilink），生成 EXTRACTED 边
- 输出：graph/graph.json、graph/graph.html（vis.js 交互图）
