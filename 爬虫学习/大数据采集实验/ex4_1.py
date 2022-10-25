# 编写一个函数，随机（均匀）产生a~g的字符

import random
import time

def rand_alphabet(limit=1):
    random.seed(time)
    for i in range(limit):
        yield random.choice(seq=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

if __name__=='__main__':
    for i in rand_alphabet(5):
        print(i, end=' ')