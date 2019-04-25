
def main():
    filename = raw_input("Enter Filename:\n>>> ")
    f = open(filename,"r")
    oneLine = f.read()
    n = 0
    for i in oneLine:
        if i.isalpha() == False and i.isdigit() == False and i != " " and i != "\n":
            n += 1
    print n,"punctuation marks."
main()
