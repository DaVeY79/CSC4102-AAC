"""Write a recursive algorithm to compute factorial of a number"""
import time
#start_time = time.time()
count = 0
def fact(x):
    global count
    if x == 2:
        count += 2
        return 2
    else:
        count += 2
        return x*fact(x-1)

fac = fact(10)
print(fac)
#print("Time taken for recursive factorial %s seconds" % (time.time() - start_time))
print("Time taken for recursive factorial %s steps" %count)
