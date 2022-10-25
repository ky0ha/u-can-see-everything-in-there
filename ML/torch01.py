import torch
x = torch.rand(5,3)
print(x)

# Tensors(张量)
# Tensors 类似于 NumPy 的 ndarrays ，同时  Tensors 可以使用 GPU 进行计算。
from __future__ import print_function
import torch
#构造一个5x3矩阵，不初始化。
x = torch.empty(5, 3)
print(x)