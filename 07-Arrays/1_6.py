def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n-1]

# Test the function with day numbers 1, 4, and 7
print(weekday(1))  # Monday
print(weekday(4))  # Thursday
print(weekday(7))  # Sunday

