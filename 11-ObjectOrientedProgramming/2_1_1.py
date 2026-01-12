class Student:
    def __init__(self, name, age, major):
        """Przyjmujemy dane od razu przy tworzeniu obiektu"""
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        """Klasa sama decyduje, jak ma wyglądać jej print"""
        return f"{self.name}, {self.age} years old, Major: {self.major}"

if __name__ == "__main__":
    student1 = Student("Dominic", 19, "Computer Science")
    student2 = Student("Olivia", 21, "Mathematics")
    student3 = Student("Marcus", 20, "Physics")

    print('LIST OF STUDENTS')
    print('================')
    print(student1)
    print(student2)
    print(student3)