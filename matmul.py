def matmul(A,B,n):
    for i in range(0,n):
        for j in range(0,n):
            res[i,j] = 0
            for k in range(0,n):
                res[i,j]+=A[i,k]*B[k,j]
    return res
