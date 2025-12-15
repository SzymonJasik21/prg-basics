two_dimensional_array = [
    [10,15,20,25],
    [15,30,45,60]
]
R = len(two_dimensional_array)
C = len(two_dimensional_array[0])

for i in range (R):
    for j in range (C):
        print(two_dimensional_array[i][j], end = "\t")

    print()

