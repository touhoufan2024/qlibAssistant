import numpy as np
from sklearn.tree import DecisionTreeRegressor, export_text

# 1. 模拟一些量化数据 (X 是因子, y 是收益率)
# 因子：[PE, Volume_Change]
X = np.array([
    [5,  0.1], [8,  0.2], [12, -0.1],  # 低 PE 组
    [30, 0.5], [35, 0.6], [40, -0.2]   # 高 PE 组
])
y = np.array([0.05, 0.04, 0.02, -0.01, -0.02, -0.05])

# 2. 初始化决策树 (设置最大深度为 2，防止它像你之前担心的那样“钻牛角尖”)
# 在 Qlib 中，这个参数对应于配置里的 "max_depth"
model = DecisionTreeRegressor(max_depth=2)

# 3. 训练模型
model.fit(X, y)

# 4. 打印出决策树的逻辑 (就像看一堆 if-else 源码)
tree_rules = export_text(model, feature_names=['PE', 'Volume_Change'])
print("--- 决策树的逻辑判断过程 ---")
print(tree_rules)

# 5. 预测新数据
new_stock = np.array([[10, 0.15]]) # 一只 PE 为 10，成交量温和放大 15% 的股票
prediction = model.predict(new_stock)
print(f"预测该股票的收益率为: {prediction[0]:.2%}")