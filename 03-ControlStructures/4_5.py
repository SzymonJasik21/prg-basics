plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    char_code = ord(char)
    new_char_code = char_code + 1
    encrypted_char = chr(new_char_code)
    encrypted_text = encrypted_text + encrypted_char

print(plain_text)
print(encrypted_text)