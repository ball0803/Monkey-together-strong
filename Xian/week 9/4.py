'''
Write a program to get integers m and n (n is an even number), then display m lines of the output.
Each line shows n symbols. The first half (1 to n / 2) of each line displays ‘>’ and the second half (n / 2 +
1 through n) display ‘<’.
'''

m, n = map(int, input().split())
for _ in range(m):
    print('>'*(n//2), '<'*(n//2), sep='')
