# Wiki 索引

> 本知识库按照 [llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) 格式搭建，由 AI 维护。
> 工作流配置见 `.workbuddy/skills/wiki-agent/SKILL.md`：摄入（ingest）→ 查询（query）→ 健康检查（health）→ 诊断（lint）→ 知识图谱（graph）。

## 总览

- [总览](overview.md) — 跨所有源文档的动态综合

## 源（Sources）

- [环境搭建与 Git 基础](sources/2026-09-03-环境搭建与git基础.md) — 第一次搭建学习环境，Git 三步曲与网络踩坑记录
- [统计学基础概念](sources/2026-09-10-统计学基础概念.md) — 第一章笔记：两大分支、基本概念、数据类型
- [描述性统计入门练习](sources/2026-09-10-描述性统计入门练习.md) — 用 pandas 计算班级成绩的描述统计
- [数据类型与统计量练习](sources/2026-09-10-数据类型与统计量练习.md) — 数据类型识别 + 极端值对均值/中位数的影响实验
- [Agent 学习资料](sources/2026-09-10-agent学习资料.md) — 智能体的四大组成与 Agent Loop
- [LLM 上下文学习资料](sources/2026-09-10-llm上下文学习资料.md) — 上下文窗口机制与模型"失忆"的原因
- [Skill 学习资料](sources/2026-09-10-skill学习资料.md) — SKILL.md 结构、触发机制、与 Prompt/记忆/插件的辨析
- [概念关系综合分析](sources/2026-09-10-概念关系综合分析.md) — Agent / 上下文 / Skill 三者的三层架构与闭环
- [课程仓库说明](sources/2026-09-10-课程仓库说明.md) — 仓库用途、目录约定与 AI 使用核查记录

## 实体（Entities）

- [统计与数据分析课程](entities/统计与数据分析课程.md) — 本知识库所属的课程项目（仓库 yagwen-data-analysis）
- [Git](entities/Git.md) — 课程日常使用的版本控制系统
- [GitHub](entities/GitHub.md) — 托管课程仓库的代码平台
- [Python](entities/Python.md) — 课程使用的编程语言
- [pandas](entities/pandas.md) — 数据分析核心库，练习代码的主力
- [WorkBuddy](entities/WorkBuddy.md) — 使用的 AI 助手，本知识库的维护者
- [GLM](entities/GLM.md) — WorkBuddy 背后的大模型
- [Anthropic](entities/Anthropic.md) — Agent 学习资料中"复杂度递增"观点的来源
- [LilianWeng](entities/LilianWeng.md) — Agent 综述作者，学习资料的参考来源

## 概念（Concepts）

- [描述统计](concepts/描述统计.md) — 总结和展示已有数据的分支
- [推断统计](concepts/推断统计.md) — 用样本推断总体的分支
- [总体与样本](concepts/总体与样本.md) — 总体/样本/参数/统计量四要素与"双 P 双 S"口诀
- [数据类型](concepts/数据类型.md) — 定类/定序/离散/连续，决定统计方法的选择
- [集中趋势与离散程度](concepts/集中趋势与离散程度.md) — 均值/中位数/众数；极差/方差/标准差
- [Git工作流](concepts/Git工作流.md) — add / commit / push 三步曲
- [智能体](concepts/智能体.md) — Agent：规划/记忆/工具使用/行动四大组成
- [LLM上下文](concepts/LLM上下文.md) — 上下文窗口机制与注意力
- [Skill](concepts/Skill.md) — 交给 AI 的标准作业手册（SOP）
- [概念学习](concepts/概念学习.md) — 七段式结构化学习资料生成方法论

## 综合（Syntheses）

- [Agent、上下文、Skill 三者关系](syntheses/agent上下文skill三者关系.md) — 回答"三者分别是什么、如何协同工作"
