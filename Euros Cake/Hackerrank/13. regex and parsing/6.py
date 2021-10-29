s = input()
k = input()
g = 0
for i in range(len(s)-len(k)+1):
    if s[i:i+len(k)] == k:
        print((i, len(k)+i-1))
        g += 1

if g == 0:
    print((-1, -1))
