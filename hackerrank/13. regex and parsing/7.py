import re
for _ in range(int(input())):
    line = input()
    
    print(re.sub(r'(?<= )(\|\||\&\&)(?= )', lambda x: 'and' if x.group(0) == '&&' else 'or', line))
