n = int(input())

for i in range(1, n+1):
    print('A'*i, '-'*((n-i)*2), 'A'*i, sep='')

for i in range(n-1, 0, -1):
    print('A'*i, '-'*((n-i)*2), 'A'*i, sep='')
