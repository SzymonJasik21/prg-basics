hours = int(input('Enter the number of hours: '))

if hours >= 1 and hours <= 2:
    fee = 5
elif hours >= 3 and hours <= 6:
    fee = 15
elif hours > 6:
    fee = 20
else:
    fee = 0

print(f'The parking fee is: {fee} PLN')