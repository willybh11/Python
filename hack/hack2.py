from random import *
#why is it so hard to make the matrix
def main():#  [0]=white  [1]=green
    colors = ['\033[0m','\033[32m']
    s = ''
    a = randint(0,84)
    b = randint(0,84)
    c = randint(0,84)
    for i in range(85):
        if i in [a,b,c]:
            s += colors[0]+chr(randint(97,122))+' '
        else:
            s += chr(randint(97,122))+' '
    for i in s:
        print i

main()
