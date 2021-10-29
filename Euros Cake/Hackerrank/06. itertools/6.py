from itertools import combinations

N = int(input())
K = (x for x in input().split())
i = int(input())

e = [x for x in combinations(K, i)]
n = [y for y in e if 'a' in y]
print(len(n)/len(e))
