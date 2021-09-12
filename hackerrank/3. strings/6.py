import re
if __name__ == '__main__':
    s = input()
    print(True if len(re.findall('[a-zA-Z0-9]', s)) else False) 
    print(True if len(re.findall('[a-zA-Z]', s)) else False) 
    print(True if len(re.findall('[0-9]', s)) else False) 
    print(True if len(re.findall('[a-z]', s)) else False) 
    print(True if len(re.findall('[A-Z]', s)) else False) 
