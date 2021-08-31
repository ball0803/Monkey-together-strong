'''
Write a program to receive the user's name, surname, and age. Then generate the user's password
according to the following conditions.
- if the user's first and last name are both longer than five characters, generate a password by
taking the first two characters of your first name followed by the last character of your last name
and the last digit of the age, respectively.
- In other cases, use the first name concrete's first character with the age and the last letter of the
last name, respectively.
'''

name = input()
fam = input()
age = input()

if len(name) > 5 and len(fam) > 5:
    print(f'{name[:2]}{fam[-1]}{age[-1]}')
else:
    print(f'{name[0]}{age}{fam[-1]}')
