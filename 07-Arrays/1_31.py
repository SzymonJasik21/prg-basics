array = [
    [-38, 19], 
    [5, 40],
    [-7, 11],
    [29, 16]
]
min_value = array[0][0]
max_value = array[0][0]

min_row, min_column = 0,0
max_row, max_column = 0,0

R = len(array)
C = len(array[0])


# R - ROW
for i in range(R):
    for j in range(C):
        current_value = array[i][j]
        if current_value < min_value:
            min_value = current_value
            min_row = i
            min_column = j
        if current_value > max_value:
            max_value = current_value
            max_row = i
            max_column = j

print(f"Min value: {min_value}")
print(f"Minimum postion: Row {min_row}, Column {min_column}")
print(f"Max value: {max_value}")
print(f"Maximum postion: Row {max_row}, Column {max_column}")

