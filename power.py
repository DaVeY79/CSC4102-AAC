""" Write an algorithm to computer x^n """
import time
start_time = time.time()
#x = int(input("Enter value of x : "))
#n = int(input("Enter value of n : "))
def power(x,n):
    pow = x
    if n == 0:
        return 1
    elif n == 1:
        return pow
    else:
        for i in range(1,n):
            pow *= x
    return pow

print("{}^{} is = {}".format(10,24,power(10,24)))
print("Time taken for brute force power computation %s seconds" % (time.time() - start_time))
