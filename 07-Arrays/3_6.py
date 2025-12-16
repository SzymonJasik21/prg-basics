numbers = [15, 8, 31, 47, 2, 19]

total_sum = 0
index = 0

while index < len(numbers):
    total_sum += numbers[index]
    index += 1

mean = total_sum / len(numbers)

print("Array:", end=" ")
for n in numbers:
    print(n, end=" ")

print(f"\nArithmetic mean: {mean:.2f}")