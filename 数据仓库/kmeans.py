import pandas as pd
import numpy as np
def K_mean(data, knum):
    p = len(data[0,:])
    cluscenter = np.zeros((knum, p))
    lastcluscenter = np.zeros((knum, p))
    for i in range(knum):
        cluscenter[i,:] = data[i,:]
        lastcluscenter[i,:] = data[i,:]
    clusindex = np.zeros((len(data)))
    while True:
        for i in range(len(data)):
            sumsquare = np.zeros((knum))
            for k in range(knum):
                sumsquare[k] = sum((data[i,:] - cluscenter[k,:])**2)
            sumsquare = np.sqrt(sumsquare)
            s = pd.Series(sumsquare).sort_values()
            clusindex[i] = s.index[0]
        clusdata = np.hstack((data, clusdata.reshape((len(data), 1))))
        for i in range(knum):
            cluscenter[i,:] = np.mean(clusdata[clusdata[:,p] == i, :-1], 0).reshape(1, p)
        t = abs(lastcluscenter-cluscenter)
        if sum(sum(t))==0:
            return clusdata
            break
        else:
            for k in range(knum):
                lastcluscenter[k,:] = cluscenter[k,:]
D = pd.read_excel('D.xlsx', header=None)
D = D.values
r = K_mean(D, 2)
x0 = r[r[:,2] == 0,0]
y0 = r[r[:,2] == 0,1]
x1 = r[r[:,2] == 1,0]
y1 = r[r[:,2] == 1,1]
