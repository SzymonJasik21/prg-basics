def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
bank_transactions = [510.50, 25.00, -33.00, 15.75, 5.00, -100.20, 12.00, 8.40, 30.00, -22.10, 18.00]
piles_of_blocks = [100, 50, 200, 500, 20, 150, 300, 40, 80, 120]

print("1. Zużycie paliwa (oryginalne):", car_fuel_consumption)
bubble_sort(car_fuel_consumption)
print("1. Zużycie paliwa (posortowane):", car_fuel_consumption)

print("-" * 30)

print("2. Transakcje bankowe (oryginalne):", bank_transactions)
bubble_sort(bank_transactions)
print("2. Transakcje bankowe (posortowane):", bank_transactions)

print("-" * 30)

print("3. Stosy klocków (oryginalne):", piles_of_blocks)
bubble_sort(piles_of_blocks)
print("3. Stosy klocków (posortowane):", piles_of_blocks)