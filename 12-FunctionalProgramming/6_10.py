import matplotlib.pyplot as plt

data = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

sorted_items = sorted(data.items(), key=lambda item: item[1])

cities = list(map(lambda x: x[0], sorted_items))
temperatures = list(map(lambda x: x[1], sorted_items))

plt.bar(cities, temperatures, color='skyblue')
plt.title("Temperatures in Polish Cities")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")

plt.savefig('temperatures_chart.png')