def transpose_matrix(m):
    if not m:
        return []
    R = len(m)
    C = len(m[0])
    
    transposed = [[0 for i in range(R)] for j in range(C)]

    for i in range(R):
        for j in range(C):
            transposed[j][i] = m[i][j]
    return transposed

def print_array(arr):
    for row in arr:
        for element in row:
            print(element,end = "\t")
        print()

matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0],
]
matrix3 = [
    [5,6,7,8]
]

print("Oryginalna macierz 1:")
print_array(matrix1)

print("Oryginalna macierz 2:")
print_array(matrix2)

print("Oryginalna macierz 3:")
print_array(matrix3)

print("=" * 55)

print("\nTransponowana macierz 1 (3x3 -> 3x3):")
transposed1 = transpose_matrix(matrix1)
print_array(transposed1)

print("\nTransponowana macierz 2 (2x5 -> 5x2):")
transposed2 = transpose_matrix(matrix2)
print_array(transposed2)

print("\nTransponowana macierz 3 (1x4 -> 4x1):")
transposed3 = transpose_matrix(matrix3)
print_array(transposed3)


