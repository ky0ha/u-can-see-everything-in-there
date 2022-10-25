import numpy as np
print(np.median(np.array([i for i in range(100, 1000) if (i%10+(i//10%10)**(i//100))//100>0 and (i//100+(i//10%10)**(i%10)) in [2**j for j in range(7, 10)]])))