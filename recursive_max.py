def recur_max(arr,n,maxim):
    if n<0:
        return maxim
    else:
        if arr[n] > maxim:
            maxim = arr[n]
    return recur_max(arr,n-1,maxim)

arr = [100034,12,997,45,21,76,123,27,789,98,99]
print(recur_max(arr,len(arr)-2,arr[-1]))
