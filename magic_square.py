import numpy as np

def magic_square(dim):
    arr = np.array([[np.nan]*dim]*dim)
    magic_mat = fill_magic_square(arr,val = 1,x = 0, y = dim // 2)
    return magic_mat

def fill_magic_square(arr,val,x,y):
    if np.isnan(arr).any() == False:
        return arr
    else:
        x,y = set_circular_coord(x, arr,axis = 0),set_circular_coord(y, arr, axis = 1)
        if np.isnan(arr[x,y]) == False:
            x,y = set_circular_coord(x+2, arr, axis = 0), set_circular_coord(y+1, arr, axis = 1)
        arr[x,y] = val
        val = val+1
        return fill_magic_square(arr,val,x-1,y-1)

def set_circular_coord(x, arr, axis):
    x = x%arr.shape[axis]
    if x < 0:
        return arr.shape[axis]+x
    elif x >= arr.shape[axis]:
        return arr.shape[axis]-x
    else:
        return x

a = magic_square(3)
print(a)
