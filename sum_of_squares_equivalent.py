def isSOSEqual(n):
    sum = 0
    ori  = n
    while n>0:
        d = n%10
        sum += d**2
        n = int(n/10)
    return True if sum == 1 else False

if isSOSEqual(n):
    print("{} is equal to sum of squares of its digits {}".format(n,digits))
else:
    print("{} is not equal to sum of squares of its digits {}".format(n,digits))

print(happy_nos)
