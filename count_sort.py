def countsort(A):
    k = max(A)
    n = len(A)
    #A = [None,*A]
    B = ([0]*(n+1))
    C = ([0]*(k+1))
    for i in range(0,n):
        C[A[i]] = C[A[i]]+1
    for i in range(1,k+1):
        C[i] = C[i]+C[i-1]
    for i in range(n-1,-1,-1):
        B[C[A[i]]] = A[i]
        C[A[i]] = C[A[i]] - 1
    return B[1:]

def radixcountsort(arr,exp):
    n = len(arr)
    output=[0]*n
    count=[0]*10
    for i in range(0, n):
        index=int(arr[i]/exp)
        count[index%10] = count[index%10]+1

    for i in range(1,10):
        count[i] = count[i]+count[i-1]

    for i in range(n-1,-1,-1):
        index=int(arr[i]/exp)
        output[count[index%10]-1] = arr[i]
        count[index%10] = count[index%10]-1

    return output


if __name__ == "__main__":
    A = [4,2,1,3,1,2,1,3]
    print(countsort(A))
    #print(radixcountsort(A,1))
