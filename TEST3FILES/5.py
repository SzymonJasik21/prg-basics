class Student:
    def __init__(self, imie, nazwisko, punkty):
        self.imie = imie
        self.nazwisko = nazwisko
        self.punkty = punkty

    def __str__(self):
        inicjaly = self.imie[0] + self.nazwisko[0]
        if self.punkty >= 50:
            separator = "+"
        else:
            separator = "-"
        return inicjaly.upper() + separator + str(self.punkty)

if __name__ == "__main__":
    print(Student("Anna", "Nowak", 85))
    print(Student("Tomasz", "Kos", 40))