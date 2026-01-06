class Car:
 def __init__(self, brand, model, year):
     self.brand = brand  # Object attribute
     self.model = model  # Object attribute
     self.year = year    # Object attribute
    
 def display_info(self):
     print(f"Car: {self.brand} {self.model}, Year: {self.year}")
     