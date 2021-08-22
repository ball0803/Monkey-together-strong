'''
Write a code that receives a 6-digit integer from the keyboard, and outputs all the digits from the
back to the front. For example, if input is 123456, the output is 654321.
Input
A single line contains a positive 6-digit integer to be flipped.
Output
A single line contains the flipped input integer
'''

num = input()
print(*(char for char in reversed(num)), sep='')
