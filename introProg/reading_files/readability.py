def main():
    filename = raw_input("Enter Filename:\n>>> ")
    f = open(filename,"r")
    oneline = f.read()
    words = oneline.split()
    avg = 0
    for i in words:
        x = ""
        for y in i:
            if y.isalpha():
                x += y
        avg += len(i)
    avg = float(avg)/len(words)
    print "The average word length is",round(avg),", but the exact average is",avg,"."
main()
