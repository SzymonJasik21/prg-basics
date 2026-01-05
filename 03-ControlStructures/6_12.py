number_of_products = int(input("Number of products purchased: "))
product_price = float(input("Product price: "))

if number_of_products > 2:
    discounted_products = number_of_products - 2
    full_price_products = 2
    
    amount_to_pay = (full_price_products * product_price) + (discounted_products * product_price * 0.75)
else:
    amount_to_pay = number_of_products * product_price

print(f"Amount to pay: {amount_to_pay:.2f}")