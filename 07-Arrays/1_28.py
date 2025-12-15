two_dimensional_array = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

sum_of_last_column = 0
for row in two_dimensional_array:
    last_element = row[-1]
    sum_of_last_column += last_element
print("Sum of the last column: ", sum_of_last_column)
