msg, shift = input().split()
shift = int(shift)
if shift < 1 or shift > 26:
    print("Error")
else:
    encode = ''
    for char in msg:
        x = ord(char.lower()) - shift
        if x < 97:
            x += 26
        encode += chr(x).upper()
    print(encode)
