print '''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
    '''

def problem():
    limit = input("What number should I go up to?\n>>> ")
    maybeFactors = primeRange(int(limit**0.5)+1)
    s = 2
    for i in range(3,limit,2):
        if factorPtest(maybeFactors,i):
            s += i
    print "The sum of primes up to",limit,"is:",s

problem()
