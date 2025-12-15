
#shopping_list = [
 #  "milk", "bread", "eggs", "butter", "cheese",
  # "tomatoes", "potatoes", "carrots", "onions", "garlic"
#]

#for item in shopping_list:
   # print(item)

shopping_list = [
   "milk", "bread", "eggs", "butter", "cheese",
   "tomatoes", "potatoes", "carrots", "onions", "garlic"
]
#for product in shopping_list:
 #  print(product)

separator = ', '

wszystkie_produkty = separator.join(map(str, shopping_list))

print(wszystkie_produkty)