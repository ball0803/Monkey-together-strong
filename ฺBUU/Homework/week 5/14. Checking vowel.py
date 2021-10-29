'''
Write a program to receive one character, and check if the character received is a vowel (a, e, i, o,
u) then print out the result as an example.
Note that the input is guaranteed to contain only lowercase a-z letters
'''

vowels = {char for char in 'aeiou'}
char = input()
print('yes' if char in vowels else 'no')
