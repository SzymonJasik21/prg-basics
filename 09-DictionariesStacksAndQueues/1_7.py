store_inventory = {
    'Laptop': 15,
    'Desktop PC': 10,
    'Monitor': 25,
    'Keyboard': 50,
    'Mouse': 60,
    'External Hard Drive': 30,
    'Printer': 12,
    'Router': 20,
    'USB Flash Drive': 100,
    'Graphics Card': 8
}

total_products = 0

print(f"{'PRODUCT':<20} | {'QUANTITY'}")
print("-" * 32)

for product, quantity in store_inventory.items():
    print(f"{product:<20} | {quantity}")
    total_products += quantity

print("-" * 32)
print(f"Total number of products: {total_products}")