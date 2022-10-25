from collections import namedtuple
import math as Math
import random
from typing import Iterable, List
import numpy as np


# indi = namedtuple("indi", ["x", "fitness"])
class indi(object):
    def __init__(self, x:Iterable, fitness:float):
        self.x = x
        self.fitness = fitness
    
    def clone(self):
        return indi(self.x, self.fitness)

def six_hump_camel_back(x):
    return 4*Math.pow(x[0], 2) - 2.1*Math.pow(x[0], 4)+ Math.pow(x[0],6)/3.0 + x[0]*x[1] - 4*Math.pow(x[1], 2) + 4*Math.pow(x[1], 4)

class DE(object):
    D = 2
    F = 0.5
    CR = 0.9
    LOW = [-3, -2]
    UP = [3, 2]
    PS = 30
    MaxFEs = 5E3
    
    # rnd, FEs, pop, bestIdx
    
    def __init__(self):
        # rnd = random
        # pop = [indi([0, 0], 0) for _ in range(self.PS)]
        self.FEs = 0
        self.pop: List[indi] = []
    
    def increaseFEs(self, count):
        self.FEs += count
    
    def _sample(self, count, idx):
        # t = 0
        # r = []
        # while t<count:
        #     num = random.randrange(0, self.PS)
        #     if num not in r and num!=idx:
        #         r.append(num)
        #         t += 1
        r = []
        l = [i for i in range(self.PS)]
        l.remove(idx)
        for i in range(count):
            tempidx = int(random.random() * len(l))
            r.append(l.pop(tempidx))
        return r
    
    def init(self):
        for _ in range(self.PS):
            vector = np.random.rand(2)
            self.pop.append(indi(vector, six_hump_camel_back(vector)))
        self.increaseFEs(self.PS)
    
    def iteration(self):
        while self.FEs <= self.MaxFEs:
            for i in range(self.PS):
                # trialindi = indi([0 for _ in range(self.D)], 0)
                # self.clone(trialindi, self.pop[i])
                trialindi = self.pop[i].clone()
                rndD = int(random.random())
                r = self._sample(3, i)
                for j in range(self.D):
                    num = random.random()
                    if num<=self.CR or rndD==j:
                        trialindi.x[j] = self.pop[r[0]].x[j] + self.F*(self.pop[r[1]].x[j]-self.pop[r[2]].x[j])
                        if trialindi.x[j]<self.LOW[j] or self.UP[j]<trialindi.x[j]:
                            trialindi.x[j] = self.LOW[j] + random.random()*(self.UP[j]-self.LOW[j])
                trialindi.fitness = six_hump_camel_back(trialindi.x)
                if trialindi.fitness < self.pop[i].fitness:
                    # self.clone(self.pop[i], trialindi)
                    self.pop[i] = trialindi.clone()
                self.increaseFEs(self.PS)
            
    def getBest(self):
        self.bestIdx = 0
        for i in range(self.PS):
            if self.pop[i].fitness < self.pop[self.bestIdx].fitness:
                self.bestIdx = i
        return self.pop[self.bestIdx]

sample = DE()
sample.init()
sample.iteration()
best = sample.getBest()
print(f"Best fitness={best.fitness}")
for i in range(sample.D):
    print(f"x_{i+1}={best.x[i]}", end=' ')
    if (i+1) % 5 == 0:
        print()
print(six_hump_camel_back(best.x))
# import matplotlib.pyplot as plt
# x = []
# y = []
# for i in range(100):
#     sample = DE()
#     sample.init()
#     sample.iteration()
#     best = sample.getBest()
#     x.append(best.x[0])
#     y.append(best.x[1])
# plt.scatter(x, y)
# plt.show()