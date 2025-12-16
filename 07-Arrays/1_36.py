def convert_2d_to_1d(array_2d):
    array_1d = []
    for row in array_2d:
        array_1d.extend(row)
    return array_1d
def print_array_1d(arr):
    for element in arr:
        print(element, end = "\t")
    print()

matrix1 = [
    [2,3],
    [1,5]
]
matrix2 = [
    [5, 0, 3, 7, 5],
    [9,0,9,1,2]
]
matrix3 = [
    [2,1],
    [3,5],
    [7,4],
    [2,6]
]

print("Oryginalna macierz 1:")
print(matrix1)
array1d_1 = convert_2d_to_1d(matrix1)
print("Macierz 1 (1D):")
print_array_1d(array1d_1) 
print("-" * 30)

print("Oryginalna macierz 2:")
print(matrix2)
array1d_2 = convert_2d_to_1d(matrix2)
print("Macierz 2 (1D):")
print_array_1d(array1d_2)
print("-" * 30)

print("Oryginalna macierz 3:")
print(matrix3)
array1d_3 = convert_2d_to_1d(matrix3)
print("Macierz 3 (1D):")
print_array_1d(array1d_3)