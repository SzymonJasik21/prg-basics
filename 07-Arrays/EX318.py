def get_second_largest(arr):
    if len(arr) < 2:
        return None
    
    largest = arr[0]
    second_largest = arr[0]
    
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
            
    return second_largest

def get_range_difference(arr):
    if not arr:
        return 0
    
    min_val = arr[0]
    max_val = arr[0]
    
    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
            
    return max_val - min_val

def get_median(arr):
    n = len(arr)
    if n == 0:
        return None
    
    # Kopiowanie i sortowanie bąbelkowe (bez funkcji wbudowanych)
    temp_arr = []
    for x in arr:
        temp_arr.append(x)
        
    for i in range(n):
        for j in range(0, n - i - 1):
            if temp_arr[j] > temp_arr[j + 1]:
                temp_arr[j], temp_arr[j + 1] = temp_arr[j + 1], temp_arr[j]
    
    if n % 2 != 0:
        return temp_arr[n // 2]
    else:
        mid1 = temp_arr[(n // 2) - 1]
        mid2 = temp_arr[n // 2]
        return (mid1 + mid2) / 2

def get_min_max(arr):
    if not arr:
        return []
    
    min_val = arr[0]
    max_val = arr[0]
    
    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
            
    return [min_val, max_val]

def to_string_with_minus(arr):
    result = ""
    for i in range(len(arr)):
        result += str(arr[i])
        if i < len(arr) - 1:
            result += "-"
    return result