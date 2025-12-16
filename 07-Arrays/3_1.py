numbers = [34, 7, 19, 4, 21, 8]

even_count = 0
index = 0

while index < len(numbers):
    if numbers[index] % 2 == 0:
        even_count += 1
    index += 1

print("Array: 34, 7, 19, 4, 21, 8")
print("Number of even values:", even_count)