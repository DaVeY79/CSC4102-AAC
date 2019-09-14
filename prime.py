def isPrime(n):
    count = 0
    for i in range(2,n):
        if n%i == 0:
            count += 1
            break
    return False if count else True

n = 17
print("{} is prime".format(n)) if isPrime(n) else print("{} is not prime".format(n))
