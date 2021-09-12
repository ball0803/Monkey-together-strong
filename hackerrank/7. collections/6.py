from collections import deque

t = int(input())
d = deque()
for _ in range(t):
    command, *arg = input().split()
    if command == 'pop' or  command == 'popleft':
        eval(f'd.{command}()')
    else:
        eval(f'd.{command}({arg[0]})')
print(*d)
