import random
import time
import math

def radixSort(ls, radix):
    bucket = [[] for i in range(radix)]
    k = int(math.ceil(math.log(max(ls), radix)))

    for i in range(1, k+1):
        for val in ls:
            bucket[val % (radix**i) // (radix)**(i-1)].append(val)
        ls.clear()

        for each in bucket:
            ls.extend(each)
            bucket = [[] for i in range(radix)]
    
    return ls

def main():
    L = random.sample(range(1, 10001), 10000)
    time_start = time.time()
    L = radixSort(L, 10)
    time_end = time.time()
    print(L)
    print("Useing time is : {:.6f}".format(time_end - time_start))

main()