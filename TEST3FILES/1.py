class Ksiazka:
    def __init__(self, tytul, autor, strony):
        self.tytul = tytul
        self.autor = autor
        self.strony = strony

    def __str__(self):
        """Zwraca czytelny opis obiektu"""
        return f"'{self.tytul}' napisana przez {self.autor} ({self.strony} stron)"

moje_czytadło = Ksiazka("Wiedźmin", "Andrzej Sapkowski", 300)
print(moje_czytadło)