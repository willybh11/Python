print '''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is,
3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    '''

def problem():
    sum = 0
    sum_of_sq = 0
    for i in range(1,101):
        sum += i
        sum_of_sq += i**2
    print "sofsq:",sum_of_sq
    print "sqofs:",sum**2
    print "diff :",(sum**2) - sum_of_sq

problem()
