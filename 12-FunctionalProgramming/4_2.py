speeds = [48, 47, 54, 50, 42, 68, 39, 46]

too_fast = list(filter(lambda s: s > 50, speeds))

print("Recorded values:", ", ".join(map(str, speeds)))
print("Speed too high:", ", ".join(map(str, too_fast)))