# step 1: generate on array with 100 elements [1, 2, 3, ..., 100]
# step 2: convert the array to a pandas dataframe
# step 3: sum the dataframe
import pandas as pd

print(f"the sum of range [1,100] is {pd.DataFrame([i+1 for i in range(100)], columns=['num']).sum()[0]}")