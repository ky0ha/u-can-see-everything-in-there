# 第二题
# 1）用pandas生成一个三行一列的向量series，行标是a,b,c，值是1,2,3
# 2）用pandas生成一个三行三列的dataframe，行标是a,b,c，列标e,f,g，值是1~9
# 3）把2)的第一行全部制成NaN
# 4）按列用平均方式补齐
import pandas as pd
import numpy as np

s_vals = [i+1 for i in range(3)]
series = pd.Series(s_vals, ['a', 'b', 'c'])
print(series)

df_vals = [[3*i+j+1 for j in range(3)] for i in range(3)]
dataframe = pd.DataFrame(df_vals, ['a', 'b', 'c'], ['e', 'f', 'g'])
print(dataframe)

dataframe.iloc[0,:] = np.nan
print(dataframe)

dataframe.fillna(dataframe.mean(), inplace=True)
print(dataframe)