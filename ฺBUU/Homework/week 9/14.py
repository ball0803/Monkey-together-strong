'''
Write a program to get a positive integer (n) and display a rectangle of size n x n as in the following
example. (Each symbol separated by a space)
Note: the tick in the figure is a minus sign symbol.
'''

n = int(input())
print('* '*n)
for _ in range(n-2):
    print('* ', '- '*(n-2), '*', sep='')
print('* '*n)
