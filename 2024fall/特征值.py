import numpy as np

# 输入矩阵
A = np.array([
    [4,1,0,-1],
    [1,4,-1,0],
    [0,-1,4,1],
    [-1,0,1,4]
])

# 计算特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(A)

# 输出特征值
print("特征值：")
print(eigenvalues)

# 输出特征向量
print("特征向量：")
print(eigenvectors)
