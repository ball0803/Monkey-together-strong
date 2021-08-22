import re

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

s = input() + '-'
translate = ''
count = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        translate += f'{count}{s[i]}'
        count = 1

print(translate)




# seq =  input()
# code = ''
# previous_char = seq[0]
# count = 1

# for char in seq[1:]:
#     if char == previous_char:
#         count += 1 
#     else:
#         code += f'{count}{previous_char}'
#         previous_char = char
#         count = 1
# print(code)

