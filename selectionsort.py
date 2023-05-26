def selectionSort(array, size):
    for i in range(size):
        min = i
        for j in range(i+1, size):
            if array[j] < array[min]:
                min = j
        (array[i], array[min]) = (array[min], array[i])
 
arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)