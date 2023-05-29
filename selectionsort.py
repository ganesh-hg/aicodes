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


'''The selectionSort function takes two parameters: array, which is the input array to be sorted, and size, which represents the size of the array.

The outer loop iterates i from 0 to size - 1 (inclusive). This loop selects the minimum element in each iteration and moves it to its correct position.

Inside the outer loop, a variable min is initialized with the value of i. This variable keeps track of the index of the current minimum element.

The inner loop iterates j from i+1 to size (exclusive). This loop compares each element with the current minimum element and updates the min index if a smaller element is found.

If array[j] is smaller than array[min], it means a new minimum element has been found. The min index is updated to j.

After the inner loop finishes, the minimum element has been found for the current iteration of the outer loop. The minimum element is swapped with the element at index i using tuple assignment (array[i], array[min]) = (array[min], array[i]). This places the minimum element in its correct sorted position at the beginning of the array.

The outer loop continues until all elements have been iterated and sorted.

Once the sorting is complete, the sorted array is printed using print(arr).

The code defines an array arr with some initial unsorted elements.

The variable size is assigned the length of the array using len(arr).

The selectionSort function is called with the arr array and size as arguments to sort the array using the Selection Sort algorithm.

Finally, the sorted array is printed using print(arr).

In summary, the code implements the Selection Sort algorithm to sort an array in ascending order. It repeatedly selects the minimum element from the unsorted part of the array and swaps it with the element at the beginning of the unsorted part, gradually building a sorted array.'''
