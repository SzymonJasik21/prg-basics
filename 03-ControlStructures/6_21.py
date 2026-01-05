amount = int(input("Enter the amount in PLN: "))

remaining = amount
five_pln = remaining // 5
remaining %= 5

two_pln = remaining // 2
remaining %= 2

one_pln = remaining

print(f"The amount of PLN {amount} in coins:")
print(f"5 PLN coins: {five_pln}")
print(f"2 PLN coins: {two_pln}")
print(f"1 PLN coins: {one_pln}")