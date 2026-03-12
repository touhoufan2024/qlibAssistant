import numpy as np

# 1. 模拟 A 股数据
# 假设有 1000 只股票 (N), 每只股票有 5 个因子 (M, 比如 PE, PB, Momentum等)
N, M = 1000, 5
X = np.random.randn(N, M)  # 特征矩阵
# 模拟真实的收益率 y = 0.5*f1 - 0.2*f2 + ... + 偏置
true_w = np.array([0.5, -0.2, 0.1, 0.0, 0.8])
y = X @ true_w + 0.05 + np.random.randn(N) * 0.1  # 实际收益率（带噪声）

# 2. 初始化模型参数
w = np.zeros(M)  # 权重向量
b = 0.0          # 偏置项
lr = 0.01        # 学习率

print(f"开始训练... 初始权重: {w}")

# 3. 训练循环 (体现向量与矩阵的协作)
for epoch in range(1000):
    # --- 前向传播 (核心：矩阵-向量乘法) ---
    # 这一步在 GPU 上会触发矩阵单元
    y_pred = np.dot(X, w) + b  
    
    # --- 计算误差 (核心：向量减法) ---
    error = y_pred - y
    
    # --- 计算梯度 (核心：矩阵转置后的乘法) ---
    # dw = (X的转置 乘以 误差) / 样本数
    # 这一步同样是矩阵/向量乘法的高峰期
    dw = (1 / N) * np.dot(X.T, error)
    db = (1 / N) * np.sum(error)
    
    # --- 参数更新 (核心：向量加减) ---
    # 这属于控制流和简单向量操作
    w = w - lr * dw
    b = b - lr * db
    
    if epoch % 20 == 0:
        loss = np.mean(error**2)
        print(f"Epoch {epoch}: Loss = {loss:.6f}")

print("-" * 30)
print(f"训练结束!")
print(f"模型学到的权重: {w}")
print(f"真实的权重对比: {true_w}")
print(f"真实的偏置: {b}")