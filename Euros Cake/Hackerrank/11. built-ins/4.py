n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

k = int(input())

for athlete in sorted(arr, key=lambda athlete: athlete[k]):
    print(*athlete)
