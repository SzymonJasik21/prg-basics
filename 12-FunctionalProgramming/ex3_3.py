stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]

print(f"Product in stock: {stock}")

sum_value = sum(map(lambda x : x[0]*x[1], stock))
print(f"Sum value: {sum_value:.2f} ")

