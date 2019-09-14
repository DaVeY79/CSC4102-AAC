""" Program to check if a number is equal to the sum of its divisors"""

def factors(n):
    """input : integer
       return : list of divisors of integer"""
    factorlist = []
    for i in range(2,n/2):
        if n%i == 0:
            factorlist.append([i,n/i])
    factorlist.append([1,n])
    return factorlist

def check_div_sum(n):

    factorlist = factors(n)
    if n == sum(factorlist):
        print("{} is a sum of its factors {}".format(n,factorlist))
    else:
        print("{} is not the sum of its factors {}".format(n,factorlist))
