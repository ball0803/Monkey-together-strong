_ = int(input())
s = set(i for i in map(int, input().split()))
n = int(input())
for _ in range(n):
    cmd, *arg = input().split()
    if not arg:
        arg = ''
    else:
        arg = arg[0]
    eval(f's.{cmd}({arg})')
print(sum(s))
