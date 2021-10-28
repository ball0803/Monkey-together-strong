import re
for _ in range(int(input())):
    line = input()
    
    c = re.compile(r'(?<!^)(#(?:[0-9a-fA-F]{3}){1,2})')
    if bool(c.findall(line)):
        print(*c.findall(line), sep='\n')
