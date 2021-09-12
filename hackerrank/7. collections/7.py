from collections import Counter

s = input()
c = Counter(sorted(s))
for a, b in c.most_common(3):
    print(a, b)
