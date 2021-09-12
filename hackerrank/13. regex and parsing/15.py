# Enter your code here. Read input from STDIN. Print output to STDOUTseen = ''
from string import ascii_uppercase, digits
import re
for _ in range(1, int(input())+1):
    uid = str(input())
    seen = ''
    valid = True
    
    if len(uid) == 10:
        for char in uid:
            if char not in seen and char.isalnum():
                seen = seen + char
            else:
                valid = False
                break
        if len(re.findall(r'[A-Z]', seen)) > 1 and len(re.findall(r'[0-9]', seen)) >2 :
            
            pass
        else:
            valid = False
    else:
        valid = False

    print('Valid' if valid else 'Invalid')
