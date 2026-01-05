price = float(input('Enter price: '))
discount_percentage = float(input('Enter discount %: '))

reduction = price * (discount_percentage / 100)
price_with_discount = price - reduction

print(f"Enter price: {price:.2f}")
print(f"Enter discount %: {discount_percentage:.0f}")
print(f"Price with discount: {price_with_discount:.2f}")
print(f"Reduction: {reduction:.2f}")