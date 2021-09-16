n = 4
r = 10
space = 8
values = [1+(i/100) for i in range(1, r+1)]

print('Period'.ljust(space+2), end='')
for i in range(1, r+1):
    print(f'{i}%'.ljust(space), end='')
print()

for i in range(n):
    print(f'{i+1}'.ljust(space+2), end='')
    for value in values:
        print(f'{value*(value**i):.3f}'.ljust(space), end='')
    print()
