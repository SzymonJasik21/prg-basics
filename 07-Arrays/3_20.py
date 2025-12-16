def separate_even_odd(array):
    next_even = 0
    n = len(array)
    for current_index in range(n):
        if array[current_index] % 2 == 0:
        
            array[next_even], array[current_index] = array[current_index], array[next_even]
            next_even += 1
    return array 
array = [7,9,2,4,5,6]
print(f"Tablica apoczątkowa: {array}")
separated_array = separate_even_odd(array)
print(f"Tablica po podziale na parzyste i nieparzyste: {separated_array}")