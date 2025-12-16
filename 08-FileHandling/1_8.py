def read_from_file(name):
    with open(name, 'r') as file:
        content = file.read()
    return content

file_content = read_from_file('pets.txt')
file_lines = file_content.splitlines()

total_words = 0

print("Text content:")
for line in file_lines:
    print(line)
    
    words_in_line = line.split()
    number_of_words = len(words_in_line)
    
    total_words += number_of_words

print("\nTotal number of words:", total_words)