import math

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a_user = float(input("Enter side a: "))
b_user = float(input("Enter side b: "))
c_user = float(input("Enter side c: "))
print(f"The area of a triangle with sides {a_user}, {b_user}, {c_user} is {triangle_area(a_user, b_user, c_user)}")

area1 = triangle_area(3, 4, 5)
print(f"The area of a triangle with sides 3, 4, 5 is {area1}")

area2 = triangle_area(5, 12, 13)
print(f"The area of a triangle with sides 5, 12, 13 is {area2}")

area3 = triangle_area(7, 24, 25)
print(f"The area of a triangle with sides 7, 24, 25 is {area3}")