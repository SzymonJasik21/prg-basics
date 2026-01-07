class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        initial = self.name[0]
        result = f"{self.surname}{initial}{self.seniority}"
        
        if self.age >= 18:
            return result.upper()
        else:
            return result.lower()

    def __repr__(self):
        return self.__str__()