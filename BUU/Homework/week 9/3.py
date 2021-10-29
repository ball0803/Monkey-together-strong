'''
Write a program to get the input numbers for m variable and n variable. The program will print out
n lines from 1 to n numbers. Each line will print the line number m times.
'''

m, n = map(int ,input().split())

for i in range(1, n+1):
    print(f'{i} '*m)
