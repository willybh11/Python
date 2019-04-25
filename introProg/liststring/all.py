from part_one import *
from part_two import *
from part_three import *
def main():
    part = input("Part One: numerical list exercises.\nPart Two: using strings as lists; working with characters.\nPart Three: encoding/decoding, palindromes, anagrams.\n\nPart Number:\n>>> ")
    if part == 1:
        print directions_1()
        problem = input("\nProblem Number:\n>>> ")
        if problem == 1: prob1_1()
        if problem == 2: prob2_1()
        if problem == 3: prob3_1()
        if problem == 4: prob4_1()
    if part == 2:
        print directions_2()
        problem = input("\nProblem Number:\n>>> ")
        if problem == 1: prob1_2()
        if problem == 2: prob2_2()
        if problem == 3: prob3_2()
        if problem == 4: prob4_2()
    if part == 3:
        print directions_3()
        problem = input("\nProblem Number:\n>>> ")
        if problem == 1: print prob1_3()
        if problem == 2: print prob2_3()
        if problem == 3: print prob3_3()
main()
