'''
A bank manager has set up a safe code as H 4567. Your task is to write a program to read one letter and
one integer form a keyboard and verify the code. The program must show the output as follows.
- if the code is valid, it will display safe unlocked.
- if only the character h or H is valid, the program displays safe locked - change digit.
- if only the numeric value is valid, the program displays safe locked - change char.
- if the entered code is wrong (does not match both letters and numbers), the program displays
safe locked.
'''

char = input().lower()
num = input()

if char == 'h' and num == '4567':
    print('safe unlocked')
elif char == 'h':
    print('safe locked - change digit')
elif num == '4567':
    print('safe locked - change char')
else:
    print('safe locked')
