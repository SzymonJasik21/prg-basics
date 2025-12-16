###
# Reads the entire contents of a file
#
def read_from_file(name):
   with open(name, 'r') as file:
      content = file.read()
   return content

# reads the entire file
file_content = read_from_file('countries.txt')

# splits the entire file contents into lines
# and stores them in an array
file_lines = file_content.splitlines()

sorted_lines = sorted(file_lines, key=lambda line: line.split('.')[1].strip())

# prints the array
#for line in file_lines:
 #  print(line)

for i, line in enumerate(sorted_lines, start=1):
    country_info = line.split('.', 1)[1].strip() 
    print(f"{i}. {country_info}")