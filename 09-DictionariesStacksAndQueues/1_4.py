#person = {
   #"name": "Szymon",
   #"surname": "Jasik",
   #"age": 18,
   #"hobby": ["music","football","fashion"],
  # "married": False,
 #  "phone":{"landline":"none","mobile":"573954391"}
#}

person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

# Display name
print("Name:", person["name"])

# Display hobby
print("Hobby:", person["hobby"])

# Display entire dictionary
print("\nOriginal dictionary:")
print(person)

# Change surname to 'Nowak'
person["surname"] = "Nowak"

# Change marriage status
person["married"] = False

# Add gender
person["gender"] = "male"

# Add new hobby
person["hobby"] = "bicycle"

# Add work phone
person["phone"]["work"] = "313131444"

# Display entire dictionary (iterate over items)
print("\nUpdated dictionary:")
for key, value in person.items():
    print(f"{key} : {value}")