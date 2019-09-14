def binary_search(arr,val,lower,upper):
    mid = (lower+upper)/2
    while lower < upper :
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            return binary_search(arr,val,lower,mid)
        else:
            return binary_search(arr,val,mid,upper)
    return -1
