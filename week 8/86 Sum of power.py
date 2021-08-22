'''
Write a program to receive one integer number (N) and then print the sum of first N number that raised to
the square (12
+ 22 + 32 +… N2
) on the screen. For example, if you receive a value of 5, then the program
must display the result as 55 which is calculated from 12 +22 +32 +42 +52 etc.
Input:
A single line representing the first N order to find the sum of squares.
Output:
A single line showing the sum of squares of the first N number.
'''

n = int(input())
print((n*(n+1)*((2*n)+1))//6)
