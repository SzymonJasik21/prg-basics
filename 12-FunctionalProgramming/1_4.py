ms_to_kmh = lambda ms: ms * 3.6

test_values = [10, 35]

for v in test_values:
    print(f"{v} m/s = {int(ms_to_kmh(v))} km/h")