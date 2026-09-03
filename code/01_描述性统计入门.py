# 第一章示例：用 Python 计算描述性统计
# 完成日期：2026-09-03

import pandas as pd

# 模拟一次小测的班级成绩
scores = pd.Series([78, 85, 92, 66, 74, 88, 95, 60, 83, 71])

print("=== 班级成绩描述性统计 ===")
print(f"人数:   {scores.count()}")
print(f"平均分: {scores.mean():.2f}")
print(f"中位数: {scores.median():.1f}")
print(f"标准差: {scores.std():.2f}")
print(f"最高分: {scores.max()}")
print(f"最低分: {scores.min()}")

# 用 pandas 一行搞定
print("\n=== describe() 一览 ===")
print(scores.describe())
