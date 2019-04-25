import time

def oneline(array):
    return array if len(array) < 2 else quicksort([i for i in array[1:] if i <= array[0]]) + [array[0]] + quicksort([i for i in array[1:] if i > array[0]])

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

print oneline([10, 5, 2, 3])
