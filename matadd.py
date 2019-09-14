def matadd(A,B,n):
    res = np.zeros([n,n])
    for i in range(0,n):
        for j in range(0,n):
            res[i,j] = A[i,j]+B[i,j]
    return res
