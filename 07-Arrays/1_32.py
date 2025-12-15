array = [
    [10, 11, 12, 13, 14],
    [20, 21, 22, 23, 24],
    [30, 31, 32, 33, 34]
]
def print_array(arr):
    for row in arr:
        for element in row:
            print(element,end = "\t")
        print()
print("Tablica przed zamianą wierszy:")
print_array(array)

first_row_index = 0
last_row_index = len(array) - 1

array[first_row_index], array[last_row_index] = array[last_row_index], array[first_row_index]

print("\nTablica po zamianie pierwszego (indeks 0) i ostatniego wiersza:")
print_array(array)

