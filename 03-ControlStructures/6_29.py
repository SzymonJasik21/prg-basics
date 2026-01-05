n = int(input("Enter the number of prime numbers to find: "))

count = 0
number = 2

while count < n:
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(number, end=" ")
        count += 1
    
    number += 1