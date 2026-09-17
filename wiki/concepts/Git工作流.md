---
title: "Git工作流"
type: concept
tags: [Git, 工作流]
sources: [2026-09-03-环境搭建与git基础, 2026-09-10-课程仓库说明]
last_updated: 2026-09-10
---

## 定义

课程日常使用的 Git 三步提交流程，每天学完一个小节执行一次。

## 三步曲

```bash
git add .                    # 1. 暂存：告诉 git 哪些改动要记录
git commit -m "修改说明"      # 2. 提交：在本地生成一个存档点
git push                     # 3. 推送：把存档点同步到 GitHub
```

## 踩坑经验

- push 报 `Connection was reset` → DNS 解析到不通的 IP → 本地转发代理解决
- 通则：先判断是不是网络问题，再排查命令

## 关联

- [[Git]] — 工具本身
- [[GitHub]] — push 的目标
- [[统计与数据分析课程]] — 使用场景
