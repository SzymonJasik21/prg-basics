###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
print('Last but one value', arr[-2])
#sum = arr[0]+arr[1]+arr[2]+arr[3]+arr[4]
sum = arr[0]+arr[-1]
print('Sum of first and last value', sum)
srodek_index = len(arr) // 2
print(arr[srodek_index])
#print(arr[2])
#for element in arr:
separator = ' '
#    print(element, end=' ')
print(separator.join(map(str, arr)))
