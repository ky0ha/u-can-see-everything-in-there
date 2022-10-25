import numpy as np
a, b, c, d, e = np.array([5 for _ in range(10)], dtype=np.float32), np.eye(3)*7, np.arange(1, 20, 3), np.array([np.array([12, 13, 14, 15])+i for i in range(0, 11, 5)]), np.array([np.array([14, 15, 16, 17])+i for i in range(0, 31, 10)])
print(a, b, c, d, e, sep='\n')