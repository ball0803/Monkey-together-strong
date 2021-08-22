'''
Write a Python program that get an one integer (multiplication formula), and then use the for loop to
display the multiplication formula. As example in the table.
'''

n = int(input())
for i in range(1, 13):
    print(f'{n} * {i} = {n * i}')

