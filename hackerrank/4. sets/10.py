_ = int(input())
a = set(map(int, input().split()))
n = int(input())
for _ in range(n):
    cmd, _ = input().split()
    b = set(i for i in map(int, input().split()))
    eval(f'a.{cmd}(b)')

print(sum(a))
