def create_2d_arr(x,y):
    two_dimensional_array = [[0 for column in range (y)] for rown in range(x)]
    return two_dimensional_array
rows = 3
collumns = 5
my_array = create_2d_arr(rows,collumns)

for row in my_array:
    for element in row:
        print(element, end = "\t")
    print()
