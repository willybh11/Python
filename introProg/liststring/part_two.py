def directions_2():
    return "\n1) Take in a string. Count the vowels in the string. Count y as a vowel. This is a good time to learn the in operator. Ask me about it or look it up. You can do this in multiple ways.\n2) Input a sting. Count the number of non-space characters. You can do this in ultiple ways as well. Can you do it by counting spaces?\n3) Take in a string Print only the letters in the string, and make them all capital letters. Then make them all small letters.\n4) Use this string for the following program:\n8295815097991628184014892095210417542494818618938024213152859970499140884256647420351285241154616293\na) Print the string above with all eros first, followed by all ones, twos, etc.\nb) Prit the numbers in alphabetical order. So since eight comes before all other numbers, print hte word eight as many times as there are 8's. Then print five, then four, as many times as there are those numbers.\n\n***Problems 1-3 count as 1, and 4 is problem 2***"
def prob1_2():
    line,V,A,t,s = raw_input("This program is #'s 1-3 combined, problem two is actually just the fourth problem.\n\nEnter a string:\n>>>"),["a","e","i","o","u","y"],[],0,0
    for i in range(0,len(line)):
        if line[i] == " ": s += 1
        elif line[i].isalpha(): A.append(line[i])
        for l in range(0,len(V)):
            if line[i] == V[l]: t += 1
        b = "".join(A)
    print "\nThere are",t,"vowels in the string.\nThere are",s,"spaces in the string.\nThere are",(len(line)-s),"non-spaces in the string.\nThe list with only letters is: ",b,"\nWith every letter as a capital that list is: ",b.upper(),"\nWith every letter as a lowercase that list is: ",b.lower(),"\n"
def prob2_2():
    zeros,ones,twos,threes,fours,fives,sixes,sevens,eights,nines,n = 0,0,0,0,0,0,0,0,0,0,"8295815097991628184014892095210417542494818618938024213152859970499140884256647420351285241154616293"
    for i in range(len(n)):
        if n[i] == "0": zeros += 1
        if n[i] == "1": ones += 1
        if n[i] == "2": twos += 1
        if n[i] == "3": threes += 1
        if n[i] == "4": fours += 1
        if n[i] == "5": fives += 1
        if n[i] == "6": sixes += 1
        if n[i] == "7": sevens += 1
        if n[i] == "8": eights += 1
        if n[i] == "9": nines += 1
    print n,"\n\n","0"*zeros,"1"*ones,"2"*twos,"3"*threes,"4"*fours,"5"*fives,"6"*sixes,"7"*sevens,"8"*eights,"9"*nines,"\n\n","eight"*eights,"five"*fives,"four"*fours,"nine"*nines,"one"*ones,"seven"*sevens,"six"*sixes,"three"*threes,"two"*twos,"zero"*zeros
