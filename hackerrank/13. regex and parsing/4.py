import re
g = input()

k = r'([a-zA-Z0-9])\1+'
print(re.search(k, g).groups()[0] if re.search(k, g) else -1)
