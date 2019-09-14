""" Implementing fibonacci sum recursively"""
count = 0

def recur_fib(n):
    global count
    if n <= 1:
        count += 2
        return n
    else:
        count += 2
        return recur_fib(n-1)+recur_fib(n-2)

fib_no = recur_fib(5)
print(fib_no)
print("Number of steps for program : {}".format(count))
