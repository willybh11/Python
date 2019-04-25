
def triangle(inp):
    if len(inp) == 1:
        return inp
    print inp
    output = []
    for i in range(len(inp)-1):
        sum = inp[i] + inp[i+1]
        output.append(sum)
    return triangle(output)

print triangle(range(1,6))