def process_lines(data):
    # Dzielimy tekst na listę linii
    lines = data.splitlines()
    
    # Filtrujemy tylko te linie, które nie są puste (po usunięciu spacji)
    clean_lines = []
    for line in lines:
        if line.strip():
            clean_lines.append(line)
            
    return clean_lines

if __name__ == "__main__":
    multiline_text = """Pierwsza linia
    Druga linia
    
    Czwarta linia po pustej"""
    
    result = process_lines(multiline_text)
    
    print("Liczba linii:", len(result))
    print("Linie:", result)