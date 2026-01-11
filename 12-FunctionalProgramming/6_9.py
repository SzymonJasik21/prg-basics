temperatures = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

positive_stations = filter(lambda item: item[1] > 0, temperatures.items())

city_names = [item[0] for item in positive_stations]

print(f"Cities with positive temperatures: {' '.join(city_names)}")