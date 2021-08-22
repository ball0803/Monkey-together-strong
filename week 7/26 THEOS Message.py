from collections import Counter

'''
THEOS Message is the encoding of a message consisting of A-Z characters. It assembles adjacent characters
and form a code. For example, AAAAA can be made a THEOS message as 5A. The ABBCD can be made as
a THEOS message as 1A2B1C1D. Write a program to read and encode the text and output as the THEOS
message.
Input
The string is composed of A-Z that is 5 characters long.
Output
The THEOS message.
'''

s = Counter(input())
translate = ''
for char in s.keys():
    translate += f'{s[char]}{char}'
print(translate)
