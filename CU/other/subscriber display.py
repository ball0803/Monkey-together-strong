n = int(input())
suffix = ('B', 'M', 'K')
p = 0
x = 1_000_000_000
while x > 1:
    if n // x <= 0:
        x = x // 1000 
        p = p + 1
    else:
        k = round(n/x, 1) if n/x < 10 else round(n/x, 0)
        print(k, suffix[p], sep='')
        break
else:
    print(n)
