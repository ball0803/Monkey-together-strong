'''
Write a program to receive one message with a length of 3 characters and then counting the vowel
characters (a, e, i, o, u).
Note that the input is guaranteed to contain only lowercase a-z letters
'''

s = input()
print(sum(s.count(char) for char in 'aeiou'))
