def read_from_file(name):
    with open(name) as file:
        content = file.read()
    return content

file_content = read_from_file('pets.txt')
file_lines = file_content.splitlines()

total = 0
