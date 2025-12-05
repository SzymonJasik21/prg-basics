###
# Reads from file, line by line
#
#with open('countries.txt', 'r') as file:
 #   for line in file:
  #     print(line, end="")


# print_countries.py
# Odczyt z pliku i numerowanie krajów

with open('countries.txt', 'r') as file:
    for i, line in enumerate(file, start=1):
        print(f"{i}. {line.strip()}")
