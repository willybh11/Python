def directions_3():
    return "1) Make a secret encoding program that takes in a string and produces a new string that is an offset of some ASCII value added to or subtracted from the original string.\n2) Write a program that can check to see if a given string is a palindrome. Go hang a salami, I'm a lasagna hog! What sorts of issues will you have to deal with in this program?\n3) Input 2 strings and determine whether or not they are anagrams of each other. For example, earthworms and Swarthmore are anagrams of each other because each letter of one exists in the other."
def prob1_3():
    inp,choice,key,output = raw_input("ENTER STRING:\n>>> "),input("ENTER:\n1) Encode\n2) Decode\n>>> "),input("ENTER KEY:\n>>> "),""
    if choice == 1: key -= key*2
    for i in range(len(inp)): output += chr(ord(inp[i])+key)
    return output
def prob2_3():
    x,A,inp = -1,[],raw_input("Enter a palindrome (or not):\n>>> ")
    for i in range(len(inp)):
        if inp[i].isalpha(): A += inp[i]
    for i in range(int(round(len(A)/2))):
        x += 1
        if A[len(A)-1-x].lower() != A[x].lower():
            return "' %s ' is not a palindrome." %(inp)
    return "' %s ' is  a palindrome!" %(inp)
def prob3_3():
    a,b,c,d = raw_input("ANAGRAM TESTER (does not count punctuation/spaces)\nString 1:\n>>> "),raw_input("String 2:\n>>> "),[],[]
    for x in range(97,123):
        for y in range(len(a)):
            if ord(a[y].lower()) == x: c += a[y].lower()
        for y in range(len(b)):
            if ord(b[y]) == x: d += b[y]
    if c == d: return "These strings are anagrams of eachother!"
    return "These strings are NOT anagrams of eachother."
