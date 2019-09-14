""" Brute force approach for computing factorial of a number"""
import time
start_time = time.time()

def factorial(x):
    fact= x
    for i in range(x-1,1,-1):
        fact *= i
    print(fact)

factorial(5)
print("Time taken for factorial %s seconds" % (time.time() - start_time))
