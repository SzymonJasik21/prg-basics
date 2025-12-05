countries = [
{"name": "Germany", "population": 83200000},
    {"name": "France", "population": 67800000},
    {"name": "Japan", "population": 125800000},
    {"name": "Canada", "population": 38250000}
]

print("COUNTRY  POPULATION")

for country in countries:
    print(f"{country['name']}   {country['population']}")