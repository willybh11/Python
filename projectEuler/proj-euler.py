from extras import *
from time import clock

def main():
    names = ["Multiples of 3 and 5","Even Fibonacci Numbers","Largest Prime Factor","Largest Palindrome Product","Smallest Multiple","Sum Square Difference","10001st Prime","Largest Product in a Series","Special Pythagorean Triplet","Summation of Primes","Largest Product in a Grid"]
    for i in range(len(names)): print str(i+1) + ")" + chr(9) , names[i] 
    filename = "problems/e"+raw_input("\nEnter Problem Number:\n>>> ")+".py"
    start = clock()
    execfile(filename)
    print "That took %f seconds."%(clock()-start)

main()
