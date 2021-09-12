a = set(input().split())
n = int(input())
for _ in range(n):
    b = set(input().split())
    if not a.issuperset(b):
        print(False)
        break
else:
    print(True)
