import time

def getPiovt(ls,a,n):
    basic = n
    i, j = a, n
    while i!=j:
        while(ls[i]<=ls[basic] and i!=j):
            i+=1
        while(ls[j]>=ls[basic] and i!=j):
            j-=1
        ls[i], ls[j] = ls[j], ls[i]
    else:
        ls[i], ls[basic] = ls[basic], ls[i]
        basic = i
    return basic

def quickSort(ls,a,n): 
    if a < n: 
  
        pi = getPiovt(ls,a,n) 
  
        quickSort(ls, a, pi-1) 
        quickSort(ls, pi+1, n)
    else:
        return ls

import random
ls = random.sample(range(1, 10001), 10000)
b=ls
sorted(b)
print("Before the sorting, the list is: {} \n".format(ls))
n=len(ls)
time_start = time.time()
quickSort(ls,0,n-1)
time_end = time.time()
print("After the sorting once, the list is: {} \n".format(ls))
print("Useing time is : {:.6f}".format(time_end - time_start))
print("The true result is: {}\n".format(b))
if b==ls:
    print("And your sort is right!")
else:
    print("Sorry, the result is wrong!")