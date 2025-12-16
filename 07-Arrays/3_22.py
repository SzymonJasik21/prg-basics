import random
def random_element(array):
    if not array:
        return None
    return random.choice(array)
data_array = ["banan","arbuz","cytryna","kiwi","malina","truskawka","jagoda"]
print(f"Tablica wejściowa: {data_array}")
print("\nLosowo wybrane elementy:")

for i in range(5):
    random_element_gen = random_element(data_array)
    print(f"Wybór {i+1}: {random_element_gen}")

    

