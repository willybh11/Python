def main():
    pnums = []
    cnums = []
    avg2 = 0
    firstFive = []
    i = 0
    avg = 0
    for x in range(1,1001):
        pnums.append(x)
        cnums.append(0)
    f = open("nums.txt","r")
    oneline = f.read()
    nums = oneline.split("\n")
    del nums[len(nums)-1]
    for x in nums:
        print x
        avg += int(x)
        if nums.index(x) < 50 or nums.index(x) > 100:
                avg2 += int(x)
        for y in pnums:
            if int(x) == y:
                cnums[pnums.index(y)] += 1
    while len(firstFive) < 5:
        i += 1
        if int(nums[i]) % 31 == 0:
            firstFive.append(int(nums[i]))
    avg = avg/len(nums)
    avg2 = avg2/len(nums)
    print "\nThe average of the numbers is:",avg
    print "The most common number is:",pnums[cnums.index(max(cnums))]
    print "It occurred %i times." %(max(cnums))
    print "The first five numbers divisible by 31 are:",firstFive
    print "If the 50th-100th lines are removed, the new average is:",avg2
main()
