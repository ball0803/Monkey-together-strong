import itertools

k, m = map(int, input().rstrip().split())

k_list = list()
for _ in range(k):
    items = sorted(map(int, input().split()[1:]), reverse=True)
    k_list.append(items)

all_product = list(itertools.product(*k_list))
result = sum(x*x for x in all_product[0])
if result <= m - 1:
    print(result)
else:
    a = set()
    # I have sinned
    for prod in all_product:
        s = 0
        for item in prod:
            s += (item * item)
        a.add(s % m)
    print(max(a))

