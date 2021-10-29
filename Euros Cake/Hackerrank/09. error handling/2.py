import re

t = int(input())
for _ in range(t):
    t = input()
    try:
        k = re.search(t, '')
    except:
        print(False)
    else:
        print(True)
