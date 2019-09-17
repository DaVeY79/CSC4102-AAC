def bubblesort(a):
    n = len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

nos_list = [16,14,12,10,8,3,17,12]
print(bubblesort(nos_list))
