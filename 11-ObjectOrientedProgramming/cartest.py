class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def _str_(self):
        return f"{self.year} {self.brand} {self.model}"
    
    #creating instance of the car
    my_car = Car("Toyota", "Corolla", 2021)


    print(my_car)