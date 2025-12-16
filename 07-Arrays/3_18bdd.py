def find_second_largest(arr):
    if len(arr) < 2:
        return None 
    largest = arr[0]
    second_largest = arr[0]

    for x in arr:
        if x > largest:
            second_largest = largest
            largest = x
        elif x > second_largest and x < largest:
            second_largest = x
        elif largest == second_largest and x != largest:
            if x < largest:
                second_largest = x
    if largest == second_largest:
        largest = arr[0]
        second_largest = arr[0]
        
    for x in arr:
        if x> largest:
            largest = x 
        second_largest = largest
    for x in 
