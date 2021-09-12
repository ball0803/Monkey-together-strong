from itertools import permutations
o, n = input().split()
permu = permutations(o, int(n))
for g in sorted(permu):
    print(*g, sep='')
    
