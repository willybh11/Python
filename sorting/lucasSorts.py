import random
import os
from time import *


def selection_sort(Array):
    for j in range(len(Array)-1):
        iMin = j
        for i in range(j+1, len(Array)):
            if Array[i] < Array[iMin]:
                iMin = i
        if iMin != j:
            Array[j], Array[iMin] = Array[iMin], Array[j]

    return(Array)


def bubble_sort(Array):
    n = len(Array)
    for j in range(1, n):
        for i in range(0, n-1):
                if (Array[i + 1] < Array[i]):
                    Array[i + 1], Array[i] = Array[i], Array[i + 1]
    return(Array)


def quick_sort(A):
    quick_sort2(A, 0, len(A)-1)
    return(A)


def quick_sort2(A, low, hi):
    if low < hi:
        p = partition(A, low, hi)
        quick_sort2(A, low, p-1)
        quick_sort2(A, p+1, hi)

    return(A)


def get_pivot(A, low, hi):
    mid = (hi + low) // 2
    pivot = hi
    if A[low] < A[mid]:
        if A[mid] < A[hi]:
            pivot = mid
    elif A[low] < A[hi]:
        pivot = low
    return(pivot)


def partition(A, low, hi):
    pivotIndex = get_pivot(A, low, hi)
    pivotValue = A[pivotIndex]
    A[pivotIndex], A[low] = A[low], A[pivotIndex]
    border = low

    for i in range(low, hi+1):
        if A[i] < pivotValue:
            border += 1
            A[i], A[border] = A[border], A[i]
    A[low], A[border] = A[border], A[low]

    return(border)


def main():
    stay = True
    while stay:
        os.system("clear")
        choice = input("OPTIONS:\n1: random list\n2: input list\n3: quit\n\nChoice: ")
        while choice not in ["1", "2", "3"]:
            print("please try again")
            choice = input("OPTIONS:\n1: random list\n2: input list\n\nChoice: ")

        Array = []
        items = 1000000

        if choice == "1":
            for i in range(items):  # random.randint(1, 30)
                Array.append(random.randint(1, items))
        elif choice == "2":
            temp = input("your Array (numbers separated by spaces):\n")
            temp = temp.split(" ")
            for i in temp:
                if i.isdigit():
                    Array.append(int(i))
        else:
            stay = False
        if stay:
            sort_alg = input("\nWhich sorting algorithm would you like to use?\n1: Bubble Sort\n2: Selection Sort\n3: Quick Sort\n\nChoice: ")
            while choice not in ["1", "2", "3"]:
                print("please try again")
                sort_alg = input("Which sorting algorithm would you like to use?\n1: Bubble Sort\n2: Selection Sort\n3: Quick Sort\n\nChoice: ")

            # print("\n\nUnsorted Array:", Array)
            if sort_alg == "1":
                time1 = clock()  # start time
                sArray = bubble_sort(Array)
                finalTime = clock() - time1  # end timer
            elif sort_alg == "2":
                time1 = clock()  # start time
                sArray = selection_sort(Array)
                finalTime = clock() - time1  # end timer
            else:
                time1 = clock()  # start time
                sArray = quick_sort(Array)
                finalTime = clock() - time1  # end timer
            # print("\nSorted Array:", sArray)
            print("\nSorted", items, "items in", finalTime, "seconds")

            time = clock()
            Array.sort()
            finalTime = clock() - time

            print("Python took ", finalTime, "seconds")

            input("press ENTER to continue")


main()
