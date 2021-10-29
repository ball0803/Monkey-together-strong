'''
Write a program to receive one letter (T represents the area of a triangle and R for the area of a
square), then get the base length and height of the triangle or the square's width and print out the result
as the example.
'''

shape = input()
a = int(input())
b = int(input())
print(f'Area of the triangle = {a * b * 0.5:2d}' if shape == 'T' else f'Area of the square = {a * b:2d}')
