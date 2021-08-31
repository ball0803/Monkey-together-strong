'''
Write a program to receive a message that is five characters long. The last letter will be the first
letter for shuffle characters, and the subsequent characters shuffle from the back to the front,
respectively. The print out of the result should convert to be the lowercase.
'''

name = input().lower()
print(*(char for char in reversed(name)), sep='')
