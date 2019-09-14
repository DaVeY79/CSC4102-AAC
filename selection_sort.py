def selectionSort(arr):
    """ Implementing selection sort"""
    for i in range(0,len(arr)-1):
        min_pos = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_pos]:
                min_pos = j
        if min_pos != i:
            arr[i], arr[min_pos] = arr[min_pos], arr[i]
    return arr

arr = list([5,7,19,12,2,5,1,9,23,42])
print("Original array : {}".format(arr))
sorted_arr = selectionSort(arr)
print("After sorting : {}".format(sorted_arr))
