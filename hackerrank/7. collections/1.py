from collections import Counter


_ = input()
shoes = Counter(map(int, input().split()))
customers_list = []
n = int(input())
for _ in range(n):
    c = input().split()
    customers_list.append(c)

result = 0
for m in customers_list:
    size, pay = map(int, m)
    if shoes[size] > 0:
        result += pay
        shoes[size] -= 1
print(result)
        