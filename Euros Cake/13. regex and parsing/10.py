import re
import email.utils
for _ in range(int(input())):
    name, emails = email.utils.parseaddr(input())
    c = re.compile(r'^([a-zA-Z])([a-zA-Z0-9-._])*@([a-zA-Z]+\.[a-zA-Z]{1,3})$')
    if bool(c.match(emails)):
        print(name, f'<{emails}>')
