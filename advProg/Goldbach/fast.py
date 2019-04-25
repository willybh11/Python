from time import clock
from math import sqrt

# runs in < 0.007 seconds!!

def main():
    n = 3
    while 1:
        n += 2
        for square in xrange(int( sqrt(n/2) ), -1, -1):
            possiblePrime = n - 2*square**2
            for possibleFactor in xrange(3, int( sqrt(possiblePrime) + 1 ), 2):
                if possiblePrime % possibleFactor == 0: break
            else: break
        else: break

    # print 'Answer:',n

start = clock()
for i in range(100):
    main()
print 'Average: %.4f seconds' %((clock()-start) / 100)
