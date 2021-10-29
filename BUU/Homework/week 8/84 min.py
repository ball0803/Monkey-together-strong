'''
Write a program to get one integer from the keyboard (N), then loops to get all n integers, and then find
out which number has the smallest value to display on the screen.
Input:
The first line is a number that indicates the number of iterations for N numbers.
The next N lines are the numbers to find the smallest value.
Output:
A single line shows the number with the smallest value.
'''

n = int(input())
seq = (int(input()) for _ in range(n))
print(min(seq))
