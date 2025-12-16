def compare(array1, array2):
    if len(array1) != len(array2):
        return False
    
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
            
    return True

list1_a = ["water", "book", "sky"]
list1_b = ["water", "book", "sky"]

list2_a = [True, False]
list2_b = [True, False, True]

list3_a = [5, 3, 1]
list3_b = [5, 3, 1]

list4_a = [3, 2, 1]
list4_b = [3, 2]

print("Comparison 1:", compare(list1_a, list1_b))
print("Comparison 2:", compare(list2_a, list2_b))
print("Comparison 3:", compare(list3_a, list3_b))
print("Comparison 4:", compare(list4_a, list4_b))