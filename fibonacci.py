def fibonacci(n):
    a = 0
    b = 1
    print(str(a)+","+str(b),end=',')
    for i in range(n-1):
        c = a+b
        a = b
        b = c
        print(str(c),end=',')
