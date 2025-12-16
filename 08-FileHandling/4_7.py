import re

# Pobranie tekstu od użytkownika
text = input("Enter text: ")

# Definicja wzorca dla samogłosek
# [aeiouy] - zestaw znaków, których szukamy
vowels_pattern = r'[aeiouy]'

# Wykorzystanie re.findall do znalezienia wszystkich wystąpień
# re.IGNORECASE sprawia, że program zliczy zarówno 'a' jak i 'A'
vowels_found = re.findall(vowels_pattern, text, re.IGNORECASE)

# Liczba samogłosek to długość listy znalezionych elementów
count = len(vowels_found)

print(f"The number of vowels in the text is: {count}")