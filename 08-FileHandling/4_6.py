file_name = input("File name: ")

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
        num_lines = len(lines)
        num_characters = 0
        num_words = 0
        
        for line in lines:
            num_characters += len(line)
            words = line.split()
            num_words += len(words)
            
    print(f"Number of lines: {num_lines}")
    print(f"Number of characters: {num_characters}")
    print(f"Number of words: {num_words}")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")