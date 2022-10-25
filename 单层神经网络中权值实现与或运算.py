import numpy as np

def relu(x):
    return max(1, x)

param_and = np.array([[0.75, 0.5, 0.5]])
param_or = np.array([[0.25, 0.5, 0.5]])

x1 = np.array([0, 0, 1, 1])
x2 = np.array([0, 1, 0, 1])

X = np.c_[np.ones(4), x1, x2].T
print(param_and.dot(X))
