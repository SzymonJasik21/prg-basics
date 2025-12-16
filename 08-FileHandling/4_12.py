import csv

# Konfiguracja mapowania gatunków na pliki
GENRE_CONFIG = {
    'Fantasy': 'books_fantasy.txt',
    'Historical': 'books_historical.txt',
    'Romance': 'books_romance.txt',
    'Classic': 'books_classic.txt'
}

def read_books(file_path):
    """Odczytuje wszystkie książki z pliku CSV i zwraca listę słowników."""
    books = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                books.append(row)
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku {file_path}")
    return books

def filter_books_by_genre(books_list, genre):
    """Filtruje listę książek, zwracając tylko te z wybranego gatunku."""
    return [book for book in books_list if book['Genre'] == genre]

def save_to_file(books_list, output_file):
    """Zapisuje dane książek do pliku tekstowego."""
    if not books_list:
        return
        
    with open(output_file, mode='w', encoding='utf-8') as file:
        for book in books_list:
            # Tworzymy czytelną linię tekstu z danych książki
            line = f"{book['Title']} | {book['Author']} | {book['Year']}\n"
            file.write(line)

def process_books():
    """Główna funkcja koordynująca proces kopiowania."""
    input_file = 'books.csv'
    
    # 1. Odczytaj wszystkie dane raz
    all_books = read_books(input_file)
    
    if not all_books:
        return

    # 2. Przetwórz każdy gatunek zgodnie z konfiguracją
    for genre, filename in GENRE_CONFIG.items():
        filtered = filter_books_by_genre(all_books, genre)
        
        if filtered:
            save_to_file(filtered, filename)
            print(f"Zapisano {len(filtered)} pozycji do: {filename}")
        else:
            print(f"Brak książek z gatunku: {genre}")

# Uruchomienie programu
if __name__ == "__main__":
    process_books()