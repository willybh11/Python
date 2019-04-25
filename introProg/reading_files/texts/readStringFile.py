'''This program demonstrates how to read a file into a string and
create a list from the string

Matt Zipin, 2/17
This will work for text files such as sample.txt.
Lists of numbers, such as num.txt, will not read as a single line
'''

def main():
    x = raw_input("Enter a filename: ")
    f=open(x,"r")   # open for reading only
    line=f.read()   # line is one long string, the entire file
    print line
    A=line.split()  #creates a list called A--default separator is a space
    print A



main()
