'''
Write a program to receive the student ID (guaranteed with eight characters long) and then check
the id code of Faculty of Information by looking at the 3rd and 4th digit codes that are ‘1’ and ‘6’ then
print out the result as an example.
'''

iden = input()
print('yes' if iden[2:4] == '16' else 'no') 
