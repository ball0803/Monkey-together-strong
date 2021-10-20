n = int(input())
arr = list(map(int, input().split()))
x = int(input())

if not arr.count(x):
    print(-1)
else:
    print(*(i for i in range(n-1) if arr[i] == x))
