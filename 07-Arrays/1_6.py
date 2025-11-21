#Write a program that prints the name of the day of the week for a given 
# day number. Then, using the defined function, print the name of 
# the day of the week for the following day numbers: 1, 4, 7.

###
# Returns the name of the day of the week for a given day number (1-Monday ... 7-Sunday)
#
 
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    # subtract 1 because list indices start at 0
    return weekdays[n - 1]

# Test the function with day numbers 1, 4, and 7
print(weekday(1))  # Monday
print(weekday(4))  # Thursday
print(weekday(7))  # Sunday

