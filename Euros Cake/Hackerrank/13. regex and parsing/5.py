import re
g = input()
c = r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})[qwrtypsdfghjklzxcvbnm]'
if [*re.finditer(c, g, flags=re.IGNORECASE)]:
    print(*re.findall(c, g, flags=re.IGNORECASE), sep='\n')
else:
    print(-1)
