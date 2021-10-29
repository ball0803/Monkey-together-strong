'''
Write a program to get a positive integer (n) and display a rectangle of size n x n as in the following
example
'''

n = int(input())
print('1 '*n)
for i in range(2, n-1):
    print(f'{i} ', '- '*(n-2), f'{i}', sep='')
print(f'{n} '*n)
