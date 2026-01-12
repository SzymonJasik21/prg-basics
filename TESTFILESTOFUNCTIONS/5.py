import json

konfiguracja = {
    "rozdzielczosc": "1920x1080",
    "glosnosc": 80,
    "skroty_klawiszowe": ["F1", "ESC","SPACE"]
}

with open("config.json", "w") as f:
    # indent=4 sprawia, ze plik bedzie czytelny dla czlowieka (ladne wciecia)
    json.dump(konfiguracja, f, indent=4)