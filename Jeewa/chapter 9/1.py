colorList = ['red', 'yellow','black', 'brown', 'grey']
char = input()
found = None
for color in colorList:
    if color.startswith(char):
        found = color
        break
print(found if found else f'no color start with {char}')
