def indentity_matrix(n):
    matrix = [[0 for j in range (n)]for i in range (n)]

    for i in range (n):
        matrix[i][i] = 1
    return matrix

def print_array(arr):
    for row in arr:
       for element in row:
           print(element, end = "\t")
       print()

n3 = 3
id_matrix_3 = indentity_matrix(n3)
print(f"Macierz jednostkowa {n3}x{n3}:")
print_array(id_matrix_3)

#print("=" * 60)

n5 = 5
id_matrix_5 = indentity_matrix(n5)
print(f"Macierz jednostkowa {n5}x{n5}:")
print_array(id_matrix_5)

#print("=" * 60)

n8 = 8
id_matrix_8 = indentity_matrix(n8)
print(f"Macierz jednostkowa {n8}x{n8}:")
print_array(id_matrix_8)

