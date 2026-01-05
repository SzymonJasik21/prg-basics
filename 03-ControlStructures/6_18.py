x = float(input("x = "))
y = float(input("y = "))

if x > 0 and y > 0:
    position = "is in the first quadrant of the coordinate system"
elif x < 0 and y > 0:
    position = "is in the second quadrant of the coordinate system"
elif x < 0 and y < 0:
    position = "is in the third quadrant of the coordinate system"
elif x > 0 and y < 0:
    position = "is in the fourth quadrant of the coordinate system"
elif x == 0 and y == 0:
    position = "is located in the position (0,0) of the coordinate system"
elif x == 0:
    position = "is on the Y axis"
else:
    position = "is on the X axis"

print(f"Point P({x},{y}) {position}")