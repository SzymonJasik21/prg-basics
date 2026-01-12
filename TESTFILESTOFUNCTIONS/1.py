pracownicy = [
    {"imie": "Jan", "wiek": 35},
    {"imie": "Anna", "wiek": 28},
    {"imie": "Marek", "wiek": 42}
]

# Sortujemy według wartości pod kluczem "wiek"
pracownicy.sort(key=lambda osoba: osoba["wiek"])

print(pracownicy)
# Wynik: Anna (28), Jan (35), Marek (42)