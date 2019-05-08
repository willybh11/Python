F,s = [0,1],0
while F[len(F)-1] < 4000000:
    F.append(F[len(F)-1]+F[len(F)-2])
    if F[len(F)-1]%2 == 0: s += F[len(F)-1]

print(s)