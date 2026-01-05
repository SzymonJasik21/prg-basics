# Program pobiera temperaturę w stopniach Celsjusza
# Następnie przelicza ją na Kelwiny (dodając 273.15)
# Oraz na stopnie Fahrenheita (mnożąc przez 9/5 i dodając 32)
# Na koniec wyświetla sformatowane wyniki

celsius = float(input('Enter temperature in Celsius: '))

kelvin = celsius + 273.15
fahrenheit = (celsius * 9/5) + 32

print(f"Temperature in Celsius: {celsius}")
print(f"Temperature in Kelvin: {kelvin}")
print(f"Temperature in Fahrenheit: {fahrenheit}")