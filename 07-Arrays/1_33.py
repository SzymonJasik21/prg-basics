array = [
    [10, 11, 12, 13, 14],
    [20, 21, 22, 23, 24],
    [30, 31, 32, 33, 34]
]

def print_array(arr):
    for row in arr:
        for element in row:
            print(element, end = "\t")
        print()
print("Tablica przed zamianą kolumn")
print_array(array)

first_column_index = 0
last_column_index = len(array[0]) - 1

for row in array:
    row[first_column_index], row[last_column_index] = row[last_column_index],row [first_column_index]
print("\nTablica po zamianie pierwszej (indeks 0) i ostatniej kolumny:")
print_array(array)

