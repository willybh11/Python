A = [9,1,7,3,8,4,10,5,6,2] 						# unsorted array

for i in range(len(A)): 						# index of each item, starting at 0

	min_index = i 								# eventual index of smallest VALUE
	for j in range(i+1, len(A)): 				# go through all items AFTER index i
		if A[min_index] > A[j]: 				# if the item is < value at min_index,
			min_index = j 						# set min_index to ITS index
 
	A[i], A[min_index] = A[min_index], A[i]	 	# switch original min_index with smallest item

print(A)										# print sorted array
