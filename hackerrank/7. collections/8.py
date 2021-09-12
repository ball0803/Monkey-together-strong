from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    deq = deque(map(int, input().split()))
    current = max(deq[-1], deq[0])
    while deq:
        l = deq[0]
        r = deq[-1]
        if l <= current and r <= current:
            if l > r:
                current = l
                deq.popleft()
            else:
                current = r
                deq.pop()
        else:
            print('No')
            break
    else:
        print('Yes')            
