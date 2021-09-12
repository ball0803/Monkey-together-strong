from itertools import combinations_with_replacement
o, n = input().split()
for g in combinations_with_replacement(sorted(o), int(n)):
    print(*g, sep='')
    