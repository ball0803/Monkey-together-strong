t = int(input())
d = dict()
for _ in range(t):
    word = input()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
print(len(d))
print(*d.values())
