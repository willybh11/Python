def main():
    filename = raw_input("Enter Filename:\n>>> ")
    f = open(filename,"r")
    oneline = f.read()
    by_line = oneline.split("\n")
    by_word = oneline.split()
    by_letter = []
    for x in oneline:
        by_letter.append(x)
    print " ".join(by_line[::-1]),"\n"
    print " ".join(by_word[::-1])
    print " ".join(by_letter[::-1])
main()
