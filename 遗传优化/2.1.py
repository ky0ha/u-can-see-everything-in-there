'''
torch 库的引用部分，用于构建数据集和神经网络
'''
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader

'''
matplotlib 库的引用部分，用于绘制图像
'''
import matplotlib
import matplotlib.pyplot as plt


'''
神经网络部分：
    * 一个输入层，一个输出层，一个隐含层
    * 输入层结点 1 个，输出层结点 1 个，隐含层结点 10 个
    * 层之间的连接使用线性函数
    * 激活函数使用 tansig
    * 使用动态 SGD 作为优化器，使用 MSE 损失函数作为损失函数
'''
class Net(nn.Module):
    tanh = nn.Tanh()
    def __init__(self):
        super(Net, self).__init__()
        self.hidden = nn.Linear(1, 10)
        # self.sig = nn.Sigmoid()
        self.predict = nn.Linear(10, 1)
    
    def forward(self, input):
        out = self.hidden(input)
        out = self.tanh(out)
        # out = self.sig(out)
        out = self.predict(out)
        return out
    
    def hidden_param(self):
        return self.hidden.get_parameter()
    
    def predict_param(self):
        return self.predict.get_submodule
    

net = Net()
# net = nn.Sequential(nn.Linear(1,10),nn.Sigmoid(),nn.Linear(10,1))
criterion = nn.MSELoss()
optimizer = optim.Adam(net.parameters(), lr=0.1)

'''
数据生成部分
'''
x = torch.range(-5, 5, 0.01).view(-1, 1)
# x = torch.randn((1, 10000)).view(-1, 1)
# print(x.shape)
train = torch.sin(x)
data_loader = DataLoader((x,train),batch_size=4)
# print(data_loader)
'''
获取未训练网络的预测结果
'''
with torch.no_grad():
    y_without_training = torch.Tensor([net(i) for i in x])

'''
训练网络，对数据集循环利用两次
'''
for epoch in range(100):
    running_loss = 0.0
    for i, data in enumerate(data_loader):
        # 获取输入
        # print(data.shape)
        inputs, labels = data[0], data[1]
        
        # 前向传播
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        # 梯度清零
        optimizer.zero_grad()
        # 误差反向传播
        loss.backward()
        
        # 优化
        optimizer.step()
        
        # 输出统计数据
        # running_loss += loss.item()
        # if i%2000 == 1999:  # 每 2000 个数据打印一次
        #     print(f'[{epoch+1}, {i+1:5d}] loss {running_loss/2000:.3f}')
        #     running_loss = 0.0
else:
    print("finished training!")

'''
获取训练后的，根据训练集进行的预测结果(不能体现模型预测效果，只能表示模型是否学习到了东西)
'''
# with torch.no_grad():
#     y_after_training = torch.Tensor([net(i) for i in x])
#     for i in range(0, 10000, 1000):
#         print(f"输入：{x[i]}, \t输出：{net(x[i])}       \t目标值：{train[i]} \t误差：{train[i]-net(x[i])}")

net.eval()
y_after_training = net(x).detach()
# print(y_after_training.shape)

# for i in net.get_parameter("Linear"):
#     print(i)
# for i in net.hidden_param("weight"):
#     print(i)
# print()
# for i in net.predict_param():
#     print(i)

'''
绘图部分
'''
plt.plot(x, train, 'b', ms=5)
plt.plot(x, y_without_training, 'r,', ms=1)
plt.plot(x, y_after_training, marker='*', ms=1, c='hotpink')
# plt.scatter(x, y_without_training, c='red', marker='*', s=5)
# plt.scatter(x, y_after_training, c='hotpink', marker='x', s=5)

plt.show()