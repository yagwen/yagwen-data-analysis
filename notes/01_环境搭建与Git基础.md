# 学习笔记：环境搭建与 Git 基础（2026-09-03）

## 今天完成了什么

1. 创建 GitHub 账号和公开仓库 `yagwen-data-analysis`
2. 把仓库克隆到本地
3. 搭好学习目录结构并完成第一次 push

## Git 三步曲（每天都要用的）

```bash
git add .                    # 1. 暂存：告诉 git 哪些改动要记录
git commit -m "修改说明"      # 2. 提交：在本地生成一个存档点
git push                     # 3. 推送：把存档点同步到 GitHub
```

## 今天遇到的坑

- push 时报 `Connection was reset`：DNS 把 github.com 解析到了不通的 IP，
  最终用本地转发代理解决。以后遇到类似报错，先判断是不是网络问题。

## 下次学习计划

- [ ] 阅读 `code/01_描述性统计入门.py`，跑一遍
- [ ] 复习：均值、中位数、标准差各自的含义
