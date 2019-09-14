def insertion_sort(values):
    for i in range(1,len(values)):
        item = values[i]
        j = i-1
        while((item < values[j]) and (j >= 0)):
            values[j+1] = values[j]
            j = j - 1
        values[j+1] = item
    return values

values = [16,14,12,10,8,3,17,12]
print(insertion_sort(values))
