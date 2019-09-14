"""Write a divide-and-conquer approach to calculate x^n""""
import time
start_time = time.time()

def power(x,n):
    if n == 1:
        return x
    temp = power(x,round(n/2))
    if n%2 == 0:
        return temp*temp
    else:
        return x*temp*temp

# def power(x,n):
#     while n > 0:
#         #temp = power(x,round(n/2))
#         if n%2 == 0:
#             return temp*temp
#         else:
#             return x*temp*temp
#         n = round(n/2)


#x = int(input("Enter value of x : "))
#n = int(input("Enter value of n : "))
print("{}^{} is = {}".format(10,24,power(10,24)))
print("Time taken for divide and conquer power computation %s seconds" % (time.time() - start_time))
