A = [9,1,7,3,8,4,10,5,6,2] 					# unsorted array

for i in range(len(A)):                     # for each index
    for j in range(0, len(A)-i-1):          # the largest item will end up on the far right of the array, so we can ignore it on sequential pass-throughs
        if A[j] > A[j+1]:                   # if val at j > the next,
            A[j], A[j+1] = A[j+1], A[j]     # swap them.

print A