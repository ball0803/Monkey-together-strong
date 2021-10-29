n = int(input().rstrip())
s = set()
for _ in range(n):
    country = input().rstrip()
    s.add(country)

print(len(s))
