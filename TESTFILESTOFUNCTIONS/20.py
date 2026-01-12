line1 = "Oto niezależny zabójczy metal,\n"
line2 = 'wstyd dla naszego narodu.\n'

# Blok 'with' automatycznie wywoła .close() na końcu
with open('output.txt', 'w') as fout:
    fout.write(line1)
    fout.write(line2)

# Tutaj plik jest już bezpiecznie zamknięty