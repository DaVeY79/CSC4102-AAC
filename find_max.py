from quicksort import qsort

arr = [2,1,3,7,4,5,14,27,11]
sorted_arr = qsort(arr)
max = sorted_arr.pop()

print("The maximum value in the list is {}".format(max))
