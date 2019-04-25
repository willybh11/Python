def mergeSort(A):                                   # must be a function: Merge Sort is recursive
    if len(A) > 1:                                  # arrays should not be split past 2
        midpoint = len(A) // 2                      # floored midpoint of array
        L = mergeSort(A[:midpoint])                 # recursively sort left half of array
        R = mergeSort(A[midpoint:])                 # recursively sort right half of array

        indexL,indexR,indexA = 0,0,0                # using variables instead of a for loop gives necessary flexibility

        while indexL < len(L) and indexR < len(R):  # run through entire half
            if L[indexL] < R[indexR]:               # if left side < right side, 
                A[indexA] = L[indexL]               # put left side back into full array
                indexL += 1                         # add 1 so we can continue iterating through L
            else:                                   # right side > left side
                A[indexA] = R[indexR]               # put right side back into full array
                indexR += 1                         # continue iterating through R
            indexA += 1                             # continue iterating through A
		
        while indexL < len(L):                      # we finished either L or R, now we have to clean up the rest
            A[indexA] = L[indexL]                   # add value to main array
            indexL += 1                             # continue iterating through L
            indexA += 1                             # continue iterating through A
		
        while indexR < len(R):                      # make sure R is finished
            A[indexA] = R[indexR]                         
            indexR += 1
            indexA += 1

    return A                                        # return sorted list (may be a sublist)
print mergeSort([9,1,7,3,8,4,10,5,6,2])
