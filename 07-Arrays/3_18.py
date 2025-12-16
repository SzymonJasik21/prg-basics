import EX318

numbers = [7, 3, 8, 5, 2]

print("Numbers:", ", ".join(map(str, numbers)))

second_largest = EX318.get_second_largest(numbers)
print(f"Second largest number: {second_largest}")

median = EX318.get_median(numbers)
print(f"Median: {median}")

min_max = EX318.get_min_max(numbers)
print(f"Smallest and largest number: {min_max[0]},{min_max[1]}")

numbers_string = EX318.to_string_with_minus(numbers)
print(f"Numbers as a string: {numbers_string}")