array = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

N = len(array)
for i in range(N):
    for j in range(N):
        array[i][j] = (i+1)*(j+1)
    
for row in array:
    for element in row:
            print(f"{element:2}", end = "\t")
    print()
