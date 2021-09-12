'''
Write a program to get a positive integer (n) and display the number patterns as the examples
below.
'''
n = int(input())
for i in range(1, n+1):
    print(f'{i} '*n)
