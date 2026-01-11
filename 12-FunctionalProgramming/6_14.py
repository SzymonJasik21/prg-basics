capacity = 500
tolerance_percent = 2
tolerance_value = capacity * (tolerance_percent / 100)
min_fill = capacity - tolerance_value
max_fill = capacity + tolerance_value

filled_bottles = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]

def is_incorrect(fill):
    return fill < min_fill or fill > max_fill

incorrect_bottles = list(filter(is_incorrect, filled_bottles))
incorrect_percentage = (len(incorrect_bottles) / len(filled_bottles)) * 100

print(f"Bottle capacity:    {capacity}ml")
print(f"Filling tolerance:  {tolerance_percent}%")
print(f"Filled bottles:     {', '.join(map(str, filled_bottles))}")
print(f"Incorrectly filled: {int(incorrect_percentage)}%")