'''
Write a program to get integers n and m, then displays the patterns as below.
- The output contains n lines, each line has m column.
- Each column displays m numbers which is a line number
'''

m, n = map(int, input().split())
for i in range(1, m+1):
    print(f'{str(i)*n} ' * n)
