from collections import defaultdict

s_a, s_b = map(int, input().split())
d_a = defaultdict(list)
for i in range(1, s_a+1):
    w = input()
    d_a[w].append(i)

for _ in range(s_b):
    lookup = input()
    if d_a[lookup]:
        print(*d_a[lookup])
    else:
        print(-1)        
