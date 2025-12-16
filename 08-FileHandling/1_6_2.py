def read_from_file(name):
   with open(name, 'r') as file:
      content = file.read()
   return content

file_content = read_from_file('countries.txt')
file_lines = file_content.splitlines()

# Oczyszczamy linie: usuwamy numerację z pliku (wszystko przed kropką)
clean_countries = []
for line in file_lines:
    if '.' in line:
        clean_countries.append(line.split('.', 1)[1].strip())
    else:
        clean_countries.append(line.strip())

# Sortujemy czystą listę
sorted_countries = sorted(clean_countries)

# Drukujemy z nową numeracją
for i, country in enumerate(sorted_countries, start=1):
    print(f"{i}. {country}")