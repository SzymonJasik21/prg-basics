numbers = [8, 2, 5, 1, 9]
powers = []

for n in numbers:
    powers.append(n**2)

print("Array:", end=" ")
for n in numbers:
    print(n, end=" ")

print("\n2nd power:", end=" ")
for p in powers:
    print(p, end=" ")