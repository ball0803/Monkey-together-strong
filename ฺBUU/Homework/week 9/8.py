'''
Write a program to get a positive integer (n) and display the number patterns as the examples
below.
'''
n = int(input())
print(' 1')
for i in range(2, n+1):
    print(f'{i} '*i)
