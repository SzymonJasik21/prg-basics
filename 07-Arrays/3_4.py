numbers = [-15, 8, -31, 47, -2, 19]

min_val = numbers[0]
max_val = numbers[0]

for num in numbers:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num

print("Array:", numbers)
print("Minimum number:", min_val)
print("Maximum number:", max_val)