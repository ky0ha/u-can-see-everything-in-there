import matplotlib.pyplot as plt
import torch.nn.functional as F
import torch
import numpy as np

x = np.array([[2, 6, 1], [1, 2, 8], [1, 8, 5]])
y = np.array([10, 20, 28])

def getTheta(X_b, y):        #X_b为xi的训练集数值构成的矩阵， y为x对应的y的值构成的向量，函数效果为根据X_b和y求出x的参数矩阵
    theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
    return theta_best

theta = getTheta(x, y)
print(theta)

print(np.array([5, 4, 7]).dot(theta))
print(np.array([7, 40.5, 5]).dot(theta))