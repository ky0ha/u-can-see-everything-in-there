import math as Math
import random
from typing import List
import numpy as np

D = 2       # x 向量维度
F = 0.5     # 缩放率
CR = 0.9        # 变异率
LOW = [-3, -2]      # 上界
UP = [3, 2]     # 下界
PS = 30     # 种群大小
MaxFEs = 5E3        # ? 最大函数评估数

class indi:
    '''
    种群中每个个体对应的类，具有两个参数和一个方法：
    @param x 个体对应的向量
    @param fitness 个体的适应度，具体值为目标函数在当前个体上的值
    @method clone 返回一个当前个体的深拷贝
    '''
    def __init__(self, x, fitness):
        self.x = x
        self.fitness = fitness

    def clone(self):
        return indi(self.x, self.fitness)

def six_hump_camel_back(x):
    '''
    目标函数：:math:`y = 4 x_1^2 - 2.1 x_1^4 + x_1^6 + x_1 x_2 - 4 x_2^2 + r x_2^4`
    '''
    return 4*Math.pow(x[0], 2) - 2.1*Math.pow(x[0], 4)+ Math.pow(x[0],6)/3.0 + x[0]*x[1] - 4*Math.pow(x[1], 2) + 4*Math.pow(x[1], 4)

FEs = 0     # ? 当前函数评估数
pop :List[indi] = []        # 种群
for i in range(PS):     # 初始化种群
    x = np.random.rand(2)       # 生成当前个体的 x
    pop.append(indi(x, six_hump_camel_back(x)))     # 将当前个体的 fitness 求出，并将个体存入种群数组
FEs += PS   # ? 函数评估数加 PS

while FEs<= MaxFEs:     # 当当前评估数不超过最大评估数时，进行差分进化算法
    for i in range(PS):     # 遍历整个种群
        trialindi = pop[i].clone()      # 将当前个体的深拷贝存储到变量中
        
        # * DE/rand/1
        r = random.sample(range(PS-1), 3)   # 随机选三个除了 i 以外的数字，作为选出的三个个体的索引
        for j in range(3):      # 选择方法使用 sample 先从 [0, PS-1) 中不重复的随机选择三个数字
            if r[j]>=i:     # 再将三个数字中，超过当前个体 i 的数字进行 +1
                r[j] += 1       # 实现避免选择到第 i 个个体的效果
        v = pop[r[0]].x + F * (pop[r[1]].x - pop[r[2]].x)       # * :math:`V_i(t)=X_{r1}(t)+F \cdot (X_{r2}(t)-X_{r3}(t))`
        
        # * bin
        jrand = random.randint(1, D)        # * 随机 [1, D] 的整数作为 rand_j，因为 bin 交叉必须保证 U 有至少一个基因来自于 V
        u = np.array([(pop[i].x[j], v[j])[random.random()<CR or jrand==j] for j in range(D)])       # 交叉操作，使用特殊的三目运算写法实现交叉
        
        # * selection
        u_fitness = six_hump_camel_back(u)      # 求出 U 的适应度
        if u_fitness<pop[i].fitness:        # 实验个体 U 和 当前个体 X 优胜劣汰
            pop[i] = indi(u, u_fitness)
    FEs += PS       # 评估数 +PS

# 找出 DE 算法后的种群内的最有适应度个体
best_index = 0
for i in range(PS):
    if pop[i].fitness < pop[best_index].fitness:
        best_index = i

# 输出结果
print(f"best fitness : {pop[best_index].fitness}")
for i in range(D):
    print(f"x{i} = {pop[best_index].x[i]:.4f}", end='\t')