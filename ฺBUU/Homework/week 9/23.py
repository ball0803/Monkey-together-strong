m, n = map(int, input().split())

for i in range(m):
    val = [x for x in range((i*n)+1, ((i+1)*n)+1)]
    if i % 2 == 1:
        val = reversed(val)
    print(*val)
    
