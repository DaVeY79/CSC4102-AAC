def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[int(len(arr)/2)]
        lower = [i for i in arr if i < pivot]
        higher = [i for i in arr if i > pivot]
        return qsort(lower)+[pivot]+qsort(higher)

if __name__ == "__main__":
    arr = [2,1,3,7,4,5,14,27,11]
    print("Array is {}".format(arr))
    sorted_arr = qsort(arr)
    print("Sorted array is {}".format(sorted_arr))
