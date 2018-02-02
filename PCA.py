import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from matplotlib.mlab import PCA
from itertools import cycle

def PCA(Filename):

    a = np.loadtxt(Filename, dtype = "string", delimiter = '\t')
    diseases = a[:,-1]
    uniques, d = np.unique(diseases, return_inverse = True)


    b = np.delete(a, -1, axis=1)
    x_f = b.astype(np.float)
    count = x_f.shape[0]

    mean = np.mean(x_f, axis=0)

    x = x_f - mean
    xT = x.transpose()
    S = np.dot(xT, x)
    S =  float (1)/float(count) * S


    eigvals, eigvectors = LA.eig(S)

    #find two largest eigenvalues and the corresponding eigenvectors
    #Look for something faster than sorting
    max_two = eigvals.argsort()[-2:][::-1]
    #max_two = eigvals.argmax()

    v1 = eigvectors[:,max_two[0]]
    v2 = eigvectors[: ,max_two[1]]

    #to get y1
    y1 = np.dot(v1.transpose(),xT)
    y2 = np.dot(v2.transpose(), xT)
    n = v1.transpose()

    scatters = []

    for dis in range(0, len(uniques)):
        a1 = []
        a2 = []
        for n in range(0, len(d)):
            if(d[n] == dis):
                a1.append(y1[n])
                a2.append(y2[n])
        scatter = plt.scatter(a1, a2, c = np.random.random(5))
        scatters.append(scatter)

    plt.legend(scatters, uniques)
    plt.show()

    U, s, V = np.linalg.svd(x_f, full_matrices=True)


    newdata = V[:,:2]

    newdata_0 = newdata[:,0]
    newdata_1 = newdata[:,1]

    newdata_y0 = np.dot(newdata_0, xT)
    newdata_y1 = np.dot(newdata_1, xT)

    scatters = []

    for dis in range(0, len(uniques)):
        a1 = []
        a2 = []
        for n in range(0, len(d)):
            if(d[n] == dis):
                a1.append(newdata_y0[n])
                a2.append(newdata_y1[n])
        scatter = plt.scatter(a1, a2, c = np.random.random(5))
        scatters.append(scatter)

    plt.legend(scatters, uniques)
    plt.show()

    X_embedded = TSNE(n_components=2).fit_transform(x_f)

    scatters = []

    for dis in range(0, len(uniques)):
        a1 = []
        a2 = []
        for n in range(0, len(d)):
            if(d[n] == dis):
                a1.append(X_embedded[:,0][n])
                a2.append(X_embedded[:,1][n])
        scatter = plt.scatter(a1, a2, c = np.random.random(5))
        scatters.append(scatter)

    plt.legend(scatters, uniques)

    plt.show()


PCA('pca_a.txt')
PCA('pca_b.txt')
PCA('pca_c.txt')
