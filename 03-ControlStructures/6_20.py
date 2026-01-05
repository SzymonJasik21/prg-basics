decimal_number = int(input("Enter decimal number: "))

if decimal_number == 0:
    binary_string = "0"
else:
    number = decimal_number
    remainders = []
    
    while number > 0:
        remainder = number % 2
        remainders.append(str(remainder))
        number = number // 2
    
    binary_string = "".join(remainders[::-1])

print(f"{decimal_number}(10) = {binary_string}(2)")