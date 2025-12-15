def is_subset(array1,array2):
    for element in array1:
        if element not in array2:
            return False
    return True
A1=[1,5,3]
B1=[5,3,7,1,9]
print(f"Czy A1 jest podzbiorem B1? {is_subset(A1,B1)}")

