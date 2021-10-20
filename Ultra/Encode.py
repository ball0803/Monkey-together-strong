VOWELS = {char for char in 'aeiuo'}

string = input()

encode = ''
for char in string:
    if char.lower() in VOWELS:
        offset = 2
    else:
        offset = 1
    char = ord(char) + offset
    encode += chr(char)
print(encode)
