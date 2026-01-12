class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def podwyzka(self, procent):
        self.pensja += self.pensja * (procent / 100)

    def __str__(self):
        return f"Pracownik: {self.imie} {self.nazwisko}, Zarobki: {self.pensja:.2f} PLN"

if __name__ == "__main__":
    pracownik1 = Pracownik("Jan", "Kowalski", 5000)
    print(pracownik1)
    
    pracownik1.podwyzka(10)
    print("Po podwyżce:")
    print(pracownik1)

    pracownik2 = Pracownik("Maria", "Nowak", 7500)
    print(pracownik2)