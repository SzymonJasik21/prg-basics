def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

array1 = [64, 34, 25, 12, 22, 11, 90]
array2 = [5, 1, 4, 2, 8]
array3 = [10, -2, 0, 33, 7, 1]

print("Array 1 (Sorted):", bubblesort(array1))
print("Array 2 (Sorted):", bubblesort(array2))
print("Array 3 (Sorted):", bubblesort(array3))