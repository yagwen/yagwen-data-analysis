---
title: "Skill"
type: concept
tags: [AI, Skill]
sources: [2026-09-10-skill学习资料, 2026-09-10-概念关系综合分析]
last_updated: 2026-09-10
---

## 定义

**Skill（AI 技能）**：交给 AI 的**标准作业手册（SOP）**——如同给新员工的一份工作手册。核心价值：**教会一次，以后每次都懂**。

## SKILL.md 的构成

1. 元数据（YAML 头）
2. 触发标签
3. 正文（Markdown）
4. 标准作业流程
5. 参考资源（可选）

## 辨析

| 对比 | 区别 |
|---|---|
| Skill vs Prompt | Prompt 是一次性指令；Skill 是可复用的完整流程 |
| Skill vs 记忆 | 记忆是被动积累的信息；Skill 是主动编写的操作规范 |
| Skill vs 插件 | 插件提供能力接口；Skill 提供做事方法 |

## 在三者关系中的位置

Skill 是**知识层**——"随取随用的标准手册"，**Skill 沉淀经验**。详见[[agent上下文skill三者关系]]。

## 我的实践

- 已在 [[WorkBuddy]] 中使用自建的 concept-learning Skill（见[[概念学习]]）
- 触发机制：对话匹配适用场景后自动加载 SKILL.md 并按流程执行

## 关联

- [[LLM上下文]] — Skill 被触发时注入上下文
- [[智能体]] — Agent 复用 Skill 沉淀的经验
- [[概念学习]] — 一个具体实例
