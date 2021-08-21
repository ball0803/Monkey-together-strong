'''
Write a program to receive the citizen ID (the user may enter any number of digits). For checking
citizen ID by the input-digits should equal to 13 digits.
'''

iden = input()
print('yes' if len(iden) == 13 else 'no')
