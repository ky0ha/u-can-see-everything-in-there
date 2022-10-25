if __name__ == '__main__':
    import numpy as np
    from numpy.linalg import eig

    data_path = r'C:\Users\25315\Downloads\数据.txt'
    with open(data_path, 'r', encoding='utf-8') as f:
        origin_data = f.readlines()[1:]
    data = np.array(list(map(lambda x:x[:-1].split(' '), origin_data)), dtype=np.int16)

    def pca(X,k):
        X = X - X.mean(axis = 0) #向量X去中心化
        X_cov = np.cov(X.T, ddof = 0) #计算向量X的协方差矩阵，自由度可以选择0或1
        eigenvalues,eigenvectors = eig(X_cov) #计算协方差矩阵的特征值和特征向量
        klarge_index = eigenvalues.argsort()[-k:][::-1] #选取最大的K个特征值及其特征向量
        k_eigenvectors = eigenvectors[klarge_index] #用X与特征向量相乘
        return np.dot(X, k_eigenvectors.T)

    X_pca = pca(data, 2)
    print(X_pca)

    import matplotlib.pyplot as plt

    # data = data - data.mean(axis = 0)

    # #计算协方差矩阵
    # X_cov = np.cov(data.T, ddof = 0)

    # #计算协方差矩阵的特征值和特征向量
    # eigenvalues,eigenvectors = eig(X_cov)

    # tot = sum(eigenvalues)
    # var_exp = [(i/tot) for i in sorted(eigenvalues, reverse = True)]
    # cum_var_exp = np.cumsum(var_exp)

    # plt.bar(range(1,5), var_exp, alpha = 0.5, align = 'center', label = 'individual var')
    # plt.step(range(1,5), cum_var_exp, where = 'mid', label = 'cumulative var')
    # plt.ylabel('variance rtion')
    # plt.xlabel('principal components')
    # plt.legend(loc = 'best')
    # plt.show()

    from sklearn.cluster import KMeans
    import pandas as pd

    kmodel = KMeans(n_clusters=3, n_jobs=4)
    kmodel.fit(X_pca)
    
    y_predict = kmodel.predict(X_pca)
    plt.scatter(X_pca[:,0],X_pca[:,1],c=y_predict)
    plt.show()
    print(kmodel.predict((X_pca[:30,:])))
    print(kmodel.calinski_harabaz_score(X_pca,y_predict))
    print(kmodel.cluster_centers_)
    print(kmodel.inertia_)
    print(kmodel.silhouette_score(X_pca,y_predict))