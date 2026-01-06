def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f"{hours:02}:{minutes:02}"
    
    elif time_format == '12':
        period = "am" if hours < 12 else "pm"
        h12 = hours % 12
        if h12 == 0:
            h12 = 12
        return f"{h12}:{minutes:02}{period}"

print(f"time_string(15, 38, '24') -> {time_string(15, 38, '24')}")
print(f"time_string(8, 3, '24') -> {time_string(8, 3, '24')}")
print(f"time_string(0, 5, '24') -> {time_string(0, 5, '24')}")
print(f"time_string(11, 15, '12') -> {time_string(11, 15, '12')}")
print(f"time_string(0, 7, '12') -> {time_string(0, 7, '12')}")
print(f"time_string(7, 30, '12') -> {time_string(7, 30, '12')}")
print(f"time_string(12, 46, '12') -> {time_string(12, 46, '12')}")
print(f"time_string(13, 10, '12') -> {time_string(13, 10, '12')}")
print(f"time_string(19, 2, '12') -> {time_string(19, 2, '12')}")