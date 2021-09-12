'''
Write a program to get a positive integer (n) and display the pattern as a following example.
'''
n = int(input())
for i in range(1, n+1):
    print('-'*(n-i), '*'*i, sep='')

for i in range(n-1, 0, -1):
    print('-'*(n-i), '*'*i, sep='')
