import re

# Wczytanie danych z klawiatury
username = input("Enter username: ")
password = input("Enter password: ")

# Definicja wzorców (patternów)
# [a-z] - tylko małe litery, {6,} - minimum 6 znaków
username_pattern = r'^[a-z]{6,}$'

# [a-zA-Z0-9_] - litery, cyfry i podkreślnik, {8,} - minimum 8 znaków
password_pattern = r'^[a-zA-Z0-9_]{8,}$'

# Sprawdzenie zgodności
username_match = re.match(username_pattern, username)
password_match = re.match(password_pattern, password)

# Wyświetlenie wyników
if username_match and password_match:
   print("Username and password are valid.")
else:
   if not username_match:
      print("Invalid username! Must be at least 6 lowercase letters.")
   if not password_match:
      print("Invalid password! Must be at least 8 characters (letters, numbers, underscores).")