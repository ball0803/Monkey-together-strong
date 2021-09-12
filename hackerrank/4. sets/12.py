n = int(input())

for i in range(n):
    a = input()
    set1 = set(input().split())
    b = input()
    set2 = set(input().split())
    print(set1.issubset(set2))
