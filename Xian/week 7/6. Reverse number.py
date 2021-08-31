'''
Write a program to receive a four-digit integer. Then reverse the number from back to front. The
range of input number is 1000 - 9999 only.
'''

num = input()
print(*(char for char in reversed(num)), sep='')
