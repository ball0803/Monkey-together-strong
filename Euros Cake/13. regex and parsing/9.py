import re
for _ in range(int(input())):
    n = input()

    print('YES' if re.match(r'^(7|8|9)([0-9]{9})', n) and len(n) == 10 else 'NO')
