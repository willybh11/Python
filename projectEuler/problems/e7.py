print '''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
    '''

def problem():
    x,limit = 1,0
    while limit != 10001:
        x += 1
        if isprime(x): limit += 1
    print x

problem()
