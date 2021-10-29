'''
Write a program to get a positive integer (n) and display the pattern as a following example.
'''
n = int(input())
for i in range(n-1, -1, -1):
    print('-'*i, '*'*((n*2)-1-(i*2)), '-'*i, sep='')
