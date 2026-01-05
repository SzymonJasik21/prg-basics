for row in range(1, 8):
    for col in range(7):
        number = row + (col * 7)
        print(f"{number:<2}", end=" ")
    print()