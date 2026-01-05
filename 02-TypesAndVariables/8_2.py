import math

r = float(input('Enter radius: '))
pi = math.pi

area = pi * r**2
circumference = 2 * pi * r

print(f'r = {r} --> circumference = {circumference:.2f}, area = {area:.2f}')