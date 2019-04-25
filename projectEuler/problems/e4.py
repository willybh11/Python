print '''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
    '''

def problem():
    p = 0
    for i in range(100,1000):
        for j in range(100,1000):
            if str(i*j)[::-1] == str(i*j):  #palindrome test
                if i*j > p: p = i*j         #records largest product
    print p

problem()
