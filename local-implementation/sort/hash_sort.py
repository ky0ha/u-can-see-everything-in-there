import numpy as np
import random
import time

def getPosition(x):
    return x//10, x%10

def hashSort(L):
    ls = np.zeros((10,10), dtype = np.int)
    for i in L:
        x, y = getPosition(i)
        ls[x][y] = i
    
    L.clear()

    for i in range(10):
        for j in range(10):
            if ls[i][j] != 0:
                L.append(ls[i][j])

    print(ls)
    return L

def main():
    L = random.sample(range(1, 100), 20)
    time_start = time.time()
    L = hashSort(L)
    time_end = time.time()
    print(L)
    print("Useing time is : {:.6f}".format(time_end - time_start))

main()