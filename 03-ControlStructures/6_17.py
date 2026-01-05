import datetime

time_input = input("Enter time (24-hour format): ")

time_obj = datetime.datetime.strptime(time_input, "%H:%M")
time_12h = time_obj.strftime("%I:%M%p").lower().lstrip("0")

print(f"Time in 12-hour format: {time_12h}")