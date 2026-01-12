#with open("notatki.txt", "w") as f:
 #   f.write("Pierwsza linia\n")
  #  f.write("Druga linia\n")

uzytkownik = "Marek"
postep = 0.7452
sciezka = "C:/pliki/projekt"

with open("logi.txt", "w") as f:
    f.write("=== LOG SYSTEMOWY ===\n")
    f.write(f"Uzytkownik: {uzytkownik}\n")
    f.write(f"Postep: {postep:.2%}\n")  # Wyswietli 74.52%
    f.write(f"Lokalizacja: {sciezka}\n")