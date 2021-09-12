from itertools import combinations
o, n = input().split()
for i in range(int(n)):
    for g in combinations(sorted(o), i+1):
        print(*g, sep='')
