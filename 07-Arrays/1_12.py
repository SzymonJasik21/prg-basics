arr = [2, 3, 2, 5, 8, 1, 9, 8]
counts = {}
for element in arr:
    if element in counts:
        counts[element]+=1
    else:
        counts[element]=1

unique_elements = []
for element in counts:
    if counts[element] == 1:
        unique_elements.append(element)
print ("Array", arr)
print ("Unique elemts: ", unique_elements)
