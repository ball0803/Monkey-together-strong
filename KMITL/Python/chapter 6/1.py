arr = input().split()
print(arr)
print(*(x for x in map(int, arr) if x % 2 == 0))
