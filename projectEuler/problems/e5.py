print '''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    '''

def problem():
    n = 2520
    while not test5(n): n += 2520
    print n

problem()
