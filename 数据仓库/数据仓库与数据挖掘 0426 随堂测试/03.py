import numpy as np
from itertools import permutations

def to_int(iterable):
    return int(''.join(str(i) for i in iterable))
permutes = np.array([to_int(i) for i in permutations(range(10), 10) if i[0]!=0 and i[-1] in (0, 5) and to_int(i)%55555==0])

print(np.median(permutes))