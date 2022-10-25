import torch
import torch.functional as F
import torch.optim as optim
import torch.nn as nn
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

class Net(nn.Module):
    tanh = nn.Tanh()
    def __init__(self):
        super(Net, self).__init__()
        self.hidden = nn.Linear(1, 5)
        self.predict = nn.Linear(5, 1)
    
    def forward(self, input):
        out = self.hidden(input)
        out = self.tanh(out)
        out = self.predict(out)
        return out

net = Net()
# net = nn.Sequential(nn.Linear(1,10),nn.Sigmoid(),nn.Linear(10,1))
criterion = nn.MSELoss()
optimizer = optim.Adam(net.parameters(), lr=0.1)

x = torch.range(-5, 5, 0.01).view(-1, 1)
train = torch.sin(x)
data_loader = DataLoader((x,train),batch_size=4)

for epoch in range(100):
    running_loss = 0.0
    for i, data in enumerate(data_loader):
        inputs, labels = data[0], data[1]

        outputs = net(inputs)
        loss = criterion(outputs, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
else:
    print("finished training!")

net.eval()
y_after_training = net(x).detach()

plt.plot(x, train, 'b', ms=5)
plt.plot(x, y_after_training, marker='*', ms=1, c='hotpink')

plt.show()