from itertools import groupby
s = input()
print(*((len(tuple(b)), int(a)) for a, b in groupby(s)))
