price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

total_before = 0
print("--- Before Discount ---")
for item, price in price_list.items():
    print(f"{item:<10}: {price:>6.2f}")
    total_before += price

print(f"Total value before: {total_before:.2f}\n")

total_after = 0
print("--- After 10% Discount ---")
for item, price in price_list.items():
    # Obliczanie nowej ceny i aktualizacja słownika
    new_price = round(price * 0.90, 2)
    price_list[item] = new_price
    
    print(f"{item:<10}: {new_price:>6.2f}")
    total_after += new_price

print(f"Total value after: {total_after:.2f}")