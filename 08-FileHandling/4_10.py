import csv

file_name = 'clothing.csv'

with open(file_name, 'r') as file:
    # Używamy DictReader, aby móc odwoływać się do kolumn po nazwach
    reader = csv.DictReader(file)
    
    print(f"{'Product':<25} {'Price':<10} {'Stock':<10}")
    print("-" * 45)
    
    for row in reader:
        # Konwertujemy wartości na liczby, aby móc je porównać
        price = float(row['Price'])
        stock = int(row['Stock'])
        
        # Sprawdzamy oba warunki jednocześnie
        if price < 60 and stock < 40:
            print(f"{row['Name']:<25} {price:<10.2f} {stock:<10}")