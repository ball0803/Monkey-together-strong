'''
Write a program to receive the age (int) and status (char) of a visitor to a particular zoo then print
out the entrance ticket price. If the visitor is under 18 or student status (s), the ticket price is 20 baht, but
50 baht for the entrance ticket in all other cases.
'''
age = int(input())
status = input()
print('20 B.' if age < 18 or status == 's' else '50 B.')

