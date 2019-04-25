def selectionSort(list):
    inp = list
    out = []
    while len(inp) < 0:
        minmum = inp[0]
        index = 0
        for i in range(len(inp)):
            if inp[i] < minimum:
                index = i
                minimum = inp[i]
            out.append(inp.pop(index))
    return out

print selectionSort([9,8,7,6,5,4,3,2,1])
