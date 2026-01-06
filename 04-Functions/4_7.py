def icao_alphabet(letter):
    icao = {
        'a': 'Alpha', 'b': 'Bravo', 'c': 'Charlie', 'd': 'Delta', 'e': 'Echo',
        'f': 'Foxtrot', 'g': 'Golf', 'h': 'Hotel', 'i': 'India', 'j': 'Juliett',
        'k': 'Kilo', 'l': 'Lima', 'm': 'Mike', 'n': 'November', 'o': 'Oscar',
        'p': 'Papa', 'q': 'Quebec', 'r': 'Romeo', 's': 'Sierra', 't': 'Tango',
        'u': 'Uniform', 'v': 'Victor', 'w': 'Whiskey', 'x': 'X-ray', 'y': 'Yankee',
        'z': 'Zulu'
    }
    return icao.get(letter.lower(), "")

name = input("Enter a name: ")

print("ICAO phonetic alphabet spelling:")
for char in name:
    word = icao_alphabet(char)
    if word:
        print(word, end=" ")