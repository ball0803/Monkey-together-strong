_ = int(input())
a = set(i for i in map(int, input().split()))
_ = int(input())
b = set(i for i in map(int, input().split()))

print(len(a.intersection(b)))
