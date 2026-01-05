import random

dice_roll_1 = random.randint(1, 6)
dice_roll_2 = random.randint(1, 6)
dice_roll_3 = random.randint(1, 6)

total = dice_roll_1 + dice_roll_2 + dice_roll_3

print(f"Roll 1: {dice_roll_1}")
print(f"Roll 2: {dice_roll_2}")
print(f"Roll 3: {dice_roll_3}")
print(f"Total sum: {total}")