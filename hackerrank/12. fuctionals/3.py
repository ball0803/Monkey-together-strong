def fun(s):
    s = s.lower()
    sep_1 = s.find('@')
    sep_2 = s.find('.')

    if sep_1 == -1 or sep_2 == -1 or sep_2 < sep_1:
        return False

    username, domain, ext = s[:sep_1], s[sep_1+1:sep_2], s[sep_2+1:]
    if len(username) == 0 or len(domain) == 0 or len(ext) == 0 or len(ext) > 3:
        return False

    for character in username:
        if 97 <= ord(character) <= 122 or 48 <= ord(character) <= 57 or character == '-' or character == '_':
            pass
        else:
            return False

    for character in domain:
        if 97 <= ord(character) <= 122 or 48 <= ord(character) <= 57:
            pass
        else:
            return False

    for character in ext:
        if 97 <= ord(character) <= 122:
            pass
        else:
            return False

    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
