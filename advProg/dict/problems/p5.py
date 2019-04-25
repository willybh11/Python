def main(): #ascending/descending
    dic1 = {"cat":"CAT", "dog":"DOG", "fish":"FISH", "bird":"BIRD"}

    print "Ascending:"
    ascending = []
    for i in dic1:
        ascending.append(i)
    print ascending[::-1]

    print "Descending:"
    descending = []
    for i in dic1:
        descending.append(i)
    print descending

main()
