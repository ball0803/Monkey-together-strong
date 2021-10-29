'''
Write a program to get two numeric values from the keyboard where the result calculated by the
first number divide with the second number, then print out the result as the example.
'''

a = int(input())
b = int(input())
print(f'{a} is divisible by {b}' if a % b == 0 else f'{a} is indivisible by {b}')
