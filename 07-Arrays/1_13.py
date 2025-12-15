def occurs(number, array):
    if number in array:
        return True
    else:
        return False
    
array_test = [2,4,6,8,10]
#correct = True

print("Wprowadź liczbę do sprawdzenia czy występuje ona w tablicy: ")
try:
    input_number = int(input())
except ValueError:
    print("Podana liczba nie spełnia warunków")
    #exit()
#correct = False
else:   
    if occurs(input_number, array_test):
        print(f"Liczba {input_number} występuje w danej tablicy")
    else:
        print(f"Liczba {input_number} nie występuje w danej tablicy")