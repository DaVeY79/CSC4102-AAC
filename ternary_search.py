import math

def ternary_search(arr,val,lower,upper):
    lower_mid = math.ceil((lower+upper)/3)
    upper_mid = lower_mid+math.floor((lower+upper)/3)
    while lower < upper:
        if arr[lower_mid] == val:
            return lower_mid
        elif arr[upper_mid] == val:
            return upper_mid
        elif arr[lower_mid] >= val:
            return ternary_search(arr,val,lower,lower_mid)
        elif (arr[low_mid] < val and arr[upper_mid] >= val):
            return ternary_search(arr,val,lower_mid+1,upper_mid)
        else:
            return ternary_search(arr,val,upper_mid+1,upper)
    return -1


a = [2,3,5,6,7,9,11]

print(ternary_search(a,7,0,len(a)-1))
