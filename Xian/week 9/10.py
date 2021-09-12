'''
Write a program to get a positive integer (n) and display the number patterns as the examples
below.
'''
n = int(input())
for i in range(n, 0, -1):
    print(*(x for x in range(1, i+1)), sep=' ')
