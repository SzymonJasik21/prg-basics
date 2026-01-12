def count_file_lines(filename):
    try:
        count = 0
        with open(filename, 'r') as fhand:
            for line in fhand:
                count += 1
        return count
    except FileNotFoundError:
        return -1

if __name__ == "__main__":
    file_name = 'mbox-short.txt'
    wynik = count_file_lines(file_name)
    
    if wynik == -1:
        print('Nie znaleziono pliku:', file_name)
    else:
        print('Liczba linii:', wynik)