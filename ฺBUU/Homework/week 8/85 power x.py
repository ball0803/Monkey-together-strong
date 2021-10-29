'''
Write a program to get one numeric value (N) to defined the number of iterations then calculate the
number (x) one by one to find the value of xx and display the result on the screen until there have N
numbers.
Input
The first line is a number that indicates the number of iterations for input N numbers.
The next N lines are numbers to find the power value.
Output
The exponent of the 1st to the nth number.
'''

n = int(input())
seq = (int(input()) for _ in range(n))
print(*(i**i for i in seq), sep='\n')
