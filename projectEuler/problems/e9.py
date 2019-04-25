print '''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
    '''

def problem():
    for c in range(1,999):
        for b in range(1,c):
            for a in range(1,b):
                if a+b+c == 1000 and a**2 + b**2 == c**2:
                    A = [a,b,c,a*b*c]
    print "a:",A[0]
    print "b:",A[1]
    print "c:",A[2]
    print "a * b * c =",A[3]

problem()
