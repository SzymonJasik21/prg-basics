numbers = [15.5, 3.1, 20.0, 8.75, 4.2, 21.3, 11.0]
while True: 
    user_input = input("Enter value to compare: ")
    try:
        value = float(user_input)
        break
    except ValueError:
        print("Nieprawidłowe wartość. Prosze wpisać inną liczbe")
count = 0 
for number in numbers:
    if number > value:
        count += 1

print("\n--- Wyniki ---")
print(f"Tablica wejściowa: {numbers}")
print(f"Wartość progowa (wprowadzona): {value}")
print(f"Liczba elementów większych od {value}: {count}")    
