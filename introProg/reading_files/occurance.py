import time
def main():
    filename = raw_input("Enter Filename:\n>>> ")
    start = time.clock()
    f = open(filename,"r")
    end = False
    A = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    B = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    while end == False:
        l = f.readline()
        for i in range(len(l)):
            for x in A:
                if l[i].lower() == x:
                    B[A.index(x)] += 1
        if len(l) == 0:
            end = True
    f.close()
    for i in range(len(A)):
        print A[i],":",B[i]
    print "\nThis program took %f seconds to calculate." %(time.clock()-start)
main()
