
'''
Write a program to receive the first and last name of user then print out the message "Hello,
name and surname" and the alias name which derived from the first 2 characters of the first and last
name.
Input: receive first and last name of user.
Output: display 2 lines as follows
 The first line shows: "Hello", your first and last name.
 The second line shows: The alias name which derive from the first 2 characters of the first and
last name.
'''

f = input()
l = input()
print(f'Hello {f} {l}')
print(f'{f[:2]}{l[:2]}')