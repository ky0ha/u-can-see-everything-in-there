import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn


'''
网络构建部分
'''
class RBFN(nn.Module):
    """
    以高斯核作为径向基函数
    """
    def __init__(self, centers, n_out=1):
        """
        :param centers: shape=[center_num,data_dim]
        :param n_out:
        """
        super(RBFN, self).__init__()
        self.n_out = n_out
        self.num_centers = centers.size(0) # 隐层节点的个数
        self.dim_centure = centers.size(1) # 
        self.centers = nn.Parameter(centers)
        # self.beta = nn.Parameter(torch.ones(1, self.num_centers), requires_grad=True)
        self.beta = torch.ones(1, self.num_centers)*10
        # 对线性层的输入节点数目进行了修改
        self.linear = nn.Linear(self.num_centers+self.dim_centure, self.n_out, bias=True)
        # self.initialize_weights()# 创建对象时自动执行


    def kernel_fun(self, batches:torch.Tensor):
        n_input = batches.size(0)  # number of inputs
        # print(n_input, self.num_centers)
        A = self.centers.view(self.num_centers, -1).repeat(n_input, 1, 1)
        B = batches.view(n_input, -1).unsqueeze(1).repeat(1, self.num_centers, 1)
        C = torch.exp(-self.beta.mul((A - B).pow(2).sum(2, keepdim=False)))
        return C

    def forward(self, batches):
        radial_val = self.kernel_fun(batches)
        class_score = self.linear(torch.cat([batches, radial_val], dim=1))
        return class_score

'''
数据生成部分
'''
data = torch.tensor(np.arange(-1, 1, 0.1), dtype=torch.float32).view(-1, 1)
label = torch.sin(5*data)+torch.cos(3*data).view(-1, 1)

'''
创建网络对象，创建损失函数和优化器对象
'''
# centers = data[0:-1:2, :].clone()
centers = torch.rand(20, 1)
print(centers.shape)
rbf = RBFN(centers)
loss_fn = torch.nn.MSELoss()
optimizer = torch.optim.Adam(rbf.parameters(), lr=0.1)

'''
获取未训练之前网络的回归结果
'''
with torch.no_grad():
    y_without_training = rbf(data)

'''
训练过程
'''
for epoch in range(50):
    # for j in range(20):
    #     input = data[j]
    #     target = label[j]
        
    #     outputs = rbf(input)
    #     loss = loss_fn(outputs, target)
        
    #     optimizer.zero_grad()
    #     loss.backward()
    #     optimizer.step()
    # else:
    #     print(epoch)
    outputs = rbf(data)
    loss = loss_fn(label, outputs)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
else:
    print("finished")

'''
获取训练结束后的网络的回归结果
'''
with torch.no_grad():
    y_after_training = rbf(data)

'''
绘图
'''
plt.plot(data, label, ms=10)
plt.plot(data, y_without_training, '.', ms=5, c='red')
plt.plot(data, y_after_training, marker=',', ms=1, c='hotpink')
plt.show()