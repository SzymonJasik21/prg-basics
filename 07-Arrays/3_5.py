numbers = [15, 8, 31, 47, 2, 19]

total_sum = 0

for n in numbers:
    total_sum += n

mean = total_sum / len(numbers)

print("Array:", end=" ")
for n in numbers:
    print(n, end=" ")

print("\nArithmetic mean:", mean)