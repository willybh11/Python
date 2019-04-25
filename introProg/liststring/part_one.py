from random import *
def directions_1():
        return "\n1) Input a series of numbers. Put them in a list. Find the average of the series, print the series and then print each number, both on one line and one line at a time.\n2) Create a list of 20 random numbers, from 1-100. Print all of the odd numbers. Print the highest even number.\n3) Create a new list of 50 random numbers, from 1-50. Does 27 exist in the list? How many times? Run this multiple times. Write code to determine the frequency of 27, then print the list and look carefully to verify your answer. Can you do this in multiple ways? What would make it easier to check your answer?\n4) Create a new list of 101 random numbers, from 1-1000. Determine the median value in the list. Why did I specify 101 numbers for this task?"
def prob1_1():
    A,s = [],0
    for i in range(5): A.append(input("Enter a number: "))
    for i in range(len(A)): s += A[i]
    avg = s/5.0
    print "The avg is:",avg,"\n\n",A,"\n\nThe individual numbers are:"
    for i in range(len(A)): print A[i]
def prob2_1():
    A,O,E,max=[],[],[],0
    for i in range(20):
        num = randint(1,101)
        if num%2 != 0: O.append(num)
        else: E.append(num)
    for i in range(len(E)):
        if max < E[i]: max = E[i]
    print "Twenty numbers were generated.\nOdds:\n",E,"\nThe highest even number was:",max
def prob3_1():
    A,t = [],0
    for i in range(50):
        A.append(randint(1,51))
        if A[int(len(A))-1] == 27: t += 1
    print A,"\n\nNumber of times 27 appeared:",t
def prob4_1(): #You asked why you asked for 101 numbers...\nIt's because if you name the list A, you print A[51] ;)
    A = []
    for i in range(101): A.append(randint(1,1001))
    A.sort()
    print A,"\n",A[51]
