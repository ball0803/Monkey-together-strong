import re
for _ in range(int(input())):
    g = input()
    print(bool(re.match("^[\+-]?\d*\.\d+$", g)))
