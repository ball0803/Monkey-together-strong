words = input().split()
words[0] = words[0].lower()
words[1:] = map(lambda x: x.title(), words[1:])
print(''.join(words))
