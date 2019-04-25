
import time
def main():
    #filename = raw_input("Enter Filename:\n>>> ")
    f = open('texts/twain.txt',"r")
    d = open("texts/words.txt","r")
    dictionary = d.read().split("\n")
    wordlist = f.read()
    wordlist = wordlist.replace("-"," ")
    wordlist = wordlist.split()
    for x in range(0,len(wordlist)):
        for i in range(len(wordlist[x])):#this for loop checks if every
            if not wordlist[x][i].isdigit():          #character is a digit
                break
            if i == len(wordlist)-1:
                wordlist[x] = "yes"
        for i in range(10):
            wordlist[x] = wordlist[x].strip(",").strip(".").strip("`").strip(";").strip("'")
    errors = []
    start = time.clock()
    print "total length will be",len(wordlist)
    for y in range(0,len(wordlist)):
        x = wordlist[y]
        if not (x.lower() in dictionary):
            errors.append(x)
        if y%1000==0:
            print "I'm at",y
    d.close()
    f.close()
    print len(errors),"Errors:\n",errors
    print "This program took",time.clock()-start,"seconds to run."

main()
