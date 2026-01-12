class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

    def __str__(self):
        if self.cena > 50:
            wynik = self.nazwa.upper()
        else:
            wynik = self.nazwa.lower()
        return wynik + str(self.cena)

if __name__ == "__main__":
    print(Produkt("Klawiatura", 120))
    print(Produkt("Myszka", 30))