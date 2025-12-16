file_name = "powers.txt"

with open(file_name, "w") as file:
    for i in range(1, 101):
        second_power = i ** 2
        third_power = i ** 3
        
        result_line = f"{i},{second_power},{third_power}"
        
        print(result_line)
        file.write(result_line + "\n")