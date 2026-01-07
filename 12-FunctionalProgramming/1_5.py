def avg_speed(distance, hours, minutes):
    total_hours = hours + (minutes / 60)
    return round(distance / total_hours, 1)

distance = float(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))

result = avg_speed(distance, hours, minutes)

print(f"Average speed: {result} km/h")