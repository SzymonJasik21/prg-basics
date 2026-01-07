is_even = lambda number: number % 2 == 0

test_numbers = [2, 7, 10, 15, 22]

for n in test_numbers:
    result = is_even(n)
    print(f"Is {n} even? {result}")

user_input = int(input("Enter a number to check: "))
print(f"Result for {user_input}: {is_even(user_input)}")