import numpy as np

rand_array = np.random.random(9)
print(f"rand_array is :\n{rand_array}\n", f"median is : {np.median(rand_array):.8f}", f"and average is : {np.mean(rand_array):.8f}", sep='\n')
# print(f"\nmedian after repeat 100 times is : {np.median([np.mean(np.random.random(9)) for _ in range(100)])}:.8f")
avg = 0
for i in range(100):
    avg = (avg*i + np.median(np.random.random(9))) / (i+1)
print(f'{avg:.8f}')