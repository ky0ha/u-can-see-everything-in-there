import torch
import torch.nn as nn
import torch.functional as F

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(1, 3)
        self.predict = nn.Linear(3, 1)
    
    def forward(self, inputs):
        out = self.hidden(inputs)
        out = self.predict(out)
        return out

net = Net()
for i in net.parameters():
    print(i)
print(net(torch.tensor([1], dtype=torch.float32)))