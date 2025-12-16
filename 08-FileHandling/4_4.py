file_name = 'it_company.csv'

with open(file_name, 'r', encoding='utf-8') as file:
    lines_count = 0
    
    for line in file:
        print(line.strip())
        lines_count += 1
        
        # Co 5 linii zatrzymaj program
        if lines_count % 5 == 0:
            input('\nPress Enter key...\n')

print("End of file reached.")
