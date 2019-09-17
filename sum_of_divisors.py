""" Program to check if a number is equal to the sum of its divisors"""

def factors(n):
    """input : integer
       return : list of divisors of integer"""
    factorlist,i,ori_n,n = [],2,n,int(n/2)
    while i < n:
        if ori_n%i == 0:
            factorlist += [i,int(ori_n/i)]
            n = int(ori_n/i)
        i += 1
    factorlist += [1,ori_n]
    return factorlist

def check_div_sum(n):
    factorlist = sorted(factors(n))
    if n == sum(factorlist):
        print("{} is a sum of its factors {}".format(n,factorlist))
    else:
        print("{} is not the sum of its factors {}".format(n,factorlist))

check_div_sum(1136)
