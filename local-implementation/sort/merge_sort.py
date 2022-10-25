from random import randint
from time import perf_counter

def merge_create_new_list(l1:list, l2:list):
    r = []
    while l1!=[] and l2!=[]:
        if l1[0]<l2[0]:
            r.append(l1.pop(0))
        else:
            r.append(l2.pop(0))
    return r+l1+l2
    # r = []
    # i, j = 0, 0
    # imax, jmax = len(l1), len(l2)
    # while i!=imax and j!=jmax:
    #     if l1[i]<l2[j]:
    #         r.append(l1[i])
    #         i+=1
    #     else:
    #         r.append(l2[j])
    #         j+=1
    # r = r + l1[i:] + l2[j:]
    # return r



# ls = [randint(0, 100) for _ in range(20)]
# print(f'the list before sort is :\n{ls}')

# time = []
# for i in range(100):
#     l1 = sorted([randint(0, 100) for _ in range(100)])
#     l2 = sorted([randint(0, 100) for _ in range(100)])

l1 = sorted([randint(0, 1000) for _ in range(1000)])
l2 = sorted([randint(0, 1000) for _ in range(1000)])
start = perf_counter()
print(merge_create_new_list(l1, l2))
end = perf_counter()
print(end-start)