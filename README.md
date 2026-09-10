# 统计与数据分析

本仓库用于《统计与数据分析》课程的学习：存放课堂笔记、练习代码、课程作业和小项目。
当前包含 **AI Skill 实践作业**（见下方第二部分）。

## 仓库结构

```
yagwen-data-analysis/
├── README.md                        # 本文件：仓库说明
├── .gitignore                       # Git 忽略规则
├── .workbuddy/
│   └── skills/
│       └── concept-learning/
│           └── SKILL.md             # 【作业】个人学习 Skill：概念学习资料生成
├── learning-materials/              # 【作业】用 Skill 生成的三份概念学习资料
│   ├── agent.html                   #   Agent（智能体）
│   ├── llm-context.html             #   LLM 上下文
│   └── skill.html                   #   Skill（技能）
├── concept-relationship.html        # 【作业】三个概念的关系图 + 个人理解
├── notes/                           # 学习笔记（Markdown）
├── code/                            # 课后练习代码（Python）
├── homework/                        # 课程作业
└── data/                            # 练习用数据集
```

## 一、课程学习使用方法

1. 平时在本地写笔记、写代码，放进对应文件夹
2. 每次学完一个小节，执行三步提交：

```bash
git add .                      # 1. 把改动加入暂存区
git commit -m "本次修改说明"    # 2. 提交到本地仓库
git push                       # 3. 推送到 GitHub
```

## 二、AI Skill 实践作业

### 1. Skill 说明

- **名称**：concept-learning（概念学习资料生成）
- **位置**：`.workbuddy/skills/concept-learning/SKILL.md`（项目级 Skill）
- **功能**：输入任意概念名称，自动生成一份结构化学习资料（定义、个人理解、核心机制、应用场景、学习边界、概念辨析、自测题、可核查参考资料）。

### 2. 调用方式

在 WorkBuddy 中打开本仓库作为工作目录，直接对话触发，例如：

```
帮我学习一下 Agent 这个概念，入门深度
```

WorkBuddy 匹配到 Skill 的适用场景后，自动加载 `.workbuddy/skills/concept-learning/SKILL.md`
并按其中定义的流程生成资料到 `learning-materials/` 目录。

### 3. 已生成的学习资料

| 文件 | 概念 | 核心内容 |
|---|---|---|
| `learning-materials/agent.html` | Agent（智能体） | 四大组成：规划 / 记忆 / 工具使用 / 行动 |
| `learning-materials/llm-context.html` | LLM 上下文 | 上下文窗口机制、位置注意力、与长期记忆的区别 |
| `learning-materials/skill.html` | Skill（技能） | SKILL.md 结构、触发机制、与 Prompt/记忆/插件的辨析 |
| `concept-relationship.html` | 三者关系 | Mermaid 关系图 + 个人理解（上下文决定上限，Skill 沉淀经验） |

### 4. AI 使用与人工核查记录

**AI 参与的部分：**
- 使用 WorkBuddy（模型：GLM）生成 SKILL.md 初稿、三份学习资料的 HTML 初稿、概念关系图和本 README 的作业章节。
- AI 提供了概念的解释框架、机制表格和参考资料链接。

**人工核查与修改：**
- [x] 逐条点击核查了所有参考链接，确认真实可访问，无编造 URL。
- [x] 核对概念表述与 Anthropic / Lilian Weng 等来源原文，修正了初稿中不准确的类比。
- [x] "我的理解"章节以自己的语言改写，替换为自己使用 AI 工具的真实经历。
- [x] 自测题答案经本人复核，确认与正文内容一致。

**敏感信息处理：**
- 仓库不含任何账号、密码、API Key、个人证件号等敏感信息。
- `.gitignore` 已配置排除 `.env`、密钥类文件；提交前检查过文件清单。

## 学习进度

- [ ] 第一章：统计学基础概念
- [ ] 第二章：描述性统计
- [ ] 第三章：概率与分布
- [ ] 第四章：Python 数据分析基础（pandas / numpy）
- [ ] 第五章：数据可视化（matplotlib）
- [ ] 第六章：推断统计与假设检验

---
最后更新：2026-09-10
